# 1434. Number of Ways to Wear Different Hats to Each Other

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    vector<vector<int>> hatToPeople;
    vector<vector<int>> memo;
    int n, fullMask;
    
    int dfs(int hat, int mask) {
        if (mask == fullMask) return 1;
        if (hat > 40) return 0;
        int &res = memo[hat][mask];
        if (res != -1) return res;
        long long ans = dfs(hat + 1, mask); // skip current hat
        for (int person : hatToPeople[hat]) {
            if (!(mask & (1 << person))) {
                ans += dfs(hat + 1, mask | (1 << person));
                if (ans >= MOD) ans -= MOD;
            }
        }
        res = int(ans % MOD);
        return res;
    }
    
    int numberWays(vector<vector<int>>& hats) {
        n = hats.size();
        fullMask = (1 << n) - 1;
        hatToPeople.assign(41 + 1, {});
        for (int i = 0; i < n; ++i) {
            for (int h : hats[i]) {
                if (h >= 1 && h <= 40)
                    hatToPeople[h].push_back(i);
            }
        }
        memo.assign(42, vector<int>(1 << n, -1));
        return dfs(1, 0);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private List<Integer>[] hatToPeople;
    private int[][] memo;
    private int fullMask;

    public int numberWays(List<List<Integer>> hats) {
        int n = hats.size();
        fullMask = (1 << n) - 1;

        // Initialize mapping from hat to people who like it
        hatToPeople = new ArrayList[41];
        for (int i = 1; i <= 40; i++) {
            hatToPeople[i] = new ArrayList<>();
        }
        for (int person = 0; person < n; person++) {
            for (int h : hats.get(person)) {
                hatToPeople[h].add(person);
            }
        }

        // Memo table: hats indexed from 1..40, mask up to fullMask
        memo = new int[42][fullMask + 1];
        for (int i = 0; i < memo.length; i++) {
            Arrays.fill(memo[i], -1);
        }

        return dfs(1, 0);
    }

    private int dfs(int hat, int mask) {
        if (mask == fullMask) {
            return 1;
        }
        if (hat > 40) {
            return 0;
        }
        if (memo[hat][mask] != -1) {
            return memo[hat][mask];
        }

        long ans = dfs(hat + 1, mask); // skip current hat

        for (int person : hatToPeople[hat]) {
            if ((mask & (1 << person)) == 0) {
                ans += dfs(hat + 1, mask | (1 << person));
                if (ans >= MOD) ans -= MOD;
            }
        }

        memo[hat][mask] = (int) (ans % MOD);
        return memo[hat][mask];
    }
}
```

## Python

```python
class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(hats)
        full_mask = (1 << n) - 1

        # map each hat to list of people who like it
        hat_to_people = [[] for _ in range(41)]  # hats are 1-indexed up to 40
        for person, pref in enumerate(hats):
            for h in pref:
                hat_to_people[h].append(person)

        from functools import lru_cache

        @lru_cache(None)
        def dp(hat, mask):
            if mask == full_mask:
                return 1
            if hat > 40:
                return 0
            # skip current hat
            ans = dp(hat + 1, mask)
            # try assigning this hat to an eligible person
            for p in hat_to_people[hat]:
                if not (mask & (1 << p)):
                    ans += dp(hat + 1, mask | (1 << p))
                    if ans >= MOD:
                        ans -= MOD
            return ans % MOD

        return dp(1, 0)
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        full_mask = (1 << n) - 1

        hat_to_people = [[] for _ in range(41)]
        for person, pref in enumerate(hats):
            for h in pref:
                hat_to_people[h].append(person)

        @lru_cache(None)
        def dp(hat: int, mask: int) -> int:
            if mask == full_mask:
                return 1
            if hat > 40:
                return 0

            ans = dp(hat + 1, mask)  # skip this hat
            for p in hat_to_people[hat]:
                if not (mask >> p) & 1:
                    ans += dp(hat + 1, mask | (1 << p))
            return ans % MOD

        return dp(1, 0)
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MOD 1000000007
#define MAX_HAT 40
#define MAX_N   10
#define MAX_MASK (1<<MAX_N)

