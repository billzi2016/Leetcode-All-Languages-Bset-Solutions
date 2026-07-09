# 2513. Minimize the Maximum of Two Arrays

## Cpp

```cpp
class Solution {
public:
    bool feasible(long long m, int d1, int d2, long long need1, long long need2) {
        long long cntDiv1 = m / d1;
        long long cntDiv2 = m / d2;
        long long g = std::gcd(d1, d2);
        __int128 lcm128 = (__int128)d1 / g * d2;
        long long lcm = (long long)lcm128;
        long long cntBoth = m / lcm;

        long long exclusive1 = cntDiv2 - cntBoth; // not divisible by d1, divisible by d2
        long long exclusive2 = cntDiv1 - cntBoth; // not divisible by d2, divisible by d1
        long long common = m - cntDiv1 - cntDiv2 + cntBoth; // not divisible by either

        long long needCommon1 = need1 > exclusive1 ? need1 - exclusive1 : 0;
        long long needCommon2 = need2 > exclusive2 ? need2 - exclusive2 : 0;

        return (__int128)needCommon1 + needCommon2 <= common;
    }

    int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        long long cnt1 = uniqueCnt1;
        long long cnt2 = uniqueCnt2;
        long long lo = 1, hi = 1;
        while (!feasible(hi, divisor1, divisor2, cnt1, cnt2)) {
            hi <<= 1;
        }
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (feasible(mid, divisor1, divisor2, cnt1, cnt2))
                hi = mid;
            else
                lo = mid + 1;
        }
        return (int)lo;
    }
};
```

## Java

