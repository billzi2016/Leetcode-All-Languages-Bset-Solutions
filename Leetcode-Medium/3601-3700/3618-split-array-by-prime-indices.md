# 3618. Split Array by Prime Indices

## Cpp

```cpp
class Solution {
public:
    long long splitArray(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<bool> isPrime(n, true);
        if (n > 0) isPrime[0] = false;
        if (n > 1) isPrime[1] = false;
        for (int p = 2; p * p < n; ++p) {
            if (isPrime[p]) {
                for (int multiple = p * p; multiple < n; multiple += p)
                    isPrime[multiple] = false;
            }
        }
        long long sumA = 0, sumB = 0;
        for (int i = 0; i < n; ++i) {
            if (isPrime[i])
                sumA += nums[i];
            else
                sumB += nums[i];
        }
        return std::llabs(sumA - sumB);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long splitArray(int[] nums) {
        int n = nums.length;
        boolean[] isPrime = new boolean[n];
        if (n > 2) {
            Arrays.fill(isPrime, true);
            isPrime[0] = false;
            isPrime[1] = false;
            for (int i = 2; i * i < n; i++) {
                if (isPrime[i]) {
                    for (int j = i * i; j < n; j += i) {
                        isPrime[j] = false;
                    }
                }
            }
        } else {
            if (n > 0) isPrime[0] = false;
            if (n > 1) isPrime[1] = false;
        }

        long sumA = 0, sumB = 0;
        for (int i = 0; i < n; i++) {
            if (isPrime[i]) {
                sumA += nums[i];
            } else {
                sumB += nums[i];
            }
        }
        return Math.abs(sumA - sumB);
    }
}
```

## Python

```python
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            # No prime indices (prime numbers start from 2)
            return abs(sum(nums))
        
        is_prime = [True] * n
        is_prime[0] = False
        if n > 1:
            is_prime[1] = False
        
        p = 2
        while p * p < n:
            if is_prime[p]:
                step = p
                start = p * p
                for multiple in range(start, n, step):
                    is_prime[multiple] = False
            p += 1
        
        sum_a = 0
        sum_b = 0
        for i, val in enumerate(nums):
            if is_prime[i]:
                sum_a += val
            else:
                sum_b += val
        return abs(sum_a - sum_b)
```

## Python3

```python
from typing import List
import math

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        sumA = 0
        sumB = 0

        if n < 2:
            # No prime indices exist
            for v in nums:
                sumB += v
            return abs(sumA - sumB)

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        limit = int(math.isqrt(n - 1))
        for i in range(2, limit + 1):
            if is_prime[i]:
                step = i
                start = i * i
                for j in range(start, n, step):
                    is_prime[j] = False

        for idx, val in enumerate(nums):
            if is_prime[idx]:
                sumA += val
            else:
                sumB += val

        return abs(sumA - sumB)
```

## C

```c
#include <stdlib.h>

long long splitArray(int* nums, int numsSize) {
    if (numsSize <= 0) return 0;
    
    char *isPrime = (char *)malloc(numsSize * sizeof(char));
    for (int i = 0; i < numsSize; ++i) isPrime[i] = 1;
    if (numsSize > 0) isPrime[0] = 0;
    if (numsSize > 1) isPrime[1] = 0;
    
    for (int p = 2; (long long)p * p < numsSize; ++p) {
        if (isPrime[p]) {
            for (long long multiple = (long long)p * p; multiple < numsSize; multiple += p)
                isPrime[multiple] = 0;
        }
    }
    
    long long sumA = 0, sumB = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (isPrime[i]) sumA += nums[i];
        else sumB += nums[i];
    }
    
    free(isPrime);
    
    long long diff = sumA - sumB;
    return diff >= 0 ? diff : -diff;
}
```

## Csharp

```csharp
public class Solution
{
    public long SplitArray(int[] nums)
    {
        int n = nums.Length;
        bool[] isPrime = new bool[n];
        if (n > 2)
        {
            for (int i = 2; i < n; i++) isPrime[i] = true;

            for (int p = 2; p * p < n; p++)
            {
                if (!isPrime[p]) continue;
                for (int multiple = p * p; multiple < n; multiple += p)
                    isPrime[multiple] = false;
            }
        }

        long sumA = 0, sumB = 0;
        for (int i = 0; i < n; i++)
        {
            if (isPrime[i])
                sumA += nums[i];
            else
                sumB += nums[i];
        }

        long diff = sumA - sumB;
        return diff >= 0 ? diff : -diff;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var splitArray = function(nums) {
    const n = nums.length;
    // Sieve of Eratosthenes for indices [0, n-1]
    const isPrime = new Uint8Array(n);
    if (n > 2) {
        for (let i = 2; i < n; i++) isPrime[i] = 1;
        for (let p = 2; p * p < n; p++) {
            if (isPrime[p]) {
                for (let multiple = p * p; multiple < n; multiple += p) {
                    isPrime[multiple] = 0;
                }
            }
        }
    }
    let sumA = 0, sumB = 0;
    for (let i = 0; i < n; i++) {
        if (isPrime[i]) sumA += nums[i];
        else sumB += nums[i];
    }
    return Math.abs(sumA - sumB);
};
```

