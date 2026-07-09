# 0229. Majority Element II

## Cpp

```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return {};
        // First pass: find up to two candidates
        int cand1 = 0, cand2 = 1; // initialize with different values
        int cnt1 = 0, cnt2 = 0;
        for (int num : nums) {
            if (cnt1 > 0 && num == cand1) {
                ++cnt1;
            } else if (cnt2 > 0 && num == cand2) {
                ++cnt2;
            } else if (cnt1 == 0) {
                cand1 = num;
                cnt1 = 1;
            } else if (cnt2 == 0) {
                cand2 = num;
                cnt2 = 1;
            } else {
                --cnt1;
                --cnt2;
            }
        }
        // Second pass: verify the candidates
        cnt1 = cnt2 = 0;
        for (int num : nums) {
            if (num == cand1) ++cnt1;
            else if (num == cand2) ++cnt2;
        }
        vector<int> result;
        if (cnt1 > n / 3) result.push_back(cand1);
        if (cnt2 > n / 3) result.push_back(cand2);
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int candidate1 = 0, candidate2 = 1;
        int count1 = 0, count2 = 0;

        for (int num : nums) {
            if (count1 > 0 && num == candidate1) {
                count1++;
            } else if (count2 > 0 && num == candidate2) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        count1 = 0;
        count2 = 0;
        for (int num : nums) {
            if (num == candidate1) {
                count1++;
            } else if (num == candidate2) {
                count2++;
            }
        }

        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        if (count1 > n / 3) result.add(candidate1);
        if (count2 > n / 3) result.add(candidate2);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # First pass: find up to two candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Second pass: verify the candidates
        result = []
        threshold = len(nums) // 3
        for cand in (candidate1, candidate2):
            if cand is not None and nums.count(cand) > threshold:
                result.append(cand)
        
        return result
```

