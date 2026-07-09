# 3455. Shortest Matching Substring

## Cpp

```cpp
class Solution {
public:
    vector<int> kmp(const string& s, const string& pat) {
        int n = s.size(), m = pat.size();
        if (m == 0) {
            vector<int> all(n + 1);
            iota(all.begin(), all.end(), 0);
            return all;
        }
        vector<int> lps(m, 0);
        for (int i = 1, len = 0; i < m;) {
            if (pat[i] == pat[len]) {
                lps[i++] = ++len;
            } else if (len) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        vector<int> res;
        for (int i = 0, j = 0; i < n;) {
            if (s[i] == pat[j]) {
                ++i; ++j;
                if (j == m) {
                    res.push_back(i - j);
                    j = lps[j - 1];
                }
            } else {
                if (j) j = lps[j - 1];
                else ++i;
            }
        }
        return res;
    }

    int shortestMatchingSubstring(string s, string p) {
        int n = s.size();
        size_t firstStar = p.find('*');
        size_t secondStar = p.find('*', firstStar + 1);
        string a = p.substr(0, firstStar);
        string b = p.substr(firstStar + 1, secondStar - firstStar - 1);
        string c = p.substr(secondStar + 1);

        vector<int> posA = kmp(s, a);
        vector<int> posB = kmp(s, b);
        vector<int> posC = kmp(s, c);

        const int INF = 1e9;
        int ans = INF;

        if (a.empty()) {
            for (int i = 0; i <= n; ++i) {
                int endA = i;
                auto itb = lower_bound(posB.begin(), posB.end(), endA);
                if (itb == posB.end()) continue;
                int k = *itb;
                int endB = k + b.size();
                auto itc = lower_bound(posC.begin(), posC.end(), endB);
                if (itc == posC.end()) continue;
                int l = *itc;
                int len = (l + c.size()) - i;
                ans = min(ans, len);
            }
        } else {
            for (int i : posA) {
                int endA = i + a.size();
                auto itb = lower_bound(posB.begin(), posB.end(), endA);
                if (itb == posB.end()) continue;
                int k = *itb;
                int endB = k + b.size();
                auto itc = lower_bound(posC.begin(), posC.end(), endB);
                if (itc == posC.end()) continue;
                int l = *itc;
                int len = (l + c.size()) - i;
                ans = min(ans, len);
            }
        }

        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int shortestMatchingSubstring(String s, String p) {
        int first = p.indexOf('*');
        int second = p.indexOf('*', first + 1);
        String a = p.substring(0, first);
        String b = p.substring(first + 1, second);
        String c = p.substring(second + 1);
        int lenA = a.length(), lenB = b.length(), lenC = c.length();
        int totalFixed = lenA + lenB + lenC;
        if (totalFixed > s.length()) return -1;

        List<Integer> occA = getOccurrences(s, a);
        List<Integer> occB = getOccurrences(s, b);
        List<Integer> occC = getOccurrences(s, c);

        if ((lenA > 0 && occA.isEmpty()) ||
            (lenB > 0 && occB.isEmpty()) ||
            (lenC > 0 && occC.isEmpty())) {
            return -1;
        }

        int ans = Integer.MAX_VALUE;
        for (int start : occA) {
            if (start + lenA > s.length()) continue;
            int idxB = lowerBound(occB, start + lenA);
            if (idxB == -1) continue;
            int bStart = occB.get(idxB);
            int idxC = lowerBound(occC, bStart + lenB);
            if (idxC == -1) continue;
            int cStart = occC.get(idxC);
            int length = (cStart + lenC) - start;
            if (length < ans) {
                ans = length;
                if (ans == totalFixed) break; // cannot get shorter
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    private static List<Integer> getOccurrences(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        List<Integer> res = new ArrayList<>();
        if (m == 0) {
            for (int i = 0; i <= n; i++) res.add(i);
            return res;
        }
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m;) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                lps[i++] = ++len;
            } else {
                if (len != 0) len = lps[len - 1];
                else lps[i++] = 0;
            }
        }
        for (int i = 0, j = 0; i < n;) {
            if (text.charAt(i) == pattern.charAt(j)) {
                i++; j++;
                if (j == m) {
                    res.add(i - m);
                    j = lps[j - 1];
                }
            } else {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
        return res;
    }

    private static int lowerBound(List<Integer> list, int target) {
        int lo = 0, hi = list.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid) < target) lo = mid + 1;
            else hi = mid;
        }
        return lo < list.size() ? lo : -1;
    }
}
```

## Python

```python
class Solution(object):
    def shortestMatchingSubstring(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: int
        """
        n = len(s)
        # split pattern into three parts a * b * c
        first = p.find('*')
        second = p.find('*', first + 1)
        a = p[:first]
        b = p[first + 1:second]
        c = p[second + 1:]

        # if all three are empty, empty substring matches
        if not a and not b and not c:
            return 0

        INF = n + 5

        def kmp_find(text, pattern):
            m = len(pattern)
            if m == 0:
                return []
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            res = []
            i = j = 0
            N = len(text)
            while i < N:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                    if j == m:
                        res.append(i - j)
                        j = lps[j - 1]
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return res

        def build_nxt(segment):
            seg_len = len(segment)
            if seg_len == 0:
                # matches at every position
                return None  # indicate trivial match
            occ = kmp_find(s, segment)
            match = [False] * n
            for pos in occ:
                match[pos] = True
            nxt = [INF] * (n + 2)
            for i in range(n, -1, -1):
                if i <= n - seg_len and match[i]:
                    nxt[i] = i
                else:
                    nxt[i] = nxt[i + 1]
            return nxt

        nxt_a = build_nxt(a)
        nxt_b = build_nxt(b)
        nxt_c = build_nxt(c)

        len_a, len_b, len_c = len(a), len(b), len(c)
        ans = INF

        for start_idx in range(0, n + 1):
            # position of a
            if nxt_a is None:
                pos_a = start_idx
            else:
                pos_a = nxt_a[start_idx]
                if pos_a == INF:
                    break  # no further a possible, can stop early
            after_a = pos_a + len_a
            if after_a > n:
                continue

            # position of b
            if nxt_b is None:
                pos_b = after_a
            else:
                pos_b = nxt_b[after_a]
                if pos_b == INF:
                    continue
            after_b = pos_b + len_b
            if after_b > n:
                continue

            # position of c
            if nxt_c is None:
                pos_c = after_b
            else:
                pos_c = nxt_c[after_b]
                if pos_c == INF:
                    continue
            end_pos = pos_c + len_c
            if end_pos > n:
                continue

            cur_len = end_pos - pos_a
            if cur_len < ans:
                ans = cur_len

        return -1 if ans == INF else ans
```

## Python3

