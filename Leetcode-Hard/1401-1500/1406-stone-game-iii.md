# 1406. Stone Game III

## Cpp

```cpp
class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<long long> dp(n + 1, 0); // dp[i]: max diff current player can achieve from i
        const long long NEG_INF = -4e18;
        for (int i = n - 1; i >= 0; --i) {
            long long best = NEG_INF;
            long long sum = 0;
            for (int k = 1; k <= 3 && i + k <= n; ++k) {
                sum += stoneValue[i + k - 1];
                long long candidate = sum - dp[i + k];
                if (candidate > best) best = candidate;
            }
            dp[i] = best;
        }
        if (dp[0] > 0) return "Alice";
        if (dp[0] == 0) return "Tie";
        return "Bob";
    }
};
```

## Java

```java
class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        long[] dp = new long[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            long take = 0;
            long best = Long.MIN_VALUE;
            for (int k = 1; k <= 3 && i + k <= n; ++k) {
                take += stoneValue[i + k - 1];
                long cur = take - dp[i + k];
                if (cur > best) {
                    best = cur;
                }
            }
            dp[i] = best;
        }
        long diff = dp[0];
        if (diff > 0) return "Alice";
        if (diff < 0) return "Bob";
        return "Tie";
    }
}
```

## Python

```python
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i]: max difference current player can achieve from i
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            cur_sum = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                cur_sum += stoneValue[i + k - 1]
                # opponent will get dp[i+k], so current diff is cur_sum - dp[i+k]
                best = max(best, cur_sum - dp[i + k])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
```

## Python3

```python
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 4)  # extra space for i+3 accesses
        for i in range(n - 1, -1, -1):
            best = -10**9
            cur_sum = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                cur_sum += stoneValue[i + k - 1]
                candidate = cur_sum - dp[i + k]
                if candidate > best:
                    best = candidate
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

char* stoneGameIII(int* stoneValue, int stoneValueSize) {
    int n = stoneValueSize;
    int *dp = (int*)malloc((n + 1) * sizeof(int));
    dp[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        int best = INT_MIN;
        int sum = 0;
        for (int k = 1; k <= 3 && i + k <= n; ++k) {
            sum += stoneValue[i + k - 1];
            int cand = sum - dp[i + k];
            if (cand > best) best = cand;
        }
        dp[i] = best;
    }
    int diff = dp[0];
    free(dp);
    
    const char *ans;
    if (diff > 0) ans = "Alice";
    else if (diff < 0) ans = "Bob";
    else ans = "Tie";
    
    char *res = (char*)malloc(strlen(ans) + 1);
    strcpy(res, ans);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string StoneGameIII(int[] stoneValue) {
        int n = stoneValue.Length;
        long[] dp = new long[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            long best = long.MinValue;
            long sum = 0;
            for (int k = 1; k <= 3 && i + k <= n; ++k) {
                sum += stoneValue[i + k - 1];
                long candidate = sum - dp[i + k];
                if (candidate > best) best = candidate;
            }
            dp[i] = best;
        }
        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stoneValue
 * @return {string}
 */
var stoneGameIII = function(stoneValue) {
    const n = stoneValue.length;
    const dp = new Array(n + 1).fill(0); // dp[i]: max diff current player can achieve from i
    
    for (let i = n - 1; i >= 0; --i) {
        let best = -Infinity;
        let sum = 0;
        for (let k = 1; k <= 3 && i + k <= n; ++k) {
            sum += stoneValue[i + k - 1];
            const cur = sum - dp[i + k];
            if (cur > best) best = cur;
        }
        dp[i] = best;
    }
    
    if (dp[0] > 0) return "Alice";
    if (dp[0] < 0) return "Bob";
    return "Tie";
};
```

## Typescript

