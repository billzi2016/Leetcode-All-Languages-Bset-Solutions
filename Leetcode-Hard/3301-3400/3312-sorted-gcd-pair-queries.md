# 3312. Sorted GCD Pair Queries

## Cpp

```cpp
class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int n = nums.size();
        int maxVal = 0;
        for (int x : nums) if (x > maxVal) maxVal = x;
        vector<int> freq(maxVal + 1, 0);
        for (int x : nums) ++freq[x];
        
        vector<long long> cnt(maxVal + 1, 0);
        for (int d = 1; d <= maxVal; ++d) {
            for (int m = d; m <= maxVal; m += d) {
                cnt[d] += freq[m];
            }
        }
        
        vector<long long> exact(maxVal + 1, 0);
        for (int d = maxVal; d >= 1; --d) {
            long long total = cnt[d] * (cnt[d] - 1) / 2;
            for (int m = d * 2; m <= maxVal; m += d) {
                total -= exact[m];
            }
            exact[d] = total;
        }
        
        vector<long long> pref(maxVal + 1, 0);
        for (int g = 1; g <= maxVal; ++g) {
            pref[g] = pref[g - 1] + exact[g];
        }
        
        vector<int> ans;
        ans.reserve(queries.size());
        for (long long q : queries) {
            int lo = 1, hi = maxVal, res = maxVal;
            while (lo <= hi) {
                int mid = (lo + hi) >> 1;
                if (pref[mid] > q) {
                    res = mid;
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            }
            ans.push_back(res);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] gcdValues(int[] nums, long[] queries) {
        int maxV = 0;
        for (int v : nums) if (v > maxV) maxV = v;

        int[] freq = new int[maxV + 1];
        for (int v : nums) freq[v]++;

        long[] cnt = new long[maxV + 1];
        for (int d = 1; d <= maxV; ++d) {
            for (int m = d; m <= maxV; m += d) {
                cnt[d] += freq[m];
            }
        }

        long[] exact = new long[maxV + 1];
        for (int d = maxV; d >= 1; --d) {
            long total = cnt[d] * (cnt[d] - 1) / 2;
            for (int m = d << 1; m <= maxV; m += d) {
                total -= exact[m];
            }
            exact[d] = total;
        }

        long[] pref = new long[maxV + 1];
        for (int d = 1; d <= maxV; ++d) {
            pref[d] = pref[d - 1] + exact[d];
        }

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; ++i) {
            long k = queries[i];
            int lo = 1, hi = maxV;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (pref[mid] > k) {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            ans[i] = lo;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        import bisect

        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d]: number of elements divisible by d
        cnt = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            s = 0
            for m in range(d, max_val + 1, d):
                s += freq[m]
            cnt[d] = s

        # f[d]: number of pairs with GCD exactly d
        f = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            total = cnt[d] * (cnt[d] - 1) // 2
            mul = d * 2
            while mul <= max_val:
                total -= f[mul]
                mul += d
            f[d] = total

        # prefix sums of counts for binary search
        pref = [0]
        cur = 0
        for d in range(1, max_val + 1):
            cur += f[d]
            pref.append(cur)

        return [bisect.bisect_left(pref, k + 1) for k in queries]
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        cnt = [0] * (max_val + 1)
        for x in nums:
            cnt[x] += 1

        # f[d]: number of elements divisible by d
        f = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            s = 0
            for m in range(d, max_val + 1, d):
                s += cnt[m]
            f[d] = s

        # total[d]: number of pairs with gcd exactly d
        total = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            c = f[d]
            if c >= 2:
                cur = c * (c - 1) // 2
            else:
                cur = 0
            m = d * 2
            while m <= max_val:
                cur -= total[m]
                m += d
            total[d] = cur

        # prefix sums of counts for binary search
        pref = [0] * (max_val + 1)
        running = 0
        for d in range(1, max_val + 1):
            running += total[d]
            pref[d] = running

        ans = []
        for q in queries:
            # need smallest d with pref[d] > q  (0-indexed)
            g = bisect.bisect_left(pref, q + 1)
            ans.append(g)
        return ans
```

## C