```python
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        n = len(s)
        # split pattern into three parts a * b * c
        first_star = p.find('*')
        second_star = p.find('*', first_star + 1)
        a = p[:first_star]
        b = p[first_star + 1:second_star]
        c = p[second_star + 1:]

        la, lb, lc = len(a), len(b), len(c)

        def kmp_occurrences(text: str, pat: str):
            if not pat:
                return list(range(len(text) + 1))
            m = len(pat)
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j and pat[i] != pat[j]:
                    j = lps[j - 1]
                if pat[i] == pat[j]:
                    j += 1
                    lps[i] = j
            res = []
            j = 0
            for i, ch in enumerate(text):
                while j and ch != pat[j]:
                    j = lps[j - 1]
                if ch == pat[j]:
                    j += 1
                    if j == m:
                        res.append(i - m + 1)
                        j = lps[j - 1]
            return res

        A = kmp_occurrences(s, a)
        B = kmp_occurrences(s, b)
        C = kmp_occurrences(s, c)

        INF = 10 ** 9
        # best_a_up_to[i] = minimal start of a whose end <= i
        best_a_up_to = [INF] * (n + 1)
        for st in A:
            end = st + la
            if end <= n:
                if st < best_a_up_to[end]:
                    best_a_up_to[end] = st
        cur_min = INF
        for i in range(n + 1):
            if best_a_up_to[i] < cur_min:
                cur_min = best_a_up_to[i]
            best_a_up_to[i] = cur_min

        # next_c_start[pos] = minimal start of c >= pos
        next_c_start = [INF] * (n + 2)
        for st in C:
            if st <= n:
                if st < next_c_start[st]:
                    next_c_start[st] = st
        cur = INF
        for i in range(n, -1, -1):
            if next_c_start[i] < cur:
                cur = next_c_start[i]
            next_c_start[i] = cur

        ans = INF
        for sb in B:
            a_start = best_a_up_to[sb]
            if a_start == INF:
                continue
            pos_c_needed = sb + lb
            if pos_c_needed > n:
                continue
            c_start = next_c_start[pos_c_needed]
            if c_start == INF:
                continue
            total_len = (c_start + lc) - a_start
            if total_len < ans:
                ans = total_len

        return -1 if ans == INF else ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static void buildLPS(const string &pat, vector<int> &lps) {
    int m = pat.size();
    lps.assign(m, 0);
    for (int i = 1, len = 0; i < m; ) {
        if (pat[i] == pat[len]) {
            lps[i++] = ++len;
        } else if (len) {
            len = lps[len - 1];
        } else {
            lps[i++] = 0;
        }
    }
}

static vector<char> kmpOccurrences(const string &text, const string &pat) {
    int n = text.size(), m = pat.size();
    vector<char> occ(n + 1, 0); // occ[i]=1 if pat occurs starting at i
    if (m == 0) { // empty pattern matches everywhere including at position n
        fill(occ.begin(), occ.end(), 1);
        return occ;
    }
    if (m > n) return occ;
    vector<int> lps;
    buildLPS(pat, lps);
    for (int i = 0, j = 0; i < n; ) {
        if (text[i] == pat[j]) {
            ++i; ++j;
            if (j == m) {
                occ[i - m] = 1;
                j = lps[j - 1];
            }
        } else if (j) {
            j = lps[j - 1];
        } else {
            ++i;
        }
    }
    return occ;
}

int shortestMatchingSubstring(char* s, char* p) {
    string S(s), P(p);
    int n = S.size();

    // split pattern into A * B * C
    size_t firstStar = P.find('*');
    size_t secondStar = P.find('*', firstStar + 1);
    string A = P.substr(0, firstStar);
    string B = P.substr(firstStar + 1, secondStar - firstStar - 1);
    string C = P.substr(secondStar + 1);

    int lenA = A.size(), lenB = B.size(), lenC = C.size();

    // occurrences
    vector<char> occA = kmpOccurrences(S, A);
    vector<char> occB = kmpOccurrences(S, B);
    vector<char> occC = kmpOccurrences(S, C);

    const int INF = n + 5;
    vector<int> nextB(n + 2, INF), nextC(n + 2, INF);
    // build next arrays from right to left
    for (int i = n; i >= 0; --i) {
        if (occB[i]) nextB[i] = i;
        else nextB[i] = nextB[i + 1];
        if (occC[i]) nextC[i] = i;
        else nextC[i] = nextC[i + 1];
    }

    int answer = INF;

    for (int i = 0; i <= n; ++i) {
        if (!occA[i]) continue;
        int posAfterA = i + lenA;
        if (posAfterA > n) continue;
        int j = nextB[posAfterA];
        if (j == INF) continue;
        int posAfterB = j + lenB;
        if (posAfterB > n) continue;
        int k = nextC[posAfterB];
        if (k == INF) continue;
        int endPos = k + lenC;
        if (endPos > n) continue;
        answer = min(answer, endPos - i);
    }

    return (answer == INF) ? -1 : answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int ShortestMatchingSubstring(string s, string p) {
        int firstStar = p.IndexOf('*');
        int secondStar = p.IndexOf('*', firstStar + 1);
        string a = p.Substring(0, firstStar);
        string b = p.Substring(firstStar + 1, secondStar - firstStar - 1);
        string c = p.Substring(secondStar + 1);

        int n = s.Length;
        const int INF = 1000000007;

        int[] nextB = BuildNext(s, b);
        int[] nextC = BuildNext(s, c);

        int ans = INF;

        if (a.Length == 0) {
            // start can be at any position up to the beginning of segment B
            if (b.Length == 0) {
                for (int i = 0; i <= n; i++) {
                    int posC = nextC[i];
                    if (posC == INF) continue;
                    int len = (posC + c.Length) - i;
                    if (len < ans) ans = len;
                }
            } else {
                List<int> occB = GetOccurrences(s, b);
                foreach (int posB in occB) {
                    int afterB = posB + b.Length;
                    int posC = nextC[afterB];
                    if (posC == INF) continue;
                    int len = (posC + c.Length) - posB; // start at posB
                    if (len < ans) ans = len;
                }
            }
        } else {
            List<int> occA = GetOccurrences(s, a);
            foreach (int i in occA) {
                int afterA = i + a.Length;
                int posB = nextB[afterA];
                if (posB == INF) continue;
                int afterB = posB + b.Length;
                int posC = nextC[afterB];
                if (posC == INF) continue;
                int len = (posC + c.Length) - i;
                if (len < ans) ans = len;
            }
        }

        return ans == INF ? -1 : ans;
    }

    private int[] BuildNext(string s, string pat) {
        int n = s.Length;
        const int INF = 1000000007;
        int[] nxt = new int[n + 1];
        if (pat.Length == 0) {
            for (int i = 0; i <= n; i++) nxt[i] = i;
            return nxt;
        }
        List<int> occ = GetOccurrences(s, pat);
        int j = 0;
        for (int i = 0; i <= n; i++) {
            while (j < occ.Count && occ[j] < i) j++;
            if (j < occ.Count) nxt[i] = occ[j];
            else nxt[i] = INF;
        }
        return nxt;
    }

    private List<int> GetOccurrences(string text, string pat) {
        List<int> res = new List<int>();
        int n = text.Length, m = pat.Length;
        if (m == 0) {
            for (int i = 0; i <= n; i++) res.Add(i);
            return res;
        }
        // build LPS array
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m;) {
            if (pat[i] == pat[len]) {
                lps[i++] = ++len;
            } else if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        // KMP search
        for (int i = 0, j = 0; i < n;) {
            if (text[i] == pat[j]) {
                i++; j++;
                if (j == m) {
                    res.Add(i - j);
                    j = lps[j - 1];
                }
            } else {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @return {number}
 */
var shortestMatchingSubstring = function(s, p) {
    const n = s.length;
    const idx1 = p.indexOf('*');
    const idx2 = p.indexOf('*', idx1 + 1);
    const A = p.slice(0, idx1);
    const B = p.slice(idx1 + 1, idx2);
    const C = p.slice(idx2 + 1);
    const lenA = A.length, lenB = B.length, lenC = C.length;
    const INF = n + 5;

    // KMP to find all start positions where pattern occurs in text
    function kmpSearch(text, pattern) {
        const m = pattern.length;
        const res = new Array(n).fill(false);
        if (m === 0) return res;
        const lps = new Array(m).fill(0);
        for (let i = 1, len = 0; i < m;) {
            if (pattern[i] === pattern[len]) {
                lps[i++] = ++len;
            } else if (len !== 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        let i = 0, j = 0;
        while (i < n) {
            if (text[i] === pattern[j]) {
                i++; j++;
                if (j === m) {
                    const start = i - m;
                    res[start] = true;
                    j = lps[j - 1];
                }
            } else if (j !== 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
        return res;
    }

    const matchA = lenA > 0 ? kmpSearch(s, A) : null;
    const matchB = lenB > 0 ? kmpSearch(s, B) : null;
    const matchC = lenC > 0 ? kmpSearch(s, C) : null;

    function buildNext(match, len) {
        const nxt = new Array(n + 2);
        if (len === 0) {
            for (let i = 0; i <= n; ++i) nxt[i] = i;
            return nxt;
        }
        nxt[n] = INF;
        for (let i = n - 1; i >= 0; --i) {
            if (i <= n - len && match[i]) nxt[i] = i;
            else nxt[i] = nxt[i + 1];
        }
        return nxt;
    }

    const nextA = buildNext(matchA, lenA);
    const nextB = buildNext(matchB, lenB);
    const nextC = buildNext(matchC, lenC);

    let ans = INF;
    for (let a = 0; a <= n; ++a) {
        if (lenA > 0 && (a > n - lenA || !matchA[a])) continue;
        const bPos = nextB[a + lenA];
        if (bPos > n) continue;
        const cPos = nextC[bPos + lenB];
        if (cPos > n) continue;
        const length = (cPos + lenC) - a;
        if (length < ans) ans = length;
    }

    return ans === INF ? -1 : ans;
};
```

