# 2523. Closest Prime Numbers in Range

## Cpp

```cpp
class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        if (right < 2) return {-1, -1};
        vector<char> isPrime(right + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * 1LL * i <= right; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= right; j += i)
                    isPrime[j] = false;
            }
        }
        int prev = -1;
        int bestA = -1, bestB = -1;
        int minDiff = INT_MAX;
        for (int num = max(left, 2); num <= right; ++num) {
            if (!isPrime[num]) continue;
            if (prev != -1) {
                int diff = num - prev;
                if (diff < minDiff) {
                    minDiff = diff;
                    bestA = prev;
                    bestB = num;
                    if (minDiff == 2) break; // cannot get smaller
                }
            }
            prev = num;
        }
        if (bestA == -1) return {-1, -1};
        return {bestA, bestB};
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[] closestPrimes(int left, int right) {
        boolean[] isPrime = new boolean[right + 1];
        Arrays.fill(isPrime, true);
        if (right >= 0) isPrime[0] = false;
        if (right >= 1) isPrime[1] = false;

        for (int i = 2; i * i <= right; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= right; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int prev = -1;
        int bestA = -1, bestB = -1;
        int minDiff = Integer.MAX_VALUE;

        for (int i = left; i <= right; i++) {
            if (isPrime[i]) {
                if (prev != -1) {
                    int diff = i - prev;
                    if (diff < minDiff) {
                        minDiff = diff;
                        bestA = prev;
                        bestB = i;
                        if (minDiff == 2) break; // smallest possible gap
                    }
                }
                prev = i;
            }
        }

        if (bestA == -1) return new int[]{-1, -1};
        return new int[]{bestA, bestB};
    }
}
```

## Python

```python
class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        n = right
        # Sieve of Eratosthenes using bytearray for memory efficiency
        is_prime = bytearray(b'\x01') * (n + 1)
        if n >= 0:
            is_prime[0] = 0
        if n >= 1:
            is_prime[1] = 0

        import math
        limit = int(math.isqrt(n))
        for i in range(2, limit + 1):
            if is_prime[i]:
                start = i * i
                step = i
                is_prime[start:n + 1:step] = b'\x00' * (((n - start) // step) + 1)

        prev = -1
        best = [-1, -1]
        min_gap = 10 ** 9

        for num in range(left, right + 1):
            if is_prime[num]:
                if prev != -1:
                    gap = num - prev
                    if gap < min_gap:
                        min_gap = gap
                        best = [prev, num]
                        # smallest possible gap found; can return immediately
                        if gap == 2:
                            return best
                prev = num

        return best
```

## Python3

```python
from typing import List
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2 or left > right:
            return [-1, -1]
        n = right
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        limit = int(math.isqrt(n))
        for i in range(2, limit + 1):
            if is_prime[i]:
                step = i
                start = i * i
                is_prime[start:n+1:step] = [False] * ((n - start) // step + 1)
        prev = -1
        best_pair = [-1, -1]
        min_gap = float('inf')
        for num in range(left, right + 1):
            if is_prime[num]:
                if prev != -1:
                    gap = num - prev
                    if gap < min_gap:
                        min_gap = gap
                        best_pair = [prev, num]
                        if min_gap == 2:  # cannot get smaller than twin primes
                            return best_pair
                prev = num
        return best_pair if min_gap != float('inf') else [-1, -1]
```

## C

