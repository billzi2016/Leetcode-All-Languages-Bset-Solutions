# 3472. Longest Palindromic Subsequence After at Most K Operations

## Cpp

```cpp
class Solution {
public:
    int longestPalindromicSubsequence(string s, int K) {
        int n = s.size();
        auto dist = [&](char a, char b) {
            int d = abs(a - b);
            return min(d, 26 - d);
        };
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(K + 1, 0)));
        for (int i = 0; i < n; ++i) {
            for (int c = 0; c <= K; ++c) dp[i][i][c] = 1;
        }
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                int d = dist(s[l], s[r]);
                for (int c = 0; c <= K; ++c) {
                    int best = max(dp[l + 1][r][c], dp[l][r - 1][c]);
                    if (c >= d) {
                        int inner = (l + 1 <= r - 1) ? dp[l + 1][r - 1][c - d] : 0;
                        best = max(best, inner + 2);
                    }
                    dp[l][r][c] = best;
                }
            }
        }
        return dp[0][n - 1][K];
    }
};
```

## Java

```java
class Solution {
    public int longestPalindromicSubsequence(String s, int K) {
        int n = s.length();
        int[][][] dp = new int[n][n][K + 1];
        // Initialize single characters
        for (int i = 0; i < n; i++) {
            for (int c = 0; c <= K; c++) {
                dp[i][i][c] = 1;
            }
        }

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                int d = dist(s.charAt(i), s.charAt(j));
                for (int c = 0; c <= K; c++) {
                    int best = Math.max(dp[i + 1][j][c], dp[i][j - 1][c]);
                    if (c >= d) {
                        int inner = (i + 1 <= j - 1) ? dp[i + 1][j - 1][c - d] : 0;
                        best = Math.max(best, inner + 2);
                    }
                    dp[i][j][c] = best;
                }
                // make it monotonic: cost at most c
                for (int c = 1; c <= K; c++) {
                    if (dp[i][j][c - 1] > dp[i][j][c]) {
                        dp[i][j][c] = dp[i][j][c - 1];
                    }
                }
            }
        }
        return dp[0][n - 1][K];
    }

    private int dist(char a, char b) {
        int x = a - 'a';
        int y = b - 'a';
        int diff = Math.abs(x - y);
        return Math.min(diff, 26 - diff);
    }
}
```

## Python

```python
import sys
from array import array

class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        K = k
        # helper to compute cyclic distance between two chars
        def dist(a, b):
            d = abs(ord(a) - ord(b))
            return d if d <= 13 else 26 - d

        size = n * n * (K + 1)
        dp = array('H', [0]) * size

        # base case: single character substrings have length 1 for any allowed cost
        for i in range(n):
            base_offset = ((i * n) + i) * (K + 1)
            for c in range(K + 1):
                dp[base_offset + c] = 1

        # fill DP for increasing substring lengths
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                base_off = ((i * n) + j) * (K + 1)
                off_i1_j = (((i + 1) * n) + j) * (K + 1)
                off_i_j1 = ((i * n) + (j - 1)) * (K + 1)
                off_i1_j1 = (((i + 1) * n) + (j - 1)) * (K + 1)

                d = dist(s[i], s[j])
                for c in range(K + 1):
                    best = dp[off_i1_j + c]          # skip i
                    val2 = dp[off_i_j1 + c]           # skip j
                    if val2 > best:
                        best = val2
                    if c >= d:
                        cand = 2 + dp[off_i1_j1 + (c - d)]
                        if cand > best:
                            best = cand
                    dp[base_off + c] = best

        result_offset = ((0 * n) + (n - 1)) * (K + 1)
        return dp[result_offset + K]
```

## Python3

