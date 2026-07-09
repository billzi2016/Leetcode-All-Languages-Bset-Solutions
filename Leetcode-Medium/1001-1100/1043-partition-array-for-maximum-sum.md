# 1043. Partition Array for Maximum Sum

## Cpp

```cpp
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            int curMax = 0;
            for (int len = 1; len <= k && i + len <= n; ++len) {
                curMax = max(curMax, arr[i + len - 1]);
                dp[i] = max(dp[i], curMax * len + dp[i + len]);
            }
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.length;
        long[] dp = new long[n + 1];
        for (int i = n - 1; i >= 0; --i) {
            long curMax = 0;
            long best = 0;
            for (int j = 1; j <= k && i + j <= n; ++j) {
                curMax = Math.max(curMax, arr[i + j - 1]);
                long candidate = curMax * j + dp[i + j];
                if (candidate > best) {
                    best = candidate;
                }
            }
            dp[i] = best;
        }
        return (int) dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * (n + 1)  # dp[i]: max sum for subarray starting at i
        for i in range(n - 1, -1, -1):
            cur_max = 0
            best = 0
            for length in range(1, k + 1):
                if i + length > n:
                    break
                cur_max = max(cur_max, arr[i + length - 1])
                best = max(best, cur_max * length + dp[i + length])
            dp[i] = best
        return dp[0]
```

## Python3

```python
from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            cur_max = 0
            best = 0
            limit = min(k, n - i)
            for j in range(1, limit + 1):
                cur_max = max(cur_max, arr[i + j - 1])
                best = max(best, cur_max * j + dp[i + j])
            dp[i] = best
        return dp[0]
```

## C

```c
int maxSumAfterPartitioning(int* arr, int arrSize, int k) {
    int *dp = (int *)malloc((arrSize + 1) * sizeof(int));
    dp[arrSize] = 0;
    for (int i = arrSize - 1; i >= 0; --i) {
        long long best = 0;
        int curMax = 0;
        for (int len = 1; len <= k && i + len <= arrSize; ++len) {
            if (arr[i + len - 1] > curMax) curMax = arr[i + len - 1];
            long long cand = (long long)curMax * len + dp[i + len];
            if (cand > best) best = cand;
        }
        dp[i] = (int)best;
    }
    int ans = dp[0];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxSumAfterPartitioning(int[] arr, int k)
    {
        int n = arr.Length;
        long[] dp = new long[n + 1]; // dp[n] = 0 by default

        for (int i = n - 1; i >= 0; i--)
        {
            long best = 0;
            int maxVal = 0;

            for (int len = 1; len <= k && i + len <= n; len++)
            {
                if (arr[i + len - 1] > maxVal)
                    maxVal = arr[i + len - 1];

                long candidate = (long)maxVal * len + dp[i + len];
                if (candidate > best)
                    best = candidate;
            }

            dp[i] = best;
        }

        return (int)dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var maxSumAfterPartitioning = function(arr, k) {
    const n = arr.length;
    const dp = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        let curMax = 0;
        let best = 0;
        for (let len = 1; len <= k && i + len <= n; len++) {
            curMax = Math.max(curMax, arr[i + len - 1]);
            best = Math.max(best, dp[i + len] + curMax * len);
        }
        dp[i] = best;
    }
    return dp[0];
};
```

## Typescript

```typescript
function maxSumAfterPartitioning(arr: number[], k: number): number {
    const n = arr.length;
    const dp = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        let curMax = 0;
        let best = 0;
        for (let len = 1; len <= k && i + len <= n; ++len) {
            curMax = Math.max(curMax, arr[i + len - 1]);
            const candidate = curMax * len + dp[i + len];
            if (candidate > best) best = candidate;
        }
        dp[i] = best;
    }
    return dp[0];
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function maxSumAfterPartitioning($arr, $k) {
        $n = count($arr);
        $dp = array_fill(0, $n + 1, 0); // dp[n] = 0

        for ($i = $n - 1; $i >= 0; --$i) {
            $maxVal = 0;
            $best = 0;
            $limit = min($n - 1, $i + $k - 1);
            for ($j = $i; $j <= $limit; ++$j) {
                if ($arr[$j] > $maxVal) {
                    $maxVal = $arr[$j];
                }
                $len = $j - $i + 1;
                $candidate = $maxVal * $len + $dp[$j + 1];
                if ($candidate > $best) {
                    $best = $candidate;
                }
            }
            $dp[$i] = $best;
        }

        return $dp[0];
    }
}
?>
```

## Swift

```swift
class Solution {
    func maxSumAfterPartitioning(_ arr: [Int], _ k: Int) -> Int {
        let n = arr.count
        var dp = Array(repeating: 0, count: n + 1)
        if n == 0 { return 0 }
        for i in stride(from: n - 1, through: 0, by: -1) {
            var curMax = 0
            var best = 0
            var j = i
            while j < min(n, i + k) {
                curMax = max(curMax, arr[j])
                let length = j - i + 1
                let candidate = curMax * length + dp[j + 1]
                if candidate > best { best = candidate }
                j += 1
            }
            dp[i] = best
        }
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumAfterPartitioning(arr: IntArray, k: Int): Int {
        val n = arr.size
        val dp = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            var curMax = 0
            var best = 0
            var j = i
            while (j < n && j - i + 1 <= k) {
                if (arr[j] > curMax) curMax = arr[j]
                val len = j - i + 1
                val candidate = curMax * len + dp[j + 1]
                if (candidate > best) best = candidate
                j++
            }
            dp[i] = best
        }
        return dp[0]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxSumAfterPartitioning(List<int> arr, int k) {
    final n = arr.length;
    final dp = List<int>.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      int curMax = 0;
      int best = 0;
      for (int j = 1; j <= k && i + j <= n; ++j) {
        curMax = max(curMax, arr[i + j - 1]);
        best = max(best, dp[i + j] + curMax * j);
      }
      dp[i] = best;
    }
    return dp[0];
  }
}
```

