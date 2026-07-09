# 3008. Find Beautiful Indices in the Given Array II

## Cpp

```cpp
class Solution {
public:
    // KMP prefix function
    vector<int> buildLPS(const string& pat) {
        int m = pat.size();
        vector<int> lps(m, 0);
        for (int i = 1, len = 0; i < m; ) {
            if (pat[i] == pat[len]) {
                lps[i++] = ++len;
            } else {
                if (len) len = lps[len - 1];
                else lps[i++] = 0;
            }
        }
        return lps;
    }

    // Return starting indices where pat occurs in txt
    vector<int> getOccurrences(const string& txt, const string& pat) {
        int n = txt.size(), m = pat.size();
        if (m > n) return {};
        vector<int> lps = buildLPS(pat);
        vector<int> occ;
        for (int i = 0, j = 0; i < n; ) {
            if (txt[i] == pat[j]) {
                ++i; ++j;
                if (j == m) {
                    occ.push_back(i - m);
                    j = lps[j - 1];
                }
            } else {
                if (j) j = lps[j - 1];
                else ++i;
            }
        }
        return occ;
    }

    vector<int> beautifulIndices(string s, string a, string b, int k) {
        vector<int> posA = getOccurrences(s, a);
        vector<int> posB = getOccurrences(s, b);
        if (posA.empty() || posB.empty()) return {};

        vector<int> res;
        for (int idx : posA) {
            auto it = lower_bound(posB.begin(), posB.end(), idx);
            bool ok = false;
            if (it != posB.end() && abs(*it - idx) <= k) ok = true;
            if (!ok && it != posB.begin()) {
                --it;
                if (abs(*it - idx) <= k) ok = true;
            }
            if (ok) res.push_back(idx);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        int n = s.length();
        boolean[] isBStart = new boolean[n];
        for (int pos : getOccurrences(s, b)) {
            isBStart[pos] = true;
        }
        int[] left = new int[n];
        int last = -n * 2;
        for (int i = 0; i < n; i++) {
            if (isBStart[i]) last = i;
            left[i] = last;
        }
        int[] right = new int[n];
        int next = n * 2;
        for (int i = n - 1; i >= 0; i--) {
            if (isBStart[i]) next = i;
            right[i] = next;
        }
        List<Integer> res = new ArrayList<>();
        for (int pos : getOccurrences(s, a)) {
            int lDist = pos - left[pos];
            int rDist = right[pos] - pos;
            if (lDist <= k || rDist <= k) {
                res.add(pos);
            }
        }
        return res;
    }

    private List<Integer> getOccurrences(String text, String pattern) {
        List<Integer> occ = new ArrayList<>();
        int n = text.length(), m = pattern.length();
        if (m > n) return occ;
        int[] pi = new int[m];
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) {
                j = pi[j - 1];
            }
            if (pattern.charAt(i) == pattern.charAt(j)) j++;
            pi[i] = j;
        }
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j > 0 && text.charAt(i) != pattern.charAt(j)) {
                j = pi[j - 1];
            }
            if (text.charAt(i) == pattern.charAt(j)) j++;
            if (j == m) {
                occ.add(i - m + 1);
                j = pi[j - 1];
            }
        }
        return occ;
    }
}
```

## Python

