# 2584. Split the Array to Make Coprime Products

## Cpp

```cpp
class Solution {
public:
    int findValidSplit(std::vector<int>& nums) {
        const int MAXA = 1000000;
        static std::vector<int> spf(MAXA + 1);
        static bool ready = false;
        if (!ready) {
            for (int i = 2; i <= MAXA; ++i) {
                if (spf[i] == 0) {
                    for (int j = i; j <= MAXA; j += i)
                        if (spf[j] == 0) spf[j] = i;
                }
            }
            ready = true;
        }

        int n = nums.size();
        std::vector<int> last(MAXA + 1, -1);
        // record last occurrence of each prime factor
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                last[p] = i;
                while (x % p == 0) x /= p;
            }
        }

        int curMax = -1;
        for (int i = 0; i < n - 1; ++i) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                curMax = std::max(curMax, last[p]);
                while (x % p == 0) x /= p;
            }
            if (curMax == i) return i;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int findValidSplit(int[] nums) {
        int n = nums.length;
        if (n < 2) return -1;

        // Find maximum value to size SPF array
        int maxVal = 0;
        for (int v : nums) {
            if (v > maxVal) maxVal = v;
        }

        // Build smallest prime factor (SPF) sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long) i * i <= maxVal) {
                    for (int j = i * i; j <= maxVal; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        // Map each prime to its first and last occurrence indices
        java.util.HashMap<Integer, int[]> range = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                while (x % p == 0) x /= p;
                int[] idx = range.get(p);
                if (idx == null) {
                    range.put(p, new int[]{i, i});
                } else {
                    idx[1] = i; // update last occurrence
                }
            }
        }

        int curMax = -1;
        for (int i = 0; i < n - 1; i++) { // split must leave at least one element on the right
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                while (x % p == 0) x /= p;
                int[] idx = range.get(p);
                curMax = Math.max(curMax, idx[1]);
            }
            if (i == curMax) return i;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def findValidSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        max_val = max(nums)
        # smallest prime factor sieve
        spf = [0] * (max_val + 1)
        for i in range(2, max_val + 1):
            if spf[i] == 0:
                spf[i] = i
                if i * i <= max_val:
                    step = i
                    for j in range(i * i, max_val + 1, step):
                        if spf[j] == 0:
                            spf[j] = i

        n = len(nums)
        prime_factors = [None] * n
        last_occurrence = {}

        # factorize each number and record last occurrence of each prime
        for idx, num in enumerate(nums):
            x = num
            primes = []
            while x > 1:
                p = spf[x]
                if p == 0:   # when x is prime larger than sqrt(max_val)
                    p = x
                primes.append(p)
                while x % p == 0:
                    x //= p
            uniq = set(primes)          # unique primes for this element
            prime_factors[idx] = list(uniq)
            for p in uniq:
                last_occurrence[p] = idx

        cur_max = -1
        for i in range(n - 1):   # split must leave at least one element on the right
            for p in prime_factors[i]:
                if last_occurrence[p] > cur_max:
                    cur_max = last_occurrence[p]
            if cur_max <= i:    # all primes seen so far end no later than i
                return i
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        # smallest prime factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        def prime_factors(x: int) -> List[int]:
            res = []
            while x > 1:
                p = spf[x]
                res.append(p)
                while x % p == 0:
                    x //= p
            return list(set(res))

        # first pass: record last occurrence of each prime
        last_occurrence = {}
        factors_per_index = [None] * n
        for idx, val in enumerate(nums):
            primes = prime_factors(val)
            factors_per_index[idx] = primes
            for p in primes:
                last_occurrence[p] = idx

        cur_max = -1
        for i in range(n - 1):  # split after i, i <= n-2
            for p in factors_per_index[i]:
                cur_max = max(cur_max, last_occurrence[p])
            if cur_max == i:
                return i
        return -1
```

## C

