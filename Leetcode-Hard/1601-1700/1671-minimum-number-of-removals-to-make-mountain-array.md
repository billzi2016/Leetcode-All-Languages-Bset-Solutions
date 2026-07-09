# 1671. Minimum Number of Removals to Make Mountain Array

## Cpp

```cpp
class Solution {
public:
    vector<int> lisLengths(const vector<int>& a) {
        int n = a.size();
        vector<int> res(n);
        vector<int> tail;
        tail.reserve(n);
        for (int i = 0; i < n; ++i) {
            auto it = lower_bound(tail.begin(), tail.end(), a[i]);
            int idx = it - tail.begin();
            if (it == tail.end()) tail.push_back(a[i]);
            else *it = a[i];
            res[i] = idx + 1;
        }
        return res;
    }

    int minimumMountainRemovals(vector<int>& nums) {
        int n = nums.size();
        vector<int> inc = lisLengths(nums);
        vector<int> revNums(nums.rbegin(), nums.rend());
        vector<int> decRev = lisLengths(revNums);
        vector<int> dec(n);
        for (int i = 0; i < n; ++i) {
            dec[i] = decRev[n - 1 - i];
        }

        int best = 0;
        for (int i = 0; i < n; ++i) {
            if (inc[i] > 1 && dec[i] > 1) {
                best = max(best, inc[i] + dec[i] - 1);
            }
        }
        return n - best;
    }
};
```

## Java

```java
class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int n = nums.length;
        int[] inc = new int[n];
        int[] dec = new int[n];
        
        // LIS from left
        int[] tail = new int[n];
        int len = 0;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int pos = lowerBound(tail, len, x);
            tail[pos] = x;
            if (pos == len) len++;
            inc[i] = pos + 1;
        }
        
        // LIS on reversed array to get LDS lengths
        int[] revTail = new int[n];
        int revLen = 0;
        for (int i = n - 1; i >= 0; i--) {
            int x = nums[i];
            int pos = lowerBound(revTail, revLen, x);
            revTail[pos] = x;
            if (pos == revLen) revLen++;
            dec[i] = pos + 1;
        }
        
        int ans = n; // worst case remove all but three
        for (int i = 0; i < n; i++) {
            if (inc[i] > 1 && dec[i] > 1) {
                int keep = inc[i] + dec[i] - 1;
                ans = Math.min(ans, n - keep);
            }
        }
        return ans;
    }
    
    private int lowerBound(int[] arr, int size, int target) {
        int lo = 0, hi = size;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # LIS lengths ending at each position
        lis_left = [0] * n
        tails = []
        for i, x in enumerate(nums):
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
            lis_left[i] = idx + 1

        # LDS lengths starting at each position (via reversed LIS)
        rev = nums[::-1]
        lis_rev = [0] * n
        tails.clear()
        for i, x in enumerate(rev):
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
            lis_rev[i] = idx + 1
        lds_right = lis_rev[::-1]

        min_remove = n  # upper bound
        for i in range(n):
            if lis_left[i] > 1 and lds_right[i] > 1:
                keep = lis_left[i] + lds_right[i] - 1
                removals = n - keep
                if removals < min_remove:
                    min_remove = removals
        return min_remove
```

## Python3

```python
class Solution:
    def minimumMountainRemovals(self, nums):
        from bisect import bisect_left

        def lis_lengths(arr):
            tails = []
            res = [0] * len(arr)
            for i, x in enumerate(arr):
                idx = bisect_left(tails, x)  # strict increasing
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
                res[i] = idx + 1
            return res

        n = len(nums)
        inc = lis_lengths(nums)
        dec = lis_lengths(nums[::-1])[::-1]

        best = 0
        for i in range(n):
            if inc[i] > 1 and dec[i] > 1:
                length = inc[i] + dec[i] - 1
                if length > best:
                    best = length

        return n - best
```

## C

