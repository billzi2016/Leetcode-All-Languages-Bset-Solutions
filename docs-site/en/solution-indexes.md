# Solution Indexes

The generated problem indexes live in the repository difficulty directories. The documentation site exposes them as MkDocs pages through symlinks, so the long tables are not copied into `docs-site/`.

| Difficulty | English index | Chinese index |
| --- | --- | --- |
| Easy | [Easy index](solution-indexes/Leetcode-Easy/index.md) | [Easy 中文清单](../cn/solution-indexes/Leetcode-Easy/index.md) |
| Medium | [Medium index](solution-indexes/Leetcode-Medium/index.md) | [Medium 中文清单](../cn/solution-indexes/Leetcode-Medium/index.md) |
| Hard | [Hard index](solution-indexes/Leetcode-Hard/index.md) | [Hard 中文清单](../cn/solution-indexes/Leetcode-Hard/index.md) |

Regenerate these files with:

```bash
PYTHONPATH=src python scripts/generate_difficulty_readmes.py
```

The generated rows use the same output path rules as the solution generator, including fixed-width bucket directories such as `0001-0100`.