```c
#include <stdlib.h>
#include <math.h>
#include <limits.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestPrimes(int left, int right, int* returnSize) {
    int n = right;
    char *isPrime = (char *)malloc((n + 1) * sizeof(char));
    for (int i = 0; i <= n; ++i) isPrime[i] = 1;
    if (n >= 0) isPrime[0] = 0;
    if (n >= 1) isPrime[1] = 0;

    int limit = (int)sqrt((double)n);
    for (int i = 2; i <= limit; ++i) {
        if (isPrime[i]) {
            for (long long j = 1LL * i * i; j <= n; j += i)
                isPrime[(int)j] = 0;
        }
    }

    int prev = -1;
    int bestA = -1, bestB = -1;
    int bestDiff = INT_MAX;

    for (int num = left > 2 ? left : 2; num <= right; ++num) {
        if (isPrime[num]) {
            if (prev != -1) {
                int diff = num - prev;
                if (diff < bestDiff) {
                    bestDiff = diff;
                    bestA = prev;
                    bestB = num;
                }
            }
            prev = num;
        }
    }

    free(isPrime);

    int *res = (int *)malloc(2 * sizeof(int));
    res[0] = bestA;
    res[1] = bestB;
    *returnSize = 2;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] ClosestPrimes(int left, int right)
    {
        if (right < 2) return new int[] { -1, -1 };

        bool[] isPrime = new bool[right + 1];
        for (int i = 2; i <= right; i++) isPrime[i] = true;

        for (int p = 2; p * p <= right; p++)
        {
            if (!isPrime[p]) continue;
            for (int multiple = p * p; multiple <= right; multiple += p)
                isPrime[multiple] = false;
        }

        int prev = -1;
        int bestA = -1, bestB = -1;
        int minDiff = int.MaxValue;

        for (int i = left; i <= right; i++)
        {
            if (!isPrime[i]) continue;

            if (prev != -1)
            {
                int diff = i - prev;
                if (diff < minDiff)
                {
                    minDiff = diff;
                    bestA = prev;
                    bestB = i;
                    if (minDiff == 2) break; // smallest possible gap
                }
            }
            prev = i;
        }

        if (bestA == -1) return new int[] { -1, -1 };
        return new int[] { bestA, bestB };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var closestPrimes = function(left, right) {
    const n = right;
    const isPrime = new Uint8Array(n + 1);
    for (let i = 2; i <= n; ++i) isPrime[i] = 1;

    const limit = Math.floor(Math.sqrt(n));
    for (let p = 2; p <= limit; ++p) {
        if (isPrime[p]) {
            for (let multiple = p * p; multiple <= n; multiple += p) {
                isPrime[multiple] = 0;
            }
        }
    }

    let prev = -1;
    let bestA = -1, bestB = -1;
    let minDiff = Number.MAX_SAFE_INTEGER;

    for (let i = left; i <= right; ++i) {
        if (isPrime[i]) {
            if (prev !== -1) {
                const diff = i - prev;
                if (diff < minDiff) {
                    minDiff = diff;
                    bestA = prev;
                    bestB = i;
                    if (minDiff === 2) break; // smallest possible gap
                }
            }
            prev = i;
        }
    }

    return bestA === -1 ? [-1, -1] : [bestA, bestB];
};
```

## Typescript