```c
int findValidSplit(int* nums, int numsSize) {
    const int MAXA = 1000000;
    static int spf[MAXA + 1];
    static int lastPos[MAXA + 1];
    static int initialized = 0;

    if (!initialized) {
        for (int i = 0; i <= MAXA; ++i) spf[i] = i;
        spf[0] = 0;
        spf[1] = 1;
        for (int i = 2; i * i <= MAXA; ++i) {
            if (spf[i] == i) {
                for (int j = i * i; j <= MAXA; j += i) {
                    if (spf[j] == j) spf[j] = i;
                }
            }
        }
        initialized = 1;
    }

    for (int i = 0; i <= MAXA; ++i) lastPos[i] = -1;

    // Record the last occurrence index of each prime factor
    for (int idx = 0; idx < numsSize; ++idx) {
        int x = nums[idx];
        while (x > 1) {
            int p = spf[x];
            while (x % p == 0) x /= p;
            lastPos[p] = idx;
        }
    }

    int curMax = -1;
    for (int i = 0; i < numsSize - 1; ++i) {
        int x = nums[i];
        while (x > 1) {
            int p = spf[x];
            while (x % p == 0) x /= p;
            if (lastPos[p] > curMax) curMax = lastPos[p];
        }
        if (curMax == i) return i;
    }

    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int FindValidSplit(int[] nums) {
        const int MAX_VAL = 1000000;
        int[] spf = new int[MAX_VAL + 1];
        for (int i = 2; i <= MAX_VAL; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long)i * i <= MAX_VAL) {
                    for (int j = i * i; j <= MAX_VAL; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        int n = nums.Length;
        var first = new Dictionary<int, int>();
        var last = new Dictionary<int, int>();

        for (int idx = 0; idx < n; idx++) {
            int x = nums[idx];
            foreach (int p in GetDistinctPrimes(x, spf)) {
                if (!first.ContainsKey(p)) first[p] = idx;
                last[p] = idx;
            }
        }

        List<int>[] starts = new List<int>[n];
        foreach (var kvp in first) {
            int prime = kvp.Key;
            int fIdx = kvp.Value;
            if (starts[fIdx] == null) starts[fIdx] = new List<int>();
            starts[fIdx].Add(prime);
        }

        int curMax = -1;
        for (int i = 0; i < n - 1; i++) {
            var list = starts[i];
            if (list != null) {
                foreach (int p in list) {
                    int lIdx = last[p];
                    if (lIdx > curMax) curMax = lIdx;
                }
            }
            if (curMax <= i) return i;
        }

        return -1;
    }

    private static IEnumerable<int> GetDistinctPrimes(int x, int[] spf) {
        while (x > 1) {
            int p = spf[x];
            if (p == 0) p = x; // safety for numbers > MAX_VAL, though not needed here
            yield return p;
            while (x % p == 0) x /= p;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findValidSplit = function(nums) {
    const n = nums.length;
    if (n < 2) return -1;

    // Find maximum value to limit SPF sieve
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    // Build smallest prime factor array up to maxVal
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i * i <= maxVal; i++) {
        if (spf[i] === 0) {
            for (let j = i * i; j <= maxVal; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }
    for (let i = 2; i <= maxVal; i++) {
        if (spf[i] === 0) spf[i] = i;
    }

    // Store unique prime factors per index and last occurrence of each prime
    const primesPerIdx = new Array(n);
    const lastPos = Object.create(null); // map prime -> last index

    for (let idx = 0; idx < n; idx++) {
        let x = nums[idx];
        const list = [];
        while (x > 1) {
            const p = spf[x];
            list.push(p);
            while (x % p === 0) x = Math.trunc(x / p);
        }
        primesPerIdx[idx] = list;
        for (const p of list) {
            lastPos[p] = idx; // overwrite with later index
        }
    }

    let maxReach = -1;
    for (let i = 0; i < n - 1; i++) {
        const list = primesPerIdx[i];
        for (const p of list) {
            const pos = lastPos[p];
            if (pos > maxReach) maxReach = pos;
        }
        if (maxReach <= i) return i;
    }

    return -1;
};
```

## Typescript