## Typescript

```typescript
function splitArray(nums: number[]): number {
    const n = nums.length;
    const isPrime = new Uint8Array(n);
    if (n > 2) {
        for (let i = 2; i < n; i++) isPrime[i] = 1;
        for (let p = 2; p * p < n; p++) {
            if (isPrime[p]) {
                for (let multiple = p * p; multiple < n; multiple += p) {
                    isPrime[multiple] = 0;
                }
            }
        }
    }
    let sumA = 0, sumB = 0;
    for (let i = 0; i < n; i++) {
        if (isPrime[i]) sumA += nums[i];
        else sumB += nums[i];
    }
    return Math.abs(sumA - sumB);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function splitArray($nums) {
        $n = count($nums);
        if ($n < 3) {
            // No prime indices (2 is the smallest prime index)
            $sumA = 0;
            $sumB = array_sum($nums);
            return abs($sumA - $sumB);
        }

        // Sieve of Eratosthenes for indices [0, n-1]
        $isPrime = array_fill(0, $n, true);
        $isPrime[0] = false;
        $isPrime[1] = false;

        for ($i = 2; $i * $i < $n; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j < $n; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }

        $sumA = 0;
        $sumB = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($isPrime[$i]) {
                $sumA += $nums[$i];
            } else {
                $sumB += $nums[$i];
            }
        }

        return abs($sumA - $sumB);
    }
}
```

## Swift

```swift
class Solution {
    func splitArray(_ nums: [Int]) -> Int {
        let n = nums.count
        var isPrime = [Bool](repeating: true, count: max(n, 2))
        if n > 0 { isPrime[0] = false }
        if n > 1 { isPrime[1] = false }
        
        var i = 2
        while i * i < n {
            if isPrime[i] {
                var j = i * i
                while j < n {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        
        var sumA: Int64 = 0
        var sumB: Int64 = 0
        
        for idx in 0..<n {
            if isPrime[idx] {
                sumA += Int64(nums[idx])
            } else {
                sumB += Int64(nums[idx])
            }
        }
        
        let diff = sumA - sumB
        return diff >= 0 ? Int(diff) : Int(-diff)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitArray(nums: IntArray): Long {
        val n = nums.size
        if (n == 0) return 0L

        // Sieve of Eratosthenes for indices [0, n-1]
        val isPrime = BooleanArray(n) { true }
        if (n > 0) isPrime[0] = false
        if (n > 1) isPrime[1] = false
        var p = 2
        while (p * p < n) {
            if (isPrime[p]) {
                var multiple = p * p
                while (multiple < n) {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p++
        }

        var sumA = 0L
        var sumB = 0L
        for (i in nums.indices) {
            if (isPrime[i]) {
                sumA += nums[i].toLong()
            } else {
                sumB += nums[i].toLong()
            }
        }
        return kotlin.math.abs(sumA - sumB)
    }
}
```

## Dart

```dart
class Solution {
  int splitArray(List<int> nums) {
    int n = nums.length;
    List<bool> isPrime = List.filled(n, true);
    if (n > 0) isPrime[0] = false;
    if (n > 1) isPrime[1] = false;
    for (int i = 2; i * i < n; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j < n; j += i) {
          isPrime[j] = false;
        }
      }
    }
    int sumA = 0, sumB = 0;
    for (int i = 0; i < n; ++i) {
      if (isPrime[i]) {
        sumA += nums[i];
      } else {
        sumB += nums[i];
      }
    }
    return (sumA - sumB).abs();
  }
}
```

## Golang

```go
func splitArray(nums []int) int64 {
    n := len(nums)
    if n == 0 {
        return 0
    }
    isPrime := make([]bool, n)
    for i := 2; i < n; i++ {
        isPrime[i] = true
    }
    for p := 2; p*p < n; p++ {
        if isPrime[p] {
            for multiple := p * p; multiple < n; multiple += p {
                isPrime[multiple] = false
            }
        }
    }

    var sumA, sumB int64
    for i, v := range nums {
        if isPrime[i] {
            sumA += int64(v)
        } else {
            sumB += int64(v)
        }
    }
    diff := sumA - sumB
    if diff < 0 {
        diff = -diff
    }
    return diff
}
```

## Ruby

