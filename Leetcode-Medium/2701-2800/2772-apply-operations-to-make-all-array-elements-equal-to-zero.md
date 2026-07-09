# 2772. Apply Operations to Make All Array Elements Equal to Zero

## Cpp

```cpp
class Solution {
public:
    bool checkArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> diff(n + 1, 0);
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            long long need = (long long)nums[i] - cur;
            if (need < 0) return false;
            if (need > 0) {
                if (i + k > n) return false;
                cur += need;
                diff[i + k] -= need;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkArray(int[] nums, int k) {
        int n = nums.length;
        long[] diff = new long[n + 1];
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            long need = nums[i] - cur;
            if (need < 0) return false;
            if (i + k <= n) {
                if (need > 0) {
                    cur += need;
                    diff[i + k] -= need;
                }
            } else {
                if (need != 0) return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * (n + 1)   # difference array for scheduled decrements ending at position i
        cur = 0                # cumulative decrement affecting current index
        
        for i in range(n):
            cur += diff[i]
            need = nums[i] - cur
            if need < 0:
                return False
            if need > 0:
                if i + k > n:
                    return False
                cur += need          # apply need decrements starting here
                diff[i + k] -= need  # they stop affecting after position i+k-1
        
        return True
```

## Python3

```python
from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        cur = 0
        for i in range(n):
            cur += diff[i]
            need = nums[i] - cur
            if need < 0:
                return False
            if need > 0:
                if i + k > n:
                    return False
                cur += need
                diff[i + k] -= need
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool checkArray(int* nums, int numsSize, int k) {
    long long *diff = (long long*)calloc(numsSize + 1, sizeof(long long));
    if (!diff) return false;
    long long cur = 0;
    for (int i = 0; i < numsSize; ++i) {
        cur += diff[i];
        long long need = (long long)nums[i] - cur;
        if (need < 0) { free(diff); return false; }
        if (i + k > numsSize) {
            if (need != 0) { free(diff); return false; }
        } else {
            if (need > 0) {
                cur += need;
                diff[i + k] -= need;
            }
        }
    }
    free(diff);
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckArray(int[] nums, int k)
    {
        int n = nums.Length;
        long[] diff = new long[n + 1];
        long cur = 0;
        for (int i = 0; i < n; i++)
        {
            cur += diff[i];
            long need = nums[i] - cur;
            if (need < 0) return false;
            if (need > 0)
            {
                if (i + k > n) return false;
                cur += need;
                diff[i + k] -= need;
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkArray = function(nums, k) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    let cur = 0;
    for (let i = 0; i < n; ++i) {
        cur += diff[i];
        const need = nums[i] - cur;
        if (need < 0) return false;
        if (i <= n - k) {
            if (need > 0) {
                cur += need;
                diff[i + k] -= need;
            }
        } else {
            if (need !== 0) return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkArray(nums: number[], k: number): boolean {
    const n = nums.length;
    const diff: number[] = new Array(n + 1).fill(0);
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        const need = nums[i] - cur;
        if (need < 0) return false;
        if (need > 0) {
            if (i + k > n) return false;
            cur += need;
            diff[i + k] -= need;
        }
    }
    return true;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function checkArray($nums, $k) {
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $need = $nums[$i] - $cur;
            if ($need < 0) {
                return false;
            }
            if ($need > 0) {
                if ($i + $k > $n) {
                    return false;
                }
                $cur += $need;          // apply operation starting at i
                $diff[$i + $k] -= $need; // will be removed after k positions
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkArray(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            let need = nums[i] - cur
            if need < 0 { return false }
            if need > 0 {
                if i + k > n { return false }
                cur += need
                diff[i + k] -= need
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkArray(nums: IntArray, k: Int): Boolean {
        val n = nums.size
        val diff = LongArray(n + 1)
        var cur = 0L
        for (i in 0 until n) {
            cur += diff[i]
            val need = nums[i].toLong() - cur
            if (need < 0) return false
            if (need > 0) {
                if (i + k > n) return false
                cur += need
                diff[i + k] -= need
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkArray(List<int> nums, int k) {
    int n = nums.length;
    List<int> diff = List.filled(n + 1, 0);
    int acc = 0;
    for (int i = 0; i < n; ++i) {
      acc += diff[i];
      int need = nums[i] - acc;
      if (need < 0) return false;
      if (i + k <= n) {
        if (need > 0) {
          acc += need;
          diff[i + k] -= need;
        }
      } else {
        if (need != 0) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func checkArray(nums []int, k int) bool {
	n := len(nums)
	diff := make([]int, n+1) // diff[i] stores the decrement to remove from cur at position i
	cur := 0
	for i := 0; i < n; i++ {
		cur += diff[i]
		need := nums[i] - cur
		if need < 0 {
			return false
		}
		if need > 0 {
			if i+k > n {
				return false
			}
			cur += need
			diff[i+k] -= need
		}
	}
	return true
}
```

