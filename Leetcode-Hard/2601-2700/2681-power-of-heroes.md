# 2681. Power of Heroes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sumOfPower(vector<int>& nums) {
        const long long MOD = 1000000007LL;
        vector<long long> a(nums.begin(), nums.end());
        sort(a.begin(), a.end());
        long long dp = 0; // Σ_{i=0}^{j-1} a[i] * 2^{j-1-i}
        long long ans = 0;
        for (long long x : a) {
            long long term = ((dp + x) % MOD) * (x % MOD) % MOD * (x % MOD) % MOD;
            ans += term;
            if (ans >= MOD) ans -= MOD;
            dp = (x + 2LL * dp) % MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int sumOfPower(int[] nums) {
        final long MOD = 1_000_000_007L;
        Arrays.sort(nums);
        long ans = 0;
        long dp = 0; // sum_{i=0}^{j-1} nums[i] * 2^{(j-1)-i}
        for (int j = 0; j < nums.length; ++j) {
            long val = nums[j];
            long sq = (val * val) % MOD;
            long cube = (sq * val) % MOD;
            ans = (ans + cube) % MOD;
            if (j > 0) {
                ans = (ans + (sq * dp) % MOD) % MOD;
            }
            dp = (val + (2L * dp) % MOD) % MOD; // update for next index
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfPower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] << 1) % MOD

        inv2 = (MOD + 1) // 2
        invpow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            invpow2[i] = invpow2[i - 1] * inv2 % MOD

        pref = 0          # Σ a[i] * invpow2[i]
        ans = 0
        for j, val in enumerate(nums):
            a = val % MOD
            term = (pow2[j - 1] * pref) % MOD if j > 0 else 0
            contrib = (a * a) % MOD
            contrib = contrib * ((term + a) % MOD) % MOD
            ans = (ans + contrib) % MOD
            pref = (pref + a * invpow2[j]) % MOD

        return ans
```

## Python3

```python
class Solution:
    def sumOfPower(self, nums):
        MOD = 10**9 + 7
        nums.sort()
        ans = 0
        cur = 0  # Σ_{i<j} a[i] * 2^{j-i-1}
        for v in nums:
            v_mod = v % MOD
            ans = (ans + (v_mod * v_mod % MOD) * cur) % MOD   # pair contributions where v is max
            ans = (ans + pow(v_mod, 3, MOD)) % MOD           # single-element subset
            cur = (cur * 2 + v_mod) % MOD
        return ans % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int sumOfPower(int* nums, int numsSize) {
    const long long MOD = 1000000007LL;
    vector<long long> a(nums, nums + numsSize);
    sort(a.begin(), a.end());
    long long cur = 0; // Σ_{i<j} a[i] * 2^{j-i-1}
    long long ans = 0;
    for (int j = 0; j < numsSize; ++j) {
        long long val = a[j] % MOD;
        long long sq = (__int128)val * val % MOD;          // a[j]^2 mod MOD
        long long sumMin = (cur + val) % MOD;              // Σ_{i≤j} a[i]*2^{j-i-1}
        long long term = (__int128)sq * sumMin % MOD;     // contribution for this max
        ans += term;
        if (ans >= MOD) ans -= MOD;
        cur = ((cur * 2) % MOD + val) % MOD;               // update for next index
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfPower(int[] nums) {
        const long MOD = 1000000007L;
        Array.Sort(nums);
        int n = nums.Length;
        if (n == 0) return 0;

        long[] pow2 = new long[n];
        long[] invPow2 = new long[n];
        pow2[0] = 1;
        for (int i = 1; i < n; i++) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long inv2 = (MOD + 1) / 2; // modular inverse of 2
        invPow2[0] = 1;
        for (int i = 1; i < n; i++) {
            invPow2[i] = (invPow2[i - 1] * inv2) % MOD;
        }

        long prefInv = 0;
        long ans = 0;

        for (int j = 0; j < n; j++) {
            long aj = nums[j] % MOD;
            long ajSq = (aj * aj) % MOD;

            if (j > 0) {
                long temp = pow2[j - 1];
                long contrib = ajSq * ((temp * prefInv) % MOD) % MOD;
                ans = (ans + contrib) % MOD;
            }

            // contribution of subset containing only this element
            long self = ajSq * aj % MOD; // aj^3
            ans = (ans + self) % MOD;

            // update prefix sum for future calculations
            prefInv = (prefInv + aj * invPow2[j] % MOD) % MOD;
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfPower = function(nums) {
    const MOD = 1000000007n;
    nums.sort((a, b) => a - b);
    let ans = 0n;
    let cur = 0n; // Σ_{i<j} nums[i] * 2^{j-i-1}
    for (const x of nums) {
        const v = BigInt(x);
        const sq = (v * v) % MOD;          // nums[j]^2
        ans = (ans + sq * cur) % MOD;      // contributions with earlier mins
        ans = (ans + sq * v) % MOD;        // single-element subset (nums[i]^3)
        cur = (cur * 2n + v) % MOD;        // update for next index
    }
    return Number(ans);
};
```

## Typescript

```typescript
function sumOfPower(nums: number[]): number {
    const MOD = 1000000007n;
    const arr = nums.map(BigInt);
    arr.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
    let ans = 0n;
    let dp = 0n;
    for (let i = 0; i < arr.length; i++) {
        const x = arr[i] % MOD;
        const x2 = (x * x) % MOD;
        // singleton contribution
        ans = (ans + (x2 * x) % MOD) % MOD;
        // contributions where current element is the maximum and previous elements are minima
        ans = (ans + (x2 * dp) % MOD) % MOD;
        // update dp for next iteration
        dp = (dp * 2n + x) % MOD;
    }
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfPower($nums) {
        $mod = 1000000007;
        sort($nums, SORT_NUMERIC);
        $f = 0;
        $ans = 0;
        foreach ($nums as $val) {
            $valSq = ($val * $val) % $mod;               // val^2
            $ans = ($ans + ($valSq * $val) % $mod) % $mod; // single element contribution (val^3)
            $ans = ($ans + ($valSq * $f) % $mod) % $mod;   // contributions where this is max and earlier min
            $f = ((2 * $f) % $mod + $val) % $mod;          // update prefix sum for next iterations
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfPower(_ nums: [Int]) -> Int {
        let MOD: Int64 = 1_000_000_007
        var a = nums.map { Int64($0) }
        a.sort()
        let n = a.count
        
        var pow2 = [Int64](repeating: 0, count: n + 1)
        pow2[0] = 1
        if n > 0 {
            for i in 1...n {
                pow2[i] = (pow2[i - 1] * 2) % MOD
            }
        }
        
        let inv2: Int64 = (MOD + 1) / 2   // modular inverse of 2
        var invPow2 = [Int64](repeating: 0, count: n + 1)
        invPow2[0] = 1
        if n > 0 {
            for i in 1...n {
                invPow2[i] = (invPow2[i - 1] * inv2) % MOD
            }
        }
        
        var ans: Int64 = 0
        var pref: Int64 = 0   // Σ a_i * invPow2[i]
        
        for j in 0..<n {
            let val = a[j] % MOD
            // singleton contribution: val^3
            let cube = ((val * val) % MOD * val) % MOD
            ans += cube
            if ans >= MOD { ans -= MOD }
            
            if j > 0 {
                let sq = (val * val) % MOD
                var term = (pref * pow2[j - 1]) % MOD
                term = (sq * term) % MOD
                ans += term
                if ans >= MOD { ans -= MOD }
                if ans >= MOD { ans -= MOD } // in case addition exceeds twice MOD
            }
            
            // update prefix for future maxima
            let add = (val * invPow2[j]) % MOD
            pref += add
            if pref >= MOD { pref -= MOD }
        }
        
        return Int(ans % MOD)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfPower(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        val inv2 = 500_000_004L  // modular inverse of 2 modulo MOD
        val n = nums.size
        val arr = nums.map { it.toLong() }.sorted()
        val pow2 = LongArray(n + 1)
        val invPow2 = LongArray(n + 1)
        pow2[0] = 1L
        for (i in 1..n) {
            pow2[i] = (pow2[i - 1] * 2L) % MOD
        }
        invPow2[0] = 1L
        for (i in 1..n) {
            invPow2[i] = (invPow2[i - 1] * inv2) % MOD
        }

        var ans = 0L

        // singleton contributions: v^3
        for (v in arr) {
            val vm = v % MOD
            ans = (ans + ((vm * vm) % MOD) * vm % MOD) % MOD
        }

        var prefixWeighted = 0L  // Σ nums[i] * invPow2[i] for i < current j
        for (j in 0 until n) {
            val vj = arr[j] % MOD
            if (j > 0) {
                val term = (vj * vj) % MOD          // vj^2
                val factor = (pow2[j - 1] * prefixWeighted) % MOD
                ans = (ans + term * factor % MOD) % MOD
            }
            // update prefix for future positions
            prefixWeighted = (prefixWeighted + vj * invPow2[j] % MOD) % MOD
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int sumOfPower(List<int> nums) {
    nums.sort();
    int n = nums.length;
    List<int> pow2 = List.filled(n, 0);
    List<int> invPow2 = List.filled(n, 0);

    pow2[0] = 1;
    for (int i = 1; i < n; ++i) {
      pow2[i] = (pow2[i - 1] * 2) % _mod;
    }

    int inv2 = _modPow(2, _mod - 2);
    invPow2[0] = 1;
    for (int i = 1; i < n; ++i) {
      invPow2[i] = (invPow2[i - 1] * inv2) % _mod;
    }

    int ans = 0;
    int sumInv = 0;

    for (int j = 0; j < n; ++j) {
      int val = nums[j] % _mod;

      // single element contribution: val^3
      int cube = ((val * val) % _mod * val) % _mod;
      ans = (ans + cube) % _mod;

      if (j > 0) {
        int sq = (val * val) % _mod;
        int contrib = sq;
        contrib = (contrib * pow2[j - 1]) % _mod;
        contrib = (contrib * sumInv) % _mod;
        ans = (ans + contrib) % _mod;
      }

      // update prefix sum of nums[i] * invPow2[i]
      int add = (val * invPow2[j]) % _mod;
      sumInv = (sumInv + add) % _mod;
    }

    return ans;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func sumOfPower(nums []int) int {
	const MOD int64 = 1000000007
	sort.Ints(nums)
	var cur int64 = 0
	var ans int64 = 0
	for _, x := range nums {
		val := int64(x) % MOD
		square := (val * val) % MOD
		contrib := (cur * square) % MOD               // subsets where min is before current max
		contrib = (contrib + (square*val)%MOD) % MOD   // singleton subset
		ans = (ans + contrib) % MOD
		cur = (cur*2 + val) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def sum_of_power(nums)
  mod = 1_000_000_007
  nums.sort!
  dp = 0
  ans = 0
  nums.each do |x|
    xm = x % mod
    xsq = (xm * xm) % mod
    term = xsq * ((xm + dp) % mod) % mod
    ans += term
    ans %= mod
    dp = (dp * 2 + xm) % mod
  end
  ans
end
```

## Scala

```scala
object Solution {
    def sumOfPower(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        val sorted = nums.sorted.map(_.toLong)
        var ans = 0L
        var dp = 0L
        for (x <- sorted) {
            val x2 = (x * x) % MOD
            // single element contribution: x^3
            ans = (ans + (x2 * x) % MOD) % MOD
            // contributions where x is the maximum and some previous element is minimum
            ans = (ans + (x2 * dp) % MOD) % MOD
            // update dp for future elements
            dp = (dp * 2 + x) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_power(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut a: Vec<i64> = nums.into_iter().map(|v| v as i64).collect();
        a.sort_unstable();
        let mut cur: i64 = 0;
        let mut ans: i64 = 0;
        for &x in &a {
            let sum_min = (cur + x) % MOD;
            let sq = (x % MOD) * (x % MOD) % MOD;
            ans = (ans + sq * sum_min % MOD) % MOD;
            cur = (2 * cur + x) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (sum-of-power nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (state
          (foldl
           (lambda (x acc)
             (let* ((weighted (car acc))
                    (ans (cadr acc))
                    (xm   (modulo x MOD))
                    (x2   (modulo (* xm xm) MOD))
                    (contrib1 (modulo (* x2 weighted) MOD))      ; max^2 * sum_{i<j} min*2^{...}
                    (contrib2 (modulo (* x2 xm) MOD))           ; max^3 for i=j
                    (new-ans (modulo (+ ans contrib1 contrib2) MOD))
                    (new-weighted (modulo (+ (* 2 weighted) xm) MOD)))
               (list new-weighted new-ans)))
           (list 0 0)
           sorted)))
    (cadr state)))
```

## Erlang

```erlang
-spec sum_of_power(Nums :: [integer()]) -> integer().
sum_of_power(Nums) ->
    Mod = 1000000007,
    Sorted = lists:sort(Nums),
    {Ans, _S} = lists:foldl(
        fun (Val, {Acc, S}) ->
            V = Val rem Mod,
            MaxSq = (V * V) rem Mod,
            Contrib = (MaxSq * S) rem Mod,
            Acc1 = (Acc + Contrib) rem Mod,
            Single = (V * MaxSq) rem Mod,
            Acc2 = (Acc1 + Single) rem Mod,
            SNew = ((S * 2) rem Mod + V) rem Mod,
            {Acc2, SNew}
        end,
        {0, 0},
        Sorted
    ),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_power(nums :: [integer]) :: integer
  def sum_of_power(nums) do
    mod = 1_000_000_007
    sorted = Enum.sort(nums)

    {ans, _} =
      Enum.reduce(sorted, {0, 0}, fn x, {acc, cur} ->
        xm = rem(x, mod)
        x2 = rem(xm * xm, mod)
        pair = rem(x2 * cur, mod)
        single = rem(x2 * xm, mod)   # x^3
        new_acc = rem(acc + pair + single, mod)
        new_cur = rem(cur * 2 + xm, mod)
        {new_acc, new_cur}
      end)

    ans
  end
end
```
