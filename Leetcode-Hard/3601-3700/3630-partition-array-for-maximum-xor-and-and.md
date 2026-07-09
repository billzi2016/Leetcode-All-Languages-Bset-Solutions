# 3630. Partition Array for Maximum XOR and AND

## Cpp

```cpp
class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        const long long ALL_MASK = (1LL << 31) - 1; // bits 0..30
        int totalXor = 0;
        for (int v : nums) totalXor ^= v;
        long long best = 0;
        int totalMask = (int)ALL_MASK;
        int subsets = 1 << n;
        for (int maskB = 0; maskB < subsets; ++maskB) {
            int xorB = 0;
            int andB = totalMask;
            bool hasB = false;
            // compute xorB, andB
            for (int i = 0; i < n; ++i) {
                if (maskB >> i & 1) {
                    hasB = true;
                    xorB ^= nums[i];
                    andB &= nums[i];
                }
            }
            if (!hasB) andB = 0;
            int s = totalXor ^ xorB; // XOR of remaining elements
            long long mask = (~(long long)s) & ALL_MASK;
            long long basis[31] = {0};
            // build basis from remaining elements after masking
            for (int i = 0; i < n; ++i) {
                if ((maskB >> i & 1) == 0) {
                    long long val = ((long long)nums[i]) & mask;
                    for (int b = 30; b >= 0; --b) {
                        if (((val >> b) & 1LL) == 0) continue;
                        if (!basis[b]) {
                            basis[b] = val;
                            break;
                        }
                        val ^= basis[b];
                    }
                }
            }
            long long maxX = 0;
            for (int b = 30; b >= 0; --b) {
                if ((maxX ^ basis[b]) > maxX) maxX ^= basis[b];
            }
            long long cur = (long long)andB + (long long)s + 2LL * maxX;
            if (cur > best) best = cur;
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public long maximizeXorAndXor(int[] nums) {
        int n = nums.length;
        long best = 0;
        int totalMasks = 1 << n;
        for (int maskB = 0; maskB < totalMasks; maskB++) {
            int andB = 0;
            boolean hasB = false;
            int xorRest = 0;
            for (int i = 0; i < n; i++) {
                if ((maskB >> i & 1) == 1) {
                    if (!hasB) {
                        andB = nums[i];
                        hasB = true;
                    } else {
                        andB &= nums[i];
                    }
                } else {
                    xorRest ^= nums[i];
                }
            }
            if (!hasB) andB = 0;

            int mask = ~xorRest; // bits where xorRest is 0
            int[] basis = new int[31]; // up to bit 30 (since nums[i] <= 1e9)
            for (int i = 0; i < n; i++) {
                if ((maskB >> i & 1) == 0) {
                    int val = nums[i] & mask;
                    for (int b = 30; b >= 0; b--) {
                        if (((val >> b) & 1) == 0) continue;
                        if (basis[b] == 0) {
                            basis[b] = val;
                            break;
                        }
                        val ^= basis[b];
                    }
                }
            }

            int maxXor = 0;
            for (int b = 30; b >= 0; b--) {
                if ((maxXor ^ basis[b]) > maxXor) {
                    maxXor ^= basis[b];
                }
            }

            long total = (long) andB + (long) xorRest + 2L * maxXor;
            if (total > best) best = total;
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maximizeXorAndXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_xor = 0
        for v in nums:
            total_xor ^= v

        size = 1 << n
        xor_mask = [0] * size
        for mask in range(1, size):
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)
            xor_mask[mask] = xor_mask[mask ^ lsb] ^ nums[idx]

        best = 0
        # basis array for bits 0..30
        for mask in range(size):
            s = total_xor ^ xor_mask[mask]          # XOR of elements not in B
            not_s = ~s                               # Python infinite bits, will mask later
            basis = [0] * 31                         # up to bit 30

            m = (~mask) & (size - 1)                 # bits of indices not in B
            while m:
                lsb = m & -m
                idx = (lsb.bit_length() - 1)
                val = nums[idx] & not_s
                x = val
                for b in range(30, -1, -1):
                    if (x >> b) & 1:
                        if basis[b]:
                            x ^= basis[b]
                        else:
                            basis[b] = x
                            break
                m ^= lsb

            # get maximum xor from basis
            cur = 0
            for b in range(30, -1, -1):
                if (cur ^ basis[b]) > cur:
                    cur ^= basis[b]

            candidate = s + (cur << 1)   # s + 2*cur
            if candidate > best:
                best = candidate

        return best
```

