
import os
import re
import streamlit as st

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from resume_parser import extract_resume_text
from prompt import resume_analysis_prompt


load_dotenv()


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)


st.title("📄 AI Resume Analyzer & Job Matcher")

st.write(
    "Upload your resume and paste a job description to identify "
    "matching skills, skill gaps, relevant projects, ATS keywords, "
    "and resume-JD match score."
)

st.divider()


uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "📋 Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


if uploaded_file is not None:

    if not job_description.strip():
        st.warning("Please paste a Job Description before analyzing.")
        st.stop()

    st.success("Resume uploaded successfully! ✅")

    if st.button("Analyze Resume"):

        resume_text = extract_resume_text(uploaded_file)

        if not resume_text.strip():

            st.error("Could not extract text from this PDF.")

        else:

            try:

                llm = ChatGoogleGenerativeAI(
                    model="gemini-3.6-flash",
                    temperature=0.3,
                    google_api_key=os.getenv("GEMINI_API_KEY")
                )

                final_prompt = resume_analysis_prompt.format(
                    resume_text=resume_text,
                    job_description=job_description
                )

                with st.spinner("🤖 Analyzing your resume..."):

                    response = llm.invoke(final_prompt)

                if isinstance(response.content, str):

                    analysis = response.content

                else:

                    analysis = "".join(
                        item["text"]
                        for item in response.content
                        if isinstance(item, dict)
                        and item.get("type") == "text"
                    )

                # -----------------------------------------
                # Extract Match Scores from Gemini Response
                # -----------------------------------------

                skills_match = re.search(
                    r"Skills Match Score:\s*(\d+)",
                    analysis,
                    re.IGNORECASE
                )

                ats_match = re.search(
                    r"ATS Keyword Match Score:\s*(\d+)",
                    analysis,
                    re.IGNORECASE
                )

                experience_match = re.search(
                    r"Experience Match Score:\s*(\d+)",
                    analysis,
                    re.IGNORECASE
                )

                education_match = re.search(
                    r"Education and Certification Match Score:\s*(\d+)",
                    analysis,
                    re.IGNORECASE
                )

                project_match = re.search(
                    r"Project/Domain Relevance Score:\s*(\d+)",
                    analysis,
                    re.IGNORECASE
                )


                # -----------------------------------------
                # Calculate Weighted Match Score
                # -----------------------------------------

                if all([
                    skills_match,
                    ats_match,
                    experience_match,
                    education_match,
                    project_match
                ]):

                    skills_score = int(skills_match.group(1))
                    ats_score = int(ats_match.group(1))
                    experience_score = int(experience_match.group(1))
                    education_score = int(education_match.group(1))
                    project_score = int(project_match.group(1))

                    overall_score = round(
                        (skills_score * 0.40)
                        + (ats_score * 0.25)
                        + (experience_score * 0.15)
                        + (education_score * 0.10)
                        + (project_score * 0.10)
                    )

                    # Keep scores within 0-100
                    overall_score = max(
                        0,
                        min(100, overall_score)
                    )

                    # -----------------------------------------
                    # Display Overall Match Score
                    # -----------------------------------------

                    st.subheader("📊 Resume–JD Match Score")

                    st.metric(
                        label="Overall Match Score",
                        value=f"{overall_score}%"
                    )

                    if overall_score >= 80:
                        st.success("🟢 Strong Match")

                    elif overall_score >= 60:
                        st.warning("🟡 Moderate Match")

                    else:
                        st.error("🔴 Low Match")


                    # -----------------------------------------
                    # Display Score Breakdown
                    # -----------------------------------------

                    st.subheader("📈 Score Breakdown")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.write(
                            f"**Skills Match:** {skills_score}%"
                        )

                        st.write(
                            f"**ATS Keyword Match:** {ats_score}%"
                        )

                        st.write(
                            f"**Experience Match:** {experience_score}%"
                        )

                    with col2:

                        st.write(
                            f"**Education & Certification:** "
                            f"{education_score}%"
                        )

                        st.write(
                            f"**Project/Domain Relevance:** "
                            f"{project_score}%"
                        )


                    st.divider()


                # -----------------------------------------
                # Display Detailed AI Analysis
                # -----------------------------------------

                st.subheader("📊 Detailed Resume Analysis")

                st.markdown(analysis)


                # -----------------------------------------
                # Download Analysis
                # -----------------------------------------

                st.download_button(
                    label="📥 Download Analysis",
                    data=analysis,
                    file_name="resume_analysis.txt",
                    mime="text/plain"
                )

                st.divider()

                st.success(
                    "✅ Analysis completed successfully!"
                )


            except Exception as e:

                st.error(
                    "⚠️ Unable to analyze the resume."
                )

                st.info(
                    "Please check your Gemini API key or API quota."
                )

