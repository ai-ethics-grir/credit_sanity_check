
⚠️ **Disclaimer**  
This repository contains demonstration code and synthetic data for AI Ethics PoCs.
It is not production-ready. Unauthorized commercial use is prohibited.

# Credit Scoring Sanity Check

**Author:** Grimaldi Roberto | AI Ethics  
**Goal:** Detect unstable AI-driven credit decisions via controlled feature perturbations and route high-risk flips to human review.  
**Context:** Swiss banking compliance (FINMA) and LPD/GDPR.

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Logical Steps
1. Scope & risk definition (decision scope, impact, escalation).
2. Data audit (schema, leakage, drift baseline, minimization).
3. Baseline model (logistic/GBM with nested CV).
4. Perturbation tests (±5–10% on key features) → record flips.
5. Explainability (SHAP) for flipped cases; extract unstable features.
6. Human-in-the-loop routing for flip-risk above threshold.
7. Stability score + release gate; block auto-approval below threshold.
8. Documentation (model card, data lineage, decision policy).

## KPIs
- Business: ≥18% fewer false approvals.
- Ethics: Explainability score ≥0.90; stability index ↑.
- Compliance: Human oversight for all flagged cases (FINMA).

## Files
- `app.py` — Streamlit demo app.
- `reports/model_card.md`, `reports/ethics_note.md`, `reports/compliance_checklist.md`
- `assets/cover.png` — cover image placeholder.
