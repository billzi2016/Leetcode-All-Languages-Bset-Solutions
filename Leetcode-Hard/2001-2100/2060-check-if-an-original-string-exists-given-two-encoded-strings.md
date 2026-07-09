# 2060. Check if an Original String Exists Given Two Encoded Strings

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool possiblyEquals(string s1, string s2) {
        int n1 = s1.size(), n2 = s2.size();
        queue<tuple<int,int,int>> q;
        unordered_set<string> vis;
        auto encode = [&](int i,int j,int d)->string{
            return to_string(i)+'#'+to_string(j)+'#'+to_string(d);
        };
        q.emplace(0,0,0);
        vis.insert(encode(0,0,0));
        
        auto getNumbers = [&](const string& s, int idx){
            vector<pair<int,int>> res;
            int val = 0;
            for(int len=1; idx+len<= (int)s.size() && len<=3; ++len){
                if(!isdigit(s[idx+len-1])) break;
                val = val*10 + (s[idx+len-1]-'0');
                res.emplace_back(idx+len, val);
            }
            return res;
        };
        
        while(!q.empty()){
            auto [i,j,d] = q.front(); q.pop();
            if(i==n1 && j==n2 && d==0) return true;
            
            // number token from s1
            if(i<n1 && isdigit(s1[i])){
                for(auto [ni,val]: getNumbers(s1,i)){
                    int nd = d + val;
                    string key = encode(ni,j,nd);
                    if(!vis.count(key)){
                        vis.insert(key);
                        q.emplace(ni,j,nd);
                    }
                }
            }
            // number token from s2
            if(j<n2 && isdigit(s2[j])){
                for(auto [nj,val]: getNumbers(s2,j)){
                    int nd = d - val;
                    string key = encode(i,nj,nd);
                    if(!vis.count(key)){
                        vis.insert(key);
                        q.emplace(i,nj,nd);
                    }
                }
            }
            // both letters with zero diff
            if(i<n1 && j<n2 && isalpha(s1[i]) && isalpha(s2[j]) && d==0){
                if(s1[i]==s2[j]){
                    string key = encode(i+1,j+1,d);
                    if(!vis.count(key)){
                        vis.insert(key);
                        q.emplace(i+1,j+1,d);
                    }
                }
            }
            // consume pending diff with letters
            if(i<n1 && isalpha(s1[i]) && d<0){
                string key = encode(i+1,j,d+1);
                if(!vis.count(key)){
                    vis.insert(key);
                    q.emplace(i+1,j,d+1);
                }
            }
            if(j<n2 && isalpha(s2[j]) && d>0){
                string key = encode(i,j+1,d-1);
                if(!vis.count(key)){
                    vis.insert(key);
                    q.emplace(i,j+1,d-1);
                }
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean possiblyEquals(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        Set<String> visited = new HashSet<>();
        return dfs(0, 0, 0, s1, s2, n, m, visited);
    }

    private boolean dfs(int i, int j, int diff,
                        String s1, String s2, int n, int m,
                        Set<String> visited) {
        String key = i + "," + j + "," + diff;
        if (!visited.add(key)) return false;

        if (i == n && j == m) return diff == 0;

        if (diff > 0) { // extra chars from s1
            if (j < m && Character.isLetter(s2.charAt(j))) {
                if (dfs(i, j + 1, diff - 1, s1, s2, n, m, visited)) return true;
            }
            if (j < m && Character.isDigit(s2.charAt(j))) {
                int val = 0;
                for (int len = 1; len <= 3 && j + len <= m; ++len) {
                    char c = s2.charAt(j + len - 1);
                    if (!Character.isDigit(c)) break;
                    val = val * 10 + (c - '0');
                    if (dfs(i, j + len, diff - val, s1, s2, n, m, visited)) return true;
                }
            }
        } else if (diff < 0) { // extra chars from s2
            if (i < n && Character.isLetter(s1.charAt(i))) {
                if (dfs(i + 1, j, diff + 1, s1, s2, n, m, visited)) return true;
            }
            if (i < n && Character.isDigit(s1.charAt(i))) {
                int val = 0;
                for (int len = 1; len <= 3 && i + len <= n; ++len) {
                    char c = s1.charAt(i + len - 1);
                    if (!Character.isDigit(c)) break;
                    val = val * 10 + (c - '0');
                    if (dfs(i + len, j, diff + val, s1, s2, n, m, visited)) return true;
                }
            }
        } else { // diff == 0
            if (i < n && j < m &&
                Character.isLetter(s1.charAt(i)) && Character.isLetter(s2.charAt(j))) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    if (dfs(i + 1, j + 1, 0, s1, s2, n, m, visited)) return true;
                }
            }
            if (i < n && Character.isDigit(s1.charAt(i))) {
                int val = 0;
                for (int len = 1; len <= 3 && i + len <= n; ++len) {
                    char c = s1.charAt(i + len - 1);
                    if (!Character.isDigit(c)) break;
                    val = val * 10 + (c - '0');
                    if (dfs(i + len, j, diff + val, s1, s2, n, m, visited)) return true;
                }
            }
            if (j < m && Character.isDigit(s2.charAt(j))) {
                int val = 0;
                for (int len = 1; len <= 3 && j + len <= m; ++len) {
                    char c = s2.charAt(j + len - 1);
                    if (!Character.isDigit(c)) break;
                    val = val * 10 + (c - '0');
                    if (dfs(i, j + len, diff - val, s1, s2, n, m, visited)) return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, diff):
            # diff = (expanded length of s1) - (expanded length of s2)
            if i == n1 and j == n2:
                return diff == 0
            # prune impossible large diffs (optional)
            if abs(diff) > 200:  # safe bound given constraints
                return False

            # When one side has extra unmatched characters
            if diff > 0:
                # consume a letter from s2
                if j < n2 and s2[j].isalpha():
                    if dfs(i, j + 1, diff - 1):
                        return True
                # consume a number from s2 (adds to s2 side)
                if j < n2 and s2[j].isdigit():
                    val = 0
                    for k in range(j, min(n2, j + 3)):
                        if not s2[k].isdigit():
                            break
                        val = val * 10 + int(s2[k])
                        if dfs(i, k + 1, diff - val):
                            return True
                return False

            if diff < 0:
                # consume a letter from s1
                if i < n1 and s1[i].isalpha():
                    if dfs(i + 1, j, diff + 1):
                        return True
                # consume a number from s1 (adds to s1 side)
                if i < n1 and s1[i].isdigit():
                    val = 0
                    for k in range(i, min(n1, i + 3)):
                        if not s1[k].isdigit():
                            break
                        val = val * 10 + int(s1[k])
                        if dfs(k + 1, j, diff + val):
                            return True
                return False

            # diff == 0 : need to match next tokens
            # both letters
            if i < n1 and j < n2 and s1[i].isalpha() and s2[j].isalpha():
                if s1[i] == s2[j] and dfs(i + 1, j + 1, 0):
                    return True

            # s1 letter vs s2 number
            if i < n1 and s1[i].isalpha() and j < n2 and s2[j].isdigit():
                val = 0
                for k in range(j, min(n2, j + 3)):
                    if not s2[k].isdigit():
                        break
                    val = val * 10 + int(s2[k])
                    # match the letter with one character of the number
                    new_diff = -(val - 1)
                    if dfs(i + 1, k + 1, new_diff):
                        return True

            # s2 letter vs s1 number
            if j < n2 and s2[j].isalpha() and i < n1 and s1[i].isdigit():
                val = 0
                for k in range(i, min(n1, i + 3)):
                    if not s1[k].isdigit():
                        break
                    val = val * 10 + int(s1[k])
                    new_diff = (val - 1)
                    if dfs(k + 1, j + 1, new_diff):
                        return True

            # both numbers
            if i < n1 and j < n2 and s1[i].isdigit() and s2[j].isdigit():
                val1 = 0
                for p in range(i, min(n1, i + 3)):
                    if not s1[p].isdigit():
                        break
                    val1 = val1 * 10 + int(s1[p])
                    val2 = 0
                    for q in range(j, min(n2, j + 3)):
                        if not s2[q].isdigit():
                            break
                        val2 = val2 * 10 + int(s2[q])
                        if dfs(p + 1, q + 1, val1 - val2):
                            return True

            return False

        return dfs(0, 0, 0)
```

## Python3

```python
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, diff: int) -> bool:
            if i == len(s1) and j == len(s2):
                return diff == 0

            # take a number from s1
            if i < len(s1) and s1[i].isdigit():
                for l in range(1, 4):
                    if i + l <= len(s1) and s1[i:i + l].isdigit():
                        val = int(s1[i:i + l])
                        if dfs(i + l, j, diff + val):
                            return True

            # take a number from s2
            if j < len(s2) and s2[j].isdigit():
                for l in range(1, 4):
                    if j + l <= len(s2) and s2[j:j + l].isdigit():
                        val = int(s2[j:j + l])
                        if dfs(i, j + l, diff - val):
                            return True

            # match letters according to current diff
            if diff > 0:
                # need a letter from s2 to consume one pending char from s1
                if j < len(s2) and s2[j].isalpha():
                    if dfs(i, j + 1, diff - 1):
                        return True
            elif diff < 0:
                # need a letter from s1 to consume one pending char from s2
                if i < len(s1) and s1[i].isalpha():
                    if dfs(i + 1, j, diff + 1):
                        return True
            else:  # diff == 0
                if i < len(s1) and j < len(s2):
                    if s1[i] == s2[j] and s1[i].isalpha():
                        if dfs(i + 1, j + 1, 0):
                            return True

            return False

        return dfs(0, 0, 0)
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

typedef struct Node {
    long long key;
    UT_hash_handle hh;
} Node;

static char *g_s1, *g_s2;
static int g_n1, g_n2;
static Node *visited = NULL;

static bool dfs(int i, int j, int diff) {
    long long enc = ((long long)i << 24) | ((long long)j << 12) | (diff + 1000);
    Node *found;
    HASH_FIND_LL(visited, &enc, sizeof(enc), found);
    if (found) return false;
    found = (Node *)malloc(sizeof(Node));
    found->key = enc;
    HASH_ADD_LL(visited, key, found);

    if (i == g_n1 && j == g_n2) {
        return diff == 0;
    }

    // Process number token in s1
    if (i < g_n1 && isdigit(g_s1[i])) {
        int val = 0, ii = i;
        while (ii < g_n1 && isdigit(g_s1[ii])) {
            val = val * 10 + (g_s1[ii] - '0');
            ii++;
        }
        if (dfs(ii, j, diff + val)) return true;
    }

    // Process number token in s2
    if (j < g_n2 && isdigit(g_s2[j])) {
        int val = 0, jj = j;
        while (jj < g_n2 && isdigit(g_s2[jj])) {
            val = val * 10 + (g_s2[jj] - '0');
            jj++;
        }
        if (dfs(i, jj, diff - val)) return true;
    }

    // Both letters
    if (i < g_n1 && j < g_n2 && isalpha(g_s1[i]) && isalpha(g_s2[j])) {
        if (diff == 0) {
            if (g_s1[i] == g_s2[j]) {
                if (dfs(i + 1, j + 1, 0)) return true;
            }
        } else if (diff > 0) { // extra chars from s1 to match with s2 letter
            if (dfs(i, j + 1, diff - 1)) return true;
        } else { // diff < 0, extra chars from s2 to match with s1 letter
            if (dfs(i + 1, j, diff + 1)) return true;
        }
    }

    // When diff > 0 we can consume a pending char from s1 against a digit token already handled,
    // similarly for diff < 0. No further actions needed here.

    return false;
}

bool possiblyEquals(char* s1, char* s2) {
    g_s1 = s1;
    g_s2 = s2;
    g_n1 = (int)strlen(s1);
    g_n2 = (int)strlen(s2);

    // clear visited hash
    Node *cur, *tmp;
    HASH_ITER(hh, visited, cur, tmp) {
        HASH_DEL(visited, cur);
        free(cur);
    }

    bool res = dfs(0, 0, 0);
    // clean up after call
    HASH_ITER(hh, visited, cur, tmp) {
        HASH_DEL(visited, cur);
        free(cur);
    }
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool PossiblyEquals(string s1, string s2) {
        int n = s1.Length, m = s2.Length;
        var visited = new HashSet<string>();
        
        bool Dfs(int i, int j, int diff) {
            if (i == n && j == m) return diff == 0;
            string key = $"{i},{j},{diff}";
            if (visited.Contains(key)) return false;
            visited.Add(key);
            
            // digits in s1
            if (i < n && Char.IsDigit(s1[i])) {
                int val = 0;
                for (int k = i; k < Math.Min(i + 3, n) && Char.IsDigit(s1[k]); ++k) {
                    val = val * 10 + (s1[k] - '0');
                    if (Dfs(k + 1, j, diff + val)) return true;
                }
            }
            // digits in s2
            if (j < m && Char.IsDigit(s2[j])) {
                int val = 0;
                for (int k = j; k < Math.Min(j + 3, m) && Char.IsDigit(s2[k]); ++k) {
                    val = val * 10 + (s2[k] - '0');
                    if (Dfs(i, k + 1, diff - val)) return true;
                }
            }
            // match letters directly when no pending difference
            if (i < n && j < m && Char.IsLetter(s1[i]) && Char.IsLetter(s2[j])
                && s1[i] == s2[j] && diff == 0) {
                if (Dfs(i + 1, j + 1, diff)) return true;
            }
            // consume a letter from s1 as contribution
            if (i < n && Char.IsLetter(s1[i])) {
                if (Dfs(i + 1, j, diff + 1)) return true;
            }
            // consume a letter from s2 as contribution
            if (j < m && Char.IsLetter(s2[j])) {
                if (Dfs(i, j + 1, diff - 1)) return true;
            }
            return false;
        }
        
        return Dfs(0, 0, 0);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var possiblyEquals = function(s1, s2) {
    const n1 = s1.length, n2 = s2.length;
    const memo = new Set();

    const isLetter = ch => {
        const code = ch.charCodeAt(0);
        return code >= 97 && code <= 122; // a-z
    };
    const isDigit = ch => {
        const code = ch.charCodeAt(0);
        return code >= 48 && code <= 57; // 0-9 (but input has only 1-9)
    };

    function dfs(i, j, diff) {
        const key = i + ',' + j + ',' + diff;
        if (memo.has(key)) return false;
        if (i === n1 && j === n2) return diff === 0;
        memo.add(key);

        // diff > 0 : s1 has extra unmatched characters
        if (diff > 0) {
            if (j < n2) {
                const c = s2[j];
                if (isLetter(c)) {
                    return dfs(i, j + 1, diff - 1);
                } else {
                    let num = 0;
                    for (let k = j; k < Math.min(j + 3, n2); ++k) {
                        const ch = s2[k];
                        if (!isDigit(ch)) break;
                        num = num * 10 + (ch.charCodeAt(0) - 48);
                        if (dfs(i, k + 1, diff - num)) return true;
                    }
                }
            }
        } else if (diff < 0) { // s2 has extra unmatched characters
            if (i < n1) {
                const c = s1[i];
                if (isLetter(c)) {
                    return dfs(i + 1, j, diff + 1);
                } else {
                    let num = 0;
                    for (let k = i; k < Math.min(i + 3, n1); ++k) {
                        const ch = s1[k];
                        if (!isDigit(ch)) break;
                        num = num * 10 + (ch.charCodeAt(0) - 48);
                        if (dfs(k + 1, j, diff + num)) return true;
                    }
                }
            }
        } else { // diff == 0
            if (i < n1 && j < n2) {
                const c1 = s1[i], c2 = s2[j];
                const l1 = isLetter(c1), l2 = isLetter(c2);
                if (l1 && l2) {
                    if (c1 !== c2) return false;
                    return dfs(i + 1, j + 1, 0);
                } else if (!l1 && !l2) { // both numbers
                    let num1 = 0;
                    for (let p = i; p < Math.min(i + 3, n1); ++p) {
                        const ch1 = s1[p];
                        if (!isDigit(ch1)) break;
                        num1 = num1 * 10 + (ch1.charCodeAt(0) - 48);
                        let num2 = 0;
                        for (let q = j; q < Math.min(j + 3, n2); ++q) {
                            const ch2 = s2[q];
                            if (!isDigit(ch2)) break;
                            num2 = num2 * 10 + (ch2.charCodeAt(0) - 48);
                            if (dfs(p + 1, q + 1, num1 - num2)) return true;
                        }
                    }
                } else if (l1 && !l2) { // letter vs number
                    let num = 0;
                    for (let q = j; q < Math.min(j + 3, n2); ++q) {
                        const ch2 = s2[q];
                        if (!isDigit(ch2)) break;
                        num = num * 10 + (ch2.charCodeAt(0) - 48);
                        // match the letter with one of the wildcard chars from number
                        if (dfs(i + 1, q + 1, -(num - 1))) return true;
                    }
                } else { // !l1 && l2 : number vs letter
                    let num = 0;
                    for (let p = i; p < Math.min(i + 3, n1); ++p) {
                        const ch1 = s1[p];
                        if (!isDigit(ch1)) break;
                        num = num * 10 + (ch1.charCodeAt(0) - 48);
                        if (dfs(p + 1, j + 1, num - 1)) return true;
                    }
                }
            } else {
                // one string finished while diff == 0 -> cannot match further
                return false;
            }
        }
        return false;
    }

    return dfs(0, 0, 0);
};
```

## Typescript

```typescript
function possiblyEquals(s1: string, s2: string): boolean {
    const n = s1.length;
    const m = s2.length;
    const memo = new Map<string, boolean>();
    const isDigit = (ch: string) => ch >= '0' && ch <= '9';

    function getNums(str: string, idx: number): Array<[number, number]> {
        const res: Array<[number, number]> = [];
        let val = 0;
        for (let l = 1; l <= 3 && idx + l <= str.length; ++l) {
            const ch = str[idx + l - 1];
            if (!isDigit(ch)) break;
            val = val * 10 + (ch.charCodeAt(0) - 48);
            res.push([val, idx + l]);
        }
        return res;
    }

    function dfs(i: number, j: number, diff: number): boolean {
        const key = `${i},${j},${diff}`;
        if (memo.has(key)) return memo.get(key)!;

        // both strings consumed
        if (i === n && j === m) {
            const ans = diff === 0;
            memo.set(key, ans);
            return ans;
        }

        let ok = false;

        if (diff > 0) { // extra chars from s1 need to be matched by s2
            if (j < m && !isDigit(s2[j])) {
                ok = dfs(i, j + 1, diff - 1);
            } else if (j < m && isDigit(s2[j])) {
                for (const [val, nj] of getNums(s2, j)) {
                    if (dfs(i, nj, diff - val)) { ok = true; break; }
                }
            }
        } else if (diff < 0) { // extra chars from s2 need to be matched by s1
            if (i < n && !isDigit(s1[i])) {
                ok = dfs(i + 1, j, diff + 1);
            } else if (i < n && isDigit(s1[i])) {
                for (const [val, ni] of getNums(s1, i)) {
                    if (dfs(ni, j, diff + val)) { ok = true; break; }
                }
            }
        } else { // diff == 0
            if (i < n && j < m) {
                const c1 = s1[i], c2 = s2[j];
                const d1 = isDigit(c1), d2 = isDigit(c2);
                if (!d1 && !d2) {
                    if (c1 === c2) ok = dfs(i + 1, j + 1, 0);
                } else if (!d1 && d2) {
                    for (const [val, nj] of getNums(s2, j)) {
                        // consume one char from the number to match c1
                        if (dfs(i + 1, nj, -(val - 1))) { ok = true; break; }
                    }
                } else if (d1 && !d2) {
                    for (const [val, ni] of getNums(s1, i)) {
                        // consume one char from the number to match c2
                        if (dfs(ni, j + 1, val - 1)) { ok = true; break; }
                    }
                } else { // both digits
                    const list1 = getNums(s1, i);
                    const list2 = getNums(s2, j);
                    outer: for (const [v1, ni] of list1) {
                        for (const [v2, nj] of list2) {
                            if (dfs(ni, nj, v1 - v2)) { ok = true; break outer; }
                        }
                    }
                }
            }
        }

        memo.set(key, ok);
        return ok;
    }

    return dfs(0, 0, 0);
}
```

## Php

```php
class Solution {
    private $s1;
    private $s2;
    private $n1;
    private $n2;
    private $memo = [];

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function possiblyEquals($s1, $s2) {
        $this->s1 = $s1;
        $this->s2 = $s2;
        $this->n1 = strlen($s1);
        $this->n2 = strlen($s2);
        return $this->dfs(0, 0, 0);
    }

    private function dfs($i, $j, $diff) {
        $key = $i . ',' . $j . ',' . $diff;
        if (isset($this->memo[$key])) {
            return $this->memo[$key];
        }
        // reached end of both strings
        if ($i == $this->n1 && $j == $this->n2) {
            $res = ($diff == 0);
            $this->memo[$key] = $res;
            return $res;
        }

        // diff > 0 : s1 has extra characters to match
        if ($diff > 0) {
            // consume a letter from s2
            if ($j < $this->n2 && ctype_alpha($this->s2[$j])) {
                if ($this->dfs($i, $j + 1, $diff - 1)) {
                    $this->memo[$key] = true;
                    return true;
                }
            }
            // consume a number from s2
            if ($j < $this->n2 && ctype_digit($this->s2[$j])) {
                $val = 0;
                for ($l = 1; $l <= 3 && $j + $l <= $this->n2 && ctype_digit($this->s2[$j + $l - 1]); $l++) {
                    $digit = intval($this->s2[$j + $l - 1]);
                    $val = $val * 10 + $digit;
                    if ($this->dfs($i, $j + $l, $diff - $val)) {
                        $this->memo[$key] = true;
                        return true;
                    }
                }
            }
        } elseif ($diff < 0) { // diff < 0 : s2 has extra characters
            if ($i < $this->n1 && ctype_alpha($this->s1[$i])) {
                if ($this->dfs($i + 1, $j, $diff + 1)) {
                    $this->memo[$key] = true;
                    return true;
                }
            }
            if ($i < $this->n1 && ctype_digit($this->s1[$i])) {
                $val = 0;
                for ($l = 1; $l <= 3 && $i + $l <= $this->n1 && ctype_digit($this->s1[$i + $l - 1]); $l++) {
                    $digit = intval($this->s1[$i + $l - 1]);
                    $val = $val * 10 + $digit;
                    if ($this->dfs($i + $l, $j, $diff + $val)) {
                        $this->memo[$key] = true;
                        return true;
                    }
                }
            }
        } else { // diff == 0
            // both letters
            if ($i < $this->n1 && $j < $this->n2 && ctype_alpha($this->s1[$i]) && ctype_alpha($this->s2[$j])) {
                if ($this->s1[$i] === $this->s2[$j]) {
                    if ($this->dfs($i + 1, $j + 1, 0)) {
                        $this->memo[$key] = true;
                        return true;
                    }
                }
            }
            // s1 letter vs s2 number
            if ($i < $this->n1 && ctype_alpha($this->s1[$i]) && $j < $this->n2 && ctype_digit($this->s2[$j])) {
                $val = 0;
                for ($l = 1; $l <= 3 && $j + $l <= $this->n2 && ctype_digit($this->s2[$j + $l - 1]); $l++) {
                    $digit = intval($this->s2[$j + $l - 1]);
                    $val = $val * 10 + $digit;
                    // one character from s1 matches one of the expanded chars
                    if ($this->dfs($i + 1, $j + $l, -($val - 1))) {
                        $this->memo[$key] = true;
                        return true;
                    }
                }
            }
            // s2 letter vs s1 number
            if ($j < $this->n2 && ctype_alpha($this->s2[$j]) && $i < $this->n1 && ctype_digit($this->s1[$i])) {
                $val = 0;
                for ($l = 1; $l <= 3 && $i + $l <= $this->n1 && ctype_digit($this->s1[$i + $l - 1]); $l++) {
                    $digit = intval($this->s1[$i + $l - 1]);
                    $val = $val * 10 + $digit;
                    if ($this->dfs($i + $l, $j + 1, $val - 1)) {
                        $this->memo[$key] = true;
                        return true;
                    }
                }
            }
            // both numbers
            if ($i < $this->n1 && $j < $this->n2 && ctype_digit($this->s1[$i]) && ctype_digit($this->s2[$j])) {
                $val1 = 0;
                for ($l1 = 1; $l1 <= 3 && $i + $l1 <= $this->n1 && ctype_digit($this->s1[$i + $l1 - 1]); $l1++) {
                    $digit1 = intval($this->s1[$i + $l1 - 1]);
                    $val1 = $val1 * 10 + $digit1;
                    $val2 = 0;
                    for ($l2 = 1; $l2 <= 3 && $j + $l2 <= $this->n2 && ctype_digit($this->s2[$j + $l2 - 1]); $l2++) {
                        $digit2 = intval($this->s2[$j + $l2 - 1]);
                        $val2 = $val2 * 10 + $digit2;
                        if ($this->dfs($i + $l1, $j + $l2, $val1 - $val2)) {
                            $this->memo[$key] = true;
                            return true;
                        }
                    }
                }
            }
        }

        $this->memo[$key] = false;
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func possiblyEquals(_ s1: String, _ s2: String) -> Bool {
        let a1 = Array(s1)
        let a2 = Array(s2)
        var visited = Set<String>()
        
        func isLetter(_ c: Character) -> Bool {
            return c.isLetter
        }
        func isDigit(_ c: Character) -> Bool {
            return c.isNumber
        }
        
        func dfs(_ i: Int, _ j: Int, _ diff: Int) -> Bool {
            let key = "\(i)#\(j)#\(diff)"
            if visited.contains(key) { return false }
            
            if i == a1.count && j == a2.count {
                return diff == 0
            }
            
            // diff > 0 : extra chars from s1 need to be matched by s2
            if diff > 0 {
                // consume a letter from s2
                if j < a2.count && isLetter(a2[j]) {
                    if dfs(i, j + 1, diff - 1) { return true }
                }
                // consume a number from s2 (adds pending chars on s2 side)
                if j < a2.count && isDigit(a2[j]) {
                    var val = 0
                    var k = j
                    while k < a2.count && isDigit(a2[k]) && k - j < 3 {
                        val = val * 10 + Int(String(a2[k]))!
                        if dfs(i, k + 1, diff - val) { return true }
                        k += 1
                    }
                }
            } else if diff < 0 {
                // extra chars from s2 need to be matched by s1
                if i < a1.count && isLetter(a1[i]) {
                    if dfs(i + 1, j, diff + 1) { return true }
                }
                if i < a1.count && isDigit(a1[i]) {
                    var val = 0
                    var k = i
                    while k < a1.count && isDigit(a1[k]) && k - i < 3 {
                        val = val * 10 + Int(String(a1[k]))!
                        if dfs(k + 1, j, diff + val) { return true }
                        k += 1
                    }
                }
            } else { // diff == 0
                // letter vs letter
                if i < a1.count && j < a2.count && isLetter(a1[i]) && isLetter(a2[j]) {
                    if a1[i] == a2[j] && dfs(i + 1, j + 1, 0) { return true }
                }
                // letter vs number
                if i < a1.count && isLetter(a1[i]) && j < a2.count && isDigit(a2[j]) {
                    var val = 0
                    var k = j
                    while k < a2.count && isDigit(a2[k]) && k - j < 3 {
                        val = val * 10 + Int(String(a2[k]))!
                        // consume the letter and use part of the number
                        if dfs(i + 1, k + 1, 1 - val) { return true }
                        k += 1
                    }
                }
                // number vs letter
                if i < a1.count && isDigit(a1[i]) && j < a2.count && isLetter(a2[j]) {
                    var val = 0
                    var k = i
                    while k < a1.count && isDigit(a1[k]) && k - i < 3 {
                        val = val * 10 + Int(String(a1[k]))!
                        if dfs(k + 1, j + 1, val - 1) { return true }
                        k += 1
                    }
                }
                // number vs number
                if i < a1.count && isDigit(a1[i]) && j < a2.count && isDigit(a2[j]) {
                    var p = i
                    while p < a1.count && isDigit(a1[p]) && p - i < 3 {
                        var val1 = 0
                        var q = i
                        // compute val1 for substring i...p
                        for idx in i...p {
                            val1 = val1 * 10 + Int(String(a1[idx]))!
                        }
                        var r = j
                        while r < a2.count && isDigit(a2[r]) && r - j < 3 {
                            var val2 = 0
                            for idx in j...r {
                                val2 = val2 * 10 + Int(String(a2[idx]))!
                            }
                            if dfs(p + 1, r + 1, val1 - val2) { return true }
                            r += 1
                        }
                        p += 1
                    }
                }
            }
            
            visited.insert(key)
            return false
        }
        
        return dfs(0, 0, 0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun possiblyEquals(s1: String, s2: String): Boolean {
        val n1 = s1.length
        val n2 = s2.length
        val visited = HashSet<String>()

        fun dfs(i: Int, j: Int, diff: Int): Boolean {
            val key = "$i,$j,$diff"
            if (!visited.add(key)) return false

            if (i == n1 && j == n2) return diff == 0

            when {
                diff > 0 -> { // s1 has extra unmatched characters
                    if (j < n2 && s2[j].isLetter()) {
                        if (dfs(i, j + 1, diff - 1)) return true
                    }
                    var num = 0
                    var jj = j
                    while (jj < n2 && s2[jj].isDigit()) {
                        num = num * 10 + (s2[jj] - '0')
                        if (dfs(i, jj + 1, diff - num)) return true
                        if (jj - j + 1 >= 3) break
                        jj++
                    }
                }
                diff < 0 -> { // s2 has extra unmatched characters
                    if (i < n1 && s1[i].isLetter()) {
                        if (dfs(i + 1, j, diff + 1)) return true
                    }
                    var num = 0
                    var ii = i
                    while (ii < n1 && s1[ii].isDigit()) {
                        num = num * 10 + (s1[ii] - '0')
                        if (dfs(ii + 1, j, diff + num)) return true
                        if (ii - i + 1 >= 3) break
                        ii++
                    }
                }
                else -> { // diff == 0
                    if (i < n1 && j < n2 && s1[i].isLetter() && s2[j].isLetter()) {
                        if (s1[i] == s2[j]) {
                            if (dfs(i + 1, j + 1, 0)) return true
                        }
                    } else {
                        // s1 digit branch
                        if (i < n1 && s1[i].isDigit()) {
                            var num = 0
                            var ii = i
                            while (ii < n1 && s1[ii].isDigit()) {
                                num = num * 10 + (s1[ii] - '0')
                                if (dfs(ii + 1, j, -num)) return true
                                if (ii - i + 1 >= 3) break
                                ii++
                            }
                        }
                        // s2 digit branch
                        if (j < n2 && s2[j].isDigit()) {
                            var num = 0
                            var jj = j
                            while (jj < n2 && s2[jj].isDigit()) {
                                num = num * 10 + (s2[jj] - '0')
                                if (dfs(i, jj + 1, num)) return true
                                if (jj - j + 1 >= 3) break
                                jj++
                            }
                        }
                    }
                }
            }
            return false
        }

        return dfs(0, 0, 0)
    }

    private fun Char.isLetter(): Boolean = this in 'a'..'z'
    private fun Char.isDigit(): Boolean = this in '0'..'9'
}
```

## Dart

```dart
class Solution {
  bool possiblyEquals(String s1, String s2) {
    int n1 = s1.length;
    int n2 = s2.length;
    Set<String> memo = {};

    bool isLetter(String str, int idx) {
      int code = str.codeUnitAt(idx);
      return code >= 97 && code <= 122; // 'a'..'z'
    }

    bool dfs(int i, int j, int diff) {
      String key = '$i,$j,$diff';
      if (memo.contains(key)) return false;
      memo.add(key);

      if (i == n1 && j == n2) return diff == 0;

      // s1 has extra pending characters
      if (diff > 0) {
        if (j >= n2) return false;
        if (isLetter(s2, j)) {
          if (dfs(i, j + 1, diff - 1)) return true;
        }
        int val = 0;
        for (int k = j; k < n2 && k - j < 3 && !isLetter(s2, k); ++k) {
          val = val * 10 + (s2.codeUnitAt(k) - 48);
          if (dfs(i, k + 1, diff - val)) return true;
        }
        return false;
      }

      // s2 has extra pending characters
      if (diff < 0) {
        if (i >= n1) return false;
        if (isLetter(s1, i)) {
          if (dfs(i + 1, j, diff + 1)) return true;
        }
        int val = 0;
        for (int k = i; k < n1 && k - i < 3 && !isLetter(s1, k); ++k) {
          val = val * 10 + (s1.codeUnitAt(k) - 48);
          if (dfs(k + 1, j, diff + val)) return true;
        }
        return false;
      }

      // diff == 0
      if (i < n1 && j < n2 && isLetter(s1, i) && isLetter(s2, j) && s1[i] == s2[j]) {
        if (dfs(i + 1, j + 1, 0)) return true;
      }

      // number from s1
      if (i < n1 && !isLetter(s1, i)) {
        int val = 0;
        for (int k = i; k < n1 && k - i < 3 && !isLetter(s1, k); ++k) {
          val = val * 10 + (s1.codeUnitAt(k) - 48);
          if (dfs(k + 1, j, diff + val)) return true;
        }
      }

      // number from s2
      if (j < n2 && !isLetter(s2, j)) {
        int val = 0;
        for (int k = j; k < n2 && k - j < 3 && !isLetter(s2, k); ++k) {
          val = val * 10 + (s2.codeUnitAt(k) - 48);
          if (dfs(i, k + 1, diff - val)) return true;
        }
      }

      return false;
    }

    return dfs(0, 0, 0);
  }
}
```

## Golang

```go
func possiblyEquals(s1 string, s2 string) bool {
	type key struct {
		i, j, d int
	}
	n1, n2 := len(s1), len(s2)
	isLetter := func(c byte) bool { return c >= 'a' && c <= 'z' }
	memo := make(map[key]bool)

	var dfs func(i, j, diff int) bool
	dfs = func(i, j, diff int) bool {
		if i == n1 && j == n2 && diff == 0 {
			return true
		}
		k := key{i, j, diff}
		if _, ok := memo[k]; ok {
			return false
		}

		// Helper to parse numbers up to length 3
		parseNums := func(s string, start int) []struct{ val, nxt int } {
			res := []struct{ val, nxt int }{}
			val := 0
			for p := start; p < len(s) && p-start < 3 && !isLetter(s[p]); p++ {
				val = val*10 + int(s[p]-'0')
				res = append(res, struct{ val, nxt int }{val, p + 1})
			}
			return res
		}

		if diff > 0 { // s1 has extra unmatched chars to be consumed by s2
			if j < n2 {
				if isLetter(s2[j]) {
					if dfs(i, j+1, diff-1) {
						return true
					}
				} else {
					for _, p := range parseNums(s2, j) {
						if dfs(i, p.nxt, diff-p.val) {
							return true
						}
					}
				}
			}
		} else if diff < 0 { // s2 has extra unmatched chars to be consumed by s1
			if i < n1 {
				if isLetter(s1[i]) {
					if dfs(i+1, j, diff+1) {
						return true
					}
				} else {
					for _, p := range parseNums(s1, i) {
						if dfs(p.nxt, j, diff+p.val) {
							return true
						}
					}
				}
			}
		} else { // diff == 0, need to match next tokens
			// letter vs letter
			if i < n1 && j < n2 && isLetter(s1[i]) && isLetter(s2[j]) {
				if s1[i] == s2[j] && dfs(i+1, j+1, 0) {
					return true
				}
			}
			// letter vs number
			if i < n1 && isLetter(s1[i]) && j < n2 && !isLetter(s2[j]) {
				for _, p := range parseNums(s2, j) {
					if dfs(i+1, p.nxt, -(p.val-1)) {
						return true
					}
				}
			}
			if j < n2 && isLetter(s2[j]) && i < n1 && !isLetter(s1[i]) {
				for _, p := range parseNums(s1, i) {
					if dfs(p.nxt, j+1, p.val-1) {
						return true
					}
				}
			}
			// number vs number
			if i < n1 && !isLetter(s1[i]) && j < n2 && !isLetter(s2[j]) {
				nums1 := parseNums(s1, i)
				nums2 := parseNums(s2, j)
				for _, a := range nums1 {
					for _, b := range nums2 {
						if dfs(a.nxt, b.nxt, a.val-b.val) {
							return true
						}
					}
				}
			}
		}

		memo[k] = false
		return false
	}

	return dfs(0, 0, 0)
}
```

## Ruby

```ruby
def possibly_equals(s1, s2)
  @s1 = s1
  @s2 = s2
  @n1 = s1.length
  @n2 = s2.length
  @vis = {}
  dfs(0, 0, 0)
end

def dfs(i, j, diff)
  return true if i == @n1 && j == @n2 && diff == 0
  key = [i, j, diff]
  return false if @vis[key]
  @vis[key] = true

  # helper lambdas for character checks
  letter = ->(b) { b >= 97 && b <= 122 }
  digit  = ->(b) { b >= 48 && b <= 57 }

  if diff > 0
    # need to consume from s2
    if j < @n2
      b = @s2.getbyte(j)
      if letter.call(b)
        return true if dfs(i, j + 1, diff - 1)
      elsif digit.call(b)
        val = 0
        (j...[[@n2, j + 3].min]).each do |k|
          bk = @s2.getbyte(k)
          break unless digit.call(bk)
          val = val * 10 + (bk - 48)
          return true if dfs(i, k + 1, diff - val)
        end
      end
    end
  elsif diff < 0
    # need to consume from s1
    if i < @n1
      b = @s1.getbyte(i)
      if letter.call(b)
        return true if dfs(i + 1, j, diff + 1)
      elsif digit.call(b)
        val = 0
        (i...[[@n1, i + 3].min]).each do |k|
          bk = @s1.getbyte(k)
          break unless digit.call(bk)
          val = val * 10 + (bk - 48)
          return true if dfs(k + 1, j, diff + val)
        end
      end
    end
  else # diff == 0
    # both letters
    if i < @n1 && j < @n2
      b1 = @s1.getbyte(i)
      b2 = @s2.getbyte(j)
      if letter.call(b1) && letter.call(b2) && b1 == b2
        return true if dfs(i + 1, j + 1, 0)
      end
    end

    # s1 letter vs s2 number
    if i < @n1 && j < @n2
      b1 = @s1.getbyte(i)
      b2 = @s2.getbyte(j)
      if letter.call(b1) && digit.call(b2)
        val = 0
        (j...[[@n2, j + 3].min]).each do |k|
          bk = @s2.getbyte(k)
          break unless digit.call(bk)
          val = val * 10 + (bk - 48)
          # after matching one letter, remaining diff is 1 - val
          return true if dfs(i + 1, k + 1, 1 - val)
        end
      end
    end

    # s1 number vs s2 letter
    if i < @n1 && j < @n2
      b1 = @s1.getbyte(i)
      b2 = @s2.getbyte(j)
      if digit.call(b1) && letter.call(b2)
        val = 0
        (i...[[@n1, i + 3].min]).each do |k|
          bk = @s1.getbyte(k)
          break unless digit.call(bk)
          val = val * 10 + (bk - 48)
          # after matching one letter, remaining diff is val - 1
          return true if dfs(k + 1, j + 1, val - 1)
        end
      end
    end

    # both numbers
    if i < @n1 && j < @n2
      b1 = @s1.getbyte(i)
      b2 = @s2.getbyte(j)
      if digit.call(b1) && digit.call(b2)
        val1 = 0
        (i...[[@n1, i + 3].min]).each do |k|
          bk1 = @s1.getbyte(k)
          break unless digit.call(bk1)
          val1 = val1 * 10 + (bk1 - 48)

          val2 = 0
          (j...[[@n2, j + 3].min]).each do |l|
            bk2 = @s2.getbyte(l)
            break unless digit.call(bk2)
            val2 = val2 * 10 + (bk2 - 48)
            return true if dfs(k + 1, l + 1, val1 - val2)
          end
        end
      end
    end
  end

  false
end
```

## Scala

```scala
object Solution {
  def possiblyEquals(s1: String, s2: String): Boolean = {
    val n1 = s1.length
    val n2 = s2.length
    import scala.collection.mutable.{Set => MutSet}
    val visited = MutSet[(Int, Int, Int)]()

    def parseNum(str: String, idx: Int): (Int, Int) = {
      var i = idx
      var num = 0
      while (i < str.length && str(i).isDigit) {
        num = num * 10 + (str(i) - '0')
        i += 1
      }
      (num, i)
    }

    def dfs(i: Int, j: Int, diff: Int): Boolean = {
      if (i == n1 && j == n2) return diff == 0
      val key = (i, j, diff)
      if (visited.contains(key)) return false

      if (diff > 0) {
        // s1 has extra unmatched characters to be consumed by s2
        if (j < n2 && s2(j).isLetter) {
          if (dfs(i, j + 1, diff - 1)) return true
        }
        if (j < n2 && s2(j).isDigit) {
          val (num, nj) = parseNum(s2, j)
          if (dfs(i, nj, diff - num)) return true
        }
      } else if (diff < 0) {
        // s2 has extra unmatched characters to be consumed by s1
        if (i < n1 && s1(i).isLetter) {
          if (dfs(i + 1, j, diff + 1)) return true
        }
        if (i < n1 && s1(i).isDigit) {
          val (num, ni) = parseNum(s1, i)
          if (dfs(ni, j, diff + num)) return true
        }
      } else { // diff == 0
        // both letters
        if (i < n1 && j < n2 && s1(i).isLetter && s2(j).isLetter) {
          if (s1(i) == s2(j) && dfs(i + 1, j + 1, 0)) return true
        }
        // s1 letter vs s2 number
        if (i < n1 && s1(i).isLetter && j < n2 && s2(j).isDigit) {
          val (num, nj) = parseNum(s2, j)
          if (dfs(i + 1, nj, -(num - 1))) return true
        }
        // s1 number vs s2 letter
        if (i < n1 && s1(i).isDigit && j < n2 && s2(j).isLetter) {
          val (num, ni) = parseNum(s1, i)
          if (dfs(ni, j + 1, num - 1)) return true
        }
        // both numbers
        if (i < n1 && s1(i).isDigit && j < n2 && s2(j).isDigit) {
          val (num1, ni) = parseNum(s1, i)
          val (num2, nj) = parseNum(s2, j)
          if (dfs(ni, nj, num1 - num2)) return true
        }
      }

      visited.add(key)
      false
    }

    dfs(0, 0, 0)
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn possibly_equals(s1: String, s2: String) -> bool {
        fn dfs(
            i: usize,
            j: usize,
            diff: i32,
            a: &[u8],
            b: &[u8],
            memo: &mut HashSet<(usize, usize, i32)>,
        ) -> bool {
            let n = a.len();
            let m = b.len();

            if i == n && j == m {
                return diff == 0;
            }
            if !memo.insert((i, j, diff)) {
                return false;
            }

            if diff > 0 {
                // need to consume from b
                if j >= m {
                    return false;
                }
                if b[j].is_ascii_digit() {
                    let mut val: i32 = 0;
                    let mut k = j;
                    while k < m && b[k].is_ascii_digit() {
                        val = val * 10 + (b[k] - b'0') as i32;
                        k += 1;
                        if dfs(i, k, diff - val, a, b, memo) {
                            return true;
                        }
                    }
                } else {
                    // consume one concrete character from b
                    if dfs(i, j + 1, diff - 1, a, b, memo) {
                        return true;
                    }
                }
            } else if diff < 0 {
                // need to consume from a
                if i >= n {
                    return false;
                }
                if a[i].is_ascii_digit() {
                    let mut val: i32 = 0;
                    let mut k = i;
                    while k < n && a[k].is_ascii_digit() {
                        val = val * 10 + (a[k] - b'0') as i32;
                        k += 1;
                        if dfs(k, j, diff + val, a, b, memo) {
                            return true;
                        }
                    }
                } else {
                    // consume one concrete character from a
                    if dfs(i + 1, j, diff + 1, a, b, memo) {
                        return true;
                    }
                }
            } else {
                // diff == 0
                // try number from a
                if i < n && a[i].is_ascii_digit() {
                    let mut val: i32 = 0;
                    let mut k = i;
                    while k < n && a[k].is_ascii_digit() {
                        val = val * 10 + (a[k] - b'0') as i32;
                        k += 1;
                        if dfs(k, j, diff + val, a, b, memo) {
                            return true;
                        }
                    }
                }
                // try number from b
                if j < m && b[j].is_ascii_digit() {
                    let mut val: i32 = 0;
                    let mut k = j;
                    while k < m && b[k].is_ascii_digit() {
                        val = val * 10 + (b[k] - b'0') as i32;
                        k += 1;
                        if dfs(i, k, diff - val, a, b, memo) {
                            return true;
                        }
                    }
                }
                // both letters
                if i < n && j < m && !a[i].is_ascii_digit() && !b[j].is_ascii_digit() {
                    if a[i] == b[j] {
                        if dfs(i + 1, j + 1, 0, a, b, memo) {
                            return true;
                        }
                    } else {
                        return false;
                    }
                }
            }

            false
        }

        let bytes1 = s1.as_bytes();
        let bytes2 = s2.as_bytes();
        let mut memo: HashSet<(usize, usize, i32)> = HashSet::new();
        dfs(0, 0, 0, bytes1, bytes2, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (possibly-equals s1 s2)
  (-> string? string? boolean?)
  (let* ((n1 (string-length s1))
         (n2 (string-length s2))
         (memo (make-hash)))
    (define (char-numeric? c)
      (and (char>=? c #\0) (char<=? c #\9)))
    (define (dfs i j diff)
      (let ((key (list i j diff)))
        (if (hash-has-key? memo key)
            (hash-ref memo key)
            (let ((res
                   (cond
                     [(and (= i n1) (= j n2) (= diff 0)) #t]
                     [(> diff 0)
                      (if (= j n2)
                          #f
                          (let ((c (string-ref s2 j)))
                            (if (char-numeric? c)
                                (for/or ([len (in-range 1 (min 3 (- n2 j)) + 1)])
                                  (define num (string->number (substring s2 j (+ j len))))
                                  (and num (dfs i (+ j len) (+ diff num))))
                                (dfs i (add1 j) (sub1 diff)))) )]
                     [(< diff 0)
                      (if (= i n1)
                          #f
                          (let ((c (string-ref s1 i)))
                            (if (char-numeric? c)
                                (for/or ([len (in-range 1 (min 3 (- n1 i)) + 1)])
                                  (define num (string->number (substring s1 i (+ i len))))
                                  (and num (dfs (+ i len) j (+ diff num))))
                                (dfs (add1 i) j (add1 diff)))) )]
                     [else ; diff == 0
                      (cond
                        [(and (= i n1) (= j n2)) #t]
                        [(= i n1) #f]
                        [(= j n2) #f]
                        [else
                         (let ((c1 (string-ref s1 i))
                               (c2 (string-ref s2 j)))
                           (cond
                             [(and (char-alphabetic? c1) (char-alphabetic? c2))
                              (if (char=? c1 c2)
                                  (dfs (add1 i) (add1 j) 0)
                                  #f)]
                             [(char-numeric? c1)
                              (for/or ([len (in-range 1 (min 3 (- n1 i)) + 1)])
                                (define num (string->number (substring s1 i (+ i len))))
                                (and num (dfs (+ i len) j num)))]
                             [(char-numeric? c2)
                              (for/or ([len (in-range 1 (min 3 (- n2 j)) + 1)])
                                (define num (string->number (substring s2 j (+ j len))))
                                (and num (dfs i (+ j len) (- num))))]
                             [else #f]))])]))))
              (hash-set! memo key res)
              res)))))
    (dfs 0 0 0)))
```

## Erlang

```erlang
-module(solution).
-export([possibly_equals/2]).

-spec possibly_equals(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
possibly_equals(S1, S2) ->
    Tokens1List = tokenize(binary_to_list(S1)),
    Tokens2List = tokenize(binary_to_list(S2)),
    T1 = list_to_tuple(Tokens1List),
    T2 = list_to_tuple(Tokens2List),
    Size1 = tuple_size(T1),
    Size2 = tuple_size(T2),
    {Result, _} = dfs(0, 0, 0, T1, T2, Size1, Size2, #{}),
    Result.

%% Tokenization: returns list of {letter, Char} or {num, Value}
tokenize([]) -> [];
tokenize([C|Rest]) when C >= $0, C =< $9 ->
    {NumDigitsRev, RestAfter} = take_digits([C|Rest], []),
    Number = list_to_integer(lists:reverse(NumDigitsRev)),
    [{num, Number} | tokenize(RestAfter)];
tokenize([C|Rest]) ->
    [{letter, C} | tokenize(Rest)].

take_digits([C|Rest], Acc) when C >= $0, C =< $9 ->
    take_digits(Rest, [C|Acc]);
take_digits(Other, Acc) -> {Acc, Other}.

%% Depth‑first search with memoization
dfs(I, J, Diff, T1, T2, Size1, Size2, Memo) ->
    case maps:get({I,J,Diff}, Memo, undefined) of
        true -> {true, Memo};
        false -> {false, Memo};
        undefined ->
            Result =
                if I =:= Size1, J =:= Size2, Diff =:= 0 ->
                        true;
                   true ->
                        NextStates = next_states(I, J, Diff, T1, T2, Size1, Size2),
                        try_next(NextStates, T1, T2, Size1, Size2, Memo)
                end,
            NewMemo = maps:put({I,J,Diff}, Result, Memo),
            {Result, NewMemo}
    end.

try_next([], _T1, _T2, _S1, _S2, Memo) -> {false, Memo};
try_next([{NI,NJ,ND}|Rest], T1, T2, S1, S2, Memo) ->
    case dfs(NI, NJ, ND, T1, T2, S1, S2, Memo) of
        {true, NewMemo} -> {true, NewMemo};
        {false, NewMemo} -> try_next(Rest, T1, T2, S1, S2, NewMemo)
    end.

next_states(I, J, Diff, T1, T2, Size1, Size2) when Diff > 0 ->
    if J >= Size2 -> [];
       true ->
            Tok2 = get_token(J, T2, Size2),
            case Tok2 of
                {letter,_} -> [{I, J+1, Diff-1}];
                {num,N}   -> [{I, J+1, Diff - N}]
            end
    end;
next_states(I, J, Diff, T1, T2, Size1, Size2) when Diff < 0 ->
    if I >= Size1 -> [];
       true ->
            Tok1 = get_token(I, T1, Size1),
            case Tok1 of
                {letter,_} -> [{I+1, J, Diff+1}];
                {num,N}   -> [{I+1, J, Diff + N}]
            end
    end;
next_states(I, J, 0, T1, T2, Size1, Size2) ->
    case {I >= Size1, J >= Size2} of
        {true, true} -> []; % base case handled earlier
        _ ->
            Tok1 = if I < Size1 -> get_token(I, T1, Size1); true -> undefined end,
            Tok2 = if J < Size2 -> get_token(J, T2, Size2); true -> undefined end,
            case {Tok1, Tok2} of
                {undefined,_} -> [];
                {_,undefined} -> [];
                {{letter,C1},{letter,C2}} ->
                    if C1 =:= C2 -> [{I+1,J+1,0}] else [] end;
                {{letter,_},{num,N}} ->
                    [{I+1,J+1, -(N-1)}];
                {{num,N},{letter,_}} ->
                    [{I+1,J+1, N-1}];
                {{num,N1},{num,N2}} ->
                    [{I+1,J+1, N1 - N2}]
            end
    end.

get_token(Index, Tuple, Size) when Index < Size ->
    element(Index + 1, Tuple);
get_token(_, _, _) -> undefined.
```

## Elixir

```elixir
defmodule Solution do
  @spec possibly_equals(s1 :: String.t(), s2 :: String.t()) :: boolean()
  def possibly_equals(s1, s2) do
    c1 = String.to_charlist(s1)
    c2 = String.to_charlist(s2)
    {res, _} = dfs(0, 0, 0, c1, c2, %{})
    res
  end

  # core DFS with memoization
  defp dfs(i, j, diff, c1, c2, memo) do
    key = {i, j, diff}

    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        len1 = length(c1)
        len2 = length(c2)

        cond do
          i == len1 and j == len2 ->
            result = diff == 0
            {result, Map.put(memo, key, result)}

          true ->
            {ok, new_memo} = explore(i, j, diff, c1, c2, memo)
            {ok, Map.put(new_memo, key, ok)}
        end
    end
  end

  # explore possible moves from current state
  defp explore(i, j, diff, c1, c2, memo) do
    len1 = length(c1)
    len2 = length(c2)

    cond do
      diff > 0 ->
        if j >= len2 do
          {false, memo}
        else
          ch = Enum.at(c2, j)

          if ch in ?a..?z do
            dfs(i, j + 1, diff - 1, c1, c2, memo)
          else
            nums = numbers(c2, j)
            try_consume_numbers(nums, i, j, diff, :s2, c1, c2, memo)
          end
        end

      diff < 0 ->
        if i >= len1 do
          {false, memo}
        else
          ch = Enum.at(c1, i)

          if ch in ?a..?z do
            dfs(i + 1, j, diff + 1, c1, c2, memo)
          else
            nums = numbers(c1, i)
            try_consume_numbers(nums, i, j, diff, :s1, c1, c2, memo)
          end
        end

      true ->
        if i >= len1 or j >= len2 do
          {false, memo}
        else
          ch1 = Enum.at(c1, i)
          ch2 = Enum.at(c2, j)

          cond do
            ch1 in ?a..?z and ch2 in ?a..?z ->
              if ch1 == ch2,
                do: dfs(i + 1, j + 1, 0, c1, c2, memo),
                else: {false, memo}

            ch1 in ?a..?z and not (ch2 in ?a..?z) ->
              nums = numbers(c2, j)

              Enum.reduce_while(nums, {false, memo}, fn {v, nj}, {_b, m} ->
                {ok, new_m} = dfs(i + 1, nj, -v, c1, c2, m)
                if ok, do: {:halt, {true, new_m}}, else: {:cont, {false, new_m}}
              end)

            not (ch1 in ?a..?z) and ch2 in ?a..?z ->
              nums = numbers(c1, i)

              Enum.reduce_while(nums, {false, memo}, fn {v, ni}, {_b, m} ->
                {ok, new_m} = dfs(ni, j + 1, v, c1, c2, m)
                if ok, do: {:halt, {true, new_m}}, else: {:cont, {false, new_m}}
              end)

            true ->
              nums1 = numbers(c1, i)
              nums2 = numbers(c2, j)

              Enum.reduce_while(nums1, {false, memo}, fn {v1, ni}, {_b, m} ->
                res =
                  Enum.reduce_while(nums2, {false, m}, fn {v2, nj}, {_b2, m2} ->
                    {ok, new_m2} = dfs(ni, nj, v1 - v2, c1, c2, m2)
                    if ok, do: {:halt, {true, new_m2}}, else: {:cont, {false, new_m2}}
                  end)

                case res do
                  {true, _} -> {:halt, res}
                  {false, m3} -> {:cont, {false, m3}}
                end
              end)
          end
        end
    end
  end

  # consume a number when we have a pending diff
  defp try_consume_numbers(nums, i, j, diff, side, c1, c2, memo) do
    Enum.reduce_while(nums, {false, memo}, fn {v, npos}, {_b, m} ->
      case side do
        :s2 ->
          {ok, new_m} = dfs(i, npos, diff - v, c1, c2, m)

        :s1 ->
          {ok, new_m} = dfs(npos, j, diff + v, c1, c2, m)
      end

      if ok, do: {:halt, {true, new_m}}, else: {:cont, {false, new_m}}
    end)
  end

  # generate possible numbers (up to 3 digits) starting at idx
  defp numbers(chars, idx) do
    max_len = min(3, length(chars) - idx)

    Enum.reduce_while(1..max_len, [], fn l, acc ->
      slice = Enum.slice(chars, idx, l)

      if Enum.all?(slice, &(&1 in ?0..?9)) do
        val = Enum.reduce(slice, 0, fn d, a -> a * 10 + (d - ?0) end)
        {:cont, [{val, idx + l} | acc]}
      else
        {:cont, acc}
      end
    end)
    |> Enum.reverse()
  end
end
```
