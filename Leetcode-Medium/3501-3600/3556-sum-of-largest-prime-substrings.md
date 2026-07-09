# 3556. Sum of Largest Prime Substrings

## Cpp

```cpp
class Solution {
public:
    bool isPrime(long long x) {
        if (x < 2) return false;
        if (x % 2 == 0) return x == 2;
        for (long long d = 3; d * d <= x; d += 2) {
            if (x % d == 0) return false;
        }
        return true;
    }

    long long sumOfLargestPrimes(string s) {
        unordered_set<long long> primes;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            long long val = 0;
            for (int j = i; j < n; ++j) {
                val = val * 10 + (s[j] - '0');
                if (val > 1 && isPrime(val)) {
                    primes.insert(val);
                }
            }
        }
        vector<long long> vec(primes.begin(), primes.end());
        sort(vec.begin(), vec.end(), greater<long long>());
        long long sum = 0;
        for (int i = 0; i < (int)vec.size() && i < 3; ++i) {
            sum += vec[i];
        }
        return sum;
    }
};
```

## Java

```java
class Solution {
    public long sumOfLargestPrimes(String s) {
        int n = s.length();
        java.util.TreeSet<Long> primes = new java.util.TreeSet<>((a, b) -> Long.compare(b, a));
        for (int i = 0; i < n; i++) {
            long val = 0;
            for (int j = i; j < n; j++) {
                val = val * 10 + (s.charAt(j) - '0');
                if (isPrime(val)) {
                    primes.add(val);
                }
            }
        }
        long sum = 0;
        int count = 0;
        for (long p : primes) {
            sum += p;
            if (++count == 3) break;
        }
        return sum;
    }

    private boolean isPrime(long x) {
        if (x < 2) return false;
        if ((x & 1) == 0) return x == 2;
        for (long i = 3; i * i <= x; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            i = 3
            limit = int(n ** 0.5) + 1
            while i <= limit:
                if n % i == 0:
                    return False
                i += 2
            return True

        primes = set()
        n = len(s)
        for i in range(n):
            num = 0
            for j in range(i, n):
                # build number incrementally to avoid repeated int conversion
                num = num * 10 + (ord(s[j]) - ord('0'))
                if is_prime(num):
                    primes.add(num)

        if not primes:
            return 0
        largest_three = sorted(primes, reverse=True)[:3]
        return sum(largest_three)
```

## Python3

```python
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n % 2 == 0:
                return n == 2
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

        primes = set()
        n = len(s)
        for i in range(n):
            num = 0
            for j in range(i, n):
                # build number incrementally to avoid repeated int conversion overhead
                num = num * 10 + (ord(s[j]) - ord('0'))
                if is_prime(num):
                    primes.add(num)

        if not primes:
            return 0
        largest_three = sorted(primes, reverse=True)[:3]
        return sum(largest_three)
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <math.h>

static int cmp_desc(const void *a, const void *b) {
    unsigned long long x = *(const unsigned long long *)a;
    unsigned long long y = *(const unsigned long long *)b;
    if (x < y) return 1;
    if (x > y) return -1;
    return 0;
}

static int isPrime(unsigned long long n) {
    if (n < 2) return 0;
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0) return 0;
    unsigned long long limit = (unsigned long long)sqrt((double)n);
    for (unsigned long long i = 3; i <= limit; i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

long long sumOfLargestPrimes(char* s) {
    int len = strlen(s);
    unsigned long long primes[55]; // maximum possible unique substrings
    int cnt = 0;

    for (int i = 0; i < len; ++i) {
        unsigned long long val = 0;
        for (int j = i; j < len; ++j) {
            val = val * 10 + (unsigned long long)(s[j] - '0');
            if (val >= 2 && isPrime(val)) {
                int exists = 0;
                for (int k = 0; k < cnt; ++k) {
                    if (primes[k] == val) { exists = 1; break; }
                }
                if (!exists) {
                    primes[cnt++] = val;
                }
            }
        }
    }

    if (cnt == 0) return 0;

    qsort(primes, cnt, sizeof(unsigned long long), cmp_desc);

    long long sum = 0;
    int limit = cnt < 3 ? cnt : 3;
    for (int i = 0; i < limit; ++i) {
        sum += (long long)primes[i];
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution
{
    public long SumOfLargestPrimes(string s)
    {
        var primes = new HashSet<long>();
        int n = s.Length;
        for (int i = 0; i < n; i++)
        {
            long val = 0;
            for (int j = i; j < n; j++)
            {
                val = val * 10 + (s[j] - '0');
                if (IsPrime(val))
                    primes.Add(val);
            }
        }

        var list = new List<long>(primes);
        list.Sort((a, b) => b.CompareTo(a)); // descending

        long sum = 0;
        for (int i = 0; i < list.Count && i < 3; i++)
            sum += list[i];

        return sum;
    }

    private bool IsPrime(long n)
    {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        for (long i = 3; i * i <= n; i += 2)
            if (n % i == 0) return false;
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var sumOfLargestPrimes = function(s) {
    const n = s.length;
    const primeSet = new Set();

    const isPrime = (num) => {
        if (num === 2) return true;
        if (num < 2 || num % 2 === 0) return false;
        for (let d = 3; d * d <= num; d += 2) {
            if (num % d === 0) return false;
        }
        return true;
    };

    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j <= n; ++j) {
            const num = Number(s.slice(i, j));
            if (num >= 2 && isPrime(num)) {
                primeSet.add(num);
            }
        }
    }

    const primes = Array.from(primeSet).sort((a, b) => b - a);
    let sum = 0;
    for (let i = 0; i < Math.min(3, primes.length); ++i) {
        sum += primes[i];
    }
    return sum;
};
```

