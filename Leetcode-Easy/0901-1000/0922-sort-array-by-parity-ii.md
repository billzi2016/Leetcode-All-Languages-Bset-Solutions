# 0922. Sort Array By Parity II

## Cpp

```cpp
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int n = nums.size();
        int i = 0, j = 1;
        while (i < n && j < n) {
            if ((nums[i] & 1) == 0) { // even at even index
                i += 2;
                continue;
            }
            if ((nums[j] & 1) == 1) { // odd at odd index
                j += 2;
                continue;
            }
            swap(nums[i], nums[j]);
            i += 2;
            j += 2;
        }
        return nums;
    }
};
```

## Java

```java
class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int n = nums.length;
        int evenIdx = 0, oddIdx = 1;
        while (evenIdx < n && oddIdx < n) {
            if ((nums[evenIdx] & 1) == 0) {
                evenIdx += 2;
                continue;
            }
            if ((nums[oddIdx] & 1) == 1) {
                oddIdx += 2;
                continue;
            }
            // swap mismatched pair
            int temp = nums[evenIdx];
            nums[evenIdx] = nums[oddIdx];
            nums[oddIdx] = temp;
            evenIdx += 2;
            oddIdx += 2;
        }
        return nums;
    }
}
```

## Python

```python
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        n = len(nums)
        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 == 1:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
```

## Python3

```python
from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        n = len(nums)
        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
                continue
            if nums[j] % 2 == 1:
                j += 2
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
        return nums
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParityII(int* nums, int numsSize, int* returnSize) {
    int *res = (int *)malloc(numsSize * sizeof(int));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    *returnSize = numsSize;
    int evenIdx = 0; // positions for even numbers
    int oddIdx = 1;  // positions for odd numbers

    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & 1) == 0) {          // even number
            res[evenIdx] = nums[i];
            evenIdx += 2;
        } else {                           // odd number
            res[oddIdx] = nums[i];
            oddIdx += 2;
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SortArrayByParityII(int[] nums) {
        int n = nums.Length;
        int[] result = new int[n];
        int evenIdx = 0, oddIdx = 1;
        foreach (int num in nums) {
            if ((num & 1) == 0) {
                result[evenIdx] = num;
                evenIdx += 2;
            } else {
                result[oddIdx] = num;
                oddIdx += 2;
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
var sortArrayByParityII = function(nums) {
    let i = 0, j = 1;
    const n = nums.length;
    while (i < n && j < n) {
        while (i < n && nums[i] % 2 === 0) i += 2;
        while (j < n && nums[j] % 2 === 1) j += 2;
        if (i < n && j < n) {
            const temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i += 2;
            j += 2;
        }
    }
    return nums;
};
```

## Typescript

```typescript
function sortArrayByParityII(nums: number[]): number[] {
    const n = nums.length;
    const res = new Array<number>(n);
    let evenIdx = 0;
    let oddIdx = 1;
    for (const num of nums) {
        if ((num & 1) === 0) { // even
            res[evenIdx] = num;
            evenIdx += 2;
        } else { // odd
            res[oddIdx] = num;
            oddIdx += 2;
        }
    }
    return res;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortArrayByParityII($nums) {
        $n = count($nums);
        $i = 0; // even index pointer
        $j = 1; // odd index pointer
        while ($i < $n && $j < $n) {
            if ($nums[$i] % 2 == 0) {
                $i += 2;
                continue;
            }
            if ($nums[$j] % 2 == 1) {
                $j += 2;
                continue;
            }
            // swap misplaced elements
            $tmp = $nums[$i];
            $nums[$i] = $nums[$j];
            $nums[$j] = $tmp;
            $i += 2;
            $j += 2;
        }
        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func sortArrayByParityII(_ nums: [Int]) -> [Int] {
        var evens = [Int]()
        var odds = [Int]()
        for num in nums {
            if num % 2 == 0 {
                evens.append(num)
            } else {
                odds.append(num)
            }
        }
        var result = Array(repeating: 0, count: nums.count)
        var eIdx = 0
        var oIdx = 0
        for i in 0..<nums.count {
            if i % 2 == 0 {
                result[i] = evens[eIdx]
                eIdx += 1
            } else {
                result[i] = odds[oIdx]
                oIdx += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortArrayByParityII(nums: IntArray): IntArray {
        var i = 0
        var j = 1
        val n = nums.size
        while (i < n && j < n) {
            if (nums[i] % 2 == 0) {
                i += 2
            } else if (nums[j] % 2 == 1) {
                j += 2
            } else {
                val tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 2
                j += 2
            }
        }
        return nums
    }
}
```