```typescript
function closestPrimes(left: number, right: number): number[] {
    const n = right;
    const isPrime = new Uint8Array(n + 1);
    if (n >= 2) {
        isPrime.fill(1, 2);
    }
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= n; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    let prev = -1;
    let bestA = -1, bestB = -1;
    let minDiff = Number.MAX_SAFE_INTEGER;

    for (let i = left; i <= right; ++i) {
        if (isPrime[i]) {
            if (prev !== -1) {
                const diff = i - prev;
                if (diff < minDiff) {
                    minDiff = diff;
                    bestA = prev;
                    bestB = i;
                    if (minDiff === 2) break; // cannot get smaller
                }
            }
            prev = i;
        }
    }

    return bestA === -1 ? [-1, -1] : [bestA, bestB];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer[]
     */
    function closestPrimes($left, $right) {
        $limit = $right;
        // Sieve of Eratosthenes
        $isPrime = array_fill(0, $limit + 1, true);
        if ($limit >= 0) $isPrime[0] = false;
        if ($limit >= 1) $isPrime[1] = false;
        for ($i = 2; $i * $i <= $limit; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $limit; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }

        $prev = -1;
        $best = [-1, -1];
        $minDiff = PHP_INT_MAX;

        for ($num = $left; $num <= $right; $num++) {
            if ($isPrime[$num]) {
                if ($prev != -1) {
                    $diff = $num - $prev;
                    if ($diff < $minDiff) {
                        $minDiff = $diff;
                        $best = [$prev, $num];
                        if ($diff == 2) { // smallest possible gap
                            return $best;
                        }
                    }
                }
                $prev = $num;
            }
        }

        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func closestPrimes(_ left: Int, _ right: Int) -> [Int] {
        if right < 2 { return [-1, -1] }
        var isPrime = [Bool](repeating: true, count: right + 1)
        if right >= 0 { isPrime[0] = false }
        if right >= 1 { isPrime[1] = false }
        let limit = Int(Double(right).squareRoot())
        if limit >= 2 {
            for i in 2...limit where isPrime[i] {
                var j = i * i
                while j <= right {
                    isPrime[j] = false
                    j += i
                }
            }
        }
        var prev: Int? = nil
        var bestDiff = Int.max
        var ans = [-1, -1]
        for num in left...right where isPrime[num] {
            if let p = prev {
                let diff = num - p
                if diff < bestDiff {
                    bestDiff = diff
                    ans[0] = p
                    ans[1] = num
                    if bestDiff == 2 { return ans }
                }
            }
            prev = num
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closestPrimes(left: Int, right: Int): IntArray {
        val n = right
        val isPrime = BooleanArray(n + 1) { true }
        if (n >= 0) isPrime[0] = false
        if (n >= 1) isPrime[1] = false
        var i = 2
        while (i * i <= n) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= n) {
                    isPrime[j] = false
                    j += i
                }
            }
            i++
        }

        var prev = -1
        var bestA = -1
        var bestB = -1
        var minDiff = Int.MAX_VALUE

        for (num in left..right) {
            if (isPrime[num]) {
                if (prev != -1) {
                    val diff = num - prev
                    if (diff < minDiff) {
                        minDiff = diff
                        bestA = prev
                        bestB = num
                        if (minDiff == 2) break
                    }
                }
                prev = num
            }
        }

        return if (bestA == -1) intArrayOf(-1, -1) else intArrayOf(bestA, bestB)
    }
}
```

## Dart

```dart
class Solution {
  List<int> closestPrimes(int left, int right) {
    if (right < 2) return [-1, -1];
    List<bool> isPrime = List.filled(right + 1, true);
    isPrime[0] = false;
    if (right >= 1) isPrime[1] = false;

    for (int i = 2; i * i <= right; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j <= right; j += i) {
          isPrime[j] = false;
        }
      }
    }

    int prev = -1;
    int bestA = -1, bestB = -1;
    int minDiff = 1 << 30;

    for (int i = left; i <= right; ++i) {
      if (isPrime[i]) {
        if (prev != -1) {
          int diff = i - prev;
          if (diff < minDiff) {
            minDiff = diff;
            bestA = prev;
            bestB = i;
            if (minDiff == 2) break; // smallest possible gap
          }
        }
        prev = i;
      }
    }

    if (bestA == -1) return [-1, -1];
    return [bestA, bestB];
  }
}
```

## Golang

```go
func closestPrimes(left int, right int) []int {
    if right < 2 || left > right {
        return []int{-1, -1}
    }
    n := right
    isPrime := make([]bool, n+1)
    for i := 2; i <= n; i++ {
        isPrime[i] = true
    }
    for p := 2; p*p <= n; p++ {
        if isPrime[p] {
            for multiple := p * p; multiple <= n; multiple += p {
                isPrime[multiple] = false
            }
        }
    }

    prev := -1
    bestA, bestB := -1, -1
    minDiff := int(^uint(0) >> 1) // max int

    for i := left; i <= right; i++ {
        if i >= 2 && isPrime[i] {
            if prev != -1 {
                diff := i - prev
                if diff < minDiff {
                    minDiff = diff
                    bestA, bestB = prev, i
                    if minDiff == 2 { // smallest possible gap
                        return []int{bestA, bestB}
                    }
                }
            }
            prev = i
        }
    }

    if bestA == -1 {
        return []int{-1, -1}
    }
    return []int{bestA, bestB}
}
```

