# 2438. Range Product Queries of Powers

## Cpp

```cpp
class Solution {
public:
    static const long long MOD = 1000000007LL;
    
    long long modPow(long long a, long long e) {
        long long res = 1 % MOD;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            e >>= 1;
        }
        return res;
    }
    
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        // Build powers array from set bits of n
        vector<long long> powers;
        for (int i = 0; n > 0; ++i) {
            if (n & 1) powers.push_back(1LL << i);
            n >>= 1;
        }
        int m = powers.size();
        // Prefix products
        vector<long long> pref(m + 1, 1);
        for (int i = 0; i < m; ++i) {
            pref[i + 1] = (pref[i] * (powers[i] % MOD)) % MOD;
        }
        // Precompute modular inverses of prefix products
        vector<long long> invPref(m + 1);
        for (int i = 0; i <= m; ++i) {
            invPref[i] = modPow(pref[i], MOD - 2);
        }
        // Answer queries
        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int l = q[0];
            int r = q[1];
            long long prod = pref[r + 1] * invPref[l] % MOD;
            ans.push_back((int)prod);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int[] productQueries(int n, int[][] queries) {
        // Build powers array from binary representation of n (ascending order)
        long[] powers = new long[31];
        int m = 0;
        for (int bit = 0; bit < 31; bit++) {
            if ((n & (1 << bit)) != 0) {
                powers[m++] = (1L << bit) % MOD;
            }
        }

        // Prefix products
        long[] pref = new long[m + 1];
        pref[0] = 1L;
        for (int i = 0; i < m; i++) {
            pref[i + 1] = (pref[i] * powers[i]) % MOD;
        }

        // Precompute modular inverses of prefix values
        long[] invPref = new long[m + 1];
        for (int i = 0; i <= m; i++) {
            invPref[i] = modPow(pref[i], MOD - 2);
        }

        int q = queries.length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            int left = queries[i][0];
            int right = queries[i][1];
            long res = pref[right + 1] * invPref[left] % MOD;
            ans[i] = (int) res;
        }
        return ans;
    }

    private long modPow(long base, long exp) {
        long result = 1L;
        long b = base % MOD;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        # collect exponents of set bits in increasing order
        exps = []
        i = 0
        while n:
            if n & 1:
                exps.append(i)
            n >>= 1
            i += 1
        # prefix sums of exponents
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)
        res = []
        for l, r in queries:
            total_exp = pref[r + 1] - pref[l]
            res.append(pow(2, total_exp, MOD))
        return res
```

## Python3

```python
from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        i = 0
        temp = n
        while temp:
            if temp & 1:
                powers.append(1 << i)
            i += 1
            temp >>= 1

        m = len(powers)
        pref = [1] * (m + 1)
        for idx in range(m):
            pref[idx + 1] = pref[idx] * powers[idx] % MOD

        inv_pref = [pow(x, MOD - 2, MOD) for x in pref]

        ans = []
        for l, r in queries:
            ans.append(pref[r + 1] * inv_pref[l] % MOD)
        return ans
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

static long long modPow(long long a, long long e) {
    long long res = 1;
    a %= MOD;
    while (e) {
        if (e & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize; // unused

    int powers[31];
    int len = 0;
    for (int i = 0; i < 31; ++i) {
        if ((n >> i) & 1) {
            powers[len++] = 1 << i;
        }
    }

    long long pref[32];
    pref[0] = 1;
    for (int i = 0; i < len; ++i) {
        pref[i + 1] = (pref[i] * powers[i]) % MOD;
    }

    long long invPref[32];
    for (int i = 0; i <= len; ++i) {
        invPref[i] = modPow(pref[i], MOD - 2);
    }

    int* ans = (int*)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;

    for (int q = 0; q < queriesSize; ++q) {
        int l = queries[q][0];
        int r = queries[q][1];
        long long prod = (pref[r + 1] * invPref[l]) % MOD;
        ans[q] = (int)prod;
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1_000_000_007L;
    
    public int[] ProductQueries(int n, int[][] queries) {
        // Extract exponents of set bits (positions)
        List<int> exps = new List<int>();
        int pos = 0;
        int temp = n;
        while (temp > 0) {
            if ((temp & 1) == 1) exps.Add(pos);
            temp >>= 1;
            pos++;
        }
        
        int m = exps.Count;
        long[] pref = new long[m + 1];
        for (int i = 0; i < m; i++) {
            pref[i + 1] = pref[i] + exps[i];
        }
        
        int q = queries.Length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            long expSum = pref[r + 1] - pref[l];
            ans[i] = (int)ModPow(2, expSum, MOD);
        }
        return ans;
    }
    
    private long ModPow(long baseVal, long exp, long mod) {
        long result = 1;
        baseVal %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * baseVal) % mod;
            }
            baseVal = (baseVal * baseVal) % mod;
            exp >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var productQueries = function(n, queries) {
    const MOD = 1000000007;
    const powers = [];
    let bit = 0;
    let temp = n;
    while (temp > 0) {
        if ((temp & 1) === 1) {
            powers.push(1 << bit);
        }
        temp >>= 1;
        bit++;
    }

    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [l, r] = queries[i];
        let prod = 1;
        for (let j = l; j <= r; ++j) {
            prod = (prod * powers[j]) % MOD;
        }
        ans[i] = prod;
    }
    return ans;
};
```

