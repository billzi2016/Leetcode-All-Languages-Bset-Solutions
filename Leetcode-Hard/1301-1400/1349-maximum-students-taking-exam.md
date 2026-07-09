# 1349. Maximum Students Taking Exam

## Cpp

```cpp
class Solution {
public:
    int maxStudents(vector<vector<char>>& seats) {
        int m = seats.size();
        int n = seats[0].size();
        vector<int> rowMask(m, 0);
        for (int i = 0; i < m; ++i) {
            int mask = 0;
            for (int j = 0; j < n; ++j) {
                if (seats[i][j] == '.') mask |= (1 << j);
            }
            rowMask[i] = mask;
        }

        // Precompute all valid masks for each row
        vector<vector<int>> valid(m);
        int totalMasks = 1 << n;
        for (int i = 0; i < m; ++i) {
            for (int mask = 0; mask < totalMasks; ++mask) {
                // seats must be good
                if ((mask & ~rowMask[i]) != 0) continue;
                // no adjacent students in the same row
                if (mask & (mask << 1)) continue;
                valid[i].push_back(mask);
            }
        }

        const int NEG = -1e9;
        vector<int> dpPrev(totalMasks, NEG), dpCurr(totalMasks, NEG);
        dpPrev[0] = 0;

        for (int i = 0; i < m; ++i) {
            fill(dpCurr.begin(), dpCurr.end(), NEG);
            for (int mask : valid[i]) {
                int cnt = __builtin_popcount(mask);
                for (int prevMask = 0; prevMask < totalMasks; ++prevMask) {
                    if (dpPrev[prevMask] == NEG) continue;
                    // check upper-left and upper-right conflicts
                    if ((mask & (prevMask << 1)) != 0) continue;
                    if ((mask & (prevMask >> 1)) != 0) continue;
                    dpCurr[mask] = max(dpCurr[mask], dpPrev[prevMask] + cnt);
                }
            }
            dpPrev.swap(dpCurr);
        }

        int ans = 0;
        for (int v : dpPrev) ans = max(ans, v);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxStudents(char[][] seats) {
        int m = seats.length;
        int n = seats[0].length;
        int totalMask = 1 << n;

        // Precompute valid masks for each row
        List<int[]> validMasksPerRow = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int seatMask = 0;
            for (int j = 0; j < n; j++) {
                if (seats[i][j] == '.') {
                    seatMask |= (1 << j);
                }
            }
            List<Integer> list = new ArrayList<>();
            for (int mask = 0; mask < totalMask; mask++) {
                // seats must be good
                if ((mask & ~seatMask) != 0) continue;
                // no adjacent students in the same row
                if ((mask & (mask << 1)) != 0) continue;
                list.add(mask);
            }
            int[] arr = new int[list.size()];
            for (int k = 0; k < list.size(); k++) arr[k] = list.get(k);
            validMasksPerRow.add(arr);
        }

        int[] dpPrev = new int[totalMask];
        Arrays.fill(dpPrev, -1);
        dpPrev[0] = 0;

        for (int row = 0; row < m; row++) {
            int[] dpCurr = new int[totalMask];
            Arrays.fill(dpCurr, -1);
            int[] curMasks = validMasksPerRow.get(row);
            for (int prevMask = 0; prevMask < totalMask; prevMask++) {
                if (dpPrev[prevMask] < 0) continue;
                for (int curMask : curMasks) {
                    // check upper-left and upper-right conflicts
                    if ((curMask & (prevMask << 1)) != 0) continue;
                    if ((curMask & (prevMask >> 1)) != 0) continue;
                    int val = dpPrev[prevMask] + Integer.bitCount(curMask);
                    if (val > dpCurr[curMask]) {
                        dpCurr[curMask] = val;
                    }
                }
            }
            dpPrev = dpCurr;
        }

        int ans = 0;
        for (int v : dpPrev) {
            if (v > ans) ans = v;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        m = len(seats)
        n = len(seats[0])
        # good seat mask per row
        good_masks = []
        for row in seats:
            mask = 0
            for j, ch in enumerate(row):
                if ch == '.':
                    mask |= (1 << j)
            good_masks.append(mask)

        # precompute valid masks for each row and their bit counts
        valid_masks_per_row = []
        bits_cnt = {}
        for i in range(m):
            good = good_masks[i]
            valid = []
            for mask in range(1 << n):
                if (mask & ~good) != 0:      # uses broken seat
                    continue
                if (mask & (mask >> 1)) != 0:  # adjacent students in same row
                    continue
                valid.append(mask)
                bits_cnt[mask] = bits_cnt.get(mask, bin(mask).count('1'))
            valid_masks_per_row.append(valid)

        dp_prev = {0: 0}
        for i in range(m):
            dp_curr = {}
            for cur in valid_masks_per_row[i]:
                cur_bits = bits_cnt[cur]
                for prev, val in dp_prev.items():
                    # check upper-left and upper-right conflicts
                    if (cur & (prev << 1)) != 0 or (cur & (prev >> 1)) != 0:
                        continue
                    new_val = val + cur_bits
                    if cur not in dp_curr or new_val > dp_curr[cur]:
                        dp_curr[cur] = new_val
            dp_prev = dp_curr

        return max(dp_prev.values() or [0])
```

