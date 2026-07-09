# 3404. Count Special Subsequences

## Cpp

```cpp
class Solution {
public:
    long long numberOfSubsequences(vector<int>& nums) {
        int n = nums.size();
        unordered_map<unsigned long long, int> leftCount;
        long long ans = 0;
        for (int r = 2; r <= n - 2; ++r) {
            int q = r - 1;
            // add all pairs (p, q) where p < q
            for (int p = 0; p < q; ++p) {
                int a = nums[p];
                int b = nums[q];
                int g = std::gcd(a, b);
                a /= g;
                b /= g;
                unsigned long long key = ((unsigned long long)a << 32) | (unsigned int)b;
                ++leftCount[key];
            }
            // match with pairs (r, s)
            for (int s = r + 1; s < n; ++s) {
                int a = nums[s];
                int b = nums[r];
                int g = std::gcd(a, b);
                a /= g;
                b /= g;
                unsigned long long key = ((unsigned long long)a << 32) | (unsigned int)b;
                auto it = leftCount.find(key);
                if (it != leftCount.end()) ans += it->second;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long numberOfSubsequences(int[] nums) {
        int n = nums.length;
        java.util.Map<Long, Integer> cnt = new java.util.HashMap<>();
        long ans = 0L;
        for (int q = n - 3; q >= 1; --q) {
            int r = q + 1;
            // add all pairs (r, s) where s > r
            for (int s = r + 1; s < n; ++s) {
                long key = encode(nums[s], nums[r]);
                cnt.put(key, cnt.getOrDefault(key, 0) + 1);
            }
            // count matching pairs for all p < q
            for (int p = 0; p < q; ++p) {
                long key = encode(nums[p], nums[q]);
                ans += cnt.getOrDefault(key, 0);
            }
        }
        return ans;
    }

    private long encode(int num, int den) {
        int g = gcd(num, den);
        int a = num / g;
        int b = den / g;
        return ((long) a << 32) | (b & 0xffffffffL);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
import math, bisect
from collections import defaultdict

class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # map ratio (num, den) -> list of r indices where nums[s]/nums[r] == ratio
        ratio_to_rlist = defaultdict(list)

        for r in range(n):
            nr = nums[r]
            for s in range(r + 1, n):
                g = math.gcd(nums[s], nr)
                key = (nums[s] // g, nr // g)
                ratio_to_rlist[key].append(r)   # store denominator index

        total = 0
        for q in range(1, n - 2):
            nq = nums[q]
            for p in range(q):
                g = math.gcd(nums[p], nq)
                key = (nums[p] // g, nq // g)
                lst = ratio_to_rlist.get(key)
                if lst:
                    # count r > q
                    idx = bisect.bisect_right(lst, q)
                    total += len(lst) - idx

        return total
```

## Python3