## Python3

```python
from typing import List

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        for v in nums:
            total_xor ^= v

        MAX_BIT = 31
        FULL_MASK = (1 << MAX_BIT) - 1
        best = 0

        for bm in range(1 << n):
            # compute AND and XOR of subset B
            and_val = FULL_MASK
            xor_b = 0
            cnt = 0
            for i in range(n):
                if (bm >> i) & 1:
                    cnt += 1
                    and_val &= nums[i]
                    xor_b ^= nums[i]
            if cnt == 0:
                and_val = 0

            # XOR of remaining elements
            s = total_xor ^ xor_b
            mask = (~s) & FULL_MASK

            # build linear basis for masked remaining numbers
            basis = [0] * MAX_BIT
            for i in range(n):
                if (bm >> i) & 1:
                    continue
                x = nums[i] & mask
                for b in range(MAX_BIT - 1, -1, -1):
                    if not (x >> b) & 1:
                        continue
                    if basis[b] == 0:
                        basis[b] = x
                        break
                    x ^= basis[b]

            # get maximum xor from the basis
            max_xor = 0
            for b in range(MAX_BIT - 1, -1, -1):
                if (max_xor ^ basis[b]) > max_xor:
                    max_xor ^= basis[b]

            cur = and_val + s + (max_xor << 1)
            if cur > best:
                best = cur

        return best
```

## C