## Typescript

```typescript
function sumOfLargestPrimes(s: string): number {
    const isPrime = (n: number): boolean => {
        if (n < 2) return false;
        if (n === 2) return true;
        if (n % 2 === 0) return false;
        const limit = Math.floor(Math.sqrt(n));
        for (let i = 3; i <= limit; i += 2) {
            if (n % i === 0) return false;
        }
        return true;
    };

    const primes = new Set<number>();
    const n = s.length;

    for (let i = 0; i < n; ++i) {
        let numStr = '';
        for (let j = i; j < n; ++j) {
            numStr += s[j];
            const val = parseInt(numStr, 10);
            if (isPrime(val)) primes.add(val);
        }
    }

    const sortedPrimes = Array.from(primes).sort((a, b) => b - a);
    let sum = 0;
    for (let i = 0; i < Math.min(3, sortedPrimes.length); ++i) {
        sum += sortedPrimes[i];
    }
    return sum;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function sumOfLargestPrimes($s) {
        $len = strlen($s);
        $primeSet = [];
        for ($i = 0; $i < $len; $i++) {
            $numStr = '';
            for ($j = $i; $j < $len; $j++) {
                $numStr .= $s[$j];
                $val = intval($numStr);
                if ($val < 2) continue;
                if (!isset($primeSet[$val]) && $this->isPrime($val)) {
                    $primeSet[$val] = true;
                }
            }
        }
        if (empty($primeSet)) return 0;
        $primes = array_keys($primeSet);
        rsort($primes, SORT_NUMERIC);
        $sum = 0;
        $cnt = min(3, count($primes));
        for ($k = 0; $k < $cnt; $k++) {
            $sum += $primes[$k];
        }
        return $sum;
    }

    private function isPrime(int $num): bool {
        if ($num < 2) return false;
        if ($num == 2) return true;
        if ($num % 2 == 0) return false;
        $limit = (int)sqrt($num);
        for ($i = 3; $i <= $limit; $i += 2) {
            if ($num % $i == 0) return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfLargestPrimes(_ s: String) -> Int {
        let digits = s.compactMap { $0.wholeNumberValue }
        let n = digits.count
        var primeSet = Set<Int>()
        
        func isPrime(_ num: Int) -> Bool {
            if num < 2 { return false }
            if num == 2 || num == 3 { return true }
            if num % 2 == 0 { return false }
            var i = 3
            while i * i <= num {
                if num % i == 0 { return false }
                i += 2
            }
            return true
        }
        
        for i in 0..<n {
            var value = 0
            for j in i..<n {
                value = value * 10 + digits[j]
                if isPrime(value) {
                    primeSet.insert(value)
                }
            }
        }
        
        let sortedPrimes = primeSet.sorted(by: >)
        var sum = 0
        for k in 0..<min(3, sortedPrimes.count) {
            sum += sortedPrimes[k]
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfLargestPrimes(s: String): Long {
        val primes = mutableSetOf<Long>()
        val n = s.length
        for (i in 0 until n) {
            var numStr = ""
            for (j in i until n) {
                numStr += s[j]
                // Convert substring to number, leading zeros are ignored by toLong()
                val value = numStr.toLong()
                if (isPrime(value)) {
                    primes.add(value)
                }
            }
        }
        if (primes.isEmpty()) return 0L
        val sorted = primes.sortedDescending()
        var sum = 0L
        for (k in 0 until minOf(3, sorted.size)) {
            sum += sorted[k]
        }
        return sum
    }

    private fun isPrime(num: Long): Boolean {
        if (num < 2) return false
        if (num == 2L) return true
        if (num % 2L == 0L) return false
        var i = 3L
        val limit = kotlin.math.sqrt(num.toDouble()).toLong()
        while (i <= limit) {
            if (num % i == 0L) return false
            i += 2
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int sumOfLargestPrimes(String s) {
    final Set<int> primes = {};

    bool isPrime(int n) {
      if (n < 2) return false;
      if (n == 2) return true;
      if (n % 2 == 0) return false;
      for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
      }
      return true;
    }

    int n = s.length;
    for (int i = 0; i < n; ++i) {
      int value = 0;
      for (int j = i; j < n; ++j) {
        // Build number incrementally to avoid parsing each time
        value = value * 10 + (s.codeUnitAt(j) - 48);
        if (isPrime(value)) {
          primes.add(value);
        }
      }
    }

    if (primes.isEmpty) return 0;
    List<int> list = primes.toList()
      ..sort((a, b) => b.compareTo(a)); // descending
    int sum = 0;
    for (int i = 0; i < list.length && i < 3; ++i) {
      sum += list[i];
    }
    return sum;
  }
}
```

