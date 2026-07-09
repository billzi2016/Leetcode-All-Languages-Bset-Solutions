# 0673. Number of Longest Increasing Subsequence

## Cpp

```cpp
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        vector<int> length(n, 1), count(n, 1);
        int maxLen = 1;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    if (length[j] + 1 > length[i]) {
                        length[i] = length[j] + 1;
                        count[i] = count[j];
                    } else if (length[j] + 1 == length[i]) {
                        count[i] += count[j];
                    }
                }
            }
            maxLen = max(maxLen, length[i]);
        }
        int result = 0;
        for (int i = 0; i < n; ++i) {
            if (length[i] == maxLen) result += count[i];
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int[] lengths = new int[n];
        int[] counts = new int[n];
        Arrays.fill(lengths, 1);
        Arrays.fill(counts, 1);
        int maxLen = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    if (lengths[j] + 1 > lengths[i]) {
                        lengths[i] = lengths[j] + 1;
                        counts[i] = counts[j];
                    } else if (lengths[j] + 1 == lengths[i]) {
                        counts[i] += counts[j];
                    }
                }
            }
            maxLen = Math.max(maxLen, lengths[i]);
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (lengths[i] == maxLen) {
                result += counts[i];
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        return sum(c for l, c in zip(length, count) if l == max_len)
```

## Python3

```python
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        lengths = [1] * n
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_len = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == max_len)
```

## C

```c
#include <stdlib.h>

int findNumberOfLIS(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    
    int *len = (int *)malloc(numsSize * sizeof(int));
    int *cnt = (int *)malloc(numsSize * sizeof(int));
    
    for (int i = 0; i < numsSize; ++i) {
        len[i] = 1;
        cnt[i] = 1;
    }
    
    int maxLen = 1;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[j] < nums[i]) {
                if (len[j] + 1 > len[i]) {
                    len[i] = len[j] + 1;
                    cnt[i] = cnt[j];
                } else if (len[j] + 1 == len[i]) {
                    cnt[i] += cnt[j];
                }
            }
        }
        if (len[i] > maxLen) maxLen = len[i];
    }
    
    int result = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (len[i] == maxLen) result += cnt[i];
    }
    
    free(len);
    free(cnt);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindNumberOfLIS(int[] nums)
    {
        int n = nums.Length;
        if (n == 0) return 0;

        int[] lengths = new int[n];
        int[] counts = new int[n];
        for (int i = 0; i < n; i++)
        {
            lengths[i] = 1;
            counts[i] = 1;
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (nums[j] < nums[i])
                {
                    if (lengths[j] + 1 > lengths[i])
                    {
                        lengths[i] = lengths[j] + 1;
                        counts[i] = counts[j];
                    }
                    else if (lengths[j] + 1 == lengths[i])
                    {
                        counts[i] += counts[j];
                    }
                }
            }
        }

        int maxLen = 0;
        for (int i = 0; i < n; i++)
        {
            if (lengths[i] > maxLen) maxLen = lengths[i];
        }

        int result = 0;
        for (int i = 0; i < n; i++)
        {
            if (lengths[i] == maxLen)
                result += counts[i];
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumberOfLIS = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    const lengths = new Array(n).fill(1);
    const counts = new Array(n).fill(1);
    let maxLen = 1;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (lengths[j] + 1 > lengths[i]) {
                    lengths[i] = lengths[j] + 1;
                    counts[i] = counts[j];
                } else if (lengths[j] + 1 === lengths[i]) {
                    counts[i] += counts[j];
                }
            }
        }
        maxLen = Math.max(maxLen, lengths[i]);
    }

    let result = 0;
    for (let i = 0; i < n; i++) {
        if (lengths[i] === maxLen) {
            result += counts[i];
        }
    }
    return result;
};
```

## Typescript

