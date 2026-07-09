# 1223. Dice Roll Simulation

## Cpp

```cpp
class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax) {
        const int MOD = 1000000007;
        if (n == 0) return 0;
        // dpPrev[face][cnt] : number of sequences ending with 'face' repeated cnt times
        vector<vector<int>> dpPrev(6, vector<int>(16, 0)), dpCurr(6, vector<int>(16, 0));
        for (int f = 0; f < 6; ++f) dpPrev[f][1] = 1;
        for (int i = 2; i <= n; ++i) {
            long long totalPrev = 0;
            for (int f = 0; f < 6; ++f)
                for (int c = 1; c <= rollMax[f]; ++c)
                    totalPrev = (totalPrev + dpPrev[f][c]) % MOD;

            for (int f = 0; f < 6; ++f) {
                long long sumSame = 0;
                for (int c = 1; c <= rollMax[f]; ++c) sumSame += dpPrev[f][c];
                sumSame %= MOD;
                dpCurr[f][1] = (int)((totalPrev - sumSame + MOD) % MOD);
                for (int c = 2; c <= rollMax[f]; ++c)
                    dpCurr[f][c] = dpPrev[f][c - 1];
            }
            // reset dpPrev for next iteration
            for (int f = 0; f < 6; ++f) fill(dpPrev[f].begin(), dpPrev[f].end(), 0);
            dpPrev.swap(dpCurr);
        }

        long long ans = 0;
        for (int f = 0; f < 6; ++f)
            for (int c = 1; c <= rollMax[f]; ++c)
                ans = (ans + dpPrev[f][c]) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int dieSimulator(int n, int[] rollMax) {
        int maxR = 0;
        for (int v : rollMax) maxR = Math.max(maxR, v);
        long[][] dpPrev = new long[6][maxR + 1];
        // initialization for first roll
        for (int f = 0; f < 6; f++) {
            dpPrev[f][1] = 1;
        }
        for (int pos = 2; pos <= n; pos++) {
            long[] totalFace = new long[6];
            long totalAll = 0;
            for (int f = 0; f < 6; f++) {
                long sum = 0;
                int limit = rollMax[f];
                for (int c = 1; c <= limit; c++) {
                    sum += dpPrev[f][c];
                }
                sum %= MOD;
                totalFace[f] = sum;
                totalAll += sum;
            }
            totalAll %= MOD;
            long[][] dpCurr = new long[6][maxR + 1];
            for (int f = 0; f < 6; f++) {
                // start a new streak with face f
                long val = totalAll - totalFace[f];
                if (val < 0) val += MOD;
                dpCurr[f][1] = val % MOD;
                // extend existing streaks of the same face
                int limit = rollMax[f];
                for (int c = 2; c <= limit; c++) {
                    dpCurr[f][c] = dpPrev[f][c - 1];
                }
            }
            dpPrev = dpCurr;
        }
        long ans = 0;
        for (int f = 0; f < 6; f++) {
            int limit = rollMax[f];
            for (int c = 1; c <= limit; c++) {
                ans += dpPrev[f][c];
            }
        }
        ans %= MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        # dp[face][cnt] = number of sequences ending with 'face' repeated cnt+1 times
        dp = [[0] * rollMax[i] for i in range(6)]
        for i in range(6):
            dp[i][0] = 1  # first roll can be any face once

        total_face = [1] * 6               # sum over counts for each face at current length
        total_all = sum(total_face) % MOD   # total sequences of current length

        for step in range(2, n + 1):
            new_dp = [[0] * rollMax[i] for i in range(6)]
            new_total_face = [0] * 6
            new_total_all = 0

            for f in range(6):
                # extend same face if allowed
                limit = rollMax[f]
                for c in range(limit - 1):
                    val = dp[f][c]
                    if val:
                        new_dp[f][c + 1] = (new_dp[f][c + 1] + val) % MOD

                # start a new run of this face after a different face
                sum_other = (total_all - total_face[f]) % MOD
                new_dp[f][0] = (new_dp[f][0] + sum_other) % MOD

            # recompute totals for next iteration
            for f in range(6):
                s = sum(new_dp[f]) % MOD
                new_total_face[f] = s
                new_total_all = (new_total_all + s) % MOD

            dp = new_dp
            total_face = new_total_face
            total_all = new_total_all

        return total_all % MOD if n > 0 else 0
```

