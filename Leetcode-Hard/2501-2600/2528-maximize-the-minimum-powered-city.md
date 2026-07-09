# 2528. Maximize the Minimum Powered City

## Cpp

```cpp
class Solution {
public:
    long long maxPower(vector<int>& stations, int r, int k) {
        int n = stations.size();
        // prefix sums
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + stations[i];
        // current power of each city
        vector<long long> power(n);
        for (int i = 0; i < n; ++i) {
            int left = max(0, i - r);
            int right = min(n - 1, i + r);
            power[i] = pref[right + 1] - pref[left];
        }
        long long low = 0;
        long long high = *max_element(power.begin(), power.end()) + (long long)k;
        auto feasible = [&](long long target) -> bool {
            vector<long long> diff(n + 1, 0);
            long long added = 0;
            long long curAdd = 0;
            for (int i = 0; i < n; ++i) {
                curAdd += diff[i];
                long long have = power[i] + curAdd;
                if (have < target) {
                    long long need = target - have;
                    added += need;
                    if (added > k) return false;
                    int pos = min(i + r, n - 1);
                    int left = max(0, pos - r);
                    int right = min(n - 1, pos + r);
                    curAdd += need;               // affect current city immediately
                    diff[left] += need;
                    if (right + 1 < n) diff[right + 1] -= need;
                }
            }
            return added <= k;
        };
        while (low < high) {
            long long mid = (low + high + 1) >> 1;
            if (feasible(mid)) low = mid;
            else high = mid - 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public long maxPower(int[] stations, int r, int k) {
        int n = stations.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stations[i];
        }
        long[] init = new long[n];
        long maxInit = 0;
        for (int i = 0; i < n; i++) {
            int left = Math.max(0, i - r);
            int right = Math.min(n - 1, i + r);
            init[i] = prefix[right + 1] - prefix[left];
            if (init[i] > maxInit) maxInit = init[i];
        }
        long low = 0;
        long high = maxInit + k; // safe upper bound
        while (low < high) {
            long mid = (low + high + 1) >>> 1;
            if (canReach(mid, init, r, k)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private boolean canReach(long target, long[] init, int r, int k) {
        int n = init.length;
        long[] diff = new long[n + 2];
        long curAdd = 0;
        long used = 0;
        for (int i = 0; i < n; i++) {
            curAdd += diff[i];
            long total = init[i] + curAdd;
            if (total < target) {
                long need = target - total;
                used += need;
                if (used > k) return false;
                int pos = Math.min(i + r, n - 1);
                curAdd += need;
                int endIdx = pos + r + 1;
                if (endIdx < diff.length) {
                    diff[endIdx] -= need;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        n = len(stations)
        # prefix sum of original stations
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]

        # base power each city gets from existing stations
        base = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            base[i] = pref[right + 1] - pref[left]

        def can(target):
            diff = [0] * (n + 1)   # difference array for added stations influence
            cur_add = 0
            used = 0
            for i in range(n):
                cur_add += diff[i]
                cur_power = base[i] + cur_add
                if cur_power < target:
                    need = target - cur_power
                    used += need
                    if used > k:
                        return False
                    # place at furthest position that can still cover i
                    pos = min(i + r, n - 1)
                    cur_add += need  # this city gets the added stations immediately
                    end = pos + r + 1
                    if end <= n:
                        diff[end] -= need
                # else nothing to add
            return True

        low = 0
        high = max(base) + k  # upper bound inclusive
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## Python3

```python
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 1)
        for i, v in enumerate(stations):
            if v == 0:
                continue
            L = max(0, i - r)
            R = min(n - 1, i + r)
            diff[L] += v
            diff[R + 1] -= v

        init = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            init[i] = cur

        def feasible(target: int) -> bool:
            add = [0] * (n + 1)
            cur_add = 0
            used = 0
            for i in range(n):
                cur_add += add[i]
                power = init[i] + cur_add
                if power < target:
                    need = target - power
                    used += need
                    if used > k:
                        return False
                    pos = min(n - 1, i + r)
                    L = max(0, pos - r)
                    R = min(n - 1, pos + r)
                    add[L] += need
                    add[R + 1] -= need
                    cur_add += need
            return True

        lo, hi = 0, max(init) + k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stdlib.h>