```python
class Solution:
    def longestPalindromicSubsequence(self, s: str, K: int) -> int:
        n = len(s)
        # helper to compute cyclic distance between two chars
        def dist(a: str, b: str) -> int:
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)

        # dp[i][j] will be a list of length K+1, where dp[i][j][c] is the max LPS length
        # in s[i..j] using at most c operations.
        dp = [[None] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = [1] * (K + 1)

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cur = [0] * (K + 1)
                d = dist(s[i], s[j])
                left = dp[i + 1][j]
                right = dp[i][j - 1]
                inner = dp[i + 1][j - 1]
                for c in range(K + 1):
                    best = left[c] if left[c] > right[c] else right[c]
                    if c >= d:
                        cand = inner[c - d] + 2
                        if cand > best:
                            best = cand
                    cur[c] = best
                dp[i][j] = cur

        return dp[0][n - 1][K]
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

static inline int dist_char(char a, char b) {
    int x = a - 'a';
    int y = b - 'a';
    int diff = abs(x - y);
    return diff < 26 - diff ? diff : 26 - diff;
}

int longestPalindromicSubsequence(char* s, int k) {
    const int MAXN = 200;
    const int MAXK = 200;
    static uint16_t dp[MAXN + 1][MAXN + 1][MAXK + 1];
    memset(dp, 0, sizeof(dp));

    int n = (int)strlen(s);
    if (n == 0) return 0;

    for (int i = 0; i < n; ++i)
        for (int c = 0; c <= k; ++c)
            dp[i][i][c] = 1;

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            int d = dist_char(s[i], s[j]);
            for (int c = 0; c <= k; ++c) {
                uint16_t best = dp[i + 1][j][c];
                if (dp[i][j - 1][c] > best) best = dp[i][j - 1][c];
                if (c >= d) {
                    uint16_t cand = dp[i + 1][j - 1][c - d] + 2;
                    if (cand > best) best = cand;
                }
                dp[i][j][c] = best;
            }
        }
    }

    uint16_t ans = 0;
    for (int c = 0; c <= k; ++c)
        if (dp[0][n - 1][c] > ans) ans = dp[0][n - 1][c];
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int LongestPalindromicSubsequence(string s, int k) {
        int n = s.Length;
        int[,,] dp = new int[n, n, k + 1];

        // Base case: substrings of length 1
        for (int i = 0; i < n; i++) {
            for (int c = 0; c <= k; c++) {
                dp[i, i, c] = 1;
            }
        }

        // Helper to compute cyclic distance between two characters
        int Dist(char a, char b) {
            int x = a - 'a';
            int y = b - 'a';
            int diff = Math.Abs(x - y);
            return Math.Min(diff, 26 - diff);
        }

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                int d = Dist(s[i], s[j]);
                for (int c = 0; c <= k; c++) {
                    int best = Math.Max(dp[i + 1, j, c], dp[i, j - 1, c]);

                    if (c >= d) {
                        int inner = (i + 1 <= j - 1) ? dp[i + 1, j - 1, c - d] : 0;
                        best = Math.Max(best, inner + 2);
                    }

                    dp[i, j, c] = best;
                }
            }
        }

        return dp[0, n - 1, k];
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
var longestPalindromicSubsequence = function(s, k) {
    const n = s.length;
    const K = k;
    const MOD = 26;
    const toIdx = (i, j, c) => ((i * n + j) * (K + 1) + c);
    // distance between two chars in cyclic alphabet
    const dist = (a, b) => {
        const d = Math.abs(a - b);
        return d < MOD - d ? d : MOD - d;
    };
    const codes = new Uint8Array(n);
    for (let i = 0; i < n; ++i) codes[i] = s.charCodeAt(i) - 97;

    const dp = new Uint16Array(n * n * (K + 1));

    // base: single characters
    for (let i = 0; i < n; ++i) {
        const base = toIdx(i, i, 0);
        for (let c = 0; c <= K; ++c) dp[base + c] = 1;
    }

    // lengths from 2 to n
    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            const d = dist(codes[i], codes[j]);
            const idx_i1_j = toIdx(i + 1, j, 0);
            const idx_i_j1 = toIdx(i, j - 1, 0);
            const idx_i1_j1 = toIdx(i + 1, j - 1, 0);
            for (let c = 0; c <= K; ++c) {
                let best = dp[idx_i1_j + c];
                const v2 = dp[idx_i_j1 + c];
                if (v2 > best) best = v2;
                if (c >= d) {
                    const inner = dp[idx_i1_j1 + (c - d)];
                    const cand = inner + 2;
                    if (cand > best) best = cand;
                }
                // ensure monotonicity with cost
                if (c > 0) {
                    const prev = dp[toIdx(i, j, c - 1)];
                    if (prev > best) best = prev;
                }
                dp[toIdx(i, j, c)] = best;
            }
        }
    }

    return dp[toIdx(0, n - 1, K)];
};
```

