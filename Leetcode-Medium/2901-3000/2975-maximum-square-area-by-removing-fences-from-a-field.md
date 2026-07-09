# 2975. Maximum Square Area by Removing Fences From a Field

## Cpp

```cpp
class Solution {
public:
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        const long long MOD = 1000000007LL;
        // Prepare horizontal positions
        vector<long long> H;
        H.reserve(hFences.size() + 2);
        H.push_back(1);
        for (int x : hFences) H.push_back(x);
        H.push_back(m);
        sort(H.begin(), H.end());
        // Prepare vertical positions
        vector<long long> V;
        V.reserve(vFences.size() + 2);
        V.push_back(1);
        for (int y : vFences) V.push_back(y);
        V.push_back(n);
        sort(V.begin(), V.end());

        unordered_set<long long> horizDiffs;
        horizDiffs.reserve(H.size()*H.size());
        for (size_t i = 0; i < H.size(); ++i) {
            for (size_t j = i + 1; j < H.size(); ++j) {
                horizDiffs.insert(H[j] - H[i]);
            }
        }

        long long best = -1;
        for (size_t i = 0; i < V.size(); ++i) {
            for (size_t j = i + 1; j < V.size(); ++j) {
                long long d = V[j] - V[i];
                if (horizDiffs.find(d) != horizDiffs.end()) {
                    if (d > best) best = d;
                }
            }
        }

        if (best == -1) return -1;
        long long area = (best % MOD) * (best % MOD) % MOD;
        return static_cast<int>(area);
    }
};
```

## Java

```java
class Solution {
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        final long MOD = 1_000_000_007L;
        // Prepare horizontal positions including borders
        int[] hAll = new int[hFences.length + 2];
        hAll[0] = 1;
        hAll[hAll.length - 1] = m;
        System.arraycopy(hFences, 0, hAll, 1, hFences.length);
        java.util.Arrays.sort(hAll);
        // All possible horizontal side lengths
        java.util.HashSet<Integer> hDiffs = new java.util.HashSet<>();
        for (int i = 0; i < hAll.length; i++) {
            for (int j = i + 1; j < hAll.length; j++) {
                hDiffs.add(hAll[j] - hAll[i]);
            }
        }

        // Prepare vertical positions including borders
        int[] vAll = new int[vFences.length + 2];
        vAll[0] = 1;
        vAll[vAll.length - 1] = n;
        System.arraycopy(vFences, 0, vAll, 1, vFences.length);
        java.util.Arrays.sort(vAll);

        int maxSide = 0;
        for (int i = 0; i < vAll.length; i++) {
            for (int j = i + 1; j < vAll.length; j++) {
                int diff = vAll[j] - vAll[i];
                if (hDiffs.contains(diff) && diff > maxSide) {
                    maxSide = diff;
                }
            }
        }

        if (maxSide == 0) return -1;
        long area = ((long) maxSide * maxSide) % MOD;
        return (int) area;
    }
}
```

## Python

```python
class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        # include borders
        h = list(hFences)
        v = list(vFences)

        if 1 not in h:
            h.append(1)
        if m not in h:
            h.append(m)
        if 1 not in v:
            v.append(1)
        if n not in v:
            v.append(n)

        h.sort()
        v.sort()

        # all possible distances
        h_dist = set()
        for i in range(len(h)):
            hi = h[i]
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - hi)

        max_side = -1
        # check vertical distances against horizontal ones
        for i in range(len(v)):
            vi = v[i]
            for j in range(i + 1, len(v)):
                d = v[j] - vi
                if d in h_dist and d > max_side:
                    max_side = d

        if max_side == -1:
            return -1
        return (max_side * max_side) % MOD
```

## Python3