## Python3

```python
class Solution:
    def maxStudents(self, seats):
        m = len(seats)
        n = len(seats[0])
        
        # Precompute valid masks for each row
        row_masks = []
        for i in range(m):
            good = 0
            for j in range(n):
                if seats[i][j] == '.':
                    good |= (1 << j)
            masks = []
            # iterate all subsets of good seats
            subset = good
            while True:
                # check no adjacent students in the same row
                if (subset & (subset << 1)) == 0:
                    masks.append(subset)
                if subset == 0:
                    break
                subset = (subset - 1) & good
            row_masks.append(masks)
        
        dp_prev = {0: 0}
        for i in range(m):
            dp_cur = {}
            for cur_mask in row_masks[i]:
                cur_cnt = cur_mask.bit_count()
                for prev_mask, val in dp_prev.items():
                    # check upper-left and upper-right conflicts
                    if (cur_mask & (prev_mask << 1)) == 0 and (cur_mask & (prev_mask >> 1)) == 0:
                        new_val = val + cur_cnt
                        if cur_mask not in dp_cur or new_val > dp_cur[cur_mask]:
                            dp_cur[cur_mask] = new_val
            dp_prev = dp_cur
        
        return max(dp_prev.values() or [0])
```

## C

```c
int maxStudents(char** seats, int seatsSize, int* seatsColSize) {
    int m = seatsSize;
    int n = seatsColSize[0];
    int maxMask = 1 << n;

    int bitcnt[256];
    for (int mask = 0; mask < maxMask; ++mask)
        bitcnt[mask] = __builtin_popcount(mask);

    int avail[8];
    for (int i = 0; i < m; ++i) {
        int mask = 0;
        for (int j = 0; j < n; ++j) {
            if (seats[i][j] == '.')
                mask |= (1 << j);
        }
        avail[i] = mask;
    }

    int goodMasks[256];
    int goodCount = 0;
    for (int mask = 0; mask < maxMask; ++mask) {
        if ((mask & (mask << 1)) == 0)
            goodMasks[goodCount++] = mask;
    }

    int valid[8][256];
    int vcnt[8];
    for (int i = 0; i < m; ++i) {
        int cnt = 0;
        for (int k = 0; k < goodCount; ++k) {
            int mask = goodMasks[k];
            if ((mask & ~avail[i]) == 0)
                valid[i][cnt++] = mask;
        }
        vcnt[i] = cnt;
    }

    static int dpPrev[256];
    static int dpCurr[256];
    const int NEG = -1000000;
    for (int i = 0; i < maxMask; ++i) dpPrev[i] = NEG;

    for (int idx = 0; idx < vcnt[0]; ++idx) {
        int mask = valid[0][idx];
        dpPrev[mask] = bitcnt[mask];
    }

    for (int r = 1; r < m; ++r) {
        for (int i = 0; i < maxMask; ++i) dpCurr[i] = NEG;
        for (int ci = 0; ci < vcnt[r]; ++ci) {
            int curMask = valid[r][ci];
            int curBits = bitcnt[curMask];
            for (int pi = 0; pi < vcnt[r - 1]; ++pi) {
                int prevMask = valid[r - 1][pi];
                if (dpPrev[prevMask] == NEG) continue;
                if ((curMask & (prevMask << 1)) == 0 && (curMask & (prevMask >> 1)) == 0) {
                    int val = dpPrev[prevMask] + curBits;
                    if (val > dpCurr[curMask]) dpCurr[curMask] = val;
                }
            }
        }
        for (int i = 0; i < maxMask; ++i) dpPrev[i] = dpCurr[i];
    }

    int ans = 0;
    for (int i = 0; i < maxMask; ++i)
        if (dpPrev[i] > ans) ans = dpPrev[i];
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxStudents(char[][] seats)
    {
        int m = seats.Length;
        int n = seats[0].Length;
        int maxMask = 1 << n;

        // Available seats mask per row
        int[] avail = new int[m];
        for (int i = 0; i < m; i++)
        {
            int mask = 0;
            for (int j = 0; j < n; j++)
                if (seats[i][j] == '.')
                    mask |= 1 << j;
            avail[i] = mask;
        }

        // Valid masks per row (no adjacent students, only on good seats)
        List<int>[] validMasks = new List<int>[m];
        for (int i = 0; i < m; i++)
        {
            var list = new List<int>();
            for (int mask = 0; mask < maxMask; mask++)
            {
                if ((mask & ~avail[i]) != 0) continue;          // uses broken seat
                if ((mask & (mask << 1)) != 0) continue;        // adjacent in same row
                list.Add(mask);
            }
            validMasks[i] = list;
        }

        int[] dpPrev = new int[maxMask];
        int[] dpCurr = new int[maxMask];
        for (int i = 0; i < maxMask; i++) dpPrev[i] = -1;
        dpPrev[0] = 0; // no students before first row

        for (int row = 0; row < m; row++)
        {
            for (int i = 0; i < maxMask; i++) dpCurr[i] = -1;

            foreach (int mask in validMasks[row])
            {
                int cnt = BitCount(mask);
                for (int prev = 0; prev < maxMask; prev++)
                {
                    if (dpPrev[prev] < 0) continue;
                    // check upper-left and upper-right conflicts
                    if ((mask & (prev << 1)) != 0) continue;
                    if ((mask & (prev >> 1)) != 0) continue;

                    int val = dpPrev[prev] + cnt;
                    if (val > dpCurr[mask]) dpCurr[mask] = val;
                }
            }

            // swap dp arrays
            var temp = dpPrev;
            dpPrev = dpCurr;
            dpCurr = temp;
        }

        int answer = 0;
        for (int i = 0; i < maxMask; i++)
            if (dpPrev[i] > answer) answer = dpPrev[i];
        return answer;
    }

    private int BitCount(int x)
    {
        int cnt = 0;
        while (x != 0)
        {
            cnt += x & 1;
            x >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} seats
 * @return {number}
 */
var maxStudents = function(seats) {
    const m = seats.length;
    const n = seats[0].length;
    const totalMask = 1 << n;

    // allowed positions per row as bitmask
    const allowedRow = new Array(m);
    for (let i = 0; i < m; ++i) {
        let mask = 0;
        for (let j = 0; j < n; ++j) {
            if (seats[i][j] === '.') mask |= (1 << j);
        }
        allowedRow[i] = mask;
    }

    // precompute all valid masks for each row
    const validMasks = new Array(m);
    for (let i = 0; i < m; ++i) {
        const list = [];
        const allow = allowedRow[i];
        for (let mask = 0; mask < totalMask; ++mask) {
            if ((mask & ~allow) !== 0) continue;          // seat is broken
            if ((mask & (mask << 1)) !== 0) continue;    // adjacent students in same row
            list.push(mask);
        }
        validMasks[i] = list;
    }

    // precompute popcount for all masks up to totalMask
    const bitCount = new Array(totalMask).fill(0);
    for (let mask = 1; mask < totalMask; ++mask) {
        bitCount[mask] = bitCount[mask >> 1] + (mask & 1);
    }

    // DP arrays
    let dpPrev = new Array(totalMask).fill(-Infinity);
    for (const mask of validMasks[0]) {
        dpPrev[mask] = bitCount[mask];
    }

    for (let row = 1; row < m; ++row) {
        const dpCurr = new Array(totalMask).fill(-Infinity);
        for (const curMask of validMasks[row]) {
            const curCnt = bitCount[curMask];
            for (const prevMask of validMasks[row - 1]) {
                if ((curMask & (prevMask << 1)) !== 0) continue; // upper left conflict
                if ((curMask & (prevMask >> 1)) !== 0) continue; // upper right conflict
                const val = dpPrev[prevMask] + curCnt;
                if (val > dpCurr[curMask]) dpCurr[curMask] = val;
            }
        }
        dpPrev = dpCurr;
    }

    let ans = 0;
    for (let mask = 0; mask < totalMask; ++mask) {
        if (dpPrev[mask] > ans) ans = dpPrev[mask];
    }
    return ans;
};
```