## Golang

```go
import "sort"

func sumOfLargestPrimes(s string) int64 {
	primes := make(map[int64]struct{})
	n := len(s)
	for i := 0; i < n; i++ {
		var num int64 = 0
		for j := i; j < n; j++ {
			num = num*10 + int64(s[j]-'0')
			if isPrime(num) {
				primes[num] = struct{}{}
			}
		}
	}
	vals := make([]int64, 0, len(primes))
	for v := range primes {
		vals = append(vals, v)
	}
	sort.Slice(vals, func(i, j int) bool { return vals[i] > vals[j] })
	var sum int64
	limit := 3
	if len(vals) < limit {
		limit = len(vals)
	}
	for i := 0; i < limit; i++ {
		sum += vals[i]
	}
	return sum
}

func isPrime(x int64) bool {
	if x < 2 {
		return false
	}
	if x%2 == 0 {
		return x == 2
	}
	for i := int64(3); i*i <= x; i += 2 {
		if x%i == 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
require 'set'

def prime?(num)
  return false if num < 2
  return true if num == 2
  return false if num.even?
  limit = Math.sqrt(num).to_i
  i = 3
  while i <= limit
    return false if num % i == 0
    i += 2
  end
  true
end

def sum_of_largest_primes(s)
  primes = Set.new
  n = s.length
  (0...n).each do |i|
    (i+1..n).each do |j|
      num = s[i...j].to_i
      next if num < 2
      primes.add(num) if prime?(num)
    end
  end
  primes.to_a.sort.reverse.first(3).sum
end
```

## Scala

```scala
object Solution {
    def sumOfLargestPrimes(s: String): Long = {
        val n = s.length
        val primes = scala.collection.mutable.HashSet[Long]()

        def isPrime(x: Long): Boolean = {
            if (x < 2) return false
            if (x % 2 == 0) return x == 2
            var i = 3L
            while (i * i <= x) {
                if (x % i == 0) return false
                i += 2
            }
            true
        }

        for (i <- 0 until n) {
            var num: Long = 0L
            for (j <- i until n) {
                val digit = s.charAt(j) - '0'
                num = num * 10 + digit
                if (isPrime(num)) primes += num
            }
        }

        val sorted = primes.toArray.sorted(Ordering[Long].reverse)
        var sum: Long = 0L
        var cnt = 0
        while (cnt < sorted.length && cnt < 3) {
            sum += sorted(cnt)
            cnt += 1
        }
        sum
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn sum_of_largest_primes(s: String) -> i64 {
        fn is_prime(n: u64) -> bool {
            if n < 2 {
                return false;
            }
            if n == 2 || n == 3 {
                return true;
            }
            if n % 2 == 0 {
                return false;
            }
            let mut i = 3u64;
            while i * i <= n {
                if n % i == 0 {
                    return false;
                }
                i += 2;
            }
            true
        }

        let n = s.len();
        let mut primes: HashSet<u64> = HashSet::new();

        for i in 0..n {
            for j in i + 1..=n {
                if let Ok(num) = s[i..j].parse::<u64>() {
                    if is_prime(num) {
                        primes.insert(num);
                    }
                }
            }
        }

        let mut vals: Vec<u64> = primes.into_iter().collect();
        vals.sort_unstable_by(|a, b| b.cmp(a));
        let sum: u64 = vals.iter().take(3).sum();

        sum as i64
    }
}
```