## Typescript

```typescript
function longestPalindromicSubsequence(s: string, k: number): number {
    const n = s.length;
    const K = k;
    const dp: Uint16Array[][] = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => new Uint16Array(K + 1))
    );

    // base case: single characters
    for (let i = 0; i < n; i++) {
        dp[i][i].fill(1);
    }

    const codes = new Uint8Array(n);
    for (let i = 0; i < n; i++) codes[i] = s.charCodeAt(i) - 97;

    const dist = (a: number, b: number): number => {
        const diff = Math.abs(a - b);
        return diff < 13 ? diff : 26 - diff;
    };

    for (let len = 2; len <= n; len++) {
        for (let l = 0; l + len - 1 < n; l++) {
            const r = l + len - 1;
            const d = dist(codes[l], codes[r]);
            const leftSkip = dp[l + 1][r];
            const rightSkip = dp[l][r - 1];
            const inner = l + 1 <= r - 1 ? dp[l + 1][r - 1] : null;
            const cur = dp[l][r];

            for (let c = 0; c <= K; c++) {
                let best = leftSkip[c];
                if (rightSkip[c] > best) best = rightSkip[c];
                if (c >= d) {
                    const innerVal = inner ? inner[c - d] : 0;
                    const cand = innerVal + 2;
                    if (cand > best) best = cand;
                }
                cur[c] = best;
            }
        }
    }

    return dp[0][n - 1][K];
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
    function longestPalindromicSubsequence($s, $k) {
        $n = strlen($s);
        // dp[i][j] will be an array of size k+1, representing max length with cost <=c
        $dp = array_fill(0, $n, array_fill(0, $n, null));

        // base case: single character substrings
        for ($i = 0; $i < $n; $i++) {
            $arr = array_fill(0, $k + 1, 1); // length 1 palindrome needs no cost
            $dp[$i][$i] = $arr;
        }

        // helper to compute cyclic distance between two characters
        $charDist = function($a, $b) {
            $da = ord($a) - 97; // 'a' ascii is 97
            $db = ord($b) - 97;
            $diff = abs($da - $db);
            return min($diff, 26 - $diff);
        };

        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $j = $i + $len - 1;
                $cur = array_fill(0, $k + 1, 0);
                $left  = $dp[$i + 1][$j];
                $right = $dp[$i][$j - 1];
                $mid   = $dp[$i + 1][$j - 1];
                $pairCost = $charDist($s[$i], $s[$j]);

                for ($c = 0; $c <= $k; $c++) {
                    $best = $left[$c];
                    if ($right[$c] > $best) $best = $right[$c];

                    if ($c >= $pairCost) {
                        $cand = $mid[$c - $pairCost] + 2;
                        if ($cand > $best) $best = $cand;
                    }
                    $cur[$c] = $best;
                }
                $dp[$i][$j] = $cur;
            }
        }

        $ans = 0;
        $finalArr = $dp[0][$n - 1];
        for ($c = 0; $c <= $k; $c++) {
            if ($finalArr[$c] > $ans) $ans = $finalArr[$c];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestPalindromicSubsequence(_ s: String, _ K: Int) -> Int {
        let n = s.count
        if n == 0 { return 0 }
        let chars = Array(s.utf8)
        let k = K
        var dp = [Int](repeating: 0, count: n * n * (k + 1))
        
        func idx(_ i: Int, _ j: Int, _ c: Int) -> Int {
            return ((i * n) + j) * (k + 1) + c
        }
        func get(_ i: Int, _ j: Int, _ c: Int) -> Int {
            if i > j { return 0 }
            return dp[idx(i, j, c)]
        }
        func set(_ i: Int, _ j: Int, _ c: Int, _ val: Int) {
            dp[idx(i, j, c)] = val
        }
        func dist(_ a: UInt8, _ b: UInt8) -> Int {
            let diff = abs(Int(a) - Int(b))
            return min(diff, 26 - diff)
        }
        
        for len in 1...n {
            for i in 0...(n - len) {
                let j = i + len - 1
                for c in 0...k {
                    var best: Int
                    if i == j {
                        best = 1
                    } else {
                        best = max(get(i + 1, j, c), get(i, j - 1, c))
                        let d = dist(chars[i], chars[j])
                        if c >= d {
                            let cand = get(i + 1, j - 1, c - d) + 2
                            if cand > best { best = cand }
                        }
                    }
                    set(i, j, c, best)
                }
            }
        }
        
        var ans = 0
        for c in 0...k {
            let val = get(0, n - 1, c)
            if val > ans { ans = val }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindromicSubsequence(s: String, k: Int): Int {
        val n = s.length
        if (n == 0) return 0
        val K = k
        val dp = Array(n) { Array(n) { IntArray(K + 1) } }
        for (i in 0 until n) {
            for (c in 0..K) {
                dp[i][i][c] = 1
            }
        }
        fun dist(a: Char, b: Char): Int {
            val d = kotlin.math.abs(a.code - b.code)
            return kotlin.math.min(d, 26 - d)
        }
        for (len in 2..n) {
            for (i in 0..n - len) {
                val j = i + len - 1
                val need = dist(s[i], s[j])
                for (c in 0..K) {
                    var best = dp[i + 1][j][c]
                    if (dp[i][j - 1][c] > best) best = dp[i][j - 1][c]
                    if (c >= need) {
                        val cand = dp[i + 1][j - 1][c - need] + 2
                        if (cand > best) best = cand
                    }
                    dp[i][j][c] = best
                }
            }
        }
        var ans = 0
        for (c in 0..K) {
            if (dp[0][n - 1][c] > ans) ans = dp[0][n - 1][c]
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int longestPalindromicSubsequence(String s, int k) {
    int n = s.length;
    List<int> codes = List.generate(n, (i) => s.codeUnitAt(i) - 97);
    var dp = List.generate(
        n, (_) => List.generate(n, (_) => List.filled(k + 1, 0)));
    for (int i = 0; i < n; ++i) {
      for (int c = 0; c <= k; ++c) {
        dp[i][i][c] = 1;
      }
    }

    int min(int a, int b) => a < b ? a : b;
    int cyclicDist(int x, int y) {
      int diff = (x - y).abs();
      return min(diff, 26 - diff);
    }

    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;
        int d = cyclicDist(codes[i], codes[j]);
        for (int c = 0; c <= k; ++c) {
          int best = dp[i + 1][j][c];
          if (dp[i][j - 1][c] > best) best = dp[i][j - 1][c];
          if (c >= d) {
            int inner = (i + 1 <= j - 1) ? dp[i + 1][j - 1][c - d] : 0;
            int cand = inner + 2;
            if (cand > best) best = cand;
          }
          dp[i][j][c] = best;
        }
      }
    }

    return dp[0][n - 1][k];
  }
}
```