## Typescript

```typescript
function maxStudents(seats: string[][]): number {
    const m = seats.length;
    const n = seats[0].length;
    const rowMasks: number[][] = [];

    for (let i = 0; i < m; i++) {
        let broken = 0;
        for (let j = 0; j < n; j++) {
            if (seats[i][j] === '#') broken |= (1 << j);
        }
        const valid: number[] = [];
        const limit = 1 << n;
        for (let mask = 0; mask < limit; mask++) {
            if ((mask & broken) !== 0) continue;               // seat is broken
            if ((mask & (mask << 1)) !== 0) continue;          // adjacent in same row
            valid.push(mask);
        }
        rowMasks.push(valid);
    }

    const popcnt = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    let dpPrev = new Map<number, number>();
    dpPrev.set(0, 0); // before first row

    for (let i = 0; i < m; i++) {
        const dpCurr = new Map<number, number>();
        for (const cur of rowMasks[i]) {
            const curCnt = popcnt(cur);
            for (const [prev, val] of dpPrev.entries()) {
                if ((cur << 1) & prev) continue; // upper-left conflict
                if ((cur >> 1) & prev) continue; // upper-right conflict
                const total = val + curCnt;
                const existing = dpCurr.get(cur);
                if (existing === undefined || total > existing) {
                    dpCurr.set(cur, total);
                }
            }
        }
        dpPrev = dpCurr;
    }

    let ans = 0;
    for (const v of dpPrev.values()) {
        if (v > ans) ans = v;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $seats
     * @return Integer
     */
    function maxStudents($seats) {
        $m = count($seats);
        $n = count($seats[0]);
        $validMasks = array_fill(0, $m, []);

        for ($i = 0; $i < $m; $i++) {
            $rowValid = [];
            $limit = 1 << $n;
            for ($mask = 0; $mask < $limit; $mask++) {
                // no adjacent students in the same row
                if (($mask & ($mask << 1)) != 0) continue;

                $ok = true;
                for ($j = 0; $j < $n; $j++) {
                    if ((($mask >> $j) & 1) == 1 && $seats[$i][$j] == '#') {
                        $ok = false;
                        break;
                    }
                }
                if ($ok) $rowValid[] = $mask;
            }
            $validMasks[$i] = $rowValid;
        }

        // DP for the first row
        $dpPrev = [];
        foreach ($validMasks[0] as $mask) {
            $dpPrev[$mask] = $this->popcount($mask);
        }

        // Process remaining rows
        for ($i = 1; $i < $m; $i++) {
            $dpCurr = [];
            foreach ($validMasks[$i] as $mask) {
                $best = -1;
                foreach ($dpPrev as $prevMask => $val) {
                    if ((($mask & ($prevMask << 1)) == 0) && (($mask & ($prevMask >> 1)) == 0)) {
                        $cand = $val + $this->popcount($mask);
                        if ($cand > $best) $best = $cand;
                    }
                }
                if ($best >= 0) {
                    $dpCurr[$mask] = $best;
                }
            }
            $dpPrev = $dpCurr;
        }

        $ans = 0;
        foreach ($dpPrev as $val) {
            if ($val > $ans) $ans = $val;
        }
        return $ans;
    }

    private function popcount($x) {
        $cnt = 0;
        while ($x) {
            $x &= $x - 1;
            $cnt++;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func maxStudents(_ seats: [[Character]]) -> Int {
        let m = seats.count
        guard m > 0 else { return 0 }
        let n = seats[0].count
        let maxMask = 1 << n
        
        // Precompute valid masks for each row
        var validMasksPerRow = [[Int]](repeating: [], count: m)
        for i in 0..<m {
            var masks = [Int]()
            for mask in 0..<maxMask {
                // no adjacent students in the same row
                if (mask & (mask << 1)) != 0 { continue }
                var ok = true
                for j in 0..<n {
                    if ((mask >> j) & 1) == 1 && seats[i][j] == "#" {
                        ok = false
                        break
                    }
                }
                if ok {
                    masks.append(mask)
                }
            }
            validMasksPerRow[i] = masks
        }
        
        func bitCount(_ x: Int) -> Int {
            var v = x
            var c = 0
            while v > 0 {
                c += v & 1
                v >>= 1
            }
            return c
        }
        
        var prevDP = [Int](repeating: -1, count: maxMask)
        prevDP[0] = 0
        
        for row in 0..<m {
            var curDP = [Int](repeating: -1, count: maxMask)
            for mask in validMasksPerRow[row] {
                let cnt = bitCount(mask)
                for prevMask in 0..<maxMask where prevDP[prevMask] >= 0 {
                    // check upper-left and upper-right conflicts
                    if (mask & (prevMask << 1)) != 0 { continue }
                    if (mask & (prevMask >> 1)) != 0 { continue }
                    let val = prevDP[prevMask] + cnt
                    if val > curDP[mask] {
                        curDP[mask] = val
                    }
                }
            }
            prevDP = curDP
        }
        
        return prevDP.max() ?? 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxStudents(seats: Array<CharArray>): Int {
        val m = seats.size
        val n = seats[0].size
        val totalMask = 1 shl n

        // broken mask per row: 1 where seat is '#'
        val broken = IntArray(m)
        for (i in 0 until m) {
            var mask = 0
            for (j in 0 until n) {
                if (seats[i][j] == '#') {
                    mask = mask or (1 shl j)
                }
            }
            broken[i] = mask
        }

        // valid masks per row
        val validMasks = Array(m) { mutableListOf<Int>() }
        for (i in 0 until m) {
            for (mask in 0 until totalMask) {
                if ((mask and (mask shl 1)) != 0) continue          // adjacent seats in same row
                if ((mask and broken[i]) != 0) continue             // seat is broken
                validMasks[i].add(mask)
            }
        }

        var dpPrev = IntArray(totalMask) { Int.MIN_VALUE }
        for (mask in validMasks[0]) {
            dpPrev[mask] = Integer.bitCount(mask)
        }

        for (row in 1 until m) {
            val dpCurr = IntArray(totalMask) { Int.MIN_VALUE }
            for (curMask in validMasks[row]) {
                val curCnt = Integer.bitCount(curMask)
                for (prevMask in validMasks[row - 1]) {
                    if ((curMask shl 1) and prevMask != 0) continue   // upper-left conflict
                    if ((curMask shr 1) and prevMask != 0) continue   // upper-right conflict
                    val prevVal = dpPrev[prevMask]
                    if (prevVal < 0) continue
                    val newVal = prevVal + curCnt
                    if (newVal > dpCurr[curMask]) {
                        dpCurr[curMask] = newVal
                    }
                }
            }
            dpPrev = dpCurr
        }

        return dpPrev.maxOrNull() ?: 0
    }
}
```

