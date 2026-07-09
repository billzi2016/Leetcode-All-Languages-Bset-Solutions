# 3334. Find the Maximum Factor Score of Array

## Cpp

```cpp
class Solution {
public:
    long long maxScore(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        std::vector<long long> pre_gcd(n), pre_lcm(n), suf_gcd(n), suf_lcm(n);
        auto lcm = [&](long long a, long long b)->long long{
            if (a==0 || b==0) return 0;
            long long g = std::gcd(a,b);
            return a / g * b;
        };
        for (int i = 0; i < n; ++i) {
            if (i == 0) {
                pre_gcd[i] = nums[i];
                pre_lcm[i] = nums[i];
            } else {
                pre_gcd[i] = std::gcd(pre_gcd[i-1], (long long)nums[i]);
                pre_lcm[i] = lcm(pre_lcm[i-1], (long long)nums[i]);
            }
        }
        for (int i = n-1; i >= 0; --i) {
            if (i == n-1) {
                suf_gcd[i] = nums[i];
                suf_lcm[i] = nums[i];
            } else {
                suf_gcd[i] = std::gcd(suf_gcd[i+1], (long long)nums[i]);
                suf_lcm[i] = lcm(suf_lcm[i+1], (long long)nums[i]);
            }
        }
        long long ans = pre_gcd[n-1] * pre_lcm[n-1]; // no removal
        for (int i = 0; i < n; ++i) {
            if (n == 1) { // removing the only element gives empty array score 0
                ans = std::max(ans, 0LL);
                continue;
            }
            long long g, l;
            if (i == 0) {
                g = suf_gcd[1];
                l = suf_lcm[1];
            } else if (i == n-1) {
                g = pre_gcd[n-2];
                l = pre_lcm[n-2];
            } else {
                g = std::gcd(pre_gcd[i-1], suf_gcd[i+1]);
                l = lcm(pre_lcm[i-1], suf_lcm[i+1]);
            }
            ans = std::max(ans, g * l);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private long lcm(long a, long b) {
        if (a == 0 || b == 0) return 0;
        return a / gcd(a, b) * b;
    }

    public long maxScore(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0L;

        long[] preGcd = new long[n];
        long[] preLcm = new long[n];
        for (int i = 0; i < n; i++) {
            long val = nums[i];
            if (i == 0) {
                preGcd[i] = val;
                preLcm[i] = val;
            } else {
                preGcd[i] = gcd(preGcd[i - 1], val);
                preLcm[i] = lcm(preLcm[i - 1], val);
            }
        }

        long[] sufGcd = new long[n];
        long[] sufLcm = new long[n];
        for (int i = n - 1; i >= 0; i--) {
            long val = nums[i];
            if (i == n - 1) {
                sufGcd[i] = val;
                sufLcm[i] = val;
            } else {
                sufGcd[i] = gcd(sufGcd[i + 1], val);
                sufLcm[i] = lcm(sufLcm[i + 1], val);
            }
        }

        long maxScore = preGcd[n - 1] * preLcm[n - 1]; // no removal

        for (int i = 0; i < n; i++) {
            if (n == 1) { // removing the only element yields empty array
                maxScore = Math.max(maxScore, 0L);
                continue;
            }
            long g, l;
            if (i == 0) {
                g = sufGcd[1];
                l = sufLcm[1];
            } else if (i == n - 1) {
                g = preGcd[n - 2];
                l = preLcm[n - 2];
            } else {
                g = gcd(preGcd[i - 1], sufGcd[i + 1]);
                l = lcm(preLcm[i - 1], sufLcm[i + 1]);
            }
            long score = g * l;
            if (score > maxScore) maxScore = score;
        }

        return maxScore;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math

        n = len(nums)

        # Prefix and suffix GCD
        prefix_gcd = [0] * (n + 1)
        suffix_gcd = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_gcd[i] = math.gcd(prefix_gcd[i - 1], nums[i - 1])
        for i in range(n - 1, -1, -1):
            suffix_gcd[i] = math.gcd(suffix_gcd[i + 1], nums[i])

        # Helper LCM
        def lcm(a, b):
            return a * b // math.gcd(a, b)

        # Prefix and suffix LCM (identity element is 1)
        prefix_lcm = [1] * (n + 1)
        suffix_lcm = [1] * (n + 1)
        for i in range(1, n + 1):
            prefix_lcm[i] = lcm(prefix_lcm[i - 1], nums[i - 1])
        for i in range(n - 1, -1, -1):
            suffix_lcm[i] = lcm(suffix_lcm[i + 1], nums[i])

        # No removal case
        max_score = prefix_gcd[n] * prefix_lcm[n]

        # Remove each element once
        for i in range(n):
            g = math.gcd(prefix_gcd[i], suffix_gcd[i + 1])
            l = lcm(prefix_lcm[i], suffix_lcm[i + 1])
            score = g * l
            if score > max_score:
                max_score = score

        return max_score
```