## Typescript

```typescript
function shortestMatchingSubstring(s: string, p: string): number {
    const n = s.length;
    // split pattern into three parts a * b * c
    const stars = [];
    for (let i = 0; i < p.length; ++i) if (p[i] === '*') stars.push(i);
    const a = p.slice(0, stars[0]);
    const b = p.slice(stars[0] + 1, stars[1]);
    const c = p.slice(stars[1] + 1);

    // KMP to get all start positions of pattern (non‑empty)
    function kmpOccurrences(text: string, pat: string): number[] {
        if (pat.length === 0) {
            const res: number[] = [];
            for (let i = 0; i <= text.length; ++i) res.push(i);
            return res;
        }
        const m = pat.length;
        const lps = new Array(m).fill(0);
        // build LPS
        for (let i = 1, len = 0; i < m;) {
            if (pat[i] === pat[len]) {
                lps[i++] = ++len;
            } else if (len) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        const res: number[] = [];
        for (let i = 0, j = 0; i < text.length;) {
            if (text[i] === pat[j]) {
                ++i; ++j;
                if (j === m) {
                    res.push(i - m);
                    j = lps[j - 1];
                }
            } else if (j) {
                j = lps[j - 1];
            } else {
                ++i;
            }
        }
        return res;
    }

    const A = kmpOccurrences(s, a);
    const B = kmpOccurrences(s, b);
    const C = kmpOccurrences(s, c);

    // prepare nextC array: earliest start of c at or after position i
    const INF = Number.MAX_SAFE_INTEGER;
    const isCStart = new Array(n + 1).fill(false);
    if (c.length === 0) {
        for (let i = 0; i <= n; ++i) isCStart[i] = true;
    } else {
        for (const pos of C) isCStart[pos] = true;
    }
    const nextC = new Array(n + 2).fill(INF);
    // nextC[n] = c empty ? n : INF already set
    for (let i = n; i >= 0; --i) {
        if (isCStart[i]) nextC[i] = i;
        else nextC[i] = nextC[i + 1];
    }

    function lowerBound(arr: number[], target: number): number {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    }

    const la = a.length, lb = b.length, lc = c.length;
    let ans = INF;

    for (const i of A) {
        // find earliest b start >= i+la
        const idxB = lowerBound(B, i + la);
        if (idxB === B.length) continue;
        const bPos = B[idxB];
        const needCStart = bPos + lb;
        if (needCStart > n) continue;
        const cPos = nextC[needCStart];
        if (cPos === INF) continue;
        const len = (cPos + lc) - i;
        if (len < ans) ans = len;
    }

    return ans === INF ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Integer
     */
    function shortestMatchingSubstring($s, $p) {
        // split pattern into three parts a * b * c
        $firstStar = strpos($p, '*');
        $secondStar = strpos($p, '*', $firstStar + 1);
        $a = substr($p, 0, $firstStar);
        $b = substr($p, $firstStar + 1, $secondStar - $firstStar - 1);
        $c = substr($p, $secondStar + 1);

        // collect non‑empty segments in order
        $segments = [];
        if ($a !== '') $segments[] = ['str' => $a, 'len' => strlen($a)];
        if ($b !== '') $segments[] = ['str' => $b, 'len' => strlen($b)];
        if ($c !== '') $segments[] = ['str' => $c, 'len' => strlen($c)];

        // no required literals -> empty substring matches
        if (count($segments) === 0) return 0;

        // compute occurrences for each non‑empty segment using KMP
        $occurrences = [];
        foreach ($segments as $seg) {
            $occ = $this->kmpSearch($s, $seg['str']);
            if (empty($occ)) return -1;   // required part never appears
            $occurrences[] = $occ;
        }

        $INF = PHP_INT_MAX;

        if (count($segments) === 1) {
            // shortest substring is exactly this segment
            return $segments[0]['len'];
        }

        if (count($segments) === 2) {
            $len1 = $segments[0]['len'];
            $len2 = $segments[1]['len'];
            $occ1 = $occurrences[0];
            $occ2 = $occurrences[1];

            $ptr1 = 0;
            $bestPos1 = null;
            $ans = $INF;

            foreach ($occ2 as $pos2) {
                while ($ptr1 < count($occ1) && $occ1[$ptr1] + $len1 <= $pos2) {
                    $bestPos1 = $occ1[$ptr1];
                    $ptr1++;
                }
                if ($bestPos1 !== null) {
                    $ans = min($ans, ($pos2 + $len2) - $bestPos1);
                }
            }
            return $ans === $INF ? -1 : $ans;
        }

        // count == 3
        $lenA = $segments[0]['len'];
        $lenB = $segments[1]['len'];
        $lenC = $segments[2]['len'];
        $occA = $occurrences[0];
        $occB = $occurrences[1];
        $occC = $occurrences[2];

        $ptrA = 0;
        $bestI = null;   // latest start of A that ends before current B
        $ptrC = 0;
        $ans = $INF;

        foreach ($occB as $posB) {
            while ($ptrA < count($occA) && $occA[$ptrA] + $lenA <= $posB) {
                $bestI = $occA[$ptrA];
                $ptrA++;
            }
            if ($bestI === null) continue; // no preceding A

            $needC = $posB + $lenB;
            while ($ptrC < count($occC) && $occC[$ptrC] < $needC) {
                $ptrC++;
            }
            if ($ptrC == count($occC)) break; // no further C possible

            $k = $occC[$ptrC];
            $ans = min($ans, ($k + $lenC) - $bestI);
        }

        return $ans === $INF ? -1 : $ans;
    }

    /**
     * KMP search: returns all start indices where $pattern occurs in $text.
     *
     * @param string $text
     * @param string $pattern
     * @return array
     */
    private function kmpSearch($text, $pattern) {
        $n = strlen($text);
        $m = strlen($pattern);
        if ($m == 0) return [];

        // build LPS (longest proper prefix which is also suffix) array
        $lps = array_fill(0, $m, 0);
        $len = 0;
        for ($i = 1; $i < $m; $i++) {
            while ($len > 0 && $pattern[$i] !== $pattern[$len]) {
                $len = $lps[$len - 1];
            }
            if ($pattern[$i] === $pattern[$len]) {
                $len++;
                $lps[$i] = $len;
            } else {
                $lps[$i] = 0;
            }
        }

        // search
        $res = [];
        $j = 0; // index in pattern
        for ($i = 0; $i < $n; $i++) {
            while ($j > 0 && $text[$i] !== $pattern[$j]) {
                $j = $lps[$j - 1];
            }
            if ($text[$i] === $pattern[$j]) {
                $j++;
                if ($j == $m) {
                    $res[] = $i - $m + 1;
                    $j = $lps[$j - 1];
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func shortestMatchingSubstring(_ s: String, _ p: String) -> Int {
        let sBytes = Array(s.utf8)
        let pBytes = Array(p.utf8)
        var starPos: [Int] = []
        for (i, ch) in pBytes.enumerated() {
            if ch == 42 { // '*'
                starPos.append(i)
            }
        }
        let i1 = starPos[0]
        let i2 = starPos[1]
        let aPat = Array(pBytes[0..<i1])
        let bPat = Array(pBytes[(i1 + 1)..<i2])
        let cPat = Array(pBytes[(i2 + 1)..<pBytes.count])

        // all three empty
        if aPat.isEmpty && bPat.isEmpty && cPat.isEmpty {
            return 0
        }

        func computeLPS(_ pat: [UInt8]) -> [Int] {
            var lps = [Int](repeating: 0, count: pat.count)
            var length = 0
            var i = 1
            while i < pat.count {
                if pat[i] == pat[length] {
                    length += 1
                    lps[i] = length
                    i += 1
                } else {
                    if length != 0 {
                        length = lps[length - 1]
                    } else {
                        lps[i] = 0
                        i += 1
                    }
                }
            }
            return lps
        }

        func kmpSearch(_ pat: [UInt8], _ text: [UInt8]) -> [Int] {
            if pat.isEmpty { return [] }
            let lps = computeLPS(pat)
            var res: [Int] = []
            var i = 0, j = 0
            while i < text.count {
                if pat[j] == text[i] {
                    i += 1; j += 1
                    if j == pat.count {
                        res.append(i - j)
                        j = lps[j - 1]
                    }
                } else {
                    if j != 0 {
                        j = lps[j - 1]
                    } else {
                        i += 1
                    }
                }
            }
            return res
        }

        let occA = aPat.isEmpty ? [] : kmpSearch(aPat, sBytes)
        let occB = bPat.isEmpty ? [] : kmpSearch(bPat, sBytes)
        let occC = cPat.isEmpty ? [] : kmpSearch(cPat, sBytes)

        let n = sBytes.count
        let lenA = aPat.count
        let lenB = bPat.count
        let lenC = cPat.count

        // Case when middle segment is non‑empty
        if !bPat.isEmpty {
            var answer = Int.max
            // prepare nextC array: smallest start of C >= pos
            var nextC = [Int](repeating: Int.max, count: n + 2)
            if cPat.isEmpty {
                for i in 0...n { nextC[i] = i }
            } else {
                for start in occC {
                    nextC[start] = start
                }
                var best = Int.max
                for i in stride(from: n, through: 0, by: -1) {
                    if nextC[i] != Int.max { best = nextC[i] }
                    else { nextC[i] = best }
                }
            }

            var idxA = 0
            var curMinA = Int.max

            for startB in occB {
                // update preceding A occurrences that end before or at startB
                if !aPat.isEmpty {
                    while idxA < occA.count && occA[idxA] + lenA <= startB {
                        curMinA = min(curMinA, occA[idxA])
                        idxA += 1
                    }
                }

                let startA: Int
                if aPat.isEmpty {
                    startA = startB   // can start exactly at B
                } else {
                    if curMinA == Int.max { continue }
                    startA = curMinA
                }

                let limitC = startB + lenB
                if limitC > n { continue }
                let startC = nextC[limitC]
                if startC == Int.max { continue }

                let length = (startC + lenC) - startA
                if length < answer { answer = length }
            }

            return answer == Int.max ? -1 : answer
        } else {
            // Middle segment empty: need only A and C
            if aPat.isEmpty && cPat.isEmpty {
                return 0
            }
            if aPat.isEmpty {
                // Only C matters
                return lenC
            }
            if cPat.isEmpty {
                // Only A matters
                return lenA
            }

            var answer = Int.max
            for startA in occA {
                let limit = startA + lenA
                // binary search lower bound in occC
                var l = 0, r = occC.count
                while l < r {
                    let m = (l + r) >> 1
                    if occC[m] < limit { l = m + 1 } else { r = m }
                }
                if l < occC.count {
                    let startC = occC[l]
                    let length = (startC + lenC) - startA
                    if length < answer { answer = length }
                }
            }
            return answer == Int.max ? -1 : answer
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestMatchingSubstring(s: String, p: String): Int {
        val n = s.length
        // split pattern into three parts a * b * c
        val firstStar = p.indexOf('*')
        val secondStar = p.indexOf('*', firstStar + 1)
        val a = p.substring(0, firstStar)
        val b = p.substring(firstStar + 1, secondStar)
        val c = p.substring(secondStar + 1)

        val lenA = a.length
        val lenB = b.length
        val lenC = c.length

        // KMP search for non‑empty segments
        fun kmpSearch(text: String, pattern: String): BooleanArray {
            val m = pattern.length
            val res = BooleanArray(text.length) { false }
            if (m == 0) return res
            val lps = IntArray(m)
            var len = 0
            var i = 1
            while (i < m) {
                if (pattern[i] == pattern[len]) {
                    len++
                    lps[i] = len
                    i++
                } else {
                    if (len != 0) {
                        len = lps[len - 1]
                    } else {
                        lps[i] = 0
                        i++
                    }
                }
            }
            var ti = 0
            var pi = 0
            while (ti < text.length) {
                if (text[ti] == pattern[pi]) {
                    ti++; pi++
                    if (pi == m) {
                        res[ti - m] = true
                        pi = lps[pi - 1]
                    }
                } else {
                    if (pi != 0) {
                        pi = lps[pi - 1]
                    } else {
                        ti++
                    }
                }
            }
            return res
        }

        val matchA = if (lenA == 0) BooleanArray(n + 1) { true } else kmpSearch(s, a)
        val matchB = if (lenB == 0) BooleanArray(n + 1) { true } else kmpSearch(s, b)
        val matchC = if (lenC == 0) BooleanArray(n + 1) { true } else kmpSearch(s, c)

        // build next occurrence arrays
        val INF = n + 5
        fun buildNext(matches: BooleanArray, segLen: Int): IntArray {
            val nxt = IntArray(n + 2) { INF }
            if (segLen == 0) {
                for (i in 0..n) nxt[i] = i
                return nxt
            }
            nxt[n] = INF
            for (i in n - 1 downTo 0) {
                nxt[i] = if (matches[i]) i else nxt[i + 1]
            }
            return nxt
        }

        val nextA = buildNext(matchA, lenA)
        val nextB = buildNext(matchB, lenB)
        val nextC = buildNext(matchC, lenC)

        var answer = INF

        if (lenA == 0) {
            for (startA in 0..n) {
                val afterA = startA
                val startB = nextB[afterA]
                if (startB > n) continue
                val afterB = startB + lenB
                if (afterB > n) continue
                val startC = nextC[afterB]
                if (startC > n) continue
                val finalEnd = if (lenC > 0) startC + lenC else afterB
                if (finalEnd <= n) {
                    answer = kotlin.math.min(answer, finalEnd - startA)
                }
            }
        } else {
            for (startA in 0 until n) {
                if (!matchA[startA]) continue
                val afterA = startA + lenA
                if (afterA > n) continue
                val startB = nextB[afterA]
                if (startB > n) continue
                val afterB = startB + lenB
                if (afterB > n) continue
                val startC = nextC[afterB]
                if (startC > n) continue
                val finalEnd = if (lenC > 0) startC + lenC else afterB
                if (finalEnd <= n) {
                    answer = kotlin.math.min(answer, finalEnd - startA)
                }
            }
        }

        return if (answer == INF) -1 else answer
    }
}
```