```c
#include <stdlib.h>

int* gcdValues(int* nums, int numsSize, long long* queries, int queriesSize, int* returnSize) {
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];

    int *cnt = (int*)calloc(maxVal + 1, sizeof(int));
    for (int i = 0; i < numsSize; ++i)
        cnt[nums[i]]++;

    long long *mul = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int d = 1; d <= maxVal; ++d) {
        for (int m = d; m <= maxVal; m += d)
            mul[d] += cnt[m];
    }

    long long *exact = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int d = maxVal; d >= 1; --d) {
        long long total = mul[d] * (mul[d] - 1) / 2;
        for (int m = d * 2; m <= maxVal; m += d)
            total -= exact[m];
        exact[d] = total;
    }

    long long *pref = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int d = 1; d <= maxVal; ++d) {
        pref[d] = pref[d - 1] + exact[d];
    }

    int *ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        long long k = queries[i]; // zero‑based index
        int lo = 1, hi = maxVal;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (pref[mid] > k)
                hi = mid;
            else
                lo = mid + 1;
        }
        ans[i] = lo;
    }

    free(cnt);
    free(mul);
    free(exact);
    free(pref);

    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[] GcdValues(int[] nums, long[] queries) {
        int max = 0;
        foreach (int v in nums) if (v > max) max = v;

        int[] freq = new int[max + 1];
        foreach (int v in nums) freq[v]++;

        long[] cntDiv = new long[max + 1];
        for (int d = 1; d <= max; d++) {
            long sum = 0;
            for (int m = d; m <= max; m += d) {
                sum += freq[m];
            }
            cntDiv[d] = sum;
        }

        long[] totalPairsDiv = new long[max + 1];
        for (int d = 1; d <= max; d++) {
            long c = cntDiv[d];
            totalPairsDiv[d] = c * (c - 1) / 2;
        }

        long[] exact = new long[max + 1];
        for (int d = max; d >= 1; d--) {
            long val = totalPairsDiv[d];
            for (int m = d * 2; m <= max; m += d) {
                val -= exact[m];
            }
            exact[d] = val;
        }

        long[] prefix = new long[max + 1];
        for (int g = 1; g <= max; g++) {
            prefix[g] = prefix[g - 1] + exact[g];
        }

        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            long k = queries[i];
            int lo = 1, hi = max;
            while (lo < hi) {
                int mid = (lo + hi) >> 1;
                if (prefix[mid] > k) hi = mid;
                else lo = mid + 1;
            }
            ans[i] = lo;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var gcdValues = function(nums, queries) {
    const n = nums.length;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    const cnt = new Array(maxVal + 1).fill(0);
    for (const v of nums) cnt[v]++;

    // freqDiv[d] = number of elements divisible by d
    const freqDiv = new Array(maxVal + 1).fill(0);
    for (let d = 1; d <= maxVal; ++d) {
        let sum = 0;
        for (let m = d; m <= maxVal; m += d) {
            sum += cnt[m];
        }
        freqDiv[d] = sum;
    }

    // pairsDiv[d] = total pairs where both numbers are divisible by d
    const pairsDiv = new Array(maxVal + 1).fill(0);
    for (let d = 1; d <= maxVal; ++d) {
        const f = freqDiv[d];
        pairsDiv[d] = f * (f - 1) / 2;
    }

    // exact[d] = number of pairs with GCD exactly d
    const exact = new Array(maxVal + 1).fill(0);
    for (let d = maxVal; d >= 1; --d) {
        let total = pairsDiv[d];
        for (let m = d * 2; m <= maxVal; m += d) {
            total -= exact[m];
        }
        exact[d] = total;
    }

    // pref[d] = number of pairs with GCD <= d
    const pref = new Array(maxVal + 1).fill(0);
    for (let d = 1; d <= maxVal; ++d) {
        pref[d] = pref[d - 1] + exact[d];
    }

    const res = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const k = queries[i]; // zero‑based rank
        let l = 1, r = maxVal;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (pref[mid] > k) r = mid;
            else l = mid + 1;
        }
        res[i] = l;
    }
    return res;
};
```

## Typescript

