# 1567. Maximum Length of Subarray With Positive Product

## Cpp

```cpp
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int n = nums.size();
        int maxLen = 0;
        int start = 0; // start index of current segment without zeros
        while (start < n && nums[start] == 0) ++start;
        while (start < n) {
            int end = start;
            int negCount = 0;
            int firstNeg = -1, lastNeg = -1;
            // expand until next zero or end of array
            while (end < n && nums[end] != 0) {
                if (nums[end] < 0) {
                    ++negCount;
                    if (firstNeg == -1) firstNeg = end;
                    lastNeg = end;
                }
                ++end;
            }
            // segment is [start, end-1]
            int segLen = end - start;
            if (negCount % 2 == 0) {
                maxLen = max(maxLen, segLen);
            } else {
                // remove prefix up to first negative or suffix after last negative
                if (firstNeg != -1) {
                    maxLen = max(maxLen, segLen - (firstNeg - start + 1));
                }
                if (lastNeg != -1) {
                    maxLen = max(maxLen, segLen - (end - lastNeg));
                }
            }
            // move to next segment after zero
            start = end + 1;
            while (start < n && nums[start] == 0) ++start;
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int getMaxLen(int[] nums) {
        int n = nums.length;
        int ans = 0;
        int start = 0;          // index after the last zero
        int firstNeg = -1;      // first negative index in current segment
        int lastNeg = -1;       // last negative index in current segment
        int negCount = 0;       // number of negatives in current segment

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                // reset for next segment
                start = i + 1;
                firstNeg = -1;
                lastNeg = -1;
                negCount = 0;
                continue;
            }

            if (nums[i] < 0) {
                negCount++;
                if (firstNeg == -1) firstNeg = i;
                lastNeg = i;
            }

            if (negCount % 2 == 0) {
                ans = Math.max(ans, i - start + 1);
            } else {
                // exclude prefix up to first negative or suffix from last negative
                int lenExcludingFirst = i - firstNeg;          // remove first negative and everything before it
                int lenExcludingLast = lastNeg - start;       // remove last negative and everything after it
                ans = Math.max(ans, Math.max(lenExcludingFirst, lenExcludingLast));
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0   # length of subarray ending here with positive product
        neg = 0   # length of subarray ending here with negative product
        ans = 0
        for x in nums:
            if x == 0:
                pos = neg = 0
            elif x > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            else:  # x < 0
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            ans = max(ans, pos)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        pos_len = 0   # length of subarray ending here with positive product
        neg_len = 0   # length of subarray ending here with negative product
        
        for num in nums:
            if num == 0:
                pos_len = neg_len = 0
            elif num > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            else:  # num < 0
                new_pos = neg_len + 1 if neg_len > 0 else 0
                new_neg = pos_len + 1
                pos_len, neg_len = new_pos, new_neg
            max_len = max(max_len, pos_len)
        
        return max_len
```

## C

```c
int getMaxLen(int* nums, int numsSize) {
    int pos = 0, neg = 0, ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 0) {
            pos = 0;
            neg = 0;
        } else if (nums[i] > 0) {
            pos = pos + 1;
            if (neg > 0) {
                neg = neg + 1;
            }
        } else { // nums[i] < 0
            int prevPos = pos;
            int prevNeg = neg;
            if (prevNeg > 0) {
                pos = prevNeg + 1;
            } else {
                pos = 0;
            }
            if (prevPos > 0) {
                neg = prevPos + 1;
            } else {
                neg = 1;
            }
        }
        if (pos > ans) ans = pos;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int GetMaxLen(int[] nums) {
        int maxLen = 0;
        int start = 0;          // start index of current non-zero segment
        int firstNeg = -1;      // index of first negative in the segment
        int lastNeg = -1;       // index of last negative in the segment
        int negCount = 0;       // number of negatives in the segment

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 0) {
                // reset segment information
                start = i + 1;
                firstNeg = -1;
                lastNeg = -1;
                negCount = 0;
                continue;
            }

            if (nums[i] < 0) {
                negCount++;
                if (firstNeg == -1) firstNeg = i;
                lastNeg = i;
            }

            int curLen;
            if ((negCount & 1) == 0) { // even number of negatives
                curLen = i - start + 1;
            } else {
                // exclude prefix up to first negative or suffix after last negative
                int lenExcludingPrefix = i - firstNeg;      // remove up to first negative inclusive
                int lenExcludingSuffix = lastNeg - start;   // remove from last negative onward
                curLen = Math.Max(lenExcludingPrefix, lenExcludingSuffix);
            }

            if (curLen > maxLen) maxLen = curLen;
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var getMaxLen = function(nums) {
    let pos = 0, neg = 0, ans = 0;
    for (const x of nums) {
        if (x > 0) {
            pos += 1;
            if (neg > 0) neg += 1;
        } else if (x < 0) {
            const newPos = neg > 0 ? neg + 1 : 0;
            const newNeg = pos + 1;
            pos = newPos;
            neg = newNeg;
        } else { // x === 0
            pos = 0;
            neg = 0;
        }
        if (pos > ans) ans = pos;
    }
    return ans;
};
```

