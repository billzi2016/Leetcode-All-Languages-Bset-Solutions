# 2565. Subsequence With the Minimum Score

## Cpp

```cpp
class Solution {
public:
    int minimumScore(string s, string t) {
        int n = s.size(), m = t.size();
        vector<int> pref(m);
        int p = 0;
        for (int i = 0; i < m; ++i) {
            while (p < n && s[p] != t[i]) ++p;
            if (p == n) pref[i] = n;
            else {
                pref[i] = p;
                ++p;
            }
        }
        // If whole t is already a subsequence
        if (pref[m - 1] != n) return 0;

        vector<int> suff(m + 1, -1);
        suff[m] = n; // empty suffix matches after the end
        int q = n - 1;
        for (int i = m - 1; i >= 0; --i) {
            while (q >= 0 && s[q] != t[i]) --q;
            if (q < 0) suff[i] = -1;
            else {
                suff[i] = q;
                --q;
            }
        }

        int ans = m; // remove all characters
        for (int i = 0; i < m; ++i) {
            int leftPos = (i == 0 ? -1 : pref[i - 1]);
            if (leftPos == n) continue; // prefix cannot be matched
            // find smallest k >= i such that suff[k] > leftPos
            auto it = lower_bound(suff.begin() + i, suff.end(), leftPos + 1);
            int k = it - suff.begin();
            ans = min(ans, k - i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumScore(String s, String t) {
        int n = s.length();
        int m = t.length();
        int[] left = new int[m];
        int p = 0;
        // compute earliest positions for prefixes of t
        for (int i = 0; i < m; i++) {
            while (p < n && s.charAt(p) != t.charAt(i)) p++;
            if (p == n) {
                for (int k = i; k < m; k++) left[k] = n;
                break;
            }
            left[i] = p;
            p++;
        }

        int[] right = new int[m];
        p = n - 1;
        // compute latest positions for suffixes of t
        for (int i = m - 1; i >= 0; i--) {
            while (p >= 0 && s.charAt(p) != t.charAt(i)) p--;
            if (p < 0) {
                for (int k = i; k >= 0; k--) right[k] = -1;
                break;
            }
            right[i] = p;
            p--;
        }

        int answer = m; // remove all characters

        // keep only suffix
        for (int j = 0; j < m; j++) {
            if (right[j] != -1) {
                answer = Math.min(answer, j);
            }
        }
        // keep only prefix
        for (int i = 0; i < m; i++) {
            if (left[i] != n) {
                answer = Math.min(answer, m - (i + 1));
            }
        }

        // collect valid suffix positions with their indices
        int[] rightPos = new int[m];
        int[] rightIdx = new int[m];
        int cntR = 0;
        for (int i = 0; i < m; i++) {
            if (right[i] != -1) {
                rightPos[cntR] = right[i];
                rightIdx[cntR] = i;
                cntR++;
            }
        }

        // combine prefix and suffix
        for (int i = 0; i < m; i++) {
            if (left[i] == n) continue;
            int lpos = left[i];
            // binary search first suffix with position > lpos
            int lo = 0, hi = cntR;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (rightPos[mid] > lpos) hi = mid;
                else lo = mid + 1;
            }
            if (lo == cntR) {
                // no suffix after this prefix, already considered by removing suffix
                continue;
            }
            int j = rightIdx[lo];
            answer = Math.min(answer, j - i - 1);
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumScore(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        # pref[i]: earliest index in s where t[:i+1] can be matched
        pref = [-1] * m
        j = 0
        for i, ch in enumerate(s):
            if j < m and ch == t[j]:
                pref[j] = i
                j += 1
        # If whole t is already a subsequence
        if pref[-1] != -1:
            return 0

        # suff[i]: latest index in s where t[i:] can be matched (position of t[i])
        suff = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                suff[j] = i
                j -= 1

        ans = m  # worst case: remove entire t
        r = 0
        for l in range(m + 1):  # l is start index of removal interval
            left_pos = pref[l - 1] if l > 0 else -1
            if r < l:
                r = l
            while r < m and suff[r] <= left_pos:
                r += 1
            ans = min(ans, r - l)  # length of removed segment
        return ans
```