## Python3

```python
import math
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # helper lcm
        def lcm(a: int, b: int) -> int:
            return a // math.gcd(a, b) * b

        prefix_gcd = [0] * n
        suffix_gcd = [0] * n
        prefix_lcm = [0] * n
        suffix_lcm = [0] * n

        prefix_gcd[0] = nums[0]
        prefix_lcm[0] = nums[0]
        for i in range(1, n):
            prefix_gcd[i] = math.gcd(prefix_gcd[i - 1], nums[i])
            prefix_lcm[i] = lcm(prefix_lcm[i - 1], nums[i])

        suffix_gcd[-1] = nums[-1]
        suffix_lcm[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_gcd[i] = math.gcd(suffix_gcd[i + 1], nums[i])
            suffix_lcm[i] = lcm(suffix_lcm[i + 1], nums[i])

        # score without removing any element
        ans = prefix_gcd[-1] * prefix_lcm[-1]

        for i in range(n):
            if n == 1:
                g = 0
                l = 0
            elif i == 0:
                g = suffix_gcd[1]
                l = suffix_lcm[1]
            elif i == n - 1:
                g = prefix_gcd[n - 2]
                l = prefix_lcm[n - 2]
            else:
                g = math.gcd(prefix_gcd[i - 1], suffix_gcd[i + 1])
                l = lcm(prefix_lcm[i - 1], suffix_lcm[i + 1])
            ans = max(ans, g * l)

        return ans
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

static long long lcm_ll(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return a / gcd_ll(a, b) * b;
}

long long maxScore(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    long long prefix_gcd[101];
    long long suffix_gcd[102];
    long long prefix_lcm[101];
    long long suffix_lcm[102];

    prefix_gcd[0] = 0;
    prefix_lcm[0] = 1;
    for (int i = 1; i <= numsSize; ++i) {
        long long val = nums[i - 1];
        prefix_gcd[i] = gcd_ll(prefix_gcd[i - 1], val);
        prefix_lcm[i] = lcm_ll(prefix_lcm[i - 1], val);
    }

    suffix_gcd[numsSize] = 0;
    suffix_lcm[numsSize] = 1;
    for (int i = numsSize - 1; i >= 0; --i) {
        long long val = nums[i];
        suffix_gcd[i] = gcd_ll(suffix_gcd[i + 1], val);
        suffix_lcm[i] = lcm_ll(suffix_lcm[i + 1], val);
    }

    long long ans = 0;
    // No removal
    long long total_gcd = prefix_gcd[numsSize];
    long long total_lcm = prefix_lcm[numsSize];
    if (total_gcd != 0) {
        long long score = total_gcd * total_lcm;
        if (score > ans) ans = score;
    }

    // Remove one element
    for (int i = 0; i < numsSize; ++i) {
        long long g = gcd_ll(prefix_gcd[i], suffix_gcd[i + 1]);
        long long l = lcm_ll(prefix_lcm[i], suffix_lcm[i + 1]);
        if (g != 0) {
            long long score = g * l;
            if (score > ans) ans = score;
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private static long Gcd(long a, long b)
    {
        while (b != 0)
        {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private static long Lcm(long a, long b)
    {
        if (a == 0 || b == 0) return 0;
        return a / Gcd(a, b) * b;
    }

    public long MaxScore(int[] nums)
    {
        int n = nums.Length;
        if (n == 0) return 0;

        long[] prefixGcd = new long[n];
        long[] suffixGcd = new long[n];
        long[] prefixLcm = new long[n];
        long[] suffixLcm = new long[n];

        for (int i = 0; i < n; i++)
        {
            long val = nums[i];
            if (i == 0)
            {
                prefixGcd[i] = val;
                prefixLcm[i] = val;
            }
            else
            {
                prefixGcd[i] = Gcd(prefixGcd[i - 1], val);
                prefixLcm[i] = Lcm(prefixLcm[i - 1], val);
            }
        }

        for (int i = n - 1; i >= 0; i--)
        {
            long val = nums[i];
            if (i == n - 1)
            {
                suffixGcd[i] = val;
                suffixLcm[i] = val;
            }
            else
            {
                suffixGcd[i] = Gcd(suffixGcd[i + 1], val);
                suffixLcm[i] = Lcm(suffixLcm[i + 1], val);
            }
        }

        long maxScore = prefixGcd[n - 1] * prefixLcm[n - 1]; // no removal

        for (int i = 0; i < n; i++)
        {
            if (n == 1) break; // removing the only element yields empty array with score 0

            long g, l;
            if (i == 0)
            {
                g = suffixGcd[1];
                l = suffixLcm[1];
            }
            else if (i == n - 1)
            {
                g = prefixGcd[n - 2];
                l = prefixLcm[n - 2];
            }
            else
            {
                g = Gcd(prefixGcd[i - 1], suffixGcd[i + 1]);
                l = Lcm(prefixLcm[i - 1], suffixLcm[i + 1]);
            }

            long score = g * l;
            if (score > maxScore) maxScore = score;
        }

        return maxScore;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;

    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    };
    const lcm = (a, b) => {
        if (a === 0 || b === 0) return 0;
        return (a / gcd(a, b)) * b;
    };

    // prefix GCD and LCM
    const preGcd = new Array(n + 1).fill(0);
    const preLcm = new Array(n + 1).fill(1);
    for (let i = 0; i < n; ++i) {
        preGcd[i + 1] = gcd(preGcd[i], nums[i]);
        preLcm[i + 1] = lcm(preLcm[i], nums[i]);
    }

    // suffix GCD and LCM
    const sufGcd = new Array(n + 1).fill(0);
    const sufLcm = new Array(n + 1).fill(1);
    for (let i = n - 1; i >= 0; --i) {
        sufGcd[i] = gcd(sufGcd[i + 1], nums[i]);
        sufLcm[i] = lcm(sufLcm[i + 1], nums[i]);
    }

    // score without removal
    let best = preGcd[n] * preLcm[n];

    // try removing each element
    for (let i = 0; i < n; ++i) {
        const remainingLen = n - 1;
        if (remainingLen === 0) {
            // empty array after removal, score is 0
            best = Math.max(best, 0);
            continue;
        }
        const g = gcd(preGcd[i], sufGcd[i + 1]);
        const l = lcm(preLcm[i], sufLcm[i + 1]);
        best = Math.max(best, g * l);
    }

    return best;
};
```