```python
class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        from bisect import bisect_left

        def kmp_occurrences(pat, txt):
            m, n = len(pat), len(txt)
            if m == 0 or m > n:
                return []
            # build lps array
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j and pat[i] != pat[j]:
                    j = lps[j - 1]
                if pat[i] == pat[j]:
                    j += 1
                    lps[i] = j
            # search
            res = []
            j = 0
            for i in range(n):
                while j and txt[i] != pat[j]:
                    j = lps[j - 1]
                if txt[i] == pat[j]:
                    j += 1
                    if j == m:
                        res.append(i - m + 1)
                        j = lps[j - 1]
            return res

        pos_a = kmp_occurrences(a, s)
        pos_b = kmp_occurrences(b, s)

        if not pos_a or not pos_b:
            return []

        ans = []
        for i in pos_a:
            idx = bisect_left(pos_b, i)
            ok = False
            if idx < len(pos_b) and abs(pos_b[idx] - i) <= k:
                ok = True
            if idx > 0 and abs(pos_b[idx - 1] - i) <= k:
                ok = True
            if ok:
                ans.append(i)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(pat: str, txt: str) -> List[int]:
            m, n = len(pat), len(txt)
            if m == 0 or m > n:
                return []
            # build lps array
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            # search
            res = []
            i = j = 0
            while i < n:
                if txt[i] == pat[j]:
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

        pos_a = occurrences(a, s)
        pos_b = occurrences(b, s)

        ans = []
        p = 0
        m = len(pos_b)
        for idx in pos_a:
            while p < m and pos_b[p] < idx - k:
                p += 1
            if p < m and pos_b[p] <= idx + k:
                ans.append(idx)

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static void computeLPS(const char *pat, int m, int *lps) {
    int len = 0;
    lps[0] = 0;
    for (int i = 1; i < m; ) {
        if (pat[i] == pat[len]) {
            len++;
            lps[i++] = len;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
    }
}

static void kmpSearch(const char *txt, const char *pat, char *occ) {
    int n = strlen(txt);
    int m = strlen(pat);
    if (m == 0 || n < m) return;

    int *lps = (int *)malloc(m * sizeof(int));
    computeLPS(pat, m, lps);

    int i = 0, j = 0;
    while (i < n) {
        if (txt[i] == pat[j]) {
            i++; j++;
            if (j == m) {
                occ[i - m] = 1;          // match starts at i-m
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
    free(lps);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* beautifulIndices(char* s, char* a, char* b, int k, int* returnSize) {
    int n = strlen(s);
    int la = strlen(a);
    int lb = strlen(b);

    char *occA = (char *)calloc(n, 1);
    char *occB = (char *)calloc(n, 1);

    if (la <= n) kmpSearch(s, a, occA);
    if (lb <= n) kmpSearch(s, b, occB);

    int *left = (int *)malloc(n * sizeof(int));
    int last = -1;
    for (int i = 0; i < n; ++i) {
        if (occB[i]) last = i;
        left[i] = last;
    }

    int *right = (int *)malloc(n * sizeof(int));
    int nxt = -1;
    for (int i = n - 1; i >= 0; --i) {
        if (occB[i]) nxt = i;
        right[i] = nxt;
    }

    int *res = (int *)malloc(n * sizeof(int));
    int cnt = 0;

    if (la <= n) {
        int limit = n - la;
        for (int i = 0; i <= limit; ++i) {
            if (!occA[i]) continue;
            bool ok = false;
            if (left[i] != -1 && i - left[i] <= k) ok = true;
            else if (right[i] != -1 && right[i] - i <= k) ok = true;
            if (ok) res[cnt++] = i;
        }
    }

    *returnSize = cnt;

    free(occA);
    free(occB);
    free(left);
    free(right);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    public IList<int> BeautifulIndices(string s, string a, string b, int k)
    {
        List<int> posA = GetOccurrences(s, a);
        List<int> posB = GetOccurrences(s, b);
        List<int> result = new List<int>();
        int idxB = 0;
        foreach (int i in posA)
        {
            while (idxB < posB.Count && posB[idxB] < i - k)
                idxB++;
            if (idxB < posB.Count && posB[idxB] <= i + k)
                result.Add(i);
        }
        return result;
    }

    private List<int> GetOccurrences(string text, string pattern)
    {
        int n = text.Length;
        int m = pattern.Length;
        var res = new List<int>();
        if (m == 0 || m > n) return res;

        // Build LPS array
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m;)
        {
            if (pattern[i] == pattern[len])
            {
                len++;
                lps[i] = len;
                i++;
            }
            else
            {
                if (len != 0)
                    len = lps[len - 1];
                else
                {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        // KMP search
        for (int i = 0, j = 0; i < n;)
        {
            if (text[i] == pattern[j])
            {
                i++; j++;
                if (j == m)
                {
                    res.Add(i - m);
                    j = lps[j - 1];
                }
            }
            else
            {
                if (j != 0)
                    j = lps[j - 1];
                else
                    i++;
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
 * @param {string} a
 * @param {string} b
 * @param {number} k
 * @return {number[]}
 */
var beautifulIndices = function(s, a, b, k) {
    const getOccurrences = (text, pat) => {
        const n = text.length, m = pat.length;
        if (m > n) return [];
        // build lps array for pattern
        const lps = new Array(m).fill(0);
        for (let i = 1, len = 0; i < m;) {
            if (pat.charCodeAt(i) === pat.charCodeAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len !== 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        const occ = [];
        let i = 0, j = 0;
        while (i < n) {
            if (text.charCodeAt(i) === pat.charCodeAt(j)) {
                i++; j++;
                if (j === m) {
                    occ.push(i - m);
                    j = lps[j - 1];
                }
            } else {
                if (j !== 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return occ;
    };

    const occA = getOccurrences(s, a);
    const occB = getOccurrences(s, b);
    const res = [];
    let p = 0;
    for (const idx of occA) {
        while (p < occB.length && occB[p] < idx - k) p++;
        if (p < occB.length && Math.abs(occB[p] - idx) <= k) {
            res.push(idx);
        }
    }
    return res;
};
```

