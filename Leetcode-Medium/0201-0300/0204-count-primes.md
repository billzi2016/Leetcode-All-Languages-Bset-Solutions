# 0204. Count Primes

## Cpp

```cpp
class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) return 0;
        std::vector<bool> isPrime(n, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * 1LL * i < n; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        int count = 0;
        for (int i = 2; i < n; ++i) {
            if (isPrime[i]) ++count;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0;
        boolean[] isComposite = new boolean[n];
        for (int i = 2; i * i < n; i++) {
            if (!isComposite[i]) {
                for (int j = i * i; j < n; j += i) {
                    isComposite[j] = true;
                }
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (!isComposite[i]) count++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        is_prime = bytearray(b'\x01') * n
        is_prime[0] = is_prime[1] = 0
        import math
        limit = int(math.isqrt(n - 1))
        for i in range(2, limit + 1):
            if is_prime[i]:
                start = i * i
                step = i
                is_prime[start:n:step] = b'\x00' * ((n - start - 1) // step + 1)
        return sum(is_prime)
```

## Python3

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_prime = bytearray(b'\x01') * n
        is_prime[0:2] = b'\x00\x00'
        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if is_prime[i]:
                start = i * i
                step = i
                is_prime[start:n:step] = b'\x00' * ((n - start - 1) // step + 1)
        return sum(is_prime)
```

## C

```c
#include <stdlib.h>
#include <string.h>

int countPrimes(int n) {
    if (n <= 2) return 0;
    char *isPrime = (char *)malloc(n);
    if (!isPrime) return 0; // allocation failure fallback
    memset(isPrime, 1, n);
    isPrime[0] = isPrime[1] = 0;

    for (int i = 2; i * (long long)i < n; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    int count = 0;
    for (int i = 2; i < n; ++i) {
        if (isPrime[i]) ++count;
    }

    free(isPrime);
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPrimes(int n) {
        if (n <= 2) return 0;
        bool[] isPrime = new bool[n];
        for (int i = 2; i < n; i++) isPrime[i] = true;

        int limit = (int)Math.Sqrt(n - 1);
        for (int i = 2; i <= limit; i++) {
            if (!isPrime[i]) continue;
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }

        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n <= 2) return 0;
    const isPrime = new Uint8Array(n);
    isPrime.fill(1, 2); // set indices >=2 to true
    for (let i = 2; i * i < n; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = 0;
            }
        }
    }
    let count = 0;
    for (let i = 2; i < n; ++i) {
        count += isPrime[i];
    }
    return count;
};
```

## Typescript

```typescript
function countPrimes(n: number): number {
    if (n <= 2) return 0;
    const isPrime = new Uint8Array(n);
    for (let i = 2; i < n; ++i) isPrime[i] = 1;
    const limit = Math.floor(Math.sqrt(n));
    for (let i = 2; i <= limit; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = 0;
            }
        }
    }
    let count = 0;
    for (let i = 2; i < n; ++i) {
        if (isPrime[i]) ++count;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countPrimes($n) {
        if ($n <= 2) return 0;
        $isPrime = array_fill(0, $n, true);
        $isPrime[0] = $isPrime[1] = false;
        $limit = (int)sqrt($n - 1);
        for ($i = 2; $i <= $limit; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j < $n; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }
        $count = 0;
        for ($i = 2; $i < $n; $i++) {
            if ($isPrime[$i]) $count++;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countPrimes(_ n: Int) -> Int {
        if n <= 2 { return 0 }
        var isPrime = [Bool](repeating: true, count: n)
        isPrime[0] = false
        isPrime[1] = false
        let limit = Int(Double(n).squareRoot())
        if limit >= 2 {
            for i in 2...limit {
                if isPrime[i] {
                    var j = i * i
                    while j < n {
                        isPrime[j] = false
                        j += i
                    }
                }
            }
        }
        var count = 0
        for i in 2..<n where isPrime[i] {
            count += 1
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPrimes(n: Int): Int {
        if (n <= 2) return 0
        val isPrime = BooleanArray(n) { true }
        isPrime[0] = false
        isPrime[1] = false
        var i = 2
        while (i * i < n) {
            if (isPrime[i]) {
                var j = i * i
                while (j < n) {
                    isPrime[j] = false
                    j += i
                }
            }
            i++
        }
        var count = 0
        for (k in 2 until n) {
            if (isPrime[k]) count++
        }
        return count
    }
}
```

## Dart

```dart
import 'dart:typed_data';

class Solution {
  int countPrimes(int n) {
    if (n <= 2) return 0;
    Uint8List isPrime = Uint8List(n);
    isPrime.fillRange(0, n, 1);
    isPrime[0] = 0;
    isPrime[1] = 0;
    for (int i = 2; i * i < n; ++i) {
      if (isPrime[i] == 1) {
        for (int j = i * i; j < n; j += i) {
          isPrime[j] = 0;
        }
      }
    }
    int count = 0;
    for (int i = 2; i < n; ++i) {
      if (isPrime[i] == 1) count++;
    }
    return count;
  }
}
```

## Golang

```go
func countPrimes(n int) int {
	if n <= 2 {
		return 0
	}
	isComposite := make([]bool, n)
	for i := 2; i*i < n; i++ {
		if !isComposite[i] {
			for j := i * i; j < n; j += i {
				isComposite[j] = true
			}
		}
	}
	count := 0
	for i := 2; i < n; i++ {
		if !isComposite[i] {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_primes(n)
  return 0 if n <= 2
  is_prime = Array.new(n, true)
  is_prime[0] = false
  is_prime[1] = false
  limit = Math.sqrt(n).to_i
  i = 2
  while i <= limit
    if is_prime[i]
      j = i * i
      step = i
      while j < n
        is_prime[j] = false
        j += step
      end
    end
    i += 1
  end
  count = 0
  is_prime.each { |v| count += 1 if v }
  count
end
```

## Scala

```scala
object Solution {
    def countPrimes(n: Int): Int = {
        if (n <= 2) return 0
        val isComposite = new Array[Boolean](n)
        var i = 2
        val limit = math.sqrt(n).toInt
        while (i <= limit) {
            if (!isComposite(i)) {
                var j = i * i
                while (j < n) {
                    isComposite(j) = true
                    j += i
                }
            }
            i += 1
        }
        var count = 0
        var k = 2
        while (k < n) {
            if (!isComposite(k)) count += 1
            k += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        let limit = n as usize;
        if limit < 2 {
            return 0;
        }
        let mut is_prime = vec![true; limit];
        is_prime[0] = false;
        is_prime[1] = false;
        let sqrt_limit = (limit as f64).sqrt() as usize + 1;
        for p in 2..sqrt_limit {
            if is_prime[p] {
                let mut multiple = p * p;
                while multiple < limit {
                    is_prime[multiple] = false;
                    multiple += p;
                }
            }
        }
        is_prime.iter().filter(|&&b| b).count() as i32
    }
}
```

## Racket

```racket
(define/contract (count-primes n)
  (-> exact-integer? exact-integer?)
  (if (< n 3)
      0
      (let* ([vec (make-vector n #t)]
             [limit (inexact->exact (floor (sqrt (- n 1))))])
        (vector-set! vec 0 #f)
        (vector-set! vec 1 #f)
        (for ([i (in-range 2 (add1 limit))])
          (when (vector-ref vec i)
            (let loop ((j (* i i)))
              (when (< j n)
                (vector-set! vec j #f)
                (loop (+ j i))))))
        (for/sum ([i (in-range 2 n)])
          (if (vector-ref vec i) 1 0))))))
```

## Erlang

```erlang
-module(solution).
-export([count_primes/1]).

-spec count_primes(N :: integer()) -> integer().
count_primes(N) when N =< 2 ->
    0;
count_primes(N) ->
    MaxIdx = N - 1,
    Arr0 = array:new(N, [{default,true}]),
    Arr1 = array:set(0, false, Arr0),
    Arr2 = array:set(1, false, Arr1),
    Limit = trunc(math:sqrt(MaxIdx)),
    SieveArr = sieve(2, Limit, MaxIdx, Arr2),
    array:foldl(fun(_Idx, Val, Acc) ->
        if Val -> Acc + 1; true -> Acc end
    end, 0, SieveArr).

sieve(I, Limit, MaxIdx, Arr) when I =< Limit ->
    case array:get(I, Arr) of
        true ->
            Arr1 = mark_multiples(I, I * I, MaxIdx, Arr),
            sieve(I + 1, Limit, MaxIdx, Arr1);
        false ->
            sieve(I + 1, Limit, MaxIdx, Arr)
    end;
sieve(_, _, _, Arr) -> Arr.

mark_multiples(_I, Start, MaxIdx, Arr) when Start > MaxIdx ->
    Arr;
mark_multiples(I, Start, MaxIdx, Arr) ->
    Arr1 = array:set(Start, false, Arr),
    mark_multiples(I, Start + I, MaxIdx, Arr1).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_primes(n :: integer) :: integer
  def count_primes(n) when n <= 2, do: 0

  def count_primes(n) do
    limit = :math.sqrt(n - 1) |> trunc()
    # initialize array with true values
    arr = :array.new(n, default: true)
    arr = :array.set(0, false, arr)
    arr = :array.set(1, false, arr)

    arr = sieve(arr, 2, limit, n)

    Enum.reduce(2..(n - 1), 0, fn i, acc ->
      if :array.get(i, arr), do: acc + 1, else: acc
    end)
  end

  defp sieve(arr, i, limit, n) when i > limit, do: arr

  defp sieve(arr, i, limit, n) do
    if :array.get(i, arr) do
      start = i * i
      arr = mark_multiples(arr, start, i, n)
      sieve(arr, i + 1, limit, n)
    else
      sieve(arr, i + 1, limit, n)
    end
  end

  defp mark_multiples(arr, j, step, n) when j >= n, do: arr

  defp mark_multiples(arr, j, step, n) do
    arr = :array.set(j, false, arr)
    mark_multiples(arr, j + step, step, n)
  end
end
```
