# 1278. Palindrome Partitioning III

## Cpp

```cpp
class Solution {
public:
    int palindromePartition(string s, int k) {
        int n = s.size();
        vector<vector<int>> cost(n, vector<int>(n, 0));
        // compute cost[l][r]: min changes to make s[l..r] a palindrome
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                if (len == 2) {
                    cost[l][r] = (s[l] != s[r]);
                } else {
                    cost[l][r] = cost[l + 1][r - 1] + (s[l] != s[r]);
                }
            }
        }
        const int INF = 1e9;
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, INF));
        dp[0][0] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int p = 1; p <= min(k, i); ++p) {
                for (int j = p - 1; j < i; ++j) { // previous split point
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1]);
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
    public int palindromePartition(String s, int k) {
        int n = s.length();
        // cost[i][j]: min changes to make s[i..j] a palindrome
        int[][] cost = new int[n][n];
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                if (s.charAt(i) == s.charAt(j)) {
                    cost[i][j] = (len == 2) ? 0 : cost[i + 1][j - 1];
                } else {
                    cost[i][j] = (len == 2) ? 1 : cost[i + 1][j - 1] + 1;
                }
            }
        }

        int INF = 1_000_000;
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 0; i <= n; ++i) {
            java.util.Arrays.fill(dp[i], INF);
        }
        dp[0][0] = 0;

        for (int i = 1; i <= n; ++i) { // prefix length
            for (int p = 1; p <= Math.min(k, i); ++p) {
                // last palindrome starts at t (0-indexed), ends at i-1
                for (int t = p - 1; t < i; ++t) {
                    int prev = dp[t][p - 1];
                    if (prev == INF) continue;
                    int add = cost[t][i - 1];
                    dp[i][p] = Math.min(dp[i][p], prev + add);
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
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # precompute cost to make any substring a palindrome
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                cnt = 0
                l, r = i, j
                while l < r:
                    if s[l] != s[r]:
                        cnt += 1
                    l += 1
                    r -= 1
                cost[i][j] = cnt

        from functools import lru_cache
        INF = 10 ** 9

        @lru_cache(None)
        def dfs(pos, parts):
            # pos: start index of the remaining suffix
            # parts: number of palindromes we still need to create
            if parts == 0:
                return 0 if pos == n else INF
            if pos >= n:
                return INF
            if parts == 1:
                return cost[pos][n - 1]
            best = INF
            # ensure at least (parts-1) characters remain for the rest
            max_end = n - (parts - 1)
            for end in range(pos, max_end):
                cur = cost[pos][end] + dfs(end + 1, parts - 1)
                if cur < best:
                    best = cur
            return best

        return dfs(0, k)
```

## Python3

```python
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        # precompute cost to make any substring a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                add = 0 if s[i] == s[j] else 1
                if length == 2:
                    cost[i][j] = add
                else:
                    cost[i][j] = cost[i + 1][j - 1] + add

        INF = 10 ** 9
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            max_p = min(k, i)
            for p in range(1, max_p + 1):
                best = INF
                # previous cut at position j (0 <= j < i)
                for j in range(p - 1, i):
                    cur = dp[j][p - 1] + cost[j][i - 1]
                    if cur < best:
                        best = cur
                dp[i][p] = best

        return dp[n][k]
```

## C

```c
#include <string.h>
#include <limits.h>

int palindromePartition(char* s, int k) {
    int n = strlen(s);
    const int MAXN = 105;
    static int cost[MAXN][MAXN];
    static int dp[MAXN][MAXN];
    
    // Precompute cost to make any substring a palindrome
    for (int i = 0; i < n; ++i) cost[i][i] = 0;
    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                cost[i][j] = (i + 1 <= j - 1) ? cost[i + 1][j - 1] : 0;
            } else {
                cost[i][j] = ((i + 1 <= j - 1) ? cost[i + 1][j - 1] : 0) + 1;
            }
        }
    }
    
    const int INF = INT_MAX / 2;
    for (int i = 0; i <= n; ++i)
        for (int p = 0; p <= k; ++p)
            dp[i][p] = INF;
    dp[0][0] = 0;
    
    for (int i = 1; i <= n; ++i) {
        for (int p = 1; p <= k && p <= i; ++p) {
            int best = INF;
            // previous cut position t, substring [t, i-1]
            for (int t = p - 1; t < i; ++t) {
                if (dp[t][p - 1] == INF) continue;
                int cur = dp[t][p - 1] + cost[t][i - 1];
                if (cur < best) best = cur;
            }
            dp[i][p] = best;
        }
    }
    
    return dp[n][k];
}
```

