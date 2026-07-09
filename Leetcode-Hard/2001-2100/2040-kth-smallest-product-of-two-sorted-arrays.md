# 2040. Kth Smallest Product of Two Sorted Arrays

## Cpp

```cpp
class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        int n1 = nums1.size(), n2 = nums2.size();
        auto countLE = [&](long long x)->long long{
            long long cnt = 0;
            for (int a : nums1) {
                if (a == 0) {
                    if (x >= 0) cnt += n2;
                    continue;
                }
                int l = 0, r = n2; // first index where product > x
                while (l < r) {
                    int m = (l + r) >> 1;
                    __int128 prod = (__int128)a * nums2[m];
                    if (prod <= x)
                        l = m + 1;
                    else
                        r = m;
                }
                cnt += l;
            }
            return cnt;
        };
        
        long long low = -100000LL * 100000LL - 5; // -1e10-5
        long long high = 100000LL * 100000LL + 5; // 1e10+5
        while (low < high) {
            long long mid = low + (high - low) / 2;
            if (countLE(mid) >= k)
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
    public long kthSmallestProduct(int[] nums1, int[] nums2, long k) {
        int n = nums1.length;
        int m = nums2.length;
        long low = -100000L * 100000L - 5; // -1e10-5
        long high = 100000L * 100000L + 5; // 1e10+5

        while (low < high) {
            long mid = low + (high - low) / 2;
            if (countLE(nums1, nums2, mid) >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private long countLE(int[] a, int[] b, long target) {
        int n = a.length;
        int m = b.length;
        long cnt = 0;
        for (int x : a) {
            if (x > 0) {
                // product increases with b
                int l = 0, r = m - 1, pos = -1;
                while (l <= r) {
                    int mid = (l + r) >>> 1;
                    long prod = (long) x * b[mid];
                    if (prod <= target) {
                        pos = mid;
                        l = mid + 1;
                    } else {
                        r = mid - 1;
                    }
                }
                cnt += (pos + 1);
            } else if (x < 0) {
                // product decreases with b
                int l = 0, r = m - 1, pos = m; // first index satisfying prod <= target
                while (l <= r) {
                    int mid = (l + r) >>> 1;
                    long prod = (long) x * b[mid];
                    if (prod <= target) {
                        pos = mid;
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                }
                cnt += (m - pos);
            } else { // x == 0
                if (target >= 0) {
                    cnt += m;
                }
                // else add 0
            }
        }
        return cnt;
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        n2 = len(nums2)

        def ceil_div(p, q):
            # ceil(p / q) for any non‑zero q
            return -((-p) // q)

        def count_le(x):
            total = 0
            for a in nums1:
                if a > 0:
                    # need b <= x // a
                    cnt = bisect.bisect_right(nums2, x // a)
                    total += cnt
                elif a < 0:
                    # need b >= ceil(x / a)
                    thresh = ceil_div(x, a)
                    idx = bisect.bisect_left(nums2, thresh)
                    total += n2 - idx
                else:  # a == 0
                    if x >= 0:
                        total += n2
            return total

        lo = -10**10 - 1  # exclusive lower bound
        hi = 10**10 + 1   # inclusive upper bound (answer lies within)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid
        return hi
```

## Python3

```python
import bisect, math
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n2 = len(nums2)

        def count_le(x: int) -> int:
            cnt = 0
            for a in nums1:
                if a > 0:
                    limit = x // a
                    cnt += bisect.bisect_right(nums2, limit)
                elif a == 0:
                    if x >= 0:
                        cnt += n2
                else:  # a < 0
                    limit = math.ceil(x / a)  # a is negative
                    idx = bisect.bisect_left(nums2, limit)
                    cnt += n2 - idx
            return cnt

        lo = -10**10 - 1
        hi = 10**10 + 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid
        return hi
```

## C

