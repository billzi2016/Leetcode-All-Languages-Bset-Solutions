# 0964. Least Operators to Express Number

## Cpp

```cpp
class Solution {
public:
    int x;
    unordered_map<long long,int> memo;
    
    int dfs(long long target){
        if (target == 0) return 0;
        if (memo.count(target)) return memo[target];
        if (target < x) return memo[target] = (int)(target * 2);
        
        long long p = 1;
        int k = 0;
        while (p * x <= target){
            p *= x;
            ++k;
        }
        long long a = target / p;
        long long b = target % p;
        
        int opt1 = (int)(a * k + dfs(b));
        int opt2 = (int)((x - a) * k + dfs(p - b));
        memo[target] = min(opt1, opt2);
        return memo[target];
    }
    
    int leastOpsExpressTarget(int X, int target){
        x = X;
        memo.clear();
        return dfs(target) - 1;
    }
};
```

## Java

```java
class Solution {
    private final java.util.Map<Long, Integer> memo = new java.util.HashMap<>();
    public int leastOpsExpressTarget(int x, int target) {
        return dfs(target) - 1;
    }
    private int dfs(long t) {
        if (t == 0) return 0;
        if (memo.containsKey(t)) return memo.get(t);
        long q = t / x;
        int r = (int)(t % x);
        int ans;
        if (q == 0) {
            // target < x
            ans = Math.min(r * 2 - 1, (x - r) * 2);
        } else {
            ans = Math.min(r * 2 + dfs(q), (x - r) * 2 + dfs(q + 1));
        }
        memo.put(t, ans);
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        from functools import lru_cache

        @lru_cache(None)
        def dfs(t):
            if t == 0:
                return 0
            if t < x:
                # either build t using additions of 1 (x/x) or subtract from x
                return min(t * 2 - 1, (x - t) * 2)
            q, r = divmod(t, x)
            # option 1: use q*x and add r ones
            cost_low = dfs(q) + r
            # option 2: use (q+1)*x and subtract (x-r) ones
            cost_high = dfs(q + 1) + (x - r)
            return min(cost_low, cost_high) + 1  # one multiplication by x

        # subtract one because the first operand does not need an operator
        return dfs(target) - 1
```

## Python3

```python
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        import functools

        @functools.lru_cache(None)
        def dfs(t: int) -> int:
            if t == 0:
                return 0
            if t == x:
                return 0
            if t < x:
                # either add (t) ones or subtract from one x
                return min(t * 2 - 1, (x - t) * 2)
            q, r = divmod(t, x)
            # use r ones to add
            cost_add = r * 2 + dfs(q)
            # use (x - r) ones to subtract from next multiple
            cost_sub = (x - r) * 2 + dfs(q + 1)
            return min(cost_add, cost_sub) + 1

        return dfs(target)
```

## C

```c
int leastOpsExpressTarget(int x, int target) {
    long long X = x;
    unordered_map<long long,int> memo;
    function<int(long long)> dfs = [&](long long t)->int{
        if (t == 0) return 0;
        if (t < X) {
            // build using additions of 1 (=x/x) or subtraction from x
            int addWay = (int)(t * 2 - 1);          // t times (x/x) plus (t-1) adds
            int subWay = (int)((X - t) * 2);       // build (x-t) then subtract from x
            return min(addWay, subWay);
        }
        if (memo.count(t)) return memo[t];
        long long p = X;
        int n = 0; // number of multiplications to get p (=X^{n+1})
        while (p * X <= t) {
            p *= X;
            ++n;
        }
        long long a = t / p;
        long long b = t % p;
        int ans;
        if (b == 0) {
            // exact multiple of p
            ans = min((int)(a * n + a - 1), (int)((X - a) * n + 1));
        } else {
            // either add remainder or subtract complement
            int opAdd = (int)(a * n + a + dfs(b));               // use a copies of p and add b
            int opSub = (int)((X - a) * n + 2 + dfs(p - b));    // use (x-a) copies then subtract (p-b)
            ans = min(opAdd, opSub);
        }
        memo[t] = ans;
        return ans;
    };
    return dfs(target);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private int _x;
    private Dictionary<long, int> _memo = new Dictionary<long, int>();

    public int LeastOpsExpressTarget(int x, int target) {
        _x = x;
        return Dfs(target);
    }

    private int Dfs(long target) {
        if (target == 0) return 0;
        if (_memo.TryGetValue(target, out var cached)) return cached;

        int result;
        if (target < _x) {
            // either add target copies of 1 (x/x) or subtract from x
            long opt1 = target * 2 - 1;          // target times "x/x" added together
            long opt2 = (_x - target) * 2;       // x minus (x/x) repeated
            result = (int)Math.Min(opt1, opt2);
        } else {
            // find largest power of x not exceeding target
            int k = 0;
            long power = 1;
            while (power * _x <= target) {
                power *= _x;
                k++;
            }

            // option 1: use this power and handle the remainder
            int opt1 = k + Dfs(target - power);
            // option 2: go to next higher power and subtract the complement
            int opt2 = (k + 1) + Dfs(power * _x - target);
            result = Math.Min(opt1, opt2);
        }

        _memo[target] = result;
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} target
 * @return {number}
 */
var leastOpsExpressTarget = function(x, target) {
    const memo = new Map();

    // minimal ops to express a value v where 0 < v < x
    const smallCost = (v) => Math.min(2 * v - 1, 2 * (x - v));

    const dfs = (t) => {
        if (memo.has(t)) return memo.get(t);
        let ans;
        if (t === 0) {
            // not needed in final answer; set to 0 for safety
            ans = 0;
        } else if (t < x) {
            ans = smallCost(t);
        } else {
            const q = Math.floor(t / x);
            const r = t % x;

            if (r === 0) {
                // exact multiple of x
                ans = dfs(q) + 1; // one multiplication
            } else {
                // option A: q * x + r
                const costA = dfs(q) + 1 + smallCost(r);
                // option B: (q + 1) * x - (x - r)
                const costB = dfs(q + 1) + 1 + smallCost(x - r);
                ans = Math.min(costA, costB);
            }
        }
        memo.set(t, ans);
        return ans;
    };

    return dfs(target);
};
```

