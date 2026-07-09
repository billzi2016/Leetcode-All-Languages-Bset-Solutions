# 3254. Find the Power of K-Size Subarrays I

## Cpp

```cpp
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        int n = nums.size();
        if (k == 1) return nums;
        vector<int> ans(n - k + 1, -1);
        int cnt = 1; // length of current consecutive increasing sequence
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] + 1 == nums[i + 1]) {
                ++cnt;
            } else {
                cnt = 1;
            }
            if (cnt >= k) {
                ans[i - k + 2] = nums[i + 1];
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int n = nums.length;
        if (k == 1) {
            return nums.clone();
        }
        int[] res = new int[n - k + 1];
        Arrays.fill(res, -1);
        int cnt = 1; // length of current consecutive increasing run
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] + 1 == nums[i + 1]) {
                cnt++;
            } else {
                cnt = 1;
            }
            if (cnt >= k) {
                int start = i - k + 2;
                res[start] = nums[i + 1];
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if k == 1:
            return nums[:]
        res = [-1] * (n - k + 1)
        cnt = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res[i - k + 1] = nums[i]
        return res
```

## Python3

```python
class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if k == 1:
            return nums[:]
        res = [-1] * (n - k + 1)
        cnt = 1
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res[i - k + 2] = nums[i + 1]
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultsArray(int* nums, int numsSize, int k, int* returnSize) {
    int size = numsSize - k + 1;
    if (size < 0) size = 0;               // safety, though constraints guarantee k <= n
    *returnSize = size;
    int* res = (int*)malloc(sizeof(int) * size);
    
    for (int i = 0; i < size; ++i) {
        res[i] = -1;
    }
    
    if (k == 1) {
        for (int i = 0; i < numsSize; ++i) {
            res[i] = nums[i];
        }
        return res;
    }
    
    int consecutiveCount = 1; // length of current increasing-by-1 sequence
    for (int i = 0; i < numsSize - 1; ++i) {
        if (nums[i] + 1 == nums[i + 1]) {
            ++consecutiveCount;
        } else {
            consecutiveCount = 1;
        }
        if (consecutiveCount >= k) {
            int idx = i - k + 2; // start index of the subarray
            if (idx >= 0 && idx < size) {
                res[idx] = nums[i + 1];
            }
        }
    }
    
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ResultsArray(int[] nums, int k) {
        int n = nums.Length;
        int m = n - k + 1;
        int[] res = new int[m];
        if (k == 1) {
            for (int i = 0; i < n; i++) res[i] = nums[i];
            return res;
        }
        for (int i = 0; i < m; i++) res[i] = -1;

        int cnt = 1; // length of current consecutive increasing sequence ending at current index
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] + 1 == nums[i + 1]) {
                cnt++;
            } else {
                cnt = 1;
            }
            if (cnt >= k) {
                int startIdx = i - k + 2; // window starts here
                res[startIdx] = nums[i + 1];
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
 * @param {number} k
 * @return {number[]}
 */
var resultsArray = function(nums, k) {
    const n = nums.length;
    const m = n - k + 1;
    const res = new Array(m).fill(-1);
    
    if (k === 1) {
        for (let i = 0; i < n; ++i) {
            res[i] = nums[i];
        }
        return res;
    }
    
    let cnt = 1; // length of current consecutive increasing sequence
    for (let i = 0; i < n - 1; ++i) {
        if (nums[i] + 1 === nums[i + 1]) {
            cnt++;
        } else {
            cnt = 1;
        }
        if (cnt >= k) {
            const startIdx = i - k + 2; // result position for this window
            res[startIdx] = nums[i + 1];
        }
    }
    
    return res;
};
```

## Typescript

```typescript
function resultsArray(nums: number[], k: number): number[] {
    const n = nums.length;
    const m = n - k + 1;
    const result = new Array(m).fill(-1);
    if (k === 1) return nums.slice();
    let consecutiveCount = 1;
    for (let i = 0; i < n - 1; ++i) {
        if (nums[i] + 1 === nums[i + 1]) {
            consecutiveCount++;
        } else {
            consecutiveCount = 1;
        }
        if (consecutiveCount >= k) {
            result[(i + 1) - k] = nums[i + 1];
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
     * @param Integer $k
     * @return Integer[]
     */
    function resultsArray($nums, $k) {
        $n = count($nums);
        $m = $n - $k + 1;
        if ($k == 1) {
            // each single element forms a valid subarray
            return $nums;
        }
        $res = array_fill(0, $m, -1);
        $cnt = 1; // length of current consecutive increasing sequence
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] + 1 == $nums[$i + 1]) {
                $cnt++;
            } else {
                $cnt = 1;
            }
            if ($cnt >= $k) {
                // subarray ending at index $i+1 is valid
                $res[$i - $k + 2] = $nums[$i + 1];
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func resultsArray(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        if k == 1 { return nums }
        var result = Array(repeating: -1, count: n - k + 1)
        var consecutiveCount = 1
        for i in 0..<(n - 1) {
            if nums[i] + 1 == nums[i + 1] {
                consecutiveCount += 1
            } else {
                consecutiveCount = 1
            }
            if consecutiveCount >= k {
                let startIdx = i - k + 2
                result[startIdx] = nums[i + 1]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun resultsArray(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        if (k == 1) return nums.clone()
        val res = IntArray(n - k + 1) { -1 }
        var cnt = 1
        for (i in 0 until n - 1) {
            if (nums[i] + 1 == nums[i + 1]) {
                cnt++
            } else {
                cnt = 1
            }
            if (cnt >= k) {
                val start = i - k + 2
                res[start] = nums[i + 1]
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> resultsArray(List<int> nums, int k) {
    int n = nums.length;
    if (k == 1) {
      return List<int>.from(nums);
    }
    int resSize = n - k + 1;
    if (resSize <= 0) return [];
    List<int> result = List.filled(resSize, -1);
    int consecutive = 1; // length of current increasing consecutive run
    for (int i = 0; i < n - 1; ++i) {
      if (nums[i] + 1 == nums[i + 1]) {
        consecutive++;
      } else {
        consecutive = 1;
      }
      if (consecutive >= k) {
        int startIdx = i - k + 2; // starting index of the valid subarray
        result[startIdx] = nums[i + 1];
      }
    }
    return result;
  }
}
```

