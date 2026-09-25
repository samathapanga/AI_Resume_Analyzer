

from langchain_core.prompts import PromptTemplate


resume_analysis_prompt = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template="""
You are an AI Resume Analyzer and Job Matching Assistant.

Analyze the candidate's resume against the given job description.

================ RESUME ================
{resume_text}

================ JOB DESCRIPTION ================
{job_description}

First, evaluate the resume against the job description using the following
five categories.

Give each category a score from 0 to 100.

1. Skills Match Score
Compare the technical and professional skills in the resume with the
skills required in the job description.

2. ATS Keyword Match Score
Compare important keywords and technologies in the job description with
the keywords and technologies present in the resume.

3. Experience Match Score
Compare the candidate's experience, responsibilities, and experience level
with the requirements in the job description.

4. Education and Certification Match Score
Compare the candidate's education, certifications, and relevant training
with the requirements in the job description.

5. Project/Domain Relevance Score
Compare the candidate's projects and domain knowledge with the work
described in the job description.

IMPORTANT:
- Give scores based only on the provided resume and job description.
- Do not invent skills, experience, projects, certifications, or education.
- If information is missing, reduce the relevant score.
- Return each score as a whole number from 0 to 100.
- Do not provide an overall score. The application will calculate it.

Provide the analysis in the following format:

================ MATCH SCORES ================

Skills Match Score: [0-100]
ATS Keyword Match Score: [0-100]
Experience Match Score: [0-100]
Education and Certification Match Score: [0-100]
Project/Domain Relevance Score: [0-100]

================ DETAILED ANALYSIS ================

1. Resume Summary
Give a short summary of the candidate's profile.

2. Matching Skills
List the skills from the resume that match the job description.

3. Missing Skills
List important skills from the job description that are missing or not
clearly demonstrated in the resume.

4. Experience Match
Explain how the candidate's experience and projects relate to the job
requirements.

5. Project Relevance
Identify which resume projects are relevant to this job.

6. Education and Certifications
Explain any relevant education, certifications, or training.

7. Strengths
Identify the strongest parts of the resume for this particular job.

8. Areas for Improvement
Suggest practical changes that could improve the resume for this job.

9. Suggested Skills
Suggest relevant skills the candidate could learn or strengthen based on
the job description.

10. ATS Keyword Suggestions
List important keywords from the job description that could naturally be
included in the resume, if they accurately reflect the candidate's skills
or experience.

Keep the analysis factual and specific to the provided resume and job description.
Do not invent experience, projects, certifications, or skills that are not present
in the resume.
"""
)
