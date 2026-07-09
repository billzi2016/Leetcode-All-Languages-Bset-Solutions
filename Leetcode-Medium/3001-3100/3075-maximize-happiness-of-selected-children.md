# 3075. Maximize Happiness of Selected Children

## Cpp

```cpp
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), greater<int>());
        long long ans = 0;
        for (int i = 0; i < k; ++i) {
            long long val = static_cast<long long>(happiness[i]) - i;
            if (val > 0) ans += val;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        java.util.Arrays.sort(happiness);
        long total = 0L;
        int n = happiness.length;
        for (int i = 0; i < k; i++) {
            int val = happiness[n - 1 - i];
            int adjusted = val - i;
            if (adjusted > 0) {
                total += adjusted;
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            val = happiness[i] - i
            if val > 0:
                total += val
            else:
                break
        return total
```

## Python3

```python
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            val = happiness[i] - i
            if val > 0:
                total += val
            else:
                break
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return vb - va;  // descending order
}

long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    qsort(happiness, (size_t)happinessSize, sizeof(int), cmp_desc);
    long long total = 0;
    for (int i = 0; i < k; ++i) {
        long long cur = (long long)happiness[i] - i;
        if (cur > 0)
            total += cur;
        else
            break;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaximumHappinessSum(int[] happiness, int k)
    {
        Array.Sort(happiness);
        long total = 0;
        int n = happiness.Length;
        for (int i = 0; i < k; i++)
        {
            long val = (long)happiness[n - 1 - i] - i;
            if (val > 0)
                total += val;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    // Sort in descending order to pick the largest values first
    happiness.sort((a, b) => b - a);
    
    let total = 0;
    const limit = Math.min(k, happiness.length);
    for (let i = 0; i < limit; ++i) {
        const val = happiness[i] - i; // decrease by the number of previous picks
        if (val > 0) total += val;
        // else adding zero has no effect, can break early since further values will be <= current
    }
    return total;
};
```

## Typescript

```typescript
function maximumHappinessSum(happiness: number[], k: number): number {
    happiness.sort((a, b) => b - a);
    let total = 0;
    for (let i = 0; i < k && i < happiness.length; i++) {
        const val = happiness[i] - i;
        if (val > 0) total += val;
        else break;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $happiness
     * @param Integer $k
     * @return Integer
     */
    function maximumHappinessSum($happiness, $k) {
        rsort($happiness);
        $sum = 0;
        $len = count($happiness);
        for ($i = 0; $i < $k && $i < $len; $i++) {
            $val = $happiness[$i] - $i;
            if ($val > 0) {
                $sum += $val;
            } else {
                // further values will not contribute positively
                break;
            }
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func maximumHappinessSum(_ happiness: [Int], _ k: Int) -> Int {
        let sorted = happiness.sorted(by: >)
        var total = 0
        for i in 0..<k {
            let value = sorted[i] - i
            if value > 0 {
                total += value
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumHappinessSum(happiness: IntArray, k: Int): Long {
        happiness.sort()
        var sum = 0L
        var taken = 0
        for (i in happiness.size - 1 downTo happiness.size - k) {
            val cur = happiness[i] - taken
            if (cur > 0) sum += cur.toLong()
            taken++
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int maximumHappinessSum(List<int> happiness, int k) {
    happiness.sort((a, b) => b.compareTo(a));
    int total = 0;
    for (int i = 0; i < k && i < happiness.length; i++) {
      int val = happiness[i] - i;
      if (val > 0) {
        total += val;
      }
    }
    return total;
  }
}
```

## Golang

```go
package main

import "sort"

func maximumHappinessSum(happiness []int, k int) int64 {
	sort.Slice(happiness, func(i, j int) bool { return happiness[i] > happiness[j] })
	var total int64
	for i := 0; i < k && i < len(happiness); i++ {
		val := happiness[i] - i
		if val > 0 {
			total += int64(val)
		}
	}
	return total
}
```

## Ruby

```ruby
# @param {Integer[]} happiness
# @param {Integer} k
# @return {Integer}
def maximum_happiness_sum(happiness, k)
  happiness.sort!.reverse!
  total = 0
  i = 0
  while i < k && i < happiness.length
    val = happiness[i] - i
    total += val if val > 0
    i += 1
  end
  total
end
```

## Scala

```scala
object Solution {
    def maximumHappinessSum(happiness: Array[Int], k: Int): Long = {
        val sorted = happiness.sorted(Ordering[Int].reverse)
        var total: Long = 0L
        var i = 0
        while (i < k && i < sorted.length) {
            val v = sorted(i) - i
            if (v > 0) total += v
            else return total
            i += 1
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_happiness_sum(happiness: Vec<i32>, k: i32) -> i64 {
        let mut arr = happiness;
        arr.sort_unstable_by(|a, b| b.cmp(a)); // descending order
        let limit = std::cmp::min(k as usize, arr.len());
        let mut total: i64 = 0;
        for i in 0..limit {
            let val = arr[i] as i64 - i as i64;
            if val > 0 {
                total += val;
            } else {
                break;
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (maximum-happiness-sum happiness k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted (sort happiness >)])
    (let loop ((i 0) (sum 0) (lst sorted))
      (if (or (= i k) (null? lst))
          sum
          (let* ([val (car lst)]
                 [adjusted (- val i)]
                 [add (if (> adjusted 0) adjusted 0)])
            (loop (+ i 1) (+ sum add) (cdr lst)))))))
```

## Erlang

```erlang
-spec maximum_happiness_sum(Happiness :: [integer()], K :: integer()) -> integer().
maximum_happiness_sum(Happiness, K) ->
    Sorted = lists:sort(fun(A, B) -> A > B end, Happiness),
    TakeK = lists:sublist(Sorted, K),
    {Sum, _} = lists:foldl(
        fun(Val, {Acc, I}) ->
            Adjusted = Val - I,
            NewAcc = if Adjusted > 0 -> Acc + Adjusted; true -> Acc end,
            {NewAcc, I + 1}
        end,
        {0, 0},
        TakeK),
    Sum.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_happiness_sum(happiness :: [integer], k :: integer) :: integer
  def maximum_happiness_sum(happiness, k) do
    happiness
    |> Enum.sort(&>=/2)
    |> Enum.take(k)
    |> Enum.with_index()
    |> Enum.reduce(0, fn {val, idx}, acc ->
      adjusted = val - idx
      if adjusted > 0, do: acc + adjusted, else: acc
    end)
  end
end
```
