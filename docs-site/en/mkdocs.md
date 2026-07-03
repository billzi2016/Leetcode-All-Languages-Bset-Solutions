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
  index.md
  en/
  cn/
```

The current site uses `docs-site/` directly as `docs_dir`. The root `index.md` is the language entry page, while `en/` and `cn/` hold the bilingual content. This keeps the structure flat and ensures the GitHub Pages project root gets a real homepage.

`site_dir` points to `../docs-site-build`, so generated output stays outside the source tree and is ignored by Git.

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

## Design Intent

MkDocs only publishes Markdown as a static site. It does not participate in solution generation. This lets GitHub Actions build documentation with a lightweight Python environment, without installing Ollama, downloading models, or reading the local dataset.

English and Chinese pages keep parallel names so every content change has an obvious translation target. The root homepage is only an entry point, preventing mixed-language content from accumulating at the project root.
