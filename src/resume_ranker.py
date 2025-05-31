import json
from src.generative_model import generate_response


def rank_resumes_based_on_jd(
    job_description: str,
    extracted_resumes: list,
):
    """
    Ranks and filters resumes based on job requirements using a generative AI model.
    """

    # Construct the prompt for the AI model
    prompt = f"""
Given the following job requirements:
{job_description}

Analyze the provided job description and compare it to the following resumes, prioritizing matching technical skills and programming languages. 
Only consider resumes related to the field of computer science or a relevant technical domain.

Return the top candidates in JSON format, with each candidate represented as an object containing the following information: 
"file_name": The filename of the resume.
"candidate_name": The name of the candidate.
"similarity_score": The similarity score between the job description and the resume, expressed as a number between 1-100 with up to two decimal places.
"top_keywords": A list of **no more than 15** of the most important keywords that match closely between the job description and the candidate resumes and contributed to the high similarity score. Ensure that the list **does not exceed 15 keywords** under any circumstances.

The similarity scores should primarily focus on technical skills and programming languages, followed by years of experience, education, and then other factors.
Ensure the candidates are ranked based on their similarity scores. 
If no matching resumes are found, return an empty JSON array. 
If one or more matching resumes are found, return the top 1-3 candidates, depending on the number of matches.

Ensure that all candidates have the required technical skill or technology in their resumes otherwise don't add that candidate resume in response.
"""

    # Generate the ranked resumes using the AI model
    response = generate_response(prompt, extracted_resumes)
    response_text = response.replace("`", "").replace("json", "").strip()

    response_json = json.loads(response_text)
    return response_json
