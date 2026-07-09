# 2601. Prime Subtraction Operation

## Cpp

```cpp
class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        int maxVal = *max_element(nums.begin(), nums.end());
        if (maxVal < 2) return true; // all numbers are 1, already increasing
        
        vector<bool> isPrime(maxVal + 1, true);
        isPrime[0] = false;
        if (maxVal >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= maxVal; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxVal; j += i)
                    isPrime[j] = false;
            }
        }
        vector<int> prevPrime(maxVal + 1, 0);
        int last = 0;
        for (int i = 2; i <= maxVal; ++i) {
            if (isPrime[i]) last = i;
            prevPrime[i] = last; // largest prime <= i, or 0 if none
        }
        
        int prev = 0;
        for (int &num : nums) {
            int bound = num - prev - 1; // maximum allowed prime to subtract
            if (bound >= 2) {
                int p = prevPrime[bound];
                if (p > 0) num -= p;
            }
            if (num <= prev) return false;
            prev = num;
        }
        return true;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public boolean primeSubOperation(int[] nums) {
        int max = 0;
        for (int v : nums) {
            if (v > max) max = v;
        }

        // Sieve of Eratosthenes up to max
        boolean[] isPrime = new boolean[max + 1];
        Arrays.fill(isPrime, true);
        if (max >= 0) isPrime[0] = false;
        if (max >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= max; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= max; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        // prevPrime[x] = largest prime <= x
        int[] prevPrime = new int[max + 1];
        int last = 0;
        for (int i = 2; i <= max; i++) {
            if (isPrime[i]) last = i;
            prevPrime[i] = last;
        }

        int prevVal = 0;
        for (int num : nums) {
            int bound = num - prevVal;
            if (bound <= 0) return false;

            int p = 0;
            if (bound - 1 >= 2) {
                p = prevPrime[bound - 1]; // largest prime < bound
            }

            int newVal = num - p; // guaranteed > prevVal because p < bound
            prevVal = newVal;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        max_val = max(nums)
        # Sieve of Eratosthenes up to max_val
        sieve = [True] * (max_val + 1)
        if max_val >= 0:
            sieve[0] = False
        if max_val >= 1:
            sieve[1] = False
        limit = int(max_val ** 0.5) + 1
        for i in range(2, limit):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:max_val + 1:step] = [False] * (((max_val - start) // step) + 1)

        # prev_prime[x] = largest prime <= x (0 if none)
        prev_prime = [0] * (max_val + 1)
        last = 0
        for i in range(2, max_val + 1):
            if sieve[i]:
                last = i
            prev_prime[i] = last

        prev = 0
        for num in nums:
            if num <= prev:
                return False
            diff = num - prev
            if diff > 2:
                # largest prime strictly less than diff
                p = prev_prime[diff - 1]
                if p:
                    num -= p
            prev = num
        return True
```

## Python3