```c
#include <limits.h>
#include <stdint.h>

long long maximizeXorAndXor(int* nums, int numsSize) {
    int n = numsSize;
    uint32_t totalXor = 0;
    for (int i = 0; i < n; ++i) totalXor ^= (uint32_t)nums[i];

    long long best = 0;

    int totalMasks = 1 << n;
    for (int mask = 0; mask < totalMasks; ++mask) {
        uint32_t andB = UINT_MAX;
        uint32_t xorB = 0;
        int hasB = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                if (!hasB) { andB = (uint32_t)nums[i]; hasB = 1; }
                else andB &= (uint32_t)nums[i];
                xorB ^= (uint32_t)nums[i];
            }
        }
        if (!hasB) andB = 0;

        uint32_t S = totalXor ^ xorB;
        uint32_t maskNotS = ~S;

        int basis[31] = {0};
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) {
                uint32_t val = ((uint32_t)nums[i]) & maskNotS;
                for (int b = 30; b >= 0; --b) {
                    if ((val >> b) & 1U) {
                        if (!basis[b]) { basis[b] = val; break; }
                        val ^= (uint32_t)basis[b];
                    }
                }
            }
        }

        uint32_t maxY = 0;
        for (int b = 30; b >= 0; --b) {
            if ((maxY ^ basis[b]) > maxY) maxY ^= (uint32_t)basis[b];
        }

        long long cur = (long long)andB + (long long)S + 2LL * (long long)maxY;
        if (cur > best) best = cur;
    }
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaximizeXorAndXor(int[] nums)
    {
        int n = nums.Length;
        long best = 0;
        int totalMasks = 1 << n;
        const long MASK_ALL = (1L << 31) - 1; // bits 0..30

        for (int mask = 0; mask < totalMasks; ++mask)
        {
            long andB = 0;
            bool firstAnd = true;
            long sXor = 0;

            // First pass: compute AND of B and XOR of remaining elements
            for (int i = 0; i < n; ++i)
            {
                if ((mask >> i & 1) == 1)
                {
                    if (firstAnd)
                    {
                        andB = nums[i];
                        firstAnd = false;
                    }
                    else
                    {
                        andB &= nums[i];
                    }
                }
                else
                {
                    sXor ^= nums[i];
                }
            }

            // Build linear basis for masked remaining values
            long notS = (~sXor) & MASK_ALL;
            long[] basis = new long[31];

            for (int i = 0; i < n; ++i)
            {
                if ((mask >> i & 1) == 1) continue; // element is in B

                long w = ((long)nums[i]) & notS;
                for (int bit = 30; bit >= 0; --bit)
                {
                    if (((w >> bit) & 1) == 0) continue;
                    if (basis[bit] == 0)
                    {
                        basis[bit] = w;
                        break;
                    }
                    w ^= basis[bit];
                }
            }

            // Maximize xor using the basis
            long maxY = 0;
            for (int bit = 30; bit >= 0; --bit)
            {
                if ((maxY ^ basis[bit]) > maxY) maxY ^= basis[bit];
            }

            long total = andB + sXor + 2 * maxY;
            if (total > best) best = total;
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximizeXorAndXor = function(nums) {
    const n = nums.length;
    const totalXor = nums.reduce((a, b) => a ^ b, 0);
    let best = 0;

    const maxBit = 30; // since nums[i] <= 1e9 < 2^30

    for (let mask = 0; mask < (1 << n); ++mask) {
        // compute AND and XOR of subset B (elements where bit is set)
        let andB = 0;
        let xorB = 0;
        let first = true;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                const v = nums[i];
                xorB ^= v;
                if (first) {
                    andB = v;
                    first = false;
                } else {
                    andB &= v;
                }
            }
        }
        // empty B => andB stays 0, which matches problem definition

        const s = totalXor ^ xorB; // XOR of remaining elements
        // build linear basis over (num & ~s) for remaining elements
        const basis = new Array(maxBit + 1).fill(0);
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) continue; // element belongs to B, skip
            let v = nums[i] & (~s);
            // insert v into basis
            for (let b = maxBit; b >= 0; --b) {
                if (((v >> b) & 1) === 0) continue;
                if (basis[b] === 0) {
                    basis[b] = v;
                    break;
                }
                v ^= basis[b];
            }
        }

        // maximize achievable XOR using the basis
        let maxX = 0;
        for (let b = maxBit; b >= 0; --b) {
            if ((maxX ^ basis[b]) > maxX) {
                maxX ^= basis[b];
            }
        }

        const cur = andB + s + (maxX << 1);
        if (cur > best) best = cur;
    }

    return best;
};
```

## Typescript

