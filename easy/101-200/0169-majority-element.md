# 0169. Majority Element

## Cpp

```cpp
class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        int count = 0, candidate = 0;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (num == candidate) {
                ++count;
            } else {
                --count;
            }
        }
        return candidate;
    }
};
```

## Java

```java
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (candidate == num) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }
}
```

## Python

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
```

## Python3

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
```

## C

```c
int majorityElement(int* nums, int numsSize) {
    int count = 0;
    int candidate = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (count == 0) {
            candidate = nums[i];
            count = 1;
        } else if (nums[i] == candidate) {
            ++count;
        } else {
            --count;
        }
    }
    return candidate;
}
```

## Csharp

```csharp
public class Solution {
    public int MajorityElement(int[] nums) {
        int count = 0;
        int candidate = 0;
        foreach (int num in nums) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = 0;
    let candidate = null;
    for (const num of nums) {
        if (count === 0) {
            candidate = num;
        }
        count += (num === candidate) ? 1 : -1;
    }
    return candidate;
};
```

## Typescript

```typescript
function majorityElement(nums: number[]): number {
    let count = 0;
    let candidate = 0;
    for (const num of nums) {
        if (count === 0) {
            candidate = num;
            count = 1;
        } else if (num === candidate) {
            count++;
        } else {
            count--;
        }
    }
    return candidate;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function majorityElement($nums) {
        $count = 0;
        $candidate = null;
        foreach ($nums as $num) {
            if ($count == 0) {
                $candidate = $num;
                $count = 1;
            } else {
                $count += ($num == $candidate) ? 1 : -1;
            }
        }
        return $candidate;
    }
}
```

## Swift

```swift
class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var count = 0
        var candidate = 0
        for num in nums {
            if count == 0 {
                candidate = num
            }
            count += (num == candidate) ? 1 : -1
        }
        return candidate
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun majorityElement(nums: IntArray): Int {
        var count = 0
        var candidate = 0
        for (num in nums) {
            if (count == 0) {
                candidate = num
                count = 1
            } else if (candidate == num) {
                count++
            } else {
                count--
            }
        }
        return candidate
    }
}
```

## Dart

```dart
class Solution {
  int majorityElement(List<int> nums) {
    int count = 0;
    int candidate = 0;
    for (int num in nums) {
      if (count == 0) {
        candidate = num;
        count = 1;
      } else if (num == candidate) {
        count++;
      } else {
        count--;
      }
    }
    return candidate;
  }
}
```

## Golang

```go
func majorityElement(nums []int) int {
    count := 0
    candidate := 0
    for _, num := range nums {
        if count == 0 {
            candidate = num
        }
        if num == candidate {
            count++
        } else {
            count--
        }
    }
    return candidate
}
```

## Ruby

```ruby
def majority_element(nums)
  count = 0
  candidate = nil
  nums.each do |num|
    if count == 0
      candidate = num
      count = 1
    elsif num == candidate
      count += 1
    else
      count -= 1
    end
  end
  candidate
end
```

## Scala

```scala
object Solution {
    def majorityElement(nums: Array[Int]): Int = {
        var count = 0
        var candidate = 0
        for (num <- nums) {
            if (count == 0) {
                candidate = num
                count = 1
            } else if (candidate == num) {
                count += 1
            } else {
                count -= 1
            }
        }
        candidate
    }
}
```

## Rust

```rust
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count = 0;
        let mut candidate = 0;
        for num in nums {
            if count == 0 {
                candidate = num;
                count = 1;
            } else if num == candidate {
                count += 1;
            } else {
                count -= 1;
            }
        }
        candidate
    }
}
```

## Racket

```racket
(define/contract (majority-element nums)
  (-> (listof exact-integer?) exact-integer?)
  (let-values ([(candidate _)
                (for/fold ([candidate #f] [count 0]) ([x nums])
                  (if (= count 0)
                      (values x 1)
                      (if (= x candidate)
                          (values candidate (+ count 1))
                          (values candidate (- count 1)))) )])
    candidate))
```

## Erlang

```erlang
-spec majority_element(Nums :: [integer()]) -> integer().
majority_element(Nums) ->
    {Candidate,_} = lists:foldl(
        fun(N, {Cand, Count}) ->
            case Count of
                0 -> {N,1};
                _ when N =:= Cand -> {Cand, Count+1};
                _ -> {Cand, Count-1}
            end
        end,
        {undefined,0},
        Nums),
    Candidate.
```

## Elixir

```elixir
defmodule Solution do
  @spec majority_element(nums :: [integer]) :: integer
  def majority_element(nums) do
    {candidate, _} =
      Enum.reduce(nums, {nil, 0}, fn x, {cand, cnt} ->
        cond do
          cnt == 0 -> {x, 1}
          x == cand -> {cand, cnt + 1}
          true -> {cand, cnt - 1}
        end
      end)

    candidate
  end
end
```