```typescript
function gcdValues(nums: number[], queries: number[]): number[] {
    const MAX_VAL = 50000;
    const freq = new Uint32Array(MAX_VAL + 1);
    for (const v of nums) {
        freq[v]++;
    }

    // cntDiv[d] = count of numbers divisible by d
    const cntDiv = new Uint32Array(MAX_VAL + 1);
    for (let d = 1; d <= MAX_VAL; d++) {
        let sum = 0;
        for (let m = d; m <= MAX_VAL; m += d) {
            sum += freq[m];
        }
        cntDiv[d] = sum;
    }

    // f[d] = number of pairs with GCD exactly d
    const f = new Float64Array(MAX_VAL + 1);
    for (let d = MAX_VAL; d >= 1; d--) {
        let total = cntDiv[d] * (cntDiv[d] - 1) / 2;
        for (let m = d * 2; m <= MAX_VAL; m += d) {
            total -= f[m];
        }
        f[d] = total;
    }

    // prefix sums of counts for GCD <= d
    const pref = new Float64Array(MAX_VAL + 1);
    let acc = 0;
    for (let d = 1; d <= MAX_VAL; d++) {
        acc += f[d];
        pref[d] = acc;
    }

    const ans: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const k = queries[i]; // zero‑based index
        let lo = 1, hi = MAX_VAL;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (pref[mid] > k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        ans[i] = lo;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @return Integer[]
     */
    function gcdValues($nums, $queries) {
        // Determine maximum value in nums to limit array sizes
        $maxVal = 0;
        foreach ($nums as $v) {
            if ($v > $maxVal) $maxVal = $v;
        }
        $M = $maxVal;

        // Frequency of each number
        $cnt = array_fill(0, $M + 1, 0);
        foreach ($nums as $v) {
            $cnt[$v]++;
        }

        // mul[d] = count of numbers divisible by d
        $mul = array_fill(0, $M + 1, 0);
        for ($d = 1; $d <= $M; $d++) {
            $sum = 0;
            for ($m = $d; $m <= $M; $m += $d) {
                $sum += $cnt[$m];
            }
            $mul[$d] = $sum;
        }

        // pairs[d] = number of unordered pairs where both numbers are multiples of d
        $pairs = array_fill(0, $M + 1, 0);
        for ($d = 1; $d <= $M; $d++) {
            $c = $mul[$d];
            if ($c >= 2) {
                $pairs[$d] = intdiv($c * ($c - 1), 2);
            }
        }

        // exact[d] = number of pairs with GCD exactly d (inclusion‑exclusion)
        $exact = $pairs; // copy
        for ($d = $M; $d >= 1; $d--) {
            for ($multiple = $d * 2; $multiple <= $M; $multiple += $d) {
                $exact[$d] -= $exact[$multiple];
            }
        }

        // Prefix sums: cum[d] = number of pairs with GCD <= d
        $cum = array_fill(0, $M + 1, 0);
        $running = 0;
        for ($d = 1; $d <= $M; $d++) {
            $running += $exact[$d];
            $cum[$d] = $running;
        }

        // Answer each query via binary search on cum
        $ans = [];
        foreach ($queries as $k) {
            $lo = 1;
            $hi = $M;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($cum[$mid] > $k) {
                    $hi = $mid;
                } else {
                    $lo = $mid + 1;
                }
            }
            $ans[] = $lo;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func gcdValues(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let maxV = 50000
        var freq = [Int](repeating: 0, count: maxV + 1)
        for v in nums {
            freq[v] += 1
        }
        
        // cntDivisible[d] = number of elements divisible by d
        var cntDivisible = [Int](repeating: 0, count: maxV + 1)
        var d = 1
        while d <= maxV {
            var sum = 0
            var m = d
            while m <= maxV {
                sum += freq[m]
                m += d
            }
            cntDivisible[d] = sum
            d += 1
        }
        
        // exact[d] = number of pairs with gcd exactly d
        var exact = [Int64](repeating: 0, count: maxV + 1)
        d = maxV
        while d >= 1 {
            let c = cntDivisible[d]
            var totalPairs = Int64(c) * Int64(c - 1) / 2
            var sub: Int64 = 0
            var m = d * 2
            while m <= maxV {
                sub += exact[m]
                m += d
            }
            exact[d] = totalPairs - sub
            d -= 1
        }
        
        // prefix sums of exact to get count of pairs with gcd <= g
        var pref = [Int64](repeating: 0, count: maxV + 1)
        var g = 1
        while g <= maxV {
            pref[g] = pref[g - 1] + exact[g]
            g += 1
        }
        
        // answer queries via binary search on pref
        var ans = [Int]()
        ans.reserveCapacity(queries.count)
        for k in queries {
            var low = 1
            var high = maxV
            while low < high {
                let mid = (low + high) >> 1
                if pref[mid] > Int64(k) {
                    high = mid
                } else {
                    low = mid + 1
                }
            }
            ans.append(low)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun gcdValues(nums: IntArray, queries: LongArray): IntArray {
        var maxNum = 0
        for (v in nums) if (v > maxNum) maxNum = v
        val freq = IntArray(maxNum + 1)
        for (v in nums) freq[v]++

        // cnt[d]: number of elements divisible by d
        val cnt = IntArray(maxNum + 1)
        var d = 1
        while (d <= maxNum) {
            var sum = 0
            var m = d
            while (m <= maxNum) {
                sum += freq[m]
                m += d
            }
            cnt[d] = sum
            d++
        }

        // f[d]: number of pairs with GCD exactly d
        val f = LongArray(maxNum + 1)
        d = maxNum
        while (d >= 1) {
            var total = cnt[d].toLong() * (cnt[d] - 1) / 2
            var mult = d * 2
            while (mult <= maxNum) {
                total -= f[mult]
                mult += d
            }
            f[d] = total
            d--
        }

        // prefix sums of frequencies
        val pref = LongArray(maxNum + 1)
        var acc = 0L
        d = 1
        while (d <= maxNum) {
            acc += f[d]
            pref[d] = acc
            d++
        }

        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val k = queries[i]
            var lo = 1
            var hi = maxNum
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (pref[mid] > k) {
                    hi = mid
                } else {
                    lo = mid + 1
                }
            }
            ans[i] = lo
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> gcdValues(List<int> nums, List<int> queries) {
    int n = nums.length;
    int maxNum = 0;
    for (int v in nums) {
      if (v > maxNum) maxNum = v;
    }
    int limit = maxNum;

    // frequency of each value
    List<int> freq = List.filled(limit + 1, 0);
    for (int v in nums) {
      freq[v]++;
    }

    // cntDiv[d] = number of elements divisible by d
    List<int> cntDiv = List.filled(limit + 1, 0);
    for (int d = 1; d <= limit; ++d) {
      int sum = 0;
      for (int m = d; m <= limit; m += d) {
        sum += freq[m];
      }
      cntDiv[d] = sum;
    }

    // exact[g] = number of pairs with GCD exactly g
    List<int> exact = List.filled(limit + 1, 0);
    for (int g = limit; g >= 1; --g) {
      int c = cntDiv[g];
      int total = c * (c - 1) ~/ 2;
      int sub = 0;
      for (int mult = g * 2; mult <= limit; mult += g) {
        sub += exact[mult];
      }
      exact[g] = total - sub;
    }

    // prefix sums of counts
    List<int> cum = List.filled(limit + 1, 0);
    for (int g = 1; g <= limit; ++g) {
      cum[g] = cum[g - 1] + exact[g];
    }

    List<int> ans = List.filled(queries.length, 0);
    for (int i = 0; i < queries.length; ++i) {
      int k = queries[i];
      int lo = 1, hi = limit;
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (cum[mid] > k) {
          hi = mid;
        } else {
          lo = mid + 1;
        }
      }
      ans[i] = lo;
    }
    return ans;
  }
}
```