```c
#include <stdlib.h>

int minimumMountainRemovals(int* nums, int numsSize) {
    if (numsSize < 3) return 0;
    
    int *lis = (int*)malloc(numsSize * sizeof(int));
    int *tails = (int*)malloc(numsSize * sizeof(int));
    int len = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        int l = 0, r = len;
        while (l < r) {
            int m = (l + r) >> 1;
            if (tails[m] < x)
                l = m + 1;
            else
                r = m;
        }
        if (l == len) tails[len++] = x;
        else tails[l] = x;
        lis[i] = l + 1;
    }
    
    int *lds = (int*)malloc(numsSize * sizeof(int));
    len = 0; // reuse tails array
    for (int i = numsSize - 1; i >= 0; --i) {
        int x = nums[i];
        int l = 0, r = len;
        while (l < r) {
            int m = (l + r) >> 1;
            if (tails[m] < x)
                l = m + 1;
            else
                r = m;
        }
        if (l == len) tails[len++] = x;
        else tails[l] = x;
        lds[i] = l + 1;
    }
    
    int answer = numsSize; // worst case: remove all but three elements
    for (int i = 0; i < numsSize; ++i) {
        if (lis[i] > 1 && lds[i] > 1) {
            int keep = lis[i] + lds[i] - 1;
            int removals = numsSize - keep;
            if (removals < answer) answer = removals;
        }
    }
    
    free(lis);
    free(lds);
    free(tails);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumMountainRemovals(int[] nums) {
        int n = nums.Length;
        int[] inc = GetLISLengths(nums);
        int[] revNums = new int[n];
        for (int i = 0; i < n; i++) revNums[i] = nums[n - 1 - i];
        int[] incRev = GetLISLengths(revNums);
        int[] dec = new int[n];
        for (int i = 0; i < n; i++) dec[i] = incRev[n - 1 - i];

        int minRemovals = n;
        for (int i = 0; i < n; i++) {
            if (inc[i] > 1 && dec[i] > 1) {
                int keep = inc[i] + dec[i] - 1;
                int removals = n - keep;
                if (removals < minRemovals) minRemovals = removals;
            }
        }
        return minRemovals;
    }

    private int[] GetLISLengths(int[] arr) {
        int n = arr.Length;
        int[] lisLen = new int[n];
        var tails = new List<int>();
        for (int i = 0; i < n; i++) {
            int x = arr[i];
            int pos = LowerBound(tails, x);
            if (pos == tails.Count) {
                tails.Add(x);
            } else {
                tails[pos] = x;
            }
            lisLen[i] = pos + 1;
        }
        return lisLen;
    }

    private int LowerBound(List<int> list, int target) {
        int left = 0, right = list.Count;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (list[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumMountainRemovals = function(nums) {
    const n = nums.length;
    
    // helper to compute LIS lengths ending at each index
    const lisLengths = (arr) => {
        const tails = [];
        const res = new Array(arr.length);
        for (let i = 0; i < arr.length; i++) {
            let left = 0, right = tails.length;
            while (left < right) {
                const mid = (left + right) >> 1;
                if (tails[mid] >= arr[i]) right = mid;
                else left = mid + 1;
            }
            // left is the position to replace / append
            if (left === tails.length) tails.push(arr[i]);
            else tails[left] = arr[i];
            res[i] = left + 1; // length of LIS ending at i
        }
        return res;
    };
    
    const inc = lisLengths(nums);
    const revNums = [...nums].reverse();
    const decRev = lisLengths(revNums);
    const dec = new Array(n);
    for (let i = 0; i < n; i++) {
        dec[i] = decRev[n - 1 - i];
    }
    
    let ans = n;
    for (let i = 0; i < n; i++) {
        if (inc[i] > 1 && dec[i] > 1) {
            const removals = n - (inc[i] + dec[i] - 1);
            if (removals < ans) ans = removals;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimumMountainRemovals(nums: number[]): number {
    const n = nums.length;

    const lisLengths = (arr: number[]): number[] => {
        const dp = new Array(arr.length).fill(0);
        const tails: number[] = [];
        for (let i = 0; i < arr.length; i++) {
            const x = arr[i];
            let l = 0, r = tails.length;
            while (l < r) {
                const m = (l + r) >> 1;
                if (tails[m] < x) l = m + 1;
                else r = m;
            }
            if (l === tails.length) tails.push(x);
            else tails[l] = x;
            dp[i] = l + 1;
        }
        return dp;
    };

    const inc = lisLengths(nums);
    const decReversed = lisLengths([...nums].reverse());
    const dec = decReversed.reverse();

    let answer = n; // upper bound
    for (let i = 0; i < n; i++) {
        if (inc[i] > 1 && dec[i] > 1) {
            const removals = n - (inc[i] + dec[i] - 1);
            if (removals < answer) answer = removals;
        }
    }
    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumMountainRemovals($nums) {
        $n = count($nums);
        if ($n < 3) return 0;
        
        $inc = $this->lisLengths($nums);
        $rev = array_reverse($nums);
        $decRev = $this->lisLengths($rev);
        $dec = array_reverse($decRev);
        
        $best = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($inc[$i] > 1 && $dec[$i] > 1) {
                $len = $inc[$i] + $dec[$i] - 1;
                if ($len > $best) $best = $len;
            }
        }
        return $n - $best;
    }
    
    private function lisLengths($arr) {
        $n = count($arr);
        $tails = [];
        $lens = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $arr[$i];
            $l = 0;
            $r = count($tails);
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($tails[$mid] < $x) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }
            $pos = $l;
            if ($pos === count($tails)) {
                $tails[] = $x;
            } else {
                $tails[$pos] = $x;
            }
            $lens[$i] = $pos + 1;
        }
        return $lens;
    }
}
```