## Typescript

```typescript
function beautifulIndices(s: string, a: string, b: string, k: number): number[] {
    const getOccurrences = (text: string, pat: string): number[] => {
        const n = text.length, m = pat.length;
        if (m > n) return [];
        const lps = new Array(m).fill(0);
        for (let i = 1, len = 0; i < m;) {
            if (pat[i] === pat[len]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len !== 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        const res: number[] = [];
        for (let i = 0, j = 0; i < n;) {
            if (text[i] === pat[j]) {
                i++; j++;
                if (j === m) {
                    res.push(i - m);
                    j = lps[j - 1];
                }
            } else {
                if (j !== 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return res;
    };

    const posA = getOccurrences(s, a);
    const posB = getOccurrences(s, b);
    const result: number[] = [];

    let ptr = 0; // pointer in posB
    for (const idx of posA) {
        while (ptr < posB.length && posB[ptr] < idx - k) {
            ptr++;
        }
        if (ptr < posB.length && posB[ptr] <= idx + k) {
            result.push(idx);
        }
    }

    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param String $a
     * @param String $b
     * @param Integer $k
     * @return Integer[]
     */
    function beautifulIndices($s, $a, $b, $k) {
        $posA = $this->kmp($s, $a);
        $posB = $this->kmp($s, $b);
        $res = [];
        $pb = 0;
        $lenB = count($posB);
        foreach ($posA as $i) {
            while ($pb < $lenB && $posB[$pb] < $i - $k) {
                $pb++;
            }
            if ($pb < $lenB && $posB[$pb] <= $i + $k) {
                $res[] = $i;
            }
        }
        return $res;
    }

    private function kmp($text, $pattern) {
        $n = strlen($pattern);
        if ($n == 0) return [];
        // build lps array
        $lps = array_fill(0, $n, 0);
        $len = 0;
        for ($i = 1; $i < $n; $i++) {
            while ($len > 0 && $pattern[$i] !== $pattern[$len]) {
                $len = $lps[$len - 1];
            }
            if ($pattern[$i] === $pattern[$len]) {
                $len++;
                $lps[$i] = $len;
            }
        }

        // search
        $m = strlen($text);
        $positions = [];
        $i = 0; // index for text
        $j = 0; // index for pattern
        while ($i < $m) {
            if ($text[$i] === $pattern[$j]) {
                $i++;
                $j++;
                if ($j == $n) {
                    $positions[] = $i - $j;
                    $j = $lps[$j - 1];
                }
            } else {
                if ($j != 0) {
                    $j = $lps[$j - 1];
                } else {
                    $i++;
                }
            }
        }
        return $positions;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulIndices(_ s: String, _ a: String, _ b: String, _ k: Int) -> [Int] {
        let sArr = Array(s.utf8)
        let aArr = Array(a.utf8)
        let bArr = Array(b.utf8)

        func kmp(_ text: [UInt8], _ pattern: [UInt8]) -> [Int] {
            let n = text.count
            let m = pattern.count
            if m == 0 || n < m { return [] }
            var lps = [Int](repeating: 0, count: m)
            var len = 0
            var i = 1
            while i < m {
                if pattern[i] == pattern[len] {
                    len += 1
                    lps[i] = len
                    i += 1
                } else {
                    if len != 0 {
                        len = lps[len - 1]
                    } else {
                        lps[i] = 0
                        i += 1
                    }
                }
            }
            var res: [Int] = []
            var j = 0
            i = 0
            while i < n {
                if text[i] == pattern[j] {
                    i += 1
                    j += 1
                    if j == m {
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

        let posA = kmp(sArr, aArr)
        let posB = kmp(sArr, bArr)

        var result: [Int] = []
        var pb = 0
        for pa in posA {
            while pb < posB.count && posB[pb] < pa - k {
                pb += 1
            }
            if pb < posB.count && posB[pb] <= pa + k {
                result.append(pa)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun beautifulIndices(s: String, a: String, b: String, k: Int): List<Int> {
        val posA = kmpSearch(s, a)
        val posB = kmpSearch(s, b)
        val result = mutableListOf<Int>()
        var jPtr = 0
        for (iPos in posA) {
            while (jPtr < posB.size && posB[jPtr] < iPos - k) {
                jPtr++
            }
            if (jPtr < posB.size && posB[jPtr] <= iPos + k) {
                result.add(iPos)
            }
        }
        return result
    }

    private fun kmpSearch(text: String, pattern: String): List<Int> {
        val n = text.length
        val m = pattern.length
        if (m == 0 || m > n) return emptyList()
        // Build LPS array
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
        // Search
        val res = mutableListOf<Int>()
        var ti = 0
        var pi = 0
        while (ti < n) {
            if (text[ti] == pattern[pi]) {
                ti++; pi++
                if (pi == m) {
                    res.add(ti - m)
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
}
```

