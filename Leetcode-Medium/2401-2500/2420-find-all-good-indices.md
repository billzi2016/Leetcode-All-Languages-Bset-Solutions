# 2420. Find All Good Indices

## Cpp

```cpp
class Solution {
public:
    vector<int> goodIndices(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> left(n), right(n);
        left[0] = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[i - 1] >= nums[i]) left[i] = left[i - 1] + 1;
            else left[i] = 1;
        }
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
            else right[i] = 1;
        }
        vector<int> ans;
        for (int i = k; i <= n - k - 1; ++i) {
            if (left[i - 1] >= k && right[i + 1] >= k)
                ans.push_back(i);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> goodIndices(int[] nums, int k) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];

        left[0] = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i - 1] >= nums[i]) {
                left[i] = left[i - 1] + 1;
            } else {
                left[i] = 1;
            }
        }

        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) {
                right[i] = right[i + 1] + 1;
            } else {
                right[i] = 1;
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = k; i < n - k; i++) {
            if (left[i - 1] >= k && right[i + 1] >= k) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        dec = [1] * n  # length of non‑increasing segment ending at i
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                dec[i] = dec[i - 1] + 1

        inc = [1] * n  # length of non‑decreasing segment starting at i
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        res = []
        for i in range(k, n - k):
            if dec[i - 1] >= k and inc[i + 1] >= k:
                res.append(i)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # non_inc[i]: length of consecutive non‑increasing pairs ending at i
        non_inc = [0] * n
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                non_inc[i] = non_inc[i - 1] + 1

        # non_dec[i]: length of consecutive non‑decreasing pairs starting at i
        non_dec = [0] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1

        res: List[int] = []
        # i must satisfy k <= i < n - k
        for i in range(k, n - k):
            if non_inc[i - 1] >= k - 1 and non_dec[i + 1] >= k - 1:
                res.append(i)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodIndices(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int *left = (int *)malloc(n * sizeof(int));
    int *right = (int *)malloc(n * sizeof(int));

    left[0] = 1;
    for (int i = 1; i < n; ++i) {
        if (nums[i - 1] >= nums[i])
            left[i] = left[i - 1] + 1;
        else
            left[i] = 1;
    }

    right[n - 1] = 1;
    for (int i = n - 2; i >= 0; --i) {
        if (nums[i] <= nums[i + 1])
            right[i] = right[i + 1] + 1;
        else
            right[i] = 1;
    }

    int *res = (int *)malloc(n * sizeof(int));
    int cnt = 0;

    for (int i = k; i < n - k; ++i) {
        if (left[i - 1] >= k && right[i + 1] >= k) {
            res[cnt++] = i;
        }
    }

    free(left);
    free(right);
    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> GoodIndices(int[] nums, int k) {
        int n = nums.Length;
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i - 1] >= nums[i]) {
                left[i] = left[i - 1] + 1;
            } else {
                left[i] = 1;
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1 && nums[i] <= nums[i + 1]) {
                right[i] = right[i + 1] + 1;
            } else {
                right[i] = 1;
            }
        }

        List<int> result = new List<int>();
        for (int i = k; i < n - k; i++) {
            if (left[i - 1] >= k && right[i + 1] >= k) {
                result.Add(i);
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
 * @param {number} k
 * @return {number[]}
 */
var goodIndices = function(nums, k) {
    const n = nums.length;
    const left = new Array(n).fill(1);
    for (let i = 1; i < n; ++i) {
        if (nums[i - 1] >= nums[i]) left[i] = left[i - 1] + 1;
        else left[i] = 1;
    }
    const right = new Array(n).fill(1);
    for (let i = n - 2; i >= 0; --i) {
        if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
        else right[i] = 1;
    }
    const res = [];
    for (let i = k; i <= n - k - 1; ++i) {
        if (left[i - 1] >= k && right[i + 1] >= k) {
            res.push(i);
        }
    }
    return res;
};
```

## Typescript