## Typescript

```typescript
function maxScore(nums: number[]): number {
    const n = nums.length;
    const prefixGcd = new Array(n + 1).fill(0);
    const suffixGcd = new Array(n + 1).fill(0);
    const prefixLcm = new Array(n + 1).fill(1);
    const suffixLcm = new Array(n + 1).fill(1);

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    };
    const lcm = (a: number, b: number): number => {
        if (a === 0 || b === 0) return 0;
        return (a / gcd(a, b)) * b;
    };

    for (let i = 0; i < n; ++i) {
        prefixGcd[i + 1] = gcd(prefixGcd[i], nums[i]);
        prefixLcm[i + 1] = lcm(prefixLcm[i], nums[i]);
    }
    for (let i = n - 1; i >= 0; --i) {
        suffixGcd[i] = gcd(suffixGcd[i + 1], nums[i]);
        suffixLcm[i] = lcm(suffixLcm[i + 1], nums[i]);
    }

    let ans = 0;
    // No removal
    ans = Math.max(ans, prefixGcd[n] * prefixLcm[n]);

    // Remove each element once
    for (let i = 0; i < n; ++i) {
        const g = gcd(prefixGcd[i], suffixGcd[i + 1]);
        const l = lcm(prefixLcm[i], suffixLcm[i + 1]);
        ans = Math.max(ans, g * l);
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxScore($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        
        // Prefix GCD and LCM
        $prefixGcd = [];
        $prefixLcm = [];
        for ($i = 0; $i < $n; $i++) {
            if ($i == 0) {
                $prefixGcd[$i] = $nums[$i];
                $prefixLcm[$i] = $nums[$i];
            } else {
                $prefixGcd[$i] = $this->gcd($prefixGcd[$i - 1], $nums[$i]);
                $prefixLcm[$i] = $this->lcm($prefixLcm[$i - 1], $nums[$i]);
            }
        }
        
        // Suffix GCD and LCM
        $suffixGcd = [];
        $suffixLcm = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i == $n - 1) {
                $suffixGcd[$i] = $nums[$i];
                $suffixLcm[$i] = $nums[$i];
            } else {
                $suffixGcd[$i] = $this->gcd($suffixGcd[$i + 1], $nums[$i]);
                $suffixLcm[$i] = $this->lcm($suffixLcm[$i + 1], $nums[$i]);
            }
        }
        
        // No removal case
        $maxScore = $prefixGcd[$n - 1] * $prefixLcm[$n - 1];
        
        // Try removing each element (at most one)
        for ($i = 0; $i < $n; $i++) {
            if ($n == 1) {
                // Removing the only element gives empty array => score 0
                continue;
            }
            if ($i == 0) {
                $g = $suffixGcd[1];
                $l = $suffixLcm[1];
            } elseif ($i == $n - 1) {
                $g = $prefixGcd[$n - 2];
                $l = $prefixLcm[$n - 2];
            } else {
                $g = $this->gcd($prefixGcd[$i - 1], $suffixGcd[$i + 1]);
                $l = $this->lcm($prefixLcm[$i - 1], $suffixLcm[$i + 1]);
            }
            $score = $g * $l;
            if ($score > $maxScore) {
                $maxScore = $score;
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
    
    private function lcm($a, $b) {
        if ($a == 0 || $b == 0) return 0;
        return intdiv($a, $this->gcd($a, $b)) * $b;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a, y = b
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }
        
        func lcm(_ a: Int, _ b: Int) -> Int {
            if a == 0 || b == 0 { return 0 }
            let g = gcd(a, b)
            let res = (Int64(a) / Int64(g)) * Int64(b)
            return Int(res)
        }
        
        var prefixGCD = Array(repeating: 0, count: n)
        var suffixGCD = Array(repeating: 0, count: n)
        var prefixLCM = Array(repeating: 0, count: n)
        var suffixLCM = Array(repeating: 0, count: n)
        
        for i in 0..<n {
            if i == 0 {
                prefixGCD[i] = nums[i]
                prefixLCM[i] = nums[i]
            } else {
                prefixGCD[i] = gcd(prefixGCD[i - 1], nums[i])
                prefixLCM[i] = lcm(prefixLCM[i - 1], nums[i])
            }
        }
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            if i == n - 1 {
                suffixGCD[i] = nums[i]
                suffixLCM[i] = nums[i]
            } else {
                suffixGCD[i] = gcd(suffixGCD[i + 1], nums[i])
                suffixLCM[i] = lcm(suffixLCM[i + 1], nums[i])
            }
        }
        
        var best = prefixGCD[n - 1] * prefixLCM[n - 1]
        if n == 1 { return best }
        
        for i in 0..<n {
            var g: Int
            var l: Int
            if i == 0 {
                g = suffixGCD[1]
                l = suffixLCM[1]
            } else if i == n - 1 {
                g = prefixGCD[n - 2]
                l = prefixLCM[n - 2]
            } else {
                g = gcd(prefixGCD[i - 1], suffixGCD[i + 1])
                l = lcm(prefixLCM[i - 1], suffixLCM[i + 1])
            }
            let score = g * l
            if score > best { best = score }
        }
        
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(nums: IntArray): Long {
        val n = nums.size
        if (n == 0) return 0L

        val prefixGcd = LongArray(n)
        val prefixLcm = LongArray(n)
        for (i in 0 until n) {
            val v = nums[i].toLong()
            if (i == 0) {
                prefixGcd[i] = v
                prefixLcm[i] = v
            } else {
                prefixGcd[i] = gcd(prefixGcd[i - 1], v)
                prefixLcm[i] = lcm(prefixLcm[i - 1], v)
            }
        }

        val suffixGcd = LongArray(n)
        val suffixLcm = LongArray(n)
        for (i in n - 1 downTo 0) {
            val v = nums[i].toLong()
            if (i == n - 1) {
                suffixGcd[i] = v
                suffixLcm[i] = v
            } else {
                suffixGcd[i] = gcd(suffixGcd[i + 1], v)
                suffixLcm[i] = lcm(suffixLcm[i + 1], v)
            }
        }

        var maxScore = prefixGcd[n - 1] * prefixLcm[n - 1]

        for (i in 0 until n) {
            if (n == 1) break
            val g: Long
            val l: Long
            when (i) {
                0 -> {
                    g = suffixGcd[1]
                    l = suffixLcm[1]
                }
                n - 1 -> {
                    g = prefixGcd[n - 2]
                    l = prefixLcm[n - 2]
                }
                else -> {
                    g = gcd(prefixGcd[i - 1], suffixGcd[i + 1])
                    l = lcm(prefixLcm[i - 1], suffixLcm[i + 1])
                }
            }
            val score = g * l
            if (score > maxScore) maxScore = score
        }

        return maxScore
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }

    private fun lcm(a: Long, b: Long): Long {
        if (a == 0L || b == 0L) return 0L
        return a / gcd(a, b) * b
    }
}
```