## Csharp

```csharp
public class Solution {
    public int PalindromePartition(string s, int k) {
        int n = s.Length;
        int[,] cost = new int[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int cnt = 0;
                int l = i, r = j;
                while (l < r) {
                    if (s[l] != s[r]) cnt++;
                    l++; r--;
                }
                cost[i, j] = cnt;
            }
        }

        const int INF = 1_000_000;
        int[,] dp = new int[n + 1, k + 1];
        for (int i = 0; i <= n; i++) {
            for (int p = 0; p <= k; p++) dp[i, p] = INF;
        }
        dp[0, 0] = 0;

        for (int i = 1; i <= n; i++) {
            int maxP = Math.Min(k, i);
            for (int p = 1; p <= maxP; p++) {
                int best = INF;
                for (int t = p - 1; t <= i - 1; t++) {
                    if (dp[t, p - 1] == INF) continue;
                    int val = dp[t, p - 1] + cost[t, i - 1];
                    if (val < best) best = val;
                }
                dp[i, p] = best;
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
var palindromePartition = function(s, k) {
    const n = s.length;
    // precompute cost[i][j]: min changes to make s[i..j] a palindrome
    const cost = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        for (let j = i; j < n; ++j) {
            let cnt = 0;
            let l = i, r = j;
            while (l < r) {
                if (s[l] !== s[r]) cnt++;
                l++; r--;
            }
            cost[i][j] = cnt;
        }
    }

    const INF = 1e9;
    // dp[i][p]: min changes for first i characters split into p palindromes
    const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(INF));
    dp[0][0] = 0;

    for (let i = 1; i <= n; ++i) {
        for (let p = 1; p <= k && p <= i; ++p) {
            // try last cut before position i
            for (let j = p - 1; j < i; ++j) { // need at least p-1 chars for previous parts
                const prev = dp[j][p - 1];
                if (prev !== INF) {
                    const curCost = cost[j][i - 1];
                    if (prev + curCost < dp[i][p]) {
                        dp[i][p] = prev + curCost;
                    }
                }
            }
        }
    }

    return dp[n][k];
};
```

## Typescript

```typescript
function palindromePartition(s: string, k: number): number {
    const n = s.length;
    const cost: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    // Precompute minimum changes to make any substring a palindrome
    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            if (len === 2) {
                cost[i][j] = s[i] === s[j] ? 0 : 1;
            } else {
                cost[i][j] = cost[i + 1][j - 1] + (s[i] === s[j] ? 0 : 1);
            }
        }
    }

    const INF = 1e9;
    const dp: number[][] = Array.from({ length: n + 1 }, () => Array(k + 1).fill(INF));
    dp[0][0] = 0;

    for (let t = 1; t <= n; ++t) {
        for (let p = 1; p <= k && p <= t; ++p) {
            let best = INF;
            // previous cut position
            for (let prev = p - 1; prev < t; ++prev) {
                const cur = dp[prev][p - 1] + cost[prev][t - 1];
                if (cur < best) best = cur;
            }
            dp[t][p] = best;
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
    function palindromePartition($s, $k) {
        $n = strlen($s);
        // precompute cost to make any substring a palindrome
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $j = $i + $len - 1;
                if ($s[$i] === $s[$j]) {
                    $inner = ($len > 2) ? $cost[$i + 1][$j - 1] : 0;
                    $cost[$i][$j] = $inner;
                } else {
                    $inner = ($len > 2) ? $cost[$i + 1][$j - 1] : 0;
                    $cost[$i][$j] = $inner + 1;
                }
            }
        }

        $INF = PHP_INT_MAX;
        // dp[i][p]: min changes for first i characters split into p palindromes
        $dp = array_fill(0, $n + 1, array_fill(0, $k + 1, $INF));
        $dp[0][0] = 0;

        for ($i = 1; $i <= $n; $i++) {
            $maxP = min($k, $i);
            for ($p = 1; $p <= $maxP; $p++) {
                // previous cut position j (start of current segment)
                for ($j = $p - 1; $j < $i; $j++) {
                    if ($dp[$j][$p - 1] === $INF) continue;
                    $c = $cost[$j][$i - 1];
                    $val = $dp[$j][$p - 1] + $c;
                    if ($val < $dp[$i][$p]) {
                        $dp[$i][$p] = $val;
                    }
                }
            }
        }

        return $dp[$n][$k];
    }
}
```

## Swift

