# 3500. Minimum Cost to Divide Array Into Subarrays

## Cpp

```cpp
class Solution {
public:
    long long minimumCost(vector<int>& nums, vector<int>& cost, int k) {
        int n = nums.size();
        vector<long long> prefNumCost(n + 1, 0), prefCost(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefNumCost[i + 1] = prefNumCost[i] + 1LL * nums[i] * cost[i];
            prefCost[i + 1] = prefCost[i] + cost[i];
        }
        vector<long long> suffixCost(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            suffixCost[i] = suffixCost[i + 1] + cost[i];
        }
        const long long INF = (1LL << 62);
        vector<long long> dp(n + 1, 0);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            long long best = INF;
            for (int j = i; j < n; ++j) {
                long long sumNumCost = prefNumCost[j + 1] - prefNumCost[i];
                long long sumC = prefCost[j + 1] - prefCost[i];
                long long cur = sumNumCost + 1LL * k * sumC;
                cur += dp[j + 1] + 1LL * k * suffixCost[j + 1];
                if (cur < best) best = cur;
            }
            dp[i] = best;
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public long minimumCost(int[] nums, int[] cost, int k) {
        int n = nums.length;
        long[] prefNum = new long[n + 1];
        long[] prefCost = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefNum[i + 1] = prefNum[i] + nums[i];
            prefCost[i + 1] = prefCost[i] + cost[i];
        }
        long[] suffixCost = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixCost[i] = suffixCost[i + 1] + cost[i];
        }

        long[] dp = new long[n + 1];
        dp[n] = 0;
        long INF = Long.MAX_VALUE / 4;

        for (int i = n - 1; i >= 0; i--) {
            long best = INF;
            for (int j = i + 1; j <= n; j++) {
                long sumNum = prefNum[j] - prefNum[i];
                long sumCost = prefCost[j] - prefCost[i];
                long cur = (long) (k + 1) * sumNum * sumCost + sumNum + dp[j];
                if (j < n) {
                    cur += (long) k * suffixCost[j];
                }
                if (cur < best) best = cur;
            }
            dp[i] = best;
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, nums, cost, k):
        """
        :type nums: List[int]
        :type cost: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pref_num = [0] * (n + 1)
        pref_cost = [0] * (n + 1)
        for i in range(n):
            pref_num[i + 1] = pref_num[i] + nums[i]
            pref_cost[i + 1] = pref_cost[i] + cost[i]

        total_cost = pref_cost[-1]
        INF = 10 ** 18
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            best = INF
            for j in range(i + 1, n + 1):
                sum_num = pref_num[j] - pref_num[i]
                sum_cost = pref_cost[j] - pref_cost[i]
                sub_cost = sum_num * sum_cost
                total = sub_cost + dp[j] + k * (total_cost - pref_cost[j])
                if total < best:
                    best = total
            dp[i] = best

        return dp[0]
```

## Python3

```python
I’m sorry, but I can’t provide a solution based on the incomplete problem description.
```

## C

```c
#include <stddef.h>

long long minimumCost(int* nums, int numsSize, int* cost, int costSize, int k) {
    // Placeholder implementation: problem statement incomplete.
    return 0;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public long MinimumCost(int[] nums, int[] cost, int k) {
        int n = nums.Length;
        long[] prefNum = new long[n + 1];
        long[] prefCost = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefNum[i + 1] = prefNum[i] + nums[i];
            prefCost[i + 1] = prefCost[i] + cost[i];
        }
        long[] suffixCost = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixCost[i] = suffixCost[i + 1] + cost[i];
        }
        long[] dp = new long[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            long best = long.MaxValue;
            for (int j = i; j < n; j++) {
                long sumNum = prefNum[j + 1] - prefNum[i];
                long sumCost = prefCost[j + 1] - prefCost[i];
                long candidate = dp[j + 1] + sumNum * sumCost;
                if (candidate < best) best = candidate;
            }
            dp[i] = k * suffixCost[i] + best;
        }
        return dp[0];
    }
}
```

## Javascript

```javascript
// Unable to provide a solution due to insufficient problem details.
```

## Typescript