```typescript
function findValidSplit(nums: number[]): number {
    const n = nums.length;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    // smallest prime factor sieve
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; ++i) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxVal) {
                for (let j = i * i; j <= maxVal; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    const getDistinctPrimes = (x: number): number[] => {
        const res: number[] = [];
        let num = x;
        while (num > 1) {
            const p = spf[num];
            res.push(p);
            while (num % p === 0) num = Math.floor(num / p);
        }
        return res;
    };

    // last occurrence of each prime
    const last = new Int32Array(maxVal + 1);
    last.fill(-1);
    for (let i = 0; i < n; ++i) {
        const primes = getDistinctPrimes(nums[i]);
        for (const p of primes) {
            last[p] = i;
        }
    }

    let maxLast = -1;
    for (let i = 0; i < n - 1; ++i) {
        const primes = getDistinctPrimes(nums[i]);
        for (const p of primes) {
            if (last[p] > maxLast) maxLast = last[p];
        }
        if (maxLast === i) return i;
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findValidSplit($nums) {
        $n = count($nums);
        $maxVal = 1000000;
        // smallest prime factor sieve
        $spf = array_fill(0, $maxVal + 1, 0);
        for ($i = 2; $i * $i <= $maxVal; $i++) {
            if ($spf[$i] == 0) { // i is prime
                for ($j = $i * $i; $j <= $maxVal; $j += $i) {
                    if ($spf[$j] == 0) {
                        $spf[$j] = $i;
                    }
                }
            }
        }

        $first = []; // prime => first index
        $last  = []; // prime => last index

        for ($idx = 0; $idx < $n; $idx++) {
            $x = $nums[$idx];
            $primes = [];
            while ($x > 1) {
                $p = $spf[$x] == 0 ? $x : $spf[$x];
                $primes[] = $p;
                while ($x % $p == 0) {
                    $x = intdiv($x, $p);
                }
            }
            foreach ($primes as $p) {
                if (!isset($first[$p])) {
                    $first[$p] = $idx;
                    $last[$p]  = $idx;
                } else {
                    $last[$p] = $idx;
                }
            }
        }

        // primes that start at each index
        $start = array_fill(0, $n, []);
        foreach ($first as $p => $s) {
            $start[$s][] = $p;
        }

        $maxLast = -1;
        for ($i = 0; $i < $n - 1; $i++) {
            foreach ($start[$i] as $p) {
                if ($last[$p] > $maxLast) {
                    $maxLast = $last[$p];
                }
            }
            if ($maxLast == $i) {
                return $i;
            }
        }

        return -1;
    }
}
```

## Swift

```swift
let MAXV = 1_000_000
var spfGlobal: [Int] = {
    var arr = [Int](repeating: 0, count: MAXV + 1)
    for i in 2...MAXV {
        if arr[i] == 0 {
            arr[i] = i
            if i * i <= MAXV {
                var j = i * i
                while j <= MAXV {
                    if arr[j] == 0 { arr[j] = i }
                    j += i
                }
            }
        }
    }
    return arr
}()

func getPrimeFactors(_ x: Int) -> [Int] {
    var num = x
    var res: [Int] = []
    while num > 1 {
        let p = spfGlobal[num]
        res.append(p)
        while num % p == 0 { num /= p }
    }
    return res
}

class Solution {
    func findValidSplit(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 1 { return -1 }
        var lastPos = [Int:Int]()
        for (i, val) in nums.enumerated() {
            let factors = getPrimeFactors(val)
            for p in factors {
                lastPos[p] = i
            }
        }
        var curMax = -1
        for i in 0..<(n - 1) {
            let factors = getPrimeFactors(nums[i])
            for p in factors {
                if let pos = lastPos[p], pos > curMax {
                    curMax = pos
                }
            }
            if curMax == i { return i }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MAX = 1_000_000
    private val spf = IntArray(MAX + 1)

    init {
        for (i in 2..MAX) {
            if (spf[i] == 0) {
                var j = i
                while (j <= MAX) {
                    if (spf[j] == 0) spf[j] = i
                    j += i
                }
            }
        }
    }

    private fun distinctPrimes(num: Int): IntArray {
        var x = num
        val tmp = IntArray(10)
        var sz = 0
        while (x > 1) {
            val p = spf[x]
            if (sz == 0 || tmp[sz - 1] != p) {
                tmp[sz++] = p
            }
            while (x % p == 0) x /= p
        }
        return tmp.copyOf(sz)
    }

    fun findValidSplit(nums: IntArray): Int {
        val n = nums.size
        val lastPos = HashMap<Int, Int>()
        for (i in 0 until n) {
            val primes = distinctPrimes(nums[i])
            for (p in primes) {
                lastPos[p] = i
            }
        }

        var maxLast = -1
        for (i in 0 until n - 1) {
            val primes = distinctPrimes(nums[i])
            for (p in primes) {
                val lp = lastPos[p]!!
                if (lp > maxLast) maxLast = lp
            }
            if (i == maxLast) return i
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int findValidSplit(List<int> nums) {
    int n = nums.length;
    int maxVal = 0;
    for (int v in nums) if (v > maxVal) maxVal = v;

    // Smallest prime factor sieve
    List<int> spf = List.filled(maxVal + 1, 0);
    for (int i = 2; i <= maxVal; ++i) {
      if (spf[i] == 0) {
        spf[i] = i;
        if (i * i <= maxVal) {
          for (int j = i * i; j <= maxVal; j += i) {
            if (spf[j] == 0) spf[j] = i;
          }
        }
      }
    }

    // Record last occurrence of each prime factor
    Map<int, int> lastPos = {};
    for (int idx = 0; idx < n; ++idx) {
      int x = nums[idx];
      while (x > 1) {
        int p = spf[x];
        lastPos[p] = idx;
        while (x % p == 0) {
          x ~/= p;
        }
      }
    }

    int far = -1;
    for (int i = 0; i < n - 1; ++i) {
      int x = nums[i];
      while (x > 1) {
        int p = spf[x];
        int last = lastPos[p]!;
        if (last > far) far = last;
        while (x % p == 0) {
          x ~/= p;
        }
      }
      if (far == i) return i;
    }
    return -1;
  }
}
```

