# 2970. Count the Number of Incremovable Subarrays I

## Cpp

```cpp
class Solution {
public:
    int incremovableSubarrayCount(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int l = 0; l < n; ++l) {
            for (int r = l; r < n; ++r) {
                bool ok = true;
                int prev = -1; // sentinel, since nums[i] >= 1
                // check prefix [0, l-1]
                for (int i = 0; i < l; ++i) {
                    if (prev != -1 && !(prev < nums[i])) { ok = false; break; }
                    prev = nums[i];
                }
                if (!ok) continue;
                // check suffix [r+1, n-1]
                for (int i = r + 1; i < n; ++i) {
                    if (prev != -1 && !(prev < nums[i])) { ok = false; break; }
                    prev = nums[i];
                }
                if (ok) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int incremovableSubarrayCount(int[] nums) {
        int n = nums.length;
        int count = 0;
        for (int l = 0; l < n; ++l) {
            for (int r = l; r < n; ++r) {
                int prev = -1;
                boolean ok = true;
                for (int i = 0; i < n; ++i) {
                    if (i >= l && i <= r) continue;
                    if (prev != -1 && nums[i] <= prev) {
                        ok = false;
                        break;
                    }
                    prev = nums[i];
                }
                if (ok) count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        def is_strict(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True

        count = 0
        for l in range(n):
            for r in range(l, n):
                merged = nums[:l] + nums[r+1:]
                if is_strict(merged):
                    count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            for r in range(l, n):
                prev = None
                ok = True
                for i in range(n):
                    if l <= i <= r:
                        continue
                    if prev is not None and nums[i] <= prev:
                        ok = False
                        break
                    prev = nums[i]
                if ok:
                    ans += 1
        return ans
```

## C