## Python3

```python
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        # pref[i]: earliest index in s matching t[:i]
        pref = [-1] * (m + 1)
        pos = 0
        for i in range(m):
            while pos < n and s[pos] != t[i]:
                pos += 1
            if pos == n:
                pref[i + 1] = n  # impossible
            else:
                pref[i + 1] = pos
                pos += 1

        # suff[i]: latest index in s matching t[i:]
        suff = [n] * (m + 1)
        pos = n - 1
        for i in range(m - 1, -1, -1):
            while pos >= 0 and s[pos] != t[i]:
                pos -= 1
            if pos < 0:
                suff[i] = -1  # impossible
            else:
                suff[i] = pos
                pos -= 1

        ans = m  # worst case: remove whole t
        for i in range(m + 1):
            if pref[i] == n:
                continue
            lo, hi = i, m
            best = m + 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if pref[i] < suff[mid]:
                    best = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            if best <= m:
                ans = min(ans, best - i)
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minimumScore(char* s, char* t) {
    int n = strlen(s);
    int m = strlen(t);
    int *pref = (int*)malloc(m * sizeof(int));
    int *suff = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) pref[i] = suff[i] = -1;

    // prefix matches
    int p = 0;
    for (int i = 0; i < m && p < n; ++i) {
        while (p < n && s[p] != t[i]) ++p;
        if (p == n) break;
        pref[i] = p;
        ++p;
    }

    // suffix matches
    p = n - 1;
    for (int i = m - 1; i >= 0 && p >= 0; --i) {
        while (p >= 0 && s[p] != t[i]) --p;
        if (p < 0) break;
        suff[i] = p;
        --p;
    }

    int ans = m; // remove all characters

    // Remove a prefix of t
    for (int j = 0; j < m; ++j) {
        if (suff[j] != -1) {
            if (j < ans) ans = j;
            break;
        }
    }

    // Remove a suffix of t
    for (int i = m - 1; i >= 0; --i) {
        if (pref[i] != -1) {
            int len = m - i - 1;
            if (len < ans) ans = len;
            break;
        }
    }

    // Remove a middle segment
    int j = 0;
    for (int i = 0; i < m; ++i) {
        if (pref[i] == -1) break;
        if (j <= i) j = i + 1;
        while (j < m && (suff[j] == -1 || suff[j] <= pref[i])) ++j;
        if (j < m) {
            int len = j - i - 1;
            if (len < ans) ans = len;
        }
    }

    free(pref);
    free(suff);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumScore(string s, string t) {
        int n = s.Length;
        int m = t.Length;
        int[] pref = new int[m];
        int[] suff = new int[m];

        // Compute prefix matches
        int p = 0;
        for (int i = 0; i < m; i++) {
            while (p < n && s[p] != t[i]) p++;
            if (p == n) {
                for (int k = i; k < m; k++) pref[k] = n; // sentinel for impossible
                break;
            }
            pref[i] = p;
            p++;
        }

        // Compute suffix matches
        int q = n - 1;
        for (int i = m - 1; i >= 0; i--) {
            while (q >= 0 && s[q] != t[i]) q--;
            if (q < 0) {
                for (int k = i; k >= 0; k--) suff[k] = -1; // sentinel
                break;
            }
            suff[i] = q;
            q--;
        }

        // Determine the farthest index where prefix can be matched
        int maxPrefIdx = -1;
        for (int i = 0; i < m; i++) {
            if (pref[i] == n) break;
            maxPrefIdx = i;
        }

        int answer = m; // delete whole t

        // Iterate over possible split points
        for (int i = -1; i <= maxPrefIdx; i++) {
            int leftPos = (i == -1) ? -1 : pref[i];

            // binary search the smallest j > i such that suff[j] > leftPos
            int lo = i + 1;
            int hi = m; // exclusive upper bound, using sentinel j=m with rightPos=n
            while (lo < hi) {
                int mid = (lo + hi) >> 1;
                int rightPos = (mid == m) ? n : suff[mid];
                if (rightPos > leftPos) {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }

            int j = lo; // minimal valid j
            answer = Math.Min(answer, j - i - 1);
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minimumScore = function(s, t) {
    const n = s.length, m = t.length;
    const pref = new Array(m).fill(-1);
    let p = 0;
    for (let i = 0; i < m; ++i) {
        while (p < n && s[p] !== t[i]) p++;
        if (p === n) break;
        pref[i] = p;
        p++;
    }
    // If whole t is already a subsequence
    if (pref[m - 1] !== -1) return 0;

    const suff = new Array(m).fill(-1);
    let q = n - 1;
    for (let i = m - 1; i >= 0; --i) {
        while (q >= 0 && s[q] !== t[i]) q--;
        if (q < 0) break;
        suff[i] = q;
        q--;
    }

    let ans = m; // delete all characters

    // Delete a prefix of t
    for (let j = 0; j < m; ++j) {
        if (suff[j] !== -1) {
            ans = Math.min(ans, j);
            break;
        }
    }

    // Delete a suffix of t
    for (let i = m - 1; i >= 0; --i) {
        if (pref[i] !== -1) {
            ans = Math.min(ans, m - 1 - i);
            break;
        }
    }

    // General case: delete middle segment [i, j-1]
    for (let i = 0; i < m; ++i) {
        const leftIdx = i === 0 ? -1 : pref[i - 1];
        if (i > 0 && leftIdx === -1) continue; // cannot keep prefix up to i-1

        let lo = i, hi = m - 1, pos = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (suff[mid] !== -1 && suff[mid] > leftIdx) {
                pos = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        if (pos !== -1) {
            ans = Math.min(ans, pos - i);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function minimumScore(s: string, t: string): number {
    const n = s.length;
    const m = t.length;
    const pref = new Array<number>(m).fill(-1);
    let si = 0;
    for (let ti = 0; ti < m; ti++) {
        while (si < n && s[si] !== t[ti]) si++;
        if (si === n) break;
        pref[ti] = si;
        si++;
    }
    const suff = new Array<number>(m).fill(-1);
    si = n - 1;
    for (let ti = m - 1; ti >= 0; ti--) {
        while (si >= 0 && s[si] !== t[ti]) si--;
        if (si < 0) break;
        suff[ti] = si;
        si--;
    }
    let ans = m; // remove all characters
    // Remove a prefix of t
    for (let i = 0; i < m; i++) {
        if (suff[i] !== -1) ans = Math.min(ans, i);
    }
    // Remove a suffix of t
    for (let i = m - 1; i >= 0; i--) {
        if (pref[i] !== -1) ans = Math.min(ans, m - 1 - i);
    }
    // Remove a middle segment
    for (let i = 0; i < m - 1; i++) {
        if (pref[i] === -1) continue;
        let l = i + 1, r = m - 1, pos = -1;
        while (l <= r) {
            const mid = (l + r) >> 1;
            if (suff[mid] !== -1 && suff[mid] > pref[i]) {
                pos = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        if (pos !== -1) ans = Math.min(ans, pos - i - 1);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function minimumScore($s, $t) {
        $n = strlen($s);
        $m = strlen($t);
        // left[i] = earliest index in s matching t[0..i]
        $left = array_fill(0, $m, -1);
        $p = 0;
        for ($i = 0; $i < $n && $p < $m; $i++) {
            if ($s[$i] === $t[$p]) {
                $left[$p] = $i;
                $p++;
            }
        }

        // right[i] = latest index in s matching t[i..m-1]
        $right = array_fill(0, $m, $n);
        $p = $m - 1;
        for ($i = $n - 1; $i >= 0 && $p >= 0; $i--) {
            if ($s[$i] === $t[$p]) {
                $right[$p] = $i;
                $p--;
            }
        }

        $ans = $m; // remove all characters
        for ($i = -1; $i < $m; $i++) {
            $leftPos = ($i == -1) ? -1 : $left[$i];
            if ($i != -1 && $leftPos == -1) continue; // prefix cannot be matched

            $lo = $i + 1;
            $hi = $m; // inclusive upper bound (represents empty suffix)
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                $rightPos = ($mid == $m) ? $n : $right[$mid];
                if ($rightPos > $leftPos) {
                    $hi = $mid;
                } else {
                    $lo = $mid + 1;
                }
            }
            $j = $lo; // first suffix start where condition holds
            $ans = min($ans, $j - $i - 1);
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumScore(_ s: String, _ t: String) -> Int {
        let sArr = Array(s)
        let tArr = Array(t)
        let m = sArr.count
        let n = tArr.count
        
        var left = [Int](repeating: -1, count: n)
        var right = [Int](repeating: -1, count: n)
        
        // earliest positions for prefixes of t in s
        var ti = 0
        for i in 0..<m {
            if ti < n && sArr[i] == tArr[ti] {
                left[ti] = i
                ti += 1
            }
        }
        
        // latest positions for suffixes of t in s
        ti = n - 1
        if n > 0 {
            for i in stride(from: m - 1, through: 0, by: -1) {
                if ti >= 0 && sArr[i] == tArr[ti] {
                    right[ti] = i
                    ti -= 1
                }
            }
        }
        
        var ans = n   // remove all characters
        
        // Remove a prefix of t
        for j in 0..<n where right[j] != -1 {
            ans = min(ans, j)
        }
        
        // Remove a suffix of t
        for i in 0..<n where left[i] != -1 {
            ans = min(ans, n - i - 1)
        }
        
        // Remove a middle segment
        if n > 0 {
            for i in 0..<(n - 1) {
                if left[i] == -1 { continue }
                var lo = i + 1
                var hi = n - 1
                var pos = -1
                while lo <= hi {
                    let mid = (lo + hi) >> 1
                    if right[mid] > left[i] {
                        pos = mid
                        hi = mid - 1
                    } else {
                        lo = mid + 1
                    }
                }
                if pos != -1 {
                    ans = min(ans, pos - i - 1)
                }
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumScore(s: String, t: String): Int {
        val n = t.length
        val m = s.length
        val leftPos = IntArray(n) { m } // INF = m (out of range)
        var idxS = 0
        for (i in 0 until n) {
            while (idxS < m && s[idxS] != t[i]) idxS++
            if (idxS == m) break
            leftPos[i] = idxS
            idxS++
        }
        val rightPos = IntArray(n) { -1 }
        idxS = m - 1
        for (i in n - 1 downTo 0) {
            while (idxS >= 0 && s[idxS] != t[i]) idxS--
            if (idxS < 0) break
            rightPos[i] = idxS
            idxS--
        }
        var ans = n // delete whole t
        // already subsequence without deletions
        if (leftPos[n - 1] != m) return 0
        // delete prefix only
        for (j in 0 until n) {
            if (rightPos[j] != -1) {
                ans = kotlin.math.min(ans, j)
            }
        }
        // delete suffix only
        for (i in 0 until n) {
            if (leftPos[i] != m) {
                ans = kotlin.math.min(ans, n - i - 1)
            }
        }
        // delete middle segment
        for (i in 0 until n - 1) {
            val lp = leftPos[i]
            if (lp == m) continue
            var l = i + 1
            var r = n - 1
            var pos = -1
            while (l <= r) {
                val mid = (l + r) ushr 1
                if (rightPos[mid] > lp) {
                    pos = mid
                    r = mid - 1
                } else {
                    l = mid + 1
                }
            }
            if (pos != -1) {
                ans = kotlin.math.min(ans, pos - i - 1)
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumScore(String s, String t) {
    int n = s.length;
    int m = t.length;

    // pref[i] = earliest index in s where t[0..i] matches as subsequence
    List<int> pref = List.filled(m, -1);
    int si = 0;
    for (int ti = 0; ti < m && si < n; ++ti) {
      while (si < n && s[si] != t[ti]) {
        si++;
      }
      if (si == n) break;
      pref[ti] = si;
      si++;
    }

    // suff[i] = latest index in s where t[i..m-1] matches as subsequence
    List<int> suff = List.filled(m, -1);
    int sj = n - 1;
    for (int tj = m - 1; tj >= 0 && sj >= 0; --tj) {
      while (sj >= 0 && s[sj] != t[tj]) {
        sj--;
      }
      if (sj < 0) break;
      suff[tj] = sj;
      sj--;
    }

    // If whole t is already a subsequence
    if (pref[m - 1] != -1) return 0;

    int ans = m; // worst case: remove all characters

    // Remove a suffix (keep a prefix)
    for (int i = 0; i <= m; ++i) {
      if (i == 0 || pref[i - 1] != -1) {
        int len = m - i;
        if (len < ans) ans = len;
      }
    }

    // Remove a prefix (keep a suffix)
    for (int j = 0; j < m; ++j) {
      if (suff[j] != -1) {
        int len = j + 1;
        if (len < ans) ans = len;
      }
    }

    // Remove a middle segment
    for (int i = 0; i < m; ++i) {
      int leftPos = (i == 0) ? -1 : pref[i - 1];
      if (i > 0 && leftPos == -1) continue;

      int l = i, r = m - 1;
      int posIdx = -1;
      while (l <= r) {
        int mid = (l + r) >> 1;
        if (suff[mid] != -1 && suff[mid] > leftPos) {
          posIdx = mid;
          r = mid - 1;
        } else {
          l = mid + 1;
        }
      }
      if (posIdx != -1) {
        int len = posIdx - i;
        if (len < ans) ans = len;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func minimumScore(s string, t string) int {
    n, m := len(s), len(t)

    // left[i]: earliest position in s matching t[0..i]
    left := make([]int, m)
    p := 0
    for i := 0; i < m; i++ {
        for p < n && s[p] != t[i] {
            p++
        }
        if p == n {
            left[i] = n // not found
        } else {
            left[i] = p
            p++
        }
    }

    // right[i]: latest position in s matching t[i..m-1]
    right := make([]int, m)
    p = n - 1
    for i := m - 1; i >= 0; i-- {
        for p >= 0 && s[p] != t[i] {
            p--
        }
        if p < 0 {
            right[i] = -1
        } else {
            right[i] = p
            p--
        }
    }

    // collect valid suffix positions (right[i] != -1)
    var idxs []int
    var pos []int
    for i := 0; i < m; i++ {
        if right[i] != -1 {
            idxs = append(idxs, i)
            pos = append(pos, right[i])
        }
    }

    ans := m // delete all characters

    // iterate over possible prefix end i (-1 means empty prefix)
    for i := -1; i < m; i++ {
        var leftPos int
        if i == -1 {
            leftPos = -1
        } else {
            if left[i] == n {
                continue // this prefix cannot be matched
            }
            leftPos = left[i]
        }

        // find first suffix index j > i with right[j] > leftPos
        start := sort.Search(len(idxs), func(k int) bool { return idxs[k] > i })
        if start == len(idxs) {
            // no valid suffix, need to delete the rest after i
            cur := m - i - 1
            if cur < ans {
                ans = cur
            }
            continue
        }

        // binary search on positions to satisfy right[j] > leftPos
        offset := sort.Search(len(pos)-start, func(k int) bool { return pos[start+k] > leftPos })
        if offset == len(pos)-start {
            // no suffix with position greater than leftPos
            cur := m - i - 1
            if cur < ans {
                ans = cur
            }
        } else {
            jIdx := idxs[start+offset]
            cur := jIdx - i - 1
            if cur < ans {
                ans = cur
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def minimum_score(s, t)
  n = s.length
  m = t.length

  pref = Array.new(m + 1, n)
  pref[0] = -1
  idx = 0
  (1..m).each do |i|
    ch = t[i - 1]
    while idx < n && s[idx] != ch
      idx += 1
    end
    break if idx == n

    pref[i] = idx
    idx += 1
  end

  suff = Array.new(m + 1, -1)
  suff[m] = n
  idx = n - 1
  (m - 1).downto(0) do |i|
    ch = t[i]
    while idx >= 0 && s[idx] != ch
      idx -= 1
    end
    break if idx < 0

    suff[i] = idx
    idx -= 1
  end

  ans = m
  ans = 0 if pref[m] != n

  (0..m).each do |i|
    left_pos = pref[i]
    next if left_pos == n

    lo = i
    hi = m
    while lo < hi
      mid = (lo + hi) / 2
      if suff[mid] > left_pos
        hi = mid
      else
        lo = mid + 1
      end
    end
    if lo <= m && suff[lo] > left_pos
      len = lo - i
      ans = len if len < ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def minimumScore(s: String, t: String): Int = {
    val n = s.length
    val m = t.length

    // left[i] = earliest index in s where prefix t[0..i-1] can be matched as subsequence
    val left = new Array[Int](m + 1)
    left(0) = -1
    var p = 0
    for (i <- 0 until m) {
      while (p < n && s.charAt(p) != t.charAt(i)) p += 1
      if (p == n) left(i + 1) = n
      else {
        left(i + 1) = p
        p += 1
      }
    }

    // right[i] = latest index in s where suffix t[i..m-1] can be matched as subsequence
    val right = new Array[Int](m + 1)
    right(m) = n
    var q = n - 1
    for (i <- (m - 1) to 0 by -1) {
      while (q >= 0 && s.charAt(q) != t.charAt(i)) q -= 1
      if (q < 0) right(i) = -1
      else {
        right(i) = q
        q -= 1
      }
    }

    // If whole t is already a subsequence, score is 0
    if (left(m) < n) return 0

    var ans = m // worst case: remove all characters
    for (l <- 0 to m) {
      val leftIdx = if (l == 0) -1 else left(l)
      if (leftIdx != n) { // prefix can be matched
        var lo = l + 1
        var hi = m
        while (lo < hi) {
          val mid = (lo + hi) >>> 1
          if (right(mid) > leftIdx) hi = mid else lo = mid + 1
        }
        ans = math.min(ans, lo - l)
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_score(s: String, t: String) -> i32 {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let n = t_bytes.len();
        let m = s_bytes.len();

        // left[i] = earliest index in s where t[0..=i] can be matched
        let mut left = vec![m; n];
        let mut si = 0usize;
        for ti in 0..n {
            while si < m && s_bytes[si] != t_bytes[ti] {
                si += 1;
            }
            if si == m {
                break;
            }
            left[ti] = si;
            si += 1;
        }

        // right[i] = latest index in s where t[i..] can be matched (greedy from end)
        let mut right = vec![usize::MAX; n];
        let mut si = m;
        for ti_rev in (0..n).rev() {
            while si > 0 && s_bytes[si - 1] != t_bytes[ti_rev] {
                si -= 1;
            }
            if si == 0 {
                break;
            }
            si -= 1; // match at si
            right[ti_rev] = si;
        }

        let mut ans = n as i32; // remove all characters

        // If whole t is already a subsequence, answer is 0
        if left[n - 1] != m {
            ans = 0;
        }

        for i in 0..=n {
            // left part length = i (kept prefix size)
            let left_pos: i64 = if i == 0 {
                -1
            } else {
                let pos = left[i - 1];
                if pos == m {
                    continue; // this prefix cannot be matched
                }
                pos as i64
            };

            // binary search for smallest j >= i such that right[j] > left_pos
            let mut l = i;
            let mut r = n;
            while l < r {
                let mid = (l + r) / 2;
                if right[mid] != usize::MAX && (right[mid] as i64) > left_pos {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }

            // removal length
            let remove_len = if l == n { n - i } else { l - i };
            if (remove_len as i32) < ans {
                ans = remove_len as i32;
            }
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (minimum-score s t)
  (-> string? string? exact-integer?)
  (let* ([n (string-length s)]
         [m (string-length t)]
         ;; L[i]: earliest index in s matching prefix t[0..i-1]
         [L (make-vector (add1 m) -1)])
    (vector-set! L 0 -1)
    (let ([pos 0])
      (for ([i (in-range m)])
        (while (and (< pos n)
                    (not (char=? (string-ref s pos) (string-ref t i))))
          (set! pos (add1 pos)))
        (if (>= pos n)
            (vector-set! L (add1 i) n)
            (begin
              (vector-set! L (add1 i) pos)
              (set! pos (add1 pos))))))
    ;; R[i]: latest index in s matching suffix t[i..m-1]
    (let* ([R (make-vector (add1 m) n)])
      (let ([pos (sub1 n)])
        (for ([i (in-range (sub1 m) -1 -1)]) ; i = m-1 .. 0
          (while (and (>= pos 0)
                      (not (char=? (string-ref s pos) (string-ref t i))))
            (set! pos (sub1 pos)))
          (if (< pos 0)
              (vector-set! R i -1)
              (begin
                (vector-set! R i pos)
                (set! pos (sub1 pos))))))
      ;; two‑pointer search for minimal removal length
      (let ([ans m]
            [j 0])
        (for ([i (in-range (add1 m))])
          (when (< j i) (set! j i))
          (while (and (<= j m)
                      (not (< (vector-ref L i) (vector-ref R j))))
            (set! j (add1 j)))
          (when (<= j m)
            (let ([len (- j i)])
              (when (< len ans) (set! ans len)))))
        ans))))
```