## Golang

```go
func findValidSplit(nums []int) int {
    n := len(nums)
    if n < 2 {
        return -1
    }

    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }

    // Sieve for smallest prime factor
    spf := make([]int, maxVal+1)
    for i := 2; i <= maxVal; i++ {
        if spf[i] == 0 {
            spf[i] = i
            if i*i <= maxVal {
                for j := i * i; j <= maxVal; j += i {
                    if spf[j] == 0 {
                        spf[j] = i
                    }
                }
            }
        }
    }

    // Factor each number into distinct primes and record last occurrence
    primesAt := make([][]int, n)
    last := make(map[int]int)

    for idx, val := range nums {
        x := val
        var factors []int
        for x > 1 {
            p := spf[x]
            if p == 0 { // x is prime larger than sqrt(maxVal)
                p = x
            }
            factors = append(factors, p)
            for x%p == 0 {
                x /= p
            }
        }
        primesAt[idx] = factors
        for _, p := range factors {
            last[p] = idx // keep the latest index
        }
    }

    curMax := -1
    for i := 0; i < n-1; i++ {
        for _, p := range primesAt[i] {
            if li, ok := last[p]; ok && li > curMax {
                curMax = li
            }
        }
        if curMax == i {
            return i
        }
    }
    return -1
}
```

## Ruby

```ruby
def find_valid_split(nums)
  max_val = nums.max
  limit = max_val
  spf = Array.new(limit + 1, 0)
  (2..limit).each do |i|
    next unless spf[i] == 0
    spf[i] = i
    if i * i <= limit
      j = i * i
      while j <= limit
        spf[j] = i if spf[j] == 0
        j += i
      end
    end
  end

  first_occurrence = {}
  last_occurrence = {}

  nums.each_with_index do |val, idx|
    x = val
    while x > 1
      p = spf[x]
      while (x % p).zero?
        x /= p
      end
      first_occurrence[p] ||= idx
      last_occurrence[p] = idx
    end
  end

  cur_max = -1
  (0...nums.length - 1).each do |i|
    x = nums[i]
    while x > 1
      p = spf[x]
      while (x % p).zero?
        x /= p
      end
      lm = last_occurrence[p]
      cur_max = lm if lm > cur_max
    end
    return i if cur_max == i
  end

  -1
end
```

## Scala