## Typescript

```typescript
function productQueries(n: number, queries: number[][]): number[] {
    const MOD = 1000000007n;
    const powers: bigint[] = [];
    for (let k = 0; k < 31; k++) {
        if ((n >> k) & 1) {
            powers.push(1n << BigInt(k));
        }
    }

    const result: number[] = [];
    for (const [left, right] of queries) {
        let prod = 1n;
        for (let i = left; i <= right; i++) {
            prod = (prod * powers[i]) % MOD;
        }
        result.push(Number(prod));
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function productQueries($n, $queries) {
        $MOD = 1000000007;
        $powers = [];
        $i = 0;
        while ($n > 0) {
            if ($n & 1) {
                $powers[] = 1 << $i;
            }
            $n >>= 1;
            $i++;
        }

        $answers = [];
        foreach ($queries as $q) {
            [$l, $r] = $q;
            $prod = 1;
            for ($idx = $l; $idx <= $r; $idx++) {
                $prod = ($prod * $powers[$idx]) % $MOD;
            }
            $answers[] = $prod;
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    private func modPow(_ base: Int, _ exp: Int) -> Int {
        var result = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = Int((Int64(result) * Int64(b)) % Int64(MOD))
            }
            b = Int((Int64(b) * Int64(b)) % Int64(MOD))
            e >>= 1
        }
        return result
    }

    func productQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        // Build powers array from set bits of n (ascending order)
        var powers = [Int]()
        var temp = n
        var bitPos = 0
        while temp > 0 {
            if (temp & 1) == 1 {
                let val = 1 << bitPos
                powers.append(val)
            }
            temp >>= 1
            bitPos += 1
        }

        // Prefix products modulo MOD
        var pref = [Int](repeating: 0, count: powers.count + 1)
        pref[0] = 1
        for i in 0..<powers.count {
            pref[i + 1] = Int((Int64(pref[i]) * Int64(powers[i])) % Int64(MOD))
        }

        // Answer queries using modular inverse
        var answer = [Int]()
        let invCache = [Int]() // not used, kept for potential future optimization
        for q in queries {
            let l = q[0]
            let r = q[1]
            let numerator = pref[r + 1]
            let denominatorInv = modPow(pref[l], MOD - 2)
            let prod = Int((Int64(numerator) * Int64(denominatorInv)) % Int64(MOD))
            answer.append(prod)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun productQueries(n: Int, queries: Array<IntArray>): IntArray {
        val MOD = 1_000_000_007L
        // Build the powers array from set bits of n (ascending order)
        val powers = mutableListOf<Long>()
        var bit = 0
        var temp = n
        while (temp > 0) {
            if ((temp and 1) == 1) {
                powers.add(1L shl bit)
            }
            bit++
            temp = temp shr 1
        }

        val m = powers.size
        // Prefix products modulo MOD
        val pref = LongArray(m + 1)
        pref[0] = 1L
        for (i in 0 until m) {
            pref[i + 1] = (pref[i] * powers[i]) % MOD
        }

        fun modPow(a: Long, e: Long): Long {
            var base = a % MOD
            var exp = e
            var res = 1L
            while (exp > 0) {
                if ((exp and 1L) == 1L) {
                    res = (res * base) % MOD
                }
                base = (base * base) % MOD
                exp = exp shr 1
            }
            return res
        }

        // Precompute modular inverses of prefix products
        val invPref = LongArray(m + 1)
        for (i in 0..m) {
            invPref[i] = modPow(pref[i], MOD - 2)
        }

        val answer = IntArray(queries.size)
        for (idx in queries.indices) {
            val l = queries[idx][0]
            val r = queries[idx][1]
            val prod = (pref[r + 1] * invPref[l]) % MOD
            answer[idx] = prod.toInt()
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _MOD;
    int e = exp;
    while (e > 0) {
      if ((e & 1) == 1) {
        result = (result * b) % _MOD;
      }
      b = (b * b) % _MOD;
      e >>= 1;
    }
    return result;
  }

  List<int> productQueries(int n, List<List<int>> queries) {
    // Build the powers array from binary representation of n
    List<int> powers = [];
    int pos = 0;
    int temp = n;
    while (temp > 0) {
      if ((temp & 1) == 1) {
        powers.add(1 << pos);
      }
      temp >>= 1;
      pos++;
    }

    // Prefix products
    List<int> pref = List.filled(powers.length + 1, 0);
    pref[0] = 1;
    for (int i = 0; i < powers.length; i++) {
      pref[i + 1] = (pref[i] * powers[i]) % _MOD;
    }

    // Answer queries using modular inverses
    List<int> ans = List.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      int left = queries[i][0];
      int right = queries[i][1];
      int numerator = pref[right + 1];
      int denominatorInv = _modPow(pref[left], _MOD - 2);
      ans[i] = (numerator * denominatorInv) % _MOD;
    }
    return ans;
  }
}
```

