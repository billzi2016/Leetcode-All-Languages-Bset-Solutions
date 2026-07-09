# 3229. Minimum Operations to Make Array Equal to Target

## Cpp

```cpp
class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        int n = nums.size();
        long long ans = 0;
        long long prevPos = 0, prevNeg = 0;
        for (int i = 0; i < n; ++i) {
            long long diff = (long long)target[i] - (long long)nums[i];
            long long curPos = diff > 0 ? diff : 0;
            long long curNeg = diff < 0 ? -diff : 0;
            if (curPos > prevPos) ans += curPos - prevPos;
            if (curNeg > prevNeg) ans += curNeg - prevNeg;
            prevPos = curPos;
            prevNeg = curNeg;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minimumOperations(int[] nums, int[] target) {
        int n = nums.length;
        long ops = 0L;
        long posPrev = 0L;
        long negPrev = 0L;
        for (int i = 0; i < n; i++) {
            long diff = (long) target[i] - (long) nums[i];
            if (diff > 0) {
                if (diff > posPrev) {
                    ops += diff - posPrev;
                }
                posPrev = diff;
                negPrev = 0L;
            } else if (diff < 0) {
                long ndiff = -diff;
                if (ndiff > negPrev) {
                    ops += ndiff - negPrev;
                }
                negPrev = ndiff;
                posPrev = 0L;
            } else {
                posPrev = 0L;
                negPrev = 0L;
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        ops = 0
        pos_prev = 0
        neg_prev = 0
        for a, b in zip(nums, target):
            diff = b - a
            if diff >= 0:
                pos, neg = diff, 0
            else:
                pos, neg = 0, -diff
            if pos > pos_prev:
                ops += pos - pos_prev
            if neg > neg_prev:
                ops += neg - neg_prev
            pos_prev, neg_prev = pos, neg
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        inc = dec = 0
        prev_pos = prev_neg = 0
        for a, b in zip(nums, target):
            d = b - a
            pos = d if d > 0 else 0
            neg = -d if d < 0 else 0
            if pos > prev_pos:
                inc += pos - prev_pos
            if neg > prev_neg:
                dec += neg - prev_neg
            prev_pos, prev_neg = pos, neg
        return inc + dec
```

## C

```c
#include <stddef.h>

long long minimumOperations(int* nums, int numsSize, int* target, int targetSize) {
    long long pos = 0, neg = 0;
    long long prev = 0;
    for (int i = 0; i < numsSize; ++i) {
        long long cur = (long long)target[i] - (long long)nums[i];
        long long delta = cur - prev;
        if (delta > 0)
            pos += delta;
        else
            neg -= delta; // delta is negative
        prev = cur;
    }
    return pos > neg ? pos : neg;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MinimumOperations(int[] nums, int[] target) {
        int n = nums.Length;
        long operations = 0;
        long prevPos = 0, prevNeg = 0;
        for (int i = 0; i < n; i++) {
            long diff = (long)target[i] - (long)nums[i];
            long curPos = diff > 0 ? diff : 0;
            long curNeg = diff < 0 ? -diff : 0;
            if (curPos > prevPos) operations += curPos - prevPos;
            if (curNeg > prevNeg) operations += curNeg - prevNeg;
            prevPos = curPos;
            prevNeg = curNeg;
        }
        return operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} target
 * @return {number}
 */
var minimumOperations = function(nums, target) {
    const n = nums.length;
    let prev = 0;
    let sumAbs = 0;
    let last = 0;
    for (let i = 0; i < n; ++i) {
        const cur = target[i] - nums[i];
        const delta = cur - prev;
        sumAbs += Math.abs(delta);
        prev = cur;
        if (i === n - 1) last = cur;
    }
    return (sumAbs + Math.abs(last)) / 2;
};
```

## Typescript

```typescript
function minimumOperations(nums: number[], target: number[]): number {
    const n = nums.length;
    let inc = 0;
    let dec = 0;
    let prevPos = 0;
    let prevNeg = 0;
    for (let i = 0; i < n; i++) {
        const d = target[i] - nums[i];
        const pos = d > 0 ? d : 0;
        const neg = d < 0 ? -d : 0;
        if (pos > prevPos) inc += pos - prevPos;
        if (neg > prevNeg) dec += neg - prevNeg;
        prevPos = pos;
        prevNeg = neg;
    }
    return inc + dec;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $target
     * @return Integer
     */
    function minimumOperations($nums, $target) {
        $n = count($nums);
        $ans = 0;
        $prevPos = 0; // previous positive diff
        $prevNeg = 0; // previous magnitude of negative diff

        for ($i = 0; $i < $n; ++$i) {
            $d = $target[$i] - $nums[$i];
            if ($d > 0) {
                $inc = $d - $prevPos;
                if ($inc > 0) {
                    $ans += $inc;
                }
                $prevPos = $d;
                $prevNeg = 0;
            } elseif ($d < 0) {
                $neg = -$d; // magnitude of negative diff
                $inc = $neg - $prevNeg;
                if ($inc > 0) {
                    $ans += $inc;
                }
                $prevNeg = $neg;
                $prevPos = 0;
            } else { // d == 0
                $prevPos = 0;
                $prevNeg = 0;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int], _ target: [Int]) -> Int {
        let n = nums.count
        var incOps: Int64 = 0
        var decOps: Int64 = 0
        var prevPos = 0          // previous positive height (diff > 0)
        var prevNeg = 0          // previous negative magnitude (diff < 0)
        
        for i in 0..<n {
            let diff = target[i] - nums[i]
            
            if diff > 0 {
                if diff > prevPos {
                    incOps += Int64(diff - prevPos)
                }
                prevPos = diff
            } else {
                prevPos = 0
            }
            
            let neg = -diff   // magnitude of negative part
            if neg > 0 {
                if neg > prevNeg {
                    decOps += Int64(neg - prevNeg)
                }
                prevNeg = neg
            } else {
                prevNeg = 0
            }
        }
        
        return Int(incOps + decOps)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray, target: IntArray): Long {
        var operations = 0L
        var prevPos = 0
        var prevNeg = 0
        for (i in nums.indices) {
            val diff = target[i] - nums[i]
            val pos = if (diff > 0) diff else 0
            val neg = if (diff < 0) -diff else 0
            if (pos > prevPos) operations += (pos - prevPos).toLong()
            if (neg > prevNeg) operations += (neg - prevNeg).toLong()
            prevPos = pos
            prevNeg = neg
        }
        return operations
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<int> nums, List<int> target) {
    int n = nums.length;
    int prevPos = 0;
    int prevNeg = 0;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      int diff = target[i] - nums[i];
      int curPos = diff > 0 ? diff : 0;
      int curNeg = diff < 0 ? -diff : 0;
      if (curPos > prevPos) ans += curPos - prevPos;
      if (curNeg > prevNeg) ans += curNeg - prevNeg;
      prevPos = curPos;
      prevNeg = curNeg;
    }
    return ans;
  }
}
```