```typescript
function maximizeXorAndXor(nums: number[]): number {
    const n = nums.length;
    const totalXor = nums.reduce((a, b) => a ^ b, 0);
    let best = 0;

    const limitMask = (1 << 31) - 1; // not used directly, we rely on >>>0

    for (let maskB = 0; maskB < (1 << n); ++maskB) {
        let andB = 0;
        let xorB = 0;
        let first = true;

        for (let i = 0; i < n; ++i) {
            if ((maskB >> i) & 1) {
                xorB ^= nums[i];
                if (first) {
                    andB = nums[i];
                    first = false;
                } else {
                    andB &= nums[i];
                }
            }
        }
        if (first) andB = 0; // empty B

        const s = totalXor ^ xorB;          // XOR of the remaining elements
        const mask = (~s) >>> 0;             // bits where s has 0, as unsigned 32‑bit

        // linear basis for masked values of the remaining elements
        const basis = new Array(31).fill(0);
        for (let i = 0; i < n; ++i) {
            if (!((maskB >> i) & 1)) {       // element not in B
                let v = nums[i] & mask;
                for (let bit = 30; bit >= 0; --bit) {
                    if (((v >>> bit) & 1) === 0) continue;
                    if (basis[bit] === 0) {
                        basis[bit] = v;
                        break;
                    }
                    v ^= basis[bit];
                }
            }
        }

        // obtain maximum xor from the basis
        let maxXor = 0;
        for (let bit = 30; bit >= 0; --bit) {
            if ((maxXor ^ basis[bit]) > maxXor) {
                maxXor ^= basis[bit];
            }
        }

        const candidate = andB + s + 2 * maxXor;
        if (candidate > best) best = candidate;
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximizeXorAndXor($nums) {
        $n = count($nums);
        $totalXor = 0;
        foreach ($nums as $v) {
            $totalXor ^= $v;
        }
        // mask for lower 31 bits (enough for nums <= 1e9)
        $fullMask = (1 << 31) - 1;
        $maxAns = 0;
        $limit = 1 << $n;

        for ($mask = 0; $mask < $limit; $mask++) {
            // compute AND and XOR of subset B
            $andB = 0;
            $xorB = 0;
            $first = true;
            for ($i = 0; $i < $n; $i++) {
                if (($mask >> $i) & 1) {
                    $val = $nums[$i];
                    $xorB ^= $val;
                    if ($first) {
                        $andB = $val;
                        $first = false;
                    } else {
                        $andB &= $val;
                    }
                }
            }
            if ($first) { // B is empty
                $andB = 0;
            }

            $s = $totalXor ^ $xorB; // XOR of remaining elements

            // build linear basis from masked remaining numbers
            $basis = array_fill(0, 31, 0);
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) == 0) { // element not in B
                    $w = $nums[$i] & (~$s & $fullMask);
                    $x = $w;
                    for ($bit = 30; $bit >= 0; $bit--) {
                        if (($x >> $bit) & 1) {
                            if ($basis[$bit] == 0) {
                                $basis[$bit] = $x;
                                break;
                            } else {
                                $x ^= $basis[$bit];
                            }
                        }
                    }
                }
            }

            // obtain maximum XOR from the basis
            $maxXor = 0;
            for ($bit = 30; $bit >= 0; $bit--) {
                if (($maxXor ^ $basis[$bit]) > $maxXor) {
                    $maxXor ^= $basis[$bit];
                }
            }

            // total value for this partition
            $candidate = $andB + $s + (2 * $maxXor);
            if ($candidate > $maxAns) {
                $maxAns = $candidate;
            }
        }

        return $maxAns;
    }
}
```

## Swift

