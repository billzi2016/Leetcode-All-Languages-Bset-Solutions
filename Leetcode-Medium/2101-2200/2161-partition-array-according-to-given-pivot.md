# 2161. Partition Array According to Given Pivot

## Cpp

```cpp
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> less;
        vector<int> equal;
        vector<int> greater;
        less.reserve(nums.size());
        equal.reserve(nums.size());
        greater.reserve(nums.size());
        for (int num : nums) {
            if (num < pivot) less.push_back(num);
            else if (num > pivot) greater.push_back(num);
            else equal.push_back(num);
        }
        less.insert(less.end(), equal.begin(), equal.end());
        less.insert(less.end(), greater.begin(), greater.end());
        return less;
    }
};
```

## Java

```java
class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int lessCount = 0, equalCount = 0;
        for (int num : nums) {
            if (num < pivot) {
                lessCount++;
            } else if (num == pivot) {
                equalCount++;
            }
        }
        int[] ans = new int[n];
        int lessIdx = 0;
        int eqIdx = lessCount;
        int greaterIdx = lessCount + equalCount;
        for (int num : nums) {
            if (num < pivot) {
                ans[lessIdx++] = num;
            } else if (num == pivot) {
                ans[eqIdx++] = num;
            } else {
                ans[greaterIdx++] = num;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return less + equal + greater
```

## Python3

```python
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return less + equal + greater
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int *ans = (int*)malloc(numsSize * sizeof(int));
    int idx = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] < pivot) ans[idx++] = nums[i];
    }
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == pivot) ans[idx++] = nums[i];
    }
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > pivot) ans[idx++] = nums[i];
    }
    *returnSize = numsSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] PivotArray(int[] nums, int pivot) {
        var less = new List<int>();
        var equal = new List<int>();
        var greater = new List<int>();
        
        foreach (var num in nums) {
            if (num < pivot) {
                less.Add(num);
            } else if (num == pivot) {
                equal.Add(num);
            } else {
                greater.Add(num);
            }
        }
        
        int[] result = new int[nums.Length];
        int idx = 0;
        foreach (var v in less) result[idx++] = v;
        foreach (var v in equal) result[idx++] = v;
        foreach (var v in greater) result[idx++] = v;
        
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    const less = [];
    const equal = [];
    const greater = [];
    
    for (const num of nums) {
        if (num < pivot) {
            less.push(num);
        } else if (num === pivot) {
            equal.push(num);
        } else {
            greater.push(num);
        }
    }
    
    return less.concat(equal, greater);
};
```

## Typescript

```typescript
function pivotArray(nums: number[], pivot: number): number[] {
    const less: number[] = [];
    const equal: number[] = [];
    const greater: number[] = [];
    for (const num of nums) {
        if (num < pivot) {
            less.push(num);
        } else if (num > pivot) {
            greater.push(num);
        } else {
            equal.push(num);
        }
    }
    return less.concat(equal, greater);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $pivot
     * @return Integer[]
     */
    function pivotArray($nums, $pivot) {
        $less = [];
        $equal = [];
        $greater = [];

        foreach ($nums as $num) {
            if ($num < $pivot) {
                $less[] = $num;
            } elseif ($num > $pivot) {
                $greater[] = $num;
            } else {
                $equal[] = $num;
            }
        }

        // Merge the three parts preserving order
        return array_merge($less, $equal, $greater);
    }
}
```

## Swift