## Python3

```python
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        # dp[face][cnt] = ways ending with 'face' repeated 'cnt' times (cnt >=1)
        dp = [[0] * (rollMax[f] + 1) for f in range(6)]
        for f in range(6):
            dp[f][1] = 1

        for _ in range(2, n + 1):
            newdp = [[0] * (rollMax[f] + 1) for f in range(6)]
            for f in range(6):
                maxc = rollMax[f]
                for c in range(1, maxc + 1):
                    val = dp[f][c]
                    if not val:
                        continue
                    # switch to a different face
                    add = val
                    for nf in range(6):
                        if nf == f:
                            continue
                        newdp[nf][1] = (newdp[nf][1] + add) % MOD
                    # stay on same face if allowed
                    if c + 1 <= maxc:
                        newdp[f][c + 1] = (newdp[f][c + 1] + val) % MOD
            dp = newdp

        ans = 0
        for f in range(6):
            ans = (ans + sum(dp[f])) % MOD
        return ans
```

## C

```c
#include <string.h>
#include <stdint.h>

int dieSimulator(int n, int* rollMax, int rollMaxSize) {
    const int MOD = 1000000007;
    static long long dp[2][6][16];
    memset(dp, 0, sizeof(dp));

    int cur = 0, nxt = 1;
    for (int f = 0; f < 6; ++f) {
        if (rollMax[f] >= 1)
            dp[cur][f][1] = 1;
    }

    for (int pos = 2; pos <= n; ++pos) {
        memset(dp[nxt], 0, sizeof(dp[nxt]));

        long long sumFace[6] = {0};
        for (int f = 0; f < 6; ++f) {
            for (int l = 1; l <= rollMax[f]; ++l) {
                sumFace[f] += dp[cur][f][l];
                if (sumFace[f] >= MOD) sumFace[f] -= MOD;
            }
        }

        long long totalPrev = 0;
        for (int f = 0; f < 6; ++f) {
            totalPrev += sumFace[f];
            if (totalPrev >= MOD) totalPrev -= MOD;
        }

        for (int nf = 0; nf < 6; ++nf) {
            long long add = totalPrev - sumFace[nf];
            if (add < 0) add += MOD;
            dp[nxt][nf][1] = add;

            for (int l = 1; l < rollMax[nf]; ++l) {
                dp[nxt][nf][l + 1] = dp[cur][nf][l];
            }
        }

        cur ^= 1;
        nxt ^= 1;
    }

    long long ans = 0;
    for (int f = 0; f < 6; ++f) {
        for (int l = 1; l <= rollMax[f]; ++l) {
            ans += dp[cur][f][l];
            if (ans >= MOD) ans -= MOD;
        }
    }

    return (int)ans;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public int DieSimulator(int n, int[] rollMax) {
        const int MOD = 1000000007;
        int maxR = 0;
        foreach (int v in rollMax) if (v > maxR) maxR = v;
        // dp[rolls][face][consecutive length]
        int[,,] dp = new int[n + 1, 6, maxR + 1];
        for (int f = 0; f < 6; f++) {
            dp[1, f, 1] = 1;
        }
        for (int i = 2; i <= n; i++) {
            long totalPrev = 0;
            for (int p = 0; p < 6; p++) {
                int limitP = rollMax[p];
                for (int len = 1; len <= limitP; len++) {
                    totalPrev += dp[i - 1, p, len];
                }
            }
            totalPrev %= MOD;
            for (int f = 0; f < 6; f++) {
                long sameFaceSum = 0;
                int limitF = rollMax[f];
                for (int len = 1; len <= limitF; len++) {
                    sameFaceSum += dp[i - 1, f, len];
                }
                sameFaceSum %= MOD;
                int startNew = (int)((totalPrev - sameFaceSum + MOD) % MOD);
                dp[i, f, 1] = startNew;
                for (int k = 2; k <= limitF; k++) {
                    dp[i, f, k] = dp[i - 1, f, k - 1];
                }
            }
        }
        long ans = 0;
        for (int f = 0; f < 6; f++) {
            int limit = rollMax[f];
            for (int len = 1; len <= limit; len++) {
                ans += dp[n, f, len];
            }
        }
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} rollMax
 * @return {number}
 */
var dieSimulator = function(n, rollMax) {
    const MOD = 1e9 + 7;
    // cur[face][cnt] = ways ending with 'face' repeated cnt times (cnt >=1)
    let cur = Array.from({length: 6}, (_, f) => {
        const arr = new Array(rollMax[f] + 1).fill(0);
        arr[1] = 1; // first roll can be any face once
        return arr;
    });

    for (let i = 1; i < n; ++i) { // already have i rolls, build i+1
        const nxt = Array.from({length: 6}, (_, f) => new Array(rollMax[f] + 1).fill(0));
        for (let last = 0; last < 6; ++last) {
            const maxLen = rollMax[last];
            const curArr = cur[last];
            for (let cnt = 1; cnt <= maxLen; ++cnt) {
                const val = curArr[cnt];
                if (!val) continue;
                // same face, increase count if allowed
                if (cnt < maxLen) {
                    nxt[last][cnt + 1] = (nxt[last][cnt + 1] + val) % MOD;
                }
                // switch to a different face
                for (let nf = 0; nf < 6; ++nf) {
                    if (nf === last) continue;
                    nxt[nf][1] = (nxt[nf][1] + val) % MOD;
                }
            }
        }
        cur = nxt;
    }

    let ans = 0;
    for (let f = 0; f < 6; ++f) {
        const arr = cur[f];
        for (let cnt = 1; cnt <= rollMax[f]; ++cnt) {
            ans = (ans + arr[cnt]) % MOD;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function dieSimulator(n: number, rollMax: number[]): number {
    const MOD = 1000000007;
    // Initialize dp for position 1
    let prev: number[][] = Array.from({ length: 6 }, (_, i) => new Array(rollMax[i] + 1).fill(0));
    for (let i = 0; i < 6; i++) {
        prev[i][1] = 1;
    }
    if (n === 1) return 6 % MOD;

    for (let pos = 2; pos <= n; pos++) {
        const faceSum = new Array(6).fill(0);
        let totalPrev = 0;
        // compute sums per face and overall total
        for (let f = 0; f < 6; f++) {
            let sum = 0;
            const arr = prev[f];
            for (let c = 1; c < arr.length; c++) {
                sum += arr[c];
                if (sum >= MOD) sum -= MOD;
            }
            faceSum[f] = sum;
            totalPrev += sum;
            if (totalPrev >= MOD) totalPrev -= MOD;
        }

        const next: number[][] = Array.from({ length: 6 }, (_, i) => new Array(rollMax[i] + 1).fill(0));
        for (let j = 0; j < 6; j++) {
            // start a new streak with face j
            let sumOther = totalPrev - faceSum[j];
            if (sumOther < 0) sumOther += MOD;
            next[j][1] = sumOther;

            // continue the same face if allowed
            const limit = rollMax[j];
            for (let cnt = 2; cnt <= limit; cnt++) {
                next[j][cnt] = prev[j][cnt - 1];
            }
        }

        prev = next;
    }

    let ans = 0;
    for (let f = 0; f < 6; f++) {
        const arr = prev[f];
        for (let c = 1; c < arr.length; c++) {
            ans += arr[c];
            if (ans >= MOD) ans -= MOD;
        }
    }
    return ans % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $rollMax
     * @return Integer
     */
    function dieSimulator($n, $rollMax) {
        $MOD = 1000000007;
        // dpPrev[face][len] = number of sequences ending with 'face' repeated 'len' times
        $dpPrev = [];
        for ($f = 0; $f < 6; $f++) {
            $maxLen = $rollMax[$f];
            $dpPrev[$f] = array_fill(0, $maxLen + 1, 0);
            $dpPrev[$f][1] = 1;
        }

        for ($pos = 2; $pos <= $n; $pos++) {
            $dpCurr = [];
            for ($f = 0; $f < 6; $f++) {
                $maxLen = $rollMax[$f];
                $dpCurr[$f] = array_fill(0, $maxLen + 1, 0);
            }

            for ($prevF = 0; $prevF < 6; $prevF++) {
                $maxPrevLen = $rollMax[$prevF];
                for ($len = 1; $len <= $maxPrevLen; $len++) {
                    $val = $dpPrev[$prevF][$len];
                    if ($val == 0) continue;

                    // Switch to a different face
                    for ($newF = 0; $newF < 6; $newF++) {
                        if ($newF == $prevF) continue;
                        $dpCurr[$newF][1] = ($dpCurr[$newF][1] + $val) % $MOD;
                    }

                    // Continue same face if allowed
                    if ($len + 1 <= $rollMax[$prevF]) {
                        $dpCurr[$prevF][$len + 1] = ($dpCurr[$prevF][$len + 1] + $val) % $MOD;
                    }
                }
            }

            $dpPrev = $dpCurr;
        }

        // Sum all possibilities
        $result = 0;
        for ($f = 0; $f < 6; $f++) {
            foreach ($dpPrev[$f] as $cnt) {
                $result = ($result + $cnt) % $MOD;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func dieSimulator(_ n: Int, _ rollMax: [Int]) -> Int {
        let MOD = 1_000_000_007
        var dp = [[Int]](repeating: [], count: 6)
        for i in 0..<6 {
            dp[i] = [Int](repeating: 0, count: rollMax[i] + 1)
            dp[i][1] = 1
        }
        if n == 1 {
            var ans = 0
            for i in 0..<6 { ans = (ans + dp[i][1]) % MOD }
            return ans
        }
        for _ in 2...n {
            var ndp = [[Int]](repeating: [], count: 6)
            for i in 0..<6 {
                ndp[i] = [Int](repeating: 0, count: rollMax[i] + 1)
            }
            for prev in 0..<6 {
                let maxPrev = rollMax[prev]
                if maxPrev == 0 { continue }
                for cnt in 1...maxPrev {
                    let val = dp[prev][cnt]
                    if val == 0 { continue }
                    // Continue same face
                    if cnt < maxPrev {
                        ndp[prev][cnt + 1] = (ndp[prev][cnt + 1] + val) % MOD
                    }
                    // Switch to a different face
                    for newFace in 0..<6 where newFace != prev {
                        ndp[newFace][1] = (ndp[newFace][1] + val) % MOD
                    }
                }
            }
            dp = ndp
        }
        var result = 0
        for i in 0..<6 {
            for cnt in 1...rollMax[i] {
                result = (result + dp[i][cnt]) % MOD
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun dieSimulator(n: Int, rollMax: IntArray): Int {
        val MOD = 1_000_000_007L
        if (n == 0) return 0
        val maxR = rollMax.maxOrNull()!!
        var prev = Array(6) { IntArray(maxR + 1) }
        var curr = Array(6) { IntArray(maxR + 1) }

        for (f in 0 until 6) {
            if (rollMax[f] >= 1) prev[f][1] = 1
        }

        for (step in 2..n) {
            val totalPrevFace = LongArray(6)
            for (f in 0 until 6) {
                var sum = 0L
                val limit = rollMax[f]
                for (c in 1..limit) {
                    sum += prev[f][c]
                }
                totalPrevFace[f] = sum % MOD
            }

            for (f in 0 until 6) {
                java.util.Arrays.fill(curr[f], 0)
            }

            for (f in 0 until 6) {
                var sumOther = 0L
                for (g in 0 until 6) {
                    if (g != f) sumOther += totalPrevFace[g]
                }
                curr[f][1] = (sumOther % MOD).toInt()
                val limit = rollMax[f]
                for (cnt in 2..limit) {
                    curr[f][cnt] = prev[f][cnt - 1]
                }
            }

            val temp = prev
            prev = curr
            curr = temp
        }

        var ans = 0L
        for (f in 0 until 6) {
            val limit = rollMax[f]
            for (c in 1..limit) {
                ans += prev[f][c]
            }
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int dieSimulator(int n, List<int> rollMax) {
    int maxRoll = rollMax.reduce((a, b) => a > b ? a : b);
    // dp[i][face][cnt] = number of sequences of length i ending with 'face' repeated cnt times
    List<List<List<int>>> dp = List.generate(
        n + 1,
        (_) => List.generate(6, (_) => List.filled(maxRoll + 1, 0)));

    // initialization for first roll
    for (int f = 0; f < 6; ++f) {
      dp[1][f][1] = 1;
    }

    for (int i = 2; i <= n; ++i) {
      // total sequences of length i-1
      int totalPrev = 0;
      for (int f = 0; f < 6; ++f) {
        for (int c = 1; c <= rollMax[f]; ++c) {
          totalPrev += dp[i - 1][f][c];
          if (totalPrev >= _mod) totalPrev -= _mod;
        }
      }

      for (int cur = 0; cur < 6; ++cur) {
        // sequences where previous face is the same as current
        int samePrev = 0;
        for (int c = 1; c <= rollMax[cur]; ++c) {
          samePrev += dp[i - 1][cur][c];
          if (samePrev >= _mod) samePrev -= _mod;
        }

        // start a new block of current face
        int val = totalPrev - samePrev;
        if (val < 0) val += _mod;
        dp[i][cur][1] = val;

        // continue the same face block
        for (int cnt = 2; cnt <= rollMax[cur]; ++cnt) {
          dp[i][cur][cnt] = dp[i - 1][cur][cnt - 1];
        }
      }
    }

    int ans = 0;
    for (int f = 0; f < 6; ++f) {
      for (int c = 1; c <= rollMax[f]; ++c) {
        ans += dp[n][f][c];
        if (ans >= _mod) ans -= _mod;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func dieSimulator(n int, rollMax []int) int {
	const MOD int64 = 1e9 + 7
	// dpPrev[face][cnt] = number of sequences ending with 'face' having 'cnt' consecutive rolls
	dpPrev := make([][]int64, 6)
	for f := 0; f < 6; f++ {
		dpPrev[f] = make([]int64, rollMax[f]+1) // index 0 unused
		dpPrev[f][1] = 1
	}
	if n == 1 {
		var ans int64
		for f := 0; f < 6; f++ {
			ans += dpPrev[f][1]
		}
		return int(ans % MOD)
	}
	for step := 2; step <= n; step++ {
		dpCurr := make([][]int64, 6)
		for f := 0; f < 6; f++ {
			dpCurr[f] = make([]int64, rollMax[f]+1)
		}
		for prevFace := 0; prevFace < 6; prevFace++ {
			maxCntPrev := rollMax[prevFace]
			for cnt := 1; cnt <= maxCntPrev; cnt++ {
				val := dpPrev[prevFace][cnt]
				if val == 0 {
					continue
				}
				for newFace := 0; newFace < 6; newFace++ {
					if newFace == prevFace {
						if cnt+1 <= rollMax[newFace] {
							dpCurr[newFace][cnt+1] = (dpCurr[newFace][cnt+1] + val) % MOD
						}
					} else {
						dpCurr[newFace][1] = (dpCurr[newFace][1] + val) % MOD
					}
				}
			}
		}
		dpPrev = dpCurr
	}
	var ans int64
	for f := 0; f < 6; f++ {
		for cnt := 1; cnt <= rollMax[f]; cnt++ {
			ans += dpPrev[f][cnt]
			if ans >= MOD {
				ans -= MOD
			}
		}
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

# @param {Integer} n
# @param {Integer[]} roll_max
# @return {Integer}
def die_simulator(n, roll_max)
  # dp for position 1
  prev = Array.new(6) { |i| Array.new(roll_max[i] + 1, 0) }
  (0..5).each { |f| prev[f][1] = 1 }

  if n == 1
    return 6 % MOD
  end

  (2..n).each do |_pos|
    # total sequences of previous length
    total_prev = 0
    prev.each do |arr|
      arr.each { |v| total_prev += v }
    end
    total_prev %= MOD

    cur = Array.new(6) { |i| Array.new(roll_max[i] + 1, 0) }

    (0..5).each do |f|
      max_c = roll_max[f]
      # sum of sequences ending with face f in previous step
      same_face_sum = prev[f].reduce(0) { |s, v| (s + v) % MOD }
      cur[f][1] = (total_prev - same_face_sum) % MOD

      (2..max_c).each do |c|
        cur[f][c] = prev[f][c - 1]
      end
    end

    prev = cur
  end

  ans = 0
  prev.each { |arr| arr.each { |v| ans += v } }
  ans % MOD
end
```

