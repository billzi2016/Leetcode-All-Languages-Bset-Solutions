# MkDocs Site Plan

The documentation site should be implemented as an independent MkDocs project under `docs-site/`.

## Goals

- Keep documentation site files separate from generator source code.
- Provide English and Chinese content in parallel structures.
- Make navigation predictable.
- Keep the structure simple enough to maintain manually.

## Planned MkDocs Structure

```text
docs-site/
  mkdocs.yml
  docs/
    en/
    cn/
```

The current planning documents live directly under `docs-site/en/` and `docs-site/cn/`. A later implementation can move or copy them into `docs-site/docs/` if a full MkDocs project is created.

## Navigation

The English and Chinese navigation should mirror each other:

- Overview
- LeetCode
- Languages
- Ollama Workflow
- MkDocs
- GitHub Actions
- End-to-End Workflow
- PRD