## Dart

```dart
class Solution {
  int maxStudents(List<List<String>> seats) {
    int m = seats.length;
    int n = seats[0].length;
    List<int> rowAvailable = List.filled(m, 0);
    for (int i = 0; i < m; i++) {
      int mask = 0;
      for (int j = 0; j < n; j++) {
        if (seats[i][j] == '.') {
          mask |= (1 << j);
        }
      }
      rowAvailable[i] = mask;
    }

    // Precompute valid masks for each row
    List<List<int>> validMasksPerRow = List.generate(m, (_) => []);
    int limit = 1 << n;
    for (int i = 0; i < m; i++) {
      int avail = rowAvailable[i];
      for (int mask = 0; mask < limit; mask++) {
        if ((mask & ~avail) != 0) continue; // seat not available
        if ((mask & (mask << 1)) != 0) continue; // adjacent seats in same row
        validMasksPerRow[i].add(mask);
      }
    }

    Map<int, int> dpPrev = {0: 0};
    for (int i = 0; i < m; i++) {
      Map<int, int> dpCur = {};
      for (int curMask in validMasksPerRow[i]) {
        int curCount = _popCount(curMask);
        for (var entry in dpPrev.entries) {
          int prevMask = entry.key;
          int prevVal = entry.value;
          if ((curMask & (prevMask << 1)) != 0) continue;
          if ((curMask & (prevMask >> 1)) != 0) continue;
          int newVal = prevVal + curCount;
          dpCur.update(curMask, (v) => v > newVal ? v : newVal,
              ifAbsent: () => newVal);
        }
      }
      dpPrev = dpCur;
    }

    int ans = 0;
    for (int val in dpPrev.values) {
      if (val > ans) ans = val;
    }
    return ans;
  }

  int _popCount(int x) {
    int count = 0;
    while (x != 0) {
      x &= (x - 1);
      count++;
    }
    return count;
  }
}
```

