# 2961. Double Modular Exponentiation

## Cpp

```cpp
class Solution {
public:
    long long modPow(long long base, long long exp, long long mod) {
        if (mod == 1) return 0;
        long long res = 1 % mod;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    vector<int> getGoodIndices(vector<vector<int>>& variables, int target) {
        vector<int> ans;
        for (int i = 0; i < (int)variables.size(); ++i) {
            long long a = variables[i][0];
            long long b = variables[i][1];
            long long c = variables[i][2];
            long long m = variables[i][3];
            long long first = modPow(a, b, m);
            long long result = modPow(first, c, m);
            if (result == target) ans.push_back(i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> getGoodIndices(int[][] variables, int target) {
        java.util.List<Integer> good = new java.util.ArrayList<>();
        for (int i = 0; i < variables.length; i++) {
            int a = variables[i][0];
            int b = variables[i][1];
            int c = variables[i][2];
            int m = variables[i][3];
            int first = powMod(a, b, m);
            int result = powMod(first, c, m);
            if (result == target) {
                good.add(i);
            }
        }
        return good;
    }

    private int powMod(int base, int exp, int mod) {
        if (mod == 1) return 0;
        long res = 1;
        long b = base % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * b) % mod;
            }
            b = (b * b) % mod;
            exp >>= 1;
        }
        return (int) res;
    }
}
```

## Python

```python
class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            first = pow(a, b, m)
            second = pow(first, c, m)
            if second == target:
                res.append(i)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good = []
        for i, (a, b, c, m) in enumerate(variables):
            first = pow(a, b, m)
            val = pow(first, c, m)
            if val == target:
                good.append(i)
        return good
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
static long long modPow(long long base, int exp, int mod) {
    if (mod == 1) return 0;
    long long result = 1 % mod;
    base %= mod;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getGoodIndices(int** variables, int variablesSize, int* variablesColSize, int target, int* returnSize){
    (void)variablesColSize; // unused
    int *good = (int*)malloc(sizeof(int) * variablesSize);
    int cnt = 0;
    for (int i = 0; i < variablesSize; ++i) {
        int a = variables[i][0];
        int b = variables[i][1];
        int c = variables[i][2];
        int m = variables[i][3];
        long long first = modPow(a, b, m);
        long long final = modPow(first, c, m);
        if (final == target) {
            good[cnt++] = i;
        }
    }
    *returnSize = cnt;
    return good;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> GetGoodIndices(int[][] variables, int target) {
        var good = new List<int>();
        for (int i = 0; i < variables.Length; i++) {
            int a = variables[i][0];
            int b = variables[i][1];
            int c = variables[i][2];
            int m = variables[i][3];

            long first = ModPow(a, b, m);
            long result = ModPow(first, c, m);

            if (result == target) {
                good.Add(i);
            }
        }
        return good;
    }

    private long ModPow(long baseVal, long exp, long mod) {
        if (mod == 1) return 0;
        long result = 1 % mod;
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
 * @param {number[][]} variables
 * @param {number} target
 * @return {number[]}
 */
var getGoodIndices = function(variables, target) {
    const modPow = (base, exp, mod) => {
        if (mod === 1) return 0;
        let result = 1 % mod;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) result = (result * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    };
    
    const good = [];
    for (let i = 0; i < variables.length; ++i) {
        const [a, b, c, m] = variables[i];
        const first = modPow(a, b, m);
        const second = modPow(first, c, m);
        if (second === target) good.push(i);
    }
    return good;
};
```

## Typescript

