# 1387. Sort Integers by The Power Value

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int getKth(int lo, int hi, int k) {
        unordered_map<long long,int> memo;
        memo[1] = 0;
        function<int(long long)> power = [&](long long x)->int{
            auto it = memo.find(x);
            if(it != memo.end()) return it->second;
            long long nxt = (x & 1) ? 3 * x + 1 : x / 2;
            int res = 1 + power(nxt);
            memo[x] = res;
            return res;
        };
        
        vector<pair<int,int>> vec;
        vec.reserve(hi - lo + 1);
        for(int i = lo; i <= hi; ++i){
            vec.emplace_back(power(i), i);
        }
        sort(vec.begin(), vec.end(), [](const auto& a, const auto& b){
            if(a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        });
        return vec[k-1].second;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private final Map<Long, Integer> memo = new HashMap<>();

    public Solution() {
        memo.put(1L, 0);
    }

    private int power(long x) {
        if (memo.containsKey(x)) return memo.get(x);
        long next = (x % 2 == 0) ? x / 2 : 3 * x + 1;
        int p = 1 + power(next);
        memo.put(x, p);
        return p;
    }

    public int getKth(int lo, int hi, int k) {
        List<Integer> nums = new ArrayList<>();
        for (int i = lo; i <= hi; i++) {
            nums.add(i);
        }
        Collections.sort(nums, (a, b) -> {
            int pa = power(a);
            int pb = power(b);
            if (pa != pb) return Integer.compare(pa, pb);
            return Integer.compare(a, b);
        });
        return nums.get(k - 1);
    }
}
```

## Python

```python
class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        cache = {1: 0}
        
        def power(x):
            if x in cache:
                return cache[x]
            if x % 2 == 0:
                nxt = x // 2
            else:
                nxt = 3 * x + 1
            cnt = 1 + power(nxt)
            cache[x] = cnt
            return cnt
        
        arr = [(power(v), v) for v in range(lo, hi + 1)]
        arr.sort()
        return arr[k - 1][1]
```

## Python3

```python
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}
        
        def power(x: int) -> int:
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                nxt = x // 2
            else:
                nxt = 3 * x + 1
            memo[x] = 1 + power(nxt)
            return memo[x]
        
        arr = [(power(num), num) for num in range(lo, hi + 1)]
        arr.sort(key=lambda t: (t[0], t[1]))
        return arr[k - 1][1]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int power;
} Pair;

static int getPower(int x) {
    int cnt = 0;
    long long n = x;
    while (n != 1) {
        if ((n & 1LL) == 0)
            n >>= 1;
        else
            n = n * 3 + 1;
        ++cnt;
    }
    return cnt;
}

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->power != pb->power)
        return pa->power - pb->power;
    return pa->val - pb->val;
}