## Golang

```go
func longestPalindromicSubsequence(s string, k int) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	// dp[i][j][c] = max length of palindromic subsequence in s[i..j] using at most c operations
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, k+1)
		}
	}
	// base case: single character substrings
	for i := 0; i < n; i++ {
		for c := 0; c <= k; c++ {
			dp[i][i][c] = 1
		}
	}
	// helper to compute cyclic distance between two letters
	dist := func(a, b byte) int {
		x := int(a - 'a')
		y := int(b - 'a')
		diff := (x - y + 26) % 26
		if diff > 13 {
			return 26 - diff
		}
		return diff
	}
	// fill DP for increasing lengths
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			costPair := dist(s[i], s[j])
			for c := 0; c <= k; c++ {
				best := dp[i+1][j][c]
				if dp[i][j-1][c] > best {
					best = dp[i][j-1][c]
				}
				if c >= costPair {
					val := dp[i+1][j-1][c-costPair] + 2
					if val > best {
						best = val
					}
				}
				dp[i][j][c] = best
			}
		}
	}
	return dp[0][n-1][k]
}
```

## Ruby

```ruby
def longest_palindromic_subsequence(s, k)
  n = s.length
  return 0 if n == 0

  # Precompute byte values for faster access
  bytes = s.bytes.map { |b| b - 97 } # 'a' => 0 .. 25

  dp = Array.new(n) { Array.new(n) }

  (0...n).each do |i|
    dp[i][i] = Array.new(k + 1, 1)
  end

  len = 2
  while len <= n
    i = 0
    while i + len <= n
      j = i + len - 1

      left   = dp[i + 1][j]
      right  = dp[i][j - 1]
      inner  = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : Array.new(k + 1, 0)

      d = (bytes[i] - bytes[j]).abs
      cost_pair = d < 26 - d ? d : 26 - d

      cur = Array.new(k + 1, 0)
      c = 0
      while c <= k
        best = left[c] > right[c] ? left[c] : right[c]
        if c >= cost_pair
          val = 2 + inner[c - cost_pair]
          best = val if val > best
        end
        cur[c] = best
        c += 1
      end

      dp[i][j] = cur
      i += 1
    end
    len += 1
  end

  dp[0][n - 1][k]
end
```

