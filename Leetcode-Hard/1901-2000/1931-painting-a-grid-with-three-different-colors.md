# 1931. Painting a Grid With Three Different Colors

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int colorTheGrid(int m, int n) {
        const int MOD = 1'000'000'007;
        // generate all valid column masks
        vector<int> masks;
        vector<vector<int>> cols; // colors for each mask
        int total = 1;
        for (int i = 0; i < m; ++i) total *= 3; // 3^m
        
        for (int mask = 0; mask < total; ++mask) {
            int x = mask;
            vector<int> col(m);
            bool ok = true;
            for (int i = 0; i < m; ++i) {
                col[i] = x % 3;
                x /= 3;
                if (i > 0 && col[i] == col[i-1]) { // vertical adjacency
                    ok = false;
                    break;
                }
            }
            if (ok) {
                masks.push_back(mask);
                cols.push_back(col);
            }
        }
        int sz = masks.size();
        // precompute compatibility between columns
        vector<vector<int>> adj(sz);
        for (int i = 0; i < sz; ++i) {
            for (int j = i + 1; j < sz; ++j) {
                bool ok = true;
                for (int k = 0; k < m; ++k) {
                    if (cols[i][k] == cols[j][k]) { ok = false; break; }
                }
                if (ok) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        // DP over columns
        vector<int> dp(sz, 1), ndp(sz, 0);
        for (int colIdx = 1; colIdx < n; ++colIdx) {
            fill(ndp.begin(), ndp.end(), 0);
            for (int i = 0; i < sz; ++i) {
                int cur = dp[i];
                if (!cur) continue;
                for (int nxt : adj[i]) {
                    ndp[nxt] += cur;
                    if (ndp[nxt] >= MOD) ndp[nxt] -= MOD;
                }
            }
            dp.swap(ndp);
        }
        long long ans = 0;
        for (int v : dp) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int colorTheGrid(int m, int n) {
        int totalMasks = (int) Math.pow(3, m);
        List<Integer> valid = new ArrayList<>();
        for (int mask = 0; mask < totalMasks; mask++) {
            if (isVerticallyValid(mask, m)) {
                valid.add(mask);
            }
        }

        int k = valid.size();
        @SuppressWarnings("unchecked")
        List<Integer>[] compat = new ArrayList[k];
        for (int i = 0; i < k; i++) compat[i] = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            int a = valid.get(i);
            for (int j = 0; j < k; j++) {
                int b = valid.get(j);
                if (areCompatible(a, b, m)) {
                    compat[i].add(j);
                }
            }
        }

        long[] dpPrev = new long[k];
        Arrays.fill(dpPrev, 1L); // first column

        for (int col = 1; col < n; col++) {
            long[] dpCurr = new long[k];
            for (int i = 0; i < k; i++) {
                long ways = dpPrev[i];
                if (ways == 0) continue;
                for (int j : compat[i]) {
                    dpCurr[j] += ways;
                    if (dpCurr[j] >= MOD) dpCurr[j] -= MOD;
                }
            }
            dpPrev = dpCurr;
        }

        long ans = 0;
        for (long v : dpPrev) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return (int) ans;
    }

    private boolean isVerticallyValid(int mask, int m) {
        int prev = -1;
        for (int i = 0; i < m; i++) {
            int cur = mask % 3;
            if (cur == prev) return false;
            prev = cur;
            mask /= 3;
        }
        return true;
    }

    private boolean areCompatible(int a, int b, int m) {
        for (int i = 0; i < m; i++) {
            int ca = a % 3;
            int cb = b % 3;
            if (ca == cb) return false;
            a /= 3;
            b /= 3;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # generate all column patterns where vertical adjacent cells differ
        total_masks = 3 ** m
        valid = []
        for mask in range(total_masks):
            ok = True
            prev = -1
            tmp = mask
            for _ in range(m):
                cur = tmp % 3
                if cur == prev:
                    ok = False
                    break
                prev = cur
                tmp //= 3
            if ok:
                valid.append(mask)

        k = len(valid)

        # precompute compatibility between patterns (horizontal adjacency)
        compat = [[] for _ in range(k)]

        def compatible(a, b):
            for _ in range(m):
                ca = a % 3
                cb = b % 3
                if ca == cb:
                    return False
                a //= 3
                b //= 3
            return True

        for i in range(k):
            mi = valid[i]
            lst = compat[i]
            for j in range(k):
                if compatible(mi, valid[j]):
                    lst.append(j)

        # DP over columns
        dp = [1] * k  # first column
        for _ in range(1, n):
            ndp = [0] * k
            for i in range(k):
                val = dp[i]
                if val:
                    for j in compat[i]:
                        ndp[j] = (ndp[j] + val) % MOD
            dp = ndp

        return sum(dp) % MOD
```

## Python3

```python
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        max_state = 3 ** m

        # generate all masks where vertical adjacent cells differ
        masks = []
        digits = []  # list of tuples representing colors per row
        for s in range(max_state):
            cur = s
            ok = True
            prev = -1
            cols = []
            for _ in range(m):
                c = cur % 3
                if c == prev:
                    ok = False
                    break
                cols.append(c)
                prev = c
                cur //= 3
            if ok:
                masks.append(s)
                digits.append(tuple(cols))

        k = len(masks)
        idx_of = {mask: i for i, mask in enumerate(masks)}

        # precompute compatibility between columns (horizontal adjacency)
        compat = [[] for _ in range(k)]
        for i in range(k):
            di = digits[i]
            for j in range(k):
                dj = digits[j]
                good = True
                for p in range(m):
                    if di[p] == dj[p]:
                        good = False
                        break
                if good:
                    compat[i].append(j)

        # DP over columns
        dp = [1] * k  # first column can be any valid mask
        for _ in range(n - 1):
            ndp = [0] * k
            for i in range(k):
                total = 0
                for j in compat[i]:
                    total += dp[j]
                ndp[i] = total % MOD
            dp = ndp

        return sum(dp) % MOD
```

## C

```c
#include <stdbool.h>

int colorTheGrid(int m, int n) {
    const int MOD = 1000000007;
    int pow3[6];
    pow3[0] = 1;
    for (int i = 1; i <= m; ++i) pow3[i] = pow3[i - 1] * 3;

    int total = pow3[m];
    int validMasks[243];
    int dig[243][5];
    int vcnt = 0;

    for (int mask = 0; mask < total; ++mask) {
        int tmp = mask;
        bool ok = true;
        for (int i = 0; i < m; ++i) {
            int d = tmp % 3;
            dig[vcnt][i] = d;
            tmp /= 3;
            if (i > 0 && dig[vcnt][i] == dig[vcnt][i - 1]) {
                ok = false;
            }
        }
        if (ok) {
            validMasks[vcnt++] = mask;
        }
    }

    long long dpPrev[243] = {0}, dpCurr[243];
    for (int i = 0; i < vcnt; ++i) dpPrev[i] = 1;

    for (int col = 1; col < n; ++col) {
        for (int i = 0; i < vcnt; ++i) {
            long long sum = 0;
            for (int j = 0; j < vcnt; ++j) {
                bool compatible = true;
                for (int k = 0; k < m; ++k) {
                    if (dig[i][k] == dig[j][k]) {
                        compatible = false;
                        break;
                    }
                }
                if (compatible) {
                    sum += dpPrev[j];
                    if (sum >= (1LL << 62)) sum %= MOD;
                }
            }
            dpCurr[i] = sum % MOD;
        }
        for (int i = 0; i < vcnt; ++i) dpPrev[i] = dpCurr[i];
    }

    long long ans = 0;
    for (int i = 0; i < vcnt; ++i) {
        ans += dpPrev[i];
        if (ans >= (1LL << 62)) ans %= MOD;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    
    public int ColorTheGrid(int m, int n) {
        // total number of ternary masks for a column
        int totalMasks = 1;
        for (int i = 0; i < m; i++) totalMasks *= 3;

        var validColors = new List<int[]>();
        // enumerate masks that are vertically valid
        for (int mask = 0; mask < totalMasks; mask++) {
            int x = mask;
            int[] col = new int[m];
            bool ok = true;
            for (int i = 0; i < m; i++) {
                col[i] = x % 3;
                x /= 3;
            }
            for (int i = 1; i < m; i++) {
                if (col[i] == col[i - 1]) { ok = false; break; }
            }
            if (ok) validColors.Add(col);
        }

        int V = validColors.Count;
        // precompute compatibility between masks
        var compat = new List<int>[V];
        for (int i = 0; i < V; i++) compat[i] = new List<int>();
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                bool ok = true;
                for (int row = 0; row < m; row++) {
                    if (validColors[i][row] == validColors[j][row]) { ok = false; break; }
                }
                if (ok) compat[i].Add(j);
            }
        }

        long[] dpPrev = new long[V];
        for (int i = 0; i < V; i++) dpPrev[i] = 1; // first column

        for (int colIdx = 1; colIdx < n; colIdx++) {
            long[] dpCurr = new long[V];
            for (int i = 0; i < V; i++) {
                foreach (int j in compat[i]) {
                    dpCurr[i] += dpPrev[j];
                    if (dpCurr[i] >= MOD) dpCurr[i] -= MOD;
                }
            }
            dpPrev = dpCurr;
        }

        long ans = 0;
        foreach (var v in dpPrev) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var colorTheGrid = function(m, n) {
    const MOD = 1000000007;
    const totalMasks = Math.pow(3, m);
    const validMasks = [];
    const colors = []; // array of digit arrays for each valid mask

    // enumerate all masks and keep those with no vertical equal neighbors
    for (let mask = 0; mask < totalMasks; ++mask) {
        const arr = new Array(m);
        let tmp = mask;
        for (let i = 0; i < m; ++i) {
            arr[i] = tmp % 3;
            tmp = Math.floor(tmp / 3);
        }
        let ok = true;
        for (let i = 0; i + 1 < m; ++i) {
            if (arr[i] === arr[i + 1]) { ok = false; break; }
        }
        if (ok) {
            validMasks.push(mask);
            colors.push(arr);
        }
    }

    const len = validMasks.length;
    // precompute compatibility: masks that differ in every row
    const compat = new Array(len);
    for (let i = 0; i < len; ++i) {
        compat[i] = [];
        for (let j = 0; j < len; ++j) {
            let good = true;
            for (let k = 0; k < m; ++k) {
                if (colors[i][k] === colors[j][k]) { good = false; break; }
            }
            if (good) compat[i].push(j);
        }
    }

    // DP over columns
    let dpPrev = new Array(len).fill(1); // first column
    for (let col = 1; col < n; ++col) {
        const dpCurr = new Array(len).fill(0);
        for (let i = 0; i < len; ++i) {
            const val = dpPrev[i];
            if (val === 0) continue;
            const list = compat[i];
            for (let idx = 0; idx < list.length; ++idx) {
                const j = list[idx];
                let sum = dpCurr[j] + val;
                if (sum >= MOD) sum -= MOD;
                dpCurr[j] = sum;
            }
        }
        dpPrev = dpCurr;
    }

    // sum all possibilities for the last column
    let ans = 0;
    for (let v of dpPrev) {
        ans += v;
        if (ans >= MOD) ans -= MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function colorTheGrid(m: number, n: number): number {
    const MOD = 1000000007;
    const totalMasks = Math.pow(3, m);
    const isValid = new Array<boolean>(totalMasks).fill(false);
    const colorsArr: number[][] = new Array(totalMasks);
    const validMasks: number[] = [];

    // enumerate all masks and keep those with no equal adjacent vertically
    for (let mask = 0; mask < totalMasks; ++mask) {
        let tmp = mask;
        const colors = new Array<number>(m);
        let ok = true;
        for (let i = 0; i < m; ++i) {
            colors[i] = tmp % 3;
            if (i > 0 && colors[i] === colors[i - 1]) {
                ok = false;
                break;
            }
            tmp = Math.floor(tmp / 3);
        }
        if (ok) {
            isValid[mask] = true;
            colorsArr[mask] = colors;
            validMasks.push(mask);
        }
    }

    // precompute compatibility: masks that differ in every row
    const compat: number[][] = new Array(totalMasks);
    for (const mask of validMasks) {
        const list: number[] = [];
        const colColors = colorsArr[mask];
        for (const other of validMasks) {
            const otherColors = colorsArr[other];
            let good = true;
            for (let i = 0; i < m; ++i) {
                if (colColors[i] === otherColors[i]) {
                    good = false;
                    break;
                }
            }
            if (good) list.push(other);
        }
        compat[mask] = list;
    }

    // dp over columns
    let dpPrev = new Array<number>(totalMasks).fill(0);
    for (const mask of validMasks) {
        dpPrev[mask] = 1; // first column
    }

    for (let col = 1; col < n; ++col) {
        const dpCurr = new Array<number>(totalMasks).fill(0);
        for (const mask of validMasks) {
            let sum = 0;
            const prevList = compat[mask];
            for (let i = 0, len = prevList.length; i < len; ++i) {
                sum += dpPrev[prevList[i]];
                if (sum >= MOD) sum -= MOD;
            }
            dpCurr[mask] = sum;
        }
        dpPrev = dpCurr;
    }

    let ans = 0;
    for (const mask of validMasks) {
        ans += dpPrev[mask];
        if (ans >= MOD) ans -= MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function colorTheGrid($m, $n) {
        $mod = 1000000007;

        // total number of ternary masks for a column
        $total = 1;
        for ($i = 0; $i < $m; $i++) {
            $total *= 3;
        }

        $validMasks = [];
        $maskColors = [];   // mask => array of colors per row
        $indexMap = [];

        // enumerate masks that are vertically valid (no same adjacent colors)
        for ($mask = 0; $mask < $total; $mask++) {
            $tmp = $mask;
            $colors = [];
            $prev = -1;
            $ok = true;
            for ($row = 0; $row < $m; $row++) {
                $c = $tmp % 3;
                if ($c == $prev) {
                    $ok = false;
                    break;
                }
                $colors[] = $c;
                $prev = $c;
                $tmp = intdiv($tmp, 3);
            }
            if ($ok) {
                $idx = count($validMasks);
                $validMasks[] = $mask;
                $maskColors[$mask] = $colors;
                $indexMap[$mask] = $idx;
            }
        }

        $size = count($validMasks);
        // precompute compatibility: for each mask, list of previous masks that differ in every row
        $compat = array_fill(0, $size, []);
        for ($i = 0; $i < $size; $i++) {
            $maskA = $validMasks[$i];
            $colorsA = $maskColors[$maskA];
            for ($j = 0; $j < $size; $j++) {
                $maskB = $validMasks[$j];
                $colorsB = $maskColors[$maskB];
                $ok = true;
                for ($row = 0; $row < $m; $row++) {
                    if ($colorsA[$row] == $colorsB[$row]) {
                        $ok = false;
                        break;
                    }
                }
                if ($ok) {
                    $compat[$i][] = $j; // j can be previous column for i
                }
            }
        }

        // DP initialization: first column
        $dpPrev = array_fill(0, $size, 1);

        // iterate over remaining columns
        for ($col = 1; $col < $n; $col++) {
            $dpCurr = array_fill(0, $size, 0);
            for ($i = 0; $i < $size; $i++) {
                $sum = 0;
                foreach ($compat[$i] as $prevIdx) {
                    $sum += $dpPrev[$prevIdx];
                    if ($sum >= $mod) {
                        $sum -= $mod;
                    }
                }
                $dpCurr[$i] = $sum % $mod;
            }
            $dpPrev = $dpCurr;
        }

        // sum all possibilities for the last column
        $ans = 0;
        foreach ($dpPrev as $val) {
            $ans += $val;
            if ($ans >= $mod) {
                $ans -= $mod;
            }
        }
        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func colorTheGrid(_ m: Int, _ n: Int) -> Int {
        let MOD = 1_000_000_007
        var totalMasks = 1
        for _ in 0..<m { totalMasks *= 3 }
        
        // Valid masks where vertical adjacent cells differ
        var validMasks = [Int]()
        for mask in 0..<totalMasks {
            var temp = mask
            var prev = -1
            var ok = true
            for _ in 0..<m {
                let cur = temp % 3
                if cur == prev { ok = false; break }
                prev = cur
                temp /= 3
            }
            if ok { validMasks.append(mask) }
        }
        
        let vCount = validMasks.count
        // Compatibility between masks (horizontal adjacency)
        var compat = [[Int]](repeating: [], count: vCount)
        for i in 0..<vCount {
            let maskA = validMasks[i]
            for j in 0..<vCount {
                let maskB = validMasks[j]
                var a = maskA, b = maskB
                var ok = true
                for _ in 0..<m {
                    if (a % 3) == (b % 3) { ok = false; break }
                    a /= 3
                    b /= 3
                }
                if ok { compat[i].append(j) }
            }
        }
        
        // DP over columns
        var dpPrev = [Int](repeating: 1, count: vCount) // first column
        if n == 1 {
            var ans = 0
            for v in dpPrev {
                ans += v
                if ans >= MOD { ans -= MOD }
            }
            return ans
        }
        
        for _ in 1..<n {
            var dpCurr = [Int](repeating: 0, count: vCount)
            for i in 0..<vCount {
                let ways = dpPrev[i]
                if ways == 0 { continue }
                for j in compat[i] {
                    var sum = dpCurr[j] + ways
                    if sum >= MOD { sum -= MOD }
                    dpCurr[j] = sum
                }
            }
            dpPrev = dpCurr
        }
        
        var result = 0
        for v in dpPrev {
            result += v
            if result >= MOD { result -= MOD }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    fun colorTheGrid(m: Int, n: Int): Int {
        // precompute powers of 3
        val pow3 = IntArray(m + 1)
        pow3[0] = 1
        for (i in 1..m) pow3[i] = pow3[i - 1] * 3

        // generate all valid column masks (no vertical adjacent same colors)
        val validMasks = mutableListOf<Int>()
        val limit = pow3[m]
        for (mask in 0 until limit) {
            if (isValid(mask, m)) {
                validMasks.add(mask)
            }
        }
        val sz = validMasks.size

        // precompute compatibility between masks (no horizontal same colors)
        val compat = Array(sz) { IntArray(0) }
        for (i in 0 until sz) {
            val list = mutableListOf<Int>()
            for (j in 0 until sz) {
                if (compatible(validMasks[i], validMasks[j], m)) {
                    list.add(j)
                }
            }
            compat[i] = list.toIntArray()
        }

        // DP over columns
        var dpPrev = LongArray(sz) { 1L } // first column can be any valid mask
        for (col in 1 until n) {
            val dpCurr = LongArray(sz)
            for (i in 0 until sz) {
                var sum = 0L
                for (j in compat[i]) {
                    sum += dpPrev[j]
                    if (sum >= MOD) sum -= MOD
                }
                dpCurr[i] = sum % MOD
            }
            dpPrev = dpCurr
        }

        var ans = 0L
        for (v in dpPrev) {
            ans += v
            if (ans >= MOD) ans -= MOD
        }
        return ans.toInt()
    }

    private fun isValid(mask: Int, m: Int): Boolean {
        var prev = -1
        var curMask = mask
        repeat(m) {
            val cur = curMask % 3
            if (cur == prev) return false
            prev = cur
            curMask /= 3
        }
        return true
    }

    private fun compatible(a: Int, b: Int, m: Int): Boolean {
        var aa = a
        var bb = b
        repeat(m) {
            val ca = aa % 3
            val cb = bb % 3
            if (ca == cb) return false
            aa /= 3
            bb /= 3
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int colorTheGrid(int m, int n) {
    // total possible masks in base-3 representation
    int totalMasks = 1;
    for (int i = 0; i < m; i++) totalMasks *= 3;

    // collect masks that are valid vertically (no same adjacent colors)
    List<int> validMasks = [];
    List<List<int>> colors = [];

    for (int mask = 0; mask < totalMasks; mask++) {
      List<int> arr = List.filled(m, 0);
      int x = mask;
      bool ok = true;
      for (int i = 0; i < m; i++) {
        arr[i] = x % 3;
        x ~/= 3;
        if (i > 0 && arr[i] == arr[i - 1]) {
          ok = false;
          break;
        }
      }
      if (ok) {
        validMasks.add(mask);
        colors.add(arr);
      }
    }

    int len = validMasks.length;

    // precompute compatibility between masks (horizontal adjacency)
    List<List<int>> trans = List.generate(len, (_) => []);
    for (int i = 0; i < len; i++) {
      for (int j = 0; j < len; j++) {
        bool compatible = true;
        for (int k = 0; k < m; k++) {
          if (colors[i][k] == colors[j][k]) {
            compatible = false;
            break;
          }
        }
        if (compatible) trans[i].add(j);
      }
    }

    // DP over columns
    List<int> dpPrev = List.filled(len, 1); // first column

    for (int col = 1; col < n; col++) {
      List<int> dpCurr = List.filled(len, 0);
      for (int i = 0; i < len; i++) {
        int val = dpPrev[i];
        if (val == 0) continue;
        for (int j in trans[i]) {
          dpCurr[j] += val;
          if (dpCurr[j] >= _MOD) dpCurr[j] -= _MOD;
        }
      }
      dpPrev = dpCurr;
    }

    int ans = 0;
    for (int v in dpPrev) {
      ans += v;
      if (ans >= _MOD) ans -= _MOD;
    }
    return ans;
  }
}
```

## Golang

```go
package main

const MOD = 1000000007

func colorTheGrid(m int, n int) int {
	// total possible masks in base-3
	pow3 := 1
	for i := 0; i < m; i++ {
		pow3 *= 3
	}
	validMasks := make([]int, 0)
	colors := make([][]int, 0)

	// enumerate valid column colorings (no vertical adjacent same colors)
	for mask := 0; mask < pow3; mask++ {
		tmp := mask
		col := make([]int, m)
		ok := true
		for i := 0; i < m; i++ {
			col[i] = tmp % 3
			if i > 0 && col[i] == col[i-1] {
				ok = false
			}
			tmp /= 3
		}
		if ok {
			validMasks = append(validMasks, mask)
			colors = append(colors, col)
		}
	}

	sz := len(validMasks)

	// precompute compatibility between columns (no same color in same row)
	compat := make([][]int, sz)
	for i := 0; i < sz; i++ {
		for j := 0; j < sz; j++ {
			good := true
			for k := 0; k < m; k++ {
				if colors[i][k] == colors[j][k] {
					good = false
					break
				}
			}
			if good {
				compat[i] = append(compat[i], j)
			}
		}
	}

	dpPrev := make([]int, sz)
	for i := 0; i < sz; i++ {
		dpPrev[i] = 1
	}
	dpCurr := make([]int, sz)

	// DP over columns
	for colIdx := 1; colIdx < n; colIdx++ {
		for i := 0; i < sz; i++ {
			dpCurr[i] = 0
		}
		for i := 0; i < sz; i++ {
			val := dpPrev[i]
			if val == 0 {
				continue
			}
			for _, j := range compat[i] {
				sum := dpCurr[j] + val
				if sum >= MOD {
					sum -= MOD
				}
				dpCurr[j] = sum
			}
		}
		dpPrev, dpCurr = dpCurr, dpPrev
	}

	ans := 0
	for _, v := range dpPrev {
		ans += v
		if ans >= MOD {
			ans -= MOD
		}
	}
	return ans
}
```

## Ruby

```ruby
def color_the_grid(m, n)
  mod = 1_000_000_007
  total_masks = 3 ** m
  valid_masks = []
  colors = {}

  (0...total_masks).each do |mask|
    arr = Array.new(m)
    tmp = mask
    ok = true
    (0...m).each do |i|
      color = tmp % 3
      arr[i] = color
      tmp /= 3
      if i > 0 && arr[i] == arr[i - 1]
        ok = false
        break
      end
    end
    if ok
      valid_masks << mask
      colors[mask] = arr
    end
  end

  size = valid_masks.size
  compat = Array.new(size) { [] }

  (0...size).each do |i|
    col_i = colors[valid_masks[i]]
    (0...size).each do |j|
      next if i == j
      col_j = colors[valid_masks[j]]
      ok = true
      (0...m).each do |row|
        if col_i[row] == col_j[row]
          ok = false
          break
        end
      end
      compat[i] << j if ok
    end
  end

  dp = Array.new(size, 1)
  (1...n).each do
    ndp = Array.new(size, 0)
    (0...size).each do |i|
      val = dp[i]
      next if val == 0
      compat[i].each do |j|
        ndp[j] += val
        ndp[j] -= mod if ndp[j] >= mod
      end
    end
    dp = ndp
  end

  ans = 0
  dp.each { |v| ans = (ans + v) % mod }
  ans
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

object Solution {
  private val MOD = 1000000007

  def colorTheGrid(m: Int, n: Int): Int = {
    // total number of ternary masks
    var total = 1
    for (_ <- 0 until m) total *= 3

    val validMasks = new ArrayBuffer[Int]()
    val digitsList = new ArrayBuffer[Array[Int]]()

    // enumerate masks with no equal adjacent vertical cells
    for (mask <- 0 until total) {
      var ok = true
      val digs = new Array[Int](m)
      var tmp = mask
      for (i <- 0 until m) {
        digs(i) = tmp % 3
        if (i > 0 && digs(i) == digs(i - 1)) ok = false
        tmp /= 3
      }
      if (ok) {
        validMasks += mask
        digitsList += digs
      }
    }

    val k = validMasks.length
    // precompute compatibility between masks
    val compat = Array.ofDim[Array[Int]](k)
    for (i <- 0 until k) {
      val list = new ArrayBuffer[Int]()
      for (j <- 0 until k) {
        var good = true
        var r = 0
        while (r < m && good) {
          if (digitsList(i)(r) == digitsList(j)(r)) good = false
          r += 1
        }
        if (good) list += j
      }
      compat(i) = list.toArray
    }

    // DP over columns
    var dpPrev = Array.fill[Int](k)(1)
    for (_col <- 1 until n) {
      val dpCurr = new Array[Int](k)
      for (i <- 0 until k) {
        val cur = dpPrev(i)
        if (cur != 0) {
          for (j <- compat(i)) {
            var sum = dpCurr(j) + cur
            if (sum >= MOD) sum -= MOD
            dpCurr(j) = sum
          }
        }
      }
      dpPrev = dpCurr
    }

    var ans = 0
    for (v <- dpPrev) {
      ans += v
      if (ans >= MOD) ans -= MOD
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn color_the_grid(m: i32, n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = m as usize;
        let n = n as usize;

        // total number of masks (3^m)
        let mut total_masks = 1usize;
        for _ in 0..m {
            total_masks *= 3;
        }

        // collect masks that are valid within a column (no equal adjacent cells vertically)
        let mut valid_masks: Vec<usize> = Vec::new();
        for mask in 0..total_masks {
            let mut x = mask;
            let mut ok = true;
            let mut prev = x % 3;
            x /= 3;
            for _ in 1..m {
                let cur = x % 3;
                if cur == prev {
                    ok = false;
                    break;
                }
                prev = cur;
                x /= 3;
            }
            if ok {
                valid_masks.push(mask);
            }
        }

        let k = valid_masks.len();
        // compatibility list: for each mask j, store indices i that can be previous column
        let mut compat: Vec<Vec<usize>> = vec![Vec::new(); k];
        for (j_idx, &mask_j) in valid_masks.iter().enumerate() {
            for (i_idx, &mask_i) in valid_masks.iter().enumerate() {
                // check that at each row the colors differ
                let mut a = mask_i;
                let mut b = mask_j;
                let mut good = true;
                for _ in 0..m {
                    if a % 3 == b % 3 {
                        good = false;
                        break;
                    }
                    a /= 3;
                    b /= 3;
                }
                if good {
                    compat[j_idx].push(i_idx);
                }
            }
        }

        // dp for first column: each valid mask contributes 1 way
        let mut dp_prev: Vec<i64> = vec![1; k];

        // iterate over remaining columns
        for _col in 1..n {
            let mut dp_cur: Vec<i64> = vec![0; k];
            for (j, list) in compat.iter().enumerate() {
                let mut sum = 0i64;
                for &i_idx in list {
                    sum += dp_prev[i_idx];
                    if sum >= MOD {
                        sum -= MOD;
                    }
                }
                dp_cur[j] = sum;
            }
            dp_prev = dp_cur;
        }

        let ans: i64 = dp_prev.iter().fold(0, |acc, &v| (acc + v) % MOD);
        ans as i32
    }
}
```

## Racket

```racket
(define (color-the-grid m n)
  (define MOD 1000000007)
  (define total (expt 3 m))
  ;; precompute digits for each mask and collect valid masks
  (define digits-vec (make-vector total #f))
  (define valid-masks '())
  (let loop ((mask 0))
    (when (< mask total)
      (let ((dig (make-vector m)))
        (let inner ((i 0) (x mask))
          (when (< i m)
            (vector-set! dig i (remainder x 3))
            (inner (+ i 1) (quotient x 3))))
        ;; check vertical adjacency
        (define ok #t)
        (let check ((i 0))
          (when (< i (- m 1))
            (when (= (vector-ref dig i) (vector-ref dig (+ i 1)))
              (set! ok #f))
            (check (+ i 1))))
        (when ok
          (set! valid-masks (cons mask valid-masks))
          (vector-set! digits-vec mask dig)))
      (loop (+ mask 1))))
  (set! valid-masks (reverse valid-masks))
  (define V (length valid-masks))
  (define masks-vec (list->vector valid-masks))
  ;; compatibility between masks
  (define compat (make-vector V '()))
  (for ([i (in-range V)])
    (let* ((mask1 (vector-ref masks-vec i))
           (dig1 (vector-ref digits-vec mask1))
           (lst '()))
      (for ([j (in-range V)])
        (when (not (= i j))
          (let ((dig2 (vector-ref digits-vec (vector-ref masks-vec j))))
            (define ok #t)
            (let check2 ((r 0))
              (when (< r m)
                (when (= (vector-ref dig1 r) (vector-ref dig2 r))
                  (set! ok #f))
                (check2 (+ r 1))))
            (when ok
              (set! lst (cons j lst))))))
      (vector-set! compat i (reverse lst))))
  ;; DP over columns
  (define dp-prev (make-vector V 1))
  (let loop ((col 1))
    (when (< col n)
      (define dp-curr (make-vector V 0))
      (for ([i (in-range V)])
        (define sum 0)
        (for ([j (in-list (vector-ref compat i))])
          (set! sum (+ sum (vector-ref dp-prev j))))
        (vector-set! dp-curr i (modulo sum MOD)))
      (set! dp-prev dp-curr)
      (loop (+ col 1))))
  ;; final answer
  (define ans 0)
  (for ([i (in-range V)])
    (set! ans (modulo (+ ans (vector-ref dp-prev i)) MOD)))
  ans)
```

## Erlang

```erlang
-module(solution).
-export([color_the_grid/2]).

-define(MOD, 1000000007).

-spec color_the_grid(M :: integer(), N :: integer()) -> integer().
color_the_grid(M, N) ->
    MaxMask = pow3(M),
    ValidMasks = [Mask || Mask <- lists:seq(0, MaxMask - 1), is_valid_mask(Mask, M)],
    DigitsList = [digits(Mask, M) || Mask <- ValidMasks],
    L = length(DigitsList),
    Indices = lists:seq(0, L - 1),

    %% Precompute compatibility indices
    CompatIdxs = [
        [J || {J, D2} <- lists:zip(Indices, DigitsList), compatible(Di, D2)]
     || Di <- DigitsList],

    %% Initialize DP for first column
    DPPrev = lists:duplicate(L, 1),

    %% Iterate over remaining columns
    DPFinal = iterate_columns(N - 1, CompatIdxs, DPPrev),

    %% Sum all possibilities modulo MOD
    sum_list(DPFinal) rem ?MOD.

%% Power of 3
pow3(0) -> 1;
pow3(K) when K > 0 -> 3 * pow3(K - 1).

%% Convert mask to list of digits (length M), least significant digit first
digits(Mask, Len) ->
    digits_acc(Mask, Len, []).

digits_acc(_, 0, Acc) -> lists:reverse(Acc);
digits_acc(N, K, Acc) ->
    Digit = N rem 3,
    digits_acc(N div 3, K - 1, [Digit | Acc]).

%% Check if a mask is valid (no equal adjacent vertical cells)
is_valid_mask(Mask, M) ->
    D = digits(Mask, M),
    no_adjacent_equal(D).

no_adjacent_equal([]) -> true;
no_adjacent_equal([_]) -> true;
no_adjacent_equal([A, B | Rest]) when A =/= B -> no_adjacent_equal([B | Rest]);
no_adjacent_equal(_) -> false.

%% Compatibility between two columns (all rows differ)
compatible(D1, D2) ->
    compatible_pairs(lists:zip(D1, D2)).

compatible_pairs([]) -> true;
compatible_pairs([{A, B} | Rest]) when A =/= B -> compatible_pairs(Rest);
compatible_pairs(_) -> false.

%% Iterate DP over columns
iterate_columns(0, _CompatIdxs, DP) -> DP;
iterate_columns(Times, CompatIdxs, DPPrev) ->
    DPNext = [
        sum_compatible(IdxList, DPPrev)
     || IdxList <- CompatIdxs],
    iterate_columns(Times - 1, CompatIdxs, DPNext).

%% Sum dp values for compatible previous states
sum_compatible(IdxList, DPPrev) ->
    lists:foldl(
      fun(J, Acc) ->
          (Acc + lists:nth(J + 1, DPPrev)) rem ?MOD
      end,
      0,
      IdxList).

%% Sum all elements in a list modulo MOD
sum_list(List) ->
    lists:foldl(fun(X, Acc) -> (Acc + X) rem ?MOD end, 0, List).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec color_the_grid(m :: integer, n :: integer) :: integer
  def color_the_grid(m, n) do
    mod = 1_000_000_007
    total_masks = :math.pow(3, m) |> trunc

    # generate all masks that are valid inside a column (no equal vertical neighbours)
    {valid_masks, digits_map} =
      Enum.reduce(0..total_masks - 1, {[], %{}}, fn mask, {list, dmap} ->
        digits = get_digits(mask, m)

        if valid_row?(digits) do
          {[mask | list], Map.put(dmap, mask, digits)}
        else
          {list, dmap}
        end
      end)

    valid_masks = Enum.reverse(valid_masks)

    # pre‑compute compatibility between masks (different colour in each row)
    compat =
      Enum.reduce(valid_masks, %{}, fn a, acc ->
        da = Map.fetch!(digits_map, a)

        compatible =
          Enum.filter(valid_masks, fn b ->
            db = Map.fetch!(digits_map, b)
            compatible?(da, db)
          end)

        Map.put(acc, a, compatible)
      end)

    # DP initialization for the first column
    dp0 = for mask <- valid_masks, into: %{}, do: {mask, 1}

    final_dp =
      if n == 1 do
        dp0
      else
        Enum.reduce(2..n, dp0, fn _, prev_dp ->
          Enum.reduce(valid_masks, %{}, fn cur_mask, acc ->
            sum =
              Enum.reduce(compat[cur_mask], 0, fn pre_mask, s ->
                (s + Map.get(prev_dp, pre_mask, 0)) |> rem(mod)
              end)

            if sum == 0 do
              acc
            else
              Map.put(acc, cur_mask, sum)
            end
          end)
        end)
      end

    Enum.reduce(final_dp, 0, fn {_mask, cnt}, ans -> (ans + cnt) |> rem(mod) end)
  end

  # Convert mask to a list of base‑3 digits with length m (top row first)
  defp get_digits(mask, m) do
    digits = Integer.digits(mask, 3)
    padding = List.duplicate(0, m - length(digits))
    padding ++ digits
  end

  # Check that no two adjacent rows in the same column share a colour
  defp valid_row?(digits) do
    Enum.reduce_while(0..(length(digits) - 2), true, fn i, _ ->
      if Enum.at(digits, i) == Enum.at(digits, i + 1) do
        {:halt, false}
      else
        {:cont, true}
      end
    end)
  end

  # Two columns are compatible if every corresponding row has different colours
  defp compatible?(da, db) do
    Enum.zip(da, db)
    |> Enum.all?(fn {a, b} -> a != b end)
  end
end
```
