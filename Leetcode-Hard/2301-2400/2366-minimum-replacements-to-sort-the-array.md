# 2366. Minimum Replacements to Sort the Array

## Cpp

```cpp
class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        int n = nums.size();
        long long ops = 0;
        long long bound = nums.back(); // last element stays unchanged
        for (int i = n - 2; i >= 0; --i) {
            long long cur = nums[i];
            if (cur <= bound) {
                bound = cur;
            } else {
                long long parts = (cur + bound - 1) / bound; // ceil division
                ops += parts - 1;
                bound = cur / parts; // largest piece after split
            }
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public long minimumReplacement(int[] nums) {
        int n = nums.length;
        long ops = 0L;
        long bound = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            long cur = nums[i];
            if (cur <= bound) {
                bound = cur;
            } else {
                long pieces = (cur + bound - 1) / bound; // ceil division
                ops += pieces - 1;
                bound = cur / pieces; // new maximum allowed value after split
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            cur = nums[i]
            if cur <= prev:
                prev = cur
            else:
                parts = (cur + prev - 1) // prev  # ceil division
                ops += parts - 1
                prev = cur // parts
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            cur = nums[i]
            if cur <= prev:
                prev = cur
            else:
                parts = (cur + prev - 1) // prev  # ceil division
                ans += parts - 1
                prev = cur // parts
        return ans
```

## C

```c
long long minimumReplacement(int* nums, int numsSize) {
    long long operations = 0;
    long long bound = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; --i) {
        long long cur = nums[i];
        if (cur <= bound) {
            bound = cur;
        } else {
            long long parts = (cur + bound - 1) / bound; // minimum pieces needed
            operations += parts - 1;
            bound = cur / parts; // new maximum allowed for the next element on the left
        }
    }
    return operations;
}
```

## Csharp

```csharp
public class Solution {
    public long MinimumReplacement(int[] nums) {
        int n = nums.Length;
        long ops = 0;
        long bound = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            long cur = nums[i];
            if (cur <= bound) {
                bound = cur;
            } else {
                long pieces = (cur + bound - 1) / bound; // ceil division
                ops += pieces - 1;
                bound = cur / pieces; // floor division for new bound
            }
        }
        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumReplacement = function(nums) {
    let n = nums.length;
    let ops = 0;
    let bound = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        if (nums[i] <= bound) {
            bound = nums[i];
        } else {
            const pieces = Math.ceil(nums[i] / bound);
            ops += pieces - 1;
            bound = Math.floor(nums[i] / pieces);
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minimumReplacement(nums: number[]): number {
    const n = nums.length;
    let operations = 0;
    let bound = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        if (nums[i] <= bound) {
            bound = nums[i];
        } else {
            const parts = Math.ceil(nums[i] / bound);
            operations += parts - 1;
            bound = Math.floor(nums[i] / parts);
        }
    }
    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumReplacement($nums) {
        $n = count($nums);
        $ans = 0;
        $prev = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; --$i) {
            if ($nums[$i] <= $prev) {
                $prev = $nums[$i];
            } else {
                // Minimum number of pieces needed so that each piece <= $prev
                $pieces = intdiv($nums[$i] + $prev - 1, $prev); // ceil division
                $ans += $pieces - 1;
                // New bound for the next element to the left
                $prev = intdiv($nums[$i], $pieces);
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumReplacement(_ nums: [Int]) -> Int {
        var operations: Int64 = 0
        var bound = Int64(nums.last!)
        if nums.count == 1 { return 0 }
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            let current = Int64(nums[i])
            if current <= bound {
                bound = current
            } else {
                let pieces = (current + bound - 1) / bound   // ceil division
                operations += pieces - 1
                bound = current / pieces                     // new max piece value
            }
        }
        return Int(operations)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumReplacement(nums: IntArray): Long {
        var operations = 0L
        var bound = nums[nums.size - 1].toLong()
        for (i in nums.size - 2 downTo 0) {
            val cur = nums[i].toLong()
            if (cur <= bound) {
                bound = cur
            } else {
                val pieces = (cur + bound - 1) / bound // ceil division
                operations += pieces - 1
                bound = cur / pieces
            }
        }
        return operations
    }
}
```