## Swift

```swift
class Solution {
    func minimumMountainRemovals(_ nums: [Int]) -> Int {
        let n = nums.count
        var lis = Array(repeating: 1, count: n)
        var tails = [Int]()
        for i in 0..<n {
            let x = nums[i]
            var l = 0
            var r = tails.count
            while l < r {
                let m = (l + r) / 2
                if tails[m] < x {
                    l = m + 1
                } else {
                    r = m
                }
            }
            if l == tails.count {
                tails.append(x)
            } else {
                tails[l] = x
            }
            lis[i] = l + 1
        }

        // Compute LDS using LIS on reversed array
        var ldsRev = Array(repeating: 1, count: n)
        var tails2 = [Int]()
        var idx = 0
        for val in nums.reversed() {
            let x = val
            var l = 0
            var r = tails2.count
            while l < r {
                let m = (l + r) / 2
                if tails2[m] < x {
                    l = m + 1
                } else {
                    r = m
                }
            }
            if l == tails2.count {
                tails2.append(x)
            } else {
                tails2[l] = x
            }
            ldsRev[idx] = l + 1
            idx += 1
        }

        var lds = Array(repeating: 1, count: n)
        for i in 0..<n {
            lds[i] = ldsRev[n - 1 - i]
        }

        var answer = n
        for i in 0..<n {
            if lis[i] > 1 && lds[i] > 1 {
                let keep = lis[i] + lds[i] - 1
                answer = min(answer, n - keep)
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumMountainRemovals(nums: IntArray): Int {
        val n = nums.size
        val lis = IntArray(n)
        val tailsInc = mutableListOf<Int>()
        for (i in 0 until n) {
            val x = nums[i]
            var idx = tailsInc.binarySearch(x)
            if (idx < 0) idx = -idx - 1
            if (idx == tailsInc.size) {
                tailsInc.add(x)
            } else {
                tailsInc[idx] = x
            }
            lis[i] = idx + 1
        }

        // Compute LDS starting at each index by reversing and using LIS logic
        val rev = nums.reversedArray()
        val ldsRev = IntArray(n)
        val tailsDec = mutableListOf<Int>()
        for (i in 0 until n) {
            val x = rev[i]
            var idx = tailsDec.binarySearch(x)
            if (idx < 0) idx = -idx - 1
            if (idx == tailsDec.size) {
                tailsDec.add(x)
            } else {
                tailsDec[idx] = x
            }
            ldsRev[i] = idx + 1
        }

        val lds = IntArray(n)
        for (i in 0 until n) {
            lds[n - 1 - i] = ldsRev[i]
        }

        var answer = n
        for (i in 0 until n) {
            if (lis[i] > 1 && lds[i] > 1) {
                val keep = lis[i] + lds[i] - 1
                answer = kotlin.math.min(answer, n - keep)
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minimumMountainRemovals(List<int> nums) {
    int n = nums.length;
    List<int> lis = _lisLengths(nums);
    List<int> revNums = List.from(nums.reversed);
    List<int> ldsRev = _lisLengths(revNums);
    List<int> lds = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      lds[i] = ldsRev[n - 1 - i];
    }
    int best = 0;
    for (int i = 0; i < n; i++) {
      if (lis[i] > 1 && lds[i] > 1) {
        int total = lis[i] + lds[i] - 1;
        if (total > best) best = total;
      }
    }
    return n - best;
  }

  List<int> _lisLengths(List<int> arr) {
    int n = arr.length;
    List<int> res = List.filled(n, 0);
    List<int> tails = [];
    for (int i = 0; i < n; i++) {
      int x = arr[i];
      int idx = _lowerBound(tails, x);
      if (idx == tails.length) {
        tails.add(x);
      } else {
        tails[idx] = x;
      }
      res[i] = idx + 1;
    }
    return res;
  }

  int _lowerBound(List<int> list, int target) {
    int left = 0;
    int right = list.length;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (list[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}
```

## Golang

