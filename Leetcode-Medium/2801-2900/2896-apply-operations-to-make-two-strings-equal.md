# 2896. Apply Operations to Make Two Strings Equal

## Cpp

```cpp
class Solution {
public:
    int minOperations(string s1, string s2, int x) {
        vector<int> diff;
        int n = s1.size();
        for (int i = 0; i < n; ++i) {
            if (s1[i] != s2[i]) diff.push_back(i);
        }
        int m = diff.size();
        if (m % 2 == 1) return -1;
        if (x >= 2) return m;          // flipping each individually is optimal
        // x == 1 (since x is integer and <2)
        return (m / 2) * x;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(String s1, String s2, int x) {
        int n = s1.length();
        java.util.List<Integer> diff = new java.util.ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                diff.add(i);
            }
        }
        int m = diff.size();
        if ((m & 1) == 1) return -1;
        long[] dp = new long[m + 1];
        dp[0] = 0;
        for (int i = 2; i <= m; i += 2) {
            int d = diff.get(i - 1) - diff.get(i - 2);
            long cost = Math.min((long) x, (long) d);
            dp[i] = dp[i - 2] + cost;
        }
        return (int) dp[m];
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        n = len(s1)
        diff = [i for i in range(n) if s1[i] != s2[i]]
        m = len(diff)
        if m % 2 == 1:
            return -1

        INF = 10**9
        dp = [INF] * (m + 1)
        dp[0] = 0

        for i in range(2, m + 1, 2):
            # pair the last two mismatches directly
            dist = diff[i - 1] - diff[i - 2]
            cost_pair = min(x, dist)
            dp[i] = min(dp[i], dp[i - 2] + cost_pair)

        return dp[m]
```

## Python3

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        mismatches = [i for i in range(len(s1)) if s1[i] != s2[i]]
        m = len(mismatches)
        if m % 2 == 1:
            return -1
        INF = 10**9
        dp = [INF] * (m + 1)
        dp[0] = 0
        pair_cost = min(x, 2)  # cost to fix two mismatched bits together vs two single flips
        for i in range(1, m + 1):
            # flip a single bit
            dp[i] = min(dp[i], dp[i - 1] + 1)
            if i >= 2:
                dp[i] = min(dp[i], dp[i - 2] + pair_cost)
        return dp[m]
```

## C

```c
#include <string.h>

