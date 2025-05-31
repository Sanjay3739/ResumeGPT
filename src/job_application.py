import streamlit as st
import base64
from src.resume_extraction import get_all_resumes_from_folder
from src.resume_ranker import rank_resumes_based_on_jd
from src.job_description_formatter import format_job_description

# Set page layout to wide
st.set_page_config(
    page_title="GenAi Lab",
    page_icon="assets/favicon.svg",
    layout="wide",
)

def job_application_main():
    """
    Main function for the job application Streamlit app.
    Provides a form for users to input job requirements and ranks resumes based on the input.
    """
    # Constants
    STYLE_PATH = "src/style/style.css"

    # Inject CSS
    with open(STYLE_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    st.title("Job Application Form")
    # Extract all resumes from the specified folder
    extracted_resumes = get_all_resumes_from_folder()

    with st.form(key="job_application_form"):
        # Input fields for job requirements
        job_description = st.text_area("Job Description")
        # Submit button for the form
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if job_description:
                # Formats a given job description into a structured format
                formatted_jd = format_job_description(job_description)

                # Handle the case where the formatted job description is incomplete or missing sections
                if any(
                    keyword not in formatted_jd
                    for keyword in [
                        "Job Title",
                        "Job Brief",
                        "Responsibilities",
                        "Requirements and Skills",
                    ]
                ):
                    st.markdown("---")
                    st.write("**There may not be enough information in the job description, or no relevant record was found.**")
                else:
                    with st.expander("**Formatted Job Description**", expanded=False):
                        st.markdown("---")
                        st.write(formatted_jd)
                    # Rank resumes based on the formatted job description
                    candidates = rank_resumes_based_on_jd(
                        formatted_jd,
                        extracted_resumes,
                    )

                    if "error" in candidates:
                        st.error(candidates["error"])
                    else:
                        if len(candidates) > 0:
                            # Filter candidates with a similarity score greater than 50%
                            top_candidates = [candidate for candidate in candidates if candidate['similarity_score'] > 50]

                            if len(top_candidates) > 0:
                                # Display the top candidates with similarity scores
                                st.write(f"## Top {len(top_candidates)} Candidates:")
                                for idx, candidate in enumerate(top_candidates[:3], start=1):  # Limit to top 3 candidates
                                    st.markdown("---")
                                    # Create a Base64 link for the PDF file
                                    pdf_file_path = f"resumes/{candidate['file_name']}"
                                    try:
                                        with open(pdf_file_path, "rb") as pdf_file:
                                            pdf_data = pdf_file.read()
                                            pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")
                                            pdf_link = f'<a href="data:application/pdf;base64,{pdf_base64}" target="_blank">{candidate["candidate_name"]}</a>'
                                    except FileNotFoundError:
                                        pdf_link = f'{candidate["candidate_name"]} (File not found)'

                                    st.write(f"**Candidate {idx}:**")
                                    st.markdown(f"**Candidate Name:** {pdf_link}", unsafe_allow_html=True)
                                    st.write(f"**Similarity Score:** {candidate['similarity_score']}%")

                                    # Print top keywords as a comma-separated string
                                    top_keywords = ", ".join(candidate["top_keywords"])
                                    st.write(f"**Top Keywords:** {top_keywords}")
                            else:
                                st.write("No relevant record was found")
                        else:
                            st.write("No relevant record was found.")
            else:
                st.error("Please fill out job description.")
