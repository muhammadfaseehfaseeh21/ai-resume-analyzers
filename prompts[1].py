def build_analysis_prompt(resume_text: str, job_description: str = "") -> str:
    jd_section = job_description.strip() if job_description.strip() else (
        "No Job Description was provided. Analyze the resume using general ATS-friendly "
        "resume standards and do not invent a target job."
    )

    return f"""
Analyze the following resume for an ATS-style resume review.

IMPORTANT:
- Do not invent facts about the candidate.
- Do not judge protected personal characteristics.
- If a Job Description is provided, compare the resume against it.
- If no Job Description is provided, give a general resume analysis.
- The ATS score is an estimated compatibility score, not a real ATS score.
- Use only information present in the resume and job description.
- Return ONLY a valid JSON object.

JOB DESCRIPTION:
{jd_section}

RESUME:
{resume_text}

Return JSON with exactly these fields:
{{
  "ats_score": 0,
  "keyword_match": 0,
  "experience_match": 0,
  "summary": "Short professional summary of the analysis",
  "strengths": ["strength 1", "strength 2", "strength 3"],
  "weaknesses": ["weakness 1", "weakness 2", "weakness 3"],
  "matching_keywords": ["keyword 1", "keyword 2"],
  "missing_keywords": ["keyword 1", "keyword 2"],
  "suggestions": ["suggestion 1", "suggestion 2", "suggestion 3"],
  "resume_improvements": "A concise paragraph explaining the most useful changes."
}}

Scoring guidance:
- ats_score: 0-100 estimated overall compatibility.
- keyword_match: 0-100 based on relevant keywords/skills found in the resume.
- experience_match: 0-100 based on how well the demonstrated experience matches the target role.
"""