```java
class Solution {
    public int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        long d1 = divisor1;
        long d2 = divisor2;
        long cnt1 = uniqueCnt1;
        long cnt2 = uniqueCnt2;
        long g = gcd(d1, d2);
        long lcm = d1 / g * d2;

        long low = 1;
        long high = (cnt1 + cnt2) * Math.max(d1, d2); // safe upper bound
        if (high < low) high = Long.MAX_VALUE / 2; // fallback

        while (low < high) {
            long mid = (low + high) >>> 1;
            if (can(mid, d1, d2, lcm, cnt1, cnt2)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return (int) low;
    }

    private boolean can(long m, long d1, long d2, long lcm, long need1, long need2) {
        long div1 = m / d1;          // multiples of divisor1
        long div2 = m / d2;          // multiples of divisor2
        long both = m / lcm;         // multiples of both (i.e., unusable)

        long a = div2 - both;        // not divisible by d1, but divisible by d2
        long b = div1 - both;        // not divisible by d2, but divisible by d1
        long c = m - div1 - div2 + both; // not divisible by either

        long needFromCForFirst = Math.max(0L, need1 - a);
        long needFromCForSecond = Math.max(0L, need2 - b);

        return needFromCForFirst + needFromCForSecond <= c;
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
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """
        from math import gcd

        def lcm(a, b):
            return a // gcd(a, b) * b

        L = lcm(divisor1, divisor2)

        def can(limit):
            total = limit
            div1 = total // divisor1
            div2 = total // divisor2
            divBoth = total // L

            # numbers not divisible by divisor1 / divisor2
            notDiv1 = total - div1
            notDiv2 = total - div2

            both = total - div1 - div2 + divBoth  # not divisible by either
            only1 = notDiv1 - both   # not divisible by divisor1 but divisible by divisor2
            only2 = notDiv2 - both   # not divisible by divisor2 but divisible by divisor1

            needFromBoth1 = max(0, uniqueCnt1 - only1)
            needFromBoth2 = max(0, uniqueCnt2 - only2)

            return needFromBoth1 + needFromBoth2 <= both

        lo, hi = 1, 10**18
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        from math import gcd
        def lcm(a, b):
            return a // gcd(a, b) * b

        L = lcm(divisor1, divisor2)

        def feasible(m: int) -> bool:
            # exclusive numbers for arr1: divisible by divisor2 but not by divisor1
            ex1 = m // divisor2 - m // L
            # exclusive numbers for arr2: divisible by divisor1 but not by divisor2
            ex2 = m // divisor1 - m // L
            # shared numbers: not divisible by either divisor
            shared = m - m // divisor1 - m // divisor2 + m // L

            need1 = uniqueCnt1 - ex1 if uniqueCnt1 > ex1 else 0
            need2 = uniqueCnt2 - ex2 if uniqueCnt2 > ex2 else 0
            return need1 + need2 <= shared

        lo, hi = 1, 10**18
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
#include <limits.h>

static long long gcd_ll(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static int feasible(long long m, int d1, int d2, int cnt1, int cnt2) {
    long long div1 = m / d1;
    long long div2 = m / d2;
    long long lcm = (long long)d1 / gcd_ll(d1, d2) * d2;
    long long bothDiv = m / lcm;

    long long notDiv1 = m - div1;               // usable for arr1
    long long notDiv2 = m - div2;               // usable for arr2
    long long common  = m - (div1 + div2 - bothDiv); // not divisible by either

    long long onlyArr1 = notDiv1 - common;      // divisible by d2 but not by d1
    long long onlyArr2 = notDiv2 - common;      // divisible by d1 but not by d2

    long long needForArr1 = cnt1 > onlyArr1 ? (cnt1 - onlyArr1) : 0;
    long long needForArr2 = cnt2 > onlyArr2 ? (cnt2 - onlyArr2) : 0;

    return needForArr1 + needForArr2 <= common;
}

int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
    long long low = 1;
    long long high = (long long)(divisor1 > divisor2 ? divisor1 : divisor2) *
                     ((long long)uniqueCnt1 + uniqueCnt2);
    if (high < low) high = INT_MAX; // safety

    while (low < high) {
        long long mid = low + (high - low) / 2;
        if (feasible(mid, divisor1, divisor2, uniqueCnt1, uniqueCnt2))
            high = mid;
        else
            low = mid + 1;
    }
    return (int)low;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2)
    {
        long d1 = divisor1;
        long d2 = divisor2;
        long need1 = uniqueCnt1;
        long need2 = uniqueCnt2;

        long g = Gcd(d1, d2);
        long lcm = d1 / g * d2;

        long low = 1;
        long high = Math.Max(divisor1, divisor2) * (need1 + need2);
        while (!Feasible(high, d1, d2, lcm, need1, need2))
            high <<= 1; // double until feasible

        while (low < high)
        {
            long mid = low + (high - low) / 2;
            if (Feasible(mid, d1, d2, lcm, need1, need2))
                high = mid;
            else
                low = mid + 1;
        }

        return (int)low;
    }

    private bool Feasible(long m, long d1, long d2, long lcm, long need1, long need2)
    {
        long notDiv1 = m - m / d1; // numbers <=m not divisible by divisor1
        long notDiv2 = m - m / d2; // numbers <=m not divisible by divisor2

        if (notDiv1 < need1 || notDiv2 < need2)
            return false;

        long bothNotDiv = m - m / d1 - m / d2 + m / lcm; // not divisible by either
        long totalDistinct = notDiv1 + notDiv2 - bothNotDiv; // union size

        return totalDistinct >= need1 + need2;
    }

    private long Gcd(long a, long b)
    {
        while (b != 0)
        {
            long t = a % b;
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
 * @param {number} divisor1
 * @param {number} divisor2
 * @param {number} uniqueCnt1
 * @param {number} uniqueCnt2
 * @return {number}
 */
var minimizeSet = function(divisor1, divisor2, uniqueCnt1, uniqueCnt2) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const lcm = divisor1 / gcd(divisor1, divisor2) * divisor2;

    const can = (m) => {
        const notDiv1 = m - Math.floor(m / divisor1);
        const notDiv2 = m - Math.floor(m / divisor2);
        const bothDivisible = Math.floor(m / lcm);
        const totalAvailable = m - bothDivisible; // numbers not divisible by at least one divisor
        return notDiv1 >= uniqueCnt1 && notDiv2 >= uniqueCnt2 && (uniqueCnt1 + uniqueCnt2) <= totalAvailable;
    };

    let lo = 1, hi = 2000000005; // safe upper bound (> max possible answer)
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (can(mid)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
};
```

