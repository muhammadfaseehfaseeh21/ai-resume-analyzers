import json
import os
from groq import Groq
from prompts import build_analysis_prompt

MODEL_NAME = "openai/gpt-oss-120b"


def _clean_json(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def analyze_resume(resume_text: str, job_description: str = "") -> dict:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Add it to your environment or Streamlit Secrets.")

    client = Groq(api_key=api_key)
    prompt = build_analysis_prompt(resume_text, job_description)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional resume and ATS analysis assistant. "
                    "Return only valid JSON matching the requested structure."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_completion_tokens=3000,
        response_format={"type": "json_object"},
    )

    content = response.choices[0].message.content
    data = json.loads(_clean_json(content))

    defaults = {
        "ats_score": 0,
        "keyword_match": 0,
        "experience_match": 0,
        "summary": "",
        "strengths": [],
        "weaknesses": [],
        "matching_keywords": [],
        "missing_keywords": [],
        "suggestions": [],
        "resume_improvements": "",
    }
    defaults.update(data)
    return defaults
