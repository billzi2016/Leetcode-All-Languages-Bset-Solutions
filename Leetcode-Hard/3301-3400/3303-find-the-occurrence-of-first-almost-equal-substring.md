# 3303. Find the Occurrence of First Almost Equal Substring

## Cpp

```cpp
class Solution {
public:
    // Z-algorithm
    vector<int> zFunction(const string& s) {
        int n = s.size();
        vector<int> z(n);
        int l = 0, r = 0;
        for (int i = 1; i < n; ++i) {
            if (i <= r) z[i] = min(r - i + 1, z[i - l]);
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        z[0] = n;
        return z;
    }

    int minStartingIndex(string s, string pattern) {
        int n = s.size(), m = pattern.size();
        if (m > n) return -1;

        // pref: longest prefix match of pattern with s starting at i
        string concat1 = pattern + "#" + s;
        vector<int> z1 = zFunction(concat1);
        vector<int> pref(n);
        for (int i = 0; i < n; ++i) {
            int val = z1[m + 1 + i];
            if (val > m) val = m;
            pref[i] = val;
        }

        // suff: longest suffix match of pattern with s ending at i
        string rev_s(s.rbegin(), s.rend());
        string rev_p(pattern.rbegin(), pattern.rend());
        string concat2 = rev_p + "#" + rev_s;
        vector<int> z2 = zFunction(concat2);
        vector<int> suff(n);
        for (int i = 0; i < n; ++i) {
            int pos_rev = n - 1 - i;
            int val = z2[m + 1 + pos_rev];
            if (val > m) val = m;
            suff[i] = val;
        }

        for (int start = 0; start <= n - m; ++start) {
            int leftMatch = pref[start];
            if (leftMatch >= m) return start; // exact match
            int needSuffix = m - leftMatch - 1;
            if (needSuffix <= 0) return start; // only one mismatch at the last character
            int endIdx = start + m - 1;
            if (suff[endIdx] >= needSuffix) return start;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minStartingIndex(String s, String pattern) {
        int n = s.length();
        int m = pattern.length();
        if (m > n) return -1;

        // Z-function for pattern + "#" + s
        StringBuilder sb = new StringBuilder(m + 1 + n);
        sb.append(pattern).append('#').append(s);
        int[] z = zFunction(sb.toString());

        int[] pref = new int[n];
        for (int i = 0; i < n; i++) {
            int idx = m + 1 + i;
            pref[i] = Math.min(z[idx], m);
        }

        // Z-function for reversed strings
        String revPattern = new StringBuilder(pattern).reverse().toString();
        String revS = new StringBuilder(s).reverse().toString();
        StringBuilder sb2 = new StringBuilder(m + 1 + n);
        sb2.append(revPattern).append('#').append(revS);
        int[] zRev = zFunction(sb2.toString());

        int[] suff = new int[n];
        for (int i = 0; i < n; i++) {
            int revIdx = m + 1 + (n - 1 - i);
            suff[i] = Math.min(zRev[revIdx], m);
        }

        for (int start = 0; start <= n - m; start++) {
            int L = pref[start];
            if (L == m) return start; // exact match
            int R = suff[start + m - 1];
            if (L + R >= m - 1) return start;
        }
        return -1;
    }

    private int[] zFunction(String str) {
        int n = str.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && str.charAt(z[i]) == str.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }
}
```

## Python

```python
class Solution(object):
    def minStartingIndex(self, s, pattern):
        """
        :type s: str
        :type pattern: str
        :rtype: int
        """
        n = len(s)
        m = len(pattern)

        def z_function(t):
            L = len(t)
            z = [0] * L
            l = r = 0
            for i in range(1, L):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < L and t[z[i]] == t[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            z[0] = L
            return z

        # pref[i]: longest prefix of pattern matching s starting at i
        combined = pattern + "#" + s
        z1 = z_function(combined)
        pref = [0] * n
        offset = m + 1
        for i in range(n):
            v = z1[offset + i]
            if v > m:
                v = m
            pref[i] = v

        # suff[i]: longest suffix of pattern matching s ending at i
        rev_pat = pattern[::-1]
        rev_s = s[::-1]
        combined2 = rev_pat + "#" + rev_s
        z2 = z_function(combined2)
        suff = [0] * n
        for i in range(n):
            rev_idx = n - 1 - i
            v = z2[offset + rev_idx]
            if v > m:
                v = m
            suff[i] = v

        limit = n - m
        need = m - 1
        for start in range(limit + 1):
            if pref[start] + suff[start + m - 1] >= need:
                return start
        return -1
```

## Python3

