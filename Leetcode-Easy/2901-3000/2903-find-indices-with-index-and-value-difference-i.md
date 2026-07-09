# 2903. Find Indices With Index and Value Difference I

## Cpp

```cpp
class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (abs(i - j) >= indexDifference && abs(nums[i] - nums[j]) >= valueDifference) {
                    return {i, j};
                }
            }
        }
        return {-1, -1};
    }
};
```

## Java

```java
class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Math.abs(i - j) >= indexDifference && Math.abs(nums[i] - nums[j]) >= valueDifference) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{-1, -1};
    }
}
```

## Python

```python
class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
```

## Python3

```python
from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
```

## C

```c
#include <stdlib.h>

int* findIndices(int* nums, int numsSize, int indexDifference, int valueDifference, int* returnSize) {
    int *ans = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = 0; j < numsSize; ++j) {
            if (abs(i - j) >= indexDifference && abs(nums[i] - nums[j]) >= valueDifference) {
                ans[0] = i;
                ans[1] = j;
                return ans;
            }
        }
    }
    ans[0] = -1;
    ans[1] = -1;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindIndices(int[] nums, int indexDifference, int valueDifference) {
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Math.Abs(i - j) >= indexDifference && Math.Abs(nums[i] - nums[j]) >= valueDifference) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] { -1, -1 };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} indexDifference
 * @param {number} valueDifference
 * @return {number[]}
 */
var findIndices = function(nums, indexDifference, valueDifference) {
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (Math.abs(i - j) >= indexDifference && Math.abs(nums[i] - nums[j]) >= valueDifference) {
                return [i, j];
            }
        }
    }
    return [-1, -1];
};
```

## Typescript

```typescript
function findIndices(nums: number[], indexDifference: number, valueDifference: number): number[] {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (Math.abs(i - j) >= indexDifference && Math.abs(nums[i] - nums[j]) >= valueDifference) {
                return [i, j];
            }
        }
    }
    return [-1, -1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $indexDifference
     * @param Integer $valueDifference
     * @return Integer[]
     */
    function findIndices($nums, $indexDifference, $valueDifference) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if (abs($i - $j) >= $indexDifference && abs($nums[$i] - $nums[$j]) >= $valueDifference) {
                    return [$i, $j];
                }
            }
        }
        return [-1, -1];
    }
}
```

## Swift

```swift
class Solution {
    func findIndices(_ nums: [Int], _ indexDifference: Int, _ valueDifference: Int) -> [Int] {
        let n = nums.count
        for i in 0..<n {
            for j in 0..<n {
                if abs(i - j) >= indexDifference && abs(nums[i] - nums[j]) >= valueDifference {
                    return [i, j]
                }
            }
        }
        return [-1, -1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findIndices(nums: IntArray, indexDifference: Int, valueDifference: Int): IntArray {
        val n = nums.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (kotlin.math.abs(i - j) >= indexDifference &&
                    kotlin.math.abs(nums[i] - nums[j]) >= valueDifference) {
                    return intArrayOf(i, j)
                }
            }
        }
        return intArrayOf(-1, -1)
    }
}
```

## Dart

```dart
class Solution {
  List<int> findIndices(List<int> nums, int indexDifference, int valueDifference) {
    int n = nums.length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if ((i - j).abs() >= indexDifference &&
            (nums[i] - nums[j]).abs() >= valueDifference) {
          return [i, j];
        }
      }
    }
    return [-1, -1];
  }
}
```

## Golang

```go
func findIndices(nums []int, indexDifference int, valueDifference int) []int {
	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}
	n := len(nums)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if abs(i-j) >= indexDifference && abs(nums[i]-nums[j]) >= valueDifference {
				return []int{i, j}
			}
		}
	}
	return []int{-1, -1}
}
```

## Ruby

```ruby
def find_indices(nums, index_difference, value_difference)
  n = nums.length
  (0...n).each do |i|
    (0...n).each do |j|
      if (i - j).abs >= index_difference && (nums[i] - nums[j]).abs >= value_difference
        return [i, j]
      end
    end
  end
  [-1, -1]
end
```

## Scala

```scala
object Solution {
    def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
        val n = nums.length
        for (i <- 0 until n) {
            for (j <- 0 until n) {
                if (math.abs(i - j) >= indexDifference && math.abs(nums(i) - nums(j)) >= valueDifference) {
                    return Array(i, j)
                }
            }
        }
        Array(-1, -1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        let n = nums.len();
        for i in 0..n {
            for j in 0..n {
                let idx_diff = (i as i32 - j as i32).abs();
                let val_diff = (nums[i] - nums[j]).abs();
                if idx_diff >= index_difference && val_diff >= value_difference {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![-1, -1]
    }
}
```

## Racket

```racket
(define/contract (find-indices nums indexDifference valueDifference)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let ((n (length nums)))
    (let loop-i ((i 0))
      (if (>= i n)
          (list -1 -1)
          (let inner-loop ((j 0))
            (cond
              [(>= j n) (loop-i (add1 i))]
              [else
               (if (and (>= (abs (- i j)) indexDifference)
                        (>= (abs (- (list-ref nums i) (list-ref nums j))) valueDifference))
                   (list i j)
                   (inner-loop (add1 j)))]))))))
```

## Erlang

```erlang
-spec find_indices(Nums :: [integer()], IndexDifference :: integer(), ValueDifference :: integer()) -> [integer()].
find_indices(Nums, IndexDifference, ValueDifference) ->
    Len = length(Nums),
    find_i(0, Len, Nums, IndexDifference, ValueDifference).

find_i(I, Len, _Nums, _IndexDiff, _ValueDiff) when I >= Len ->
    [-1, -1];
find_i(I, Len, Nums, IndexDiff, ValueDiff) ->
    case find_j(I, 0, Len, Nums, IndexDiff, ValueDiff) of
        {ok, J} -> [I, J];
        not_found -> find_i(I + 1, Len, Nums, IndexDiff, ValueDiff)
    end.

find_j(_I, J, Len, _Nums, _IndexDiff, _ValueDiff) when J >= Len ->
    not_found;
find_j(I, J, Len, Nums, IndexDiff, ValueDiff) ->
    AbsIdx = erlang:abs(I - J),
    if
        AbsIdx >= IndexDiff,
        (erlang:abs(lists:nth(I + 1, Nums) - lists:nth(J + 1, Nums)) >= ValueDiff) ->
            {ok, J};
        true ->
            find_j(I, J + 1, Len, Nums, IndexDiff, ValueDiff)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_indices(nums :: [integer], index_difference :: integer, value_difference :: integer) :: [integer]
  def find_indices(nums, index_difference, value_difference) do
    len = length(nums)

    result =
      Enum.reduce_while(0..len - 1, nil, fn i, _ ->
        Enum.reduce_while(0..len - 1, nil, fn j, _ ->
          if abs(i - j) >= index_difference and
               abs(Enum.at(nums, i) - Enum.at(nums, j)) >= value_difference do
            {:halt, [i, j]}
          else
            {:cont, nil}
          end
        end)
        |> case do
          nil -> {:cont, nil}
          pair -> {:halt, pair}
        end
      end)

    case result do
      nil -> [-1, -1]
      pair -> pair
    end
  end
end
```
