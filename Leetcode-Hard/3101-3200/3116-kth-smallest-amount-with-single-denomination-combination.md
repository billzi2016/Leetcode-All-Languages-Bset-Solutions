# 3116. Kth Smallest Amount With Single Denomination Combination

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        int n = coins.size();
        int totalMask = 1 << n;
        vector<long long> lcm(totalMask, 0);
        lcm[0] = 1;
        for (int mask = 1; mask < totalMask; ++mask) {
            int b = __builtin_ctz(mask);               // lowest set bit
            int prev = mask ^ (1 << b);
            long long prevL = lcm[prev];
            long long d = coins[b];
            long long g = std::gcd(prevL, d);
            long long cur = prevL / g * d;
            if (cur < 0 || cur > (long long)4e18) cur = (long long)4e18; // safeguard
            lcm[mask] = cur;
        }

        auto countUpTo = [&](long long x) -> long long {
            long long cnt = 0;
            for (int mask = 1; mask < totalMask; ++mask) {
                if (lcm[mask] == 0) continue;
                long long add = x / lcm[mask];
                if (__builtin_popcount(mask) & 1)
                    cnt += add;
                else
                    cnt -= add;
            }
            return cnt;
        };

        int minCoin = *min_element(coins.begin(), coins.end());
        long long low = 1, high = (long long)minCoin * k; // inclusive upper bound

        while (low < high) {
            long long mid = low + (high - low) / 2;
            if (countUpTo(mid) >= k)
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public long findKthSmallest(int[] coins, int k) {
        int n = coins.length;
        long minCoin = Long.MAX_VALUE;
        for (int c : coins) if (c < minCoin) minCoin = c;
        long low = 1;
        long high = minCoin * (long) k; // upper bound
        while (low < high) {
            long mid = low + (high - low) / 2;
            if (count(mid, coins, n) >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private long count(long x, int[] coins, int n) {
        long cnt = 0;
        int totalMasks = 1 << n;
        for (int mask = 1; mask < totalMasks; ++mask) {
            long lcm = 1;
            boolean overflow = false;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    int c = coins[i];
                    long g = gcd(lcm, c);
                    long tmp = lcm / g;
                    // check overflow: tmp * c > x ?
                    if (tmp > x / c) {
                        overflow = true;
                        break;
                    }
                    lcm = tmp * c;
                }
            }
            if (!overflow && lcm <= x) {
                long add = x / lcm;
                if ((Integer.bitCount(mask) & 1) == 1) {
                    cnt += add;
                } else {
                    cnt -= add;
                }
            }
        }
        return cnt;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        from math import gcd

        n = len(coins)
        total_masks = 1 << n
        lcm_sub = [0] * total_masks
        bits_cnt = [0] * total_masks

        for mask in range(1, total_masks):
            # isolate lowest set bit
            lowbit = mask & -mask
            i = (lowbit.bit_length() - 1)  # index of that bit
            prev = mask ^ lowbit
            if prev == 0:
                lcm_sub[mask] = coins[i]
            else:
                a = lcm_sub[prev]
                b = coins[i]
                g = gcd(a, b)
                # avoid overflow (Python handles big ints)
                lcm_sub[mask] = a // g * b
            bits_cnt[mask] = bits_cnt[prev] + 1

        def count(x):
            total = 0
            for mask in range(1, total_masks):
                l = lcm_sub[mask]
                if l == 0:
                    continue
                cnt = x // l
                if bits_cnt[mask] & 1:
                    total += cnt
                else:
                    total -= cnt
            return total

        lo = 1
        hi = min(coins) * k  # safe upper bound
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        min_coin = min(coins)

        def count_upto(x: int) -> int:
            total = 0
            for mask in range(1, 1 << n):
                l = 1
                bits = mask
                idx = 0
                overflow = False
                while bits:
                    if bits & 1:
                        d = coins[idx]
                        g = math.gcd(l, d)
                        l = l // g * d
                        if l > x:
                            overflow = True
                            break
                    idx += 1
                    bits >>= 1
                if overflow:
                    continue
                add = x // l
                if mask.bit_count() & 1:   # odd size -> add
                    total += add
                else:                       # even size -> subtract
                    total -= add
            return total

        low, high = 1, k * min_coin
        while low < high:
            mid = (low + high) // 2
            if count_upto(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
```

## C

```c
#include <stddef.h>
#include <stdint.h>

static long long gcd_ll(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

/* compute lcm of a and b, but if it exceeds limit, return limit+1 */
static long long lcm_limit(long long a, long long b, long long limit) {
    long long g = gcd_ll(a, b);
    __int128 mul = (__int128)(a / g) * (__int128)b;
    if (mul > (__int128)limit) return limit + 1;
    return (long long)mul;
}

/* count numbers <= x that are divisible by at least one coin */
static long long count_up_to(long long x, int *coins, int n) {
    long long total = 0;
    int subsets = 1 << n;
    for (int mask = 1; mask < subsets; ++mask) {
        long long l = 1;
        int bits = __builtin_popcount((unsigned)mask);
        bool overflow = false;
        for (int i = 0; i < n; ++i) if (mask & (1 << i)) {
            l = lcm_limit(l, (long long)coins[i], x);
            if (l > x) { overflow = true; break; }
        }
        if (overflow) continue;
        long long add = x / l;
        if (bits & 1) total += add;
        else total -= add;
    }
    return total;
}

long long findKthSmallest(int* coins, int coinsSize, int k) {
    long long minCoin = coins[0];
    for (int i = 1; i < coinsSize; ++i)
        if ((long long)coins[i] < minCoin) minCoin = coins[i];

    long long low = 1;
    long long high = minCoin * (long long)k; // upper bound

    while (low < high) {
        long long mid = low + (high - low) / 2;
        if (count_up_to(mid, coins, coinsSize) >= k)
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution {
    private int n;
    private long[] lcms;
    private const long INF = long.MaxValue;

    private static long Gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private static long Lcm(long a, long b) {
        if (a == INF || b == INF) return INF;
        long g = Gcd(a, b);
        // check overflow: a/g * b
        long div = a / g;
        if (div > INF / b) return INF;
        return div * b;
    }

    private void PrecomputeLCMs(int[] coins) {
        int maxMask = 1 << n;
        lcms = new long[maxMask];
        for (int mask = 1; mask < maxMask; ++mask) {
            int lsb = mask & -mask;
            int idx = BitOperations.TrailingZeroCount((uint)lsb);
            int prev = mask ^ lsb;
            if (prev == 0) {
                lcms[mask] = coins[idx];
            } else {
                lcms[mask] = Lcm(lcms[prev], coins[idx]);
            }
        }
    }

    private long CountUpTo(long x) {
        long total = 0;
        int maxMask = 1 << n;
        for (int mask = 1; mask < maxMask; ++mask) {
            long l = lcms[mask];
            if (l == 0 || l > x) continue;
            long add = x / l;
            int bits = BitOperations.PopCount((uint)mask);
            if ((bits & 1) == 1) total += add;
            else total -= add;
        }
        return total;
    }

    public long FindKthSmallest(int[] coins, int k) {
        n = coins.Length;
        Array.Sort(coins);
        PrecomputeLCMs(coins);

        long minCoin = coins[0];
        long low = 1;
        long high = minCoin * (long)k; // guaranteed upper bound

        while (low < high) {
            long mid = low + (high - low) / 2;
            if (CountUpTo(mid) >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} coins
 * @param {number} k
 * @return {number}
 */
var findKthSmallest = function(coins, k) {
    const n = coins.length;
    const totalMask = 1 << n;

    // precompute lcm for each subset and its sign (+1 for odd size, -1 for even)
    const lcms = new Array(totalMask).fill(0);
    const bitsCnt = new Array(totalMask).fill(0);
    const signs = new Array(totalMask).fill(0);

    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    for (let mask = 1; mask < totalMask; ++mask) {
        const lowbit = mask & -mask;
        let idx = 0;
        while (((lowbit >> idx) & 1) === 0) idx++; // index of the added coin

        const prevMask = mask ^ lowbit;
        bitsCnt[mask] = bitsCnt[prevMask] + 1;
        signs[mask] = (bitsCnt[mask] % 2 === 1) ? 1 : -1;

        if (prevMask === 0) {
            lcms[mask] = coins[idx];
        } else {
            const prevLcm = lcms[prevMask];
            const curCoin = coins[idx];
            const g = gcd(prevLcm, curCoin);
            // safe multiplication within Number range
            let newLcm = (prevLcm / g) * curCoin;
            if (newLcm > Number.MAX_SAFE_INTEGER) newLcm = Number.MAX_SAFE_INTEGER;
            lcms[mask] = newLcm;
        }
    }

    const countUpTo = (x) => {
        let cnt = 0;
        for (let mask = 1; mask < totalMask; ++mask) {
            const l = lcms[mask];
            if (l > x) continue;
            cnt += signs[mask] * Math.floor(x / l);
        }
        return cnt;
    };

    const minCoin = Math.min(...coins);
    let low = 1;
    let high = minCoin * k; // safe upper bound

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (countUpTo(mid) >= k) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function findKthSmallest(coins: number[], k: number): number {
    const n = coins.length;
    const minCoin = Math.min(...coins);
    let low = 1;
    let high = minCoin * k; // safe upper bound

    function gcd(a: number, b: number): number {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    function lcmLimited(a: number, b: number, limit: number): number {
        const g = gcd(a, b);
        const div = a / g;
        if (div > Math.floor(limit / b)) return limit + 1; // overflow beyond limit
        return div * b;
    }

    function countUpTo(x: number): number {
        let total = 0;
        const limit = x;
        const masks = 1 << n;
        for (let mask = 1; mask < masks; ++mask) {
            let l = 1;
            let bits = 0;
            for (let i = 0; i < n; ++i) {
                if ((mask >> i) & 1) {
                    bits++;
                    l = lcmLimited(l, coins[i], limit);
                    if (l > limit) break;
                }
            }
            if (l > limit) continue;
            const cnt = Math.floor(x / l);
            if (bits & 1) total += cnt;
            else total -= cnt;
        }
        return total;
    }

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (countUpTo(mid) >= k) high = mid;
        else low = mid + 1;
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $coins
     * @param Integer $k
     * @return Integer
     */
    function findKthSmallest($coins, $k) {
        sort($coins);
        $n = count($coins);
        $minCoin = $coins[0];
        $low = 1;
        $high = $minCoin * $k; // upper bound

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->countUpTo($mid, $coins, $n) >= $k) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }

    private function countUpTo($x, $coins, $n) {
        $size = 1 << $n;
        $lcmArr = array_fill(0, $size, 0);
        $bitsArr = array_fill(0, $size, 0);
        $total = 0;

        for ($mask = 1; $mask < $size; $mask++) {
            $leastBit = $mask & (-$mask);
            $prevMask = $mask ^ $leastBit;
            $bitsArr[$mask] = $bitsArr[$prevMask] + 1;

            // find index of the least significant set bit
            $idx = 0;
            while ((($leastBit >> $idx) & 1) == 0) {
                $idx++;
            }

            $prevLcm = $lcmArr[$prevMask];
            if ($prevLcm == 0) {
                $currLcm = $coins[$idx];
            } else {
                $g = $this->gcd($prevLcm, $coins[$idx]);
                $aDivG = intdiv($prevLcm, $g);
                // overflow / exceed x check
                if ($aDivG > 0 && $aDivG <= intdiv($x, $coins[$idx])) {
                    $currLcm = $aDivG * $coins[$idx];
                    if ($currLcm > $x) {
                        $currLcm = $x + 1;
                    }
                } else {
                    $currLcm = $x + 1; // treat as infinity
                }
            }

            $lcmArr[$mask] = $currLcm;

            if ($currLcm > $x || $currLcm == 0) continue;
            $cnt = intdiv($x, $currLcm);
            if (($bitsArr[$mask] & 1) == 1) {
                $total += $cnt;
            } else {
                $total -= $cnt;
            }
        }

        return $total;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func findKthSmallest(_ coins: [Int], _ k: Int) -> Int {
        let n = coins.count
        let totalMask = 1 << n
        var lcms = [UInt64](repeating: 0, count: totalMask)
        var signs = [Int](repeating: 0, count: totalMask)
        let overflowLimit: UInt64 = UInt64.max / 2

        func gcd(_ a: UInt64, _ b: UInt64) -> UInt64 {
            var x = a, y = b
            while y != 0 {
                let temp = x % y
                x = y
                y = temp
            }
            return x
        }

        for mask in 1..<totalMask {
            let lowbit = mask & -mask
            let idx = Int(log2(Double(lowbit)))   // alternative: trailingZeroBitCount
            // Using trailingZeroBitCount is more reliable
            // let idx = lowbit.trailingZeroBitCount

            let prev = mask ^ lowbit
            if prev == 0 {
                lcms[mask] = UInt64(coins[idx])
            } else {
                let a = lcms[prev]
                let b = UInt64(coins[idx])
                let g = gcd(a, b)
                var part = a / g
                if part > overflowLimit / b {
                    lcms[mask] = overflowLimit
                } else {
                    lcms[mask] = part * b
                }
            }
            signs[mask] = (mask.nonzeroBitCount % 2 == 1) ? 1 : -1
        }

        func count(_ x: UInt64) -> UInt64 {
            var total: Int64 = 0
            for mask in 1..<totalMask {
                let l = lcms[mask]
                if l == 0 || l > x { continue }
                let term = Int64(x / l)
                total += Int64(signs[mask]) * term
            }
            return UInt64(total)
        }

        let minCoin = coins.min()!
        var low: UInt64 = 1
        var high: UInt64 = UInt64(minCoin) * UInt64(k)

        while low < high {
            let mid = (low + high) >> 1
            if count(mid) >= UInt64(k) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return Int(low)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKthSmallest(coins: IntArray, k: Int): Long {
        val coinVals = coins.map { it.toLong() }.toLongArray()
        var minCoin = coinVals.minOrNull() ?: 1L
        var low = 1L
        var high = minCoin * k.toLong()
        while (low < high) {
            val mid = (low + high) / 2
            if (count(mid, coinVals) >= k.toLong()) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private fun count(x: Long, coins: LongArray): Long {
        val n = coins.size
        var total = 0L
        val limitMask = 1 shl n
        for (mask in 1 until limitMask) {
            var lcm = 1L
            var bits = 0
            var valid = true
            var m = mask
            var idx = 0
            while (m != 0) {
                if ((m and 1) == 1) {
                    bits++
                    val c = coins[idx]
                    val g = gcd(lcm, c)
                    val tmp = lcm / g
                    if (tmp > x / c) { // lcm would exceed x
                        valid = false
                        break
                    }
                    lcm = tmp * c
                    if (lcm > x) {
                        valid = false
                        break
                    }
                }
                idx++
                m = m shr 1
            }
            if (!valid) continue
            val cnt = x / lcm
            if ((bits and 1) == 1) total += cnt else total -= cnt
        }
        return total
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int findKthSmallest(List<int> coins, int k) {
    int n = coins.length;
    int totalMasks = 1 << n;

    // Precompute LCM for each subset and parity (odd/even size)
    List<int> lcms = List.filled(totalMasks, 0);
    List<bool> oddCount = List.filled(totalMasks, false);

    for (int mask = 1; mask < totalMasks; ++mask) {
      int least = mask & -mask;
      int i = least.bitLength - 1; // index of the added coin
      int prev = mask ^ least;

      int l = lcms[prev];
      int d = coins[i];
      if (l == 0) {
        l = d;
      } else {
        int g = _gcd(l, d);
        l = (l ~/ g) * d; // safe within constraints
      }
      lcms[mask] = l;
      oddCount[mask] = !oddCount[prev]; // toggle parity
    }

    int minCoin = coins.reduce((a, b) => a < b ? a : b);
    int low = 1;
    int high = minCoin * k; // upper bound sufficient

    while (low < high) {
      int mid = low + ((high - low) >> 1);
      if (_countUpTo(mid, lcms, oddCount) >= k) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }

  int _countUpTo(int x, List<int> lcms, List<bool> oddCount) {
    int total = 0;
    for (int mask = 1; mask < lcms.length; ++mask) {
      int l = lcms[mask];
      if (l == 0 || l > x) continue;
      int cnt = x ~/ l;
      if (oddCount[mask]) {
        total += cnt;
      } else {
        total -= cnt;
      }
    }
    return total;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func findKthSmallest(coins []int, k int) int64 {
	n := len(coins)
	minCoin := coins[0]
	for _, c := range coins {
		if c < minCoin {
			minCoin = c
		}
	}

	gcd := func(a, b int64) int64 {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	count := func(x int64) int64 {
		var total int64 = 0
		limitMask := 1 << n
		for mask := 1; mask < limitMask; mask++ {
			lcm := int64(1)
			overflow := false
			for i := 0; i < n; i++ {
				if (mask>>i)&1 == 1 {
					d := int64(coins[i])
					g := gcd(lcm, d)
					tmp := lcm / g
					if tmp > x/d { // would exceed x
						overflow = true
						break
					}
					lcm = tmp * d
				}
			}
			if overflow || lcm == 0 {
				continue
			}
			bitsCnt := bits.OnesCount(uint(mask))
			add := x / lcm
			if bitsCnt%2 == 1 {
				total += add
			} else {
				total -= add
			}
		}
		return total
	}

	low, high := int64(1), int64(minCoin)*int64(k)
	for low < high {
		mid := (low + high) / 2
		if count(mid) >= int64(k) {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}
```

## Ruby

```ruby
def find_kth_smallest(coins, k)
  n = coins.length
  min_coin = coins.min
  # count numbers <= x that are divisible by at least one coin
  count = lambda do |x|
    total = 0
    (1...(1 << n)).each do |mask|
      l = 1
      bits = 0
      i = 0
      while i < n
        if (mask & (1 << i)) != 0
          bits += 1
          c = coins[i]
          g = l.gcd(c)
          l = l / g * c
          break if l > x
        end
        i += 1
      end
      next if l > x
      cur = x / l
      total += (bits.odd? ? cur : -cur)
    end
    total
  end

  low = 1
  high = min_coin * k
  while low < high
    mid = (low + high) >> 1
    if count.call(mid) >= k
      high = mid
    else
      low = mid + 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
    def findKthSmallest(coins: Array[Int], k: Int): Long = {
        val n = coins.length
        val totalMask = 1 << n
        val lcms = new Array[Long](totalMask)

        for (mask <- 1 until totalMask) {
            val lsb = mask & -mask
            val idx = Integer.numberOfTrailingZeros(lsb)
            val prev = mask ^ lsb
            if (prev == 0) {
                lcms(mask) = coins(idx).toLong
            } else {
                val a = lcms(prev)
                val b = coins(idx).toLong
                val g = gcd(a, b)
                lcms(mask) = a / g * b
            }
        }

        def count(x: Long): Long = {
            var res = 0L
            for (mask <- 1 until totalMask) {
                val l = lcms(mask)
                if (l <= x && l > 0) {
                    val bits = Integer.bitCount(mask)
                    val add = x / l
                    if ((bits & 1) == 1) res += add else res -= add
                }
            }
            res
        }

        var low: Long = 1L
        var high: Long = coins.max.toLong * k.toLong

        while (low < high) {
            val mid = (low + high) >>> 1
            if (count(mid) >= k) high = mid else low = mid + 1
        }
        low
    }

    @annotation.tailrec
    private def gcd(a: Long, b: Long): Long = {
        if (b == 0) a.abs else gcd(b, a % b)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_kth_smallest(coins: Vec<i32>, k: i32) -> i64 {
        let n = coins.len();
        let mut c: Vec<i64> = coins.iter().map(|&x| x as i64).collect();

        // helper gcd for i128
        fn gcd_i128(mut a: i128, mut b: i128) -> i128 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            if a < 0 { -a } else { a }
        }

        // count numbers <= x that are multiples of at least one coin
        fn count(x: i64, c: &Vec<i64>, n: usize) -> i64 {
            let mut total: i64 = 0;
            for mask in 1usize..(1usize << n) {
                let mut bits = 0i32;
                let mut lcm_val: i128 = 1;
                for i in 0..n {
                    if (mask >> i) & 1 == 1 {
                        bits += 1;
                        let d = c[i] as i128;
                        let g = gcd_i128(lcm_val, d);
                        lcm_val = lcm_val / g * d;
                        if lcm_val > x as i128 {
                            break;
                        }
                    }
                }
                if lcm_val > x as i128 {
                    continue;
                }
                let cnt = (x as i128) / lcm_val;
                if bits % 2 == 1 {
                    total += cnt as i64;
                } else {
                    total -= cnt as i64;
                }
            }
            total
        }

        let max_coin = *c.iter().max().unwrap();
        let mut low: i64 = 1;
        let mut high: i64 = max_coin * k as i64; // upper bound

        while low < high {
            let mid = low + (high - low) / 2;
            if count(mid, &c, n) >= k as i64 {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        low
    }
}
```

## Racket

```racket
#lang racket

(define (gcd a b)
  (if (= b 0) a (gcd b (remainder a b))))

(define (lcm2 a b)
  (/ (* a b) (gcd a b)))

;; Preprocess all non‑empty subsets: store (lcm . sign) where sign = +1 for odd size, -1 for even size
(define (preprocess coins)
  (let* ([n (length coins)]
         [limit (arithmetic-shift 1 n)])
    (for/list ([mask (in-range 1 limit)])
      (let loop-sub ((i 0) (m mask) (lcm-val 1) (bits 0))
        (if (= i n)
            (cons lcm-val (if (odd? bits) 1 -1))
            (if (zero? (bitwise-and m 1))
                (loop-sub (+ i 1) (arithmetic-shift m -1) lcm-val bits)
                (let ([new-lcm (lcm2 lcm-val (list-ref coins i))])
                  (loop-sub (+ i 1) (arithmetic-shift m -1) new-lcm (+ bits 1)))))))))

;; Count numbers ≤ x that are divisible by at least one coin using inclusion‑exclusion
(define (count-up-to x pre)
  (for/sum ([pair pre])
    (* (cdr pair) (quotient x (car pair)))))

(define/contract (find-kth-smallest coins k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([pre (preprocess coins)]
         [minc (apply min coins)]
         [high (* minc k)]) ; answer never exceeds this
    (let loop ((low 1) (high high))
      (if (= low high)
          low
          (let* ([mid (quotient (+ low high) 2)]
                 [cnt (count-up-to mid pre)])
            (if (>= cnt k)
                (loop low mid)
                (loop (+ mid 1) high)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_kth_smallest/2]).

-spec find_kth_smallest(Coins :: [integer()], K :: integer()) -> integer().
find_kth_smallest(Coins, K) ->
    Sorted = lists:sort(Coins),
    MinCoin = hd(Sorted),
    Subsets = build_subsets(Sorted),
    Upper = K * MinCoin,
    binary_search(1, Upper, K, Subsets).

binary_search(Low, High, K, Subsets) when Low < High ->
    Mid = (Low + High) div 2,
    Cnt = count_upto(Mid, Subsets),
    if
        Cnt >= K -> binary_search(Low, Mid, K, Subsets);
        true     -> binary_search(Mid + 1, High, K, Subsets)
    end;
binary_search(Low, _High, _K, _Subsets) ->
    Low.

count_upto(X, Subsets) ->
    lists:foldl(fun({Lcm, Sign}, Acc) ->
        Acc + Sign * (X div Lcm)
    end, 0, Subsets).

build_subsets(Coins) ->
    N = length(Coins),
    MaxMask = (1 bsl N) - 1,
    build_subsets(1, MaxMask, Coins, []).

build_subsets(Mask, MaxMask, _Coins, Acc) when Mask > MaxMask ->
    Acc;
build_subsets(Mask, MaxMask, Coins, Acc) ->
    Lcm = lcm_of_mask(Mask, Coins),
    Bits = bit_count(Mask),
    Sign = if Bits rem 2 == 1 -> 1; true -> -1 end,
    build_subsets(Mask + 1, MaxMask, Coins, [{Lcm, Sign} | Acc]).

lcm_of_mask(Mask, Coins) ->
    lcm_of_mask(Mask, Coins, 0, 1).

lcm_of_mask(_Mask, [], _Idx, Acc) -> Acc;
lcm_of_mask(Mask, [C|Rest], Idx, Acc) ->
    case (Mask band (1 bsl Idx)) of
        0 -> lcm_of_mask(Mask, Rest, Idx + 1, Acc);
        _ -> NewAcc = lcm(Acc, C),
             lcm_of_mask(Mask, Rest, Idx + 1, NewAcc)
    end.

lcm(A, B) ->
    A div gcd(A, B) * B.

gcd(0, B) -> B;
gcd(A, 0) -> A;
gcd(A, B) when A < B -> gcd(B, A);
gcd(A, B) -> gcd(B, A rem B).

bit_count(0) -> 0;
bit_count(N) -> 1 + bit_count(N band (N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec find_kth_smallest(coins :: [integer], k :: integer) :: integer
  def find_kth_smallest(coins, k) do
    subsets = build_subsets(coins)
    max_coin = Enum.max(coins)
    low = 1
    high = max_coin * k
    binary_search(low, high, k, subsets)
  end

  defp build_subsets(coins) do
    n = length(coins)
    total_masks = (1 <<< n) - 1

    Enum.reduce(1..total_masks, [], fn mask, acc ->
      {lcm_val, bits} = lcm_of_mask(mask, coins)
      [{lcm_val, bits} | acc]
    end)
  end

  defp lcm_of_mask(mask, coins) do
    {lcm_val, bits} =
      Enum.with_index(coins)
      |> Enum.reduce({1, 0}, fn {c, idx}, {cur_lcm, cur_bits} ->
        if (mask &&& (1 <<< idx)) != 0 do
          {Integer.lcm(cur_lcm, c), cur_bits + 1}
        else
          {cur_lcm, cur_bits}
        end
      end)

    {lcm_val, bits}
  end

  defp binary_search(low, high, k, subsets) when low < high do
    mid = div(low + high, 2)
    cnt = count_upto(mid, subsets)

    if cnt >= k do
      binary_search(low, mid, k, subsets)
    else
      binary_search(mid + 1, high, k, subsets)
    end
  end

  defp binary_search(low, _high, _k, _subsets), do: low

  defp count_upto(x, subsets) do
    Enum.reduce(subsets, 0, fn {lcm_val, bits}, acc ->
      c = div(x, lcm_val)

      if rem(bits, 2) == 1 do
        acc + c
      else
        acc - c
      end
    end)
  end
end
```
