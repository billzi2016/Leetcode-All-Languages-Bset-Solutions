# 2507. Smallest Value After Replacing With Sum of Prime Factors

## Cpp

```cpp
class Solution {
public:
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * 1LL * i <= x; ++i) {
            if (x % i == 0) return false;
        }
        return true;
    }

    int sumPrimeFactors(int x) {
        int sum = 0;
        for (int i = 2; i * 1LL * i <= x; ++i) {
            while (x % i == 0) {
                sum += i;
                x /= i;
            }
        }
        if (x > 1) sum += x; // remaining prime factor
        return sum;
    }

    int smallestValue(int n) {
        while (!isPrime(n)) {
            int s = sumPrimeFactors(n);
            if (s == n) break; // reached a fixed point like 4
            n = s;
        }
        return n;
    }
};
```

## Java

```java
class Solution {
    public int smallestValue(int n) {
        int max = n;
        int[] spf = new int[max + 1];
        for (int i = 2; i <= max; i++) {
            if (spf[i] == 0) { // i is prime
                spf[i] = i;
                if ((long) i * i <= max) {
                    for (int j = i * i; j <= max; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        int cur = n;
        while (true) {
            int sum = 0;
            int temp = cur;
            while (temp > 1) {
                int p = spf[temp];
                if (p == 0) p = temp; // should not happen, but safety
                sum += p;
                temp /= p;
            }
            if (sum == cur) break;
            cur = sum;
        }
        return cur;
    }
}
```

## Python

```python
class Solution(object):
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """
        LIMIT = 100000
        # build smallest prime factor (SPF) sieve
        spf = list(range(LIMIT + 1))
        for i in range(2, int(LIMIT ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, LIMIT + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        def sum_prime_factors(x):
            total = 0
            while x > 1:
                p = spf[x]
                total += p
                x //= p
            return total

        # iterate until n becomes prime (spf[n] == n)
        while spf[n] != n:
            n = sum_prime_factors(n)
        return n
```

## Python3

```python
class Solution:
    def smallestValue(self, n: int) -> int:
        limit = 100000
        spf = [0] * (limit + 1)
        for i in range(2, limit + 1):
            if spf[i] == 0:
                spf[i] = i
                if i * i <= limit:
                    step = i
                    start = i * i
                    for j in range(start, limit + 1, step):
                        if spf[j] == 0:
                            spf[j] = i

        def sum_prime_factors(x: int) -> int:
            s = 0
            while x > 1:
                p = spf[x]
                s += p
                x //= p
            return s

        cur = n
        while True:
            nxt = sum_prime_factors(cur)
            if nxt == cur:
                break
            cur = nxt
        return cur
```

## C

```c
int sumPrimeFactors(int x) {
    int sum = 0;
    for (int i = 2; i * i <= x; ++i) {
        while (x % i == 0) {
            sum += i;
            x /= i;
        }
    }
    if (x > 1) sum += x;
    return sum;
}

int smallestValue(int n) {
    int cur = n;
    while (1) {
        int nxt = sumPrimeFactors(cur);
        if (nxt == cur) break;
        cur = nxt;
    }
    return cur;
}
```

## Csharp

```csharp
public class Solution
{
    private const int LIMIT = 100000;
    private readonly int[] spf;

    public Solution()
    {
        spf = new int[LIMIT + 1];
        for (int i = 0; i <= LIMIT; i++) spf[i] = i;
        for (int i = 2; i * i <= LIMIT; i++)
        {
            if (spf[i] == i)
            {
                for (int j = i * i; j <= LIMIT; j += i)
                {
                    if (spf[j] == j) spf[j] = i;
                }
            }
        }
    }

    private int SumPrimeFactors(int x)
    {
        int sum = 0;
        while (x > 1)
        {
            int p = spf[x];
            sum += p;
            x /= p;
        }
        return sum;
    }

    public int SmallestValue(int n)
    {
        while (true)
        {
            int s = SumPrimeFactors(n);
            if (s == n) break; // reached fixed point (prime or 4)
            n = s;
        }
        return n;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var smallestValue = function(n) {
    const sumPrimeFactors = (x) => {
        let sum = 0;
        let num = x;
        for (let p = 2; p * p <= num; ++p) {
            while (num % p === 0) {
                sum += p;
                num /= p;
            }
        }
        if (num > 1) sum += num;
        return sum;
    };
    
    let cur = n;
    while (true) {
        const nxt = sumPrimeFactors(cur);
        if (nxt === cur) break;
        cur = nxt;
    }
    return cur;
};
```