#include <string.h>

static long long *initPower;
static long long *diffArr;
static int n;
static int R;
static long long K;

static int max(int a, int b) { return a > b ? a : b; }
static int min(int a, int b) { return a < b ? a : b; }

static int canReach(long long target) {
    memset(diffArr, 0, sizeof(long long) * n);
    long long cur = 0;
    long long used = 0;
    for (int i = 0; i < n; ++i) {
        cur += diffArr[i];
        long long curPower = initPower[i] + cur;
        if (curPower < target) {
            long long need = target - curPower;
            used += need;
            if (used > K) return 0;
            int pos = i + R;
            if (pos >= n) pos = n - 1;
            cur += need;
            long long endIdx = (long long)pos + R + 1;
            if (endIdx < n) diffArr[endIdx] -= need;
        }
    }
    return 1;
}

long long maxPower(int* stations, int stationsSize, int r, int k) {
    n = stationsSize;
    R = r;
    K = k;

    initPower = (long long*)malloc(sizeof(long long) * n);
    diffArr   = (long long*)malloc(sizeof(long long) * n);

    // prefix sums of original stations
    long long *pref = (long long*)malloc(sizeof(long long) * (n + 1));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + stations[i];
    }

    long long maxInit = 0;
    for (int i = 0; i < n; ++i) {
        int left = max(0, i - R);
        int right = min(n - 1, i + R);
        initPower[i] = pref[right + 1] - pref[left];
        if (initPower[i] > maxInit) maxInit = initPower[i];
    }
    free(pref);

    long long low = 0;
    long long high = maxInit + K; // upper bound

    while (low < high) {
        long long mid = (low + high + 1) >> 1;
        if (canReach(mid))
            low = mid;
        else
            high = mid - 1;
    }

    free(initPower);
    free(diffArr);
    return low;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxPower(int[] stations, int r, int k) {
        int n = stations.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + stations[i];

        long[] orig = new long[n];
        for (int i = 0; i < n; i++) {
            int left = Math.Max(0, i - r);
            int right = Math.Min(n - 1, i + r);
            orig[i] = pref[right + 1] - pref[left];
        }

        long maxOrig = 0;
        foreach (var v in orig) if (v > maxOrig) maxOrig = v;

        long low = 0, high = maxOrig + k; // inclusive upper bound
        while (low < high) {
            long mid = (low + high + 1) >> 1;
            if (CanAchieve(mid, orig, r, k)) low = mid;
            else high = mid - 1;
        }
        return low;
    }

    private bool CanAchieve(long target, long[] orig, int r, int k) {
        int n = orig.Length;
        long[] diff = new long[n];
        long curAdd = 0;
        long used = 0;

        for (int i = 0; i < n; i++) {
            curAdd += diff[i];
            long total = orig[i] + curAdd;
            if (total < target) {
                long need = target - total;
                used += need;
                if (used > k) return false;

                curAdd += need;
                int pos = Math.Min(i + r, n - 1);
                int end = pos + r + 1;
                if (end < n) diff[end] -= need;
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stations
 * @param {number} r
 * @param {number} k
 * @return {number}
 */
var maxPower = function(stations, r, k) {
    const n = stations.length;
    // prefix sums for initial power calculation
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + stations[i];
    }
    const initPower = new Array(n);
    let maxInit = 0;
    for (let i = 0; i < n; ++i) {
        const left = Math.max(0, i - r);
        const right = Math.min(n - 1, i + r);
        const sum = pref[right + 1] - pref[left];
        initPower[i] = sum;
        if (sum > maxInit) maxInit = sum;
    }

    // feasibility check for a target minimum power
    const canAchieve = (target) => {
        const diff = new Array(n + 1).fill(0);
        let curAdd = 0;
        let remaining = k;
        for (let i = 0; i < n; ++i) {
            curAdd += diff[i];
            const total = initPower[i] + curAdd;
            if (total >= target) continue;
            const need = target - total;
            remaining -= need;
            if (remaining < 0) return false;
            curAdd += need;
            // place added stations as far right as possible
            const pos = Math.min(n - 1, i + r);
            const endIdx = Math.min(n, pos + r + 1); // exclusive index where effect ends
            diff[endIdx] -= need;
        }
        return true;
    };

    let low = 0;
    let high = maxInit + k; // safe upper bound
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canAchieve(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maxPower(stations: number[], r: number, k: number): number {
    const n = stations.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + stations[i];

    const init = new Array(n);
    for (let i = 0; i < n; ++i) {
        const left = Math.max(0, i - r);
        const right = Math.min(n - 1, i + r);
        init[i] = pref[right + 1] - pref[left];
    }

    let low = 0;
    let high = Math.max(...init) + k;

    const canAchieve = (target: number): boolean => {
        const add = new Array(n).fill(0);
        let cur = 0;
        let used = 0;
        for (let i = 0; i < n; ++i) {
            if (i - r - 1 >= 0) cur -= add[i - r - 1];
            const total = init[i] + cur;
            if (total < target) {
                const need = target - total;
                used += need;
                if (used > k) return false;
                const pos = Math.min(n - 1, i + r);
                add[pos] += need;
                cur += need;
            }
        }
        return true;
    };

    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canAchieve(mid)) low = mid;
        else high = mid - 1;
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $stations
     * @param Integer $r
     * @param Integer $k
     * @return Integer
     */
    function maxPower($stations, $r, $k) {
        $n = count($stations);
        // initial power using line sweep
        $diff = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $l = max(0, $i - $r);
            $rr = min($n - 1, $i + $r);
            $diff[$l] += $stations[$i];
            $diff[$rr + 1] -= $stations[$i];
        }
        $power = array_fill(0, $n, 0);
        $cur = 0;
        for ($i = 0; $i < $n; ++$i) {
            $cur += $diff[$i];
            $power[$i] = $cur;
        }

        $low = 0;
        $high = max($power) + $k; // safe upper bound

        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canAchieve($mid, $power, $r, $k, $n)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }

    private function canAchieve($target, $basePower, $r, $k, $n) {
        $addDiff = array_fill(0, $n + 2, 0);
        $curAdd = 0;
        $used = 0;

        for ($i = 0; $i < $n; ++$i) {
            $curAdd += $addDiff[$i];
            $curr = $basePower[$i] + $curAdd;
            if ($curr < $target) {
                $need = $target - $curr;
                $used += $need;
                if ($used > $k) {
                    return false;
                }
                $idx = min($i + $r, $n - 1);
                $l = max(0, $idx - $r);
                $rr = min($n - 1, $idx + $r);
                $addDiff[$l] += $need;
                $addDiff[$rr + 1] -= $need;
                // effect on current city
                $curAdd += $need;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {
        let n = stations.count
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(stations[i])
        }
        var initPower = [Int64](repeating: 0, count: n)
        for i in 0..<n {
            let left = max(0, i - r)
            let right = min(n - 1, i + r)
            initPower[i] = prefix[right + 1] - prefix[left]
        }
        var minInit = initPower[0]
        for v in initPower where v < minInit {
            minInit = v
        }
        var low = minInit
        var high = minInit + Int64(k) // inclusive upper bound
        
        func canAchieve(_ target: Int64) -> Bool {
            var diff = [Int64](repeating: 0, count: n + 1)
            var curAdd: Int64 = 0
            var used: Int64 = 0
            for i in 0..<n {
                curAdd += diff[i]
                let current = initPower[i] + curAdd
                if current < target {
                    let need = target - current
                    used += need
                    if used > Int64(k) { return false }
                    curAdd += need
                    let right = min(n - 1, i + 2 * r)
                    if right + 1 <= n {
                        diff[right + 1] -= need
                    }
                }
            }
            return true
        }
        
        while low < high {
            let mid = (low + high + 1) / 2
            if canAchieve(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return Int(low)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPower(stations: IntArray, r: Int, k: Int): Long {
        val n = stations.size
        // prefix sums of original stations
        val pref = LongArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + stations[i]
        }
        // initial power at each city
        val init = LongArray(n)
        for (i in 0 until n) {
            val left = if (i - r > 0) i - r else 0
            val right = if (i + r < n) i + r else n - 1
            init[i] = pref[right + 1] - pref[left]
        }

        var low = 0L
        var high = init.maxOrNull()!! + k.toLong()
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (canAchieve(mid, init, r, k.toLong())) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }

    private fun canAchieve(target: Long, init: LongArray, r: Int, kTotal: Long): Boolean {
        val n = init.size
        val diff = LongArray(n + 1)
        var curAdd = 0L
        var remainingK = kTotal

        for (i in 0 until n) {
            curAdd += diff[i]
            var total = init[i] + curAdd
            if (total < target) {
                val need = target - total
                remainingK -= need
                if (remainingK < 0) return false
                // place stations at the farthest position that still covers i
                val pos = if (i + r < n) i + r else n - 1
                curAdd += need
                val endIdx = if (pos + r < n) pos + r else n - 1
                diff[endIdx + 1] -= need
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int maxPower(List<int> stations, int r, int k) {
    int n = stations.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + stations[i];
    }
    // base power for each city
    List<int> base = List.filled(n, 0);
    int maxBase = 0;
    for (int i = 0; i < n; ++i) {
      int left = i - r;
      if (left < 0) left = 0;
      int right = i + r;
      if (right >= n) right = n - 1;
      base[i] = prefix[right + 1] - prefix[left];
      if (base[i] > maxBase) maxBase = base[i];
    }

    bool canAchieve(int target) {
      List<int> diff = List.filled(n + 1, 0);
      int curAdd = 0;
      int used = 0;
      for (int i = 0; i < n; ++i) {
        curAdd += diff[i];
        int total = base[i] + curAdd;
        if (total >= target) continue;
        int need = target - total;
        used += need;
        if (used > k) return false;

        int pos = i + r;
        if (pos >= n) pos = n - 1; // furthest right position that still covers i
        int start = pos - r;
        if (start < 0) start = 0;
        int end = pos + r;
        if (end >= n) end = n - 1;

        diff[start] += need;
        if (end + 1 <= n) diff[end + 1] -= need;
        curAdd += need; // effect on current city
      }
      return true;
    }

    int low = 0;
    int high = maxBase + k;
    while (low < high) {
      int mid = ((low + high + 1) >> 1);
      if (canAchieve(mid)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func maxPower(stations []int, r int, k int) int64 {
	n := len(stations)
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(stations[i])
	}
	initPower := make([]int64, n)
	for i := 0; i < n; i++ {
		left := i - r
		if left < 0 {
			left = 0
		}
		right := i + r
		if right >= n {
			right = n - 1
		}
		initPower[i] = pref[right+1] - pref[left]
	}
	var low int64 = 0
	var high int64 = 0
	for _, v := range initPower {
		if v > high {
			high = v
		}
	}
	high += int64(k)
	for low < high {
		mid := (low + high + 1) / 2
		if canAchieve(mid, initPower, r, k) {
			low = mid
		} else {
			high = mid - 1
		}
	}
	return low
}

func canAchieve(target int64, init []int64, r int, k int) bool {
	n := len(init)
	diff := make([]int64, n+1)
	var curAdd int64
	var used int64
	for i := 0; i < n; i++ {
		curAdd += diff[i]
		curPower := init[i] + curAdd
		if curPower < target {
			need := target - curPower
			used += need
			if used > int64(k) {
				return false
			}
			pos := i + r
			if pos >= n {
				pos = n - 1
			}
			left := pos - r
			if left < 0 {
				left = 0
			}
			right := pos + r
			if right >= n {
				right = n - 1
			}
			diff[left] += need
			diff[right+1] -= need
			curAdd += need
		}
	}
	return used <= int64(k)
}
```

## Ruby

```ruby
def max_power(stations, r, k)
  n = stations.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + stations[i] }

  power = Array.new(n, 0)
  (0...n).each do |i|
    left = i - r
    left = 0 if left < 0
    right = i + r
    right = n - 1 if right >= n
    power[i] = pref[right + 1] - pref[left]
  end

  total_sum = stations.inject(0, :+)
  low = 0
  high = total_sum + k

  feasible = lambda do |target|
    add = Array.new(n, 0)
    cur = 0
    used = 0
    (0...n).each do |i|
      idx = i - r - 1
      cur -= add[idx] if idx >= 0
      total = power[i] + cur
      if total < target
        deficit = target - total
        used += deficit
        return false if used > k
        pos = i + r
        pos = n - 1 if pos >= n
        add[pos] += deficit
        cur += deficit
      end
    end
    true
  end

  while low < high
    mid = (low + high + 1) >> 1
    if feasible.call(mid)
      low = mid
    else
      high = mid - 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
    def maxPower(stations: Array[Int], r: Int, k: Int): Long = {
        val n = stations.length
        // Prefix sums for original stations
        val pref = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            pref(i + 1) = pref(i) + stations(i).toLong
            i += 1
        }
        // Initial power each city receives from existing stations
        val initPower = new Array[Long](n)
        i = 0
        while (i < n) {
            val left = Math.max(0, i - r)
            val right = Math.min(n - 1, i + r)
            initPower(i) = pref(right + 1) - pref(left)
            i += 1
        }

        def can(target: Long): Boolean = {
            var remaining = k.toLong
            val diff = new Array[Long](n + 1)
            var curAdd = 0L
            var idx = 0
            while (idx < n) {
                curAdd += diff(idx)
                val total = initPower(idx) + curAdd
                if (total < target) {
                    val need = target - total
                    remaining -= need
                    if (remaining < 0) return false
                    curAdd += need
                    val endIdx = idx + r + 1
                    if (endIdx < n) diff(endIdx) -= need
                }
                idx += 1
            }
            true
        }

        var low = 0L
        var high = stations.map(_.toLong).sum + k.toLong
        while (low < high) {
            val mid = (low + high + 1) >>> 1
            if (can(mid)) low = mid else high = mid - 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i64 {
        let n = stations.len();
        let r_usize = r as usize;

        // prefix sums of original stations
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + stations[i] as i64;
        }

        // power each city gets from existing stations
        let mut orig = vec![0i64; n];
        for i in 0..n {
            let left = if i >= r_usize { i - r_usize } else { 0 };
            let right = std::cmp::min(n - 1, i + r_usize);
            orig[i] = pref[right + 1] - pref[left];
        }

        let max_orig = *orig.iter().max().unwrap();
        let mut low: i64 = 0;
        let mut high: i64 = max_orig + k as i64; // inclusive upper bound

        while low < high {
            let mid = (low + high + 1) / 2;
            if Self::can(&orig, n, r_usize, k as i64, mid) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        low
    }

    fn can(orig: &[i64], n: usize, r: usize, k: i64, target: i64) -> bool {
        let mut diff = vec![0i64; n + 1];
        let mut cur_add: i64 = 0;
        let mut used: i64 = 0;

        for i in 0..n {
            cur_add += diff[i];
            let total = orig[i] + cur_add;
            if total < target {
                let need = target - total;
                used += need;
                if used > k {
                    return false;
                }
                // place stations at the farthest right position that still covers i
                let pos = std::cmp::min(n - 1, i + r);
                cur_add += need; // they affect current city and future ones within range
                let end = std::cmp::min(n - 1, pos + r);
                if end + 1 < diff.len() {
                    diff[end + 1] -= need;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (max-power stations r k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length stations))
         (stations-vec (list->vector stations))
         ;; prefix sums
         (pref (make-vector (+ n 1) 0)))
    (for ([i (in-range n)])
      (vector-set! pref (add1 i)
                   (+ (vector-ref pref i) (vector-ref stations-vec i))))
    ;; initial power for each city
    (define init-power
      (let ((v (make-vector n 0)))
        (for ([i (in-range n)])
          (let* ((left (max 0 (- i r)))
                 (right (min n (+ i r) -1)) ; right index inclusive
                 (sum (- (vector-ref pref (add1 right))
                         (vector-ref pref left))))
            (vector-set! v i sum)))
        v))
    ;; helper: can we achieve at least target minimum power?
    (define (feasible? target)
      (let ((diff (make-vector n 0))
            (cur-add 0)
            (used 0))
        (let loop ((i 0) (cur cur-add) (u used))
          (if (= i n)
              #t
              (begin
                (set! cur (+ cur (vector-ref diff i)))
                (define power (+ (vector-ref init-power i) cur))
                (if (>= power target)
                    (loop (add1 i) cur u)
                    (let* ((need (- target power))
                           (new-used (+ u need)))
                      (if (> new-used k)
                          #f
                          (begin
                            (define pos (min (+ i r) (sub1 n)))
                            (define end (min (+ pos r) (sub1 n)))
                            ;; schedule removal after 'end'
                            (when (< (add1 end) n)
                              (vector-set! diff (add1 end)
                                           (- (vector-ref diff (add1 end)) need)))
                            (loop (add1 i) (+ cur need) new-used)))))))))
    ;; binary search for maximum feasible minimum power
    (let* ((max-init (apply max (vector->list init-power)))
           (low 0)
           (high (+ max-init k))) ; upper bound cannot exceed this
      (let loop ((lo low) (hi high))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi 1) 2))) ; ceil mid
              (if (feasible? mid)
                  (loop mid hi)
                  (loop lo (sub1 mid)))))))))
```

## Erlang

```erlang
-export([max_power/3]).

max_power(Stations, R, K) ->
    StationsTuple = list_to_tuple(Stations),
    N = tuple_size(StationsTuple),

    % compute initial power for each city
    PowerList = compute_initial_powers(N, R, StationsTuple),
    PowerTuple = list_to_tuple(PowerList),

    MaxInit = lists:max(PowerList),
    Upper = MaxInit + K,
    binsearch(0, Upper, N, R, K, PowerTuple).

%% binary search for the answer
binsearch(Low, High, N, R, K, PowerTuple) when Low >= High ->
    Low;
binsearch(Low, High, N, R, K, PowerTuple) ->
    Mid = (Low + High + 1) div 2,
    case feasible(Mid, N, R, K, PowerTuple) of
        true -> binsearch(Mid, High, N, R, K, PowerTuple);
        false -> binsearch(Low, Mid - 1, N, R, K, PowerTuple)
    end.

%% check if we can achieve at least Target power for every city
feasible(Target, N, R, K, PowerTuple) ->
    Rem = array:new(N + R + 5, {default,0}),
    feasible_loop(0, 0, K, Target, N, R, PowerTuple, Rem).

feasible_loop(I, CurAdd, Kleft, Target, N, R, PowerTuple, Rem) when I == N ->
    true;
feasible_loop(I, CurAdd, Kleft, Target, N, R, PowerTuple, Rem) ->
    Remove = array:get(I, Rem),
    NewCur = CurAdd - Remove,
    Total = element(I + 1, PowerTuple) + NewCur,
    if
        Total >= Target ->
            feasible_loop(I + 1, NewCur, Kleft, Target, N, R, PowerTuple, Rem);
        true ->
            Need = Target - Total,
            case Need =< Kleft of
                false -> false;
                true ->
                    NewK = Kleft - Need,
                    UpdatedCur = NewCur + Need,
                    Pos = erlang:min(I + R, N - 1),
                    EndIdx = Pos + R + 1,
                    Rem2 = if
                        EndIdx < N ->
                            Old = array:get(EndIdx, Rem),
                            array:set(EndIdx, Old + Need, Rem);
                        true -> Rem
                    end,
                    feasible_loop(I + 1, UpdatedCur, NewK, Target, N, R, PowerTuple, Rem2)
            end
    end.

%% compute initial powers using sliding window
compute_initial_powers(N, R, StationsTuple) ->
    InitialRight = erlang:min(R, N - 1),
    InitSum = sum_range(0, InitialRight, StationsTuple),
    compute_loop(0, InitSum, N, R, StationsTuple, []).

compute_loop(I, Window, N, R, StationsTuple, Acc) when I == N ->
    lists:reverse(Acc);
compute_loop(I, Window, N, R, StationsTuple, Acc) ->
    NewAcc = [Window | Acc],
    LeftIdx = I - R,
    Sub = if LeftIdx >= 0 -> element(LeftIdx + 1, StationsTuple); true -> 0 end,
    RightIdx = I + R + 1,
    Add = if RightIdx < N -> element(RightIdx + 1, StationsTuple); true -> 0 end,
    NewWindow = Window - Sub + Add,
    compute_loop(I + 1, NewWindow, N, R, StationsTuple, NewAcc).

%% sum elements from From to To inclusive
sum_range(From, To, Tuple) when From > To ->
    0;
sum_range(From, To, Tuple) ->
    sum_range_acc(From, To, Tuple, 0).

sum_range_acc(I, To, Tuple, Acc) when I > To ->
    Acc;
sum_range_acc(I, To, Tuple, Acc) ->
    Val = element(I + 1, Tuple),
    sum_range_acc(I + 1, To, Tuple, Acc + Val).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_power(stations :: [integer], r :: integer, k :: integer) :: integer
  def max_power(stations, r, k) do
    n = length(stations)

    # prefix sums as tuple for O(1) access
    pref =
      stations
      |> Enum.scan(0, fn x, acc -> acc + x end)
      |> List.to_tuple()
      |> then(fn t -> :erlang.list_to_tuple([0 | Tuple.to_list(t)]) end)

    init_power =
      for i <- 0..(n - 1) do
        left = max(i - r, 0)
        right = min(i + r, n - 1)
        elem(pref, right + 1) - elem(pref, left)
      end

    init_min = Enum.min(init_power)

    feasible = fn target ->
      res =
        Enum.reduce_while(0..(n - 1), {0, 0, %{}}, fn i, {cur_add, used, expires} ->
          cur_add = cur_add - Map.get(expires, i, 0)
          expires = Map.delete(expires, i)

          total = Enum.at(init_power, i) + cur_add

          if total < target do
            need = target - total
            new_used = used + need

            if new_used > k do
              {:halt, false}
            else
              cur_add = cur_add + need
              pos = min(i + r, n - 1)
              expire_idx = pos + r + 1

              expires =
                if expire_idx < n do
                  Map.update(expires, expire_idx, need, &(&1 + need))
                else
                  expires
                end

              {:cont, {cur_add, new_used, expires}}
            end
          else
            {:cont, {cur_add, used, expires}}
          end
        end)

      case res do
        false -> false
        _ -> true
      end
    end

    binary_search = fn low, high, fun ->
      if low < high do
        mid = div(low + high + 1, 2)

        if fun.(mid) do
          recur = binary_search.(mid, high, fun)
          recur
        else
          recur = binary_search.(low, mid - 1, fun)
          recur
        end
      else
        low
      end
    end

    binary_search.(0, init_min + k, feasible)
  end
end
```
