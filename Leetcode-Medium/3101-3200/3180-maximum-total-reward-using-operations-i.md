# 3180. Maximum Total Reward Using Operations I

## Cpp

```cpp
class Solution {
public:
    int maxTotalReward(vector<int>& rewardValues) {
        sort(rewardValues.begin(), rewardValues.end());
        int n = rewardValues.size();
        int total = 0;
        for (int v : rewardValues) total += v;
        vector<char> dp(total + 1, 0);
        dp[0] = 1;
        for (int v : rewardValues) {
            int upper = min(total, 2 * v - 1);
            for (int j = upper; j >= v; --j) {
                if (!dp[j] && dp[j - v]) {
                    dp[j] = 1;
                }
            }
        }
        for (int j = total; j >= 0; --j) {
            if (dp[j]) return j;
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int maxTotalReward(int[] rewardValues) {
        java.util.Arrays.sort(rewardValues);
        int total = 0;
        for (int v : rewardValues) total += v;
        boolean[] dp = new boolean[total + 1];
        dp[0] = true;
        for (int v : rewardValues) {
            for (int s = v - 1; s >= 0; --s) {
                if (dp[s]) dp[s + v] = true;
            }
        }
        for (int i = total; i >= 0; --i) {
            if (dp[i]) return i;
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        rewardValues.sort()
        bits = 1  # bit i set => sum i achievable
        for v in rewardValues:
            mask = (1 << v) - 1          # sums strictly less than v
            eligible = bits & mask       # only those can be extended by v
            bits |= eligible << v        # add new reachable sums
        return bits.bit_length() - 1
```

## Python3

```python
from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp = 1  # bitmask with sum 0 achievable
        for v in rewardValues:
            candidates = dp & ((1 << v) - 1)   # sums strictly less than v
            dp |= candidates << v
        return dp.bit_length() - 1
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int maxTotalReward(int* rewardValues, int rewardValuesSize) {
    qsort(rewardValues, rewardValuesSize, sizeof(int), cmp_int);
    
    long total = 0;
    for (int i = 0; i < rewardValuesSize; ++i) total += rewardValues[i];
    int maxSum = (int)total;
    
    char *dp = (char *)calloc(maxSum + 1, sizeof(char));
    dp[0] = 1;
    int ans = 0;
    
    for (int i = 0; i < rewardValuesSize; ++i) {
        int v = rewardValues[i];
        for (int s = v - 1; s >= 0; --s) {
            if (dp[s]) {
                int ns = s + v;
                if (!dp[ns]) {
                    dp[ns] = 1;
                    if (ns > ans) ans = ns;
                }
            }
        }
    }
    
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxTotalReward(int[] rewardValues) {
        System.Array.Sort(rewardValues);
        int maxVal = rewardValues[rewardValues.Length - 1];
        int limit = 2 * maxVal; // maximum possible total reward is less than 2*maxVal
        bool[] dp = new bool[limit];
        dp[0] = true;
        foreach (int v in rewardValues) {
            for (int s = v - 1; s >= 0; --s) {
                if (dp[s]) {
                    dp[s + v] = true;
                }
            }
        }
        for (int i = limit - 1; i >= 0; --i) {
            if (dp[i]) return i;
        }
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rewardValues
 * @return {number}
 */
var maxTotalReward = function(rewardValues) {
    rewardValues.sort((a, b) => a - b);
    const totalSum = rewardValues.reduce((acc, v) => acc + v, 0);
    // dp[s] == 1 means sum s is reachable
    const dp = new Uint8Array(totalSum + 1);
    dp[0] = 1;
    let maxReach = 0;

    for (const v of rewardValues) {
        // iterate descending to avoid using the same value multiple times
        for (let s = maxReach; s >= 0; --s) {
            if (dp[s] && s < v) {
                const ns = s + v;
                dp[ns] = 1;
                if (ns > maxReach) maxReach = ns;
            }
        }
    }

    for (let i = totalSum; i >= 0; --i) {
        if (dp[i]) return i;
    }
    return 0;
};
```

## Typescript

```typescript
function maxTotalReward(rewardValues: number[]): number {
    if (rewardValues.length === 0) return 0;
    rewardValues.sort((a, b) => a - b);
    const maxV = rewardValues[rewardValues.length - 1];
    const limit = maxV * 2; // maximum possible total reward
    let dp = new Uint8Array(limit + 1);
    dp[0] = 1;

    for (const v of rewardValues) {
        const next = dp.slice(); // copy current reachable sums
        // we can only use previous sum s that is less than v
        const maxS = Math.min(v - 1, limit - v);
        for (let s = 0; s <= maxS; ++s) {
            if (dp[s]) {
                next[s + v] = 1;
            }
        }
        dp = next;
    }

    for (let i = limit; i >= 0; --i) {
        if (dp[i]) return i;
    }
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rewardValues
     * @return Integer
     */
    function maxTotalReward($rewardValues) {
        sort($rewardValues);
        $totalSum = array_sum($rewardValues);
        // Initialize DP array
        $dp = array_fill(0, $totalSum + 1, false);
        $dp[0] = true;

        foreach ($rewardValues as $v) {
            // Only consider previous totals that are less than current value
            for ($j = $v - 1; $j >= 0; --$j) {
                if ($dp[$j]) {
                    $dp[$j + $v] = true;
                }
            }
        }

        // Find the maximum achievable total reward
        for ($ans = $totalSum; $ans >= 0; --$ans) {
            if ($dp[$ans]) {
                return $ans;
            }
        }
        return 0; // fallback, should never reach here
    }
}
```

## Swift