```typescript
function goodIndices(nums: number[], k: number): number[] {
    const n = nums.length;
    const left: number[] = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (nums[i - 1] >= nums[i]) {
            left[i] = left[i - 1] + 1;
        }
    }

    const right: number[] = new Array(n).fill(1);
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= nums[i + 1]) {
            right[i] = right[i + 1] + 1;
        }
    }

    const res: number[] = [];
    for (let i = k; i <= n - k - 1; i++) {
        if (left[i - 1] >= k && right[i + 1] >= k) {
            res.push(i);
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
     * @param Integer $k
     * @return Integer[]
     */
    function goodIndices($nums, $k) {
        $n = count($nums);
        if ($n == 0) return [];

        $left = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] >= $nums[$i]) {
                $left[$i] = $left[$i - 1] + 1;
            } else {
                $left[$i] = 0;
            }
        }

        $right = array_fill(0, $n, 0);
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] <= $nums[$i + 1]) {
                $right[$i] = $right[$i + 1] + 1;
            } else {
                $right[$i] = 0;
            }
        }

        $need = $k - 1; // number of required consecutive comparisons
        $result = [];

        for ($i = $k; $i <= $n - $k - 1; $i++) {
            if ($left[$i - 1] >= $need && $right[$i + 1] >= $need) {
                $result[] = $i;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func goodIndices(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        if n == 0 { return [] }
        var incPref = Array(repeating: 0, count: n)
        var decPref = Array(repeating: 0, count: n)
        if n > 1 {
            for i in 1..<n {
                incPref[i] = incPref[i - 1] + (nums[i - 1] < nums[i] ? 1 : 0)
                decPref[i] = decPref[i - 1] + (nums[i - 1] > nums[i] ? 1 : 0)
            }
        }
        var result = [Int]()
        if n >= 2 {
            for i in k..<(n - k) {
                let leftViolations = incPref[i - 1] - incPref[i - k]
                let rightViolations = decPref[i + k] - decPref[i + 1]
                if leftViolations == 0 && rightViolations == 0 {
                    result.append(i)
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun goodIndices(nums: IntArray, k: Int): List<Int> {
        val n = nums.size
        val left = IntArray(n)
        left[0] = 1
        for (i in 1 until n) {
            left[i] = if (nums[i - 1] >= nums[i]) left[i - 1] + 1 else 1
        }
        val right = IntArray(n)
        right[n - 1] = 1
        for (i in n - 2 downTo 0) {
            right[i] = if (nums[i] <= nums[i + 1]) right[i + 1] + 1 else 1
        }
        val result = ArrayList<Int>()
        for (i in k until n - k) {
            if (left[i - 1] >= k && right[i + 1] >= k) {
                result.add(i)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> goodIndices(List<int> nums, int k) {
    int n = nums.length;
    List<int> dec = List.filled(n, 1);
    for (int i = 1; i < n; i++) {
      if (nums[i] <= nums[i - 1]) {
        dec[i] = dec[i - 1] + 1;
      } else {
        dec[i] = 1;
      }
    }

    List<int> inc = List.filled(n, 1);
    for (int i = n - 2; i >= 0; i--) {
      if (nums[i] <= nums[i + 1]) {
        inc[i] = inc[i + 1] + 1;
      } else {
        inc[i] = 1;
      }
    }

    List<int> res = [];
    for (int i = k; i <= n - k - 1; i++) {
      if (dec[i - 1] >= k && inc[i + 1] >= k) {
        res.add(i);
      }
    }
    return res;
  }
}
```

## Golang

```go
func goodIndices(nums []int, k int) []int {
	n := len(nums)
	if n == 0 || k == 0 {
		return []int{}
	}
	left := make([]int, n)
	right := make([]int, n)

	// left[i]: length of longest non‑increasing subarray ending at i
	for i := 0; i < n; i++ {
		if i > 0 && nums[i-1] >= nums[i] {
			left[i] = left[i-1] + 1
		} else {
			left[i] = 1
		}
	}

	// right[i]: length of longest non‑decreasing subarray starting at i
	for i := n - 1; i >= 0; i-- {
		if i+1 < n && nums[i] <= nums[i+1] {
			right[i] = right[i+1] + 1
		} else {
			right[i] = 1
		}
	}

	ans := make([]int, 0)
	for i := k; i <= n-k-1; i++ {
		if left[i-1] >= k && right[i+1] >= k {
			ans = append(ans, i)
		}
	}
	return ans
}
```

