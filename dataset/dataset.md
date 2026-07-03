# LeetCode Problems Dataset

This directory documents how to obtain the merged LeetCode problem dataset. The data file `merged_problems.json` is not committed to this repository; download it into this directory when needed.

- Local data file: `merged_problems.json`
- Source repository: https://github.com/neenza/leetcode-problems/tree/master
- Original file: https://github.com/neenza/leetcode-problems/blob/master/merged_problems.json
- Direct download URL: https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json

## Where This JSON Comes From

`merged_problems.json` comes from the root directory of `neenza/leetcode-problems`. That upstream repository contains both a `problems/` directory and a pre-merged `merged_problems.json` file.

This project does not re-crawl or regenerate LeetCode data. When data is needed, download the already merged JSON file from the upstream repository for local reading, analysis, or conversion into solution artifacts.

## Data Structure

`merged_problems.json` contains a top-level `questions` field, which is an array of problem objects. Each problem object usually contains the following fields:

Some fields (like solutions, images, follow_ups) may be missing for certain problems.

- `title`: Problem title, for example `Container With Most Water`.
- `problem_id`: Internal LeetCode problem ID, stored as a string.
- `frontend_id`: LeetCode frontend display ID, stored as a string.
- `difficulty`: Difficulty level, usually `Easy`, `Medium`, or `Hard`.
- `problem_slug`: URL-friendly problem name, for example `container-with-most-water`.
- `topics`: Array of topic tags, such as `Array` and `Two Pointers`.
- `description`: Full problem statement, usually Markdown or text.
- `examples`: Array of examples. Each example object usually contains:
  - `example_num`: Example number.
  - `example_text`: Input, output, and explanation text.
  - `images`: Array of image URLs if the example contains images; this field is not used in model prompts.
- `constraints`: Array of problem constraints.
- `follow_ups`: Array of follow-up questions, usually empty when none exist.
- `hints`: Array of solving hints.
- `code_snippets`: Object containing starter code for multiple languages, such as `python`, `cpp`, and `java`.
- `solution` / `solutions`: Official solution or editorial content for some problems, usually as an HTML string.

## How to Download or Update

To use the dataset or sync the latest upstream version, run this command from the repository root:

```bash
curl -L -o dataset/merged_problems.json https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json
```

After updating, it is recommended to verify that the file is valid JSON and optionally record the upstream commit or download date.
