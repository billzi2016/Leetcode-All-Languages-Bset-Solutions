# 3301. Maximize the Total Height of Unique Towers

## Cpp

```cpp
class Solution {
public:
    long long maximumTotalSum(vector<int>& maximumHeight) {
        sort(maximumHeight.begin(), maximumHeight.end(), greater<int>());
        long long total = 0;
        long long prev = LLONG_MAX;
        for (int h : maximumHeight) {
            long long cur = min<long long>(h, prev - 1);
            if (cur <= 0) return -1;
            total += cur;
            prev = cur;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public long maximumTotalSum(int[] maximumHeight) {
        int n = maximumHeight.length;
        java.util.Arrays.sort(maximumHeight);
        long sum = 0;
        long prev = Long.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            long cur = Math.min(maximumHeight[i], prev - 1);
            if (cur <= 0) {
                return -1;
            }
            sum += cur;
            prev = cur;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        maximumHeight.sort(reverse=True)
        total = 0
        prev = float('inf')
        for h in maximumHeight:
            cur = min(h, prev - 1)
            if cur <= 0:
                return -1
            total += cur
            prev = cur
        return total
```

## Python3

```python
class Solution:
    def maximumTotalSum(self, maximumHeight):
        maximumHeight.sort(reverse=True)
        prev = 10**18
        total = 0
        for h in maximumHeight:
            cur = min(h, prev - 1)
            if cur <= 0:
                return -1
            total += cur
            prev = cur
        return total
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmpDesc(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    if (av < bv) return 1;   // b should come before a
    if (av > bv) return -1;  // a should come before b
    return 0;
}

long long maximumTotalSum(int* maximumHeight, int maximumHeightSize) {
    if (maximumHeightSize == 0) return -1LL;
    qsort(maximumHeight, maximumHeightSize, sizeof(int), cmpDesc);
    
    long long total = 0;
    int prev = INT_MAX; // effectively no limit for the first tower
    
    for (int i = 0; i < maximumHeightSize; ++i) {
        int allowed = maximumHeight[i];
        if (prev != INT_MAX && allowed > prev - 1)
            allowed = prev - 1;
        if (allowed <= 0)
            return -1LL;
        total += allowed;
        prev = allowed;
    }
    
    return total;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaximumTotalSum(int[] maximumHeight) {
        Array.Sort(maximumHeight);
        long total = 0;
        long prev = long.MaxValue;
        for (int i = maximumHeight.Length - 1; i >= 0; i--) {
            long cur = Math.Min(maximumHeight[i], prev - 1);
            if (cur <= 0) return -1;
            total += cur;
            prev = cur;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} maximumHeight
 * @return {number}
 */
var maximumTotalSum = function(maximumHeight) {
    // Sort in descending order
    maximumHeight.sort((a, b) => b - a);
    
    let total = 0;
    // Height assigned to previous (larger) tower
    let prev = Infinity; // start with very large value
    
    for (let i = 0; i < maximumHeight.length; ++i) {
        const allowed = Math.min(maximumHeight[i], prev - 1);
        if (allowed <= 0) return -1;
        total += allowed;
        prev = allowed;
    }
    
    return total;
};
```

## Typescript

```typescript
function maximumTotalSum(maximumHeight: number[]): number {
    // Sort heights in descending order
    maximumHeight.sort((a, b) => b - a);
    
    let prev = Infinity;
    let total = 0;
    
    for (const h of maximumHeight) {
        const cur = Math.min(h, prev - 1);
        if (cur <= 0) return -1;
        total += cur;
        prev = cur;
    }
    
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $maximumHeight
     * @return Integer
     */
    function maximumTotalSum($maximumHeight) {
        rsort($maximumHeight);
        $prev = PHP_INT_MAX;
        $total = 0;
        foreach ($maximumHeight as $h) {
            $cur = min($h, $prev - 1);
            if ($cur <= 0) {
                return -1;
            }
            $total += $cur;
            $prev = $cur;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maximumTotalSum(_ maximumHeight: [Int]) -> Int {
        let sortedHeights = maximumHeight.sorted(by: >)
        var prev = Int.max
        var total: Int64 = 0
        for height in sortedHeights {
            let allowed = min(height, prev - 1)
            if allowed <= 0 {
                return -1
            }
            total += Int64(allowed)
            prev = allowed
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTotalSum(maximumHeight: IntArray): Long {
        val sorted = maximumHeight.sortedDescending()
        var prev = Long.MAX_VALUE
        var total = 0L
        for (h in sorted) {
            val cur = minOf(h.toLong(), prev - 1)
            if (cur <= 0) return -1
            total += cur
            prev = cur
        }
        return total
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maximumTotalSum(List<int> maximumHeight) {
    maximumHeight.sort((a, b) => b.compareTo(a));
    const int INF = 1 << 60;
    int prev = INF;
    int total = 0;
    for (int h in maximumHeight) {
      int cur = min(h, prev - 1);
      if (cur <= 0) return -1;
      total += cur;
      prev = cur;
    }
    return total;
  }
}
```