## Racket

```racket
(require racket/math)

(define (is-prime? n)
  (cond [(< n 2) #false]
        [(= n 2) #true]
        [(even? n) #false]
        [else
         (let loop ([d 3] [limit (integer-sqrt n)])
           (if (> d limit)
               #true
               (if (= (remainder n d) 0)
                   #false
                   (loop (+ d 2) limit))))]))

(define/contract (sum-of-largest-primes s)
  (-> string? exact-integer?)
  (let* ([len (string-length s)]
         [primes (make-hash)])
    (define (add-if-prime num)
      (when (is-prime? num)
        (hash-set! primes num #t)))
    (for ([i (in-range len)])
      (for ([j (in-range (+ i 1) (+ len 1))])
        (let* ([sub (substring s i j)]
               [num (string->number sub)])
          (when (and num (exact-integer? num))
            (add-if-prime num)))))
    (define sorted (sort (hash-keys primes) >))
    (for/sum ([p (in-list (take sorted 3))]) p)))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_largest_primes/1]).

-spec sum_of_largest_primes(S :: unicode:unicode_binary()) -> integer().
sum_of_largest_primes(S) ->
    Chars = binary_to_list(S),
    N = length(Chars),
    PrimeMap = collect_primes(0, N, Chars, #{}),
    Primes = maps:keys(PrimeMap),
    SortedDesc = lists:reverse(lists:sort(Primes)),
    Top3 = take_n(SortedDesc, 3),
    sum_list(Top3).

collect_primes(I, N, _Chars, Acc) when I >= N ->
    Acc;
collect_primes(I, N, Chars, Acc) ->
    Acc1 = collect_from_start(I, N, Chars, 0, Acc),
    collect_primes(I + 1, N, Chars, Acc1).

collect_from_start(Pos, N, _Chars, _Num, Acc) when Pos >= N ->
    Acc;
collect_from_start(Pos, N, Chars, Num, Acc) ->
    Digit = lists:nth(Pos + 1, Chars) - $0,
    NewNum = Num * 10 + Digit,
    Acc1 = case (NewNum > 1) andalso is_prime(NewNum) of
               true -> maps:put(NewNum, true, Acc);
               false -> Acc
           end,
    collect_from_start(Pos + 1, N, Chars, NewNum, Acc1).

-spec is_prime(integer()) -> boolean().
is_prime(N) when N < 2 ->
    false;
is_prime(2) ->
    true;
is_prime(N) when N rem 2 =:= 0 ->
    false;
is_prime(N) ->
    Max = trunc(math:sqrt(N)),
    is_prime_odd(N, 3, Max).

-spec is_prime_odd(integer(), integer(), integer()) -> boolean().
is_prime_odd(_N, I, Max) when I > Max ->
    true;
is_prime_odd(N, I, Max) ->
    case N rem I of
        0 -> false;
        _ -> is_prime_odd(N, I + 2, Max)
    end.

-spec take_n(list(), non_neg_integer()) -> list().
take_n(_List, 0) -> [];
take_n([], _) -> [];
take_n([H|T], K) when K > 0 ->
    [H | take_n(T, K - 1)].

-spec sum_list(list(integer())) -> integer().
sum_list(L) ->
    lists:foldl(fun(X, Acc) -> X + Acc end, 0, L).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_largest_primes(String.t()) :: integer()
  def sum_of_largest_primes(s) do
    len = String.length(s)

    primes =
      0..(len - 1)
      |> Enum.reduce(MapSet.new(), fn i, set ->
        (i + 1)..len
        |> Enum.reduce(set, fn j, acc ->
          substr = String.slice(s, i, j - i)
          num = String.to_integer(substr)

          if is_prime(num) do
            MapSet.put(acc, num)
          else
            acc
          end
        end)
      end)

    primes
    |> Enum.sort(&>=/2)
    |> Enum.take(3)
    |> Enum.sum()
  end

  defp is_prime(n) when n < 2, do: false
  defp is_prime(2), do: true
  defp is_prime(n) when rem(n, 2) == 0, do: false
  defp is_prime(n) do
    limit = :math.sqrt(n) |> trunc()
    check_divisor(3, limit, n)
  end

  defp check_divisor(current, limit, _n) when current > limit, do: true
  defp check_divisor(current, limit, n) do
    if rem(n, current) == 0, do: false, else: check_divisor(current + 2, limit, n)
  end
end
```