## Dart

```dart
class Solution {
  int shortestMatchingSubstring(String s, String p) {
    int n = s.length;
    // Split pattern into three parts a * b * c
    int firstStar = p.indexOf('*');
    int secondStar = p.indexOf('*', firstStar + 1);
    String a = p.substring(0, firstStar);
    String b = p.substring(firstStar + 1, secondStar);
    String c = p.substring(secondStar + 1);

    // Helper: KMP to find all occurrences of pattern in text
    List<int> kmpSearch(String text, String pat) {
      if (pat.isEmpty) return [];
      int n = text.length;
      int m = pat.length;
      List<int> lps = List.filled(m, 0);
      // build LPS array
      for (int i = 1, len = 0; i < m;) {
        if (pat[i] == pat[len]) {
          len++;
          lps[i] = len;
          i++;
        } else {
          if (len != 0) {
            len = lps[len - 1];
          } else {
            lps[i] = 0;
            i++;
          }
        }
      }
      List<int> occ = [];
      int i = 0, j = 0;
      while (i < n) {
        if (text[i] == pat[j]) {
          i++;
          j++;
          if (j == m) {
            occ.add(i - j);
            j = lps[j - 1];
          }
        } else {
          if (j != 0) {
            j = lps[j - 1];
          } else {
            i++;
          }
        }
      }
      return occ;
    }

    const int INF = 1 << 60;

    // bestLeft[pos] = latest start index of a such that it ends <= pos
    List<int> bestLeft = List.filled(n + 1, -1);
    if (a.isEmpty) {
      for (int i = 0; i <= n; ++i) bestLeft[i] = i;
    } else {
      List<int> occA = kmpSearch(s, a);
      int idx = 0;
      int last = -1;
      int lenA = a.length;
      for (int pos = 0; pos <= n; ++pos) {
        while (idx < occA.length && occA[idx] + lenA <= pos) {
          last = occA[idx];
          idx++;
        }
        bestLeft[pos] = last;
      }
    }

    // bestRight[pos] = earliest start index of c such that it starts >= pos
    List<int> bestRight = List.filled(n + 1, INF);
    if (c.isEmpty) {
      for (int i = 0; i <= n; ++i) bestRight[i] = i;
    } else {
      List<int> occC = kmpSearch(s, c);
      int idx = occC.length - 1;
      int next = INF;
      for (int pos = n; pos >= 0; --pos) {
        while (idx >= 0 && occC[idx] >= pos) {
          next = occC[idx];
          idx--;
        }
        bestRight[pos] = next;
      }
    }

    int ans = INF;
    int lenB = b.length;

    if (b.isEmpty) {
      for (int j = 0; j <= n; ++j) {
        int i = bestLeft[j];
        if (i == -1) continue;
        int k = bestRight[j]; // pos after empty b is j
        if (k == INF) continue;
        int curLen = (k + c.length) - i;
        if (curLen < ans) ans = curLen;
      }
    } else {
      List<int> occB = kmpSearch(s, b);
      for (int j in occB) {
        int i = bestLeft[j];
        if (i == -1) continue;
        int afterB = j + lenB;
        if (afterB > n) continue;
        int k = bestRight[afterB];
        if (k == INF) continue;
        int curLen = (k + c.length) - i;
        if (curLen < ans) ans = curLen;
      }
    }

    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func shortestMatchingSubstring(s string, p string) int {
    // split pattern into three parts a * b * c
    first := -1
    second := -1
    for i := 0; i < len(p); i++ {
        if p[i] == '*' {
            if first == -1 {
                first = i
            } else {
                second = i
                break
            }
        }
    }
    a := p[:first]
    b := p[first+1 : second]
    c := p[second+1:]

    n := len(s)

    // helper to find all occurrences (including empty pattern)
    findOccurrences := func(text, pat string) []int {
        if len(pat) == 0 {
            res := make([]int, len(text)+1)
            for i := 0; i <= len(text); i++ {
                res[i] = i
            }
            return res
        }
        m := len(pat)
        // build lps array
        lps := make([]int, m)
        length := 0
        for i := 1; i < m; {
            if pat[i] == pat[length] {
                length++
                lps[i] = length
                i++
            } else {
                if length != 0 {
                    length = lps[length-1]
                } else {
                    lps[i] = 0
                    i++
                }
            }
        }
        // KMP search
        res := []int{}
        i, j := 0, 0
        for i < len(text) {
            if text[i] == pat[j] {
                i++
                j++
                if j == m {
                    res = append(res, i-j)
                    j = lps[j-1]
                }
            } else {
                if j != 0 {
                    j = lps[j-1]
                } else {
                    i++
                }
            }
        }
        return res
    }

    occA := findOccurrences(s, a)
    occB := findOccurrences(s, b)
    occC := findOccurrences(s, c)

    // mark starts for B and C
    isB := make([]bool, n+1)
    for _, pos := range occB {
        if pos <= n {
            isB[pos] = true
        }
    }
    isC := make([]bool, n+1)
    for _, pos := range occC {
        if pos <= n {
            isC[pos] = true
        }
    }

    const INF = int(1e9)
    nextB := make([]int, n+2) // extra slot for simplicity
    nextC := make([]int, n+2)

    // build next arrays from right to left
    nxt := INF
    for i := n; i >= 0; i-- {
        if isB[i] {
            nxt = i
        }
        nextB[i] = nxt
    }
    nxt = INF
    for i := n; i >= 0; i-- {
        if isC[i] {
            nxt = i
        }
        nextC[i] = nxt
    }

    ans := INF
    lenA, lenB, lenC := len(a), len(b), len(c)

    for _, startA := range occA {
        posAfterA := startA + lenA
        if posAfterA > n {
            continue
        }
        startB := nextB[posAfterA]
        if startB == INF || startB+lenB > n {
            continue
        }
        posAfterB := startB + lenB
        if posAfterB > n {
            continue
        }
        startC := nextC[posAfterB]
        if startC == INF || startC+lenC > n {
            continue
        }
        length := (startC + lenC) - startA
        if length < ans {
            ans = length
        }
    }

    if ans == INF {
        return -1
    }
    return ans
}
```

