# 2790. Maximum Number of Groups With Increasing Length

## Cpp

```cpp
class Solution {
public:
    int maxIncreasingGroups(vector<int>& usageLimits) {
        sort(usageLimits.begin(), usageLimits.end());
        int groups = 0;
        for (int x : usageLimits) {
            if (x > groups) ++groups;
        }
        return groups;
    }
};
```

## Java

```java
class Solution {
    public int maxIncreasingGroups(List<Integer> usageLimits) {
        int n = usageLimits.size();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = usageLimits.get(i);
        }
        java.util.Arrays.sort(arr);
        int groups = 0;
        for (int limit : arr) {
            if (limit >= groups + 1) {
                groups++;
            }
        }
        return groups;
    }
}
```

## Python

```python
class Solution(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        :type usageLimits: List[int]
        :rtype: int
        """
        usageLimits.sort()
        groups = 0
        for limit in usageLimits:
            if limit > groups:
                groups += 1
        return groups
```

## Python3

```python
class Solution:
    def maxIncreasingGroups(self, usageLimits):
        total_limit = sum(usageLimits)
        # Upper bound for k from total slots needed: k(k+1)/2 <= total_limit
        hi = int((2 * total_limit) ** 0.5) + 2

        def feasible(k):
            need = k * (k + 1) // 2
            cur = 0
            for u in usageLimits:
                cur += u if u < k else k
                if cur >= need:
                    return True
            return cur >= need

        lo = 0
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int maxIncreasingGroups(int* usageLimits, int usageLimitsSize) {
    qsort(usageLimits, usageLimitsSize, sizeof(int), cmp_int);
    long long need = 1;      // size of the next group to form
    long long sum = 0;       // total available usages processed so far

    for (int i = 0; i < usageLimitsSize; ++i) {
        sum += (long long)usageLimits[i];
        if (sum >= need) {
            ++need;
        }
    }
    return (int)(need - 1);
}
```

## Csharp

```csharp
public class Solution {
    public int MaxIncreasingGroups(IList<int> usageLimits) {
        int[] arr = new int[usageLimits.Count];
        for (int i = 0; i < usageLimits.Count; i++) arr[i] = usageLimits[i];
        Array.Sort(arr);
        int need = 1;
        int groups = 0;
        foreach (int limit in arr) {
            if (limit >= need) {
                groups++;
                need++;
            }
        }
        return groups;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} usageLimits
 * @return {number}
 */
var maxIncreasingGroups = function(usageLimits) {
    const n = usageLimits.length;
    let lo = 0, hi = n; // answer is in [0, n]
    
    const canForm = (x) => {
        if (x === 0) return true;
        const required = x * (x + 1) / 2;
        let total = 0;
        for (let v of usageLimits) {
            total += Math.min(v, x);
            if (total >= required) return true;
        }
        return false;
    };
    
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (canForm(mid)) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    return lo;
};
```

## Typescript

```typescript
function maxIncreasingGroups(usageLimits: number[]): number {
    usageLimits.sort((a, b) => a - b);
    let groups = 0;
    for (const v of usageLimits) {
        if (v > groups) groups++;
    }
    return groups;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $usageLimits
     * @return Integer
     */
    function maxIncreasingGroups($usageLimits) {
        sort($usageLimits);
        $cur = 1;
        foreach ($usageLimits as $limit) {
            if ($limit >= $cur) {
                $cur++;
            }
        }
        return $cur - 1;
    }
}
```

## Swift

```swift
class Solution {
    func maxIncreasingGroups(_ usageLimits: [Int]) -> Int {
        let sorted = usageLimits.sorted()
        var groups = 0
        for limit in sorted {
            if limit > groups {
                groups += 1
            }
        }
        return groups
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxIncreasingGroups(usageLimits: List<Int>): Int {
        val n = usageLimits.size
        var low = 0
        var high = n + 1 // exclusive upper bound

        while (low + 1 < high) {
            val mid = (low + high) ushr 1
            if (canForm(mid, usageLimits)) {
                low = mid
            } else {
                high = mid
            }
        }
        return low
    }

    private fun canForm(k: Int, limits: List<Int>): Boolean {
        val need = k.toLong() * (k + 1L) / 2L
        var sum = 0L
        for (v in limits) {
            sum += if (v < k) v else k
            if (sum >= need) return true
        }
        return sum >= need
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxIncreasingGroups(List<int> usageLimits) {
    int total = 0;
    for (var v in usageLimits) total += v;

    int low = 0;
    int high = ((sqrt(8 * total + 1) - 1) / 2).floor();

    while (low < high) {
      int mid = (low + high + 1) >> 1;
      if (_canForm(mid, usageLimits)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }

  bool _canForm(int x, List<int> limits) {
    int need = x * (x + 1) ~/ 2;
    int sum = 0;
    for (var v in limits) {
      sum += v < x ? v : x;
      if (sum >= need) return true;
    }
    return sum >= need;
  }
}
```