int minOperations(char* s1, char* s2, int x) {
    int n = strlen(s1);
    int diffs[505];
    int m = 0;
    for (int i = 0; i < n; ++i) {
        if (s1[i] != s2[i]) diffs[m++] = i;
    }
    if (m % 2 == 1) return -1;
    if (m == 0) return 0;

    static int dp[505][505];
    const int INF = 1000000000;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < m; ++j)
            dp[i][j] = INF;

    for (int len = 2; len <= m; len += 2) {
        for (int l = 0; l + len - 1 < m; ++l) {
            int r = l + len - 1;
            for (int k = l + 1; k <= r; k += 2) {
                int costPair = diffs[k] - diffs[l];
                if (costPair > x) costPair = x;
                int left = (k == l + 1) ? 0 : dp[l + 1][k - 1];
                int right = (k == r) ? 0 : dp[k + 1][r];
                int total = left + right + costPair;
                if (total < dp[l][r]) dp[l][r] = total;
            }
        }
    }
    return dp[0][m - 1];
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(string s1, string s2, int x) {
        List<int> diff = new List<int>();
        for (int i = 0; i < s1.Length; i++) {
            if (s1[i] != s2[i]) diff.Add(i);
        }
        int m = diff.Count;
        if (m == 0) return 0;
        if ((m & 1) == 1) return -1;

        const int INF = 1_000_000_000;
        int[] dp = new int[m + 1];
        for (int i = 0; i <= m; i++) dp[i] = INF;
        dp[0] = 0;

        for (int i = 1; i <= m; i++) {
            // flip a single mismatched position using operation with cost x
            dp[i] = Math.Min(dp[i], dp[i - 1] + x);
            if (i >= 2) {
                int dist = diff[i - 1] - diff[i - 2];
                int pairCost = Math.Min(dist, 2 * x);
                dp[i] = Math.Min(dp[i], dp[i - 2] + pairCost);
            }
        }

        return dp[m];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {number} x
 * @return {number}
 */
var minOperations = function(s1, s2, x) {
    const n = s1.length;
    const diff = [];
    for (let i = 0; i < n; ++i) {
        if (s1[i] !== s2[i]) diff.push(i);
    }
    const m = diff.length;
    if (m % 2 === 1) return -1;

    const INF = 1e15;
    const dp = new Array(m + 1).fill(INF);
    dp[0] = 0;

    for (let i = 2; i <= m; i += 2) {
        // Pair the last two mismatched positions
        const costPair = Math.min(x, diff[i - 1] - diff[i - 2]);
        dp[i] = Math.min(dp[i], dp[i - 2] + costPair);
    }

    return dp[m];
};
```

## Typescript

```typescript
function minOperations(s1: string, s2: string, x: number): number {
    const n = s1.length;
    const diff: number[] = [];
    for (let i = 0; i < n; i++) {
        if (s1[i] !== s2[i]) diff.push(i);
    }
    const m = diff.length;
    if (m % 2 === 1) return -1;
    let ans = 0;
    for (let i = 0; i < m; i += 2) {
        const dist = diff[i + 1] - diff[i];
        ans += Math.min(x, dist);
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @param Integer $x
     * @return Integer
     */
    function minOperations($s1, $s2, $x) {
        $n = strlen($s1);
        $diff = [];
        for ($i = 0; $i < $n; $i++) {
            if ($s1[$i] !== $s2[$i]) {
                $diff[] = $i;
            }
        }
        $m = count($diff);
        if ($m === 0) return 0;

        $dp = array_fill(0, $m + 1, PHP_INT_MAX);
        $dp[0] = 0;

        for ($i = 1; $i <= $m; $i++) {
            // Use a single flip on the i‑th mismatched position
            if ($dp[$i - 1] + $x < $dp[$i]) {
                $dp[$i] = $dp[$i - 1] + $x;
            }
            // Pair the last two mismatches
            if ($i >= 2) {
                $pairCost = $diff[$i - 1] - $diff[$i - 2];
                $candidate = $dp[$i - 2] + $pairCost;
                if ($candidate < $dp[$i]) {
                    $dp[$i] = $candidate;
                }
            }
        }

        return $dp[$m];
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ s1: String, _ s2: String, _ x: Int) -> Int {
        let n = s1.count
        let a1 = Array(s1)
        let a2 = Array(s2)
        var diff = [Int]()
        for i in 0..<n {
            if a1[i] != a2[i] {
                diff.append(i)
            }
        }
        let m = diff.count
        if m % 2 == 1 { return -1 }
        if m == 0 { return 0 }
        var dp = Array(repeating: Int.max / 2, count: m + 1)
        dp[0] = 0
        for i in stride(from: 2, through: m, by: 2) {
            let cost = min(x, diff[i - 1] - diff[i - 2])
            dp[i] = min(dp[i], dp[i - 2] + cost)
        }
        return dp[m]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(s1: String, s2: String, x: Int): Int {
        val diff = mutableListOf<Int>()
        for (i in s1.indices) {
            if (s1[i] != s2[i]) diff.add(i)
        }
        val m = diff.size
        if (m % 2 == 1) return -1
        if (m == 0) return 0
        val INF = 1_000_000_000
        val dp = Array(m + 1) { IntArray(m + 1) { INF } }
        for (i in 0..m) dp[i][i] = 0
        var len = 2
        while (len <= m) {
            var l = 0
            while (l + len <= m) {
                val r = l + len
                var best = INF
                var k = l + 1
                while (k < r) {
                    val costPair = kotlin.math.min(x, diff[k] - diff[l])
                    val cur = dp[l + 1][k] + dp[k + 1][r] + costPair
                    if (cur < best) best = cur
                    k += 2
                }
                dp[l][r] = best
                l++
            }
            len += 2
        }
        return dp[0][m]
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(String s1, String s2, int x) {
    List<int> diff = [];
    for (int i = 0; i < s1.length; i++) {
      if (s1[i] != s2[i]) diff.add(i);
    }
    int m = diff.length;
    const int INF = 1 << 60;
    List<int> dp = List.filled(m + 1, INF);
    dp[0] = 0;
    for (int i = 1; i <= m; i++) {
      // Flip this single mismatched bit
      dp[i] = dp[i - 1] + x;
      if (i >= 2) {
        int dist = diff[i - 1] - diff[i - 2];
        int pairCost = dist < 2 * x ? dist : 2 * x;
        int candidate = dp[i - 2] + pairCost;
        if (candidate < dp[i]) dp[i] = candidate;
      }
    }
    int ans = dp[m];
    return ans >= INF ~/ 2 ? -1 : ans;
  }
}
```

## Golang

```go
func minOperations(s1 string, s2 string, x int) int {
    n := len(s1)
    diff := make([]int, 0, n)
    for i := 0; i < n; i++ {
        if s1[i] != s2[i] {
            diff = append(diff, i)
        }
    }
    m := len(diff)
    if m%2 == 1 {
        return -1
    }
    // When x == 1, each pair can be fixed with cost 1 using the first operation.
    if x == 1 {
        return m / 2
    }
    ans := 0
    for i := 0; i < m; i += 2 {
        d := diff[i+1] - diff[i]
        if d < x {
            ans += d
        } else {
            ans += x
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_operations(s1, s2, x)
  n = s1.length
  diff = []
  (0...n).each do |i|
    diff << i if s1[i] != s2[i]
  end
  m = diff.size
  return 0 if m == 0
  return -1 if m.odd?

  inf = 1 << 60
  dp = Array.new(m + 1, inf)
  dp[0] = 0

  (1..m).each do |i|
    # flip a single mismatched position
    dp[i] = [dp[i], dp[i - 1] + 1].min
    if i >= 2
      pair_cost = [x, diff[i - 1] - diff[i - 2]].min
      dp[i] = [dp[i], dp[i - 2] + pair_cost].min
    end
  end

  dp[m]
end
```

## Scala

```scala
object Solution {
    def minOperations(s1: String, s2: String, x: Int): Int = {
        val n = s1.length
        val diff = scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < n) {
            if (s1.charAt(i) != s2.charAt(i)) diff += i
            i += 1
        }
        val m = diff.size
        if (m % 2 == 1) return -1
        if (m == 0) return 0

        val INF = Int.MaxValue / 4
        val w = Array.ofDim[Int](m, m)
        var a = 0
        while (a < m) {
            var b = a + 1
            while (b < m) {
                val d = diff(b) - diff(a)
                w(a)(b) = math.min(x, d)
                w(b)(a) = w(a)(b)
                b += 1
            }
            a += 1
        }

        val dp = Array.ofDim[Int](m, m)
        var l = 0
        while (l < m) {
            var r = l
            while (r < m) {
                dp(l)(r) = INF
                r += 1
            }
            l += 1
        }

        var len = 2
        while (len <= m) {
            var left = 0
            while (left + len - 1 < m) {
                val right = left + len - 1
                var best = INF
                var k = left + 1
                while (k <= right) {
                    val costPair = w(left)(k)
                    val leftCost = if (left + 1 <= k - 1) dp(left + 1)(k - 1) else 0
                    val rightCost = if (k + 1 <= right) dp(k + 1)(right) else 0
                    val total = costPair + leftCost + rightCost
                    if (total < best) best = total
                    k += 2 // keep segments even-sized
                }
                dp(left)(right) = best
                left += 1
            }
            len += 2
        }

        dp(0)(m - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(s1: String, s2: String, x: i32) -> i32 {
        let n = s1.len();
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        let mut diff: Vec<i64> = Vec::new();
        for i in 0..n {
            if b1[i] != b2[i] {
                diff.push(i as i64);
            }
        }
        let m = diff.len();
        if m % 2 == 1 {
            return -1;
        }
        let x64 = x as i64;
        let mut dp = vec![i64::MAX / 4; m + 1];
        dp[0] = 0;
        for i in 1..=m {
            // use a single operation (pair with some matched position)
            dp[i] = dp[i].min(dp[i - 1] + x64);
            if i >= 2 {
                let d = diff[i - 1] - diff[i - 2];
                let pair_cost = std::cmp::min(d, x64);
                dp[i] = dp[i].min(dp[i - 2] + pair_cost);
            }
        }
        dp[m] as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations s1 s2 x)
  (-> string? string? exact-integer? exact-integer?)
  (let* ((n (string-length s1))
         (diffs
          (let loop ((i 0) (acc '()))
            (if (= i n)
                (reverse acc)
                (if (char=? (string-ref s1 i) (string-ref s2 i))
                    (loop (+ i 1) acc)
                    (loop (+ i 1) (cons i acc))))))
         (m (length diffs)))
    (if (odd? m)
        -1
        (let ((dp (make-vector (+ m 1) 0)))
          (vector-set! dp 0 0)
          (when (> m 0)
            (vector-set! dp 1 1))
          (for ([i (in-range 2 (+ m 1))])
            (let* ((cost-single (+ (vector-ref dp (- i 1)) 1))
                   (dist (- (list-ref diffs (- i 1))
                            (list-ref diffs (- i 2))))
                   (pair-cost (min x dist))
                   (cost-pair (+ (vector-ref dp (- i 2)) pair-cost)))
              (vector-set! dp i (min cost-single cost-pair))))
          (vector-ref dp m)))))
```

## Erlang

```erlang
-spec min_operations(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), X :: integer()) -> integer().
min_operations(S1, S2, X) ->
    Diff = count_diff(binary_to_list(S1), binary_to_list(S2), 0),
    case Diff rem 2 of
        1 -> -1;
        0 ->
            PairCost = erlang:min(2, X),
            (Diff div 2) * PairCost
    end.

count_diff([], [], Acc) -> Acc;
count_diff([H1|T1], [H2|T2], Acc) ->
    NewAcc = if H1 =:= H2 -> Acc; true -> Acc + 1 end,
    count_diff(T1, T2, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(s1 :: String.t(), s2 :: String.t(), x :: integer) :: integer
  def min_operations(s1, s2, x) do
    s1_bytes = :binary.bin_to_list(s1)
    s2_bytes = :binary.bin_to_list(s2)

    diff =
      Enum.with_index(s1_bytes)
      |> Enum.reduce([], fn {c, i}, acc ->
        if c != Enum.at(s2_bytes, i), do: [i | acc], else: acc
      end)
      |> Enum.reverse()

    m = length(diff)

    if rem(m, 2) == 1 do
      -1
    else
      pairs = div(m, 2)

      Enum.reduce(0..(pairs - 1), 0, fn k, acc ->
        i = k * 2
        a = Enum.at(diff, i)
        b = Enum.at(diff, i + 1)
        gap = b - a
        pair_cost = min(min(x, gap), 2)
        acc + pair_cost
      end)
    end
  end
end
```
