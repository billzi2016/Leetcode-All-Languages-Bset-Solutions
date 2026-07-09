# 0985. Sum of Even Numbers After Queries

## Cpp

```cpp
class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        long long evenSum = 0;
        for (int v : nums) {
            if ((v & 1) == 0) evenSum += v;
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int val = q[0];
            int idx = q[1];
            if ((nums[idx] & 1) == 0) evenSum -= nums[idx];
            nums[idx] += val;
            if ((nums[idx] & 1) == 0) evenSum += nums[idx];
            ans.push_back(static_cast<int>(evenSum));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        long evenSum = 0;
        for (int num : nums) {
            if ((num & 1) == 0) {
                evenSum += num;
            }
        }
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int val = queries[i][0];
            int idx = queries[i][1];
            int oldVal = nums[idx];
            if ((oldVal & 1) == 0) {
                evenSum -= oldVal;
            }
            int newVal = oldVal + val;
            nums[idx] = newVal;
            if ((newVal & 1) == 0) {
                evenSum += newVal;
            }
            answer[i] = (int) evenSum;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = sum(x for x in nums if x % 2 == 0)
        res = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            res.append(even_sum)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            result.append(even_sum)
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumEvenAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    long long evenSum = 0;
    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & 1) == 0) {
            evenSum += nums[i];
        }
    }

    int *result = (int *)malloc(sizeof(int) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        int val = queries[i][0];
        int idx = queries[i][1];

        if ((nums[idx] & 1) == 0) {
            evenSum -= nums[idx];
        }

        nums[idx] += val;

        if ((nums[idx] & 1) == 0) {
            evenSum += nums[idx];
        }

        result[i] = (int)evenSum;
    }

    *returnSize = queriesSize;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SumEvenAfterQueries(int[] nums, int[][] queries) {
        long sum = 0;
        foreach (int num in nums) {
            if ((num & 1) == 0) sum += num;
        }
        int m = queries.Length;
        int[] answer = new int[m];
        for (int i = 0; i < m; i++) {
            int val = queries[i][0];
            int idx = queries[i][1];
            if ((nums[idx] & 1) == 0) sum -= nums[idx];
            nums[idx] += val;
            if ((nums[idx] & 1) == 0) sum += nums[idx];
            answer[i] = (int)sum;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumEvenAfterQueries = function(nums, queries) {
    let evenSum = 0;
    for (const v of nums) {
        if ((v & 1) === 0) evenSum += v;
    }
    const result = [];
    for (const [val, idx] of queries) {
        const oldVal = nums[idx];
        if ((oldVal & 1) === 0) evenSum -= oldVal;
        const newVal = oldVal + val;
        nums[idx] = newVal;
        if ((newVal & 1) === 0) evenSum += newVal;
        result.push(evenSum);
    }
    return result;
};
```

## Typescript

```typescript
function sumEvenAfterQueries(nums: number[], queries: number[][]): number[] {
    let evenSum = 0;
    for (const v of nums) {
        if ((v & 1) === 0) evenSum += v;
    }
    const result: number[] = [];
    for (const [val, idx] of queries) {
        const oldVal = nums[idx];
        if ((oldVal & 1) === 0) evenSum -= oldVal;
        const newVal = oldVal + val;
        nums[idx] = newVal;
        if ((newVal & 1) === 0) evenSum += newVal;
        result.push(evenSum);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function sumEvenAfterQueries($nums, $queries) {
        $evenSum = 0;
        foreach ($nums as $v) {
            if ($v % 2 == 0) {
                $evenSum += $v;
            }
        }

        $result = [];
        foreach ($queries as $q) {
            $val = $q[0];
            $idx = $q[1];

            // If current value is even, remove it from sum
            if ($nums[$idx] % 2 == 0) {
                $evenSum -= $nums[$idx];
            }

            // Apply the query
            $nums[$idx] += $val;

            // If new value is even, add it to sum
            if ($nums[$idx] % 2 == 0) {
                $evenSum += $nums[$idx];
            }

            $result[] = $evenSum;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func sumEvenAfterQueries(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var arr = nums
        var sumEven = 0
        for v in arr where (v & 1) == 0 {
            sumEven += v
        }
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let val = q[0]
            let idx = q[1]
            let old = arr[idx]
            if (old & 1) == 0 {
                sumEven -= old
            }
            let newVal = old + val
            arr[idx] = newVal
            if (newVal & 1) == 0 {
                sumEven += newVal
            }
            result.append(sumEven)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumEvenAfterQueries(nums: IntArray, queries: Array<IntArray>): IntArray {
        var evenSum = 0L
        for (v in nums) {
            if ((v and 1) == 0) evenSum += v.toLong()
        }
        val result = IntArray(queries.size)
        for (i in queries.indices) {
            val add = queries[i][0]
            val idx = queries[i][1]
            val oldVal = nums[idx]
            if ((oldVal and 1) == 0) evenSum -= oldVal.toLong()
            val newVal = oldVal + add
            nums[idx] = newVal
            if ((newVal and 1) == 0) evenSum += newVal.toLong()
            result[i] = evenSum.toInt()
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> sumEvenAfterQueries(List<int> nums, List<List<int>> queries) {
    int evenSum = 0;
    for (var v in nums) {
      if (v % 2 == 0) evenSum += v;
    }
    List<int> ans = [];
    for (var q in queries) {
      int val = q[0];
      int idx = q[1];
      int old = nums[idx];
      if (old % 2 == 0) evenSum -= old;
      int newVal = old + val;
      nums[idx] = newVal;
      if (newVal % 2 == 0) evenSum += newVal;
      ans.add(evenSum);
    }
    return ans;
  }
}
```

