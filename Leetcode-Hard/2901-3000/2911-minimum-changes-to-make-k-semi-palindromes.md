# 2911. Minimum Changes to Make K Semi-palindromes

## Cpp

```cpp
class Solution {
public:
    int minimumChanges(string s, int k) {
        int n = s.size();
        const int INF = 1e9;
        vector<vector<int>> cost(n, vector<int>(n, 0));
        // compute cost to make substring [l..r] a palindrome
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                if (len == 2) cost[l][r] = (s[l] != s[r]);
                else cost[l][r] = cost[l+1][r-1] + (s[l] != s[r]);
            }
        }
        // dp[i][c]: min changes for first i characters split into c parts
        vector<vector<int>> dp(n+1, vector<int>(k+1, INF));
        dp[0][0] = 0;
        for (int i = 2; i <= n; ++i) { // at least length 2 for a part
            for (int cnt = 1; cnt <= k; ++cnt) {
                for (int j = 0; j <= i-2; ++j) { // previous cut position
                    if (dp[j][cnt-1] == INF) continue;
                    dp[i][cnt] = min(dp[i][cnt], dp[j][cnt-1] + cost[j][i-1]);
                }
            }
        }
        return dp[n][k];
    }
};
```

## Java

```java
class Solution {
    public int minimumChanges(String s, int k) {
        int n = s.length();
        char[] c = s.toCharArray();
        int[][] cost = new int[n][n];
        // precompute costs for substrings of length >= 2
        for (int l = 0; l < n; ++l) {
            for (int r = l + 1; r < n; ++r) {
                int len = r - l + 1;
                int pal = 0;
                for (int i = 0; i < len / 2; ++i) {
                    if (c[l + i] != c[r - i]) pal++;
                }
                int best = pal;
                if ((len & 1) == 0) { // even length, also consider making two halves identical
                    int half = 0;
                    int halfLen = len / 2;
                    for (int i = 0; i < halfLen; ++i) {
                        if (c[l + i] != c[l + i + halfLen]) half++;
                    }
                    best = Math.min(best, half);
                }
                cost[l][r] = best;
            }
        }

        final int INF = 1_000_000_000;
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 0; i <= n; ++i) {
            java.util.Arrays.fill(dp[i], INF);
        }
        dp[0][0] = 0;

        // dp[pos][parts]: first pos characters split into parts substrings
        for (int pos = 2; pos <= n; ++pos) { // need at least length 2 for a part
            for (int parts = 1; parts <= k; ++parts) {
                // previous cut position must leave enough chars for remaining parts
                int minPrev = (parts - 1) * 2;
                for (int prev = minPrev; prev <= pos - 2; ++prev) {
                    if (dp[prev][parts - 1] == INF) continue;
                    int curCost = cost[prev][pos - 1];
                    dp[pos][parts] = Math.min(dp[pos][parts], dp[prev][parts - 1] + curCost);
                }
            }
        }

        return dp[n][k];
    }
}
```

## Python

```python
class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # precompute cost to make any substring a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    cost[i][j] = cost[i + 1][j - 1] if i + 1 <= j - 1 else 0
                else:
                    cost[i][j] = (cost[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 1

        INF = 10 ** 9
        # dp[i][c]: min changes for prefix s[0:i] (i chars) into c palindromes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for c in range(1, min(k, i) + 1):
                # try all possible previous cut positions
                best = INF
                for p in range(c - 1, i):  # at least c-1 chars before to have c-1 parts
                    cur = dp[p][c - 1] + cost[p][i - 1]
                    if cur < best:
                        best = cur
                dp[i][c] = best

        return dp[n][k]
```

## Python3

```python
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10 ** 9

        # cost[i][j]: min changes to make s[i..j] a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if i + 1 <= j - 1:
                    inner = cost[i + 1][j - 1]
                else:
                    inner = 0
                cost[i][j] = inner + (s[i] != s[j])

        # dp[i][p]: min changes for first i characters split into p parts
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(2, n + 1):          # prefix length
            max_parts = min(k, i // 2)     # each part at least length 2
            for p in range(1, max_parts + 1):
                # previous cut position j (prefix length before current part)
                # need at least 2 chars for the current part and enough chars left for remaining parts
                for j in range((p - 1) * 2, i - 1):
                    if i - j >= 2:
                        dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])

        return dp[n][k]
```