## Typescript

```typescript
function minimizeSet(divisor1: number, divisor2: number, uniqueCnt1: number, uniqueCnt2: number): number {
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const lcm = divisor1 / gcd(divisor1, divisor2) * divisor2;

    const can = (m: number): boolean => {
        // numbers divisible by divisor2 but not divisor1 -> only for arr1
        const div2NotDiv1 = Math.floor(m / divisor2) - Math.floor(m / lcm);
        // numbers divisible by divisor1 but not divisor2 -> only for arr2
        const div1NotDiv2 = Math.floor(m / divisor1) - Math.floor(m / lcm);
        // numbers not divisible by either divisor -> can be used for both
        const bothFree = m - Math.floor(m / divisor1) - Math.floor(m / divisor2) + Math.floor(m / lcm);

        const need1 = Math.max(0, uniqueCnt1 - div2NotDiv1);
        const need2 = Math.max(0, uniqueCnt2 - div1NotDiv2);
        return need1 + need2 <= bothFree;
    };

    let low = 1;
    let high = 1;
    while (!can(high)) {
        high *= 2;
    }
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (can(mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $divisor1
     * @param Integer $divisor2
     * @param Integer $uniqueCnt1
     * @param Integer $uniqueCnt2
     * @return Integer
     */
    function minimizeSet($divisor1, $divisor2, $uniqueCnt1, $uniqueCnt2) {
        $g = $this->gcd($divisor1, $divisor2);
        $lcm = intdiv($divisor1, $g) * $divisor2;

        $low = 1;
        $high = max($divisor1, $divisor2) * ($uniqueCnt1 + $uniqueCnt2);

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->can($mid, $divisor1, $divisor2, $lcm, $uniqueCnt1, $uniqueCnt2)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }

    private function can($m, $d1, $d2, $lcm, $cnt1, $cnt2) {
        $a = $m - intdiv($m, $d1);               // not divisible by d1
        $b = $m - intdiv($m, $d2);               // not divisible by d2
        $c = $m - intdiv($m, $d1) - intdiv($m, $d2) + intdiv($m, $lcm); // not divisible by both

        if ($cnt1 > $a || $cnt2 > $b) {
            return false;
        }

        $ex1 = $a - $c; // numbers only usable for arr1
        $ex2 = $b - $c; // numbers only usable for arr2

        $need1 = max(0, $cnt1 - $ex1);
        $need2 = max(0, $cnt2 - $ex2);

        return ($need1 + $need2) <= $c;
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
    func minimizeSet(_ divisor1: Int, _ divisor2: Int, _ uniqueCnt1: Int, _ uniqueCnt2: Int) -> Int {
        let d1 = Int64(divisor1)
        let d2 = Int64(divisor2)
        let need1 = Int64(uniqueCnt1)
        let need2 = Int64(uniqueCnt2)

        func gcd(_ a: Int64, _ b: Int64) -> Int64 {
            var x = a
            var y = b
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }

        func lcm(_ a: Int64, _ b: Int64) -> Int64 {
            return a / gcd(a, b) * b
        }

        let l = lcm(d1, d2)

        func feasible(_ m: Int64) -> Bool {
            let total = m
            let div1 = total / d1          // numbers divisible by divisor1
            let div2 = total / d2          // numbers divisible by divisor2
            let both = total / l           // numbers divisible by both

            let typeA = total - div1 - div2 + both   // not divisible by either (shared)
            let typeB = div2 - both                  // divisible only by divisor2 (exclusive for arr1)
            let typeC = div1 - both                  // divisible only by divisor1 (exclusive for arr2)

            if need1 > typeA + typeB { return false }
            if need2 > typeA + typeC { return false }

            let reqFromShared1 = max(Int64(0), need1 - typeB)
            let reqFromShared2 = max(Int64(0), need2 - typeC)

            return reqFromShared1 + reqFromShared2 <= typeA
        }

        var low: Int64 = 1
        var high: Int64 = Int64(max(divisor1, divisor2)) * (need1 + need2)

        while low < high {
            let mid = (low + high) / 2
            if feasible(mid) {
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
    fun minimizeSet(divisor1: Int, divisor2: Int, uniqueCnt1: Int, uniqueCnt2: Int): Int {
        val d1 = divisor1.toLong()
        val d2 = divisor2.toLong()
        val need1 = uniqueCnt1.toLong()
        val need2 = uniqueCnt2.toLong()

        fun gcd(a: Long, b: Long): Long {
            var x = a
            var y = b
            while (y != 0L) {
                val tmp = x % y
                x = y
                y = tmp
            }
            return x
        }

        val lcm = d1 / gcd(d1, d2) * d2

        fun can(m: Long): Boolean {
            val notDiv1 = m - m / d1
            val notDiv2 = m - m / d2
            val both = m - m / d1 - m / d2 + m / lcm
            val only1 = notDiv1 - both   // divisible by d2 but not by d1
            val only2 = notDiv2 - both   // divisible by d1 but not by d2

            var needBoth1 = need1 - only1
            if (needBoth1 < 0) needBoth1 = 0
            var needBoth2 = need2 - only2
            if (needBoth2 < 0) needBoth2 = 0

            return needBoth1 + needBoth2 <= both
        }

        var low = 1L
        var high = 1L
        while (!can(high)) {
            high = high shl 1
        }
        while (low < high) {
            val mid = (low + high) ushr 1
            if (can(mid)) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
    int g = _gcd(divisor1, divisor2);
    int lcm = divisor1 ~/ g * divisor2;

    int low = 1;
    int high = max(divisor1, divisor2) * (uniqueCnt1 + uniqueCnt2);

    while (!_feasible(high, divisor1, divisor2, lcm, uniqueCnt1, uniqueCnt2)) {
      high *= 2;
    }

    while (low < high) {
      int mid = low + ((high - low) >> 1);
      if (_feasible(mid, divisor1, divisor2, lcm, uniqueCnt1, uniqueCnt2)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }

  bool _feasible(int m, int d1, int d2, int lcm, int need1, int need2) {
    int cntDiv1 = m ~/ d1;
    int cntDiv2 = m ~/ d2;
    int cntBothDiv = m ~/ lcm;

    int onlyArr2 = cntDiv1 - cntBothDiv; // usable only for arr2
    int onlyArr1 = cntDiv2 - cntBothDiv; // usable only for arr1
    int bothUsable = m - cntDiv1 - cntDiv2 + cntBothDiv; // usable for both

    int needFromBoth1 = max(0, need1 - onlyArr1);
    int needFromBoth2 = max(0, need2 - onlyArr2);

    return needFromBoth1 + needFromBoth2 <= bothUsable;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int tmp = a % b;
      a = b;
      b = tmp;
    }
    return a;
  }
}
```