```python
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)

        def z_algorithm(t: str):
            L = len(t)
            z = [0] * L
            l = r = 0
            for i in range(1, L):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < L and t[z[i]] == t[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            z[0] = L
            return z

        # dp1: longest prefix of pattern matching s starting at each position
        concat1 = pattern + "#" + s
        z1 = z_algorithm(concat1)
        dp1 = [0] * n
        offset1 = m + 1
        for i in range(n):
            val = z1[offset1 + i]
            if val > m:
                val = m
            dp1[i] = val

        # dp2: longest suffix of pattern matching s ending at each position
        rev_s = s[::-1]
        rev_pat = pattern[::-1]
        concat2 = rev_pat + "#" + rev_s
        z2 = z_algorithm(concat2)
        dp2 = [0] * n
        offset2 = m + 1
        for i in range(n):
            rev_idx = n - 1 - i
            val = z2[offset2 + rev_idx]
            if val > m:
                val = m
            dp2[i] = val

        # check each window
        for start in range(n - m + 1):
            end = start + m - 1
            if dp1[start] == m:
                return start
            if dp1[start] + dp2[end] >= m - 1:
                return start
        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void computeZ(const char *str, int len, int *z) {
    z[0] = len;
    int l = 0, r = 0;
    for (int i = 1; i < len; ++i) {
        if (i <= r)
            z[i] = (r - i + 1 < z[i - l]) ? r - i + 1 : z[i - l];
        else
            z[i] = 0;
        while (i + z[i] < len && str[z[i]] == str[i + z[i]])
            ++z[i];
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
}

int minStartingIndex(char* s, char* pattern) {
    int n = strlen(s);
    int m = strlen(pattern);
    if (m > n) return -1;

    // dp1: longest prefix match of pattern starting at each position in s
    int totalLen1 = m + 1 + n;
    char *concat1 = (char *)malloc(totalLen1 + 1);
    memcpy(concat1, pattern, m);
    concat1[m] = '#';
    memcpy(concat1 + m + 1, s, n);
    concat1[totalLen1] = '\0';

    int *z1 = (int *)malloc((totalLen1) * sizeof(int));
    computeZ(concat1, totalLen1, z1);

    int *dp1 = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int val = z1[m + 1 + i];
        dp1[i] = (val > m) ? m : val;
    }

    // reverse strings for suffix matches
    char *rev_s = (char *)malloc(n + 1);
    char *rev_p = (char *)malloc(m + 1);
    for (int i = 0; i < n; ++i) rev_s[i] = s[n - 1 - i];
    rev_s[n] = '\0';
    for (int i = 0; i < m; ++i) rev_p[i] = pattern[m - 1 - i];
    rev_p[m] = '\0';

    int totalLen2 = m + 1 + n;
    char *concat2 = (char *)malloc(totalLen2 + 1);
    memcpy(concat2, rev_p, m);
    concat2[m] = '#';
    memcpy(concat2 + m + 1, rev_s, n);
    concat2[totalLen2] = '\0';

    int *z2 = (int *)malloc((totalLen2) * sizeof(int));
    computeZ(concat2, totalLen2, z2);

    int *dp2 = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        // position in reversed s corresponding to original index i
        int revPos = n - 1 - i;
        int val = z2[m + 1 + revPos];
        dp2[i] = (val > m) ? m : val;
    }

    // search for minimal starting index
    for (int i = 0; i <= n - m; ++i) {
        if (dp1[i] == m) {               // exact match
            free(concat1); free(z1); free(dp1);
            free(rev_s); free(rev_p); free(concat2); free(z2); free(dp2);
            return i;
        }
        int endIdx = i + m - 1;
        if (dp1[i] + dp2[endIdx] >= m - 1) {
            free(concat1); free(z1); free(dp1);
            free(rev_s); free(rev_p); free(concat2); free(z2); free(dp2);
            return i;
        }
    }

    free(concat1); free(z1); free(dp1);
    free(rev_s); free(rev_p); free(concat2); free(z2); free(dp2);
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinStartingIndex(string s, string pattern) {
        int n = s.Length;
        int m = pattern.Length;
        if (m > n) return -1;

        int[] dp1 = new int[n];
        int[] dp2 = new int[n];

        // Prefix matches
        string combined = pattern + "#" + s;
        int[] z = Z(combined);
        for (int i = 0; i < n; i++) {
            int v = z[m + 1 + i];
            if (v > m) v = m;
            dp1[i] = v;
        }

        // Suffix matches using reversed strings
        char[] revSArr = s.ToCharArray();
        Array.Reverse(revSArr);
        string revS = new string(revSArr);

        char[] revPatArr = pattern.ToCharArray();
        Array.Reverse(revPatArr);
        string revPattern = new string(revPatArr);

        string combined2 = revPattern + "#" + revS;
        int[] z2 = Z(combined2);
        for (int i = 0; i < n; i++) {
            int revIdx = n - 1 - i;
            int v = z2[m + 1 + revIdx];
            if (v > m) v = m;
            dp2[i] = v;
        }

        // Check each window
        for (int i = 0; i <= n - m; i++) {
            if (dp1[i] + dp2[i + m - 1] >= m - 1) return i;
        }
        return -1;
    }

    private int[] Z(string str) {
        int len = str.Length;
        int[] z = new int[len];
        int l = 0, r = 0;
        for (int i = 1; i < len; i++) {
            if (i <= r) z[i] = Math.Min(r - i + 1, z[i - l]);
            while (i + z[i] < len && str[z[i]] == str[i + z[i]]) z[i]++;
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} pattern
 * @return {number}
 */
var minStartingIndex = function(s, pattern) {
    const n = s.length;
    const m = pattern.length;
    if (m > n) return -1;

    // Z-algorithm
    const zAlgorithm = (str) => {
        const len = str.length;
        const z = new Array(len).fill(0);
        let l = 0, r = 0;
        for (let i = 1; i < len; i++) {
            if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);
            while (i + z[i] < len && str[z[i]] === str[i + z[i]]) z[i]++;
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        z[0] = len;
        return z;
    };

    // dp1: longest prefix of pattern matching s starting at i
    const concat1 = pattern + "#" + s;
    const z1 = zAlgorithm(concat1);
    const offset1 = m + 1; // start index of s in concat1
    const dp1 = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        let val = z1[offset1 + i];
        if (val > m) val = m;
        dp1[i] = val;
    }

    // dp2: longest suffix of pattern matching s ending at i
    const revS = s.split('').reverse().join('');
    const revP = pattern.split('').reverse().join('');
    const concat2 = revP + "#" + revS;
    const z2 = zAlgorithm(concat2);
    const offset2 = m + 1; // start index of revS in concat2
    const dp2 = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        const revIdx = n - 1 - i;
        let val = z2[offset2 + revIdx];
        if (val > m) val = m;
        dp2[i] = val;
    }

    // Scan windows
    for (let start = 0; start <= n - m; start++) {
        const end = start + m - 1;
        if (dp1[start] >= m) return start;                     // exact match
        if (dp1[start] + dp2[end] >= m - 1) return start;      // at most one mismatch
    }
    return -1;
};
```