## Dart

```dart
class Solution {
  List<int> sortArrayByParityII(List<int> nums) {
    int n = nums.length;
    int i = 0; // even index
    int j = 1; // odd index
    while (i < n && j < n) {
      while (i < n && nums[i] % 2 == 0) i += 2;
      while (j < n && nums[j] % 2 == 1) j += 2;
      if (i < n && j < n) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        i += 2;
        j += 2;
      }
    }
    return nums;
  }
}
```

## Golang

```go
func sortArrayByParityII(nums []int) []int {
	n := len(nums)
	i, j := 0, 1
	for i < n && j < n {
		for i < n && nums[i]%2 == 0 {
			i += 2
		}
		for j < n && nums[j]%2 == 1 {
			j += 2
		}
		if i < n && j < n {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	return nums
}
```

## Ruby

```ruby
def sort_array_by_parity_ii(nums)
  i = 0
  j = 1
  n = nums.length
  while i < n && j < n
    if nums[i].even?
      i += 2
    elsif nums[j].odd?
      j += 2
    else
      nums[i], nums[j] = nums[j], nums[i]
      i += 2
      j += 2
    end
  end
  nums
end
```

## Scala

```scala
object Solution {
    def sortArrayByParityII(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val result = new Array[Int](n)
        var evenIdx = 0
        var oddIdx = 1
        for (num <- nums) {
            if ((num & 1) == 0) {
                result(evenIdx) = num
                evenIdx += 2
            } else {
                result(oddIdx) = num
                oddIdx += 2
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_array_by_parity_ii(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut i = 0usize; // even index
        let mut j = 1usize; // odd index
        while i < n && j < n {
            while i < n && nums[i] % 2 == 0 {
                i += 2;
            }
            while j < n && nums[j] % 2 != 0 {
                j += 2;
            }
            if i < n && j < n {
                nums.swap(i, j);
                i += 2;
                j += 2;
            }
        }
        nums
    }
}
```

## Racket

```racket
(define/contract (sort-array-by-parity-ii nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((evens (filter even? nums))
         (odds  (filter odd? nums))
         (n     (length nums)))
    (let build ((i 0) (e evens) (o odds) (acc '()))
      (if (= i n)
          (reverse acc)
          (if (even? i)
              (build (+ i 1) (cdr e) o (cons (car e) acc))
              (build (+ i 1) e (cdr o) (cons (car o) acc)))))))
```

## Erlang

```erlang
-spec sort_array_by_parity_ii(Nums :: [integer()]) -> [integer()].
sort_array_by_parity_ii(Nums) ->
    {Evens, Odds} = split(Nums, [], []),
    interleave(Evens, Odds, []).

split([], EvAcc, OdAcc) ->
    {lists:reverse(EvAcc), lists:reverse(OdAcc)};
split([H|T], EvAcc, OdAcc) ->
    case H rem 2 of
        0 -> split(T, [H|EvAcc], OdAcc);
        _ -> split(T, EvAcc, [H|OdAcc])
    end.

interleave([], [], Acc) ->
    lists:reverse(Acc);
interleave([E|Es], [O|Os], Acc) ->
    interleave(Es, Os, [O,E|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_array_by_parity_ii(nums :: [integer]) :: [integer]
  def sort_array_by_parity_ii(nums) do
    {evens, odds} = Enum.split_with(nums, fn x -> rem(x, 2) == 0 end)
    len = length(nums)

    {_e, _o, rev_res} =
      Enum.reduce(0..(len - 1), {evens, odds, []}, fn i, {es, os, acc} ->
        if rem(i, 2) == 0 do
          [e | rest_es] = es
          {rest_es, os, [e | acc]}
        else
          [o | rest_os] = os
          {es, rest_os, [o | acc]}
        end
      end)

    Enum.reverse(rev_res)
  end
end
```
