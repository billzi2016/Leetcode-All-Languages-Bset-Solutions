# 1909. Remove One Element to Make the Array Strictly Increasing

## Cpp

```cpp
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        int n = nums.size();
        int cnt = 0;
        int idx = -1;
        for (int i = 1; i < n; ++i) {
            if (nums[i] <= nums[i-1]) {
                ++cnt;
                idx = i;
                if (cnt > 1) return false;
            }
        }
        if (cnt == 0) return true;
        // violation at idx: nums[idx] <= nums[idx-1]
        // try removing nums[idx] or nums[idx-1]
        if (idx == 1 || nums[idx] > nums[idx-2]) return true;
        if (idx + 1 == n || nums[idx+1] > nums[idx-1]) return true;
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean canBeIncreasing(int[] nums) {
        int violations = 0;
        int idx = -1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                violations++;
                idx = i;
                if (violations > 1) return false;
            }
        }
        if (violations == 0) return true;
        int n = nums.length;
        boolean removeCurrent = (idx == n - 1) || (nums[idx + 1] > nums[idx - 1]);
        boolean removePrev = (idx == 1) || (nums[idx] > nums[idx - 2]);
        return removeCurrent || removePrev;
    }
}
```

## Python

```python
class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        idx = -1
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                cnt += 1
                idx = i
                if cnt > 1:
                    return False
        if cnt == 0:
            return True
        # one violation at position idx (nums[idx] <= nums[idx-1])
        i = idx
        remove_prev_ok = (i == 1) or (nums[i] > nums[i - 2])
        remove_curr_ok = (i == n - 1) or (nums[i + 1] > nums[i - 1])
        return remove_prev_ok or remove_curr_ok
```

## Python3

```python
from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        idx = -1
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                cnt += 1
                idx = i
                if cnt > 1:
                    return False
        if cnt == 0:
            return True
        # violation at idx: compare removing nums[idx] or nums[idx-1]
        # remove nums[idx]
        if idx == n - 1 or nums[idx + 1] > nums[idx - 1]:
            return True
        # remove nums[idx-1]
        if idx == 1 or nums[idx] > nums[idx - 2]:
            return True
        return False
```

## C

```c
#include <stdbool.h>

bool canBeIncreasing(int* nums, int numsSize) {
    int cnt = 0;
    int idx = -1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] <= nums[i - 1]) {
            cnt++;
            idx = i;
            if (cnt > 1) return false;
        }
    }
    if (cnt == 0) return true;
    // Check removal possibilities
    bool removePrev = (idx == 1) || (nums[idx] > nums[idx - 2]);
    bool removeCurr = (idx == numsSize - 1) || (nums[idx + 1] > nums[idx - 1]);
    return removePrev || removeCurr;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanBeIncreasing(int[] nums) {
        int n = nums.Length;
        int violations = 0;
        int violationIdx = -1;
        for (int i = 1; i < n; i++) {
            if (nums[i] <= nums[i - 1]) {
                violations++;
                violationIdx = i;
                if (violations > 1) return false;
            }
        }
        if (violations == 0) return true;

        bool IsIncreasingSkipping(int skip) {
            int prev = 0;
            bool hasPrev = false;
            for (int i = 0; i < n; i++) {
                if (i == skip) continue;
                if (hasPrev && nums[i] <= prev) return false;
                prev = nums[i];
                hasPrev = true;
            }
            return true;
        }

        return IsIncreasingSkipping(violationIdx) || IsIncreasingSkipping(violationIdx - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canBeIncreasing = function(nums) {
    let cnt = 0;
    let idx = -1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= nums[i - 1]) {
            cnt++;
            idx = i;
            if (cnt > 1) return false;
        }
    }
    // No violations, already strictly increasing
    if (cnt === 0) return true;
    // Single violation at idx
    const n = nums.length;
    // Check removing nums[idx] or nums[idx-1]
    const removeCurrentOk = (idx === 1) || (nums[idx] > nums[idx - 2]);
    const removePrevOk = (idx === n - 1) || (nums[idx + 1] > nums[idx - 1]);
    return removeCurrentOk || removePrevOk;
};
```

## Typescript

