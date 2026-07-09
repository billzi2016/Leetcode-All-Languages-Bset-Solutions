# 1526. Minimum Number of Increments on Subarrays to Form a Target Array

## Cpp

```cpp
class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        long long ans = 0;
        int prev = 0;
        for (int x : target) {
            if (x > prev) ans += x - prev;
            prev = x;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int minNumberOperations(int[] target) {
        long operations = 0;
        int previous = 0;
        for (int value : target) {
            if (value > previous) {
                operations += value - previous;
            }
            previous = value;
        }
        return (int) operations;
    }
}
```

## Python

```python
class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        ans = 0
        prev = 0
        for cur in target:
            if cur > prev:
                ans += cur - prev
            prev = cur
        return ans
```

## Python3

```python
class Solution:
    def minNumberOperations(self, target):
        ops = 0
        prev = 0
        for x in target:
            if x > prev:
                ops += x - prev
            prev = x
        return ops
```

## C

```c
int minNumberOperations(int* target, int targetSize) {
    long long ans = 0;
    int prev = 0;
    for (int i = 0; i < targetSize; ++i) {
        if (target[i] > prev) {
            ans += target[i] - prev;
        }
        prev = target[i];
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinNumberOperations(int[] target)
    {
        long operations = 0;
        int previous = 0;
        foreach (int value in target)
        {
            if (value > previous)
                operations += value - previous;
            previous = value;
        }
        return (int)operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} target
 * @return {number}
 */
var minNumberOperations = function(target) {
    let ops = target[0];
    for (let i = 1; i < target.length; ++i) {
        if (target[i] > target[i - 1]) {
            ops += target[i] - target[i - 1];
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minNumberOperations(target: number[]): number {
    let operations = 0;
    let prev = 0;
    for (const cur of target) {
        if (cur > prev) {
            operations += cur - prev;
        }
        prev = cur;
    }
    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $target
     * @return Integer
     */
    function minNumberOperations($target) {
        $prev = 0;
        $ans = 0;
        foreach ($target as $val) {
            if ($val > $prev) {
                $ans += $val - $prev;
            }
            $prev = $val;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minNumberOperations(_ target: [Int]) -> Int {
        var ops = 0
        var prev = 0
        for value in target {
            if value > prev {
                ops += value - prev
            }
            prev = value
        }
        return ops
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minNumberOperations(target: IntArray): Int {
        var ops = target[0]
        for (i in 1 until target.size) {
            if (target[i] > target[i - 1]) {
                ops += target[i] - target[i - 1]
            }
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minNumberOperations(List<int> target) {
    if (target.isEmpty) return 0;
    int ops = target[0];
    for (int i = 1; i < target.length; i++) {
      if (target[i] > target[i - 1]) {
        ops += target[i] - target[i - 1];
      }
    }
    return ops;
  }
}
```

## Golang

```go
func minNumberOperations(target []int) int {
	if len(target) == 0 {
		return 0
	}
	ops := target[0]
	for i := 1; i < len(target); i++ {
		if target[i] > target[i-1] {
			ops += target[i] - target[i-1]
		}
	}
	return ops
}
```

## Ruby

```ruby
def min_number_operations(target)
  ops = 0
  prev = 0
  target.each do |val|
    ops += val - prev if val > prev
    prev = val
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minNumberOperations(target: Array[Int]): Int = {
        var ops: Long = 0L
        var prev = 0
        for (v <- target) {
            if (v > prev) ops += v - prev
            prev = v
        }
        ops.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_number_operations(target: Vec<i32>) -> i32 {
        let mut ops: i64 = 0;
        let mut prev = 0i32;
        for &val in target.iter() {
            if val > prev {
                ops += (val - prev) as i64;
            }
            prev = val;
        }
        ops as i32
    }
}
```

## Racket

```racket
(define/contract (min-number-operations target)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst target) (prev 0) (ans 0))
    (if (null? lst)
        ans
        (let* ((cur (car lst))
               (add (max (- cur prev) 0)))
          (loop (cdr lst) cur (+ ans add))))))
```

## Erlang

```erlang
-module(solution).
-export([min_number_operations/1]).

-spec min_number_operations(Target :: [integer()]) -> integer().
min_number_operations(Target) ->
    loop(Target, 0, 0).

loop([], _Prev, Acc) ->
    Acc;
loop([X|Rest], Prev, Acc) when X > Prev ->
    loop(Rest, X, Acc + (X - Prev));
loop([X|Rest], Prev, Acc) ->
    loop(Rest, X, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_number_operations(target :: [integer]) :: integer
  def min_number_operations([]), do: 0
  def min_number_operations([first | rest]) do
    {ans, _} =
      Enum.reduce(rest, {first, first}, fn cur, {acc, prev} ->
        inc = max(cur - prev, 0)
        {acc + inc, cur}
      end)

    ans
  end
end
```