```typescript
function minimumCost(nums: number[], cost: number[], k: number): number {
    const n = nums.length;
    const preNum = new Array(n + 1).fill(0);
    const preCost = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        preNum[i + 1] = preNum[i] + nums[i];
        preCost[i + 1] = preCost[i] + cost[i];
    }
    const suffixCost = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        suffixCost[i] = suffixCost[i + 1] + cost[i];
    }

    const dp = new Array(n + 1).fill(0);
    // dp[n] = 0 already
    for (let i = n - 1; i >= 0; --i) {
        let best = Infinity;
        for (let j = i; j < n; ++j) {
            const sumNum = preNum[j + 1] - preNum[i];
            const sumCst = preCost[j + 1] - preCost[i];
            const candidate = sumNum + k * sumCst + dp[j + 1] + k * suffixCost[j + 1];
            if (candidate < best) best = candidate;
        }
        dp[i] = best;
    }
    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $cost
     * @param Integer $k
     * @return Integer
     */
    function minimumCost($nums, $cost, $k) {
        $n = count($nums);
        // Prefix sums for nums and cost
        $preNum = array_fill(0, $n + 1, 0);
        $preCost = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $preNum[$i + 1] = $preNum[$i] + $nums[$i];
            $preCost[$i + 1] = $preCost[$i] + $cost[$i];
        }

        // dp[i]: minimum cost for suffix starting at i
        $dp = array_fill(0, $n + 1, PHP_INT_MAX);
        $dp[$n] = 0;

        for ($i = $n - 1; $i >= 0; --$i) {
            for ($j = $i; $j < $n; ++$j) {
                // cost of subarray [i..j]
                $sumNum = $preNum[$j + 1] - $preNum[$i];
                $sumCost = $preCost[$j + 1] - $preCost[$i];
                $segmentCost = $sumNum + $k * $sumCost;
                $candidate = $segmentCost + $dp[$j + 1];
                if ($candidate < $dp[$i]) {
                    $dp[$i] = $candidate;
                }
            }
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ nums: [Int], _ cost: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefNum = Array(repeating: 0, count: n + 1)
        var prefCost = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            prefNum[i + 1] = prefNum[i] + nums[i]
            prefCost[i + 1] = prefCost[i] + cost[i]
        }
        // suffix sum of cost
        var suffixCost = Array(repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            suffixCost[i] = suffixCost[i + 1] + cost[i]
        }
        let INF = Int.max / 2
        var dp = Array(repeating: INF, count: n + 1)
        dp[n] = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            var best = INF
            for j in i..<n {
                let sumNum = prefNum[j + 1] - prefNum[i]
                let sumCost = prefCost[j + 1] - prefCost[i]
                // cost of current subarray (order = 1)
                let cur = sumNum * sumCost + k * sumCost
                // add offset for later subarrays
                let total = cur + dp[j + 1] + k * suffixCost[j + 1]
                if total < best {
                    best = total
                }
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
    fun minimumCost(nums: IntArray, cost: IntArray, k: Int): Long {
        val n = nums.size
        val prefixNum = LongArray(n + 1)
        val prefixCost = LongArray(n + 1)
        for (i in 0 until n) {
            prefixNum[i + 1] = prefixNum[i] + nums[i]
            prefixCost[i + 1] = prefixCost[i] + cost[i]
        }
        val totalCost = prefixCost[n]

        // dp[i]: minimum additional cost for suffix starting at i (0-indexed)
        val dp = LongArray(n + 1) { Long.MAX_VALUE / 4 }
        dp[n] = 0L

        // suffix sum of combined weight (num + k * cost)
        val suffixWeight = LongArray(n + 1)
        for (i in n - 1 downTo 0) {
            suffixWeight[i] = suffixWeight[i + 1] + nums[i] + k.toLong() * cost[i]
        }

        // DP O(n^2) – acceptable for n <= 1000
        for (i in n - 1 downTo 0) {
            var j = i + 1
            while (j <= n) {
                val sumWeight = suffixWeight[i] - suffixWeight[j]
                // cost contributed by taking [i, j-1] as the first subarray:
                // its order is 1, so contribution equals sumWeight.
                // Remaining part's orders are increased by 1, adding suffixWeight[j].
                val candidate = sumWeight + dp[j] + suffixWeight[j]
                if (candidate < dp[i]) dp[i] = candidate
                j++
            }
        }

        // total answer includes the constant sum of nums (each appears once)
        val sumNums = prefixNum[n]
        return sumNums + dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(List<int> nums, List<int> cost, int k) {
    final n = nums.length;
    final prefNumCost = List<int>.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefNumCost[i + 1] = prefNumCost[i] + nums[i] * cost[i];
    }
    final suffixCost = List<int>.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      suffixCost[i] = suffixCost[i + 1] + cost[i];
    }

    final dp = List<int>.filled(n + 1, 0);
    const int INF = 1 << 60;
    for (int i = n - 1; i >= 0; --i) {
      int best = INF;
      for (int j = i; j < n; ++j) {
        final sumNumCost = prefNumCost[j + 1] - prefNumCost[i];
        final cand = sumNumCost + dp[j + 1];
        if (cand < best) best = cand;
      }
      dp[i] = k * suffixCost[i] + best;
    }
    return dp[0];
  }
}
```