## Golang

```go
package main

import "math/bits"

func maxStudents(seats [][]byte) int {
	m := len(seats)
	n := len(seats[0])
	maxMask := 1 << n

	// validMasks[row] contains all seat configurations for that row
	validMasks := make([][]int, m)
	for i := 0; i < m; i++ {
		for mask := 0; mask < maxMask; mask++ {
			if (mask & (mask >> 1)) != 0 { // adjacent seats in same row
				continue
			}
			ok := true
			for j := 0; j < n; j++ {
				if ((mask>>j)&1) == 1 && seats[i][j] == '#' {
					ok = false
					break
				}
			}
			if ok {
				validMasks[i] = append(validMasks[i], mask)
			}
		}
	}

	dpPrev := make([]int, maxMask)
	for i := range dpPrev {
		dpPrev[i] = -1
	}
	dpPrev[0] = 0 // empty previous row

	for r := 0; r < m; r++ {
		dpCurr := make([]int, maxMask)
		for i := range dpCurr {
			dpCurr[i] = -1
		}
		for _, cur := range validMasks[r] {
			curCnt := bits.OnesCount(uint(cur))
			for prev := 0; prev < maxMask; prev++ {
				if dpPrev[prev] < 0 {
					continue
				}
				// check cheating between rows: upper-left and upper-right
				if (cur&(prev<<1)) != 0 || (cur&(prev>>1)) != 0 {
					continue
				}
				if dpCurr[cur] < dpPrev[prev]+curCnt {
					dpCurr[cur] = dpPrev[prev] + curCnt
				}
			}
		}
		dpPrev = dpCurr
	}

	ans := 0
	for _, v := range dpPrev {
		if v > ans {
			ans = v
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_students(seats)
  m = seats.size
  n = seats[0].size
  # Precompute allowed positions per row as bitmask
  allowed = Array.new(m, 0)
  m.times do |i|
    mask = 0
    seats[i].each_with_index { |c, j| mask |= (1 << j) if c == '.' }
    allowed[i] = mask
  end

  # Generate all valid masks for each row (no adjacent students and only on good seats)
  valid_masks_per_row = Array.new(m) { [] }
  max_mask = 1 << n
  m.times do |i|
    (0...max_mask).each do |mask|
      next unless (mask & ~allowed[i]).zero?          # only good seats
      next unless (mask & (mask << 1)).zero?          # no left/right adjacency
      valid_masks_per_row[i] << mask
    end
  end

  # Precompute bit counts for all masks up to n bits
  bit_count = Array.new(max_mask, 0)
  (1...max_mask).each do |mask|
    bit_count[mask] = bit_count[mask >> 1] + (mask & 1)
  end

  dp = {0 => 0}
  m.times do |row|
    new_dp = {}
    valid_masks_per_row[row].each do |curr|
      curr_cnt = bit_count[curr]
      dp.each do |prev, val|
        # check upper-left and upper-right conflicts
        next unless ((curr << 1) & prev).zero?
        next unless ((curr >> 1) & prev).zero?
        total = val + curr_cnt
        if !new_dp.key?(curr) || total > new_dp[curr]
          new_dp[curr] = total
        end
      end
    end
    dp = new_dp
  end

  dp.values.max || 0
end
```