## Ruby

```ruby
def shortest_matching_substring(s, p)
  # split pattern into three parts A * B * C
  parts = p.split('*')
  a_str, b_str, c_str = parts[0], parts[1], parts[2]

  n = s.length
  s_bytes = s.bytes

  len_a = a_str.length
  len_b = b_str.length
  len_c = c_str.length

  # KMP search returning start indices
  kmp_search = lambda do |text, pat|
    m = pat.length
    return [] if m == 0
    ntxt = text.length
    lps = Array.new(m, 0)
    len = 0
    i = 1
    while i < m
      if pat[i] == pat[len]
        len += 1
        lps[i] = len
        i += 1
      else
        if len != 0
          len = lps[len - 1]
        else
          lps[i] = 0
          i += 1
        end
      end
    end

    res = []
    i = 0
    j = 0
    while i < ntxt
      if text[i] == pat[j]
        i += 1
        j += 1
        if j == m
          res << (i - j)
          j = lps[j - 1]
        end
      else
        if j != 0
          j = lps[j - 1]
        else
          i += 1
        end
      end
    end
    res
  end

  # occurrence arrays (true where segment matches)
  occ_a = Array.new(n + 1, false)
  occ_b = Array.new(n + 1, false)
  occ_c = Array.new(n + 1, false)

  if len_a == 0
    (0..n).each { |i| occ_a[i] = true }
  else
    kmp_search.call(s_bytes, a_str.bytes).each { |pos| occ_a[pos] = true }
  end

  if len_b == 0
    (0..n).each { |i| occ_b[i] = true }
  else
    kmp_search.call(s_bytes, b_str.bytes).each { |pos| occ_b[pos] = true }
  end

  if len_c == 0
    (0..n).each { |i| occ_c[i] = true }
  else
    kmp_search.call(s_bytes, c_str.bytes).each { |pos| occ_c[pos] = true }
  end

  inf = n + 1
  next_a = Array.new(n + 2, inf)
  next_b = Array.new(n + 2, inf)
  next_c = Array.new(n + 2, inf)

  i = n
  while i >= 0
    next_a[i] = occ_a[i] ? i : next_a[i + 1]
    next_b[i] = occ_b[i] ? i : next_b[i + 1]
    next_c[i] = occ_c[i] ? i : next_c[i + 1]
    i -= 1
  end

  answer = inf
  (0..n).each do |start|
    a_start = next_a[start]
    next if a_start == inf
    b_pos = a_start + len_a
    b_start = next_b[b_pos]
    next if b_start == inf
    c_pos = b_start + len_b
    c_start = next_c[c_pos]
    next if c_start == inf
    length = (c_start + len_c) - start
    answer = length if length < answer
  end

  answer == inf ? -1 : answer
end
```