## Typescript

```typescript
function getMaxLen(nums: number[]): number {
    const n = nums.length;
    let ans = 0;
    let i = 0;

    while (i < n) {
        // skip zeros
        while (i < n && nums[i] === 0) i++;
        if (i >= n) break;

        const start = i;
        let negCount = 0;
        let firstNeg = -1;
        let lastNeg = -1;

        // process segment without zeros
        while (i < n && nums[i] !== 0) {
            if (nums[i] < 0) {
                negCount++;
                if (firstNeg === -1) firstNeg = i;
                lastNeg = i;
            }
            i++;
        }

        const segLen = i - start; // length of current zero-free segment

        if (negCount % 2 === 0) {
            ans = Math.max(ans, segLen);
        } else {
            // remove prefix up to first negative or suffix from last negative
            const option1 = i - 1 - firstNeg; // exclude prefix including firstNeg
            const option2 = lastNeg - start;   // exclude suffix starting at lastNeg
            ans = Math.max(ans, option1, option2);
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function getMaxLen($nums) {
        $n = count($nums);
        $maxLen = 0;
        $start = 0;
        $firstNeg = -1;
        $lastNeg = -1;
        $negCount = 0;

        for ($i = 0; $i <= $n; $i++) {
            if ($i == $n || $nums[$i] == 0) {
                $len = $i - $start;
                if ($len > 0) {
                    if ($negCount % 2 == 0) {
                        if ($len > $maxLen) {
                            $maxLen = $len;
                        }
                    } else {
                        $removePrefix = $firstNeg - $start + 1;
                        $removeSuffix = $i - 1 - $lastNeg + 1;
                        $cand1 = $len - $removePrefix;
                        $cand2 = $len - $removeSuffix;
                        $candidate = max($cand1, $cand2);
                        if ($candidate > $maxLen) {
                            $maxLen = $candidate;
                        }
                    }
                }
                // reset for next segment
                $start = $i + 1;
                $firstNeg = -1;
                $lastNeg = -1;
                $negCount = 0;
            } else {
                if ($nums[$i] < 0) {
                    $negCount++;
                    if ($firstNeg == -1) {
                        $firstNeg = $i;
                    }
                    $lastNeg = $i;
                }
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func getMaxLen(_ nums: [Int]) -> Int {
        var maxLen = 0
        var start = 0               // start index of current segment (after last zero)
        var negCount = 0
        var firstNeg = -1
        var lastNeg = -1
        
        for i in 0..<nums.count {
            let val = nums[i]
            if val == 0 {
                // reset segment
                start = i + 1
                negCount = 0
                firstNeg = -1
                lastNeg = -1
                continue
            }
            
            if val < 0 {
                negCount += 1
                if firstNeg == -1 { firstNeg = i }
                lastNeg = i
            }
            
            if negCount % 2 == 0 {
                // whole segment up to i has positive product
                maxLen = max(maxLen, i - start + 1)
            } else {
                // exclude prefix up to first negative or suffix after last negative
                if firstNeg != -1 {
                    maxLen = max(maxLen, i - firstNeg)
                }
                if lastNeg != -1 {
                    maxLen = max(maxLen, lastNeg - start)
                }
            }
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMaxLen(nums: IntArray): Int {
        var ans = 0
        var i = 0
        val n = nums.size
        while (i < n) {
            if (nums[i] == 0) {
                i++
                continue
            }
            var start = i
            var negCount = 0
            var firstNeg = -1
            var lastNeg = -1
            while (i < n && nums[i] != 0) {
                if (nums[i] < 0) {
                    negCount++
                    if (firstNeg == -1) firstNeg = i
                    lastNeg = i
                }
                i++
            }
            val end = i - 1 // inclusive
            if (negCount % 2 == 0) {
                ans = maxOf(ans, end - start + 1)
            } else {
                val len1 = end - firstNeg // exclude prefix up to first negative
                val len2 = lastNeg - start // exclude suffix from last negative
                ans = maxOf(ans, len1, len2)
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int getMaxLen(List<int> nums) {
    int pos = 0, neg = 0, ans = 0;
    for (int x in nums) {
      if (x == 0) {
        pos = 0;
        neg = 0;
      } else if (x > 0) {
        pos = pos + 1;
        neg = (neg > 0) ? neg + 1 : 0;
      } else { // x < 0
        int newPos = (neg > 0) ? neg + 1 : 0;
        int newNeg = pos + 1;
        pos = newPos;
        neg = newNeg;
      }
      if (pos > ans) ans = pos;
    }
    return ans;
  }
}
```

