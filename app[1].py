import streamlit as st
from resume_parser import extract_text_from_file
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload a resume, optionally paste a Job Description, and get an AI-powered ATS-style analysis.")

with st.sidebar:
    st.header("Settings")
    st.info("Model: openai/gpt-oss-120b via Groq")
    st.caption("The ATS score is an estimate, not a guarantee of how a real ATS will score a resume.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"],
    help="Supported formats: PDF and DOCX"
)

job_description = st.text_area(
    "Job Description (optional)",
    height=220,
    placeholder="Paste the job description here to compare the resume against the role."
)

analyze_button = st.button("🔍 Analyze Resume", type="primary", use_container_width=True)

if analyze_button:
    if uploaded_file is None:
        st.error("Please upload a PDF or DOCX resume first.")
        st.stop()

    with st.spinner("Reading and analyzing your resume..."):
        try:
            resume_text = extract_text_from_file(uploaded_file)

            if not resume_text.strip():
                st.error("No readable text was found in the uploaded file.")
                st.stop()

            result = analyze_resume(resume_text, job_description)

            st.success("Analysis completed!")

            col1, col2, col3 = st.columns(3)
            col1.metric("ATS Score", f"{result['ats_score']}/100")
            col2.metric("Keyword Match", f"{result['keyword_match']}%")
            col3.metric("Experience Match", f"{result['experience_match']}%")

            st.subheader("📌 Summary")
            st.write(result["summary"])

            st.subheader("💪 Strengths")
            for item in result["strengths"]:
                st.write(f"• {item}")

            st.subheader("⚠️ Weaknesses")
            for item in result["weaknesses"]:
                st.write(f"• {item}")

            st.subheader("🔑 Matching Keywords / Skills")
            if result["matching_keywords"]:
                st.write(", ".join(result["matching_keywords"]))
            else:
                st.write("No strong matching keywords identified.")

            st.subheader("❌ Missing Keywords / Skills")
            if result["missing_keywords"]:
                st.write(", ".join(result["missing_keywords"]))
            else:
                st.write("No major missing keywords identified.")

            st.subheader("🛠️ Improvement Suggestions")
            for item in result["suggestions"]:
                st.write(f"• {item}")

            st.subheader("📝 Suggested Resume Improvements")
            st.write(result["resume_improvements"])

        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.info("Check that your GROQ_API_KEY is configured correctly.")