int getKth(int lo, int hi, int k) {
    int size = hi - lo + 1;
    Pair *arr = (Pair *)malloc(size * sizeof(Pair));
    for (int i = 0; i < size; ++i) {
        arr[i].val = lo + i;
        arr[i].power = getPower(arr[i].val);
    }
    qsort(arr, size, sizeof(Pair), cmpPair);
    int result = arr[k - 1].val;
    free(arr);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<long, int> _memo = new Dictionary<long, int>();

    public int GetKth(int lo, int hi, int k) {
        _memo[1] = 0;
        var list = new List<(int power, int value)>();
        for (int i = lo; i <= hi; i++) {
            int p = Power(i);
            list.Add((p, i));
        }
        list.Sort((a, b) => {
            int cmp = a.power.CompareTo(b.power);
            return cmp != 0 ? cmp : a.value.CompareTo(b.value);
        });
        return list[k - 1].value;
    }

    private int Power(long n) {
        if (_memo.TryGetValue(n, out int val)) return val;
        long next = (n & 1) == 0 ? n / 2 : 3 * n + 1;
        int res = 1 + Power(next);
        _memo[n] = res;
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} lo
 * @param {number} hi
 * @param {number} k
 * @return {number}
 */
var getKth = function(lo, hi, k) {
    const memo = new Map();
    memo.set(1, 0);
    
    const power = (x) => {
        if (memo.has(x)) return memo.get(x);
        let next;
        if (x % 2 === 0) {
            next = x / 2;
        } else {
            next = 3 * x + 1;
        }
        const val = 1 + power(next);
        memo.set(x, val);
        return val;
    };
    
    const arr = [];
    for (let i = lo; i <= hi; ++i) {
        arr.push(i);
    }
    
    arr.sort((a, b) => {
        const pa = power(a);
        const pb = power(b);
        if (pa !== pb) return pa - pb;
        return a - b;
    });
    
    return arr[k - 1];
};
```

## Typescript

```typescript
function getKth(lo: number, hi: number, k: number): number {
    const memo = new Map<number, number>();
    memo.set(1, 0);
    function power(x: number): number {
        if (memo.has(x)) return memo.get(x)!;
        const next = x % 2 === 0 ? x / 2 : 3 * x + 1;
        const val = 1 + power(next);
        memo.set(x, val);
        return val;
    }
    const arr: number[] = [];
    for (let i = lo; i <= hi; ++i) arr.push(i);
    arr.sort((a, b) => {
        const pa = power(a), pb = power(b);
        if (pa !== pb) return pa - pb;
        return a - b;
    });
    return arr[k - 1];
}
```

## Php

```php
class Solution {
    private $memo = [1 => 0];

    private function power(int $x): int {
        if (isset($this->memo[$x])) {
            return $this->memo[$x];
        }
        $next = ($x % 2 === 0) ? intdiv($x, 2) : 3 * $x + 1;
        $this->memo[$x] = 1 + $this->power($next);
        return $this->memo[$x];
    }

    /**
     * @param Integer $lo
     * @param Integer $hi
     * @param Integer $k
     * @return Integer
     */
    function getKth($lo, $hi, $k) {
        $list = [];
        for ($i = $lo; $i <= $hi; $i++) {
            $list[] = [$i, $this->power($i)];
        }
        usort($list, function ($a, $b) {
            if ($a[1] === $b[1]) {
                return $a[0] <=> $b[0];
            }
            return $a[1] <=> $b[1];
        });
        return $list[$k - 1][0];
    }
}
```

## Swift

```swift
class Solution {
    private var memo: [Int: Int] = [1: 0]
    
    private func power(_ x: Int) -> Int {
        if let cached = memo[x] {
            return cached
        }
        let next: Int
        if x % 2 == 0 {
            next = x / 2
        } else {
            next = 3 * x + 1
        }
        let result = 1 + power(next)
        memo[x] = result
        return result
    }
    
    func getKth(_ lo: Int, _ hi: Int, _ k: Int) -> Int {
        var list: [(value: Int, pow: Int)] = []
        for v in lo...hi {
            list.append((v, power(v)))
        }
        list.sort { a, b in
            if a.pow == b.pow {
                return a.value < b.value
            } else {
                return a.pow < b.pow
            }
        }
        return list[k - 1].value
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val memo = HashMap<Long, Int>().apply { this[1L] = 0 }

    private fun power(x: Long): Int {
        memo[x]?.let { return it }
        val res = if (x % 2L == 0L) {
            1 + power(x / 2)
        } else {
            1 + power(3 * x + 1)
        }
        memo[x] = res
        return res
    }

    fun getKth(lo: Int, hi: Int, k: Int): Int {
        val list = mutableListOf<Pair<Int, Int>>()
        for (i in lo..hi) {
            list.add(Pair(i, power(i.toLong())))
        }
        list.sortWith(compareBy<Pair<Int, Int>> { it.second }.thenBy { it.first })
        return list[k - 1].first
    }
}
```

## Dart

```dart
class Solution {
  final Map<int, int> _memo = {1: 0};

  int _power(int x) {
    if (_memo.containsKey(x)) return _memo[x]!;
    int next = (x & 1) == 0 ? x ~/ 2 : 3 * x + 1;
    int p = 1 + _power(next);
    _memo[x] = p;
    return p;
  }

  int getKth(int lo, int hi, int k) {
    List<int> nums = [for (int i = lo; i <= hi; i++) i];
    nums.sort((a, b) {
      int pa = _power(a);
      int pb = _power(b);
      if (pa == pb) return a - b;
      return pa - pb;
    });
    return nums[k - 1];
  }
}
```

## Golang

```go
package main

import "sort"

var powerMemo = map[int]int{1: 0}

func getPower(x int) int {
	if v, ok := powerMemo[x]; ok {
		return v
	}
	var res int
	if x%2 == 0 {
		res = 1 + getPower(x/2)
	} else {
		res = 1 + getPower(3*x+1)
	}
	powerMemo[x] = res
	return res
}

func getKth(lo int, hi int, k int) int {
	nums := make([]int, hi-lo+1)
	idx := 0
	for i := lo; i <= hi; i++ {
		nums[idx] = i
		idx++
	}
	sort.Slice(nums, func(i, j int) bool {
		pi := getPower(nums[i])
		pj := getPower(nums[j])
		if pi == pj {
			return nums[i] < nums[j]
		}
		return pi < pj
	})
	return nums[k-1]
}
```

## Ruby

```ruby
def get_kth(lo, hi, k)
  memo = {1 => 0}
  power = lambda do |x|
    return memo[x] if memo.key?(x)
    memo[x] = x.even? ? 1 + power.call(x / 2) : 1 + power.call(3 * x + 1)
  end

  nums = (lo..hi).to_a
  nums.sort_by! { |n| [power.call(n), n] }
  nums[k - 1]
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    private val memo = mutable.Map[Long, Int](1L -> 0)

    private def power(x: Long): Int = {
        memo.getOrElseUpdate(x, {
            val next = if ((x & 1L) == 0L) x / 2 else 3 * x + 1
            1 + power(next)
        })
    }

    def getKth(lo: Int, hi: Int, k: Int): Int = {
        val seq = (lo to hi).map { n => (n, power(n)) }
        val sorted = seq.sortWith {
            case ((a1, p1), (a2, p2)) =>
                if (p1 != p2) p1 < p2 else a1 < a2
        }
        sorted(k - 1)._1
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    fn power(x: u64, memo: &mut HashMap<u64, i32>) -> i32 {
        if let Some(&v) = memo.get(&x) {
            return v;
        }
        let next = if x % 2 == 0 { x / 2 } else { 3 * x + 1 };
        let res = 1 + Self::power(next, memo);
        memo.insert(x, res);
        res
    }

    pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
        let mut memo: HashMap<u64, i32> = HashMap::new();
        memo.insert(1, 0);
        let mut arr: Vec<(i32, i32)> = Vec::new();

        for n in lo..=hi {
            let p = Self::power(n as u64, &mut memo);
            arr.push((n, p));
        }

        arr.sort_by(|a, b| {
            if a.1 != b.1 {
                a.1.cmp(&b.1)
            } else {
                a.0.cmp(&b.0)
            }
        });

        arr[(k - 1) as usize].0
    }
}
```

## Racket

```racket
(define power-hash (make-hash))
(hash-set! power-hash 1 0)

(define (power n)
  (cond
    [(hash-has-key? power-hash n) (hash-ref power-hash n)]
    [else
     (let* ([next (if (even? n) (/ n 2) (+ (* 3 n) 1))]
            [p (+ 1 (power next))])
       (hash-set! power-hash n p)
       p)]))

(define/contract (get-kth lo hi k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([nums (for/list ([i (in-range lo (add1 hi))]) i)]
         [sorted (sort nums
                       (lambda (a b)
                         (let ([pa (power a)] [pb (power b)])
                           (if (= pa pb)
                               (< a b)
                               (< pa pb)))) )])
    (list-ref sorted (- k 1))))
```

## Erlang

```erlang
-module(solution).
-export([get_kth/3]).

-spec get_kth(integer(), integer(), integer()) -> integer().
get_kth(Lo, Hi, K) ->
    Cache0 = #{1 => 0},
    {Pairs, _Cache} = lists:foldl(
        fun(N, {Acc, Cache}) ->
            {P, NewCache} = power(N, Cache),
            {[{P, N} | Acc], NewCache}
        end,
        {[], Cache0},
        lists:seq(Lo, Hi)
    ),
    Sorted = lists:sort(Pairs),
    {_Power, Result} = lists:nth(K, Sorted),
    Result.

power(1, Cache) ->
    {0, Cache};
power(N, Cache) ->
    case maps:is_key(N, Cache) of
        true ->
            {maps:get(N, Cache), Cache};
        false ->
            Next = if N rem 2 == 0 -> N div 2; true -> 3 * N + 1 end,
            {PNext, Cache1} = power(Next, Cache),
            P = PNext + 1,
            Cache2 = maps:put(N, P, Cache1),
            {P, Cache2}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_kth(lo :: integer, hi :: integer, k :: integer) :: integer
  def get_kth(lo, hi, k) do
    {_, pairs} =
      Enum.reduce(lo..hi, {%{1 => 0}, []}, fn num, {memo, acc} ->
        {p, memo2} = power(num, memo)
        {memo2, [{num, p} | acc]}
      end)

    sorted = Enum.sort_by(pairs, fn {num, p} -> {p, num} end)
    {result, _} = Enum.at(sorted, k - 1)
    result
  end

  defp power(1, memo), do: {0, Map.put_new(memo, 1, 0)}
  defp power(x, memo) do
    case Map.fetch(memo, x) do
      {:ok, v} -> {v, memo}
      :error ->
        next = if rem(x, 2) == 0, do: div(x, 2), else: 3 * x + 1
        {next_steps, memo1} = power(next, memo)
        steps = 1 + next_steps
        {steps, Map.put(memo1, x, steps)}
    end
  end
end
```