```typescript
function findNumberOfLIS(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;

    const length = new Array(n).fill(1);
    const count = new Array(n).fill(1);

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (length[j] + 1 > length[i]) {
                    length[i] = length[j] + 1;
                    count[i] = count[j];
                } else if (length[j] + 1 === length[i]) {
                    count[i] += count[j];
                }
            }
        }
    }

    const maxLen = Math.max(...length);
    let result = 0;
    for (let i = 0; i < n; i++) {
        if (length[i] === maxLen) {
            result += count[i];
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
     * @return Integer
     */
    function findNumberOfLIS($nums) {
        $n = count($nums);
        if ($n === 0) {
            return 0;
        }
        $length = array_fill(0, $n, 1);
        $count  = array_fill(0, $n, 1);

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($nums[$j] < $nums[$i]) {
                    if ($length[$j] + 1 > $length[$i]) {
                        $length[$i] = $length[$j] + 1;
                        $count[$i]  = $count[$j];
                    } elseif ($length[$j] + 1 == $length[$i]) {
                        $count[$i] += $count[$j];
                    }
                }
            }
        }

        $maxLen = max($length);
        $result = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($length[$i] == $maxLen) {
                $result += $count[$i];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findNumberOfLIS(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 1 { return n }
        
        var lengths = Array(repeating: 1, count: n)
        var counts = Array(repeating: 1, count: n)
        
        for i in 0..<n {
            for j in 0..<i {
                if nums[j] < nums[i] {
                    if lengths[j] + 1 > lengths[i] {
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    } else if lengths[j] + 1 == lengths[i] {
                        counts[i] += counts[j]
                    }
                }
            }
        }
        
        let maxLen = lengths.max()!
        var result = 0
        for i in 0..<n where lengths[i] == maxLen {
            result += counts[i]
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findNumberOfLIS(nums: IntArray): Int {
        val n = nums.size
        if (n <= 1) return n
        val lengths = IntArray(n) { 1 }
        val counts = IntArray(n) { 1 }
        var maxLen = 1

        for (i in 0 until n) {
            for (j in 0 until i) {
                if (nums[j] < nums[i]) {
                    when {
                        lengths[j] + 1 > lengths[i] -> {
                            lengths[i] = lengths[j] + 1
                            counts[i] = counts[j]
                        }
                        lengths[j] + 1 == lengths[i] -> {
                            counts[i] += counts[j]
                        }
                    }
                }
            }
            if (lengths[i] > maxLen) maxLen = lengths[i]
        }

        var result = 0
        for (i in 0 until n) {
            if (lengths[i] == maxLen) result += counts[i]
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int findNumberOfLIS(List<int> nums) {
    int n = nums.length;
    if (n == 0) return 0;

    List<int> length = List.filled(n, 1);
    List<int> count = List.filled(n, 1);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (nums[j] < nums[i]) {
          int candLen = length[j] + 1;
          if (candLen > length[i]) {
            length[i] = candLen;
            count[i] = count[j];
          } else if (candLen == length[i]) {
            count[i] += count[j];
          }
        }
      }
    }

    int maxLen = 0;
    for (int len in length) {
      if (len > maxLen) maxLen = len;
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
      if (length[i] == maxLen) {
        result += count[i];
      }
    }
    return result;
  }
}
```

## Golang

```go
func findNumberOfLIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	n := len(nums)
	length := make([]int, n)
	count := make([]int, n)

	maxLen := 1
	for i := 0; i < n; i++ {
		length[i] = 1
		count[i] = 1
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				if length[j]+1 > length[i] {
					length[i] = length[j] + 1
					count[i] = count[j]
				} else if length[j]+1 == length[i] {
					count[i] += count[j]
				}
			}
		}
		if length[i] > maxLen {
			maxLen = length[i]
		}
	}

	result := 0
	for i := 0; i < n; i++ {
		if length[i] == maxLen {
			result += count[i]
		}
	}
	return result
}
```

## Ruby