## Golang

```go
import "sort"

func maximumTotalSum(maximumHeight []int) int64 {
	sort.Slice(maximumHeight, func(i, j int) bool { return maximumHeight[i] > maximumHeight[j] })
	var total int64
	prev := int64(1 << 60)
	for _, h := range maximumHeight {
		cur := int64(h)
		if prev-1 < cur {
			cur = prev - 1
		}
		if cur <= 0 {
			return -1
		}
		total += cur
		prev = cur
	}
	return total
}
```

## Ruby

```ruby
def maximum_total_sum(maximum_height)
  heights = maximum_height.sort.reverse
  prev = (1 << 62) # sufficiently large sentinel
  total = 0

  heights.each do |h|
    cur = [h, prev - 1].min
    return -1 if cur <= 0
    total += cur
    prev = cur
  end

  total
end
```

## Scala

```scala
object Solution {
    def maximumTotalSum(maximumHeight: Array[Int]): Long = {
        val sorted = maximumHeight.sorted(Ordering.Int.reverse)
        var prev: Long = Long.MaxValue
        var total: Long = 0L
        for (hInt <- sorted) {
            val h = hInt.toLong
            val allowed = math.min(h, prev - 1)
            if (allowed <= 0) return -1L
            total += allowed
            prev = allowed
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_total_sum(maximum_height: Vec<i32>) -> i64 {
        let mut heights = maximum_height;
        heights.sort_unstable_by(|a, b| b.cmp(a)); // descending
        let mut total: i64 = 0;
        let mut prev: i64 = i64::MAX;

        for h in heights {
            let cur = if prev == i64::MAX {
                h as i64
            } else {
                std::cmp::min(prev - 1, h as i64)
            };
            if cur <= 0 {
                return -1;
            }
            total += cur;
            prev = cur;
        }

        total
    }
}
```

## Racket

```racket
(define/contract (maximum-total-sum maximumHeight)
  (-> (listof exact-integer?) exact-integer?)
  (let ([sorted (sort maximumHeight >)])
    (if (null? sorted)
        0
        (let loop ((remaining (cdr sorted))
                   (prev (car sorted))
                   (total (car sorted)))
          (cond
            [(null? remaining) total]
            [else
             (let* ([cur (car remaining)]
                    [h (min cur (- prev 1))])
               (if (<= h 0)
                   -1
                   (loop (cdr remaining) h (+ total h))))])))))
```

## Erlang

```erlang
-spec maximum_total_sum(MaximumHeight :: [integer()]) -> integer().
maximum_total_sum(MaximumHeight) ->
    Sorted = lists:sort(fun(A, B) -> A > B end, MaximumHeight),
    case Sorted of
        [] -> 0;
        [First | Rest] ->
            case assign(Rest, First, First) of
                {ok, Sum} -> Sum;
                error -> -1
            end
    end.

assign([], _Prev, Sum) -> {ok, Sum};
assign([H | T], Prev, Sum) ->
    Cur = erlang:min(H, Prev - 1),
    if
        Cur =< 0 -> error;
        true -> assign(T, Cur, Sum + Cur)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_total_sum(maximum_height :: [integer]) :: integer
  def maximum_total_sum(maximum_height) do
    sorted = Enum.sort(maximum_height, fn a, b -> a > b end)

    case Enum.reduce_while(sorted, {nil, 0}, fn h, {prev, acc} ->
           cur = if is_nil(prev), do: h, else: min(h, prev - 1)

           if cur <= 0 do
             {:halt, :impossible}
           else
             {:cont, {cur, acc + cur}}
           end
         end) do
      :impossible -> -1
      {_last, total} -> total
    end
  end
end
```
