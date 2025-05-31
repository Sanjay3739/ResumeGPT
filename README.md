# Job Matching Model with GEMINI

This project provides a job matching solution using the Google Gemini API. The application extracts text from PDF resumes, ranks them based on job descriptions, and displays the top candidates with similarity scores.

## Table of Contents

- Features
- Requirements
- Installation
- Configuration
- Running the Application
- Usage
- Project Structure
- Code Explanation
- Example Output

## Features

- **Resume Extraction**: Extract text from PDF resumes stored in a specified folder.
- **Job Description Input**: Provide job requirements.
- **Format Job Description**: Format or rewrite the provided job requirements using the Google Gemini API.
- **Resume Ranking**: Rank and filter resumes based on job requirements using the Google Gemini API.
- **Interactive Interface**: A Streamlit application for inputting job requirements and viewing ranked resumes.

## Requirements

1. **Python 3.9 or higher**
2. **PyPDF2** (for PDF text extraction)
3. **Google Generative AI Python Client Library** (for interacting with the Gemini API)
4. **Streamlit** (for the interactive web interface)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sanjay3739/ResumeGPT.git
   cd ResumeGPT
   ```

2. **Create a virtual environment and activate:**
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory of the project and add your Google Gemini credentials and other configuration details:
    ```dotenv
    # Google Gemini api credentials
    GEMINI_API_KEY = your-gemini-api-key

    # HTTP Proxy Settings
    http_proxy=http://172.20.0.251:8080
    https_proxy=http://172.20.0.251:8080
    ```

2. **Update Configuration File (`config.py`):**
   - The `config.py` file contains configuration details required for the project. Customize the following variables:
     - `RESUMES_FOLDER`: The directory where PDF resumes are stored.
     - `GEMINI_API_KEY`: Your API key for Google Gemini.
     - `MODEL_NAME`: The name of the generative AI model to be used.

## Running the Application

1. Run the application using the following command:

    ```bash
    streamlit run app.py --server.port 5022
    
    ```

2. ``` Note ``` : Ubuntu server to run streamlit in the Background then used below command

    ```bash
    nohup streamlit run app.py --server.fileWatcherType none --server.port 5022 > cv.log 2>&1 &
    ```
   This will launch the Streamlit app where you can input job requirements and view ranked resumes.

## Usage

- **Resume Extraction:** Extracts text from PDF resumes in the specified folder.
- **Job Description Input:** Enter short job discription based on your requirements.
- **Format Job Description:** Format or rewrite job discription properly.
- **Resume Ranking:** The `rank_resumes_based_on_jd` function ranks the resumes based on job requirements using the Google Gemini API and displays the top candidates.

## Project Structure

- `app.py`: Entry point for the Streamlit application.
- `src/`: Contains the core logic for resume extraction and ranking.
  - `job_application.py`: Main script to execute the job application functionality.
  - `resume_extraction.py`: Functions to extract text from PDF resumes.
  - `resume_ranker.py`: Functions to rank resumes based on job description.
  - `generative_model.py`: Functions to generate response using the Google Gemini API.
  - `job_description_formatter.py`: Functions to format provided job description.
- `utils/`: Contains configuration files.
  - `config.py`: Configuration file for API keys and folder paths.

## Code Explanation

- **Libraries:** The project uses `PyPDF2` for extracting text from PDFs, `google.generativeai` for interacting with the Gemini API, and `streamlit` for the web interface.
- **Resume Extraction:** The `resume_extraction.py` script extracts text from PDF resumes located in the `RESUMES_FOLDER`.
- **Generative Model Interaction:** The `generative_model.py` file contains functions to interact with the Google Gemini API, generating content based on job descriptions and ranking resumes by relevance. It manages API calls and processes responses to identify the best candidates.
- **Job Description Formatting:** The `job_description_formatter.py` file provides functions to format job descriptions into a structured format, clearly presenting requirements, responsibilities, and skills. It utilizes prompts to ensure consistency and clarity in job descriptions.
- **Resume Ranking:** The `resume_ranker.py` script constructs a prompt for the Gemini API to rank resumes based on job requirements and returns the top candidates.
- **Streamlit Interface:** The `app.py` script creates an interactive interface where users can input job requirements and view ranked resumes.

## Example Output

During interaction with the Streamlit application, you might see outputs like:
