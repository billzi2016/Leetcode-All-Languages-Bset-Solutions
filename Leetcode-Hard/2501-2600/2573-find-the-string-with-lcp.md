# 2573. Find the String with LCP

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class DSU {
public:
    vector<int> p, r;
    DSU(int n = 0) { init(n); }
    void init(int n) {
        p.resize(n);
        r.assign(n, 0);
        iota(p.begin(), p.end(), 0);
    }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    void unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return;
        if (r[a] < r[b]) swap(a, b);
        p[b] = a;
        if (r[a] == r[b]) ++r[a];
    }
};

class Solution {
public:
    string findTheString(vector<vector<int>>& lcp) {
        int n = lcp.size();
        // basic validation
        for (int i = 0; i < n; ++i) {
            if (lcp[i][i] != n - i) return "";
            for (int j = i + 1; j < n; ++j) {
                if (lcp[i][j] != lcp[j][i]) return "";
            }
        }

        DSU dsu(n);
        // union positions that must have same character (first char of common prefix)
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (lcp[i][j] > 0) dsu.unite(i, j);
            }
        }

        // build inequality graph
        vector<unordered_set<int>> adj(n);
        auto addEdge = [&](int a, int b) {
            if (a == b) return;
            adj[a].insert(b);
            adj[b].insert(a);
        };

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int ri = dsu.find(i), rj = dsu.find(j);
                if (lcp[i][j] == 0) {
                    addEdge(ri, rj);
                } else {
                    int k = lcp[i][j];
                    if (i + k < n && j + k < n) {
                        int rp = dsu.find(i + k), rq = dsu.find(j + k);
                        addEdge(rp, rq);
                    }
                }
            }
        }

        // assign letters to components greedily
        vector<char> compChar(n, 0);
        string ans;
        ans.resize(n);
        for (int i = 0; i < n; ++i) {
            int r = dsu.find(i);
            if (!compChar[r]) {
                bool used[26] = {false};
                for (int nb : adj[r]) {
                    if (compChar[nb]) used[compChar[nb] - 'a'] = true;
                }
                int c = -1;
                for (int k = 0; k < 26; ++k) if (!used[k]) { c = k; break; }
                if (c == -1) return "";
                compChar[r] = char('a' + c);
            }
            ans[i] = compChar[r];
        }

        // verify by recomputing LCP matrix
        vector<vector<int>> calc(n, vector<int>(n, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (ans[i] == ans[j]) {
                    int v = 1;
                    if (i + 1 < n && j + 1 < n) v += calc[i + 1][j + 1];
                    calc[i][j] = v;
                }
            }
        }
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (calc[i][j] != lcp[i][j]) return "";

        return ans;
    }
};
```

## Java

```java
class Solution {
    public String findTheString(int[][] lcp) {
        int n = lcp.length;
        // Validate dimensions
        for (int i = 0; i < n; i++) {
            if (lcp[i].length != n) return "";
        }
        // Basic validation: diagonal and bounds, symmetry
        for (int i = 0; i < n; i++) {
            if (lcp[i][i] != n - i) return "";
            for (int j = 0; j < n; j++) {
                if (lcp[i][j] != lcp[j][i]) return "";
                int maxLen = Math.min(n - i, n - j);
                if (lcp[i][j] < 0 || lcp[i][j] > maxLen) return "";
            }
        }

        DSU dsu = new DSU(n);
        // Union positions that must be equal (lcp > 0)
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (lcp[i][j] > 0) {
                    dsu.union(i, j);
                }
            }
        }

        int[] groupChar = new int[n];
        java.util.Arrays.fill(groupChar, -1);
        char[] ans = new char[n];

        // Assign letters greedily from left to right
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            if (groupChar[root] == -1) {
                boolean[] forbid = new boolean[26];
                for (int j = 0; j < n; j++) {
                    if (lcp[i][j] == 0) {
                        int r2 = dsu.find(j);
                        if (groupChar[r2] != -1) {
                            forbid[groupChar[r2]] = true;
                        }
                    }
                }
                int c = -1;
                for (int ch = 0; ch < 26; ch++) {
                    if (!forbid[ch]) { c = ch; break; }
                }
                if (c == -1) return "";
                groupChar[root] = c;
            }
            ans[i] = (char)('a' + groupChar[root]);
        }

        // Verify by recomputing LCP matrix
        int[][] calc = new int[n][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (ans[i] == ans[j]) {
                    calc[i][j] = 1 + ((i + 1 < n && j + 1 < n) ? calc[i + 1][j + 1] : 0);
                } else {
                    calc[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (calc[i][j] != lcp[i][j]) return "";
            }
        }

        return new String(ans);
    }

    private static class DSU {
        int[] parent, size;
        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void union(int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }
}
```

## Python

```python
class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        n = len(lcp)
        # basic validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                k = lcp[i][j]
                if k > n - max(i, j):
                    return ""
                if k > 0:
                    if i + 1 < n and j + 1 < n:
                        if lcp[i + 1][j + 1] != k - 1:
                            return ""
        # DSU for equality groups (positive LCP)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)

        # assign smallest possible letters to groups
        root_char = {}
        next_ord = ord('a')
        res = [''] * n
        for i in range(n):
            r = find(i)
            if r not in root_char:
                if next_ord > ord('z'):
                    return ""
                root_char[r] = chr(next_ord)
                next_ord += 1
            res[i] = root_char[r]
        s = ''.join(res)

        # recompute LCP matrix from constructed string
        calc = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    if i + 1 < n and j + 1 < n:
                        calc[i][j] = 1 + calc[i + 1][j + 1]
                    else:
                        calc[i][j] = 1
        # verify equality
        for i in range(n):
            for j in range(n):
                if calc[i][j] != lcp[i][j]:
                    return ""
        return s
```

## Python3

```python
class Solution:
    def findTheString(self, lcp):
        n = len(lcp)

        # validate diagonal
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        # union positions that must be equal
        for i in range(n):
            row = lcp[i]
            for j in range(i + 1, n):
                if row[j] > 0:
                    union(i, j)

        # assign smallest possible letters to each component
        comp_char = {}
        next_ord = ord('a')
        res = [''] * n
        for i in range(n):
            r = find(i)
            if r not in comp_char:
                if next_ord > ord('z'):
                    return ""
                comp_char[r] = chr(next_ord)
                next_ord += 1
            res[i] = comp_char[r]

        s = ''.join(res)

        # recompute LCP matrix from constructed string
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            si = s[i]
            dpi = dp[i]
            dpip1 = dp[i + 1]
            for j in range(n - 1, -1, -1):
                if si == s[j]:
                    dpi[j] = dpip1[j + 1] + 1
                else:
                    dpi[j] = 0

        # verify equality
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""

        return s
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int find_set(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void union_set(int *parent, int *rank, int a, int b) {
    int ra = find_set(parent, a);
    int rb = find_set(parent, b);
    if (ra == rb) return;
    if (rank[ra] < rank[rb]) {
        parent[ra] = rb;
    } else if (rank[ra] > rank[rb]) {
        parent[rb] = ra;
    } else {
        parent[rb] = ra;
        rank[ra]++;
    }
}

char* findTheString(int** lcp, int lcpSize, int* lcpColSize) {
    int n = lcpSize;
    if (n == 0) return "";
    
    // basic validation of diagonal and symmetry
    for (int i = 0; i < n; ++i) {
        if (lcp[i][i] != n - i) return "";
        for (int j = 0; j < n; ++j) {
            if (lcp[i][j] != lcp[j][i]) return "";
            int maxlen = n - (i > j ? i : j);
            if (lcp[i][j] < 0 || lcp[i][j] > maxlen) return "";
        }
    }

    // DSU to group equal characters
    int *parent = (int*)malloc(n * sizeof(int));
    int *rank   = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (lcp[i][j] > 0) {
                union_set(parent, rank, i, j);
            }
        }
    }

    // assign smallest possible letters to groups
    int *groupChar = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) groupChar[i] = -1;
    char *ans = (char*)malloc((n + 1) * sizeof(char));
    ans[n] = '\0';
    int nextIdx = 0; // 0 -> 'a'

    for (int i = 0; i < n; ++i) {
        int r = find_set(parent, i);
        if (groupChar[r] == -1) {
            if (nextIdx >= 26) { // not enough letters
                free(parent); free(rank); free(groupChar); free(ans);
                return "";
            }
            groupChar[r] = 'a' + nextIdx;
            ++nextIdx;
        }
        ans[i] = (char)groupChar[r];
    }

    // verify by recomputing LCP matrix
    int *dpFlat = (int*)calloc((n + 1) * (n + 1), sizeof(int));
    #define DP(i,j) dpFlat[(i)*(n+1)+(j)]
    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (ans[i] == ans[j]) DP(i,j) = 1 + DP(i+1, j+1);
            else DP(i,j) = 0;
        }
    }

    for (int i = 0; i < n && ans[0]; ++i) {
        for (int j = 0; j < n; ++j) {
            if (DP(i,j) != lcp[i][j]) {
                free(parent); free(rank); free(groupChar);
                free(dpFlat);
                free(ans);
                return "";
            }
        }
    }

    free(parent); free(rank); free(groupChar);
    free(dpFlat);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string FindTheString(int[][] lcp) {
        int n = lcp.Length;
        // Validate diagonal entries
        for (int i = 0; i < n; i++) {
            if (lcp[i][i] != n - i) return "";
        }

        // DSU initialization
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        void Union(int a, int b) {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb;
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra;
            } else {
                parent[rb] = ra;
                rank[ra]++;
            }
        }

        // Union positions that must be equal according to lcp
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int len = lcp[i][j];
                for (int k = 0; k < len; k++) {
                    Union(i + k, j + k);
                }
            }
        }

        // Assign smallest possible letters to each component
        Dictionary<int, char> compChar = new Dictionary<int, char>();
        char nextChar = 'a';
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            int root = Find(i);
            if (!compChar.ContainsKey(root)) {
                if (nextChar > 'z') return "";
                compChar[root] = nextChar;
                nextChar++;
            }
            sb.Append(compChar[root]);
        }

        string s = sb.ToString();

        // Verify constructed string matches the given lcp matrix
        int[,] calc = new int[n, n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (s[i] == s[j]) {
                    int val = 1;
                    if (i + 1 < n && j + 1 < n) val += calc[i + 1, j + 1];
                    calc[i, j] = val;
                } else {
                    calc[i, j] = 0;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (calc[i, j] != lcp[i][j]) return "";
            }
        }

        return s;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} lcp
 * @return {string}
 */
var findTheString = function(lcp) {
    const n = lcp.length;
    // validate diagonal
    for (let i = 0; i < n; ++i) {
        if (lcp[i][i] !== n - i) return "";
    }
    // DSU
    class DSU {
        constructor(size) {
            this.parent = new Int32Array(size);
            this.rank = new Uint8Array(size);
            for (let i = 0; i < size; ++i) this.parent[i] = i;
        }
        find(x) {
            let p = this.parent[x];
            if (p !== x) this.parent[x] = this.find(p);
            return this.parent[x];
        }
        union(a, b) {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return;
            if (this.rank[ra] < this.rank[rb]) {
                [ra, rb] = [rb, ra];
            }
            this.parent[rb] = ra;
            if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
        }
    }
    const dsu = new DSU(n);
    // union positions that must have same first character
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (lcp[i][j] > 0) dsu.union(i, j);
        }
    }
    // assign smallest letters to each component
    const compChar = new Map();
    let nextCode = 'a'.charCodeAt(0);
    const resArr = new Array(n);
    for (let i = 0; i < n; ++i) {
        const root = dsu.find(i);
        if (!compChar.has(root)) {
            if (nextCode > 'z'.charCodeAt(0)) return "";
            compChar.set(root, String.fromCharCode(nextCode));
            nextCode++;
        }
        resArr[i] = compChar.get(root);
    }
    const word = resArr.join('');
    // compute LCP matrix from constructed word
    const dp = Array.from({ length: n }, () => new Uint16Array(n));
    for (let i = n - 1; i >= 0; --i) {
        for (let j = n - 1; j >= 0; --j) {
            if (word[i] === word[j]) {
                dp[i][j] = 1 + ((i + 1 < n && j + 1 < n) ? dp[i + 1][j + 1] : 0);
            } else {
                dp[i][j] = 0;
            }
            if (dp[i][j] !== lcp[i][j]) return "";
        }
    }
    return word;
};
```

## Typescript

```typescript
function findTheString(lcp: number[][]): string {
    const n = lcp.length;
    // basic validation
    for (let i = 0; i < n; ++i) {
        if (lcp[i][i] !== n - i) return "";
    }
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (lcp[i][j] !== lcp[j][i]) return "";
            const maxLen = Math.min(n - i, n - j);
            if (lcp[i][j] > maxLen) return "";
        }
    }

    // DSU
    const parent = new Int32Array(n);
    const rank = new Int8Array(n);
    for (let i = 0; i < n; ++i) parent[i] = i;
    const find = (x: number): number => {
        let p = x;
        while (parent[p] !== p) {
            p = parent[p];
        }
        // path compression
        while (parent[x] !== x) {
            const nxt = parent[x];
            parent[x] = p;
            x = nxt;
        }
        return p;
    };
    const union = (a: number, b: number): void => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }
    };

    // union positions with positive LCP
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (lcp[i][j] > 0) union(i, j);
        }
    }

    const groupChar: string[] = new Array(n).fill('');
    const result: string[] = new Array(n);

    // assign characters greedily
    for (let i = 0; i < n; ++i) {
        const ri = find(i);
        if (groupChar[ri] === '') {
            const forbid = new Set<string>();
            for (let j = 0; j < i; ++j) {
                if (lcp[i][j] === 0) {
                    const rj = find(j);
                    const ch = groupChar[rj];
                    if (ch !== '') forbid.add(ch);
                }
            }
            let assigned = '';
            for (let c = 0; c < 26; ++c) {
                const ch = String.fromCharCode(97 + c);
                if (!forbid.has(ch)) {
                    assigned = ch;
                    break;
                }
            }
            if (assigned === '') return "";
            groupChar[ri] = assigned;
        }
        result[i] = groupChar[ri];
    }

    // recompute LCP matrix from constructed string
    const computed: number[][] = Array.from({ length: n }, () => new Int32Array(n));
    for (let i = n - 1; i >= 0; --i) {
        for (let j = n - 1; j >= 0; --j) {
            if (result[i] === result[j]) {
                let val = 1;
                if (i + 1 < n && j + 1 < n) val += computed[i + 1][j + 1];
                computed[i][j] = val;
            } else {
                computed[i][j] = 0;
            }
        }
    }

    // verify equality
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (computed[i][j] !== lcp[i][j]) return "";
        }
    }

    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $lcp
     * @return String
     */
    function findTheString($lcp) {
        $n = count($lcp);
        // basic validation
        for ($i = 0; $i < $n; ++$i) {
            if ($lcp[$i][$i] !== $n - $i) return "";
        }
        for ($i = 0; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                if ($lcp[$i][$j] !== $lcp[$j][$i]) return "";
                $maxLen = $n - max($i, $j);
                if ($lcp[$i][$j] > $maxLen) return "";
            }
        }

        // DSU for equality constraints
        class DSU {
            public $parent;
            function __construct($n) {
                $this->parent = range(0, $n - 1);
            }
            function find($x) {
                if ($this->parent[$x] !== $x) {
                    $this->parent[$x] = $this->find($this->parent[$x]);
                }
                return $this->parent[$x];
            }
            function union($a, $b) {
                $ra = $this->find($a);
                $rb = $this->find($b);
                if ($ra !== $rb) {
                    $this->parent[$rb] = $ra;
                }
            }
        }

        $dsu = new DSU($n);

        // process equality using offset method with next-pointer
        for ($d = 1; $d < $n; ++$d) {
            // next array for this offset
            $next = [];
            for ($i = 0; $i <= $n; ++$i) $next[$i] = $i;
            // recursive findNext using closure
            $findNext = function($x) use (&$next, &$findNext) {
                if ($next[$x] === $x) return $x;
                $next[$x] = $findNext($next[$x]);
                return $next[$x];
            };
            for ($i = 0; $i + $d < $n; ++$i) {
                $len = $lcp[$i][$i + $d];
                if ($len == 0) continue;
                $pos = $i;
                while (true) {
                    $pos = $findNext($pos);
                    if ($pos >= $i + $len) break;
                    $dsu->union($pos, $pos + $d);
                    // mark processed
                    $next[$pos] = $pos + 1;
                    $pos++; // move forward for next iteration
                }
            }
        }

        // build inequality graph and check contradictions
        $adj = array_fill(0, $n, []);
        for ($i = 0; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                $len = $lcp[$i][$j];
                if ($i + $len < $n && $j + $len < $n) {
                    $aRoot = $dsu->find($i + $len);
                    $bRoot = $dsu->find($j + $len);
                    if ($aRoot === $bRoot) return "";
                    $adj[$aRoot][] = $bRoot;
                    $adj[$bRoot][] = $aRoot;
                }
            }
        }

        // assign smallest possible letters to each component
        $char = [];
        for ($i = 0; $i < $n; ++$i) {
            $root = $dsu->find($i);
            if (!isset($char[$root])) {
                $used = array_fill(0, 26, false);
                foreach ($adj[$root] as $nbr) {
                    if (isset($char[$nbr])) {
                        $idx = ord($char[$nbr]) - 97;
                        $used[$idx] = true;
                    }
                }
                $cIdx = 0;
                while ($cIdx < 26 && $used[$cIdx]) ++$cIdx;
                if ($cIdx == 26) return "";
                $char[$root] = chr(97 + $cIdx);
            }
        }

        // build resulting string
        $res = '';
        for ($i = 0; $i < $n; ++$i) {
            $res .= $char[$dsu->find($i)];
        }

        // verify by recomputing LCP matrix
        $calc = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = $n - 1; $i >= 0; --$i) {
            for ($j = $n - 1; $j >= 0; --$j) {
                if ($res[$i] === $res[$j]) {
                    $calc[$i][$j] = 1;
                    if ($i + 1 < $n && $j + 1 < $n) {
                        $calc[$i][$j] += $calc[$i + 1][$j + 1];
                    }
                } else {
                    $calc[$i][$j] = 0;
                }
            }
        }
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($calc[$i][$j] !== $lcp[$i][$j]) return "";
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    class DSU {
        var parent: [Int]
        init(_ n: Int) {
            parent = Array(0..<n)
        }
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        func union(_ a: Int, _ b: Int) {
            let ra = find(a)
            let rb = find(b)
            if ra != rb {
                parent[ra] = rb
            }
        }
    }

    func findTheString(_ lcp: [[Int]]) -> String {
        let n = lcp.count
        // diagonal must be n
        for i in 0..<n {
            if lcp[i][i] != n { return "" }
        }

        let dsu = DSU(n)

        // Union positions according to LCP values
        for i in 0..<n {
            for j in (i + 1)..<n {
                let v = lcp[i][j]
                if v == 0 { continue }
                if i + v > n || j + v > n { return "" }
                var k = 0
                while k < v {
                    dsu.union(i + k, j + k)
                    k += 1
                }
            }
        }

        // Assign smallest possible letters to each component
        var compChar = Array(repeating: -1, count: n)   // char index for root
        var nextIdx = 0
        var chars = [Character](repeating: "a", count: n)

        for i in 0..<n {
            let r = dsu.find(i)
            if compChar[r] == -1 {
                if nextIdx >= 26 { return "" }
                compChar[r] = nextIdx
                nextIdx += 1
            }
            let ch = Character(UnicodeScalar(97 + compChar[r])!)
            chars[i] = ch
        }

        let word = String(chars)

        // Recompute LCP matrix from constructed string
        var calc = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                if chars[i] == chars[j] {
                    let nxt = (i + 1 < n && j + 1 < n) ? calc[i + 1][j + 1] : 0
                    calc[i][j] = 1 + nxt
                } else {
                    calc[i][j] = 0
                }
            }
        }

        // Verify against given LCP (ignore diagonal which is already checked)
        for i in 0..<n {
            for j in 0..<n where i != j {
                if lcp[i][j] != calc[i][j] {
                    return ""
                }
            }
        }

        return word
    }
}
```

## Kotlin

```kotlin
import java.util.StringTokenizer

class Solution {
    private class DSU(n: Int) {
        private val parent = IntArray(n) { it }
        private val rank = IntArray(n)

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (rank[ra] < rank[rb]) {
                val t = ra; ra = rb; rb = t
            }
            parent[rb] = ra
            if (rank[ra] == rank[rb]) rank[ra]++
        }
    }

    fun findTheString(lcp: Array<IntArray>): String {
        val n = lcp.size
        // basic validation
        for (i in 0 until n) {
            if (lcp[i][i] != n - i) return ""
            for (j in i + 1 until n) {
                if (lcp[i][j] != lcp[j][i]) return ""
            }
        }
        // consistency of decreasing property
        for (i in 0 until n) {
            for (j in 0 until n) {
                val v = lcp[i][j]
                if (v > 0) {
                    if (i + v > n || j + v > n) return ""
                    if (i + 1 < n && j + 1 < n) {
                        if (lcp[i + 1][j + 1] != v - 1) return ""
                    } else {
                        if (v != 1) return ""
                    }
                }
            }
        }

        // union equal first characters
        val dsu = DSU(n)
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (lcp[i][j] > 0) dsu.union(i, j)
            }
        }

        // map each root to component id
        val compId = IntArray(n)
        val rootToIdx = HashMap<Int, Int>()
        var cnt = 0
        for (i in 0 until n) {
            val r = dsu.find(i)
            val idx = rootToIdx.getOrPut(r) { cnt++ }
            compId[i] = idx
        }

        // adjacency for inequality constraints
        val adj = Array(cnt) { mutableSetOf<Int>() }
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (lcp[i][j] == 0) {
                    val a = compId[i]
                    val b = compId[j]
                    if (a == b) return ""
                    adj[a].add(b)
                    adj[b].add(a)
                }
            }
        }

        // assign letters greedily to achieve lexicographically smallest string
        val compChar = CharArray(cnt) { '\u0000' }
        for (i in 0 until n) {
            val cid = compId[i]
            if (compChar[cid] == '\u0000') {
                val used = BooleanArray(26)
                for (nb in adj[cid]) {
                    val ch = compChar[nb]
                    if (ch != '\u0000') used[ch.code - 'a'.code] = true
                }
                var found = false
                for (k in 0 until 26) {
                    if (!used[k]) {
                        compChar[cid] = ('a'.code + k).toChar()
                        found = true
                        break
                    }
                }
                if (!found) return ""
            }
        }

        // build result string
        val sb = StringBuilder()
        for (i in 0 until n) sb.append(compChar[compId[i]])
        val res = sb.toString()

        // final verification of LCP matrix
        val calc = Array(n) { IntArray(n) }
        for (i in n - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (res[i] == res[j]) {
                    calc[i][j] = 1 + if (i + 1 < n && j + 1 < n) calc[i + 1][j + 1] else 0
                } else {
                    calc[i][j] = 0
                }
            }
        }
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (calc[i][j] != lcp[i][j]) return ""
            }
        }

        return res
    }
}
```

## Dart

```dart
class Solution {
  String findTheString(List<List<int>> lcp) {
    int n = lcp.length;
    // Validate dimensions
    for (var row in lcp) {
      if (row.length != n) return "";
    }

    // Diagonal check
    for (int i = 0; i < n; ++i) {
      if (lcp[i][i] != n - i) return "";
    }

    // Symmetry and basic bounds check
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (lcp[i][j] != lcp[j][i]) return "";
        int maxLen = n - (i > j ? i : j);
        if (lcp[i][j] > maxLen) return "";
      }
    }

    // DSU for equal characters
    var dsu = _DSU(n);

    // Validate recurrence and build unions
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        int val = lcp[i][j];
        if (val == 0) continue;

        // Recurrence condition
        if (i + 1 < n && j + 1 < n) {
          if (val != lcp[i + 1][j + 1] + 1) return "";
        } else {
          if (val != 1) return "";
        }

        dsu.union(i, j);
      }
    }

    // Assign smallest possible letters to each component
    List<String> chars = List.filled(n, '');
    Map<int, String> compChar = {};
    int nextCode = 'a'.codeUnitAt(0);
    for (int i = 0; i < n; ++i) {
      int root = dsu.find(i);
      if (!compChar.containsKey(root)) {
        if (nextCode > 'z'.codeUnitAt(0)) return "";
        compChar[root] = String.fromCharCode(nextCode);
        nextCode++;
      }
      chars[i] = compChar[root]!;
    }

    String ans = chars.join();

    // Verify constructed LCP matrix matches the given one
    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));
    for (int i = n - 1; i >= 0; --i) {
      for (int j = n - 1; j >= 0; --j) {
        if (ans.codeUnitAt(i) == ans.codeUnitAt(j)) {
          int v = 1;
          if (i + 1 < n && j + 1 < n) v += dp[i + 1][j + 1];
          dp[i][j] = v;
        } else {
          dp[i][j] = 0;
        }
        if (dp[i][j] != lcp[i][j]) return "";
      }
    }

    return ans;
  }
}

class _DSU {
  List<int> parent;
  _DSU(int n) : parent = List.generate(n, (i) => i);
  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  void union(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra != rb) parent[ra] = rb;
  }
}
```

## Golang

```go
func findTheString(lcp [][]int) string {
    n := len(lcp)
    if n == 0 {
        return ""
    }
    // validate diagonal and bounds
    for i := 0; i < n; i++ {
        if lcp[i][i] != n-i {
            return ""
        }
    }

    type DSU struct {
        parent []int
        rank   []int
    }
    newDSU := func(size int) *DSU {
        p := make([]int, size)
        r := make([]int, size)
        for i := 0; i < size; i++ {
            p[i] = i
        }
        return &DSU{parent: p, rank: r}
    }
    var find func(*DSU, int) int
    find = func(d *DSU, x int) int {
        if d.parent[x] != x {
            d.parent[x] = find(d, d.parent[x])
        }
        return d.parent[x]
    }
    union := func(d *DSU, a, b int) {
        ra := find(d, a)
        rb := find(d, b)
        if ra == rb {
            return
        }
        if d.rank[ra] < d.rank[rb] {
            ra, rb = rb, ra
        }
        d.parent[rb] = ra
        if d.rank[ra] == d.rank[rb] {
            d.rank[ra]++
        }
    }

    dsu := newDSU(n)

    min := func(a, b int) int {
        if a < b {
            return a
        }
        return b
    }

    // validate matrix and union equal positions
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            v := lcp[i][j]
            if v > min(n-i, n-j) {
                return ""
            }
            if v > 0 {
                // recurrence check
                if i+1 < n && j+1 < n {
                    if lcp[i+1][j+1] != v-1 {
                        return ""
                    }
                } else {
                    if v != 1 {
                        return ""
                    }
                }
                union(dsu, i, j)
            }
        }
    }

    // build adjacency for zero LCP constraints
    adj := make([][]int, n)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if lcp[i][j] == 0 {
                ri := find(dsu, i)
                rj := find(dsu, j)
                if ri == rj {
                    return ""
                }
                adj[ri] = append(adj[ri], rj)
                adj[rj] = append(adj[rj], ri)
            }
        }
    }

    assign := make([]byte, n) // 0 means unassigned
    res := make([]byte, n)

    for i := 0; i < n; i++ {
        root := find(dsu, i)
        if assign[root] == 0 {
            used := [26]bool{}
            for _, nb := range adj[root] {
                c := assign[nb]
                if c != 0 {
                    used[c-'a'] = true
                }
            }
            var ch byte = 0
            for k := 0; k < 26; k++ {
                if !used[k] {
                    ch = byte('a' + k)
                    break
                }
            }
            if ch == 0 { // no available letter
                return ""
            }
            assign[root] = ch
        }
        res[i] = assign[root]
    }

    return string(res)
}
```

## Ruby

```ruby
def find_the_string(lcp)
  n = lcp.size
  # basic validation
  (0...n).each do |i|
    return "" unless lcp[i][i] == n - i
    (0...n).each do |j|
      return "" if lcp[i][j] != lcp[j][i]
    end
  end

  parent = Array.new(n) { |i| i }
  rank   = Array.new(n, 0)

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if rank[ra] < rank[rb]
      parent[ra] = rb
    elsif rank[ra] > rank[rb]
      parent[rb] = ra
    else
      parent[rb] = ra
      rank[ra] += 1
    end
  end

  # process equality constraints by offset
  (1...n).each do |d|
    cur_l = -1
    cur_r = -1
    i = 0
    while i < n - d
      len = lcp[i][i + d]
      if len > 0
        start = i
        finish = i + len - 1
        if cur_l == -1
          cur_l = start
          cur_r = finish
        else
          if start <= cur_r + 1
            cur_r = [cur_r, finish].max
          else
            (cur_l..cur_r).each { |p| union.call(p, p + d) }
            cur_l = start
            cur_r = finish
          end
        end
      end
      i += 1
    end
    if cur_l != -1
      (cur_l..cur_r).each { |p| union.call(p, p + d) }
    end
  end

  # assign smallest possible letters to groups
  root_to_char = {}
  next_code = 'a'.ord
  chars = Array.new(n)
  (0...n).each do |i|
    r = find.call(i)
    unless root_to_char.key?(r)
      return "" if next_code > 'z'.ord
      root_to_char[r] = next_code.chr
      next_code += 1
    end
    chars[i] = root_to_char[r]
  end
  s = chars.join

  # recompute LCP matrix to verify correctness
  calc = Array.new(n) { Array.new(n, 0) }
  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      if s[i] == s[j]
        calc[i][j] = 1 + ((i + 1 < n && j + 1 < n) ? calc[i + 1][j + 1] : 0)
      else
        calc[i][j] = 0
      end
    end
  end

  (0...n).each do |i|
    (0...n).each do |j|
      return "" if calc[i][j] != lcp[i][j]
    end
  end

  s
end
```

## Scala

```scala
object Solution {
  def findTheString(lcp: Array[Array[Int]]): String = {
    val n = lcp.length
    // basic validation
    for (i <- 0 until n) {
      if (lcp(i)(i) != n - i) return ""
      var j = i + 1
      while (j < n) {
        if (lcp(i)(j) != lcp(j)(i)) return ""
        j += 1
      }
    }

    // DSU for positions that must have same first character
    class DSU(val size: Int) {
      private val parent = (0 until size).toArray
      def find(x: Int): Int = {
        if (parent(x) != x) parent(x) = find(parent(x))
        parent(x)
      }
      def union(a: Int, b: Int): Unit = {
        val ra = find(a)
        val rb = find(b)
        if (ra != rb) parent(rb) = ra
      }
    }

    val dsu = new DSU(n)

    // Union positions with lcp > 0 (same first character)
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        if (lcp(i)(j) > 0) dsu.union(i, j)
        j += 1
      }
      i += 1
    }

    // Determine components and their minimal index
    import scala.collection.mutable
    val minIdx = mutable.Map[Int, Int]()
    for (idx <- 0 until n) {
      val r = dsu.find(idx)
      minIdx.get(r) match {
        case Some(v) => if (idx < v) minIdx(r) = idx
        case None    => minIdx(r) = idx
      }
    }

    // Sort components by minimal index to assign letters greedily
    val sortedRoots = minIdx.toSeq.sortBy(_._2).map(_._1)
    if (sortedRoots.length > 26) return ""

    val chars = new Array[Char](n)
    var cur = 'a'
    for (root <- sortedRoots) {
      for (pos <- 0 until n) {
        if (dsu.find(pos) == root) chars(pos) = cur
      }
      cur = (cur + 1).toChar
    }

    val word = new String(chars)

    // Compute LCP matrix of constructed word
    val dp = Array.ofDim[Int](n + 1, n + 1)
    var ii = n - 1
    while (ii >= 0) {
      var jj = n - 1
      while (jj >= 0) {
        if (word.charAt(ii) == word.charAt(jj)) {
          dp(ii)(jj) = 1 + dp(ii + 1)(jj + 1)
        }
        jj -= 1
      }
      ii -= 1
    }

    // Verify against given lcp
    for (a <- 0 until n) {
      var b = 0
      while (b < n) {
        if (dp(a)(b) != lcp(a)(b)) return ""
        b += 1
      }
    }

    word
  }
}
```

## Rust

```rust
use std::cmp::max;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}
impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        DSU { parent, size: vec![1; n] }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }
    fn union(&mut self, a: usize, b: usize) {
        let mut ra = self.find(a);
        let mut rb = self.find(b);
        if ra == rb { return; }
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }
}

impl Solution {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        let n = lcp.len();
        if n == 0 { return "".to_string(); }
        // basic validation of dimensions
        for row in &lcp {
            if row.len() != n { return "".to_string(); }
        }
        // diagonal check: lcp[i][i] must be n - i
        for i in 0..n {
            if lcp[i][i] as usize != n - i { return "".to_string(); }
        }

        let mut dsu = DSU::new(n);
        // union positions that must have same character (lcp > 0)
        for i in 0..n {
            for j in (i+1)..n {
                if lcp[i][j] > 0 {
                    dsu.union(i, j);
                }
            }
        }

        // assign smallest possible letters to each component
        let mut comp_char: Vec<Option<char>> = vec![None; n];
        let mut next_byte: u8 = b'a';
        let mut s_bytes: Vec<u8> = vec![b' '; n];
        for i in 0..n {
            let root = dsu.find(i);
            if comp_char[root].is_none() {
                if next_byte > b'z' { return "".to_string(); }
                comp_char[root] = Some(next_byte as char);
                next_byte += 1;
            }
            s_bytes[i] = comp_char[root].unwrap() as u8;
        }

        // compute LCP matrix of constructed string
        let mut calc: Vec<Vec<i32>> = vec![vec![0; n]; n];
        for i_rev in (0..n).rev() {
            for j_rev in (0..n).rev() {
                if s_bytes[i_rev] == s_bytes[j_rev] {
                    let mut val = 1;
                    if i_rev + 1 < n && j_rev + 1 < n {
                        val += calc[i_rev + 1][j_rev + 1];
                    }
                    calc[i_rev][j_rev] = val as i32;
                } else {
                    calc[i_rev][j_rev] = 0;
                }
            }
        }

        // verify equality with given lcp matrix
        for i in 0..n {
            for j in 0..n {
                if calc[i][j] != lcp[i][j] {
                    return "".to_string();
                }
            }
        }

