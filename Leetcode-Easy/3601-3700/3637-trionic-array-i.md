# 3637. Trionic Array I

## Cpp

```cpp
class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return false;
        for (int p = 1; p <= n - 2; ++p) {
            // check strictly increasing from 0 to p
            bool incPrefix = true;
            for (int i = 1; i <= p; ++i) {
                if (nums[i] <= nums[i - 1]) { incPrefix = false; break; }
            }
            if (!incPrefix) continue;
            for (int q = p + 1; q <= n - 2; ++q) {
                // check strictly decreasing from p to q
                bool decMid = true;
                for (int i = p + 1; i <= q; ++i) {
                    if (nums[i] >= nums[i - 1]) { decMid = false; break; }
                }
                if (!decMid) continue;
                // check strictly increasing from q to n-1
                bool incSuffix = true;
                for (int i = q + 1; i < n; ++i) {
                    if (nums[i] <= nums[i - 1]) { incSuffix = false; break; }
                }
                if (incSuffix) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isTrionic(int[] nums) {
        int n = nums.length;
        for (int p = 1; p <= n - 2; p++) {
            // first segment: strictly increasing from 0 to p
            boolean incFirst = true;
            for (int i = 1; i <= p; i++) {
                if (nums[i] <= nums[i - 1]) {
                    incFirst = false;
                    break;
                }
            }
            if (!incFirst) continue;

            for (int q = p + 1; q <= n - 2; q++) {
                // second segment: strictly decreasing from p to q
                boolean decMid = true;
                for (int i = p + 1; i <= q; i++) {
                    if (nums[i] >= nums[i - 1]) {
                        decMid = false;
                        break;
                    }
                }
                if (!decMid) continue;

                // third segment: strictly increasing from q to n-1
                boolean incLast = true;
                for (int i = q + 1; i < n; i++) {
                    if (nums[i] <= nums[i - 1]) {
                        incLast = false;
                        break;
                    }
                }
                if (incLast) return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 5:
            return False

        def inc(l, r):
            for i in range(l + 1, r + 1):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        def dec(l, r):
            for i in range(l + 1, r + 1):
                if nums[i] >= nums[i - 1]:
                    return False
            return True

        for p in range(1, n - 2):          # need at least one element after p and before end
            if not inc(0, p):
                continue
            for q in range(p + 1, n - 1):   # q must be < n-1
                if dec(p, q) and inc(q, n - 1):
                    return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n - 2):
            # check first segment increasing
            inc_first = True
            for i in range(p):
                if nums[i] >= nums[i + 1]:
                    inc_first = False
                    break
            if not inc_first:
                continue
            for q in range(p + 1, n - 1):
                # check middle segment decreasing
                dec_mid = True
                for i in range(p, q):
                    if nums[i] <= nums[i + 1]:
                        dec_mid = False
                        break
                if not dec_mid:
                    continue
                # check last segment increasing
                inc_last = True
                for i in range(q + 1, n - 1):
                    if nums[i] >= nums[i + 1]:
                        inc_last = False
                        break
                if inc_last:
                    return True
        return False
```

## C