## Golang

```go
func gcdValues(nums []int, queries []int64) []int {
    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }

    freq := make([]int, maxVal+1)
    for _, v := range nums {
        freq[v]++
    }

    cnt := make([]int64, maxVal+1)
    for d := 1; d <= maxVal; d++ {
        var c int64
        for m := d; m <= maxVal; m += d {
            c += int64(freq[m])
        }
        cnt[d] = c
    }

    pairs := make([]int64, maxVal+1)
    for d := 1; d <= maxVal; d++ {
        c := cnt[d]
        if c >= 2 {
            pairs[d] = c * (c - 1) / 2
        }
    }

    exact := make([]int64, maxVal+1)
    for d := maxVal; d >= 1; d-- {
        val := pairs[d]
        for m := d * 2; m <= maxVal; m += d {
            val -= exact[m]
        }
        exact[d] = val
    }

    pref := make([]int64, maxVal+1)
    var sum int64
    for d := 1; d <= maxVal; d++ {
        sum += exact[d]
        pref[d] = sum
    }

    res := make([]int, len(queries))
    for i, k := range queries {
        lo, hi := 1, maxVal
        for lo < hi {
            mid := (lo + hi) / 2
            if pref[mid] > k {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        res[i] = lo
    }
    return res
}
```

## Ruby

