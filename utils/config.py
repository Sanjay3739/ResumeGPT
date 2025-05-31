import os
from dotenv import load_dotenv

load_dotenv()

# Google Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Name of the generative AI model
MODEL_NAME = "gemini-1.5-flash"

# Configuration for text generation
GENERATION_CONFIG = {"temperature": 0.3}

# Folder where PDF resumes are stored
RESUMES_FOLDER = "resumes"

# HEADER_URL
HEADER_URL = os.getenv("HEADER_URL")