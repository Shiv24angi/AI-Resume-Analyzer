import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber

# Set API Key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyDjiPC3D0H__KHXxuHiPJ1RbOJPGj3plhE'
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        if text.strip():
            return text.strip()
    except Exception as e:
        print(f"Direct extraction failed: {e}")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            text += pytesseract.image_to_string(image) + "\n"
    except Exception as e:
        print(f"OCR failed: {e}")
    return text.strip()

# Resume analysis with Gemini
def analyze_resume(resume_text, job_description=None):
    if not resume_text:
        return {"error": "Resume text is required."}
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    You are an experienced HR with Technical Experience in the field of any one job role from Data Science, Data Analyst, DevOPS, Machine Learning Engineer, Prompt Engineer, AI Engineer, Full Stack Web Development, Big Data Engineering, Marketing Analyst, Human Resource Manager, Software Developer your task is to review the provided resume.
    Please share your professional evaluation on whether the candidate's profile aligns with the role.ALso mention Skills he already have and siggest some skills to imorve his resume , alos suggest some course he might take to improve the skills.Highlight the strengths and weaknesses.
    Resume:
    {resume_text}
    """
    if job_description:
        prompt += f"\nCompare with this job description:\n{job_description}"
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit app UI
def main():
    st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

    st.markdown("""
<style>
/* === GLOBAL STYLES === */
html, body, .stApp {
    background-color: #fef4e9 !important;
    color: #3d2e26 !important;
    font-family: 'Georgia', serif;
}

/* === TITLES === */
.title, h1, h2, h3 {
    color: #a05e2c !important;
    background-color: #fff8f3;
    padding: 16px;
    border-radius: 10px;
    text-align: center;
}

/* === INPUT FIELDS === */
input[type="text"],
textarea,
.stTextInput > div > div > input,
.stTextArea > div > textarea {
    background-color: #fff8f3 !important;
    color: #3d2e26 !important;
    border: 1px solid #dcb7a0 !important;
    border-radius: 8px;
    padding: 10px;
}

/* === LABELS === */
label,
.stTextInput label,
.stTextArea label {
    color: #3d2e26 !important;
    font-weight: bold;
}

/* === FILE UPLOADER === */
div[data-testid="stFileDropzone"] {
    background-color: #fff8f3 !important;
    border: 2px dashed #dcb7a0 !important;
    border-radius: 10px;
    color: #3d2e26 !important;
}
div[data-testid="stFileDropzone"] > div {
    color: #3d2e26 !important;
}
.stFileUploader button {
    background-color: #b86e47 !important;
    color: #fff8f3 !important;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    padding: 6px 16px;
}
.stFileUploader button:hover {
    background-color: #a05e2c !important;
    color: #ffffff !important;
}

/* === BUTTONS === */
.stButton > button {
    background-color: #b86e47 !important;
    color: #ffffff !important; /* ✅ White text */
    font-weight: bold !important;
    padding: 0.6em 2em !important;
    border-radius: 8px !important;
    border: none !important;
    transition: 0.3s ease-in-out;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    opacity: 1 !important;
    font-family: 'Georgia', serif !important;
}
.stButton > button:hover {
    background-color: #a05e2c !important;
    color: #ffffff !important; /* White on hover too */
}
.stButton > button:disabled {
    background-color: #b86e47 !important;
    color: #ffffff !important;
    cursor: not-allowed;
    opacity: 1 !important;
}

/* === BOX STYLING === */
.box, .stContainer {
    background-color: #fff8f3;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
    color: #3d2e26;
}

/* === FOOTER === */
.footer {
    text-align: center;
    padding: 20px 0;
    color: #a05e2c;
    font-size: 14px;
}
.footer a {
    color: #b86e47;
    font-weight: bold;
    text-decoration: none;
}

/* === SCROLLBAR === */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: #fff8f3;
}
::-webkit-scrollbar-thumb {
    background: #b86e47;
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: #a05e2c;
}

/* === DISABLE STREAMLIT MENU/FOOTER === */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

    # Title Block
    st.markdown('<div class="title"><h1>AI Resume Analyzer</h1><p>Smart insights on your resume with AI</p></div>', unsafe_allow_html=True)
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("📄**Upload your resume (PDF only)**", type=["pdf"])
    with col2:
        job_description = st.text_area("🧾**Optional: Job Description**", placeholder="Paste the job description here...", height=200)

    if uploaded_file:
        st.markdown('<p style="color: #a05e2c; font-weight: bold;">✔ Resume uploaded successfully.</p>', unsafe_allow_html=True)

        with open("uploaded_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        resume_text = extract_text_from_pdf("uploaded_resume.pdf")

        if st.button("Analyze Resume"):
            with st.spinner("Analyzing resume..."):
                try:
                    analysis = analyze_resume(resume_text, job_description)
                    st.markdown('<div class="box">', unsafe_allow_html=True)
                    st.subheader("Resume Analysis:")
                    st.write(analysis)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Analysis failed: {e}")
    else:
        st.markdown('<p style="color:#a05e2c; font-weight: bold;">Please upload a resume in PDF format to proceed.</p>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()