## Scala

```scala
object Solution {
    def longestPalindromicSubsequence(s: String, k: Int): Int = {
        val n = s.length
        val chars = s.toCharArray
        val dp = Array.ofDim[Int](n, n, k + 1)

        // Base case: single characters
        for (i <- 0 until n) {
            var c = 0
            while (c <= k) {
                dp(i)(i)(c) = 1
                c += 1
            }
        }

        def dist(a: Char, b: Char): Int = {
            val diff = ((a - b + 26) % 26).toInt
            Math.min(diff, 26 - diff)
        }

        var len = 2
        while (len <= n) {
            var l = 0
            while (l + len - 1 < n) {
                val r = l + len - 1
                val d = dist(chars(l), chars(r))
                var c = 0
                while (c <= k) {
                    var best = dp(l + 1)(r)(c)
                    if (dp(l)(r - 1)(c) > best) best = dp(l)(r - 1)(c)
                    if (c >= d) {
                        val inner = if (l + 1 <= r - 1) dp(l + 1)(r - 1)(c - d) else 0
                        val cand = inner + 2
                        if (cand > best) best = cand
                    }
                    dp(l)(r)(c) = best
                    c += 1
                }
                l += 1
            }
            len += 1
        }

        dp(0)(n - 1)(k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_palindromic_subsequence(s: String, k: i32) -> i32 {
        let n = s.len();
        if n == 0 {
            return 0;
        }
        let bytes = s.as_bytes();
        let K = k as usize;

        // dp[l][r][c] = max palindrome length in s[l..=r] using at most c operations
        let mut dp = vec![vec![vec![0i16; K + 1]; n]; n];

        for i in 0..n {
            for c in 0..=K {
                dp[i][i][c] = 1;
            }
        }

        // minimal cyclic distance between two letters
        let dist = |a: u8, b: u8| -> usize {
            let diff = ((a as i32 - b as i32 + 26) % 26) as usize;
            std::cmp::min(diff, 26 - diff)
        };

        for len in 2..=n {
            for l in 0..=n - len {
                let r = l + len - 1;
                for c in 0..=K {
                    // skip left or right character
                    let mut best = dp[l + 1][r][c].max(dp[l][r - 1][c]);

                    // try to pair s[l] and s[r]
                    let d = dist(bytes[l], bytes[r]);
                    if c >= d {
                        let inner = if l + 1 <= r - 1 {
                            dp[l + 1][r - 1][c - d]
                        } else {
                            0
                        };
                        best = best.max(inner + 2);
                    }

                    dp[l][r][c] = best;
                }
            }
        }

        let mut ans = 0i16;
        for c in 0..=K {
            ans = ans.max(dp[0][n - 1][c]);
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (longest-palindromic-subsequence s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (maxc (+ k 1))
         ;; dp[i][j] is a vector of length maxc
         (dp (let ((tmp (make-vector n)))
               (for ([i (in-range n)])
                 (vector-set! tmp i (make-vector n))
                 (let ((row (vector-ref tmp i)))
                   (for ([j (in-range n)])
                     (vector-set! row j (make-vector maxc 0)))))
               tmp)))
    ;; helper to compute cyclic distance between two chars
    (define (char-dist a b)
      (let* ((ai (- (char->integer a) (char->integer #\a)))
             (bi (- (char->integer b) (char->integer #\a)))
             (diff (abs (- ai bi))))
        (min diff (- 26 diff))))
    ;; DP over substring lengths
    (for ([len (in-range 1 (add1 n))])
      (let ((max-i (- n len))) ; inclusive upper bound for i
        (for ([i (in-range 0 (add1 max-i))])
          (let* ((j (+ i len -1))
                 (row-i (vector-ref dp i))
                 (vec-ij (vector-ref row-i j)))
            (for ([c (in-range maxc)])
              (if (= i j)
                  (vector-set! vec-ij c 1) ; single character
                  (begin
                    ;; best without using both ends
                    (define best
                      (max (vector-ref (vector-ref dp (+ i 1) j) c)
                           (vector-ref (vector-ref dp i (- j 1)) c)))
                    (define d (char-dist (string-ref s i) (string-ref s j)))
                    (when (>= c d)
                      (define inner
                        (if (> (+ i 1) (- j 1))
                            0
                            (vector-ref (vector-ref dp (+ i 1) (- j 1)) (- c d))))
                      (set! best (max best (+ inner 2))))
                    (vector-set! vec-ij c best)))))))))
    ;; answer for whole string with at most k operations
    (if (= n 0)
        0
        (vector-ref (vector-ref dp 0 (- n 1)) k))) )
```