## C

```c
#include <string.h>
#include <limits.h>

int minimumChanges(char* s, int k) {
    int n = (int)strlen(s);
    static int cost[201][201];
    for (int i = 0; i < n; ++i) cost[i][i] = 0;
    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            if (len == 2)
                cost[i][j] = (s[i] != s[j]);
            else
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j]);
        }
    }

    const int INF = INT_MAX / 4;
    static int dp[201][101];
    for (int i = 0; i <= n; ++i)
        for (int c = 0; c <= k; ++c)
            dp[i][c] = INF;
    dp[0][0] = 0;

    for (int i = 2; i <= n; ++i) {               // total length considered
        for (int c = 1; c <= k && c * 2 <= i; ++c) {
            int minPrev = INF;
            for (int j = 2 * (c - 1); j <= i - 2; ++j) { // split point
                if (dp[j][c - 1] == INF) continue;
                int cur = dp[j][c - 1] + cost[j][i - 1];
                if (cur < minPrev) minPrev = cur;
            }
            dp[i][c] = minPrev;
        }
    }

    return dp[n][k];
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumChanges(string s, int k) {
        int n = s.Length;
        int[,] cost = new int[n, n];
        for (int l = 0; l < n; l++) {
            for (int r = l; r < n; r++) {
                int cnt = 0;
                int i = l, j = r;
                while (i < j) {
                    if (s[i] != s[j]) cnt++;
                    i++; j--;
                }
                cost[l, r] = cnt;
            }
        }

        int INF = 1_000_000_000;
        int[,] dp = new int[n + 1, k + 1];
        for (int i = 0; i <= n; i++) {
            for (int p = 0; p <= k; p++) {
                dp[i, p] = INF;
            }
        }
        dp[0, 0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int p = 1; p <= k; p++) {
                // each part must have length at least 2
                for (int prev = i - 2; prev >= 0; prev--) {
                    if (dp[prev, p - 1] == INF) continue;
                    int cur = dp[prev, p - 1] + cost[prev, i - 1];
                    if (cur < dp[i, p]) dp[i, p] = cur;
                }
            }
        }

        return dp[n, k];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var minimumChanges = function(s, k) {
    const n = s.length;
    // precompute cost[l][r]: min changes to make s[l..r] a palindrome
    const cost = Array.from({ length: n }, () => Array(n).fill(0));
    for (let len = 2; len <= n; ++len) {
        for (let l = 0; l + len - 1 < n; ++l) {
            const r = l + len - 1;
            if (len === 2) {
                cost[l][r] = s[l] === s[r] ? 0 : 1;
            } else {
                cost[l][r] = cost[l + 1][r - 1] + (s[l] === s[r] ? 0 : 1);
            }
        }
    }

    const INF = 1e9;
    // dp[i][p]: min changes for first i characters split into p parts
    const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(INF));
    dp[0][0] = 0;

    for (let p = 1; p <= k; ++p) {
        // each part needs at least length 2
        for (let i = 2 * p; i <= n; ++i) {
            let best = INF;
            // previous cut position t, start of current segment is t, end is i-1
            for (let t = 2 * (p - 1); t <= i - 2; ++t) {
                if (dp[t][p - 1] === INF) continue;
                const cur = dp[t][p - 1] + cost[t][i - 1];
                if (cur < best) best = cur;
            }
            dp[i][p] = best;
        }
    }

    return dp[n][k];
};
```

## Typescript