```c
int incremovableSubarrayCount(int* nums, int numsSize) {
    int n = numsSize;
    if (n == 0) return 0;
    // prefix strictly increasing flags
    int pref[n];
    pref[0] = 1; // true
    for (int i = 1; i < n; ++i) {
        pref[i] = pref[i-1] && (nums[i-1] < nums[i]);
    }
    // suffix strictly increasing flags
    int suff[n];
    suff[n-1] = 1;
    for (int i = n - 2; i >= 0; --i) {
        suff[i] = suff[i+1] && (nums[i] < nums[i+1]);
    }
    int count = 0;
    for (int l = 0; l < n; ++l) {
        for (int r = l; r < n; ++r) {
            // check prefix up to l-1
            if (l > 0 && !pref[l-1]) continue;
            // check suffix from r+1
            if (r < n - 1 && !suff[r+1]) continue;
            // cross condition
            if (l > 0 && r < n - 1) {
                if (!(nums[l-1] < nums[r+1])) continue;
            }
            count++;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int IncremovableSubarrayCount(int[] nums) {
        int n = nums.Length;
        int count = 0;
        for (int l = 0; l < n; ++l) {
            for (int r = l; r < n; ++r) {
                int prev = -1;
                bool ok = true;
                for (int i = 0; i < n; ++i) {
                    if (i >= l && i <= r) continue;
                    if (prev != -1 && nums[i] <= prev) {
                        ok = false;
                        break;
                    }
                    prev = nums[i];
                }
                if (ok) count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var incremovableSubarrayCount = function(nums) {
    const n = nums.length;
    // pref[i]: nums[0..i] is strictly increasing
    const pref = new Array(n).fill(false);
    for (let i = 0; i < n; ++i) {
        if (i === 0) pref[i] = true;
        else pref[i] = pref[i - 1] && nums[i - 1] < nums[i];
    }
    // suff[i]: nums[i..n-1] is strictly increasing
    const suff = new Array(n).fill(false);
    for (let i = n - 1; i >= 0; --i) {
        if (i === n - 1) suff[i] = true;
        else suff[i] = suff[i + 1] && nums[i] < nums[i + 1];
    }
    
    let count = 0;
    for (let l = 0; l < n; ++l) {
        for (let r = l; r < n; ++r) {
            const leftOk = (l === 0) || pref[l - 1];
            const rightOk = (r === n - 1) || suff[r + 1];
            if (!leftOk || !rightOk) continue;
            if (l > 0 && r < n - 1 && !(nums[l - 1] < nums[r + 1])) continue;
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function incremovableSubarrayCount(nums: number[]): number {
    const n = nums.length;
    const pref = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
        if (i === 0) pref[i] = true;
        else pref[i] = pref[i - 1] && nums[i - 1] < nums[i];
    }
    const suff = new Array(n).fill(false);
    for (let i = n - 1; i >= 0; i--) {
        if (i === n - 1) suff[i] = true;
        else suff[i] = suff[i + 1] && nums[i] < nums[i + 1];
    }
    let ans = 0;
    for (let l = 0; l < n; l++) {
        for (let r = l; r < n; r++) {
            let ok = true;
            if (l > 0 && !pref[l - 1]) ok = false;
            if (r < n - 1 && !suff[r + 1]) ok = false;
            if (ok && l > 0 && r < n - 1 && !(nums[l - 1] < nums[r + 1])) ok = false;
            if (ok) ans++;
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
    function incremovableSubarrayCount($nums) {
        $n = count($nums);
        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            for ($r = $l; $r < $n; $r++) {
                $prev = null;
                $ok = true;
                // check prefix [0, l-1]
                for ($i = 0; $i < $l; $i++) {
                    if ($prev !== null && $nums[$i] <= $prev) {
                        $ok = false;
                        break;
                    }
                    $prev = $nums[$i];
                }
                if (!$ok) continue;
                // check suffix [r+1, n-1]
                for ($i = $r + 1; $i < $n; $i++) {
                    if ($prev !== null && $nums[$i] <= $prev) {
                        $ok = false;
                        break;
                    }
                    $prev = $nums[$i];
                }
                if ($ok) $ans++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func incremovableSubarrayCount(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        var preInc = Array(repeating: true, count: n)
        for i in 1..<n {
            preInc[i] = preInc[i - 1] && (nums[i - 1] < nums[i])
        }
        var sufInc = Array(repeating: true, count: n)
        if n > 1 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                sufInc[i] = sufInc[i + 1] && (nums[i] < nums[i + 1])
            }
        }
        var ans = 0
        for l in 0..<n {
            for r in l..<n {
                if l > 0 && !preInc[l - 1] { continue }
                if r < n - 1 && !sufInc[r + 1] { continue }
                if l > 0 && r < n - 1 && nums[l - 1] >= nums[r + 1] { continue }
                ans += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun incremovableSubarrayCount(nums: IntArray): Int {
        val n = nums.size
        val pref = BooleanArray(n)
        for (i in 0 until n) {
            pref[i] = if (i == 0) true else pref[i - 1] && nums[i - 1] < nums[i]
        }
        val suf = BooleanArray(n)
        for (i in n - 1 downTo 0) {
            suf[i] = if (i == n - 1) true else suf[i + 1] && nums[i] < nums[i + 1]
        }
        var ans = 0
        for (l in 0 until n) {
            for (r in l until n) {
                if (l > 0 && !pref[l - 1]) continue
                if (r < n - 1 && !suf[r + 1]) continue
                if (l > 0 && r < n - 1 && nums[l - 1] >= nums[r + 1]) continue
                ans++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int incremovableSubarrayCount(List<int> nums) {
    int n = nums.length;
    int ans = 0;
    for (int l = 0; l < n; ++l) {
      for (int r = l; r < n; ++r) {
        int? prev;
        bool ok = true;
        // check prefix [0, l-1]
        for (int i = 0; i < l; ++i) {
          if (prev != null && nums[i] <= prev) {
            ok = false;
            break;
          }
          prev = nums[i];
        }
        if (!ok) continue;
        // check suffix [r+1, n-1]
        for (int i = r + 1; i < n; ++i) {
          if (prev != null && nums[i] <= prev) {
            ok = false;
            break;
          }
          prev = nums[i];
        }
        if (ok) ans++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func incremovableSubarrayCount(nums []int) int {
    n := len(nums)
    ans := 0
    for l := 0; l < n; l++ {
        for r := l; r < n; r++ {
            prev := 0 // nums[i] >= 1, so 0 works as -infinity
            ok := true
            for i := 0; i < n; i++ {
                if i >= l && i <= r {
                    continue
                }
                if nums[i] <= prev {
                    ok = false
                    break
                }
                prev = nums[i]
            }
            if ok {
                ans++
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def incremovable_subarray_count(nums)
  n = nums.length
  count = 0
  (0...n).each do |l|
    (l...n).each do |r|
      prev = nil
      ok = true
      i = 0
      while i < n
        if i < l || i > r
          if !prev.nil? && nums[i] <= prev
            ok = false
            break
          end
          prev = nums[i]
        end
        i += 1
      end
      count += 1 if ok
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def incremovableSubarrayCount(nums: Array[Int]): Int = {
        val n = nums.length
        if (n == 0) return 0

        // pref[i] true if nums[0..i] is strictly increasing
        val pref = new Array[Boolean](n)
        for (i <- 0 until n) {
            pref(i) = if (i == 0) true else pref(i - 1) && nums(i - 1) < nums(i)
        }

        // suff[i] true if nums[i..n-1] is strictly increasing
        val suff = new Array[Boolean](n)
        for (i <- (0 until n).reverse) {
            suff(i) = if (i == n - 1) true else suff(i + 1) && nums(i) < nums(i + 1)
        }

        var count = 0
        for (l <- 0 until n) {
            for (r <- l until n) {
                val leftOk = if (l == 0) true else pref(l - 1)
                val rightOk = if (r == n - 1) true else suff(r + 1)
                val crossOk = if (l > 0 && r < n - 1) nums(l - 1) < nums(r + 1) else true
                if (leftOk && rightOk && crossOk) count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // inc_prefix[i] is true if nums[0..=i] is strictly increasing
        let mut inc_prefix = vec![true; n];
        for i in 1..n {
            inc_prefix[i] = inc_prefix[i - 1] && nums[i - 1] < nums[i];
        }
        // inc_suffix[i] is true if nums[i..=n-1] is strictly increasing
        let mut inc_suffix = vec![true; n];
        for i in (0..n - 1).rev() {
            inc_suffix[i] = inc_suffix[i + 1] && nums[i] < nums[i + 1];
        }

        let mut count: i32 = 0;
        for l in 0..n {
            for r in l..n {
                let left_ok = if l == 0 { true } else { inc_prefix[l - 1] };
                let right_ok = if r == n - 1 { true } else { inc_suffix[r + 1] };
                let boundary_ok = if l > 0 && r < n - 1 {
                    nums[l - 1] < nums[r + 1]
                } else {
                    true
                };
                if left_ok && right_ok && boundary_ok {
                    count += 1;
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (incremovable-subarray-count nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (letrec
        ;; returns #t if removing subarray [l..r] leaves a strictly increasing sequence
        ((check (lambda (l r i prev)
                  (cond [(= i n) #t]
                        [(and (>= i l) (<= i r))
                         (check l r (+ i 1) prev)]
                        [else
                         (let ((val (vector-ref vec i)))
                           (if (and prev (<= val prev))
                               #f
                               (check l r (+ i 1) val)))]))))
      (let loop-l ((l 0) (total 0))
        (if (= l n)
            total
            (let loop-r ((r l) (tot total))
              (if (> r (- n 1))
                  (loop-l (+ l 1) tot)
                  (if (check l r 0 #f)
                      (loop-r (+ r 1) (+ tot 1))
                      (loop-r (+ r 1) tot)))))))))
```