```typescript
function canBeIncreasing(nums: number[]): boolean {
    let violations = 0;
    let idx = -1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= nums[i - 1]) {
            violations++;
            idx = i;
            if (violations > 1) return false;
        }
    }
    if (violations === 0) return true;
    const n = nums.length;
    // Try removing nums[idx] or nums[idx-1]
    if (idx === 1 || nums[idx] > nums[idx - 2]) return true;
    if (idx === n - 1 || nums[idx + 1] > nums[idx - 1]) return true;
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canBeIncreasing($nums) {
        $n = count($nums);
        $cnt = 0;
        $idx = -1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] <= $nums[$i - 1]) {
                $cnt++;
                $idx = $i;
                if ($cnt > 1) {
                    return false;
                }
            }
        }
        if ($cnt == 0) {
            return true;
        }
        // single violation at idx
        if ($idx == 1 || $nums[$idx] > $nums[$idx - 2]) {
            return true;
        }
        if ($idx == $n - 1 || $nums[$idx + 1] > $nums[$idx - 1]) {
            return true;
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canBeIncreasing(_ nums: [Int]) -> Bool {
        let n = nums.count
        var violations = 0
        var idx = -1
        
        for i in 1..<n {
            if nums[i] <= nums[i - 1] {
                violations += 1
                idx = i
                if violations > 1 { return false }
            }
        }
        
        if violations == 0 { return true }
        // Single violation at position idx
        // If removing either nums[idx] or nums[idx-1] fixes the array
        if idx == 1 || idx == n - 1 {
            return true
        }
        if nums[idx] > nums[idx - 2] {
            return true
        }
        if nums[idx + 1] > nums[idx - 1] {
            return true
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canBeIncreasing(nums: IntArray): Boolean {
        var violations = 0
        var idx = -1
        for (i in 1 until nums.size) {
            if (nums[i] <= nums[i - 1]) {
                violations++
                idx = i
                if (violations > 1) return false
            }
        }
        if (violations == 0) return true
        val n = nums.size
        // Try removing nums[idx-1]
        val removePrevOk = idx == 1 || nums[idx] > nums[idx - 2]
        // Try removing nums[idx]
        val removeCurrOk = idx + 1 == n || nums[idx + 1] > nums[idx - 1]
        return removePrevOk || removeCurrOk
    }
}
```

## Dart

```dart
class Solution {
  bool canBeIncreasing(List<int> nums) {
    int violations = 0;
    int idx = -1;
    for (int i = 1; i < nums.length; ++i) {
      if (nums[i] <= nums[i - 1]) {
        violations++;
        idx = i;
        if (violations > 1) return false;
      }
    }
    if (violations == 0) return true;
    int n = nums.length;
    bool removeCurrent = (idx == 1) || (nums[idx] > nums[idx - 2]);
    bool removePrev = (idx == n - 1) || (nums[idx + 1] > nums[idx - 1]);
    return removeCurrent || removePrev;
  }
}
```

## Golang

```go
func canBeIncreasing(nums []int) bool {
	n := len(nums)
	if n <= 2 {
		return true
	}
	cnt, idx := 0, -1
	for i := 1; i < n; i++ {
		if nums[i] <= nums[i-1] {
			cnt++
			idx = i
			if cnt > 1 {
				return false
			}
		}
	}
	if cnt == 0 {
		return true
	}
	// Try removing nums[idx-1]
	if idx == 1 || nums[idx] > nums[idx-2] {
		return true
	}
	// Try removing nums[idx]
	if idx == n-1 || nums[idx+1] > nums[idx-1] {
		return true
	}
	return false
}
```

## Ruby

```ruby
def can_be_increasing(nums)
  n = nums.length
  cnt = 0
  idx = -1
  (1...n).each do |i|
    if nums[i] <= nums[i - 1]
      cnt += 1
      idx = i
      break if cnt > 1
    end
  end
  return true if cnt == 0

  check = lambda do |remove_idx|
    prev = nil
    nums.each_with_index do |v, i|
      next if i == remove_idx
      return false if !prev.nil? && v <= prev
      prev = v
    end
    true
  end

  return true if check.call(idx)
  return true if check.call(idx - 1)

  false
end
```

## Scala

