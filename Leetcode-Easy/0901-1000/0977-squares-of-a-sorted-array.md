# 0977. Squares of a Sorted Array

## Cpp

```cpp
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        int left = 0, right = n - 1;
        for (int i = n - 1; i >= 0; --i) {
            if (abs(nums[left]) > abs(nums[right])) {
                result[i] = nums[left] * nums[left];
                ++left;
            } else {
                result[i] = nums[right] * nums[right];
                --right;
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int left = 0, right = n - 1;
        for (int i = n - 1; i >= 0; i--) {
            if (Math.abs(nums[left]) > Math.abs(nums[right])) {
                result[i] = nums[left] * nums[left];
                left++;
            } else {
                result[i] = nums[right] * nums[right];
                right--;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] * nums[left]
                left += 1
            else:
                res[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int *res = (int*)malloc(numsSize * sizeof(int));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    int left = 0, right = numsSize - 1;
    for (int i = numsSize - 1; i >= 0; --i) {
        int lval = nums[left];
        int rval = nums[right];
        if (abs(lval) > abs(rval)) {
            res[i] = lval * lval;
            ++left;
        } else {
            res[i] = rval * rval;
            --right;
        }
    }
    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SortedSquares(int[] nums) {
        int n = nums.Length;
        int[] res = new int[n];
        int left = 0, right = n - 1, pos = n - 1;
        while (left <= right) {
            long leftSq = (long)nums[left] * nums[left];
            long rightSq = (long)nums[right] * nums[right];
            if (rightSq > leftSq) {
                res[pos--] = (int)rightSq;
                right--;
            } else {
                res[pos--] = (int)leftSq;
                left++;
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    const n = nums.length;
    const result = new Array(n);
    let left = 0, right = n - 1, pos = n - 1;
    
    while (left <= right) {
        const leftVal = Math.abs(nums[left]);
        const rightVal = Math.abs(nums[right]);
        if (leftVal > rightVal) {
            result[pos] = leftVal * leftVal;
            left++;
        } else {
            result[pos] = rightVal * rightVal;
            right--;
        }
        pos--;
    }
    
    return result;
};
```

## Typescript

```typescript
function sortedSquares(nums: number[]): number[] {
    const n = nums.length;
    const result = new Array<number>(n);
    let left = 0, right = n - 1;
    for (let i = n - 1; i >= 0; i--) {
        if (Math.abs(nums[left]) > Math.abs(nums[right])) {
            result[i] = nums[left] * nums[left];
            left++;
        } else {
            result[i] = nums[right] * nums[right];
            right--;
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
    function sortedSquares($nums) {
        $n = count($nums);
        $result = array_fill(0, $n, 0);
        $left = 0;
        $right = $n - 1;
        $pos = $n - 1;

        while ($left <= $right) {
            $lVal = $nums[$left];
            $rVal = $nums[$right];

            if (abs($lVal) > abs($rVal)) {
                $result[$pos] = $lVal * $lVal;
                $left++;
            } else {
                $result[$pos] = $rVal * $rVal;
                $right--;
            }
            $pos--;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        var left = 0
        var right = nums.count - 1
        var result = Array(repeating: 0, count: nums.count)
        var pos = nums.count - 1
        
        while left <= right {
            let leftSq = nums[left] * nums[left]
            let rightSq = nums[right] * nums[right]
            if leftSq > rightSq {
                result[pos] = leftSq
                left += 1
            } else {
                result[pos] = rightSq
                right -= 1
            }
            pos -= 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortedSquares(nums: IntArray): IntArray {
        val n = nums.size
        val result = IntArray(n)
        var left = 0
        var right = n - 1
        var idx = n - 1
        while (left <= right) {
            val leftVal = nums[left]
            val rightVal = nums[right]
            val leftSq = leftVal * leftVal
            val rightSq = rightVal * rightVal
            if (leftSq > rightSq) {
                result[idx] = leftSq
                left++
            } else {
                result[idx] = rightSq
                right--
            }
            idx--
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> sortedSquares(List<int> nums) {
    int n = nums.length;
    List<int> result = List.filled(n, 0);
    int left = 0, right = n - 1, pos = n - 1;

    while (left <= right) {
      int leftVal = nums[left];
      int rightVal = nums[right];
      if (leftVal.abs() > rightVal.abs()) {
        result[pos] = leftVal * leftVal;
        left++;
      } else {
        result[pos] = rightVal * rightVal;
        right--;
      }
      pos--;
    }

    return result;
  }
}
```

## Golang

```go
func sortedSquares(nums []int) []int {
	n := len(nums)
	res := make([]int, n)
	left, right := 0, n-1
	pos := n - 1
	for left <= right {
		if nums[left]*nums[left] > nums[right]*nums[right] {
			res[pos] = nums[left] * nums[left]
			left++
		} else {
			res[pos] = nums[right] * nums[right]
			right--
		}
		pos--
	}
	return res
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def sorted_squares(nums)
  n = nums.length
  left = 0
  right = n - 1
  result = Array.new(n)
  idx = n - 1

  while left <= right
    l_sq = nums[left] * nums[left]
    r_sq = nums[right] * nums[right]

    if l_sq > r_sq
      result[idx] = l_sq
      left += 1
    else
      result[idx] = r_sq
      right -= 1
    end

    idx -= 1
  end

  result
end
```

## Scala

```scala
object Solution {
    def sortedSquares(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val result = new Array[Int](n)
        var left = 0
        var right = n - 1
        var pos = n - 1

        while (left <= right) {
            val leftSq = nums(left) * nums(left)
            val rightSq = nums(right) * nums(right)

            if (leftSq > rightSq) {
                result(pos) = leftSq
                left += 1
            } else {
                result(pos) = rightSq
                right -= 1
            }
            pos -= 1
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = vec![0i32; n];
        let (mut left, mut right) = (0usize, n - 1);
        let mut pos = n;
        while left <= right {
            let left_sq = nums[left] * nums[left];
            let right_sq = nums[right] * nums[right];
            if left_sq > right_sq {
                res[pos - 1] = left_sq;
                left += 1;
            } else {
                res[pos - 1] = right_sq;
                if right == 0 {
                    break;
                }
                right -= 1;
            }
            pos -= 1;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (sorted-squares nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let loop ([l 0] [r (sub1 n)] [i (sub1 n)] [out (make-vector n)])
      (if (> l r)
          (vector->list out)
          (let* ([left (vector-ref v l)]
                 [right (vector-ref v r)]
                 [lsq (* left left)]
                 [rsq (* right right)])
            (if (>= lsq rsq)
                (begin
                  (vector-set! out i lsq)
                  (loop (+ l 1) r (- i 1) out))
                (begin
                  (vector-set! out i rsq)
                  (loop l (- r 1) (- i 1) out))))))))
```

## Erlang

```erlang
-spec sorted_squares(Nums :: [integer()]) -> [integer()].
sorted_squares(Nums) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    reverse_build(Tuple, 1, N, []).

reverse_build(_Tuple, L, R, Acc) when L > R ->
    lists:reverse(Acc);
reverse_build(Tuple, L, R, Acc) ->
    LeftVal = element(L, Tuple),
    RightVal = element(R, Tuple),
    LSq = LeftVal * LeftVal,
    RSq = RightVal * RightVal,
    if
        LSq > RSq ->
            reverse_build(Tuple, L + 1, R, [LSq | Acc]);
        true ->
            reverse_build(Tuple, L, R - 1, [RSq | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sorted_squares(nums :: [integer]) :: [integer]
  def sorted_squares(nums) do
    nums
    |> Enum.map(&(&1 * &1))
    |> Enum.sort()
  end
end
```