## Erlang

```erlang
-export([minimum_score/2]).

-spec minimum_score(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
minimum_score(S, T) ->
    SList = binary_to_list(S),
    TList = binary_to_list(T),
    STup = list_to_tuple(SList),
    TTup = list_to_tuple(TList),
    N = tuple_size(STup),
    M = tuple_size(TTup),

    LeftList = build_left(0, 0, M, N, STup, TTup, []),
    RightList = build_right(M - 1, N - 1, M, N, STup, TTup, []),

    LeftTuple = list_to_tuple(LeftList),
    RightTuple = list_to_tuple(RightList),

    iterate(-1, M - 1, LeftTuple, RightTuple, N, M).

%% Build left array: earliest positions in S matching prefixes of T
build_left(I_t, PosS, M, N, STup, TTup, Acc) when I_t < M ->
    Char = element(I_t + 1, TTup),
    case find_next(STup, Char, PosS, N) of
        {found, P} ->
            build_left(I_t + 1, P + 1, M, N, STup, TTup, [P | Acc]);
        not_found ->
            RestCount = M - I_t,
            Rest = lists:duplicate(RestCount, N),
            lists:reverse(Acc) ++ Rest
    end;
build_left(_I_t, _PosS, _M, _N, _STup, _TTup, Acc) ->
    lists:reverse(Acc).

%% Build right array: latest positions in S matching suffixes of T
build_right(I, PosS, M, N, STup, TTup, Acc) when I >= 0 ->
    Char = element(I + 1, TTup),
    case find_prev(STup, Char, PosS) of
        {found, P} ->
            build_right(I - 1, P - 1, M, N, STup, TTup, [P | Acc]);
        not_found ->
            RestCount = I + 1,
            Rest = lists:duplicate(RestCount, -1),
            Rest ++ Acc
    end;
build_right(_I, _PosS, _M, _N, _STup, _TTup, Acc) ->
    Acc.

%% Find next occurrence of Char in STup starting from Pos (0‑based)
find_next(STup, Char, Pos, N) when Pos < N ->
    case element(Pos + 1, STup) of
        Char -> {found, Pos};
        _ -> find_next(STup, Char, Pos + 1, N)
    end;
find_next(_STup, _Char, _Pos, _N) ->
    not_found.

%% Find previous occurrence of Char in STup starting from Pos (0‑based)
find_prev(STup, Char, Pos) when Pos >= 0 ->
    case element(Pos + 1, STup) of
        Char -> {found, Pos};
        _ -> find_prev(STup, Char, Pos - 1)
    end;
find_prev(_STup, _Char, _Pos) ->
    not_found.

%% Binary search for smallest index j with RightTuple[j] > LPos
binary_search(LPos, RightTuple, Low, High, _N) when Low =< High ->
    Mid = (Low + High) div 2,
    Val = element(Mid + 1, RightTuple),
    if
        Val > LPos -> binary_search(LPos, RightTuple, Low, Mid - 1, _N);
        true       -> binary_search(LPos, RightTuple, Mid + 1, High, _N)
    end;
binary_search(_LPos, _RightTuple, Low, _High, _N) ->
    Low.

%% Iterate over possible split positions to compute minimal removal length
iterate(I, MaxI, LeftTuple, RightTuple, N, Ans) when I =< MaxI ->
    LeftPos = case I of
        -1 -> -1;
        _  -> element(I + 1, LeftTuple)
    end,
    J = binary_search(LeftPos, RightTuple, 0, MaxI, N),
    Len = J - I - 1,
    NewAns = if Len < Ans -> Len; true -> Ans end,
    iterate(I + 1, MaxI, LeftTuple, RightTuple, N, NewAns);
iterate(_I, _MaxI, _LeftTuple, _RightTuple, _N, Ans) ->
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_score(s :: String.t(), t :: String.t()) :: integer
  def minimum_score(s, t) do
    s_chars = :binary.bin_to_list(s)
    t_chars = :binary.bin_to_list(t)

    left_vals = build_left(s_chars, t_chars)
    right_vals = build_right(s_chars, t_chars)

    n = length(t_chars)
    left_tuple = List.to_tuple(left_vals)
    right_tuple = List.to_tuple(right_vals)

    ans0 = n
    ans1 = if elem(left_tuple, n - 1) != -1, do: 0, else: ans0

    ans2 =
      0..(n - 1)
      |> Enum.reduce(ans1, fn i, acc ->
        left_pos = elem(left_tuple, i)

        acc =
          if left_pos != -1 do
            min(acc, n - i - 1)
          else
            acc
          end

        if left_pos != -1 do
          pos = lower_bound(right_tuple, n, left_pos)

          if pos < n and pos > i do
            min(acc, pos - i - 1)
          else
            acc
          end
        else
          acc
        end
      end)

    ans3 =
      0..(n - 1)
      |> Enum.reduce(ans2, fn j, acc ->
        right_pos = elem(right_tuple, j)

        if right_pos != -1 do
          min(acc, j)
        else
          acc
        end
      end)

    ans3
  end

  defp build_left(s_chars, t_list) do
    n = length(t_list)
    arr = :array.new(n, default: -1)

    {arr, _} =
      Enum.reduce(Enum.with_index(s_chars), {arr, t_list}, fn {c, idx},
                                                             {a, rem_t} ->
        case rem_t do
          [^c | rest] ->
            i = n - length(rem_t)
            { :array.set(i, idx, a), rest }

          _ ->
            {a, rem_t}
        end
      end)

    :array.to_list(arr)
  end

  defp build_right(s_chars, t_list) do
    n = length(t_list)
    m = length(s_chars)
    arr = :array.new(n, default: -1)

    rev_s = Enum.reverse(s_chars)
    t_rev = Enum.reverse(t_list)

    {arr, _} =
      Enum.reduce(Enum.with_index(rev_s), {arr, t_rev}, fn {c, rev_idx},
                                                          {a, rem_t} ->
        case rem_t do
          [^c | rest] ->
            matched = n - length(rem_t)
            orig_idx = n - 1 - matched
            s_idx = m - 1 - rev_idx
            { :array.set(orig_idx, s_idx, a), rest }

          _ ->
            {a, rem_t}
        end
      end)

    :array.to_list(arr)
  end

  defp lower_bound(tuple, len, target) do
    lo = 0
    hi = len

    while lo < hi do
      mid = div(lo + hi, 2)

      if elem(tuple, mid) <= target do
        lo = mid + 1
      else
        hi = mid
      end
    end

    lo
  end
end
```