## Typescript

```typescript
function minStartingIndex(s: string, pattern: string): number {
    const n = s.length;
    const m = pattern.length;
    if (m > n) return -1;

    // Z-function implementation
    function zFunction(str: string): Int32Array {
        const len = str.length;
        const z = new Int32Array(len);
        let l = 0, r = 0;
        for (let i = 1; i < len; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < len && str.charCodeAt(z[i]) === str.charCodeAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        z[0] = len;
        return z;
    }

    // Prefix matches: longest common prefix of s[i...] and pattern
    const concat1 = pattern + "#" + s;
    const z1 = zFunction(concat1);
    const pref = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        let v = z1[m + 1 + i];
        if (v > m) v = m;
        pref[i] = v;
    }

    // Suffix matches: longest common suffix ending at each position
    const revPattern = pattern.split('').reverse().join('');
    const revS = s.split('').reverse().join('');
    const concat2 = revPattern + "#" + revS;
    const z2 = zFunction(concat2);
    const suff = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        const idxRev = n - 1 - i;
        let v = z2[m + 1 + idxRev];
        if (v > m) v = m;
        suff[i] = v;
    }

    // Check each window
    for (let start = 0; start <= n - m; start++) {
        const leftMatch = pref[start];
        const rightMatch = suff[start + m - 1];
        if (leftMatch + rightMatch >= m - 1) return start;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $pattern
     * @return Integer
     */
    function minStartingIndex($s, $pattern) {
        $n = strlen($s);
        $m = strlen($pattern);
        if ($m > $n) return -1;

        // Z-algorithm helper
        $zFunc = function(string $str): array {
            $len = strlen($str);
            $z = array_fill(0, $len, 0);
            $l = 0;
            $r = 0;
            for ($i = 1; $i < $len; $i++) {
                if ($i <= $r) {
                    $z[$i] = min($r - $i + 1, $z[$i - $l]);
                }
                while ($i + $z[$i] < $len && $str[$z[$i]] === $str[$i + $z[$i]]) {
                    $z[$i]++;
                }
                if ($i + $z[$i] - 1 > $r) {
                    $l = $i;
                    $r = $i + $z[$i] - 1;
                }
            }
            $z[0] = $len;
            return $z;
        };

        // dp1: longest prefix of pattern matching s starting at i
        $combined1 = $pattern . '#' . $s;
        $z1 = $zFunc($combined1);
        $dp1 = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = $m + 1 + $i;
            $val = $z1[$idx];
            if ($val > $m) $val = $m;
            $dp1[$i] = $val;
        }

        // dp2: longest suffix of pattern matching s ending at i
        $revPattern = strrev($pattern);
        $revS = strrev($s);
        $combined2 = $revPattern . '#' . $revS;
        $z2 = $zFunc($combined2);
        $dp2 = array_fill(0, $n, 0);
        for ($iRev = 0; $iRev < $n; $iRev++) {
            $idx = $m + 1 + $iRev;
            $val = $z2[$idx];
            if ($val > $m) $val = $m;
            $origIdx = $n - 1 - $iRev;
            $dp2[$origIdx] = $val;
        }

        // Scan possible starts
        for ($start = 0; $start <= $n - $m; $start++) {
            $pref = $dp1[$start];
            if ($pref == $m) {
                return $start; // exact match
            }
            $suffixLen = $dp2[$start + $m - 1];
            if ($pref + $suffixLen >= $m - 1) {
                return $start;
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minStartingIndex(_ s: String, _ pattern: String) -> Int {
        let sBytes = Array(s.utf8)
        let pBytes = Array(pattern.utf8)
        let n = sBytes.count
        let m = pBytes.count
        if m > n { return -1 }
        
        func computeZ(_ arr: [UInt8]) -> [Int] {
            let len = arr.count
            var z = Array(repeating: 0, count: len)
            var l = 0, r = 0
            for i in 1..<len {
                if i <= r {
                    z[i] = min(r - i + 1, z[i - l])
                }
                while i + z[i] < len && arr[z[i]] == arr[i + z[i]] {
                    z[i] += 1
                }
                if i + z[i] - 1 > r {
                    l = i
                    r = i + z[i] - 1
                }
            }
            return z
        }
        
        // Prefix matches
        var combined = pBytes
        combined.append(0)               // separator not present in lowercase letters
        combined += sBytes
        let zPref = computeZ(combined)
        var pref = Array(repeating: 0, count: n)
        for i in 0..<n {
            let matchLen = min(zPref[m + 1 + i], m)
            pref[i] = matchLen
        }
        
        // Suffix matches via reversed strings
        let revP = pBytes.reversed()
        let revS = sBytes.reversed()
        var combinedRev = Array(revP)
        combinedRev.append(0)
        combinedRev += Array(revS)
        let zSuf = computeZ(combinedRev)
        var suff = Array(repeating: 0, count: n)
        for i in 0..<n {
            let matchLen = min(zSuf[m + 1 + i], m)
            let origIdx = n - 1 - i
            suff[origIdx] = matchLen
        }
        
        // Scan windows
        for start in 0...(n - m) {
            let leftMatch = pref[start]
            if leftMatch == m { return start }               // exact match
            let rightMatch = suff[start + m - 1]
            if leftMatch + rightMatch >= m - 1 {
                return start
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minStartingIndex(s: String, pattern: String): Int {
        val n = s.length
        val m = pattern.length
        if (m == 1) return 0

        // Prefix matches
        val combined1 = pattern + "#" + s
        val z1 = zFunction(combined1)
        val prefMatch = IntArray(n)
        for (i in 0 until n) {
            var v = z1[m + 1 + i]
            if (v > m) v = m
            prefMatch[i] = v
        }

        // Suffix matches using reversed strings
        val revPattern = pattern.reversed()
        val revS = s.reversed()
        val combined2 = revPattern + "#" + revS
        val z2 = zFunction(combined2)
        val suffMatch = IntArray(n)
        for (i in 0 until n) {
            val revIdx = n - 1 - i
            var v = z2[m + 1 + revIdx]
            if (v > m) v = m
            suffMatch[i] = v
        }

        for (i in 0..n - m) {
            val pref = prefMatch[i]
            if (pref == m) return i
            val endIdx = i + m - 1
            val suf = suffMatch[endIdx]
            if (pref + suf == m - 1) return i
        }
        return -1
    }

    private fun zFunction(str: String): IntArray {
        val n = str.length
        val z = IntArray(n)
        var l = 0
        var r = 0
        for (i in 1 until n) {
            if (i <= r) {
                z[i] = kotlin.math.min(r - i + 1, z[i - l])
            }
            while (i + z[i] < n && str[z[i]] == str[i + z[i]]) {
                z[i]++
            }
            if (i + z[i] - 1 > r) {
                l = i
                r = i + z[i] - 1
            }
        }
        z[0] = n
        return z
    }
}
```

