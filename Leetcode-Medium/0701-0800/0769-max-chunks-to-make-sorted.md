# 0769. Max Chunks To Make Sorted

## Cpp

```cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int chunks = 0;
        int mx = -1;
        for (int i = 0; i < (int)arr.size(); ++i) {
            mx = max(mx, arr[i]);
            if (mx == i) ++chunks;
        }
        return chunks;
    }
};
```

## Java

```java
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int chunks = 0;
        int max = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
            if (max == i) {
                chunks++;
            }
        }
        return chunks;
    }
}
```

## Python

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 0
        cur_max = 0
        for i, val in enumerate(arr):
            if val > cur_max:
                cur_max = val
            if cur_max == i:
                chunks += 1
        return chunks
```

## Python3

```python
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        cur_max = 0
        for i, val in enumerate(arr):
            if val > cur_max:
                cur_max = val
            if cur_max == i:
                chunks += 1
        return chunks
```

## C

```c
int maxChunksToSorted(int* arr, int arrSize) {
    int chunks = 0;
    int curMax = 0;
    for (int i = 0; i < arrSize; ++i) {
        if (arr[i] > curMax) curMax = arr[i];
        if (curMax == i) ++chunks;
    }
    return chunks;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxChunksToSorted(int[] arr)
    {
        int chunks = 0;
        int max = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] > max) max = arr[i];
            if (max == i) chunks++;
        }
        return chunks;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    let chunks = 0;
    let maxVal = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > maxVal) maxVal = arr[i];
        if (maxVal === i) chunks++;
    }
    return chunks;
};
```

## Typescript

```typescript
function maxChunksToSorted(arr: number[]): number {
    let chunks = 0;
    let curMax = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > curMax) curMax = arr[i];
        if (curMax === i) chunks++;
    }
    return chunks;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    public function maxChunksToSorted($arr) {
        $max = 0;
        $chunks = 0;
        foreach ($arr as $i => $val) {
            if ($val > $max) {
                $max = $val;
            }
            if ($max == $i) {
                $chunks++;
            }
        }
        return $chunks;
    }
}
```

## Swift

```swift
class Solution {
    func maxChunksToSorted(_ arr: [Int]) -> Int {
        var chunks = 0
        var currentMax = 0
        for (i, val) in arr.enumerated() {
            if val > currentMax {
                currentMax = val
            }
            if currentMax == i {
                chunks += 1
            }
        }
        return chunks
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxChunksToSorted(arr: IntArray): Int {
        var chunks = 0
        var currentMax = 0
        for (i in arr.indices) {
            if (arr[i] > currentMax) currentMax = arr[i]
            if (currentMax == i) {
                chunks++
            }
        }
        return chunks
    }
}
```

## Dart

```dart
class Solution {
  int maxChunksToSorted(List<int> arr) {
    int chunks = 0;
    int maxVal = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] > maxVal) {
        maxVal = arr[i];
      }
      if (maxVal == i) {
        chunks++;
      }
    }
    return chunks;
  }
}
```

## Golang

```go
func maxChunksToSorted(arr []int) int {
    chunks, maxVal := 0, 0
    for i, v := range arr {
        if v > maxVal {
            maxVal = v
        }
        if maxVal == i {
            chunks++
        }
    }
    return chunks
}
```

## Ruby

```ruby
def max_chunks_to_sorted(arr)
  max_val = 0
  chunks = 0
  arr.each_with_index do |v, i|
    max_val = v if v > max_val
    chunks += 1 if max_val == i
  end
  chunks
end
```

## Scala

```scala
object Solution {
    def maxChunksToSorted(arr: Array[Int]): Int = {
        var maxSoFar = 0
        var chunks = 0
        for (i <- arr.indices) {
            if (arr(i) > maxSoFar) maxSoFar = arr(i)
            if (maxSoFar == i) chunks += 1
        }
        chunks
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let mut chunks = 0;
        let mut cur_max = -1i32;
        for (i, &val) in arr.iter().enumerate() {
            if val > cur_max {
                cur_max = val;
            }
            if cur_max == i as i32 {
                chunks += 1;
            }
        }
        chunks
    }
}
```

## Racket

```racket
(define/contract (max-chunks-to-sorted arr)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst arr) (idx 0) (mx -1) (cnt 0))
    (if (null? lst)
        cnt
        (let* ((val (car lst))
               (new-mx (max mx val))
               (new-cnt (if (= new-mx idx) (+ cnt 1) cnt)))
          (loop (cdr lst) (+ idx 1) new-mx new-cnt)))))
```

## Erlang

```erlang
-module(solution).
-export([max_chunks_to_sorted/1]).

-spec max_chunks_to_sorted(Arr :: [integer()]) -> integer().
max_chunks_to_sorted(Arr) ->
    max_chunks_to_sorted(Arr, 0, -1, 0).

max_chunks_to_sorted([], _Idx, _Max, Count) ->
    Count;
max_chunks_to_sorted([H|T], Idx, MaxSoFar, Count) ->
    NewMax = erlang:max(H, MaxSoFar),
    NewCount = case NewMax == Idx of
        true -> Count + 1;
        false -> Count
    end,
    max_chunks_to_sorted(T, Idx + 1, NewMax, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_chunks_to_sorted(arr :: [integer]) :: integer
  def max_chunks_to_sorted(arr) do
    {chunks, _} =
      Enum.reduce(Enum.with_index(arr), {0, -1}, fn {val, idx}, {cnt, cur_max} ->
        new_max = if val > cur_max, do: val, else: cur_max

        if new_max == idx do
          {cnt + 1, new_max}
        else
          {cnt, new_max}
        end
      end)

    chunks
  end
end
```