```swift
class Solution {
    func maximizeXorAndXor(_ nums: [Int]) -> Int {
        let n = nums.count
        let allMask = (1 << 31) - 1   // keep bits up to 30
        var best = 0
        let totalMasks = 1 << n
        
        for mask in 0..<totalMasks {
            var s = 0
            // XOR of elements not in B (mask)
            for i in 0..<n where (mask & (1 << i)) == 0 {
                s ^= nums[i]
            }
            
            let complementMask = (~s) & allMask
            var basis = Array(repeating: 0, count: 31)
            
            // Build linear basis from transformed numbers of remaining elements
            for i in 0..<n where (mask & (1 << i)) == 0 {
                var x = nums[i] & complementMask
                var bit = 30
                while bit >= 0 && x != 0 {
                    if ((x >> bit) & 1) == 1 {
                        if basis[bit] == 0 {
                            basis[bit] = x
                            break
                        } else {
                            x ^= basis[bit]
                        }
                    }
                    bit -= 1
                }
            }
            
            // Get maximum subset xor from the basis
            var maxXor = 0
            for i in stride(from: 30, through: 0, by: -1) {
                if (maxXor ^ basis[i]) > maxXor {
                    maxXor ^= basis[i]
                }
            }
            
            let candidate = s + 2 * maxXor
            if candidate > best { best = candidate }
        }
        
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeXorAndXor(nums: IntArray): Long {
        val n = nums.size
        val totalMask = (1 shl n) - 1
        val size = 1 shl n
        val xorAll = IntArray(size)
        val andAll = IntArray(size) // default 0 for empty set

        for (mask in 1 until size) {
            val lsb = mask and -mask
            val idx = Integer.numberOfTrailingZeros(lsb)
            val prev = mask xor lsb
            xorAll[mask] = xorAll[prev] xor nums[idx]
            if (prev == 0) {
                andAll[mask] = nums[idx]
            } else {
                andAll[mask] = andAll[prev] and nums[idx]
            }
        }

        // mask with lower 31 bits set to 1
        val maskAll = -1 ushr 1   // 0x7fffffff

        var answer = 0L
        for (bMask in 0 until size) {
            val andB = andAll[bMask]
            val rMask = totalMask xor bMask
            val s = xorAll[rMask]

            // bits where s has 0 within considered range
            val maskBits = maskAll xor s

            // linear basis for masked remaining numbers
            val basis = IntArray(31)
            var i = 0
            while (i < n) {
                if ((bMask and (1 shl i)) == 0) {
                    var v = nums[i] and maskBits
                    var x = v
                    for (bit in 30 downTo 0) {
                        if ((x shr bit) and 1 == 0) continue
                        if (basis[bit] == 0) {
                            basis[bit] = x
                            break
                        }
                        x = x xor basis[bit]
                    }
                }
                i++
            }

            var maxXor = 0
            for (bit in 30 downTo 0) {
                if ((maxXor xor basis[bit]) > maxXor) {
                    maxXor = maxXor xor basis[bit]
                }
            }

            val candidate = s.toLong() + 2L * maxXor.toLong() + andB.toLong()
            if (candidate > answer) answer = candidate
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximizeXorAndXor(List<int> nums) {
    int n = nums.length;
    int totalXor = 0;
    for (int v in nums) totalXor ^= v;

    int best = 0;
    int maxMask = 1 << n;

    for (int mask = 0; mask < maxMask; ++mask) {
      int andB = -1;
      int xorB = 0;
      bool hasB = false;

      for (int i = 0; i < n; ++i) {
        if ((mask >> i & 1) == 1) {
          hasB = true;
          andB &= nums[i];
          xorB ^= nums[i];
        }
      }
      if (!hasB) andB = 0;

      int s = totalXor ^ xorB; // XOR of elements not in B

      // Build linear basis for masked numbers
      List<int> basis = List.filled(31, 0);
      for (int i = 0; i < n; ++i) {
        if ((mask >> i & 1) == 1) continue;
        int val = nums[i] & (~s);
        for (int b = 30; b >= 0; --b) {
          if (((val >> b) & 1) == 0) continue;
          if (basis[b] == 0) {
            basis[b] = val;
            break;
          }
          val ^= basis[b];
        }
      }

      // Maximize x & ~s using the basis
      int cur = 0;
      for (int b = 30; b >= 0; --b) {
        if ((cur ^ basis[b]) > cur) cur ^= basis[b];
      }

      int total = andB + s + 2 * cur;
      if (total > best) best = total;
    }
    return best;
  }
}
```

## Golang

```go
func maximizeXorAndXor(nums []int) int64 {
    n := len(nums)
    totalXor := 0
    for _, v := range nums {
        totalXor ^= v
    }
    best := int64(0)
    limit := 1 << n

    for mask := 0; mask < limit; mask++ {
        xorB := 0
        andVal := 0
        first := true
        for i := 0; i < n; i++ {
            if (mask>>i)&1 == 1 {
                v := nums[i]
                xorB ^= v
                if first {
                    andVal = v
                    first = false
                } else {
                    andVal &= v
                }
            }
        }

        var andCon int64
        if mask != 0 {
            andCon = int64(andVal)
        }

        s := totalXor ^ xorB

        // linear basis for masked values
        const maxBit = 60
        basis := make([]int, maxBit+1)
        for i := 0; i < n; i++ {
            if (mask>>i)&1 == 0 {
                val := nums[i] & (^s)
                x := val
                for b := maxBit; b >= 0 && x != 0; b-- {
                    if ((x >> b) & 1) == 0 {
                        continue
                    }
                    if basis[b] == 0 {
                        basis[b] = x
                        break
                    }
                    x ^= basis[b]
                }
            }
        }

        maxXor := 0
        for b := maxBit; b >= 0; b-- {
            if (maxXor ^ basis[b]) > maxXor {
                maxXor ^= basis[b]
            }
        }

        cur := andCon + int64(s) + int64(2*maxXor)
        if cur > best {
            best = cur
        }
    }
    return best
}
```

## Ruby

