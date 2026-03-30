# Breeze Agent PoC

## Basic PoC
- Detect environment
- Run correct command
- Fallback logic

Run:
```
cd basic
python agent.py run_tests
```

---

## Advanced PoC
- Skills defined in docs
- Extractor generates skills.json
- Drift detection

Run:
```
cd advanced
python extractor.py
python extractor.py --check
```