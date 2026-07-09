# 1464. Maximum Product of Two Elements in an Array

## Cpp

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max1 = 0, max2 = 0;
        for (int x : nums) {
            if (x > max1) {
                max2 = max1;
                max1 = x;
            } else if (x > max2) {
                max2 = x;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
};
```

## Java

```java
class Solution {
    public int maxProduct(int[] nums) {
        int max1 = 0, max2 = 0;
        for (int num : nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
}
```

## Python

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
```

## Python3

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = 0
        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x
        return (max1 - 1) * (max2 - 1)
```

## C

```c
int maxProduct(int* nums, int numsSize) {
    int max1 = 0, max2 = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > max1) {
            max2 = max1;
            max1 = nums[i];
        } else if (nums[i] > max2) {
            max2 = nums[i];
        }
    }
    return (max1 - 1) * (max2 - 1);
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProduct(int[] nums) {
        int max1 = 0, max2 = 0;
        foreach (int num in nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let max1 = 0, max2 = 0;
    for (const n of nums) {
        if (n > max1) {
            max2 = max1;
            max1 = n;
        } else if (n > max2) {
            max2 = n;
        }
    }
    return (max1 - 1) * (max2 - 1);
};
```

## Typescript

```typescript
function maxProduct(nums: number[]): number {
    let max1 = 0, max2 = 0;
    for (const num of nums) {
        if (num > max1) {
            max2 = max1;
            max1 = num;
        } else if (num > max2) {
            max2 = num;
        }
    }
    return (max1 - 1) * (max2 - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProduct($nums) {
        $first = 0;
        $second = 0;
        foreach ($nums as $num) {
            if ($num > $first) {
                $second = $first;
                $first = $num;
            } elseif ($num > $second) {
                $second = $num;
            }
        }
        return ($first - 1) * ($second - 1);
    }
}
```

## Swift

```swift
class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        var max1 = 0
        var max2 = 0
        for num in nums {
            if num > max1 {
                max2 = max1
                max1 = num
            } else if num > max2 {
                max2 = num
            }
        }
        return (max1 - 1) * (max2 - 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProduct(nums: IntArray): Int {
        var max1 = 0
        var max2 = 0
        for (num in nums) {
            if (num > max1) {
                max2 = max1
                max1 = num
            } else if (num > max2) {
                max2 = num
            }
        }
        return (max1 - 1) * (max2 - 1)
    }
}
```

## Dart

```dart
class Solution {
  int maxProduct(List<int> nums) {
    int max1 = 0, max2 = 0;
    for (int num in nums) {
      if (num > max1) {
        max2 = max1;
        max1 = num;
      } else if (num > max2) {
        max2 = num;
      }
    }
    return (max1 - 1) * (max2 - 1);
  }
}
```

## Golang

```go
func maxProduct(nums []int) int {
    max1, max2 := 0, 0
    for _, v := range nums {
        if v > max1 {
            max2 = max1
            max1 = v
        } else if v > max2 {
            max2 = v
        }
    }
    return (max1 - 1) * (max2 - 1)
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
  biggest = 0
  second_biggest = 0

  nums.each do |num|
    if num > biggest
      second_biggest = biggest
      biggest = num
    elsif num > second_biggest
      second_biggest = num
    end
  end

  (biggest - 1) * (second_biggest - 1)
end
```

## Scala

```scala
object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        var max1 = 0
        var max2 = 0
        for (num <- nums) {
            if (num > max1) {
                max2 = max1
                max1 = num
            } else if (num > max2) {
                max2 = num
            }
        }
        (max1 - 1) * (max2 - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max1 = 0;
        let mut max2 = 0;
        for &num in nums.iter() {
            if num > max1 {
                max2 = max1;
                max1 = num;
            } else if num > max2 {
                max2 = num;
            }
        }
        (max1 - 1) * (max2 - 1)
    }
}
```

## Racket

```racket
(define/contract (max-product nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (biggest 0) (second-biggest 0))
    (if (null? lst)
        (* (- biggest 1) (- second-biggest 1))
        (let ((x (car lst)))
          (cond
            [(> x biggest) (loop (cdr lst) x biggest)]
            [(> x second-biggest) (loop (cdr lst) biggest x)]
            [else (loop (cdr lst) biggest second-biggest)])))))
```

## Erlang

```erlang
-spec max_product(Nums :: [integer()]) -> integer().
max_product(Nums) ->
    {Max1, Max2} = lists:foldl(
        fun(N, {M1, M2}) ->
            if
                N > M1 -> {N, M1};
                N > M2 -> {M1, N};
                true   -> {M1, M2}
            end
        end,
        {0, 0},
        Nums),
    (Max1 - 1) * (Max2 - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_product(nums :: [integer]) :: integer
  def max_product(nums) do
    {max1, max2} =
      Enum.reduce(nums, {0, 0}, fn num, {big, sec} ->
        cond do
          num > big -> {num, big}
          num > sec -> {big, num}
          true -> {big, sec}
        end
      end)

    (max1 - 1) * (max2 - 1)
  end
end
```