```python
from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        H = hFences + [1, m]
        V = vFences + [1, n]
        # Compute all possible distances between pairs in each set
        diffsH = set()
        for i in range(len(H)):
            hi = H[i]
            for j in range(i + 1, len(H)):
                diffsH.add(H[j] - hi)
        diffsV = set()
        for i in range(len(V)):
            vi = V[i]
            for j in range(i + 1, len(V)):
                diffsV.add(V[j] - vi)
        common = diffsH & diffsV
        if not common:
            return -1
        side = max(common)
        return (side * side) % MOD
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int maximizeSquareArea(int m, int n, int* hFences, int hFencesSize, int* vFences, int vFencesSize) {
    const int MOD = 1000000007;

    /* Build full horizontal fence list */
    int totalH = hFencesSize + 2;
    int *h = (int *)malloc(totalH * sizeof(int));
    h[0] = 1;
    for (int i = 0; i < hFencesSize; ++i) h[i + 1] = hFences[i];
    h[totalH - 1] = m;
    qsort(h, totalH, sizeof(int), cmp_int);

    /* Build full vertical fence list */
    int totalV = vFencesSize + 2;
    int *v = (int *)malloc(totalV * sizeof(int));
    v[0] = 1;
    for (int i = 0; i < vFencesSize; ++i) v[i + 1] = vFences[i];
    v[totalV - 1] = n;
    qsort(v, totalV, sizeof(int), cmp_int);

    /* All possible differences */
    int cntH = totalH * (totalH - 1) / 2;
    int cntV = totalV * (totalV - 1) / 2;

    int *diffH = (int *)malloc(cntH * sizeof(int));
    int *diffV = (int *)malloc(cntV * sizeof(int));

    int idx = 0;
    for (int i = 0; i < totalH; ++i) {
        for (int j = i + 1; j < totalH; ++j) {
            diffH[idx++] = h[j] - h[i];
        }
    }

    idx = 0;
    for (int i = 0; i < totalV; ++i) {
        for (int j = i + 1; j < totalV; ++j) {
            diffV[idx++] = v[j] - v[i];
        }
    }

    free(h);
    free(v);

    qsort(diffH, cntH, sizeof(int), cmp_int);
    qsort(diffV, cntV, sizeof(int), cmp_int);

    int i = cntH - 1;
    int j = cntV - 1;
    int best = -1;

    while (i >= 0 && j >= 0) {
        if (diffH[i] == diffV[j]) {
            best = diffH[i];
            break;
        } else if (diffH[i] > diffV[j]) {
            --i;
        } else {
            --j;
        }
    }

    free(diffH);
    free(diffV);

    if (best == -1) return -1;
    long long area = (long long)best * best % MOD;
    return (int)area;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int MaximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        // Get all possible lengths from horizontal fences (x-direction)
        var hLengths = GetAllLengths(m, hFences);
        
        // Generate lengths from vertical fences and find maximum common length
        long maxLen = 0;
        var positionsV = new List<int>(vFences.Length + 2);
        positionsV.Add(1);
        positionsV.AddRange(vFences);
        positionsV.Add(n);
        positionsV.Sort();
        
        int vCount = positionsV.Count;
        long[] gapsV = new long[vCount - 1];
        for (int i = 0; i < vCount - 1; i++) {
            gapsV[i] = (long)positionsV[i + 1] - positionsV[i];
        }
        
        for (int i = 0; i < gapsV.Length; i++) {
            long sum = 0;
            for (int j = i; j < gapsV.Length; j++) {
                sum += gapsV[j];
                if (hLengths.Contains(sum) && sum > maxLen) {
                    maxLen = sum;
                }
            }
        }
        
        if (maxLen == 0) return -1;
        long res = (maxLen % MOD) * (maxLen % MOD) % MOD;
        return (int)res;
    }
    
    private HashSet<long> GetAllLengths(int totalSize, int[] fences) {
        var positions = new List<int>(fences.Length + 2);
        positions.Add(1);
        positions.AddRange(fences);
        positions.Add(totalSize);
        positions.Sort();
        
        int count = positions.Count;
        long[] gaps = new long[count - 1];
        for (int i = 0; i < count - 1; i++) {
            gaps[i] = (long)positions[i + 1] - positions[i];
        }
        
        var set = new HashSet<long>();
        for (int i = 0; i < gaps.Length; i++) {
            long sum = 0;
            for (int j = i; j < gaps.Length; j++) {
                sum += gaps[j];
                set.Add(sum);
            }
        }
        return set;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[]} hFences
 * @param {number[]} vFences
 * @return {number}
 */
var maximizeSquareArea = function(m, n, hFences, vFences) {
    const MOD = 1000000007n;
    
    // include the immutable outer fences
    const H = [1, ...hFences, m];
    const V = [1, ...vFences, n];
    
    // collect all possible horizontal distances
    const hSet = new Set();
    for (let i = 0; i < H.length; ++i) {
        for (let j = i + 1; j < H.length; ++j) {
            hSet.add(H[j] - H[i]);
        }
    }
    
    // find the maximum distance that also appears vertically
    let maxSide = 0;
    for (let i = 0; i < V.length; ++i) {
        for (let j = i + 1; j < V.length; ++j) {
            const d = V[j] - V[i];
            if (d > maxSide && hSet.has(d)) {
                maxSide = d;
            }
        }
    }
    
    if (maxSide === 0) return -1;
    
    const areaMod = (BigInt(maxSide) * BigInt(maxSide)) % MOD;
    return Number(areaMod);
};
```