```c
#include <stddef.h>

static long long countLessOrEqual(const int *nums1, int n1, const int *nums2, int n2, long long target) {
    long long cnt = 0;
    for (int i = 0; i < n1; ++i) {
        int x = nums1[i];
        if (x == 0) {
            if (target >= 0) cnt += n2;
            continue;
        }
        if (x > 0) {
            int l = 0, r = n2 - 1, pos = -1;
            while (l <= r) {
                int m = l + ((r - l) >> 1);
                long long prod = (long long)x * nums2[m];
                if (prod <= target) {
                    pos = m;
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            cnt += (pos + 1);
        } else { // x < 0
            int l = 0, r = n2 - 1, pos = n2;
            while (l <= r) {
                int m = l + ((r - l) >> 1);
                long long prod = (long long)x * nums2[m];
                if (prod <= target) {
                    pos = m;
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
            cnt += (n2 - pos);
        }
    }
    return cnt;
}

long long kthSmallestProduct(int* nums1, int nums1Size, int* nums2, int nums2Size, long long k) {
    long long lo = -10000000000LL - 5; // less than minimal possible product
    long long hi =  10000000000LL + 5; // greater than maximal possible product
    while (lo < hi) {
        long long mid = lo + ((hi - lo) >> 1);
        if (countLessOrEqual(nums1, nums1Size, nums2, nums2Size, mid) >= k)
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public long KthSmallestProduct(int[] nums1, int[] nums2, long k) {
        // arrays are already sorted according to problem statement
        long low = -100000L * 100000L - 1;   // smaller than any possible product
        long high = 100000L * 100000L + 1;   // larger than any possible product

        while (low + 1 < high) {
            long mid = low + (high - low) / 2;
            if (CountLessOrEqual(mid, nums1, nums2) >= k)
                high = mid;
            else
                low = mid;
        }
        return high;
    }

    private static long CountLessOrEqual(long x, int[] aArr, int[] bArr) {
        int n1 = aArr.Length, n2 = bArr.Length;
        long cnt = 0;

        for (int i = 0; i < n1; ++i) {
            long a = aArr[i];
            if (a == 0) {
                if (x >= 0) cnt += n2;
                continue;
            }
            if (a > 0) {
                // find first index where product > x, count of <= x is that index
                int l = 0, r = n2;
                while (l < r) {
                    int m = (l + r) >> 1;
                    long prod = a * (long)bArr[m];
                    if (prod <= x)
                        l = m + 1;
                    else
                        r = m;
                }
                cnt += l;
            } else { // a < 0
                // products decrease with increasing b, find first index where product <= x
                int l = 0, r = n2;
                while (l < r) {
                    int m = (l + r) >> 1;
                    long prod = a * (long)bArr[m];
                    if (prod <= x)
                        r = m;
                    else
                        l = m + 1;
                }
                cnt += n2 - l;
            }
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var kthSmallestProduct = function(nums1, nums2, k) {
    const n2 = nums2.length;

    // count of products <= val
    const countLE = (val) => {
        let cnt = 0;
        for (let x of nums1) {
            if (x === 0) {
                if (val >= 0) cnt += n2;
                continue;
            }
            if (x > 0) {
                // y <= floor(val / x)
                const target = Math.floor(val / x);
                // upper bound: first index > target
                let l = 0, r = n2;
                while (l < r) {
                    const m = (l + r) >> 1;
                    if (nums2[m] <= target) l = m + 1;
                    else r = m;
                }
                cnt += l;
            } else { // x < 0
                // y >= ceil(val / x)
                const target = Math.ceil(val / x);
                // lower bound: first index >= target
                let l = 0, r = n2;
                while (l < r) {
                    const m = (l + r) >> 1;
                    if (nums2[m] >= target) r = m;
                    else l = m + 1;
                }
                cnt += n2 - l;
            }
            // early exit to avoid unnecessary work
            if (cnt >= k) break;
        }
        return cnt;
    };

    let low = -10000000000 - 5;   // -1e10 - epsilon
    let high = 10000000000 + 5;   // 1e10 + epsilon

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (countLE(mid) >= k) {
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
function kthSmallestProduct(nums1: number[], nums2: number[], k: number): number {
    const n2 = nums2.length;

    function countLE(v: number): number {
        let cnt = 0;
        for (const a of nums1) {
            if (a === 0) {
                if (v >= 0) cnt += n2;
                continue;
            }
            if (a > 0) {
                const limit = Math.floor(v / a);
                // upper bound: first index with value > limit
                let lo = 0, hi = n2;
                while (lo < hi) {
                    const mid = (lo + hi) >> 1;
                    if (nums2[mid] <= limit) lo = mid + 1;
                    else hi = mid;
                }
                cnt += lo;
            } else { // a < 0
                // find first index where a * nums2[idx] <= v
                let lo = 0, hi = n2;
                while (lo < hi) {
                    const mid = (lo + hi) >> 1;
                    if (a * nums2[mid] > v) lo = mid + 1;
                    else hi = mid;
                }
                cnt += n2 - lo;
            }
            if (cnt >= k) break; // early exit
        }
        return cnt;
    }

    let left = -1e10 - 5;
    let right = 1e10 + 5;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (countLE(mid) >= k) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function kthSmallestProduct($nums1, $nums2, $k) {
        $n2 = count($nums2);
        // helper closure to count pairs <= mid
        $countLE = function($mid) use ($nums1, $nums2, $n2) {
            $cnt = 0;
            foreach ($nums1 as $x) {
                if ($x >= 0) {
                    // binary search for first index where product > mid
                    $lo = 0;
                    $hi = $n2; // exclusive
                    while ($lo < $hi) {
                        $m = intdiv($lo + $hi, 2);
                        if ($x * $nums2[$m] <= $mid) {
                            $lo = $m + 1;
                        } else {
                            $hi = $m;
                        }
                    }
                    $cnt += $lo; // number of valid j
                } else { // x < 0
                    // products decrease as nums2 increases
                    $lo = 0;
                    $hi = $n2;
                    while ($lo < $hi) {
                        $m = intdiv($lo + $hi, 2);
                        if ($x * $nums2[$m] <= $mid) {
                            $hi = $m; // move left
                        } else {
                            $lo = $m + 1;
                        }
                    }
                    $cnt += $n2 - $lo;
                }
            }
            return $cnt;
        };
        
        $low = -10000000001; // less than minimal possible product
        $high = 10000000001; // greater than maximal possible product
        
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($countLE($mid) >= $k) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func kthSmallestProduct(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        let n2 = nums2.count
        // Helper to count products <= x
        func countLE(_ x: Int64) -> Int64 {
            var cnt: Int64 = 0
            for a in nums1 {
                if a >= 0 {
                    var l = 0, r = n2
                    while l < r {
                        let m = (l + r) >> 1
                        let prod = Int64(a) * Int64(nums2[m])
                        if prod <= x {
                            l = m + 1
                        } else {
                            r = m
                        }
                    }
                    cnt += Int64(l)
                } else {
                    var l = 0, r = n2
                    while l < r {
                        let m = (l + r) >> 1
                        let prod = Int64(a) * Int64(nums2[m])
                        if prod <= x {
                            r = m
                        } else {
                            l = m + 1
                        }
                    }
                    cnt += Int64(n2 - l)
                }
            }
            return cnt
        }

        let INF: Int64 = 10_000_000_000 // 1e10
        var lo: Int64 = -INF - 1
        var hi: Int64 = INF + 1

        while lo + 1 < hi {
            let mid = lo + (hi - lo) / 2
            if countLE(mid) >= Int64(k) {
                hi = mid
            } else {
                lo = mid
            }
        }
        return Int(hi)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthSmallestProduct(nums1: IntArray, nums2: IntArray, k: Long): Long {
        val n2 = nums2.size
        fun countLe(v: Long): Long {
            var cnt = 0L
            for (x in nums1) {
                if (x >= 0) {
                    var l = 0
                    var r = n2
                    while (l < r) {
                        val m = (l + r) ushr 1
                        if (x.toLong() * nums2[m].toLong() <= v) {
                            l = m + 1
                        } else {
                            r = m
                        }
                    }
                    cnt += l.toLong()
                } else {
                    var l = 0
                    var r = n2
                    while (l < r) {
                        val m = (l + r) ushr 1
                        if (x.toLong() * nums2[m].toLong() <= v) {
                            r = m
                        } else {
                            l = m + 1
                        }
                    }
                    cnt += (n2 - l).toLong()
                }
            }
            return cnt
        }

        var left = -100000L * 100000L - 1   // exclusive lower bound
        var right = 100000L * 100000L + 1   // inclusive upper bound

        while (left + 1 < right) {
            val mid = left + (right - left) / 2
            if (countLe(mid) >= k) {
                right = mid
            } else {
                left = mid
            }
        }
        return right
    }
}
```