## Golang

```go
func getMaxLen(nums []int) int {
    n := len(nums)
    ans := 0
    i := 0
    for i < n {
        if nums[i] == 0 {
            i++
            continue
        }
        start := i
        negCount := 0
        firstNeg, lastNeg := -1, -1
        for i < n && nums[i] != 0 {
            if nums[i] < 0 {
                negCount++
                if firstNeg == -1 {
                    firstNeg = i
                }
                lastNeg = i
            }
            i++
        }
        segLen := i - start
        if negCount%2 == 0 {
            if segLen > ans {
                ans = segLen
            }
        } else {
            // exclude prefix up to first negative
            len1 := i - 1 - firstNeg
            if len1 > ans {
                ans = len1
            }
            // exclude suffix after last negative
            len2 := lastNeg - start
            if len2 > ans {
                ans = len2
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def get_max_len(nums)
  max_len = 0
  start = 0
  neg_count = 0
  first_neg = -1
  last_neg = -1

  nums.each_with_index do |val, i|
    if val == 0
      seg_len = i - start
      if seg_len > 0
        if (neg_count & 1) == 0
          max_len = [max_len, seg_len].max
        else
          len1 = i - (first_neg + 1)
          len2 = last_neg - start
          max_len = [max_len, len1, len2].max
        end
      end
      start = i + 1
      neg_count = 0
      first_neg = -1
      last_neg = -1
    else
      if val < 0
        neg_count += 1
        first_neg = i if first_neg == -1
        last_neg = i
      end
    end
  end

  seg_len = nums.length - start
  if seg_len > 0
    if (neg_count & 1) == 0
      max_len = [max_len, seg_len].max
    else
      len1 = nums.length - (first_neg + 1)
      len2 = last_neg - start
      max_len = [max_len, len1, len2].max
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def getMaxLen(nums: Array[Int]): Int = {
        var maxLen = 0
        var start = 0               // index after the last zero
        var negCount = 0
        var firstNeg = -1
        var lastNeg = -1

        for (i <- nums.indices) {
            val v = nums(i)
            if (v == 0) {
                // reset segment
                start = i + 1
                negCount = 0
                firstNeg = -1
                lastNeg = -1
            } else {
                if (v < 0) {
                    negCount += 1
                    if (firstNeg == -1) firstNeg = i
                    lastNeg = i
                }
                if (negCount % 2 == 0) {
                    maxLen = math.max(maxLen, i - start + 1)
                } else {
                    // exclude prefix up to first negative or suffix after last negative
                    val len1 = i - firstNeg
                    val len2 = lastNeg - start
                    maxLen = math.max(maxLen, math.max(len1, len2))
                }
            }
        }

        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_max_len(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut max_len: i32 = 0;
        let mut i = 0usize;

        while i < n {
            if nums[i] == 0 {
                i += 1;
                continue;
            }
            // start of a non‑zero segment
            let start = i;
            let mut cnt_neg = 0usize;
            let mut first_neg: Option<usize> = None;
            let mut last_neg = start; // placeholder, will be set when a negative appears

            while i < n && nums[i] != 0 {
                if nums[i] < 0 {
                    cnt_neg += 1;
                    if first_neg.is_none() {
                        first_neg = Some(i);
                    }
                    last_neg = i;
                }
                i += 1;
            }

            let seg_len = i - start; // length of current segment

            if cnt_neg % 2 == 0 {
                max_len = max_len.max(seg_len as i32);
            } else {
                // remove prefix up to first negative (inclusive)
                if let Some(fn_idx) = first_neg {
                    let len1 = i - fn_idx - 1;
                    max_len = max_len.max(len1 as i32);
                }
                // remove suffix starting from last negative (inclusive)
                let len2 = last_neg - start;
                max_len = max_len.max(len2 as i32);
            }
        }

        max_len
    }
}
```