```typescript
function minimumChanges(s: string, k: number): number {
    const n = s.length;
    // precompute cost to make any substring a palindrome
    const cost: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            let cnt = 0;
            let l = i, r = j;
            while (l < r) {
                if (s[l] !== s[r]) cnt++;
                l++; r--;
            }
            cost[i][j] = cnt;
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    // dp[pos][parts] = min changes for first pos characters split into parts substrings
    const dp: number[][] = Array.from({ length: n + 1 }, () => Array(k + 1).fill(INF));
    dp[0][0] = 0;

    for (let i = 2; i <= n; ++i) { // at least one part of length >=2
        for (let parts = 1; parts <= k && parts * 2 <= i; ++parts) {
            // try previous cut position j, where substring [j, i-1] is the last part
            for (let j = (parts - 1) * 2; j <= i - 2; ++j) {
                if (dp[j][parts - 1] === INF) continue;
                const curCost = dp[j][parts - 1] + cost[j][i - 1];
                if (curCost < dp[i][parts]) dp[i][parts] = curCost;
            }
        }
    }

    return dp[n][k];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function minimumChanges($s, $k) {
        $n = strlen($s);
        // precompute cost to make any substring a palindrome
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $j = $i + $len - 1;
                $c = ($s[$i] !== $s[$j]) ? 1 : 0;
                if ($i + 1 <= $j - 1) {
                    $c += $cost[$i + 1][$j - 1];
                }
                $cost[$i][$j] = $c;
            }
        }

        $INF = 1 << 30;
        // dp[i][p]: min changes for suffix starting at i with p parts remaining
        $dp = array_fill(0, $n + 1, array_fill(0, $k + 1, $INF));
        $dp[$n][0] = 0;

        for ($i = $n - 1; $i >= 0; $i--) {
            for ($p = 1; $p <= $k; $p++) {
                // need at least 2 characters per remaining part
                if (($n - $i) < 2 * $p) {
                    continue;
                }
                $best = $INF;
                // end index j (inclusive), length >=2 => j >= i+1
                for ($j = $i + 1; $j < $n; $j++) {
                    if (($n - ($j + 1)) < 2 * ($p - 1)) {
                        continue;
                    }
                    $cand = $cost[$i][$j] + $dp[$j + 1][$p - 1];
                    if ($cand < $best) {
                        $best = $cand;
                    }
                }
                $dp[$i][$p] = $best;
            }
        }

        return $dp[0][$k];
    }
}
```

## Swift

```swift
class Solution {
    func minimumChanges(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        if k == 0 { return 0 }
        // cost[i][j]: min changes to make s[i...j] a palindrome (length >=2)
        var cost = Array(repeating: Array(repeating: 0, count: n), count: n)
        if n >= 2 {
            for length in 2...n {
                for i in 0..<(n - length + 1) {
                    let j = i + length - 1
                    if length == 2 {
                        cost[i][j] = (chars[i] == chars[j]) ? 0 : 1
                    } else {
                        cost[i][j] = cost[i + 1][j - 1] + ((chars[i] == chars[j]) ? 0 : 1)
                    }
                }
            }
        }
        let INF = Int.max / 4
        var dp = Array(repeating: Array(repeating: INF, count: k + 1), count: n + 1)
        dp[0][0] = 0
        
        for i in 0..<n {
            for parts in 0..<k {
                let cur = dp[i][parts]
                if cur == INF { continue }
                // need at least (k - parts) * 2 characters remaining including current position
                if n - i < (k - parts) * 2 { continue }
                for j in (i + 1)..<n {
                    let remaining = n - (j + 1)
                    let needed = (k - parts - 1) * 2
                    if remaining < needed { continue }
                    let newCost = cur + cost[i][j]
                    if newCost < dp[j + 1][parts + 1] {
                        dp[j + 1][parts + 1] = newCost
                    }
                }
            }
        }
        return dp[n][k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumChanges(s: String, k: Int): Int {
        val n = s.length
        val cost = Array(n) { IntArray(n) }
        // compute minimal changes to make any substring a palindrome
        for (len in 2..n) {
            var i = 0
            while (i + len - 1 < n) {
                val j = i + len - 1
                if (len == 2) {
                    cost[i][j] = if (s[i] == s[j]) 0 else 1
                } else {
                    cost[i][j] = cost[i + 1][j - 1] + if (s[i] == s[j]) 0 else 1
                }
                i++
            }
        }

        val INF = 1_000_000_0
        val dp = Array(n + 1) { IntArray(k + 1) { INF } }
        dp[0][0] = 0

        for (i in 2..n) { // total length considered
            for (parts in 1..k) {
                if (i < parts * 2) continue // each part needs at least length 2
                var prevStart = (parts - 1) * 2
                while (prevStart <= i - 2) {
                    val prevLen = prevStart
                    if (dp[prevLen][parts - 1] != INF) {
                        val curCost = cost[prevLen][i - 1]
                        dp[i][parts] = kotlin.math.min(dp[i][parts], dp[prevLen][parts - 1] + curCost)
                    }
                    prevStart++
                }
            }
        }

        return dp[n][k]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minimumChanges(String s, int k) {
    int n = s.length;
    List<List<int>> cost = List.generate(n, (_) => List.filled(n, 0));

    // Precompute the minimal changes to make any substring a palindrome
    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;
        if (len == 2) {
          cost[i][j] = s[i] == s[j] ? 0 : 1;
        } else {
          cost[i][j] = cost[i + 1][j - 1] + (s[i] == s[j] ? 0 : 1);
        }
      }
    }

    const int INF = 1 << 30;
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(k + 1, INF));
    dp[n][0] = 0;

    for (int pos = n - 1; pos >= 0; --pos) {
      for (int parts = 1; parts <= k; ++parts) {
        // Not enough characters left to form required parts
        if ((n - pos) < 2 * parts) continue;
        for (int end = pos + 1; end < n; ++end) { // ensure length >= 2
          int remaining = n - (end + 1);
          if (remaining < 2 * (parts - 1)) continue;
          int curCost = cost[pos][end];
          int next = dp[end + 1][parts - 1];
          if (next != INF) {
            dp[pos][parts] = min(dp[pos][parts], curCost + next);
          }
        }
      }
    }

    return dp[0][k];
  }
}
```

