# 0167. Two Sum II - Input Array Is Sorted

## Cpp

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = (int)numbers.size() - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return {left + 1, right + 1};
            } else if (sum < target) {
                ++left;
            } else {
                --right;
            }
        }
        return {};
    }
};
```

## Java

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return new int[]{left + 1, right + 1};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[0]; // guaranteed to have a solution
    }
}
```

## Python

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        # As per problem statement, there is exactly one solution.
        return []
```

## Python3

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        # As per problem statement, exactly one solution exists; this line is never reached.
        return []
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int left = 0;
    int right = numbersSize - 1;
    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            break;
        } else if (sum < target) {
            ++left;
        } else {
            --right;
        }
    }
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = left + 1;   // convert to 1-indexed
    result[1] = right + 1;
    *returnSize = 2;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.Length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return new int[] { left + 1, right + 1 };
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[0]; // guaranteed to find a solution
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;
    while (left < right) {
        const sum = numbers[left] + numbers[right];
        if (sum === target) {
            return [left + 1, right + 1];
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return [];
};
```

## Typescript

```typescript
function twoSum(numbers: number[], target: number): number[] {
    let left = 0;
    let right = numbers.length - 1;
    while (left < right) {
        const sum = numbers[left] + numbers[right];
        if (sum === target) {
            return [left + 1, right + 1];
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    // According to problem constraints, a solution always exists.
    return [];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $numbers
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($numbers, $target) {
        $left = 0;
        $right = count($numbers) - 1;

        while ($left < $right) {
            $sum = $numbers[$left] + $numbers[$right];
            if ($sum == $target) {
                return [$left + 1, $right + 1];
            } elseif ($sum < $target) {
                $left++;
            } else {
                $right--;
            }
        }

        // According to problem constraints, a solution always exists.
        return [];
    }
}
```

## Swift

```swift
class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var left = 0
        var right = numbers.count - 1
        while left < right {
            let sum = numbers[left] + numbers[right]
            if sum == target {
                return [left + 1, right + 1]
            } else if sum < target {
                left += 1
            } else {
                right -= 1
            }
        }
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var left = 0
        var right = numbers.size - 1
        while (left < right) {
            val sum = numbers[left] + numbers[right]
            when {
                sum == target -> return intArrayOf(left + 1, right + 1)
                sum < target -> left++
                else -> right--
            }
        }
        return intArrayOf(-1, -1) // guaranteed to have a solution
    }
}
```

## Dart

```dart
class Solution {
  List<int> twoSum(List<int> numbers, int target) {
    int left = 0;
    int right = numbers.length - 1;
    while (left < right) {
      int sum = numbers[left] + numbers[right];
      if (sum == target) {
        return [left + 1, right + 1];
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }
    // As per problem statement, a solution always exists.
    return [];
  }
}
```

## Golang

```go
func twoSum(numbers []int, target int) []int {
    left, right := 0, len(numbers)-1
    for left < right {
        sum := numbers[left] + numbers[right]
        if sum == target {
            return []int{left + 1, right + 1}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return nil
}
```

## Ruby

```ruby
def two_sum(numbers, target)
  left = 0
  right = numbers.length - 1
  while left < right
    sum = numbers[left] + numbers[right]
    if sum == target
      return [left + 1, right + 1]
    elsif sum < target
      left += 1
    else
      right -= 1
    end
  end
  []
end
```

## Scala

```scala
object Solution {
    def twoSum(numbers: Array[Int], target: Int): Array[Int] = {
        var left = 0
        var right = numbers.length - 1
        while (left < right) {
            val sum = numbers(left) + numbers(right)
            if (sum == target) return Array(left + 1, right + 1)
            else if (sum < target) left += 1
            else right -= 1
        }
        // According to problem constraints, a solution always exists.
        Array.empty[Int]
    }
}
```

## Rust

```rust
impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left = 0usize;
        let mut right = numbers.len() - 1;
        while left < right {
            let sum = numbers[left] + numbers[right];
            if sum == target {
                return vec![(left as i32) + 1, (right as i32) + 1];
            } else if sum < target {
                left += 1;
            } else {
                right -= 1;
            }
        }
        Vec::new()
    }
}
```

## Racket

```racket
(define/contract (two-sum numbers target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let loop ((i 0) (j (- (length numbers) 1)))
    (cond
      [(>= i j) (error "No solution")]
      [else
       (define sum (+ (list-ref numbers i) (list-ref numbers j)))
       (cond
         [(= sum target) (list (+ i 1) (+ j 1))]
         [(< sum target) (loop (+ i 1) j)]
         [else (loop i (- j 1))])])))
```

## Erlang

```erlang
-module(solution).
-export([two_sum/2]).

-spec two_sum(Numbers :: [integer()], Target :: integer()) -> [integer()].
two_sum(Numbers, Target) ->
    Tuple = list_to_tuple(Numbers),
    find_pair(Tuple, 1, tuple_size(Tuple), Target).

find_pair(_Tuple, L, R, _Target) when L >= R ->
    []; % guaranteed solution exists
find_pair(Tuple, L, R, Target) ->
    Sum = element(L, Tuple) + element(R, Tuple),
    case Sum of
        S when S == Target -> [L, R];
        S when S < Target  -> find_pair(Tuple, L + 1, R, Target);
        _                  -> find_pair(Tuple, L, R - 1, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec two_sum(numbers :: [integer], target :: integer) :: [integer]
  def two_sum(numbers, target) do
    do_two_sum(numbers, target, 0, length(numbers) - 1)
  end

  defp do_two_sum(nums, target, left, right) when left < right do
    sum = Enum.at(nums, left) + Enum.at(nums, right)

    cond do
      sum == target -> [left + 1, right + 1]
      sum < target -> do_two_sum(nums, target, left + 1, right)
      true -> do_two_sum(nums, target, left, right - 1)
    end
  end
end
```