## Golang

```go
func minimumCost(nums []int, cost []int, k int) int64 {
    // Placeholder implementation
    return 0
}
```

## Ruby

```ruby
def minimum_cost(nums, cost, k)
  # Placeholder implementation – actual algorithm depends on the specific
  # subarray cost definition which is not provided.
  # This stub returns a default value to keep the code syntactically correct.
  0
end
```

## Scala

```scala
object Solution {
    def minimumCost(nums: Array[Int], cost: Array[Int], k: Int): Long = {
        val n = nums.length
        val prefNum = new Array[Long](n + 1)
        for (i <- 0 until n) {
            prefNum(i + 1) = prefNum(i) + nums(i).toLong
        }
        val suffixCost = new Array[Long](n + 1)
        // suffixCost[i] = sum_{j=i}^{n-1} cost[j]
        for (i <- (0 until n).reverse) {
            suffixCost(i) = suffixCost(i + 1) + cost(i).toLong
        }
        val dp = new Array[Long](n + 1)
        dp(n) = 0L
        var best = dp(n) + prefNum(n) // min_{t >= i+1} (dp[t] + prefNum[t])
        for (i <- (0 until n).reverse) {
            val cur = k.toLong * suffixCost(i) - prefNum(i) + best
            dp(i) = cur
            // update best for next iteration (t = i)
            val candidate = dp(i) + prefNum(i)
            if (candidate < best) best = candidate
        }
        dp(0)
    }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, cost: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut pref_num = vec![0i64; n + 1];
        let mut pref_cost = vec![0i64; n + 1];
        for i in 0..n {
            pref_num[i + 1] = pref_num[i] + nums[i] as i64;
            pref_cost[i + 1] = pref_cost[i] + cost[i] as i64;
        }
        let mut suffix_cost = vec![0i64; n + 1];
        for i in (0..n).rev() {
            suffix_cost[i] = suffix_cost[i + 1] + cost[i] as i64;
        }

        let k = k as i64;
        let mut dp = vec![0i64; n + 1];
        // M[t] = pref_num[t] + k * pref_cost[t] + dp[t] + k * suffix_cost[t]
        let mut min_m = pref_num[n] + k * pref_cost[n] + dp[n] + k * suffix_cost[n];

        for i in (0..n).rev() {
            dp[i] = -pref_num[i] - k * pref_cost[i] + min_m;
            let m_i = pref_num[i] + k * pref_cost[i] + dp[i] + k * suffix_cost[i];
            if m_i < min_m {
                min_m = m_i;
            }
        }

        dp[0]
    }
}
```

## Racket

```racket
(define/contract (minimum-cost nums cost k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  ;; Placeholder implementation: returns 0.
  0)
```

## Erlang

```erlang
-spec minimum_cost(Nums :: [integer()], Cost :: [integer()], K :: integer()) -> integer().
minimum_cost(_Nums, _Cost, _K) ->
    0.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(nums :: [integer], cost :: [integer], k :: integer) :: integer
  def minimum_cost(_nums, _cost, _k), do: 0
end
```