```swift
class Solution {
    func palindromePartition(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var cost = Array(repeating: Array(repeating: 0, count: n), count: n)
        
        // Precompute minimal changes to make any substring a palindrome
        for i in 0..<n {
            for j in i..<n {
                var cnt = 0
                var l = i
                var r = j
                while l < r {
                    if chars[l] != chars[r] { cnt += 1 }
                    l += 1
                    r -= 1
                }
                cost[i][j] = cnt
            }
        }
        
        let INF = 1_000_000
        var dp = Array(repeating: Array(repeating: INF, count: k + 1), count: n + 1)
        dp[0][0] = 0
        
        if k == 0 { return 0 }
        
        for i in 1...n {
            for p in 1...k {
                if p > i { continue } // cannot have more partitions than characters
                var best = INF
                // previous cut position t (start of current substring)
                for t in (p - 1)...(i - 1) {
                    let cur = dp[t][p - 1] + cost[t][i - 1]
                    if cur < best { best = cur }
                }
                dp[i][p] = best
            }
        }
        
        return dp[n][k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun palindromePartition(s: String, k: Int): Int {
        val n = s.length
        // precompute cost to make any substring a palindrome
        val cost = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in i until n) {
                var cnt = 0
                var l = i
                var r = j
                while (l < r) {
                    if (s[l] != s[r]) cnt++
                    l++; r--
                }
                cost[i][j] = cnt
            }
        }

        val INF = 1_000_000_000
        val dp = Array(n + 1) { IntArray(k + 1) { INF } }
        dp[0][0] = 0

        for (i in 1..n) {
            val maxP = if (k < i) k else i
            for (p in 1..maxP) {
                var best = INF
                // previous cut position j, substring s[j..i-1]
                for (j in p - 1 .. i - 1) {
                    val prev = dp[j][p - 1]
                    if (prev == INF) continue
                    val cur = prev + cost[j][i - 1]
                    if (cur < best) best = cur
                }
                dp[i][p] = best
            }
        }

        return dp[n][k]
    }
}
```

## Dart

```dart
class Solution {
  int palindromePartition(String s, int k) {
    int n = s.length;
    List<int> chars = s.codeUnits;

    // Precompute cost to make any substring a palindrome
    List<List<int>> cost = List.generate(n, (_) => List.filled(n, 0));
    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;
        int inner = (i + 1 <= j - 1) ? cost[i + 1][j - 1] : 0;
        cost[i][j] = inner + (chars[i] == chars[j] ? 0 : 1);
      }
    }

    const int INF = 1 << 30;
    // dp[pos][parts] = minimal changes for suffix starting at pos with exactly parts partitions
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(k + 1, INF));
    dp[n][0] = 0;

    for (int i = n - 1; i >= 0; --i) {
      for (int parts = 1; parts <= k; ++parts) {
        if (n - i < parts) {
          dp[i][parts] = INF;
          continue;
        }
        int best = INF;
        // try ending the first part at j
        for (int j = i; j < n; ++j) {
          // remaining characters must be enough for remaining parts-1
          if (n - (j + 1) < parts - 1) break;
          int curCost = cost[i][j];
          int next = dp[j + 1][parts - 1];
          if (next != INF && curCost + next < best) {
            best = curCost + next;
          }
        }
        dp[i][parts] = best;
      }
    }

    return dp[0][k];
  }
}
```

## Golang

```go
func palindromePartition(s string, k int) int {
	n := len(s)
	// precompute cost[i][j]: min changes to make s[i..j] a palindrome
	cost := make([][]int, n)
	for i := 0; i < n; i++ {
		cost[i] = make([]int, n)
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			if s[i] == s[j] {
				if i+1 <= j-1 {
					cost[i][j] = cost[i+1][j-1]
				} else {
					cost[i][j] = 0
				}
			} else {
				if i+1 <= j-1 {
					cost[i][j] = cost[i+1][j-1] + 1
				} else {
					cost[i][j] = 1
				}
			}
		}
	}
	const INF = int(1 << 30)
	// dp[i][p]: min changes for first i characters split into p palindromes
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, k+1)
		for p := 0; p <= k; p++ {
			dp[i][p] = INF
		}
	}
	dp[0][0] = 0

	for i := 1; i <= n; i++ {
		for p := 1; p <= k && p <= i; p++ {
			best := INF
			// split point t: prefix length before current part
			for t := p - 1; t < i; t++ {
				if dp[t][p-1] == INF {
					continue
				}
				cur := dp[t][p-1] + cost[t][i-1]
				if cur < best {
					best = cur
				}
			}
			dp[i][p] = best
		}
	}
	return dp[n][k]
}
```

## Ruby

