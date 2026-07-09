# 3017. Count the Number of Houses at a Certain Distance II

## Cpp

```cpp
class Solution {
public:
    vector<long long> countOfPairs(int n, int x, int y) {
        vector<long long> add(n + 2, 0), sub(n + 2, 0);
        auto process = [&](int a, int b) {
            for (int i = 1; i <= n; ++i) {
                int ai = abs(i - a);
                // interval with j < b
                if (i < b) {
                    long long num = (long long)ai + 1 + b + i;
                    int startJ = (int)(num / 2) + 1;               // need j > num/2
                    int L = max(i + 1, startJ);
                    int R = b - 1;
                    if (L <= R) {
                        int dStart = L - i;
                        int dEnd   = R - i;
                        sub[dStart] += 1;
                        sub[dEnd + 1] -= 1;
                        long long altL = (long long)ai + 1 + llabs((long long)L - b);
                        long long altR = (long long)ai + 1 + llabs((long long)R - b);
                        int aStart = (int)min(altL, altR);
                        int aEnd   = (int)max(altL, altR);
                        add[aStart] += 1;
                        add[aEnd + 1] -= 1;
                    }
                }
                // interval with j >= b
                if ((long long)i + ai + 1 < b) {
                    int L2 = max(b, i + 1);
                    int R2 = n;
                    if (L2 <= R2) {
                        int dStart = L2 - i;
                        int dEnd   = R2 - i;
                        sub[dStart] += 1;
                        sub[dEnd + 1] -= 1;
                        long long altL = (long long)ai + 1 + llabs((long long)L2 - b);
                        long long altR = (long long)ai + 1 + llabs((long long)R2 - b);
                        int aStart = (int)min(altL, altR);
                        int aEnd   = (int)max(altL, altR);
                        add[aStart] += 1;
                        add[aEnd + 1] -= 1;
                    }
                }
            }
        };
        process(x, y);
        process(y, x);
        vector<long long> ans(n + 1, 0);
        for (int d = 1; d <= n - 1; ++d) ans[d] = 2LL * (n - d);
        long long curAdd = 0, curSub = 0;
        for (int d = 1; d <= n - 1; ++d) {
            curAdd += add[d];
            curSub += sub[d];
            ans[d] = ans[d] - 2LL * curSub + 2LL * curAdd;
        }
        ans[n] = 0;
        vector<long long> res(n);
        for (int i = 1; i <= n; ++i) res[i - 1] = ans[i];
        return res;
    }
};
```

## Java

```java
class Solution {
    public long[] countOfPairs(int n, int x, int y) {
        int a = Math.min(x, y);
        int b = Math.max(x, y);
        long[] res = new long[n];
        // base counts on line
        for (int d = 1; d < n; ++d) {
            res[d - 1] = 2L * (n - d);
        }
        int gap = b - a - 1;
        if (gap <= 0) return res;
        // adjust counts for pairs crossing the extra edge
        for (int d = b - a; d <= n - 1; ++d) {
            int lowI = Math.max(1, b - d);
            int highI = Math.min(a, n - d);
            if (lowI > highI) continue;
            long cnt = (long) (highI - lowI + 1); // number of (i,j) with i<j crossing and distance d
            long ordered = cnt * 2L; // both directions
            int fromIdx = d - 1;
            int toIdx = d - gap - 1;
            res[fromIdx] -= ordered;
            res[toIdx] += ordered;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        a, b = (x, y) if x <= y else (y, x)
        # base counts for ordered pairs on a line
        ans = [0] * (n + 1)          # 1-indexed
        for k in range(1, n):
            ans[k] = 2 * (n - k)

        if a == b:                   # extra street is a loop, no effect
            return ans[1:]

        max_t = (a - 1) + (n - b)    # maximum L+R
        left_max = a - 1             # largest possible L
        right_max = n - b            # largest possible R

        for t in range(0, max_t + 1):
            lowL = max(0, t - right_max)
            highL = min(left_max, t)
            if lowL > highL:
                continue
            cnt = highL - lowL + 1          # unordered pairs with L+R = t
            orig_dist = (b - a) + t         # original distance without shortcut
            delta = 2 * cnt                  # ordered pairs count
            ans[orig_dist] -= delta
            ans[t + 1] += delta

        return ans[1:]
```