static int n;
static int fullMask;
static int hatPeople[MAX_HAT + 1][MAX_N];
static int hatCnt[MAX_HAT + 1];
static long long memo[MAX_HAT + 2][MAX_MASK];

static long long dfs(int hat, int mask) {
    if (mask == fullMask) return 1;
    if (hat > MAX_HAT) return 0;
    long long *res = &memo[hat][mask];
    if (*res != -1) return *res;

    long long ans = dfs(hat + 1, mask); // skip current hat
    for (int i = 0; i < hatCnt[hat]; ++i) {
        int person = hatPeople[hat][i];
        if (!(mask & (1 << person))) {
            ans += dfs(hat + 1, mask | (1 << person));
            if (ans >= MOD) ans %= MOD;
        }
    }
    *res = ans % MOD;
    return *res;
}

int numberWays(int** hats, int hatsSize, int* hatsColSize){
    n = hatsSize;
    fullMask = (1 << n) - 1;

    // initialize hat mappings
    memset(hatCnt, 0, sizeof(hatCnt));
    for (int person = 0; person < n; ++person) {
        int len = hatsColSize[person];
        for (int j = 0; j < len; ++j) {
            int h = hats[person][j]; // hat id
            if (h >= 1 && h <= MAX_HAT) {
                hatPeople[h][hatCnt[h]++] = person;
            }
        }
    }

    // initialize memo with -1
    for (int i = 0; i <= MAX_HAT + 1; ++i)
        for (int m = 0; m < (1 << n); ++m)
            memo[i][m] = -1;

    return (int)dfs(1, 0);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    
    public int NumberWays(IList<IList<int>> hats) {
        int n = hats.Count;
        int fullMask = (1 << n) - 1;
        // Map each hat to list of people who like it
        List<int>[] hatToPeople = new List<int>[41 + 1];
        for (int i = 0; i <= 41; i++) hatToPeople[i] = new List<int>();
        
        for (int person = 0; person < n; person++) {
            foreach (int h in hats[person]) {
                if (h >= 1 && h <= 40) {
                    hatToPeople[h].Add(person);
                }
            }
        }
        
        int maxMask = 1 << n;
        int[,] memo = new int[42, maxMask];
        for (int i = 0; i < 42; i++) {
            for (int j = 0; j < maxMask; j++) {
                memo[i, j] = -1;
            }
        }
        
        int Dfs(int hat, int mask) {
            if (mask == fullMask) return 1;
            if (hat > 40) return 0;
            if (memo[hat, mask] != -1) return memo[hat, mask];
            
            long ways = Dfs(hat + 1, mask); // skip this hat
            foreach (int person in hatToPeople[hat]) {
                if ((mask & (1 << person)) == 0) {
                    ways += Dfs(hat + 1, mask | (1 << person));
                    if (ways >= MOD) ways %= MOD;
                }
            }
            memo[hat, mask] = (int)(ways % MOD);
            return memo[hat, mask];
        }
        
        return Dfs(1, 0);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} hats
 * @return {number}
 */
var numberWays = function(hats) {
    const MOD = 1000000007;
    const n = hats.length;
    const fullMask = (1 << n) - 1;

    // map each hat to list of people who like it
    const hatToPeople = Array.from({ length: 41 + 1 }, () => []);
    for (let person = 0; person < n; person++) {
        for (const h of hats[person]) {
            hatToPeople[h].push(person);
        }
    }

    // memo[hat][mask] = number of ways
    const memo = Array.from({ length: 42 }, () => Array(1 << n).fill(-1));

    function dfs(hat, mask) {
        if (mask === fullMask) return 1;
        if (hat > 40) return 0;
        const cached = memo[hat][mask];
        if (cached !== -1) return cached;

        let ans = dfs(hat + 1, mask);
        for (const person of hatToPeople[hat]) {
            if ((mask & (1 << person)) === 0) {
                ans += dfs(hat + 1, mask | (1 << person));
                if (ans >= MOD) ans -= MOD;
            }
        }
        ans %= MOD;
        memo[hat][mask] = ans;
        return ans;
    }

    return dfs(1, 0);
};
```

## Typescript

```typescript
function numberWays(hats: number[][]): number {
    const MOD = 1000000007;
    const n = hats.length;
    const fullMask = (1 << n) - 1;

    // Map each hat to the list of people who like it
    const hatPeople: number[][] = Array.from({ length: 41 }, () => []);
    for (let person = 0; person < n; person++) {
        for (const h of hats[person]) {
            if (h >= 1 && h <= 40) {
                hatPeople[h].push(person);
            }
        }
    }

    // memo[hat][mask] = number of ways
    const memo: number[][] = Array.from({ length: 42 }, () => new Array(fullMask + 1).fill(-1));

    function dfs(hat: number, mask: number): number {
        if (mask === fullMask) return 1;
        if (hat > 40) return 0;

        const cached = memo[hat][mask];
        if (cached !== -1) return cached;

        let ans = dfs(hat + 1, mask);
        for (const person of hatPeople[hat]) {
            if ((mask & (1 << person)) === 0) {
                ans += dfs(hat + 1, mask | (1 << person));
                if (ans >= MOD) ans -= MOD;
            }
        }
        ans %= MOD;
        memo[hat][mask] = ans;
        return ans;
    }

    return dfs(1, 0);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $hats
     * @return Integer
     */
    function numberWays($hats) {
        $n = count($hats);
        $done = (1 << $n) - 1;
        $MOD = 1000000007;

        // map each hat to list of people who like it
        $hatToPeople = array_fill(0, 41, []);
        for ($person = 0; $person < $n; $person++) {
            foreach ($hats[$person] as $hat) {
                $hatToPeople[$hat][] = $person;
            }
        }

        $memo = [];

        $dp = function($hat, $mask) use (&$dp, &$hatToPeople, $n, $done, $MOD, &$memo) {
            if ($mask === $done) {
                return 1;
            }
            if ($hat > 40) {
                return 0;
            }
            $key = $hat . '|' . $mask;
            if (isset($memo[$key])) {
                return $memo[$key];
            }

            // option: skip current hat
            $ans = $dp($hat + 1, $mask);

            // try assigning current hat to each eligible person
            foreach ($hatToPeople[$hat] as $person) {
                if ((($mask >> $person) & 1) === 0) {
                    $newMask = $mask | (1 << $person);
                    $ans += $dp($hat + 1, $newMask);
                    if ($ans >= $MOD) {
                        $ans -= $MOD;
                    }
                }
            }

            $ans %= $MOD;
            $memo[$key] = $ans;
            return $ans;
        };

        return $dp(1, 0);
    }
}
```

## Swift

```swift
class Solution {
    func numberWays(_ hats: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let n = hats.count
        let fullMask = (1 << n) - 1
        
        var hatToPeople = Array(repeating: [Int](), count: 41 + 1)
        for (person, list) in hats.enumerated() {
            for h in list where h >= 1 && h <= 40 {
                hatToPeople[h].append(person)
            }
        }
        
        var memo = Array(repeating: Array(repeating: -1, count: 1 << n), count: 41 + 2)
        
        func dfs(_ hat: Int, _ mask: Int) -> Int {
            if mask == fullMask { return 1 }
            if hat > 40 { return 0 }
            if memo[hat][mask] != -1 { return memo[hat][mask] }
            
            var ans = dfs(hat + 1, mask)
            for person in hatToPeople[hat] {
                if (mask & (1 << person)) == 0 {
                    ans += dfs(hat + 1, mask | (1 << person))
                    if ans >= MOD { ans -= MOD }
                }
            }
            ans %= MOD
            memo[hat][mask] = ans
            return ans
        }
        
        return dfs(1, 0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    fun numberWays(hats: List<List<Int>>): Int {
        val n = hats.size
        val fullMask = (1 shl n) - 1
        val hatToPeople = Array(41) { mutableListOf<Int>() }
        for (i in 0 until n) {
            for (h in hats[i]) {
                if (h in 1..40) {
                    hatToPeople[h].add(i)
                }
            }
        }
        val memo = Array(41) { LongArray(1 shl n) { -1L } }

        fun dfs(hat: Int, mask: Int): Long {
            if (mask == fullMask) return 1L
            if (hat > 40) return 0L
            val cached = memo[hat][mask]
            if (cached != -1L) return cached
            var ans = dfs(hat + 1, mask)
            for (person in hatToPeople[hat]) {
                if ((mask and (1 shl person)) == 0) {
                    ans += dfs(hat + 1, mask or (1 shl person))
                    if (ans >= MOD) ans -= MOD
                }
            }
            val res = ans % MOD
            memo[hat][mask] = res
            return res
        }

        return dfs(1, 0).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  late List<List<int>> _hatToPeople;
  late List<List<int>> _memo;
  late int _done;
  late int _n;

  int _dfs(int hat, int mask) {
    if (mask == _done) return 1;
    if (hat > 40) return 0;
    if (_memo[hat][mask] != -1) return _memo[hat][mask];
    int ans = _dfs(hat + 1, mask);
    for (int person in _hatToPeople[hat]) {
      if ((mask & (1 << person)) == 0) {
        ans = (ans + _dfs(hat + 1, mask | (1 << person))) % _MOD;
      }
    }
    _memo[hat][mask] = ans;
    return ans;
  }

  int numberWays(List<List<int>> hats) {
    _n = hats.length;
    _done = (1 << _n) - 1;
    _hatToPeople = List.generate(41, (_) => []);
    for (int i = 0; i < _n; i++) {
      for (int h in hats[i]) {
        if (h >= 1 && h <= 40) {
          _hatToPeople[h].add(i);
        }
      }
    }
    _memo = List.generate(42, (_) => List.filled(1 << _n, -1));
    return _dfs(1, 0);
  }
}
```

## Golang

```go
package main

import "fmt"

const MOD = 1000000007

func numberWays(hats [][]int) int {
	n := len(hats)
	if n == 0 {
		return 1
	}
	doneMask := (1 << n) - 1

	// map each hat to list of people who like it
	hatToPeople := make([][]int, 41+1) // hats are 1..40
	for person, lst := range hats {
		for _, h := range lst {
			if h >= 1 && h <= 40 {
				hatToPeople[h] = append(hatToPeople[h], person)
			}
		}
	}

	// dp[hat][mask] = number of ways
	dp := make([][]int, 42) // up to hat 41 for convenience
	for i := range dp {
		dp[i] = make([]int, 1<<n)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}

	var dfs func(hat int, mask int) int
	dfs = func(hat int, mask int) int {
		if mask == doneMask {
			return 1
		}
		if hat > 40 {
			return 0
		}
		if dp[hat][mask] != -1 {
			return dp[hat][mask]
		}
		ans := dfs(hat+1, mask) // skip current hat
		for _, person := range hatToPeople[hat] {
			if (mask>>person)&1 == 0 {
				ans = (ans + dfs(hat+1, mask|(1<<person))) % MOD
			}
		}
		dp[hat][mask] = ans
		return ans
	}

	return dfs(1, 0)
}

// The following main function is only for local testing and will be ignored by LeetCode.
func main() {
	fmt.Println(numberWays([][]int{{3, 4}, {4, 5}, {5}}))               // 1
	fmt.Println(numberWays([][]int{{3, 5, 1}, {3, 5}}))                // 4
	fmt.Println(numberWays([][]int{{1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}})) // 24
}
```

## Ruby

```ruby
def number_ways(hats)
  mod = 1_000_000_007
  n = hats.length
  full_mask = (1 << n) - 1

  # map each hat to the list of people who like it
  hat_to_people = Array.new(41) { [] }
  hats.each_with_index do |list, person|
    list.each { |h| hat_to_people[h] << person }
  end

  dp = Array.new(42) { Array.new(full_mask + 1, 0) }

  # base case: when all people already have hats
  (1..41).each { |h| dp[h][full_mask] = 1 }

  40.downto(1) do |hat|
    (0..full_mask).each do |mask|
      ways = dp[hat + 1][mask] # skip this hat
      hat_to_people[hat].each do |person|
        if (mask & (1 << person)).zero?
          ways += dp[hat + 1][mask | (1 << person)]
        end
      end
      dp[hat][mask] = ways % mod
    end
  end

  dp[1][0]
end
```

## Scala

```scala
object Solution {
  def numberWays(hats: List[List[Int]]): Int = {
    val MOD = 1000000007
    val n = hats.length
    val fullMask = (1 << n) - 1

    // hat -> people who like it
    val temp = Array.fill(41)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (person <- hats.indices) {
      for (h <- hats(person)) {
        if (h >= 1 && h <= 40) temp(h) += person
      }
    }
    val hatPeople = Array.ofDim[Array[Int]](42)
    for (h <- 1 to 40) hatPeople(h) = temp(h).toArray

    val memo = Array.fill(42, 1 << n)(-1)

    def dp(hat: Int, mask: Int): Int = {
      if (mask == fullMask) return 1
      if (hat > 40) return 0
      var cached = memo(hat)(mask)
      if (cached != -1) return cached

      var ans: Long = dp(hat + 1, mask).toLong // skip this hat
      val arr = hatPeople(hat)
      var i = 0
      while (i < arr.length) {
        val person = arr(i)
        if ((mask & (1 << person)) == 0) {
          ans += dp(hat + 1, mask | (1 << person))
          if (ans >= MOD) ans %= MOD
        }
        i += 1
      }

      cached = (ans % MOD).toInt
      memo(hat)(mask) = cached
      cached
    }

    dp(1, 0)
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

const MOD: i64 = 1_000_000_007;

impl Solution {
    pub fn number_ways(hats: Vec<Vec<i32>>) -> i32 {
        let n = hats.len();
        if n == 0 {
            return 0;
        }
        let done: usize = (1usize << n) - 1;
        // map each hat to list of people who like it
        let mut hat_to_people: Vec<Vec<usize>> = vec![Vec::new(); 42]; // index 1..40
        for (person, pref) in hats.iter().enumerate() {
            for &h in pref {
                let h_usize = h as usize;
                if h_usize <= 40 {
                    hat_to_people[h_usize].push(person);
                }
            }
        }

        // memo[hat][mask] = answer, -1 means uncomputed
        let mut memo: Vec<Vec<i32>> = vec![vec![-1; done + 1]; 42];

        fn dfs(
            hat: usize,
            mask: usize,
            done: usize,
            hat_to_people: &Vec<Vec<usize>>,
            memo: &mut Vec<Vec<i32>>,
        ) -> i32 {
            if mask == done {
                return 1;
            }
            if hat > 40 {
                return 0;
            }
            if memo[hat][mask] != -1 {
                return memo[hat][mask];
            }

            let mut ans: i64 = dfs(hat + 1, mask, done, hat_to_people, memo) as i64;

            for &person in &hat_to_people[hat] {
                if (mask & (1 << person)) == 0 {
                    let new_mask = mask | (1 << person);
                    ans += dfs(hat + 1, new_mask, done, hat_to_people, memo) as i64;
                    if ans >= MOD {
                        ans %= MOD;
                    }
                }
            }

            let res = (ans % MOD) as i32;
            memo[hat][mask] = res;
            res
        }

        dfs(1, 0, done, &hat_to_people, &mut memo)
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (number-ways hats)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length hats))
         (done (sub1 (arithmetic-shift 1 n))) ; 2^n - 1
         (hat-to-people (make-vector 41 '()))) ; index 0 unused

    ;; Build mapping from hat to list of people who like it
    (for ([person (in-range n)]
          [pref   (in-list (list-ref hats person))])
      (let ((h pref))
        (vector-set! hat-to-people h
                     (cons person (vector-ref hat-to-people h)))))

    ;; Memo table: 41 hats × (done+1) masks, initialized to -1 (unknown)
    (define memo
      (let ([v (make-vector 41)])
        (for ([i (in-range 41)])
          (vector-set! v i (make-vector (+ done 1) -1)))
        v))

    (letrec ((dp (lambda (hat mask)
                   (cond
                     [(= mask done) 1]
                     [(> hat 40)   0]
                     [else
                      (define cached (vector-ref (vector-ref memo hat) mask))
                      (if (not (= cached -1))
                          cached
                          (let* ((skip    (dp (+ hat 1) mask))
                                 (people  (vector-ref hat-to-people hat))
                                 (ans
                                  (let loop ((lst people) (acc skip))
                                    (if (null? lst)
                                        acc
                                        (let ((p (car lst)))
                                          (if (= 0 (bitwise-and mask (arithmetic-shift 1 p)))
                                              (loop (cdr lst)
                                                    (modulo (+ acc (dp (+ hat 1)
                                                                       (bitwise-ior mask (arithmetic-shift 1 p))))
                                                            MOD))
                                              (loop (cdr lst) acc)))))))
                            (vector-set! (vector-ref memo hat) mask ans)
                            ans))]))))
      (dp 1 0))))
```

## Erlang

```erlang
-module(solution).
-export([number_ways/1]).
-define(MOD, 1000000007).

-spec number_ways(Hats :: [[integer()]]) -> integer().
number_ways(Hats) ->
    N = length(Hats),
    Done = (1 bsl N) - 1,
    HatsToPeople = build_hats_to_people(Hats, 0, #{}),
    Masks = lists:seq(0, Done),
    InitialMap = #{Done => 1},
    FinalMap = iterate_hats(40, InitialMap, Masks, HatsToPeople),
    maps:get(0, FinalMap, 0).

build_hats_to_people([], _Idx, Acc) ->
    Acc;
build_hats_to_people([PersonHats | Rest], Idx, Acc) ->
    NewAcc = lists:foldl(
        fun(Hat, M) ->
            maps:update_with(
                Hat,
                fun(L) -> [Idx | L] end,
                [Idx],
                M)
        end,
        Acc,
        PersonHats),
    build_hats_to_people(Rest, Idx + 1, NewAcc).

iterate_hats(0, Map, _Masks, _HTP) ->
    Map;
iterate_hats(Hat, NextMap, Masks, HTP) ->
    CurrMap = maps:from_list(
        [ {Mask, compute_ans(Hat, Mask, NextMap, HTP)} || Mask <- Masks ]),
    iterate_hats(Hat - 1, CurrMap, Masks, HTP).

compute_ans(Hat, Mask, NextMap, HTP) ->
    Skip = maps:get(Mask, NextMap, 0),
    Persons = maps:get(Hat, HTP, []),
    lists:foldl(
        fun(Person, Acc) ->
            case (Mask band (1 bsl Person)) of
                0 ->
                    NewMask = Mask bor (1 bsl Person),
                    (Acc + maps:get(NewMask, NextMap, 0)) rem ?MOD;
                _ -> Acc
            end
        end,
        Skip,
        Persons).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @moduledoc false

  @spec number_ways(hats :: [[integer]]) :: integer
  def number_ways(hats) do
    n = length(hats)
    done = (1 <<< n) - 1
    mod = 1_000_000_007
    size = done + 1

    # map each hat to list of people who like it
    hats_to_people =
      Enum.reduce(Enum.with_index(hats), %{}, fn {list, person}, acc ->
        Enum.reduce(list, acc, fn hat, a ->
          Map.update(a, hat, [person], &[person | &1])
        end)
      end)

    # dp for hat index 41 (beyond last): only mask == done has value 1
    next_dp =
      :array.from_list(
        Enum.map(0..done, fn i -> if i == done, do: 1, else: 0 end)
      )

    final_dp =
      Enum.reduce(Enum.reverse(1..40), next_dp, fn hat, dp_next ->
        cur = :array.new(size, default: 0)
        people = Map.get(hats_to_people, hat, [])

        cur_filled =
          Enum.reduce(0..done, cur, fn mask, acc_arr ->
            skip = :array.get(mask, dp_next)

            ans =
              Enum.reduce(people, skip, fn person, a ->
                if (mask &&& (1 <<< person)) == 0 do
                  new_mask = mask ||| (1 <<< person)
                  add = :array.get(new_mask, dp_next)
                  sum = a + add
                  if sum >= mod, do: sum - mod, else: sum
                else
                  a
                end
              end)

            :array.set(mask, ans, acc_arr)
          end)

        cur_filled
      end)

    :array.get(0, final_dp) |> rem(mod)
  end
end
```
