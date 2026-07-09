# 2547. Minimum Cost to Split an Array

## Cpp

```cpp
class Solution {
public:
    int minCost(vector<int>& nums, int k) {
        int n = nums.size();
        const long long INF = (1LL<<60);
        vector<long long> dp(n+1, INF);
        dp[0] = 0;
        for (int r = 1; r <= n; ++r) {
            vector<int> freq(n, 0);
            long long cur = 0;
            long long best = INF;
            for (int l = r; l >= 1; --l) {
                int x = nums[l-1];
                int cnt = ++freq[x];
                if (cnt == 2) cur += 2;
                else if (cnt > 2) cur += 1;
                long long cost = dp[l-1] + k + cur;
                if (cost < best) best = cost;
            }
            dp[r] = best;
        }
        return (int)dp[n];
    }
};
```

## Java

```java
class Solution {
    public int minCost(int[] nums, int k) {
        int n = nums.length;
        long[] dp = new long[n + 1];
        final long INF = Long.MAX_VALUE / 4;
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;
        int size = n; // because nums[i] < n
        for (int r = 1; r <= n; r++) {
            int[] freq = new int[size];
            long importance = 0;
            for (int l = r - 1; l >= 0; l--) {
                int val = nums[l];
                freq[val]++;
                if (freq[val] == 2) {
                    importance += 2;
                } else if (freq[val] > 2) {
                    importance += 1;
                }
                long cost = dp[l] + k + importance;
                if (cost < dp[r]) dp[r] = cost;
            }
        }
        return (int) dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0

        for r in range(1, n + 1):
            freq = {}
            dup_len = 0
            best = INF
            # expand subarray to the left
            for l in range(r, 0, -1):
                x = nums[l - 1]
                cnt = freq.get(x, 0)
                if cnt == 1:
                    dup_len += 2          # count becomes 2, add both occurrences
                elif cnt >= 2:
                    dup_len += 1          # each additional occurrence adds one more
                freq[x] = cnt + 1

                cur = dp[l - 1] + k + dup_len
                if cur < best:
                    best = cur
            dp[r] = best

        return dp[n]
```

## Python3

```python
from typing import List

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for r in range(1, n + 1):
            freq = {}
            cur = 0
            best = INF
            for l in range(r, 0, -1):
                x = nums[l - 1]
                f = freq.get(x, 0)
                if f == 1:
                    cur += 2          # becomes duplicated, both occurrences count
                elif f >= 2:
                    cur += 1          # already counted, add one more occurrence
                # f == 0 -> first occurrence, no contribution to trimmed length
                freq[x] = f + 1
                cost = dp[l - 1] + k + cur
                if cost < best:
                    best = cost
            dp[r] = best
        return dp[n]
```

## C

```c
#include <limits.h>
#include <string.h>
#include <stdlib.h>

int minCost(int* nums, int numsSize, int k) {
    const long long INF = (1LL << 60);
    long long *dp = (long long *)malloc((numsSize + 1) * sizeof(long long));
    for (int i = 0; i <= numsSize; ++i) dp[i] = INF;
    dp[0] = 0;

    int maxVal = numsSize; // nums[i] < numsSize
    int *freq = (int *)malloc((maxVal + 1) * sizeof(int));

    for (int r = 1; r <= numsSize; ++r) {
        memset(freq, 0, (maxVal + 1) * sizeof(int));
        long long cur = 0;
        dp[r] = INF;
        for (int l = r - 1; l >= 0; --l) {
            int x = nums[l];
            if (freq[x] == 0) {
                // becomes 1, no contribution
            } else if (freq[x] == 1) {
                cur += 2; // both occurrences now counted
            } else {
                cur += 1; // additional occurrence counted
            }
            freq[x]++;

            long long cost = dp[l] + k + cur;
            if (cost < dp[r]) dp[r] = cost;
        }
    }

    int result = (int)dp[numsSize];
    free(dp);
    free(freq);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MinCost(int[] nums, int k) {
        int n = nums.Length;
        long[] dp = new long[n + 1];
        const long INF = (long)4e18;
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;

        for (int r = 1; r <= n; r++) {
            int[] freq = new int[n];
            int curTrim = 0;
            dp[r] = INF;
            for (int l = r - 1; l >= 0; --l) {
                int x = nums[l];
                if (freq[x] == 0) {
                    freq[x] = 1;
                } else if (freq[x] == 1) {
                    freq[x] = 2;
                    curTrim += 2;
                } else {
                    freq[x]++;
                    curTrim += 1;
                }
                long candidate = dp[l] + k + curTrim;
                if (candidate < dp[r]) dp[r] = candidate;
            }
        }

        return (int)dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minCost = function(nums, k) {
    const n = nums.length;
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;
    // Since nums[i] < n, we can size frequency array to n
    for (let r = 1; r <= n; ++r) {
        const freq = new Array(n).fill(0);
        let trimmedLen = 0;
        for (let l = r - 1; l >= 0; --l) {
            const x = nums[l];
            freq[x]++;
            if (freq[x] === 2) {
                trimmedLen += 2; // both occurrences now count
            } else if (freq[x] > 2) {
                trimmedLen += 1; // each extra occurrence adds one
            }
            dp[r] = Math.min(dp[r], dp[l] + k + trimmedLen);
        }
    }
    return dp[n];
};
```

