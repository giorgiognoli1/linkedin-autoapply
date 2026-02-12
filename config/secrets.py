'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.3.10.30
'''


import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Login Credentials for LinkedIn (Optional)
username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")


## Artificial Intelligence (Beta Not-Recommended)
# Use AI
use_AI = True                          # True or False, Note: True or False are case-sensitive

# Select AI Provider
ai_provider = "gemini"               # "openai", "deepseek", "gemini"

# Your LLM url or other AI api url and port
llm_api_url = "https://api.openai.com/v1/"

# Your LLM API key or other AI API key 
llm_api_key = os.getenv("LLM_API_KEY")

# Your LLM model name or other AI model name
llm_model = os.getenv("LLM_MODEL", "gemini-2.0-flash")

llm_spec = "openai"
'''
Note: Currently "openai", "deepseek", "gemini" and "openai-like" api endpoints are supported.
Most LLMs are compatible with openai, so keeping it as "openai-like" will work.
'''

# # Yor local embedding model name or other AI Embedding model name
# llm_embedding_model = "nomic-embed-text-v1.5"

# Do you want to stream AI output?
stream_output = False                    # Examples: True or False. (False is recommended for performance, True is recommended for user experience!)
'''
Set `stream_output = True` if you want to stream AI output or `stream_output = False` if not.
'''
##




############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I por my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################
