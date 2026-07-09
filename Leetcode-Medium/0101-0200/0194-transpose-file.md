# 0194. Transpose File

## Bash

```bash
#!/usr/bin/env bash
awk '
{
    for (i = 1; i <= NF; i++) a[NR,i] = $i
}
END {
    for (i = 1; i <= NF; i++) {
        for (j = 1; j <= NR; j++) {
            printf "%s%s", a[j,i], (j == NR ? ORS : OFS)
        }
    }
}
' file.txt
```