```ruby
def palindrome_partition(s, k)
  n = s.length
  # Precompute cost to make any substring a palindrome
  cost = Array.new(n) { Array.new(n, 0) }
  (0...n).each do |i|
    (i...n).each do |j|
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

  inf = 1 << 30
  dp = Array.new(n + 1) { Array.new(k + 1, inf) }
  dp[0][0] = 0

  (1..n).each do |i|
    (1..k).each do |p|
      # last segment starts at j (0-index), ends at i-1
      (p - 1...i).each do |j|
        prev = dp[j][p - 1]
        next if prev == inf
        cur = prev + cost[j][i - 1]
        dp[i][p] = cur if cur < dp[i][p]
      end
    end
  end

  dp[n][k]
end
```

## Scala

```scala
object Solution {
  def palindromePartition(s: String, k: Int): Int = {
    val n = s.length
    // cost[i][j]: min changes to make s[i..j] a palindrome
    val cost = Array.ofDim[Int](n, n)
    for (i <- 0 until n) cost(i)(i) = 0
    for (len <- 2 to n) {
      var i = 0
      while (i + len <= n) {
        val j = i + len - 1
        val inner = if (i + 1 <= j - 1) cost(i + 1)(j - 1) else 0
        cost(i)(j) = inner + (if (s.charAt(i) == s.charAt(j)) 0 else 1)
        i += 1
      }
    }

    val INF = Int.MaxValue / 4
    val dp = Array.ofDim[Int](n + 1, k + 1)
    for (i <- 0 to n; p <- 0 to k) dp(i)(p) = INF
    dp(0)(0) = 0

    for (i <- 1 to n) {
      val maxP = math.min(k, i)
      var p = 1
      while (p <= maxP) {
        var best = INF
        var t = p - 1 // previous cut position
        while (t <= i - 1) {
          val prev = dp(t)(p - 1)
          if (prev != INF) {
            val cur = cost(t)(i - 1)
            val total = prev + cur
            if (total < best) best = total
          }
          t += 1
        }
        dp(i)(p) = best
        p += 1
      }
    }

    dp(n)(k)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn palindrome_partition(s: String, k: i32) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();

        // cost[i][j]: minimum changes to make s[i..=j] a palindrome
        let mut cost = vec![vec![0i32; n]; n];
        for i in (0..n).rev() {
            for j in i + 1..n {
                let inner = if i + 1 <= j - 1 { cost[i + 1][j - 1] } else { 0 };
                cost[i][j] = inner + if bytes[i] == bytes[j] { 0 } else { 1 };
            }
        }

        let k_usize = k as usize;
        let inf: i32 = 1_000_000_000;
        // dp[p][i]: min changes to partition first i characters into p palindromes
        let mut dp = vec![vec![inf; n + 1]; k_usize + 1];
        dp[0][0] = 0;

        for p in 1..=k_usize {
            for i in 1..=n {
                let mut best = inf;
                // last segment starts at j, ends at i-1
                for j in (p - 1)..=i - 1 {
                    let prev = dp[p - 1][j];
                    if prev == inf {
                        continue;
                    }
                    let c = cost[j][i - 1];
                    let cand = prev + c;
                    if cand < best {
                        best = cand;
                    }
                }
                dp[p][i] = best;
            }
        }

        dp[k_usize][n]
    }
}
```

## Racket

```racket
(define/contract (palindrome-partition s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (INF 1000000)
         ;; precompute cost[i][j]: min changes to make s[i..j] palindrome
         (cost (let ((mat (make-vector n)))
                 (for ([i (in-range n)])
                   (vector-set! mat i (make-vector n INF))
                   (for ([j (in-range i n)])
                     (let loop ((l i) (r j) (cnt 0))
                       (if (>= l r)
                           (vector-set! (vector-ref mat i) j cnt)
                           (let ((c1 (string-ref s l))
                                 (c2 (string-ref s r)))
                             (loop (+ l 1) (- r 1)
                                   (if (char=? c1 c2) cnt (+ cnt 1))))))))
                 mat))
         ;; dp[i][p]: min changes for first i chars split into p palindromes
         (dp (let ((mat (make-vector (add1 n))))
               (for ([i (in-range (add1 n))])
                 (vector-set! mat i (make-vector (add1 k) INF)))
               (vector-set! (vector-ref mat 0) 0 0)
               mat)))
    ;; DP computation
    (for ([i (in-range 1 (add1 n))])
      (let ((maxp (min i k)))
        (for ([p (in-range 1 (add1 maxp))])
          (let ((best (let loop ((j (sub1 i)) (cur INF))
                        (if (< j (sub1 p))
                            cur
                            (let* ((prev (vector-ref (vector-ref dp j) (sub1 p)))
                                   (cst  (vector-ref (vector-ref cost j) (sub1 i)))
                                   (total (+ prev cst)))
                              (loop (- j 1) (if (< total cur) total cur)))))))
            (vector-set! (vector-ref dp i) p best)))))
    (vector-ref (vector-ref dp n) k)))
```