## Ruby

```ruby
def good_indices(nums, k)
  n = nums.length
  left = Array.new(n, 1)
  (1...n).each do |i|
    if nums[i - 1] >= nums[i]
      left[i] = left[i - 1] + 1
    else
      left[i] = 1
    end
  end

  right = Array.new(n, 1)
  (n - 2).downto(0) do |i|
    if nums[i] <= nums[i + 1]
      right[i] = right[i + 1] + 1
    else
      right[i] = 1
    end
  end

  res = []
  (k...(n - k)).each do |i|
    if left[i - 1] >= k && right[i + 1] >= k
      res << i
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def goodIndices(nums: Array[Int], k: Int): List[Int] = {
        val n = nums.length
        if (n == 0) return Nil

        // violations for non‑increasing (need nums[i] >= nums[i+1])
        val badDec = new Array[Int](n - 1)
        // violations for non‑decreasing (need nums[i] <= nums[i+1])
        val badInc = new Array[Int](n - 1)

        var i = 0
        while (i < n - 1) {
            if (nums(i) < nums(i + 1)) badDec(i) = 1 else badDec(i) = 0
            if (nums(i) > nums(i + 1)) badInc(i) = 1 else badInc(i) = 0
            i += 1
        }

        // prefix sums of violations
        val prefBadDec = new Array[Int](n)
        val prefBadInc = new Array[Int](n)

        var sum = 0
        i = 0
        while (i < n - 1) {
            sum += badDec(i)
            prefBadDec(i + 1) = sum
            i += 1
        }

        sum = 0
        i = 0
        while (i < n - 1) {
            sum += badInc(i)
            prefBadInc(i + 1) = sum
            i += 1
        }

        val res = scala.collection.mutable.ListBuffer[Int]()
        var idx = k
        while (idx <= n - k - 1) {
            // check left side: subarray [idx-k, idx-1] non‑increasing
            val leftViol = prefBadDec(idx - 1) - prefBadDec(idx - k)
            if (leftViol == 0) {
                // check right side: subarray [idx+1, idx+k] non‑decreasing
                val rightViol = prefBadInc(idx + k) - prefBadInc(idx + 1)
                if (rightViol == 0) res += idx
            }
            idx += 1
        }

        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn good_indices(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k_usize = k as usize;
        if n == 0 || k_usize == 0 || n < 2 * k_usize + 1 {
            return Vec::new();
        }

        // left[i]: length of longest non‑increasing suffix ending at i
        let mut left = vec![1usize; n];
        for i in 1..n {
            if nums[i - 1] >= nums[i] {
                left[i] = left[i - 1] + 1;
            } else {
                left[i] = 1;
            }
        }

        // right[i]: length of longest non‑decreasing prefix starting at i
        let mut right = vec![1usize; n];
        for i in (0..n - 1).rev() {
            if nums[i] <= nums[i + 1] {
                right[i] = right[i + 1] + 1;
            } else {
                right[i] = 1;
            }
        }

        let mut ans = Vec::new();
        for i in k_usize..(n - k_usize) {
            if left[i - 1] >= k_usize && right[i + 1] >= k_usize {
                ans.push(i as i32);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (good-indices nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((arr (list->vector nums))
         (n (vector-length arr)))
    (if (< n (* 2 k))
        '()
        (let ((left (make-vector n 1))
              (right (make-vector n 1)))
          ;; left[i] = length of longest non‑increasing subarray ending at i
          (for ([i (in-range 1 n)])
            (if (>= (vector-ref arr (- i 1)) (vector-ref arr i))
                (vector-set! left i (+ 1 (vector-ref left (- i 1))))
                (vector-set! left i 1)))
          ;; right[i] = length of longest non‑decreasing subarray starting at i
          (for ([i (in-range (- n 2) -1 -1)])
            (if (<= (vector-ref arr i) (vector-ref arr (+ i 1)))
                (vector-set! right i (+ 1 (vector-ref right (+ i 1))))
                (vector-set! right i 1)))
          ;; collect good indices
          (let loop ((i k) (acc '()))
            (if (> i (- n k 1))
                (reverse acc)
                (let ((good-left (>= (vector-ref left (- i 1)) k))
                      (good-right (>= (vector-ref right (+ i 1)) k)))
                  (loop (+ i 1)
                        (if (and good-left good-right)
                            (cons i acc)
                            acc)))))))))
```

