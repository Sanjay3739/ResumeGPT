import PyPDF2
import os
from utils.config import RESUMES_FOLDER


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Parameters:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text
        return extracted_text


def get_all_resumes_from_folder():
    """
    Extracts text from all PDF resumes in the specified resumes folder.

    Returns:
        list: A list of strings, each containing the filename and extracted text of a resume.
    """
    # Get all PDF files from the resumes folder
    resume_files = [f for f in os.listdir(RESUMES_FOLDER) if f.endswith(".pdf")]
    extracted_resumes = []
    for resume_file in resume_files:
        resume_path = os.path.join(RESUMES_FOLDER, resume_file)
        extracted_text = extract_text_from_pdf(resume_path)
        extracted_resumes.append(f"Resume: {resume_file}\n\n{extracted_text}\n")
    return extracted_resumes
