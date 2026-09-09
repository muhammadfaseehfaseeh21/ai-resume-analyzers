# AI Resume Analyzer

A beginner-friendly Streamlit application that analyzes PDF/DOCX resumes using Groq's `openai/gpt-oss-120b` model.

## Features

- Upload PDF or DOCX resumes
- Extract resume text
- Optional Job Description comparison
- ATS-style estimated score
- Keyword/skill matching
- Missing keywords
- Strengths and weaknesses
- Improvement suggestions
- Separate Python files for easier learning and maintenance

## Project Structure

```text
ai_resume_analyzer/
├── app.py
├── analyzer.py
├── resume_parser.py
├── prompts.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## API Key

This project uses Groq's API with:

```text
openai/gpt-oss-120b
```

Create a Groq API key and store it as `GROQ_API_KEY`.

Never put your real API key directly inside `app.py` or upload it to GitHub.

## Run Locally

Install the packages from `requirements.txt`, set `GROQ_API_KEY`, and start Streamlit:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud

1. Create a GitHub repository.
2. Upload all project files.
3. Open Streamlit Community Cloud.
4. Select your GitHub repository.
5. Set the main file to:

```text
app.py
```

6. Open the app's Secrets settings.
7. Add:

```toml
GROQ_API_KEY = "your_real_groq_api_key"
```

8. Deploy the app.

## Important

The ATS score produced by this application is an AI-generated estimate. It is not an official score from a specific company's ATS.

For best results, provide a complete Job Description along with the resume.