## Dart

```dart
class Solution {
  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a.abs();
  }

  int _lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return a ~/ _gcd(a, b) * b;
  }

  int maxScore(List<int> nums) {
    int n = nums.length;
    List<int> preGcd = List.filled(n + 1, 0);
    List<int> sufGcd = List.filled(n + 1, 0);
    List<int> preLcm = List.filled(n + 1, 1);
    List<int> sufLcm = List.filled(n + 1, 1);

    for (int i = 0; i < n; ++i) {
      preGcd[i + 1] = _gcd(preGcd[i], nums[i]);
      preLcm[i + 1] = _lcm(preLcm[i], nums[i]);
    }
    for (int i = n - 1; i >= 0; --i) {
      sufGcd[i] = _gcd(sufGcd[i + 1], nums[i]);
      sufLcm[i] = _lcm(sufLcm[i + 1], nums[i]);
    }

    int maxScore = preGcd[n] * preLcm[n];

    for (int i = 0; i < n; ++i) {
      int g = _gcd(preGcd[i], sufGcd[i + 1]);
      int l = _lcm(preLcm[i], sufLcm[i + 1]);
      int score = g * l;
      if (score > maxScore) maxScore = score;
    }

    return maxScore;
  }
}
```

## Golang

```go
func maxScore(nums []int) int64 {
    n := len(nums)
    if n == 0 {
        return 0
    }
    // helper functions
    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }
    var gcd64 func(a, b int64) int64
    gcd64 = func(a, b int64) int64 {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }
    lcm64 := func(a, b int64) int64 {
        if a == 0 || b == 0 {
            return 0
        }
        g := gcd64(a, b)
        return a / g * b
    }

    // prefix GCD and LCM
    prefGcd := make([]int, n)
    prefLcm := make([]int64, n)
    prefGcd[0] = nums[0]
    prefLcm[0] = int64(nums[0])
    for i := 1; i < n; i++ {
        prefGcd[i] = gcd(prefGcd[i-1], nums[i])
        prefLcm[i] = lcm64(prefLcm[i-1], int64(nums[i]))
    }

    // suffix GCD and LCM
    suffGcd := make([]int, n)
    suffLcm := make([]int64, n)
    suffGcd[n-1] = nums[n-1]
    suffLcm[n-1] = int64(nums[n-1])
    for i := n - 2; i >= 0; i-- {
        suffGcd[i] = gcd(suffGcd[i+1], nums[i])
        suffLcm[i] = lcm64(suffLcm[i+1], int64(nums[i]))
    }

    // score without removal
    maxScore := int64(prefGcd[n-1]) * prefLcm[n-1]

    // consider removing each element (at most one)
    for i := 0; i < n; i++ {
        if n == 1 { // removal would leave empty array, score = 0
            break
        }
        var g int
        var l int64
        if i == 0 {
            g = suffGcd[1]
            l = suffLcm[1]
        } else if i == n-1 {
            g = prefGcd[n-2]
            l = prefLcm[n-2]
        } else {
            g = gcd(prefGcd[i-1], suffGcd[i+1])
            l = lcm64(prefLcm[i-1], suffLcm[i+1])
        }
        score := int64(g) * l
        if score > maxScore {
            maxScore = score
        }
    }

    return maxScore
}
```

