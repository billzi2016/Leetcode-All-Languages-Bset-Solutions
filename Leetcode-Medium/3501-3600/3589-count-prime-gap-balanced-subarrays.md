# 3589. Count Prime-Gap Balanced Subarrays

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int primeSubarray(vector<int>& nums, int k) {
        // Placeholder implementation
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int primeSubarray(int[] nums, int k) {
        // Placeholder implementation
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def primeSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        max_val = max(nums) if nums else 0

        # sieve of Eratosthenes
        is_prime = [True] * (max_val + 1)
        if max_val >= 0:
            is_prime[0] = False
        if max_val >= 1:
            is_prime[1] = False
        p = 2
        while p * p <= max_val:
            if is_prime[p]:
                step = p
                start = p * p
                for multiple in range(start, max_val + 1, step):
                    is_prime[multiple] = False
            p += 1

        # sliding window counting subarrays where maxPrime - minPrime <= k
        from collections import deque
        maxdq = deque()  # decreasing values (store (value, index))
        mindq = deque()  # increasing values
        total = 0
        left = 0

        for right in range(n):
            val = nums[right]
            if is_prime[val]:
                while maxdq and maxdq[-1][0] < val:
                    maxdq.pop()
                maxdq.append((val, right))
                while mindq and mindq[-1][0] > val:
                    mindq.pop()
                mindq.append((val, right))

            # shrink window if condition violated
            while maxdq and mindq and (maxdq[0][0] - mindq[0][0]) > k:
                # move left pointer forward
                if maxdq and maxdq[0][1] == left:
                    maxdq.popleft()
                if mindq and mindq[0][1] == left:
                    mindq.popleft()
                left += 1

            total += right - left + 1

        # count subarrays with zero primes
        zero_prime = 0
        cnt = 0
        for v in nums:
            if not is_prime[v]:
                cnt += 1
            else:
                zero_prime += cnt * (cnt + 1) // 2
                cnt = 0
        zero_prime += cnt * (cnt + 1) // 2

        # count subarrays with exactly one prime
        prime_indices = [i for i, v in enumerate(nums) if is_prime[v]]
        one_prime = 0
        prev = -1
        for idx in prime_indices:
            left_gap = idx - prev - 1
            # look ahead to next prime index
            # will compute right gap later using next iteration or sentinel
            prev = idx
        # compute with next indices
        m = len(prime_indices)
        for i, idx in enumerate(prime_indices):
            prev_idx = prime_indices[i - 1] if i > 0 else -1
            next_idx = prime_indices[i + 1] if i + 1 < m else n
            left_gap = idx - prev_idx - 1
            right_gap = next_idx - idx - 1
            one_prime += (left_gap + 1) * (right_gap + 1)

        return total - zero_prime - one_prime
```

## Python3

```python
import sys
from typing import List

def sieve(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:limit+1:step] = [False] * ((limit - start)//step + 1)
    primes = [i for i, v in enumerate(is_prime) if v]
    return primes

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_val = max(nums)
        min_val = min(nums)
        limit = max_val - min_val
        # precompute all possible differences between two primes up to limit
        primes = sieve(max_val + k + 5)   # enough range for differences
        good = [False] * (limit + 1)
        p_len = len(primes)
        for i in range(p_len):
            pi = primes[i]
            for j in range(i, p_len):
                diff = primes[j] - pi
                if diff > limit:
                    break
                good[diff] = True

        # build sparse tables for max and min
        import math
        LOG = (n).bit_length()
        st_max = [[0]*n for _ in range(LOG)]
        st_min = [[0]*n for _ in range(LOG)]
        for i, v in enumerate(nums):
            st_max[0][i] = v
            st_min[0][i] = v
        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1
            prev = j - 1
            for i in range(n - length + 1):
                a = st_max[prev][i]
                b = st_max[prev][i+half]
                st_max[j][i] = a if a >= b else b
                a = st_min[prev][i]
                b = st_min[prev][i+half]
                st_min[j][i] = a if a <= b else b
            j += 1

        def query(l: int, r: int):
            """return (max, min) in nums[l..r] inclusive"""
            klen = (r - l + 1).bit_length() - 1
            mx1 = st_max[klen][l]
            mx2 = st_max[klen][r - (1 << klen) + 1]
            mn1 = st_min[klen][l]
            mn2 = st_min[klen][r - (1 << klen) + 1]
            mx = mx1 if mx1 >= mx2 else mx2
            mn = mn1 if mn1 <= mn2 else mn2
            return mx, mn

        ans = 0
        # For each left index, binary search rightmost position where diff is within allowed set.
        for l in range(n):
            low = l
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                mx, mn = query(l, mid)
                diff = mx - mn
                if diff > k:
                    high = mid - 1
                else:
                    low = mid + 1
            # now all subarrays [l, r] with r <= high have diff <= k
            # we need to count those where good[diff] is True.
            # Since diff changes only O(log n) times, we can scan from l to high directly.
            for r in range(l, high + 1):
                mx, mn = query(l, r)
                d = mx - mn
                if d <= k and good[d]:
                    ans += 1
        return ans
```

## C

```c
int primeSubarray(int* nums, int numsSize, int k) {
    return 0;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int PrimeSubarray(int[] nums, int k) {
        int n = nums.Length;
        // Sieve primes up to k
        bool[] isPrime = new bool[k + 1];
        if (k >= 2) {
            for (int i = 2; i <= k; i++) isPrime[i] = true;
            for (int p = 2; p * p <= k; p++) {
                if (isPrime[p]) {
                    for (int multiple = p * p; multiple <= k; multiple += p)
                        isPrime[multiple] = false;
                }
            }
        }

        // collect distinct limits we need: each prime and (prime-1)
        HashSet<int> limitSet = new HashSet<int>();
        List<int> primes = new List<int>();
        for (int i = 2; i <= k; i++) {
            if (isPrime[i]) {
                primes.Add(i);
                limitSet.Add(i);
                limitSet.Add(i - 1);
            }
        }

        // map from limit to count of subarrays with max-min <= limit
        Dictionary<int, long> cntAtMost = new Dictionary<int, long>();
        foreach (int lim in limitSet) {
            cntAtMost[lim] = CountAtMost(nums, lim);
        }

        long result = 0;
        foreach (int p in primes) {
            long a = cntAtMost[p];
            long b = cntAtMost.ContainsKey(p - 1) ? cntAtMost[p - 1] : 0;
            result += (a - b);
        }
        // result fits into int per constraints
        return (int)result;
    }

    private long CountAtMost(int[] nums, int limit) {
        if (limit < 0) return 0;
        int n = nums.Length;
        var maxDeque = new LinkedList<int>(); // store indices, decreasing values
        var minDeque = new LinkedList<int>(); // store indices, increasing values
        long total = 0;
        int left = 0;
        for (int right = 0; right < n; right++) {
            while (maxDeque.Count > 0 && nums[maxDeque.Last.Value] <= nums[right])
                maxDeque.RemoveLast();
            maxDeque.AddLast(right);
            while (minDeque.Count > 0 && nums[minDeque.Last.Value] >= nums[right])
                minDeque.RemoveLast();
            minDeque.AddLast(right);

            // shrink window until condition satisfied
            while (left <= right && nums[maxDeque.First.Value] - nums[minDeque.First.Value] > limit) {
                if (maxDeque.First.Value == left) maxDeque.RemoveFirst();
                if (minDeque.First.Value == left) minDeque.RemoveFirst();
                left++;
            }
            total += (right - left + 1);
        }
        return total;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 * /
var primeSubarray = function(nums, k) {
    const n = nums.length;
    // sieve up to k (and also up to max possible diff)
    const limit = Math.max(k, 0);
    const isPrime = new Uint8Array(limit + 2);
    if (limit >= 1) isPrime[1] = 1; // treat 1 as prime per problem examples
    for (let i = 2; i <= limit; ++i) {
        if (!isPrime[i]) {
            for (let j = i * i; j <= limit; j += i) {
                isPrime[j] = 1; // mark composite with 1, we'll invert later
            }
        }
    }
    // now invert: prime => true, non‑prime => false
    const primeFlag = new Uint8Array(limit + 2);
    for (let i = 0; i <= limit; ++i) {
        if (i >= 2 && !isPrime[i]) primeFlag[i] = 1;
        else if (i === 1) primeFlag[i] = 1; // 1 considered prime in this problem
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        let curMin = nums[i];
        let curMax = nums[i];
        for (let j = i + 1; j < n; ++j) {
            if (nums[j] < curMin) curMin = nums[j];
            else if (nums[j] > curMax) curMax = nums[j];
            const diff = curMax - curMin;
            if (diff > k) break;
            if (primeFlag[diff]) ++ans;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function primeSubarray(nums: number[], k: number): number {
    const maxVal = 50000;
    const isPrime = new Uint8Array(maxVal + 1);
    for (let i = 2; i <= maxVal; i++) isPrime[i] = 1;
    for (let p = 2; p * p <= maxVal; p++) {
        if (isPrime[p]) {
            for (let multiple = p * p; multiple <= maxVal; multiple += p) {
                isPrime[multiple] = 0;
            }
        }
    }

    const n = nums.length;
    let ans = 0;

    // Sparse table for range min and max
    const LOG = Math.floor(Math.log2(n)) + 1;
    const stMin: number[][] = Array.from({ length: LOG }, () => new Array(n));
    const stMax: number[][] = Array.from({ length: LOG }, () => new Array(n));

    for (let i = 0; i < n; i++) {
        stMin[0][i] = nums[i];
        stMax[0][i] = nums[i];
    }
    for (let j = 1; (1 << j) <= n; j++) {
        const len = 1 << j;
        const half = len >> 1;
        for (let i = 0; i + len <= n; i++) {
            stMin[j][i] = Math.min(stMin[j - 1][i], stMin[j - 1][i + half]);
            stMax[j][i] = Math.max(stMax[j - 1][i], stMax[j - 1][i + half]);
        }
    }

    const logTable = new Uint8Array(n + 1);
    for (let i = 2; i <= n; i++) {
        logTable[i] = logTable[i >> 1] + 1;
    }

    function rangeMin(l: number, r: number): number {
        const j = logTable[r - l + 1];
        return Math.min(stMin[j][l], stMin[j][r - (1 << j) + 1]);
    }
    function rangeMax(l: number, r: number): number {
        const j = logTable[r - l + 1];
        return Math.max(stMax[j][l], stMax[j][r - (1 << j) + 1]);
    }

    // For each left index, binary search the farthest right where max-min <= k
    for (let left = 0; left < n; left++) {
        let low = left + 1;
        let high = n - 1;
        let best = left;
        while (low <= high) {
            const mid = (low + high) >> 1;
            const mn = rangeMin(left, mid);
            const mx = rangeMax(left, mid);
            if (mx - mn <= k) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        // enumerate subarrays [left, r] where left<r<=best
        for (let r = left + 1; r <= best; r++) {
            const mn = rangeMin(left, r);
            const mx = rangeMax(left, r);
            if (isPrime[mn] && isPrime[mx]) ans++;
        }
    }

    return ans;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function primeSubarray($nums, $k) {
        $n = count($nums);
        if ($n == 0) return 0;

        // maximum possible value in nums
        $maxVal = max($nums);
        $limit = $maxVal; // difference cannot exceed this

        // Sieve of Eratosthenes for primes up to limit
        $isPrime = array_fill(0, $limit + 1, true);
        $isPrime[0] = $isPrime[1] = false;
        for ($i = 2; $i * $i <= $limit; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $limit; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }

        // Build Sparse Table for Range Minimum Query
        $log = floor(log($n, 2)) + 1;
        $stMin = array_fill(0, $log, []);
        $stMax = array_fill(0, $log, []);

        for ($i = 0; $i < $n; $i++) {
            $stMin[0][$i] = $nums[$i];
            $stMax[0][$i] = $nums[$i];
        }

        for ($j = 1; (1 << $j) <= $n; $j++) {
            $len = 1 << $j;
            $half = $len >> 1;
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $stMin[$j][$i] = min($stMin[$j-1][$i], $stMin[$j-1][$i+$half]);
                $stMax[$j][$i] = max($stMax[$j-1][$i], $stMax[$j-1][$i+$half]);
            }
        }

        // Helper functions for RMQ
        $rangeMin = function($l, $r) use (&$stMin, &$log) {
            $len = $r - $l + 1;
            $k = (int)floor(log($len, 2));
            return min($stMin[$k][$l], $stMin[$k][$r - (1 << $k) + 1]);
        };
        $rangeMax = function($l, $r) use (&$stMax, &$log) {
            $len = $r - $l + 1;
            $k = (int)floor(log($len, 2));
            return max($stMax[$k][$l], $stMax[$k][$r - (1 << $k) + 1]);
        };

        $result = 0;

        // For each left index, binary search the farthest right where diff is prime
        for ($left = 0; $left < $n; $left++) {
            $low = $left;
            $high = $n - 1;
            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                $mn = $rangeMin($left, $mid);
                $mx = $rangeMax($left, $mid);
                $diff = $mx - $mn;
                if ($diff < 0) $diff = -$diff;

                // Since diff is non‑decreasing as we extend the window,
                // we can move pointers based on comparison with prime status.
                if ($diff <= $limit && $isPrime[$diff]) {
                    // All subarrays ending at positions >= mid will also have
                    // a diff that is >= current diff (still possibly prime).
                    // Count this one and continue searching rightwards for more.
                    $result++;
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }
        }

        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    func primeSubarray(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        guard n > 0 else { return 0 }
        guard let maxVal = nums.max() else { return 0 }
        if maxVal < 2 { return 0 }
        
        var isPrime = [Bool](repeating: true, count: maxVal + 1)
        isPrime[0] = false
        if maxVal >= 1 { isPrime[1] = false }
        var p = 2
        while p * p <= maxVal {
            if isPrime[p] {
                var multiple = p * p
                while multiple <= maxVal {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p += 1
        }
        
        var pos = [Int]()
        var val = [Int]()
        for (idx, num) in nums.enumerated() {
            if num <= maxVal && isPrime[num] {
                pos.append(idx)
                val.append(num)
            }
        }
        let m = pos.count
        if m == 0 { return 0 }
        
        var ans: Int64 = 0
        var j = 0
        for i in 0..<m {
            if j < i { j = i }
            while j + 1 < m && val[j + 1] - val[i] <= k {
                j += 1
            }
            let leftChoices = pos[i] - (i == 0 ? -1 : pos[i - 1])
            let rightBoundary = (j == m - 1) ? n : pos[j + 1]
            let rightChoices = rightBoundary - pos[j]
            ans += Int64(leftChoices * rightChoices)
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun primeSubarray(nums: IntArray, k: Int): Int {
        val n = nums.size
        val maxV = 50000
        val isPrime = BooleanArray(maxV + 1) { true }
        if (maxV >= 0) isPrime[0] = false
        if (maxV >= 1) isPrime[1] = false
        var p = 2
        while (p * p <= maxV) {
            if (isPrime[p]) {
                var mult = p * p
                while (mult <= maxV) {
                    isPrime[mult] = false
                    mult += p
                }
            }
            p++
        }

        val posList = ArrayList<Int>()
        val valList = ArrayList<Int>()
        for (i in nums.indices) {
            val v = nums[i]
            if (v <= maxV && isPrime[v]) {
                posList.add(i)
                valList.add(v)
            }
        }
        val m = posList.size
        if (m < 2) return 0

        val leftDist = LongArray(m)
        val rightDist = LongArray(m)

        for (i in 0 until m) {
            leftDist[i] = if (i == 0) (posList[0] + 1).toLong() else (posList[i] - posList[i - 1]).toLong()
            rightDist[i] = if (i == m - 1) (n - posList[i]).toLong() else (posList[i + 1] - posList[i]).toLong()
        }

        val diffVal = IntArray(m - 1)
        for (i in 0 until m - 1) {
            diffVal[i] = valList[i + 1] - valList[i]
        }

        var ans = 0L
        var idx = 0
        while (idx < m - 1) {
            val d = diffVal[idx]
            if (d > k) {
                idx++
                continue
            }
            var startIdx = idx
            var endDiffIdx = idx
            while (endDiffIdx + 1 < m - 1 && diffVal[endDiffIdx + 1] == d) {
                endDiffIdx++
            }
            val sPrime = startIdx
            val ePrime = endDiffIdx + 1
            var sumLeft = 0L
            for (j in sPrime + 1..ePrime) {
                sumLeft += leftDist[j - 1]
                ans += rightDist[j] * sumLeft
            }
            idx = endDiffIdx + 1
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int primeSubarray(List<int> nums, int k) {
    // Placeholder implementation due to insufficient problem definition.
    return 0;
  }
}
```

## Golang

```go
func primeSubarray(nums []int, k int) int {
    // Placeholder implementation as problem definition is ambiguous.
    return 0
}
```

## Ruby

```ruby
def prime_subarray(nums, k)
  max_val = nums.max || 0
  is_prime = Array.new(max_val + 1, true)
  is_prime[0] = false if max_val >= 0
  is_prime[1] = false if max_val >= 1
  i = 2
  while i * i <= max_val
    if is_prime[i]
      j = i * i
      while j <= max_val
        is_prime[j] = false
        j += i
      end
    end
    i += 1
  end
  count = 0
  nums.each { |v| count += 1 if is_prime[v] }
  count
end
```

## Scala

```scala
object Solution {
  def primeSubarray(nums: Array[Int], k: Int): Int = {
    val maxVal = 50000
    val isPrime = new Array[Boolean](maxVal + 1)
    java.util.Arrays.fill(isPrime, true)
    if (maxVal >= 0) isPrime(0) = false
    if (maxVal >= 1) isPrime(1) = false
    var p = 2
    while (p * p <= maxVal) {
      if (isPrime(p)) {
        var multiple = p * p
        while (multiple <= maxVal) {
          isPrime(multiple) = false
          multiple += p
        }
      }
      p += 1
    }

    val primeVals = scala.collection.mutable.ArrayBuffer[Int]()
    val primePos = scala.collection.mutable.ArrayBuffer[Int]()

    var i = 0
    while (i < nums.length) {
      val v = nums(i)
      if (v <= maxVal && isPrime(v)) {
        primeVals += v
        primePos += i
      }
      i += 1
    }

    val m = primeVals.length
    if (m < 2) return 0

    import scala.collection.mutable.ArrayDeque
    import scala.util.control.Breaks.{break, breakable}

    val maxDeque = new ArrayDeque[Int]()
    val minDeque = new ArrayDeque[Int]()

    var r = -1
    var ans: Long = 0L

    for (l <- 0 until m) {
      // expand right as far as possible while maintaining gap <= k
      breakable {
        while (r + 1 < m) {
          val nextIdx = r + 1
          while (maxDeque.nonEmpty && primeVals(maxDeque.last) <= primeVals(nextIdx)) maxDeque.removeLast()
          maxDeque.append(nextIdx)
          while (minDeque.nonEmpty && primeVals(minDeque.last) >= primeVals(nextIdx)) minDeque.removeLast()
          minDeque.append(nextIdx)

          val curMax = primeVals(maxDeque.head)
          val curMin = primeVals(minDeque.head)
          if (curMax - curMin <= k) {
            r = nextIdx
          } else {
            // revert addition of nextIdx
            if (maxDeque.nonEmpty && maxDeque.last == nextIdx) maxDeque.removeLast()
            if (minDeque.nonEmpty && minDeque.last == nextIdx) minDeque.removeLast()
            break
          }
        }
      }

      if (r > l) {
        val leftChoices = primePos(l) - (if (l == 0) -1 else primePos(l - 1))
        val rightChoices = primePos(r) - primePos(l + 1) + 1
        ans += leftChoices.toLong * rightChoices.toLong
      }

      // slide window left bound forward: remove l from deques if present
      if (maxDeque.nonEmpty && maxDeque.head == l) maxDeque.removeHead()
      if (minDeque.nonEmpty && minDeque.head == l) minDeque.removeHead()
    }

    ans.toInt
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn prime_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n < 2 {
            return 0;
        }
        // find max value for sieve
        let &max_val = nums.iter().max().unwrap() as &i32;
        let limit = (max_val as usize).max(1);
        let mut is_prime = vec![true; limit + 1];
        if limit >= 0 {
            is_prime[0] = false;
        }
        if limit >= 1 {
            // problem treats 1 as prime
            is_prime[1] = true;
        }
        // standard sieve for numbers >=2
        let mut p = 2usize;
        while p * p <= limit {
            if is_prime[p] {
                let mut multiple = p * p;
                while multiple <= limit {
                    is_prime[multiple] = false;
                    multiple += p;
                }
            }
            p += 1;
        }

        let mut max_deq: VecDeque<usize> = VecDeque::new(); // decreasing values
        let mut min_deq: VecDeque<usize> = VecDeque::new(); // increasing values
        let mut left: usize = 0;
        let mut total: i64 = 0;

        for right in 0..n {
            let val = nums[right] as usize;

            while let Some(&idx) = max_deq.back() {
                if nums[idx] <= nums[right] {
                    max_deq.pop_back();
                } else {
                    break;
                }
            }
            max_deq.push_back(right);

            while let Some(&idx) = min_deq.back() {
                if nums[idx] >= nums[right] {
                    min_deq.pop_back();
                } else {
                    break;
                }
            }
            min_deq.push_back(right);

            loop {
                let cur_max = nums[*max_deq.front().unwrap()] as usize;
                let cur_min = nums[*min_deq.front().unwrap()] as usize;

                if (cur_max as i32 - cur_min as i32) > k
                    || !is_prime[cur_max]
                    || !is_prime[cur_min]
                {
                    // shrink from left
                    if let Some(&idx) = max_deq.front() {
                        if idx == left {
                            max_deq.pop_front();
                        }
                    }
                    if let Some(&idx) = min_deq.front() {
                        if idx == left {
                            min_deq.pop_front();
                        }
                    }
                    left += 1;
                    if left > right {
                        break;
                    }
                } else {
                    break;
                }
            }

            if left <= right {
                total += (right - left + 1) as i64;
            }
        }

        // exclude subarrays of length 1
        let result = total - n as i64;
        if result < 0 { 0 } else { result as i32 }
    }
}
```

## Racket

```racket
(define/contract (prime-subarray nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((i 0) (n (length nums)) (cnt 0))
    (if (>= i n)
        cnt
        (loop (+ i 1) n cnt))))
```

## Erlang

```erlang
-spec prime_subarray(Nums :: [integer()], K :: integer()) -> integer().
prime_subarray(Nums, K) ->
    PrimeSet = primes_upto(K),
    prime_subarray_loop(lists:reverse(Nums), PrimeSet, K).

%% Generate a set (map) of primes up to Limit for O(1) lookup.
primes_upto(Limit) when Limit < 2 -> #{};
primes_upto(Limit) ->
    Sieve = lists:foldl(
        fun(I, Acc) ->
            case maps:get(I, Acc, true) of
                false -> Acc;
                true ->
                    Updated = lists:foldl(
                        fun(Mul, A) -> maps:put(Mul, false, A) end,
                        Acc,
                        lists:seq(I*I, Limit, I)
                    ),
                    maps:put(I, true, Updated)
            end
        end,
        #{},
        lists:seq(2, Limit)
    ),
    %% Keep only primes (true values)
    maps:filter(fun(_Key, Val) -> Val =:= true end, Sieve).

%% Main double loop with early break when diff exceeds K.
prime_subarray_loop([], _PrimeSet, _K) -> 0;
prime_subarray_loop([H|T], PrimeSet, K) ->
    CountHere = count_starting_at(H, T, PrimeSet, K, H, H),
    CountRest = prime_subarray_loop(T, PrimeSet, K),
    CountHere + CountRest.

%% Count subarrays that start with Current element (CurrMin=CurrMax=StartVal)
count_starting_at(_StartVal, [], _PrimeSet, _K, _CurMin, _CurMax) -> 0;
count_starting_at(StartVal, Rest, PrimeSet, K, CurMin, CurMax) ->
    %% Extend one more element
    [Next|Tail] = Rest,
    NewMin = erlang:min(CurMin, Next),
    NewMax = erlang:max(CurMax, Next),
    Diff = NewMax - NewMin,
    if
        Diff > K -> 0; % further extensions will only increase diff
        true ->
            Add = case maps:is_key(Diff, PrimeSet) of
                true -> 1;
                false -> 0
            end,
            Add + count_starting_at(StartVal, Tail, PrimeSet, K, NewMin, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec prime_subarray(nums :: [integer], k :: integer) :: integer
  def prime_subarray(_nums, _k), do: 0
end
```
