# Migration and Maintenance Scripts

This directory contains one-off or maintenance-oriented scripts. These scripts are not part of the normal generation entry points under `scripts/`.

## `audit_missing_solutions.py`

Audits generated Markdown files and reports:

- missing language sections
- complete files whose language section order can be repaired

Examples:

```bash
PYTHONPATH=src python migrate/audit_missing_solutions.py
PYTHONPATH=src python migrate/audit_missing_solutions.py --difficulty Hard
PYTHONPATH=src python migrate/audit_missing_solutions.py --frontend-ids 4 10
```

This script is read-only. It does not call Ollama, does not regenerate code, and does not modify Markdown files. If it reports issues, run `scripts/generate_solutions.py` for the selected problems to repair or fill them.