## Golang

```go
func maxSumAfterPartitioning(arr []int, k int) int {
	n := len(arr)
	dp := make([]int, n+1)

	for i := n - 1; i >= 0; i-- {
		maxVal := 0
		best := 0
		limit := k
		if i+limit > n {
			limit = n - i
		}
		for j := 1; j <= limit; j++ {
			if arr[i+j-1] > maxVal {
				maxVal = arr[i+j-1]
			}
			cur := maxVal*j + dp[i+j]
			if cur > best {
				best = cur
			}
		}
		dp[i] = best
	}
	return dp[0]
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def max_sum_after_partitioning(arr, k)
  n = arr.length
  dp = Array.new(n + 1, 0)

  (n - 1).downto(0) do |i|
    max_val = 0
    j = 0
    while j < k && i + j < n
      cur = arr[i + j]
      max_val = cur if cur > max_val
      candidate = max_val * (j + 1) + dp[i + j + 1]
      dp[i] = candidate if candidate > dp[i]
      j += 1
    end
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
    def maxSumAfterPartitioning(arr: Array[Int], k: Int): Int = {
        val n = arr.length
        val dp = new Array[Long](n + 1) // dp[n] = 0 by default
        for (i <- (n - 1) to 0 by -1) {
            var curMax = 0L
            var best = 0L
            var j = i
            while (j < n && j - i + 1 <= k) {
                curMax = math.max(curMax, arr(j).toLong)
                val len = j - i + 1
                val candidate = curMax * len + dp(j + 1)
                if (candidate > best) best = candidate
                j += 1
            }
            dp(i) = best
        }
        dp(0).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let k_usize = k as usize;
        // dp[i] stores the maximum sum for subarray starting at index i
        let mut dp = vec![0i64; n + 1];
        for i in (0..n).rev() {
            let mut cur_max = 0i64;
            let mut best = 0i64;
            let limit = std::cmp::min(n, i + k_usize);
            for j in i..limit {
                cur_max = cur_max.max(arr[j] as i64);
                let len = (j - i + 1) as i64;
                let candidate = cur_max * len + dp[j + 1];
                if candidate > best {
                    best = candidate;
                }
            }
            dp[i] = best;
        }
        dp[0] as i32
    }
}
```

## Racket

```racket
(define/contract (max-sum-after-partitioning arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector arr))
         (n (vector-length v))
         (dp (make-vector (+ n 1) 0)))
    (for ([start (in-range (sub1 n) -1 -1)])
      (let ((best 0)
            (curr-max 0))
        (for ([len (in-range 1 (+ k 1))])
          (when (<= (+ start len) n)
            (define idx (- (+ start len) 1))
            (define val (vector-ref v idx))
            (set! curr-max (max curr-max val))
            (define candidate (+ (* curr-max len) (vector-ref dp (+ start len))))
            (set! best (max best candidate))))
        (vector-set! dp start best)))
    (vector-ref dp 0)))
```

## Erlang

```erlang
-spec max_sum_after_partitioning(Arr :: [integer()], K :: integer()) -> integer().
max_sum_after_partitioning(Arr, K) ->
    N = length(Arr),
    ArrT = list_to_tuple(Arr),
    DP0 = #{N => 0},
    DP = compute(N - 1, ArrT, K, DP0),
    maps:get(0, DP).

%% Compute dp values from index I down to 0.
compute(-1, _ArrT, _K, DP) ->
    DP;
compute(I, ArrT, K, DP) ->
    Max = find_max_loop(I, ArrT, K, DP, 1, 0, 0),
    NewDP = maps:put(I, Max, DP),
    compute(I - 1, ArrT, K, NewDP).

%% Iterate over possible subarray lengths starting at I.
find_max_loop(_I, _ArrT, _K, _DP, L, _CurrMax, Best) when L > _K ->
    Best;
find_max_loop(I, ArrT, K, DP, L, CurrMax, Best) ->
    N = tuple_size(ArrT),
    case I + L =< N of
        true ->
            Val = element(I + L, ArrT),               % tuple is 1‑based
            NewCurrMax = erlang:max(CurrMax, Val),
            Sum = NewCurrMax * L + maps:get(I + L, DP),
            NewBest = erlang:max(Best, Sum),
            find_max_loop(I, ArrT, K, DP, L + 1, NewCurrMax, NewBest);
        false ->
            Best
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_after_partitioning(arr :: [integer], k :: integer) :: integer
  def max_sum_after_partitioning(arr, k) do
    n = length(arr)
    # dp tuple of size n+1, indexed from 1 (dp[0] at position 1)
    dp = :erlang.make_tuple(n + 1, 0)

    dp =
      Enum.reduce(:lists.seq(n - 1, 0, -1), dp, fn start, dp_acc ->
        {_, best} =
          Enum.reduce(1..k, {0, 0}, fn len, {cur_max, cur_best} ->
            i = start + len - 1

            if i >= n do
              {cur_max, cur_best}
            else
              val = Enum.at(arr, i)
              new_max = if val > cur_max, do: val, else: cur_max
              next_sum = :erlang.element(i + 2, dp_acc)   # dp[i+1]
              total = new_max * len + next_sum
              new_best = if total > cur_best, do: total, else: cur_best
              {new_max, new_best}
            end
          end)

        :erlang.setelement(start + 1, dp_acc, best)
      end)

    :erlang.element(1, dp)
  end
end
```