## Golang

```go
package main

import "sort"

func maxIncreasingGroups(usageLimits []int) int {
	sort.Ints(usageLimits)
	n := len(usageLimits)
	low, high := 0, n
	for low < high {
		mid := (low + high + 1) / 2
		if feasible(mid, usageLimits) {
			low = mid
		} else {
			high = mid - 1
		}
	}
	return low
}

func feasible(k int, limits []int) bool {
	var total int64
	need := int64(k) * int64(k+1) / 2
	kk := int64(k)
	for _, v := range limits {
		if v >= k {
			total += kk
		} else {
			total += int64(v)
		}
		if total >= need {
			return true
		}
	}
	return total >= need
}
```

## Ruby

```ruby
def max_increasing_groups(usage_limits)
  usage_limits.sort!
  cur = 0
  usage_limits.each do |limit|
    cur += 1 if limit > cur
  end
  cur
end
```

## Scala

```scala
object Solution {
    def maxIncreasingGroups(usageLimits: List[Int]): Int = {
        val limits = usageLimits.map(_.toLong)
        val totalTokens = limits.sum
        var low = 0L
        var high = ((Math.sqrt(8.0 * totalTokens + 1) - 1) / 2).toLong

        while (low < high) {
            val mid = (low + high + 1) / 2
            var available = 0L
            for (v <- limits) {
                available += math.min(v, mid)
            }
            val need = mid * (mid + 1) / 2
            if (available >= need) low = mid else high = mid - 1
        }
        low.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_increasing_groups(usage_limits: Vec<i32>) -> i32 {
        // total possible usages
        let total: i64 = usage_limits.iter().map(|&x| x as i64).sum();
        // upper bound for k from sum_{i=1}^k i <= total  => k(k+1)/2 <= total
        let mut high: i64 =
            (( (1.0_f64 + 8.0 * total as f64).sqrt() - 1.0) / 2.0).floor() as i64;
        let mut low: i64 = 0;

        while low < high {
            let mid = (low + high + 1) / 2;
            if Self::feasible(mid, &usage_limits) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        low as i32
    }

    fn feasible(k: i64, limits: &[i32]) -> bool {
        let required = k * (k + 1) / 2;
        let mut sum: i64 = 0;
        for &v in limits {
            sum += std::cmp::min(v as i64, k);
            if sum >= required {
                return true;
            }
        }
        sum >= required
    }
}
```

## Racket

```racket
(define/contract (max-increasing-groups usageLimits)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort usageLimits <))
         (n (length sorted)))
    (let loop ((low 0) (high n))
      (if (= low high)
          low
          (let* ((mid (+ low (quotient (+ (- high low) 1) 2))) ; ceil of average
                 (need (/ (* mid (+ mid 1)) 2))
                 (cap (let sum-loop ((lst sorted) (acc 0))
                        (if (null? lst)
                            acc
                            (sum-loop (cdr lst) (+ acc (min (car lst) mid)))))))
            (if (>= cap need)
                (loop mid high)
                (loop low (- mid 1))))))))
```

## Erlang

```erlang
-spec max_increasing_groups(UsageLimits :: [integer()]) -> integer().
max_increasing_groups(UsageLimits) ->
    Sorted = lists:sort(UsageLimits),
    process(Sorted, 1, 0).

process([], Cur, _Sum) ->
    Cur - 1;
process([H|T], Cur, Sum) ->
    Total = Sum + H,
    {NewCur, NewSum} = consume(Total, Cur),
    process(T, NewCur, NewSum).

consume(Sum, Cur) when Sum >= Cur ->
    consume(Sum - Cur, Cur + 1);
consume(Sum, Cur) ->
    {Cur, Sum}.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_increasing_groups(usage_limits :: [integer]) :: integer
  def max_increasing_groups(usage_limits) do
    usage_limits
    |> Enum.sort()
    |> Enum.reduce_while(1, fn limit, cur ->
      if limit >= cur do
        {:cont, cur + 1}
      else
        {:halt, cur}
      end
    end)
    |> Kernel.-(1)
  end
end
```