```python
from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        left_counts = defaultdict(int)
        ans = 0
        for r in range(2, n - 1):
            q = r - 1
            # add all (p, q) pairs where p < q
            for p in range(q):
                a, b = nums[p], nums[q]
                g = gcd(a, b)
                key = (a // g, b // g)
                left_counts[key] += 1
            # count matching (r, s) pairs
            for s in range(r + 1, n):
                a, b = nums[s], nums[r]
                g = gcd(a, b)
                key = (a // g, b // g)
                ans += left_counts.get(key, 0)
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

long long numberOfSubsequences(int* nums, int numsSize) {
    int n = numsSize;
    const int MOD_VAL = 1001; // since values after reduction are <=1000
    vector<unordered_map<int,int>> rightMaps(n);
    
    // Build right maps: for each i, count ratios nums[s]/nums[i] with s>i
    for (int i = n - 1; i >= 0; --i) {
        for (int s = i + 1; s < n; ++s) {
            int a = nums[s];
            int b = nums[i];
            int g = gcd_int(a, b);
            a /= g;
            b /= g;
            int key = a * MOD_VAL + b;
            ++rightMaps[i][key];
        }
    }
    
    long long ans = 0;
    unordered_map<int,long long> pref; // cumulative left counts for processed indices
    
    for (int i = 0; i < n; ++i) {
        // Use current right map with all earlier left contributions
        for (const auto& kv : rightMaps[i]) {
            auto it = pref.find(kv.first);
            if (it != pref.end()) {
                ans += it->second * (long long)kv.second;
            }
        }
        // Compute left counts for index i and add to prefix map
        unordered_map<int,int> leftMap;
        for (int p = 0; p < i; ++p) {
            int a = nums[p];
            int b = nums[i];
            int g = gcd_int(a, b);
            a /= g;
            b /= g;
            int key = a * MOD_VAL + b;
            ++leftMap[key];
        }
        for (const auto& kv : leftMap) {
            pref[kv.first] += kv.second;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long NumberOfSubsequences(int[] nums) {
        int n = nums.Length;
        // Map for all (r,s) pairs where r > current q
        var rightMap = new Dictionary<(int, int), int>();
        // Initialize with all pairs where r >= 2
        for (int r = 2; r <= n - 2; r++) {
            for (int s = r + 1; s < n; s++) {
                var key = Reduce(nums[s], nums[r]);
                if (rightMap.TryGetValue(key, out int cnt))
                    rightMap[key] = cnt + 1;
                else
                    rightMap[key] = 1;
            }
        }

        long ans = 0L;

        // Iterate q from 1 to n-3
        for (int q = 1; q <= n - 3; q++) {
            // Count contributions with current q
            for (int p = 0; p < q; p++) {
                var key = Reduce(nums[p], nums[q]);
                if (rightMap.TryGetValue(key, out int cnt))
                    ans += cnt;
            }

            // Remove pairs where r == q+1 from rightMap for next iteration
            int rRemove = q + 1;
            for (int s = rRemove + 1; s < n; s++) {
                var key = Reduce(nums[s], nums[rRemove]);
                if (rightMap.TryGetValue(key, out int cnt)) {
                    if (cnt == 1)
                        rightMap.Remove(key);
                    else
                        rightMap[key] = cnt - 1;
                }
            }
        }

        return ans;
    }

    private static (int, int) Reduce(int numerator, int denominator) {
        int g = Gcd(numerator, denominator);
        return (numerator / g, denominator / g);
    }

    private static int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfSubsequences = function(nums) {
    const n = nums.length;
    const left = [];
    const right = [];

    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    // generate all (p,q) pairs where p < q
    for (let q = 1; q < n - 1; ++q) {
        for (let p = 0; p < q; ++p) {
            let a = nums[p];
            let b = nums[q];
            const g = gcd(a, b);
            a /= g;
            b /= g;
            left.push({ key: a + '#' + b, idx: q });
        }
    }

    // generate all (r,s) pairs where r < s
    for (let r = 0; r < n - 1; ++r) {
        for (let s = r + 1; s < n; ++s) {
            let a = nums[s];
            let b = nums[r];
            const g = gcd(a, b);
            a /= g;
            b /= g;
            right.push({ key: a + '#' + b, idx: r });
        }
    }

    left.sort((a, b) => a.idx - b.idx);
    right.sort((a, b) => a.idx - b.idx);

    const cntMap = new Map();
    let i = 0;
    let ans = 0;

    for (const rp of right) {
        while (i < left.length && left[i].idx < rp.idx) {
            const k = left[i].key;
            cntMap.set(k, (cntMap.get(k) || 0) + 1);
            i++;
        }
        ans += cntMap.get(rp.key) || 0;
    }

    return ans;
};
```

## Typescript