```typescript
function stoneGameIII(stoneValue: number[]): string {
    const n = stoneValue.length;
    const dp = new Array<number>(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        let best = -Infinity;
        let curSum = 0;
        for (let k = 1; k <= 3 && i + k <= n; ++k) {
            curSum += stoneValue[i + k - 1];
            const diff = curSum - dp[i + k];
            if (diff > best) best = diff;
        }
        dp[i] = best;
    }
    if (dp[0] > 0) return "Alice";
    if (dp[0] < 0) return "Bob";
    return "Tie";
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stoneValue
     * @return String
     */
    function stoneGameIII($stoneValue) {
        $n = count($stoneValue);
        $dp = array_fill(0, $n + 1, 0); // dp[n] = 0

        for ($i = $n - 1; $i >= 0; --$i) {
            $take = 0;
            $best = -INF;
            for ($k = 1; $k <= 3 && $i + $k <= $n; ++$k) {
                $take += $stoneValue[$i + $k - 1];
                $candidate = $take - $dp[$i + $k];
                if ($candidate > $best) {
                    $best = $candidate;
                }
            }
            $dp[$i] = $best;
        }

        $diff = $dp[0];
        if ($diff > 0) {
            return "Alice";
        } elseif ($diff < 0) {
            return "Bob";
        } else {
            return "Tie";
        }
    }
}
```

## Swift

```swift
class Solution {
    func stoneGameIII(_ stoneValue: [Int]) -> String {
        let n = stoneValue.count
        var dp = Array(repeating: 0, count: n + 4)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var best = Int.min
            var takeSum = 0
            for k in 1...3 {
                if i + k - 1 < n {
                    takeSum += stoneValue[i + k - 1]
                    let cur = takeSum - dp[i + k]
                    if cur > best { best = cur }
                }
            }
            dp[i] = best
        }
        let diff = dp[0]
        if diff > 0 {
            return "Alice"
        } else if diff < 0 {
            return "Bob"
        } else {
            return "Tie"
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGameIII(stoneValue: IntArray): String {
        val n = stoneValue.size
        val dp = IntArray(n + 4)
        for (i in n - 1 downTo 0) {
            var sum = 0
            var best = Int.MIN_VALUE
            for (k in 1..3) {
                if (i + k - 1 >= n) break
                sum += stoneValue[i + k - 1]
                val candidate = sum - dp[i + k]
                if (candidate > best) best = candidate
            }
            dp[i] = best
        }
        return when {
            dp[0] > 0 -> "Alice"
            dp[0] < 0 -> "Bob"
            else -> "Tie"
        }
    }
}
```

## Dart

```dart
class Solution {
  String stoneGameIII(List<int> stoneValue) {
    int n = stoneValue.length;
    List<int> dp = List.filled(n + 1, 0);
    const int NEG_INF = -(1 << 60);
    for (int i = n - 1; i >= 0; --i) {
      int sum = 0;
      int best = NEG_INF;
      for (int k = 1; k <= 3 && i + k <= n; ++k) {
        sum += stoneValue[i + k - 1];
        int candidate = sum - dp[i + k];
        if (candidate > best) best = candidate;
      }
      dp[i] = best;
    }
    if (dp[0] > 0) return "Alice";
    if (dp[0] < 0) return "Bob";
    return "Tie";
  }
}
```

## Golang

```go
func stoneGameIII(stoneValue []int) string {
    n := len(stoneValue)
    dp := make([]int, n+1)
    const negInf = -1 << 60
    for i := n - 1; i >= 0; i-- {
        sum := 0
        best := negInf
        for k := 1; k <= 3 && i+k <= n; k++ {
            sum += stoneValue[i+k-1]
            cand := sum - dp[i+k]
            if cand > best {
                best = cand
            }
        }
        dp[i] = best
    }
    if dp[0] > 0 {
        return "Alice"
    } else if dp[0] < 0 {
        return "Bob"
    }
    return "Tie"
}
```

## Ruby

```ruby
def stone_game_iii(stone_value)
  n = stone_value.length
  dp = Array.new(n + 1, 0)

  (n - 1).downto(0) do |i|
    best = -Float::INFINITY
    sum = 0
    1.upto(3) do |k|
      break if i + k > n
      sum += stone_value[i + k - 1]
      candidate = sum - dp[i + k]
      best = candidate if candidate > best
    end
    dp[i] = best
  end

  diff = dp[0]
  if diff > 0
    "Alice"
  elsif diff < 0
    "Bob"
  else
    "Tie"
  end
end
```

## Scala