```swift
class Solution {
    func pivotArray(_ nums: [Int], _ pivot: Int) -> [Int] {
        var less = [Int]()
        var equal = [Int]()
        var greater = [Int]()
        
        for num in nums {
            if num < pivot {
                less.append(num)
            } else if num == pivot {
                equal.append(num)
            } else {
                greater.append(num)
            }
        }
        
        return less + equal + greater
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pivotArray(nums: IntArray, pivot: Int): IntArray {
        val less = mutableListOf<Int>()
        val equal = mutableListOf<Int>()
        val greater = mutableListOf<Int>()
        for (num in nums) {
            when {
                num < pivot -> less.add(num)
                num == pivot -> equal.add(num)
                else -> greater.add(num)
            }
        }
        return (less + equal + greater).toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> pivotArray(List<int> nums, int pivot) {
    List<int> less = [];
    List<int> equal = [];
    List<int> greater = [];

    for (int num in nums) {
      if (num < pivot) {
        less.add(num);
      } else if (num == pivot) {
        equal.add(num);
      } else {
        greater.add(num);
      }
    }

    less.addAll(equal);
    less.addAll(greater);
    return less;
  }
}
```

## Golang

```go
func pivotArray(nums []int, pivot int) []int {
	n := len(nums)
	lessCount, equalCount := 0, 0
	for _, v := range nums {
		if v < pivot {
			lessCount++
		} else if v == pivot {
			equalCount++
		}
	}
	ans := make([]int, n)
	lessIdx, equalIdx, greaterIdx := 0, lessCount, lessCount+equalCount
	for _, v := range nums {
		if v < pivot {
			ans[lessIdx] = v
			lessIdx++
		} else if v == pivot {
			ans[equalIdx] = v
			equalIdx++
		} else {
			ans[greaterIdx] = v
			greaterIdx++
		}
	}
	return ans
}
```

## Ruby

```ruby
def pivot_array(nums, pivot)
  less = []
  equal = []
  greater = []

  nums.each do |num|
    if num < pivot
      less << num
    elsif num > pivot
      greater << num
    else
      equal << num
    end
  end

  less + equal + greater
end
```

## Scala

```scala
object Solution {
    def pivotArray(nums: Array[Int], pivot: Int): Array[Int] = {
        val less = scala.collection.mutable.ArrayBuffer[Int]()
        val equal = scala.collection.mutable.ArrayBuffer[Int]()
        val greater = scala.collection.mutable.ArrayBuffer[Int]()

        for (num <- nums) {
            if (num < pivot) less += num
            else if (num == pivot) equal += num
            else greater += num
        }

        val result = new Array[Int](nums.length)
        var idx = 0
        for (v <- less) { result(idx) = v; idx += 1 }
        for (v <- equal) { result(idx) = v; idx += 1 }
        for (v <- greater) { result(idx) = v; idx += 1 }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut less = Vec::new();
        let mut equal = Vec::new();
        let mut greater = Vec::new();

        for num in nums {
            if num < pivot {
                less.push(num);
            } else if num == pivot {
                equal.push(num);
            } else {
                greater.push(num);
            }
        }

        less.extend(equal);
        less.extend(greater);
        less
    }
}
```

## Racket

```racket
(define/contract (pivot-array nums pivot)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let loop ((lst nums) (less '()) (eq '()) (greater '()))
    (if (null? lst)
        (append (reverse less) (reverse eq) (reverse greater))
        (let ((x (car lst)))
          (cond [(< x pivot) (loop (cdr lst) (cons x less) eq greater)]
                [(= x pivot) (loop (cdr lst) less (cons x eq) greater)]
                [else       (loop (cdr lst) less eq (cons x greater))])))))
```

## Erlang

```erlang
-spec pivot_array(Nums :: [integer()], Pivot :: integer()) -> [integer()].
pivot_array(Nums, Pivot) ->
    Less = [X || X <- Nums, X < Pivot],
    Equal = [X || X <- Nums, X == Pivot],
    Greater = [X || X <- Nums, X > Pivot],
    Less ++ Equal ++ Greater.
```

## Elixir

```elixir
defmodule Solution do
  @spec pivot_array(nums :: [integer], pivot :: integer) :: [integer]
  def pivot_array(nums, pivot) do
    less = for x <- nums, x < pivot, do: x
    equal = for x <- nums, x == pivot, do: x
    greater = for x <- nums, x > pivot, do: x
    less ++ equal ++ greater
  end
end
```
