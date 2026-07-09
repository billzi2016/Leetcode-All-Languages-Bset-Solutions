# 1953. Maximum Number of Weeks for Which You Can Work

## Cpp

```cpp
class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        long long total = 0;
        long long mx = 0;
        for (int v : milestones) {
            total += v;
            if (v > mx) mx = v;
        }
        long long rest = total - mx;
        long long possible = 2 * rest + 1;
        return min(total, possible);
    }
};
```

## Java

```java
class Solution {
    public long numberOfWeeks(int[] milestones) {
        long sum = 0;
        long max = 0;
        for (int m : milestones) {
            sum += m;
            if (m > max) max = m;
        }
        long others = sum - max;
        if (max > others + 1) {
            return 2 * others + 1;
        } else {
            return sum;
        }
    }
}
```

## Python

```python
class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        total = sum(milestones)
        max_milestone = max(milestones)
        rest = total - max_milestone
        # If the largest project can be interleaved with others completely
        if max_milestone <= rest + 1:
            return total
        else:
            # We can use all other milestones and alternate with the biggest one,
            # ending with a week on the biggest project.
            return 2 * rest + 1
```

## Python3

```python
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        mx = max(milestones)
        return min(total, 2 * (total - mx) + 1)
```

## C

```c
long long numberOfWeeks(int* milestones, int milestonesSize) {
    long long total = 0;
    long long mx = 0;
    for (int i = 0; i < milestonesSize; ++i) {
        long long val = (long long)milestones[i];
        total += val;
        if (val > mx) mx = val;
    }
    long long rest = total - mx;
    if (mx <= rest + 1) return total;
    return 2 * rest + 1;
}
```

## Csharp

```csharp
public class Solution {
    public long NumberOfWeeks(int[] milestones) {
        long total = 0;
        long max = 0;
        foreach (int m in milestones) {
            total += m;
            if (m > max) max = m;
        }
        if (max > total - max) {
            return 2 * (total - max) + 1;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} milestones
 * @return {number}
 */
var numberOfWeeks = function(milestones) {
    let total = 0;
    let max = 0;
    for (const m of milestones) {
        total += m;
        if (m > max) max = m;
    }
    const rest = total - max;
    return max > rest + 1 ? 2 * rest + 1 : total;
};
```

## Typescript

```typescript
function numberOfWeeks(milestones: number[]): number {
    let total = 0;
    let max = 0;
    for (const m of milestones) {
        total += m;
        if (m > max) max = m;
    }
    const possible = 2 * (total - max) + 1;
    return Math.min(total, possible);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $milestones
     * @return Integer
     */
    function numberOfWeeks($milestones) {
        $total = 0;
        $max = 0;
        foreach ($milestones as $v) {
            $total += $v;
            if ($v > $max) {
                $max = $v;
            }
        }
        $rest = $total - $max;
        if ($max > $rest) {
            return $rest * 2 + 1;
        } else {
            return $total;
        }
    }
}
```

## Swift

```swift
class Solution {
    func numberOfWeeks(_ milestones: [Int]) -> Int {
        var total: Int64 = 0
        var maxM: Int64 = 0
        for m in milestones {
            let val = Int64(m)
            total += val
            if val > maxM { maxM = val }
        }
        let rest = total - maxM
        let possible = rest * 2 + 1
        let ans = min(total, possible)
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfWeeks(milestones: IntArray): Long {
        var total = 0L
        var maxVal = 0L
        for (m in milestones) {
            val v = m.toLong()
            total += v
            if (v > maxVal) maxVal = v
        }
        val sumOthers = total - maxVal
        return if (maxVal <= sumOthers + 1) total else 2 * sumOthers + 1
    }
}
```

## Dart

```dart
class Solution {
  int numberOfWeeks(List<int> milestones) {
    int maxVal = 0;
    int total = 0;
    for (int m in milestones) {
      if (m > maxVal) maxVal = m;
      total += m;
    }
    int other = total - maxVal;
    return (maxVal <= other + 1) ? total : 2 * other + 1;
  }
}
```

## Golang

```go
func numberOfWeeks(milestones []int) int64 {
    var total int64
    var maxVal int64
    for _, v := range milestones {
        val := int64(v)
        total += val
        if val > maxVal {
            maxVal = val
        }
    }
    other := total - maxVal
    limit := 2*other + 1
    if total < limit {
        return total
    }
    return limit
}
```

## Ruby

```ruby
def number_of_weeks(milestones)
  total = milestones.sum
  max_milestone = milestones.max
  other = total - max_milestone
  if max_milestone > other
    2 * other + 1
  else
    total
  end
end
```

## Scala

```scala
object Solution {
    def numberOfWeeks(milestones: Array[Int]): Long = {
        var total: Long = 0L
        var maxVal: Long = 0L
        for (m <- milestones) {
            val v = m.toLong
            total += v
            if (v > maxVal) maxVal = v
        }
        val rest = total - maxVal
        val possible = 2 * rest + 1
        if (total <= possible) total else possible
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_weeks(milestones: Vec<i32>) -> i64 {
        let mut total: i64 = 0;
        let mut max_val: i64 = 0;
        for m in milestones {
            let v = m as i64;
            total += v;
            if v > max_val {
                max_val = v;
            }
        }
        let others = total - max_val;
        if max_val > others {
            2 * others + 1
        } else {
            total
        }
    }
}
```

## Racket

```racket
(define/contract (number-of-weeks milestones)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([total (apply + milestones)]
         [mx (apply max milestones)]
         [rest (- total mx)])
    (if (> mx (+ rest 1))
        (+ (* 2 rest) 1)
        total)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_weeks/1]).

-spec number_of_weeks(Milestones :: [integer()]) -> integer().
number_of_weeks(Milestones) ->
    {Sum, Max} = lists:foldl(
        fun(X, {S, M}) -> {S + X, erlang:max(X, M)} end,
        {0, 0},
        Milestones
    ),
    Rest = Sum - Max,
    if
        Max > Rest -> 2 * Rest + 1;
        true -> Sum
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_weeks(milestones :: [integer]) :: integer
  def number_of_weeks(milestones) do
    total = Enum.sum(milestones)
    max_val = Enum.max(milestones)
    other = total - max_val
    possible = 2 * other + 1
    min(total, possible)
  end
end
```