## Erlang

```erlang
-spec good_indices(Nums :: [integer()], K :: integer()) -> [integer()].
good_indices(Nums, K) ->
    N = length(Nums),
    LeftGood = left_scan(Nums, K),
    RightRev = left_scan(lists:reverse(Nums), K),
    RightGood = lists:reverse(RightRev),
    LTuple = list_to_tuple(LeftGood),
    RTuple = list_to_tuple(RightGood),
    collect(K, N, K, LTuple, RTuple, []).

left_scan(Nums, K) ->
    left_scan(Nums, K, undefined, 0, 0, []).

left_scan([], _K, _Prev, _Cnt, _Idx, Acc) ->
    lists:reverse(Acc);
left_scan([H|T], K, Prev, Cnt, Idx, Acc) ->
    NewCnt = case Prev of
        undefined -> 0;
        _ ->
            if Prev >= H -> Cnt + 1; true -> 0 end
    end,
    Good = if Idx >= K-1 -> (NewCnt >= K-1); true -> false end,
    left_scan(T, K, H, NewCnt, Idx+1, [Good|Acc]).

collect(I, N, _K, LTuple, RTuple, Acc) when I =< N - _K - 1 ->
    LeftOk = element(I, LTuple),
    RightOk = element(I + 2, RTuple),
    NewAcc = if LeftOk andalso RightOk -> [I|Acc]; true -> Acc end,
    collect(I+1, N, _K, LTuple, RTuple, NewAcc);
collect(_, _, _, _, _, Acc) ->
    lists:reverse(Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec good_indices(nums :: [integer], k :: integer) :: [integer]
  def good_indices(nums, k) do
    n = length(nums)
    nums_t = List.to_tuple(nums)

    left_cnt = build_left_counts(nums_t, n)
    right_cnt = build_right_counts(nums_t, n)

    start_i = k
    end_i_exclusive = n - k

    Enum.reduce(start_i..(end_i_exclusive - 1), [], fn i, acc ->
      if elem(left_cnt, i - 1) >= k - 1 and elem(right_cnt, i + 1) >= k - 1 do
        [i | acc]
      else
        acc
      end
    end)
    |> Enum.reverse()
  end

  defp build_left_counts(nums_t, n) do
    {list_rev, _} =
      Enum.reduce(0..(n - 1), {[], 0}, fn idx, {acc, prev} ->
        val =
          if idx == 0 do
            0
          else
            a = elem(nums_t, idx - 1)
            b = elem(nums_t, idx)

            if a >= b, do: prev + 1, else: 0
          end

        {[val | acc], val}
      end)

    List.to_tuple(Enum.reverse(list_rev))
  end

  defp build_right_counts(nums_t, n) do
    indices = Enum.to_list(0..(n - 2)) |> Enum.reverse()

    {list_rev, _} =
      Enum.reduce(indices, {[], 0}, fn idx, {acc, prev} ->
        a = elem(nums_t, idx)
        b = elem(nums_t, idx + 1)

        val = if a <= b, do: prev + 1, else: 0
        {[val | acc], val}
      end)

    full_list = list_rev ++ [0]
    List.to_tuple(full_list)
  end
end
```