```scala
object Solution {
    def stoneGameIII(stoneValue: Array[Int]): String = {
        val n = stoneValue.length
        val dp = new Array[Int](n + 1)
        for (i <- n - 1 to 0 by -1) {
            var best = Int.MinValue
            var sum = 0
            var k = 1
            while (k <= 3 && i + k <= n) {
                sum += stoneValue(i + k - 1)
                val cur = sum - dp(i + k)
                if (cur > best) best = cur
                k += 1
            }
            dp(i) = best
        }
        if (dp(0) > 0) "Alice"
        else if (dp(0) < 0) "Bob"
        else "Tie"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        let n = stone_value.len();
        let mut dp = vec![0i64; n + 1];
        for i in (0..n).rev() {
            let mut best = i64::MIN;
            let mut sum = 0i64;
            for k in 0..3 {
                if i + k >= n { break; }
                sum += stone_value[i + k] as i64;
                let cur = sum - dp[i + k + 1];
                if cur > best {
                    best = cur;
                }
            }
            dp[i] = best;
        }
        let diff = dp[0];
        if diff > 0 {
            "Alice".to_string()
        } else if diff < 0 {
            "Bob".to_string()
        } else {
            "Tie".to_string()
        }
    }
}
```

## Racket

```racket
(define/contract (stone-game-iii stoneValue)
  (-> (listof exact-integer?) string?)
  (let* ((n (length stoneValue))
         (stones (list->vector stoneValue))
         (dp (make-vector (+ n 1) 0)))
    (for ([i (in-range (sub1 n) -1 -1)])
      (let ((best -1000000000)
            (sum 0))
        (for ([k (in-range 1 4)])
          (when (<= (+ i k) n)
            (set! sum (+ sum (vector-ref stones (- (+ i k) 1))))
            (let ((candidate (- sum (vector-ref dp (+ i k)))))
              (when (> candidate best)
                (set! best candidate)))))
        (vector-set! dp i best)))
    (let ((diff (vector-ref dp 0)))
      (cond [(> diff 0) "Alice"]
            [(< diff 0) "Bob"]
            [else "Tie"]))))
```

## Erlang

```erlang
-export([stone_game_iii/1]).

-spec stone_game_iii(StoneValue :: [integer()]) -> unicode:unicode_binary().
stone_game_iii(StoneValue) ->
    Tuple = list_to_tuple(StoneValue),
    Len = tuple_size(Tuple),
    Indices = lists:seq(0, Len - 1),
    RevIdx = lists:reverse(Indices),
    NegInf = -1000000000,
    {Diff, _, _} =
        lists:foldl(
            fun(I, {Dp1, Dp2, Dp3}) ->
                V1 = element(I + 1, Tuple),
                Cand1 = V1 - Dp1,
                Cand2 = if I + 1 < Len ->
                            V2 = element(I + 2, Tuple),
                            (V1 + V2) - Dp2;
                        true -> NegInf
                    end,
                Cand3 = if I + 2 < Len ->
                            V2 = element(I + 2, Tuple),
                            V3 = element(I + 3, Tuple),
                            (V1 + V2 + V3) - Dp3;
                        true -> NegInf
                    end,
                MaxCand = max(Cand1, max(Cand2, Cand3)),
                {MaxCand, Dp1, Dp2}
            end,
            {0, 0, 0},
            RevIdx),
    case Diff > 0 of
        true -> <<"Alice">>;
        false ->
            case Diff < 0 of
                true -> <<"Bob">>;
                false -> <<"Tie">>
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec stone_game_iii(stone_value :: [integer]) :: String.t()
  def stone_game_iii(stone_value) do
    stones = List.to_tuple(stone_value)
    n = tuple_size(stones)

    diff = compute(n - 1, stones, n, 0, 0, 0)

    cond do
      diff > 0 -> "Alice"
      diff < 0 -> "Bob"
      true -> "Tie"
    end
  end

  defp compute(i, _stones, _n, dp0, _dp1, _dp2) when i < 0, do: dp0

  defp compute(i, stones, n, dp0, dp1, dp2) do
    # take one stone
    sum1 = elem(stones, i)
    cand1 = sum1 - dp0
    best = cand1

    {best, sum2} =
      if i + 2 <= n do
        s = sum1 + elem(stones, i + 1)
        c = s - dp1
        {if(c > best, do: c, else: best), s}
      else
        {best, sum1}
      end

    best =
      if i + 3 <= n do
        s = sum2 + elem(stones, i + 2)
        c = s - dp2
        if(c > best, do: c, else: best)
      else
        best
      end

    compute(i - 1, stones, n, best, dp0, dp1)
  end
end
```