## Dart

```dart
class Solution {
  int minStartingIndex(String s, String pattern) {
    int n = s.length;
    int m = pattern.length;
    if (m > n) return -1;

    List<int> pref = _prefixMatches(s, pattern);
    List<int> suff = _suffixMatches(s, pattern);

    for (int i = 0; i <= n - m; ++i) {
      int preLen = pref[i];
      if (preLen == m) return i;
      int endIdx = i + m - 1;
      int sufLen = suff[endIdx];
      if (preLen + 1 + sufLen >= m) return i;
    }
    return -1;
  }

  List<int> _prefixMatches(String s, String pattern) {
    int n = s.length;
    int m = pattern.length;
    String combined = pattern + "#" + s;
    List<int> z = _zFunction(combined);
    List<int> pref = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int pos = m + 1 + i;
      int val = z[pos];
      if (val > m) val = m;
      pref[i] = val;
    }
    return pref;
  }

  List<int> _suffixMatches(String s, String pattern) {
    int n = s.length;
    int m = pattern.length;
    String revPattern = _reverse(pattern);
    String revS = _reverse(s);
    String combined = revPattern + "#" + revS;
    List<int> z = _zFunction(combined);
    List<int> suff = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int pos = m + 1 + i;
      int val = z[pos];
      if (val > m) val = m;
      int origIdx = n - 1 - i;
      suff[origIdx] = val;
    }
    return suff;
  }

  String _reverse(String str) {
    List<int> codes = str.codeUnits.reversed.toList();
    return String.fromCharCodes(codes);
  }

  List<int> _zFunction(String s) {
    int n = s.length;
    List<int> z = List.filled(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
      if (i <= r) {
        int k = i - l;
        int bound = r - i + 1;
        z[i] = (z[k] < bound) ? z[k] : bound;
      }
      while (i + z[i] < n && s.codeUnitAt(z[i]) == s.codeUnitAt(i + z[i])) {
        z[i]++;
      }
      if (i + z[i] - 1 > r) {
        l = i;
        r = i + z[i] - 1;
      }
    }
    return z;
  }
}
```

