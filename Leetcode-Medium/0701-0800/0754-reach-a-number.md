# 0754. Reach a Number

## Cpp

```cpp
class Solution {
public:
    int reachNumber(int target) {
        long long t = std::llabs((long long)target);
        long long sum = 0;
        int k = 0;
        while (sum < t) {
            ++k;
            sum += k;
        }
        while ((sum - t) % 2 != 0) {
            ++k;
            sum += k;
        }
        return k;
    }
};
```

## Java

```java
class Solution {
    public int reachNumber(int target) {
        long t = Math.abs((long) target);
        int k = 0;
        long sum = 0;
        while (sum < t) {
            k++;
            sum += k;
        }
        long diff = sum - t;
        if ((diff & 1) == 0) {
            return k;
        }
        // diff is odd
        if (((k + 1) & 1) == 1) {
            return k + 1;
        } else {
            return k + 2;
        }
    }
}
```

## Python

```python
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        total = 0
        while total < target:
            k += 1
            total += k
        # Adjust until the difference is even
        while (total - target) % 2 != 0:
            k += 1
            total += k
        return k
```

## Python3

```python
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        total = 0
        while total < target:
            k += 1
            total += k
        while (total - target) % 2 != 0:
            k += 1
            total += k
        return k
```

## C

```c
#include <stdlib.h>

int reachNumber(int target) {
    long long t = llabs((long long)target);
    long long k = 0;
    long long sum = 0;
    while (sum < t) {
        ++k;
        sum += k;
    }
    while ((sum - t) % 2 != 0) {
        ++k;
        sum += k;
    }
    return (int)k;
}
```

## Csharp

```csharp
public class Solution
{
    public int ReachNumber(int target)
    {
        long t = Math.Abs((long)target);
        long sum = 0;
        int k = 0;
        while (sum < t)
        {
            k++;
            sum += k;
        }
        while ((sum - t) % 2 != 0)
        {
            k++;
            sum += k;
        }
        return k;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} target
 * @return {number}
 */
var reachNumber = function(target) {
    let t = Math.abs(target);
    let k = 0;
    let sum = 0;
    while (sum < t || ((sum - t) & 1)) {
        k++;
        sum += k;
    }
    return k;
};
```

## Typescript

```typescript
function reachNumber(target: number): number {
    let t = Math.abs(target);
    let k = 0;
    let sum = 0;
    while (sum < t) {
        k++;
        sum += k;
    }
    while ((sum - t) % 2 !== 0) {
        k++;
        sum += k;
    }
    return k;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $target
     * @return Integer
     */
    function reachNumber($target) {
        $target = abs($target);
        $k = 0;
        $sum = 0;
        while ($sum < $target) {
            $k++;
            $sum += $k;
        }
        $delta = $sum - $target;
        if ($delta % 2 == 0) {
            return $k;
        }
        // delta is odd
        // If next step (k+1) is odd, adding it makes delta even
        if ((($k + 1) & 1) == 1) {
            return $k + 1;
        } else {
            // need two more steps
            return $k + 2;
        }
    }
}
```

## Swift

```swift
class Solution {
    func reachNumber(_ target: Int) -> Int {
        var t = abs(target)
        var sum = 0
        var k = 0
        while sum < t {
            k += 1
            sum += k
        }
        if (sum - t) % 2 == 0 {
            return k
        } else {
            // If current k is even, one extra move makes the difference even.
            // If k is odd, need two more moves.
            return k + (k % 2 == 0 ? 1 : 2)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reachNumber(target: Int): Int {
        var t = kotlin.math.abs(target).toLong()
        var sum = 0L
        var k = 0
        while (sum < t) {
            k++
            sum += k
        }
        var delta = sum - t
        if (delta % 2 == 0L) return k
        while (true) {
            k++
            sum += k
            delta = sum - t
            if (delta % 2 == 0L) return k
        }
    }
}
```

## Dart

```dart
class Solution {
  int reachNumber(int target) {
    int t = target.abs();
    int steps = 0;
    int sum = 0;
    while (sum < t || ((sum - t) & 1) == 1) {
      steps++;
      sum += steps;
    }
    return steps;
  }
}
```

## Golang

```go
func reachNumber(target int) int {
    if target < 0 {
        target = -target
    }
    sum, k := 0, 0
    for sum < target || ((sum-target)&1) != 0 {
        k++
        sum += k
    }
    return k
}
```

## Ruby

```ruby
def reach_number(target)
  t = target.abs
  k = 0
  sum = 0
  while sum < t || ((sum - t) & 1) == 1
    k += 1
    sum += k
  end
  k
end
```

## Scala

```scala
object Solution {
    def reachNumber(target: Int): Int = {
        var t = math.abs(target).toLong
        var k = 0L
        var sum = 0L
        while (sum < t || ((sum - t) & 1L) == 1L) {
            k += 1
            sum += k
        }
        k.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reach_number(target: i32) -> i32 {
        let mut need = target.abs() as i64;
        let mut k: i64 = 0;
        let mut sum: i64 = 0;
        while sum < need {
            k += 1;
            sum += k;
        }
        let delta = sum - need;
        if delta % 2 == 0 {
            return k as i32;
        }
        // delta is odd
        if (k + 1) % 2 == 1 {
            (k + 1) as i32
        } else {
            (k + 2) as i32
        }
    }
}
```

## Racket

```racket
(define/contract (reach-number target)
  (-> exact-integer? exact-integer?)
  (let ((t (abs target)))
    (let loop ((k 0) (sum 0))
      (if (and (>= sum t) (even? (- sum t)))
          k
          (let* ((next-k (+ k 1))
                 (next-sum (+ sum next-k)))
            (loop next-k next-sum))))))
```

## Erlang

```erlang
-module(solution).
-export([reach_number/1]).

-spec reach_number(Target :: integer()) -> integer().
reach_number(Target) ->
    Abs = erlang:abs(Target),
    find_moves(Abs, 0, 0).

find_moves(_Target, K, Sum) when Sum >= _Target, ((Sum - _Target) rem 2) =:= 0 ->
    K;
find_moves(Target, K, Sum) ->
    NewK = K + 1,
    NewSum = Sum + NewK,
    find_moves(Target, NewK, NewSum).
```

## Elixir

```elixir
defmodule Solution do
  @spec reach_number(target :: integer) :: integer
  def reach_number(target) do
    t = abs(target)
    {k, sum} = find_k(t, 0, 0)

    delta = sum - t

    cond do
      rem(delta, 2) == 0 -> k
      rem(k + 1, 2) == 1 -> k + 1
      true -> k + 2
    end
  end

  defp find_k(target, k, sum) when sum >= target, do: {k, sum}
  defp find_k(target, k, sum), do: find_k(target, k + 1, sum + k + 1)
end
```