## Racket

```racket
(define/contract (get-max-len nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let loop ((i 0) (seg-start -1) (neg-count 0) (first-neg -1) (last-neg -1) (max-len 0))
      (if (> i n)
          max-len
          (let ([val (if (< i n) (vector-ref v i) 0)]) ; sentinel zero at end
            (if (= val 0)
                (let* ([new-max
                        (if (>= seg-start 0)
                            (let* ([len (- i seg-start)])
                              (if (even? neg-count)
                                  (max max-len len)
                                  (let* ([cand1 (- i (+ first-neg 1))]
                                         [cand2 (- last-neg seg-start)])
                                    (max max-len (max cand1 cand2)))))
                            max-len)])
                  (loop (+ i 1) -1 0 -1 -1 new-max))
                (let* ([new-seg-start (if (= seg-start -1) i seg-start)]
                       [new-neg-count (if (< val 0) (+ neg-count 1) neg-count)]
                       [new-first-neg (if (and (< val 0) (= first-neg -1)) i first-neg)]
                       [new-last-neg (if (< val 0) i last-neg)])
                  (loop (+ i 1) new-seg-start new-neg-count new-first-neg new-last-neg max-len))))))))
```

## Erlang

```erlang
-module(solution).
-export([get_max_len/1]).

-spec get_max_len(Nums :: [integer()]) -> integer().
get_max_len(Nums) ->
    loop(Nums, 0, 0, 0, -1, -1, 0).

loop([], Index, SegStart, NegCount, FirstNeg, LastNeg, Max) ->
    Len = Index - SegStart,
    Candidate = candidate(Len, NegCount, FirstNeg, LastNeg),
    max(Candidate, Max);
loop([H|T], Index, SegStart, NegCount, FirstNeg, LastNeg, Max) when H == 0 ->
    Len = Index - SegStart,
    Candidate = candidate(Len, NegCount, FirstNeg, LastNeg),
    NewMax = max(Candidate, Max),
    loop(T, Index + 1, Index + 1, 0, -1, -1, NewMax);
loop([H|T], Index, SegStart, NegCount, FirstNeg, LastNeg, Max) when H < 0 ->
    RelIdx = Index - SegStart,
    NewFirst = case NegCount of
        0 -> RelIdx;
        _ -> FirstNeg
    end,
    loop(T, Index + 1, SegStart, NegCount + 1, NewFirst, RelIdx, Max);
loop([_H|T], Index, SegStart, NegCount, FirstNeg, LastNeg, Max) ->
    loop(T, Index + 1, SegStart, NegCount, FirstNeg, LastNeg, Max).

candidate(Len, _NegCount, _FirstNeg, _LastNeg) when Len =< 0 -> 0;
candidate(Len, NegCount, FirstNeg, LastNeg) ->
    case NegCount rem 2 of
        0 -> Len;
        1 -> max(Len - FirstNeg - 1, LastNeg)
    end.

max(A, B) when A >= B -> A;
max(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_max_len(nums :: [integer]) :: integer
  def get_max_len(nums) do
    {ans, _, _} =
      Enum.reduce(nums, {0, 0, 0}, fn num, {ans, pos, neg} ->
        cond do
          num == 0 ->
            {ans, 0, 0}

          num > 0 ->
            new_pos = pos + 1
            new_neg = if neg > 0, do: neg + 1, else: 0
            {max(ans, new_pos), new_pos, new_neg}

          true -> # num < 0
            new_pos = if neg > 0, do: neg + 1, else: 0
            new_neg = pos + 1
            {max(ans, new_pos), new_pos, new_neg}
        end
      end)

    ans
  end
end
```