## Golang

```go
func minimumChanges(s string, k int) int {
    n := len(s)
    // Precompute cost to make any substring a palindrome
    cost := make([][]int, n)
    for i := 0; i < n; i++ {
        cost[i] = make([]int, n)
    }
    b := []byte(s)
    for l := 0; l < n; l++ {
        for r := l + 1; r < n; r++ { // length at least 2
            cnt := 0
            i, j := l, r
            for i < j {
                if b[i] != b[j] {
                    cnt++
                }
                i++
                j--
            }
            cost[l][r] = cnt
        }
    }

    const INF = int(1e9)
    dp := make([][]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([]int, k+1)
        for p := 0; p <= k; p++ {
            dp[i][p] = INF
        }
    }
    dp[0][0] = 0

    for i := 0; i < n; i++ { // end index of current substring
        for parts := 1; parts <= k; parts++ {
            for l := 0; l <= i; l++ { // start index of current substring
                if i-l+1 < 2 { // length must be at least 2
                    continue
                }
                if dp[l][parts-1] == INF {
                    continue
                }
                val := dp[l][parts-1] + cost[l][i]
                if val < dp[i+1][parts] {
                    dp[i+1][parts] = val
                }
            }
        }
    }

    return dp[n][k]
}
```

## Ruby

```ruby
def minimum_changes(s, k)
  n = s.length
  # precompute cost to make substring [i..j] a palindrome
  cost = Array.new(n) { Array.new(n, 0) }
  (0...n).each do |i|
    (i + 1...n).each do |j|
      l = i
      r = j
      cnt = 0
      while l < r
        cnt += 1 if s[l] != s[r]
        l += 1
        r -= 1
      end
      cost[i][j] = cnt
    end
  end

  inf = 1 << 60
  dp = Array.new(k + 1) { Array.new(n + 1, inf) }
  dp[0][0] = 0

  (1..k).each do |parts|
    (1..n).each do |i|
      best = inf
      # start index of the last part (0‑based)
      ((parts - 1)..(i - 1)).each do |t|
        next if i - t < 2          # each semi‑palindrome must have length >= 2
        val = dp[parts - 1][t] + cost[t][i - 1]
        best = val if val < best
      end
      dp[parts][i] = best
    end
  end

  dp[k][n]
end
```

## Scala