## Dart

```dart
class Solution {
  List<int> beautifulIndices(String s, String a, String b, int k) {
    List<int> posA = _kmp(s, a);
    List<int> posB = _kmp(s, b);
    List<int> res = [];
    if (posA.isEmpty || posB.isEmpty) return res;
    for (int i in posA) {
      int left = i - k;
      int right = i + k;
      int idx = _lowerBound(posB, left);
      if (idx < posB.length && posB[idx] <= right) {
        res.add(i);
      }
    }
    return res;
  }

  List<int> _kmp(String text, String pattern) {
    List<int> t = text.codeUnits;
    List<int> p = pattern.codeUnits;
    int n = t.length, m = p.length;
    if (m > n) return [];
    List<int> lps = List.filled(m, 0);
    int len = 0;
    for (int i = 1; i < m;) {
      if (p[i] == p[len]) {
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
      if (t[i] == p[j]) {
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

  int _lowerBound(List<int> arr, int target) {
    int lo = 0, hi = arr.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (arr[mid] < target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}
```

## Golang

```go
func beautifulIndices(s string, a string, b string, k int) []int {
	getOcc := func(text, pat string) []int {
		n, m := len(text), len(pat)
		if m == 0 || n < m {
			return nil
		}
		lps := make([]int, m)
		for i, j := 1, 0; i < m; {
			if pat[i] == pat[j] {
				j++
				lps[i] = j
				i++
			} else {
				if j != 0 {
					j = lps[j-1]
				} else {
					lps[i] = 0
					i++
				}
			}
		}
		res := []int{}
		for i, j := 0, 0; i < n; {
			if text[i] == pat[j] {
				i++
				j++
				if j == m {
					res = append(res, i-m)
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

	posA := getOcc(s, a)
	posB := getOcc(s, b)

	ans := []int{}
	p := 0
	for _, idx := range posA {
		for p < len(posB) && posB[p] < idx-k {
			p++
		}
		if p < len(posB) && posB[p] <= idx+k {
			ans = append(ans, idx)
		}
	}
	return ans
}
```

## Ruby

```ruby
def compute_prefix(pattern)
  m = pattern.length
  pi = Array.new(m, 0)
  j = 0
  (1...m).each do |i|
    while j > 0 && pattern[i] != pattern[j]
      j = pi[j - 1]
    end
    if pattern[i] == pattern[j]
      j += 1
      pi[i] = j
    end
  end
  pi
end

def kmp_positions(text, pattern)
  n = text.length
  m = pattern.length
  return [] if m > n
  pi = compute_prefix(pattern)
  res = []
  j = 0
  (0...n).each do |i|
    while j > 0 && text[i] != pattern[j]
      j = pi[j - 1]
    end
    if text[i] == pattern[j]
      j += 1
      if j == m
        res << i - m + 1
        j = pi[j - 1]
      end
    end
  end
  res
end

# @param {String} s
# @param {String} a
# @param {String} b
# @param {Integer} k
# @return {Integer[]}
def beautiful_indices(s, a, b, k)
  pos_a = kmp_positions(s, a)
  pos_b = kmp_positions(s, b)
  return [] if pos_a.empty? || pos_b.empty?

  res = []
  n_b = pos_b.length
  pos_a.each do |i|
    lo = 0
    hi = n_b
    while lo < hi
      mid = (lo + hi) / 2
      if pos_b[mid] < i
        lo = mid + 1
      else
        hi = mid
      end
    end
    ok = false
    if lo < n_b && (pos_b[lo] - i).abs <= k
      ok = true
    elsif lo > 0 && (i - pos_b[lo - 1]).abs <= k
      ok = true
    end
    res << i if ok
  end
  res
end
```

