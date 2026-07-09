# 2780. Minimum Index of a Valid Split

## Cpp

```cpp
class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return -1;
        
        // Boyer-Moore to find candidate majority element
        int cand = nums[0];
        int cnt = 0;
        for (int v : nums) {
            if (cnt == 0) {
                cand = v;
                cnt = 1;
            } else if (v == cand) {
                ++cnt;
            } else {
                --cnt;
            }
        }
        
        // Count total occurrences of candidate
        int total = 0;
        for (int v : nums) if (v == cand) ++total;
        // Given problem guarantees a dominant element, so cand is valid
        
        int leftCnt = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] == cand) ++leftCnt;
            int leftSize = i + 1;
            int rightSize = n - leftSize;
            int rightCnt = total - leftCnt;
            if (leftCnt * 2 > leftSize && rightCnt * 2 > rightSize)
                return i;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minimumIndex(java.util.List<Integer> nums) {
        int n = nums.size();
        // Find the dominant element using Boyer-Moore majority vote
        int candidate = 0;
        int cnt = 0;
        for (int num : nums) {
            if (cnt == 0) {
                candidate = num;
                cnt = 1;
            } else if (num == candidate) {
                cnt++;
            } else {
                cnt--;
            }
        }

        // Count total occurrences of the dominant element
        int total = 0;
        for (int num : nums) {
            if (num == candidate) total++;
        }

        int leftCount = 0;
        for (int i = 0; i < n - 1; i++) { // split must leave non‑empty right part
            if (nums.get(i) == candidate) leftCount++;
            int rightCount = total - leftCount;
            int leftSize = i + 1;
            int rightSize = n - leftSize;
            if (leftCount * 2 > leftSize && rightCount * 2 > rightSize) {
                return i;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Find the dominant element using Boyer-Moore majority vote
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Total occurrences of the dominant element
        total = sum(1 for x in nums if x == candidate)

        left_cnt = 0
        for i, num in enumerate(nums):
            if num == candidate:
                left_cnt += 1
            left_len = i + 1
            right_len = n - left_len
            if right_len == 0:   # cannot split after the last element
                break
            if left_cnt * 2 > left_len and (total - left_cnt) * 2 > right_len:
                return i
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the dominant element using Boyer-Moore majority vote
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Total occurrences of the dominant element
        total = sum(1 for x in nums if x == candidate)

        left_cnt = 0
        for i in range(n - 1):  # split must leave at least one element on the right
            if nums[i] == candidate:
                left_cnt += 1
            left_len = i + 1
            right_len = n - left_len
            if left_cnt * 2 > left_len and (total - left_cnt) * 2 > right_len:
                return i
        return -1
```

## C

