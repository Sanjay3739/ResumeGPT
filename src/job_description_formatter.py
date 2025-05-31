from src.generative_model import generate_response

def format_job_description(job_description: str) -> str:
    """
    Formats a given job description into a structured format using the AI model.
    """

    # Construct the prompt to instruct the AI on how to structure the job description
    prompt = f"""
You are a formatting assistant. Given the following job description:
{job_description}

Format the above job description strictly in the following format:

Job Title:
- [Insert job title here]

Job Brief:
- [Provide a concise summary of the role]

Responsibilities:
- [List each responsibility]

Requirements and Skills:
- [List the technical requirements and skills needed]

Avoid adding too many extra details when formatting the job description.
Do not leave any section empty; ensure that each section is filled, but keep the details concise.
Only consider job descriptions related to the field of computer science or a relevant technical domain; otherwise, return the response: out of domain.
"""
    # Generate the formatted job description using the AI model
    return generate_response(prompt)