```ruby
def gcd_values(nums, queries)
  max_val = nums.max
  freq = Array.new(max_val + 1, 0)
  nums.each { |x| freq[x] += 1 }

  cnt = Array.new(max_val + 1, 0)
  d = 1
  while d <= max_val
    sum = 0
    mult = d
    while mult <= max_val
      sum += freq[mult]
      mult += d
    end
    cnt[d] = sum
    d += 1
  end

  exact = Array.new(max_val + 1, 0)
  d = max_val
  while d >= 1
    total = cnt[d] * (cnt[d] - 1) / 2
    mult = d * 2
    while mult <= max_val
      total -= exact[mult]
      mult += d
    end
    exact[d] = total
    d -= 1
  end

  pref = Array.new(max_val + 1, 0)
  sum = 0
  d = 1
  while d <= max_val
    sum += exact[d]
    pref[d] = sum
    d += 1
  end

  answers = []
  queries.each do |k|
    lo = 1
    hi = max_val
    while lo < hi
      mid = (lo + hi) / 2
      if pref[mid] > k
        hi = mid
      else
        lo = mid + 1
      end
    end
    answers << lo
  end
  answers
end
```

## Scala

```scala
object Solution {
    def gcdValues(nums: Array[Int], queries: Array[Long]): Array[Int] = {
        val maxV = nums.max
        val freq = new Array[Int](maxV + 1)
        for (v <- nums) freq(v) += 1

        // cnt[d]: number of elements divisible by d
        val cnt = new Array[Long](maxV + 1)
        var d = 1
        while (d <= maxV) {
            var sum: Long = 0L
            var m = d
            while (m <= maxV) {
                sum += freq(m)
                m += d
            }
            cnt(d) = sum
            d += 1
        }

        // exact[g]: number of pairs with GCD exactly g
        val exact = new Array[Long](maxV + 1)
        var g = maxV
        while (g >= 1) {
            val c = cnt(g)
            var total: Long = c * (c - 1) / 2
            var mult = g + g // 2 * g
            while (mult <= maxV) {
                total -= exact(mult)
                mult += g
            }
            exact(g) = total
            g -= 1
        }

        // prefix sums of counts for binary search
        val pref = new Array[Long](maxV + 1)
        var acc: Long = 0L
        var i = 1
        while (i <= maxV) {
            acc += exact(i)
            pref(i) = acc
            i += 1
        }

        // answer queries
        val res = new Array[Int](queries.length)
        var idx = 0
        while (idx < queries.length) {
            val q = queries(idx)
            var l = 1
            var r = maxV
            while (l < r) {
                val mid = (l + r) >>> 1
                if (pref(mid) > q) r = mid else l = mid + 1
            }
            res(idx) = l
            idx += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn gcd_values(nums: Vec<i32>, queries: Vec<i64>) -> Vec<i32> {
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut freq = vec![0i32; max_val + 1];
        for &v in &nums {
            freq[v as usize] += 1;
        }

        // cnt[d]: number of elements divisible by d
        let mut cnt = vec![0i64; max_val + 1];
        for d in 1..=max_val {
            let mut sum = 0i64;
            let mut m = d;
            while m <= max_val {
                sum += freq[m] as i64;
                m += d;
            }
            cnt[d] = sum;
        }

        // f[g]: number of pairs with GCD exactly g
        let mut f = vec![0i64; max_val + 1];
        for g in (1..=max_val).rev() {
            let mut total = cnt[g] * (cnt[g] - 1) / 2;
            let mut mult = g * 2;
            while mult <= max_val {
                total -= f[mult];
                mult += g;
            }
            f[g] = total;
        }

        // prefix sums of counts for binary search
        let mut pref = vec![0i64; max_val + 1];
        for g in 1..=max_val {
            pref[g] = pref[g - 1] + f[g];
        }

        // answer queries
        let mut ans = Vec::with_capacity(queries.len());
        for &q in &queries {
            let mut lo = 1usize;
            let mut hi = max_val;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if pref[mid] > q {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            ans.push(lo as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (gcd-values nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((max-val (apply max nums))
         (size (+ max-val 1))
         (freq (make-vector size 0))
         (cnt (make-vector size 0))
         (exact (make-vector size 0)))
    ;; frequency of each number
    (for-each (lambda (v)
                (vector-set! freq v (+ 1 (vector-ref freq v))))
              nums)
    ;; count numbers divisible by d
    (let loop ((d 1))
      (when (<= d max-val)
        (let ((sum 0))
          (let inner ((m d))
            (when (<= m max-val)
              (set! sum (+ sum (vector-ref freq m)))
              (inner (+ m d))))
          (vector-set! cnt d sum))
        (loop (+ d 1))))
    ;; exact pairs with GCD == g, descending
    (let loop ((g max-val))
      (when (>= g 1)
        (define c (vector-ref cnt g))
        (define total (/ (* c (- c 1)) 2))
        (define sub
          (let ((s 0))
            (let inner ((m (+ g g)))
              (when (<= m max-val)
                (set! s (+ s (vector-ref exact m)))
                (inner (+ m g))))
            s))
        (vector-set! exact g (- total sub))
        (loop (- g 1))))
    ;; prepare queries with original indices
    (define qlen (length queries))
    (define qvec (list->vector queries))
    (define pairs
      (let loop ((i (- qlen 1)) (acc '()))
        (if (< i 0)
            acc
            (loop (- i 1) (cons (list (vector-ref qvec i) i) acc)))))
    (define sorted-pairs (sort pairs (lambda (a b) (< (first a) (first b)))))
    ;; answer queries by scanning GCD values increasingly
    (let ((ans (make-vector qlen))
          (ptr 0)
          (cum 0))
      (for ([g (in-range 1 (+ max-val 1))])
        (set! cum (+ cum (vector-ref exact g)))
        (let loop ()
          (when (and (< ptr qlen)
                     (< (first (list-ref sorted-pairs ptr)) cum))
            (define idx (second (list-ref sorted-pairs ptr)))
            (vector-set! ans idx g)
            (set! ptr (+ ptr 1))
            (loop))))
      (vector->list ans))))
```