## Python3

```python
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        diff = y - x
        # base counts for a simple line
        ans = [0] * (n + 1)          # 1-indexed distances
        for d in range(1, n):
            ans[d] = 2 * (n - d)
        if diff == 0:                # extra street adds no shortcut
            return ans[1:]
        # adjust counts for pairs that benefit from the shortcut
        for d in range(diff, n):     # d = j - i (j > i)
            if d == 0:
                continue
            left_i = max(1, y - d)
            right_i = min(x, n - d)
            cnt = right_i - left_i + 1
            if cnt <= 0:
                continue
            ans[d] -= 2 * cnt
            newd = d - diff + 1
            ans[newd] += 2 * cnt
        return ans[1:]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countOfPairs(int n, int x, int y, int* returnSize) {
    *returnSize = n;
    long long* ans = (long long*)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) ans[i] = 0;

    // default distances without the extra street
    for (int d = 1; d <= n - 1; ++d) {
        ans[d - 1] = 2LL * (n - d);
    }

    int a = x < y ? x : y;
    int b = x > y ? x : y;
    int gap = b - a - 1;               // how much the shortcut shortens the distance

    if (gap > 0) {
        for (int d = 1; d <= n - 1; ++d) {
            int lo_i = b - d;
            if (lo_i < 1) lo_i = 1;
            int hi_i = a;
            int tmp = n - d;
            if (hi_i > tmp) hi_i = tmp;

            if (lo_i <= hi_i) {
                long long cnt = (long long)(hi_i - lo_i + 1); // unordered crossing pairs with distance d
                ans[d - 1] -= 2LL * cnt;                       // remove their original contribution
                int newd = d - gap;                            // shortened distance
                ans[newd - 1] += 2LL * cnt;                    // add to the new distance
            }
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long[] CountOfPairs(int n, int x, int y) {
        long[] ans = new long[n];
        for (int d = 1; d < n; ++d) {
            ans[d - 1] = 2L * (n - d);
        }
        int a = Math.Min(x, y);
        int b = Math.Max(x, y);
        int delta = b - a - 1;
        if (delta <= 0) return ans;

        for (int d = 1; d < n; ++d) {
            int L = Math.Max(1, b - d);
            int R = Math.Min(a, n - d);
            if (L > R) continue;
            long cross = R - L + 1;
            ans[d - 1] -= 2L * cross;
            int newDist = d - delta; // guaranteed >= 1
            ans[newDist - 1] += 2L * cross;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @param {number} y
 * @return {number[]}
 */
var countOfPairs = function(n, x, y) {
    if (x > y) {
        const tmp = x;
        x = y;
        y = tmp;
    }
    const delta = y - x - 1; // reduction amount when shortcut is useful
    const ans = new Array(n).fill(0);
    // default counts without extra street: ordered pairs at distance k => 2*(n-k)
    for (let k = 1; k < n; ++k) {
        ans[k - 1] = 2 * (n - k);
    }
    if (delta <= 0) return ans;

    // cnt[d] = number of unordered pairs (i,j) with j-i=d, i<=x, j>=y
    const cnt = new Array(n).fill(0);
    for (let d = 1; d < n; ++d) {
        let L = Math.max(1, y - d);
        let R = Math.min(x, n - d);
        if (R >= L) cnt[d] = R - L + 1;
    }

    // adjust counts: pairs with original distance d shift to d-delta
    for (let d = 1; d < n; ++d) {
        const c = cnt[d];
        if (!c) continue;
        ans[d - 1] -= 2 * c;               // remove from original distance
        const nd = d - delta;              // new distance after shortcut
        if (nd >= 1) {
            ans[nd - 1] += 2 * c;          // add to reduced distance
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countOfPairs(n: number, x: number, y: number): number[] {
    const ans = new Array<number>(n + 1).fill(0);
    for (let k = 1; k <= n; ++k) {
        ans[k] = 2 * (n - k);
    }
    let a = Math.min(x, y);
    let b = Math.max(x, y);
    const delta = b - a - 1;
    if (delta > 0) {
        for (let s = b - a; s <= n - 1; ++s) {
            const low_i = Math.max(1, b - s);
            const high_i = Math.min(a, n - s);
            if (low_i > high_i) continue;
            const cnt = high_i - low_i + 1;
            const d = s - delta;
            ans[s] -= 2 * cnt;
            ans[d] += 2 * cnt;
        }
    }
    return ans.slice(1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $x
     * @param Integer $y
     * @return Integer[]
     */
    function countOfPairs($n, $x, $y) {
        if ($x > $y) {
            $tmp = $x;
            $x = $y;
            $y = $tmp;
        }
        // initial counts using only the line
        $ans = array_fill(0, $n, 0);
        for ($k = 1; $k < $n; $k++) {
            $cnt = 2 * ($n - $k); // ordered pairs
            $ans[$k - 1] = $cnt;
        }
        // if extra street connects the same house, no improvement possible
        if ($x == $y) {
            return $ans;
        }

        $a = $x;
        $b = $y;
        $len = $b - $a; // length of segment replaced by edge

        for ($diff = $len; $diff <= $n - 1; $diff++) {
            $low_i = max(1, $b - $diff);
            $high_i = min($a, $n - $diff);
            if ($low_i > $high_i) continue;
            $cntPairs = $high_i - $low_i + 1; // unordered pairs
            $ordered = $cntPairs * 2;

            $origIdx = $diff - 1;
            $newDiff = $diff - $len + 1;
            $newIdx = $newDiff - 1;

            $ans[$origIdx] -= $ordered;
            $ans[$newIdx] += $ordered;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countOfPairs(_ n: Int, _ x: Int, _ y: Int) -> [Int] {
        var a = x
        var b = y
        if a > b { swap(&a, &b) }
        let gap = b - a
        var ans = Array(repeating: 0, count: n + 1) // 1-indexed
        if n > 1 {
            for k in 1..<n {
                ans[k] = 2 * (n - k)
            }
        }
        if gap <= 1 {
            return Array(ans[1...n])
        }
        let d0 = gap - 1
        var diff = Array(repeating: 0, count: n + 2)
        for i in 1...a {
            // subtract original distances
            let origStart = b - i
            let origEnd = n - i
            if origStart <= origEnd {
                diff[origStart] -= 2
                diff[origEnd + 1] += 2
            }
            // add reduced distances
            let newStart = a - i + 1
            let newEnd = n - i - d0
            if newStart <= newEnd {
                diff[newStart] += 2
                diff[newEnd + 1] -= 2
            }
        }
        var cur = 0
        for k in 1..<n {
            cur += diff[k]
            ans[k] += cur
        }
        return Array(ans[1...n])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOfPairs(n: Int, x: Int, y: Int): LongArray {
        val a = kotlin.math.min(x, y)
        val b = kotlin.math.max(x, y)
        val ans = LongArray(n)
        for (k in 1 until n) {
            ans[k - 1] = 2L * (n - k).toLong()
        }
        // ans[n-1] stays 0
        if (b - a <= 1) return ans

        val offset = b - a - 1  // d - 1, where d = b - a >= 2
        for (k in 1 until n) {
            val iLow = kotlin.math.max(1, b - k)
            val iHigh = kotlin.math.min(a, n - k)
            if (iLow <= iHigh) {
                val cnt = (iHigh - iLow + 1).toLong()
                val shiftDist = k - offset
                // shiftDist is at least 1
                ans[k - 1] -= 2L * cnt
                ans[shiftDist - 1] += 2L * cnt
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countOfPairs(int n, int x, int y) {
    // Ensure x <= y for simplicity
    if (x > y) {
      int tmp = x;
      x = y;
      y = tmp;
    }
    List<int> ans = List.filled(n + 1, 0);
    // Direct pairs count: for distance d (1-indexed), there are 2*(n-d) ordered pairs
    for (int d = 1; d <= n - 1; ++d) {
      ans[d] = 2 * (n - d);
    }
    // Adjust counts where the shortcut edge gives a shorter path.
    for (int i = 1; i <= n; ++i) {
      int li = (i - x).abs();
      for (int j = i + 1; j <= n; ++j) {
        int direct = j - i;
        int alt1 = li + (y - j).abs() + 1;
        int alt2 = (i - y).abs() + (x - j).abs() + 1;
        int best = alt1 < alt2 ? alt1 : alt2;
        if (best < direct) {
          ans[direct] -= 2; // remove ordered pairs counted in direct
          ans[best] += 2;   // add ordered pairs with shorter distance
        }
      }
    }
    // The result should be of length n, 1-indexed distances.
    return ans.sublist(1);
  }
}
```