```typescript
function getGoodIndices(variables: number[][], target: number): number[] {
    const res: number[] = [];
    
    const powMod = (base: number, exp: number, mod: number): number => {
        if (mod === 1) return 0;
        let result = 1 % mod;
        let b = base % mod;
        let e = exp;
        while (e > 0) {
            if (e & 1) result = (result * b) % mod;
            b = (b * b) % mod;
            e >>= 1;
        }
        return result;
    };
    
    for (let i = 0; i < variables.length; ++i) {
        const [a, b, c, m] = variables[i];
        const first = powMod(a, b, m);
        const second = powMod(first, c, m);
        if (second === target) res.push(i);
    }
    
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $variables
     * @param Integer $target
     * @return Integer[]
     */
    function getGoodIndices($variables, $target) {
        $good = [];
        foreach ($variables as $i => $arr) {
            [$a, $b, $c, $m] = $arr;
            $first = $this->modPow($a, $b, $m);
            $second = $this->modPow($first, $c, $m);
            if ($second === $target) {
                $good[] = $i;
            }
        }
        return $good;
    }

    private function modPow($base, $exp, $mod) {
        if ($mod == 1) {
            return 0;
        }
        $result = 1 % $mod;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getGoodIndices(_ variables: [[Int]], _ target: Int) -> [Int] {
        var good = [Int]()
        for (i, v) in variables.enumerated() {
            let a = v[0], b = v[1], c = v[2], m = v[3]
            let first = modPow(a, b, m)
            let second = modPow(first, c, m)
            if second == target {
                good.append(i)
            }
        }
        return good
    }
    
    private func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
        var result = 1 % mod
        var b = base % mod
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % mod
            }
            b = (b * b) % mod
            e >>= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getGoodIndices(variables: Array<IntArray>, target: Int): List<Int> {
        val good = mutableListOf<Int>()
        for (i in variables.indices) {
            val a = variables[i][0]
            val b = variables[i][1]
            val c = variables[i][2]
            val m = variables[i][3]
            val first = modPow(a, b, m)
            val result = modPow(first, c, m)
            if (result == target) good.add(i)
        }
        return good
    }

    private fun modPow(base: Int, exp: Int, mod: Int): Int {
        if (mod == 1) return 0
        var result = 1L
        var b = (base % mod).toLong()
        var e = exp
        val m = mod.toLong()
        while (e > 0) {
            if ((e and 1) == 1) {
                result = (result * b) % m
            }
            b = (b * b) % m
            e = e shr 1
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  List<int> getGoodIndices(List<List<int>> variables, int target) {
    List<int> good = [];
    for (int i = 0; i < variables.length; ++i) {
      var v = variables[i];
      int a = v[0], b = v[1], c = v[2], m = v[3];
      int first = _modPow(a, b, m);
      int second = _modPow(first, c, m);
      if (second == target) good.add(i);
    }
    return good;
  }

  int _modPow(int base, int exp, int mod) {
    if (mod == 1) return 0;
    int result = 1 % mod;
    int b = base % mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % mod;
      }
      b = (b * b) % mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
func getGoodIndices(variables [][]int, target int) []int {
    good := []int{}
    for i, v := range variables {
        a, b, c, m := v[0], v[1], v[2], v[3]
        first := modPow(a, b, m)
        second := modPow(first, c, m)
        if second == target {
            good = append(good, i)
        }
    }
    return good
}

func modPow(base, exp, mod int) int {
    if mod == 1 {
        return 0
    }
    result := 1 % mod
    base %= mod
    for exp > 0 {
        if exp&1 == 1 {
            result = (result * base) % mod
        }
        base = (base * base) % mod
        exp >>= 1
    }
    return result
}
```

## Ruby

```ruby
# @param {Integer[][]} variables
# @param {Integer} target
# @return {Integer[]}
def get_good_indices(variables, target)
  def mod_pow(base, exp, mod)
    return 0 if mod == 1
    result = 1 % mod
    base %= mod
    while exp > 0
      result = (result * base) % mod if (exp & 1) == 1
      base = (base * base) % mod
      exp >>= 1
    end
    result
  end

  good = []
  variables.each_with_index do |(a, b, c, m), idx|
    first = mod_pow(a, b, m)
    val = mod_pow(first, c, m)
    good << idx if val == target
  end
  good
end
```

## Scala