## Golang

```go
func minStartingIndex(s string, pattern string) int {
    n, m := len(s), len(pattern)
    if m > n {
        return -1
    }
    // Z algorithm helper
    zAlg := func(str string) []int {
        l := len(str)
        z := make([]int, l)
        left, right := 0, 0
        for i := 1; i < l; i++ {
            if i <= right {
                if z[i-left] < right-i+1 {
                    z[i] = z[i-left]
                } else {
                    z[i] = right - i + 1
                }
            }
            for i+z[i] < l && str[z[i]] == str[i+z[i]] {
                z[i]++
            }
            if i+z[i]-1 > right {
                left, right = i, i+z[i]-1
            }
        }
        return z
    }

    // dp1: prefix matches of pattern starting at each position in s
    combined := pattern + "#" + s
    z1 := zAlg(combined)
    dp1 := make([]int, n)
    offset := m + 1
    for i := 0; i < n; i++ {
        val := z1[offset+i]
        if val > m {
            val = m
        }
        dp1[i] = val
    }

    // reverse strings for suffix matches
    rev := func(str string) string {
        b := []byte(str)
        for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
            b[i], b[j] = b[j], b[i]
        }
        return string(b)
    }

    revS := rev(s)
    revP := rev(pattern)
    combined2 := revP + "#" + revS
    z2 := zAlg(combined2)
    dp2 := make([]int, n) // suffix match length ending at each index in original s
    for i := 0; i < n; i++ {
        val := z2[offset+i]
        if val > m {
            val = m
        }
        origEnd := n - 1 - i
        dp2[origEnd] = val
    }

    // scan windows
    for i := 0; i <= n-m; i++ {
        leftMatch := dp1[i]
        if leftMatch == m {
            return i
        }
        rightMatch := dp2[i+m-1]
        if leftMatch+rightMatch >= m-1 {
            return i
        }
    }
    return -1
}
```

## Ruby