## Ruby

```ruby
def max_score(nums)
  n = nums.length
  return 0 if n == 0

  prefix_gcd = Array.new(n)
  prefix_lcm = Array.new(n)

  (0...n).each do |i|
    if i.zero?
      prefix_gcd[i] = nums[i]
      prefix_lcm[i] = nums[i]
    else
      prefix_gcd[i] = prefix_gcd[i - 1].gcd(nums[i])
      prefix_lcm[i] = prefix_lcm[i - 1].lcm(nums[i])
    end
  end

  suffix_gcd = Array.new(n)
  suffix_lcm = Array.new(n)

  (n - 1).downto(0) do |i|
    if i == n - 1
      suffix_gcd[i] = nums[i]
      suffix_lcm[i] = nums[i]
    else
      suffix_gcd[i] = suffix_gcd[i + 1].gcd(nums[i])
      suffix_lcm[i] = suffix_lcm[i + 1].lcm(nums[i])
    end
  end

  max_score = prefix_gcd[n - 1] * prefix_lcm[n - 1]

  (0...n).each do |i|
    next if n == 1 # removal would leave empty array, score 0

    if i.zero?
      g = suffix_gcd[1]
      l = suffix_lcm[1]
    elsif i == n - 1
      g = prefix_gcd[n - 2]
      l = prefix_lcm[n - 2]
    else
      g = prefix_gcd[i - 1].gcd(suffix_gcd[i + 1])
      l = prefix_lcm[i - 1].lcm(suffix_lcm[i + 1])
    end

    score = g * l
    max_score = score if score > max_score
  end

  max_score
end
```