## Typescript

```typescript
function maximizeSquareArea(m: number, n: number, hFences: number[], vFences: number[]): number {
    const MOD = 1000000007n;

    // add outer boundaries
    hFences.push(1);
    hFences.push(m);
    vFences.push(1);
    vFences.push(n);

    hFences.sort((a, b) => a - b);
    vFences.sort((a, b) => a - b);

    const horizDiffs = new Set<number>();
    for (let i = 0; i < hFences.length; i++) {
        for (let j = i + 1; j < hFences.length; j++) {
            horizDiffs.add(hFences[j] - hFences[i]);
        }
    }

    let maxSide = 0;
    for (let i = 0; i < vFences.length; i++) {
        for (let j = i + 1; j < vFences.length; j++) {
            const d = vFences[j] - vFences[i];
            if (horizDiffs.has(d) && d > maxSide) {
                maxSide = d;
            }
        }
    }

    if (maxSide === 0) return -1;

    const area = (BigInt(maxSide) * BigInt(maxSide)) % MOD;
    return Number(area);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[] $hFences
     * @param Integer[] $vFences
     * @return Integer
     */
    function maximizeSquareArea($m, $n, $hFences, $vFences) {
        $MOD = 1000000007;

        // Add borders to fence lists
        $h = $hFences;
        $h[] = 1;
        $h[] = $m;
        sort($h);

        $v = $vFences;
        $v[] = 1;
        $v[] = $n;
        sort($v);

        // All possible horizontal gaps
        $hSet = [];
        $lenH = count($h);
        for ($i = 0; $i < $lenH; $i++) {
            for ($j = $i + 1; $j < $lenH; $j++) {
                $diff = $h[$j] - $h[$i];
                $hSet[$diff] = true;
            }
        }

        // Find maximum common gap with vertical gaps
        $maxSide = 0;
        $lenV = count($v);
        for ($i = 0; $i < $lenV; $i++) {
            for ($j = $i + 1; $j < $lenV; $j++) {
                $diff = $v[$j] - $v[$i];
                if (isset($hSet[$diff]) && $diff > $maxSide) {
                    $maxSide = $diff;
                }
            }
        }

        if ($maxSide == 0) {
            return -1;
        }

        $area = ($maxSide % $MOD) * ($maxSide % $MOD) % $MOD;
        return $area;
    }
}
```

## Swift