## Typescript

```typescript
function smallestValue(n: number): number {
    const MAX = 100000;
    const spf = new Uint32Array(MAX + 1);
    for (let i = 2; i <= MAX; i++) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= MAX) {
                for (let j = i * i; j <= MAX; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    const primeFactorSum = (x: number): number => {
        let sum = 0;
        while (x > 1) {
            const p = spf[x];
            sum += p;
            x = Math.floor(x / p);
        }
        return sum;
    };

    let cur = n;
    while (true) {
        const nxt = primeFactorSum(cur);
        if (nxt === cur) break;
        cur = nxt;
    }
    return cur;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestValue($n) {
        while (true) {
            $sum = $this->primeFactorSum($n);
            if ($sum == $n) {
                break;
            }
            $n = $sum;
        }
        return $n;
    }

    private function primeFactorSum($x) {
        $sum = 0;
        for ($p = 2; $p * $p <= $x; $p++) {
            while ($x % $p == 0) {
                $sum += $p;
                $x /= $p;
            }
        }
        if ($x > 1) {
            $sum += $x;
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func smallestValue(_ n: Int) -> Int {
        var current = n
        while true {
            let next = sumPrimeFactors(current)
            if next == current { break }
            current = next
        }
        return current
    }
    
    private func sumPrimeFactors(_ x: Int) -> Int {
        var num = x
        var sum = 0
        var p = 2
        while p * p <= num {
            while num % p == 0 {
                sum += p
                num /= p
            }
            p += (p == 2 ? 1 : 2) // after 2, check only odd numbers
        }
        if num > 1 {
            sum += num
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    private fun buildSpf(limit: Int): IntArray {
        val spf = IntArray(limit + 1) { it }
        var i = 2
        while (i * i <= limit) {
            if (spf[i] == i) {
                var j = i * i
                while (j <= limit) {
                    if (spf[j] == j) spf[j] = i
                    j += i
                }
            }
            i++
        }
        return spf
    }

    private fun sumPrimeFactors(x: Int, spf: IntArray): Int {
        var num = x
        var sum = 0
        while (num > 1) {
            val p = spf[num]
            sum += p
            num /= p
        }
        return sum
    }

    fun smallestValue(n: Int): Int {
        val spf = buildSpf(n)
        var cur = n
        while (true) {
            val s = sumPrimeFactors(cur, spf)
            if (s == cur) break
            cur = s
        }
        return cur
    }
}
```

## Dart

```dart
class Solution {
  int smallestValue(int n) {
    int max = n;
    List<int> spf = List.filled(max + 1, 0);
    for (int i = 2; i <= max; ++i) {
      if (spf[i] == 0) {
        spf[i] = i;
        if (i * i <= max) {
          for (int j = i * i; j <= max; j += i) {
            if (spf[j] == 0) spf[j] = i;
          }
        }
      }
    }

    int cur = n;
    while (true) {
      int sum = 0;
      int temp = cur;
      while (temp > 1) {
        int p = spf[temp];
        sum += p;
        temp ~/= p;
      }
      if (sum == cur) break;
      cur = sum;
    }
    return cur;
  }
}
```

## Golang

```go
func smallestValue(n int) int {
	const limit = 100000
	spf := make([]int, limit+1)
	for i := 2; i <= limit; i++ {
		if spf[i] == 0 {
			spf[i] = i
			if i*i <= limit {
				for j := i * i; j <= limit; j += i {
					if spf[j] == 0 {
						spf[j] = i
					}
				}
			}
		}
	}

	for {
		if n > 1 && spf[n] == n { // prime
			return n
		}
		sum := 0
		x := n
		for x > 1 {
			p := spf[x]
			sum += p
			x /= p
		}
		if sum == n {
			return n
		}
		n = sum
	}
}
```

## Ruby

```ruby
def prime?(x)
  return false if x < 2
  return true if x == 2 || x == 3
  return false if x.even?
  i = 3
  while i * i <= x
    return false if x % i == 0
    i += 2
  end
  true
end

def sum_prime_factors(x)
  sum = 0
  while (x & 1) == 0
    sum += 2
    x >>= 1
  end
  f = 3
  while f * f <= x
    while x % f == 0
      sum += f
      x /= f
    end
    f += 2
  end
  sum + (x > 1 ? x : 0)
end

def smallest_value(n)
  loop do
    break if prime?(n) || n == 4
    s = sum_prime_factors(n)
    break if s == n
    n = s
  end
  n
end
```

