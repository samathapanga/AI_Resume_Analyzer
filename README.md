# 📄 AI Resume Analyzer & Job Matcher

An AI-powered resume analysis application that compares a candidate's resume with a Job Description (JD) and provides a Resume–JD Match Score, matching skills, skill gaps, project relevance, and ATS keyword suggestions.

## 🚀 Project Overview

The AI Resume Analyzer & Job Matcher uses Generative AI to analyze how well a resume aligns with a specific Job Description.

Users can upload their resume as a PDF and paste a Job Description. The application extracts the resume text and sends it along with the Job Description to Gemini 3.6 Flash through LangChain.

The application then generates a detailed analysis and calculates an overall Resume–JD Match Score.

## ✨ Features

- 📄 Upload resume in PDF format
- 📋 Paste Job Description
- 🤖 AI-powered resume analysis
- 📊 Resume–JD Match Score
- 📈 Score breakdown
- ✅ Matching skills identification
- ❌ Missing skills identification
- 💼 Experience matching
- 📁 Project relevance analysis
- 🎓 Education and certification analysis
- 🔑 ATS keyword suggestions
- 💡 Areas for improvement
- 📥 Downloadable analysis report

## 🧮 Match Score

The application evaluates the resume across five categories:

| Category | Weight |
|---|---:|
| Skills Match | 40% |
| ATS Keyword Match | 25% |
| Experience Match | 15% |
| Education & Certification | 10% |
| Project/Domain Relevance | 10% |

The final Resume–JD Match Score is calculated using a weighted formula in Python.

```text
Overall Score =
(Skills × 40%)
+ (ATS Keywords × 25%)
+ (Experience × 15%)
+ (Education × 10%)
+ (Projects × 10%)