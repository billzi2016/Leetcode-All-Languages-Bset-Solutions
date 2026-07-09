# 1051. Height Checker

## Cpp

```cpp
class Solution {
public:
    int heightChecker(std::vector<int>& heights) {
        std::vector<int> expected = heights;
        std::sort(expected.begin(), expected.end());
        int mismatches = 0;
        for (size_t i = 0; i < heights.size(); ++i) {
            if (heights[i] != expected[i]) ++mismatches;
        }
        return mismatches;
    }
};
```

## Java

```java
class Solution {
    public int heightChecker(int[] heights) {
        int[] expected = heights.clone();
        java.util.Arrays.sort(expected);
        int mismatches = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != expected[i]) {
                mismatches++;
            }
        }
        return mismatches;
    }
}
```

## Python

```python
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        return sum(h1 != h2 for h1, h2 in zip(heights, expected))
```

## Python3

```python
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(h != e for h, e in zip(heights, expected))
```

## C

```c
#include <string.h>

int heightChecker(int* heights, int heightsSize) {
    int cnt[101];
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < heightsSize; ++i) {
        cnt[heights[i]]++;
    }
    int res = 0;
    int cur = 1;
    for (int i = 0; i < heightsSize; ++i) {
        while (cur <= 100 && cnt[cur] == 0) cur++;
        if (heights[i] != cur) res++;
        cnt[cur]--;
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int HeightChecker(int[] heights) {
        int[] expected = (int[])heights.Clone();
        Array.Sort(expected);
        int mismatches = 0;
        for (int i = 0; i < heights.Length; i++) {
            if (heights[i] != expected[i]) mismatches++;
        }
        return mismatches;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    const expected = [...heights].sort((a, b) => a - b);
    let mismatches = 0;
    for (let i = 0; i < heights.length; i++) {
        if (heights[i] !== expected[i]) mismatches++;
    }
    return mismatches;
};
```

## Typescript

```typescript
function heightChecker(heights: number[]): number {
    const expected = [...heights].sort((a, b) => a - b);
    let mismatches = 0;
    for (let i = 0; i < heights.length; i++) {
        if (heights[i] !== expected[i]) mismatches++;
    }
    return mismatches;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @return Integer
     */
    function heightChecker($heights) {
        $sorted = $heights;
        sort($sorted, SORT_NUMERIC);
        $count = 0;
        $n = count($heights);
        for ($i = 0; $i < $n; $i++) {
            if ($heights[$i] !== $sorted[$i]) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func heightChecker(_ heights: [Int]) -> Int {
        let expected = heights.sorted()
        var mismatches = 0
        for i in 0..<heights.count {
            if heights[i] != expected[i] {
                mismatches += 1
            }
        }
        return mismatches
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun heightChecker(heights: IntArray): Int {
        val expected = heights.clone()
        expected.sort()
        var mismatches = 0
        for (i in heights.indices) {
            if (heights[i] != expected[i]) mismatches++
        }
        return mismatches
    }
}
```

## Dart

```dart
class Solution {
  int heightChecker(List<int> heights) {
    List<int> expected = List.from(heights);
    expected.sort();
    int count = 0;
    for (int i = 0; i < heights.length; i++) {
      if (heights[i] != expected[i]) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func heightChecker(heights []int) int {
    freq := make([]int, 101)
    for _, h := range heights {
        freq[h]++
    }
    mismatches, idx := 0, 0
    for h := 1; h <= 100; h++ {
        for freq[h] > 0 {
            if heights[idx] != h {
                mismatches++
            }
            idx++
            freq[h]--
        }
    }
    return mismatches
}
```

## Ruby

```ruby
# @param {Integer[]} heights
# @return {Integer}
def height_checker(heights)
  expected = heights.sort
  mismatches = 0
  heights.each_with_index do |h, i|
    mismatches += 1 if h != expected[i]
  end
  mismatches
end
```

## Scala

```scala
object Solution {
  def heightChecker(heights: Array[Int]): Int = {
    val sorted = heights.clone()
    java.util.Arrays.sort(sorted)
    var count = 0
    for (i <- heights.indices) {
      if (heights(i) != sorted(i)) count += 1
    }
    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut expected = heights.clone();
        expected.sort_unstable();
        heights.iter()
            .zip(expected.iter())
            .filter(|(a, b)| a != b)
            .count() as i32
    }
}
```

## Racket

```racket
(define/contract (height-checker heights)
  (-> (listof exact-integer?) exact-integer?)
  (let ((sorted (sort heights <)))
    (let loop ((orig heights) (s sorted) (cnt 0))
      (if (null? orig)
          cnt
          (loop (cdr orig) (cdr s)
                (+ cnt (if (= (car orig) (car s)) 0 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([height_checker/1]).

-spec height_checker(Heights :: [integer()]) -> integer().
height_checker(Heights) ->
    Sorted = lists:sort(Heights),
    count_mismatch(Heights, Sorted, 0).

count_mismatch([], [], Acc) -> Acc;
count_mismatch([H|T1], [S|T2], Acc) ->
    NewAcc = if H =/= S -> Acc + 1; true -> Acc end,
    count_mismatch(T1, T2, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec height_checker(heights :: [integer]) :: integer
  def height_checker(heights) do
    sorted = Enum.sort(heights)

    Enum.zip(heights, sorted)
    |> Enum.count(fn {a, b} -> a != b end)
  end
end
```