## Erlang

```erlang
-module(solution).
-export([palindrome_partition/2]).

-spec palindrome_partition(S :: unicode:unicode_binary(), K :: integer()) -> integer().
palindrome_partition(S, K) ->
    L = unicode:characters_to_list(S),
    N = length(L),
    CostMap = build_cost_map(L, N),
    INF = 1 bsl 30,
    DP = fill_dp(1, K, N, CostMap, INF, #{}),
    maps:get({K,0}, DP).

build_cost_map(L, N) ->
    lists:foldl(fun(I, AccI) ->
        lists:foldl(fun(J, AccJ) ->
            C = cost_substring(L, I, J),
            maps:put({I,J}, C, AccJ)
        end, AccI, lists:seq(I, N-1))
    end, #{}, lists:seq(0, N-1)).

cost_substring(L, I, J) ->
    Len = J - I + 1,
    Half = Len div 2,
    cost_substring_loop(L, I, J, 0, Half).

cost_substring_loop(_L, _I, _J, Offset, Half) when Offset >= Half -> 0;
cost_substring_loop(L, I, J, Offset, Half) ->
    CharLeft = lists:nth(I + Offset + 1, L),
    CharRight = lists:nth(J - Offset + 1, L),
    Diff = if CharLeft =:= CharRight -> 0; true -> 1 end,
    Diff + cost_substring_loop(L, I, J, Offset+1, Half).

fill_dp(CurCnt, MaxCnt, N, CostMap, INF, DP) when CurCnt > MaxCnt ->
    DP;
fill_dp(CurCnt, MaxCnt, N, CostMap, INF, DP) ->
    Positions = lists:seq(0, N-1),
    NewDP = lists:foldl(fun(Pos, AccDP) ->
        Remaining = N - Pos,
        UpdatedDP =
            if Remaining < CurCnt ->
                    maps:put({CurCnt,Pos}, INF, AccDP);
               true ->
                    Value =
                        if CurCnt == 1 ->
                                maps:get({Pos,N-1}, CostMap);
                           true ->
                                MaxEnd = N - CurCnt,
                                Values = [ maps:get({Pos,End}, CostMap) +
                                           maps:get({CurCnt-1, End+1}, AccDP)
                                         || End <- lists:seq(Pos, MaxEnd) ],
                                lists:min(Values)
                        end,
                    maps:put({CurCnt,Pos}, Value, AccDP)
            end,
        UpdatedDP
    end, DP, Positions),
    fill_dp(CurCnt + 1, MaxCnt, N, CostMap, INF, NewDP).
```

## Elixir

```elixir
defmodule Solution do
  @spec palindrome_partition(s :: String.t(), k :: integer) :: integer
  def palindrome_partition(s, k) do
    chars = String.graphemes(s)
    n = length(chars)

    # Precompute cost to make any substring a palindrome
    cost =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, {i, i}, 0)
      end)
      |> Enum.reduce(2..n, fn len, acc ->
        Enum.reduce(0..(n - len), acc, fn i, acc2 ->
          j = i + len - 1

          inner =
            if i + 1 <= j - 1 do
              Map.get(acc2, {i + 1, j - 1}, 0)
            else
              0
            end

          add = if Enum.at(chars, i) == Enum.at(chars, j), do: 0, else: 1
          Map.put(acc2, {i, j}, inner + add)
        end)
      end)

    inf = 1_000_000

    # DP map: key {p, i} -> minimal changes for first i chars split into p parts
    dp_initial = %{{0, 0} => 0}

    dp =
      Enum.reduce(1..k, dp_initial, fn p, dp_acc ->
        Enum.reduce(1..n, dp_acc, fn i, dp2 ->
          if i < p do
            Map.put(dp2, {p, i}, inf)
          else
            min_val =
              Enum.reduce(p - 1..i - 1, inf, fn j, cur_min ->
                prev = Map.get(dp2, {p - 1, j}, inf)

                if prev == inf do
                  cur_min
                else
                  c = Map.get(cost, {j, i - 1}, 0)
                  val = prev + c

                  if val < cur_min, do: val, else: cur_min
                end
              end)

            Map.put(dp2, {p, i}, min_val)
          end
        end)
      end)

    Map.get(dp, {k, n})
  end
end
```