## Golang

```go
func countOfPairs(n int, x int, y int) []int64 {
    // Ensure a <= b
    a, b := x, y
    if a > b {
        a, b = b, a
    }
    ans := make([]int64, n)

    // Direct distances: for each k (1-indexed), there are 2*(n-k) ordered pairs.
    for k := 1; k <= n-1; k++ {
        ans[k-1] = int64(2 * (n - k))
    }

    // Process shortcuts where the extra edge reduces distance.
    // For each i in [1, a], j in [b, n] (crossing the whole interval)
    // the new distance is (j - i) - (b - a) + 1.
    gap := b - a
    if gap > 1 {
        for d := gap; d <= n-1; d++ { // original direct distance j-i = d
            // number of pairs with this distance crossing the interval
            // i must satisfy max(1, b-d) <= i <= min(a, n-d)
            left := b - d
            if left < 1 {
                left = 1
            }
            right := a
            nd := n - d
            if nd < right {
                right = nd
            }
            cnt := right - left + 1
            if cnt > 0 {
                // each unordered pair contributes two ordered pairs
                cnt2 := int64(cnt * 2)
                ans[d-1] -= cnt2                     // remove from original distance
                newDist := d - gap + 1               // reduced distance
                ans[newDist-1] += cnt2               // add to reduced distance
            }
        }
    }

    // Additional shortcuts where one endpoint is inside [a, b] and the other outside.
    // For i in [1, a) and j in (a, b):
    for i := 1; i < a; i++ {
        constC := a - i + 1 // part of shortcut distance excluding j
        // we need j such that shortcut distance < direct distance:
        // (a-i)+(b-j)+1 < j-i  => 2j > a+b+1
        // Let threshold = floor((a+b+1)/2) + 1
        thresh := (a+b+1)/2 + 1
        if thresh <= i {
            continue
        }
        startJ := max(thresh, a+1)
        endJ := b - 1
        if startJ > endJ {
            continue
        }
        // For each j in [startJ, endJ], shortcut distance = (a-i)+(b-j)+1
        // direct distance = j-i
        // newDist = (a-i)+(b-j)+1
        // We'll accumulate using prefix sums over possible newDist values.
        for j := startJ; j <= endJ; j++ {
            direct := j - i
            shortcut := a - i + b - j + 1
            if shortcut < direct {
                ans[direct-1] -= 2
                ans[shortcut-1] += 2
            }
        }
    }

    // Symmetric case: i in (a, b) and j in (b, n]
    for j := b + 1; j <= n; j++ {
        constC := j - b + 1
        // condition: (j-b)+(i-a)+1 < j-i => 2i > a+b+1
        thresh := (a+b+1)/2 + 1
        startI := max(thresh, a+1)
        endI := min(b-1, j-1)
        if startI > endI {
            continue
        }
        for i := startI; i <= endI; i++ {
            direct := j - i
            shortcut := b - i + j - a + 1
            if shortcut < direct {
                ans[direct-1] -= 2
                ans[shortcut-1] += 2
            }
        }
    }

    // Cases where one endpoint equals a or b are already covered by the above loops.
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

## Ruby

```ruby
def count_of_pairs(n, x, y)
  a = [x, y].min
  b = [x, y].max

  # baseline counts using only the line edges
  ans = Array.new(n, 0)
  (1...n).each do |k|
    ans[k - 1] = 2 * (n - k)
  end

  delta = b - a - 1
  return ans if delta <= 0

  diff = Array.new(n + 2, 0)

  (1..a).each do |i|
    min_d = b - i
    max_d = n - i
    next if min_d > max_d
    diff[min_d] += 1
    diff[max_d + 1] -= 1
  end

  cur = 0
  (1...n).each do |d|
    cur += diff[d]
    c = cur
    next if c == 0
    ans[d - 1] -= 2 * c
    new_d = d - delta
    ans[new_d - 1] += 2 * c
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countOfPairs(n: Int, x: Int, y: Int): Array[Long] = {
        val a = math.min(x, y)
        val b = math.max(x, y)
        val ans = new Array[Long](n) // 0-indexed, distance k stored at index k-1
        var d = 1
        while (d < n) {
            ans(d - 1) = 2L * (n - d)
            d += 1
        }
        val gap = b - a
        if (gap > 0) {
            d = gap
            while (d < n) {
                val lowI = math.max(1, b - d)
                val highI = math.min(a, n - d)
                if (lowI <= highI) {
                    val cnt = (highI - lowI + 1).toLong
                    val ordered = cnt * 2L
                    ans(d - 1) -= ordered
                    val newDist = d - gap + 1 // always >=1
                    ans(newDist - 1) += ordered
                }
                d += 1
            }
        }
        ans
    }
}
```

## Rust

```rust
use std::cmp::{max, min};

