# 0042. Trapping Rain Water

## Cpp

```cpp
class Solution {
public:
    int trap(std::vector<int>& height) {
        int n = height.size();
        if (n == 0) return 0;
        int left = 0, right = n - 1;
        int left_max = 0, right_max = 0;
        long long ans = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                } else {
                    ans += left_max - height[left];
                }
                ++left;
            } else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                } else {
                    ans += right_max - height[right];
                }
                --right;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int trap(int[] height) {
        if (height == null || height.length < 3) return 0;
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0;
        int water = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    water += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    water += rightMax - height[right];
                }
                right--;
            }
        }
        return water;
    }
}
```

## Python

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
```

## Python3

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
```

## C

```c
int trap(int* height, int heightSize) {
    if (heightSize < 3) return 0;
    int left = 0, right = heightSize - 1;
    int left_max = 0, right_max = 0;
    long long ans = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= left_max) {
                left_max = height[left];
            } else {
                ans += left_max - height[left];
            }
            ++left;
        } else {
            if (height[right] >= right_max) {
                right_max = height[right];
            } else {
                ans += right_max - height[right];
            }
            --right;
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int Trap(int[] height)
    {
        if (height == null || height.Length < 3)
            return 0;

        int left = 0;
        int right = height.Length - 1;
        int leftMax = 0;
        int rightMax = 0;
        long water = 0;

        while (left < right)
        {
            if (height[left] < height[right])
            {
                if (height[left] >= leftMax)
                    leftMax = height[left];
                else
                    water += leftMax - height[left];
                left++;
            }
            else
            {
                if (height[right] >= rightMax)
                    rightMax = height[right];
                else
                    water += rightMax - height[right];
                right--;
            }
        }

        return (int)water;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const n = height.length;
    if (n < 3) return 0;
    let left = 0, right = n - 1;
    let leftMax = 0, rightMax = 0;
    let ans = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                ans += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                ans += rightMax - height[right];
            }
            right--;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function trap(height: number[]): number {
    const n = height.length;
    if (n < 3) return 0;

    let left = 0, right = n - 1;
    let leftMax = 0, rightMax = 0;
    let water = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                water += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                water += rightMax - height[right];
            }
            right--;
        }
    }

    return water;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function trap($height) {
        $n = count($height);
        if ($n == 0) return 0;
        $left = 0;
        $right = $n - 1;
        $leftMax = 0;
        $rightMax = 0;
        $water = 0;

        while ($left < $right) {
            if ($height[$left] < $height[$right]) {
                if ($height[$left] >= $leftMax) {
                    $leftMax = $height[$left];
                } else {
                    $water += $leftMax - $height[$left];
                }
                $left++;
            } else {
                if ($height[$right] >= $rightMax) {
                    $rightMax = $height[$right];
                } else {
                    $water += $rightMax - $height[$right];
                }
                $right--;
            }
        }

        return $water;
    }
}
```

## Swift

```swift
class Solution {
    func trap(_ height: [Int]) -> Int {
        let n = height.count
        if n < 3 { return 0 }
        var left = 0
        var right = n - 1
        var leftMax = 0
        var rightMax = 0
        var water = 0
        
        while left < right {
            if height[left] < height[right] {
                if height[left] >= leftMax {
                    leftMax = height[left]
                } else {
                    water += leftMax - height[left]
                }
                left += 1
            } else {
                if height[right] >= rightMax {
                    rightMax = height[right]
                } else {
                    water += rightMax - height[right]
                }
                right -= 1
            }
        }
        return water
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun trap(height: IntArray): Int {
        var left = 0
        var right = height.size - 1
        var leftMax = 0
        var rightMax = 0
        var ans = 0
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left]
                } else {
                    ans += leftMax - height[left]
                }
                left++
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right]
                } else {
                    ans += rightMax - height[right]
                }
                right--
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int trap(List<int> height) {
    int left = 0;
    int right = height.length - 1;
    int leftMax = 0;
    int rightMax = 0;
    int ans = 0;

    while (left < right) {
      if (height[left] < height[right]) {
        if (height[left] >= leftMax) {
          leftMax = height[left];
        } else {
          ans += leftMax - height[left];
        }
        left++;
      } else {
        if (height[right] >= rightMax) {
          rightMax = height[right];
        } else {
          ans += rightMax - height[right];
        }
        right--;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func trap(height []int) int {
    n := len(height)
    if n == 0 {
        return 0
    }
    left, right := 0, n-1
    leftMax, rightMax := 0, 0
    ans := 0
    for left < right {
        if height[left] < height[right] {
            if height[left] >= leftMax {
                leftMax = height[left]
            } else {
                ans += leftMax - height[left]
            }
            left++
        } else {
            if height[right] >= rightMax {
                rightMax = height[right]
            } else {
                ans += rightMax - height[right]
            }
            right--
        }
    }
    return ans
}
```