## Scala

```scala
object Solution {
  def maxStudents(seats: Array[Array[Char]]): Int = {
    val m = seats.length
    val n = seats(0).length
    val rowValidMasks = new Array[Array[Int]](m)

    for (i <- 0 until m) {
      var availMask = 0
      for (j <- 0 until n) {
        if (seats(i)(j) == '.') availMask |= (1 << j)
      }
      val masks = scala.collection.mutable.ArrayBuffer[Int]()
      val limit = 1 << n
      for (mask <- 0 until limit) {
        if ((mask & ~availMask) == 0 && (mask & (mask << 1)) == 0) {
          masks += mask
        }
      }
      rowValidMasks(i) = masks.toArray
    }

    var dpPrev = scala.collection.mutable.Map[Int, Int]()
    dpPrev(0) = 0

    for (i <- 0 until m) {
      val dpCurr = scala.collection.mutable.Map[Int, Int]()
      for (curMask <- rowValidMasks(i)) {
        val curCount = Integer.bitCount(curMask)
        for ((prevMask, prevVal) <- dpPrev) {
          if ((curMask & (prevMask << 1)) == 0 && (curMask & (prevMask >> 1)) == 0) {
            val total = prevVal + curCount
            val existing = dpCurr.getOrElse(curMask, -1)
            if (total > existing) dpCurr(curMask) = total
          }
        }
      }
      dpPrev = dpCurr
    }

    dpPrev.values.max
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_students(seats: Vec<Vec<char>>) -> i32 {
        let m = seats.len();
        let n = seats[0].len();
        let max_mask = 1usize << n;

        // Precompute all valid seat configurations for each row
        let mut valid_masks: Vec<Vec<usize>> = vec![Vec::new(); m];
        for i in 0..m {
            for mask in 0..max_mask {
                // No two students sit side by side
                if (mask & (mask << 1)) != 0 {
                    continue;
                }
                // Seats must be not broken
                let mut ok = true;
                for j in 0..n {
                    if seats[i][j] == '#' && ((mask >> j) & 1) == 1 {
                        ok = false;
                        break;
                    }
                }
                if ok {
                    valid_masks[i].push(mask);
                }
            }
        }

        // DP: dp[mask] = max students up to current row with this mask
        let mut dp = vec![-1i32; max_mask];
        for &mask in &valid_masks[0] {
            dp[mask] = mask.count_ones() as i32;
        }

        for row in 1..m {
            let mut new_dp = vec![-1i32; max_mask];
            for &cur in &valid_masks[row] {
                let cur_cnt = cur.count_ones() as i32;
                for &prev in &valid_masks[row - 1] {
                    if dp[prev] < 0 {
                        continue;
                    }
                    // No cheating with upper-left or upper-right
                    if (cur & (prev << 1)) != 0 || (cur & (prev >> 1)) != 0 {
                        continue;
                    }
                    let val = dp[prev] + cur_cnt;
                    if val > new_dp[cur] {
                        new_dp[cur] = val;
                    }
                }
            }
            dp = new_dp;
        }

        *dp.iter().max().unwrap()
    }
}
```