## Scala

```scala
object Solution {
  def dieSimulator(n: Int, rollMax: Array[Int]): Int = {
    val MOD = 1000000007L
    val maxRoll = 15
    var dpPrev = Array.ofDim[Long](6, maxRoll + 1)
    for (face <- 0 until 6) dpPrev(face)(1) = 1L

    var pos = 2
    while (pos <= n) {
      // total sequences ending with each face regardless of consecutive length
      val totalFace = new Array[Long](6)
      var sumAll = 0L
      for (face <- 0 until 6) {
        var s = 0L
        var len = 1
        while (len <= rollMax(face)) {
          s += dpPrev(face)(len)
          if (s >= MOD) s -= MOD
          len += 1
        }
        totalFace(face) = s
        sumAll += s
        if (sumAll >= MOD) sumAll -= MOD
      }

      val dpCurr = Array.ofDim[Long](6, maxRoll + 1)
      for (nf <- 0 until 6) {
        // continue same face
        var len = 1
        while (len < rollMax(nf)) { // can extend up to limit-1
          val v = dpPrev(nf)(len)
          if (v != 0) {
            var nv = dpCurr(nf)(len + 1) + v
            if (nv >= MOD) nv -= MOD
            dpCurr(nf)(len + 1) = nv
          }
          len += 1
        }
        // switch from other faces
        var sumOther = sumAll - totalFace(nf)
        if (sumOther < 0) sumOther += MOD
        var cur = dpCurr(nf)(1) + sumOther
        if (cur >= MOD) cur -= MOD
        dpCurr(nf)(1) = cur
      }

      dpPrev = dpCurr
      pos += 1
    }

    var ans = 0L
    for (face <- 0 until 6) {
      var len = 1
      while (len <= rollMax(face)) {
        ans += dpPrev(face)(len)
        if (ans >= MOD) ans -= MOD
        len += 1
      }
    }
    (ans % MOD).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn die_simulator(n: i32, roll_max: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n_usize = n as usize;
        // maximum possible rollMax per constraints
        const MAX_R: usize = 15;
        // dp[pos][face][cnt] where cnt starts from 1
        let mut dp = vec![vec![vec![0i64; MAX_R + 1]; 6]; n_usize + 1];
        for f in 0..6 {
            dp[1][f][1] = 1;
        }
        for pos in 1..n_usize {
            for f in 0..6 {
                let limit_f = roll_max[f] as usize;
                for cnt in 1..=limit_f {
                    let cur = dp[pos][f][cnt];
                    if cur == 0 {
                        continue;
                    }
                    // Continue with the same face
                    if cnt < limit_f {
                        let nxt_cnt = cnt + 1;
                        dp[pos + 1][f][nxt_cnt] =
                            (dp[pos + 1][f][nxt_cnt] + cur) % MOD;
                    }
                    // Switch to a different face
                    for nf in 0..6 {
                        if nf == f {
                            continue;
                        }
                        dp[pos + 1][nf][1] = (dp[pos + 1][nf][1] + cur) % MOD;
                    }
                }
            }
        }
        let mut ans: i64 = 0;
        for f in 0..6 {
            let limit_f = roll_max[f] as usize;
            for cnt in 1..=limit_f {
                ans = (ans + dp[n_usize][f][cnt]) % MOD;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (die-simulator n rollMax)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((rm (list->vector rollMax))
         (faces 6)
         (cur (for/vector ([f faces])
                (make-vector (+ (vector-ref rm f) 1) 0))))
    ;; first roll
    (for ([f faces])
      (vector-set! (vector-ref cur f) 1 1))
    ;; DP transitions for positions 2..n
    (for ([pos (in-range 2 (+ n 1))])
      (let ((nxt (for/vector ([f faces])
                   (make-vector (+ (vector-ref rm f) 1) 0))))
        (for ([f faces])
          (let* ((vec (vector-ref cur f))
                 (maxc (vector-ref rm f)))
            (for ([cnt (in-range 1 (+ maxc 1))])
              (define val (vector-ref vec cnt))
              (when (> val 0)
                ;; extend same face
                (when (< cnt maxc)
                  (let ((dest (vector-ref nxt f)))
                    (vector-set! dest (+ cnt 1)
                                 (modulo (+ (vector-ref dest (+ cnt 1)) val) MOD))))
                ;; switch to other faces
                (for ([g faces])
                  (unless (= g f)
                    (let ((dest (vector-ref nxt g)))
                      (vector-set! dest 1
                                   (modulo (+ (vector-ref dest 1) val) MOD)))))))))
        (set! cur nxt)))
    ;; sum all possibilities
    (let ((ans 0))
      (for ([f faces])
        (let ((vec (vector-ref cur f)))
          (for ([i (in-range 1 (vector-length vec))])
            (set! ans (modulo (+ ans (vector-ref vec i)) MOD)))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([die_simulator/2]).

-define(MOD, 1000000007).

die_simulator(N, RollMax) ->
    RollMaxTuple = list_to_tuple(RollMax),
    InitMap = init_map(),
    case N of
        1 -> 6;
        _ ->
            FinalMap = loop(2, N, InitMap, RollMaxTuple),
            maps:fold(fun(_K, V, Acc) -> (Acc + V) rem ?MOD end, 0, FinalMap)
    end.

init_map() ->
    lists:foldl(fun(F, Acc) -> maps:put({F,1}, 1, Acc) end,
                maps:new(),
                lists:seq(1,6)).

loop(Pos, N, CurrMap, RollMaxTuple) when Pos =< N ->
    NewMap = transition(CurrMap, RollMaxTuple),
    loop(Pos+1, N, NewMap, RollMaxTuple);
loop(_Pos, _N, CurrMap, _RollMaxTuple) ->
    CurrMap.

transition(CurrMap, RollMaxTuple) ->
    maps:fold(fun({F,R}, Val, Acc) ->
        MaxF = element(F, RollMaxTuple),
        Acc1 = if R < MaxF -> add(Acc, {F,R+1}, Val); true -> Acc end,
        lists:foldl(fun(G, A) when G =/= F ->
                add(A, {G,1}, Val)
            end, Acc1, lists:seq(1,6))
    end, maps:new(), CurrMap).

add(Map, Key, AddVal) ->
    Old = maps:get(Key, Map, 0),
    New = (Old + AddVal) rem ?MOD,
    maps:put(Key, New, Map).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec die_simulator(n :: integer, roll_max :: [integer]) :: integer
  def die_simulator(n, roll_max) do
    mod = 1_000_000_007

    # DP for position 1: each face can appear once
    init_dp =
      Enum.map(0..5, fn i ->
        max_len = Enum.at(roll_max, i)
        arr = List.duplicate(0, max_len + 1)
        List.replace_at(arr, 1, 1)
      end)

    dp =
      if n == 1 do
        init_dp
      else
        Enum.reduce(2..n, init_dp, fn _pos, dp_prev ->
          # total sequences ending with each face (any run length)
          totals = Enum.map(dp_prev, &Enum.sum/1)

          new_dp =
            Enum.map(0..5, fn f ->
              max_len = Enum.at(roll_max, f)
              arr = List.duplicate(0, max_len + 1)

              # sequences where current face starts a new run
              other_sum =
                Enum.reduce(0..5, 0, fn g, acc ->
                  if g != f do
                    (acc + Enum.at(totals, g)) |> rem(mod)
                  else
                    acc
                  end
                end)

              arr = List.replace_at(arr, 1, other_sum)

              # extend previous runs of the same face
              face_prev = Enum.at(dp_prev, f)

              arr =
                Enum.reduce(2..max_len, arr, fn c, a ->
                  prev_val = Enum.at(face_prev, c - 1)
                  List.replace_at(a, c, rem(prev_val, mod))
                end)

              arr
            end)

          new_dp
        end)
      end

    dp
    |> Enum.flat_map(& &1)
    |> Enum.reduce(0, fn x, acc -> (acc + x) |> rem(mod) end)
  end
end
```
