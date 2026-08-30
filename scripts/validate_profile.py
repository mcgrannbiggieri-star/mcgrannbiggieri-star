from __future__ import annotations

import re


REQUIRED = {
    "missing title": "AI Evaluation & Data Quality Specialist",
    "missing subtitle": "Multilingual LLM Evaluation",
    "missing bilingual repository": "bilingual-llm-evaluation",
    "missing annotation repository": "coco-annotation-quality-audit",
    "missing benchmark repository": "regression-model-benchmark",
    "missing portfolio": "jinkun-huang-ai-data-quality.mcgrannbiggieri.chatgpt.site",
    "missing linkedin": "linkedin.com/in/hjk085386417",
    "missing bachelor's degree": "Bachelor's degree in Artificial Intelligence",
    "missing c1 english": "C1 English",
    "missing availability": "30–40 hours per week",
    "missing independent-practice framing": "Independent AI evaluation practice since 2023",
}


def validate(text: str) -> list[str]:
    errors = [label for label, value in REQUIRED.items() if value not in text]
    lowered = text.lower()
    if "software engineer" in lowered:
        errors.append("unsupported software-engineer positioning")
    if "top 1%" in lowered or "world-class" in lowered:
        errors.append("inflated ranking language")
    if re.search(r"(?:\+?86[\s-]*)?1[3-9](?:[\s-]*\d){9}", text):
        errors.append("phone number present")
    if "120 prompt pairs" in lowered or "240 ai responses" in lowered:
        errors.append("superseded llm metric wording")
    if "1,150 annotations" in lowered or "1150 annotations" in lowered:
        errors.append("superseded coco metric wording")
    return errors