```scala
object Solution {
    def getGoodIndices(variables: Array[Array[Int]], target: Int): List[Int] = {
        def modPow(base: Int, exp: Int, mod: Int): Int = {
            if (mod == 1) return 0
            var result = 1L % mod
            var b = base.toLong % mod
            var e = exp
            val m = mod.toLong
            while (e > 0) {
                if ((e & 1) == 1) result = (result * b) % m
                b = (b * b) % m
                e >>= 1
            }
            result.toInt
        }

        val good = scala.collection.mutable.ListBuffer[Int]()
        for (i <- variables.indices) {
            val a = variables(i)(0)
            val b = variables(i)(1)
            val c = variables(i)(2)
            val m = variables(i)(3)

            val first = modPow(a, b, m)
            val finalVal = modPow(first, c, m)

            if (finalVal == target) good += i
        }
        good.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_good_indices(variables: Vec<Vec<i32>>, target: i32) -> Vec<i32> {
        fn mod_pow(mut base: i64, mut exp: i32, modulus: i64) -> i64 {
            if modulus == 1 {
                return 0;
            }
            let mut result = 1 % modulus;
            base %= modulus;
            while exp > 0 {
                if (exp & 1) == 1 {
                    result = (result * base) % modulus;
                }
                base = (base * base) % modulus;
                exp >>= 1;
            }
            result
        }

        let mut good = Vec::new();
        for (i, v) in variables.iter().enumerate() {
            let a = v[0] as i64;
            let b = v[1];
            let c = v[2];
            let m = v[3] as i64;

            let first = mod_pow(a, b, m);
            let final_val = mod_pow(first, c, m);

            if final_val == target as i64 {
                good.push(i as i32);
            }
        }
        good
    }
}
```

## Racket

```racket
(define (pow-mod base exp mod)
  (if (= mod 1)
      0
      (let loop ((b (modulo base mod)) (e exp) (res 1))
        (if (= e 0)
            res
            (let* ((new-res (if (odd? e) (modulo (* res b) mod) res))
                   (b2 (modulo (* b b) mod)))
              (loop b2 (quotient e 2) new-res))))))

(define/contract (get-good-indices variables target)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  (let loop ((idx 0) (lst variables) (acc '()))
    (if (null? lst)
        (reverse acc)
        (let* ((row (car lst))
               (a (list-ref row 0))
               (b (list-ref row 1))
               (c (list-ref row 2))
               (m (list-ref row 3))
               (first (pow-mod a b m))
               (second (pow-mod first c m)))
          (loop (+ idx 1)
                (cdr lst)
                (if (= second target) (cons idx acc) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([get_good_indices/2]).

-spec get_good_indices(Variables :: [[integer()]], Target :: integer()) -> [integer()].
get_good_indices(Variables, Target) ->
    get_good_indices(Variables, Target, 0, []).

get_good_indices([], _Target, _Idx, Acc) ->
    lists:reverse(Acc);
get_good_indices([Var|Rest], Target, Idx, Acc) ->
    [A,B,C,M] = Var,
    X = mod_pow(A, B, M),
    Y = mod_pow(X, C, M),
    NewAcc = case Y == Target of
        true -> [Idx|Acc];
        false -> Acc
    end,
    get_good_indices(Rest, Target, Idx+1, NewAcc).

-spec mod_pow(integer(), integer(), integer()) -> integer().
mod_pow(_Base, _Exp, 1) ->
    0;
mod_pow(Base, Exp, Mod) ->
    mod_pow_loop(Base rem Mod, Exp, Mod, 1).

mod_pow_loop(_, 0, _, Acc) ->
    Acc;
mod_pow_loop(Base, Exp, Mod, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem Mod,
    mod_pow_loop((Base * Base) rem Mod, Exp bsr 1, Mod, NewAcc);
mod_pow_loop(Base, Exp, Mod, Acc) ->
    mod_pow_loop((Base * Base) rem Mod, Exp bsr 1, Mod, Acc).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec get_good_indices(variables :: [[integer]], target :: integer) :: [integer]
  def get_good_indices(variables, target) do
    variables
    |> Enum.with_index()
    |> Enum.reduce([], fn {var, idx}, acc ->
      [a, b, c, m] = var

      result =
        if m == 1 do
          0
        else
          mod_pow(mod_pow(a, b, m), c, m)
        end

      if result == target do
        [idx | acc]
      else
        acc
      end
    end)
    |> Enum.reverse()
  end

  defp mod_pow(_base, _exp, 1), do: 0
  defp mod_pow(base, exp, mod) when exp >= 0 do
    do_mod_pow(rem(base, mod), exp, mod, 1)
  end

  defp do_mod_pow(_base, 0, _mod, acc), do: acc

  defp do_mod_pow(base, exp, mod, acc) do
    acc = if (exp &&& 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    exp = exp >>> 1
    do_mod_pow(base, exp, mod, acc)
  end
end
```