## Erlang

```erlang
-module(solution).
-export([incremovable_subarray_count/1]).

-spec incremovable_subarray_count(Nums :: [integer()]) -> integer().
incremovable_subarray_count(Nums) ->
    N = length(Nums),
    lists:foldl(
        fun(L, AccL) ->
            lists:foldl(
                fun(R, AccR) when R >= L ->
                    Prefix = lists:sublist(Nums, 1, L),
                    Suffix = lists:nthtail(R + 1, Nums),
                    Combined = Prefix ++ Suffix,
                    case is_strictly_increasing(Combined) of
                        true -> AccR + 1;
                        false -> AccR
                    end
                end,
                AccL,
                lists:seq(L, N - 1)
            )
        end,
        0,
        lists:seq(0, N - 1)
    ).

is_strictly_increasing([]) -> true;
is_strictly_increasing([_]) -> true;
is_strictly_increasing([A, B | Rest]) when A < B ->
    is_strictly_increasing([B | Rest]);
is_strictly_increasing(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec incremovable_subarray_count(nums :: [integer]) :: integer
  def incremovable_subarray_count(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)

    # left_good[i] == true if nums[0..i] is strictly increasing
    {left_rev, _} =
      Enum.reduce(0..(n - 1), {[], true}, fn i, {list, prev_ok} ->
        ok =
          if i == 0 do
            true
          else
            prev_ok && elem(arr, i) > elem(arr, i - 1)
          end

        {[ok | list], ok}
      end)

    left_good = Enum.reverse(left_rev)

    # right_good[i] == true if nums[i..n-1] is strictly increasing
    {right_rev, _} =
      Enum.reduce(Enum.reverse(0..(n - 1)), {[], true}, fn i, {list, prev_ok} ->
        ok =
          if i == n - 1 do
            true
          else
            prev_ok && elem(arr, i) < elem(arr, i + 1)
          end

        {[ok | list], ok}
      end)

    right_good = Enum.reverse(right_rev)

    Enum.reduce(0..(n - 1), 0, fn l, acc_l ->
      Enum.reduce(l..(n - 1), acc_l, fn r, acc_r ->
        prefix_ok = if l == 0, do: true, else: Enum.at(left_good, l - 1)
        suffix_ok = if r == n - 1, do: true, else: Enum.at(right_good, r + 1)

        ok =
          if prefix_ok and suffix_ok do
            if l > 0 and r < n - 1 do
              elem(arr, l - 1) < elem(arr, r + 1)
            else
              true
            end
          else
            false
          end

        if ok, do: acc_r + 1, else: acc_r
      end)
    end)
  end
end
```
