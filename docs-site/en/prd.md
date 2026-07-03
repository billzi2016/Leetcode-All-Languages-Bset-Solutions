# Documentation Site PRD

## Objective

Build a bilingual documentation site for this repository using MkDocs and GitHub Actions.

The documentation site is not just a project landing page. It is an operating manual. It should explain why the dataset file is not committed, why prompts are split into three layers, why generation proceeds from Easy to Hard, why logs are separated, and why GitHub Pages only publishes documentation instead of running the model.

## Requirements

- Documentation source must be organized into English and Chinese sections.
- The site must explain LeetCode, supported languages, generation workflow, MkDocs, and GitHub Actions.
- Mermaid diagrams should describe the multi-file documentation structure and deployment flow.
- The documentation site should be deployable through GitHub Pages.
- The workflow should be simple, maintainable, and reusable.
- The docs must explain the full-generation entry point, tmux usage, dependency installation location, and cancellation commands.
- The docs must explain the split between stdout, stderr, and failures logs.
- The docs must explain the boundary between the generator and documentation site: generation depends on local Ollama, while GitHub Actions only deploys docs.

## Design Intent

- The bilingual source lives in `docs-site/cn/` and `docs-site/en/` so Chinese and English content remain easy to maintain independently.
- The root `docs-site/index.md` is only a language entry page, ensuring the GitHub Pages project root opens correctly.
- `workflow.md` ties together data, prompts, Ollama, output, logs, and deployment so the site does not explain only isolated pieces.
- `ollama.md` explains local inference and server source builds, making it clear that model serving is outside GitHub Actions.
- `languages.md` uses LeetCode 1 to show submission entry points, so readers understand that generated code must preserve starter-code shape.

## Deliverables

- English documentation under `docs-site/en/`.
- Chinese documentation under `docs-site/cn/`.
- MkDocs planning documentation.
- GitHub Actions planning documentation.
- Mermaid workflow diagrams.

## Acceptance Criteria

- English and Chinese folders exist.
- Each language has matching topic files.
- LeetCode, languages, Ollama workflow, MkDocs, GitHub Actions, and end-to-end workflow are documented.
- Mermaid diagrams render in Markdown-compatible viewers.
- The documentation can guide a later MkDocs + GitHub Actions implementation.
- The project root opens a documentation homepage with links to both Chinese and English sections.
- Readers can start full generation with tmux, inspect progress, cancel tasks, and locate failure logs from the docs.