```python
class Solution:
    def primeSubOperation(self, nums):
        from math import isqrt
        max_val = max(nums)
        # Sieve of Eratosthenes up to max_val
        is_prime = [True] * (max_val + 1)
        if max_val >= 0:
            is_prime[0] = False
        if max_val >= 1:
            is_prime[1] = False
        for i in range(2, isqrt(max_val) + 1):
            if is_prime[i]:
                step = i * i
                while step <= max_val:
                    is_prime[step] = False
                    step += i

        # prevPrime[x] = largest prime <= x
        prev_prime = [0] * (max_val + 1)
        last = 0
        for i in range(2, max_val + 1):
            if is_prime[i]:
                last = i
            prev_prime[i] = last

        prev = 0
        for num in nums:
            if num <= prev:
                return False
            diff = num - prev
            # largest prime strictly less than diff
            p = prev_prime[diff - 1] if diff > 2 else 0
            new_val = num - p if p else num
            prev = new_val
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool primeSubOperation(int* nums, int numsSize) {
    const int MAXV = 1000;
    bool isPrime[MAXV + 1];
    memset(isPrime, true, sizeof(isPrime));
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= MAXV; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= MAXV; j += i)
                isPrime[j] = false;
        }
    }

    int prevPrime[MAXV + 1];
    prevPrime[0] = prevPrime[1] = 0;
    for (int i = 2; i <= MAXV; ++i) {
        if (isPrime[i])
            prevPrime[i] = i;
        else
            prevPrime[i] = prevPrime[i - 1];
    }

    int prev = 0; // value of previous element after adjustments
    for (int i = 0; i < numsSize; ++i) {
        int cur = nums[i];
        if (cur <= prev)
            return false;

        int diff = cur - prev;               // > 0
        int p = 0;
        if (diff - 1 >= 2)
            p = prevPrime[diff - 1];          // largest prime < diff

        cur -= p;
        if (cur <= prev)                     // safety check
            return false;

        prev = cur;
    }
    return true;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public bool PrimeSubOperation(int[] nums) {
        int max = 0;
        foreach (int v in nums) if (v > max) max = v;
        int limit = Math.Max(max, 2);
        bool[] isPrime = new bool[limit + 1];
        for (int i = 0; i <= limit; i++) isPrime[i] = true;
        isPrime[0] = false;
        if (limit >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i)
                    isPrime[j] = false;
            }
        }
        int[] largestLess = new int[limit + 2];
        int lastPrime = 0;
        for (int i = 0; i <= limit + 1; i++) {
            if (i - 1 >= 2 && isPrime[i - 1]) lastPrime = i - 1;
            largestLess[i] = lastPrime;
        }

        int prev = 0;
        for (int i = 0; i < nums.Length; i++) {
            int diff = nums[i] - prev;
            if (diff <= 0) return false;
            int p = largestLess[diff]; // largest prime < diff
            nums[i] -= p;
            prev = nums[i];
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
var primeSubOperation = function(nums) {
    const n = nums.length;
    let maxVal = 0;
    for (let v of nums) if (v > maxVal) maxVal = v;

    // Sieve of Eratosthenes up to maxVal
    const isPrime = new Array(maxVal + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let i = 2; i * i <= maxVal; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j <= maxVal; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // best[x] = largest prime <= x
    const best = new Array(maxVal + 1).fill(0);
    for (let i = 2; i <= maxVal; ++i) {
        best[i] = isPrime[i] ? i : best[i - 1];
    }

    let prev = 0;
    for (let num of nums) {
        const bound = num - prev;
        if (bound <= 0) return false;

        // largest prime strictly less than bound
        const p = bound > 1 ? best[bound - 1] : 0;
        const cur = num - p;
        if (cur <= prev) return false; // safety check
        prev = cur;
    }
    return true;
};
```

## Typescript