```ruby
def find_number_of_lis(nums)
  n = nums.length
  return 0 if n == 0

  lengths = Array.new(n, 1)
  counts  = Array.new(n, 1)

  max_len = 1

  (0...n).each do |i|
    (0...i).each do |j|
      next unless nums[j] < nums[i]

      if lengths[j] + 1 > lengths[i]
        lengths[i] = lengths[j] + 1
        counts[i] = counts[j]
      elsif lengths[j] + 1 == lengths[i]
        counts[i] += counts[j]
      end
    end
    max_len = [max_len, lengths[i]].max
  end

  result = 0
  (0...n).each do |i|
    result += counts[i] if lengths[i] == max_len
  end
  result
end
```

## Scala

```scala
object Solution {
    def findNumberOfLIS(nums: Array[Int]): Int = {
        val n = nums.length
        if (n <= 1) return n

        val lengths = Array.fill(n)(1)
        val counts = Array.fill(n)(1)

        var maxLen = 1

        for (i <- 0 until n) {
            for (j <- 0 until i) {
                if (nums(j) < nums(i)) {
                    if (lengths(j) + 1 > lengths(i)) {
                        lengths(i) = lengths(j) + 1
                        counts(i) = counts(j)
                    } else if (lengths(j) + 1 == lengths(i)) {
                        counts(i) += counts(j)
                    }
                }
            }
            if (lengths(i) > maxLen) maxLen = lengths(i)
        }

        var result = 0
        for (i <- 0 until n) {
            if (lengths(i) == maxLen) result += counts(i)
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut lengths = vec![1usize; n];
        let mut counts = vec![1i64; n];

        for i in 0..n {
            for j in 0..i {
                if nums[j] < nums[i] {
                    if lengths[j] + 1 > lengths[i] {
                        lengths[i] = lengths[j] + 1;
                        counts[i] = counts[j];
                    } else if lengths[j] + 1 == lengths[i] {
                        counts[i] += counts[j];
                    }
                }
            }
        }

        let max_len = *lengths.iter().max().unwrap();
        let mut result: i64 = 0;
        for i in 0..n {
            if lengths[i] == max_len {
                result += counts[i];
            }
        }
        result as i32
    }
}
```

## Racket