```typescript
function numberOfSubsequences(nums: number[]): number {
    const n = nums.length;
    // helper GCD
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    // suffixMaps[r] stores counts of reduced fractions nums[s]/nums[r] for all s > r
    const suffixMaps: Map<string, number>[] = new Array(n);
    for (let r = 0; r < n - 1; ++r) {
        const map = new Map<string, number>();
        const denom = nums[r];
        for (let s = r + 1; s < n; ++s) {
            const num = nums[s];
            const g = gcd(num, denom);
            const key = `${num / g}/${denom / g}`;
            map.set(key, (map.get(key) ?? 0) + 1);
        }
        suffixMaps[r] = map;
    }

    let ans = 0;
    const leftMap = new Map<string, number>();

    // iterate r from right to left, expanding left pairs as q = r-1 becomes allowed
    for (let r = n - 2; r >= 2; --r) {
        const q = r - 1;
        const denomQ = nums[q];
        for (let p = 0; p < q; ++p) {
            const numP = nums[p];
            const g = gcd(numP, denomQ);
            const key = `${numP / g}/${denomQ / g}`;
            leftMap.set(key, (leftMap.get(key) ?? 0) + 1);
        }

        const rightMap = suffixMaps[r];
        for (const [key, cntR] of rightMap.entries()) {
            const cntL = leftMap.get(key) ?? 0;
            ans += cntL * cntR;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    private function gcd(int $a, int $b): int {
        while ($b !== 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    public function numberOfSubsequences(array $nums): int {
        $n = count($nums);
        if ($n < 4) return 0;

        // Precompute keys for all pairs (p, q) where p < q, grouped by second index q
        $bySecond = array_fill(0, $n, []);
        for ($q = 1; $q <= $n - 2; $q++) {
            $list = [];
            for ($p = 0; $p < $q; $p++) {
                $g = $this->gcd($nums[$p], $nums[$q]);
                $key = intdiv($nums[$p], $g) . '/' . intdiv($nums[$q], $g);
                $list[] = $key;
            }
            $bySecond[$q] = $list;
        }

        $cntKey = []; // counts of left-side ratios whose second index is less than current r
        $ans = 0;

        for ($r = 1; $r <= $n - 2; $r++) {
            // Count matching right-side pairs (r, s) with s > r
            for ($s = $r + 1; $s < $n; $s++) {
                $g = $this->gcd($nums[$s], $nums[$r]);
                $key = intdiv($nums[$s], $g) . '/' . intdiv($nums[$r], $g);
                if (isset($cntKey[$key])) {
                    $ans += $cntKey[$key];
                }
            }

            // Add left-side pairs ending at index r to cntKey for future iterations
            foreach ($bySecond[$r] as $k) {
                if (isset($cntKey[$k])) {
                    $cntKey[$k]++;
                } else {
                    $cntKey[$k] = 1;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    struct Pair: Hashable {
        let num: Int
        let den: Int
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
    
    func numberOfSubsequences(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 4 { return 0 }
        var leftCounts = [Pair: Int]()
        var result: Int64 = 0
        
        // r will be the third index in the quadruple (p,q,r,s)
        for r in 2..<(n - 1) {
            let q = r - 1
            // add all pairs (p, q) where p < q
            for p in 0..<q {
                let a = nums[p]
                let b = nums[q]
                let g = gcd(a, b)
                let key = Pair(num: a / g, den: b / g)
                leftCounts[key, default: 0] += 1
            }
            
            // for each s > r, count matching (p,q) pairs
            for s in (r + 1)..<n {
                let c = nums[s]
                let d = nums[r]
                let g2 = gcd(c, d)
                let key2 = Pair(num: c / g2, den: d / g2)
                if let cnt = leftCounts[key2] {
                    result += Int64(cnt)
                }
            }
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSubsequences(nums: IntArray): Long {
        val n = nums.size
        var ans = 0L
        val leftMap = HashMap<Pair<Int, Int>, Int>()
        for (r in 2 until n - 1) {
            // add all pairs (p, q) where q == r-1
            val q = r - 1
            for (p in 0 until q) {
                val key = normalize(nums[p], nums[q])
                leftMap[key] = (leftMap[key] ?: 0) + 1
            }
            // count matching right pairs (r, s)
            for (s in r + 1 until n) {
                val key = normalize(nums[s], nums[r])
                ans += (leftMap[key] ?: 0).toLong()
            }
        }
        return ans
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }

    private fun normalize(num: Int, den: Int): Pair<Int, Int> {
        val g = gcd(num, den)
        return Pair(num / g, den / g)
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSubsequences(List<int> nums) {
    int n = nums.length;

    int gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a;
    }

    Map<String, int> cnt = {};

    // initial pairs with left index n-2
    if (n >= 2) {
      for (int s = n - 1; s > n - 2; --s) {
        int num = nums[s];
        int den = nums[n - 2];
        int g = gcd(num, den);
        num ~/= g;
        den ~/= g;
        String key = '$num/$den';
        cnt[key] = (cnt[key] ?? 0) + 1;
      }
    }

    int ans = 0;

    for (int q = n - 3; q >= 1; --q) {
      // count contributions from (p, q)
      for (int p = 0; p < q; ++p) {
        int num = nums[p];
        int den = nums[q];
        int g = gcd(num, den);
        num ~/= g;
        den ~/= g;
        String key = '$num/$den';
        ans += cnt[key] ?? 0;
      }

      // add pairs where left index = q
      for (int s = q + 1; s < n; ++s) {
        int num = nums[s];
        int den = nums[q];
        int g = gcd(num, den);
        num ~/= g;
        den ~/= g;
        String key = '$num/$den';
        cnt[key] = (cnt[key] ?? 0) + 1;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func numberOfSubsequences(nums []int) int64 {
	type frac struct{ num, den int }
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		if a < 0 {
			return -a
		}
		return a
	}
	reduce := func(num, den int) (int, int) {
		g := gcd(num, den)
		return num / g, den / g
	}

	n := len(nums)
	cnt := make(map[frac]int64)
	var ans int64

	for r := 2; r <= n-2; r++ {
		q := r - 1
		// add all (p,q) pairs where p < q
		for p := 0; p < q; p++ {
			num, den := reduce(nums[p], nums[q])
			cnt[frac{num, den}]++
		}
		// count matching (r,s) pairs
		for s := r + 1; s < n; s++ {
			num, den := reduce(nums[s], nums[r])
			if v, ok := cnt[frac{num, den}]; ok {
				ans += v
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def number_of_subsequences(nums)
  n = nums.length
  ratio_map = Hash.new { |h, k| h[k] = [] }

  (0...n - 1).each do |r|
    (r + 1...n).each do |s|
      a = nums[s]
      b = nums[r]
      g = a.gcd(b)
      key = [(a / g), (b / g)]
      ratio_map[key] << r
    end
  end

  ans = 0
  (1...n - 2).each do |q|
    (0...q).each do |p|
      a = nums[p]
      b = nums[q]
      g = a.gcd(b)
      key = [(a / g), (b / g)]
      list = ratio_map[key]
      next if list.empty?
      idx = list.bsearch_index { |x| x > q }
      ans += list.length - idx if idx
    end
  end

  ans
end
```

