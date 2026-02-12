#!/usr/bin/env python3
"""
Resume Generator Module
Generates AI-customized resumes for each job application.
"""

import os
import re
import subprocess
from datetime import datetime
import jinja2
import google.generativeai as genai

from config.secrets import llm_api_key, llm_model
from config.settings import generated_resume_path
from modules.helpers import print_lg

# Paths
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "all resumes", "default")
TEMPLATE_FILE = "resume_template.html"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "all resumes", "generated")

# User information for AI context
USER_INFO = """
Giorgio Gnoli - CRM & CX Leader with 15+ years experience.
Expert in: Salesforce Marketing Cloud, HubSpot, CDP, Loyalty Management.
Key achievements: Managed CRM across 14 countries, Led global teams of 46+ professionals.
Industries: Automotive (Mercedes-Benz), Consumer Goods (Fater/Pampers), Retail.
Certifications: Salesforce Admin, Marketing Cloud Consultant, Email Specialist.
"""


def _sanitize_filename(name: str) -> str:
    """Sanitize a string to be safe for filenames."""
    # Remove or replace special characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name)
    return name[:50]  # Limit length


def _simplify_job_title(title: str) -> str:
    """
    Simplify job title for filename.
    Removes: parenthetical content, pipe separators, company names after |
    Example: 'Senior Salesforce Consultant (Non Profit Partner) | Mason Frank' -> 'Senior_Salesforce_Consultant'
    """
    # Remove everything after | (usually company name)
    title = title.split('|')[0].strip()
    # Remove parenthetical content
    title = re.sub(r'\([^)]*\)', '', title)
    # Clean up extra spaces
    title = re.sub(r'\s+', ' ', title).strip()
    # Sanitize for filename
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title[:40]  # Limit length


def _generate_ai_content(job_title: str, job_description: str, company_name: str) -> str:
    """Generate customized Salesforce experience bullets using Gemini AI."""
    print_lg(f"🤖 Generating AI content for: {job_title} at {company_name}")
    
    try:
        genai.configure(api_key=llm_api_key)
        model = genai.GenerativeModel(llm_model)
        
        prompt = f"""
You are an expert resume writer. Your task is to rewrite the "Salesforce Experience" section of the user's resume to be EXTREMELY tailored to the specific job description below.

**GOAL:** The recruiter must see this candidate as the perfect fit for THEIR specific Salesforce needs.

**ORIGINAL EXPERIENCE (Salesforce - Marketing Cloud Solution Engineer, 2021-2024):**
- Subject Matter Expert in Loyalty Management, CDP, and Marketing Cloud Personalization.
- Supported major accounts in Automotive and Luxury sectors in digital strategy.
- Key speaker at Salesforce World Tour and international events.

**USER BACKGROUND:**
{USER_INFO}

**TARGET JOB TITLE:** {job_title}

**COMPANY:** {company_name}

**JOB DESCRIPTION:**
{job_description[:2000]}  

**INSTRUCTIONS:**
1.  **ANALYZE** the Job Description: Identify the specific Salesforce clouds, tools, or methodologies they are asking for (e.g., is it more Admin-focused? Strategy-focused? Marketing Cloud? CDP?).
2.  **REWRITE** the bullet points to directly address these specific requirements using the User's background. 
    - If they want **Strategy/CX**, highlight the "Digital Strategy" and "Loyalty" aspects.
    - If they want **Technical/Implementation**, highlight "Subject Matter Expert", "CDP", "Personalization".
    - If they want **Leadership**, highlight "Supported major accounts" and "Speaker" roles.
3.  **KEYWORDS:** Use the exact terminology found in the Job Description where possible.
4.  **FORMAT:** Return ONLY HTML bullet points in this format: <ul><li>Point 1</li><li>Point 2</li></ul>
5.  **LENGTH:** Use 3-4 powerful, result-oriented bullet points.
"""
        
        response = model.generate_content(prompt)
        result = response.text
        
        # Clean markdown if present
        if "```html" in result:
            result = result.split("```html")[1].split("```")[0].strip()
        elif "```" in result:
            result = result.replace("```", "").strip()
        
        print_lg("   ✅ AI content generated successfully")
        return result
        
    except Exception as e:
        print_lg(f"   ❌ AI generation failed: {e}")
        # Return default content if AI fails
        return """<ul>
            <li>Subject Matter Expert in Loyalty Management, CDP, and Marketing Cloud Personalization.</li>
            <li>Supported major accounts in Automotive and Luxury sectors in digital strategy.</li>
            <li>Key speaker at Salesforce World Tour and international events.</li>
        </ul>"""


