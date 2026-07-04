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

## `audit_suspicious_solutions.py`

Audits generated Markdown files for suspicious code blocks, such as unusually long outputs, natural-language explanations inside code fences, Markdown leftovers, or repeated lines.

The length check is dynamic. Each run builds baselines from the currently generated solutions, preferring `difficulty + language`, then `language`, then global statistics when samples are limited.

```bash
PYTHONPATH=src python migrate/audit_suspicious_solutions.py
```

The script is read-only for solution files. It writes a local Markdown report to:

```text
migrate/suspicious_solutions_report.md
```

The report is ignored by Git.

## `rename_bucket_dirs.py`

Renames old bucket directories to fixed-width ranges:

```text
1-100 -> 0001-0100
101-200 -> 0101-0200
```

Dry run:

```bash
python migrate/rename_bucket_dirs.py
```

Apply the rename:

```bash
python migrate/rename_bucket_dirs.py --apply
```

This migration is intentionally separate from the generator. The generator only writes new paths; this script handles historical directory names when needed.