## Erlang

```erlang
-spec gcd_values(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
gcd_values(Nums, Queries) ->
    Max = lists:max(Nums),
    FreqMap = build_freq_map(Nums, #{}),
    CntMap = build_cnt_map(Max, FreqMap, #{}),
    PairMultMap = maps:map(fun(_D, Cnt) -> (Cnt * (Cnt - 1)) div 2 end, CntMap),
    ExactMap = build_exact_map(Max, PairMultMap, #{}),
    PrefTuple = build_prefix_tuple(Max, ExactMap),
    lists:map(fun(Q) -> binary_search(Q, PrefTuple, Max) end, Queries).

build_freq_map([], Acc) -> Acc;
build_freq_map([H|T], Acc) ->
    NewAcc = maps:update_with(H, fun(C) -> C + 1 end, 1, Acc),
    build_freq_map(T, NewAcc).

build_cnt_map(0, _Freq, Acc) -> Acc;
build_cnt_map(D, Freq, Acc) when D > 0 ->
    Count = count_divisible(D, Max = maps:get(max_key, Freq, D), Freq, 0),
    NewAcc = maps:put(D, Count, Acc),
    build_cnt_map(D - 1, Freq, NewAcc).

count_divisible(_D, Limit, _Freq, Acc) when Limit < _D -> Acc;
count_divisible(D, Max, Freq, Acc) ->
    count_divisible_step(D, D, Max, Freq, Acc).

count_divisible_step(Cur, Step, Max, Freq, Acc) when Cur > Max -> Acc;
count_divisible_step(Cur, Step, Max, Freq, Acc) ->
    NewAcc = Acc + maps:get(Cur, Freq, 0),
    count_divisible_step(Cur + Step, Step, Max, Freq, NewAcc).

build_exact_map(0, _PairMap, Acc) -> Acc;
build_exact_map(D, PairMap, Acc) when D > 0 ->
    Total = maps:get(D, PairMap, 0),
    Sub = subtract_multiples(D * 2, D, Max = maps:get(max_key, PairMap, D), Acc, 0),
    Exact = Total - Sub,
    NewAcc = maps:put(D, Exact, Acc),
    build_exact_map(D - 1, PairMap, NewAcc).

subtract_multiples(Cur, Step, Max, ExactMap, Acc) when Cur > Max -> Acc;
subtract_multiples(Cur, Step, Max, ExactMap, Acc) ->
    NewAcc = Acc + maps:get(Cur, ExactMap, 0),
    subtract_multiples(Cur + Step, Step, Max, ExactMap, NewAcc).

build_prefix_tuple(Max, ExactMap) ->
    {_, RevList} = lists:foldl(
        fun(D, {PrevSum, List}) ->
            CurExact = maps:get(D, ExactMap, 0),
            NewSum = PrevSum + CurExact,
            {NewSum, [NewSum | List]}
        end,
        {0, []},
        lists:seq(1, Max)
    ),
    list_to_tuple(lists:reverse(RevList)).

binary_search(K, PrefTuple, Max) ->
    binary_search_loop(1, Max, K, PrefTuple).

binary_search_loop(Low, High, K, Pref) when Low < High ->
    Mid = (Low + High) div 2,
    Val = element(Mid, Pref),
    if
        Val > K -> binary_search_loop(Low, Mid, K, Pref);
        true -> binary_search_loop(Mid + 1, High, K, Pref)
    end;
binary_search_loop(Low, _High, _K, _Pref) ->
    Low.
```