```c
#include <stdbool.h>

static bool isIncreasing(int *nums, int start, int end) {
    for (int i = start; i < end; ++i) {
        if (nums[i] >= nums[i + 1]) return false;
    }
    return true;
}

static bool isDecreasing(int *nums, int start, int end) {
    for (int i = start; i < end; ++i) {
        if (nums[i] <= nums[i + 1]) return false;
    }
    return true;
}

bool isTrionic(int* nums, int numsSize) {
    if (numsSize < 3) return false;
    for (int p = 1; p <= numsSize - 3; ++p) {          // ensure at least one element after q
        if (!isIncreasing(nums, 0, p)) continue;
        for (int q = p + 1; q <= numsSize - 2; ++q) {
            if (!isDecreasing(nums, p + 1, q)) continue;
            if (isIncreasing(nums, q + 1, numsSize - 1))
                return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsTrionic(int[] nums) {
        int n = nums.Length;
        // Helper lambdas for monotonic checks
        System.Func<int, int, bool> inc = (l, r) => {
            for (int i = l; i < r; ++i)
                if (nums[i] >= nums[i + 1]) return false;
            return true;
        };
        System.Func<int, int, bool> dec = (l, r) => {
            for (int i = l; i < r; ++i)
                if (nums[i] <= nums[i + 1]) return false;
            return true;
        };

        for (int p = 1; p <= n - 3; ++p) {          // p must be >0 and < q
            for (int q = p + 1; q <= n - 2; ++q) { // q must be < n-1
                if (inc(0, p) && dec(p + 1, q) && inc(q + 1, n - 1))
                    return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isTrionic = function(nums) {
    const n = nums.length;
    // need at least one element before p, between p and q, and after q
    for (let p = 1; p <= n - 3; ++p) {
        // check strictly increasing from index 0 to p
        let incLeft = true;
        for (let i = 0; i < p; ++i) {
            if (nums[i] >= nums[i + 1]) { incLeft = false; break; }
        }
        if (!incLeft) continue;

        for (let q = p + 1; q <= n - 2; ++q) {
            // check strictly decreasing from p to q
            let decMid = true;
            if (nums[p] <= nums[p + 1]) decMid = false;
            else {
                for (let i = p + 1; i < q; ++i) {
                    if (nums[i] <= nums[i + 1]) { decMid = false; break; }
                }
            }
            if (!decMid) continue;

            // check strictly increasing from q to end
            let incRight = true;
            if (nums[q] >= nums[q + 1]) incRight = false;
            else {
                for (let i = q + 1; i < n - 1; ++i) {
                    if (nums[i] >= nums[i + 1]) { incRight = false; break; }
                }
            }
            if (incRight) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function isTrionic(nums: number[]): boolean {
    const n = nums.length;
    for (let p = 1; p <= n - 3; ++p) {
        // first segment strictly increasing [0..p]
        let incFirst = true;
        for (let i = 0; i < p; ++i) {
            if (nums[i] >= nums[i + 1]) { incFirst = false; break; }
        }
        if (!incFirst) continue;

        for (let q = p + 1; q <= n - 2; ++q) {
            // second segment strictly decreasing [p..q]
            let decMid = true;
            for (let i = p; i < q; ++i) {
                if (nums[i] <= nums[i + 1]) { decMid = false; break; }
            }
            if (!decMid) continue;

            // third segment strictly increasing [q..n-1]
            let incLast = true;
            for (let i = q; i < n - 1; ++i) {
                if (nums[i] >= nums[i + 1]) { incLast = false; break; }
            }
            if (incLast) return true;
        }
    }
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
    function isTrionic($nums) {
        $n = count($nums);
        // need at least one element in each of the three parts
        for ($p = 1; $p <= $n - 2; $p++) {
            for ($q = $p + 1; $q <= $n - 2; $q++) {
                $ok = true;
                // first part: strictly increasing from index 0 to p
                for ($i = 0; $i < $p; $i++) {
                    if ($nums[$i] >= $nums[$i + 1]) {
                        $ok = false;
                        break;
                    }
                }
                if (!$ok) continue;
                // second part: strictly decreasing from p to q
                for ($i = $p; $i < $q; $i++) {
                    if ($nums[$i] <= $nums[$i + 1]) {
                        $ok = false;
                        break;
                    }
                }
                if (!$ok) continue;
                // third part: strictly increasing from q to end
                for ($i = $q; $i < $n - 1; $i++) {
                    if ($nums[$i] >= $nums[$i + 1]) {
                        $ok = false;
                        break;
                    }
                }
                if ($ok) return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isTrionic(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n < 3 { return false }
        // p must be at least 1 and at most n-3 (so that q can exist and last segment non-empty)
        for p in 1..<(n - 2) {
            var firstInc = true
            if p > 0 {
                for i in 0..<p {
                    if nums[i] >= nums[i + 1] {
                        firstInc = false
                        break
                    }
                }
            }
            if !firstInc { continue }
            
            // q must be greater than p and less than n-1
            for q in (p + 1)..<(n - 1) {
                var middleDec = true
                if q > p + 1 {
                    for i in (p + 1)..<q {
                        if nums[i] <= nums[i + 1] {
                            middleDec = false
                            break
                        }
                    }
                }
                if !middleDec { continue }
                
                var lastInc = true
                if q + 1 < n - 1 {
                    for i in (q + 1)..<(n - 1) {
                        if nums[i] >= nums[i + 1] {
                            lastInc = false
                            break
                        }
                    }
                }
                if lastInc { return true }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isTrionic(nums: IntArray): Boolean {
        val n = nums.size
        for (p in 1 until n - 1) {
            var incFirst = true
            for (i in 1..p) {
                if (nums[i] <= nums[i - 1]) {
                    incFirst = false
                    break
                }
            }
            if (!incFirst) continue
            for (q in p + 1 until n - 1) {
                var decMid = true
                for (i in p + 1..q) {
                    if (nums[i] >= nums[i - 1]) {
                        decMid = false
                        break
                    }
                }
                if (!decMid) continue
                var incLast = true
                for (i in q + 1 until n) {
                    if (nums[i] <= nums[i - 1]) {
                        incLast = false
                        break
                    }
                }
                if (incLast) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isTrionic(List<int> nums) {
    int n = nums.length;
    for (int p = 1; p <= n - 3; ++p) {
      // check strictly increasing from 0 to p
      bool incFirst = true;
      for (int i = 0; i < p; ++i) {
        if (nums[i] >= nums[i + 1]) {
          incFirst = false;
          break;
        }
      }
      if (!incFirst) continue;

      for (int q = p + 1; q <= n - 2; ++q) {
        // check strictly decreasing from p to q
        bool decMid = true;
        for (int i = p; i < q; ++i) {
          if (nums[i] <= nums[i + 1]) {
            decMid = false;
            break;
          }
        }
        if (!decMid) continue;

        // check strictly increasing from q to end
        bool incLast = true;
        for (int i = q; i < n - 1; ++i) {
          if (nums[i] >= nums[i + 1]) {
            incLast = false;
            break;
          }
        }
        if (incLast) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func isTrionic(nums []int) bool {
	n := len(nums)
	if n < 3 {
		return false
	}
	for p := 1; p <= n-3; p++ {
		// check first segment strictly increasing up to p
		okInc := true
		for i := 0; i < p; i++ {
			if nums[i] >= nums[i+1] {
				okInc = false
				break
			}
		}
		if !okInc {
			continue
		}
		for q := p + 1; q <= n-2; q++ {
			// check middle segment strictly decreasing from p to q
			okDec := true
			for i := p; i < q; i++ {
				if nums[i] <= nums[i+1] {
					okDec = false
					break
				}
			}
			if !okDec {
				continue
			}
			// check last segment strictly increasing from q to end
			okInc2 := true
			for i := q; i < n-1; i++ {
				if nums[i] >= nums[i+1] {
					okInc2 = false
					break
				}
			}
			if okInc2 {
				return true
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def is_trionic(nums)
  n = nums.length
  return false if n < 4
  (1..n - 3).each do |p|
    inc_first = true
    (0...p).each do |i|
      unless nums[i] < nums[i + 1]
        inc_first = false
        break
      end
    end
    next unless inc_first

    ((p + 1)..(n - 2)).each do |q|
      dec_mid = true
      (p + 1...q).each do |i|
        unless nums[i] > nums[i + 1]
          dec_mid = false
          break
        end
      end
      next unless dec_mid

      inc_last = true
      ((q + 1)...(n - 1)).each do |i|
        unless nums[i] < nums[i + 1]
          inc_last = false
          break
        end
      end
      return true if inc_last
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def isTrionic(nums: Array[Int]): Boolean = {
        val n = nums.length
        for (p <- 1 until n - 2) {
            // first segment strictly increasing
            if ((0 until p).forall(i => nums(i) < nums(i + 1))) {
                for (q <- p + 1 until n - 1) {
                    // second segment strictly decreasing
                    if ((p until q).forall(i => nums(i) > nums(i + 1)) &&
                        (q until n - 1).forall(i => nums(i) < nums(i + 1))) {
                        return true
                    }
                }
            }
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_trionic(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n < 3 {
            return false;
        }
        for p in 1..=n - 2 {
            // left segment strictly increasing
            let mut ok_left = true;
            for i in 0..p {
                if nums[i] >= nums[i + 1] {
                    ok_left = false;
                    break;
                }
            }
            if !ok_left {
                continue;
            }
            for q in p + 1..=n - 2 {
                // middle segment strictly decreasing
                let mut ok_mid = true;
                for i in p..q {
                    if nums[i] <= nums[i + 1] {
                        ok_mid = false;
                        break;
                    }
                }
                if !ok_mid {
                    continue;
                }
                // right segment strictly increasing
                let mut ok_right = true;
                for i in q..n - 1 {
                    if nums[i] >= nums[i + 1] {
                        ok_right = false;
                        break;
                    }
                }
                if ok_right {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (is-trionic nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((vec (list->vector nums))
         (n (vector-length vec)))
    (define (inc-between? start end)
      (let loop ((i start))
        (if (>= i end) #t
            (if (< (vector-ref vec i) (vector-ref vec (+ i 1)))
                (loop (+ i 1))
                #f))))
    (define (dec-between? start end)
      (let loop ((i start))
        (if (>= i end) #t
            (if (> (vector-ref vec i) (vector-ref vec (+ i 1)))
                (loop (+ i 1))
                #f))))
    (let loop-p ((p 1))
      (cond
        [(> p (- n 3)) #f]
        [else
         (let inner-loop-q ((q (+ p 1)))
           (cond
             [(> q (- n 2)) (loop-p (+ p 1))]
             [(and (inc-between? 0 p)
                   (dec-between? p q)
                   (inc-between? q (- n 1))) #t]
             [else (inner-loop-q (+ q 1))]))]))) ))
```