## Golang

```go
func minimizeSet(divisor1 int, divisor2 int, uniqueCnt1 int, uniqueCnt2 int) int {
    d1 := int64(divisor1)
    d2 := int64(divisor2)
    u1 := int64(uniqueCnt1)
    u2 := int64(uniqueCnt2)

    // compute lcm
    g := gcd(d1, d2)
    lcm := d1 / g * d2

    // upper bound for binary search
    high := maxInt64(d1, d2) * (u1 + u2)
    low := int64(1)

    for low < high {
        mid := (low + high) >> 1
        if feasible(mid, d1, d2, lcm, u1, u2) {
            high = mid
        } else {
            low = mid + 1
        }
    }
    return int(low)
}

func feasible(m, d1, d2, lcm, u1, u2 int64) bool {
    cntDiv1 := m / d1
    cntDiv2 := m / d2
    cntBoth := m / lcm

    notDiv1 := m - cntDiv1
    notDiv2 := m - cntDiv2

    if notDiv1 < u1 || notDiv2 < u2 {
        return false
    }

    extra1 := notDiv1 - u1
    extra2 := notDiv2 - u2

    overlap := m - cntDiv1 - cntDiv2 + cntBoth // numbers not divisible by either divisor

    return extra1+extra2 >= overlap
}

func gcd(a, b int64) int64 {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func maxInt64(a, b int64) int64 {
    if a > b {
        return a
    }
    return b
}
```

