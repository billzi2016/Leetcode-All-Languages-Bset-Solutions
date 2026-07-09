# 0313. Super Ugly Number

## Cpp

```cpp
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        if (n == 1) return 1;
        int k = primes.size();
        vector<int> idx(k, 0);
        vector<long long> nextMul(k);
        for (int i = 0; i < k; ++i) nextMul[i] = primes[i];
        vector<int> ugly(n);
        ugly[0] = 1;
        for (int i = 1; i < n; ++i) {
            long long nextVal = *min_element(nextMul.begin(), nextMul.end());
            ugly[i] = static_cast<int>(nextVal);
            for (int j = 0; j < k; ++j) {
                if (nextMul[j] == nextVal) {
                    idx[j]++;
                    nextMul[j] = (long long)primes[j] * ugly[idx[j]];
                }
            }
        }
        return ugly[n - 1];
    }
};
```

## Java

```java
class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        if (n == 1) return 1;
        int k = primes.length;
        int[] ugly = new int[n];
        ugly[0] = 1;
        int[] idx = new int[k];
        long[] next = new long[k];
        for (int i = 0; i < k; i++) {
            next[i] = primes[i];
        }
        for (int i = 1; i < n; i++) {
            long minVal = Long.MAX_VALUE;
            for (long val : next) {
                if (val < minVal) minVal = val;
            }
            ugly[i] = (int) minVal;
            for (int j = 0; j < k; j++) {
                if (next[j] == minVal) {
                    idx[j]++;
                    next[j] = (long) primes[j] * ugly[idx[j]];
                }
            }
        }
        return ugly[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k
        next_mul = list(primes)  # primes[i] * ugly[idx[i]]

        for i in range(1, n):
            nxt = min(next_mul)
            ugly[i] = nxt
            for j in range(k):
                if next_mul[j] == nxt:
                    idx[j] += 1
                    next_mul[j] = primes[j] * ugly[idx[j]]
        return ugly[-1]
```

## Python3

```python
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k
        next_mul = primes[:]  # initial multiples with ugly[0]=1

        for i in range(1, n):
            next_ugly = min(next_mul)
            ugly[i] = next_ugly
            for j in range(k):
                if next_mul[j] == next_ugly:
                    idx[j] += 1
                    next_mul[j] = primes[j] * ugly[idx[j]]
        return ugly[-1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int nthSuperUglyNumber(int n, int* primes, int primesSize) {
    if (n == 1) return 1;
    
    int *ugly = (int *)malloc(n * sizeof(int));
    ugly[0] = 1;
    
    int *idx = (int *)calloc(primesSize, sizeof(int));
    unsigned long long *cand = (unsigned long long *)malloc(primesSize * sizeof(unsigned long long));
    
    for (int i = 0; i < primesSize; ++i) {
        cand[i] = (unsigned long long)primes[i];
    }
    
    for (int i = 1; i < n; ++i) {
        unsigned long long minVal = ULLONG_MAX;
        for (int j = 0; j < primesSize; ++j) {
            if (cand[j] < minVal) minVal = cand[j];
        }
        ugly[i] = (int)minVal;
        for (int j = 0; j < primesSize; ++j) {
            if (cand[j] == minVal) {
                idx[j]++;
                cand[j] = (unsigned long long)primes[j] * (unsigned long long)ugly[idx[j]];
            }
        }
    }
    
    int result = ugly[n - 1];
    free(ugly);
    free(idx);
    free(cand);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int NthSuperUglyNumber(int n, int[] primes)
    {
        if (n == 1) return 1;
        int k = primes.Length;
        int[] ugly = new int[n];
        ugly[0] = 1;

        int[] idx = new int[k];
        long[] nextMul = new long[k];
        for (int i = 0; i < k; i++)
            nextMul[i] = primes[i];

        for (int i = 1; i < n; i++)
        {
            long nextUgly = nextMul[0];
            for (int j = 1; j < k; j++)
                if (nextMul[j] < nextUgly) nextUgly = nextMul[j];

            ugly[i] = (int)nextUgly;

            for (int j = 0; j < k; j++)
            {
                if (nextMul[j] == nextUgly)
                {
                    idx[j]++;
                    nextMul[j] = (long)primes[j] * ugly[idx[j]];
                }
            }
        }

        return ugly[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
    const ugly = new Array(n);
    ugly[0] = 1;
    const k = primes.length;
    const idx = new Array(k).fill(0);
    const nextMul = primes.slice(); // primes[i] * ugly[0]

    for (let i = 1; i < n; i++) {
        let minVal = Number.MAX_SAFE_INTEGER;
        for (let j = 0; j < k; j++) {
            if (nextMul[j] < minVal) minVal = nextMul[j];
        }
        ugly[i] = minVal;
        for (let j = 0; j < k; j++) {
            if (nextMul[j] === minVal) {
                idx[j]++;
                nextMul[j] = primes[j] * ugly[idx[j]];
            }
        }
    }

    return ugly[n - 1];
};
```

