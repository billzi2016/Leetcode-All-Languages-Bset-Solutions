# 0192. Word Frequency

## Bash

```bash
#!/usr/bin/env bash
awk '{ for(i=1;i<=NF;i++) cnt[$i]++ } END{ for (w in cnt) print w, cnt[w] }' words.txt |
sort -k2,2nr -k1,1
```
