# 3623. Count Number of Trapezoids I

## Cpp

```cpp
class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        const long long MOD = 1000000007LL;
        unordered_map<long long, long long> cnt;
        cnt.reserve(points.size()*2);
        for (auto& p : points) {
            cnt[p[1]]++;
        }
        vector<long long> combs;
        combs.reserve(cnt.size());
        for (auto& kv : cnt) {
            long long c = kv.second;
            if (c >= 2) {
                long long ways = (c * (c - 1) / 2) % MOD;
                combs.push_back(ways);
            }
        }
        long long ans = 0, prefix = 0;
        for (long long v : combs) {
            ans = (ans + v * prefix) % MOD;
            prefix = (prefix + v) % MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long INV2 = 500000004L; // modular inverse of 2 mod MOD

    public int countTrapezoids(int[][] points) {
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        for (int[] p : points) {
            map.merge(p[1], 1, Integer::sum);
        }

        long sumA = 0;
        long sumSq = 0;
        for (int cnt : map.values()) {
            if (cnt >= 2) {
                long a = ((long) cnt * (cnt - 1) / 2) % MOD; // C(cnt,2)
                sumA = (sumA + a) % MOD;
                sumSq = (sumSq + a * a % MOD) % MOD;
            }
        }

        long result = ( (sumA * sumA) % MOD - sumSq + MOD ) % MOD;
        result = (result * INV2) % MOD;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        inv2 = (MOD + 1) // 2  # modular inverse of 2
        
        cnt_by_y = {}
        for x, y in points:
            cnt_by_y[y] = cnt_by_y.get(y, 0) + 1
        
        total_a = 0          # sum of C(cnt,2) over all y
        sum_sq = 0           # sum of (C(cnt,2))^2 over all y
        
        for cnt in cnt_by_y.values():
            if cnt >= 2:
                a = cnt * (cnt - 1) // 2
                a_mod = a % MOD
                total_a = (total_a + a_mod) % MOD
                sum_sq = (sum_sq + a_mod * a_mod) % MOD
        
        ans = ( (total_a * total_a - sum_sq) % MOD ) * inv2 % MOD
        return ans
```

## Python3

