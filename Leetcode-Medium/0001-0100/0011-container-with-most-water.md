# 0011. Container With Most Water

## Cpp

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        long long maxArea = 0;
        while (left < right) {
            long long width = right - left;
            long long h = min(height[left], height[right]);
            maxArea = max(maxArea, width * h);
            if (height[left] < height[right]) ++left;
            else --right;
        }
        return static_cast<int>(maxArea);
    }
};
```

## Java

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            int h = Math.min(height[left], height[right]);
            int area = h * (right - left);
            if (area > maxArea) {
                maxArea = area;
            }
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}
```

## Python

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            if height[left] < height[right]:
                area = height[left] * width
                left += 1
            else:
                area = height[right] * width
                right -= 1
            if area > max_area:
                max_area = area
        return max_area
```

## Python3

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            h_left, h_right = height[left], height[right]
            width = right - left
            if h_left < h_right:
                area = width * h_left
                left += 1
            else:
                area = width * h_right
                right -= 1
            if area > max_area:
                max_area = area
        return max_area
```

## C

```c
int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize - 1;
    int max_area = 0;
    while (left < right) {
        int h = height[left] < height[right] ? height[left] : height[right];
        int area = h * (right - left);
        if (area > max_area) {
            max_area = area;
        }
        if (height[left] < height[right]) {
            ++left;
        } else {
            --right;
        }
    }
    return max_area;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxArea(int[] height) {
        int left = 0;
        int right = height.Length - 1;
        int maxArea = 0;
        while (left < right) {
            int width = right - left;
            int h = height[left] < height[right] ? height[left] : height[right];
            int area = width * h;
            if (area > maxArea) maxArea = area;
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max = 0;
    while (left < right) {
        const h = Math.min(height[left], height[right]);
        const area = h * (right - left);
        if (area > max) max = area;
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max;
};
```

## Typescript

```typescript
function maxArea(height: number[]): number {
    let left = 0;
    let right = height.length - 1;
    let max = 0;
    while (left < right) {
        const width = right - left;
        const h = Math.min(height[left], height[right]);
        const area = width * h;
        if (area > max) max = area;
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function maxArea($height) {
        $left = 0;
        $right = count($height) - 1;
        $max = 0;
        while ($left < $right) {
            $h = min($height[$left], $height[$right]);
            $area = $h * ($right - $left);
            if ($area > $max) {
                $max = $area;
            }
            if ($height[$left] < $height[$right]) {
                $left++;
            } else {
                $right--;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var left = 0
        var right = height.count - 1
        var maxArea = 0
        
        while left < right {
            let width = right - left
            let currentHeight = min(height[left], height[right])
            maxArea = max(maxArea, width * currentHeight)
            
            if height[left] < height[right] {
                left += 1
            } else {
                right -= 1
            }
        }
        
        return maxArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxArea(height: IntArray): Int {
        var left = 0
        var right = height.size - 1
        var maxArea = 0
        while (left < right) {
            val h = if (height[left] < height[right]) height[left] else height[right]
            val area = h * (right - left)
            if (area > maxArea) {
                maxArea = area
            }
            if (height[left] < height[right]) {
                left++
            } else {
                right--
            }
        }
        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  int maxArea(List<int> height) {
    int left = 0;
    int right = height.length - 1;
    int max = 0;
    while (left < right) {
      int h = height[left] < height[right] ? height[left] : height[right];
      int area = h * (right - left);
      if (area > max) {
        max = area;
      }
      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }
    return max;
  }
}
```

## Golang

```go
func maxArea(height []int) int {
    left, right := 0, len(height)-1
    maxArea := 0
    for left < right {
        var h int
        if height[left] < height[right] {
            h = height[left]
        } else {
            h = height[right]
        }
        area := h * (right - left)
        if area > maxArea {
            maxArea = area
        }
        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }
    return maxArea
}
```

## Ruby

```ruby
def max_area(height)
  left = 0
  right = height.length - 1
  max = 0
  while left < right
    h = height[left] < height[right] ? height[left] : height[right]
    area = (right - left) * h
    max = area if area > max
    if height[left] < height[right]
      left += 1
    else
      right -= 1
    end
  end
  max
end
```

## Scala

```scala
object Solution {
    def maxArea(height: Array[Int]): Int = {
        var left = 0
        var right = height.length - 1
        var max = 0
        while (left < right) {
            val h = Math.min(height(left), height(right))
            val area = h * (right - left)
            if (area > max) max = area
            if (height(left) < height(right)) left += 1 else right -= 1
        }
        max
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0usize;
        let mut right = height.len() - 1;
        let mut max_area = 0i32;

        while left < right {
            let width = (right - left) as i32;
            let h_left = height[left];
            let h_right = height[right];
            let current_height = if h_left < h_right { h_left } else { h_right };
            let area = width * current_height;
            if area > max_area {
                max_area = area;
            }

            if h_left < h_right {
                left += 1;
            } else {
                right -= 1;
            }
        }

        max_area
    }
}
```

## Racket

```racket
(define/contract (max-area height)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector height)]
         [n (vector-length v)])
    (let loop ([l 0] [r (sub1 n)] [best 0])
      (if (>= l r)
          best
          (let* ([hl (vector-ref v l)]
                 [hr (vector-ref v r)]
                 [area (* (min hl hr) (- r l))]
                 [new-best (if (> area best) area best)])
            (if (< hl hr)
                (loop (+ l 1) r new-best)
                (loop l (- r 1) new-best)))))))
```

## Erlang

```erlang
-spec max_area(Height :: [integer()]) -> integer().
max_area(Height) ->
    Tuple = list_to_tuple(Height),
    Len = tuple_size(Tuple),
    max_area_loop(Tuple, 0, Len - 1, 0).

max_area_loop(_Tuple, L, R, Max) when L >= R ->
    Max;
max_area_loop(Tuple, L, R, Max) ->
    HLeft = element(L + 1, Tuple),
    HRight = element(R + 1, Tuple),
    Area = (R - L) * erlang:min(HLeft, HRight),
    NewMax = if Area > Max -> Area; true -> Max end,
    case HLeft =< HRight of
        true -> max_area_loop(Tuple, L + 1, R, NewMax);
        false -> max_area_loop(Tuple, L, R - 1, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_area(height :: [integer]) :: integer
  def max_area(height) do
    len = length(height)
    do_max_area(height, 0, len - 1, 0)
  end

  defp do_max_area(_height, left, right, max) when left >= right, do: max

  defp do_max_area(height, left, right, max) do
    h_left = Enum.at(height, left)
    h_right = Enum.at(height, right)

    area = min(h_left, h_right) * (right - left)
    new_max = if area > max, do: area, else: max

    cond do
      h_left < h_right ->
        do_max_area(height, left + 1, right, new_max)

      h_left > h_right ->
        do_max_area(height, left, right - 1, new_max)

      true ->
        # heights equal, move either pointer; moving left is sufficient
        do_max_area(height, left + 1, right, new_max)
    end
  end
end
```
