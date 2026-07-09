# 0334. Increasing Triplet Subsequence

## Cpp

```cpp
class Solution {
public:
    bool increasingTriplet(std::vector<int>& nums) {
        int first = INT_MAX, second = INT_MAX;
        for (int x : nums) {
            if (x <= first) {
                first = x;
            } else if (x <= second) {
                second = x;
            } else {
                return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;
        for (int num : nums) {
            if (num <= first) {
                first = num;
            } else if (num <= second) {
                second = num;
            } else {
                return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```

## C

```c
#include <limits.h>
#include <stdbool.h>

bool increasingTriplet(int* nums, int numsSize) {
    int first = INT_MAX;
    int second = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] <= first) {
            first = nums[i];
        } else if (nums[i] <= second) {
            second = nums[i];
        } else {
            return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool IncreasingTriplet(int[] nums) {
        int first = int.MaxValue;
        int second = int.MaxValue;
        foreach (int num in nums) {
            if (num <= first) {
                first = num;
            } else if (num <= second) {
                second = num;
            } else {
                return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    let first = Infinity, second = Infinity;
    for (const n of nums) {
        if (n <= first) {
            first = n;
        } else if (n <= second) {
            second = n;
        } else {
            return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function increasingTriplet(nums: number[]): boolean {
    let first = Number.POSITIVE_INFINITY;
    let second = Number.POSITIVE_INFINITY;
    for (const x of nums) {
        if (x <= first) {
            first = x;
        } else if (x <= second) {
            second = x;
        } else {
            return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function increasingTriplet($nums) {
        $first = PHP_INT_MAX;
        $second = PHP_INT_MAX;
        foreach ($nums as $num) {
            if ($num <= $first) {
                $first = $num;
            } elseif ($num <= $second) {
                $second = $num;
            } else {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func increasingTriplet(_ nums: [Int]) -> Bool {
        var first = Int.max
        var second = Int.max
        for num in nums {
            if num <= first {
                first = num
            } else if num <= second {
                second = num
            } else {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun increasingTriplet(nums: IntArray): Boolean {
        var first = Int.MAX_VALUE
        var second = Int.MAX_VALUE
        for (num in nums) {
            when {
                num <= first -> first = num
                num <= second -> second = num
                else -> return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool increasingTriplet(List<int> nums) {
    int first = 0x7FFFFFFFFFFFFFFF; // large positive sentinel
    int second = 0x7FFFFFFFFFFFFFFF;
    for (int x in nums) {
      if (x <= first) {
        first = x;
      } else if (x <= second) {
        second = x;
      } else {
        return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func increasingTriplet(nums []int) bool {
	if len(nums) < 3 {
		return false
	}
	maxInt := int(^uint(0) >> 1)
	first, second := maxInt, maxInt
	for _, x := range nums {
		if x <= first {
			first = x
		} else if x <= second {
			second = x
		} else {
			return true
		}
	}
	return false
}
```

## Ruby

```ruby
def increasing_triplet(nums)
  first = second = Float::INFINITY
  nums.each do |num|
    if num <= first
      first = num
    elsif num <= second
      second = num
    else
      return true
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def increasingTriplet(nums: Array[Int]): Boolean = {
        var first = Int.MaxValue
        var second = Int.MaxValue
        for (x <- nums) {
            if (x <= first) {
                first = x
            } else if (x <= second) {
                second = x
            } else {
                return true
            }
        }
        false
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        let mut first = i32::MAX;
        let mut second = i32::MAX;
        for &x in nums.iter() {
            if x <= first {
                first = x;
            } else if x <= second {
                second = x;
            } else {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (increasing-triplet nums)
  (-> (listof exact-integer?) boolean?)
  (let loop ((lst nums) (first +inf.0) (second +inf.0))
    (if (null? lst)
        #f
        (let ((x (car lst)))
          (cond
            [(<= x first) (loop (cdr lst) x second)]
            [(<= x second) (loop (cdr lst) first x)]
            [else #t])))))
```

## Erlang

```erlang
-spec increasing_triplet(Nums :: [integer()]) -> boolean().
increasing_triplet(Nums) ->
    increasing_triplet(Nums, 2147483648, 2147483648).

increasing_triplet([], _First, _Second) ->
    false;
increasing_triplet([H|T], First, Second) when H =< First ->
    increasing_triplet(T, H, Second);
increasing_triplet([H|T], First, Second) when H =< Second ->
    increasing_triplet(T, First, H);
increasing_triplet(_List, _First, _Second) ->
    true.
```

## Elixir

```elixir
defmodule Solution do
  @spec increasing_triplet(nums :: [integer]) :: boolean
  def increasing_triplet(nums) do
    inc_triplet(nums, 2_147_483_648, 2_147_483_648)
  end

  defp inc_triplet([], _first, _second), do: false

  defp inc_triplet([h | t], first, second) when h <= first do
    inc_triplet(t, h, second)
  end

  defp inc_triplet([h | t], first, second) when h <= second do
    inc_triplet(t, first, h)
  end

  defp inc_triplet(_list, _first, _second), do: true
end
```