```c
int minimumIndex(int* nums, int numsSize) {
    if (numsSize <= 1) return -1;

    // Boyer-Moore to find the majority candidate
    int cand = 0;
    int cnt = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (cnt == 0) {
            cand = nums[i];
            cnt = 1;
        } else if (nums[i] == cand) {
            ++cnt;
        } else {
            --cnt;
        }
    }

    // Count total occurrences of the candidate
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == cand) ++total;
    }

    int leftCnt = 0;
    for (int i = 0; i < numsSize - 1; ++i) { // split must leave non‑empty right part
        if (nums[i] == cand) ++leftCnt;
        int rightCnt = total - leftCnt;

        int leftLen = i + 1;
        int rightLen = numsSize - leftLen;

        if (leftCnt * 2 > leftLen && rightCnt * 2 > rightLen)
            return i;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumIndex(IList<int> nums) {
        int n = nums.Count;
        if (n < 2) return -1;

        // Find the dominant element using Boyer-Moore majority vote
        int candidate = nums[0];
        int count = 0;
        foreach (int v in nums) {
            if (count == 0) {
                candidate = v;
                count = 1;
            } else if (v == candidate) {
                count++;
            } else {
                count--;
            }
        }

        // Count total occurrences of the dominant element
        int total = 0;
        foreach (int v in nums) {
            if (v == candidate) total++;
        }

        // Scan for the earliest valid split
        int leftCount = 0;
        for (int i = 0; i < n - 1; i++) { // ensure both parts are non‑empty
            if (nums[i] == candidate) leftCount++;

            int leftSize = i + 1;
            int rightSize = n - leftSize;
            int rightCount = total - leftCount;

            if (leftCount * 2 > leftSize && rightCount * 2 > rightSize)
                return i;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumIndex = function(nums) {
    const n = nums.length;
    if (n < 2) return -1;

    // Boyer-Moore to find the dominant element candidate
    let cand = nums[0];
    let cnt = 0;
    for (const v of nums) {
        if (cnt === 0) {
            cand = v;
            cnt = 1;
        } else if (v === cand) {
            cnt++;
        } else {
            cnt--;
        }
    }

    // Count total occurrences of the candidate
    let total = 0;
    for (const v of nums) {
        if (v === cand) total++;
    }

    // Scan for earliest valid split
    let leftCount = 0;
    for (let i = 0; i < n - 1; i++) { // ensure second part non‑empty
        if (nums[i] === cand) leftCount++;
        const rightCount = total - leftCount;

        const leftSize = i + 1;
        const rightSize = n - leftSize;

        if (leftCount * 2 > leftSize && rightCount * 2 > rightSize) {
            return i;
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minimumIndex(nums: number[]): number {
    const n = nums.length;
    if (n <= 1) return -1;

    // Boyer-Moore to find the dominant element
    let candidate = nums[0];
    let count = 0;
    for (const num of nums) {
        if (count === 0) {
            candidate = num;
            count = 1;
        } else if (num === candidate) {
            count++;
        } else {
            count--;
        }
    }

    // Total frequency of the dominant element
    let totalFreq = 0;
    for (const num of nums) {
        if (num === candidate) totalFreq++;
    }

    // Find minimal valid split index
    let leftFreq = 0;
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] === candidate) leftFreq++;
        const leftSize = i + 1;
        const rightSize = n - leftSize;
        const rightFreq = totalFreq - leftFreq;

        if (leftFreq * 2 > leftSize && rightFreq * 2 > rightSize) {
            return i;
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumIndex($nums) {
        $n = count($nums);
        // Find the dominant (majority) element using Boyer-Moore
        $candidate = null;
        $cnt = 0;
        foreach ($nums as $num) {
            if ($cnt == 0) {
                $candidate = $num;
                $cnt = 1;
            } else {
                if ($num === $candidate) {
                    $cnt++;
                } else {
                    $cnt--;
                }
            }
        }

        // Count total occurrences of the candidate
        $total = 0;
        foreach ($nums as $num) {
            if ($num === $candidate) {
                $total++;
            }
        }

        // Scan for the earliest valid split
        $prefixCount = 0;
        for ($i = 0; $i < $n - 1; $i++) { // ensure both parts are non‑empty
            if ($nums[$i] === $candidate) {
                $prefixCount++;
            }
            $leftSize = $i + 1;
            $rightSize = $n - $i - 1;
            $rightCount = $total - $prefixCount;

            if ($prefixCount * 2 > $leftSize && $rightCount * 2 > $rightSize) {
                return $i;
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumIndex(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 2 { return -1 }
        
        // Find the dominant (majority) element using Boyer-Moore
        var candidate = 0
        var count = 0
        for num in nums {
            if count == 0 {
                candidate = num
                count = 1
            } else if num == candidate {
                count += 1
            } else {
                count -= 1
            }
        }
        
        // Count total occurrences of the candidate
        var total = 0
        for num in nums where num == candidate {
            total += 1
        }
        
        // Scan for the earliest valid split
        var leftCount = 0
        for i in 0..<(n - 1) {   // split must leave a non‑empty right part
            if nums[i] == candidate {
                leftCount += 1
            }
            let leftSize = i + 1
            let rightSize = n - leftSize
            if leftCount * 2 > leftSize && (total - leftCount) * 2 > rightSize {
                return i
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumIndex(nums: List<Int>): Int {
        val n = nums.size
        // Find the dominant element using Boyer-Moore majority vote
        var candidate = 0
        var count = 0
        for (num in nums) {
            if (count == 0) {
                candidate = num
                count = 1
            } else {
                if (num == candidate) count++ else count--
            }
        }
        // Total occurrences of the dominant element
        var total = 0
        for (num in nums) {
            if (num == candidate) total++
        }
        var leftCount = 0
        // Check each possible split index (i from 0 to n-2)
        for (i in 0 until n - 1) {
            if (nums[i] == candidate) leftCount++
            val leftSize = i + 1
            val rightSize = n - leftSize
            val rightCount = total - leftCount
            if (leftCount * 2 > leftSize && rightCount * 2 > rightSize) {
                return i
            }
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minimumIndex(List<int> nums) {
    int n = nums.length;
    // Find the dominant element using Boyer-Moore majority vote
    int candidate = nums[0];
    int cnt = 0;
    for (int num in nums) {
      if (cnt == 0) {
        candidate = num;
        cnt = 1;
      } else if (num == candidate) {
        cnt++;
      } else {
        cnt--;
      }
    }

    // Count total occurrences of the dominant element
    int total = 0;
    for (int num in nums) {
      if (num == candidate) total++;
    }

    // Scan for the earliest valid split
    int prefix = 0;
    for (int i = 0; i < n - 1; ++i) {
      if (nums[i] == candidate) prefix++;
      int leftSize = i + 1;
      int rightSize = n - leftSize;
      if (prefix * 2 > leftSize && (total - prefix) * 2 > rightSize) {
        return i;
      }
    }
    return -1;
  }
}
```

