# 3285. Find Indices of Stable Mountains

## Cpp

```cpp
class Solution {
public:
    vector<int> stableMountains(vector<int>& height, int threshold) {
        vector<int> res;
        for (int i = 1; i < (int)height.size(); ++i) {
            if (height[i - 1] > threshold) {
                res.push_back(i);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i < height.length; i++) {
            if (height[i - 1] > threshold) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                res.append(i)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                res.append(i)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* stableMountains(int* height, int heightSize, int threshold, int* returnSize) {
    int *res = (int*)malloc(heightSize * sizeof(int));
    int cnt = 0;
    for (int i = 1; i < heightSize; ++i) {
        if (height[i - 1] > threshold) {
            res[cnt++] = i;
        }
    }
    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> StableMountains(int[] height, int threshold) {
        var result = new List<int>();
        for (int i = 1; i < height.Length; i++) {
            if (height[i - 1] > threshold) {
                result.Add(i);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} height
 * @param {number} threshold
 * @return {number[]}
 */
var stableMountains = function(height, threshold) {
    const res = [];
    for (let i = 1; i < height.length; ++i) {
        if (height[i - 1] > threshold) {
            res.push(i);
        }
    }
    return res;
};
```

## Typescript

```typescript
function stableMountains(height: number[], threshold: number): number[] {
    const result: number[] = [];
    for (let i = 1; i < height.length; i++) {
        if (height[i - 1] > threshold) {
            result.push(i);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $height
     * @param Integer $threshold
     * @return Integer[]
     */
    function stableMountains($height, $threshold) {
        $n = count($height);
        $res = [];
        for ($i = 1; $i < $n; ++$i) {
            if ($height[$i - 1] > $threshold) {
                $res[] = $i;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func stableMountains(_ height: [Int], _ threshold: Int) -> [Int] {
        var result = [Int]()
        for i in 1..<height.count {
            if height[i - 1] > threshold {
                result.append(i)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stableMountains(height: IntArray, threshold: Int): List<Int> {
        val result = ArrayList<Int>()
        for (i in 1 until height.size) {
            if (height[i - 1] > threshold) {
                result.add(i)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> stableMountains(List<int> height, int threshold) {
    List<int> res = [];
    for (int i = 1; i < height.length; i++) {
      if (height[i - 1] > threshold) {
        res.add(i);
      }
    }
    return res;
  }
}
```

## Golang

```go
func stableMountains(height []int, threshold int) []int {
    var res []int
    for i := 1; i < len(height); i++ {
        if height[i-1] > threshold {
            res = append(res, i)
        }
    }
    return res
}
```

## Ruby

```ruby
def stable_mountains(height, threshold)
  result = []
  (1...height.length).each do |i|
    result << i if height[i - 1] > threshold
  end
  result
end
```

## Scala

```scala
object Solution {
    def stableMountains(height: Array[Int], threshold: Int): List[Int] = {
        val result = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 1 until height.length) {
            if (height(i - 1) > threshold) result += i
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stable_mountains(height: Vec<i32>, threshold: i32) -> Vec<i32> {
        let mut res = Vec::new();
        for i in 1..height.len() {
            if height[i - 1] > threshold {
                res.push(i as i32);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (stable-mountains height threshold)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ((n (length height)))
    (for/list ([i (in-range 1 n)]
               #:when (> (list-ref height (- i 1)) threshold))
      i)))
```

## Erlang

```erlang
-module(find_indices_of_stable_mountains).
-export([stable_mountains/2]).

-spec stable_mountains(Height :: [integer()], Threshold :: integer()) -> [integer()].
stable_mountains(Height, Threshold) ->
    case Height of
        [] -> [];
        [_] -> [];
        [Prev|Tail] ->
            stable_mountains(Tail, Threshold, 1, Prev, [])
    end.

stable_mountains([], _Threshold, _Idx, _Prev, Acc) ->
    lists:reverse(Acc);
stable_mountains([Curr|Rest], Threshold, Idx, Prev, Acc) ->
    NewAcc = if Prev > Threshold -> [Idx | Acc]; true -> Acc end,
    stable_mountains(Rest, Threshold, Idx + 1, Curr, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec stable_mountains(height :: [integer], threshold :: integer) :: [integer]
  def stable_mountains(height, threshold) do
    len = length(height)

    1..(len - 1)
    |> Enum.filter(fn i -> Enum.at(height, i - 1) > threshold end)
  end
end
```
