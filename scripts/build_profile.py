from __future__ import annotations

import json
from pathlib import Path


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_profile(stage_root: Path) -> str:
    llm = read_json(stage_root / "bilingual-llm-evaluation" / "data" / "metrics.json")
    coco = read_json(stage_root / "coco-annotation-quality-audit" / "data" / "metrics.json")
    regression = read_json(stage_root / "regression-model-benchmark" / "data" / "metrics.json")
    best_name = regression["best_model_by_test_mae"]
    best = regression["models"][best_name]
    best_display = best_name.replace("_", " ").title()

    return f"""# Hi, I'm Jinkun Huang

## AI Evaluation & Data Quality Specialist

### Multilingual LLM Evaluation · Human Feedback · Benchmarking · Python-Assisted QA

> **Publication context (August 2026):** This profile and its linked repositories were published together as a curated, privacy-safe portfolio release. Their GitHub creation dates record the public release, not when every underlying task was performed.

I turn ambiguous AI outputs and messy datasets into review decisions that another person can inspect, challenge, and reproduce. My work sits at the intersection of language judgment, annotation quality, model evaluation, and lightweight Python automation.

I am especially interested in the hard middle of AI training: defining what “good” means, applying it consistently, documenting edge cases, and converting reviewer feedback into a usable quality signal.

## Evidence projects

| Project | Verified evidence | What it shows |
|---|---|---|
| [Bilingual LLM Evaluation](https://github.com/mcgrannbiggieri-star/bilingual-llm-evaluation) | {llm['prompt_instances']} prompt instances, {llm['model_responses']} model responses, {llm['evaluation_records']} review records, {llm['dimension_scores']:,} dimension scores | Bilingual rubric design, blind review, pairwise preference, rationales, calibration, privacy-safe export |
| [COCO Annotation Quality Audit](https://github.com/mcgrannbiggieri-star/coco-annotation-quality-audit) | {coco['images_audited']} images, {coco['annotations_audited']:,} annotations, {coco['represented_categories']} represented categories | Deterministic structural QA, issue logging, source hashing, scope and limitation control |
| [Regression Model Benchmark](https://github.com/mcgrannbiggieri-star/regression-model-benchmark) | {regression['dataset']['rows']:,} records; best holdout MAE {best['test_mae']:.4f} with {best_display} | Leakage-aware comparison, train-only five-fold CV, holdout evaluation, reproducible metrics and diagnostics |

## Core capabilities

- Multilingual LLM response evaluation and pairwise preference ranking
- Rubric-based scoring, reviewer calibration, error taxonomy, and written rationales
- Factuality, instruction-following, relevance, safety, and language-quality review
- Multimodal annotation QA and Python-assisted CSV/JSON validation
- Dataset reconciliation, issue logs, audit trails, and benchmark documentation
- Clear asynchronous communication for distributed evaluation workflows

## Technical toolkit

`Python` · `pandas` · `NumPy` · `scikit-learn` · `JSON/CSV` · `Excel` · `Git`

## Working profile

- Bachelor's degree in Artificial Intelligence
- Independent AI evaluation practice since 2023, supported by published portfolio studies
- Native Mandarin Chinese · C1 English
- Available 30–40 hours per week for remote collaboration (UTC+8)

## Contact

- [AI Data Quality Portfolio](https://jinkun-huang-ai-data-quality.mcgrannbiggieri.chatgpt.site/)
- [LinkedIn](https://www.linkedin.com/in/hjk085386417)
- [Email](mailto:mcgrannbiggieri@gmail.com)

> All public metrics above are read from the linked repositories' generated `metrics.json` files. The projects are independent portfolio studies, not client or employer claims.
"""


def main() -> None:
    stage_root = Path(__file__).parents[2]
    output = Path(__file__).parents[1] / "README.md"
    output.write_text(build_profile(stage_root).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