## Scala

```scala
object Solution {
  def shortestMatchingSubstring(s: String, p: String): Int = {
    val n = s.length
    // split pattern into three parts a * b * c
    val firstStar = p.indexOf('*')
    val secondStar = p.indexOf('*', firstStar + 1)
    val a = p.substring(0, firstStar)
    val b = p.substring(firstStar + 1, secondStar)
    val c = p.substring(secondStar + 1)

    if (a.isEmpty && b.isEmpty && c.isEmpty) return 0

    // KMP to find all occurrences of pattern in text
    def kmpSearch(text: String, pat: String): Array[Int] = {
      if (pat.isEmpty) return Array.emptyIntArray
      val n = text.length
      val m = pat.length
      val lps = new Array[Int](m)
      var len = 0
      var i = 1
      while (i < m) {
        if (pat.charAt(i) == pat.charAt(len)) {
          len += 1
          lps(i) = len
          i += 1
        } else {
          if (len != 0) {
            len = lps(len - 1)
          } else {
            lps(i) = 0
            i += 1
          }
        }
      }
      val buf = scala.collection.mutable.ArrayBuffer[Int]()
      var ti = 0
      var pi = 0
      while (ti < n) {
        if (text.charAt(ti) == pat.charAt(pi)) {
          ti += 1
          pi += 1
          if (pi == m) {
            buf += (ti - m)
            pi = lps(pi - 1)
          }
        } else {
          if (pi != 0) pi = lps(pi - 1)
          else ti += 1
        }
      }
      buf.toArray
    }

    // occurrence flags for each part
    def occFlags(part: String): Array[Boolean] = {
      val flag = new Array[Boolean](n + 1)
      if (part.isEmpty) java.util.Arrays.fill(flag, true)
      else {
        val starts = kmpSearch(s, part)
        var idx = 0
        while (idx < starts.length) {
          flag(starts(idx)) = true
          idx += 1
        }
      }
      flag
    }

    val occA = occFlags(a)
    val occB = occFlags(b)
    val occC = occFlags(c)

    val INF = n + 5

    // next occurrence arrays
    def buildNext(flag: Array[Boolean]): Array[Int] = {
      val nxt = new Array[Int](n + 2)
      nxt(n) = if (flag(n)) n else INF
      var i = n - 1
      while (i >= 0) {
        nxt(i) = if (flag(i)) i else nxt(i + 1)
        i -= 1
      }
      nxt
    }

    val nextB = buildNext(occB)
    val nextC = buildNext(occC)

    var ans = Int.MaxValue
    val aLen = a.length
    val bLen = b.length
    val cLen = c.length

    var i = 0
    while (i <= n) {
      if (occA(i)) {
        val afterA = i + aLen
        if (afterA <= n) {
          val j = nextB(afterA)
          if (j <= n) {
            val afterB = j + bLen
            if (afterB <= n) {
              val k = nextC(afterB)
              if (k <= n) {
                val len = (k + cLen) - i
                if (len < ans) ans = len
              }
            }
          }
        }
      }
      i += 1
    }

    if (ans == Int.MaxValue) -1 else ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_matching_substring(s: String, p: String) -> i32 {
        let s_bytes = s.as_bytes();
        let n = s_bytes.len();

        // split pattern into three parts
        let parts: Vec<&str> = p.split('*').collect(); // exactly 3 parts
        let a = parts[0].as_bytes();
        let b = parts[1].as_bytes();
        let c = parts[2].as_bytes();

        // KMP matcher returning start positions as bool vector
        fn kmp_match(text: &[u8], pat: &[u8]) -> Vec<bool> {
            let n = text.len();
            let m = pat.len();
            if m == 0 {
                return vec![true; n + 1];
            }
            // build lps
            let mut lps = vec![0usize; m];
            let mut len = 0usize;
            for i in 1..m {
                while len > 0 && pat[i] != pat[len] {
                    len = lps[len - 1];
                }
                if pat[i] == pat[lens] {
                    len += 1;
                    lps[i] = len;
                }
            }
            // search
            let mut res = vec![false; n];
            let mut i = 0usize;
            let mut j = 0usize;
            while i < n {
                while j > 0 && text[i] != pat[j] {
                    j = lps[j - 1];
                }
                if text[i] == pat[j] {
                    j += 1;
                }
                if j == m {
                    res[i + 1 - m] = true;
                    j = lps[j - 1];
                }
                i += 1;
            }
            res
        }

        // build next occurrence array for a segment
        fn build_next(matches: &Vec<bool>, seg_len: usize, n: usize) -> Vec<usize> {
            let mut next = vec![usize::MAX; n + 1];
            for i in (0..=n).rev() {
                if i + seg_len <= n && matches[i] {
                    next[i] = i;
                } else if i + 1 <= n {
                    next[i] = next[i + 1];
                }
            }
            next
        }

        // match vectors and next arrays for each part
        let (match_a, next_a) = if a.is_empty() {
            (vec![true; n + 1], (0..=n).collect())
        } else {
            let m = kmp_match(s_bytes, a);
            let nxt = build_next(&m, a.len(), n);
            (m, nxt)
        };
        let (match_b, next_b) = if b.is_empty() {
            (vec![true; n + 1], (0..=n).collect())
        } else {
            let m = kmp_match(s_bytes, b);
            let nxt = build_next(&m, b.len(), n);
            (m, nxt)
        };
        let (match_c, next_c) = if c.is_empty() {
            (vec![true; n + 1], (0..=n).collect())
        } else {
            let m = kmp_match(s_bytes, c);
            let nxt = build_next(&m, c.len(), n);
            (m, nxt)
        };

        let la = a.len();
        let lb = b.len();
        let lc = c.len();

        let mut ans = usize::MAX;

        // iterate over possible start positions x
        for x in 0..=n {
            // check if segment a matches at x (if non‑empty)
            if la > 0 {
                if x + la > n || !match_a[x] {
                    continue;
                }
            } else {
                // empty a always matches, but x can be up to n
                if x > n { continue; }
            }

            let after_a = x + la;
            if after_a > n { continue; }
            let y = next_b[after_a];
            if y == usize::MAX { continue; }

            let after_b = y + lb;
            if after_b > n { continue; }
            let z = next_c[after_b];
            if z == usize::MAX { continue; }

            let length = (z + lc) - x;
            if length < ans {
                ans = length;
            }
        }

        if ans == usize::MAX {
            -1
        } else {
            ans as i32
        }
    }
}
```