```scala
object Solution {
  def findValidSplit(nums: Array[Int]): Int = {
    val maxVal = 1000000
    val spf = new Array[Int](maxVal + 1)
    for (i <- 2 to maxVal) {
      if (spf(i) == 0) {
        var j = i
        while (j <= maxVal) {
          if (spf(j) == 0) spf(j) = i
          j += i
        }
      }
    }

    val n = nums.length
    val first = new Array[Int](maxVal + 1)
    val last = new Array[Int](maxVal + 1)
    java.util.Arrays.fill(first, Int.MaxValue)

    // Record first and last occurrence of each prime factor
    for (idx <- 0 until n) {
      var x = nums(idx)
      while (x > 1) {
        val p = spf(x)
        if (first(p) == Int.MaxValue) first(p) = idx
        last(p) = idx
        while (x % p == 0) x /= p
      }
    }

    var maxLast = -1
    for (i <- 0 until n - 1) {
      var x = nums(i)
      while (x > 1) {
        val p = spf(x)
        maxLast = math.max(maxLast, last(p))
        while (x % p == 0) x /= p
      }
      if (maxLast == i) return i
    }
    -1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_valid_split(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 2 {
            return -1;
        }
        const MAX: usize = 1_000_000;
        // smallest prime factor sieve
        let mut spf = vec![0usize; MAX + 1];
        for i in 2..=MAX {
            if spf[i] == 0 {
                spf[i] = i;
                let mut j = i * 2;
                while j <= MAX {
                    if spf[j] == 0 {
                        spf[j] = i;
                    }
                    j += i;
                }
            }
        }

        use std::collections::HashMap;
        // last occurrence of each prime
        let mut last: HashMap<usize, usize> = HashMap::new();
        for (idx, &val) in nums.iter().enumerate() {
            let mut x = val as usize;
            while x > 1 {
                let p = spf[x];
                last.insert(p, idx);
                while x % p == 0 {
                    x /= p;
                }
            }
        }

        let mut max_last: usize = 0;
        for i in 0..n - 1 {
            let mut x = nums[i] as usize;
            while x > 1 {
                let p = spf[x];
                if let Some(&pos) = last.get(&p) {
                    if pos > max_last {
                        max_last = pos;
                    }
                }
                while x % p == 0 {
                    x /= p;
                }
            }
            if max_last == i {
                return i as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define (sieve-spf limit)
  (let ([spf (make-vector (+ limit 1) 0)])
    (for ([i (in-range 2 (add1 limit))])
      (when (= (vector-ref spf i) 0)
        (vector-set! spf i i)
        (let ([start (* i i)])
          (when (<= start limit)
            (for ([j (in-range start (add1 limit) i)])
              (when (= (vector-ref spf j) 0)
                (vector-set! spf j i)))))))
    spf))

(define (prime-factors n spf)
  (let loop ([x n] [seen (make-hash)])
    (if (= x 1)
        (hash-keys seen)
        (let* ([p (vector-ref spf x)])
          (hash-set! seen p #t)
          (loop (/ x p) seen)))))

(define/contract (find-valid-split nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [max-val (if (null? nums) 0 (apply max nums))]
         [spf (sieve-spf max-val)])
    (if (< n 2)
        -1
        (begin
          ;; last occurrence of each prime
          (define last (make-hash))
          (for ([i (in-range n)]
                [num nums])
            (let ([primes (prime-factors num spf)])
              (for ([p primes])
                (hash-set! last p i))))
          ;; scan for split
          (let loop ([i 0] [cur-max -1])
            (if (>= i (- n 1))
                -1
                (begin
                  (let* ([num (list-ref nums i)]
                         [primes (prime-factors num spf)])
                    (for ([p primes])
                      (let ([last-index (hash-ref last p)])
                        (when (> last-index cur-max)
                          (set! cur-max last-index)))))
                  (if (<= cur-max i)
                      i
                      (loop (+ i 1) cur-max)))))))))
```

## Erlang