## Typescript

```typescript
function leastOpsExpressTarget(x: number, target: number): number {
    const memo = new Map<number, number>();
    function dfs(t: number): number {
        if (t === 0) return 0;
        if (memo.has(t)) return memo.get(t)!;
        let ans: number;
        if (t < x) {
            const option1 = t * 2 - 1;          // use t times (x/x) and additions
            const option2 = (x - t) * 2;        // subtract from x
            ans = Math.min(option1, option2);
        } else {
            const q = Math.floor(t / x);
            const r = t % x;
            const optA = r + dfs(q);            // add r copies after building q*x
            const optB = (x - r) + dfs(q + 1);   // subtract (x-r) copies after building (q+1)*x
            ans = Math.min(optA, optB) + 1;     // plus one multiplication/division operator
        }
        memo.set(t, ans);
        return ans;
    }
    return dfs(target);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $target
     * @return Integer
     */
    function leastOpsExpressTarget($x, $target) {
        $this->x = $x;
        $this->memo = [];
        return $this->dfs($target) - 1;
    }

    private function dfs($t) {
        if ($t == 0) {
            return 0;
        }
        if (isset($this->memo[$t])) {
            return $this->memo[$t];
        }
        $x = $this->x;
        if ($t < $x) {
            $res = min($t * 2 - 1, ($x - $t) * 2);
            $this->memo[$t] = $res;
            return $res;
        }
        $q = intdiv($t, $x);
        $r = $t % $x;
        $ans = min($this->dfs($q) + $r, $this->dfs($q + 1) + ($x - $r));
        $this->memo[$t] = $ans;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    private var X = 0
    private var memo = [Int:Int]()
    
    func leastOpsExpressTarget(_ x: Int, _ target: Int) -> Int {
        self.X = x
        let result = dfs(target)
        return result - 1
    }
    
    private func dfs(_ t: Int) -> Int {
        if let cached = memo[t] { return cached }
        var ans: Int
        if t == 0 {
            ans = 0
        } else if t < X {
            let opt1 = t * 2 - 1          // use t times (x/x) and additions
            let opt2 = (X - t) * 2        // subtract from x
            ans = min(opt1, opt2)
        } else {
            let a = t / X
            let b = t % X
            // option 1: use addition for remainder b
            var op1 = dfs(a) + b * 2
            // option 2: use subtraction for remainder (X - b)
            var op2 = Int.max
            if b != 0 {
                op2 = dfs(a + 1) + (X - b) * 2 + 1
            }
            ans = min(op1, op2)
        }
        memo[t] = ans
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val memo = HashMap<Long, Int>()
    fun leastOpsExpressTarget(x: Int, target: Int): Int {
        return dfs(x.toLong(), target.toLong())
    }

    private fun dfs(x: Long, t: Long): Int {
        if (t == 0L) return 0
        memo[t]?.let { return it }
        val result = if (t < x) {
            val ti = t.toInt()
            val xi = x.toInt()
            kotlin.math.min(ti * 2 - 1, (xi - ti) * 2)
        } else {
            var p = 1L
            var k = 0
            while (p * x <= t) {
                p *= x
                k++
            }
            val a = t / p
            val b = t % p

            // Use a copies of p
            var op1 = (a * k + dfs(x, b)).toInt()
            if (b == 0L) {
                op1 -= 1   // exact multiple, no extra addition needed
                memo[t] = op1
                return op1
            }

            // Use a+1 copies of p and subtract the excess
            val op2 = ((a + 1) * k + dfs(x, p - b)).toInt()
            kotlin.math.min(op1, op2)
        }
        memo[t] = result
        return result
    }
}
```

