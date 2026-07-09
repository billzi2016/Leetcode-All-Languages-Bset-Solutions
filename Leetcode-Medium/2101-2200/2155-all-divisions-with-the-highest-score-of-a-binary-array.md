# 2155. All Divisions With the Highest Score of a Binary Array

## Cpp

```cpp
class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        int n = nums.size();
        int totalOnes = 0;
        for (int v : nums) if (v == 1) ++totalOnes;
        
        int leftZeros = 0, leftOnes = 0;
        int best = -1;
        vector<int> ans;
        
        for (int i = 0; i <= n; ++i) {
            int score = leftZeros + (totalOnes - leftOnes);
            if (score > best) {
                best = score;
                ans.clear();
                ans.push_back(i);
            } else if (score == best) {
                ans.push_back(i);
            }
            if (i == n) break;
            if (nums[i] == 0) ++leftZeros;
            else ++leftOnes;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> maxScoreIndices(int[] nums) {
        int n = nums.length;
        int totalOnes = 0;
        for (int num : nums) {
            if (num == 1) totalOnes++;
        }
        int zerosLeft = 0, onesLeft = 0;
        int maxScore = -1;
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            int score = zerosLeft + (totalOnes - onesLeft);
            if (score > maxScore) {
                maxScore = score;
                result.clear();
                result.add(i);
            } else if (score == maxScore) {
                result.add(i);
            }
            if (i < n) {
                if (nums[i] == 0) zerosLeft++;
                else onesLeft++;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_ones = sum(nums)
        left_zeros = 0
        left_ones = 0
        max_score = -1
        result = []
        n = len(nums)
        for i in range(n + 1):
            score = left_zeros + (total_ones - left_ones)
            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)
            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    left_ones += 1
        return result
```

## Python3