## Dart

```dart
class Solution {
  int kthSmallestProduct(List<int> nums1, List<int> nums2, int k) {
    const int INF = 10000000000; // 1e10
    int left = -INF - 5;
    int right = INF + 5;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (_countLE(nums1, nums2, mid) >= k) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }

  int _countLE(List<int> a, List<int> b, int v) {
    int n2 = b.length;
    int total = 0;
    for (int x in a) {
      if (x == 0) {
        if (v >= 0) total += n2;
        continue;
      }
      if (x > 0) {
        int lo = 0, hi = n2;
        while (lo < hi) {
          int mid = (lo + hi) >> 1;
          if (x * b[mid] <= v) {
            lo = mid + 1;
          } else {
            hi = mid;
          }
        }
        total += lo;
      } else { // x < 0
        int lo = 0, hi = n2;
        while (lo < hi) {
          int mid = (lo + hi) >> 1;
          if (x * b[mid] <= v) {
            hi = mid;
          } else {
            lo = mid + 1;
          }
        }
        total += n2 - lo;
      }
    }
    return total;
  }
}
```

## Golang

```go
func kthSmallestProduct(nums1 []int, nums2 []int, k int64) int64 {
	n2 := len(nums2)

	// count of products <= v
	countLE := func(v int64) int64 {
		var cnt int64
		for _, a := range nums1 {
			if a >= 0 {
				lo, hi := 0, n2
				for lo < hi {
					mid := (lo + hi) / 2
					prod := int64(a) * int64(nums2[mid])
					if prod <= v {
						lo = mid + 1
					} else {
						hi = mid
					}
				}
				cnt += int64(lo)
			} else {
				lo, hi := 0, n2
				for lo < hi {
					mid := (lo + hi) / 2
					prod := int64(a) * int64(nums2[mid])
					if prod <= v {
						hi = mid
					} else {
						lo = mid + 1
					}
				}
				cnt += int64(n2 - lo)
			}
		}
		return cnt
	}

	low := int64(-10000000000) - 5
	high := int64(10000000000) + 5

	for low < high {
		mid := (low + high) / 2
		if countLE(mid) >= k {
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
def count_le(v, nums1, nums2)
  n2 = nums2.length
  total = 0
  nums1.each do |x|
    if x > 0
      limit = v / x
      lo = 0
      hi = n2
      while lo < hi
        mid = (lo + hi) >> 1
        if nums2[mid] <= limit
          lo = mid + 1
        else
          hi = mid
        end
      end
      total += lo
    elsif x == 0
      total += v >= 0 ? n2 : 0
    else # x < 0
      lo = 0
      hi = n2
      while lo < hi
        mid = (lo + hi) >> 1
        if x * nums2[mid] <= v
          hi = mid
        else
          lo = mid + 1
        end
      end
      total += n2 - lo
    end
  end
  total
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def kth_smallest_product(nums1, nums2, k)
  low = -10**10 - 1
  high = 10**10 + 1
  while low < high
    mid = (low + high) >> 1
    cnt = count_le(mid, nums1, nums2)
    if cnt >= k
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
    def kthSmallestProduct(nums1: Array[Int], nums2: Array[Int], k: Long): Long = {
        val n2 = nums2.length

        def countLE(v: Long): Long = {
            var cnt: Long = 0L
            for (x <- nums1) {
                val xv = x.toLong
                if (xv >= 0) {
                    var l = 0
                    var r = n2
                    while (l < r) {
                        val m = (l + r) >>> 1
                        if (xv * nums2(m).toLong <= v) l = m + 1 else r = m
                    }
                    cnt += l.toLong
                } else {
                    var l = 0
                    var r = n2
                    while (l < r) {
                        val m = (l + r) >>> 1
                        if (xv * nums2(m).toLong <= v) r = m else l = m + 1
                    }
                    cnt += (n2 - l).toLong
                }
            }
            cnt
        }

        var lo: Long = -100000L * 100000L - 5L   // less than minimal possible product
        var hi: Long = 100000L * 100000L + 5L    // greater than maximal possible product

        while (lo + 1 < hi) {
            val mid = lo + (hi - lo) / 2
            if (countLE(mid) >= k) hi = mid else lo = mid
        }
        hi
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_smallest_product(nums1: Vec<i32>, nums2: Vec<i32>, k: i64) -> i64 {
        fn count_le(v: i64, a: &[i32], b: &[i32]) -> i64 {
            let n2 = b.len() as i64;
            let mut cnt: i64 = 0;
            for &x in a.iter() {
                if x >= 0 {
                    // nums2 is sorted ascending, product non‑decreasing
                    let mut l = 0usize;
                    let mut r = b.len();
                    while l < r {
                        let m = (l + r) / 2;
                        let prod = (x as i64) * (b[m] as i64);
                        if prod <= v {
                            l = m + 1;
                        } else {
                            r = m;
                        }
                    }
                    cnt += l as i64; // number of valid j
                } else {
                    // x < 0, product non‑increasing
                    let mut l = 0usize;
                    let mut r = b.len();
                    while l < r {
                        let m = (l + r) / 2;
                        let prod = (x as i64) * (b[m] as i64);
                        if prod <= v {
                            r = m; // move left to find first <= v
                        } else {
                            l = m + 1;
                        }
                    }
                    cnt += n2 - l as i64; // indices from l .. end satisfy <= v
                }
            }
            cnt
        }

        let mut left: i64 = -10_000_000_001; // less than any possible product
        let mut right: i64 = 10_000_000_001; // greater than any possible product

        while left + 1 < right {
            let mid = left + (right - left) / 2;
            if count_le(mid, &nums1, &nums2) >= k {
                right = mid;
            } else {
                left = mid;
            }
        }
        right
    }
}
```