```swift
class Solution {
    func maximizeSquareArea(_ m: Int, _ n: Int, _ hFences: [Int], _ vFences: [Int]) -> Int {
        let mod = 1_000_000_007
        var h = hFences
        h.append(1)
        h.append(m)
        h.sort()
        
        var horizontalDiffs = Set<Int>()
        for i in 0..<h.count {
            for j in i+1..<h.count {
                let diff = h[j] - h[i]
                if diff > 0 {
                    horizontalDiffs.insert(diff)
                }
            }
        }
        
        var v = vFences
        v.append(1)
        v.append(n)
        v.sort()
        
        var maxCommon = 0
        for i in 0..<v.count {
            for j in i+1..<v.count {
                let diff = v[j] - v[i]
                if diff > 0 && horizontalDiffs.contains(diff) {
                    if diff > maxCommon {
                        maxCommon = diff
                    }
                }
            }
        }
        
        if maxCommon == 0 {
            return -1
        }
        let lMod = maxCommon % mod
        let area = Int((Int64(lMod) * Int64(lMod)) % Int64(mod))
        return area
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeSquareArea(m: Int, n: Int, hFences: IntArray, vFences: IntArray): Int {
        val MOD = 1_000_000_007L

        // Prepare positions including borders
        val hPos = mutableListOf<Int>()
        hPos.add(1)
        for (x in hFences) hPos.add(x)
        hPos.add(m)
        hPos.sort()

        val vPos = mutableListOf<Int>()
        vPos.add(1)
        for (y in vFences) vPos.add(y)
        vPos.add(n)
        vPos.sort()

        // All possible horizontal lengths
        val horizSet = HashSet<Long>()
        for (i in 0 until hPos.size) {
            for (j in i + 1 until hPos.size) {
                horizSet.add((hPos[j] - hPos[i]).toLong())
            }
        }

        // All possible vertical lengths
        val vertSet = HashSet<Long>()
        for (i in 0 until vPos.size) {
            for (j in i + 1 until vPos.size) {
                vertSet.add((vPos[j] - vPos[i]).toLong())
            }
        }

        // Find maximum common length
        var maxLen = 0L
        // iterate over smaller set for efficiency
        val (smallSet, largeSet) = if (horizSet.size <= vertSet.size) {
            horizSet to vertSet
        } else {
            vertSet to horizSet
        }
        for (len in smallSet) {
            if (largeSet.contains(len) && len > maxLen) {
                maxLen = len
            }
        }

        if (maxLen == 0L) return -1

        val areaMod = ((maxLen % MOD) * (maxLen % MOD)) % MOD
        return areaMod.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int maximizeSquareArea(int m, int n, List<int> hFences, List<int> vFences) {
    // Prepare sorted fence positions including borders
    List<int> hPos = [1];
    hPos.addAll(hFences);
    hPos.sort();
    hPos.add(m);

    List<int> vPos = [1];
    vPos.addAll(vFences);
    vPos.sort();
    vPos.add(n);

    // Segment lengths between consecutive fences
    List<int> hSeg = [];
    for (int i = 0; i < hPos.length - 1; ++i) {
      hSeg.add(hPos[i + 1] - hPos[i]);
    }
    List<int> vSeg = [];
    for (int i = 0; i < vPos.length - 1; ++i) {
      vSeg.add(vPos[i + 1] - vPos[i]);
    }

    // All possible sums of consecutive horizontal segments
    Set<int> horizSums = {};
    for (int i = 0; i < hSeg.length; ++i) {
      int sum = 0;
      for (int j = i; j < hSeg.length; ++j) {
        sum += hSeg[j];
        horizSums.add(sum);
      }
    }

    // Find maximum common length with vertical sums
    int maxLen = 0;
    for (int i = 0; i < vSeg.length; ++i) {
      int sum = 0;
      for (int j = i; j < vSeg.length; ++j) {
        sum += vSeg[j];
        if (horizSums.contains(sum) && sum > maxLen) {
          maxLen = sum;
        }
      }
    }

    if (maxLen == 0) return -1;

    int sideMod = maxLen % _mod;
    return ((sideMod * sideMod) % _mod);
  }
}
```

## Golang

