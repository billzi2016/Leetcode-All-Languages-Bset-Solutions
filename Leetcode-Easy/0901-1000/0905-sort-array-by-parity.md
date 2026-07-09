# 0905. Sort Array By Parity

## Cpp

```cpp
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int i = 0, j = (int)nums.size() - 1;
        while (i < j) {
            if (nums[i] % 2 == 0) {
                ++i;
            } else if (nums[j] % 2 == 1) {
                --j;
            } else {
                swap(nums[i], nums[j]);
                ++i;
                --j;
            }
        }
        return nums;
    }
};
```

## Java

```java
class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            if ((nums[left] & 1) == 0) {
                left++;
            } else if ((nums[right] & 1) == 1) {
                right--;
            } else {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            }
        }
        return nums;
    }
}
```

## Python

```python
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]
        return evens + odds
```

## Python3

```python
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return nums
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int *result = (int *)malloc(numsSize * sizeof(int));
    if (!result) {
        *returnSize = 0;
        return NULL;
    }
    
    int idx = 0;
    // First, place even numbers
    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & 1) == 0) { // even
            result[idx++] = nums[i];
        }
    }
    // Then, place odd numbers
    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & 1) != 0) { // odd
            result[idx++] = nums[i];
        }
    }
    
    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] SortArrayByParity(int[] nums)
    {
        int left = 0, right = nums.Length - 1;
        while (left < right)
        {
            if ((nums[left] & 1) == 0)
            {
                left++;
                continue;
            }
            if ((nums[right] & 1) == 1)
            {
                right--;
                continue;
            }
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
        return nums;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    let i = 0, j = nums.length - 1;
    while (i < j) {
        if (nums[i] % 2 === 0) {
            i++;
            continue;
        }
        if (nums[j] % 2 === 1) {
            j--;
            continue;
        }
        // swap even at j with odd at i
        [nums[i], nums[j]] = [nums[j], nums[i]];
        i++;
        j--;
    }
    return nums;
};
```

## Typescript

```typescript
function sortArrayByParity(nums: number[]): number[] {
    let i = 0;
    let j = nums.length - 1;
    while (i < j) {
        if (nums[i] % 2 === 0) {
            i++;
        } else {
            while (i < j && nums[j] % 2 !== 0) {
                j--;
            }
            if (i < j) {
                const temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--;
            }
        }
    }
    return nums;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortArrayByParity($nums) {
        $i = 0;
        $j = count($nums) - 1;
        while ($i < $j) {
            if ($nums[$i] % 2 == 0) {
                $i++;
            } elseif ($nums[$j] % 2 == 1) {
                $j--;
            } else {
                $tmp = $nums[$i];
                $nums[$i] = $nums[$j];
                $nums[$j] = $tmp;
                $i++;
                $j--;
            }
        }
        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func sortArrayByParity(_ nums: [Int]) -> [Int] {
        var result = Array(repeating: 0, count: nums.count)
        var left = 0
        var right = nums.count - 1
        
        for num in nums {
            if num % 2 == 0 {
                result[left] = num
                left += 1
            } else {
                result[right] = num
                right -= 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortArrayByParity(nums: IntArray): IntArray {
        var i = 0
        var j = nums.lastIndex
        while (i < j) {
            if (nums[i] % 2 == 0) {
                i++
            } else if (nums[j] % 2 != 0) {
                j--
            } else {
                val tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i++
                j--
            }
        }
        return nums
    }
}
```

## Dart

```dart
class Solution {
  List<int> sortArrayByParity(List<int> nums) {
    int i = 0;
    int j = nums.length - 1;
    while (i < j) {
      if (nums[i] % 2 == 0) {
        i++;
      } else if (nums[j] % 2 == 1) {
        j--;
      } else {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        i++;
        j--;
      }
    }
    return nums;
  }
}
```

## Golang

```go
func sortArrayByParity(nums []int) []int {
    i, j := 0, len(nums)-1
    for i < j {
        if nums[i]%2 == 0 {
            i++
        } else if nums[j]%2 == 1 {
            j--
        } else {
            nums[i], nums[j] = nums[j], nums[i]
            i++
            j--
        }
    }
    return nums
}
```

## Ruby

```ruby
def sort_array_by_parity(nums)
  i = 0
  j = nums.length - 1
  while i < j
    if nums[i].even?
      i += 1
    elsif nums[j].odd?
      j -= 1
    else
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
      j -= 1
    end
  end
  nums
end
```

## Scala

```scala
object Solution {
    def sortArrayByParity(nums: Array[Int]): Array[Int] = {
        val evens = nums.filter(_ % 2 == 0)
        val odds = nums.filter(_ % 2 != 0)
        evens ++ odds
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_array_by_parity(nums: Vec<i32>) -> Vec<i32> {
        let mut arr = nums;
        if arr.is_empty() {
            return arr;
        }
        let mut i = 0usize;
        let mut j = arr.len() - 1;
        while i < j {
            if arr[i] % 2 == 0 {
                i += 1;
            } else {
                arr.swap(i, j);
                if j == 0 { break; }
                j -= 1;
            }
        }
        arr
    }
}
```

## Racket

```racket
(define/contract (sort-array-by-parity nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (append (filter even? nums) (filter odd? nums)))
```

## Erlang

```erlang
-module(solution).
-export([sort_array_by_parity/1]).

-spec sort_array_by_parity(Nums :: [integer()]) -> [integer()].
sort_array_by_parity(Nums) ->
    Evens = [X || X <- Nums, X rem 2 == 0],
    Odds = [X || X <- Nums, X rem 2 == 1],
    Evens ++ Odds.
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_array_by_parity(nums :: [integer]) :: [integer]
  def sort_array_by_parity(nums) do
    evens = Enum.filter(nums, fn x -> rem(x, 2) == 0 end)
    odds = Enum.filter(nums, fn x -> rem(x, 2) == 1 end)
    evens ++ odds
  end
end
```