## Scala

```scala
object Solution {
  def beautifulIndices(s: String, a: String, b: String, k: Int): List[Int] = {
    val n = s.length
    val occA = findOccurrences(s, a)
    val occB = findOccurrences(s, b)

    // nearest left occurrence of b for each position
    val left = new Array[Int](n)
    var last = -1
    var i = 0
    while (i < n) {
      if (occB(i)) last = i
      left(i) = last
      i += 1
    }

    // nearest right occurrence of b for each position
    val right = new Array[Int](n)
    var next = -1
    i = n - 1
    while (i >= 0) {
      if (occB(i)) next = i
      right(i) = next
      i -= 1
    }

    val res = scala.collection.mutable.ListBuffer[Int]()
    i = 0
    while (i < n) {
      if (occA(i)) {
        var minDist = Int.MaxValue
        val l = left(i)
        if (l != -1) {
          val d = i - l
          if (d < minDist) minDist = d
        }
        val r = right(i)
        if (r != -1) {
          val d = r - i
          if (d < minDist) minDist = d
        }
        if (minDist <= k) res += i
      }
      i += 1
    }

    res.toList
  }

  private def findOccurrences(text: String, pat: String): Array[Boolean] = {
    val n = text.length
    val m = pat.length
    val occ = new Array[Boolean](n)
    if (m == 0 || m > n) return occ

    // build lps array for pattern
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

    // KMP search
    var ti = 0
    var pj = 0
    while (ti < n) {
      if (text.charAt(ti) == pat.charAt(pj)) {
        ti += 1
        pj += 1
        if (pj == m) {
          occ(ti - m) = true
          pj = lps(pj - 1)
        }
      } else {
        if (pj != 0) {
          pj = lps(pj - 1)
        } else {
          ti += 1
        }
      }
    }

    occ
  }
}
```

## Rust