## Golang

```go
func resultsArray(nums []int, k int) []int {
	n := len(nums)
	if k == 1 {
		res := make([]int, n)
		copy(res, nums)
		return res
	}
	size := n - k + 1
	result := make([]int, size)
	for i := range result {
		result[i] = -1
	}
	cnt := 1
	for i := 0; i < n-1; i++ {
		if nums[i]+1 == nums[i+1] {
			cnt++
		} else {
			cnt = 1
		}
		if cnt >= k {
			result[i+1-k] = nums[i+1]
		}
	}
	return result
}
```

## Ruby

```ruby
def results_array(nums, k)
  n = nums.length
  return [] if n == 0
  return nums.clone if k == 1

  res = Array.new(n - k + 1, -1)
  cnt = 1

  (0...n - 1).each do |i|
    if nums[i] + 1 == nums[i + 1]
      cnt += 1
    else
      cnt = 1
    end

    if cnt >= k
      idx = i - k + 2
      res[idx] = nums[i + 1]
    end
  end

  res
end
```

## Scala

```scala
object Solution {
    def resultsArray(nums: Array[Int], k: Int): Array[Int] = {
        val n = nums.length
        if (k == 1) return nums.clone()
        val resSize = n - k + 1
        val result = Array.fill(resSize)(-1)
        var cnt = 1
        for (i <- 0 until n - 1) {
            if (nums(i) + 1 == nums(i + 1)) cnt += 1 else cnt = 1
            if (cnt >= k) {
                val idx = i - k + 2
                result(idx) = nums(i + 1)
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k_usize = k as usize;
        if k_usize == 1 {
            return nums;
        }
        if n < k_usize {
            return vec![];
        }
        let mut result = vec![-1; n - k_usize + 1];
        let mut cnt: usize = 1;
        for i in 0..n - 1 {
            if nums[i] + 1 == nums[i + 1] {
                cnt += 1;
            } else {
                cnt = 1;
            }
            if cnt >= k_usize {
                let start = i + 2 - k_usize;
                result[start] = nums[i + 1];
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (results-array nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ((n (length nums)))
    (if (= k 1)
        nums
        (let* ((vec (list->vector nums))
               (res (make-vector (+ (- n k) 1) -1)))
          (let loop ((i 0) (cnt 1))
            (when (< i (- n 1))
              (if (= (+ (vector-ref vec i) 1) (vector-ref vec (+ i 1)))
                  (set! cnt (+ cnt 1))
                  (set! cnt 1))
              (when (>= cnt k)
                (let ((idx (+ (- i k) 2))) ; start index of the subarray
                  (vector-set! res idx (vector-ref vec (+ i 1)))))
              (loop (+ i 1) cnt)))
          (vector->list res)))))
```

## Erlang

```erlang
-module(solution).
-export([results_array/2]).

-spec results_array(Nums :: [integer()], K :: integer()) -> [integer()].
results_array(Nums, K) when K =:= 1 ->
    Nums;
results_array(Nums, K) ->
    process(Nums, K, [], undefined, 0, 0).

process([], _K, Acc, _Prev, _Count, _Pos) ->
    lists:reverse(Acc);
process([X|Rest], K, Acc, Prev, Count, Pos) ->
    NewCount = case Prev of
        undefined -> 1;
        _ when Prev + 1 == X -> Count + 1;
        _ -> 1
    end,
    {NewAcc, NewPos} =
        if Pos >= K - 1 ->
                Value = if NewCount >= K -> X; true -> -1 end,
                {[Value|Acc], Pos + 1};
           true ->
                {Acc, Pos + 1}
        end,
    process(Rest, K, NewAcc, X, NewCount, NewPos).
```

## Elixir

```elixir
defmodule Solution do
  @spec results_array(nums :: [integer], k :: integer) :: [integer]
  def results_array(nums, k) do
    len = length(nums)
    max_start = len - k

    Enum.map(0..max_start, fn start ->
      if consecutive?(nums, start, k) do
        Enum.at(nums, start + k - 1)
      else
        -1
      end
    end)
  end

  defp consecutive?(_list, _start, k) when k <= 1, do: true

  defp consecutive?(list, start, k) do
    Enum.reduce_while(0..(k - 2), true, fn offset, _acc ->
      a = Enum.at(list, start + offset)
      b = Enum.at(list, start + offset + 1)

      if a + 1 == b do
        {:cont, true}
      else
        {:halt, false}
      end
    end) == true
  end
end
```
