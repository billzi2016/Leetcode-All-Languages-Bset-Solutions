# 2954. Count the Number of Infection Sequences

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modpow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    int numberOfSequence(int n, vector<int>& sick) {
        int m = sick.size();
        // factorials up to n
        vector<long long> fact(n + 1), invFact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modpow(fact[n], MOD - 2);
        for (int i = n; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        int totalUninfected = n - m;
        long long ans = fact[totalUninfected];
        long long extraPow = 0;
        
        // left gap
        if (sick[0] > 0) {
            int len = sick[0];
            ans = ans * invFact[len] % MOD;
        }
        // internal gaps
        for (int i = 1; i < m; ++i) {
            int len = sick[i] - sick[i - 1] - 1;
            if (len > 0) {
                ans = ans * invFact[len] % MOD;
                extraPow += (len - 1);
            }
        }
        // right gap
        int rightLen = n - 1 - sick.back();
        if (rightLen > 0) {
            ans = ans * invFact[rightLen] % MOD;
        }
        
        ans = ans * modpow(2, extraPow) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int numberOfSequence(int n, int[] sick) {
        int m = sick.length;
        // factorials up to n
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i >= 1; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }

        int startGap = sick[0];
        int endGap = n - 1 - sick[m - 1];
        long total = startGap + endGap;

        java.util.List<Integer> internal = new java.util.ArrayList<>();
        for (int i = 0; i < m - 1; i++) {
            int gap = sick[i + 1] - sick[i] - 1;
            if (gap > 0) {
                internal.add(gap);
                total += gap;
            }
        }

        long ans = fact[(int) total];
        ans = ans * invFact[startGap] % MOD;
        ans = ans * invFact[endGap] % MOD;

        long extraPow = 0;
        for (int len : internal) {
            ans = ans * invFact[len] % MOD;
            extraPow += len - 1;
        }
        if (extraPow > 0) {
            ans = ans * modPow(2, extraPow) % MOD;
        }

        return (int) ans;
    }

    private long modPow(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = res * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSequence(self, n, sick):
        """
        :type n: int
        :type sick: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        # precompute factorials and inverse factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        start_len = sick[0]                     # gap before first infected
        end_len = n - 1 - sick[-1]              # gap after last infected
        internal_gaps = []
        for i in range(1, len(sick)):
            gap = sick[i] - sick[i - 1] - 1
            if gap > 0:
                internal_gaps.append(gap)

        total_uninfected = start_len + end_len + sum(internal_gaps)

        ans = fact[total_uninfected]
        ans = ans * inv_fact[start_len] % MOD
        ans = ans * inv_fact[end_len] % MOD
        for L in internal_gaps:
            ans = ans * inv_fact[L] % MOD
            ans = ans * pow(2, L - 1, MOD) % MOD

        return ans
```

## Python3

```python
class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(sick)
        total_uninfected = n - m

        # factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        ans = fact[total_uninfected]

        # left edge segment
        left_len = sick[0]
        ans = ans * inv_fact[left_len] % MOD

        # right edge segment
        right_len = n - 1 - sick[-1]
        ans = ans * inv_fact[right_len] % MOD

        # internal segments
        for i in range(m - 1):
            gap = sick[i + 1] - sick[i] - 1
            if gap:
                ans = ans * inv_fact[gap] % MOD
                ans = ans * pow(2, gap - 1, MOD) % MOD

        return ans
```

## C

```c
#include <stdlib.h>

static const int MOD = 1000000007;

static long long modpow(long long a, long long e) {
    long long res = 1;
    a %= MOD;
    while (e > 0) {
        if (e & 1) res = res * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return res;
}

int numberOfSequence(int n, int* sick, int sickSize) {
    int maxN = n;
    long long *fact = (long long *)malloc((maxN + 1) * sizeof(long long));
    long long *invFact = (long long *)malloc((maxN + 1) * sizeof(long long));
    if (!fact || !invFact) return 0; // safety

    fact[0] = 1;
    for (int i = 1; i <= maxN; ++i)
        fact[i] = fact[i - 1] * i % MOD;

    invFact[maxN] = modpow(fact[maxN], MOD - 2);
    for (int i = maxN; i > 0; --i)
        invFact[i - 1] = invFact[i] * i % MOD;

    int len_start = sick[0];
    int len_end = n - 1 - sick[sickSize - 1];

    int total_uninfected = len_start + len_end;
    for (int i = 0; i < sickSize - 1; ++i) {
        int gap = sick[i + 1] - sick[i] - 1;
        if (gap > 0) total_uninfected += gap;
    }

    long long ans = fact[total_uninfected];
    ans = ans * invFact[len_start] % MOD;
    ans = ans * invFact[len_end] % MOD;

    for (int i = 0; i < sickSize - 1; ++i) {
        int gap = sick[i + 1] - sick[i] - 1;
        if (gap > 0) {
            ans = ans * invFact[gap] % MOD;
            ans = ans * modpow(2, gap - 1) % MOD;
        }
    }

    free(fact);
    free(invFact);
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const long MOD = 1000000007L;
    
    private static long ModPow(long a, long e) {
        long res = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) == 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            e >>= 1;
        }
        return res;
    }
    
    public int NumberOfSequence(int n, int[] sick) {
        int m = sick.Length;
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n; i >= 1; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
        
        int totalUninfected = n - m;
        long ans = fact[totalUninfected];
        
        // start gap
        int startGap = sick[0];
        ans = ans * invFact[startGap] % MOD;
        
        // end gap
        int endGap = n - 1 - sick[m - 1];
        ans = ans * invFact[endGap] % MOD;
        
        // internal gaps
        for (int i = 1; i < m; i++) {
            int len = sick[i] - sick[i - 1] - 1;
            if (len <= 0) continue;
            ans = ans * invFact[len] % MOD;
            ans = ans * ModPow(2, len - 1) % MOD;
        }
        
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} sick
 * @return {number}
 */
var numberOfSequence = function(n, sick) {
    const MOD = 1000000007n;
    
    // fast power (base BigInt, exp Number)
    function modPow(base, exp) {
        let result = 1n;
        let b = base % MOD;
        while (exp > 0) {
            if (exp & 1) result = (result * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return result;
    }
    
    // precompute factorials and inverse factorials up to n
    const fact = new Array(n + 1);
    const invFact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    // Fermat inverse of fact[n]
    invFact[n] = modPow(fact[n], 1000000005); // MOD-2
    for (let i = n; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    
    const totalUninfected = n - sick.length;
    let ans = fact[totalUninfected];
    
    // helper to multiply by inverse factorial of a segment length
    function applyInvFact(len) {
        if (len > 0) {
            ans = (ans * invFact[len]) % MOD;
        }
    }
    
    // start segment (left edge)
    const startLen = sick[0];
    applyInvFact(startLen);
    
    // end segment (right edge)
    const endLen = n - 1 - sick[sick.length - 1];
    applyInvFact(endLen);
    
    // middle segments
    for (let i = 1; i < sick.length; ++i) {
        const gap = sick[i] - sick[i - 1] - 1;
        if (gap > 0) {
            applyInvFact(gap);
            ans = (ans * modPow(2n, gap - 1)) % MOD;
        }
    }
    
    return Number(ans);
};
```

## Typescript

```typescript
function numberOfSequence(n: number, sick: number[]): number {
    const MOD = 1000000007n;

    // fast power with bigint exponent
    const modPow = (base: bigint, exp: bigint): bigint => {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if ((e & 1n) === 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };

    // precompute factorials and inverse factorials up to n
    const fact: bigint[] = new Array(n + 1);
    const invFact: bigint[] = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * BigInt(i + 1)) % MOD;
    }

    const totalUninfected = n - sick.length;
    let ans = fact[totalUninfected];

    // process gaps between infected positions
    let prev = -1;
    for (const pos of sick) {
        const gap = pos - prev - 1; // number of healthy people in this segment
        if (gap > 0) {
            ans = (ans * invFact[gap]) % MOD;
            if (prev !== -1) { // internal gap, both sides have infected persons
                ans = (ans * modPow(2n, BigInt(gap - 1))) % MOD;
            }
        }
        prev = pos;
    }

    // handle the trailing gap after the last infected person
    const endGap = n - 1 - sick[sick.length - 1];
    if (endGap > 0) {
        ans = (ans * invFact[endGap]) % MOD;
    }

    return Number(ans);
}
```

## Php

```php
<?php
class Solution {

    const MOD = 1000000007;

    /**
     * @param Integer $n
     * @param Integer[] $sick
     * @return Integer
     */
    function numberOfSequence($n, $sick) {
        $m = count($sick);
        // total uninfected people
        $S = $n - $m;

        // precompute factorials up to S
        $fact = array_fill(0, $S + 1, 1);
        for ($i = 1; $i <= $S; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % self::MOD;
        }
        // precompute inverse factorials
        $invFact = array_fill(0, $S + 1, 1);
        $invFact[$S] = $this->modPow($fact[$S], self::MOD - 2);
        for ($i = $S; $i > 0; $i--) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % self::MOD;
        }

        // lengths of segments
        $segments = [];

        // start segment
        $startLen = $sick[0];
        if ($startLen > 0) {
            $segments[] = $startLen;
        }

        // internal segments
        $k = 0; // exponent for power of 2
        for ($i = 0; $i < $m - 1; $i++) {
            $len = $sick[$i + 1] - $sick[$i] - 1;
            if ($len > 0) {
                $segments[] = $len;
                $k += $len - 1;
            }
        }

        // end segment
        $endLen = $n - 1 - $sick[$m - 1];
        if ($endLen > 0) {
            $segments[] = $endLen;
        }

        // multinomial coefficient part
        $ans = $fact[$S];
        foreach ($segments as $len) {
            $ans = ($ans * $invFact[$len]) % self::MOD;
        }

        // multiply by 2^k for internal segments
        if ($k > 0) {
            $ans = ($ans * $this->modPow(2, $k)) % self::MOD;
        }

        return $ans;
    }

    private function modPow($base, $exp) {
        $mod = self::MOD;
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func numberOfSequence(_ n: Int, _ sick: [Int]) -> Int {
        let totalUninfected = n - sick.count
        var fact = [Int](repeating: 0, count: n + 1)
        var invFact = [Int](repeating: 0, count: n + 1)

        fact[0] = 1
        if n > 0 {
            for i in 1...n {
                fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(MOD))
            }
        }

        func modPow(_ base: Int, _ exp: Int) -> Int {
            var result: Int64 = 1
            var b: Int64 = Int64(base)
            var e = exp
            let m = Int64(MOD)
            while e > 0 {
                if e & 1 == 1 {
                    result = (result * b) % m
                }
                b = (b * b) % m
                e >>= 1
            }
            return Int(result)
        }

        invFact[n] = modPow(fact[n], MOD - 2)
        if n > 0 {
            for i in stride(from: n, to: 0, by: -1) {
                invFact[i - 1] = Int((Int64(invFact[i]) * Int64(i)) % Int64(MOD))
            }
        }

        var ans = fact[totalUninfected]

        // leading gap
        let leftGap = sick.first!
        if leftGap > 0 {
            ans = Int((Int64(ans) * Int64(invFact[leftGap])) % Int64(MOD))
        }

        // internal gaps
        for i in 0..<(sick.count - 1) {
            let gap = sick[i + 1] - sick[i] - 1
            if gap > 0 {
                ans = Int((Int64(ans) * Int64(invFact[gap])) % Int64(MOD))
                // multiply by 2^{gap-1}
                let pow2 = modPow(2, gap - 1)
                ans = Int((Int64(ans) * Int64(pow2)) % Int64(MOD))
            }
        }

        // trailing gap
        let rightGap = n - 1 - sick.last!
        if rightGap > 0 {
            ans = Int((Int64(ans) * Int64(invFact[rightGap])) % Int64(MOD))
        }

        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) res = res * b % MOD
            b = b * b % MOD
            e = e shr 1
        }
        return res
    }

    fun numberOfSequence(n: Int, sick: IntArray): Int {
        val max = n
        val fact = LongArray(max + 1)
        val invFact = LongArray(max + 1)
        val pow2 = LongArray(max + 1)

        fact[0] = 1L
        for (i in 1..max) fact[i] = fact[i - 1] * i % MOD

        invFact[max] = modPow(fact[max], MOD - 2)
        for (i in max - 1 downTo 0) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD
        }

        pow2[0] = 1L
        for (i in 1..max) pow2[i] = (pow2[i - 1] * 2) % MOD

        var totalUninfected = 0
        val internalLengths = mutableListOf<Int>()

        // left edge segment
        val leftLen = if (sick[0] > 0) sick[0] else 0
        if (leftLen > 0) totalUninfected += leftLen

        // right edge segment
        val rightLen = if (sick[sick.size - 1] < n - 1) n - 1 - sick[sick.size - 1] else 0
        if (rightLen > 0) totalUninfected += rightLen

        // internal segments
        for (i in 0 until sick.size - 1) {
            val gap = sick[i + 1] - sick[i] - 1
            if (gap > 0) {
                internalLengths.add(gap)
                totalUninfected += gap
            }
        }

        var ans = fact[totalUninfected]

        if (leftLen > 0) ans = ans * invFact[leftLen] % MOD
        if (rightLen > 0) ans = ans * invFact[rightLen] % MOD
        for (len in internalLengths) {
            ans = ans * invFact[len] % MOD
            ans = ans * pow2[len - 1] % MOD
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int numberOfSequence(int n, List<int> sick) {
    int m = sick.length;
    int totalUninfected = n - m;

    // Precompute factorials and inverse factorials up to n
    List<int> fact = List.filled(n + 1, 0);
    List<int> invFact = List.filled(n + 1, 0);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) {
      fact[i] = (fact[i - 1] * i) % _MOD;
    }
    invFact[n] = _modPow(fact[n], _MOD - 2);
    for (int i = n; i >= 1; --i) {
      invFact[i - 1] = (invFact[i] * i) % _MOD;
    }

    // Precompute powers of 2 up to n
    List<int> pow2 = List.filled(n + 1, 0);
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pow2[i] = (pow2[i - 1] * 2) % _MOD;
    }

    int ans = fact[totalUninfected];

    // Start segment
    int startLen = sick[0];
    ans = (ans * invFact[startLen]) % _MOD;

    // End segment
    int endLen = n - 1 - sick[m - 1];
    ans = (ans * invFact[endLen]) % _MOD;

    // Internal segments
    for (int i = 0; i < m - 1; ++i) {
      int len = sick[i + 1] - sick[i] - 1;
      if (len > 0) {
        ans = (ans * invFact[len]) % _MOD;
        ans = (ans * pow2[len - 1]) % _MOD;
      }
    }

    return ans;
  }

  int _modPow(int base, int exp) {
    long result = 1;
    long b = base % _MOD;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _MOD;
      }
      b = (b * b) % _MOD;
      exp >>= 1;
    }
    return result.toInt();
  }
}
```

## Golang

```go
package main

import (
	"math"
)

const MOD int64 = 1000000007

func modPow(a, e int64) int64 {
	res := int64(1)
	a %= MOD
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		e >>= 1
	}
	return res
}

func numberOfSequence(n int, sick []int) int {
	// precompute factorials up to n
	fact := make([]int64, n+1)
	invFact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[n] = modPow(fact[n], MOD-2)
	for i := n; i >= 1; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	totalUninfected := 0
	exponent := int64(0)

	// start gap
	if sick[0] > 0 {
		gap := sick[0]
		totalUninfected += gap
	}
	// interior gaps
	for i := 0; i < len(sick)-1; i++ {
		gap := sick[i+1] - sick[i] - 1
		if gap > 0 {
			totalUninfected += gap
			exponent = (exponent + int64(gap-1)) % (MOD - 1) // exponent modulo MOD-1 not strictly needed but safe
		}
	}
	// end gap
	lastGap := n - 1 - sick[len(sick)-1]
	if lastGap > 0 {
		totalUninfected += lastGap
	}

	// compute multinomial coefficient: totalUninfected! / product gaps!
	ans := fact[totalUninfected]
	// start gap factor
	if sick[0] > 0 {
		gap := sick[0]
		ans = ans * invFact[gap] % MOD
	}
	// interior gaps factors
	for i := 0; i < len(sick)-1; i++ {
		gap := sick[i+1] - sick[i] - 1
		if gap > 0 {
			ans = ans * invFact[gap] % MOD
		}
	}
	// end gap factor
	if lastGap > 0 {
		ans = ans * invFact[lastGap] % MOD
	}

	// multiply by 2^{sum(gap-1)} for interior gaps
	ans = ans * modPow(2, exponent) % MOD

	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  mod = MOD
  res = 1
  a %= mod
  while e > 0
    res = res * a % mod if (e & 1) == 1
    a = a * a % mod
    e >>= 1
  end
  res
end

def number_of_sequence(n, sick)
  # precompute factorials up to n
  fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact = Array.new(n + 1, 1)
  inv_fact[n] = mod_pow(fact[n], MOD - 2)
  n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % MOD }

  len_start = sick[0]
  len_end   = n - 1 - sick[-1]

  internal_lengths = []
  k = 0
  (1...sick.length).each do |i|
    gap = sick[i] - sick[i - 1] - 1
    if gap > 0
      internal_lengths << gap
      k += gap - 1
    end
  end

  total_uninfected = len_start + len_end + internal_lengths.inject(0, :+)

  ans = fact[total_uninfected]
  ans = ans * inv_fact[len_start] % MOD
  ans = ans * inv_fact[len_end] % MOD
  internal_lengths.each do |l|
    ans = ans * inv_fact[l] % MOD
  end

  ans = ans * mod_pow(2, k) % MOD
  ans
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

  private def modPow(base: Long, exp: Long): Long = {
    var b = base % MOD
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1L) == 1L) res = (res * b) % MOD
      b = (b * b) % MOD
      e >>= 1
    }
    res
  }

  def numberOfSequence(n: Int, sick: Array[Int]): Int = {
    // factorials and inverse factorials up to n
    val fact = new Array[Long](n + 1)
    val invFact = new Array[Long](n + 1)
    fact(0) = 1L
    var i = 1
    while (i <= n) {
      fact(i) = (fact(i - 1) * i) % MOD
      i += 1
    }
    invFact(n) = modPow(fact(n), MOD - 2)
    i = n
    while (i > 0) {
      invFact(i - 1) = (invFact(i) * i) % MOD
      i -= 1
    }

    val startLen = sick(0)
    val endLen = n - 1 - sick(sick.length - 1)
    val totalUninfected = n - sick.length

    var ans = fact(totalUninfected)

    // divide by factorials of the edge segments
    ans = (ans * invFact(startLen)) % MOD
    ans = (ans * invFact(endLen)) % MOD

    var pow2Exp = 0L
    i = 0
    while (i < sick.length - 1) {
      val len = sick(i + 1) - sick(i) - 1
      if (len > 0) {
        ans = (ans * invFact(len)) % MOD
        pow2Exp += (len - 1).toLong
      }
      i += 1
    }

    // multiply by 2^{pow2Exp}
    ans = (ans * modPow(2L, pow2Exp)) % MOD

    ans.toInt
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res = 1i64;
    while exp > 0 {
        if exp & 1 == 1 {
            res = res * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    res
}

impl Solution {
    pub fn number_of_sequence(n: i32, sick: Vec<i32>) -> i32 {
        let n_usize = n as usize;
        let m = sick.len();
        // precompute factorials up to n
        let mut fact = vec![1i64; n_usize + 1];
        for i in 1..=n_usize {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![1i64; n_usize + 1];
        inv_fact[n_usize] = mod_pow(fact[n_usize], MOD - 2);
        for i in (0..n_usize).rev() {
            inv_fact[i] = inv_fact[i + 1] * ((i + 1) as i64) % MOD;
        }

        let total_uninfected = n_usize - m;
        let mut ans = fact[total_uninfected];

        // start gap
        if let Some(&first) = sick.first() {
            let len_start = first as usize;
            if len_start > 0 {
                ans = ans * inv_fact[len_start] % MOD;
            }
        }

        // end gap
        if let Some(&last) = sick.last() {
            let len_end = (n - 1 - last) as usize;
            if len_end > 0 {
                ans = ans * inv_fact[len_end] % MOD;
            }
        }

        // internal gaps
        for i in 0..m.saturating_sub(1) {
            let left = sick[i];
            let right = sick[i + 1];
            let len = (right - left - 1) as usize;
            if len > 0 {
                ans = ans * inv_fact[len] % MOD;
                // multiply by 2^{len-1}
                let pow = mod_pow(2, (len - 1) as i64);
                ans = ans * pow % MOD;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; fast modular exponentiation
(define (modpow base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (let* ((res (if (odd? e) (modulo (* res b) MOD) res))
               (b   (modulo (* b b) MOD)))
          (loop b (quotient e 2) res)))))

;; precompute factorials and inverse factorials up to limit
(define (precompute-factorials limit)
  (let* ((fact (make-vector (+ limit 1) 0))
         (invf (make-vector (+ limit 1) 0)))
    (vector-set! fact 0 1)
    (for ([i (in-range 1 (add1 limit))])
      (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
    (vector-set! invf limit (modpow (vector-ref fact limit) (- MOD 2)))
    (for ([i (in-range limit 0 -1)])
      (when (> i 0)
        (vector-set! invf (- i 1)
                     (modulo (* (vector-ref invf i) i) MOD))))
    (values fact invf)))

(define/contract (number-of-sequence n sick)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((start-len (car sick))                     ; length before first infected
         ;; collect internal segment lengths and keep last infected position
         (internal-data
          (for/fold ([prev (car sick)]
                     [lens '()]
                     ) ([cur (cdr sick)])
            (let ((gap (- cur prev 1)))
              (if (> gap 0)
                  (values cur (cons gap lens))
                  (values cur lens)))))
         (last-infected (car (reverse sick)))       ; last infected position
         (end-len (if (= last-infected (- n 1))
                      0
                      (- n 1 last-infected)))
         (internal-lens (reverse (second internal-data))) ; restore original order
         (all-lengths (append (list start-len) internal-lens (list end-len)))
         (total-uninfected (apply + all-lengths))
         (k (apply + (map (lambda (len) (- len 1)) internal-lens))))
    ;; precompute factorials up to n
    (define-values (fact invf) (precompute-factorials n))
    ;; multinomial coefficient: total! / prod(len!)
    (let ((res (vector-ref fact total-uninfected)))
      (for ([len all-lengths])
        (set! res (modulo (* res (vector-ref invf len)) MOD)))
      ;; multiply by 2^k for internal segments
      (set! res (modulo (* res (modpow 2 k)) MOD))
      res)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_sequence/2]).

-define(MOD, 1000000007).

-spec number_of_sequence(N :: integer(), Sick :: [integer()]) -> integer().
number_of_sequence(N, Sick) ->
    Mod = ?MOD,
    FactTuple = precompute_fact(N, Mod),
    TotalUninfected = N - length(Sick),

    Ans0 = fact(TotalUninfected, FactTuple),

    % gaps at the ends
    LenStart = case Sick of
        [] -> N;
        [First|_] -> First
    end,
    LenEnd = N - 1 - lists:last(Sick),

    InternalGaps = get_internal_gaps(Sick, []),

    GapsAll = [LenStart | (InternalGaps ++ [LenEnd])],

    Ans1 = apply_factorial_inverses(Ans0, GapsAll, FactTuple, Mod),

    % multiply by 2^{gap-1} for each internal gap
    AnsFinal = lists:foldl(fun(Gap, Acc) ->
        case Gap > 0 of
            true -> (Acc * mod_pow(2, Gap - 1, Mod)) rem Mod;
            false -> Acc
        end
    end, Ans1, InternalGaps),

    AnsFinal.

%% Precompute factorials up to N, stored in a tuple where element(I+1) = I!
-spec precompute_fact(N :: integer(), Mod :: integer()) -> tuple().
precompute_fact(N, Mod) ->
    FactList = build_fact(0, 1, [], N, Mod),
    list_to_tuple(FactList).

%% Build factorial list [0!,1!,...,N!]
-spec build_fact(I :: integer(), Cur :: integer(), Acc :: [integer()], N :: integer(), Mod :: integer()) -> [integer()].
build_fact(I, Cur, Acc, N, Mod) when I =< N ->
    NewAcc = [Cur | Acc],
    NextCur = (Cur * (I + 1)) rem Mod,
    build_fact(I + 1, NextCur, NewAcc, N, Mod);
build_fact(_, _, Acc, _, _) ->
    lists:reverse(Acc).

%% Retrieve factorial I! from tuple
-spec fact(I :: integer(), FactTuple :: tuple()) -> integer().
fact(I, FactTuple) ->
    element(I + 1, FactTuple).

%% Apply division by each gap's factorial using modular inverses
-spec apply_factorial_inverses(Ans :: integer(), Gaps :: [integer()], FactTuple :: tuple(), Mod :: integer()) -> integer().
apply_factorial_inverses(Ans, [], _, _) ->
    Ans;
apply_factorial_inverses(Ans, [G|Rest], FactTuple, Mod) ->
    Inv = mod_pow(fact(G, FactTuple), Mod - 2, Mod),
    NewAns = (Ans * Inv) rem Mod,
    apply_factorial_inverses(NewAns, Rest, FactTuple, Mod).

%% Extract internal gaps lengths (between two sick positions)
-spec get_internal_gaps(Sick :: [integer()], Acc :: [integer()]) -> [integer()].
get_internal_gaps([Prev, Curr | Rest], Acc) ->
    Gap = Curr - Prev - 1,
    NewAcc = case Gap > 0 of
        true -> [Gap | Acc];
        false -> Acc
    end,
    get_internal_gaps([Curr | Rest], NewAcc);
get_internal_gaps(_, Acc) ->
    lists:reverse(Acc).

%% Fast modular exponentiation
-spec mod_pow(Base :: integer(), Exp :: integer(), Mod :: integer()) -> integer().
mod_pow(_Base, 0, _Mod) ->
    1;
mod_pow(Base, Exp, Mod) when Exp band 1 =:= 1 ->
    (Base * mod_pow((Base * Base) rem Mod, Exp bsr 1, Mod)) rem Mod;
mod_pow(Base, Exp, Mod) ->
    mod_pow((Base * Base) rem Mod, Exp bsr 1, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec number_of_sequence(n :: integer, sick :: [integer]) :: integer
  def number_of_sequence(n, sick) do
    mod = 1_000_000_007

    # factorials up to n
    fact_list =
      Enum.scan(0..n, 1, fn i, acc ->
        if i == 0 do
          1
        else
          rem(acc * i, mod)
        end
      end)

    fact = List.to_tuple(fact_list)

    # inverse factorials
    inv_fact_n = pow_mod(elem(fact, n), mod - 2, mod)

    inv_fact_list =
      Enum.reduce((n - 1)..0, [inv_fact_n], fn i, acc ->
        next = rem(hd(acc) * (i + 1), mod)
        [next | acc]
      end)

    inv_fact = List.to_tuple(inv_fact_list)

    total_uninfected = n - length(sick)
    res_initial = elem(fact, total_uninfected)

    start_len = hd(sick)
    end_len = n - 1 - List.last(sick)

    res =
      rem(res_initial * elem(inv_fact, start_len), mod)
      |> rem(elem(inv_fact, end_len))

    {res_after_internal, exponent} = process_internal(sick, inv_fact, res, 0, mod)

    final_res = rem(res_after_internal * pow_mod(2, exponent, mod), mod)
    final_res
  end

  defp process_internal([], _inv_fact, res, exp, _mod), do: {res, exp}
  defp process_internal([_], _inv_fact, res, exp, _mod), do: {res, exp}

  defp process_internal([a, b | rest], inv_fact, res, exp, mod) do
    gap = b - a - 1

    if gap > 0 do
      new_res = rem(res * elem(inv_fact, gap), mod)
      new_exp = exp + gap - 1
      process_internal([b | rest], inv_fact, new_res, new_exp, mod)
    else
      process_internal([b | rest], inv_fact, res, exp, mod)
    end
  end

  defp pow_mod(_a, 0, _mod), do: 1

  defp pow_mod(a, b, mod) when rem(b, 2) == 0 do
    half = pow_mod(a, div(b, 2), mod)
    rem(half * half, mod)
  end

  defp pow_mod(a, b, mod) do
    rem(a * pow_mod(a, b - 1, mod), mod)
  end
end
```