## Golang

```go
func sumEvenAfterQueries(nums []int, queries [][]int) []int {
    // Calculate initial sum of even numbers
    sum := 0
    for _, v := range nums {
        if v%2 == 0 {
            sum += v
        }
    }

    res := make([]int, len(queries))
    for i, q := range queries {
        val, idx := q[0], q[1]
        // If the current element is even, remove it from sum
        if nums[idx]%2 == 0 {
            sum -= nums[idx]
        }
        // Apply the query update
        nums[idx] += val
        // If the new value is even, add it to sum
        if nums[idx]%2 == 0 {
            sum += nums[idx]
        }
        res[i] = sum
    }
    return res
}
```

## Ruby

```ruby
def sum_even_after_queries(nums, queries)
  sum = 0
  nums.each { |v| sum += v if v.even? }
  result = []
  queries.each do |val, idx|
    old = nums[idx]
    sum -= old if old.even?
    new_val = old + val
    nums[idx] = new_val
    sum += new_val if new_val.even?
    result << sum
  end
  result
end
```

## Scala

```scala
object Solution {
    def sumEvenAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        var evenSum: Long = 0L
        for (v <- nums) {
            if ((v & 1) == 0) evenSum += v
        }
        val res = new Array[Int](queries.length)
        var i = 0
        while (i < queries.length) {
            val value = queries(i)(0)
            val idx = queries(i)(1)
            val oldVal = nums(idx)
            if ((oldVal & 1) == 0) evenSum -= oldVal
            val newVal = oldVal + value
            nums(idx) = newVal
            if ((newVal & 1) == 0) evenSum += newVal
            res(i) = evenSum.toInt
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_even_after_queries(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut arr = nums;
        let mut even_sum: i64 = arr.iter().filter(|&&x| x % 2 == 0).map(|&x| x as i64).sum();
        let mut result = Vec::with_capacity(queries.len());
        for q in queries {
            let val = q[0];
            let idx = q[1] as usize;
            let old = arr[idx];
            if old % 2 == 0 {
                even_sum -= old as i64;
            }
            let new_val = old + val;
            arr[idx] = new_val;
            if new_val % 2 == 0 {
                even_sum += new_val as i64;
            }
            result.push(even_sum as i32);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (sum-even-after-queries nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (length nums)]
         [vec (list->vector nums)]
         [init-sum
          (let loop ((i 0) (s 0))
            (if (= i n)
                s
                (loop (+ i 1)
                      (if (even? (vector-ref vec i))
                          (+ s (vector-ref vec i))
                          s))))])
    (let loop ((qs queries) (curr-sum init-sum) (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ([pair (car qs)]
                 [val (first pair)]
                 [idx (second pair)]
                 [old (vector-ref vec idx)])
            (when (even? old)
              (set! curr-sum (- curr-sum old)))
            (define new (+ old val))
            (vector-set! vec idx new)
            (when (even? new)
              (set! curr-sum (+ curr-sum new)))
            (loop (cdr qs) curr-sum (cons curr-sum acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([sum_even_after_queries/2]).
-spec sum_even_after_queries(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
sum_even_after_queries(Nums, Queries) ->
    EvenSum = lists:foldl(fun(N, Acc) ->
        case N band 1 of
            0 -> Acc + N;
            _ -> Acc
        end
    end, 0, Nums),
    Arr = array:from_list(Nums),
    {ResRev, _} = process_queries(Queries, Arr, EvenSum, []),
    lists:reverse(ResRev).

process_queries([], _Arr, _EvenSum, Acc) ->
    {Acc, undefined};
process_queries([[Val, Index]|Rest], Arr, EvenSum, Acc) ->
    Old = array:get(Index, Arr),
    New = Old + Val,
    EvenSum1 = case Old band 1 of
        0 -> EvenSum - Old;
        _ -> EvenSum
    end,
    EvenSum2 = case New band 1 of
        0 -> EvenSum1 + New;
        _ -> EvenSum1
    end,
    Arr1 = array:set(Index, New, Arr),
    process_queries(Rest, Arr1, EvenSum2, [EvenSum2|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_even_after_queries(nums :: [integer], queries :: [[integer]]) :: [integer]
  def sum_even_after_queries(nums, queries) do
    nums_map = Enum.with_index(nums) |> Map.new(fn {v, i} -> {i, v} end)
    init_sum = sum_even(nums)

    {_final_state, rev_result} =
      Enum.reduce(queries, {{nums_map, init_sum}, []}, fn [val, idx], {{map, sum}, acc} ->
        cur = Map.get(map, idx)

        sum_without_cur =
          if rem(cur, 2) == 0 do
            sum - cur
          else
            sum
          end

        new_val = cur + val
        map_updated = Map.put(map, idx, new_val)

        sum_with_new =
          if rem(new_val, 2) == 0 do
            sum_without_cur + new_val
          else
            sum_without_cur
          end

        {{map_updated, sum_with_new}, [sum_with_new | acc]}
      end)

    Enum.reverse(rev_result)
  end

  defp sum_even(list) do
    Enum.reduce(list, 0, fn x, acc ->
      if rem(x, 2) == 0, do: acc + x, else: acc
    end)
  end
end
```