## Python3

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # First pass: find up to two candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Second pass: verify the candidates
        result = []
        threshold = len(nums) // 3
        for cand in (candidate1, candidate2):
            if cand is not None and nums.count(cand) > threshold:
                result.append(cand)
        
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* majorityElement(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 0;
    if (numsSize == 0) {
        return result;
    }
    
    int cand1 = 0, cand2 = 1; // initial dummy values
    int cnt1 = 0, cnt2 = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        int n = nums[i];
        if (cnt1 > 0 && n == cand1) {
            ++cnt1;
        } else if (cnt2 > 0 && n == cand2) {
            ++cnt2;
        } else if (cnt1 == 0) {
            cand1 = n;
            cnt1 = 1;
        } else if (cnt2 == 0) {
            cand2 = n;
            cnt2 = 1;
        } else {
            --cnt1;
            --cnt2;
        }
    }
    
    // Verify the candidates
    cnt1 = cnt2 = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == cand1) ++cnt1;
        else if (nums[i] == cand2) ++cnt2;
    }
    
    int limit = numsSize / 3;
    if (cnt1 > limit) {
        result[(*returnSize)++] = cand1;
    }
    if (cand2 != cand1 && cnt2 > limit) {
        result[(*returnSize)++] = cand2;
    }
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        int count1 = 0, count2 = 0;
        int candidate1 = 0, candidate2 = 1; // initialize to different values

        foreach (int num in nums) {
            if (count1 > 0 && num == candidate1) {
                count1++;
            } else if (count2 > 0 && num == candidate2) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        // Verify the candidates
        count1 = 0;
        count2 = 0;
        foreach (int num in nums) {
            if (num == candidate1) count1++;
            else if (num == candidate2) count2++;
        }

        List<int> result = new List<int>();
        int n = nums.Length;
        if (count1 > n / 3) result.Add(candidate1);
        if (count2 > n / 3) result.Add(candidate2);
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
var majorityElement = function(nums) {
    let candidate1 = null, candidate2 = null;
    let count1 = 0, count2 = 0;

    for (const num of nums) {
        if (candidate1 !== null && num === candidate1) {
            count1++;
        } else if (candidate2 !== null && num === candidate2) {
            count2++;
        } else if (count1 === 0) {
            candidate1 = num;
            count1 = 1;
        } else if (count2 === 0) {
            candidate2 = num;
            count2 = 1;
        } else {
            count1--;
            count2--;
        }
    }

    // Verify the candidates
    count1 = 0;
    count2 = 0;
    for (const num of nums) {
        if (candidate1 !== null && num === candidate1) count1++;
        else if (candidate2 !== null && num === candidate2) count2++;
    }

    const result = [];
    const n = nums.length;
    if (count1 > Math.floor(n / 3)) result.push(candidate1);
    if (candidate2 !== candidate1 && count2 > Math.floor(n / 3)) result.push(candidate2);
    return result;
};
```

## Typescript

```typescript
function majorityElement(nums: number[]): number[] {
    let candidate1 = 0, candidate2 = 0;
    let count1 = 0, count2 = 0;

    for (const num of nums) {
        if (count1 > 0 && num === candidate1) {
            count1++;
        } else if (count2 > 0 && num === candidate2) {
            count2++;
        } else if (count1 === 0) {
            candidate1 = num;
            count1 = 1;
        } else if (count2 === 0) {
            candidate2 = num;
            count2 = 1;
        } else {
            count1--;
            count2--;
        }
    }

    count1 = 0;
    count2 = 0;
    for (const num of nums) {
        if (num === candidate1) count1++;
        else if (num === candidate2) count2++;
    }

    const result: number[] = [];
    const limit = Math.floor(nums.length / 3);
    if (count1 > limit) result.push(candidate1);
    if (candidate2 !== candidate1 && count2 > limit) result.push(candidate2);
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
    function majorityElement($nums) {
        $candidate1 = null;
        $candidate2 = null;
        $count1 = 0;
        $count2 = 0;

        foreach ($nums as $num) {
            if ($candidate1 !== null && $num == $candidate1) {
                $count1++;
            } elseif ($candidate2 !== null && $num == $candidate2) {
                $count2++;
            } elseif ($count1 == 0) {
                $candidate1 = $num;
                $count1 = 1;
            } elseif ($count2 == 0) {
                $candidate2 = $num;
                $count2 = 1;
            } else {
                $count1--;
                $count2--;
            }
        }

        // Verify the candidates
        $cnt1 = 0;
        $cnt2 = 0;
        foreach ($nums as $num) {
            if ($candidate1 !== null && $num == $candidate1) {
                $cnt1++;
            } elseif ($candidate2 !== null && $num == $candidate2) {
                $cnt2++;
            }
        }

        $result = [];
        $n = count($nums);
        $threshold = intdiv($n, 3);

        if ($candidate1 !== null && $cnt1 > $threshold) {
            $result[] = $candidate1;
        }
        if ($candidate2 !== null && $candidate2 != $candidate1 && $cnt2 > $threshold) {
            $result[] = $candidate2;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func majorityElement(_ nums: [Int]) -> [Int] {
        var candidate1 = 0
        var candidate2 = 1
        var count1 = 0
        var count2 = 0
        
        for num in nums {
            if count1 > 0 && num == candidate1 {
                count1 += 1
            } else if count2 > 0 && num == candidate2 {
                count2 += 1
            } else if count1 == 0 {
                candidate1 = num
                count1 = 1
            } else if count2 == 0 {
                candidate2 = num
                count2 = 1
            } else {
                count1 -= 1
                count2 -= 1
            }
        }
        
        count1 = 0
        count2 = 0
        for num in nums {
            if num == candidate1 {
                count1 += 1
            } else if num == candidate2 {
                count2 += 1
            }
        }
        
        var result: [Int] = []
        let n = nums.count
        if count1 > n / 3 {
            result.append(candidate1)
        }
        if candidate2 != candidate1 && count2 > n / 3 {
            result.append(candidate2)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun majorityElement(nums: IntArray): List<Int> {
        var candidate1 = 0
        var candidate2 = 0
        var count1 = 0
        var count2 = 0

        for (num in nums) {
            when {
                count1 > 0 && num == candidate1 -> count1++
                count2 > 0 && num == candidate2 -> count2++
                count1 == 0 -> {
                    candidate1 = num
                    count1 = 1
                }
                count2 == 0 -> {
                    candidate2 = num
                    count2 = 1
                }
                else -> {
                    count1--
                    count2--
                }
            }
        }

        // Verify the candidates
        count1 = 0
        count2 = 0
        for (num in nums) {
            if (num == candidate1) count1++
            else if (num == candidate2) count2++
        }

        val result = mutableListOf<Int>()
        val n = nums.size
        if (count1 > n / 3) result.add(candidate1)
        if (candidate2 != candidate1 && count2 > n / 3) result.add(candidate2)

        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> majorityElement(List<int> nums) {
    int? cand1;
    int? cand2;
    int cnt1 = 0, cnt2 = 0;

    for (int num in nums) {
      if (cand1 != null && num == cand1) {
        cnt1++;
      } else if (cand2 != null && num == cand2) {
        cnt2++;
      } else if (cnt1 == 0) {
        cand1 = num;
        cnt1 = 1;
      } else if (cnt2 == 0) {
        cand2 = num;
        cnt2 = 1;
      } else {
        cnt1--;
        cnt2--;
      }
    }

    cnt1 = 0;
    cnt2 = 0;
    for (int num in nums) {
      if (cand1 != null && num == cand1) {
        cnt1++;
      } else if (cand2 != null && num == cand2) {
        cnt2++;
      }
    }

    List<int> result = [];
    int limit = nums.length ~/ 3;
    if (cand1 != null && cnt1 > limit) result.add(cand1);
    if (cand2 != null && cand2 != cand1 && cnt2 > limit) result.add(cand2);
    return result;
  }
}
```

## Golang

```go
func majorityElement(nums []int) []int {
    var candidate1, candidate2 int
    count1, count2 := 0, 0

    for _, num := range nums {
        if count1 > 0 && num == candidate1 {
            count1++
        } else if count2 > 0 && num == candidate2 {
            count2++
        } else if count1 == 0 {
            candidate1 = num
            count1 = 1
        } else if count2 == 0 {
            candidate2 = num
            count2 = 1
        } else {
            count1--
            count2--
        }
    }

    // Verify the candidates
    count1, count2 = 0, 0
    for _, num := range nums {
        if num == candidate1 {
            count1++
        } else if num == candidate2 {
            count2++
        }
    }

    n := len(nums)
    res := []int{}
    if count1 > n/3 {
        res = append(res, candidate1)
    }
    if count2 > n/3 && candidate2 != candidate1 {
        res = append(res, candidate2)
    }
    return res
}
```

## Ruby

```ruby
def majority_element(nums)
  return [] if nums.empty?

  cand1 = nil
  cand2 = nil
  count1 = 0
  count2 = 0

  nums.each do |num|
    if cand1 == num
      count1 += 1
    elsif cand2 == num
      count2 += 1
    elsif count1 == 0
      cand1 = num
      count1 = 1
    elsif count2 == 0
      cand2 = num
      count2 = 1
    else
      count1 -= 1
      count2 -= 1
    end
  end

  cnt1 = 0
  cnt2 = 0
  nums.each do |num|
    cnt1 += 1 if num == cand1
    cnt2 += 1 if num == cand2
  end

  res = []
  threshold = nums.length / 3
  res << cand1 if count1 > 0 && cnt1 > threshold
  res << cand2 if cand2 != cand1 && count2 > 0 && cnt2 > threshold
  res
end
```

## Scala

```scala
object Solution {
  def majorityElement(nums: Array[Int]): List[Int] = {
    var cand1 = 0
    var cand2 = 0
    var cnt1 = 0
    var cnt2 = 0

    for (num <- nums) {
      if (cnt1 > 0 && num == cand1) {
        cnt1 += 1
      } else if (cnt2 > 0 && num == cand2) {
        cnt2 += 1
      } else if (cnt1 == 0) {
        cand1 = num
        cnt1 = 1
      } else if (cnt2 == 0) {
        cand2 = num
        cnt2 = 1
      } else {
        cnt1 -= 1
        cnt2 -= 1
      }
    }

    var count1 = 0
    var count2 = 0
    for (num <- nums) {
      if (num == cand1) count1 += 1
      else if (num == cand2) count2 += 1
    }

    val n = nums.length
    val res = scala.collection.mutable.ListBuffer[Int]()
    if (count1 > n / 3) res += cand1
    if (cand2 != cand1 && count2 > n / 3) res += cand2

    res.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        let mut count1 = 0;
        let mut count2 = 0;
        let mut candidate1 = 0;
        let mut candidate2 = 0;

        for &num in nums.iter() {
            if count1 > 0 && num == candidate1 {
                count1 += 1;
            } else if count2 > 0 && num == candidate2 {
                count2 += 1;
            } else if count1 == 0 {
                candidate1 = num;
                count1 = 1;
            } else if count2 == 0 {
                candidate2 = num;
                count2 = 1;
            } else {
                count1 -= 1;
                count2 -= 1;
            }
        }

        let mut cnt1 = 0;
        let mut cnt2 = 0;
        for &num in nums.iter() {
            if num == candidate1 {
                cnt1 += 1;
            } else if num == candidate2 {
                cnt2 += 1;
            }
        }

        let threshold = (nums.len() as i32) / 3;
        let mut result = Vec::new();
        if cnt1 > threshold {
            result.push(candidate1);
        }
        if candidate2 != candidate1 && cnt2 > threshold {
            result.push(candidate2);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (majority-element nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (letrec ((first-pass
            (lambda (lst cand1 cnt1 cand2 cnt2)
              (if (null? lst)
                  (values cand1 cnt1 cand2 cnt2)
                  (let ((x (car lst)))
                    (cond
                      [(and (> cnt1 0) (= x cand1))
                       (first-pass (cdr lst) cand1 (+ cnt1 1) cand2 cnt2)]
                      [(and (> cnt2 0) (= x cand2))
                       (first-pass (cdr lst) cand1 cnt1 cand2 (+ cnt2 1))]
                      [(= cnt1 0)
                       (first-pass (cdr lst) x 1 cand2 cnt2)]
                      [(= cnt2 0)
                       (first-pass (cdr lst) cand1 cnt1 x 1)]
                      [else
                       (first-pass (cdr lst) cand1 (- cnt1 1) cand2 (- cnt2 1))]))))))
    (let-values ([(cand1 _ cand2 _) (first-pass nums #f 0 #f 0)])
      (define cnt1 0)
      (define cnt2 0)
      (for ([x nums])
        (when (and cand1 (= x cand1))
          (set! cnt1 (+ cnt1 1)))
        (when (and cand2 (= x cand2))
          (set! cnt2 (+ cnt2 1))))
      (define threshold (quotient (length nums) 3))
      (define res '())
      (when (and cand1 (> cnt1 threshold))
        (set! res (cons cand1 res)))
      (when (and cand2 (> cnt2 threshold) (not (equal? cand2 cand1)))
        (set! res (cons cand2 res)))
      (reverse res))))
```

## Erlang

```erlang
-module(solution).
-export([majority_element/1]).

-spec majority_element(Nums :: [integer()]) -> [integer()].
majority_element([]) ->
    [];
majority_element(Nums) ->
    {Cand1, _, Cand2, _} = lists:foldl(fun update/2, {undefined,0,undefined,0}, Nums),
    {Count1, Count2} = count_candidates(Nums, Cand1, Cand2, 0, 0),
    Threshold = length(Nums) div 3,
    Result0 = [],
    Result1 = if Count1 > Threshold, Cand1 =/= undefined -> [Cand1 | Result0]; true -> Result0 end,
    Result2 = if Count2 > Threshold, Cand2 =/= undefined, Cand2 =/= Cand1 -> [Cand2 | Result1]; true -> Result1 end,
    lists:reverse(Result2).

update(X, {Cand1, 0, Cand2, C2}) ->
    {X, 1, Cand2, C2};
update(X, {Cand1, C1, Cand2, 0}) ->
    {Cand1, C1, X, 1};
update(X, {Cand1, C1, Cand2, C2}) when X =:= Cand1 ->
    {Cand1, C1 + 1, Cand2, C2};
update(X, {Cand1, C1, Cand2, C2}) when X =:= Cand2 ->
    {Cand1, C1, Cand2, C2 + 1};
update(_X, {Cand1, C1, Cand2, C2}) ->
    {Cand1, C1 - 1, Cand2, C2 - 1}.

count_candidates([], _Cand1, _Cand2, Acc1, Acc2) ->
    {Acc1, Acc2};
count_candidates([X|Rest], Cand1, Cand2, Acc1, Acc2) ->
    NewAcc1 = if X =:= Cand1 -> Acc1 + 1; true -> Acc1 end,
    NewAcc2 = if X =:= Cand2 -> Acc2 + 1; true -> Acc2 end,
    count_candidates(Rest, Cand1, Cand2, NewAcc1, NewAcc2).
```

## Elixir

```elixir
defmodule Solution do
  @spec majority_element(nums :: [integer]) :: [integer]
  def majority_element(nums) do
    {c1, c2, cnt1, cnt2} =
      Enum.reduce(nums, {nil, nil, 0, 0}, fn num, {cand1, cand2, count1, count2} ->
        cond do
          count1 > 0 and num == cand1 -> {cand1, cand2, count1 + 1, count2}
          count2 > 0 and num == cand2 -> {cand1, cand2, count1, count2 + 1}
          count1 == 0 -> {num, cand2, 1, count2}
          count2 == 0 -> {cand1, num, count1, 1}
          true -> {cand1, cand2, count1 - 1, count2 - 1}
        end
      end)

    n = length(nums)
    threshold = div(n, 3)

    result =
      []
      |> maybe_add(c1, nums, threshold)
      |> maybe_add(c2, nums, threshold)

    Enum.reverse(result)
  end

  defp maybe_add(acc, nil, _nums, _threshold), do: acc
  defp maybe_add(acc, cand, nums, threshold) do
    if Enum.count(nums, fn x -> x == cand end) > threshold and not Enum.member?(acc, cand) do
      [cand | acc]
    else
      acc
    end
  end
end
```
