# 0442. Find All Duplicates in an Array

## Cpp

```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;
        for (int i = 0; i < (int)nums.size(); ++i) {
            int idx = abs(nums[i]) - 1;
            if (nums[idx] < 0) {
                result.push_back(idx + 1);
            } else {
                nums[idx] = -nums[idx];
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> duplicates = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            if (nums[index] < 0) {
                duplicates.add(index + 1);
            } else {
                nums[index] = -nums[index];
            }
        }
        return duplicates;
    }
}
```

## Python

```python
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(idx + 1)
            else:
                nums[idx] = -nums[idx]
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(idx + 1)
            else:
                nums[idx] = -nums[idx]
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDuplicates(int* nums, int numsSize, int* returnSize) {
    int *result = (int*)malloc(numsSize * sizeof(int));
    int count = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val < 0) val = -val;
        int idx = val - 1;
        
        if (nums[idx] < 0) {
            result[count++] = val;
        } else {
            nums[idx] = -nums[idx];
        }
    }
    
    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        var result = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            int index = Math.Abs(nums[i]) - 1;
            if (nums[index] < 0) {
                result.Add(index + 1);
            } else {
                nums[index] = -nums[index];
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    const result = [];
    for (let i = 0; i < nums.length; i++) {
        const idx = Math.abs(nums[i]) - 1;
        if (nums[idx] < 0) {
            result.push(idx + 1);
        } else {
            nums[idx] = -nums[idx];
        }
    }
    return result;
};
```

## Typescript

```typescript
function findDuplicates(nums: number[]): number[] {
    const result: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        const idx = Math.abs(nums[i]) - 1;
        if (nums[idx] < 0) {
            result.push(idx + 1);
        } else {
            nums[idx] = -nums[idx];
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findDuplicates($nums) {
        $result = [];
        foreach ($nums as $i => $val) {
            $index = abs($val) - 1;
            if ($nums[$index] < 0) {
                $result[] = $index + 1;
            } else {
                $nums[$index] = -$nums[$index];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findDuplicates(_ nums: [Int]) -> [Int] {
        var arr = nums
        var result = [Int]()
        for i in 0..<arr.count {
            let val = abs(arr[i])
            let index = val - 1
            if arr[index] < 0 {
                result.append(val)
            } else {
                arr[index] = -arr[index]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDuplicates(nums: IntArray): List<Int> {
        val result = mutableListOf<Int>()
        for (i in nums.indices) {
            val index = kotlin.math.abs(nums[i]) - 1
            if (nums[index] < 0) {
                result.add(index + 1)
            } else {
                nums[index] = -nums[index]
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findDuplicates(List<int> nums) {
    List<int> result = [];
    for (int i = 0; i < nums.length; i++) {
      int val = nums[i].abs();
      int idx = val - 1;
      if (nums[idx] < 0) {
        result.add(val);
      } else {
        nums[idx] = -nums[idx];
      }
    }
    return result;
  }
}
```

## Golang

```go
func findDuplicates(nums []int) []int {
    var result []int
    for _, v := range nums {
        idx := abs(v) - 1
        if nums[idx] < 0 {
            result = append(result, idx+1)
        } else {
            nums[idx] = -nums[idx]
        }
    }
    return result
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
```

## Ruby

```ruby
def find_duplicates(nums)
  result = []
  nums.each do |num|
    idx = num.abs - 1
    if nums[idx] < 0
      result << num.abs
    else
      nums[idx] = -nums[idx]
    end
  end
  result
end
```

## Scala

```scala
import scala.collection.mutable.ListBuffer

object Solution {
  def findDuplicates(nums: Array[Int]): List[Int] = {
    val duplicates = ListBuffer[Int]()
    var i = 0
    while (i < nums.length) {
      val idx = math.abs(nums(i)) - 1
      if (nums(idx) < 0) {
        duplicates += idx + 1
      } else {
        nums(idx) = -nums(idx)
      }
      i += 1
    }
    duplicates.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_duplicates(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        let mut res = Vec::new();
        for i in 0..nums.len() {
            let idx = (nums[i].abs() - 1) as usize;
            if nums[idx] > 0 {
                nums[idx] = -nums[idx];
            } else {
                res.push(idx as i32 + 1);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (find-duplicates nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((lst nums) (seen (make-hash)) (dup '()))
    (cond
      [(null? lst) (reverse dup)]
      [else
       (define x (car lst))
       (if (hash-has-key? seen x)
           (loop (cdr lst) seen (cons x dup))
           (begin (hash-set! seen x #t) (loop (cdr lst) seen dup)))])))
```

## Erlang

```erlang
-spec find_duplicates(Nums :: [integer()]) -> [integer()].
find_duplicates(Nums) ->
    CountMap = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Nums
    ),
    Dups = [K || {K, V} <- maps:to_list(CountMap), V == 2],
    lists:sort(Dups).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_duplicates(nums :: [integer]) :: [integer]
  def find_duplicates(nums) do
    nums
    |> Enum.frequencies()
    |> Enum.filter(fn {_k, v} -> v == 2 end)
    |> Enum.map(&elem(&1, 0))
    |> Enum.sort()
  end
end
```