## Dart

```dart
class Solution {
  late int _x;
  final Map<int, int> _memo = {};

  int leastOpsExpressTarget(int x, int target) {
    _x = x;
    return _dfs(target);
  }

  int _dfs(int t) {
    if (t == 0) return 0;
    if (_memo.containsKey(t)) return _memo[t]!;
    int res;
    if (t < _x) {
      int option1 = t * 2 - 1; // using additions of 1 (x/x)
      int option2 = (_x - t) * 2; // using subtraction from x
      res = option1 < option2 ? option1 : option2;
    } else {
      int k = 0;
      int p = 1;
      while (p * _x <= t) {
        p *= _x;
        k++;
      }
      int a = t ~/ p;
      // Option 1: use a copies of p
      res = a * k + _dfs(t - a * p);
      // Option 2: go over to the next power and subtract
      if (a != _x) {
        int cost2 = (_x - a) * k + 1 + _dfs(p * _x - t);
        if (cost2 < res) res = cost2;
      }
    }
    _memo[t] = res;
    return res;
  }
}
```

## Golang

```go
func leastOpsExpressTarget(x int, target int) int {
	if target == 0 {
		return 0
	}
	memo := make(map[int]int)
	var dfs func(int) int
	dfs = func(t int) int {
		if v, ok := memo[t]; ok {
			return v
		}
		var res int
		if t < x {
			a := 2*t - 1          // use t times (x/x) and add them
			b := 2 * (x - t)      // subtract from x
			if a < b {
				res = a
			} else {
				res = b
			}
		} else {
			q := t / x
			r := t % x
			op1 := dfs(q) + r          // q*x + r
			op2 := dfs(q+1) + (x - r)  // (q+1)*x - (x-r)
			if op1 < op2 {
				res = op1
			} else {
				res = op2
			}
			res++ // the multiplication/division at this level
		}
		memo[t] = res
		return res
	}
	ans := dfs(target) - 1
	if ans < 0 {
		ans = 0
	}
	return ans
}
```

## Ruby

```ruby
def least_ops_express_target(x, target)
  memo = {}
  dfs = lambda do |t|
    return 0 if t == 0
    return [x - 1, 2].min if t == 1
    return memo[t] if memo.key?(t)

    q, r = t.divmod(x)
    op_add = r + dfs.call(q)
    op_sub = (x - r) + dfs.call(q + 1)
    res = [op_add, op_sub].min
    res += 1 if q > 0
    memo[t] = res
    res
  end

  dfs.call(target)
end
```

## Scala

```scala
object Solution {
    def leastOpsExpressTarget(x: Int, target: Int): Int = {
        import scala.collection.mutable

        val memo = mutable.Map[Long, Int]()

        def dfs(t: Long): Int = {
            if (t == 0) return 0
            if (t == 1) return Math.min(x - 1, 2)
            memo.getOrElseUpdate(t, {
                val q = t / x
                val r = (t % x).toInt

                var ans = Int.MaxValue / 2

                // Option 1: use r times addition of x^k
                val opt1 = r + dfs(q) + (if (q > 0) 1 else 0)
                ans = Math.min(ans, opt1)

                // Option 2: use (x - r) times subtraction (overshoot to next multiple)
                val opt2 = (x - r) + dfs(q + 1) + 1
                ans = Math.min(ans, opt2)

                ans
            })
        }

        dfs(target.toLong)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn least_ops_express_target(x: i32, target: i32) -> i32 {
        fn dfs(t: i64, x: i64, memo: &mut HashMap<i64, i32>) -> i32 {
            if t == 0 {
                return 0;
            }
            if let Some(&v) = memo.get(&t) {
                return v;
            }
            let res = if t < x {
                // use only 1's (x/x) or complement using subtraction
                let a = t * 2 - 1;               // t times (x/x) + (t-1) additions
                let b = (x - t) * 2 + 1;         // (x-t) times (x/x) then one subtraction
                std::cmp::min(a, b) as i32
            } else {
                // find highest power p = x^k <= t
                let mut p: i64 = 1;
                let mut k: i32 = 0; // exponent
                while p * x <= t {
                    p *= x;
                    k += 1;
                }
                // now p = x^k, k >= 1
                let q = t / p;
                let r = t % p;

                // Option A: use q copies of p and handle remainder r
                // cost for q copies: each copy needs (k-1) multiplications,
                // plus (q-1) additions between them.
                // Total operators for the q copies = q * k - 1
                let mut cost_a = (q * (k as i64) - 1) as i32 + dfs(r, x, memo);
                if r != 0 {
                    cost_a += 1; // addition to add remainder
                }

                // Option B: go over one more power and subtract the difference
                let diff = p * x - t;
                // building x^{k+1} needs k multiplications (exponent-1)
                let mut cost_b = k as i32 + dfs(diff, x, memo) + 1; // subtraction

                std::cmp::min(cost_a, cost_b)
            };
            memo.insert(t, res);
            res
        }

        let mut memo: HashMap<i64, i32> = HashMap::new();
        dfs(target as i64, x as i64, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (least-ops-express-target x target)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ([memo (make-hash)])
    (define (dfs t)
      (cond
        [(zero? t) 0]
        [else
         (if (hash-has-key? memo t)
             (hash-ref memo t)
             (begin
               ;; find largest power cur = x^k <= t
               (let loop ([cur 1] [k 0])
                 (if (<= (* cur x) t)
                     (loop (* cur x) (+ k 1))
                     (let* ([a (quotient t cur)]
                            [b (remainder t cur)])
                       (define result
                         (if (= b 0)
                             (+ (* a k) (- a 1))
                             (let* ([cost1 (+ (* a k) (- a 1) (dfs b))]
                                    [cost2 (+ (* (+ a 1) k) a (dfs (- cur b)))])
                               (min cost1 cost2))))
                       (hash-set! memo t result)
                       result))))]))))
    (dfs target)))
```