```ruby
def maximize_xor_and_xor(nums)
  n = nums.length
  total_subsets = 1 << n
  mask_all = (1 << 31) - 1
  best = 0

  (0...total_subsets).each do |b|
    and_val = nil
    s = 0
    i = 0
    while i < n
      if ((b >> i) & 1) == 1
        if and_val.nil?
          and_val = nums[i]
        else
          and_val &= nums[i]
        end
      else
        s ^= nums[i]
      end
      i += 1
    end
    and_val = 0 if and_val.nil?

    mask = (~s) & mask_all
    basis = Array.new(31, 0)

    i = 0
    while i < n
      if ((b >> i) & 1) == 0
        v = nums[i] & mask
        x = v
        bit = 30
        while bit >= 0
          if ((x >> bit) & 1) == 1
            if basis[bit] == 0
              basis[bit] = x
              break
            else
              x ^= basis[bit]
            end
          end
          bit -= 1
        end
      end
      i += 1
    end

    max_xor = 0
    bit = 30
    while bit >= 0
      if (max_xor ^ basis[bit]) > max_xor
        max_xor ^= basis[bit]
      end
      bit -= 1
    end

    total = and_val + s + 2 * max_xor
    best = total if total > best
  end

  best
end
```

## Scala

```scala
object Solution {
    def maximizeXorAndXor(nums: Array[Int]): Long = {
        val n = nums.length
        val totalXor = nums.foldLeft(0)(_ ^ _)
        var best: Long = 0L
        val limit = 1 << n

        for (mask <- 0 until limit) {
            // compute AND of B and XOR of B
            var andVal = -1
            var xorB = 0
            var i = 0
            while (i < n) {
                if ((mask >> i & 1) == 1) {
                    andVal &= nums(i)
                    xorB ^= nums(i)
                }
                i += 1
            }
            if (mask == 0) andVal = 0

            val sXor = totalXor ^ xorB // XOR of remaining elements

            // build linear basis for masked values
            val basis = new Array[Int](31) // bits 30..0
            i = 0
            while (i < n) {
                if ((mask >> i & 1) == 0) {
                    var v = nums(i) & ~sXor
                    var x = v
                    var b = 30
                    while (b >= 0 && x != 0) {
                        if (((x >> b) & 1) != 0) {
                            if (basis(b) == 0) {
                                basis(b) = x
                                // inserted, break inner loop
                                b = -1
                            } else {
                                x ^= basis(b)
                            }
                        }
                        b -= 1
                    }
                }
                i += 1
            }

            var maxMaskXor = 0
            var b = 30
            while (b >= 0) {
                if ((maxMaskXor ^ basis(b)) > maxMaskXor) {
                    maxMaskXor ^= basis(b)
                }
                b -= 1
            }

            val candidate = andVal.toLong + sXor.toLong + 2L * maxMaskXor
            if (candidate > best) best = candidate
        }

        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_xor_and_xor(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let size = 1usize << n;
        // Convert to u32 for bitwise operations
        let nums_u: Vec<u32> = nums.iter().map(|&x| x as u32).collect();

        // Precompute total xor of all elements
        let mut total_xor: u32 = 0;
        for &v in &nums_u {
            total_xor ^= v;
        }

        // Precompute xor and AND for every subset mask
        let mut xor_sub = vec![0u32; size];
        let mut and_sub = vec![0u32; size]; // 0 for empty set
        for mask in 1..size {
            let idx = mask.trailing_zeros() as usize;
            let prev = mask & !(1usize << idx);
            xor_sub[mask] = xor_sub[prev] ^ nums_u[idx];
            if prev == 0 {
                and_sub[mask] = nums_u[idx];
            } else {
                and_sub[mask] = and_sub[prev] & nums_u[idx];
            }
        }

        let mut answer: i64 = 0;

        // Iterate over all possible B subsets
        for mask in 0..size {
            let and_b = and_sub[mask] as i64;
            let xor_b = xor_sub[mask];
            let s = total_xor ^ xor_b;          // XOR of remaining elements
            let not_s = !s;                     // bits where s has 0

            // Linear basis for values (v & ~s) of remaining elements
            let mut basis = [0u32; 32]; // up to bit 31 (since nums <= 1e9)
            for i in 0..n {
                if (mask >> i) & 1 == 0 {
                    let mut x = nums_u[i] & not_s;
                    // insert into basis
                    for bit in (0..32).rev() {
                        if ((x >> bit) & 1) == 0 {
                            continue;
                        }
                        if basis[bit] == 0 {
                            basis[bit] = x;
                            break;
                        } else {
                            x ^= basis[bit];
                        }
                    }
                }
            }

            // Compute maximum xor achievable from the basis
            let mut max_x: u32 = 0;
            for bit in (0..32).rev() {
                if (max_x ^ basis[bit]) > max_x {
                    max_x ^= basis[bit];
                }
            }

            // Candidate value: AND(B) + s + 2 * max_x
            let candidate = and_b + s as i64 + 2 * max_x as i64;
            if candidate > answer {
                answer = candidate;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define (maximize-xor-and-xor nums)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (limit-mask (sub1 (expt 2 31))) ; bits 0..30 set
         (total-xor (let loop ((i 0) (acc 0))
                      (if (= i n)
                          acc
                          (loop (+ i 1) (bitwise-xor acc (vector-ref arr i))))))
         (best (let ((ans 0))
                 (for ([mask (in-range (expt 2 n))])
                   ;; compute xorB and andB for subset B = mask
                   (define xorB 0)
                   (define andB 0)
                   (if (= mask 0)
                       (set! andB 0)
                       (set! andB #xffffffff))
                   (for ([i (in-range n)])
                     (when (not (zero? (bitwise-and mask (arithmetic-shift 1 i))))
                       (set! xorB (bitwise-xor xorB (vector-ref arr i)))
                       (when (not (= mask 0))
                         (set! andB (bitwise-and andB (vector-ref arr i))))))
                   ;; s = XOR of elements not in B
                   (define s (bitwise-xor total-xor xorB))
                   (define maskLimited (bitwise-and (bitwise-not s) limit-mask))
                   ;; build linear basis over (num & maskLimited) for elements not in B
                   (define basis (make-vector 31 0))
                   (for ([i (in-range n)])
                     (when (zero? (bitwise-and mask (arithmetic-shift 1 i))) ; i not in B
                       (let ((v (bitwise-and (vector-ref arr i) maskLimited)))
                         (let insert ((val v))
                           (when (> val 0)
                             (define msb (- (integer-length val) 1))
                             (define cur (vector-ref basis msb))
                             (if (= cur 0)
                                 (vector-set! basis msb val)
                                 (insert (bitwise-xor val cur)))))))))
                   ;; obtain maximum xor from the basis
                   (define maxX 0)
                   (for ([b (in-range 30 -1 -1)]) ; descending bits
                     (let ((vec (vector-ref basis b)))
                       (when (and (> vec 0) (> (bitwise-xor maxX vec) maxX))
                         (set! maxX (bitwise-xor maxX vec)))))
                   ;; total value for this partition
                   (define total (+ s (arithmetic-shift maxX 1) andB))
                   (when (> total ans)
                     (set! ans total)))
                 ans)))
    best))
```