## Erlang

```erlang
-spec longest_palindromic_subsequence(S :: unicode:unicode_binary(), K :: integer()) -> integer().
longest_palindromic_subsequence(S, K) ->
    CharList = binary_to_list(S),
    CharTuple = list_to_tuple([C - $a || C <- CharList]),
    N = length(CharList),
    ZeroTuple = list_to_tuple(lists:duplicate(K + 1, 0)),
    DPMap0 = #{},
    DPMapFinal = longest_pal_subseq_len(1, N, K, CharTuple, ZeroTuple, DPMap0),
    FinalTuple = maps:get({0, N - 1}, DPMapFinal),
    element(K + 1, FinalTuple).

%% iterate over substring lengths
longest_pal_subseq_len(Len, N, _K, _CharTuple, _ZeroTuple, DPMap) when Len > N ->
    DPMap;
longest_pal_subseq_len(Len, N, K, CharTuple, ZeroTuple, DPMap) ->
    DPMap2 = dp_len(Len, N, K, CharTuple, ZeroTuple, DPMap),
    longest_pal_subseq_len(Len + 1, N, K, CharTuple, ZeroTuple, DPMap2).

%% process all i for a given length
dp_len(Len, N, K, CharTuple, ZeroTuple, DPMap) ->
    MaxI = N - Len,
    dp_i(0, MaxI, Len, K, CharTuple, ZeroTuple, DPMap).

dp_i(I, MaxI, _Len, _K, _CharTuple, _ZeroTuple, DPMap) when I > MaxI ->
    DPMap;
dp_i(I, MaxI, Len, K, CharTuple, ZeroTuple, DPMap) ->
    J = I + Len - 1,
    NewDPMap =
        if Len == 1 ->
                Tuple = list_to_tuple(lists:duplicate(K + 1, 1)),
                maps:put({I, J}, Tuple, DPMap);
           true ->
                Prev1 = maps:get({I + 1, J}, DPMap),
                Prev2 = maps:get({I, J - 1}, DPMap),
                Prev3 = if I + 1 =< J - 1 -> maps:get({I + 1, J - 1}, DPMap); true -> ZeroTuple end,
                C1 = element(I + 1, CharTuple),
                C2 = element(J + 1, CharTuple),
                Dist = cyclic_dist(C1, C2),
                Tuple = build_tuple(0, K, Dist, Prev1, Prev2, Prev3, []),
                maps:put({I, J}, Tuple, DPMap)
        end,
    dp_i(I + 1, MaxI, Len, K, CharTuple, ZeroTuple, NewDPMap).

%% build tuple for all cost values
build_tuple(Cur, MaxC, Dist, P1, P2, P3, Acc) when Cur =< MaxC ->
    A1 = element(Cur + 1, P1),
    A2 = element(Cur + 1, P2),
    Best0 = if A1 > A2 -> A1; true -> A2 end,
    Best =
        if Cur >= Dist ->
                Cand = element(Cur - Dist + 1, P3) + 2,
                if Cand > Best0 -> Cand; true -> Best0 end;
           true -> Best0
        end,
    build_tuple(Cur + 1, MaxC, Dist, P1, P2, P3, [Best | Acc]);
build_tuple(_Cur, _MaxC, _Dist, _P1, _P2, _P3, Acc) ->
    list_to_tuple(lists:reverse(Acc)).

%% cyclic distance between two letters (0..25)
cyclic_dist(A, B) ->
    Diff = abs(A - B),
    erlang:min(Diff, 26 - Diff).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindromic_subsequence(s :: String.t(), k :: integer) :: integer
  def longest_palindromic_subsequence(s, k) do
    chars = String.to_charlist(s)
    n = length(chars)

    zero_vec = List.duplicate(0, k + 1) |> List.to_tuple()
    one_vec = List.duplicate(1, k + 1) |> List.to_tuple()

    # base dp for substrings of length 1
    dp =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, {i, i}, one_vec)
      end)

    dp =
      Enum.reduce(2..n, dp, fn len, dp_acc ->
        Enum.reduce(0..(n - len), dp_acc, fn i, inner_dp ->
          j = i + len - 1
          d = dist(Enum.at(chars, i), Enum.at(chars, j))

          vec_i1j = Map.get(inner_dp, {i + 1, j})
          vec_ij1 = Map.get(inner_dp, {i, j - 1})
          vec_inner = Map.get(inner_dp, {i + 1, j - 1}, zero_vec)

          cur_list =
            for c <- 0..k do
              best = max(elem(vec_i1j, c), elem(vec_ij1, c))

              if c >= d do
                cand = elem(vec_inner, c - d) + 2
                if cand > best, do: cand, else: best
              else
                best
              end
            end

          Map.put(inner_dp, {i, j}, List.to_tuple(cur_list))
        end)
      end)

    final_vec = Map.get(dp, {0, n - 1})
    elem(final_vec, k)
  end

  defp dist(a, b) do
    diff = abs(a - b)
    min(diff, 26 - diff)
  end
end
```