## Golang

```go
func minimumIndex(nums []int) int {
    n := len(nums)
    if n < 2 {
        return -1
    }
    // Boyer-Moore to find majority candidate
    cand, cnt := 0, 0
    for _, v := range nums {
        if cnt == 0 {
            cand = v
            cnt = 1
        } else if v == cand {
            cnt++
        } else {
            cnt--
        }
    }
    // Count total occurrences of candidate
    total := 0
    for _, v := range nums {
        if v == cand {
            total++
        }
    }
    // Scan for earliest valid split
    pref := 0
    for i, v := range nums[:n-1] { // split index i, right part non‑empty
        if v == cand {
            pref++
        }
        leftSize := i + 1
        rightSize := n - leftSize
        if pref*2 > leftSize && (total-pref)*2 > rightSize {
            return i
        }
    }
    return -1
}
```

## Ruby

```ruby
def minimum_index(nums)
  n = nums.length
  return -1 if n < 2

  # Boyer-Moore to find the dominant element (majority candidate)
  candidate = nil
  count = 0
  nums.each do |num|
    if count == 0
      candidate = num
      count = 1
    elsif num == candidate
      count += 1
    else
      count -= 1
    end
  end

  # Total occurrences of the dominant element
  total = 0
  nums.each { |num| total += 1 if num == candidate }

  left_cnt = 0
  nums.each_with_index do |num, i|
    left_cnt += 1 if num == candidate
    left_size = i + 1
    right_size = n - left_size
    next if right_size == 0

    if left_cnt * 2 > left_size && (total - left_cnt) * 2 > right_size
      return i
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
  def minimumIndex(nums: List[Int]): Int = {
    val n = nums.length
    if (n <= 1) return -1

    val arr = nums.toArray

    // Find the dominant element using Boyer-Moore majority vote
    var candidate = 0
    var cnt = 0
    for (v <- arr) {
      if (cnt == 0) {
        candidate = v
        cnt = 1
      } else if (v == candidate) {
        cnt += 1
      } else {
        cnt -= 1
      }
    }

    // Count total occurrences of the dominant element
    var total = 0
    for (v <- arr) if (v == candidate) total += 1

    var leftCount = 0
    var i = 0
    while (i < n - 1) {
      if (arr(i) == candidate) leftCount += 1
      val leftSize = i + 1
      val rightSize = n - leftSize
      val rightCount = total - leftCount
      if (leftCount * 2 > leftSize && rightCount * 2 > rightSize) return i
      i += 1
    }
    -1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        // Find the dominant element using Boyer-Moore voting algorithm
        let mut candidate = 0;
        let mut count = 0;
        for &num in &nums {
            if count == 0 {
                candidate = num;
                count = 1;
            } else if num == candidate {
                count += 1;
            } else {
                count -= 1;
            }
        }

        // Count total occurrences of the dominant element
        let mut total = 0usize;
        for &num in &nums {
            if num == candidate {
                total += 1;
            }
        }

        // Scan for the earliest valid split
        let mut left_cnt = 0usize;
        for i in 0..n - 1 {
            if nums[i] == candidate {
                left_cnt += 1;
            }
            let left_len = i + 1;
            let right_len = n - left_len;
            let right_cnt = total - left_cnt;

            if left_cnt * 2 > left_len && right_cnt * 2 > right_len {
                return i as i32;
            }
        }

        -1
    }
}
```