```ruby
def min_starting_index(s, pattern)
  n = s.length
  m = pattern.length
  return -1 if m > n

  # Z-algorithm
  z_algo = lambda do |str|
    l = str.length
    z = Array.new(l, 0)
    left = right = 0
    (1...l).each do |i|
      if i <= right
        z[i] = [right - i + 1, z[i - left]].min
      end
      while i + z[i] < l && str[z[i]] == str[i + z[i]]
        z[i] += 1
      end
      if i + z[i] - 1 > right
        left = i
        right = i + z[i] - 1
      end
    end
    z[0] = l
    z
  end

  # dp1: longest prefix match of pattern starting at each position in s
  combined = pattern + "#" + s
  z1 = z_algo.call(combined)
  offset = m + 1
  dp1 = Array.new(n, 0)
  (0...n).each do |i|
    dp1[i] = [z1[offset + i], m].min
  end

  # dp2: longest suffix match of pattern ending at each position in s
  rev_p = pattern.reverse
  rev_s = s.reverse
  combined_rev = rev_p + "#" + rev_s
  z2 = z_algo.call(combined_rev)
  offset2 = m + 1
  dp2 = Array.new(n, 0)
  (0...n).each do |j|
    rev_idx = n - 1 - j
    dp2[j] = [z2[offset2 + rev_idx], m].min
  end

  (0..n - m).each do |i|
    pref = dp1[i]
    if pref == m
      return i
    else
      needed_suffix = m - pref - 1
      if needed_suffix <= dp2[i + m - 1]
        return i
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def minStartingIndex(s: String, pattern: String): Int = {
        val n = s.length
        val m = pattern.length
        if (m == 0) return -1

        // Z-algorithm
        def computeZ(str: String): Array[Int] = {
            val len = str.length
            val z = new Array[Int](len)
            var l = 0
            var r = 0
            var i = 1
            while (i < len) {
                if (i <= r) {
                    z(i) = math.min(r - i + 1, z(i - l))
                }
                while (i + z(i) < len && str.charAt(z(i)) == str.charAt(i + z(i))) {
                    z(i) += 1
                }
                if (i + z(i) - 1 > r) {
                    l = i
                    r = i + z(i) - 1
                }
                i += 1
            }
            z
        }

        // dp1: longest prefix match starting at each position in s
        val concat1 = pattern + "#" + s
        val z1 = computeZ(concat1)
        val offset1 = m + 1
        val dp1 = new Array[Int](n)
        var idx = 0
        while (idx < n) {
            var v = z1(offset1 + idx)
            if (v > m) v = m
            dp1(idx) = v
            idx += 1
        }

        // dp2: longest suffix match ending at each position in s
        val revPattern = pattern.reverse
        val revS = s.reverse
        val concat2 = revPattern + "#" + revS
        val z2 = computeZ(concat2)
        val offset2 = m + 1
        val dp2 = new Array[Int](n)
        idx = 0
        while (idx < n) {
            val revIdx = n - 1 - idx
            var v = z2(offset2 + revIdx)
            if (v > m) v = m
            dp2(idx) = v
            idx += 1
        }

        // check each window
        var start = 0
        while (start <= n - m) {
            val pref = dp1(start)
            val suff = dp2(start + m - 1)
            if (pref + suff >= m - 1) return start
            start += 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_starting_index(s: String, pattern: String) -> i32 {
        let n = s.len();
        let m = pattern.len();
        if m == 0 || n < m {
            return -1;
        }
        let sb = s.as_bytes();
        let pb = pattern.as_bytes();

        // Z-function helper
        fn z_function(arr: &[u8]) -> Vec<usize> {
            let n = arr.len();
            let mut z = vec![0usize; n];
            let (mut l, mut r) = (0usize, 0usize);
            for i in 1..n {
                if i <= r {
                    z[i] = std::cmp::min(r - i + 1, z[i - l]);
                }
                while i + z[i] < n && arr[z[i]] == arr[i + z[i]] {
                    z[i] += 1;
                }
                if i + z[i] - 1 > r {
                    l = i;
                    r = i + z[i] - 1;
                }
            }
            z[0] = n;
            z
        }

        // prefix matches: longest prefix of pattern matching s starting at each position
        let mut combined = Vec::with_capacity(m + 1 + n);
        combined.extend_from_slice(pb);
        combined.push(b'#');
        combined.extend_from_slice(sb);
        let z = z_function(&combined);
        let offset = m + 1;
        let mut pref = vec![0usize; n];
        for i in 0..n {
            pref[i] = std::cmp::min(z[offset + i], m);
        }

        // suffix matches: longest suffix of pattern matching s ending at each position
        let rev_s: Vec<u8> = sb.iter().rev().cloned().collect();
        let rev_p: Vec<u8> = pb.iter().rev().cloned().collect();
        let mut combined_rev = Vec::with_capacity(m + 1 + n);
        combined_rev.extend_from_slice(&rev_p);
        combined_rev.push(b'#');
        combined_rev.extend_from_slice(&rev_s);
        let z2 = z_function(&combined_rev);
        let offset2 = m + 1;
        let mut suff = vec![0usize; n];
        for j in 0..n {
            let len = std::cmp::min(z2[offset2 + j], m);
            let orig_idx = n - 1 - j;
            suff[orig_idx] = len;
        }

        // check each window
        for start in 0..=n - m {
            let pref_len = pref[start];
            let suff_len = suff[start + m - 1];
            if pref_len + suff_len >= m - 1 {
                return start as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
#lang racket
(provide min-starting-index)

;; Z-function: returns a vector where z[i] is the length of the longest substring
;; starting at i that is also a prefix of the whole string.
(define (z-function str)
  (let* ((n (string-length str))
         (z (make-vector n 0)))
    (let loop ((i 1) (l 0) (r 0))
      (when (< i n)
        (if (< i r)
            (vector-set! z i (min (- r i) (vector-ref z (- i l))))
            (vector-set! z i 0))
        ;; expand
        (let expand ((k (vector-ref z i)))
          (when (and (< (+ i k) n)
                     (char=? (string-ref str (+ i k))
                             (string-ref str k)))
            (vector-set! z i (+ k 1))
            (expand (+ k 1))))
        (when (> (+ i (vector-ref z i)) r)
          (set! l i)
          (set! r (+ i (vector-ref z i))))
        (loop (+ i 1) l r)))
    z))

(define/contract (min-starting-index s pattern)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s))
         (m (string-length pattern))
         ;; dp1: longest prefix match of pattern starting at each position in s
         (dp1 (make-vector n 0))
         ;; compute Z on pattern#s
         (combined (string-append pattern "#" s))
         (z1 (z-function combined)))
    (for ([i (in-range n)])
      (let ((val (vector-ref z1 (+ m 1 i))))
        (vector-set! dp1 i (if (> val m) m val))))
    ;; dp2: longest suffix match of pattern ending at each position in s
    (define rev-s (list->string (reverse (string->list s))))
    (define rev-pat (list->string (reverse (string->list pattern))))
    (define combined2 (string-append rev-pat "#" rev-s))
    (define z2 (z-function combined2))
    (define dp2 (make-vector n 0))
    (for ([i (in-range n)])
      (let* ((rev-index (- n 1 i)) ; position in reversed s
             (val (vector-ref z2 (+ m 1 rev-index))))
        (vector-set! dp2 i (if (> val m) m val))))
    ;; search for minimal index with at most one mismatch
    (let loop ((i 0))
      (cond
        [(> i (- n m)) -1] ; no more windows
        [else
         (define l (vector-ref dp1 i))
         (define r (vector-ref dp2 (+ i m -1)))
         (if (or (= l m) (>= (+ l r) (- m 1)))
             i
             (loop (+ i 1)))]))))
```