## Erlang

```erlang
-module(solution).
-export([maximize_xor_and_xor/1]).

-define(ALL_BITS, (1 bsl 31) - 1).

-spec maximize_xor_and_xor(Nums :: [integer()]) -> integer().
maximize_xor_and_xor(Nums) ->
    N = length(Nums),
    Arr = list_to_tuple(Nums),
    TotalMasks = 1 bsl N,
    loop_masks(0, TotalMasks, N, Arr, ?ALL_BITS, 0).

loop_masks(Mask, Limit, N, Arr, AllMask, Max) when Mask < Limit ->
    {AndB, XorRest} = compute_and_xor(N, Arr, Mask),
    S = XorRest,
    NotS = bnot(S) band AllMask,
    Basis = build_basis(N, Arr, Mask, NotS, []),
    MaxXor = max_from_basis(Basis),
    Candidate = AndB + S + 2 * MaxXor,
    NewMax = if Candidate > Max -> Candidate; true -> Max end,
    loop_masks(Mask + 1, Limit, N, Arr, AllMask, NewMax);
loop_masks(_, _, _, _, _, Max) ->
    Max.

compute_and_xor(N, Arr, Mask) ->
    compute_and_xor(0, N - 1, Arr, Mask, undefined, 0).

compute_and_xor(I, Last, _Arr, _Mask, AndAcc, XorAcc) when I > Last ->
    AndVal = case AndAcc of
        undefined -> 0;
        _ -> AndAcc
    end,
    {AndVal, XorAcc};
compute_and_xor(I, Last, Arr, Mask, AndAcc, XorAcc) ->
    Elem = element(I + 1, Arr),
    Bit = 1 bsl I,
    if (Mask band Bit) =/= 0 ->
            NewAnd = case AndAcc of
                undefined -> Elem;
                _ -> AndAcc band Elem
            end,
            compute_and_xor(I + 1, Last, Arr, Mask, NewAnd, XorAcc);
       true ->
            compute_and_xor(I + 1, Last, Arr, Mask, AndAcc, XorAcc bxor Elem)
    end.

build_basis(N, Arr, Mask, NotS, Basis) ->
    build_basis(0, N - 1, Arr, Mask, NotS, Basis).

build_basis(I, Last, _Arr, _Mask, _NotS, Basis) when I > Last ->
    Basis;
build_basis(I, Last, Arr, Mask, NotS, Basis) ->
    Elem = element(I + 1, Arr),
    Bit = 1 bsl I,
    NewBasis =
        if (Mask band Bit) =:= 0 ->
                V = Elem band NotS,
                insert_basis(Basis, V);
           true -> Basis
        end,
    build_basis(I + 1, Last, Arr, Mask, NotS, NewBasis).

insert_basis(Basis, X) when X =:= 0 ->
    Basis;
insert_basis(Basis, X) ->
    Reduced = lists:foldl(fun(B, Acc) ->
                case (Acc bxor B) < Acc of
                    true -> Acc bxor B;
                    false -> Acc
                end
            end, X, Basis),
    if Reduced =:= 0 -> Basis; true -> [Reduced | Basis] end.

max_from_basis(Basis) ->
    Sorted = lists:sort(fun(A, B) -> A > B end, Basis),
    lists:foldl(fun(B, Acc) ->
                case (Acc bxor B) > Acc of
                    true -> Acc bxor B;
                    false -> Acc
                end
            end, 0, Sorted).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec maximize_xor_and_xor(nums :: [integer]) :: integer
  def maximize_xor_and_xor(nums) do
    n = length(nums)
    max_mask = 1 <<< n

    Enum.reduce(0..max_mask - 1, 0, fn mask, best ->
      {and_val_opt, s, rem} =
        Enum.reduce(Enum.with_index(nums), {nil, 0, []}, fn {v, i},
                                                          {a, sx, r} ->
          if ((mask >>> i) &&& 1) == 1 do
            a2 = if a == nil, do: v, else: band(a, v)
            {a2, sx, r}
          else
            {a, bxor(sx, v), [v | r]}
          end
        end)

      and_val = if and_val_opt == nil, do: 0, else: and_val_opt

      mask_not_s = bnot(s)

      basis =
        Enum.reduce(rem, [], fn v, bas ->
          x = band(v, mask_not_s)

          x_red =
            Enum.reduce(bas, x, fn b, acc ->
              if bxor(acc, b) < acc, do: bxor(acc, b), else: acc
            end)

          if x_red != 0, do: [x_red | bas], else: bas
        end)
        |> Enum.sort(&>=/2)

      max_x =
        Enum.reduce(basis, 0, fn b, acc ->
          nx = bxor(acc, b)
          if nx > acc, do: nx, else: acc
        end)

      total = and_val + s + (max_x <<< 1)
      if total > best, do: total, else: best
    end)
  end
end
```