```typescript
function primeSubOperation(nums: number[]): boolean {
    const n = nums.length;
    if (n === 0) return true;

    const maxNum = Math.max(...nums);
    const limit = maxNum;

    // Sieve of Eratosthenes
    const isPrime = new Array(limit + 1).fill(true);
    if (limit >= 0) isPrime[0] = false;
    if (limit >= 1) isPrime[1] = false;
    for (let i = 2; i * i <= limit; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= limit; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // largestPrimeBelow[x] = largest prime strictly less than x
    const largestPrimeBelow = new Array(limit + 2).fill(0);
    let lastPrime = 0;
    for (let i = 0; i <= limit + 1; i++) {
        largestPrimeBelow[i] = lastPrime;
        if (i <= limit && isPrime[i]) {
            lastPrime = i;
        }
    }

    let prev = 0;
    for (const num of nums) {
        if (num <= prev) return false;
        const diff = num - prev; // positive
        const p = largestPrimeBelow[diff]; // may be 0 if no prime < diff
        const newVal = num - p;
        // newVal is guaranteed > prev because p < diff
        prev = newVal;
    }
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
    function primeSubOperation($nums) {
        $max = max($nums);
        // Sieve of Eratosthenes
        $isPrime = array_fill(0, $max + 1, true);
        if ($max >= 0) $isPrime[0] = false;
        if ($max >= 1) $isPrime[1] = false;
        for ($i = 2; $i * $i <= $max; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $max; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }

        // prevPrime[i] = largest prime <= i (0 if none)
        $prevPrime = array_fill(0, $max + 1, 0);
        $last = 0;
        for ($i = 2; $i <= $max; $i++) {
            if ($isPrime[$i]) {
                $last = $i;
            }
            $prevPrime[$i] = $last;
        }

        $prevVal = 0;
        foreach ($nums as $num) {
            $bound = $num - $prevVal;
            if ($bound <= 0) {
                return false;
            }
            // largest prime strictly less than bound
            $largestPrime = $prevPrime[$bound - 1];
            $newVal = $num - $largestPrime;
            $prevVal = $newVal;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func primeSubOperation(_ nums: [Int]) -> Bool {
        var maxVal = 0
        for v in nums { if v > maxVal { maxVal = v } }
        let limit = max(2, maxVal)
        var isPrime = [Bool](repeating: true, count: limit + 1)
        if limit >= 0 { isPrime[0] = false }
        if limit >= 1 { isPrime[1] = false }
        var i = 2
        while i * i <= limit {
            if isPrime[i] {
                var j = i * i
                while j <= limit {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        var prevPrime = [Int](repeating: 0, count: limit + 1)
        var last = 0
        if limit >= 2 {
            for v in 2...limit {
                if isPrime[v] { last = v }
                prevPrime[v] = last
            }
        }
        var prev = 0
        for num in nums {
            let diff = num - prev
            if diff <= 1 { return false }
            let p = prevPrime[diff - 1]
            if p == 0 { return false }
            let newVal = num - p
            if newVal <= prev { return false }
            prev = newVal
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun primeSubOperation(nums: IntArray): Boolean {
        val maxVal = nums.maxOrNull() ?: 0
        if (maxVal < 2) return true

        // Sieve of Eratosthenes up to maxVal
        val isPrime = BooleanArray(maxVal + 1) { true }
        isPrime[0] = false
        if (maxVal >= 1) isPrime[1] = false
        var i = 2
        while (i * i <= maxVal) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= maxVal) {
                    isPrime[j] = false
                    j += i
                }
            }
            i++
        }

        // prevPrime[x] = largest prime <= x, or 0 if none
        val prevPrime = IntArray(maxVal + 1)
        var last = 0
        for (k in 0..maxVal) {
            if (isPrime[k]) last = k
            prevPrime[k] = last
        }

        var prev = 0
        for (num in nums) {
            val diff = num - prev
            if (diff <= 0) return false
            var p = 0
            if (diff > 2) {
                // need largest prime < diff, i.e., <= diff-1
                p = prevPrime[diff - 1]
            }
            val newVal = num - p
            if (newVal <= prev) return false
            prev = newVal
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool primeSubOperation(List<int> nums) {
    const int maxVal = 1000;
    // Sieve of Eratosthenes
    List<bool> isPrime = List.filled(maxVal + 1, true);
    isPrime[0] = false;
    isPrime[1] = false;
    for (int i = 2; i * i <= maxVal; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j <= maxVal; j += i) {
          isPrime[j] = false;
        }
      }
    }
    // previousPrime[x] = largest prime <= x
    List<int> prevPrime = List.filled(maxVal + 1, 0);
    int last = 0;
    for (int i = 2; i <= maxVal; ++i) {
      if (isPrime[i]) last = i;
      prevPrime[i] = last;
    }

    int prev = 0; // value of previous element after operations
    for (int num in nums) {
      if (num <= prev) return false;
      int diff = num - prev; // need a prime < diff to subtract
      int p = 0;
      if (diff > 2) {
        p = prevPrime[diff - 1]; // largest prime strictly less than diff
      }
      int cur = (p > 0) ? num - p : num;
      if (cur <= prev) return false; // safety check
      prev = cur;
    }
    return true;
  }
}
```

## Golang