## Ruby

```ruby
def check_array(nums, k)
  n = nums.length
  diff = Array.new(n + 1, 0)
  cur = 0
  (0...n).each do |i|
    cur += diff[i]
    remaining = nums[i] - cur
    if remaining > 0
      return false if i + k > n
      cur += remaining
      diff[i + k] -= remaining
    elsif remaining < 0
      return false
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkArray(nums: Array[Int], k: Int): Boolean = {
        val n = nums.length
        val diff = new Array[Long](n + 1)
        var cur: Long = 0L
        for (i <- 0 until n) {
            cur += diff(i)
            val need = nums(i).toLong - cur
            if (need < 0) return false
            if (need > 0) {
                if (i + k > n) return false
                cur += need
                diff(i + k) -= need
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_array(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        let k_usize = k as usize;
        // diff[i] stores the amount to subtract from cur when we exit position i
        let mut diff = vec![0i64; n + 1];
        let mut cur: i64 = 0;
        for i in 0..n {
            cur += diff[i];
            let val = nums[i] as i64 - cur;
            if val < 0 {
                return false;
            }
            if i + k_usize <= n {
                if val > 0 {
                    cur += val;
                    diff[i + k_usize] -= val;
                }
            } else {
                if val != 0 {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (check-array nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (diff (make-vector (+ n 1) 0)))
    (let loop ((i 0) (curAdd 0))
      (if (= i n)
          #t
          (begin
            (set! curAdd (+ curAdd (vector-ref diff i)))
            (define need (- (vector-ref arr i) curAdd))
            (cond [(< need 0) #f]
                  [(<= i (- n k))
                   (when (> need 0)
                     (set! curAdd (+ curAdd need))
                     (vector-set! diff (+ i k)
                                  (+ (vector-ref diff (+ i k)) (- need))))
                   (loop (+ i 1) curAdd)]
                  [else
                   (if (= need 0)
                       (loop (+ i 1) curAdd)
                       #f)]))))))
```

## Erlang

```erlang
-module(solution).
-export([check_array/2]).

-spec check_array(Nums :: [integer()], K :: integer()) -> boolean().
check_array(Nums, K) ->
    N = length(Nums),
    loop(Nums, K, N, 0, 0, queue:new()).

loop([], _K, _N, _I, _Cur, _Q) ->
    true;
loop([H|T], K, N, I, Cur, Q) ->
    {Q1, Cur1} =
        if I >= K ->
                case queue:out(Q) of
                    {{value, Exp}, QRest} -> {QRest, Cur - Exp};
                    {empty, _} -> {Q, Cur}
                end;
           true -> {Q, Cur}
        end,
    Need = H - Cur1,
    case Need of
        X when X < 0 ->
            false;
        X when X > 0 ->
            if I + K > N ->
                    false;
               true ->
                    Q2 = queue:in(X, Q1),
                    loop(T, K, N, I+1, Cur1 + X, Q2)
            end;
        _ -> % Need == 0
            loop(T, K, N, I+1, Cur1, Q1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_array(nums :: [integer], k :: integer) :: boolean
  def check_array(nums, k) do
    n = length(nums)
    diff = :array.from_list(List.duplicate(0, n + 1))

    {ok, _} =
      Enum.reduce_while(Enum.with_index(nums), {true, {0, diff}}, fn {val, i},
                                                                   {_status,
                                                                    {cur, d}} ->
        cur = cur + :array.get(i, d)
        need = val - cur

        cond do
          need < 0 ->
            {:halt, {false, nil}}

          need > 0 ->
            if i + k > n do
              {:halt, {false, nil}}
            else
              cur2 = cur + need
              d2 = :array.set(i + k, (:array.get(i + k, d) - need), d)
              {:cont, {true, {cur2, d2}}}
            end

          true ->
            {:cont, {true, {cur, d}}}
        end
      end)

    ok
  end
end
```