## Racket

```racket
(define (first-star str start)
  (let loop ((i start))
    (if (= i (string-length str))
        #f
        (if (char=? (string-ref str i) #\*)
            i
            (loop (+ i 1))))))

(define (range-vector limit)
  (let ((vec (make-vector (+ limit 1))))
    (for ([i (in-range (+ limit 1))])
      (vector-set! vec i i))
    vec))

(define (kmp-occurrences text pat)
  (let* ((n (string-length text))
         (m (string-length pat)))
    (if (= m 0)
        (range-vector n) ; not used for non‑empty patterns
        (let ((pi (make-vector m 0)))
          ;; prefix function
          (let loop ((i 1) (j 0))
            (when (< i m)
              (let inner ((j j))
                (if (and (> j 0)
                         (not (char=? (string-ref pat i) (string-ref pat j))))
                    (inner (vector-ref pi (- j 1)))
                    (begin
                      (when (char=? (string-ref pat i) (string-ref pat j))
                        (set! j (+ j 1)))
                      (vector-set! pi i j)
                      (loop (+ i 1) j))))))
          ;; search
          (let ((occ '())
                (j 0))
            (define (advance-j j i)
              (if (and (> j 0)
                       (not (char=? (string-ref pat j) (string-ref text i))))
                  (advance-j (vector-ref pi (- j 1)) i)
                  j))
            (for ([i (in-range n)])
              (set! j (advance-j j i))
              (when (char=? (string-ref pat j) (string-ref text i))
                (set! j (+ j 1)))
              (when (= j m)
                (set! occ (cons (- i m + 1) occ))
                (set! j (vector-ref pi (- j 1)))))
            (list->vector (reverse occ)))))))

(define (first-ge vec val)
  (let loop ((lo 0) (hi (vector-length vec)))
    (if (= lo hi)
        #f
        (let ((mid (quotient (+ lo hi) 2)))
          (if (>= (vector-ref vec mid) val)
              (loop lo mid)
              (loop (+ mid 1) hi))))))

(define/contract (shortest-matching-substring s p)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s))
         (star1 (first-star p 0))
         (star2 (first-star p (+ star1 1)))
         (a (substring p 0 star1))
         (b (substring p (+ star1 1) star2))
         (c (substring p (+ star2 1)))
         (len-a (string-length a))
         (len-b (string-length b))
         (len-c (string-length c))
         (occA (if (= len-a 0) (range-vector n) (kmp-occurrences s a)))
         (occB (if (= len-b 0) (range-vector n) (kmp-occurrences s b)))
         (occC (if (= len-c 0) (range-vector n) (kmp-occurrences s c))))
    (if (or (and (> len-a 0) (= (vector-length occA) 0))
            (and (> len-b 0) (= (vector-length occB) 0))
            (and (> len-c 0) (= (vector-length occC) 0)))
        -1
        (let ((inf (expt 2 31))
              (best inf))
          (for ([aPos (in-vector occA)])
            (let* ((minB (+ aPos len-a))
                   (bIdx (first-ge occB minB)))
              (when bIdx
                (let* ((bPos (vector-ref occB bIdx))
                       (minC (+ bPos len-b))
                       (cIdx (first-ge occC minC)))
                  (when cIdx
                    (let* ((cPos (vector-ref occC cIdx))
                           (len (- (+ cPos len-c) aPos)))
                      (when (< len best)
                        (set! best len))))))))
          (if (= best inf) -1 best)))))
```

## Erlang