```python
from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)
        zeros_left = 0
        ones_left = 0
        max_score = total_ones  # score for division at index 0
        result = [0]

        for i, v in enumerate(nums):
            if v == 0:
                zeros_left += 1
            else:
                ones_left += 1
            score = zeros_left + (total_ones - ones_left)  # division after position i (index i+1)
            if score > max_score:
                max_score = score
                result = [i + 1]
            elif score == max_score:
                result.append(i + 1)

        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxScoreIndices(int* nums, int numsSize, int* returnSize) {
    int totalOnes = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) totalOnes++;
    }

    int leftZeros = 0, leftOnes = 0;
    int maxScore = -1;

    // First pass: find maximum score
    for (int i = 0; i <= numsSize; ++i) {
        int rightOnes = totalOnes - leftOnes;
        int score = leftZeros + rightOnes;
        if (score > maxScore) maxScore = score;

        if (i < numsSize) {
            if (nums[i] == 0) leftZeros++;
            else leftOnes++;
        }
    }

    // Second pass: collect indices with maximum score
    int* result = (int*)malloc((numsSize + 1) * sizeof(int));
    int idx = 0;
    leftZeros = 0; leftOnes = 0;

    for (int i = 0; i <= numsSize; ++i) {
        int rightOnes = totalOnes - leftOnes;
        int score = leftZeros + rightOnes;
        if (score == maxScore) {
            result[idx++] = i;
        }

        if (i < numsSize) {
            if (nums[i] == 0) leftZeros++;
            else leftOnes++;
        }
    }

    *returnSize = idx;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> MaxScoreIndices(int[] nums) {
        int n = nums.Length;
        int totalOnes = 0;
        foreach (int v in nums) {
            if (v == 1) totalOnes++;
        }

        List<int> result = new List<int>();
        int maxScore = -1;
        int leftZeros = 0, leftOnes = 0;

        for (int i = 0; i <= n; i++) {
            int score = leftZeros + (totalOnes - leftOnes);
            if (score > maxScore) {
                maxScore = score;
                result.Clear();
                result.Add(i);
            } else if (score == maxScore) {
                result.Add(i);
            }

            if (i < n) {
                if (nums[i] == 0) leftZeros++;
                else leftOnes++;
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
var maxScoreIndices = function(nums) {
    const n = nums.length;
    let totalOnes = 0;
    for (const v of nums) if (v === 1) totalOnes++;
    
    let leftZeros = 0, leftOnes = 0;
    let maxScore = -Infinity;
    const result = [];
    
    // division at index 0
    let score = totalOnes; // leftZeros=0, right ones = totalOnes
    maxScore = score;
    result.push(0);
    
    for (let i = 1; i <= n; ++i) {
        const val = nums[i - 1];
        if (val === 0) leftZeros++;
        else leftOnes++;
        
        score = leftZeros + (totalOnes - leftOnes);
        if (score > maxScore) {
            maxScore = score;
            result.length = 0;
            result.push(i);
        } else if (score === maxScore) {
            result.push(i);
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function maxScoreIndices(nums: number[]): number[] {
    const totalOnes = nums.reduce((sum, v) => sum + v, 0);
    let leftZeros = 0;
    let leftOnes = 0;
    let maxScore = -1;
    const result: number[] = [];
    for (let i = 0; i <= nums.length; i++) {
        const score = leftZeros + (totalOnes - leftOnes);
        if (score > maxScore) {
            maxScore = score;
            result.length = 0;
            result.push(i);
        } else if (score === maxScore) {
            result.push(i);
        }
        if (i < nums.length) {
            if (nums[i] === 0) leftZeros++;
            else leftOnes++;
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
    function maxScoreIndices($nums) {
        $n = count($nums);
        $totalOnes = 0;
        foreach ($nums as $v) {
            if ($v == 1) {
                $totalOnes++;
            }
        }

        $leftZeros = 0;
        $leftOnes = 0;
        $maxScore = -1;
        $result = [];

        for ($i = 0; $i <= $n; $i++) {
            $score = $leftZeros + ($totalOnes - $leftOnes);
            if ($score > $maxScore) {
                $maxScore = $score;
                $result = [$i];
            } elseif ($score == $maxScore) {
                $result[] = $i;
            }

            if ($i < $n) {
                if ($nums[$i] == 0) {
                    $leftZeros++;
                } else {
                    $leftOnes++;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maxScoreIndices(_ nums: [Int]) -> [Int] {
        let n = nums.count
        let totalOnes = nums.reduce(0, +)
        var leftZeros = 0
        var leftOnes = 0
        var maxScore = -1
        var result: [Int] = []
        
        for i in 0...n {
            let score = leftZeros + (totalOnes - leftOnes)
            if score > maxScore {
                maxScore = score
                result = [i]
            } else if score == maxScore {
                result.append(i)
            }
            
            if i < n {
                if nums[i] == 0 {
                    leftZeros += 1
                } else {
                    leftOnes += 1
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
    fun maxScoreIndices(nums: IntArray): List<Int> {
        val totalOnes = nums.count { it == 1 }
        var leftZeros = 0
        var leftOnes = 0
        var maxScore = -1
        val result = mutableListOf<Int>()
        for (i in 0..nums.size) {
            val score = leftZeros + (totalOnes - leftOnes)
            if (score > maxScore) {
                maxScore = score
                result.clear()
                result.add(i)
            } else if (score == maxScore) {
                result.add(i)
            }
            if (i < nums.size) {
                if (nums[i] == 0) leftZeros++ else leftOnes++
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> maxScoreIndices(List<int> nums) {
    int totalOnes = 0;
    for (int v in nums) {
      if (v == 1) totalOnes++;
    }
    int leftZeros = 0, leftOnes = 0;
    int maxScore = -1;
    List<int> result = [];
    int n = nums.length;
    for (int i = 0; i <= n; ++i) {
      int score = leftZeros + (totalOnes - leftOnes);
      if (score > maxScore) {
        maxScore = score;
        result = [i];
      } else if (score == maxScore) {
        result.add(i);
      }
      if (i < n) {
        if (nums[i] == 0) {
          leftZeros++;
        } else {
          leftOnes++;
        }
      }
    }
    return result;
  }
}
```

## Golang

```go
func maxScoreIndices(nums []int) []int {
    totalOnes := 0
    for _, v := range nums {
        if v == 1 {
            totalOnes++
        }
    }

    leftZeros, leftOnes := 0, 0
    maxScore := -1
    res := []int{}

    // division at index 0
    score := totalOnes
    if score > maxScore {
        maxScore = score
        res = []int{0}
    } else if score == maxScore {
        res = append(res, 0)
    }

    for i := 1; i <= len(nums); i++ {
        if nums[i-1] == 0 {
            leftZeros++
        } else {
            leftOnes++
        }
        score = leftZeros + (totalOnes - leftOnes)
        if score > maxScore {
            maxScore = score
            res = []int{i}
        } else if score == maxScore {
            res = append(res, i)
        }
    }

    return res
}
```

## Ruby