```go
import "sort"

func minimumMountainRemovals(nums []int) int {
	n := len(nums)
	if n < 3 {
		return 0
	}
	leftLis := lisLengths(nums)

	rev := make([]int, n)
	for i := 0; i < n; i++ {
		rev[i] = nums[n-1-i]
	}
	rightLisRev := lisLengths(rev)
	rightLds := make([]int, n)
	for i := 0; i < n; i++ {
		rightLds[i] = rightLisRev[n-1-i]
	}

	maxKeep := 0
	for i := 0; i < n; i++ {
		if leftLis[i] > 1 && rightLds[i] > 1 {
			keep := leftLis[i] + rightLds[i] - 1
			if keep > maxKeep {
				maxKeep = keep
			}
		}
	}
	return n - maxKeep
}

func lisLengths(arr []int) []int {
	n := len(arr)
	res := make([]int, n)
	tails := []int{}
	for i, v := range arr {
		pos := sort.Search(len(tails), func(i int) bool { return tails[i] >= v })
		if pos == len(tails) {
			tails = append(tails, v)
		} else {
			tails[pos] = v
		}
		res[i] = pos + 1
	}
	return res
}
```

## Ruby

```ruby
def minimum_mountain_removals(nums)
  n = nums.size

  # helper to compute LIS length ending at each index
  lis_lengths = lambda do |arr|
    tails = []
    res = Array.new(arr.length, 0)
    arr.each_with_index do |x, i|
      l = 0
      r = tails.length
      while l < r
        m = (l + r) / 2
        if tails[m] < x
          l = m + 1
        else
          r = m
        end
      end
      idx = l
      if idx == tails.length
        tails << x
      else
        tails[idx] = x
      end
      res[i] = idx + 1
    end
    res
  end

  inc = lis_lengths.call(nums)
  dec = lis_lengths.call(nums.reverse).reverse

  min_remove = n # upper bound
  (0...n).each do |i|
    next if inc[i] <= 1 || dec[i] <= 1
    keep = inc[i] + dec[i] - 1
    removals = n - keep
    min_remove = removals if removals < min_remove
  end

  min_remove
end
```

## Scala