## Ruby

```ruby
def minimize_set(divisor1, divisor2, unique_cnt1, unique_cnt2)
  lcm = divisor1.lcm(divisor2)
  left = 1
  right = (10**18)

  while left < right
    mid = (left + right) / 2

    cnt1 = mid - mid / divisor1          # not divisible by divisor1
    cnt2 = mid - mid / divisor2          # not divisible by divisor2
    both = mid - mid / divisor1 - mid / divisor2 + mid / lcm  # not divisible by either

    only1 = cnt1 - both   # usable only for arr1
    only2 = cnt2 - both   # usable only for arr2

    need1 = unique_cnt1 - only1
    need1 = 0 if need1 < 0
    need2 = unique_cnt2 - only2
    need2 = 0 if need2 < 0

    if need1 + need2 <= both
      right = mid
    else
      left = mid + 1
    end
  end

  left
end
```

## Scala

```scala
object Solution {
  def minimizeSet(divisor1: Int, divisor2: Int, uniqueCnt1: Int, uniqueCnt2: Int): Int = {
    val d1 = divisor1.toLong
    val d2 = divisor2.toLong
    val cnt1 = uniqueCnt1.toLong
    val cnt2 = uniqueCnt2.toLong

    def gcd(a: Long, b: Long): Long = {
      var x = a
      var y = b
      while (y != 0) {
        val t = x % y
        x = y
        y = t
      }
      x
    }

    val lcm = d1 / gcd(d1, d2) * d2

    def feasible(m: Long): Boolean = {
      val notDiv1 = m - m / d1          // numbers <= m not divisible by divisor1
      val notDiv2 = m - m / d2          // numbers <= m not divisible by divisor2
      val notDivEither = m - m / d1 - m / d2 + m / lcm // not divisible by either

      val exclusive1 = notDiv1 - notDivEither
      val exclusive2 = notDiv2 - notDivEither

      val need1 = if (cnt1 > exclusive1) cnt1 - exclusive1 else 0L
      val need2 = if (cnt2 > exclusive2) cnt2 - exclusive2 else 0L

      need1 + need2 <= notDivEither
    }

    var low: Long = 1L
    var high: Long = 1L << 60 // sufficiently large upper bound

    while (low < high) {
      val mid = (low + high) >>> 1
      if (feasible(mid)) high = mid else low = mid + 1
    }
    low.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_set(divisor1: i32, divisor2: i32, unique_cnt1: i32, unique_cnt2: i32) -> i32 {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }

        fn can(m: i64, d1: i64, d2: i64, cnt1: i64, cnt2: i64, lcm: i64) -> bool {
            let not_div1 = m - m / d1;
            let not_div2 = m - m / d2;
            let not_both = m - m / lcm;
            let only1 = not_div1 - not_both;
            let only2 = not_div2 - not_both;
            let need1 = if cnt1 > only1 { cnt1 - only1 } else { 0 };
            let need2 = if cnt2 > only2 { cnt2 - only2 } else { 0 };
            need1 + need2 <= not_both
        }

        let d1 = divisor1 as i64;
        let d2 = divisor2 as i64;
        let cnt1 = unique_cnt1 as i64;
        let cnt2 = unique_cnt2 as i64;
        let lcm = d1 / gcd(d1, d2) * d2;

        let mut low: i64 = 1;
        let mut high: i64 = 1;
        while !can(high, d1, d2, cnt1, cnt2, lcm) {
            high <<= 1;
        }
        while low < high {
            let mid = low + (high - low) / 2;
            if can(mid, d1, d2, cnt1, cnt2, lcm) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        low as i32
    }
}
```

## Racket