## Golang

```go
const MOD int64 = 1000000007

func modPow(a, e int64) int64 {
	var res int64 = 1
	a %= MOD
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		e >>= 1
	}
	return res
}

func productQueries(n int, queries [][]int) []int {
	var powers []int64
	for i := 0; n > 0; i++ {
		if n&1 == 1 {
			powers = append(powers, (int64(1)<<i)%MOD)
		}
		n >>= 1
	}
	m := len(powers)
	pref := make([]int64, m+1)
	pref[0] = 1
	for i := 0; i < m; i++ {
		pref[i+1] = pref[i] * powers[i] % MOD
	}
	invPref := make([]int64, m+1)
	for i := 0; i <= m; i++ {
		invPref[i] = modPow(pref[i], MOD-2)
	}
	ans := make([]int, len(queries))
	for idx, q := range queries {
		l, r := q[0], q[1]
		val := pref[r+1] * invPref[l] % MOD
		ans[idx] = int(val)
	}
	return ans
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = (result * b) % mod if (e & 1) == 1
    b = (b * b) % mod
    e >>= 1
  end
  result
end

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def product_queries(n, queries)
  powers = []
  i = 0
  while (1 << i) <= n
    if (n & (1 << i)) != 0
      powers << (1 << i)
    end
    i += 1
  end

  m = powers.length
  pref = Array.new(m + 1, 1)
  (0...m).each do |idx|
    pref[idx + 1] = (pref[idx] * powers[idx]) % MOD
  end

  inv_pref = Array.new(m + 1)
  (0..m).each do |idx|
    inv_pref[idx] = mod_pow(pref[idx], MOD - 2, MOD)
  end

  answers = []
  queries.each do |l, r|
    ans = (pref[r + 1] * inv_pref[l]) % MOD
    answers << ans
  end
  answers
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L

    private def modPow(base: Long, exp: Int): Int = {
        var result = 1L
        var b = base % MOD
        var e = exp
        while (e > 0) {
            if ((e & 1) == 1) result = (result * b) % MOD
            b = (b * b) % MOD
            e >>= 1
        }
        result.toInt
    }

    def productQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
        // collect exponents of set bits in increasing order
        val exps = scala.collection.mutable.ArrayBuffer[Int]()
        var pos = 0
        var temp = n
        while (temp > 0) {
            if ((temp & 1) == 1) exps += pos
            pos += 1
            temp >>= 1
        }

        // prefix sums of exponents
        val pref = new Array[Int](exps.length + 1)
        for (i <- exps.indices) {
            pref(i + 1) = pref(i) + exps(i)
        }

        val ans = new Array[Int](queries.length)
        var i = 0
        while (i < queries.length) {
            val left = queries(i)(0)
            val right = queries(i)(1)
            val sumExp = pref(right + 1) - pref(left)
            ans(i) = modPow(2L, sumExp)
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn product_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        // Build the powers array from binary representation of n
        let mut powers: Vec<i64> = Vec::new();
        let mut bit = 0usize;
        let mut val = n as u32;
        while val > 0 {
            if (val & 1) == 1 {
                powers.push(1i64 << bit);
            }
            bit += 1;
            val >>= 1;
        }

        // Answer each query
        let mut result: Vec<i32> = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let left = q[0] as usize;
            let right = q[1] as usize;
            let mut prod: i64 = 1;
            for &p in powers[left..=right].iter() {
                prod = (prod * (p % MOD)) % MOD;
            }
            result.push(prod as i32);
        }
        result
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (build-powers n)
  (let loop ((i 0) (temp n) (acc '()))
    (if (= temp 0)
        (reverse acc)
        (let ((bit (bitwise-and temp 1)))
          (loop (+ i 1) (arithmetic-shift temp -1)
                (if (= bit 1)
                    (cons (expt 2 i) acc)
                    acc))))))

(define (query-product powers q)
  (let* ((l (first q))
         (r (second q)))
    (let loop ((idx l) (prod 1))
      (if (> idx r)
          prod
          (loop (+ idx 1)
                (modulo (* prod (list-ref powers idx)) MOD))))))

(define/contract (product-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let ((powers (build-powers n)))
    (map (lambda (q) (query-product powers q)) queries)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec product_queries(N :: integer(), Queries :: [[integer()]]) -> [integer()].
product_queries(N, Queries) ->
    Powers = build_powers(N),
    [product_range(Powers, L, R) || [L, R] <- Queries].

build_powers(N) -> build_powers(N, 0, []).

build_powers(N, K, Acc) when (1 bsl K) > N ->
    lists:reverse(Acc);
build_powers(N, K, Acc) ->
    case N band (1 bsl K) of
        0 -> build_powers(N, K + 1, Acc);
        _ -> build_powers(N, K + 1, [(1 bsl K) | Acc])
    end.

product_range(Powers, L, R) ->
    product_range(Powers, 0, L, R, 1).

product_range([], _, _, _, Acc) ->
    Acc;
product_range([H|T], Index, L, R, Acc) ->
    NewAcc = if
        Index >= L, Index =< R -> (Acc * H) rem ?MOD;
        true -> Acc
    end,
    product_range(T, Index + 1, L, R, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @moduledoc false
  @spec product_queries(n :: integer, queries :: [[integer]]) :: [integer]
  def product_queries(n, queries) do
    mod = 1_000_000_007

    powers = build_powers(n)
    pref = prefix_products(powers, mod)

    Enum.map(queries, fn [l, r] ->
      left_prod = Enum.at(pref, l)
      right_prod = Enum.at(pref, r + 1)
      inv_left = mod_pow(left_prod, mod - 2, mod)
      rem(right_prod * inv_left, mod)
    end)
  end

  defp build_powers(n) do
    build_powers(n, 0, [])
  end

  defp build_powers(0, _exp, acc), do: Enum.reverse(acc)

  defp build_powers(num, exp, acc) do
    if (num &&& 1) == 1 do
      build_powers(num >>> 1, exp + 1, [(1 <<< exp) | acc])
    else
      build_powers(num >>> 1, exp + 1, acc)
    end
  end

  defp prefix_products(powers, mod) do
    # builds [1, p0, p0*p1, ..., product of all]
    Enum.reduce(powers, [1], fn x, acc ->
      prev = hd(acc)
      [(rem(prev * x, mod)) | acc]
    end)
    |> Enum.reverse()
  end

  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) when exp > 0 do
    if rem(exp, 2) == 1 do
      tmp = mod_pow(rem(base * base, mod), div(exp - 1, 2), mod)
      rem(base * tmp, mod)
    else
      mod_pow(rem(base * base, mod), div(exp, 2), mod)
    end
  end
end
```
