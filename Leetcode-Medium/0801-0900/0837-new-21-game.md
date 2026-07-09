# 0837. New 21 Game

## Cpp

```cpp
class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (k == 0 || n >= k + maxPts - 1) return 1.0;
        vector<double> dp(n + 1, 0.0);
        dp[0] = 1.0;
        double windowSum = 1.0; // sum of probabilities for the last maxPts states that are < k
        for (int i = 1; i <= n; ++i) {
            dp[i] = windowSum / maxPts;
            if (i < k) {
                windowSum += dp[i];
            }
            if (i - maxPts >= 0 && i - maxPts < k) {
                windowSum -= dp[i - maxPts];
            }
        }
        double ans = 0.0;
        for (int i = k; i <= n; ++i) ans += dp[i];
        return ans;
    }
};
```

## Java

```java
class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if (k == 0 || n >= k + maxPts - 1) {
            return 1.0;
        }
        double[] dp = new double[n + 1];
        dp[0] = 1.0;
        double windowSum = 1.0; // sum of probabilities that can lead to the next point
        for (int i = 1; i <= n; i++) {
            dp[i] = windowSum / maxPts;
            if (i < k) {
                windowSum += dp[i];
            }
            int outIdx = i - maxPts;
            if (outIdx >= 0 && outIdx < k) {
                windowSum -= dp[outIdx];
            }
        }
        double ans = 0.0;
        for (int i = k; i <= n; i++) {
            ans += dp[i];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        ans = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            else:
                ans += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return ans
```

## Python3

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Edge cases
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0  # sum of probabilities for the last maxPts states that are still active (< k)

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return sum(dp[k:])
```

## C

```c
#include <stdlib.h>