## Erlang

```erlang
-spec least_ops_express_target(X :: integer(), Target :: integer()) -> integer().
least_ops_express_target(X, Target) ->
    {Res, _} = dfs(Target, X, #{}),
    Res.

%% dfs(Target, X, Memo) -> {Result, UpdatedMemo}
dfs(0, _, Memo) ->
    {0, Memo};
dfs(Target, X, Memo) when is_map_key(Target, Memo) ->
    {maps:get(Target, Memo), Memo};
dfs(Target, X, Memo) when Target < X ->
    Res = min(Target * 2 - 1, (X - Target) * 2),
    NewMemo = maps:put(Target, Res, Memo),
    {Res, NewMemo};
dfs(Target, X, Memo) ->
    {P, K} = max_power_leq(Target, X, 1, 0),
    A = Target div P,
    B = Target rem P,
    %% option 1
    {CostB, Memo1} = dfs(B, X, Memo),
    Cost1 = A * K + CostB + A,
    case A == X of
        true ->
            MinCost = Cost1,
            FinalMemo = Memo1;
        false ->
            {CostPB, Memo2} = dfs(P - B, X, Memo1),
            Cost2 = (X - A) * K + CostPB + (X - A),
            MinCost = min(Cost1, Cost2),
            FinalMemo = Memo2
    end,
    UpdatedMemo = maps:put(Target, MinCost, FinalMemo),
    {MinCost, UpdatedMemo}.

%% Find the largest power P = X^K such that P <= N.
max_power_leq(N, X, P, K) when P * X =< N ->
    max_power_leq(N, X, P * X, K + 1);
max_power_leq(_, _, P, K) ->
    {P, K}.
```

## Elixir

```elixir
defmodule Solution do
  @spec least_ops_express_target(x :: integer, target :: integer) :: integer
  def least_ops_express_target(x, target) do
    {res, _} = dfs(target, x, %{})
    res
  end

  defp dfs(0, _x, memo), do: {0, memo}

  defp dfs(t, x, memo) when t < x do
    case Map.fetch(memo, t) do
      {:ok, v} -> {v, memo}
      :error ->
        res = min(t * 2 - 1, (x - t) * 2)
        {res, Map.put(memo, t, res)}
    end
  end

  defp dfs(t, x, memo) do
    case Map.fetch(memo, t) do
      {:ok, v} -> {v, memo}
      :error ->
        {p, k} = find_pow(x, t, 1, 0)
        a = div(t, p)
        b = rem(t, p)

        if b == 0 do
          res = a * k - 1
          {res, Map.put(memo, t, res)}
        else
          {c1, memo1} = dfs(b, x, memo)
          cost1 = a * k + c1

          {c2, memo2} = dfs(p - b, x, memo1)
          cost2 = (x - a) * k + c2

          res = min(cost1, cost2)
          {res, Map.put(memo2, t, res)}
        end
    end
  end

  defp find_pow(x, limit, p, k) do
    if p * x <= limit do
      find_pow(x, limit, p * x, k + 1)
    else
      {p, k}
    end
  end
end
```