```go
func primeSubOperation(nums []int) bool {
    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }

    // Sieve of Eratosthenes up to maxVal
    isPrime := make([]bool, maxVal+1)
    for i := 2; i <= maxVal; i++ {
        isPrime[i] = true
    }
    for p := 2; p*p <= maxVal; p++ {
        if isPrime[p] {
            for multiple := p * p; multiple <= maxVal; multiple += p {
                isPrime[multiple] = false
            }
        }
    }

    // prevPrime[i] = largest prime <= i (0 if none)
    prevPrime := make([]int, maxVal+1)
    last := 0
    for i := 2; i <= maxVal; i++ {
        if isPrime[i] {
            last = i
        }
        prevPrime[i] = last
    }

    prev := 0
    for _, val := range nums {
        diff := val - prev
        if diff <= 1 { // need at least a prime (2) less than diff
            return false
        }
        // largest prime strictly less than diff
        p := prevPrime[diff-1]
        if p == 0 {
            return false
        }
        newVal := val - p
        if newVal <= prev { // should not happen, safety check
            return false
        }
        prev = newVal
    }
    return true
}
```

## Ruby

```ruby
def prime_sub_operation(nums)
  max_val = nums.max
  limit = max_val
  is_prime = Array.new(limit + 1, true)
  if limit >= 0
    is_prime[0] = false
    is_prime[1] = false if limit >= 1
  end
  i = 2
  while i * i <= limit
    if is_prime[i]
      j = i * i
      while j <= limit
        is_prime[j] = false
        j += i
      end
    end
    i += 1
  end

  prev_prime = Array.new(limit + 1, -1)
  last = -1
  (2..limit).each do |idx|
    if is_prime[idx]
      last = idx
    end
    prev_prime[idx] = last
  end

  prev = 0
  nums.each do |num|
    diff = num - prev
    bound = diff - 1
    if bound >= 2
      p = prev_prime[bound]
      if p && p > 0
        num -= p
      end
    end
    return false if num <= prev
    prev = num
  end
  true
end
```

## Scala

```scala
object Solution {
    def primeSubOperation(nums: Array[Int]): Boolean = {
        if (nums.isEmpty) return true
        val limit = nums.max
        // Sieve of Eratosthenes
        val isPrime = Array.fill(limit + 1)(true)
        if (limit >= 0) isPrime(0) = false
        if (limit >= 1) isPrime(1) = false
        var p = 2
        while (p * p <= limit) {
            if (isPrime(p)) {
                var multiple = p * p
                while (multiple <= limit) {
                    isPrime(multiple) = false
                    multiple += p
                }
            }
            p += 1
        }
        // previousPrime[i] = largest prime <= i, 0 if none
        val prevPrime = new Array[Int](limit + 1)
        var last = 0
        for (i <- 2 to limit) {
            if (isPrime(i)) last = i
            prevPrime(i) = last
        }

        var prevVal = 0 // virtual previous value before first element
        for (cur <- nums) {
            val bound = cur - prevVal
            if (bound <= 0) return false
            // largest prime strictly less than bound
            val prime = if (bound - 1 >= 2) prevPrime(bound - 1) else 0
            var newVal = cur
            if (prime > 0) newVal = cur - prime
            if (newVal <= prevVal) return false
            prevVal = newVal
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn prime_sub_operation(nums: Vec<i32>) -> bool {
        if nums.is_empty() {
            return true;
        }
        let max_val = *nums.iter().max().unwrap() as usize;

        // Sieve of Eratosthenes
        let mut is_prime = vec![true; max_val + 1];
        if max_val >= 0 {
            is_prime[0] = false;
        }
        if max_val >= 1 {
            is_prime[1] = false;
        }
        let limit = (max_val as f64).sqrt() as usize;
        for i in 2..=limit {
            if is_prime[i] {
                let mut j = i * i;
                while j <= max_val {
                    is_prime[j] = false;
                    j += i;
                }
            }
        }

        // previous_prime[x] = largest prime <= x
        let mut prev_prime = vec![0usize; max_val + 1];
        for i in 2..=max_val {
            if is_prime[i] {
                prev_prime[i] = i;
            } else {
                prev_prime[i] = prev_prime[i - 1];
            }
        }

        let mut prev: i32 = 0;
        for &num in nums.iter() {
            let diff = num - prev;
            if diff <= 2 {
                return false;
            }
            // largest prime strictly less than diff
            let idx = (diff - 1) as usize;
            let p = prev_prime[idx] as i32;
            if p == 0 {
                return false;
            }
            let new_val = num - p;
            prev = new_val;
        }
        true
    }
}
```