## Elixir

```elixir
defmodule Solution do
  @spec gcd_values(nums :: [integer], queries :: [integer]) :: [integer]
  def gcd_values(nums, queries) do
    max_val = Enum.max(nums)

    cnt_arr = build_counts(nums, max_val)
    f_arr = compute_multiples(cnt_arr, max_val)
    {_g_arr, pref_arr} = compute_g_and_prefix(f_arr, max_val)

    Enum.map(queries, fn q -> kth_gcd(q, pref_arr, max_val) end)
  end

  defp build_counts(nums, max_val) do
    arr = :array.new(max_val + 1, default: 0)

    Enum.reduce(nums, arr, fn v, a ->
      cur = :array.get(v, a)
      :array.set(v, cur + 1, a)
    end)
  end

  defp compute_multiples(cnt_arr, max_val) do
    f_arr = :array.new(max_val + 1, default: 0)

    Enum.reduce(1..max_val, f_arr, fn d, acc ->
      total = sum_multiples(d, max_val, cnt_arr)
      :array.set(d, total, acc)
    end)
  end

  defp sum_multiples(d, max_val, cnt_arr) do
    Enum.reduce(1..div(max_val, d), 0, fn k, acc ->
      m = d * k
      acc + :array.get(m, cnt_arr)
    end)
  end

  defp compute_g_and_prefix(f_arr, max_val) do
    # compute exact GCD counts g[d] using inclusion‑exclusion
    g_arr =
      Enum.reduce(max_val..1, :array.new(max_val + 1, default: 0), fn d, ga ->
        f = :array.get(d, f_arr)
        total_pairs = div(f * (f - 1), 2)
        sub = sum_multiples_g(d, max_val, ga)
        g = total_pairs - sub
        :array.set(d, g, ga)
      end)

    # prefix sums pref[d] = number of pairs with GCD <= d
    pref_arr =
      Enum.reduce(1..max_val, :array.new(max_val + 1, default: 0), fn d, pa ->
        prev = if d == 1, do: 0, else: :array.get(d - 1, pa)
        g = :array.get(d, g_arr)
        :array.set(d, prev + g, pa)
      end)

    {g_arr, pref_arr}
  end

  defp sum_multiples_g(d, max_val, g_arr) do
    Enum.reduce(2..div(max_val, d), 0, fn k, acc ->
      m = d * k
      acc + :array.get(m, g_arr)
    end)
  end

  defp kth_gcd(k, pref_arr, max_val) do
    binary_search(1, max_val, k, pref_arr)
  end

  defp binary_search(lo, hi, k, pref_arr) when lo < hi do
    mid = div(lo + hi, 2)

    if :array.get(mid, pref_arr) > k do
      binary_search(lo, mid, k, pref_arr)
    else
      binary_search(mid + 1, hi, k, pref_arr)
    end
  end

  defp binary_search(lo, _hi, _k, _pref_arr), do: lo
end
```