## Typescript

```typescript
function minCost(nums: number[], k: number): number {
    const n = nums.length;
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    for (let r = 1; r <= n; ++r) {
        const freq = new Array(n + 1).fill(0);
        let trimmed = 0;
        for (let l = r - 1; l >= 0; --l) {
            const x = nums[l];
            freq[x]++;
            if (freq[x] === 2) {
                trimmed += 2;
            } else if (freq[x] > 2) {
                trimmed += 1;
            }
            const cost = k + trimmed;
            const candidate = dp[l] + cost;
            if (candidate < dp[r]) dp[r] = candidate;
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minCost($nums, $k) {
        $n = count($nums);
        $INF = 1 << 60;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;

        for ($r = 1; $r <= $n; $r++) {
            $freq = [];
            $extra = 0; // trimmed length for current subarray [l..r-1]

            for ($l = $r - 1; $l >= 0; $l--) {
                $x = $nums[$l];
                if (!isset($freq[$x])) {
                    $freq[$x] = 1;
                } else {
                    $prev = $freq[$x];
                    $freq[$x] = $prev + 1;
                    if ($prev == 1) {
                        // element becomes duplicated, both occurrences count
                        $extra += 2;
                    } elseif ($prev >= 2) {
                        // another occurrence of already duplicated element
                        $extra += 1;
                    }
                }

                $cost = $dp[$l] + $k + $extra;
                if ($cost < $dp[$r]) {
                    $dp[$r] = $cost;
                }
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var dp = Array(repeating: Int.max / 2, count: n + 1)
        dp[0] = 0
        
        for r in 1...n {
            var freq = Array(repeating: 0, count: n + 1) // nums[i] < n
            var cur = k
            var l = r - 1
            while l >= 0 {
                let x = nums[l]
                let f = freq[x]
                if f == 1 {
                    cur += 2
                } else if f >= 2 {
                    cur += 1
                }
                freq[x] = f + 1
                dp[r] = min(dp[r], dp[l] + cur)
                l -= 1
            }
        }
        
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(nums: IntArray, k: Int): Int {
        val n = nums.size
        val dp = LongArray(n + 1) { Long.MAX_VALUE / 4 }
        dp[0] = 0L
        for (r in 1..n) {
            val freq = IntArray(n)
            var trimmed = 0L
            for (l in r - 1 downTo 0) {
                val x = nums[l]
                when (freq[x]) {
                    0 -> {}
                    1 -> trimmed += 2
                    else -> trimmed += 1
                }
                freq[x]++
                val cost = dp[l] + k.toLong() + trimmed
                if (cost < dp[r]) dp[r] = cost
            }
        }
        return dp[n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minCost(List<int> nums, int k) {
    int n = nums.length;
    const int INF = 0x7FFFFFFFFFFFFFFF; // large value
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    for (int r = 1; r <= n; ++r) {
      List<int> freq = List.filled(n, 0);
      int trimmedLen = 0;
      for (int l = r - 1; l >= 0; --l) {
        int x = nums[l];
        if (freq[x] == 0) {
          freq[x] = 1;
        } else if (freq[x] == 1) {
          freq[x] = 2;
          trimmedLen += 2;
        } else {
          freq[x]++;
          trimmedLen += 1;
        }
        int cost = dp[l] + k + trimmedLen;
        if (cost < dp[r]) dp[r] = cost;
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
package main

func minCost(nums []int, k int) int {
	n := len(nums)
	const INF = int(1 << 60)

	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	for r := 1; r <= n; r++ {
		freq := make([]int, n) // nums[i] < n
		cur := 0
		for l := r - 1; l >= 0; l-- {
			x := nums[l]
			cnt := freq[x]
			if cnt == 1 {
				cur += 2
			} else if cnt >= 2 {
				cur++
			}
			freq[x] = cnt + 1

			cost := dp[l] + k + cur
			if cost < dp[r] {
				dp[r] = cost
			}
		}
	}

	return dp[n]
}
```

## Ruby