```go
package main

import "sort"

func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
	const MOD int64 = 1000000007

	// Prepare horizontal positions including borders
	H := make([]int, 0, len(hFences)+2)
	H = append(H, 1, m)
	H = append(H, hFences...)
	sort.Ints(H)

	// Prepare vertical positions including borders
	V := make([]int, 0, len(vFences)+2)
	V = append(V, 1, n)
	V = append(V, vFences...)
	sort.Ints(V)

	// All possible side lengths from horizontal fences
	hDiffs := make(map[int]struct{})
	for i := 0; i < len(H); i++ {
		for j := i + 1; j < len(H); j++ {
			d := H[j] - H[i]
			hDiffs[d] = struct{}{}
		}
	}

	maxSide := -1
	// Check vertical differences against horizontal set
	for i := 0; i < len(V); i++ {
		for j := i + 1; j < len(V); j++ {
			d := V[j] - V[i]
			if _, ok := hDiffs[d]; ok && d > maxSide {
				maxSide = d
			}
		}
	}

	if maxSide == -1 {
		return -1
	}
	area := (int64(maxSide) * int64(maxSide)) % MOD
	return int(area)
}
```

## Ruby

```ruby
def maximize_square_area(m, n, h_fences, v_fences)
  mod = 1_000_000_007
  xs = [1] + h_fences.sort + [m]
  ys = [1] + v_fences.sort + [n]

  diff_set = {}
  (0...xs.length).each do |i|
    ((i + 1)...xs.length).each do |j|
      d = xs[j] - xs[i]
      diff_set[d] = true
    end
  end

  max_side = 0
  (0...ys.length).each do |i|
    ((i + 1)...ys.length).each do |j|
      d = ys[j] - ys[i]
      if diff_set[d] && d > max_side
        max_side = d
      end
    end
  end

  return -1 if max_side == 0
  (max_side * max_side) % mod
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L
    def maximizeSquareArea(m: Int, n: Int, hFences: Array[Int], vFences: Array[Int]): Int = {
        import scala.collection.mutable

        // Prepare sorted lists including borders
        val hArr = new Array[Int](hFences.length + 2)
        hArr(0) = 1
        System.arraycopy(hFences, 0, hArr, 1, hFences.length)
        hArr(hArr.length - 1) = m
        scala.util.Sorting.quickSort(hArr)

        val vArr = new Array[Int](vFences.length + 2)
        vArr(0) = 1
        System.arraycopy(vFences, 0, vArr, 1, vFences.length)
        vArr(vArr.length - 1) = n
        scala.util.Sorting.quickSort(vArr)

        // All possible horizontal lengths
        val hSet = mutable.HashSet[Int]()
        var i = 0
        while (i < hArr.length) {
            var j = i + 1
            while (j < hArr.length) {
                hSet.add(hArr(j) - hArr(i))
                j += 1
            }
            i += 1
        }

        // Find maximum common length with vertical lengths
        var maxLen = 0
        i = 0
        while (i < vArr.length) {
            var j = i + 1
            while (j < vArr.length) {
                val diff = vArr(j) - vArr(i)
                if (diff > maxLen && hSet.contains(diff)) {
                    maxLen = diff
                }
                j += 1
            }
            i += 1
        }

        if (maxLen == 0) -1
        else ((maxLen.toLong % MOD) * (maxLen.toLong % MOD) % MOD).toInt
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut hx: Vec<i64> = Vec::with_capacity(h_fences.len() + 2);
        hx.push(1);
        for &x in &h_fences {
            hx.push(x as i64);
        }
        hx.push(m as i64);
        hx.sort_unstable();

        let mut vy: Vec<i64> = Vec::with_capacity(v_fences.len() + 2);
        vy.push(1);
        for &y in &v_fences {
            vy.push(y as i64);
        }
        vy.push(n as i64);
        vy.sort_unstable();

        // All possible horizontal side lengths
        let mut horiz_set: HashSet<i64> = HashSet::new();
        for i in 0..hx.len() {
            for j in (i + 1)..hx.len() {
                horiz_set.insert(hx[j] - hx[i]);
            }
        }

        // Find the maximum common side length
        let mut best: i64 = 0;
        for i in 0..vy.len() {
            for j in (i + 1)..vy.len() {
                let d = vy[j] - vy[i];
                if horiz_set.contains(&d) && d > best {
                    best = d;
                }
            }
        }

        if best == 0 {
            -1
        } else {
            ((best % MOD) * (best % MOD) % MOD) as i32
        }
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (maximize-square-area m n hFences vFences)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([h-all (append (list 1) (sort hFences <) (list m))]
         [v-all (append (list 1) (sort vFences <) (list n))])
    ;; compute all horizontal gaps
    (define h-diffs (make-hash))
    (let ([lenh (length h-all)])
      (for ([i (in-range lenh)])
        (for ([j (in-range (+ i 1) lenh)])
          (hash-set! h-diffs (- (list-ref h-all j) (list-ref h-all i)) #t))))
    ;; find maximum common gap
    (define max-gap -1)
    (let ([lenv (length v-all)])
      (for ([i (in-range lenv)])
        (for ([j (in-range (+ i 1) lenv)])
          (let* ([diff (- (list-ref v-all j) (list-ref v-all i))])
            (when (hash-has-key? h-diffs diff)
              (when (> diff max-gap)
                (set! max-gap diff)))))))
    (if (= max-gap -1)
        -1
        (modulo (* max-gap max-gap) MOD))))
```