## Erlang

```erlang
-spec is_trionic(Nums :: [integer()]) -> boolean().
is_trionic(Nums) ->
    N = length(Nums),
    if N < 3 -> false;
       true -> trionic_check(Nums, N, 1)
    end.

trionic_check(_Nums, _N, P) when P > _N - 2 -> false;
trionic_check(Nums, N, P) ->
    case inc_range(Nums, 0, P) of
        true ->
            case q_check(Nums, N, P, P + 1) of
                true -> true;
                false -> trionic_check(Nums, N, P + 1)
            end;
        false ->
            trionic_check(Nums, N, P + 1)
    end.

q_check(_Nums, _N, _P, Q) when Q > _N - 2 -> false;
q_check(Nums, N, P, Q) ->
    case dec_range(Nums, P + 1, Q) of
        true ->
            case inc_range(Nums, Q + 1, N - 1) of
                true -> true;
                false -> q_check(Nums, N, P, Q + 1)
            end;
        false ->
            q_check(Nums, N, P, Q + 1)
    end.

inc_range(_List, I, J) when I >= J -> true;
inc_range(List, I, J) ->
    A = lists:nth(I + 1, List),
    B = lists:nth(I + 2, List),
    if A < B -> inc_range(List, I + 1, J);
       true -> false
    end.

dec_range(_List, I, J) when I >= J -> true;
dec_range(List, I, J) ->
    A = lists:nth(I + 1, List),
    B = lists:nth(I + 2, List),
    if A > B -> dec_range(List, I + 1, J);
       true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_trionic(nums :: [integer]) :: boolean
  def is_trionic(nums) do
    n = length(nums)
    if n < 4, do: false, else: check_trionic(List.to_tuple(nums), n)
  end

  defp check_trionic(arr, n) do
    Enum.any?(1..(n - 3), fn p ->
      inc_left? =
        Enum.all?(0..(p - 1), fn i -> elem(arr, i) < elem(arr, i + 1) end)

      if inc_left? do
        Enum.any?((p + 1)..(n - 2), fn q ->
          dec_mid? =
            Enum.all?(p..(q - 1), fn i -> elem(arr, i) > elem(arr, i + 1) end)

          inc_right? =
            Enum.all?(q..(n - 2), fn i -> elem(arr, i) < elem(arr, i + 1) end)

          dec_mid? and inc_right?
        end)
      else
        false
      end
    end)
  end
end
```