## Racket

```racket
(define/contract (max-students seats)
  (-> (listof (listof char?)) exact-integer?)
  (let* ((m (length seats))
         (n (if (= m 0) 0 (length (first seats))))
         (row-available
           (map (lambda (row)
                  (let loop ((i 0) (mask 0))
                    (if (= i n) mask
                        (loop (+ i 1)
                              (if (char=? (list-ref row i) #\.)
                                  (bitwise-ior mask (arithmetic-shift 1 i))
                                  mask)))))
                seats))
         (valid-masks-per-row
           (map (lambda (avail)
                  (let ((limit (expt 2 n)))
                    (let loop ((mask 0) (res '()))
                      (if (= mask limit)
                          res
                          (let ((ok (and (= (bitwise-and mask (bitwise-not avail)) 0)
                                         (= (bitwise-and mask (arithmetic-shift mask 1)) 0))))
                            (loop (+ mask 1)
                                  (if ok (cons mask res) res)))))))
                row-available))
         (popcnt
           (lambda (x)
             (let loop ((y x) (c 0))
               (if (= y 0) c
                   (loop (bitwise-and y (- y)) (+ c 1)))))))
    (define (compatible? cur prev)
      (and (zero? (bitwise-and (arithmetic-shift cur 1) prev))
           (zero? (bitwise-and (arithmetic-shift cur -1) prev))))
    (let loop ((row 0) (dp (make-hash)))
      (if (= row m)
          (for/fold ([best 0]) ([mask (in-hash-keys dp)])
            (max best (hash-ref dp mask)))
          (let* ((valid-cur (list-ref valid-masks-per-row row))
                 (newdp (make-hash)))
            (for ([curMask valid-cur])
              (if (= row 0)
                  (hash-set! newdp curMask (popcnt curMask))
                  (for ([prevMask (in-hash-keys dp)])
                    (when (compatible? curMask prevMask)
                      (let* ((val (+ (hash-ref dp prevMask) (popcnt curMask)))
                             (existing (hash-ref newdp curMask #f)))
                        (if (or (not existing) (> val existing))
                            (hash-set! newdp curMask val))))))
            (loop (+ row 1) newdp))))))
```