## Typescript

```typescript
function nthSuperUglyNumber(n: number, primes: number[]): number {
    if (n === 1) return 1;
    const k = primes.length;
    const ugly: number[] = new Array(n);
    ugly[0] = 1;

    const idx: number[] = new Array(k).fill(0);
    const nextMul: number[] = primes.slice(); // primes[i] * ugly[0]

    for (let i = 1; i < n; i++) {
        let nextUgly = nextMul[0];
        for (let j = 1; j < k; j++) {
            if (nextMul[j] < nextUgly) nextUgly = nextMul[j];
        }
        ugly[i] = nextUgly;

        for (let j = 0; j < k; j++) {
            if (nextMul[j] === nextUgly) {
                idx[j]++;
                nextMul[j] = primes[j] * ugly[idx[j]];
            }
        }
    }

    return ugly[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $primes
     * @return Integer
     */
    function nthSuperUglyNumber($n, $primes) {
        $k = count($primes);
        $ugly = array_fill(0, $n, 0);
        $ugly[0] = 1;
        $indices = array_fill(0, $k, 0);
        $candidates = $primes; // each prime * ugly[0] (which is 1)

        for ($i = 1; $i < $n; $i++) {
            $next = PHP_INT_MAX;
            foreach ($candidates as $val) {
                if ($val < $next) {
                    $next = $val;
                }
            }
            $ugly[$i] = $next;

            for ($j = 0; $j < $k; $j++) {
                if ($candidates[$j] == $next) {
                    $indices[$j]++;
                    $candidates[$j] = $primes[$j] * $ugly[$indices[$j]];
                }
            }
        }

        return $ugly[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func nthSuperUglyNumber(_ n: Int, _ primes: [Int]) -> Int {
        let k = primes.count
        var ugly = [Int](repeating: 0, count: n)
        ugly[0] = 1
        
        var idx = [Int](repeating: 0, count: k)
        var nextVals = [Int](repeating: 0, count: k)
        for i in 0..<k {
            nextVals[i] = primes[i]
        }
        
        if n == 1 { return 1 }
        
        for i in 1..<n {
            var nextUgly = Int.max
            // find minimum candidate
            for val in nextVals {
                if val < nextUgly {
                    nextUgly = val
                }
            }
            ugly[i] = nextUgly
            
            // advance pointers that match the minimum
            for j in 0..<k {
                if nextVals[j] == nextUgly {
                    idx[j] += 1
                    let newVal = primes[j] * ugly[idx[j]]
                    nextVals[j] = newVal
                }
            }
        }
        
        return ugly[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nthSuperUglyNumber(n: Int, primes: IntArray): Int {
        if (n == 1) return 1
        val k = primes.size
        val ugly = IntArray(n)
        ugly[0] = 1

        val idx = IntArray(k) { 0 }
        val nextMul = LongArray(k) { primes[it].toLong() }

        for (i in 1 until n) {
            var nextUgly = Long.MAX_VALUE
            for (j in 0 until k) {
                if (nextMul[j] < nextUgly) nextUgly = nextMul[j]
            }
            ugly[i] = nextUgly.toInt()
            for (j in 0 until k) {
                if (nextMul[j] == nextUgly) {
                    idx[j]++
                    nextMul[j] = ugly[idx[j]].toLong() * primes[j].toLong()
                }
            }
        }
        return ugly[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int nthSuperUglyNumber(int n, List<int> primes) {
    if (n == 1) return 1;
    int k = primes.length;
    List<int> ugly = List.filled(n, 0);
    ugly[0] = 1;

    List<int> idx = List.filled(k, 0);
    List<int> next = List<int>.from(primes); // primes[i] * ugly[0]

    for (int i = 1; i < n; ++i) {
      int minVal = next[0];
      for (int j = 1; j < k; ++j) {
        if (next[j] < minVal) minVal = next[j];
      }
      ugly[i] = minVal;
      for (int j = 0; j < k; ++j) {
        if (next[j] == minVal) {
          idx[j]++;
          next[j] = primes[j] * ugly[idx[j]];
        }
      }
    }

    return ugly[n - 1];
  }
}
```