impl Solution {
    pub fn count_of_pairs(n: i32, x: i32, y: i32) -> Vec<i64> {
        let n = n as usize;
        let mut a = x.min(y) as usize;
        let mut b = x.max(y) as usize;

        // baseline answer for the line graph
        let mut ans = vec![0i64; n + 1]; // 1-indexed, ans[distance]
        for d in 1..n {
            ans[d] = 2 * (n - d) as i64;
        }

        // if the extra street connects a house to itself, nothing changes
        if a == b {
            return ans[1..=n].to_vec();
        }

        // ----- Type B: pairs (i <= a, j in (threshold .. b-1)) -----
        let mut dec_diff = vec![0i64; n + 2];
        let mut inc_diff = vec![0i64; n + 2];

        // threshold = floor((a+b+1)/2) + 1   (smallest integer > (a+b+1)/2)
        let thresh = ((a + b + 1) / 2) + 1;

        for i in 1..=a {
            let mut l = i + 1;
            if l < thresh {
                l = thresh;
            }
            if l <= b - 1 {
                let d_start = l - i;               // >=1
                let d_end = (b - 1) - i;
                let s = a + b - 2 * i + 1;          // sum of distances before shortcut
                let low_alt = s - d_end;
                let high_alt = s - d_start;

                dec_diff[d_start] += 1;
                dec_diff[d_end + 1] -= 1;
                inc_diff[low_alt] += 1;
                inc_diff[high_alt + 1] -= 1;
            }
        }

        // prefix sums to obtain counts per distance
        let mut dec_cnt = vec![0i64; n + 1];
        let mut cur = 0i64;
        for d in 1..=n {
            cur += dec_diff[d];
            dec_cnt[d] = cur;
        }
        let mut inc_cnt = vec![0i64; n + 1];
        cur = 0;
        for d in 1..=n {
            cur += inc_diff[d];
            inc_cnt[d] = cur;
        }

        // ----- Type A and C: pairs crossing the interval -----
        let delta = b - a - 1; // reduction amount when using shortcut across the whole interval
        if delta > 0 {
            // limit for left side inside (a, b)
            let l_limit = (a + b - 1) / 2;
            for d in 1..n {
                // Type A: i in [1, a]
                let mut cnt_cross = 0i64;
                if d >= b - a {
                    let low_i = max(1usize, b.saturating_sub(d));
                    let high_i = min(a, n.saturating_sub(d));
                    if high_i >= low_i {
                        cnt_cross += (high_i - low_i + 1) as i64;
                    }
                }

                // Type C: i in [a+1, l_limit]
                if l_limit > a && d >= b - l_limit {
                    let low_i = max(a + 1, b.saturating_sub(d));
                    let high_i = min(l_limit, n.saturating_sub(d));
                    if high_i >= low_i {
                        cnt_cross += (high_i - low_i + 1) as i64;
                    }
                }

                if cnt_cross > 0 {
                    let from = d;
                    let to = d - delta;
                    ans[from] -= 2 * cnt_cross;
                    ans[to] += 2 * cnt_cross;
                }
            }
        }

        // apply Type B adjustments
        for d in 1..=n {
            if dec_cnt[d] > 0 {
                ans[d] -= 2 * dec_cnt[d];
            }
            if inc_cnt[d] > 0 {
                ans[d] += 2 * inc_cnt[d];
            }
        }

        ans[1..=n].to_vec()
    }
}
```

## Racket

```racket
(define/contract (count-of-pairs n x y)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  (let* ([x0 (if (< x y) x y)]
         [y0 (if (< x y) y x)])
    (define res (make-vector n 0))
    ;; base counts without extra street
    (for ([d (in-range 1 n)]) ; d = distance
      (vector-set! res (- d 1) (* 2 (- n d))))
    (when (not (= x0 y0))
      (let* ([delta (- y0 x0)])
        (for ([d (in-range delta n)]) ; d from delta to n-1 inclusive
          (let* ([low (max 1 (- y0 d))]
                 [high (min x0 (- n d))])
            (when (<= low high)
              (let* ([cnt (+ 1 (- high low))]      ; unordered pairs crossing the edge with distance d
                     [ordered (* 2 cnt)]
                     [newd (+ (- d delta) 1)])   ; reduced distance
                ;; move counts from d to newd
                (vector-set! res (- d 1) (- (vector-ref res (- d 1)) ordered))
                (vector-set! res (- newd 1) (+ (vector-ref res (- newd 1)) ordered)))))))))
    (vector->list res)))