```erlang
-spec shortest_matching_substring(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> integer().
shortest_matching_substring(S, P) ->
    SList = binary_to_list(S),
    N = length(SList),
    PL = binary_to_list(P),

    {A, B, C} = split_pattern(PL),
    LenA = length(A), LenB = length(B), LenC = length(C),

    OccA = case LenA of
               0 -> lists:seq(0, N);
               _ -> kmp_search(SList, A)
           end,

    NextBMap = case LenB of
                   0 -> undefined;
                   _ ->
                       OccB = kmp_search(SList, B),
                       build_next_map(OccB, N)
               end,
    NextCMap = case LenC of
                   0 -> undefined;
                   _ ->
                       OccC = kmp_search(SList, C),
                       build_next_map(OccC, N)
               end,

    MinLen = find_min_len(OccA, LenA, LenB, LenC, NextBMap, NextCMap, N),

    case MinLen of
        undefined -> -1;
        L -> L
    end.

%% split pattern into three parts A * B * C
split_pattern(P) ->
    Stars = find_stars(P, 0, []),
    [Idx1, Idx2] = Stars,
    A = lists:sublist(P, 1, Idx1),
    B = lists:sublist(P, Idx1 + 2, Idx2 - Idx1 - 1),
    C = lists:nthtail(Idx2 + 1, P),
    {A, B, C}.

find_stars([], _, Acc) -> lists:reverse(Acc);
find_stars([$*|Rest], Index, Acc) ->
    find_stars(Rest, Index + 1, [Index | Acc]);
find_stars([_|Rest], Index, Acc) ->
    find_stars(Rest, Index + 1, Acc).

%% KMP search returning list of start positions (0‑based)
kmp_search(Text, Pattern) when length(Pattern) =:= 0 -> [];
kmp_search(Text, Pattern) ->
    N = length(Text),
    M = length(Pattern),
    TextT = list_to_tuple(Text),
    PatT = list_to_tuple(Pattern),
    LpsArr = build_lps(PatT, M),
    search_loop(1, 0, N, M, TextT, PatT, LpsArr, []).

search_loop(I, J, N, M, _TextT, _PatT, _LpsArr, Acc) when I > N ->
    lists:reverse(Acc);
search_loop(I, J, N, M, TextT, PatT, LpsArr, Acc) ->
    CharT = element(I, TextT),
    CharP = element(J + 1, PatT),
    if CharT == CharP ->
            NewI = I + 1,
            NewJ = J + 1,
            case NewJ of
                M ->
                    StartPos = I - M,
                    NextJ = array:get(M - 1, LpsArr),
                    search_loop(NewI, NextJ, N, M, TextT, PatT, LpsArr, [StartPos | Acc]);
                _ ->
                    search_loop(NewI, NewJ, N, M, TextT, PatT, LpsArr, Acc)
            end;
       true ->
            if J == 0 ->
                    search_loop(I + 1, 0, N, M, TextT, PatT, LpsArr, Acc);
               true ->
                    PrevJ = array:get(J - 1, LpsArr),
                    search_loop(I, PrevJ, N, M, TextT, PatT, LpsArr, Acc)
            end
    end.

%% build LPS (failure) array for pattern tuple
build_lps(PatT, M) ->
    Lps0 = array:new(M, {default, 0}),
    build_lps_loop(2, 0, PatT, M, Lps0).

build_lps_loop(I, LenVal, PatT, M, LpsArr) when I =< M ->
    CharI = element(I, PatT),
    NewLen = case LenVal of
                 0 ->
                     if CharI == element(1, PatT) -> 1; true -> 0 end;
                 _ ->
                     adjust_len(LenVal, CharI, PatT, LpsArr)
             end,
    LpsArr2 = array:set(I - 1, NewLen, LpsArr),
    build_lps_loop(I + 1, NewLen, PatT, M, LpsArr2);
build_lps_loop(_, _, _, _, LpsArr) -> LpsArr.

adjust_len(LenVal, CharI, PatT, LpsArr) when LenVal > 0 ->
    CharCmp = element(LenVal + 1, PatT),
    if CharI == CharCmp ->
            LenVal + 1;
       true ->
            PrevLen = array:get(LenVal - 1, LpsArr),
            adjust_len(PrevLen, CharI, PatT, LpsArr)
    end.

%% build map: for each position pos (0..N) the smallest occurrence >= pos, or -1
build_next_map(OccList, N) ->
    Rev = lists:reverse(OccList),
    build_next_map(N, Rev, -1, #{}).

build_next_map(Pos, Rev, Next, Acc) when Pos >= 0 ->
    {NewNext, NewRev} =
        case Rev of
            [Pos|Rest] -> {Pos, Rest};
            _ -> {Next, Rev}
        end,
    Acc1 = maps:put(Pos, NewNext, Acc),
    build_next_map(Pos - 1, NewRev, NewNext, Acc1);
build_next_map(_, _, _, Acc) -> Acc.

%% find minimal length using precomputed next maps
find_min_len(OccA, LenA, LenB, LenC, NextBMap, NextCMap, _N) ->
    lists:foldl(fun(I, MinAcc) ->
        PosAfterA = I + LenA,
        StartB = if LenB == 0 -> PosAfterA;
                    true -> maps:get(PosAfterA, NextBMap, -1)
                end,
        case StartB of
            -1 -> MinAcc;
            _ ->
                PosAfterB = StartB + LenB,
                StartC = if LenC == 0 -> PosAfterB;
                            true -> maps:get(PosAfterB, NextCMap, -1)
                        end,
                case StartC of
                    -1 -> MinAcc;
                    _ ->
                        Length = (StartC + LenC) - I,
                        case MinAcc of
                            undefined -> Length;
                            L when Length < L -> Length;
                            L -> L
                        end
                end
        end
    end, undefined, OccA).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_matching_substring(String.t(), String.t()) :: integer()
  def shortest_matching_substring(s, p) do
    n = byte_size(s)

    # split pattern into three parts A * B * C
    [a, rest] = String.split(p, "*", parts: 2)
    [b, c] =
      case String.split(rest, "*", parts: 2) do
        [b1, c1] -> [b1, c1]
        _ -> ["", ""]
      end

    a_len = byte_size(a)
    b_len = byte_size(b)
    c_len = byte_size(c)

    # occurrences of each part in s using Erlang's binary matching (overlapping allowed)
    occ_a =
      if a_len == 0 do
        []
      else
        :binary.matches(s, a) |> Enum.map(fn {pos, _len} -> pos end)
      end

    occ_b =
      if b_len == 0 do
        Enum.to_list(0..n)
      else
        :binary.matches(s, b) |> Enum.map(fn {pos, _len} -> pos end)
      end

    occ_c =
      if c_len == 0 do
        []
      else
        :binary.matches(s, c) |> Enum.map(fn {pos, _len} -> pos end)
      end

    # left[i] = latest start of A such that start + a_len <= i (or i when A empty)
    left_list =
      if a_len == 0 do
        for i <- 0..n, do: i
      else
        build_left(0..n, occ_a, a_len)
      end

    # next_c[i] = earliest start of C such that start >= i (or i when C empty)
    next_c_list =
      if c_len == 0 do
        for i <- 0..n, do: i
      else
        build_next(0..n, occ_c)
      end

    left_arr = :array.from_list(left_list)
    next_c_arr = :array.from_list(next_c_list)

    min_len =
      Enum.reduce(occ_b, :math.inf(), fn b_start, acc ->
        a_start = :array.get(b_start, left_arr)

        if a_start == nil do
          acc
        else
          pos_needed = b_start + b_len

          if pos_needed > n do
            acc
          else
            c_start = :array.get(pos_needed, next_c_arr)

            if c_start == nil do
              acc
            else
              total = (c_start + c_len) - a_start
              if total < acc, do: total, else: acc
            end
          end
        end
      end)

    if min_len == :math.inf(), do: -1, else: trunc(min_len)
  end

  # Build left array using a single pass over occ list
  defp build_left(range, occ_list, a_len) do
    {result_rev, _remaining, _latest} =
      Enum.reduce(range, {[], occ_list, nil}, fn i, {acc, occ_rem, latest} ->
        {new_occ, new_latest} = advance_left(i, occ_rem, latest, a_len)
        {[new_latest | acc], new_occ, new_latest}
      end)

    Enum.reverse(result_rev)
  end

  defp advance_left(i, [h | t] = occ, _latest, a_len) when h + a_len <= i do
    # this occurrence satisfies condition; keep advancing
    advance_left(i, t, h, a_len)
  end

  defp advance_left(_i, occ, latest, _a_len), do: {occ, latest}

  # Build next_c array using reverse scan and a MapSet for O(1) membership
  defp build_next(range, occ_list) do
    set = MapSet.new(occ_list)

    {result_rev, _next} =
      Enum.reduce(Enum.reverse(range), {[], nil}, fn i, {acc, next} ->
        new_next = if MapSet.member?(set, i), do: i, else: next
        {[new_next | acc], new_next}
      end)

    result_rev
  end
end
```
