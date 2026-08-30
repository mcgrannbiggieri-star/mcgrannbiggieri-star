import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from validate_profile import validate
from build_profile import build_profile


ROOT = Path(__file__).parents[1]
STAGE_ROOT = ROOT.parent


def test_profile_requires_positioning_evidence_and_working_profile():
    errors = validate("AI Evaluation & Data Quality Specialist")
    assert "missing subtitle" in errors
    assert "missing bilingual repository" in errors
    assert "missing bachelor's degree" in errors
    assert "missing c1 english" in errors


def test_profile_rejects_unsupported_or_private_language():
    errors = validate("Software Engineer\nTop 1%\n+86 178 3374 7417")
    assert "unsupported software-engineer positioning" in errors
    assert "inflated ranking language" in errors
    assert "phone number present" in errors


def test_profile_rejects_superseded_metrics():
    errors = validate("120 prompt pairs and 240 AI responses; 1,150 annotations")
    assert "superseded llm metric wording" in errors
    assert "superseded coco metric wording" in errors


def test_actual_readme_is_publication_safe():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert validate(readme) == []
    assert "60 prompt instances" in readme
    assert "2,168 annotations" in readme
    assert "0.3111" in readme


def test_builder_reads_verified_sibling_metrics():
    text = build_profile(STAGE_ROOT)
    assert "60 prompt instances" in text
    assert "2,168 annotations" in text
    assert "77 represented categories" in text
    assert "0.3111" in text
    assert validate(text) == []