```ruby
def min_cost(nums, k)
  n = nums.length
  INF = 1 << 60
  dp = Array.new(n + 1, INF)
  dp[0] = 0

  (1..n).each do |r|
    freq = Hash.new(0)
    trimmed = 0
    l = r - 1
    while l >= 0
      x = nums[l]
      prev = freq[x]
      if prev == 1
        trimmed += 2
      elsif prev >= 2
        trimmed += 1
      end
      freq[x] = prev + 1

      cost = dp[l] + k + trimmed
      dp[r] = cost if cost < dp[r]

      l -= 1
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def minCost(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val INF = Long.MaxValue / 4
        val dp = Array.fill[Long](n + 1)(INF)
        dp(0) = 0L

        for (r <- 1 to n) {
            val freq = new Array[Int](n) // nums[i] < n
            var curTrim = 0
            var l = r - 1
            while (l >= 0) {
                val x = nums(l)
                if (freq(x) == 0) {
                    freq(x) = 1
                } else if (freq(x) == 1) {
                    freq(x) = 2
                    curTrim += 2
                } else {
                    freq(x) += 1
                    curTrim += 1
                }
                val cost = dp(l) + k.toLong + curTrim
                if (cost < dp(r)) dp(r) = cost
                l -= 1
            }
        }

        dp(n).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut dp = vec![i64::MAX / 4; n + 1];
        dp[0] = 0;
        for r in 1..=n {
            let mut freq = vec![0usize; n];
            let mut trimmed: i64 = 0;
            for l in (0..r).rev() {
                let x = nums[l] as usize;
                match freq[x] {
                    0 => freq[x] = 1,
                    1 => {
                        freq[x] = 2;
                        trimmed += 2;
                    }
                    _ => {
                        freq[x] += 1;
                        trimmed += 1;
                    }
                }
                let cost = dp[l] + k as i64 + trimmed;
                if cost < dp[r] {
                    dp[r] = cost;
                }
            }
        }
        dp[n] as i32
    }
}
```

## Racket

```racket
(define/contract (min-cost nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (dp (make-vector (add1 n) 0)))
    (for ([r (in-range 1 (add1 n))])
      (define freq (make-hash))
      (define curTrimmed 0)
      (define best +inf.0)
      (for ([l (in-range r 0 -1)]) ; l = r, r-1, ..., 1
        (let* ((x (vector-ref vec (- l 1)))
               (cnt (hash-ref freq x 0))
               (newcnt (+ cnt 1)))
          (hash-set! freq x newcnt)
          (cond [(= cnt 0) (void)]
                [(= cnt 1) (set! curTrimmed (+ curTrimmed 2))]
                [else (set! curTrimmed (+ curTrimmed 1))])
          (define cost (+ (vector-ref dp (- l 1)) k curTrimmed))
          (when (< cost best)
            (set! best cost))))
      (vector-set! dp r best))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/2]).

-spec min_cost(Nums :: [integer()], K :: integer()) -> integer().
min_cost(Nums, K) ->
    N = length(Nums),
    Arr = list_to_tuple(Nums),
    InitDP = erlang:make_tuple(N + 1, 0),
    FinalDP = compute_dp(1, N, Arr, K, InitDP),
    element(N + 1, FinalDP).

compute_dp(R, N, _Arr, _K, DPTuple) when R > N ->
    DPTuple;
compute_dp(R, N, Arr, K, DPTuple) ->
    Best = best_for_r(R, Arr, K, DPTuple),
    NewDP = erlang:setelement(R + 1, DPTuple, Best),
    compute_dp(R + 1, N, Arr, K, NewDP).

best_for_r(R, Arr, K, DPTuple) ->
    Big = 1 bsl 60,
    loop_l(R, Arr, #{}, 0, Big, K, DPTuple).

loop_l(0, _Arr, _FreqMap, _Extra, Best, _K, _DPTuple) ->
    Best;
loop_l(L, Arr, FreqMap, Extra, Best, K, DPTuple) ->
    X = element(L, Arr),
    PrevFreq = maps:get(X, FreqMap, 0),
    Delta = case PrevFreq of
                0 -> 0;
                1 -> 2;
                _ -> 1
            end,
    NewExtra = Extra + Delta,
    NewFreqMap = maps:put(X, PrevFreq + 1, FreqMap),
    PrevDP = element(L, DPTuple), % dp[l-1]
    Cost = PrevDP + K + NewExtra,
    NewBest = if Cost < Best -> Cost; true -> Best end,
    loop_l(L - 1, Arr, NewFreqMap, NewExtra, NewBest, K, DPTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(nums :: [integer], k :: integer) :: integer
  def min_cost(nums, k) do
    n = length(nums)
    arr = List.to_tuple(nums)

    dp =
      Enum.reduce(1..n, :erlang.make_tuple(n + 1, 0), fn r, dp_acc ->
        best = compute_best(arr, dp_acc, r, k)
        put_elem(dp_acc, r, best)
      end)

    elem(dp, n)
  end

  defp compute_best(arr, dp, r, k) do
    compute_loop(r - 1, %{}, 0, :erlang.bsl(1, 60), arr, dp, k)
  end

  defp compute_loop(l, _freq, _trim, best, _arr, _dp, _k) when l < 0 do
    best
  end

  defp compute_loop(l, freq, trim_len, best, arr, dp, k) do
    v = elem(arr, l)
    cnt = Map.get(freq, v, 0) + 1
    new_freq = Map.put(freq, v, cnt)

    new_trim =
      cond do
        cnt == 2 -> trim_len + 2
        cnt > 2 -> trim_len + 1
        true -> trim_len
      end

    cost = elem(dp, l) + k + new_trim
    new_best = if cost < best, do: cost, else: best

    compute_loop(l - 1, new_freq, new_trim, new_best, arr, dp, k)
  end
end
```