## Scala

```scala
object Solution {
  def smallestValue(n: Int): Int = {
    var cur = n
    while (true) {
      val sum = sumPrimeFactors(cur)
      if (sum == cur) return cur
      cur = sum
    }
    cur
  }

  private def sumPrimeFactors(num: Int): Int = {
    var x = num
    var sum = 0
    var i = 2
    while (i * i <= x) {
      while (x % i == 0) {
        sum += i
        x /= i
      }
      i += 1
    }
    if (x > 1) sum += x
    sum
  }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_value(mut n: i32) -> i32 {
        fn is_prime(x: i32) -> bool {
            if x < 2 {
                return false;
            }
            if x % 2 == 0 {
                return x == 2;
            }
            let mut d = 3;
            while d * d <= x {
                if x % d == 0 {
                    return false;
                }
                d += 2;
            }
            true
        }

        fn sum_prime_factors(mut x: i32) -> i32 {
            let mut sum = 0;
            let mut d = 2;
            while d * d <= x {
                while x % d == 0 {
                    sum += d;
                    x /= d;
                }
                d = if d == 2 { 3 } else { d + 2 };
            }
            if x > 1 {
                sum += x;
            }
            sum
        }

        while !is_prime(n) && n != 4 {
            n = sum_prime_factors(n);
        }
        n
    }
}
```

## Racket

```racket
(define (prime? k)
  (cond [(<= k 1) #false]
        [(= k 2) #true]
        [(even? k) #false]
        [else
         (let loop ((i 3))
           (if (> (* i i) k)
               #true
               (if (= (remainder k i) 0)
                   #false
                   (loop (+ i 2)))))]))

(define (sum-prime-factors n)
  (let loop ((num n) (i 2) (s 0))
    (cond [(> (* i i) num)
           (if (> num 1) (+ s num) s)]
          [(zero? (remainder num i))
           (loop (/ num i) i (+ s i))]
          [else
           (loop num (+ i 1) s)])))

(define/contract (smallest-value n)
  (-> exact-integer? exact-integer?)
  (let loop ((x n))
    (if (prime? x)
        x
        (loop (sum-prime-factors x)))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_value/1]).

-spec smallest_value(N :: integer()) -> integer().
smallest_value(N) ->
    loop(N).

loop(N) ->
    case is_prime(N) of
        true -> N;
        false ->
            Next = sum_factors(N),
            if Next == N -> N;
               true -> loop(Next)
            end
    end.

-spec is_prime(integer()) -> boolean().
is_prime(N) when N < 2 -> false;
is_prime(2) -> true;
is_prime(N) when N rem 2 =:= 0 -> false;
is_prime(N) ->
    is_prime(N, 3).

-spec is_prime(integer(), integer()) -> boolean().
is_prime(N, I) when I * I > N -> true;
is_prime(N, I) ->
    case N rem I of
        0 -> false;
        _ -> is_prime(N, I + 2)
    end.

-spec sum_factors(integer()) -> integer().
sum_factors(N) -> sum_factors(N, 2, 0).

-spec sum_factors(integer(), integer(), integer()) -> integer().
sum_factors(1, _I, Acc) -> Acc;
sum_factors(N, I, Acc) when I * I =< N ->
    case N rem I of
        0 -> sum_factors(N div I, I, Acc + I);
        _ ->
            NextI = if I == 2 -> 3; true -> I + 2 end,
            sum_factors(N, NextI, Acc)
    end;
sum_factors(N, _I, Acc) ->
    Acc + N.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_value(n :: integer) :: integer
  def smallest_value(n) do
    iterate(n)
  end

  defp iterate(current) do
    sum = sum_prime_factors(current)

    if sum == current do
      current
    else
      iterate(sum)
    end
  end

  defp sum_prime_factors(num) do
    factor_sum(num, 2, 0)
  end

  defp factor_sum(1, _i, acc), do: acc

  defp factor_sum(n, i, acc) when i * i > n do
    acc + n
  end

  defp factor_sum(n, i, acc) do
    if rem(n, i) == 0 do
      factor_sum(div(n, i), i, acc + i)
    else
      factor_sum(n, i + 1, acc)
    end
  end
end
```
