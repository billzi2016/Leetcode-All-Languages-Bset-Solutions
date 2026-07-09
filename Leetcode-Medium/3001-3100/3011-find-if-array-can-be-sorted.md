# 3011. Find if Array Can Be Sorted

## Cpp

```cpp
class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        for (size_t i = 0; i < nums.size(); ++i) {
            if (__builtin_popcount(nums[i]) != __builtin_popcount(sorted[i]))
                return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canSortArray(int[] nums) {
        int n = nums.length;
        int[] sorted = nums.clone();
        java.util.Arrays.sort(sorted);
        for (int i = 0; i < n; i++) {
            if (Integer.bitCount(nums[i]) != Integer.bitCount(sorted[i])) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        prev_max = -1  # maximum value of the previous segment after sorting
        i = 0
        while i < n:
            cur_pop = nums[i].bit_count()
            seg_min = seg_max = nums[i]
            j = i + 1
            while j < n and nums[j].bit_count() == cur_pop:
                val = nums[j]
                if val < seg_min:
                    seg_min = val
                if val > seg_max:
                    seg_max = val
                j += 1
            # after sorting each segment, its smallest element must be >= prev_max
            if prev_max > seg_min:
                return False
            prev_max = seg_max
            i = j
        return True
```

## Python3

```python
from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = -1  # all nums are positive
        cur_bits = nums[0].bit_count()
        cur_min = cur_max = nums[0]

        for x in nums[1:]:
            b = x.bit_count()
            if b == cur_bits:
                if x < cur_min:
                    cur_min = x
                if x > cur_max:
                    cur_max = x
            else:
                # segment ends, verify ordering with previous segment
                if prev_max > cur_min:
                    return False
                prev_max = cur_max
                cur_bits = b
                cur_min = cur_max = x

        # final segment check
        if prev_max > cur_min:
            return False
        return True
```

## C

```c
#include <limits.h>
#include <stdbool.h>

static int popcount(int x) {
    return __builtin_popcount((unsigned int)x);
}

bool canSortArray(int* nums, int numsSize) {
    if (numsSize <= 1) return true;
    
    int prevMax = INT_MIN;
    int i = 0;
    while (i < numsSize) {
        int curPop = popcount(nums[i]);
        int segMin = nums[i];
        int segMax = nums[i];
        int j = i + 1;
        while (j < numsSize && popcount(nums[j]) == curPop) {
            if (nums[j] < segMin) segMin = nums[j];
            if (nums[j] > segMax) segMax = nums[j];
            ++j;
        }
        if (prevMax > segMin) return false;
        prevMax = segMax;
        i = j;
    }
    return true;
}
```

## Csharp

```csharp
using System.Numerics;

public class Solution {
    public bool CanSortArray(int[] nums) {
        int n = nums.Length;
        int[] pop = new int[n];
        for (int i = 0; i < n; i++) {
            pop[i] = BitOperations.PopCount((uint)nums[i]);
        }

        int prevMax = -1;
        int i = 0;
        while (i < n) {
            int curPop = pop[i];
            int segMin = nums[i];
            int segMax = nums[i];
            i++;
            while (i < n && pop[i] == curPop) {
                if (nums[i] < segMin) segMin = nums[i];
                if (nums[i] > segMax) segMax = nums[i];
                i++;
            }
            if (segMin < prevMax) return false;
            prevMax = segMax;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canSortArray = function(nums) {
    const popcnt = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };
    
    let prevMax = -Infinity;
    let i = 0;
    const n = nums.length;
    
    while (i < n) {
        const pc = popcnt(nums[i]);
        let segMin = nums[i];
        let segMax = nums[i];
        i++;
        while (i < n && popcnt(nums[i]) === pc) {
            if (nums[i] < segMin) segMin = nums[i];
            if (nums[i] > segMax) segMax = nums[i];
            i++;
        }
        // The smallest element of current segment must be >= max of previous segment
        if (segMin < prevMax) return false;
        prevMax = segMax; // update for next segment
    }
    
    return true;
};
```

## Typescript

