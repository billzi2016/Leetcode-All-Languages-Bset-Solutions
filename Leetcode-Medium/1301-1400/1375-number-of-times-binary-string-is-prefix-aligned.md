# 1375. Number of Times Binary String Is Prefix-Aligned

## Cpp

```cpp
class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) {
        int ans = 0;
        int maxPos = 0;
        for (int i = 0; i < (int)flips.size(); ++i) {
            maxPos = max(maxPos, flips[i]);
            if (maxPos == i + 1) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numTimesAllBlue(int[] flips) {
        int maxPos = 0;
        int count = 0;
        for (int i = 0; i < flips.length; i++) {
            if (flips[i] > maxPos) {
                maxPos = flips[i];
            }
            if (maxPos == i + 1) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        res = 0
        cur_max = 0
        for i, pos in enumerate(flips, 1):  # i is the step count (1-indexed)
            if pos > cur_max:
                cur_max = pos
            if cur_max == i:
                res += 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0
        cur_max = 0
        for i, pos in enumerate(flips, 1):
            if pos > cur_max:
                cur_max = pos
            if cur_max == i:
                res += 1
        return res
```

## C

```c
#include <stddef.h>

int numTimesAllBlue(int* flips, int flipsSize) {
    int maxPos = 0;
    int count = 0;
    for (int i = 1; i <= flipsSize; ++i) {
        if (flips[i - 1] > maxPos) {
            maxPos = flips[i - 1];
        }
        if (maxPos == i) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumTimesAllBlue(int[] flips)
    {
        int result = 0;
        int maxFlipped = 0;
        for (int i = 0; i < flips.Length; i++)
        {
            if (flips[i] > maxFlipped) maxFlipped = flips[i];
            if (maxFlipped == i + 1) result++;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} flips
 * @return {number}
 */
var numTimesAllBlue = function(flips) {
    let maxPos = 0;
    let count = 0;
    for (let i = 0; i < flips.length; i++) {
        if (flips[i] > maxPos) maxPos = flips[i];
        // steps are 1-indexed
        if (maxPos === i + 1) count++;
    }
    return count;
};
```

## Typescript

```typescript
function numTimesAllBlue(flips: number[]): number {
    let count = 0;
    let maxPos = 0;
    for (let i = 0; i < flips.length; i++) {
        if (flips[i] > maxPos) maxPos = flips[i];
        if (maxPos === i + 1) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $flips
     * @return Integer
     */
    function numTimesAllBlue($flips) {
        $max = 0;
        $ans = 0;
        $n = count($flips);
        for ($i = 0; $i < $n; $i++) {
            if ($flips[$i] > $max) {
                $max = $flips[$i];
            }
            if ($max == $i + 1) {
                $ans++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numTimesAllBlue(_ flips: [Int]) -> Int {
        var result = 0
        var currentMax = 0
        for (index, position) in flips.enumerated() {
            if position > currentMax {
                currentMax = position
            }
            if currentMax == index + 1 {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numTimesAllBlue(flips: IntArray): Int {
        var count = 0
        var maxPos = 0
        for (i in flips.indices) {
            if (flips[i] > maxPos) maxPos = flips[i]
            if (maxPos == i + 1) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numTimesAllBlue(List<int> flips) {
    int count = 0;
    int maxPos = 0;
    for (int i = 0; i < flips.length; i++) {
      if (flips[i] > maxPos) {
        maxPos = flips[i];
      }
      if (maxPos == i + 1) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func numTimesAllBlue(flips []int) int {
    maxPos, count := 0, 0
    for i, v := range flips {
        if v > maxPos {
            maxPos = v
        }
        if maxPos == i+1 {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def num_times_all_blue(flips)
  max_pos = 0
  count = 0
  flips.each_with_index do |pos, idx|
    max_pos = pos if pos > max_pos
    count += 1 if max_pos == idx + 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def numTimesAllBlue(flips: Array[Int]): Int = {
        var count = 0
        var maxPos = 0
        for (i <- flips.indices) {
            maxPos = math.max(maxPos, flips(i))
            if (maxPos == i + 1) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_times_all_blue(flips: Vec<i32>) -> i32 {
        let mut max_pos = 0usize;
        let mut count = 0i32;
        for (i, &pos) in flips.iter().enumerate() {
            let p = pos as usize;
            if p > max_pos {
                max_pos = p;
            }
            if max_pos == i + 1 {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (num-times-all-blue flips)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((i 1) (max-pos 0) (cnt 0) (rest flips))
    (if (null? rest)
        cnt
        (let* ((pos (car rest))
               (new-max (if (> pos max-pos) pos max-pos))
               (new-cnt (if (= new-max i) (+ cnt 1) cnt)))
          (loop (+ i 1) new-max new-cnt (cdr rest))))))
```

## Erlang

```erlang
-spec num_times_all_blue(Flips :: [integer()]) -> integer().
num_times_all_blue(Flips) ->
    loop(Flips, 1, 0, 0).

loop([], _Idx, _Max, Count) ->
    Count;
loop([H|T], Idx, MaxSoFar, Count) ->
    NewMax = erlang:max(H, MaxSoFar),
    NewCount = if NewMax == Idx -> Count + 1; true -> Count end,
    loop(T, Idx + 1, NewMax, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_times_all_blue(flips :: [integer]) :: integer
  def num_times_all_blue(flips) do
    {count, _} =
      Enum.reduce(Enum.with_index(flips, 1), {0, 0}, fn {pos, i}, {cnt, cur_max} ->
        new_max = if pos > cur_max, do: pos, else: cur_max
        new_cnt = if new_max == i, do: cnt + 1, else: cnt
        {new_cnt, new_max}
      end)

    count
  end
end
```