## Racket

```racket
(define/contract (prime-sub-operation nums)
  (-> (listof exact-integer?) boolean?)
  (if (null? nums)
      #t
      (let* ((max-val (apply max nums))
             (is-prime (make-vector (+ max-val 1) #t)))
        ;; initialize sieve
        (vector-set! is-prime 0 #f)
        (when (> max-val 0) (vector-set! is-prime 1 #f))
        (let loop ((i 2))
          (when (<= (* i i) max-val)
            (when (vector-ref is-prime i)
              (let inner ((j (* i i)))
                (when (<= j max-val)
                  (vector-set! is-prime j #f)
                  (inner (+ j i)))))
            (loop (+ i 1))))
        ;; previous prime <= x
        (define prev-prime (make-vector (+ max-val 1) 0))
        (let ((last 0))
          (for ([idx (in-range (+ max-val 1))])
            (when (vector-ref is-prime idx)
              (set! last idx))
            (vector-set! prev-prime idx last)))
        ;; greedy adjustment
        (let loop2 ((lst nums) (prev 0))
          (if (null? lst)
              #t
              (let* ((cur (car lst)))
                (if (<= cur prev)
                    #f
                    (let* ((diff (- cur prev))
                           (new-val
                            (if (> diff 2)
                                (let ((p (vector-ref prev-prime (- diff 1))))
                                  (if (= p 0) ; no prime less than diff
                                      cur
                                      (- cur p)))
                                cur)))
                      (loop2 (cdr lst) new-val)))))))))
```

## Erlang

```erlang
-module(solution).
-export([prime_sub_operation/1]).

prime_sub_operation(Nums) ->
    process(Nums, 0).

process([], _Prev) -> 
    true;
process([Num|Rest], Prev) ->
    Diff = Num - Prev,
    if Diff =< 0 ->
            false;
       true ->
            case largest_prime_less_than(Diff) of
                undefined -> NewVal = Num;
                P -> NewVal = Num - P
            end,
            process(Rest, NewVal)
    end.

largest_prime_less_than(N) when N =< 2 ->
    undefined;
largest_prime_less_than(N) ->
    find_prime(N-1).

find_prime(X) when X < 2 ->
    undefined;
find_prime(X) ->
    if is_prime(X) -> X;
       true -> find_prime(X-1)
    end.

is_prime(Num) when Num < 2 ->
    false;
is_prime(Num) ->
    Max = trunc(math:sqrt(Num)),
    is_prime_div(Num, 2, Max).

is_prime_div(_Num, I, Max) when I > Max ->
    true;
is_prime_div(Num, I, Max) ->
    if Num rem I == 0 -> false;
       true -> is_prime_div(Num, I+1, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec prime_sub_operation(nums :: [integer]) :: boolean
  def prime_sub_operation(nums) do
    case nums do
      [] -> true
      _ ->
        max_val = Enum.max(nums)

        primes_set = MapSet.new(prime_list(max_val))

        {_last, prime_upto_map} =
          Enum.reduce(0..max_val, {0, %{}}, fn i, {last, acc} ->
            new_last = if MapSet.member?(primes_set, i), do: i, else: last
            {new_last, Map.put(acc, i, new_last)}
          end)

        Enum.reduce_while(nums, 0, fn cur, prev ->
          diff = cur - prev

          cond do
            diff <= 0 ->
              {:halt, false}

            true ->
              p =
                if diff > 2,
                  do: Map.get(prime_upto_map, diff - 1, 0),
                  else: 0

              new_val = if p == 0, do: cur, else: cur - p

              if new_val <= prev,
                do: {:halt, false},
                else: {:cont, new_val}
          end
        end)
        |> case do
          false -> false
          _ -> true
        end
    end
  end

  defp prime_list(limit) when limit < 2, do: []

  defp prime_list(limit) do
    2..limit |> Enum.filter(&prime?/1)
  end

  defp prime?(n) when n < 2, do: false
  defp prime?(2), do: true

  defp prime?(n) do
    max = :math.sqrt(n) |> trunc

    2..max
    |> Enum.all?(fn i -> rem(n, i) != 0 end)
  end
end
```