```typescript
function canSortArray(nums: number[]): boolean {
    const popCount = (n: number): number => {
        let cnt = 0;
        while (n) {
            n &= n - 1;
            cnt++;
        }
        return cnt;
    };

    if (nums.length <= 1) return true;

    let prevMax = -Infinity;

    let curPop = popCount(nums[0]);
    let curMin = nums[0];
    let curMax = nums[0];

    for (let i = 1; i < nums.length; i++) {
        const p = popCount(nums[i]);
        if (p === curPop) {
            if (nums[i] < curMin) curMin = nums[i];
            if (nums[i] > curMax) curMax = nums[i];
        } else {
            // end of current segment
            if (curMin < prevMax) return false;
            prevMax = curMax;

            // start new segment
            curPop = p;
            curMin = curMax = nums[i];
        }
    }

    // check the last segment against previous max
    if (curMin < prevMax) return false;

    return true;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canSortArray($nums) {
        $prevMax = PHP_INT_MIN;
        $currentPop = null;
        $currentMin = 0;
        $currentMax = 0;

        foreach ($nums as $val) {
            $pc = $this->popcount($val);
            if ($currentPop === null) {
                $currentPop = $pc;
                $currentMin = $currentMax = $val;
            } elseif ($pc == $currentPop) {
                if ($val < $currentMin) $currentMin = $val;
                if ($val > $currentMax) $currentMax = $val;
            } else {
                // segment ended, check ordering with previous segment
                if ($prevMax > $currentMin) {
                    return false;
                }
                $prevMax = $currentMax;
                $currentPop = $pc;
                $currentMin = $currentMax = $val;
            }
        }

        // final segment check
        if ($prevMax > $currentMin) {
            return false;
        }
        return true;
    }

    private function popcount($x) {
        $cnt = 0;
        while ($x > 0) {
            $x &= $x - 1;
            $cnt++;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func canSortArray(_ nums: [Int]) -> Bool {
        func popCount(_ x: Int) -> Int {
            var v = x
            var c = 0
            while v > 0 {
                c += 1
                v &= (v - 1)
            }
            return c
        }
        
        var groups: [(pop: Int, minVal: Int, maxVal: Int)] = []
        var i = 0
        let n = nums.count
        
        while i < n {
            let p = popCount(nums[i])
            var curMin = nums[i]
            var curMax = nums[i]
            var j = i + 1
            while j < n && popCount(nums[j]) == p {
                curMin = min(curMin, nums[j])
                curMax = max(curMax, nums[j])
                j += 1
            }
            groups.append((p, curMin, curMax))
            i = j
        }
        
        for k in 1..<groups.count {
            if groups[k - 1].maxVal > groups[k].minVal {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canSortArray(nums: IntArray): Boolean {
        var prevMax = Int.MIN_VALUE
        var curPop = Integer.bitCount(nums[0])
        var curMin = nums[0]
        var curMax = nums[0]

        for (i in 1 until nums.size) {
            val pop = Integer.bitCount(nums[i])
            if (pop == curPop) {
                if (nums[i] < curMin) curMin = nums[i]
                if (nums[i] > curMax) curMax = nums[i]
            } else {
                if (prevMax > curMin) return false
                prevMax = curMax
                curPop = pop
                curMin = nums[i]
                curMax = nums[i]
            }
        }

        if (prevMax > curMin) return false
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canSortArray(List<int> nums) {
    int popCount(int x) {
      int cnt = 0;
      while (x > 0) {
        x &= x - 1;
        cnt++;
      }
      return cnt;
    }

    int n = nums.length;
    int prevPop = popCount(nums[0]);
    int maxSeg = nums[0];
    int minSeg = nums[0];
    int prevMax = -1; // smaller than any possible element (nums[i] >= 1)

    for (int i = 1; i < n; ++i) {
      int curPop = popCount(nums[i]);
      if (curPop == prevPop) {
        if (nums[i] > maxSeg) maxSeg = nums[i];
        if (nums[i] < minSeg) minSeg = nums[i];
      } else {
        // End of current segment, validate ordering with previous segment
        if (minSeg < prevMax) return false;
        // Start new segment
        prevMax = maxSeg;
        prevPop = curPop;
        maxSeg = minSeg = nums[i];
      }
    }

    // Validate the last segment against the previous one
    if (minSeg < prevMax) return false;
    return true;
  }
}
```

## Golang

```go
import "math/bits"

func canSortArray(nums []int) bool {
	prevMax := -1
	n := len(nums)
	i := 0
	for i < n {
		curPop := bits.OnesCount(uint(nums[i]))
		segMin, segMax := nums[i], nums[i]
		j := i + 1
		for j < n && bits.OnesCount(uint(nums[j])) == curPop {
			if nums[j] < segMin {
				segMin = nums[j]
			}
			if nums[j] > segMax {
				segMax = nums[j]
			}
			j++
		}
		if prevMax > segMin {
			return false
		}
		prevMax = segMax
		i = j
	}
	return true
}
```

## Ruby

```ruby
def can_sort_array(nums)
  n = nums.length
  popcounts = nums.map { |x| x.to_s(2).count('1') }

  i = 0
  prev_max = -1
  while i < n
    cur_pop = popcounts[i]
    seg_min = nums[i]
    seg_max = nums[i]
    j = i + 1
    while j < n && popcounts[j] == cur_pop
      val = nums[j]
      seg_min = val if val < seg_min
      seg_max = val if val > seg_max
      j += 1
    end
    return false if prev_max > seg_min
    prev_max = seg_max
    i = j
  end
  true
end
```

## Scala