def _generate_ai_top_skills(job_title: str, job_description: str) -> list:
    """Generate top skills list based on job requirements using Gemini AI."""
    print_lg(f"🎯 Generating AI Top Skills for: {job_title}")
    
    try:
        genai.configure(api_key=llm_api_key)
        model = genai.GenerativeModel(llm_model)
        
        prompt = f"""
You are an expert resume consultant. Based on the job description below, select the 6 most relevant skills for this resume from the user's skill set.

**USER'S FULL SKILL SET:**
Salesforce Marketing Cloud, Salesforce Admin, CRM Strategy, HubSpot, CDP (Customer Data Platform), 
Loyalty Management, Digital Transformation, Marketing Automation, Email Marketing, Journey Builder,
AMPscript, SQL, Data Cloud, Personalization, Customer Experience (CX), Team Leadership,
Project Management, Stakeholder Management, Analytics, AI/ML Applications, Apex (basic),
Lightning Web Components (LWC), Integration, API Management

**TARGET JOB TITLE:** {job_title}

**JOB DESCRIPTION:**
{job_description[:1500]}

**INSTRUCTIONS:**
1. Select exactly 6 skills from the user's skill set that best match the job requirements.
2. Prioritize skills explicitly mentioned in the job description.
3. Keep skill names concise (max 2-3 words each).
4. Return ONLY a comma-separated list of skills, nothing else.
5. Example output: Salesforce MC, CRM Strategy, HubSpot, Loyalty Mgmt, CDP, Digital Transformation
"""
        
        response = model.generate_content(prompt)
        result = response.text.strip()
        
        # Clean and parse the skills
        skills = [skill.strip() for skill in result.split(',')]
        # Limit to 6 skills max
        skills = skills[:6]
        
        print_lg(f"   ✅ AI Top Skills generated: {skills}")
        return skills
        
    except Exception as e:
        print_lg(f"   ❌ AI top skills generation failed: {e}")
        # Return default skills if AI fails
        return ["Salesforce MC", "CRM Strategy", "HubSpot", "Loyalty Mgmt", "CDP", "Digital Transformation"]


def _render_html(custom_content: str, top_skills: list = None) -> str:
    """Render the HTML template with custom content and skills."""
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_FILE)
    
    context = {
        "salesforce_experience_custom": custom_content,
        "top_skills_custom": top_skills
    }
    
    return template.render(context)


def _html_to_pdf(html_content: str, output_pdf_path: str, html_save_path: str) -> bool:
    """Convert HTML to PDF using Chrome headless."""
    # Save HTML first
    with open(html_save_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Find Chrome
    chrome_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium"
    ]
    
    chrome_exe = None
    for path in chrome_paths:
        if os.path.exists(path):
            chrome_exe = path
            break
    
    if not chrome_exe:
        print_lg("❌ Chrome not found for PDF generation!")
        return False
    
    # Generate PDF
    abs_html_path = os.path.abspath(html_save_path)
    cmd = [
        chrome_exe,
        "--headless=new",
        f"--print-to-pdf={output_pdf_path}",
        "--no-pdf-header-footer",
        "--disable-gpu",
        f"file://{abs_html_path}"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and os.path.exists(output_pdf_path):
            return True
        else:
            print_lg(f"❌ Chrome PDF error: {result.stderr}")
            return False
    except Exception as e:
        print_lg(f"❌ PDF generation exception: {e}")
        return False


def generate_custom_resume(job_title: str, job_description: str, company_name: str) -> str:
    """
    Generate a custom resume tailored to the job.
    
    Args:
        job_title: Title of the job
        job_description: Full job description text
        company_name: Name of the company
        
    Returns:
        Absolute path to the generated PDF, or empty string if failed
    """
    print_lg(f"📄 Generating custom resume for: {job_title} | {company_name}")
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Create filename with simplified format: Giorgio Gnoli {JobTitle} {YYYYMMDD}.pdf
    simple_title = _simplify_job_title(job_title)
    date_stamp = datetime.now().strftime("%Y%m%d")
    base_name = f"Giorgio Gnoli {simple_title} {date_stamp}"
    
    pdf_path = os.path.join(OUTPUT_DIR, f"{base_name}.pdf")
    html_path = os.path.join(OUTPUT_DIR, f"{base_name}.html")
    
    try:
        # 1. Generate AI content for experience
        custom_content = _generate_ai_content(job_title, job_description, company_name)
        
        # 2. Generate AI-powered top skills
        top_skills = _generate_ai_top_skills(job_title, job_description)
        
        # 3. Render HTML with both custom content and skills
        html_output = _render_html(custom_content, top_skills)
        
        # 4. Convert to PDF
        success = _html_to_pdf(html_output, pdf_path, html_path)
        
        if success:
            print_lg(f"   ✅ Custom resume generated: {pdf_path}")
            return pdf_path
        else:
            print_lg("   ❌ Failed to generate PDF")
            return ""
            
    except Exception as e:
        print_lg(f"   ❌ Resume generation error: {e}")
        return ""


# For standalone testing
if __name__ == "__main__":
    test_pdf = generate_custom_resume(
        "CX Director",
        "We are looking for a CX Director to lead our customer experience strategy. The ideal candidate will have extensive experience with Salesforce Marketing Cloud and handling Customer Data Platforms (CDP) to drive loyalty and engagement.",
        "Test Company UK"
    )
    print(f"Generated: {test_pdf}")