```python
class Solution:
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        inv2 = (MOD + 1) // 2

        cnt_by_y = {}
        for x, y in points:
            cnt_by_y[y] = cnt_by_y.get(y, 0) + 1

        total_comb = 0          # sum of C(cnt,2)
        total_comb_sq = 0       # sum of (C(cnt,2))^2
        for cnt in cnt_by_y.values():
            if cnt >= 2:
                comb = cnt * (cnt - 1) // 2
                comb_mod = comb % MOD
                total_comb = (total_comb + comb_mod) % MOD
                total_comb_sq = (total_comb_sq + comb_mod * comb_mod) % MOD

        ans = ( (total_comb * total_comb - total_comb_sq) % MOD ) * inv2 % MOD
        return ans
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

int countTrapezoids(int** points, int pointsSize, int* pointsColSize){
    if (pointsSize < 4) return 0;
    int *ys = (int*)malloc(sizeof(int) * pointsSize);
    for (int i = 0; i < pointsSize; ++i) {
        ys[i] = points[i][1];
    }
    qsort(ys, pointsSize, sizeof(int), cmp_int);

    long long sumPrev = 0;
    long long ans = 0;

    int i = 0;
    while (i < pointsSize) {
        int y = ys[i];
        int cnt = 0;
        while (i < pointsSize && ys[i] == y) {
            ++cnt;
            ++i;
        }
        if (cnt >= 2) {
            long long cur = ((long long)cnt * (cnt - 1) / 2) % MOD;
            ans = (ans + cur * sumPrev) % MOD;
            sumPrev = (sumPrev + cur) % MOD;
        }
    }

    free(ys);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int CountTrapezoids(int[][] points) {
        const long MOD = 1000000007L;
        var yCount = new Dictionary<long, int>();
        foreach (var p in points) {
            long y = p[1];
            if (!yCount.ContainsKey(y)) yCount[y] = 0;
            yCount[y]++;
        }

        List<long> combs = new List<long>();
        foreach (var kv in yCount) {
            long cnt = kv.Value;
            if (cnt >= 2) {
                long c2 = cnt * (cnt - 1) / 2 % MOD;
                combs.Add(c2);
            }
        }

        long sum = 0, sumSq = 0;
        foreach (var v in combs) {
            sum = (sum + v) % MOD;
            sumSq = (sumSq + v * v % MOD) % MOD;
        }

        long inv2 = (MOD + 1) / 2; // modular inverse of 2
        long total = ((sum * sum) % MOD - sumSq + MOD) % MOD;
        total = total * inv2 % MOD;

        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var countTrapezoids = function(points) {
    const MOD = 1000000007n;
    const cntMap = new Map();
    for (const [, y] of points) {
        cntMap.set(y, (cntMap.get(y) || 0) + 1);
    }
    let totalC = 0n;
    let sumSq = 0n;
    for (const cnt of cntMap.values()) {
        if (cnt >= 2) {
            const c = BigInt(cnt) * (BigInt(cnt) - 1n) / 2n; // C(cnt,2)
            totalC = (totalC + c) % MOD;
            sumSq = (sumSq + (c * c) % MOD) % MOD;
        }
    }
    let ans = ((totalC * totalC) % MOD - sumSq) % MOD;
    if (ans < 0) ans += MOD;
    const inv2 = 500000004n; // modular inverse of 2 modulo 1e9+7
    ans = (ans * inv2) % MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function countTrapezoids(points: number[][]): number {
    const MOD = 1000000007n;

    // Group points by y-coordinate
    const yToId = new Map<number, number>();
    const xsPerLine: number[][] = [];
    for (const [x, y] of points) {
        let id = yToId.get(y);
        if (id === undefined) {
            id = xsPerLine.length;
            yToId.set(y, id);
            xsPerLine.push([]);
        }
        xsPerLine[id].push(x);
    }

    const lineCnt = xsPerLine.length;
    const cnt: number[] = new Array(lineCnt);
    const pairCnt: bigint[] = new Array(lineCnt);
    let totalPairsC2 = 0n;          // Σ C(cnt_i,2)
    let sumSquares = 0n;            // Σ C(cnt_i,2)^2

    for (let i = 0; i < lineCnt; ++i) {
        const c = xsPerLine[i].length;
        cnt[i] = c;
        const pc = BigInt(c) * (BigInt(c) - 1n) / 2n;
        pairCnt[i] = pc;
        totalPairsC2 += pc;
        sumSquares += pc * pc;
    }

    // total number of unordered line pairs multiplied by their C(cnt,2)
    let totalTrapezoids = (totalPairsC2 * totalPairsC2 - sumSquares) / 2n % MOD;

    // Build flat list of points with line id
    type Pt = { x: number; id: number };
    const flat: Pt[] = [];
    for (let i = 0; i < lineCnt; ++i) {
        for (const x of xsPerLine[i]) flat.push({ x, id: i });
    }
    flat.sort((a, b) => a.x - b.x);

    // Helper to compute left-disjoint count on an ordered list
    const computeLeft = (arr: Pt[]): bigint => {
        const seenCnt = new Array(lineCnt).fill(0);
        let totalC2Seen = 0n;
        let disjoint = 0n;

        for (let i = 0; i < arr.length;) {
            let j = i;
            while (j < arr.length && arr[j].x === arr[i].x) ++j;

            // contributions before updating counts
            for (let k = i; k < j; ++k) {
                const id = arr[k].id;
                const s = seenCnt[id];
                const rem = cnt[id] - s - 1; // points later in same line
                if (rem <= 0) continue;
                const curC2 = BigInt(s) * (BigInt(s) - 1n) / 2n;
                const diff = totalC2Seen - curC2;
                if (diff > 0n) {
                    disjoint += BigInt(rem) * diff;
                }
            }

            // now update seen counts
            for (let k = i; k < j; ++k) {
                const id = arr[k].id;
                const s = seenCnt[id];
                const curC2 = BigInt(s) * (BigInt(s) - 1n) / 2n;
                totalC2Seen -= curC2;
                seenCnt[id] = s + 1;
                const ns = s + 1;
                const newC2 = BigInt(ns) * (BigInt(ns) - 1n) / 2n;
                totalC2Seen += newC2;
            }

            i = j;
        }
        return disjoint;
    };

    const leftDisjoint = computeLeft(flat);
    const rightDisjoint = computeLeft([...flat].reverse());

    let result = (totalTrapezoids - leftDisjoint - rightDisjoint) % MOD;
    if (result < 0n) result += MOD;
    return Number(result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function countTrapezoids($points) {
        $mod = 1000000007;
        $cnt = [];
        foreach ($points as $p) {
            $y = $p[1];
            if (!isset($cnt[$y])) $cnt[$y] = 0;
            $cnt[$y]++;
        }
        $sum = 0;
        $sumSq = 0;
        foreach ($cnt as $c) {
            if ($c < 2) continue;
            $comb = intdiv($c * ($c - 1), 2) % $mod;
            $sum = ($sum + $comb) % $mod;
            $sumSq = ($sumSq + ($comb * $comb) % $mod) % $mod;
        }
        // answer = (sum^2 - sumSq) / 2 mod MOD
        $ans = ($sum * $sum) % $mod;
        $ans = ($ans - $sumSq + $mod) % $mod;
        // multiply by modular inverse of 2 (which is (MOD+1)/2)
        $inv2 = (int)(($mod + 1) / 2);
        $ans = ($ans * $inv2) % $mod;
        return $ans;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func countTrapezoids(_ points: [[Int]]) -> Int {
        var groups = [Int: [Int]]()
        for p in points {
            let x = p[0]
            let y = p[1]
            groups[y, default: []].append(x)
        }
        
        // Keep only groups with at least 2 points and sort x's
        var groupList: [[Int]] = []
        var c2List: [Int64] = []
        for (_, arr) in groups {
            if arr.count >= 2 {
                let sortedArr = arr.sorted()
                groupList.append(sortedArr)
                let cnt = Int64(sortedArr.count)
                c2List.append(cnt * (cnt - 1) / 2 % Int64(MOD))
            }
        }
        
        let gCount = groupList.count
        var answer: Int64 = 0
        
        for i in 0..<gCount {
            let a = groupList[i]
            let c2a = c2List[i]
            if c2a == 0 { continue }
            for j in (i+1)..<gCount {
                let b = groupList[j]
                let c2b = c2List[j]
                if c2b == 0 { continue }
                
                // total combinations
                var total = (c2a * c2b) % Int64(MOD)
                
                // crossing ABAB
                let crossABAB = crossingCount(outer: a, inner: b)
                // crossing BABA
                let crossBABA = crossingCount(outer: b, inner: a)
                
                var crossing = (crossABAB + crossBABA) % Int64(MOD)
                var nested = total - crossing
                if nested < 0 { nested += Int64(MOD) }
                answer += nested
                if answer >= Int64(MOD) { answer -= Int64(MOD) }
            }
        }
        
        return Int(answer % Int64(MOD))
    }
    
    // counts ABAB patterns where outer array provides the A positions,
    // inner array provides the B positions.
    private func crossingCount(outer: [Int], inner: [Int]) -> Int64 {
        let aCnt = outer.count
        if aCnt < 2 || inner.isEmpty { return 0 }
        let totalB = inner.count
        
        var cntBBeforeA = [Int](repeating: 0, count: aCnt)
        var idxB = 0
        for i in 0..<aCnt {
            while idxB < totalB && inner[idxB] < outer[i] {
                idxB += 1
            }
            cntBBeforeA[i] = idxB   // number of B points with x < A[i]
        }
        
        var prefixSum = [Int64](repeating: 0, count: aCnt)
        var sum: Int64 = 0
        for i in 0..<aCnt {
            sum += Int64(cntBBeforeA[i])
            prefixSum[i] = sum
        }
        
        var result: Int64 = 0
        let totalBInt64 = Int64(totalB)
        if aCnt >= 2 {
            for k in 1..<aCnt {
                let leftCount = Int64(k) * Int64(cntBBeforeA[k-1]) - prefixSum[k-1]
                if leftCount <= 0 { continue }
                let rightB = totalBInt64 - Int64(cntBBeforeA[k])
                let add = (rightB % Int64(MOD)) * (leftCount % Int64(MOD)) % Int64(MOD)
                result += add
                if result >= Int64(MOD) { result -= Int64(MOD) }
            }
        }
        return result % Int64(MOD)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countTrapezoids(points: Array<IntArray>): Int {
        val yCount = HashMap<Int, Long>()
        for (p in points) {
            val y = p[1]
            yCount[y] = (yCount[y] ?: 0L) + 1
        }
        val MOD = 1_000_000_007L
        var sumA = 0L
        var sumSqA = 0L
        for (cnt in yCount.values) {
            if (cnt >= 2) {
                val a = cnt * (cnt - 1) / 2 % MOD
                sumA = (sumA + a) % MOD
                sumSqA = (sumSqA + a * a % MOD) % MOD
            }
        }
        var ans = (sumA * sumA % MOD - sumSqA + MOD) % MOD
        val inv2 = 500_000_004L // modular inverse of 2 modulo 1e9+7
        ans = ans * inv2 % MOD
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  static const int _inv2 = 500000004; // modular inverse of 2 modulo 1e9+7

  int countTrapezoids(List<List<int>> points) {
    final Map<int, int> cnt = {};
    for (var p in points) {
      final int y = p[1];
      cnt[y] = (cnt[y] ?? 0) + 1;
    }

    int sumA = 0;      // Σ C(cnt_i, 2) mod MOD
    int sumASq = 0;    // Σ (C(cnt_i, 2))^2 mod MOD

    for (final c in cnt.values) {
      if (c >= 2) {
        int a = ((c * (c - 1)) ~/ 2) % _mod;
        sumA = (sumA + a) % _mod;
        sumASq = (sumASq + (a * a) % _mod) % _mod;
      }
    }

    // answer = ( (Σa)^2 - Σa^2 ) / 2 mod MOD
    int ans = ((sumA * sumA) % _mod - sumASq) % _mod;
    if (ans < 0) ans += _mod;
    ans = (ans * _inv2) % _mod;

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

const MOD int64 = 1000000007
const INV2 int64 = 500000004 // modular inverse of 2 modulo MOD

func comb(n int) int64 {
	if n < 2 {
		return 0
	}
	return (int64(n) * int64(n-1) / 2) % MOD
}

func countTrapezoids(points [][]int) int {
	// Map y-coordinate to index
	yIdxMap := make(map[int]int)
	var groups [][]int
	for _, p := range points {
		y := p[1]
		if _, ok := yIdxMap[y]; !ok {
			idx := len(groups)
			yIdxMap[y] = idx
			groups = append(groups, []int{})
		}
		idx := yIdxMap[y]
		groups[idx] = append(groups[idx], p[0])
	}

	m := len(groups)
	cnt := make([]int, m)
	for i := 0; i < m; i++ {
		cnt[i] = len(groups[i])
	}

	// Precompute interval counts per line
	a := make([]int64, m)
	var totalIntervalsSum int64 = 0
	var sumSquares int64 = 0
	for i := 0; i < m; i++ {
		a[i] = comb(cnt[i])
		totalIntervalsSum = (totalIntervalsSum + a[i]) % MOD
		sumSquares = (sumSquares + a[i]*a[i]) % MOD
	}

	// totalPairs = sum_{i<j} a_i * a_j
	totalPairs := (totalIntervalsSum*totalIntervalsSum - sumSquares) % MOD
	if totalPairs < 0 {
		totalPairs += MOD
	}
	totalPairs = totalPairs * INV2 % MOD

	// Prepare points with y-index
	type pt struct {
		x int
		y int
	}
	all := make([]pt, len(points))
	for i, p := range points {
		all[i] = pt{x: p[0], y: yIdxMap[p[1]]}
	}
	sort.Slice(all, func(i, j int) bool {
		if all[i].x == all[j].x {
			return all[i].y < all[j].y
		}
		return all[i].x < all[j].x
	})

	remaining := make([]int, m)
	for i := 0; i < m; i++ {
		remaining[i] = cnt[i]
	}
	seen := make([]int, m)

	// suffixSum holds sum of comb(remaining[line]) over all lines
	var suffixSum int64 = totalIntervalsSum

	var disjointTotal int64 = 0
	n := len(all)
	i := 0
	for i < n {
		j := i
		// first remove all points with this x from remaining
		for j < n && all[j].x == all[i].x {
			line := all[j].y
			curRemComb := comb(remaining[line])
			suffixSum = (suffixSum - curRemComb + MOD) % MOD
			remaining[line]--
			newRemComb := comb(remaining[line])
			suffixSum = (suffixSum + newRemComb) % MOD
			j++
		}
		// now compute contributions for this group
		for k := i; k < j; k++ {
			line := all[k].y
			left := seen[line]
			if left == 0 {
				continue
			}
			curRemComb := comb(remaining[line])
			otherSum := (suffixSum - curRemComb + MOD) % MOD
			contrib := int64(left) * otherSum % MOD
			disjointTotal = (disjointTotal + contrib) % MOD
		}
		// finally add these points to seen counts
		for k := i; k < j; k++ {
			line := all[k].y
			seen[line]++
		}
		i = j
	}

	ans := totalPairs - disjointTotal
	if ans < 0 {
		ans += MOD
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def count_trapezoids(points)
  y_counts = Hash.new(0)
  points.each { |x, y| y_counts[y] += 1 }

  combs = []
  y_counts.each_value do |c|
    next if c < 2
    comb = (c * (c - 1) / 2) % MOD
    combs << comb
  end

  ans = 0
  prefix = 0
  combs.each do |v|
    ans = (ans + v * prefix) % MOD
    prefix = (prefix + v) % MOD
  end

  ans
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L
  def countTrapezoids(points: Array[Array[Int]]): Int = {
    import scala.collection.mutable
    val cntByY = mutable.HashMap[Int, Int]()
    for (p <- points) {
      val y = p(1)
      cntByY.put(y, cntByY.getOrElse(y, 0) + 1)
    }
    var sumSoFar = 0L
    var ans = 0L
    for ((_, c) <- cntByY) {
      if (c >= 2) {
        val v = (c.toLong * (c - 1) / 2) % MOD
        ans = (ans + v * sumSoFar) % MOD
        sumSoFar = (sumSoFar + v) % MOD
      }
    }
    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashMap;
        const MOD: i64 = 1_000_000_007;
        const INV2: i64 = 500_000_004; // modular inverse of 2 modulo MOD

        let mut cnt_by_y: HashMap<i32, i64> = HashMap::new();
        for p in points {
            let y = p[1];
            *cnt_by_y.entry(y).or_insert(0) += 1;
        }

        let mut sum_a: i64 = 0;
        let mut sum_sq: i64 = 0;

        for &c in cnt_by_y.values() {
            if c >= 2 {
                let a = (c * (c - 1) / 2) % MOD; // C(c,2)
                sum_a = (sum_a + a) % MOD;
                sum_sq = (sum_sq + a * a % MOD) % MOD;
            }
        }

        let mut ans = (sum_a * sum_a % MOD - sum_sq + MOD) % MOD;
        ans = ans * INV2 % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-trapezoids points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ((MOD 1000000007)
        (INV2 500000004))
    (define (mod-pos x)
      (let ((r (remainder x MOD)))
        (if (< r 0) (+ r MOD) r)))
    (define h (make-hash))
    (for-each
     (lambda (pt)
       (let ((y (cadr pt)))
         (hash-set! h y (+ 1 (hash-ref h y 0)))))
     points)
    (define sumS 0)
    (define sumSq 0)
    (for ([cnt (in-hash-values h)])
      (when (>= cnt 2)
        (let ((s (/ (* cnt (- cnt 1)) 2)))
          (set! sumS (+ sumS s))
          (set! sumSq (+ sumSq (* s s))))))
    (let* ((sumS-mod (mod-pos sumS))
           (sumSq-mod (mod-pos sumSq))
           (temp (- (mod-pos (* sumS-mod sumS-mod)) sumSq-mod))
           (temp-mod (mod-pos temp))
           (ans (mod-pos (* temp-mod INV2))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_trapezoids/1]).
-spec count_trapezoids(Points :: [[integer()]]) -> integer().
count_trapezoids(Points) ->
    Mod = 1000000007,
    Inv2 = 500000004, % modular inverse of 2 modulo Mod
    CountMap = build_map(Points, #{}),
    CombList = [comb(C) || {_Y, C} <- maps:to_list(CountMap), C >= 2],
    Total = lists:foldl(fun(X, Acc) -> (Acc + X) rem Mod end, 0, CombList),
    SumSq = lists:foldl(fun(X, Acc) ->
                ((Acc + (X * X) rem Mod) rem Mod)
            end, 0, CombList),
    TotalSq = (Total * Total) rem Mod,
    Diff = (TotalSq - SumSq + Mod) rem Mod,
    Ans = (Diff * Inv2) rem Mod,
    Ans.

build_map([], Map) -> Map;
build_map([[_, Y] | Rest], Map) ->
    NewMap = maps:update_with(Y, fun(Old) -> Old + 1 end, 1, Map),
    build_map(Rest, NewMap).

comb(C) ->
    ((C * (C - 1)) div 2).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_trapezoids(points :: [[integer]]) :: integer
  def count_trapezoids(points) do
    mod = 1_000_000_007
    # Count points per y-coordinate
    y_counts =
      Enum.reduce(points, %{}, fn [_x, y], acc ->
        Map.update(acc, y, 1, &(&1 + 1))
      end)

    {sum, sum_sq} =
      Enum.reduce(y_counts, {0, 0}, fn {_y, cnt}, {s, ss} ->
        if cnt >= 2 do
          comb = div(cnt * (cnt - 1), 2) |> rem(mod)
          s_new = rem(s + comb, mod)
          ss_new = rem(ss + rem(comb * comb, mod), mod)
          {s_new, ss_new}
        else
          {s, ss}
        end
      end)

    inv2 = 500_000_004
    ans =
      ((rem(sum * sum, mod) - sum_sq + mod)
       |> rem(mod)
       |> Kernel.*(inv2))
      |> rem(mod)

    ans
  end
end
```
