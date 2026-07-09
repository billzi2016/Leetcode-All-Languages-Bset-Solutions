# 3574. Maximize Subarray GCD Score

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxGCDScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> v(n);
        vector<long long> odd(n);
        for (int i = 0; i < n; ++i) {
            v[i] = __builtin_ctz(nums[i]);               // exponent of 2
            odd[i] = nums[i] >> v[i];                     // odd part
        }
        long long best = 0;
        for (int l = 0; l < n; ++l) {
            long long curGcd = 0;
            int minV = INT_MAX;
            int cntMin = 0;
            for (int r = l; r < n; ++r) {
                curGcd = std::gcd(curGcd, odd[r]);
                if (v[r] < minV) {
                    minV = v[r];
                    cntMin = 1;
                } else if (v[r] == minV) {
                    ++cntMin;
                }
                __int128 g = (__int128)curGcd << minV; // base GCD
                if (cntMin <= k) g <<= 1;              // can increase by one power of two
                long long len = r - l + 1;
                __int128 score = g * len;
                if (score > best) best = (long long)score;
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public long maxGCDScore(int[] nums, int k) {
        int n = nums.length;
        int[] exp = new int[n];
        int[] odd = new int[n];
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            int cnt = 0;
            while ((v & 1) == 0) {
                cnt++;
                v >>= 1;
            }
            exp[i] = cnt;
            odd[i] = v;
        }

        long best = 0L;
        for (int i = 0; i < n; i++) {
            int curGcd = 0;
            int minExp = Integer.MAX_VALUE;
            int cntMin = 0;
            for (int j = i; j < n; j++) {
                curGcd = gcd(curGcd, odd[j]);

                if (exp[j] < minExp) {
                    minExp = exp[j];
                    cntMin = 1;
                } else if (exp[j] == minExp) {
                    cntMin++;
                }

                int effectiveExp = minExp;
                if (cntMin <= k) {
                    effectiveExp = minExp + 1;
                }

                long length = j - i + 1L;
                long factor2 = 1L << effectiveExp; // safe as exponent <= ~31
                long score = length * curGcd * factor2;
                if (score > best) {
                    best = score;
                }
            }
        }
        return best;
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
class Solution(object):
    def maxGCDScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import math
        n = len(nums)
        e = [0] * n          # exponent of 2 in each number
        odd = [0] * n        # odd part after removing all factors of 2
        for i, val in enumerate(nums):
            cnt = 0
            while (val & 1) == 0:
                cnt += 1
                val >>= 1
            e[i] = cnt
            odd[i] = val

        best = 0
        for l in range(n):
            cur_gcd = 0
            min_e = 10**9
            cnt_min = 0
            for r in range(l, n):
                # update gcd of odd parts
                if cur_gcd == 0:
                    cur_gcd = odd[r]
                else:
                    cur_gcd = math.gcd(cur_gcd, odd[r])

                # update minimum exponent and its count
                if e[r] < min_e:
                    min_e = e[r]
                    cnt_min = 1
                elif e[r] == min_e:
                    cnt_min += 1

                length = r - l + 1
                exp = min_e + (1 if cnt_min <= k else 0)
                score = length * cur_gcd * (1 << exp)
                if score > best:
                    best = score
        return best
```

## Python3

```python
import math
from typing import List

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [0] * n
        exp = [0] * n
        for i, v in enumerate(nums):
            e = 0
            while v % 2 == 0:
                v //= 2
                e += 1
            odd[i] = v
            exp[i] = e

        best = 0
        INF = 10 ** 9
        for l in range(n):
            g = 0
            min_exp = INF
            cnt_min = 0
            for r in range(l, n):
                # update odd gcd
                if g == 0:
                    g = odd[r]
                else:
                    g = math.gcd(g, odd[r])
                e = exp[r]
                if e < min_exp:
                    min_exp = e
                    cnt_min = 1
                elif e == min_exp:
                    cnt_min += 1

                # determine achievable minimal exponent after at most k doublings
                if cnt_min <= k:
                    t = min_exp + 1
                else:
                    t = min_exp

                length = r - l + 1
                score = length * g * (1 << t)
                if score > best:
                    best = score
        return best
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

long long maxGCDScore(int* nums, int numsSize, int k) {
    long long best = 0;
    for (int i = 0; i < numsSize; ++i) {
        long long cur_gcd = 0;
        int min_pow = 31; // larger than any possible v2 for nums[i] <= 1e9
        int cnt_min = 0;
        for (int j = i; j < numsSize; ++j) {
            int val = nums[j];
            cur_gcd = std::gcd(cur_gcd, (long long)val);
            int v2 = __builtin_ctz(val); // count trailing zeros
            if (v2 < min_pow) {
                min_pow = v2;
                cnt_min = 1;
            } else if (v2 == min_pow) {
                ++cnt_min;
            }
            long long len = j - i + 1;
            long long score = len * cur_gcd;
            if (cnt_min <= k) score <<= 1; // multiply by 2
            if (score > best) best = score;
        }
    }
    return best;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private static long Gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public long MaxGCDScore(int[] nums, int k) {
        int n = nums.Length;
        int[] exp = new int[n];
        int[] odd = new int[n];
        for (int i = 0; i < n; i++) {
            exp[i] = IntegerNumberOfTrailingZeros(nums[i]);
            odd[i] = nums[i] >> exp[i];
        }

        long best = 0;
        const int MAX_EXP = 31; // enough for original exponents up to 30

        for (int l = 0; l < n; l++) {
            int[] cnt = new int[MAX_EXP];
            int curMinExp = MAX_EXP; // sentinel larger than any possible exponent
            long curGcdOdd = 0;

            for (int r = l; r < n; r++) {
                int e = exp[r];
                cnt[e]++;
                if (e < curMinExp) curMinExp = e;
                curGcdOdd = Gcd(curGcdOdd, odd[r]);

                int cntMin = cnt[curMinExp];
                long finalExp = curMinExp + ((cntMin <= k) ? 1 : 0);
                long gcdVal = curGcdOdd * (1L << (int)finalExp);
                long score = (long)(r - l + 1) * gcdVal;
                if (score > best) best = score;
            }
        }

        return best;
    }

    // Helper to compute trailing zeros without using built‑in for compatibility
    private static int IntegerNumberOfTrailingZeros(int value) {
        // value is positive, so at least one bit set
        int count = 0;
        while ((value & 1) == 0) {
            count++;
            value >>= 1;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxGCDScore = function(nums, k) {
    const n = nums.length;
    // Preprocess exponent of 2 and odd part
    const exp = new Array(n);
    const odd = new Array(n);
    for (let i = 0; i < n; ++i) {
        let x = nums[i];
        let e = 0;
        while ((x & 1) === 0) { // count trailing zeros
            x >>>= 1;
            ++e;
        }
        exp[i] = e;
        odd[i] = x; // now odd
    }

    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let best = 0;

    for (let i = 0; i < n; ++i) {
        let curGcdOdd = 0;
        let curMinExp = Infinity;
        let cntMin = 0;
        for (let j = i; j < n; ++j) {
            // update odd gcd
            curGcdOdd = gcd(curGcdOdd, odd[j]);

            const e = exp[j];
            if (e < curMinExp) {
                curMinExp = e;
                cntMin = 1;
            } else if (e === curMinExp) {
                ++cntMin;
            }

            const effectiveMin = curMinExp + (k >= cntMin ? 1 : 0);
            const len = j - i + 1;
            const score = len * curGcdOdd * Math.pow(2, effectiveMin);
            if (score > best) best = score;
        }
    }

    return best;
};
```

## Typescript

```typescript
function maxGCDScore(nums: number[], k: number): number {
    const n = nums.length;
    const exps = new Array<number>(n);
    const odds = new Array<number>(n);

    for (let i = 0; i < n; i++) {
        let x = nums[i];
        let e = 0;
        while ((x & 1) === 0) { // while even
            x = Math.floor(x / 2);
            e++;
        }
        exps[i] = e;
        odds[i] = x; // odd part
    }

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let ans = 0;

    for (let l = 0; l < n; l++) {
        let curGcdOdd = 0;
        let minExp = Infinity;
        let cntMin = 0;

        for (let r = l; r < n; r++) {
            const e = exps[r];
            const o = odds[r];

            if (curGcdOdd === 0) curGcdOdd = o;
            else curGcdOdd = gcd(curGcdOdd, o);

            if (e < minExp) {
                minExp = e;
                cntMin = 1;
            } else if (e === minExp) {
                cntMin++;
            }

            const len = r - l + 1;
            let g = curGcdOdd * Math.pow(2, minExp);
            if (cntMin <= k) g *= 2; // we can raise the minimal exponent by 1
            const score = len * g;
            if (score > ans) ans = score;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxGCDScore($nums, $k) {
        $n = count($nums);
        $odd = [];
        $exp = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $e = 0;
            while (($x & 1) == 0) {
                $x >>= 1;
                $e++;
            }
            $odd[$i] = $x;
            $exp[$i] = $e;
        }

        $maxScore = 0;

        for ($l = 0; $l < $n; $l++) {
            // reset counts of exponents
            $counts = array_fill(0, 61, 0);
            $curOddGcd = 0;
            for ($r = $l; $r < $n; $r++) {
                $curOddGcd = $this->gcd($curOddGcd, $odd[$r]);
                $counts[$exp[$r]]++;

                // compute minimal exponent after at most k doublings
                $remainingK = $k;
                $carry = 0;
                $minExp = 60; // default if all can be raised beyond this
                for ($e = 0; $e <= 60; $e++) {
                    $cntAtE = $counts[$e] + $carry;
                    if ($cntAtE == 0) {
                        continue;
                    }
                    if ($cntAtE <= $remainingK) {
                        $remainingK -= $cntAtE;
                        $carry = $cntAtE; // all move to next level
                    } else {
                        $minExp = $e;
                        break;
                    }
                }

                // compute score
                $gcdVal = $curOddGcd * (1 << $minExp);
                $len = $r - $l + 1;
                $score = $len * $gcdVal;
                if ($score > $maxScore) {
                    $maxScore = $score;
                }
            }
        }

        return $maxScore;
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
    func maxGCDScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var best: Int64 = 0
        for left in 0..<n {
            var currentGcd: Int64 = 0
            var minCnt = Int.max
            var cntMin = 0
            for right in left..<n {
                var value = nums[right]
                var cnt = 0
                while (value & 1) == 0 {
                    value >>= 1
                    cnt += 1
                }
                let oddPart = Int64(value)
                currentGcd = gcd(currentGcd, oddPart)
                
                if cnt < minCnt {
                    minCnt = cnt
                    cntMin = 1
                } else if cnt == minCnt {
                    cntMin += 1
                }
                
                var exponent = minCnt
                if cntMin <= k { exponent += 1 }
                
                let length = Int64(right - left + 1)
                let pow2: Int64 = Int64(1) << exponent
                let score = length * currentGcd * pow2
                if score > best {
                    best = score
                }
            }
        }
        return Int(best)
    }
    
    private func gcd(_ a: Int64, _ b: Int64) -> Int64 {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun maxGCDScore(nums: IntArray, k: Int): Long {
        val n = nums.size
        val vArr = IntArray(n)
        val base = IntArray(n)
        var maxV = 0
        for (i in 0 until n) {
            val tz = Integer.numberOfTrailingZeros(nums[i])
            vArr[i] = tz
            base[i] = nums[i] ushr tz
            if (tz > maxV) maxV = tz
        }
        val pow2 = LongArray(maxV + 3)
        pow2[0] = 1L
        for (i in 1 until pow2.size) {
            pow2[i] = pow2[i - 1] shl 1
        }

        var ans = 0L
        for (l in 0 until n) {
            var curGcd = 0
            var minV = Int.MAX_VALUE
            var cntMin = 0
            for (r in l until n) {
                val b = base[r]
                curGcd = if (curGcd == 0) b else gcd(curGcd, b)

                val v = vArr[r]
                when {
                    v < minV -> {
                        minV = v
                        cntMin = 1
                    }
                    v == minV -> cntMin++
                }

                val len = r - l + 1
                var exp = minV
                if (cntMin <= k) exp += 1

                val score = len.toLong() * curGcd.toLong() * pow2[exp]
                if (score > ans) ans = score
            }
        }
        return ans
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  int maxGCDScore(List<int> nums, int k) {
    int n = nums.length;
    List<int> e = List.filled(n, 0);
    List<int> b = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int x = nums[i];
      int cnt = 0;
      while ((x & 1) == 0) {
        cnt++;
        x >>= 1;
      }
      e[i] = cnt;
      b[i] = x; // odd part
    }

    int _gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a;
    }

    int ans = 0;
    for (int l = 0; l < n; l++) {
      int curGcd = b[l];
      int minE = e[l];
      int cntMin = 1;
      for (int r = l; r < n; r++) {
        if (r > l) {
          curGcd = _gcd(curGcd, b[r]);
          if (e[r] < minE) {
            minE = e[r];
            cntMin = 1;
          } else if (e[r] == minE) {
            cntMin++;
          }
        }
        int len = r - l + 1;
        int pow = minE;
        if (cntMin <= k) pow = minE + 1;
        int g = curGcd * (1 << pow);
        int score = len * g;
        if (score > ans) ans = score;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxGCDScore(nums []int, k int) int64 {
	n := len(nums)
	odds := make([]int64, n)
	exps := make([]int, n)
	for i, v := range nums {
		e := 0
		for v%2 == 0 {
			v /= 2
			e++
		}
		odds[i] = int64(v)
		exps[i] = e
	}

	var ans int64 = 0
	const maxExp = 31 // larger than any possible exponent for nums ≤ 1e9

	for l := 0; l < n; l++ {
		var gOdd int64 = 0
		minExp := maxExp
		cntMin := 0
		for r := l; r < n; r++ {
			if gOdd == 0 {
				gOdd = odds[r]
			} else {
				gOdd = gcd(gOdd, odds[r])
			}
			e := exps[r]
			if e < minExp {
				minExp = e
				cntMin = 1
			} else if e == minExp {
				cntMin++
			}
			curGCD := gOdd << uint(minExp)
			if cntMin <= k {
				curGCD <<= 1
			}
			score := int64(r-l+1) * curGCD
			if score > ans {
				ans = score
			}
		}
	}
	return ans
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
```

## Ruby

```ruby
def max_gcd_score(nums, k)
  n = nums.length
  exps = Array.new(n)
  odds = Array.new(n)

  nums.each_with_index do |v, i|
    e = 0
    while (v & 1) == 0
      v >>= 1
      e += 1
    end
    exps[i] = e
    odds[i] = v
  end

  max_score = 0

  (0...n).each do |l|
    cur_gcd = 0
    min_exp = nil
    cnt_min = 0
    (l...n).each do |r|
      # update odd part gcd
      if cur_gcd == 0
        cur_gcd = odds[r]
      else
        cur_gcd = cur_gcd.gcd(odds[r])
      end

      e = exps[r]
      if min_exp.nil? || e < min_exp
        min_exp = e
        cnt_min = 1
      elsif e == min_exp
        cnt_min += 1
      end

      len = r - l + 1
      base = cur_gcd << min_exp   # multiply by 2^{min_exp}
      score = if cnt_min <= k
                len * base * 2
              else
                len * base
              end
      max_score = score if score > max_score
    end
  end

  max_score
end
```

## Scala

```scala
object Solution {
    def maxGCDScore(nums: Array[Int], k: Int): Long = {
        val n = nums.length
        val exp = new Array[Int](n)
        for (i <- 0 until n) {
            var v = nums(i)
            var cnt = 0
            while ((v & 1) == 0 && v != 0) {
                cnt += 1
                v >>= 1
            }
            exp(i) = cnt
        }

        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            Math.abs(x)
        }

        var ans: Long = 0L

        for (l <- 0 until n) {
            var curGcd = 0
            var minExp = Int.MaxValue
            var cntMin = 0
            var r = l
            while (r < n) {
                val x = nums(r)
                if (curGcd == 0) curGcd = x else curGcd = gcd(curGcd, x)

                val e = exp(r)
                if (e < minExp) {
                    minExp = e
                    cntMin = 1
                } else if (e == minExp) {
                    cntMin += 1
                }

                val len = r - l + 1
                var score = curGcd.toLong * len
                if (cntMin <= k) score *= 2L
                if (score > ans) ans = score

                r += 1
            }
        }

        ans
    }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn max_gcd_score(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut odds: Vec<i64> = Vec::with_capacity(n);
        let mut exps: Vec<i32> = Vec::with_capacity(n);
        for &v in &nums {
            let mut x = v as i64;
            let mut e = 0i32;
            while x % 2 == 0 {
                x /= 2;
                e += 1;
            }
            odds.push(x);
            exps.push(e);
        }

        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }

        let k_usize = k as usize;
        let mut best: i128 = 0;

        for l in 0..n {
            let mut g_odd: i64 = 0;
            let mut min_e: i32 = 31; // larger than any possible exponent
            let mut cnt_min: usize = 0;

            for r in l..n {
                let odd = odds[r];
                let e = exps[r];

                if g_odd == 0 {
                    g_odd = odd;
                } else {
                    g_odd = gcd(g_odd, odd);
                }

                if e < min_e {
                    min_e = e;
                    cnt_min = 1;
                } else if e == min_e {
                    cnt_min += 1;
                }

                let len = (r - l + 1) as i64;
                let mut exp_total = min_e as i64;
                if cnt_min <= k_usize {
                    exp_total += 1;
                }
                let power: i128 = 1i128 << exp_total; // safe, exp_total ≤ 31
                let score = (len as i128) * (g_odd as i128) * power;
                if score > best {
                    best = score;
                }
            }
        }

        best as i64
    }
}
```

## Racket

```racket
#lang racket
(require racket/math)

(define (max-gcd-score nums k)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (cand-hash (make-hash)))
    (define (add d) (hash-set! cand-hash d #t))
    ;; collect all possible divisors of a_i and 2*a_i
    (for ([x nums])
      (let ((limit (floor (sqrt x))))
        (let loop ((i 1))
          (when (<= i limit)
            (when (= (remainder x i) 0)
              (add i)
              (add (* 2 i))
              (let ((j (/ x i)))
                (unless (= i j)
                  (add j)
                  (add (* 2 j)))))
            (loop (+ i 1))))))
    ;; sort candidates descending
    (let* ((candidates (hash-keys cand-hash))
           (sorted (sort candidates >)))
      (let loop ((cs sorted) (best 0))
        (if (null? cs)
            best
            (let ((d (car cs)))
              (if (<= (* d n) best)
                  best
                  (let* ((status (make-vector n 0))
                         (maxlen 0)
                         (left 0)
                         (cnt 0))
                    ;; classify each element w.r.t. divisor d
                    (for ([i (in-range n)])
                      (define a (vector-ref arr i))
                      (cond [(zero? (remainder a d)) (vector-set! status i 0)]
                            [(zero? (remainder (* 2 a) d)) (vector-set! status i 1)]
                            [else (vector-set! status i -1)]))
                    ;; sliding window
                    (for ([right (in-range n)])
                      (define s (vector-ref status right))
                      (cond [(= s -1)
                             (set! left (+ right 1))
                             (set! cnt 0)]
                            [else
                             (when (= s 1) (set! cnt (+ cnt 1)))
                             ;; shrink while too many doubles
                             (let shrink ()
                               (when (> cnt k)
                                 (define sl (vector-ref status left))
                                 (when (= sl 1) (set! cnt (- cnt 1)))
                                 (set! left (+ left 1))
                                 (shrink)))
                             (let ((len (+ 1 (- right left))))
                               (when (> len maxlen) (set! maxlen len)))]))
                    (define score (* d maxlen))
                    (if (> score best)
                        (loop (cdr cs) score)
                        (loop (cdr cs) best))))))))))
```

## Erlang

```erlang
-spec max_gcd_score(Nums :: [integer()], K :: integer()) -> integer().
max_gcd_score(Nums, K) ->
    Processed = lists:map(fun(N) ->
        E = tz(N),
        O = N bsr E,
        {E, O}
    end, Nums),
    Tuple = list_to_tuple(Processed),
    N = tuple_size(Tuple),
    max_gcd_score_loop(1, N, Tuple, K, 0).

%% count trailing zeros (exponent of 2)
tz(N) -> tz(N, 0).
tz(N, Acc) when (N band 1) =:= 0 ->
    tz(N bsr 1, Acc + 1);
tz(_, Acc) -> Acc.

max_gcd_score_loop(I, N, _Tuple, _K, Max) when I > N ->
    Max;
max_gcd_score_loop(I, N, Tuple, K, Max) ->
    {E0, O0} = element(I, Tuple),
    Len0 = 1,
    ScoreBase0 = Len0 * O0 * (1 bsl E0),
    Cand0 = case E0 of
        _ when 1 =< K -> ScoreBase0 * 2;
        _ -> ScoreBase0
    end,
    NewMax = max(Max, Cand0),
    MaxAfterExtend = extend(I + 1, N, Tuple, K, I, Len0, O0, E0, 1, NewMax),
    max_gcd_score_loop(I + 1, N, Tuple, K, MaxAfterExtend).

%% Extend subarray starting at StartIdx, current position CurIdx (next to add)
extend(CurIdx, N, _Tuple, _K, _StartIdx, _Len, _GcdOdd, _MinE, _CntMin, Max) when CurIdx > N ->
    Max;
extend(CurIdx, N, Tuple, K, StartIdx, Len, GcdOdd, MinE, CntMin, Max) ->
    {E, O} = element(CurIdx, Tuple),
    NewLen = Len + 1,
    NewGcdOdd = erlang:gcd(GcdOdd, O),
    case E of
        _ when E < MinE -> UpdatedMinE = E, UpdatedCntMin = 1;
        _ when E == MinE -> UpdatedMinE = MinE, UpdatedCntMin = CntMin + 1;
        _ -> UpdatedMinE = MinE, UpdatedCntMin = CntMin
    end,
    ScoreBase = NewLen * NewGcdOdd * (1 bsl UpdatedMinE),
    Cand = case UpdatedCntMin =< K of
        true -> ScoreBase * 2;
        false -> ScoreBase
    end,
    NewMax = max(Max, Cand),
    extend(CurIdx + 1, N, Tuple, K, StartIdx, NewLen, NewGcdOdd, UpdatedMinE, UpdatedCntMin, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_gcd_score(nums :: [integer], k :: integer) :: integer
  def max_gcd_score(nums, k) do
    import Bitwise

    n = length(nums)

    # Precompute exponent of 2 and odd part for each number
    {exps_list, odds_list} =
      Enum.map_reduce(nums, [], fn num, _acc ->
        {e, odd} = count_trailing_zeros(num, 0)
        {[e | []], [odd | []]}
      end)

    exps = List.to_tuple(Enum.reverse(exps_list))
    odds = List.to_tuple(Enum.reverse(odds_list))

    # Outer loop over left index
    Enum.reduce(0..(n - 1), 0, fn l, max_score ->
      # Inner loop over right index, maintaining gcd, min exponent and its count
      {_gcd, _min_exp, _cnt_min, cur_max} =
        Enum.reduce(l..(n - 1), {0, 60, 0, max_score}, fn r,
                                                       {gcd_acc, min_e, cnt, cur_max} ->
          e = elem(exps, r)
          o = elem(odds, r)

          gcd_new =
            if r == l do
              o
            else
              Integer.gcd(gcd_acc, o)
            end

          {min_new, cnt_new} =
            cond do
              e < min_e -> {e, 1}
              e == min_e -> {min_e, cnt + 1}
              true -> {min_e, cnt}
            end

          len = r - l + 1
          pow = min_new + if(cnt_new <= k, do: 1, else: 0)
          total_gcd = gcd_new * shift_left(1, pow)
          score = len * total_gcd
          cur_max = if score > cur_max, do: score, else: cur_max

          {gcd_new, min_new, cnt_new, cur_max}
        end)

      cur_max
    end)
  end

  # Helper to count trailing zeros and obtain odd part
  defp count_trailing_zeros(0, _cnt), do: {0, 0}

  defp count_trailing_zeros(num, cnt) do
    if (num &&& 1) == 1 do
      {cnt, num}
    else
      count_trailing_zeros(num >>> 1, cnt + 1)
    end
  end
end
```