```rust
use std::cmp;

fn kmp_search(text: &[u8], pat: &[u8]) -> Vec<usize> {
    let n = text.len();
    let m = pat.len();
    if m == 0 || n < m {
        return Vec::new();
    }
    // build lps array
    let mut lps = vec![0usize; m];
    let mut len = 0usize;
    for i in 1..m {
        while len > 0 && pat[i] != pat[len] {
            len = lps[len - 1];
        }
        if pat[i] == pat[len] {
            len += 1;
            lps[i] = len;
        }
    }
    // search
    let mut res = Vec::new();
    let (mut i, mut j) = (0usize, 0usize);
    while i < n {
        if text[i] == pat[j] {
            i += 1;
            j += 1;
            if j == m {
                res.push(i - m);
                j = lps[j - 1];
            }
        } else {
            if j != 0 {
                j = lps[j - 1];
            } else {
                i += 1;
            }
        }
    }
    res
}

impl Solution {
    pub fn beautiful_indices(s: String, a: String, b: String, k: i32) -> Vec<i32> {
        let sb = s.as_bytes();
        let ab = a.as_bytes();
        let bb = b.as_bytes();
        let n = sb.len();

        let occ_a = kmp_search(sb, ab);
        let occ_b = kmp_search(sb, bb);

        let mut is_a = vec![false; n];
        for &pos in &occ_a {
            if pos < n {
                is_a[pos] = true;
            }
        }
        let mut is_b = vec![false; n];
        for &pos in &occ_b {
            if pos < n {
                is_b[pos] = true;
            }
        }

        // nearest b to the left
        let mut left = vec![-1i32; n];
        let mut last = -1i32;
        for i in 0..n {
            if is_b[i] {
                last = i as i32;
            }
            left[i] = last;
        }

        // nearest b to the right
        let mut right = vec![-1i32; n];
        let mut nxt = -1i32;
        for i in (0..n).rev() {
            if is_b[i] {
                nxt = i as i32;
            }
            right[i] = nxt;
        }

        let mut ans = Vec::new();
        for i in 0..n {
            if !is_a[i] {
                continue;
            }
            let mut ok = false;
            if left[i] != -1 && (i as i32 - left[i]) <= k {
                ok = true;
            }
            if right[i] != -1 && (right[i] - i as i32) <= k {
                ok = true;
            }
            if ok {
                ans.push(i as i32);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define (compute-prefix pat)
  (let* ((m (string-length pat))
         (pi (make-vector m 0)))
    (let loop ((i 1) (j 0))
      (when (< i m)
        (if (char=? (string-ref pat i) (string-ref pat j))
            (begin
              (set! j (+ j 1))
              (vector-set! pi i j)
              (loop (+ i 1) j))
            (if (> j 0)
                (begin
                  (set! j (vector-ref pi (- j 1)))
                  (loop i j))
                (begin
                  (vector-set! pi i 0)
                  (loop (+ i 1) 0))))))
    pi))

(define (kmp-search txt pat)
  (let* ((n (string-length txt))
         (m (string-length pat))
         (pi (compute-prefix pat)))
    (let loop ((i 0) (j 0) (res '()))
      (if (= i n)
          (reverse res)
          (if (char=? (string-ref txt i) (string-ref pat j))
              (let ((i1 (+ i 1)) (j1 (+ j 1)))
                (if (= j1 m)
                    (loop i1 (vector-ref pi (- j1 1)) (cons (- i1 m) res))
                    (loop i1 j1 res)))
              (if (> j 0)
                  (loop i (vector-ref pi (- j 1)) res)
                  (loop (+ i 1) 0 res)))))))

(define/contract (beautiful-indices s a b k)
  (-> string? string? string? exact-integer? (listof exact-integer?))
  (let* ((posA (kmp-search s a))
         (posB-list (kmp-search s b)))
    (if (or (null? posA) (null? posB-list))
        '()
        (let* ((posB (list->vector posB-list))
               (lenB (vector-length posB)))
          (let loop ((i-list posA) (bptr 0) (ans '()))
            (if (null? i-list)
                (reverse ans)
                (let* ((i (car i-list))
                       (new-bptr
                         (let advance ((p bptr))
                           (if (and (< p lenB) (< (vector-ref posB p) (- i k)))
                               (advance (+ p 1))
                               p))))
                  (if (and (< new-bptr lenB)
                           (<= (vector-ref posB new-bptr) (+ i k)))
                      (loop (cdr i-list) new-bptr (cons i ans))
                      (loop (cdr i-list) new-bptr ans)))))))))
```

## Erlang

