# AI-Powered Resume Analyzer (Next-Gen ATS)

An intelligent Applicant Tracking System designed to streamline the recruitment process by using AI to analyze resumes, match candidates to job descriptions, identify skill gaps, and recommend career improvement resources.

## 🚀 Features

- 🧾 Resume Upload & Parsing (PDF, OCR fallback)
- 📊 Resume Analysis (skills, gaps, strengths)
- 📌 Job Description Matching with Compatibility Score
- 🎯 AI-Based Career Suggestions
- 📚 Course Recommendations for Upskilling
- 🧠 Powered by Google Generative AI (Gemini)

## 🧩 Tech Stack

| Layer         | Technology             |
|--------------|------------------------|
| Frontend     | [Streamlit](https://streamlit.io) |
| Backend      | Python 3.10+           |
| AI Engine    | Google Generative AI (Gemini) |
| PDF Parsing  | pdfplumber             |
| OCR Fallback | pytesseract            |
| Config Mgmt  | dotenv (.env)          |

## 🖥️ System Workflow

1. User uploads a resume PDF.
2. Text is extracted via `pdfplumber` (fallback: `pytesseract`).
3. Resume is analyzed using Google Gemini AI:
    - Summarization
    - Skill extraction
    - Compatibility check
4. Output is displayed in an interactive Streamlit UI.

## 🧑‍💼 Target Users

- 🎓 Job Seekers looking to improve their resumes
- 🧑‍💼 Recruiters seeking faster candidate evaluation
- 🧑‍🏫 Career counselors and job platforms

## 📋 Functional Modules

### ✅ Resume Upload & Parsing
- Upload PDFs via Streamlit
- Extract text using `pdfplumber` or OCR fallback

### ✅ Resume Analysis
- AI-generated summary of resume content
- Skill extraction and gap analysis
- Personalized suggestions and strengths overview

### ✅ Job Description Matching
- Upload or input job description
- AI evaluates compatibility and calculates a match score

### ✅ Course Recommendations
- Identifies missing skills
- Recommends top-rated online courses

## 🔒 Non-Functional Requirements

- ⚡ **Performance**: Analysis within 10 seconds
- 👨‍💻 **Usability**: No technical skill needed
- 📈 **Scalability**: Supports concurrent requests
- 🔁 **Reliability**: Automatic OCR fallback
- 🔐 **Security**: API keys stored securely using `.env`
- 🧰 **Maintainability**: Modular and extensible code
- 💼 **Portability**: Runs on any Python-compatible environment

## 🔮 Future Enhancements

- 🌐 Multi-language support
- 🤝 Integration with LinkedIn / Indeed APIs
- 📝 Exportable analysis reports
- 👤 User authentication and dashboards

## 📦 Installation

```bash
git clone https://github.com/your-username/next-gen-ats.git
cd next-gen-ats
pip install -r requirements.txt
