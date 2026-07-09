# 2521. Distinct Prime Factors of Product of Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int distinctPrimeFactors(vector<int>& nums) {
        unordered_set<int> primes;
        for (int x : nums) {
            int n = x;
            for (int p = 2; p * p <= n; ++p) {
                if (n % p == 0) {
                    primes.insert(p);
                    while (n % p == 0) n /= p;
                }
            }
            if (n > 1) primes.insert(n);
        }
        return (int)primes.size();
    }
};
```

## Java

```java
class Solution {
    public int distinctPrimeFactors(int[] nums) {
        java.util.HashSet<Integer> primes = new java.util.HashSet<>();
        for (int num : nums) {
            int n = num;
            for (int p = 2; p * p <= n; ++p) {
                if (n % p == 0) {
                    primes.add(p);
                    while (n % p == 0) {
                        n /= p;
                    }
                }
            }
            if (n > 1) {
                primes.add(n);
            }
        }
        return primes.size();
    }
}
```

## Python

```python
class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # generate primes up to sqrt(1000)
        limit = int(1000 ** 0.5) + 1
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:limit + 1:step] = [False] * (((limit - start) // step) + 1)
        primes = [i for i, is_p in enumerate(sieve) if is_p]

        distinct = set()
        for num in nums:
            n = num
            for p in primes:
                if p * p > n:
                    break
                if n % p == 0:
                    distinct.add(p)
                    while n % p == 0:
                        n //= p
            if n > 1:
                distinct.add(n)

        return len(distinct)
```

## Python3

```python
from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # Sieve to generate primes up to 1000 (max possible value)
        limit = 1000
        is_prime = [True] * (limit + 1)
        primes = []
        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
                if i * i <= limit:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False

        distinct = set()
        for num in nums:
            n = num
            for p in primes:
                if p * p > n:
                    break
                if n % p == 0:
                    distinct.add(p)
                    while n % p == 0:
                        n //= p
            if n > 1:  # remaining prime factor larger than sqrt(original number)
                distinct.add(n)

        return len(distinct)
```

## C

```c
int distinctPrimeFactors(int* nums, int numsSize) {
    // Since nums[i] <= 1000, the largest possible prime factor is 997.
    // Use a fixed-size boolean array to mark seen primes.
    char seen[1001] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        for (int p = 2; p * p <= x; ++p) {
            if (x % p == 0) {
                seen[p] = 1;
                while (x % p == 0) {
                    x /= p;
                }
            }
        }
        if (x > 1) { // remaining prime factor
            seen[x] = 1;
        }
    }
    int count = 0;
    for (int i = 2; i <= 1000; ++i) {
        if (seen[i]) ++count;
    }
    return count;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int DistinctPrimeFactors(int[] nums) {
        HashSet<int> primes = new HashSet<int>();
        foreach (int num in nums) {
            int x = num;
            for (int p = 2; p * p <= x; ++p) {
                if (x % p == 0) {
                    primes.Add(p);
                    while (x % p == 0) {
                        x /= p;
                    }
                }
            }
            if (x > 1) {
                primes.Add(x);
            }
        }
        return primes.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var distinctPrimeFactors = function(nums) {
    const factors = new Set();
    for (let num of nums) {
        let x = num;
        // factor out 2 first for speed
        if (x % 2 === 0) {
            factors.add(2);
            while (x % 2 === 0) x /= 2;
        }
        // odd divisors up to sqrt(x)
        for (let d = 3; d * d <= x; d += 2) {
            if (x % d === 0) {
                factors.add(d);
                while (x % d === 0) x /= d;
            }
        }
        // remaining prime > 1
        if (x > 1) factors.add(x);
    }
    return factors.size;
};
```

## Typescript

```typescript
function distinctPrimeFactors(nums: number[]): number {
    const primeSet = new Set<number>();
    for (let val of nums) {
        let n = val;
        if (n % 2 === 0) {
            primeSet.add(2);
            while (n % 2 === 0) n /= 2;
        }
        for (let p = 3; p * p <= n; p += 2) {
            if (n % p === 0) {
                primeSet.add(p);
                while (n % p === 0) n /= p;
            }
        }
        if (n > 1) primeSet.add(n);
    }
    return primeSet.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function distinctPrimeFactors($nums) {
        $primeSet = [];
        foreach ($nums as $num) {
            $n = $num;
            if ($n % 2 == 0) {
                $primeSet[2] = true;
                while ($n % 2 == 0) {
                    $n /= 2;
                }
            }
            for ($p = 3; $p * $p <= $n; $p += 2) {
                if ($n % $p == 0) {
                    $primeSet[$p] = true;
                    while ($n % $p == 0) {
                        $n /= $p;
                    }
                }
            }
            if ($n > 1) {
                $primeSet[$n] = true;
            }
        }
        return count($primeSet);
    }
}
```

## Swift

```swift
class Solution {
    func distinctPrimeFactors(_ nums: [Int]) -> Int {
        var primes = Set<Int>()
        for num in nums {
            var x = num
            var d = 2
            while d * d <= x {
                if x % d == 0 {
                    primes.insert(d)
                    while x % d == 0 {
                        x /= d
                    }
                }
                d += (d == 2) ? 1 : 2  // after 2, check only odd numbers
            }
            if x > 1 {
                primes.insert(x)
            }
        }
        return primes.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distinctPrimeFactors(nums: IntArray): Int {
        val primes = HashSet<Int>()
        for (num in nums) {
            var x = num
            var d = 2
            while (d * d <= x) {
                if (x % d == 0) {
                    primes.add(d)
                    while (x % d == 0) {
                        x /= d
                    }
                }
                d++
            }
            if (x > 1) {
                primes.add(x)
            }
        }
        return primes.size
    }
}
```

## Dart

```dart
class Solution {
  int distinctPrimeFactors(List<int> nums) {
    final Set<int> primeSet = <int>{};
    for (var num in nums) {
      int n = num;
      for (int p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
          primeSet.add(p);
          while (n % p == 0) {
            n ~/= p;
          }
        }
      }
      if (n > 1) {
        primeSet.add(n);
      }
    }
    return primeSet.length;
  }
}
```

## Golang

```go
func distinctPrimeFactors(nums []int) int {
	primeSet := make(map[int]struct{})
	for _, num := range nums {
		n := num
		for d := 2; d*d <= n; d++ {
			if n%d == 0 {
				primeSet[d] = struct{}{}
				for n%d == 0 {
					n /= d
				}
			}
		}
		if n > 1 {
			primeSet[n] = struct{}{}
		}
	}
	return len(primeSet)
}
```

## Ruby

```ruby
require 'set'

def distinct_prime_factors(nums)
  factors = Set.new
  nums.each do |num|
    n = num
    i = 2
    while i * i <= n
      if n % i == 0
        factors.add(i)
        n /= i while n % i == 0
      end
      i += (i == 2 ? 1 : 2) # after checking 2, skip even numbers
    end
    factors.add(n) if n > 1
  end
  factors.size
end
```

## Scala

```scala
object Solution {
    def distinctPrimeFactors(nums: Array[Int]): Int = {
        val primes = scala.collection.mutable.HashSet[Int]()
        for (num <- nums) {
            var x = num
            var d = 2
            while (d * d <= x) {
                if (x % d == 0) {
                    primes += d
                    while (x % d == 0) x /= d
                }
                d += (if (d == 2) 1 else 2)
            }
            if (x > 1) primes += x
        }
        primes.size
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn distinct_prime_factors(nums: Vec<i32>) -> i32 {
        let mut factors: HashSet<i32> = HashSet::new();
        for &num in nums.iter() {
            let mut x = num;
            let mut p = 2;
            while p * p <= x {
                if x % p == 0 {
                    factors.insert(p);
                    while x % p == 0 {
                        x /= p;
                    }
                }
                p += 1;
            }
            if x > 1 {
                factors.insert(x);
            }
        }
        factors.len() as i32
    }
}
```

## Racket

```racket
(define/contract (distinct-prime-factors nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((seen (make-hash)))
    (for ([x nums])
      (let loop ((n x) (p 2))
        (cond
          [(> (* p p) n)
           (when (> n 1)
             (hash-set! seen n #t))]
          [(zero? (remainder n p))
           (hash-set! seen p #t)
           (loop (/ n p) p)]
          [else
           (loop n (+ p 1))])))
    (hash-count seen)))
```

## Erlang

```erlang
-module(solution).
-export([distinct_prime_factors/1]).

-spec distinct_prime_factors(Nums :: [integer()]) -> integer().
distinct_prime_factors(Nums) ->
    FinalMap = lists:foldl(fun(N, Acc) -> factor_number(N, Acc) end,
                           #{},
                           Nums),
    maps:size(FinalMap).

factor_number(N, Acc) when N > 1 ->
    factor_loop(N, 2, Acc);
factor_number(_, Acc) ->
    Acc.

factor_loop(1, _, Acc) ->
    Acc;
factor_loop(N, P, Acc) when P * P =< N ->
    case N rem P of
        0 ->
            NewAcc = maps:put(P, true, Acc),
            factor_loop(N div P, P, NewAcc);
        _ ->
            factor_loop(N, P + 1, Acc)
    end;
factor_loop(N, _, Acc) ->
    maps:put(N, true, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec distinct_prime_factors(nums :: [integer]) :: integer
  def distinct_prime_factors(nums) do
    nums
    |> Enum.reduce(MapSet.new(), fn n, set -> factorize(n, set) end)
    |> MapSet.size()
  end

  defp factorize(num, set) when num > 1 do
    {set2, remaining} = factorize_helper(num, 2, set)

    if remaining > 1 do
      MapSet.put(set2, remaining)
    else
      set2
    end
  end

  defp factorize(_num, set), do: set

  defp factorize_helper(num, p, set) when p * p > num do
    {set, num}
  end

  defp factorize_helper(num, p, set) do
    if rem(num, p) == 0 do
      new_set = MapSet.put(set, p)
      new_num = divide_out(num, p)
      factorize_helper(new_num, p + 1, new_set)
    else
      factorize_helper(num, p + 1, set)
    end
  end

  defp divide_out(num, p) do
    if rem(num, p) == 0 do
      divide_out(div(num, p), p)
    else
      num
    end
  end
end
```
