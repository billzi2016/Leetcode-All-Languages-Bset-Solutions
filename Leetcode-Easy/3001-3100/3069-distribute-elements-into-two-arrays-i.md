# 3069. Distribute Elements Into Two Arrays I

## Cpp

```cpp
class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        vector<int> arr1, arr2;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (i == 0) {
                arr1.push_back(nums[i]);
            } else if (i == 1) {
                arr2.push_back(nums[i]);
            } else {
                if (arr1.back() > arr2.back())
                    arr1.push_back(nums[i]);
                else
                    arr2.push_back(nums[i]);
            }
        }
        vector<int> result;
        result.reserve(n);
        result.insert(result.end(), arr1.begin(), arr1.end());
        result.insert(result.end(), arr2.begin(), arr2.end());
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] resultArray(int[] nums) {
        int n = nums.length;
        java.util.List<Integer> arr1 = new java.util.ArrayList<>();
        java.util.List<Integer> arr2 = new java.util.ArrayList<>();
        
        if (n == 0) return new int[0];
        arr1.add(nums[0]);
        if (n > 1) {
            arr2.add(nums[1]);
        }
        for (int i = 2; i < n; i++) {
            int last1 = arr1.get(arr1.size() - 1);
            int last2 = arr2.get(arr2.size() - 1);
            if (last1 > last2) {
                arr1.add(nums[i]);
            } else {
                arr2.add(nums[i]);
            }
        }
        int[] result = new int[n];
        int idx = 0;
        for (int val : arr1) {
            result[idx++] = val;
        }
        for (int val : arr2) {
            result[idx++] = val;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        return arr1 + arr2
```

## Python3

```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i, val in enumerate(nums):
            if i == 0:
                arr1.append(val)
            elif i == 1:
                arr2.append(val)
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(val)
                else:
                    arr2.append(val)
        return arr1 + arr2
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultArray(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int *arr1 = (int*)malloc(numsSize * sizeof(int));
    int *arr2 = (int*)malloc(numsSize * sizeof(int));
    int a_len = 0, b_len = 0;
    
    // First operation
    arr1[a_len++] = nums[0];
    // Second operation (if exists)
    if (numsSize > 1) {
        arr2[b_len++] = nums[1];
    }
    
    for (int i = 2; i < numsSize; ++i) {
        if (arr1[a_len - 1] > arr2[b_len - 1]) {
            arr1[a_len++] = nums[i];
        } else {
            arr2[b_len++] = nums[i];
        }
    }
    
    int *result = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < a_len; ++i) {
        result[i] = arr1[i];
    }
    for (int i = 0; i < b_len; ++i) {
        result[a_len + i] = arr2[i];
    }
    
    free(arr1);
    free(arr2);
    
    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ResultArray(int[] nums) {
        var arr1 = new System.Collections.Generic.List<int>();
        var arr2 = new System.Collections.Generic.List<int>();
        if (nums.Length == 0) return new int[0];
        arr1.Add(nums[0]);
        if (nums.Length > 1) arr2.Add(nums[1]);
        for (int i = 2; i < nums.Length; i++) {
            int last1 = arr1[arr1.Count - 1];
            int last2 = arr2[arr2.Count - 1];
            if (last1 > last2) {
                arr1.Add(nums[i]);
            } else {
                arr2.Add(nums[i]);
            }
        }
        var result = new System.Collections.Generic.List<int>(arr1);
        result.AddRange(arr2);
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var resultArray = function(nums) {
    const arr1 = [nums[0]];
    const arr2 = [nums[1]];
    
    for (let i = 2; i < nums.length; i++) {
        if (arr1[arr1.length - 1] > arr2[arr2.length - 1]) {
            arr1.push(nums[i]);
        } else {
            arr2.push(nums[i]);
        }
    }
    
    return arr1.concat(arr2);
};
```

## Typescript

```typescript
function resultArray(nums: number[]): number[] {
    const arr1: number[] = [];
    const arr2: number[] = [];

    if (nums.length === 0) return [];

    arr1.push(nums[0]);
    if (nums.length > 1) arr2.push(nums[1]);

    for (let i = 2; i < nums.length; i++) {
        const last1 = arr1[arr1.length - 1];
        const last2 = arr2[arr2.length - 1];
        if (last1 > last2) {
            arr1.push(nums[i]);
        } else {
            arr2.push(nums[i]);
        }
    }

    return arr1.concat(arr2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function resultArray($nums) {
        $arr1 = [];
        $arr2 = [];

        $n = count($nums);
        if ($n == 0) {
            return [];
        }

        // First operation
        $arr1[] = $nums[0];

        // Second operation, if exists
        if ($n > 1) {
            $arr2[] = $nums[1];
        }

        // Remaining operations
        for ($i = 2; $i < $n; $i++) {
            $last1 = end($arr1);
            $last2 = end($arr2);
            if ($last1 > $last2) {
                $arr1[] = $nums[$i];
            } else {
                $arr2[] = $nums[$i];
            }
        }

        return array_merge($arr1, $arr2);
    }
}
```

## Swift