```scala
object Solution {
    def canBeIncreasing(nums: Array[Int]): Boolean = {
        var cnt = 0
        var idx = -1
        for (i <- 1 until nums.length) {
            if (nums(i) <= nums(i - 1)) {
                cnt += 1
                idx = i
                if (cnt > 1) return false
            }
        }
        if (cnt == 0) return true

        def check(skip: Int): Boolean = {
            var prev = Int.MinValue
            for (i <- nums.indices) {
                if (i == skip) {
                    // skip this element
                } else {
                    if (nums(i) <= prev) return false
                    prev = nums(i)
                }
            }
            true
        }

        check(idx) || check(idx - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_be_increasing(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut cnt = 0;
        let mut idx = 0usize;
        for i in 1..n {
            if nums[i] <= nums[i - 1] {
                cnt += 1;
                idx = i;
                if cnt > 1 {
                    return false;
                }
            }
        }
        if cnt == 0 {
            return true;
        }
        let i = idx;
        let can_remove_i = if i + 1 >= n { true } else { nums[i + 1] > nums[i - 1] };
        let can_remove_prev = if i < 2 { true } else { nums[i] > nums[i - 2] };
        can_remove_i || can_remove_prev
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (can-be-increasing nums)
  (-> (listof exact-integer?) boolean?)
  (let ((n (length nums)))
    (define (strictly-inc? lst)
      (cond [(or (empty? lst) (empty? (rest lst))) #t]
            [else
             (let loop ((prev (first lst)) (rest (rest lst)))
               (if (empty? rest)
                   #t
                   (if (< prev (first rest))
                       (loop (first rest) (rest rest))
                       #f)))]))
    (if (strictly-inc? nums)
        #t
        (let loop ((i 0))
          (cond [(>= i n) #f]
                [else
                 (if (strictly-inc?
                      (append (take nums i)
                              (drop nums (+ i 1))))
                     #t
                     (loop (+ i 1)))])))))
```

## Erlang

```erlang
-spec can_be_increasing(Nums :: [integer()]) -> boolean().
can_be_increasing(Nums) ->
    case is_strict_increasing(Nums) of
        true -> true;
        false ->
            ViolationIdx = find_violation(Nums),
            remove_and_check(Nums, ViolationIdx - 1) orelse remove_and_check(Nums, ViolationIdx)
    end.

is_strict_increasing([]) -> true;
is_strict_increasing([_]) -> true;
is_strict_increasing([Prev, Curr | Rest]) ->
    if Prev < Curr -> is_strict_increasing([Curr|Rest]);
       true -> false
    end.

find_violation(Nums) ->
    find_violation(Nums, 0, undefined).

find_violation([], _Idx, _Prev) -> -1;
find_violation([H|T], Idx, Prev) ->
    case Prev of
        undefined ->
            find_violation(T, Idx + 1, H);
        _ ->
            if Prev >= H ->
                    Idx;
               true ->
                    find_violation(T, Idx + 1, H)
            end
    end.

remove_and_check(Nums, SkipIdx) when SkipIdx < 0 -> false;
remove_and_check(Nums, SkipIdx) ->
    check_skip(Nums, SkipIdx, 0, none).

check_skip([], _SkipIdx, _Idx, _Prev) -> true;
check_skip([H|T], SkipIdx, Idx, Prev) ->
    if Idx == SkipIdx ->
            check_skip(T, SkipIdx, Idx + 1, Prev);
       true ->
            case Prev of
                none ->
                    check_skip(T, SkipIdx, Idx + 1, H);
                _PrevVal when _PrevVal < H ->
                    check_skip(T, SkipIdx, Idx + 1, H);
                _ -> false
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_be_increasing(nums :: [integer]) :: boolean
  def can_be_increasing(nums) do
    n = length(nums)

    {violations, idx} =
      Enum.with_index(nums)
      |> Enum.reduce_while({0, nil}, fn {val, i}, {cnt, _} ->
        if i > 0 and val <= Enum.at(nums, i - 1) do
          new_cnt = cnt + 1

          if new_cnt > 1 do
            {:halt, {new_cnt, i}}
          else
            {:cont, {new_cnt, i}}
          end
        else
          {:cont, {cnt, nil}}
        end
      end)

    cond do
      violations == 0 ->
        true

      violations > 1 ->
        false

      true ->
        i = idx

        cond do
          i == 1 or Enum.at(nums, i) > Enum.at(nums, i - 2) ->
            true

          i == n - 1 or Enum.at(nums, i + 1) > Enum.at(nums, i - 1) ->
            true

          true ->
            false
        end
    end
  end
end
```