## Ruby

```ruby
def closest_primes(left, right)
  return [-1, -1] if left > right

  limit = right
  is_prime = Array.new(limit + 1, true)
  is_prime[0] = is_prime[1] = false if limit >= 1

  max_i = Math.sqrt(limit).to_i
  (2..max_i).each do |i|
    next unless is_prime[i]
    step = i
    j = i * i
    while j <= limit
      is_prime[j] = false
      j += step
    end
  end

  prev = nil
  best_pair = [-1, -1]
  min_gap = Float::INFINITY

  (left..right).each do |num|
    next unless is_prime[num]
    if prev
      gap = num - prev
      if gap < min_gap
        min_gap = gap
        best_pair = [prev, num]
        # early exit if gap == 2, can't get smaller
        return best_pair if min_gap == 2
      end
    end
    prev = num
  end

  best_pair
end
```

## Scala

```scala
object Solution {
    def closestPrimes(left: Int, right: Int): Array[Int] = {
        val n = right
        if (n < 2) return Array(-1, -1)
        val isPrime = Array.fill(n + 1)(true)
        isPrime(0) = false
        isPrime(1) = false
        var i = 2
        while (i * i <= n) {
            if (isPrime(i)) {
                var j = i * i
                while (j <= n) {
                    isPrime(j) = false
                    j += i
                }
            }
            i += 1
        }

        var prev = -1
        var bestA = -1
        var bestB = -1
        var minDiff = Int.MaxValue

        var num = left
        while (num <= right) {
            if (isPrime(num)) {
                if (prev != -1) {
                    val diff = num - prev
                    if (diff < minDiff) {
                        minDiff = diff
                        bestA = prev
                        bestB = num
                    }
                }
                prev = num
            }
            num += 1
        }

        if (bestA == -1) Array(-1, -1) else Array(bestA, bestB)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn closest_primes(left: i32, right: i32) -> Vec<i32> {
        let l = left as usize;
        let r = right as usize;
        if r < 2 {
            return vec![-1, -1];
        }
        let mut is_prime = vec![true; r + 1];
        if r >= 0 { is_prime[0] = false; }
        if r >= 1 { is_prime[1] = false; }

        let limit = (r as f64).sqrt() as usize;
        for i in 2..=limit {
            if is_prime[i] {
                let mut j = i * i;
                while j <= r {
                    is_prime[j] = false;
                    j += i;
                }
            }
        }

        let mut prev: Option<usize> = None;
        let mut best_a = -1_i32;
        let mut best_b = -1_i32;
        let mut min_diff = usize::MAX;

        for num in l..=r {
            if is_prime[num] {
                if let Some(p) = prev {
                    let diff = num - p;
                    if diff < min_diff {
                        min_diff = diff;
                        best_a = p as i32;
                        best_b = num as i32;
                    }
                }
                prev = Some(num);
            }
        }

        if best_a == -1 {
            vec![-1, -1]
        } else {
            vec![best_a, best_b]
        }
    }
}
```

## Racket

```racket
(define/contract (closest-primes left right)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let* ([size (add1 right)]
         [is-prime (make-vector size #t)])
    (when (>= size 1) (vector-set! is-prime 0 #f))
    (when (>= size 2) (vector-set! is-prime 1 #f))
    (let ([limit (exact-floor (sqrt right))])
      (for ([i (in-range 2 (add1 limit))])
        (when (vector-ref is-prime i)
          (for ([j (in-range (* i i) (add1 right) i)])
            (vector-set! is-prime j #f)))))
    (let ([prev -1]
          [best-a -1]
          [best-b -1]
          [min-diff (+ right 1)])
      (for ([n (in-range left (add1 right))])
        (when (vector-ref is-prime n)
          (if (= prev -1)
              (set! prev n)
              (let ([diff (- n prev)])
                (when (< diff min-diff)
                  (set! best-a prev)
                  (set! best-b n)
                  (set! min-diff diff))
                (set! prev n)))))
      (if (= best-a -1) (list -1 -1) (list best-a best-b)))))
```