double new21Game(int n, int k, int maxPts) {
    if (k == 0 || n >= k + maxPts - 1) return 1.0;
    
    double *dp = (double *)calloc(n + 1, sizeof(double));
    dp[0] = 1.0;
    double windowSum = 1.0;   // sum of probabilities in the sliding window
    double result = 0.0;
    
    for (int i = 1; i <= n; ++i) {
        dp[i] = windowSum / maxPts;
        
        if (i < k) {
            windowSum += dp[i];
        } else {
            result += dp[i];   // terminal states
        }
        
        if (i - maxPts >= 0) {
            windowSum -= dp[i - maxPts];
        }
    }
    
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public double New21Game(int n, int k, int maxPts) {
        if (k == 0 || n >= k + maxPts - 1) return 1.0;
        double[] dp = new double[n + 1];
        dp[0] = 1.0;
        double windowSum = 1.0;
        for (int i = 1; i <= n; ++i) {
            dp[i] = windowSum / maxPts;
            if (i < k) {
                windowSum += dp[i];
            }
            if (i - maxPts >= 0) {
                windowSum -= dp[i - maxPts];
            }
        }
        double ans = 0.0;
        for (int i = k; i <= n; ++i) {
            ans += dp[i];
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} maxPts
 * @return {number}
 */
var new21Game = function(n, k, maxPts) {
    if (k === 0) return 1.0;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1.0;
    let windowSum = 1.0; // sum of probabilities for states < k within the last maxPts draws
    for (let i = 1; i <= n; ++i) {
        dp[i] = windowSum / maxPts;
        if (i < k) {
            windowSum += dp[i];
        }
        const outIdx = i - maxPts;
        if (outIdx >= 0 && outIdx < k) {
            windowSum -= dp[outIdx];
        }
    }
    let ans = 0.0;
    for (let i = k; i <= n; ++i) {
        ans += dp[i];
    }
    return ans;
};
```

## Typescript

```typescript
function new21Game(n: number, k: number, maxPts: number): number {
    if (k === 0 || n >= k + maxPts - 1) return 1;
    const dp = new Array<number>(n + 1).fill(0);
    dp[0] = 1;
    let windowSum = 1; // sum of probabilities for the last maxPts states that are still < k
    let result = 0;
    for (let i = 1; i <= n; i++) {
        dp[i] = windowSum / maxPts;
        if (i < k) {
            windowSum += dp[i];
        } else {
            result += dp[i];
        }
        const outIdx = i - maxPts;
        if (outIdx >= 0 && outIdx < k) {
            windowSum -= dp[outIdx];
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $maxPts
     * @return Float
     */
    function new21Game($n, $k, $maxPts) {
        if ($k == 0 || $n >= $k + $maxPts - 1) {
            return 1.0;
        }

        $dp = array_fill(0, $n + 1, 0.0);
        $dp[0] = 1.0;
        $windowSum = 1.0; // sum of probabilities for the last maxPts states that are still < k

        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $windowSum / $maxPts;

            if ($i < $k) {
                $windowSum += $dp[$i];
            }

            if ($i - $maxPts >= 0) {
                $windowSum -= $dp[$i - $maxPts];
            }
        }

        $ans = 0.0;
        for ($i = $k; $i <= $n; $i++) {
            $ans += $dp[$i];
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func new21Game(_ n: Int, _ k: Int, _ maxPts: Int) -> Double {
        if k == 0 || n >= k + maxPts - 1 {
            return 1.0
        }
        var dp = [Double](repeating: 0.0, count: n + 1)
        dp[0] = 1.0
        var windowSum = 1.0
        var result = 0.0
        
        for i in 1...n {
            dp[i] = windowSum / Double(maxPts)
            if i >= k {
                result += dp[i]
            }
            if i < k {
                windowSum += dp[i]
            }
            let removeIdx = i - maxPts
            if removeIdx >= 0 && removeIdx < k {
                windowSum -= dp[removeIdx]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun new21Game(n: Int, k: Int, maxPts: Int): Double {
        if (k == 0) return 1.0
        // Maximum possible points after the game ends is (k - 1) + maxPts
        if (n >= k - 1 + maxPts) return 1.0

        val dp = DoubleArray(n + 1)
        dp[0] = 1.0
        var window = 0.0
        var answer = 0.0

        for (i in 1..n) {
            // Add probability from state i-1 if it is still drawing
            if (i - 1 < k) {
                window += dp[i - 1]
            }
            // Remove probability that falls out of the sliding window
            val outIdx = i - maxPts - 1
            if (outIdx >= 0 && outIdx < k) {
                window -= dp[outIdx]
            }

            dp[i] = window / maxPts
            if (i >= k) {
                answer += dp[i]
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  double new21Game(int n, int k, int maxPts) {
    if (k == 0) return 1.0;
    // If the maximum possible score after stopping is <= n, probability is 1.
    if (n >= k + maxPts - 1) return 1.0;

    List<double> dp = List.filled(n + 1, 0.0);
    dp[0] = 1.0;
    double windowSum = 1.0; // sum of probabilities for the last maxPts scores that are still < k
    double ans = 0.0;

    for (int i = 1; i <= n; ++i) {
      dp[i] = windowSum / maxPts;
      if (i < k) {
        windowSum += dp[i];
      } else {
        ans += dp[i];
      }
      int outIdx = i - maxPts;
      if (outIdx >= 0 && outIdx < k) {
        windowSum -= dp[outIdx];
      }
    }

    return ans;
  }
}
```

## Golang

```go
func new21Game(n int, k int, maxPts int) float64 {
	if k == 0 {
		return 1.0
	}
	if n >= k-1+maxPts {
		return 1.0
	}
	dp := make([]float64, n+1)
	dp[0] = 1.0
	windowSum := 1.0 // sum of dp[i] where i is in the sliding window and i < k

	for i := 1; i <= n; i++ {
		dp[i] = windowSum / float64(maxPts)

		if i < k {
			windowSum += dp[i]
		}
		if i-maxPts >= 0 && i-maxPts < k {
			windowSum -= dp[i-maxPts]
		}
	}

	ans := 0.0
	for i := k; i <= n; i++ {
		ans += dp[i]
	}
	return ans
}
```

## Ruby

```ruby
def new21_game(n, k, max_pts)
  return 1.0 if k == 0 || n >= k + max_pts - 1

  dp = Array.new(n + 1, 0.0)
  dp[0] = 1.0
  window_sum = 0.0

  (1..n).each do |i|
    window_sum += dp[i - 1] if i - 1 < k
    if i - max_pts - 1 >= 0 && i - max_pts - 1 < k
      window_sum -= dp[i - max_pts - 1]
    end
    dp[i] = window_sum / max_pts
  end

  ans = 0.0
  (k..n).each { |i| ans += dp[i] }
  ans
end
```

## Scala

```scala
object Solution {
    def new21Game(n: Int, k: Int, maxPts: Int): Double = {
        if (k == 0 || n >= k + maxPts - 1) return 1.0
        val dp = new Array[Double](n + 1)
        dp(0) = 1.0
        var windowSum = 1.0
        for (i <- 1 to n) {
            dp(i) = windowSum / maxPts
            if (i < k) {
                windowSum += dp(i)
            }
            if (i - maxPts >= 0) {
                windowSum -= dp(i - maxPts)
            }
        }
        var ans = 0.0
        for (i <- k to n) {
            ans += dp(i)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        let n = n as usize;
        let k = k as usize;
        let max_pts = max_pts as usize;

        if k == 0 || n >= k + max_pts - 1 {
            return 1.0;
        }

        let mut dp = vec![0f64; n + 1];
        dp[0] = 1.0;
        let mut window_sum = 1.0_f64;
        let mut ans = 0.0_f64;

        for i in 1..=n {
            let prob = window_sum / max_pts as f64;
            dp[i] = prob;
            if i >= k {
                ans += prob;
            }
            if i < k {
                window_sum += prob;
            }
            if i >= max_pts {
                let idx = i - max_pts;
                if idx < k {
                    window_sum -= dp[idx];
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (new21-game n k maxPts)
  (-> exact-integer? exact-integer? exact-integer? flonum?)
  (cond
    [(= k 0) 1.0]
    [(>= n (+ k maxPts -1)) 1.0]
    [else
     (let* ([dp (make-vector (add1 n) 0.0)])
       (vector-set! dp 0 1.0)
       (define window 1.0)
       (define ans 0.0)
       (for ([i (in-range 1 (add1 n))])
         (let ([prob (/ window maxPts)])
           (vector-set! dp i prob)
           (when (>= i k) (set! ans (+ ans prob)))
           (when (< i k) (set! window (+ window prob)))
           (when (>= (- i maxPts) 0)
             (let ([sub (vector-ref dp (- i maxPts))])
               (set! window (- window sub))))))
       ans)]))
```

## Erlang

```erlang
-module(solution).
-export([new21_game/3]).

-spec new21_game(N :: integer(), K :: integer(), MaxPts :: integer()) -> float().
new21_game(N, K, MaxPts) ->
    case K of
        0 ->
            1.0;
        _ ->
            if N >= K + MaxPts - 1 ->
                    1.0;
               true ->
                    DP0 = array:new(N + 1),
                    DP1 = array:set(0, 1.0, DP0),
                    loop(1, 1.0, 0.0, K, MaxPts, N, DP1)
            end
    end.

loop(I, W, Ans, K, MaxPts, N, DP) when I > N ->
    Ans;
loop(I, W, Ans, K, MaxPts, N, DP) ->
    DpI = W / MaxPts,
    DP2 = array:set(I, DpI, DP),
    W1 = if I < K -> W + DpI; true -> W end,
    SubIdx = I - MaxPts,
    W2 = if SubIdx >= 0 andalso SubIdx < K ->
                Val = array:get(SubIdx, DP2),
                W1 - Val;
            true -> W1
        end,
    Ans1 = if I >= K -> Ans + DpI; true -> Ans end,
    loop(I + 1, W2, Ans1, K, MaxPts, N, DP2).
```

## Elixir

```elixir
defmodule Solution do
  @spec new21_game(n :: integer, k :: integer, max_pts :: integer) :: float
  def new21_game(n, k, max_pts) do
    cond do
      k == 0 ->
        1.0

      n >= k + max_pts - 1 ->
        1.0

      true ->
        dp = :array.new(n + 1, default: 0.0)
        dp = :array.set(0, 1.0, dp)

        {dp_final, _} =
          Enum.reduce(1..n, {dp, 1.0}, fn i, {dp_acc, sum_acc} ->
            val = sum_acc / max_pts
            dp_acc = :array.set(i, val, dp_acc)

            sum_acc =
              if i < k do
                sum_acc + val
              else
                sum_acc
              end

            out_idx = i - max_pts

            sum_acc =
              if out_idx >= 0 and out_idx < k do
                out_val = :array.get(out_idx, dp_acc)
                sum_acc - out_val
              else
                sum_acc
              end

            {dp_acc, sum_acc}
          end)

        Enum.reduce(k..n, 0.0, fn i, acc ->
          acc + :array.get(i, dp_final)
        end)
    end
  end
end
```