        String::from_utf8(s_bytes).unwrap()
    }
}
```

## Racket

```racket
(define/contract (find-the-string lcp)
  (-> (listof (listof exact-integer?)) string?)
  (call/cc
    (lambda (return)
      (let* ((n (length lcp))
             (lcp-vec (list->vector (map list->vector lcp))))
        ;; basic diagonal check
        (for ([i (in-range n)])
          (when (not (= (vector-ref (vector-ref lcp-vec i) i)
                        (- n i)))
            (return "")))
        ;; symmetry check
        (for ([i (in-range n)])
          (for ([j (in-range (+ i 1) n)])
            (when (not (= (vector-ref (vector-ref lcp-vec i) j)
                          (vector-ref (vector-ref lcp-vec j) i)))
              (return ""))))
        ;; DSU initialization
        (define parent (make-vector n))
        (define rank   (make-vector n 0))
        (for ([i (in-range n)]) (vector-set! parent i i))
        (define (find x)
          (let ((p (vector-ref parent x)))
            (if (= p x)
                x
                (let ((root (find p)))
                  (vector-set! parent x root)
                  root))))
        (define (union a b)
          (let* ((ra (find a))
                 (rb (find b)))
            (when (not (= ra rb))
              (let ((ra-rank (vector-ref rank ra))
                    (rb-rank (vector-ref rank rb)))
                (cond
                  [(< ra-rank rb-rank) (vector-set! parent ra rb)]
                  [(> ra-rank rb-rank) (vector-set! parent rb ra)]
                  [else (vector-set! parent rb ra)
                        (vector-set! rank ra (+ ra-rank 1))])))))
        ;; union positions with positive LCP
        (for ([i (in-range n)])
          (for ([j (in-range (+ i 1) n)])
            (when (> (vector-ref (vector-ref lcp-vec i) j) 0)
              (union i j))))
        ;; conflict: zero LCP but same group
        (for ([i (in-range n)])
          (for ([j (in-range (+ i 1) n)])
            (when (= (vector-ref (vector-ref lcp-vec i) j) 0)
              (when (= (find i) (find j))
                (return "")))))
        ;; assign smallest letters to groups
        (define group-char (make-vector n #\space))
        (define next-code (char->integer #\a))
        (for ([i (in-range n)])
          (let ((root (find i)))
            (when (eq? (vector-ref group-char root) #\space)
              (when (> (- next-code (char->integer #\a)) 25)
                (return ""))
              (vector-set! group-char root (integer->char next-code))
              (set! next-code (+ next-code 1)))))
        ;; build result string
        (define res (make-string n))
        (for ([i (in-range n)])
          (string-set! res i (vector-ref group-char (find i))))
        ;; compute LCP matrix of constructed string via DP
        (define dp (make-vector n))
        (for ([i (in-range n)]) (vector-set! dp i (make-vector n 0)))
        (for ([i (in-range (- n 1) -1 -1)])
          (for ([j (in-range (- n 1) -1 -1)])
            (cond
              [(= i j)
               (vector-set! (vector-ref dp i) j (- n i))]
              [else
               (if (char=? (string-ref res i) (string-ref res j))
                   (let ((val (if (and (< (+ i 1) n) (< (+ j 1) n))
                                  (+ 1 (vector-ref (vector-ref dp (+ i 1)) (+ j 1)))
                                  1)))
                     (vector-set! (vector-ref dp i) j val))
                   (vector-set! (vector-ref dp i) j 0))])))
        ;; verify equality with given LCP
        (for ([i (in-range n)])
          (for ([j (in-range n)])
            (when (not (= (vector-ref (vector-ref dp i) j)
                          (vector-ref (vector-ref lcp-vec i) j)))
              (return ""))))
        res))))
```

## Erlang

```erlang
-spec find_the_string(Lcp :: [[integer()]]) -> unicode:unicode_binary().
find_the_string(Lcp) ->
    N = length(Lcp),
    %% Convert LCP matrix rows to tuples for O(1) access
    LcpTuples = [list_to_tuple(Row) || Row <- Lcp],
    case validate_and_collect(N, LcpTuples) of
        {error, _} -> <<>>,
        {ok, Pairs} ->
            %% Initialize DSU
            Parent0 = list_to_tuple(lists:seq(0, N - 1)),
            Rank0 = zero_tuple(N),
            {Parent1, _Rank1} = union_all(Pairs, Parent0, Rank0),
            %% Assign characters
            case assign_chars(0, N, Parent1, #{}, $a, []) of
                {error, _} -> <<>>,
                {CharListRev, CharMap} ->
                    CharList = lists:reverse(CharListRev),
                    CharTuple = list_to_tuple(CharList),
                    %% Verify full LCP matrix
                    case verify_lcp(N, CharTuple, LcpTuples) of
                        true -> list_to_binary(CharList);
                        false -> <<>>
                    end
            end
    end.

%% Validate diagonal and symmetry, collect pairs with lcp>0
validate_and_collect(N, LcpTuples) ->
    validate_and_collect(0, N, LcpTuples, []).

validate_and_collect(I, N, _LcpTuples, Pairs) when I >= N -> {ok, Pairs};
validate_and_collect(I, N, LcpTuples, Pairs) ->
    RowI = element(LcpTuples, I + 1),
    Diag = element(RowI, I + 1),
    ExpectedDiag = N - I,
    if Diag =/= ExpectedDiag -> {error, diag};
       true ->
           case validate_row(I, I + 1, N, LcpTuples, Pairs) of
               {error, _}=Err -> Err;
               {ok, NewPairs} -> validate_and_collect(I + 1, N, LcpTuples, NewPairs)
           end
    end.

validate_row(_I, J, N, _LcpTuples, Pairs) when J >= N -> {ok, Pairs};
validate_row(I, J, N, LcpTuples, Pairs) ->
    RowI = element(LcpTuples, I + 1),
    RowJ = element(LcpTuples, J + 1),
    LenIJ = element(RowI, J + 1),
    LenJI = element(RowJ, I + 1),
    if LenIJ =/= LenJI -> {error, sym};
       true ->
           NewPairs = if LenIJ > 0 -> [{I, J} | Pairs]; true -> Pairs end,
           validate_row(I, J + 1, N, LcpTuples, NewPairs)
    end.

%% Union all pairs
union_all([], Parent, Rank) -> {Parent, Rank};
union_all([{I, J} | Rest], Parent, Rank) ->
    {P2, R2} = union(I, J, Parent, Rank),
    union_all(Rest, P2, R2).

%% DSU find with path compression
find(X, Parent) ->
    PX = element(Parent, X + 1),
    if PX =:= X -> {X, Parent};
       true ->
           {Root, NewParent} = find(PX, Parent),
           Updated = setelement(X + 1, NewParent, Root),
           {Root, Updated}
    end.

%% DSU union by rank
union(I, J, Parent, Rank) ->
    {Ri, P1} = find(I, Parent),
    {Rj, P2} = find(J, P1),
    if Ri =:= Rj -> {P2, Rank};
       true ->
           RankI = element(Rank, Ri + 1),
           RankJ = element(Rank, Rj + 1),
           case compare(RankI, RankJ) of
               less ->
                   P3 = setelement(Ri + 1, P2, Rj),
                   {P3, Rank};
               greater ->
                   P3 = setelement(Rj + 1, P2, Ri),
                   {P3, Rank};
               equal ->
                   P3 = setelement(Rj + 1, P2, Ri),
                   NewRank = setelement(Ri + 1, Rank, RankI + 1),
                   {P3, NewRank}
           end
    end.

compare(A, B) when A < B -> less;
compare(A, B) when A > B -> greater;
compare(_, _) -> equal.

%% Assign characters to groups ensuring lexicographically smallest string
assign_chars(I, N, _Parent, _Map, _NextCode, Acc) when I >= N ->
    {Acc, #{}}; % map not needed further
assign_chars(I, N, Parent, Map, NextCode, Acc) ->
    {Root, NewParent} = find(I, Parent),
    case maps:is_key(Root, Map) of
        true ->
            Char = maps:get(Root, Map),
            assign_chars(I + 1, N, NewParent, Map, NextCode, [Char | Acc]);
        false ->
            if NextCode > $z -> {error, too_many_groups};
               true ->
                   Char = NextCode,
                   NewMap = maps:put(Root, Char, Map),
                   assign_chars(I + 1, N, NewParent, NewMap, NextCode + 1, [Char | Acc])
            end
    end.

%% Verify full LCP matrix using DP with O(N^2) time and O(N) extra space
verify_lcp(N, CharTuple, LcpTuples) ->
    ZeroRow = zero_tuple(N),
    verify_rows(N - 1, N, CharTuple, LcpTuples, ZeroRow).

verify_rows(-1, _N, _CharT, _LcpT, _NextRow) -> true;
verify_rows(I, N, CharT, LcpT, NextRow) ->
    case build_row(I, N - 1, N, CharT, LcpT, NextRow, zero_tuple(N)) of
        {error, _} -> false;
        CurrRow -> verify_rows(I - 1, N, CharT, LcpT, CurrRow)
    end.

build_row(_I, J, _N, _CharT, _LcpT, _NextRow, _Curr) when J < 0 ->
    {ok, _Curr}; % will be handled by caller
build_row(I, J, N, CharT, LcpT, NextRow, CurrAcc) ->
    CharI = element(CharT, I + 1),
    CharJ = element(CharT, J + 1),
    Val =
        if CharI =:= CharJ ->
                if I + 1 < N andalso J + 1 < N ->
                        1 + element(NextRow, J + 2);
                   true -> 1
                end;
           true -> 0
        end,
    Expected = element(element(LcpT, I + 1), J + 1),
    if Val =/= Expected ->
            {error, mismatch};
       true ->
            UpdatedCurr = setelement(J + 1, CurrAcc, Val),
            case build_row(I, J - 1, N, CharT, LcpT, NextRow, UpdatedCurr) of
                {error, _}=E -> E;
                {ok, FinalRow} -> {ok, FinalRow}
            end
    end.

zero_tuple(N) ->
    list_to_tuple(lists:duplicate(N, 0)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_string(lcp :: [[integer]]) :: String.t
  def find_the_string(lcp) do
    n = length(lcp)
    rows = lcp |> Enum.map(&List.to_tuple/1) |> List.to_tuple()

    get = fn i, j -> elem(elem(rows, i), j) end

    # basic validation of diagonal and LCP recurrence
    if not valid_matrix?(n, rows, get) do
      ""
    else
      # build DSU using :array for parents
      parent0 = :array.from_list(Enum.to_list(0..(n - 1)))

      parent =
        Enum.reduce(0..(n - 2), parent0, fn i, par ->
          Enum.reduce((i + 1)..(n - 1), par, fn j, pacc ->
            if get.(i, j) > 0 do
              union(i, j, pacc)
            else
              pacc
            end
          end)
        end)

      # compute root for each position (no path compression needed)
      roots = for i <- 0..(n - 1), do: find_root(i, parent)

      # check zero entries that would force same group -> impossible
      if has_zero_conflict?(roots, get) do
        ""
      else
        # map each distinct root to a group id and remember its smallest index
        {root_to_id, order} = groups_info(roots)

        gcount = map_size(root_to_id)
        adj = :array.new(gcount, default: MapSet.new())

        # build adjacency for inequality (zero LCP) between different groups
        adj =
          Enum.reduce(0..(n - 2), adj, fn i, a1 ->
            Enum.reduce((i + 1)..(n - 1), a1, fn j, a2 ->
              if get.(i, j) == 0 do
                r1 = roots[i]
                r2 = roots[j]

                if r1 != r2 do
                  id1 = Map.fetch!(root_to_id, r1)
                  id2 = Map.fetch!(root_to_id, r2)

                  a2
                  |> add_edge(id1, id2)
                else
                  a2
                end
              else
                a2
              end
            end)
          end)

        # greedy coloring using at most 26 letters
        colors = :array.new(gcount, default: -1)

        {colors, ok} =
          Enum.reduce(order, {colors, true}, fn {_gid, _min_idx} = grp, {col_arr, acc_ok} ->
            if not acc_ok do
              {col_arr, false}
            else
              gid = elem(grp, 0)
              neigh = :array.get(gid, adj)

              used =
                Enum.reduce(neigh, MapSet.new(), fn nb, set ->
                  c = :array.get(nb, col_arr)
                  if c != -1, do: MapSet.put(set, c), else: set
                end)

              color = Enum.find(0..25, fn x -> not MapSet.member?(used, x) end)

              if color == nil do
                {col_arr, false}
              else
                { :array.set(gid, color, col_arr), true }
              end
            end
          end)

        if not ok do
          ""
        else
          # construct final string
          chars =
            for i <- 0..(n - 1) do
              root = roots[i]
              gid = Map.fetch!(root_to_id, root)
              col = :array.get(gid, colors)
              ?a + col
            end

          List.to_string(chars)
        end
      end
    end
  end

  # Validate diagonal and recurrence property of LCP matrix
  defp valid_matrix?(n, rows, get) do
    Enum.reduce_while(0..(n - 1), true, fn i, _ ->
      diag = elem(elem(rows, i), i)
      if diag != n - i, do: {:halt, false}, else
        res =
          Enum.reduce_while(0..(n - 1), true, fn j, _inner ->
            cond do
              i == j -> {:cont, true}
              true ->
                k = get.(i, j)
                if k > 0 do
                  if i + 1 < n and j + 1 < n do
                    expected = get.(i + 1, j + 1)
                    if expected != k - 1, do: {:halt, false}, else: {:cont, true}
                  else
                    # one suffix length is 1, so k must be 1
                    if k != 1, do: {:halt, false}, else: {:cont, true}
                  end
                else
                  {:cont, true}
            end
          end)

        case res do
          false -> {:halt, false}
          true -> {:cont, true}
        end
    end) == true
  end

  # DSU find root without path compression (sufficient for n<=1000)
  defp find_root(x, parent) do
    p = :array.get(x, parent)
    if p == x, do: x, else: find_root(p, parent)
  end

  # Union by attaching root of b to root of a
  defp union(a, b, parent) do
    ra = find_root(a, parent)
    rb = find_root(b, parent)

    if ra == rb do
      parent
    else
      :array.set(rb, ra, parent)
    end
  end

  # Detect zero LCP entries that force same group (contradiction)
  defp has_zero_conflict?(roots, get) do
    n = length(roots)

    Enum.any?(0..(n - 2), fn i ->
      Enum.any?((i + 1)..(n - 1), fn j ->
        get.(i, j) == 0 and roots[i] == roots[j]
      end)
    end)
  end

  # Build mapping from root to group id and ordering by smallest index
  defp groups_info(roots) do
    {map, _cnt, order} =
      Enum.reduce(Enum.with_index(roots), {%{}, 0, []}, fn {root, idx}, {m, cnt, ord} ->
        if Map.has_key?(m, root) do
          {m, cnt, ord}
        else
          new_m = Map.put(m, root, cnt)
          {new_m, cnt + 1, [{cnt, idx} | ord]}
        end
      end)

    order_sorted = Enum.sort_by(order, fn {_id, min_idx} -> min_idx end)
    {map, order_sorted}
  end

  # Add undirected edge between two group ids in adjacency array
  defp add_edge(adj, id1, id2) do
    set1 = :array.get(id1, adj) |> MapSet.put(id2)
    set2 = :array.get(id2, adj) |> MapSet.put(id1)

    adj
    |> :array.set(id1, set1)
    |> :array.set(id2, set2)
  end
end
```
