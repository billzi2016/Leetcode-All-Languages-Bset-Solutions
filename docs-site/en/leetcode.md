# What LeetCode Is

LeetCode is an online programming practice platform centered on algorithm and data-structure problems. Each problem usually includes a title, difficulty, topic tags, a statement, examples, constraints, hints, starter code, and sometimes editorial content.

This project uses a local merged JSON dataset to generate solution files. The dataset is not committed to the repository; users download it locally when they want to run generation.

## Problem Metadata

Typical problem fields include:

- `title`: human-readable problem name.
- `frontend_id`: the public LeetCode problem number.
- `difficulty`: `Easy`, `Medium`, or `Hard`.
- `problem_slug`: URL-friendly problem slug.
- `topics`: tags such as Array, Hash Table, Dynamic Programming, or Two Pointers.
- `description`: problem statement.
- `examples`: input/output examples.
- `constraints`: input size and value limits.
- `hints`: optional hints.
- `solution` or `solutions`: optional editorial reference.
- `code_snippets`: starter code for each supported language.

The generator sends useful text fields into the problem prompt. Image URLs are excluded because the generation model is text-only.

## Output Goal

The output is not a copy of the problem statement. Each generated Markdown file is a solution file containing language sections and code blocks only.