## Ruby

```ruby
def trap(height)
  left = 0
  right = height.length - 1
  left_max = 0
  right_max = 0
  water = 0

  while left < right
    if height[left] < height[right]
      if height[left] >= left_max
        left_max = height[left]
      else
        water += left_max - height[left]
      end
      left += 1
    else
      if height[right] >= right_max
        right_max = height[right]
      else
        water += right_max - height[right]
      end
      right -= 1
    end
  end

  water
end
```

## Scala

```scala
object Solution {
    def trap(height: Array[Int]): Int = {
        val n = height.length
        if (n < 3) return 0
        var left = 0
        var right = n - 1
        var leftMax = 0
        var rightMax = 0
        var water: Long = 0L

        while (left < right) {
            if (height(left) < height(right)) {
                if (height(left) >= leftMax) {
                    leftMax = height(left)
                } else {
                    water += leftMax - height(left)
                }
                left += 1
            } else {
                if (height(right) >= rightMax) {
                    rightMax = height(right)
                } else {
                    water += rightMax - height(right)
                }
                right -= 1
            }
        }

        water.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len();
        if n == 0 {
            return 0;
        }
        let mut left = 0usize;
        let mut right = n - 1;
        let mut left_max = 0i32;
        let mut right_max = 0i32;
        let mut ans: i64 = 0;

        while left < right {
            if height[left] < height[right] {
                if height[left] >= left_max {
                    left_max = height[left];
                } else {
                    ans += (left_max - height[left]) as i64;
                }
                left += 1;
            } else {
                if height[right] >= right_max {
                    right_max = height[right];
                } else {
                    ans += (right_max - height[right]) as i64;
                }
                if right == 0 { break; }
                right -= 1;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (trap height)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector height))
         (n (vector-length v)))
    (let loop ((left 0) (right (sub1 n)) (left-max 0) (right-max 0) (ans 0))
      (if (>= left right)
          ans
          (if (< (vector-ref v left) (vector-ref v right))
              (let* ((h (vector-ref v left))
                     (new-left-max (max left-max h))
                     (add (if (> left-max h) (- left-max h) 0)))
                (loop (add1 left) right new-left-max right-max (+ ans add)))
              (let* ((h (vector-ref v right))
                     (new-right-max (max right-max h))
                     (add (if (> right-max h) (- right-max h) 0)))
                (loop left (sub1 right) left-max new-right-max (+ ans add))))))))
```

## Erlang

```erlang
-module(solution).
-export([trap/1]).

-spec trap(Height :: [integer()]) -> integer().
trap(Height) ->
    Arr = list_to_tuple(Height),
    N = tuple_size(Arr),
    loop(0, N - 1, 0, 0, 0, Arr).

loop(L, R, _LeftMax, _RightMax, Acc, _Arr) when L > R ->
    Acc;
loop(L, R, LeftMax, RightMax, Acc, Arr) ->
    HLeft = element(L + 1, Arr),
    HRight = element(R + 1, Arr),
    if
        LeftMax =< RightMax ->
            if HLeft < LeftMax ->
                    loop(L + 1, R, LeftMax, RightMax,
                         Acc + (LeftMax - HLeft), Arr);
               true ->
                    loop(L + 1, R, HLeft, RightMax, Acc, Arr)
            end;
        true ->
            if HRight < RightMax ->
                    loop(L, R - 1, LeftMax, RightMax,
                         Acc + (RightMax - HRight), Arr);
               true ->
                    loop(L, R - 1, LeftMax, HRight, Acc, Arr)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec trap(height :: [integer]) :: integer
  def trap(height) do
    heights = List.to_tuple(height)
    len = tuple_size(heights)

    if len == 0 do
      0
    else
      do_trap(heights, 0, len - 1, 0, 0, 0)
    end
  end

  defp do_trap(_heights, left, right, _lmax, _rmax, acc) when left >= right,
    do: acc

  defp do_trap(heights, left, right, lmax, rmax, acc) do
    h_left = elem(heights, left)
    h_right = elem(heights, right)

    if h_left < h_right do
      if h_left >= lmax do
        do_trap(heights, left + 1, right, h_left, rmax, acc)
      else
        do_trap(heights, left + 1, right, lmax, rmax, acc + (lmax - h_left))
      end
    else
      if h_right >= rmax do
        do_trap(heights, left, right - 1, lmax, h_right, acc)
      else
        do_trap(heights, left, right - 1, lmax, rmax, acc + (rmax - h_right))
      end
    end
  end
end
```