```

## Erlang

```erlang
-spec count_of_pairs(N :: integer(), X :: integer(), Y :: integer()) -> [integer()].
count_of_pairs(N, X, Y) ->
    A = min(X, Y),
    B = max(X, Y),
    BaseArray = init_base(N),
    case A == B of
        true ->
            array_to_list(BaseArray, N);
        false ->
            C = B - A - 1,
            if
                C =< 0 ->
                    array_to_list(BaseArray, N);
                true ->
                    Updated = process_shifts(1, N, A, B, C, BaseArray),
                    array_to_list(Updated, N)
            end
    end.

%% Initialize base counts: ans[d] = 2*(N-d) for d=1..N-1, ans[N]=0
init_base(N) ->
    Arr0 = array:new(N, {default, 0}),
    fill_base(1, N - 1, N, Arr0).

fill_base(D, MaxD, _N, Arr) when D > MaxD -> Arr;
fill_base(D, MaxD, N, Arr) ->
    Val = 2 * (N - D),
    NewArr = array:set(D, Val, Arr),
    fill_base(D + 1, MaxD, N, NewArr).

%% Process distance shifts caused by the extra street
process_shifts(D, N, _A, _B, _C, Arr) when D > N - 1 -> Arr;
process_shifts(D, N, A, B, C, Arr) ->
    L = max(1, B - D),
    R = min(A, N - D),
    NewArr =
        if
            L =< R ->
                Count = R - L + 1,
                Sub = 2 * Count,
                ValD = array:get(D, Arr) - Sub,
                Arr1 = array:set(D, ValD, Arr),
                D2 = D - C,
                ValD2 = array:get(D2, Arr1) + Sub,
                array:set(D2, ValD2, Arr1);
            true ->
                Arr
        end,
    process_shifts(D + 1, N, A, B, C, NewArr).