```swift
class Solution {
    func resultArray(_ nums: [Int]) -> [Int] {
        var arr1 = [Int]()
        var arr2 = [Int]()
        guard !nums.isEmpty else { return [] }
        arr1.append(nums[0])
        if nums.count > 1 {
            arr2.append(nums[1])
        }
        for i in 2..<nums.count {
            let last1 = arr1.last!
            let last2 = arr2.last!
            if last1 > last2 {
                arr1.append(nums[i])
            } else {
                arr2.append(nums[i])
            }
        }
        return arr1 + arr2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun resultArray(nums: IntArray): IntArray {
        val arr1 = mutableListOf<Int>()
        val arr2 = mutableListOf<Int>()
        if (nums.isEmpty()) return intArrayOf()
        arr1.add(nums[0])
        if (nums.size > 1) arr2.add(nums[1])
        for (i in 2 until nums.size) {
            if (arr1.last() > arr2.last()) {
                arr1.add(nums[i])
            } else {
                arr2.add(nums[i])
            }
        }
        val result = IntArray(arr1.size + arr2.size)
        var idx = 0
        for (v in arr1) result[idx++] = v
        for (v in arr2) result[idx++] = v
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> resultArray(List<int> nums) {
    List<int> arr1 = [];
    List<int> arr2 = [];

    if (nums.isEmpty) return [];

    arr1.add(nums[0]);
    if (nums.length > 1) arr2.add(nums[1]);

    for (int i = 2; i < nums.length; ++i) {
      if (arr1.last > arr2.last) {
        arr1.add(nums[i]);
      } else {
        arr2.add(nums[i]);
      }
    }

    return [...arr1, ...arr2];
  }
}
```

## Golang

```go
func resultArray(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	arr1 := []int{nums[0]}
	if len(nums) == 1 {
		return arr1
	}
	arr2 := []int{nums[1]}
	for i := 2; i < len(nums); i++ {
		if arr1[len(arr1)-1] > arr2[len(arr2)-1] {
			arr1 = append(arr1, nums[i])
		} else {
			arr2 = append(arr2, nums[i])
		}
	}
	return append(arr1, arr2...)
}
```

## Ruby

```ruby
def result_array(nums)
  return nums if nums.length <= 2
  arr1 = [nums[0]]
  arr2 = [nums[1]]
  nums[2..-1].each do |num|
    if arr1[-1] > arr2[-1]
      arr1 << num
    else
      arr2 << num
    end
  end
  arr1 + arr2
end
```

## Scala

```scala
object Solution {
    def resultArray(nums: Array[Int]): Array[Int] = {
        import scala.collection.mutable.ArrayBuffer
        val arr1 = ArrayBuffer[Int]()
        val arr2 = ArrayBuffer[Int]()
        if (nums.isEmpty) return Array.emptyIntArray

        arr1 += nums(0)
        if (nums.length > 1) arr2 += nums(1)

        var i = 2
        while (i < nums.length) {
            if (arr1.last > arr2.last) arr1 += nums(i)
            else arr2 += nums(i)
            i += 1
        }
        (arr1 ++ arr2).toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut arr1 = Vec::new();
        let mut arr2 = Vec::new();

        if nums.is_empty() {
            return vec![];
        }
        arr1.push(nums[0]);
        if nums.len() > 1 {
            arr2.push(nums[1]);
        }

        for i in 2..nums.len() {
            if *arr1.last().unwrap() > *arr2.last().unwrap() {
                arr1.push(nums[i]);
            } else {
                arr2.push(nums[i]);
            }
        }

        arr1.extend(arr2);
        arr1
    }
}
```

## Racket

```racket
(define/contract (result-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (arr1 (make-vector n))
         (arr2 (make-vector n))
         (idx1 0)
         (idx2 0))
    (for ([i (in-range n)])
      (define x (list-ref nums i))
      (cond
        [(= i 0)
         (vector-set! arr1 idx1 x)
         (set! idx1 (+ idx1 1))]
        [(= i 1)
         (vector-set! arr2 idx2 x)
         (set! idx2 (+ idx2 1))]
        [else
         (define last1 (if (> idx1 0) (vector-ref arr1 (- idx1 1)) -inf.0))
         (define last2 (if (> idx2 0) (vector-ref arr2 (- idx2 1)) -inf.0))
         (if (> last1 last2)
             (begin
               (vector-set! arr1 idx1 x)
               (set! idx1 (+ idx1 1)))
             (begin
               (vector-set! arr2 idx2 x)
               (set! idx2 (+ idx2 1))))]))
    (define (vec->list v len)
      (let loop ((i 0) (acc '()))
        (if (= i len)
            (reverse acc)
            (loop (+ i 1) (cons (vector-ref v i) acc)))))
    (append (vec->list arr1 idx1) (vec->list arr2 idx2))))
```

## Erlang

```erlang
-module(solution).
-export([result_array/1]).

-spec result_array(Nums :: [integer()]) -> [integer()].
result_array([]) ->
    [];
result_array([A]) ->
    [A];
result_array([A, B]) ->
    [A, B];
result_array([A, B | Rest]) ->
    {Arr1, Arr2} = distribute(Rest, [A], [B]),
    Arr1 ++ Arr2.

distribute([], Arr1, Arr2) ->
    {Arr1, Arr2};
distribute([H | T], Arr1, Arr2) ->
    Last1 = lists:last(Arr1),
    Last2 = lists:last(Arr2),
    if
        Last1 > Last2 ->
            distribute(T, Arr1 ++ [H], Arr2);
        true ->
            distribute(T, Arr1, Arr2 ++ [H])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec result_array(nums :: [integer]) :: [integer]
  def result_array(nums) do
    case nums do
      [] -> []
      [_] = single -> single
      [a, b | rest] ->
        {arr1, arr2, last1, last2} = {[a], [b], a, b}

        {final1, final2, _, _} =
          Enum.reduce(rest, {arr1, arr2, last1, last2}, fn x,
                                                          {a1, a2, l1, l2} ->
            if l1 > l2 do
              {a1 ++ [x], a2, x, l2}
            else
              {a1, a2 ++ [x], l1, x}
            end
          end)

        final1 ++ final2
    end
  end
end
```
