# 1403. Minimum Subsequence in Non-Increasing Order

## Cpp

```cpp
class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        int total = 0;
        for (int v : nums) total += v;
        int cur = 0;
        vector<int> res;
        for (int v : nums) {
            cur += v;
            res.push_back(v);
            if (cur > total - cur) break;
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        int total = 0;
        for (int v : nums) total += v;
        Arrays.sort(nums);
        List<Integer> res = new ArrayList<>();
        int cur = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            cur += nums[i];
            res.add(nums[i]);
            if (cur > total - cur) break;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        nums.sort(reverse=True)
        subseq_sum = 0
        result = []
        for x in nums:
            subseq_sum += x
            result.append(x)
            if subseq_sum > total - subseq_sum:
                break
        return result
```

## Python3

```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        cur_sum = 0
        res = []
        for x in nums:
            cur_sum += x
            res.append(x)
            if cur_sum > total - cur_sum:
                break
        return res
```

## C

```c
#include <stdlib.h>

/* Comparator for sorting in non‑increasing order */
static int cmp_desc(const void *a, const void *b) {
    return *(const int *)b - *(const int *)a;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minSubsequence(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    /* Compute total sum of the array */
    int total = 0;
    for (int i = 0; i < numsSize; ++i)
        total += nums[i];

    /* Sort numbers in non‑increasing order */
    qsort(nums, numsSize, sizeof(int), cmp_desc);

    int subseqSum = 0;
    int count = 0;
    while (count < numsSize && subseqSum <= total - subseqSum) {
        subseqSum += nums[count];
        ++count;
    }

    int *result = (int *)malloc(count * sizeof(int));
    for (int i = 0; i < count; ++i)
        result[i] = nums[i];

    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> MinSubsequence(int[] nums) {
        int total = 0;
        foreach (int v in nums) total += v;
        
        Array.Sort(nums);
        List<int> res = new List<int>();
        int curSum = 0;
        for (int i = nums.Length - 1; i >= 0; i--) {
            curSum += nums[i];
            res.Add(nums[i]);
            if (curSum > total - curSum) break;
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
var minSubsequence = function(nums) {
    const total = nums.reduce((s, v) => s + v, 0);
    nums.sort((a, b) => b - a);
    let sum = 0;
    const result = [];
    for (const val of nums) {
        sum += val;
        result.push(val);
        if (sum > total - sum) break;
    }
    return result;
};
```

## Typescript

```typescript
function minSubsequence(nums: number[]): number[] {
    nums.sort((a, b) => b - a);
    const total = nums.reduce((sum, v) => sum + v, 0);
    let cur = 0;
    const result: number[] = [];
    for (const num of nums) {
        cur += num;
        result.push(num);
        if (cur > total - cur) break;
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
    function minSubsequence($nums) {
        rsort($nums);
        $total = array_sum($nums);
        $subSum = 0;
        $result = [];
        foreach ($nums as $val) {
            $subSum += $val;
            $result[] = $val;
            if ($subSum > $total - $subSum) {
                break;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minSubsequence(_ nums: [Int]) -> [Int] {
        let sorted = nums.sorted(by: >)
        var result = [Int]()
        var curSum = 0
        let total = nums.reduce(0, +)
        for v in sorted {
            result.append(v)
            curSum += v
            if curSum > total - curSum {
                break
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSubsequence(nums: IntArray): List<Int> {
        val sorted = nums.sortedDescending()
        var total = 0L
        for (v in nums) total += v.toLong()
        var cur = 0L
        val result = mutableListOf<Int>()
        for (v in sorted) {
            cur += v.toLong()
            result.add(v)
            if (cur > total - cur) break
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> minSubsequence(List<int> nums) {
    int total = 0;
    for (int v in nums) total += v;
    List<int> sorted = List.from(nums);
    sorted.sort((a, b) => b - a);
    int cur = 0;
    List<int> res = [];
    for (int v in sorted) {
      cur += v;
      res.add(v);
      if (cur > total - cur) break;
    }
    return res;
  }
}
```

## Golang

```go
func minSubsequence(nums []int) []int {
    total := 0
    for _, v := range nums {
        total += v
    }
    sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
    curSum := 0
    res := make([]int, 0)
    for _, v := range nums {
        curSum += v
        res = append(res, v)
        if curSum > total-curSum {
            break
        }
    }
    return res
}
```

## Ruby

```ruby
def min_subsequence(nums)
  nums.sort!.reverse!
  total = nums.sum
  cur = 0
  result = []
  nums.each do |v|
    cur += v
    result << v
    break if cur > total - cur
  end
  result
end
```

## Scala

```scala
object Solution {
    def minSubsequence(nums: Array[Int]): List[Int] = {
        val sortedDesc = nums.sorted(Ordering.Int.reverse)
        val totalSum = nums.sum
        var curSum = 0
        val result = scala.collection.mutable.ListBuffer[Int]()
        for (v <- sortedDesc) {
            curSum += v
            result += v
            if (curSum > totalSum - curSum) return result.toList
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_subsequence(nums: Vec<i32>) -> Vec<i32> {
        let mut sorted = nums.clone();
        sorted.sort_unstable_by(|a, b| b.cmp(a));
        let total: i32 = sorted.iter().sum();
        let mut cur = 0;
        let mut res = Vec::new();
        for &v in &sorted {
            cur += v;
            res.push(v);
            if cur > total - cur {
                break;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (min-subsequence nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted (sort nums >))
         (total (foldl + 0 sorted)))
    (let loop ((remaining sorted) (taken '()) (sum 0))
      (if (or (null? remaining) (> (* 2 sum) total))
          (reverse taken)
          (loop (cdr remaining)
                (cons (car remaining) taken)
                (+ sum (car remaining)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_subsequence/1]).

-spec min_subsequence(Nums :: [integer()]) -> [integer()].
min_subsequence(Nums) ->
    Total = lists:sum(Nums),
    Sorted = lists:sort(fun(A, B) -> A > B end, Nums),
    take_until(Sorted, Total, 0, []).

take_until([], _Total, _Acc, Res) ->
    lists:reverse(Res);
take_until([H|T], Total, Acc, Res) ->
    NewAcc = Acc + H,
    if
        NewAcc > Total - NewAcc ->
            lists:reverse([H|Res]);
        true ->
            take_until(T, Total, NewAcc, [H|Res])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_subsequence(nums :: [integer]) :: [integer]
  def min_subsequence(nums) do
    sorted = Enum.sort(nums, &>=/2)
    total = Enum.sum(sorted)

    {selected_rev, _} =
      Enum.reduce_while(sorted, {[], 0}, fn x, {list, sum} ->
        new_sum = sum + x
        new_list = [x | list]

        if new_sum > total - new_sum do
          {:halt, {new_list, new_sum}}
        else
          {:cont, {new_list, new_sum}}
        end
      end)

    Enum.reverse(selected_rev)
  end
end
```
