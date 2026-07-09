# 1680. Concatenation of Consecutive Binary Numbers

## Cpp

```cpp
class Solution {
public:
    int concatenatedBinary(int n) {
        const int MOD = 1'000'000'007;
        // Precompute powers of two up to 31 bits (enough for n <= 1e5)
        long long pow2[32];
        pow2[0] = 1;
        for (int i = 1; i < 32; ++i) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long long ans = 0;
        for (int i = 1; i <= n; ++i) {
            int bits = 32 - __builtin_clz(i); // number of bits in i
            ans = (ans * pow2[bits] + i) % MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int concatenatedBinary(int n) {
        long result = 0;
        int bits = 0;
        int nextPowerOfTwo = 1; // 2^bits
        for (int i = 1; i <= n; i++) {
            if (i == nextPowerOfTwo) {
                bits++;
                nextPowerOfTwo <<= 1;
            }
            result = ((result << bits) + i) % MOD;
        }
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        bits = 0
        next_pow = 1
        for i in range(1, n + 1):
            if i == next_pow:
                bits += 1
                next_pow <<= 1
            ans = ((ans << bits) | i) % MOD
        return ans
```

## Python3

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        bit_len = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:  # i is a power of two
                bit_len += 1
            result = ((result << bit_len) | i) % MOD
        return result
```

## C

```c
int concatenatedBinary(int n){
    const int MOD = 1000000007;
    long long ans = 0;
    int bits = 0;
    for (int i = 1; i <= n; ++i) {
        if ((i & (i - 1)) == 0) ++bits;          // increase bit length at powers of two
        ans = ((ans << bits) + i) % MOD;         // shift left by current bit length and add i
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int ConcatenatedBinary(int n) {
        long[] pow2 = new long[32];
        pow2[0] = 1;
        for (int i = 1; i < pow2.Length; i++) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long ans = 0;
        int bits = 0;
        for (int i = 1; i <= n; i++) {
            if ((i & (i - 1)) == 0) { // i is a power of two
                bits++;
            }
            ans = (ans * pow2[bits] + i) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
var concatenatedBinary = function(n) {
    const MOD = 1000000007;
    let ans = 0;
    let len = 0;
    for (let i = 1; i <= n; ++i) {
        if ((i & (i - 1)) === 0) {
            len++;
        }
        ans = (ans * (1 << len) + i) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function concatenatedBinary(n: number): number {
    const MOD = 1_000_000_007;
    let ans = 0;
    let bits = 0;
    for (let i = 1; i <= n; i++) {
        if ((i & (i - 1)) === 0) bits++; // i is a power of two
        ans = (ans * (1 << bits) + i) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function concatenatedBinary($n) {
        $mod = 1000000007;
        $ans = 0;
        $bits = 0;
        for ($i = 1; $i <= $n; $i++) {
            if (($i & ($i - 1)) == 0) {
                $bits++;
            }
            $ans = ((($ans << $bits) % $mod) + $i) % $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func concatenatedBinary(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var result: Int64 = 0
        var bits = 0
        for i in 1...n {
            if (i & (i - 1)) == 0 { // power of two, increase bit length
                bits += 1
            }
            result = ((result << bits) % Int64(MOD) + Int64(i)) % Int64(MOD)
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun concatenatedBinary(n: Int): Int {
        val MOD = 1_000_000_007L
        var ans = 0L
        for (i in 1..n) {
            val len = 32 - Integer.numberOfLeadingZeros(i)
            ans = ((ans * (1L shl len)) % MOD + i) % MOD
        }
        return ans.toInt()
    }
}
```

## Golang

```go
package main

import "math/bits"

func concatenatedBinary(n int) int {
	const MOD = 1000000007
	ans := 0
	for i := 1; i <= n; i++ {
		l := bits.Len(uint(i))
		ans = ((ans << uint(l)) % MOD + i) % MOD
	}
	return ans
}
```

## Ruby

```ruby
def concatenated_binary(n)
  mod = 1_000_000_007
  ans = 0
  bits = 0
  i = 1
  while i <= n
    bits += 1 if (i & (i - 1)).zero?
    ans = ((ans << bits) % mod + i) % mod
    i += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def concatenatedBinary(n: Int): Int = {
        val MOD = 1000000007L
        var ans = 0L
        var bits = 0
        for (i <- 1 to n) {
            if ((i & (i - 1)) == 0) bits += 1
            ans = ((ans << bits) % MOD + i) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn concatenated_binary(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut result: i64 = 0;
        let mut bits: i64 = 0;
        let mut next_pow: i64 = 1; // next power of two
        
        for i in 1..=n as i64 {
            if i == next_pow {
                bits += 1;
                next_pow <<= 1;
            }
            result = ((result << bits) % MOD + i) % MOD;
        }
        result as i32
    }
}
```