## Racket

```racket
(define (kth-smallest-product nums1 nums2 k)
  (let* ((v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (n1 (vector-length v1))
         (n2 (vector-length v2)))
    (define (count-le v)
      (let loop ((i 0) (cnt 0))
        (if (= i n1)
            cnt
            (let ((a (vector-ref v1 i)))
              (cond
                [(zero? a)
                 (if (<= 0 v)
                     (loop (+ i 1) (+ cnt n2))
                     (loop (+ i 1) cnt))]
                [(positive? a)
                 (let rec ((lo 0) (hi n2))
                   (if (= lo hi)
                       (loop (+ i 1) (+ cnt lo))
                       (let ((mid (quotient (+ lo hi) 2)))
                         (if (<= (* a (vector-ref v2 mid)) v)
                             (rec (+ mid 1) hi)
                             (rec lo mid))))))]
                [else ; a < 0
                 (let rec ((lo 0) (hi n2))
                   (if (= lo hi)
                       (loop (+ i 1) (+ cnt (- n2 lo)))
                       (let ((mid (quotient (+ lo hi) 2)))
                         (if (<= (* a (vector-ref v2 mid)) v)
                             (rec lo mid)
                             (rec (+ mid 1) hi)))))])))))
    (let loop ((lo -10000000001) (hi 10000000001))
      (if (= lo hi)
          lo
          (let* ((mid (floor (/ (+ lo hi) 2)))
                 (cnt (count-le mid)))
            (if (>= cnt k)
                (loop lo mid)
                (loop (+ mid 1) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([kth_smallest_product/3]).

-spec kth_smallest_product(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
kth_smallest_product(Nums1, Nums2, K) ->
    A = array:from_list(Nums1),
    B = array:from_list(Nums2),
    N1 = length(Nums1),
    N2 = length(Nums2),
    Low = -10000000000,
    High = 10000000001,
    binary_search(Low, High, A, B, N1, N2, K).

binary_search(Low, High, _A, _B, _N1, _N2, _K) when Low >= High ->
    Low;
binary_search(Low, High, A, B, N1, N2, K) ->
    Mid = (Low + High) div 2,
    Cnt = count_le(Mid, A, B, N1, N2),
    if
        Cnt >= K -> binary_search(Low, Mid, A, B, N1, N2, K);
        true     -> binary_search(Mid + 1, High, A, B, N1, N2, K)
    end.

count_le(V, A, B, N1, N2) ->
    count_le_loop(0, V, A, B, N1, N2, 0).

count_le_loop(I, _V, _A, _B, N1, _N2, Acc) when I == N1 ->
    Acc;
count_le_loop(I, V, A, B, N1, N2, Acc) ->
    X = array:get(I, A),
    Add =
        case X of
            0 ->
                if V >= 0 -> N2; true -> 0 end;
            _ when X > 0 ->
                Limit = floor_div(V, X),
                upper_bound(B, N2, Limit);
            _ -> % X < 0
                Limit = ceil_div(V, X),
                N2 - lower_bound(B, N2, Limit)
        end,
    count_le_loop(I + 1, V, A, B, N1, N2, Acc + Add).

%% floor division for positive divisor
floor_div(V, X) when V >= 0 -> V div X;
floor_div(V, X) -> (V - (X - 1)) div X.

%% ceil division for negative divisor
ceil_div(V, X) ->
    Q = V div X,
    R = V rem X,
    if R == 0 -> Q; true -> Q + 1 end.

upper_bound(Array, Len, Val) ->
    ub(0, Len, Array, Val).

ub(Low, High, _Array, _Val) when Low >= High -> Low;
ub(Low, High, Array, Val) ->
    Mid = (Low + High) div 2,
    case array:get(Mid, Array) =< Val of
        true  -> ub(Mid + 1, High, Array, Val);
        false -> ub(Low, Mid, Array, Val)
    end.

lower_bound(Array, Len, Val) ->
    lb(0, Len, Array, Val).

lb(Low, High, _Array, _Val) when Low >= High -> Low;
lb(Low, High, Array, Val) ->
    Mid = (Low + High) div 2,
    case array:get(Mid, Array) < Val of
        true  -> lb(Mid + 1, High, Array, Val);
        false -> lb(Low, Mid, Array, Val)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_smallest_product(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def kth_smallest_product(nums1, nums2, k) do
    nums2_t = List.to_tuple(nums2)
    m = tuple_size(nums2_t)

    low = -10_000_000_000 - 1
    high = 10_000_000_000 + 1

    binary_search(low, high, nums1, nums2_t, m, k)
  end

  defp binary_search(low, high, nums1, nums2_t, m, k) do
    if low < high do
      mid = div(low + high, 2)
      cnt = count_le(nums1, nums2_t, m, mid)

      if cnt >= k do
        binary_search(low, mid, nums1, nums2_t, m, k)
      else
        binary_search(mid + 1, high, nums1, nums2_t, m, k)
      end
    else
      low
    end
  end

  defp count_le(nums1, nums2_t, m, v) do
    Enum.reduce(nums1, 0, fn x, acc ->
      cond do
        x == 0 ->
          if v >= 0, do: acc + m, else: acc

        x > 0 ->
          limit = floor_div(v, x)
          cnt = upper_bound(nums2_t, m, limit)
          acc + cnt

        true -> # x < 0
          idx = lower_bound_negative_product(nums2_t, m, x, v)
          acc + (m - idx)
      end
    end)
  end

  defp floor_div(a, b) when b > 0 do
    if a >= 0 do
      div(a, b)
    else
      -div(-a + b - 1, b)
    end
  end

  # number of elements <= target
  defp upper_bound(arr_t, m, target) do
    lo = 0
    hi = m

    while lo < hi do
      mid = div(lo + hi, 2)

      if :erlang.element(mid + 1, arr_t) <= target do
        lo = mid + 1
      else
        hi = mid
      end
    end

    lo
  end

  # first index where x * arr[idx] <= v (arr sorted ascending)
  defp lower_bound_negative_product(arr_t, m, x, v) do
    lo = 0
    hi = m

    while lo < hi do
      mid = div(lo + hi, 2)

      if x * :erlang.element(mid + 1, arr_t) <= v do
        hi = mid
      else
        lo = mid + 1
      end
    end

    lo
  end
end
```