```racket
(define/contract (find-number-of-lis nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (if (= n 0)
        0
        (let ((len (make-vector n 1))
              (cnt (make-vector n 1)))
          (for ([i (in-range n)])
            (for ([j (in-range i)])
              (when (< (vector-ref v j) (vector-ref v i))
                (let* ((li (+ (vector-ref len j) 1))
                       (cur (vector-ref len i)))
                  (cond
                    [(> li cur)
                     (vector-set! len i li)
                     (vector-set! cnt i (vector-ref cnt j))]
                    [(= li cur)
                     (vector-set! cnt i (+ (vector-ref cnt i) (vector-ref cnt j)))])))))
          (let ((maxlen (apply max (vector->list len))))
            (for/sum ([i (in-range n)]
                      #:when (= (vector-ref len i) maxlen))
              (vector-ref cnt i)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_number_of_lis/1]).

-spec find_number_of_lis(Nums :: [integer()]) -> integer().
find_number_of_lis(Nums) ->
    case Nums of
        [] -> 0;
        _ ->
            Len = length(Nums),
            NumTuple = list_to_tuple(Nums),
            LengthArr0 = array:new(Len),
            CountArr0 = array:new(Len),
            {LengthArr, CountArr} = loop(0, Len, NumTuple, LengthArr0, CountArr0),
            MaxLen = max_len(0, Len - 1, LengthArr, 0),
            sum_counts(0, Len - 1, LengthArr, CountArr, MaxLen, 0)
    end.

loop(I, N, _NumTuple, LenArr, CntArr) when I == N ->
    {LenArr, CntArr};
loop(I, N, NumTuple, LenArr, CntArr) ->
    ValI = element(I + 1, NumTuple),
    {Li, Ci} = inner_loop(0, I - 1, ValI, NumTuple, LenArr, CntArr, 1, 1),
    NewLenArr = array:set(I, Li, LenArr),
    NewCntArr = array:set(I, Ci, CntArr),
    loop(I + 1, N, NumTuple, NewLenArr, NewCntArr).

inner_loop(J, MaxJ, _ValI, _NumTuple, _LenArr, _CntArr, CurLen, CurCnt) when J > MaxJ ->
    {CurLen, CurCnt};
inner_loop(J, MaxJ, ValI, NumTuple, LenArr, CntArr, CurLen, CurCnt) ->
    ValJ = element(J + 1, NumTuple),
    if
        ValJ < ValI ->
            Lj = array:get(J, LenArr),
            Cj = array:get(J, CntArr),
            case Lj + 1 > CurLen of
                true ->
                    inner_loop(J + 1, MaxJ, ValI, NumTuple, LenArr, CntArr, Lj + 1, 0);
                false ->
                    if
                        Lj + 1 == CurLen ->
                            inner_loop(J + 1, MaxJ, ValI, NumTuple, LenArr, CntArr,
                                       CurLen, CurCnt + Cj);
                        true ->
                            inner_loop(J + 1, MaxJ, ValI, NumTuple, LenArr, CntArr,
                                       CurLen, CurCnt)
                    end
            end;
        true ->
            inner_loop(J + 1, MaxJ, ValI, NumTuple, LenArr, CntArr, CurLen, CurCnt)
    end.

max_len(I, MaxIdx, Arr, Cur) when I > MaxIdx -> Cur;
max_len(I, MaxIdx, Arr, Cur) ->
    L = array:get(I, Arr),
    NewCur = if L > Cur -> L; true -> Cur end,
    max_len(I + 1, MaxIdx, Arr, NewCur).

sum_counts(I, MaxIdx, LenArr, CntArr, MaxLen, Acc) when I > MaxIdx -> Acc;
sum_counts(I, MaxIdx, LenArr, CntArr, MaxLen, Acc) ->
    L = array:get(I, LenArr),
    if
        L == MaxLen ->
            C = array:get(I, CntArr),
            sum_counts(I + 1, MaxIdx, LenArr, CntArr, MaxLen, Acc + C);
        true ->
            sum_counts(I + 1, MaxIdx, LenArr, CntArr, MaxLen, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_number_of_lis(nums :: [integer]) :: integer
  def find_number_of_lis(nums) do
    n = length(nums)
    nums_arr = :array.from_list(nums)

    # initialize empty arrays for lengths and counts
    len_arr0 = :array.new(n, default: 0)
    cnt_arr0 = :array.new(n, default: 0)

    {len_arr, cnt_arr} =
      Enum.reduce(0..(n - 1), {len_arr0, cnt_arr0}, fn i, {len_acc, cnt_acc} ->
        # start with subsequence consisting of nums[i] alone
        init_len = 1
        init_cnt = 1

        {final_len, final_cnt} =
          Enum.reduce(0..(i - 1), {init_len, init_cnt}, fn j, {cur_len, cur_cnt} ->
            if :array.get(j, nums_arr) < :array.get(i, nums_arr) do
              len_j = :array.get(j, len_acc)
              cnt_j = :array.get(j, cnt_acc)

              cond do
                len_j + 1 > cur_len -> {len_j + 1, cnt_j}
                len_j + 1 == cur_len -> {cur_len, cur_cnt + cnt_j}
                true -> {cur_len, cur_cnt}
              end
            else
              {cur_len, cur_cnt}
            end
          end)

        new_len_acc = :array.set(i, final_len, len_acc)
        new_cnt_acc = :array.set(i, final_cnt, cnt_acc)
        {new_len_acc, new_cnt_acc}
      end)

    # find maximum length
    max_len =
      0..(n - 1)
      |> Enum.map(fn i -> :array.get(i, len_arr) end)
      |> Enum.max()

    # sum counts of sequences achieving max_len
    0..(n - 1)
    |> Enum.reduce(0, fn i, acc ->
      if :array.get(i, len_arr) == max_len do
        acc + :array.get(i, cnt_arr)
      else
        acc
      end
    end)
  end
end
```
