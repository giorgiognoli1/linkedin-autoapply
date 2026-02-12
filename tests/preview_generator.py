import os
import jinja2

# Paths
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "all resumes", "default")
TEMPLATE_FILE = "resume_template.html"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

def render_preview():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_FILE)
    
    # Pass empty variables to use the template's realistic default content
    context = {
        "salesforce_experience_custom": None,
        "top_skills_custom": None
    }
    
    return template.render(context)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    html_content = render_preview()
    
    output_path = os.path.join(OUTPUT_DIR, "preview.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Preview generated at: {output_path}")