## Scala

```scala
import scala.collection.mutable
object Solution {
  def numberOfSubsequences(nums: Array[Int]): Long = {
    val n = nums.length
    def gcd(a: Int, b: Int): Int = {
      var x = a
      var y = b
      while (y != 0) {
        val tmp = x % y
        x = y
        y = tmp
      }
      math.abs(x)
    }

    // Right side map: ratios for pairs (r, s) where r >= 1
    val rightMap = mutable.HashMap[(Int, Int), Int]().withDefaultValue(0)
    for (r <- 1 until n - 1) {
      val nr = nums(r)
      var s = r + 1
      while (s < n) {
        val ns = nums(s)
        val g = gcd(ns, nr)
        val key = (ns / g, nr / g)
        rightMap(key) = rightMap(key) + 1
        s += 1
      }
    }

    val leftMap = mutable.HashMap[(Int, Int), Int]().withDefaultValue(0)
    var ans: Long = 0L

    // k is the index of q (second element of left pair)
    for (k <- 0 until n - 2) {
      // add pairs (p, k) where p < k
      var p = 0
      while (p < k) {
        val g = gcd(nums(p), nums(k))
        val key = (nums(p) / g, nums(k) / g)
        leftMap(key) = leftMap(key) + 1
        p += 1
      }

      // count matches with right side
      for ((key, cntL) <- leftMap) {
        val cntR = rightMap.getOrElse(key, 0)
        ans += cntL.toLong * cntR
      }

      // remove pairs where r == k + 1 from rightMap for next iteration
      val rRemove = k + 1
      if (rRemove < n - 1) {
        var s = rRemove + 1
        while (s < n) {
          val g = gcd(nums(s), nums(rRemove))
          val key = (nums(s) / g, nums(rRemove) / g)
          val newVal = rightMap(key) - 1
          if (newVal == 0) rightMap.remove(key)
          else rightMap(key) = newVal
          s += 1
        }
      }
    }

    ans
  }
}
```