## Erlang

```erlang
-spec min_starting_index(S :: unicode:unicode_binary(), Pattern :: unicode:unicode_binary()) -> integer().
min_starting_index(S, Pattern) ->
    SList = binary_to_list(S),
    PList = binary_to_list(Pattern),
    N = length(SList),
    M = length(PList),
    case M > N of
        true -> -1;
        false ->
            PrefArr = compute_pref(SList, PList, N, M),
            SuffArr = compute_suff(SList, PList, N, M),
            find_index(PrefArr, SuffArr, N, M)
    end.

%% build prefix match lengths
compute_pref(SList, PList, N, M) ->
    Concat = PList ++ [$#] ++ SList,
    ZArr = z_algorithm(Concat),
    PrefList = [min(array:get(M + 1 + I, ZArr), M) || I <- lists:seq(0, N - 1)],
    array:from_list(PrefList).

%% build suffix match lengths
compute_suff(SList, PList, N, M) ->
    RevS = lists:reverse(SList),
    RevP = lists:reverse(PList),
    Concat = RevP ++ [$#] ++ RevS,
    ZArr = z_algorithm(Concat),
    SuffList = [min(array:get(M + 1 + (N - 1 - I), ZArr), M) || I <- lists:seq(0, N - 1)],
    array:from_list(SuffList).

find_index(Pref, Suff, N, M) ->
    MaxStart = N - M,
    find_loop(0, MaxStart, Pref, Suff, M).

find_loop(I, Max, _Pref, _Suff, _M) when I > Max -> -1;
find_loop(I, Max, Pref, Suff, M) ->
    L = array:get(I, Pref),
    case L of
        L when L == M -> I;
        _ ->
            RIdx = I + M - 1,
            Suf = array:get(RIdx, Suff),
            if L + Suf >= M - 1 -> I; true -> find_loop(I + 1, Max, Pref, Suff, M) end
    end.

%% Z-algorithm returning an array of Z-values
z_algorithm(List) ->
    TArr = array:from_list(List),
    Len = array:size(TArr),
    Z0 = array:new(Len, {default, 0}),
    z_loop(1, Len, 0, -1, TArr, Z0).

z_loop(I, Len, Lb, Rb, TArr, ZArr) when I >= Len ->
    ZArr;
z_loop(I, Len, Lb, Rb, TArr, ZArr) ->
    {ZVal, NewL, NewR} =
        if
            I > Rb ->
                Z1 = count_match(TArr, I, 0),
                {Z1, I, I + Z1 - 1};
            true ->
                K = I - Lb,
                Beta = Rb - I + 1,
                Zk = array:get(K, ZArr),
                if
                    Zk < Beta ->
                        {Zk, Lb, Rb};
                    true ->
                        Z1 = count_match(TArr, I, Beta),
                        {Z1, I, I + Z1 - 1}
                end
        end,
    ZArr2 = array:set(I, ZVal, ZArr),
    case NewR > Rb of
        true -> z_loop(I + 1, Len, NewL, NewR, TArr, ZArr2);
        false -> z_loop(I + 1, Len, Lb, Rb, TArr, ZArr2)
    end.

count_match(TArr, I, Cur) ->
    Len = array:size(TArr),
    count_match_loop(I, Cur, Len, TArr).

count_match_loop(I, Cur, Len, _TArr) when I + Cur >= Len -> Cur;
count_match_loop(I, Cur, Len, TArr) ->
    Char1 = array:get(Cur, TArr),
    Char2 = array:get(I + Cur, TArr),
    if
        Char1 == Char2 -> count_match_loop(I, Cur + 1, Len, TArr);
        true -> Cur
    end.

min(A, B) when A < B -> A;
min(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_starting_index(s :: String.t(), pattern :: String.t()) :: integer()
  def min_starting_index(s, pattern) do
    n = byte_size(s)
    m = byte_size(pattern)

    if m > n do
      -1
    else
      base = 91138233
      mod1 = 1_000_000_007
      mod2 = 1_000_000_009

      pow1 = build_pow(max(n, m), base, mod1)
      pow2 = build_pow(max(n, m), base, mod2)

      pref_s1 = build_prefix_hash(s, base, mod1)
      pref_s2 = build_prefix_hash(s, base, mod2)

      pref_p1 = build_prefix_hash(pattern, base, mod1)
      pref_p2 = build_prefix_hash(pattern, base, mod2)

      0..(n - m)
      |> Enum.reduce_while(-1, fn i, _acc ->
        lcp =
          longest_common_prefix(
            i,
            m,
            pref_s1,
            pref_p1,
            pow1,
            mod1,
            pref_s2,
            pref_p2,
            pow2,
            mod2
          )

        cond do
          lcp == m ->
            {:halt, i}

          true ->
            # check suffix after the mismatching character
            rem_len = m - lcp - 1

            if rem_len < 0 do
              {:cont, -1}
            else
              s_start = i + lcp + 1
              p_start = lcp + 1

              hash_s1 = get_sub_hash(pref_s1, s_start, i + m - 1, pow1, mod1)
              hash_p1 = get_sub_hash(pref_p1, p_start, m - 1, pow1, mod1)

              hash_s2 = get_sub_hash(pref_s2, s_start, i + m - 1, pow2, mod2)
              hash_p2 = get_sub_hash(pref_p2, p_start, m - 1, pow2, mod2)

              if hash_s1 == hash_p1 and hash_s2 == hash_p2 do
                {:halt, i}
              else
                {:cont, -1}
              end
            end
        end
      end)
    end
  end

  # Build prefix hash array (length = len+1), pref[0]=0
  defp build_prefix_hash(str, base, mod) do
    bytes = :binary.bin_to_list(str)

    {pref_rev, _} =
      Enum.reduce(bytes, {[0], 0}, fn byte, {acc, h} ->
        nh = rem(h * base + byte, mod)
        {[nh | acc], nh}
      end)

    Enum.reverse(pref_rev)
  end

  # Build powers array pow[i] = base^i % mod for i=0..len
  defp build_pow(len, base, mod) do
    {pow_rev, _} =
      Enum.reduce(1..len, {[1], 1}, fn _, {acc, cur} ->
        nxt = rem(cur * base, mod)
        {[nxt | acc], nxt}
      end)

    Enum.reverse(pow_rev)
  end

  # Get hash of substring [l, r] inclusive using prefix array and powers
  defp get_sub_hash(pref, l, r, pow, mod) do
    res = rem(pref[r + 1] - rem(pref[l] * pow[r - l + 1], mod), mod)

    if res < 0, do: res + mod, else: res
  end

  # Binary search longest common prefix length between s[i..] and pattern[0..]
  defp longest_common_prefix(i, m, pref_s1, pref_p1, pow1, mod1, pref_s2, pref_p2, pow2, mod2) do
    lcp_binsearch(0, m, i, pref_s1, pref_p1, pow1, mod1, pref_s2, pref_p2, pow2, mod2)
  end

  defp lcp_binsearch(low, high, _i, _ps1, _pp1, _pow1, _mod1, _ps2, _pp2, _pow2, _mod2)
       when low == high,
       do: low

  defp lcp_binsearch(low, high, i, ps1, pp1, pow1, mod1, ps2, pp2, pow2, mod2) do
    mid = div(low + high + 1, 2)

    hash_s1 = get_sub_hash(ps1, i, i + mid - 1, pow1, mod1)
    hash_p1 = get_sub_hash(pp1, 0, mid - 1, pow1, mod1)

    hash_s2 = get_sub_hash(ps2, i, i + mid - 1, pow2, mod2)
    hash_p2 = get_sub_hash(pp2, 0, mid - 1, pow2, mod2)

    if hash_s1 == hash_p1 and hash_s2 == hash_p2 do
      lcp_binsearch(mid, high, i, ps1, pp1, pow1, mod1, ps2, pp2, pow2, mod2)
    else
      lcp_binsearch(low, mid - 1, i, ps1, pp1, pow1, mod1, ps2, pp2, pow2, mod2)
    end
  end
end
```