```scala
object Solution {
  def canSortArray(nums: Array[Int]): Boolean = {
    var prevMax = Int.MinValue
    var i = 0
    val n = nums.length
    while (i < n) {
      val bits = Integer.bitCount(nums(i))
      var segMin = nums(i)
      var segMax = nums(i)
      var j = i + 1
      while (j < n && Integer.bitCount(nums(j)) == bits) {
        val v = nums(j)
        if (v < segMin) segMin = v
        if (v > segMax) segMax = v
        j += 1
      }
      if (prevMax > segMin) return false
      prevMax = segMax
      i = j
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn can_sort_array(nums: Vec<i32>) -> bool {
        if nums.is_empty() {
            return true;
        }
        let mut prev_pop = (nums[0] as u32).count_ones();
        let mut cur_min = nums[0];
        let mut cur_max = nums[0];
        let mut prev_max = i32::MIN;

        for &x in nums.iter().skip(1) {
            let p = (x as u32).count_ones();
            if p == prev_pop {
                if x < cur_min { cur_min = x; }
                if x > cur_max { cur_max = x; }
            } else {
                // finish previous segment
                if cur_min < prev_max {
                    return false;
                }
                prev_max = cur_max;
                // start new segment
                prev_pop = p;
                cur_min = x;
                cur_max = x;
            }
        }

        // check the last segment
        if cur_min < prev_max {
            return false;
        }
        true
    }
}
```

## Racket

```racket
(define (popcnt n)
  (let loop ((n n) (c 0))
    (if (= n 0)
        c
        (loop (bitwise-and n (- n 1)) (+ c 1)))))

(define/contract (can-sort-array nums)
  (-> (listof exact-integer?) boolean?)
  (if (null? nums)
      #t
      (let* ((first (car nums))
             (cur-pop (popcnt first))
             (cur-min first)
             (cur-max first))
        (let loop ((rest (cdr nums))
                   (prev-max -1)
                   (cur-pop cur-pop)
                   (cur-min cur-min)
                   (cur-max cur-max))
          (if (null? rest)
              (if (< cur-min prev-max) #f #t)
              (let* ((x (car rest))
                     (p (popcnt x)))
                (if (= p cur-pop)
                    (loop (cdr rest) prev-max cur-pop (min cur-min x) (max cur-max x))
                    (if (< cur-min prev-max)
                        #f
                        (loop (cdr rest) cur-max p x x)))))))))
```

## Erlang

```erlang
-module(solution).
-export([can_sort_array/1]).

-spec can_sort_array(Nums :: [integer()]) -> boolean().
can_sort_array([]) ->
    true;
can_sort_array([First|Rest]) ->
    CurrPop = popcnt(First),
    loop(Rest, CurrPop, First, First, 0).

popcnt(N) when N >= 0 ->
    popcnt(N, 0).
popcnt(0, Acc) -> Acc;
popcnt(N, Acc) ->
    popcnt(N band (N - 1), Acc + 1).

loop([], _CurrPop, _CurrMin, _CurrMax, _PrevMax) ->
    true;
loop([X|Xs], CurrPop, CurrMin, CurrMax, PrevMax) ->
    P = popcnt(X),
    if
        P == CurrPop ->
            if X < PrevMax ->
                    false;
               true ->
                    NewMin = min(CurrMin, X),
                    NewMax = max(CurrMax, X),
                    loop(Xs, CurrPop, NewMin, NewMax, PrevMax)
            end;
        true ->
            NewPrevMax = CurrMax,
            if X < NewPrevMax ->
                    false;
               true ->
                    loop(Xs, P, X, X, NewPrevMax)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec can_sort_array(nums :: [integer]) :: boolean
  def can_sort_array(nums) do
    case nums do
      [] -> true
      [_] -> true
      [first | rest] ->
        init_state = %{
          prev_pop: popcount(first),
          min_seg: first,
          max_seg: first,
          prev_max: -1_000_000_000
        }

        result =
          Enum.reduce_while(rest, init_state, fn x, acc ->
            cur_pop = popcount(x)

            if cur_pop == acc.prev_pop do
              new_min = min(acc.min_seg, x)
              new_max = max(acc.max_seg, x)
              {:cont, %{acc | min_seg: new_min, max_seg: new_max}}
            else
              if acc.prev_max > acc.min_seg do
                {:halt, false}
              else
                new_state = %{
                  prev_pop: cur_pop,
                  min_seg: x,
                  max_seg: x,
                  prev_max: acc.max_seg
                }

                {:cont, new_state}
              end
            end
          end)

        case result do
          false -> false
          state ->
            if state.prev_max > state.min_seg do
              false
            else
              true
            end
        end
    end
  end

  defp popcount(0), do: 0
  defp popcount(n) do
    (n &&& 1) + popcount(n >>> 1)
  end
end
```