```ruby
def split_array(nums)
  n = nums.length
  is_prime = Array.new(n, true)
  if n > 0
    is_prime[0] = false
    is_prime[1] = false if n > 1
  end
  limit = Math.sqrt(n).to_i
  (2..limit).each do |i|
    next unless is_prime[i]
    j = i * i
    while j < n
      is_prime[j] = false
      j += i
    end
  end

  sum_a = 0
  sum_b = 0
  nums.each_with_index do |val, idx|
    if is_prime[idx]
      sum_a += val
    else
      sum_b += val
    end
  end
  (sum_a - sum_b).abs
end
```

## Scala

```scala
object Solution {
  def splitArray(nums: Array[Int]): Long = {
    val n = nums.length
    if (n == 0) return 0L

    // Sieve of Eratosthenes for indices [0, n-1]
    val isPrime = Array.fill[Boolean](n)(true)
    if (n > 0) isPrime(0) = false
    if (n > 1) isPrime(1) = false

    var i = 2
    while (i * i < n) {
      if (isPrime(i)) {
        var j = i * i
        while (j < n) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }

    var sumA: Long = 0L
    var sumB: Long = 0L

    var idx = 0
    while (idx < n) {
      if (isPrime(idx)) sumA += nums(idx).toLong
      else sumB += nums(idx).toLong
      idx += 1
    }

    scala.math.abs(sumA - sumB)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn split_array(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut is_prime = vec![true; n];
        if n > 0 { is_prime[0] = false; }
        if n > 1 { is_prime[1] = false; }

        let limit = (n as f64).sqrt() as usize + 1;
        for p in 2..limit {
            if is_prime[p] {
                let mut multiple = p * p;
                while multiple < n {
                    is_prime[multiple] = false;
                    multiple += p;
                }
            }
        }

        let mut sum_a: i64 = 0;
        let mut sum_b: i64 = 0;
        for (i, &val) in nums.iter().enumerate() {
            if is_prime[i] {
                sum_a += val as i64;
            } else {
                sum_b += val as i64;
            }
        }

        (sum_a - sum_b).abs()
    }
}
```

## Racket

```racket
(define/contract (split-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [primes (make-vector n #t)])
    (when (> n 0) (vector-set! primes 0 #f))
    (when (> n 1) (vector-set! primes 1 #f))
    (let ([limit (if (< n 2) -1 (floor (sqrt (- n 1))))])
      (for ([i (in-range 2 (add1 limit))])
        (when (vector-ref primes i)
          (for ([j (in-range (* i i) n i)])
            (vector-set! primes j #f)))))
    (let loop ((lst nums) (idx 0) (sumA 0) (sumB 0))
      (if (null? lst)
          (abs (- sumA sumB))
          (let ([val (car lst)])
            (if (and (< idx n) (vector-ref primes idx))
                (loop (cdr lst) (add1 idx) (+ sumA val) sumB)
                (loop (cdr lst) (add1 idx) sumA (+ sumB val)))))))
```

## Erlang

```erlang
-spec split_array(Nums :: [integer()]) -> integer().
split_array(Nums) ->
    MaxIdx = length(Nums) - 1,
    PrimeList = prime_sieve(MaxIdx),
    PrimeMap = maps:from_list([{P, true} || P <- PrimeList]),
    split_loop(Nums, 0, 0, 0, PrimeMap).

prime_sieve(N) when N < 2 -> [];
prime_sieve(N) ->
    prime_sieve(lists:seq(2, N), []).

prime_sieve([], Acc) -> lists:reverse(Acc);
prime_sieve([P|Rest], Acc) ->
    Filtered = [X || X <- Rest, X rem P =/= 0],
    prime_sieve(Filtered, [P|Acc]).

split_loop([], _Idx, SumA, SumB, _PrimeMap) ->
    erlang:abs(SumA - SumB);
split_loop([H|T], Idx, SumA, SumB, PrimeMap) ->
    case maps:is_key(Idx, PrimeMap) of
        true -> split_loop(T, Idx + 1, SumA + H, SumB, PrimeMap);
        false -> split_loop(T, Idx + 1, SumA, SumB + H, PrimeMap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec split_array(nums :: [integer]) :: integer
  def split_array(nums) do
    {sum_a, sum_b} =
      Enum.reduce(Enum.with_index(nums), {0, 0}, fn {val, idx}, {a, b} ->
        if prime?(idx) do
          {a + val, b}
        else
          {a, b + val}
        end
      end)

    abs(sum_a - sum_b)
  end

  defp prime?(n) when n < 2, do: false
  defp prime?(2), do: true
  defp prime?(n) when rem(n, 2) == 0, do: false
  defp prime?(n), do: prime_check(n, 3, :math.sqrt(n) |> trunc())

  defp prime_check(_n, i, limit) when i > limit, do: true

  defp prime_check(n, i, limit) do
    if rem(n, i) == 0 do
      false
    else
      prime_check(n, i + 2, limit)
    end
  end
end
```