```ruby
def max_score_indices(nums)
  total_ones = nums.count(1)
  left_zero = 0
  left_one = 0
  max_score = -1
  result = []

  (0..nums.length).each do |i|
    score = left_zero + (total_ones - left_one)
    if score > max_score
      max_score = score
      result = [i]
    elsif score == max_score
      result << i
    end

    if i < nums.length
      if nums[i] == 0
        left_zero += 1
      else
        left_one += 1
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def maxScoreIndices(nums: Array[Int]): List[Int] = {
        val totalOnes = nums.count(_ == 1)
        var zerosLeft = 0
        var onesLeft = 0
        var maxScore = -1
        val result = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 0 to nums.length) {
            val score = zerosLeft + (totalOnes - onesLeft)
            if (score > maxScore) {
                maxScore = score
                result.clear()
                result += i
            } else if (score == maxScore) {
                result += i
            }
            if (i < nums.length) {
                if (nums(i) == 0) zerosLeft += 1 else onesLeft += 1
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score_indices(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let total_ones = nums.iter().filter(|&&x| x == 1).count() as i32;
        let mut left_zeros = 0i32;
        let mut left_ones = 0i32;
        let mut max_score = -1i32;
        let mut result: Vec<i32> = Vec::new();

        for i in 0..=n {
            let score = left_zeros + (total_ones - left_ones);
            if score > max_score {
                max_score = score;
                result.clear();
                result.push(i as i32);
            } else if score == max_score {
                result.push(i as i32);
            }
            if i < n {
                if nums[i] == 0 {
                    left_zeros += 1;
                } else {
                    left_ones += 1;
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (max-score-indices nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((vec (list->vector nums))
         (n (vector-length vec))
         (total-ones
          (for/sum ([i (in-range n)]) (vector-ref vec i))))
    (let loop ((i 0) (zeros-left 0) (ones-left 0) (max-score -1) (result '()))
      (if (> i n)
          (reverse result)
          (let* ((score (+ zeros-left (- total-ones ones-left)))
                 (next-zeros
                  (if (< i n)
                      (if (= (vector-ref vec i) 0) (add1 zeros-left) zeros-left)
                      zeros-left))
                 (next-ones
                  (if (< i n)
                      (if (= (vector-ref vec i) 1) (add1 ones-left) ones-left)
                      ones-left)))
            (cond
              [(> score max-score)
               (loop (add1 i) next-zeros next-ones score (list i))]
              [(= score max-score)
               (loop (add1 i) next-zeros next-ones max-score (cons i result))]
              [else
               (loop (add1 i) next-zeros next-ones max-score result)]))))))
```

## Erlang

```erlang
-module(solution).
-export([max_score_indices/1]).

-spec max_score_indices(Nums :: [integer()]) -> [integer()].
max_score_indices(Nums) ->
    TotalOnes = lists:foldl(fun(X, Acc) -> Acc + X end, 0, Nums),
    iterate(Nums, 0, 0, 0, -1, [], TotalOnes).

iterate([], Index, LeftZeros, LeftOnes, MaxScore, ResultAcc, TotalOnes) ->
    Score = LeftZeros + (TotalOnes - LeftOnes),
    case Score > MaxScore of
        true -> lists:reverse([Index]);
        false ->
            case Score == MaxScore of
                true -> lists:reverse([Index | ResultAcc]);
                false -> lists:reverse(ResultAcc)
            end
    end;
iterate([H|T], Index, LeftZeros, LeftOnes, MaxScore, ResultAcc, TotalOnes) ->
    Score = LeftZeros + (TotalOnes - LeftOnes),
    {NewMax, NewRes} =
        if Score > MaxScore ->
                {Score, [Index]};
           Score == MaxScore ->
                {MaxScore, [Index | ResultAcc]};
           true ->
                {MaxScore, ResultAcc}
        end,
    NewLeftZeros = LeftZeros + (case H of 0 -> 1; _ -> 0 end),
    NewLeftOnes = LeftOnes + (case H of 1 -> 1; _ -> 0 end),
    iterate(T, Index+1, NewLeftZeros, NewLeftOnes, NewMax, NewRes, TotalOnes).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score_indices(nums :: [integer]) :: [integer]
  def max_score_indices(nums) do
    total_ones = Enum.sum(nums)

    init_score = total_ones

    {_, indices, _, _} =
      Enum.reduce(Enum.with_index(nums), {init_score, [0], 0, 0}, fn {val, idx},
                                                                   {cur_max, cur_idxs, left_zero,
                                                                    left_one} ->
        new_left_zero = left_zero + if val == 0, do: 1, else: 0
        new_left_one = left_one + if val == 1, do: 1, else: 0

        right_ones = total_ones - new_left_one
        score = new_left_zero + right_ones
        division_idx = idx + 1

        {new_max, new_idxs} =
          cond do
            score > cur_max -> {score, [division_idx]}
            score == cur_max -> {cur_max, [division_idx | cur_idxs]}
            true -> {cur_max, cur_idxs}
          end

        {new_max, new_idxs, new_left_zero, new_left_one}
      end)

    Enum.reverse(indices)
  end
end
```