## Dart

```dart
class Solution {
  int minimumReplacement(List<int> nums) {
    int n = nums.length;
    int operations = 0;
    int prev = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
      int cur = nums[i];
      if (cur <= prev) {
        prev = cur;
      } else {
        int parts = ((cur + prev - 1) ~/ prev);
        operations += parts - 1;
        prev = cur ~/ parts;
      }
    }
    return operations;
  }
}
```

## Golang

```go
func minimumReplacement(nums []int) int64 {
	n := len(nums)
	if n == 0 {
		return 0
	}
	bound := nums[n-1]
	var ops int64
	for i := n - 2; i >= 0; i-- {
		cur := nums[i]
		if cur <= bound {
			bound = cur
			continue
		}
		pieces := (cur + bound - 1) / bound // ceil division
		ops += int64(pieces - 1)
		bound = cur / pieces
	}
	return ops
}
```

## Ruby

```ruby
def minimum_replacement(nums)
  ops = 0
  bound = nums[-1]
  (nums.length - 2).downto(0) do |i|
    cur = nums[i]
    if cur <= bound
      bound = cur
    else
      pieces = (cur + bound - 1) / bound
      ops += pieces - 1
      bound = cur / pieces
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minimumReplacement(nums: Array[Int]): Long = {
        var ans: Long = 0L
        var bound: Long = nums.last.toLong
        for (i <- (nums.length - 2) to 0 by -1) {
            val cur = nums(i).toLong
            if (cur <= bound) {
                bound = cur
            } else {
                val pieces = (cur + bound - 1) / bound // ceil division
                ans += pieces - 1
                bound = cur / pieces
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_replacement(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut ops: i64 = 0;
        let mut bound: i64 = *nums.last().unwrap() as i64;
        for i in (0..n - 1).rev() {
            let cur = nums[i] as i64;
            if cur <= bound {
                bound = cur;
            } else {
                // Minimum number of parts so that each part <= bound
                let parts = (cur + bound - 1) / bound; // ceil division
                ops += parts - 1;
                bound = cur / parts; // largest possible piece after split
            }
        }
        ops
    }
}
```

## Racket

```racket
(define/contract (minimum-replacement nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((i (- n 2)) (prev (vector-ref v (- n 1))) (ops 0))
      (if (< i 0)
          ops
          (let ((cur (vector-ref v i)))
            (if (<= cur prev)
                (loop (- i 1) cur ops)
                (let* ((parts (quotient (+ cur (- prev) 1) prev)) ; ceil(cur/prev)
                       (new-prev (quotient cur parts))
                       (add (- parts 1)))
                  (loop (- i 1) new-prev (+ ops add)))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_replacement/1]).

-spec minimum_replacement(Nums :: [integer()]) -> integer().
minimum_replacement(Nums) ->
    case Nums of
        [] -> 0;
        [_] -> 0;
        _ ->
            Rev = lists:reverse(Nums),
            [Bound | RestRev] = Rev,
            process(RestRev, Bound, 0)
    end.

process([], _Bound, Ops) -> Ops;
process([Cur | Tail], Bound, Ops) ->
    if
        Cur =< Bound ->
            process(Tail, Cur, Ops);
        true ->
            Parts = (Cur + Bound - 1) div Bound,
            NewOps = Ops + Parts - 1,
            NewBound = Cur div Parts,
            process(Tail, NewBound, NewOps)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_replacement(nums :: [integer]) :: integer
  def minimum_replacement(nums) do
    len = length(nums)

    if len == 1 do
      0
    else
      bound = List.last(nums)
      rev = nums |> Enum.slice(0, len - 1) |> Enum.reverse()
      helper(rev, 0, bound)
    end
  end

  defp helper([], cnt, _bound), do: cnt

  defp helper([cur | rest], cnt, bound) do
    if cur <= bound do
      helper(rest, cnt, cur)
    else
      parts = div(cur + bound - 1, bound)   # ceil division
      helper(rest, cnt + parts - 1, div(cur, parts))
    end
  end
end
```