## Golang

```go
func nthSuperUglyNumber(n int, primes []int) int {
	if n == 1 {
		return 1
	}
	k := len(primes)
	ugly := make([]int, n)
	ugly[0] = 1

	idx := make([]int, k)
	nextMul := make([]int, k)
	for i, p := range primes {
		nextMul[i] = p
	}

	for i := 1; i < n; i++ {
		minVal := nextMul[0]
		for j := 1; j < k; j++ {
			if nextMul[j] < minVal {
				minVal = nextMul[j]
			}
		}
		ugly[i] = minVal
		for j := 0; j < k; j++ {
			if nextMul[j] == minVal {
				idx[j]++
				nextMul[j] = int(int64(ugly[idx[j]]) * int64(primes[j]))
			}
		}
	}
	return ugly[n-1]
}
```

## Ruby

```ruby
def nth_super_ugly_number(n, primes)
  k = primes.length
  ugly = Array.new(n, 0)
  ugly[0] = 1
  idx = Array.new(k, 0)
  next_mul = primes.map { |p| p }

  (1...n).each do |i|
    min_val = next_mul.min
    ugly[i] = min_val
    k.times do |j|
      if next_mul[j] == min_val
        idx[j] += 1
        next_mul[j] = primes[j] * ugly[idx[j]]
      end
    end
  end

  ugly[-1]
end
```

## Scala

```scala
object Solution {
    def nthSuperUglyNumber(n: Int, primes: Array[Int]): Int = {
        val k = primes.length
        val ugly = new Array[Long](n)
        ugly(0) = 1L
        val idx = new Array[Int](k)
        val nextMul = new Array[Long](k)
        var i = 0
        while (i < k) {
            nextMul(i) = primes(i).toLong
            i += 1
        }
        var pos = 1
        while (pos < n) {
            var next = Long.MaxValue
            i = 0
            while (i < k) {
                if (nextMul(i) < next) next = nextMul(i)
                i += 1
            }
            ugly(pos) = next
            i = 0
            while (i < k) {
                if (nextMul(i) == next) {
                    idx(i) += 1
                    nextMul(i) = primes(i).toLong * ugly(idx(i))
                }
                i += 1
            }
            pos += 1
        }
        ugly(n - 1).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn nth_super_ugly_number(n: i32, primes: Vec<i32>) -> i32 {
        let n_usize = n as usize;
        if n_usize == 0 {
            return 0;
        }
        let k = primes.len();
        let mut dp = vec![0u64; n_usize];
        dp[0] = 1;
        let mut idx = vec![0usize; k];
        let mut next_mul: Vec<u64> = primes.iter().map(|&p| p as u64).collect();

        for i in 1..n_usize {
            // Find the smallest candidate
            let &next_ugly = next_mul.iter().min().unwrap();
            dp[i] = next_ugly;
            // Advance all pointers that match the minimum
            for j in 0..k {
                if next_mul[j] == next_ugly {
                    idx[j] += 1;
                    next_mul[j] = dp[idx[j]] * primes[j] as u64;
                }
            }
        }

        dp[n_usize - 1] as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (nth-super-ugly-number n primes)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((k (length primes))
         (pvec (list->vector primes))
         (uglys (make-vector n))
         (idx (make-vector k 0))
         (next (make-vector k)))
    (vector-set! uglys 0 1)
    (for ([j (in-range k)])
      (vector-set! next j (vector-ref pvec j))) ; prime * 1
    (define (vec-min vec len)
      (let loop ((i 1) (min (vector-ref vec 0)))
        (if (= i len)
            min
            (let ((v (vector-ref vec i)))
              (loop (+ i 1) (if (< v min) v min))))))
    (let loop ((i 1))
      (when (< i n)
        (let ((min-val (vec-min next k)))
          (vector-set! uglys i min-val)
          (for ([j (in-range k)])
            (when (= (vector-ref next j) min-val)
              (let* ((new-idx (+ (vector-ref idx j) 1))
                     (new-val (* (vector-ref pvec j) (vector-ref uglys new-idx))))
                (vector-set! idx j new-idx)
                (vector-set! next j new-val))))
          (loop (+ i 1)))))
    (vector-ref uglys (- n 1))))
```

