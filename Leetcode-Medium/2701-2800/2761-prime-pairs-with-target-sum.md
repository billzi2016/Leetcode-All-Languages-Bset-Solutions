# 2761. Prime Pairs With Target Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> findPrimePairs(int n) {
        if (n < 4) return {};
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * 1LL * i <= n; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i)
                    isPrime[j] = false;
            }
        }
        vector<vector<int>> res;
        for (int x = 2; x <= n / 2; ++x) {
            int y = n - x;
            if (isPrime[x] && isPrime[y]) {
                res.push_back({x, y});
            }
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> findPrimePairs(int n) {
        if (n < 4) return new ArrayList<>();
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        for (int x = 2; x <= n / 2; x++) {
            int y = n - x;
            if (isPrime[x] && isPrime[y]) {
                List<Integer> pair = new ArrayList<>(2);
                pair.add(x);
                pair.add(y);
                result.add(pair);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findPrimePairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 4:
            return []
        # Sieve of Eratosthenes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        import math
        limit = int(math.isqrt(n))
        for i in range(2, limit + 1):
            if is_prime[i]:
                step = i
                start = i * i
                is_prime[start:n+1:step] = [False] * ((n - start) // step + 1)
        res = []
        half = n // 2
        for x in range(2, half + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                res.append([x, y])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 4:
            return []
        # Sieve of Eratosthenes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if is_prime[i]:
                step = i
                start = i * i
                is_prime[start:n+1:step] = [False] * ((n - start) // step + 1)
        res: List[List[int]] = []
        for x in range(2, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                res.append([x, y])
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findPrimePairs(int n, int* returnSize, int** returnColumnSizes) {
    // Sieve of Eratosthenes
    char *isPrime = (char *)malloc((n + 1) * sizeof(char));
    if (!isPrime) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    for (int i = 0; i <= n; ++i) isPrime[i] = 1;
    if (n >= 0) isPrime[0] = 0;
    if (n >= 1) isPrime[1] = 0;
    for (int i = 2; i * i <= n; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i)
                isPrime[j] = 0;
        }
    }

    // Count valid pairs
    int cnt = 0;
    for (int x = 2; x <= n / 2; ++x) {
        int y = n - x;
        if (isPrime[x] && isPrime[y])
            ++cnt;
    }

    *returnSize = cnt;
    if (cnt == 0) {
        free(isPrime);
        *returnColumnSizes = NULL;
        return NULL;
    }

    // Allocate result structures
    int **result = (int **)malloc(cnt * sizeof(int *));
    int *colSizes = (int *)malloc(cnt * sizeof(int));
    for (int i = 0; i < cnt; ++i) colSizes[i] = 2;

    // Fill pairs
    int idx = 0;
    for (int x = 2; x <= n / 2; ++x) {
        int y = n - x;
        if (isPrime[x] && isPrime[y]) {
            int *pair = (int *)malloc(2 * sizeof(int));
            pair[0] = x;
            pair[1] = y;
            result[idx++] = pair;
        }
    }

    *returnColumnSizes = colSizes;
    free(isPrime);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindPrimePairs(int n) {
        var result = new List<IList<int>>();
        if (n < 4) return result;

        bool[] isPrime = new bool[n + 1];
        for (int i = 2; i <= n; i++) isPrime[i] = true;

        for (int p = 2; p * p <= n; p++) {
            if (!isPrime[p]) continue;
            for (int multiple = p * p; multiple <= n; multiple += p) {
                isPrime[multiple] = false;
            }
        }

        for (int x = 2; x <= n / 2; x++) {
            int y = n - x;
            if (isPrime[x] && isPrime[y]) {
                result.Add(new List<int> { x, y });
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[][]}
 */
var findPrimePairs = function(n) {
    if (n < 4) return [];
    
    const isPrime = new Uint8Array(n + 1);
    for (let i = 2; i <= n; ++i) isPrime[i] = 1;
    const limit = Math.floor(Math.sqrt(n));
    for (let p = 2; p <= limit; ++p) {
        if (!isPrime[p]) continue;
        for (let multiple = p * p; multiple <= n; multiple += p) {
            isPrime[multiple] = 0;
        }
    }
    
    const res = [];
    const half = Math.floor(n / 2);
    for (let x = 2; x <= half; ++x) {
        if (isPrime[x] && isPrime[n - x]) {
            res.push([x, n - x]);
        }
    }
    return res;
};
```

## Typescript

```typescript
function findPrimePairs(n: number): number[][] {
    const isPrime = new Uint8Array(n + 1);
    if (n >= 2) {
        for (let i = 2; i <= n; ++i) isPrime[i] = 1;
        const limit = Math.floor(Math.sqrt(n));
        for (let p = 2; p <= limit; ++p) {
            if (isPrime[p]) {
                for (let multiple = p * p; multiple <= n; multiple += p) {
                    isPrime[multiple] = 0;
                }
            }
        }
    }
    const res: number[][] = [];
    for (let x = 2; x <= Math.floor(n / 2); ++x) {
        if (isPrime[x] && isPrime[n - x]) {
            res.push([x, n - x]);
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[][]
     */
    function findPrimePairs($n) {
        if ($n < 4) return [];

        // Sieve of Eratosthenes up to n
        $isPrime = array_fill(0, $n + 1, true);
        $isPrime[0] = $isPrime[1] = false;
        $limit = (int)sqrt($n);
        for ($i = 2; $i <= $limit; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $n; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }

        $result = [];
        $half = intdiv($n, 2);
        for ($x = 2; $x <= $half; $x++) {
            $y = $n - $x;
            if ($isPrime[$x] && $isPrime[$y]) {
                $result[] = [$x, $y];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findPrimePairs(_ n: Int) -> [[Int]] {
        if n < 4 { return [] }
        var isPrime = [Bool](repeating: true, count: n + 1)
        if n >= 0 { isPrime[0] = false }
        if n >= 1 { isPrime[1] = false }
        let limit = Int(Double(n).squareRoot())
        if limit >= 2 {
            for i in 2...limit where isPrime[i] {
                var j = i * i
                while j <= n {
                    isPrime[j] = false
                    j += i
                }
            }
        }
        var result = [[Int]]()
        let maxX = n / 2
        if maxX >= 2 {
            for x in 2...maxX {
                let y = n - x
                if isPrime[x] && isPrime[y] {
                    result.append([x, y])
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPrimePairs(n: Int): List<List<Int>> {
        if (n < 4) return emptyList()
        val isPrime = BooleanArray(n + 1) { true }
        isPrime[0] = false
        if (n >= 1) isPrime[1] = false
        var p = 2
        while (p * p <= n) {
            if (isPrime[p]) {
                var multiple = p * p
                while (multiple <= n) {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p++
        }
        val result = mutableListOf<List<Int>>()
        var x = 2
        while (x <= n / 2) {
            if (isPrime[x] && isPrime[n - x]) {
                result.add(listOf(x, n - x))
            }
            x++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> findPrimePairs(int n) {
    if (n < 4) return [];
    List<bool> isPrime = List.filled(n + 1, true);
    isPrime[0] = false;
    if (n >= 1) isPrime[1] = false;

    for (int i = 2; i * i <= n; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j <= n; j += i) {
          isPrime[j] = false;
        }
      }
    }

    List<List<int>> result = [];
    for (int x = 2; x <= n ~/ 2; ++x) {
      int y = n - x;
      if (isPrime[x] && isPrime[y]) {
        result.add([x, y]);
      }
    }
    return result;
  }
}
```

## Golang

```go
func findPrimePairs(n int) [][]int {
	if n < 4 {
		return [][]int{}
	}
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
	res := make([][]int, 0)
	for x := 2; x <= n/2; x++ {
		y := n - x
		if isPrime[x] && isPrime[y] {
			res = append(res, []int{x, y})
		}
	}
	return res
}
```

## Ruby

```ruby
def find_prime_pairs(n)
  return [] if n < 4
  is_prime = Array.new(n + 1, true)
  is_prime[0] = is_prime[1] = false
  limit = Math.sqrt(n).to_i
  (2..limit).each do |i|
    next unless is_prime[i]
    j = i * i
    while j <= n
      is_prime[j] = false
      j += i
    end
  end

  result = []
  (2..n / 2).each do |x|
    y = n - x
    result << [x, y] if is_prime[x] && is_prime[y]
  end
  result
end
```

## Scala

```scala
object Solution {
    def findPrimePairs(n: Int): List[List[Int]] = {
        if (n < 4) return Nil

        val isPrime = Array.fill[Boolean](n + 1)(true)
        isPrime(0) = false
        isPrime(1) = false

        var p = 2
        while (p * p <= n) {
            if (isPrime(p)) {
                var multiple = p * p
                while (multiple <= n) {
                    isPrime(multiple) = false
                    multiple += p
                }
            }
            p += 1
        }

        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        var x = 2
        val limit = n / 2
        while (x <= limit) {
            if (isPrime(x) && isPrime(n - x)) {
                result += List(x, n - x)
            }
            x += 1
        }

        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_prime_pairs(n: i32) -> Vec<Vec<i32>> {
        if n < 2 {
            return Vec::new();
        }
        let limit = n as usize;
        // Sieve of Eratosthenes up to n
        let mut is_prime = vec![true; limit + 1];
        if limit >= 0 { is_prime[0] = false; }
        if limit >= 1 { is_prime[1] = false; }

        let sqrt_n = (limit as f64).sqrt() as usize;
        for i in 2..=sqrt_n {
            if is_prime[i] {
                let mut j = i * i;
                while j <= limit {
                    is_prime[j] = false;
                    j += i;
                }
            }
        }

        let mut res: Vec<Vec<i32>> = Vec::new();
        for x in 2..=n / 2 {
            let y = n - x;
            if is_prime[x as usize] && is_prime[y as usize] {
                res.push(vec![x, y]);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (find-prime-pairs n)
  (-> exact-integer? (listof (listof exact-integer?)))
  (let* ([size (+ n 1)]
         [prime (make-vector size #t)])
    (when (> size 0) (vector-set! prime 0 #f))
    (when (> size 1) (vector-set! prime 1 #f))
    (let loop ((i 2))
      (when (<= (* i i) n)
        (when (vector-ref prime i)
          (let inner ((j (* i i)))
            (when (<= j n)
              (vector-set! prime j #f)
              (inner (+ j i)))))
        (loop (+ i 1))))
    (for/list ([x (in-range 2 (add1 (quotient n 2))) ]
               #:when (and (vector-ref prime x)
                           (let ((y (- n x)))
                             (vector-ref prime y))))
      (list x (- n x)))))
```

## Erlang

```erlang
-module(solution).
-export([find_prime_pairs/1]).

-spec find_prime_pairs(N :: integer()) -> [[integer()]].
find_prime_pairs(N) when N >= 1 ->
    IsPrime = sieve(N),
    MaxX = N div 2,
    lists:reverse(find_pairs(N, 2, MaxX, IsPrime, [])).

%% Sieve of Eratosthenes returning an array where Index -> true if prime
sieve(N) ->
    A0 = array:new(N + 1, {default, true}),
    A1 = array:set(0, false, A0),
    A2 = array:set(1, false, A1),
    Max = trunc(math:sqrt(N)),
    sieve_loop(2, Max, N, A2).

sieve_loop(I, Max, _N, Arr) when I > Max ->
    Arr;
sieve_loop(I, Max, N, Arr) ->
    case array:get(I, Arr) of
        true ->
            Arr1 = mark_multiples(I * I, I, N, Arr),
            sieve_loop(I + 1, Max, N, Arr1);
        false ->
            sieve_loop(I + 1, Max, N, Arr)
    end.

mark_multiples(J, Step, N, Arr) when J > N ->
    Arr;
mark_multiples(J, Step, N, Arr) ->
    Arr1 = array:set(J, false, Arr),
    mark_multiples(J + Step, Step, N, Arr1).

%% Collect prime pairs [X, Y] where X+Y = N and X <= Y
find_pairs(_N, X, MaxX, _IsPrime, Acc) when X > MaxX ->
    Acc;
find_pairs(N, X, MaxX, IsPrime, Acc) ->
    Y = N - X,
    case {array:get(X, IsPrime), array:get(Y, IsPrime)} of
        {true, true} ->
            find_pairs(N, X + 1, MaxX, IsPrime, [[X, Y] | Acc]);
        _ ->
            find_pairs(N, X + 1, MaxX, IsPrime, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_prime_pairs(n :: integer) :: [[integer]]
  def find_prime_pairs(n) when n >= 0 do
    primes = sieve(n)
    max_x = div(n, 2)

    result =
      2..max_x
      |> Enum.reduce([], fn x, acc ->
        y = n - x

        if MapSet.member?(primes, x) and MapSet.member?(primes, y) do
          [[x, y] | acc]
        else
          acc
        end
      end)

    Enum.reverse(result)
  end

  defp sieve(limit) when limit >= 0 do
    arr = :array.new(limit + 1, default: true)
    arr = :array.set(0, false, arr)
    arr = :array.set(1, false, arr)

    max = :math.sqrt(limit) |> trunc()

    arr =
      Enum.reduce(2..max, arr, fn i, a ->
        if :array.get(i, a) do
          multiples = :lists.seq(i * i, limit, i)
          Enum.reduce(multiples, a, fn j, acc -> :array.set(j, false, acc) end)
        else
          a
        end
      end)

    2..limit
    |> Enum.filter(fn i -> :array.get(i, arr) end)
    |> MapSet.new()
  end
end
```