## Erlang

```erlang
-export([max_students/1]).

-spec max_students(Seats :: [[char()]]) -> integer().
max_students(Seats) ->
    N = length(hd(Seats)),
    RowSeatMasks = [seat_mask(Row) || Row <- Seats],
    ValidRows = [valid_masks_for_row(SeatMask, N) || SeatMask <- RowSeatMasks],
    FinalMap = dp_rows(ValidRows, #{0 => 0}),
    maps:fold(fun(_Mask, Val, Acc) -> if Val > Acc -> Val; true -> Acc end end, 0, FinalMap).

seat_mask(Row) ->
    seat_mask(Row, 0, 0).

seat_mask([], _Idx, Acc) -> Acc;
seat_mask([C|Rest], Idx, Acc) ->
    NewAcc = case C of
        $. -> Acc bor (1 bsl Idx);
        _ -> Acc
    end,
    seat_mask(Rest, Idx + 1, NewAcc).

valid_masks_for_row(SeatMask, N) ->
    MaxMask = (1 bsl N) - 1,
    [ {Mask, bit_count(Mask)} ||
        Mask <- lists:seq(0, MaxMask),
        ((Mask band (Mask bsl 1)) == 0),               % no adjacent students in the same row
        (Mask band SeatMask) == Mask                  % only on good seats
    ].

bit_count(0) -> 0;
bit_count(N) ->
    (N band 1) + bit_count(N bsr 1).

dp_rows([], DPMap) -> DPMap;
dp_rows([RowValid|RestRows], PrevMap) ->
    CurMap = maps:from_list(
        [ {CurMask, MaxPrev + CurCnt}
          || {CurMask, CurCnt} <- RowValid,
             MaxPrev = max_compatible(PrevMap, CurMask),
             MaxPrev >= 0
        ]),
    dp_rows(RestRows, CurMap).

max_compatible(PrevMap, CurMask) ->
    maps:fold(
        fun(PrevMask, PrevVal, Acc) ->
            case ((CurMask band (PrevMask bsl 1)) == 0) andalso
                 ((CurMask band (PrevMask bsr 1)) == 0) of
                true ->
                    if PrevVal > Acc -> PrevVal; true -> Acc end;
                false -> Acc
            end
        end,
        -1,
        PrevMap).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec max_students(seats :: [[char]]) :: integer
  def max_students(seats) do
    n = length(List.first(seats))

    row_masks =
      Enum.map(seats, fn row ->
        Enum.with_index(row)
        |> Enum.reduce(0, fn {c, i}, acc ->
          if c == ?. do
            acc ||| (1 <<< i)
          else
            acc
          end
        end)
      end)

    max_mask = 1 <<< n

    valid_no_adj =
      for mask <- 0..(max_mask - 1), ((mask &&& (mask <<< 1)) == 0), do: mask

    row_valid_masks =
      Enum.map(row_masks, fn seat_mask ->
        Enum.filter(valid_no_adj, fn m -> (m &&& seat_mask) == m end)
      end)

    dp_initial = %{0 => 0}

    final_dp =
      Enum.reduce(row_valid_masks, dp_initial, fn cur_list, dp ->
        Enum.reduce(cur_list, %{}, fn cur, new_dp ->
          cur_bits = bit_count(cur)

          Enum.reduce(dp, new_dp, fn {prev, val}, acc ->
            if ((cur &&& (prev <<< 1)) == 0) and ((cur &&& (prev >>> 1)) == 0) do
              new_val = val + cur_bits

              case Map.get(acc, cur) do
                nil -> Map.put(acc, cur, new_val)
                existing when new_val > existing -> Map.put(acc, cur, new_val)
                _ -> acc
              end
            else
              acc
            end
          end)
        end)
      end)

    final_dp |> Map.values() |> Enum.max()
  end

  defp bit_count(0), do: 0
  defp bit_count(x) do
    1 + bit_count(bsr(x, 1))
  end
end
```