## Erlang

```erlang
-module(solution).
-export([nth_super_ugly_number/2]).

-spec nth_super_ugly_number(N :: integer(), Primes :: [integer()]) -> integer().
nth_super_ugly_number(1, _Primes) ->
    1;
nth_super_ugly_number(N, Primes) when N > 1 ->
    K = length(Primes),
    Ugly0 = array:new(N, {default,0}),
    Ugly1 = array:set(1, 1, Ugly0),
    IdxList = lists:duplicate(K, 1),
    NextMult = Primes,
    loop(2, N, Primes, IdxList, NextMult, Ugly1).

loop(I, N, _Primes, _IdxList, _NextMult, Ugly) when I > N ->
    array:get(N, Ugly);
loop(I, N, Primes, IdxList, NextMult, Ugly) ->
    MinVal = lists:min(NextMult),
    Ugly1 = array:set(I, MinVal, Ugly),
    {NewIdxList, NewNextMult} = update(Primes, IdxList, NextMult, MinVal, Ugly1),
    loop(I + 1, N, Primes, NewIdxList, NewNextMult, Ugly1).

update([], [], [], _Min, _Ugly) ->
    {[], []};
update([P|Ps], [Idx|Idxs], [NM|NMs], Min, Ugly) ->
    if NM =:= Min ->
            NewIdx = Idx + 1,
            NewVal = P * array:get(NewIdx, Ugly),
            {RestIdx, RestNm} = update(Ps, Idxs, NMs, Min, Ugly),
            {[NewIdx|RestIdx], [NewVal|RestNm]};
       true ->
            {RestIdx, RestNm} = update(Ps, Idxs, NMs, Min, Ugly),
            {[Idx|RestIdx], [NM|RestNm]}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec nth_super_ugly_number(n :: integer, primes :: [integer]) :: integer
  def nth_super_ugly_number(n, primes) do
    if n == 1 do
      1
    else
      k = length(primes)
      ugly = :array.new(n, default: 0)
      ugly = :array.set(0, 1, ugly)

      idxs = List.duplicate(0, k)
      next_vals = primes

      gen(ugly, idxs, next_vals, primes, 1, n)
    end
  end

  defp gen(ugly, _idxs, _next_vals, _primes, i, n) when i == n do
    :array.get(n - 1, ugly)
  end

  defp gen(ugly, idxs, next_vals, primes, i, n) do
    min_val = Enum.min(next_vals)

    ugly2 = :array.set(i, min_val, ugly)

    k = length(primes)

    {idxs2, next_vals2} =
      Enum.reduce(0..(k - 1), {idxs, next_vals}, fn j, {i_acc, n_acc} ->
        if Enum.at(n_acc, j) == min_val do
          new_idx = Enum.at(i_acc, j) + 1
          i_acc2 = List.replace_at(i_acc, j, new_idx)
          base = :array.get(new_idx, ugly2)
          new_val = Enum.at(primes, j) * base
          n_acc2 = List.replace_at(n_acc, j, new_val)
          {i_acc2, n_acc2}
        else
          {i_acc, n_acc}
        end
      end)

    gen(ugly2, idxs2, next_vals2, primes, i + 1, n)
  end
end
```