## Golang

```go
func minimumOperations(nums []int, target []int) int64 {
    var ans int64
    prevPos, prevNeg := 0, 0
    for i := 0; i < len(nums); i++ {
        d := target[i] - nums[i]
        if d > 0 {
            curPos := d
            if curPos > prevPos {
                ans += int64(curPos - prevPos)
            }
            prevPos = curPos
        } else {
            prevPos = 0
        }

        if d < 0 {
            curNeg := -d
            if curNeg > prevNeg {
                ans += int64(curNeg - prevNeg)
            }
            prevNeg = curNeg
        } else {
            prevNeg = 0
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_operations(nums, target)
  ans = 0
  prev_pos = 0
  prev_neg = 0
  nums.each_with_index do |num, i|
    d = target[i] - num
    cur_pos = d > 0 ? d : 0
    cur_neg = d < 0 ? -d : 0
    ans += cur_pos - prev_pos if cur_pos > prev_pos
    ans += cur_neg - prev_neg if cur_neg > prev_neg
    prev_pos = cur_pos
    prev_neg = cur_neg
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int], target: Array[Int]): Long = {
        var ans: Long = 0L
        var prevPos: Long = 0L
        var prevNeg: Long = 0L
        val n = nums.length
        var i = 0
        while (i < n) {
            val d = target(i).toLong - nums(i).toLong
            val curPos = if (d > 0) d else 0L
            val curNeg = if (d < 0) -d else 0L
            if (curPos > prevPos) ans += curPos - prevPos
            if (curNeg > prevNeg) ans += curNeg - prevNeg
            prevPos = curPos
            prevNeg = curNeg
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>, target: Vec<i32>) -> i64 {
        let mut pos_prev: i64 = 0;
        let mut neg_prev: i64 = 0;
        let mut ops: i64 = 0;
        for (a, b) in nums.iter().zip(target.iter()) {
            let diff = *b as i64 - *a as i64;
            if diff > 0 {
                let cur = diff;
                if cur > pos_prev {
                    ops += cur - pos_prev;
                }
                pos_prev = cur;
                neg_prev = 0;
            } else if diff < 0 {
                let cur = -diff;
                if cur > neg_prev {
                    ops += cur - neg_prev;
                }
                neg_prev = cur;
                pos_prev = 0;
            } else {
                pos_prev = 0;
                neg_prev = 0;
            }
        }
        ops
    }
}
```

## Racket

```racket
(define/contract (minimum-operations nums target)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let loop ((ns nums) (ts target)
             (prev-pos 0) (prev-neg 0) (ans 0))
    (if (null? ns)
        ans
        (let* ((diff (- (car ts) (car ns)))
               (curr-pos (if (> diff 0) diff 0))
               (curr-neg (if (< diff 0) (- diff) 0))
               (inc (+ (max (- curr-pos prev-pos) 0)
                       (max (- curr-neg prev-neg) 0))))
          (loop (cdr ns) (cdr ts) curr-pos curr-neg (+ ans inc))))))
```

## Erlang

```erlang
-spec minimum_operations(Nums :: [integer()], Target :: [integer()]) -> integer().
minimum_operations(Nums, Target) ->
    DiffList = lists:zipwith(fun(N, T) -> T - N end, Nums, Target),
    {Ans, _, _} = lists:foldl(
        fun(Diff, {Acc, PrevPos, PrevNeg}) ->
            Pos = if Diff > 0 -> Diff; true -> 0 end,
            Neg = if Diff < 0 -> -Diff; true -> 0 end,
            AddPos = erlang:max(Pos - PrevPos, 0),
            AddNeg = erlang:max(Neg - PrevNeg, 0),
            {Acc + AddPos + AddNeg, Pos, Neg}
        end,
        {0, 0, 0},
        DiffList),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer], target :: [integer]) :: integer
  def minimum_operations(nums, target) do
    diffs = Enum.zip(nums, target) |> Enum.map(fn {a, b} -> b - a end)

    {total, last_diff} =
      Enum.reduce(diffs, {0, 0}, fn cur, {acc, prev} ->
        {acc + abs(cur - prev), cur}
      end)

    total = total + abs(last_diff)
    div(total, 2)
  end
end
```