## Erlang

```erlang
-module(solution).
-export([maximize_square_area/4]).

-define(MOD, 1000000007).

-spec maximize_square_area(integer(), integer(), [integer()], [integer()]) -> integer().
maximize_square_area(M, N, HFences, VFences) ->
    HSorted = lists:sort(HFences),
    VSorted = lists:sort(VFences),
    HPos = [1] ++ HSorted ++ [M],
    VPos = [1] ++ VSorted ++ [N],
    HMap = diffs(HPos, #{}),
    VMap = diffs(VPos, #{}),
    MaxSide = max_common(HMap, VMap, -1),
    case MaxSide of
        -1 -> -1;
        _ ->
            LMod = MaxSide rem ?MOD,
            (LMod * LMod) rem ?MOD
    end.

%% compute all positive differences between any two positions in the list
diffs([], Acc) -> Acc;
diffs([_], Acc) -> Acc;
diffs([H|T]=PosList, Acc) ->
    NewAcc = diff_with_start(H, T, Acc),
    diffs(T, NewAcc).

diff_with_start(_Start, [], Acc) -> Acc;
diff_with_start(Start, [Next|Rest], Acc) ->
    Diff = Next - Start,
    Updated = maps:put(Diff, true, Acc),
    diff_with_start(Start, Rest, Updated).

%% find maximum key present in both maps
max_common(HMap, VMap, CurrentMax) ->
    Keys = maps:keys(HMap),
    max_common_keys(Keys, VMap, CurrentMax).

max_common_keys([], _VMap, Max) -> Max;
max_common_keys([K|Rest], VMap, Max) ->
    NewMax = case maps:is_key(K, VMap) of
        true when K > Max -> K;
        _ -> Max
    end,
    max_common_keys(Rest, VMap, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec maximize_square_area(m :: integer, n :: integer, h_fences :: [integer], v_fences :: [integer]) :: integer
  def maximize_square_area(m, n, h_fences, v_fences) do
    h = Enum.sort([1] ++ h_fences ++ [m])
    v = Enum.sort([1] ++ v_fences ++ [n])

    diffs_h = differences_set(h)
    diffs_v = differences_set(v)

    max_common =
      Enum.reduce(diffs_h, nil, fn d, acc ->
        if MapSet.member?(diffs_v, d) do
          case acc do
            nil -> d
            _ when d > acc -> d
            _ -> acc
          end
        else
          acc
        end
      end)

    case max_common do
      nil -> -1
      side ->
        rem(side * side, 1_000_000_007)
    end
  end

  defp differences_set(sorted_list) do
    len = length(sorted_list)

    0..(len - 2)
    |> Enum.flat_map(fn i ->
      hi = Enum.at(sorted_list, i)

      ((i + 1)..(len - 1))
      |> Enum.map(fn j -> Enum.at(sorted_list, j) - hi end)
    end)
    |> MapSet.new()
  end
end
```