## Rust

```rust
use std::collections::HashMap;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a.abs()
}

fn reduce(num: i32, den: i32) -> (i32, i32) {
    let g = gcd(num, den);
    (num / g, den / g)
}

impl Solution {
    pub fn number_of_subsequences(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n < 4 {
            return 0;
        }

        // Precompute right side ratio maps for each r
        let mut right_maps: Vec<HashMap<(i32, i32), i32>> = vec![HashMap::new(); n];
        for r in 0..n {
            let mut map: HashMap<(i32, i32), i32> = HashMap::new();
            for s in (r + 1)..n {
                let ratio = reduce(nums[s], nums[r]);
                *map.entry(ratio).or_insert(0) += 1;
            }
            right_maps[r] = map;
        }

        let mut ans: i64 = 0;

        // Iterate over possible q
        for q in 1..=n - 3 {
            // Build left ratio map for current q
            let mut left_map: HashMap<(i32, i32), i32> = HashMap::new();
            for p in 0..q {
                let ratio = reduce(nums[p], nums[q]);
                *left_map.entry(ratio).or_insert(0) += 1;
            }

            // For each r > q, combine counts
            for r in (q + 1)..=n - 2 {
                let right = &right_maps[r];
                if left_map.len() <= right.len() {
                    for (ratio, cnt_left) in left_map.iter() {
                        if let Some(cnt_right) = right.get(ratio) {
                            ans += (*cnt_left as i64) * (*cnt_right as i64);
                        }
                    }
                } else {
                    for (ratio, cnt_right) in right.iter() {
                        if let Some(cnt_left) = left_map.get(ratio) {
                            ans += (*cnt_left as i64) * (*cnt_right as i64);
                        }
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (number-of-subsequences nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (hash (make-hash)))
    (define (add-left-pair p q)
      (let* ((a (vector-ref arr p))
             (b (vector-ref arr q))
             (g (gcd a b))
             (key (cons (/ a g) (/ b g))))
        (hash-set! hash key (+ 1 (hash-ref hash key 0)))))
    (define ans 0)
    ;; r is the third index of the subsequence
    (for ([r 2 (- n 1)])               ; r = 2 .. n-2
      ;; add all pairs (p, q) with q == r-1
      (let ((q (- r 1)))
        (for ([p 0 q])                 ; p = 0 .. q-1
          (add-left-pair p q)))
      ;; count matching right pairs (r, s)
      (for ([s (+ r 1) n])             ; s = r+1 .. n-1
        (let* ((c (vector-ref arr s))
               (d (vector-ref arr r))
               (g (gcd c d))
               (key (cons (/ c g) (/ d g))))
          (set! ans (+ ans (hash-ref hash key 0))))))
    ans)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_subsequences/1]).

-spec number_of_subsequences(Nums :: [integer()]) -> integer().
number_of_subsequences(Nums) ->
    NumTuple = list_to_tuple(Nums),
    N = tuple_size(NumTuple),

    RightMaps = build_right_maps(NumTuple, N),

    TotalRight0 = lists:foldl(fun(M, Acc) -> merge_maps(Acc, M) end, #{}, RightMaps),

    % remove contributions where r = 0
    TotalRight1 = dec_map(TotalRight0, hd(RightMaps)),

    MaxQ = N - 3,
    loop_q(1, MaxQ, NumTuple, RightMaps, TotalRight1, 0).

%% Build right maps for each index r (0 .. N-2)
build_right_maps(_NumTuple, N) when N < 2 -> [] ;
build_right_maps(NumTuple, N) ->
    build_right_maps(0, N - 2, NumTuple, []).

build_right_maps(R, MaxR, _NumTuple, Acc) when R > MaxR ->
    lists:reverse(Acc);
build_right_maps(R, MaxR, NumTuple, Acc) ->
    Map = build_right_for_r(R, NumTuple, tuple_size(NumTuple)),
    build_right_maps(R + 1, MaxR, NumTuple, [Map | Acc]).

%% Build map of ratios for a fixed r
build_right_for_r(R, NumTuple, N) ->
    Den = element(R + 1, NumTuple),
    build_right_for_s(lists:seq(R + 1, N - 1), Den, NumTuple, #{}).

build_right_for_s([], _Den, _NumTuple, Map) -> Map;
build_right_for_s([S | Rest], Den, NumTuple, Map) ->
    Num = element(S + 1, NumTuple),
    Ratio = reduce(Num, Den),
    NewMap = add_count(Map, Ratio),
    build_right_for_s(Rest, Den, NumTuple, NewMap).

%% Loop over q positions
loop_q(Q, MaxQ, _NumTuple, _RightMaps, _TotalRight, Acc) when Q > MaxQ ->
    Acc;
loop_q(Q, MaxQ, NumTuple, RightMaps, TotalRight, Acc) ->
    % remove right map for r = Q
    RightMapQ = lists:nth(Q + 1, RightMaps),
    NewTotalRight = dec_map(TotalRight, RightMapQ),

    LeftMap = build_left_for_q(Q, NumTuple),

    Contribution = maps:fold(
        fun(Key, CntL, Sum) ->
            CntR = maps:get(Key, NewTotalRight, 0),
            Sum + CntL * CntR
        end,
        0,
        LeftMap),

    loop_q(Q + 1, MaxQ, NumTuple, RightMaps, NewTotalRight, Acc + Contribution).

%% Build left map for a fixed q
build_left_for_q(Q, NumTuple) ->
    Den = element(Q + 1, NumTuple),
    build_left_for_p(lists:seq(0, Q - 1), Den, NumTuple, #{}).

build_left_for_p([], _Den, _NumTuple, Map) -> Map;
build_left_for_p([P | Rest], Den, NumTuple, Map) ->
    Num = element(P + 1, NumTuple),
    Ratio = reduce(Num, Den),
    NewMap = add_count(Map, Ratio),
    build_left_for_p(Rest, Den, NumTuple, NewMap).

%% Helper to add count in map
add_count(Map, Key) ->
    Count = maps:get(Key, Map, 0) + 1,
    maps:put(Key, Count, Map).

%% Merge two maps by adding counts
merge_maps(Total, Sub) ->
    maps:fold(
        fun(Key, Val, Acc) ->
            NewVal = maps:get(Key, Acc, 0) + Val,
            maps:put(Key, NewVal, Acc)
        end,
        Total,
        Sub).

%% Subtract sub map from total map
dec_map(Total, Sub) ->
    maps:fold(
        fun(Key, ValSub, Acc) ->
            Curr = maps:get(Key, Acc, 0),
            NewVal = Curr - ValSub,
            case NewVal of
                0 -> maps:remove(Key, Acc);
                _ -> maps:put(Key, NewVal, Acc)
            end
        end,
        Total,
        Sub).

%% Reduce fraction to its simplest form as a tuple {Num, Den}
reduce(Num, Den) ->
    G = gcd(Num, Den),
    {Num div G, Den div G}.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_subsequences(nums :: [integer]) :: integer
  def number_of_subsequences(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)

    {ans, _} =
      Enum.reduce((n - 2)..1, {0, %{}}, fn q, {acc_ans, ratio_map} ->
        r = q + 1

        # add all (r, s) pairs where s > r
        ratio_map =
          Enum.reduce((r + 1)..(n - 1), ratio_map, fn s, m ->
            a = elem(arr, s)
            b = elem(arr, r)

            g = Integer.gcd(a, b)
            key = {div(a, g), div(b, g)}
            Map.update(m, key, 1, &(&1 + 1))
          end)

        # count matching (p, q) pairs
        acc_ans =
          Enum.reduce(0..(q - 1), acc_ans, fn p, a_acc ->
            a = elem(arr, p)
            b = elem(arr, q)

            g = Integer.gcd(a, b)
            key = {div(a, g), div(b, g)}
            cnt = Map.get(ratio_map, key, 0)
            a_acc + cnt
          end)

        {acc_ans, ratio_map}
      end)

    ans
  end
end
```