## Erlang

```erlang
-module(solution).
-export([closest_primes/2]).

-spec closest_primes(Left :: integer(), Right :: integer()) -> [integer()].
closest_primes(Left, Right) ->
    Max = Right,
    Sieve0 = array:new(Max + 1, {default, true}),
    Sieve1 = array:set(0, false, array:set(1, false, Sieve0)),
    Limit = trunc(math:sqrt(Max)),
    Sieve = sieve_mark(2, Limit, Max, Sieve1),
    find_closest(Sieve, Left, Right).

sieve_mark(I, Limit, _Max, Arr) when I > Limit ->
    Arr;
sieve_mark(I, Limit, Max, Arr) ->
    case array:get(I, Arr) of
        true ->
            Arr1 = mark_multiples(I * I, I, Max, Arr),
            sieve_mark(I + 1, Limit, Max, Arr1);
        false ->
            sieve_mark(I + 1, Limit, Max, Arr)
    end.

mark_multiples(J, _Step, Max, Arr) when J > Max ->
    Arr;
mark_multiples(J, Step, Max, Arr) ->
    Arr1 = array:set(J, false, Arr),
    mark_multiples(J + Step, Step, Max, Arr1).

find_closest(Arr, Left, Right) ->
    find_closest_loop(Left, Right, Arr, undefined, -1, -1, 1000000000).

find_closest_loop(N, Right, _Arr, _Prev, BestA, BestB, _MinDiff) when N > Right ->
    case BestA of
        -1 -> [-1, -1];
        _  -> [BestA, BestB]
    end;
find_closest_loop(N, Right, Arr, Prev, BestA, BestB, MinDiff) ->
    case array:get(N, Arr) of
        true ->
            case Prev of
                undefined ->
                    find_closest_loop(N + 1, Right, Arr, N, BestA, BestB, MinDiff);
                _Prev when N - _Prev =:= 2 ->
                    [_Prev, N];
                _Prev ->
                    Diff = N - _Prev,
                    if Diff < MinDiff ->
                        find_closest_loop(N + 1, Right, Arr, N, _Prev, N, Diff);
                       true ->
                        find_closest_loop(N + 1, Right, Arr, N, BestA, BestB, MinDiff)
                    end
            end;
        false ->
            find_closest_loop(N + 1, Right, Arr, Prev, BestA, BestB, MinDiff)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec closest_primes(left :: integer, right :: integer) :: [integer]
  def closest_primes(left, right) do
    limit = right

    # Initialize sieve with all true, then set 0 and 1 to false
    sieve =
      :array.new(limit + 1, default: true)
      |> :array.set(0, false)
      |> :array.set(1, false)

    max_i = :math.sqrt(limit) |> trunc()

    sieve =
      Enum.reduce(2..max_i, sieve, fn i, acc ->
        if :array.get(i, acc) do
          mark_multiples(acc, i, i * i, limit)
        else
          acc
        end
      end)

    # Scan the range to find the closest prime pair
    result =
      Enum.reduce(left..right, %{prev: -1, a: -1, b: -1, md: 1_000_000_000}, fn num, state ->
        if :array.get(num, sieve) do
          if state.prev != -1 do
            diff = num - state.prev

            if diff < state.md do
              %{state | prev: num, a: state.prev, b: num, md: diff}
            else
              %{state | prev: num}
            end
          else
            %{state | prev: num}
          end
        else
          state
        end
      end)

    if result.a == -1 do
      [-1, -1]
    else
      [result.a, result.b]
    end
  end

  defp mark_multiples(sieve, step, start, limit) do
    do_mark(sieve, step, start, limit)
  end

  defp do_mark(sieve, _step, current, limit) when current > limit, do: sieve

  defp do_mark(sieve, step, current, limit) do
    sieve = :array.set(current, false, sieve)
    do_mark(sieve, step, current + step, limit)
  end
end
```