```erlang
-spec beautiful_indices(S :: unicode:unicode_binary(), A :: unicode:unicode_binary(), B :: unicode:unicode_binary(), K :: integer()) -> [integer()].
beautiful_indices(S, A, B, K) ->
    APos = binary:matches(S, A),
    BPos = binary:matches(S, B),
    find_beautiful(APos, BPos, K).

find_beautiful([], _, _) ->
    [];
find_beautiful(_, [], _) ->
    [];
find_beautiful(AList, BList, K) ->
    loop(AList, BList, K, []).

loop([], _BList, _K, Acc) ->
    lists:reverse(Acc);
loop(_AList, [], _K, Acc) ->
    lists:reverse(Acc);
loop([A|As], BRem, K, Acc) ->
    NewB = drop_while(BRem, fun(B) -> B < A - K end),
    case NewB of
        [] ->
            lists:reverse(Acc);
        [B|Bs] ->
            if B =< A + K ->
                    loop(As, NewB, K, [A|Acc]);
               true ->
                    loop(As, NewB, K, Acc)
            end
    end.

drop_while([], _Fun) -> [];
drop_while([H|T], Fun) when is_function(Fun, 1), Fun(H) ->
    drop_while(T, Fun);
drop_while(List, _Fun) -> List.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @base 91138233
  @mod1 1_000_000_007
  @mod2 1_000_000_009

  @spec beautiful_indices(String.t(), String.t(), String.t(), integer) :: [integer]
  def beautiful_indices(s, a, b, k) do
    s_bytes = :binary.bin_to_list(s)
    a_bytes = :binary.bin_to_list(a)
    b_bytes = :binary.bin_to_list(b)

    n = length(s_bytes)
    len_a = length(a_bytes)
    len_b = length(b_bytes)

    {pow1, pow2, pref1, pref2} = build_hash_structs(s_bytes)

    ha1 = pattern_hash(a_bytes, @mod1)
    ha2 = pattern_hash(a_bytes, @mod2)
    hb1 = pattern_hash(b_bytes, @mod1)
    hb2 = pattern_hash(b_bytes, @mod2)

    occ_a = occurrences(n, len_a, ha1, ha2, pref1, pref2, pow1, pow2)
    occ_b = occurrences(n, len_b, hb1, hb2, pref1, pref2, pow1, pow2)

    if occ_b == [] do
      []
    else
      b_len = length(occ_b)
      Enum.reduce(occ_a, [], fn i, acc ->
        idx = lower_bound(occ_b, i - k)
        cond do
          idx < b_len and :erlang.element(idx + 1, list_to_tuple(occ_b)) <= i + k -> [i | acc]
          true -> acc
        end
      end) |> Enum.reverse()
    end
  end

  # Build prefix hashes and power tables for the main string.
  defp build_hash_structs(bytes) do
    {pow1_rev, pow2_rev, pref1_rev, pref2_rev} =
      Enum.reduce(bytes, {[1], [1], [0], [0]}, fn c,
          {pow1_acc, pow2_acc, pref1_acc, pref2_acc} ->
        prev_pow1 = hd(pow1_acc)
        new_pow1 = rem(prev_pow1 * @base, @mod1)
        pow1_acc2 = [new_pow1 | pow1_acc]

        prev_pow2 = hd(pow2_acc)
        new_pow2 = rem(prev_pow2 * @base, @mod2)
        pow2_acc2 = [new_pow2 | pow2_acc]

        val = c - ?a + 1

        prev_pref1 = hd(pref1_acc)
        new_pref1 = rem(prev_pref1 * @base + val, @mod1)
        pref1_acc2 = [new_pref1 | pref1_acc]

        prev_pref2 = hd(pref2_acc)
        new_pref2 = rem(prev_pref2 * @base + val, @mod2)
        pref2_acc2 = [new_pref2 | pref2_acc]

        {pow1_acc2, pow2_acc2, pref1_acc2, pref2_acc2}
      end)

    {
      List.to_tuple(Enum.reverse(pow1_rev)),
      List.to_tuple(Enum.reverse(pow2_rev)),
      List.to_tuple(Enum.reverse(pref1_rev)),
      List.to_tuple(Enum.reverse(pref2_rev))
    }
  end

  # Compute hash of a pattern using given modulus.
  defp pattern_hash(p_bytes, mod) do
    Enum.reduce(p_bytes, 0, fn c, acc ->
      rem(acc * @base + (c - ?a + 1), mod)
    end)
  end

  # Find all start indices where a substring of length pat_len matches given hashes.
  defp occurrences(s_len, pat_len, h1_target, h2_target, pref1, pref2, pow1, pow2) do
    max_start = s_len - pat_len
    Enum.reduce(0..max_start, [], fn i, acc ->
      j = i + pat_len
      h1 = sub_hash(pref1, pow1, i, j, @mod1)
      h2 = sub_hash(pref2, pow2, i, j, @mod2)

      if h1 == h1_target and h2 == h2_target do
        [i | acc]
      else
        acc
      end
    end) |> Enum.reverse()
  end

  # Compute hash of substring [l, r) using precomputed tables.
  defp sub_hash(pref_tup, pow_tup, l, r, mod) do
    ph = :erlang.element(r + 1, pref_tup)
    pl = :erlang.element(l + 1, pref_tup)
    pw = :erlang.element(r - l + 1, pow_tup)
    hash = rem(ph - rem(pl * pw, mod), mod)
    if hash < 0, do: hash + mod, else: hash
  end

  # Lower bound binary search: first index >= target.
  defp lower_bound(arr, target) do
    low = 0
    high = length(arr)

    lb(low, high, arr, target)
  end

  defp lb(low, high, _arr, _target) when low >= high, do: low

  defp lb(low, high, arr, target) do
    mid = div(low + high, 2)
    val = Enum.at(arr, mid)

    if val < target do
      lb(mid + 1, high, arr, target)
    else
      lb(low, mid, arr, target)
    end
  end

  # Helper to convert list to tuple for fast element access in lower_bound check.
  defp list_to_tuple(list), do: List.to_tuple(list)
end
```