```scala
object Solution {
  def minimumChanges(s: String, k: Int): Int = {
    val n = s.length
    val cost = Array.ofDim[Int](n, n)
    // precompute minimal changes to make each substring a palindrome
    for (i <- 0 until n) {
      var j = i + 1
      while (j < n) {
        var l = i
        var r = j
        var cnt = 0
        while (l < r) {
          if (s.charAt(l) != s.charAt(r)) cnt += 1
          l += 1
          r -= 1
        }
        cost(i)(j) = cnt
        j += 1
      }
    }

    val INF = 1_000_000_000
    val dp = Array.ofDim[Int](n + 1, k + 1)
    for (i <- 0 to n; p <- 0 to k) dp(i)(p) = INF
    dp(0)(0) = 0

    // dp[i][p]: min changes for first i characters split into p parts (each length >=2)
    for (i <- 2 to n) {
      val maxParts = math.min(k, i / 2)
      for (p <- 1 to maxParts) {
        var best = INF
        // previous cut position j, substring s[j..i-1] is the last part
        var j = i - 2 // ensure length >=2
        while (j >= (p - 1) * 2 && j >= 0) {
          val prev = dp(j)(p - 1)
          if (prev != INF) {
            val cand = prev + cost(j)(i - 1)
            if (cand < best) best = cand
          }
          j -= 1
        }
        dp(i)(p) = best
      }
    }

    dp(n)(k)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_changes(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let k_usize = k as usize;
        // cost[i][j]: min changes to make substring [i..=j] a palindrome
        let mut cost = vec![vec![0usize; n]; n];
        for i in (0..n).rev() {
            for j in i + 1..n {
                if i + 1 <= j - 1 {
                    cost[i][j] = cost[i + 1][j - 1]
                        + if bytes[i] == bytes[j] { 0 } else { 1 };
                } else {
                    // length 2
                    cost[i][j] = if bytes[i] == bytes[j] { 0 } else { 1 };
                }
            }
        }

        let inf: usize = 1_000_000;
        let mut dp = vec![vec![inf; k_usize + 1]; n + 1];
        dp[0][0] = 0;

        for i in 1..=n {
            for parts in 1..=k_usize {
                // try all possible previous cut positions t
                let mut best = inf;
                // each part must have length at least 2
                if i >= 2 {
                    for t in (0..=i - 2) {
                        if dp[t][parts - 1] == inf {
                            continue;
                        }
                        let cur = dp[t][parts - 1] + cost[t][i - 1];
                        if cur < best {
                            best = cur;
                        }
                    }
                }
                dp[i][parts] = best;
            }
        }

        dp[n][k_usize] as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-changes s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (INF 1000000000)
         ;; precompute palindrome change costs v[i][j]
         (v (let ((vec (make-vector n)))
              (for ([i (in-range n)])
                (let ((row (make-vector n 0)))
                  (vector-set! vec i row)
                  (for ([j (in-range i n)])
                    (define (cost l r cnt)
                      (if (< l r)
                          (cost (+ l 1) (- r 1)
                                (if (char=? (string-ref s l) (string-ref s r))
                                    cnt
                                    (+ cnt 1)))
                          cnt))
                    (vector-set! row j (cost i j 0))))
              vec))
         ;; dp[pos][parts] = min changes for suffix starting at pos with parts remaining
         (dp (let ((mat (make-vector (+ n 1))))
               (for ([i (in-range (+ n 1))])
                 (vector-set! mat i (make-vector (+ k 1) INF)))
               ;; base case: no characters left and no parts needed -> 0
               (vector-set! (vector-ref mat n) 0 0)
               mat)))
    ;; fill dp bottom‑up
    (for ([pos (in-range (sub1 n) -1 -1)])
      (for ([parts (in-range 1 (add1 k))])
        (let ((best INF))
          ;; end is inclusive index of current part, must have length >=2
          (for ([end (in-range (+ pos 2) (add1 n))])
            ;; ensure enough characters remain for remaining parts
            (when (>= (- n (add1 end)) (* 2 (sub1 parts)))
              (let* ((cost-part (vector-ref (vector-ref v pos) end))
                     (next-cost (vector-ref (vector-ref dp (add1 end)) (sub1 parts)))
                     (total (+ cost-part next-cost)))
                (when (< total best)
                  (set! best total)))))
          (vector-set! (vector-ref dp pos) parts best))))
    ;; answer is dp[0][k]
    (vector-ref (vector-ref dp 0) k)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_changes/2]).

-spec minimum_changes(S :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_changes(S, K) ->
    StrList = binary_to_list(S),
    N = length(StrList),
    Tuple = list_to_tuple(StrList),
    CostMap = build_cost_map(N, Tuple),
    Big = 1000000,
    DP0 = maps:put({0,0}, 0, #{ }),
    DP = dp_loop(1, N, K, CostMap, DP0, Big),
    maps:get({N, K}, DP).

build_cost_map(N, Tuple) ->
    Pairs = [{I,J} || I <- lists:seq(0, N-2), J <- lists:seq(I+1, N-1)],
    lists:foldl(fun({I,J}, Acc) ->
        C = cost_substring(I, J, Tuple),
        maps:put({I,J}, C, Acc)
    end, #{ }, Pairs).

cost_substring(I, J, Tuple) ->
    Len = J - I + 1,
    Half = Len div 2,
    cost_loop(0, Half-1, I, J, Tuple, 0).

cost_loop(T, Max, _I, _J, _Tuple, Acc) when T > Max -> Acc;
cost_loop(T, Max, I, J, Tuple, Acc) ->
    CharL = element(I + T + 1, Tuple),
    CharR = element(J - T + 1, Tuple),
    NewAcc = if CharL =/= CharR -> Acc + 1; true -> Acc end,
    cost_loop(T + 1, Max, I, J, Tuple, NewAcc).

dp_loop(Pos, N, K, CostMap, DP, _Big) when Pos > N ->
    DP;
dp_loop(Pos, N, K, CostMap, DP, Big) ->
    DP1 = parts_loop(1, K, Pos, N, CostMap, DP, Big),
    dp_loop(Pos + 1, N, K, CostMap, DP1, Big).

parts_loop(P, K, _Pos, _N, _CostMap, DP, _Big) when P > K ->
    DP;
parts_loop(P, K, Pos, N, CostMap, DP, Big) ->
    MinVal =
        if 2 * P > Pos -> Big;
           true -> compute_min(Pos, P, CostMap, DP, Big)
        end,
    DP1 = maps:put({Pos, P}, MinVal, DP),
    parts_loop(P + 1, K, Pos, N, CostMap, DP1, Big).

compute_min(Pos, Parts, CostMap, DP, Big) ->
    MaxPrev = Pos - 2,
    compute_prev(0, MaxPrev, Pos, Parts, CostMap, DP, Big, Big).

compute_prev(Cur, Max, _Pos, _Parts, _CostMap, _DP, _Big, Best) when Cur > Max ->
    Best;
compute_prev(Cur, Max, Pos, Parts, CostMap, DP, Big, Best) ->
    case maps:find({Cur, Parts - 1}, DP) of
        {ok, PrevVal} ->
            case maps:find({Cur, Pos - 1}, CostMap) of
                {ok, Cst} ->
                    New = PrevVal + Cst,
                    NewBest = if New < Best -> New; true -> Best end,
                    compute_prev(Cur + 1, Max, Pos, Parts, CostMap, DP, Big, NewBest);
                error ->
                    compute_prev(Cur + 1, Max, Pos, Parts, CostMap, DP, Big, Best)
            end;
        error ->
            compute_prev(Cur + 1, Max, Pos, Parts, CostMap, DP, Big, Best)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_changes(s :: String.t(), k :: integer) :: integer
  def minimum_changes(s, k) do
    chars = :binary.bin_to_list(s)
    tuple = List.to_tuple(chars)
    n = tuple_size(tuple)

    # Precompute cost to make any substring [i..j] a palindrome
    cost =
      Enum.reduce(0..(n - 2), %{}, fn i, acc ->
        Enum.reduce((i + 1)..(n - 1), acc, fn j, inner_acc ->
          Map.put(inner_acc, {i, j}, mismatch(tuple, i, j))
        end)
      end)

    inf = 1_000_000

    dp_initial = %{{0, 0} => 0}

    dp_final =
      0..(n - 1)
      |> Enum.reduce(dp_initial, fn pos, dp_acc ->
        0..(k - 1)
        |> Enum.reduce(dp_acc, fn cnt, dp2 ->
          case Map.fetch(dp2, {pos, cnt}) do
            {:ok, cur} ->
              ((pos + 2)..n)
              |> Enum.reduce(dp2, fn nxt, dp3 ->
                c = Map.get(cost, {pos, nxt - 1}, 0)
                new_val = cur + c
                key = {nxt, cnt + 1}
                prev = Map.get(dp3, key, inf)

                if new_val < prev do
                  Map.put(dp3, key, new_val)
                else
                  dp3
                end
              end)

            :error ->
              dp2
          end
        end)
      end)

    Map.get(dp_final, {n, k}, 0)
  end

  defp mismatch(tuple, i, j) do
    mismatch(tuple, i, j, 0)
  end

  defp mismatch(_tuple, i, j, acc) when i >= j, do: acc

  defp mismatch(tuple, i, j, acc) do
    new_acc =
      if elem(tuple, i) == elem(tuple, j) do
        acc
      else
        acc + 1
      end

    mismatch(tuple, i + 1, j - 1, new_acc)
  end
end
```