## Racket

```racket
(define/contract (minimum-index nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         ;; Boyer-Moore to find the majority element
         (candidate
           (let loop ((lst nums) (cand #f) (cnt 0))
             (if (null? lst)
                 cand
                 (let ((x (car lst)))
                   (cond [(= cnt 0) (loop (cdr lst) x 1)]
                         [(= x cand) (loop (cdr lst) cand (+ cnt 1))]
                         [else (loop (cdr lst) cand (- cnt 1))]))))
         )
    ;; total occurrences of the candidate
    (let ((total
            (let loop ((lst nums) (acc 0))
              (if (null? lst)
                  acc
                  (loop (cdr lst) (+ acc (if (= (car lst) candidate) 1 0)))))))
      ;; scan for earliest valid split
      (let loop ((lst nums) (idx 0) (left 0))
        (if (null? lst)
            -1
            (let* ((new-left (if (= (car lst) candidate) (+ left 1) left))
                   (left-size (+ idx 1))
                   (right-size (- n left-size)))
              (if (and (> (* new-left 2) left-size)
                       (> (* (- total new-left) 2) right-size))
                  idx
                  (loop (cdr lst) (+ idx 1) new-left))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_index/1]).

-spec minimum_index(Nums :: [integer()]) -> integer().
minimum_index(Nums) ->
    X = candidate(Nums),
    Total = count_x(X, Nums),
    N = length(Nums),
    find_split(Nums, X, Total, N, 0, 0).

candidate(List) -> candidate(List, undefined, 0).
candidate([], Cand, _) -> Cand;
candidate([H|T], Cand, Cnt) ->
    case Cnt of
        0 -> candidate(T, H, 1);
        _ when H =:= Cand -> candidate(T, Cand, Cnt + 1);
        _ -> candidate(T, Cand, Cnt - 1)
    end.

count_x(X, List) ->
    lists:foldl(fun(E, Acc) ->
                        if E =:= X -> Acc + 1; true -> Acc end
                end, 0, List).

find_split(_, _, _, N, Index, _) when Index >= N - 1 ->
    -1;
find_split([H|T], X, Total, N, Index, Prefix) ->
    NewPrefix = case H of
                    _ when H =:= X -> Prefix + 1;
                    _ -> Prefix
                end,
    LenFirst = Index + 1,
    LenSecond = N - LenFirst,
    if (NewPrefix * 2 > LenFirst) andalso ((Total - NewPrefix) * 2 > LenSecond) ->
            Index;
       true ->
            find_split(T, X, Total, N, Index + 1, NewPrefix)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_index(nums :: [integer]) :: integer
  def minimum_index(nums) do
    n = length(nums)

    if n < 2 do
      -1
    else
      # Find the dominant element using Boyer-Moore majority vote
      {candidate, _} =
        Enum.reduce(nums, {nil, 0}, fn num, {cand, cnt} ->
          cond do
            cnt == 0 -> {num, 1}
            num == cand -> {cand, cnt + 1}
            true -> {cand, cnt - 1}
          end
        end)

      total = Enum.count(nums, &(&1 == candidate))

      # Scan for the earliest valid split index
      {ans, _} =
        Enum.reduce_while(Enum.with_index(nums), {-1, 0}, fn {num, idx},
                                                            {_prev_ans, left_cnt} ->
          new_left_cnt = if num == candidate, do: left_cnt + 1, else: left_cnt
          left_len = idx + 1
          right_len = n - left_len

          if left_len < n and
               new_left_cnt * 2 > left_len and
               (total - new_left_cnt) * 2 > right_len do
            {:halt, {idx, new_left_cnt}}
          else
            {:cont, {_prev_ans, new_left_cnt}}
          end
        end)

      ans
    end
  end
end
```