```racket
(define/contract (minimize-set divisor1 divisor2 uniqueCnt1 uniqueCnt2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([g (gcd divisor1 divisor2)]
         [lcm (/ (* divisor1 divisor2) g)])
    (define (feasible? m)
      (let* ([cnt1 (- m (quotient m divisor1))]
             [cnt2 (- m (quotient m divisor2))]
             [usable (- m (quotient m lcm))])
        (and (>= cnt1 uniqueCnt1)
             (>= cnt2 uniqueCnt2)
             (>= usable (+ uniqueCnt1 uniqueCnt2)))))
    ;; find an upper bound where feasible? holds
    (let loop ((hi 1))
      (if (feasible? hi)
          (let search ((lo 1) (hi hi))
            (if (= lo hi)
                lo
                (let* ([mid (quotient (+ lo hi) 2)])
                  (if (feasible? mid)
                      (search lo mid)
                      (search (+ mid 1) hi)))))
          (loop (* hi 2))))))
```

## Erlang

```erlang
-module(solution).
-export([minimize_set/4]).

-spec minimize_set(integer(), integer(), integer(), integer()) -> integer().
minimize_set(Divisor1, Divisor2, UniqueCnt1, UniqueCnt2) ->
    LCM = lcm(Divisor1, Divisor2),
    MaxDiv = erlang:max(Divisor1, Divisor2),
    Upper = MaxDiv * (UniqueCnt1 + UniqueCnt2) + MaxDiv,
    binary_search(1, Upper, Divisor1, Divisor2, LCM, UniqueCnt1, UniqueCnt2).

binary_search(Low, High, D1, D2, LCM, U1, U2) when Low < High ->
    Mid = (Low + High) div 2,
    case feasible(Mid, D1, D2, LCM, U1, U2) of
        true -> binary_search(Low, Mid, D1, D2, LCM, U1, U2);
        false -> binary_search(Mid + 1, High, D1, D2, LCM, U1, U2)
    end;
binary_search(Ans, _, _, _, _, _, _) ->
    Ans.

feasible(M, D1, D2, LCM, U1, U2) ->
    Div1 = M div D1,
    Div2 = M div D2,
    DivBoth = M div LCM,
    Only1 = Div2 - DivBoth,
    Only2 = Div1 - DivBoth,
    Both = M - Div1 - Div2 + DivBoth,
    Need1 = erlang:max(0, U1 - Only1),
    Need2 = erlang:max(0, U2 - Only2),
    Need1 + Need2 =< Both.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

lcm(A, B) ->
    G = gcd(A, B),
    (A div G) * B.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_set(integer, integer, integer, integer) :: integer
  def minimize_set(divisor1, divisor2, unique_cnt1, unique_cnt2) do
    lcm = Integer.lcm(divisor1, divisor2)

    low = 1

    # initial upper bound
    high =
      max(divisor1 * (unique_cnt1 + unique_cnt2),
        divisor2 * (unique_cnt1 + unique_cnt2))

    high =
      if feasible?(high, divisor1, divisor2, lcm, unique_cnt1, unique_cnt2) do
        high
      else
        expand_high(high, divisor1, divisor2, lcm, unique_cnt1, unique_cnt2)
      end

    binary_search(low, high, divisor1, divisor2, lcm, unique_cnt1, unique_cnt2)
  end

  defp expand_high(high, d1, d2, lcm, need1, need2) do
    new = high * 2
    if feasible?(new, d1, d2, lcm, need1, need2), do: new, else: expand_high(new, d1, d2, lcm, need1, need2)
  end

  defp binary_search(low, high, d1, d2, lcm, need1, need2) when low < high do
    mid = div(low + high, 2)

    if feasible?(mid, d1, d2, lcm, need1, need2) do
      binary_search(low, mid, d1, d2, lcm, need1, need2)
    else
      binary_search(mid + 1, high, d1, d2, lcm, need1, need2)
    end
  end

  defp binary_search(low, _high, _d1, _d2, _lcm, _need1, _need2), do: low

  defp feasible?(m, d1, d2, lcm, need1, need2) do
    cnt1 = m - div(m, d1)
    cnt2 = m - div(m, d2)
    total_allowed = m - div(m, lcm)

    cnt1 >= need1 and cnt2 >= need2 and (need1 + need2) <= total_allowed
  end
end
```