## Scala

```scala
object Solution {
  def maxScore(nums: Array[Int]): Long = {
    val n = nums.length
    if (n == 0) return 0L

    def gcdLong(a: Long, b: Long): Long = {
      var x = a
      var y = b
      while (y != 0) {
        val t = x % y
        x = y
        y = t
      }
      if (x < 0) -x else x
    }

    def lcmLong(a: Long, b: Long): Long = {
      if (a == 0L || b == 0L) 0L else a / gcdLong(a, b) * b
    }

    val preGcd = new Array[Long](n + 1)
    preGcd(0) = 0L
    for (i <- 1 to n) {
      preGcd(i) = gcdLong(preGcd(i - 1), nums(i - 1).toLong)
    }

    val sufGcd = new Array[Long](n + 1)
    sufGcd(n) = 0L
    for (i <- (n - 1) to 0 by -1) {
      sufGcd(i) = gcdLong(sufGcd(i + 1), nums(i).toLong)
    }

    val preLcm = new Array[Long](n + 1)
    preLcm(0) = 1L
    for (i <- 1 to n) {
      preLcm(i) = lcmLong(preLcm(i - 1), nums(i - 1).toLong)
    }

    val sufLcm = new Array[Long](n + 1)
    sufLcm(n) = 1L
    for (i <- (n - 1) to 0 by -1) {
      sufLcm(i) = lcmLong(sufLcm(i + 1), nums(i).toLong)
    }

    var ans: Long = preGcd(n) * preLcm(n)

    if (n > 1) {
      for (i <- 0 until n) {
        val g = gcdLong(preGcd(i), sufGcd(i + 1))
        val l = lcmLong(preLcm(i), sufLcm(i + 1))
        ans = math.max(ans, g * l)
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i64 {
        fn gcd_i32(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }
        fn gcd_i64(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // prefix gcd and lcm
        let mut pref_gcd = vec![0i32; n];
        let mut pref_lcm = vec![0i64; n];
        for i in 0..n {
            if i == 0 {
                pref_gcd[i] = nums[0];
                pref_lcm[i] = nums[0] as i64;
            } else {
                pref_gcd[i] = gcd_i32(pref_gcd[i - 1], nums[i]);
                let g = gcd_i64(pref_lcm[i - 1], nums[i] as i64);
                pref_lcm[i] = pref_lcm[i - 1] / g * (nums[i] as i64);
            }
        }

        // suffix gcd and lcm
        let mut suff_gcd = vec![0i32; n];
        let mut suff_lcm = vec![0i64; n];
        for i in (0..n).rev() {
            if i == n - 1 {
                suff_gcd[i] = nums[i];
                suff_lcm[i] = nums[i] as i64;
            } else {
                suff_gcd[i] = gcd_i32(suff_gcd[i + 1], nums[i]);
                let g = gcd_i64(suff_lcm[i + 1], nums[i] as i64);
                suff_lcm[i] = suff_lcm[i + 1] / g * (nums[i] as i64);
            }
        }

        // score without removal
        let mut ans: i64 = (pref_gcd[n - 1] as i64) * pref_lcm[n - 1];

        // consider removing each element
        for i in 0..n {
            if n == 1 {
                // removal would lead to empty array, score is 0
                continue;
            }
            let (gcd_val, lcm_val) = if i == 0 {
                (suff_gcd[1] as i64, suff_lcm[1])
            } else if i == n - 1 {
                (pref_gcd[n - 2] as i64, pref_lcm[n - 2])
            } else {
                let g = gcd_i32(pref_gcd[i - 1], suff_gcd[i + 1]) as i64;
                let gg = gcd_i64(pref_lcm[i - 1], suff_lcm[i + 1]);
                let l = pref_lcm[i - 1] / gg * suff_lcm[i + 1];
                (g, l)
            };
            ans = ans.max(gcd_val * lcm_val);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-score nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums))
         (pref-gcd (make-vector (+ n 1) 0))
         (pref-lcm (make-vector (+ n 1) 1))
         (suff-gcd (make-vector (+ n 1) 0))
         (suff-lcm (make-vector (+ n 1) 1)))
    ;; build prefix arrays
    (let loop ((i 0))
      (when (< i n)
        (let* ((a (vector-ref v i))
               (g (gcd (vector-ref pref-gcd i) a))
               (l (lcm (vector-ref pref-lcm i) a)))
          (vector-set! pref-gcd (add1 i) g)
          (vector-set! pref-lcm (add1 i) l)
          (loop (add1 i)))))
    ;; build suffix arrays
    (let loop ((i (- n 1)))
      (when (>= i 0)
        (let* ((a (vector-ref v i))
               (g (gcd a (vector-ref suff-gcd (add1 i))))
               (l (lcm a (vector-ref suff-lcm (add1 i)))))
          (vector-set! suff-gcd i g)
          (vector-set! suff-lcm i l)
          (loop (- i 1)))))
    ;; compute maximum score
    (let ((max0 (* (vector-ref pref-gcd n) (vector-ref pref-lcm n))))
      (let loop ((i 0) (best max0))
        (if (= i n)
            best
            (let* ((g (gcd (vector-ref pref-gcd i) (vector-ref suff-gcd (add1 i))))
                   (l (lcm (vector-ref pref-lcm i) (vector-ref suff-lcm (add1 i))))
                   (score (* g l))
                   (new-best (if (> score best) score best)))
              (loop (add1 i) new-best)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_score/1]).

-spec max_score(Nums :: [integer()]) -> integer().
max_score(Nums) ->
    Len = length(Nums),
    Scores0 = [factor_score(Nums)],
    Scores1 = [factor_score(remove_at(I, Nums)) || I <- lists:seq(1, Len)],
    lists:max(Scores0 ++ Scores1).

remove_at(Index, List) ->
    {Left, [_|Right]} = lists:split(Index - 1, List),
    Left ++ Right.

factor_score([]) -> 0;
factor_score(L) ->
    G = gcd_list(L),
    Lc = lcm_list(L),
    G * Lc.

gcd_list([H|T]) ->
    lists:foldl(fun gcd/2, H, T).

lcm_list([H|T]) ->
    lists:foldl(fun lcm/2, H, T).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

lcm(A, B) ->
    (A div gcd(A, B)) * B.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(nums :: [integer]) :: integer
  def max_score(nums) do
    n = length(nums)

    compute = fn list ->
      Enum.reduce(list, {0, 1}, fn x, {g, l} ->
        new_g = if g == 0, do: x, else: Integer.gcd(g, x)
        new_l = lcm(l, x)
        {new_g, new_l}
      end)
    end

    initial_score =
      case compute.(nums) do
        {g, l} -> g * l
      end

    Enum.reduce(0..(n - 1), initial_score, fn i, acc ->
      remaining = List.delete_at(nums, i)

      score =
        if remaining == [] do
          0
        else
          {g, l} = compute.(remaining)
          g * l
        end

      if score > acc, do: score, else: acc
    end)
  end

  defp lcm(a, b) do
    div(a * b, Integer.gcd(a, b))
  end
end
```