```swift
class Solution {
    func maxTotalReward(_ rewardValues: [Int]) -> Int {
        let sorted = rewardValues.sorted()
        let total = sorted.reduce(0, +)
        var dp = [Bool](repeating: false, count: total + 1)
        dp[0] = true
        
        for v in sorted {
            // Only consider previous sums that are strictly less than v
            if v > 0 {
                var s = 0
                while s < v {
                    if dp[s] {
                        dp[s + v] = true
                    }
                    s += 1
                }
            }
        }
        
        for i in stride(from: total, through: 0, by: -1) {
            if dp[i] { return i }
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTotalReward(rewardValues: IntArray): Int {
        val sorted = rewardValues.sorted()
        val totalSum = rewardValues.sum()
        val dp = BooleanArray(totalSum + 1)
        dp[0] = true
        for (v in sorted) {
            var s = v - 1
            while (s >= 0) {
                if (dp[s]) {
                    dp[s + v] = true
                }
                s--
            }
        }
        for (i in totalSum downTo 0) {
            if (dp[i]) return i
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int maxTotalReward(List<int> rewardValues) {
    if (rewardValues.isEmpty) return 0;
    rewardValues.sort();
    int maxV = rewardValues.reduce((a, b) => a > b ? a : b);
    int limit = 2 * maxV; // maximum possible total reward
    var dp = Uint8List(limit + 1);
    dp[0] = 1;

    for (int v in rewardValues) {
      for (int s = limit - v; s >= 0; --s) {
        if (dp[s] == 1 && s < v) {
          dp[s + v] = 1;
        }
      }
    }

    int ans = 0;
    for (int i = 0; i <= limit; ++i) {
      if (dp[i] == 1) ans = i;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func maxTotalReward(rewardValues []int) int {
	if len(rewardValues) == 0 {
		return 0
	}
	sort.Ints(rewardValues)

	total := 0
	for _, v := range rewardValues {
		total += v
	}

	dp := make([]bool, total+1)
	dp[0] = true
	maxReach := 0

	for _, v := range rewardValues {
		prevMax := maxReach
		for j := prevMax; j >= 0; j-- {
			if dp[j] && j < v {
				nxt := j + v
				if !dp[nxt] {
					dp[nxt] = true
					if nxt > maxReach {
						maxReach = nxt
					}
				}
			}
		}
	}

	return maxReach
}
```

## Ruby

```ruby
def max_total_reward(reward_values)
  reward_values.sort!
  total_sum = reward_values.sum
  dp = Array.new(total_sum + 1, false)
  dp[0] = true
  cur_max = 0

  reward_values.each do |v|
    limit = [v - 1, cur_max].min
    s = limit
    while s >= 0
      if dp[s]
        dp[s + v] = true
      end
      s -= 1
    end
    cur_max += v
  end

  total_sum.downto(0) do |j|
    return j if dp[j]
  end
end
```

## Scala

```scala
object Solution {
    def maxTotalReward(rewardValues: Array[Int]): Int = {
        val arr = rewardValues.sorted
        val total = arr.sum
        val dp = new Array[Boolean](total + 1)
        dp(0) = true

        for (v <- arr) {
            var upper = 2 * v - 1
            if (upper > total) upper = total
            var j = upper
            while (j >= v) {
                if (!dp(j) && dp(j - v)) {
                    // Since j <= 2*v-1, we have (j - v) < v automatically.
                    dp(j) = true
                }
                j -= 1
            }
        }

        var i = total
        while (i >= 0 && !dp(i)) {
            i -= 1
        }
        if (i >= 0) i else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_total_reward(reward_values: Vec<i32>) -> i32 {
        let mut vals = reward_values;
        vals.sort_unstable();
        let total_sum: usize = vals.iter().map(|&x| x as usize).sum();
        let mut dp = vec![false; total_sum + 1];
        dp[0] = true;
        for &v_i in vals.iter() {
            let v = v_i as usize;
            for s in (0..v).rev() {
                if dp[s] {
                    dp[s + v] = true;
                }
            }
        }
        for i in (0..=total_sum).rev() {
            if dp[i] {
                return i as i32;
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (max-total‑reward rewardValues)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort rewardValues <))
         (total (apply + sorted))
         (reach (make-vector (+ total 1) #f)))
    (vector-set! reach 0 #t)
    (define cur‑max 0)
    (for ([v sorted])
      (define limit (min (- v 1) cur‑max))
      (when (>= limit 0)
        (for ([j (in-range limit -1 -1)])
          (when (vector-ref reach j)
            (let ((nj (+ j v)))
              (unless (vector-ref reach nj)
                (vector-set! reach nj #t)
                (when (> nj cur‑max) (set! cur‑max nj))))))))
    cur‑max))
```

## Erlang

```erlang
-spec max_total_reward(RewardValues :: [integer()]) -> integer().
max_total_reward(RewardValues) ->
    Sorted = lists:sort(RewardValues),
    Bitset0 = 1,
    Bitset = lists:foldl(
        fun(V, Acc) ->
            Mask = (1 bsl V) - 1,
            Extend = ((Acc band Mask) bsl V),
            Acc bor Extend
        end,
        Bitset0,
        Sorted),
    Total = lists:sum(RewardValues),
    find_max(Bitset, Total).

find_max(_Bitset, -1) -> 0;
find_max(Bitset, I) ->
    case (Bitset bsr I) band 1 of
        1 -> I;
        0 -> find_max(Bitset, I - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_total_reward(reward_values :: [integer]) :: integer
  def max_total_reward(reward_values) do
    import Bitwise

    sorted = Enum.sort(reward_values)

    dp =
      Enum.reduce(sorted, 1, fn v, acc ->
        mask = acc &&& ((1 <<< v) - 1)
        acc ||| (mask <<< v)
      end)

    total = Enum.sum(reward_values)

    Enum.find(total..0, fn i -> (dp &&& (1 <<< i)) != 0 end)
  end
end
```