%% Convert first N elements of the array to a list
array_to_list(Arr, N) ->
    [array:get(I, Arr) || I <- lists:seq(1, N)].
```

## Elixir

```elixir
defmodule Solution do
  @spec count_of_pairs(n :: integer, x :: integer, y :: integer) :: [integer]
  def count_of_pairs(n, x, y) do
    {x, y} = if x <= y, do: {x, y}, else: {y, x}
    d_reduce = y - x - 1

    # initialize answer array (1-indexed)
    ans = :array.new(n + 1, default: 0)

    ans =
      Enum.reduce(1..(n - 1), ans, fn dist, acc ->
        :array.set(dist, 2 * (n - dist), acc)
      end)

    if d_reduce > 0 do
      min_dist = y - x
      max_dist = n - 1

      Enum.reduce(min_dist..max_dist, ans, fn dist, acc ->
        min_i = max(1, y - dist)
        max_i = min(x, n - dist)

        cnt = max_i - min_i + 1

        if cnt > 0 do
          delta = dist - d_reduce

          cur_dist = :array.get(dist, acc) - 2 * cnt
          cur_delta = :array.get(delta, acc) + 2 * cnt

          acc
          |> :array.set(dist, cur_dist)
          |> :array.set(delta, cur_delta)
        else
          acc
        end
      end)
    else
      ans
    end
    |> (fn final_ans ->
          Enum.map(1..n, fn k -> :array.get(k, final_ans) end)
        end).()
  end
end
```
