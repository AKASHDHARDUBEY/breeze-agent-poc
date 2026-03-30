# Breeze-Aware Agent Skills PoC

This project is a Proof of Concept for GSoC 2026 (Apache Airflow).

## Basic PoC
- Detects environment (host vs Breeze)
- Executes correct command
- Supports fallback logic

Run:
```
cd basic
python agent.py run_tests
```

---

## Advanced PoC
- Skills defined in documentation
- Extractor converts docs → skills.json
- Drift detection ensures consistency

Run:
```
cd advanced
python extractor.py
python extractor.py --check
```

---

## Key Idea
This project demonstrates how AI agents can:
- Understand execution environment
- Follow correct Airflow workflows
- Use documentation as source of truth