```erlang
-spec find_valid_split(Nums :: [integer()]) -> integer().
find_valid_split(Nums) ->
    MaxPrime = trunc(math:sqrt(1000000)) + 1,
    SmallPrimes = sieve_primes(MaxPrime),
    LastMap = build_last_map(Nums, SmallPrimes, #{}, 0),
    case find_split(Nums, SmallPrimes, LastMap) of
        undefined -> -1;
        Index -> Index
    end.

%% Generate list of primes up to N (inclusive)
sieve_primes(N) ->
    [X || X <- lists:seq(2, N), is_prime(X)].

is_prime(2) -> true;
is_prime(N) when N rem 2 =:= 0 -> false;
is_prime(N) ->
    Limit = trunc(math:sqrt(N)),
    is_prime(N, 3, Limit).

is_prime(_, I, Limit) when I > Limit -> true;
is_prime(N, I, Limit) ->
    if N rem I =:= 0 -> false;
       true -> is_prime(N, I + 2, Limit)
    end.

%% Build map Prime => last index where it appears
build_last_map([], _, Map, _) -> Map;
build_last_map([Num|Rest], Primes, Map, Index) ->
    Factors = factor_distinct(Num, Primes),
    NewMap = lists:foldl(fun(P, Acc) -> maps:put(P, Index, Acc) end,
                         Map, Factors),
    build_last_map(Rest, Primes, NewMap, Index + 1).

%% Find smallest valid split index
find_split(List, Primes, LastMap) ->
    find_split(List, Primes, LastMap, 0, -1).

find_split([], _, _, _, _) -> undefined;
find_split([_], _, _, _, _) -> undefined; % only one element left cannot split
find_split([Num|Rest], Primes, LastMap, Index, CurMax) ->
    Factors = factor_distinct(Num, Primes),
    NewCurMax = lists:foldl(
        fun(P, Acc) ->
            L = maps:get(P, LastMap),
            if L > Acc -> L; true -> Acc end
        end,
        CurMax, Factors),
    case Rest of
        [] -> undefined;
        _ ->
            if NewCurMax == Index -> Index;
               true -> find_split(Rest, Primes, LastMap, Index + 1, NewCurMax)
            end
    end.

%% Return distinct prime factors of Num using the list of small primes
factor_distinct(Num, Primes) -> factor_distinct(Num, Primes, []).

factor_distinct(1, _, Acc) -> lists:reverse(Acc);
factor_distinct(N, [], Acc) ->
    case N > 1 of
        true -> lists:reverse([N|Acc]);
        false -> lists:reverse(Acc)
    end;
factor_distinct(N, [P|Rest] = Ps, Acc) when P * P =< N ->
    case N rem P of
        0 ->
            NewN = divide_out(N, P),
            factor_distinct(NewN, Ps, [P|Acc]);
        _ ->
            factor_distinct(N, Rest, Acc)
    end;
factor_distinct(N, _, Acc) -> % remaining prime larger than sqrt(N)
    case N > 1 of
        true -> lists:reverse([N|Acc]);
        false -> lists:reverse(Acc)
    end.

divide_out(N, P) when N rem P =:= 0 ->
    divide_out(N div P, P);
divide_out(N, _) -> N.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_valid_split(nums :: [integer]) :: integer
  def find_valid_split(nums) do
    n = length(nums)
    if n < 2, do: -1, else: compute_split(nums, n)
  end

  defp compute_split(nums, n) do
    primes = sieve(:math.sqrt(1_000_000) |> trunc())
    {first_map, last_map} = factor_all(nums, primes)

    intervals =
      first_map
      |> Enum.reduce([], fn {p, f}, acc ->
        l = Map.get(last_map, p)
        if f < l do
          [{f, l - 1} | acc]
        else
          acc
        end
      end)
      |> Enum.sort_by(fn {s, _e} -> s end)

    scan(0, -1, intervals, n - 2)
  end

  defp scan(i, cur_end, intervals, max_i) when i > max_i, do: -1

  defp scan(i, cur_end, intervals, max_i) do
    {new_cur_end, rest} = consume(intervals, i, cur_end)

    if i > new_cur_end do
      i
    else
      scan(i + 1, new_cur_end, rest, max_i)
    end
  end

  defp consume([], _i, cur_end), do: {cur_end, []}

  defp consume([{s, e} | tail] = list, i, cur_end) when s <= i do
    new_cur = if e > cur_end, do: e, else: cur_end
    consume(tail, i, new_cur)
  end

  defp consume(list, _i, cur_end), do: {cur_end, list}

  defp factor_all(nums, primes) do
    Enum.reduce(Enum.with_index(nums), {%{}, %{}}, fn {val, idx}, {first_map, last_map} ->
      facs = distinct_factors(val, primes)

      Enum.reduce(facs, {first_map, last_map}, fn p, {fmap, lmap} ->
        fmap = Map.update(fmap, p, idx, &min(&1, idx))
        lmap = Map.update(lmap, p, idx, &max(&1, idx))
        {fmap, lmap}
      end)
    end)
  end

  defp distinct_factors(num, primes) do
    factor(num, primes, [])
    |> Enum.reverse()
  end

  defp factor(1, _primes, acc), do: acc

  defp factor(n, [p | rest] = primes, acc) when p * p <= n do
    if rem(n, p) == 0 do
      n2 = div_out(n, p)
      factor(n2, primes, [p | acc])
    else
      factor(n, rest, acc)
    end
  end

  defp factor(n, _primes, acc) do
    if n > 1, do: [n | acc], else: acc
  end

  defp div_out(n, p) do
    if rem(n, p) == 0 do
      div_out(div(n, p), p)
    else
      n
    end
  end

  defp sieve(limit) when limit < 2, do: []

  defp sieve(limit) do
    2..limit
    |> Enum.reduce([], fn i, primes ->
      if Enum.any?(primes, fn p -> rem(i, p) == 0 end) do
        primes
      else
        [i | primes]
      end
    end)
    |> Enum.reverse()
  end
end
```
