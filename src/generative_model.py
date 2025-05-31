import google.generativeai as genai
from utils.config import GEMINI_API_KEY, MODEL_NAME, GENERATION_CONFIG

# Configure the Google Generative AI model with the API key
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the AI model with the provided model name and generation configuration
model = genai.GenerativeModel(
    model_name=MODEL_NAME, generation_config=GENERATION_CONFIG
)

def generate_response(prompt: str, extracted_resumes: list = None):
    """
    Generate content from the AI model using the provided prompt.
    """
    try:
        # Use the AI model to generate content based on the prompt
        if extracted_resumes:
            response = model.generate_content([prompt] + extracted_resumes)
        else:
            response = model.generate_content([prompt])

        return response.text

    except Exception as e:
        # Catch any other errors and return a descriptive error message
        return {"error": f"An error occurred: {str(e)}"}