```scala
object Solution {
  def minimumMountainRemovals(nums: Array[Int]): Int = {
    val n = nums.length

    // Compute LIS lengths ending at each index
    def lisLengths(arr: Array[Int]): Array[Int] = {
      val res = new Array[Int](arr.length)
      val tails = scala.collection.mutable.ArrayBuffer[Int]()
      var i = 0
      while (i < arr.length) {
        var l = 0
        var r = tails.length
        // lower bound for first element >= arr(i)
        while (l < r) {
          val m = (l + r) >>> 1
          if (tails(m) < arr(i)) l = m + 1 else r = m
        }
        if (l == tails.length) tails += arr(i)
        else tails(l) = arr(i)
        res(i) = l + 1
        i += 1
      }
      res
    }

    val inc = lisLengths(nums)

    // LDS lengths starting at each index: compute LIS on reversed array
    val revNums = nums.reverse
    val revLis = lisLengths(revNums)
    val dec = new Array[Int](n)
    var j = 0
    while (j < n) {
      dec(j) = revLis(n - 1 - j)
      j += 1
    }

    var answer = n
    var idx = 0
    while (idx < n) {
      if (inc(idx) > 1 && dec(idx) > 1) {
        val keep = inc(idx) + dec(idx) - 1
        answer = math.min(answer, n - keep)
      }
      idx += 1
    }
    answer
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn minimum_mountain_removals(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        // Longest increasing subsequence lengths ending at each index
        let left = Self::lis_lengths(&nums);
        // Longest decreasing subsequence lengths starting at each index
        let rev_nums: Vec<i32> = nums.iter().rev().cloned().collect();
        let rev_lis = Self::lis_lengths(&rev_nums);
        let mut right = vec![0usize; n];
        for i in 0..n {
            right[i] = rev_lis[n - 1 - i];
        }

        let mut ans = n as i32;
        for i in 0..n {
            if left[i] > 1 && right[i] > 1 {
                let keep = left[i] + right[i] - 1; // length of mountain subsequence
                let removals = n - keep;
                if removals < ans as usize {
                    ans = removals as i32;
                }
            }
        }
        ans
    }

    fn lis_lengths(arr: &[i32]) -> Vec<usize> {
        let mut tails: Vec<i32> = Vec::new();
        let mut res = vec![0usize; arr.len()];
        for (i, &x) in arr.iter().enumerate() {
            // lower_bound for first element >= x
            let pos = match tails.binary_search(&x) {
                Ok(p) => p,
                Err(p) => p,
            };
            if pos == tails.len() {
                tails.push(x);
            } else {
                tails[pos] = x;
            }
            res[i] = pos + 1;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (minimum-mountain-removals nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums)))
    ;; compute LIS lengths ending at each position
    (define (lis-lengths vec)
      (let ((len 0)
            (tails (make-vector n #f))
            (res (make-vector n 0)))
        (for ([i (in-range n)])
          (let* ((x (vector-ref vec i))
                 (lo 0) (hi len))
            ;; binary search for first tail >= x
            (let loop ()
              (when (< lo hi)
                (define mid (quotient (+ lo hi) 2))
                (if (< (vector-ref tails mid) x)
                    (set! lo (+ mid 1))
                    (set! hi mid))
                (loop)))
            (define pos lo)               ; position to place x
            (vector-set! tails pos x)
            (when (= pos len) (set! len (+ len 1)))
            (vector-set! res i (+ pos 1))))
        res))
    (define lis (lis-lengths arr))
    ;; compute LDS lengths starting at each position via reversed LIS
    (define rev-vec (make-vector n))
    (for ([i (in-range n)])
      (vector-set! rev-vec i (vector-ref arr (- n 1 i))))
    (define rev-lis (lis-lengths rev-vec))
    (define lds (make-vector n 0))
    (for ([i (in-range n)])
      (vector-set! lds i (vector-ref rev-lis (- n 1 i))))
    ;; find minimal removals
    (let ((best n))                     ; upper bound
      (for ([i (in-range n)])
        (define li (vector-ref lis i))
        (define ld (vector-ref lds i))
        (when (and (> li 1) (> ld 1))
          (define rem (- n (+ li ld -1))) ; n - (li + ld - 1)
          (when (< rem best) (set! best rem))))
      best)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_mountain_removals/1]).

-spec minimum_mountain_removals(Nums :: [integer()]) -> integer().
minimum_mountain_removals(Nums) ->
    N = length(Nums),
    Lis = compute_lis(Nums),
    Lds = compute_lds(Nums),
    min_removals(N, Lis, Lds).

%% Compute LIS lengths ending at each position
compute_lis(List) -> compute_lis(List, [], []).

compute_lis([], _Prev, AccRev) ->
    lists:reverse(AccRev);
compute_lis([X|Rest], Prev, AccRev) ->
    Max = max_len_less_than(X, Prev, 0),
    Len = Max + 1,
    compute_lis(Rest, [{X, Len}|Prev], [Len|AccRev]).

max_len_less_than(_X, [], Acc) -> Acc;
max_len_less_than(X, [{Val, L}|Tail], Acc) ->
    NewAcc = if Val < X, L > Acc -> L; true -> Acc end,
    max_len_less_than(X, Tail, NewAcc).

%% LDS lengths starting at each position (via reversed LIS)
compute_lds(Nums) ->
    Rev = lists:reverse(Nums),
    LisRev = compute_lis(Rev),
    lists:reverse(LisRev).

%% Find minimal removals over all valid peaks
min_removals(N, [], []) -> N;
min_removals(N, [L|Ls], [R|Rs]) ->
    MinRest = min_removals(N, Ls, Rs),
    case (L > 1) andalso (R > 1) of
        true ->
            Rem = N - (L + R - 1),
            if Rem < MinRest -> Rem; true -> MinRest end;
        false -> MinRest
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_mountain_removals(nums :: [integer]) :: integer
  def minimum_mountain_removals(nums) do
    n = length(nums)

    lis = compute_lis(nums)
    lds = compute_lds(nums)

    Enum.reduce(0..(n - 1), n, fn i, best ->
      li = Enum.at(lis, i)
      ld = Enum.at(lds, i)

      if li > 1 and ld > 1 do
        removals = n - (li + ld - 1)
        Kernel.min(best, removals)
      else
        best
      end
    end)
  end

  defp compute_lis(nums) do
    Enum.reduce(0..(length(nums) - 1), [], fn i, acc ->
      val_i = Enum.at(nums, i)

      max_len =
        Enum.with_index(acc)
        |> Enum.reduce(1, fn {len_j, j}, cur ->
          if val_i > Enum.at(nums, j) do
            Kernel.max(cur, len_j + 1)
          else
            cur
          end
        end)

      acc ++ [max_len]
    end)
  end

  defp compute_lds(nums) do
    rev = Enum.reverse(nums)
    lds_rev = compute_lis(rev)
    Enum.reverse(lds_rev)
  end
end
```
