# 3326. Minimum Division Operations to Make Array Non Decreasing

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int maxv = *max_element(nums.begin(), nums.end());
        vector<int> spf(maxv + 1, 0);
        if (maxv >= 1) spf[1] = 1;
        for (int i = 2; i <= maxv; ++i) {
            if (!spf[i]) {
                spf[i] = i;
                if ((long long)i * i <= maxv) {
                    for (int j = i * i; j <= maxv; j += i)
                        if (!spf[j]) spf[j] = i;
                }
            }
        }

        long long next = LLONG_MAX;
        int ops = 0;
        for (int i = n - 1; i >= 0; --i) {
            int a = nums[i];
            int b = (a == 1 ? 1 : spf[a]); // smallest prime factor
            if ((long long)a <= next) {
                next = a;
            } else if ((long long)b <= next) {
                ++ops;
                next = b;
            } else {
                return -1;
            }
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        int max = 0;
        for (int v : nums) {
            if (v > max) max = v;
        }
        // smallest prime factor array
        int[] spf = new int[max + 1];
        for (int i = 2; i * i <= max; i++) {
            if (spf[i] == 0) { // i is prime
                for (int j = i * i; j <= max; j += i) {
                    if (spf[j] == 0) spf[j] = i;
                }
            }
        }
        for (int i = 2; i <= max; i++) {
            if (spf[i] == 0) spf[i] = i; // prime numbers
        }

        int ops = 0;
        int nextVal = nums[nums.length - 1];
        for (int idx = nums.length - 2; idx >= 0; idx--) {
            int cur = nums[idx];
            if (cur <= nextVal) {
                nextVal = cur;
                continue;
            }
            // need to reduce cur
            if (cur == 1) return -1;
            int smallest = spf[cur]; // for prime numbers this equals cur
            if (smallest == cur) { // prime, cannot be reduced
                return -1;
            }
            if (smallest <= nextVal) {
                ops++;
                nextVal = smallest;
            } else {
                return -1;
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_val = max(nums)
        # smallest prime factor sieve
        spf = [0] * (max_val + 1)
        spf[0] = 0
        if max_val >= 1:
            spf[1] = 1
        for i in range(2, max_val + 1):
            if spf[i] == 0:          # i is prime
                spf[i] = i
                if i * i <= max_val:
                    step = i
                    start = i * i
                    for j in range(start, max_val + 1, step):
                        if spf[j] == 0:
                            spf[j] = i

        ops = 0
        allowed = nums[-1]  # value of the last element after possible operations (we never reduce it)
        # iterate from second last to first
        for idx in range(len(nums) - 2, -1, -1):
            val = nums[idx]
            if val <= allowed:
                allowed = val
                continue
            # need to reduce
            if spf[val] == val:   # prime, cannot be reduced
                return -1
            reduced = spf[val]    # smallest prime factor
            if reduced > allowed:
                return -1
            ops += 1
            allowed = reduced
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        spf = list(range(max_val + 1))
        limit = int(max_val ** 0.5) + 1
        for i in range(2, limit):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        ops = 0
        next_val = nums[-1]
        for idx in range(len(nums) - 2, -1, -1):
            cur = nums[idx]
            if cur <= next_val:
                next_val = cur
                continue
            # need to reduce cur
            if cur == 1 or spf[cur] == cur:  # prime or 1 cannot be reduced effectively
                return -1
            reduced = spf[cur]  # smallest prime factor
            if reduced > next_val:
                return -1
            ops += 1
            next_val = reduced
        return ops
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int minOperations(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];
    if (maxVal < 2) { // all ones
        return 0;
    }

    int *spf = (int*)malloc((maxVal + 1) * sizeof(int));
    for (int i = 0; i <= maxVal; ++i) spf[i] = i;
    for (int i = 2; i * i <= maxVal; ++i) {
        if (spf[i] == i) { // prime
            for (int j = i * i; j <= maxVal; j += i)
                if (spf[j] == j) spf[j] = i;
        }
    }

    long limit = LONG_MAX;
    int ops = 0;
    for (int idx = numsSize - 1; idx >= 0; --idx) {
        int a = nums[idx];
        int b = a;
        if (a > 1 && spf[a] != a) { // composite
            b = spf[a]; // smallest prime factor after one operation
        }
        if ((long)a <= limit) {
            limit = a; // keep original, no operation
        } else if ((long)b <= limit) {
            ops++;
            limit = b;
        } else {
            free(spf);
            return -1;
        }
    }

    free(spf);
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;

        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long)i * i <= maxVal) {
                    for (int j = i * i; j <= maxVal; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        long ops = 0;
        for (int i = n - 2; i >= 0; i--) {
            int cur = nums[i];
            int nxt = nums[i + 1];
            while (cur > nxt) {
                if (cur == 1) return -1;
                int p = spf[cur];
                if (p == cur) return -1; // prime, cannot reduce
                cur /= p;
                ops++;
            }
            nums[i] = cur;
        }
        return (int)ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    let maxVal = 0;
    for (let v of nums) if (v > maxVal) maxVal = v;

    // smallest prime factor for each number up to maxVal
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; i++) {
        if (spf[i] === 0) {          // i is prime
            spf[i] = i;
            if (i * i <= maxVal) {
                for (let j = i * i; j <= maxVal; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    let ops = 0;
    let next = Infinity; // value that current element must not exceed
    for (let i = n - 1; i >= 0; i--) {
        const cur = nums[i];
        if (cur <= next) {
            next = cur;
        } else {
            if (cur === 1) return -1;          // cannot reduce further
            const reduced = spf[cur];           // smallest prime factor
            if (reduced <= next) {
                ops++;
                next = reduced;
            } else {
                return -1;
            }
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    const n = nums.length;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    // smallest prime factor sieve
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; i++) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxVal) {
                for (let j = i * i; j <= maxVal; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }
    spf[0] = 0;
    spf[1] = 1;

    const INF = Number.MAX_SAFE_INTEGER;

    // initialize DP for first element
    let prevVals: number[] = [];
    let prevCosts: number[] = [];

    const firstNum = nums[0];
    const firstOpts: { val: number; cost: number }[] = [{ val: firstNum, cost: 0 }];
    if (firstNum > 1 && spf[firstNum] !== firstNum) {
        firstOpts.push({ val: spf[firstNum], cost: 1 });
    }
    prevVals = firstOpts.map(o => o.val);
    prevCosts = firstOpts.map(o => o.cost);

    // process remaining elements
    for (let i = 1; i < n; i++) {
        const curNum = nums[i];
        const curOpts: { val: number; cost: number }[] = [{ val: curNum, cost: 0 }];
        if (curNum > 1 && spf[curNum] !== curNum) {
            curOpts.push({ val: spf[curNum], cost: 1 });
        }

        const curVals: number[] = [];
        const curCosts: number[] = new Array(curOpts.length).fill(INF);

        for (let ci = 0; ci < curOpts.length; ci++) {
            const cv = curOpts[ci].val;
            const ccost = curOpts[ci].cost;
            let best = INF;
            for (let pi = 0; pi < prevVals.length; pi++) {
                if (prevVals[pi] <= cv) {
                    const cand = prevCosts[pi] + ccost;
                    if (cand < best) best = cand;
                }
            }
            curCosts[ci] = best;
            curVals.push(cv);
        }

        // if no valid state, impossible
        let anyValid = false;
        for (const c of curCosts) {
            if (c < INF) { anyValid = true; break; }
        }
        if (!anyValid) return -1;

        prevVals = curVals;
        prevCosts = curCosts;
    }

    const answer = Math.min(...prevCosts);
    return answer >= INF ? -1 : answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $n = count($nums);
        if ($n <= 1) return 0;

        $maxVal = max($nums);
        // smallest prime factor array
        $spf = array_fill(0, $maxVal + 1, 0);
        for ($i = 2; $i * $i <= $maxVal; $i++) {
            if ($spf[$i] == 0) { // i is prime
                for ($j = $i * $i; $j <= $maxVal; $j += $i) {
                    if ($spf[$j] == 0) {
                        $spf[$j] = $i;
                    }
                }
            }
        }
        for ($i = 2; $i <= $maxVal; $i++) {
            if ($spf[$i] == 0) {
                $spf[$i] = $i; // prime numbers
            }
        }

        $ops = 0;
        $nextAllowed = $nums[$n - 1]; // last element stays as is

        for ($i = $n - 2; $i >= 0; $i--) {
            $cur = $nums[$i];
            if ($cur <= $nextAllowed) {
                $nextAllowed = $cur;
                continue;
            }
            if ($cur == 1) {
                return -1;
            }
            $reduced = $spf[$cur]; // smallest prime factor
            $ops++;
            if ($reduced > $nextAllowed) {
                return -1;
            }
            $nextAllowed = $reduced;
        }

        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        var maxVal = 0
        for v in nums {
            if v > maxVal { maxVal = v }
        }
        // Smallest prime factor (spf) array
        var spf = [Int](repeating: 0, count: maxVal + 1)
        if maxVal >= 2 {
            for i in 0...maxVal { spf[i] = i }
            let limit = Int(Double(maxVal).squareRoot())
            var i = 2
            while i <= limit {
                if spf[i] == i { // i is prime
                    var j = i * i
                    while j <= maxVal {
                        if spf[j] == j {
                            spf[j] = i
                        }
                        j += i
                    }
                }
                i += 1
            }
        } else if maxVal >= 1 {
            spf[1] = 1
        }
        
        var ops = 0
        var cur = Int.max   // maximum allowed value for current position (must be <= next)
        for idx in stride(from: n - 1, through: 0, by: -1) {
            let original = nums[idx]
            if original <= cur {
                cur = original
            } else {
                var reduced = original
                if original > 1 {
                    reduced = spf[original]   // smallest prime factor
                }
                if reduced < original && reduced <= cur {
                    ops += 1
                    cur = reduced
                } else {
                    return -1
                }
            }
        }
        return ops
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        val maxVal = nums.maxOrNull() ?: 0
        // smallest prime factor array
        val spf = IntArray(maxVal + 1) { it }
        var i = 2
        while (i * i <= maxVal) {
            if (spf[i] == i) {
                var j = i * i
                while (j <= maxVal) {
                    if (spf[j] == j) spf[j] = i
                    j += i
                }
            }
            i++
        }
        var ops = 0
        var cur = nums[nums.lastIndex]
        for (idx in nums.lastIndex - 1 downTo 0) {
            val v = nums[idx]
            if (v <= cur) {
                cur = v
            } else {
                val sp = if (v <= maxVal) spf[v] else v
                // sp == 0 means v == 1, cannot be reduced; sp > cur means reduction still too large
                if (sp == 0 || sp > cur) return -1
                ops++
                cur = sp
            }
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    int n = nums.length;
    int maxVal = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }

    // smallest prime factor sieve
    List<int> spf = List.filled(maxVal + 1, 0);
    for (int i = 2; i <= maxVal; ++i) {
      if (spf[i] == 0) {
        spf[i] = i;
        if (i * i <= maxVal) {
          for (int j = i * i; j <= maxVal; j += i) {
            if (spf[j] == 0) spf[j] = i;
          }
        }
      }
    }

    int ops = 0;
    int allowed = 1 << 60; // sufficiently large
    for (int idx = n - 1; idx >= 0; --idx) {
      int a = nums[idx];
      if (a <= allowed) {
        allowed = a;
        continue;
      }
      // need to reduce a
      if (a == 1) return -1; // cannot be reduced further
      int smallestPrime = spf[a];
      if (smallestPrime == 0) smallestPrime = a; // for safety, though shouldn't happen

      if (smallestPrime < a && smallestPrime <= allowed) {
        ops++;
        allowed = smallestPrime;
      } else {
        return -1;
      }
    }
    return ops;
  }
}
```

## Golang

```go
func minOperations(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }
    // smallest prime factor sieve
    spf := make([]int, maxVal+1)
    for i := 2; i <= maxVal; i++ {
        if spf[i] == 0 { // i is prime
            for j := i; j <= maxVal; j += i {
                if spf[j] == 0 {
                    spf[j] = i
                }
            }
        }
    }

    ops := 0
    nextVal := nums[n-1]

    for i := n - 2; i >= 0; i-- {
        cur := nums[i]
        if cur <= nextVal {
            nextVal = cur
            continue
        }
        // need to reduce
        if cur == 1 {
            return -1
        }
        smallest := spf[cur] // for prime numbers, spf[cur] == cur
        if smallest == cur || smallest > nextVal {
            return -1
        }
        ops++
        nextVal = smallest
    }
    return ops
}
```

## Ruby

```ruby
def min_operations(nums)
  n = nums.length
  max_val = nums.max
  spf = Array.new(max_val + 1, 0)
  (2..max_val).each do |i|
    if spf[i] == 0
      (i..max_val).step(i) { |j| spf[j] = i if spf[j] == 0 }
    end
  end
  spf[1] = 1

  ops = 0
  limit = nums[-1]

  (n - 2).downto(0) do |idx|
    val = nums[idx]
    if val <= limit
      limit = val
      next
    end

    while val > limit && spf[val] != val
      val /= spf[val]
      ops += 1
    end

    return -1 if val > limit
    limit = val
  end

  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        val n = nums.length
        if (n == 0) return 0

        // compute smallest prime factor for each number up to max(nums)
        val limit = nums.max
        val spf = new Array[Int](limit + 1)
        if (limit >= 1) spf(1) = 1
        var i = 2
        while (i <= limit) {
            if (spf(i) == 0) { // i is prime
                var j = i
                while (j <= limit) {
                    if (spf(j) == 0) spf(j) = i
                    j += i
                }
            }
            i += 1
        }

        var ops = 0
        var curMax = nums(n - 1)

        var idx = n - 2
        while (idx >= 0) {
            val v = nums(idx)
            if (v > curMax) {
                val reduced = spf(v)
                if (reduced <= curMax) {
                    ops += 1
                    curMax = reduced
                } else {
                    return -1
                }
            } else {
                curMax = v
            }
            idx -= 1
        }

        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // Find maximum value to size the sieve
        let max_val = *nums.iter().max().unwrap() as usize;

        // Smallest prime factor (spf) for each number up to max_val
        let mut spf = vec![0usize; max_val + 1];
        if max_val >= 1 {
            spf[1] = 1;
        }
        for i in 2..=max_val {
            if spf[i] == 0 {
                spf[i] = i;
                let mut j = i * i;
                while j <= max_val {
                    if spf[j] == 0 {
                        spf[j] = i;
                    }
                    j += i;
                }
            }
        }

        let mut ops: i32 = 0;
        let mut limit: i32 = i32::MAX; // maximum allowed value for current position

        for &val_i in nums.iter().rev() {
            let val = val_i as i32;
            if val <= limit {
                limit = val;
                continue;
            }
            // Need to reduce this element
            let spf_val = spf[val as usize] as i32; // smallest prime factor (prime)
            if spf_val < val && spf_val <= limit {
                ops += 1;
                limit = spf_val;
            } else {
                return -1;
            }
        }

        ops
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (max-val (if (null? nums) 0 (apply max nums)))
         (spf
          (let ((v (make-vector (+ max-val 1) 0)))
            (when (>= max-val 1)
              (vector-set! v 1 1))
            (for ([i (in-range 2 (add1 max-val))])
              (when (= (vector-ref v i) 0)
                (vector-set! v i i)
                (let loop ((j (* i i)))
                  (when (<= j max-val)
                    (when (= (vector-ref v j) 0)
                      (vector-set! v j i))
                    (set! j (+ j i))))))
            v)))
    (if (= n 0)
        0
        (let loop ((i (- n 2))
                   (cur (vector-ref arr (- n 1)))
                   (ops 0))
          (if (< i 0)
              ops
              (let ((val (vector-ref arr i)))
                (cond
                  [(<= val cur) (loop (- i 1) val ops)]
                  [else
                   (let ((reduced (vector-ref spf val)))
                     (if (and (> val 1) (< reduced val) (<= reduced cur))
                         (loop (- i 1) reduced (+ ops 1))
                         -1))]))))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    Max = lists:max(Nums),
    Limit = trunc(math:sqrt(Max)) + 1,
    Primes = primes_upto(Limit),
    process(lists:reverse(Nums), Primes, undefined, 0).

process([], _Primes, _Cur, Ops) ->
    Ops;
process([H|T], Primes, undefined, Ops) ->
    %% last element, no constraint
    process(T, Primes, H, Ops);
process([H|T], Primes, Cur, Ops) when H =< Cur ->
    process(T, Primes, H, Ops);
process([H|T], Primes, Cur, Ops) ->
    Reduced = smallest_prime_factor(H, Primes),
    case (Reduced < H) andalso (Reduced =< Cur) of
        true -> process(T, Primes, Reduced, Ops + 1);
        false -> -1
    end.

%% Generate list of primes up to N (inclusive)
primes_upto(N) when N < 2 ->
    [];
primes_upto(N) ->
    [P || P <- lists:seq(2, N), is_prime(P)].

is_prime(2) -> true;
is_prime(P) when P > 2 ->
    Limit = trunc(math:sqrt(P)),
    not has_factor(P, 2, Limit).

has_factor(_N, I, Limit) when I > Limit ->
    false;
has_factor(N, I, _Limit) when N rem I =:= 0 ->
    true;
has_factor(N, I, Limit) ->
    has_factor(N, I + 1, Limit).

%% Smallest prime factor of N using precomputed primes list
smallest_prime_factor(1, _) -> 1;
smallest_prime_factor(N, Primes) ->
    find_spf(N, Primes).

find_spf(N, []) -> N; % N is prime larger than any precomputed prime
find_spf(N, [P|Rest]) when P * P > N -> N;
find_spf(N, [P|Rest]) ->
    case N rem P of
        0 -> P;
        _ -> find_spf(N, Rest)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    max_val = Enum.max(nums)
    spf_arr = build_spf(max_val)

    get_spf = fn x ->
      case :array.get(x, spf_arr) do
        0 -> nil
        p when p == x -> nil
        p -> p
      end
    end

    try do
      {ops, _} =
        Enum.reduce(Enum.reverse(nums), {0, max_val + 1}, fn cur, {cnt, nxt} ->
          if cur <= nxt do
            {cnt, cur}
          else
            case get_spf.(cur) do
              nil -> throw(:impossible)
              sp when sp <= nxt -> {cnt + 1, sp}
              _ -> throw(:impossible)
            end
          end
        end)

      ops
    catch
      :impossible -> -1
    end
  end

  defp build_spf(max) do
    arr = :array.new(max + 1, default: 0)

    Enum.reduce(2..max, arr, fn i, acc ->
      case :array.get(i, acc) do
        0 ->
          acc1 = :array.set(i, i, acc)
          set_multiples(i, max, acc1)

        _ ->
          acc
      end
    end)
  end

  defp set_multiples(p, max, arr) do
    start = p * p

    if start > max do
      arr
    else
      set_multiples_rec(start, p, max, arr)
    end
  end

  defp set_multiples_rec(j, step, max, arr) when j <= max do
    arr =
      case :array.get(j, arr) do
        0 -> :array.set(j, step, arr)
        _ -> arr
      end

    set_multiples_rec(j + step, step, max, arr)
  end

  defp set_multiples_rec(_, _, _, arr), do: arr
end
```
