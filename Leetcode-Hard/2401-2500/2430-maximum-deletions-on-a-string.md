# 2430. Maximum Deletions on a String

## Cpp

```cpp
class Solution {
public:
    int deleteString(string s) {
        int n = s.size();
        // lcp[i][j]: longest common prefix of suffixes starting at i and j
        vector<vector<short>> lcp(n + 1, vector<short>(n + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j > i; --j) {
                if (s[i] == s[j]) {
                    lcp[i][j] = (short)(lcp[i + 1][j + 1] + 1);
                }
            }
        }

        vector<int> dp(n + 1, 0); // dp[i]: max ops to delete suffix starting at i
        dp[n] = 0; // empty string needs no operations

        for (int i = n - 1; i >= 0; --i) {
            dp[i] = 1; // delete the whole remaining part in one operation
            int maxLen = (n - i) / 2;
            for (int len = 1; len <= maxLen; ++len) {
                if (lcp[i][i + len] >= len) { // prefix of length len equals next block
                    dp[i] = max(dp[i], 1 + dp[i + len]);
                }
            }
        }

        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public int deleteString(String s) {
        int n = s.length();
        char[] ch = s.toCharArray();
        int[][] lcp = new int[n + 1][n + 1];
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j > i; --j) {
                if (ch[i] == ch[j]) {
                    lcp[i][j] = 1 + lcp[i + 1][j + 1];
                } else {
                    lcp[i][j] = 0;
                }
            }
        }

        int[] dp = new int[n + 1];
        dp[n] = 0; // empty string needs 0 operations
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = 1; // delete the whole suffix in one operation
            // try to delete a prefix of length len if it repeats immediately
            for (int len = 1; i + 2 * len <= n; ++len) {
                if (lcp[i][i + len] >= len) {
                    dp[i] = Math.max(dp[i], 1 + dp[i + len]);
                }
            }
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def deleteString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        MOD = 1000000007
        base = 91138233

        # prefix hashes and powers
        pref = [0] * (n + 1)
        power = [1] * (n + 1)
        for i in range(n):
            pref[i + 1] = (pref[i] * base + (ord(s[i]) - 96)) % MOD
            power[i + 1] = (power[i] * base) % MOD

        def get_hash(l, r):
            """hash of s[l:r]"""
            return (pref[r] - pref[l] * power[r - l]) % MOD

        dp = [0] * (n + 1)
        # dp[n] = 0 already
        for i in range(n - 1, -1, -1):
            best = 1  # delete the whole suffix at once
            max_len = (n - i) // 2
            for length in range(1, max_len + 1):
                if get_hash(i, i + length) == get_hash(i + length, i + 2 * length):
                    cand = 1 + dp[i + length]
                    if cand > best:
                        best = cand
            dp[i] = best

        return dp[0]
```

## Python3

```python
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        # lcp[i][j] = longest common prefix of s[i:] and s[j:]
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            si = s[i]
            row_i = lcp[i]
            row_ip1 = lcp[i + 1]
            for j in range(n - 1, -1, -1):
                if si == s[j]:
                    row_i[j] = row_ip1[j + 1] + 1

        dp = [0] * (n + 1)   # dp[i]: max operations to delete s[i:]
        for i in range(n - 1, -1, -1):
            best = 1                     # delete the whole suffix at once
            max_len = (n - i) // 2
            for length in range(1, max_len + 1):
                if lcp[i][i + length] >= length:
                    cand = 1 + dp[i + length]
                    if cand > best:
                        best = cand
            dp[i] = best
        return dp[0]
```

## C

```c
#include <string.h>
#include <stdlib.h>

int deleteString(char* s) {
    const unsigned long long B = 1315423911ULL;
    int n = strlen(s);
    unsigned long long *h = (unsigned long long*)malloc((n + 1) * sizeof(unsigned long long));
    unsigned long long *p = (unsigned long long*)malloc((n + 1) * sizeof(unsigned long long));
    h[0] = 0;
    p[0] = 1;
    for (int i = 0; i < n; ++i) {
        h[i + 1] = h[i] * B + (unsigned long long)(s[i]);
        p[i + 1] = p[i] * B;
    }
    #define GET_HASH(l, r) (h[(r)] - h[(l)] * p[(r) - (l)])
    
    int *dp = (int*)malloc((n + 1) * sizeof(int));
    dp[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        dp[i] = 1; // delete the whole suffix at once
        for (int L = 1; i + 2 * L <= n; ++L) {
            if (GET_HASH(i, i + L) == GET_HASH(i + L, i + 2 * L)) {
                int cand = 1 + dp[i + L];
                if (cand > dp[i]) dp[i] = cand;
            }
        }
    }
    
    int ans = dp[0];
    free(h);
    free(p);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int DeleteString(string s)
    {
        int n = s.Length;
        const ulong baseVal = 91138233UL;
        ulong[] pow = new ulong[n + 1];
        ulong[] pref = new ulong[n + 1];
        pow[0] = 1;
        for (int i = 1; i <= n; i++)
        {
            pow[i] = unchecked(pow[i - 1] * baseVal);
            pref[i] = unchecked(pref[i - 1] * baseVal + (ulong)(s[i - 1] - 'a' + 1));
        }

        ulong GetHash(int l, int r) // [l, r)
        {
            return unchecked(pref[r] - pref[l] * pow[r - l]);
        }

        int[] dp = new int[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            int best = 1; // delete the whole suffix in one operation
            // try all possible lengths where a repeat exists immediately after
            for (int len = 1; i + len * 2 <= n; len++)
            {
                if (GetHash(i, i + len) == GetHash(i + len, i + 2 * len))
                {
                    int cand = 1 + dp[i + len];
                    if (cand > best) best = cand;
                }
            }
            dp[i] = best;
        }

        return dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var deleteString = function(s) {
    const n = s.length;
    if (n === 0) return 0;

    const MOD = 1000000007n;
    const BASE = 91138233n;

    // precompute powers of base
    const pow = new Array(n + 1);
    pow[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        pow[i] = (pow[i - 1] * BASE) % MOD;
    }

    // prefix hashes, 1-indexed
    const pref = new Array(n + 1);
    pref[0] = 0n;
    for (let i = 0; i < n; ++i) {
        const val = BigInt(s.charCodeAt(i) - 96); // 'a' -> 1, ...
        pref[i + 1] = (pref[i] * BASE + val) % MOD;
    }

    const getHash = (l, r) => { // [l, r)
        let res = (pref[r] - (pref[l] * pow[r - l]) % MOD);
        if (res < 0) res += MOD;
        return res;
    };

    const dp = new Array(n + 1).fill(0);
    dp[n] = 0; // empty suffix needs 0 operations

    for (let i = n - 1; i >= 0; --i) {
        let best = 1; // delete the whole remaining part at once
        const maxLen = Math.floor((n - i) / 2);
        for (let len = 1; len <= maxLen; ++len) {
            if (getHash(i, i + len) === getHash(i + len, i + 2 * len)) {
                const candidate = 1 + dp[i + len];
                if (candidate > best) best = candidate;
            }
        }
        dp[i] = best;
    }

    return dp[0];
};
```

## Typescript

```typescript
function deleteString(s: string): number {
    const n = s.length;
    // lcp[i][j] = longest common prefix of s[i:] and s[j:]
    const lcp: Uint16Array[] = Array.from({ length: n + 1 }, () => new Uint16Array(n + 1));
    for (let i = n - 1; i >= 0; --i) {
        const row = lcp[i];
        const nextRow = lcp[i + 1];
        for (let j = n - 1; j >= 0; --j) {
            if (s.charCodeAt(i) === s.charCodeAt(j)) {
                row[j] = 1 + nextRow[j + 1];
            }
        }
    }

    const dp = new Uint16Array(n + 1); // dp[pos] = max operations to delete suffix starting at pos
    dp[n] = 0;
    for (let i = n - 1; i >= 0; --i) {
        let best = 1; // delete the whole remaining string in one operation
        const maxL = Math.floor((n - i) / 2);
        for (let L = 1; L <= maxL; ++L) {
            if (lcp[i][i + L] >= L) {
                const cand = 1 + dp[i + L];
                if (cand > best) best = cand;
            }
        }
        dp[i] = best;
    }

    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function deleteString($s) {
        $n = strlen($s);
        if ($n == 0) return 0;

        $mod = 1000000007;
        $base = 91138233;

        // prefix hashes and powers
        $hash = array_fill(0, $n + 1, 0);
        $pow  = array_fill(0, $n + 1, 0);
        $pow[0] = 1;
        for ($i = 0; $i < $n; ++$i) {
            $c = ord($s[$i]) - 96; // map 'a'..'z' to 1..26
            $hash[$i + 1] = (int)(($hash[$i] * $base + $c) % $mod);
            $pow[$i + 1]  = (int)(($pow[$i] * $base) % $mod);
        }

        // dp[i]: max operations to delete suffix starting at i
        $dp = array_fill(0, $n + 1, 0);
        $dp[$n] = 0; // empty string needs 0 ops

        for ($i = $n - 1; $i >= 0; --$i) {
            $best = 1; // delete the whole remaining part in one operation
            // try all possible prefix lengths
            for ($len = 1; $i + 2 * $len <= $n; ++$len) {
                // hash of s[i .. i+len-1]
                $h1 = $hash[$i + $len] - (int)(($hash[$i] * $pow[$len]) % $mod);
                if ($h1 < 0) $h1 += $mod;
                // hash of s[i+len .. i+2*len-1]
                $h2 = $hash[$i + 2 * $len] - (int)(($hash[$i + $len] * $pow[$len]) % $mod);
                if ($h2 < 0) $h2 += $mod;

                if ($h1 === $h2) {
                    $candidate = 1 + $dp[$i + $len];
                    if ($candidate > $best) {
                        $best = $candidate;
                    }
                }
            }
            $dp[$i] = $best;
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func deleteString(_ s: String) -> Int {
        let chars = Array(s.utf8)
        let n = chars.count
        if n == 0 { return 0 }
        
        let mod1 = 1_000_000_007
        let mod2 = 1_000_000_009
        let base = 91_138_233
        
        var pow1 = [Int](repeating: 0, count: n + 1)
        var pow2 = [Int](repeating: 0, count: n + 1)
        pow1[0] = 1
        pow2[0] = 1
        for i in 1...n {
            pow1[i] = Int((Int64(pow1[i - 1]) * Int64(base)) % Int64(mod1))
            pow2[i] = Int((Int64(pow2[i - 1]) * Int64(base)) % Int64(mod2))
        }
        
        var pref1 = [Int](repeating: 0, count: n + 1)
        var pref2 = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            pref1[i + 1] = Int(( (Int64(pref1[i]) * Int64(base)) + Int64(chars[i]) ) % Int64(mod1))
            pref2[i + 1] = Int(( (Int64(pref2[i]) * Int64(base)) + Int64(chars[i]) ) % Int64(mod2))
        }
        
        func getHash(_ pref: [Int], _ powArr: [Int], _ l: Int, _ r: Int, _ mod: Int) -> Int {
            var res = pref[r] - Int((Int64(pref[l]) * Int64(powArr[r - l])) % Int64(mod))
            if res < 0 { res += mod }
            return res
        }
        
        func equal(_ i: Int, _ j: Int, _ len: Int) -> Bool {
            let h1a = getHash(pref1, pow1, i, i + len, mod1)
            let h1b = getHash(pref1, pow1, j, j + len, mod1)
            if h1a != h1b { return false }
            let h2a = getHash(pref2, pow2, i, i + len, mod2)
            let h2b = getHash(pref2, pow2, j, j + len, mod2)
            return h2a == h2b
        }
        
        var dp = [Int](repeating: 0, count: n + 1)
        dp[n] = 0
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            var best = 1   // delete the whole suffix at once
            let maxLen = (n - i) / 2
            if maxLen > 0 {
                for len in 1...maxLen {
                    if equal(i, i + len, len) {
                        let candidate = 1 + dp[i + len]
                        if candidate > best { best = candidate }
                    }
                }
            }
            dp[i] = best
        }
        
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun deleteString(s: String): Int {
        val n = s.length
        val MOD = 1_000_000_007L
        val BASE = 91138233L

        val pow = LongArray(n + 1)
        pow[0] = 1L
        for (i in 1..n) {
            pow[i] = (pow[i - 1] * BASE) % MOD
        }

        val pref = LongArray(n + 1)
        for (i in 0 until n) {
            val v = (s[i] - 'a' + 1).toLong()
            pref[i + 1] = (pref[i] * BASE + v) % MOD
        }

        fun getHash(l: Int, r: Int): Long { // [l, r)
            var res = pref[r] - (pref[l] * pow[r - l]) % MOD
            if (res < 0) res += MOD
            return res
        }

        val dp = IntArray(n + 1)
        dp[n] = 0
        for (i in n - 1 downTo 0) {
            var best = 1 // delete all remaining at once
            val maxLen = (n - i) / 2
            var len = 1
            while (len <= maxLen) {
                if (getHash(i, i + len) == getHash(i + len, i + 2 * len)) {
                    val cand = 1 + dp[i + len]
                    if (cand > best) best = cand
                }
                len++
            }
            dp[i] = best
        }
        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int deleteString(String s) {
    int n = s.length;
    const int MOD1 = 1000000007;
    const int MOD2 = 1000000009;
    const int BASE = 91138233;

    List<int> pow1 = List.filled(n + 1, 0);
    List<int> pow2 = List.filled(n + 1, 0);
    pow1[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pow1[i] = ((pow1[i - 1] * BASE) % MOD1).toInt();
      pow2[i] = ((pow2[i - 1] * BASE) % MOD2).toInt();
    }

    List<int> pref1 = List.filled(n + 1, 0);
    List<int> pref2 = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      int code = s.codeUnitAt(i) - 96; // 'a' -> 1
      pref1[i + 1] = ((pref1[i] * BASE + code) % MOD1).toInt();
      pref2[i + 1] = ((pref2[i] * BASE + code) % MOD2).toInt();
    }

    bool equal(int a, int b, int len) {
      int h1a = pref1[a + len] - (pref1[a] * pow1[len]) % MOD1;
      if (h1a < 0) h1a += MOD1;
      int h1b = pref1[b + len] - (pref1[b] * pow1[len]) % MOD1;
      if (h1b < 0) h1b += MOD1;
      if (h1a != h1b) return false;

      int h2a = pref2[a + len] - (pref2[a] * pow2[len]) % MOD2;
      if (h2a < 0) h2a += MOD2;
      int h2b = pref2[b + len] - (pref2[b] * pow2[len]) % MOD2;
      if (h2b < 0) h2b += MOD2;
      return h2a == h2b;
    }

    List<int> dp = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      int best = 1; // delete all remaining characters in one operation
      int maxLen = (n - i) >> 1;
      for (int len = 1; len <= maxLen; ++len) {
        if (equal(i, i + len, len)) {
          int cand = 1 + dp[i + len];
          if (cand > best) best = cand;
        }
      }
      dp[i] = best;
    }
    return dp[0];
  }
}
```

## Golang

```go
func deleteString(s string) int {
    n := len(s)
    const mod1 int64 = 1000000007
    const mod2 int64 = 1000000009
    const base int64 = 91138233

    pre1 := make([]int64, n+1)
    pre2 := make([]int64, n+1)
    pow1 := make([]int64, n+1)
    pow2 := make([]int64, n+1)
    pow1[0] = 1
    pow2[0] = 1
    for i := 0; i < n; i++ {
        c := int64(s[i]-'a'+1)
        pre1[i+1] = (pre1[i]*base + c) % mod1
        pre2[i+1] = (pre2[i]*base + c) % mod2
        pow1[i+1] = (pow1[i] * base) % mod1
        pow2[i+1] = (pow2[i] * base) % mod2
    }

    getHash := func(l, r int) (int64, int64) {
        h1 := pre1[r] - (pre1[l]*pow1[r-l])%mod1
        if h1 < 0 {
            h1 += mod1
        }
        h2 := pre2[r] - (pre2[l]*pow2[r-l])%mod2
        if h2 < 0 {
            h2 += mod2
        }
        return h1, h2
    }

    equal := func(l1, r1, l2, r2 int) bool {
        h1a, h2a := getHash(l1, r1)
        h1b, h2b := getHash(l2, r2)
        return h1a == h1b && h2a == h2b
    }

    dp := make([]int, n+1)
    for i := n - 1; i >= 0; i-- {
        best := 1 // delete all remaining at once
        maxL := (n - i) / 2
        for L := 1; L <= maxL; L++ {
            if equal(i, i+L, i+L, i+2*L) {
                cand := 1 + dp[i+L]
                if cand > best {
                    best = cand
                }
            }
        }
        dp[i] = best
    }
    return dp[0]
}
```

## Ruby

```ruby
def delete_string(s)
  n = s.length
  base = 91138233
  mod1 = 1_000_000_007
  mod2 = 1_000_000_009

  pow1 = Array.new(n + 1, 0)
  pow2 = Array.new(n + 1, 0)
  pow1[0] = 1
  pow2[0] = 1
  (1..n).each do |i|
    pow1[i] = (pow1[i - 1] * base) % mod1
    pow2[i] = (pow2[i - 1] * base) % mod2
  end

  h1 = Array.new(n + 1, 0)
  h2 = Array.new(n + 1, 0)
  n.times do |i|
    c = s.getbyte(i) - 96 # 'a' => 1
    h1[i + 1] = (h1[i] * base + c) % mod1
    h2[i + 1] = (h2[i] * base + c) % mod2
  end

  equal = lambda do |l, r, len|
    x1 = (h1[l + len] - (h1[l] * pow1[len]) % mod1) % mod1
    y1 = (h1[r + len] - (h1[r] * pow1[len]) % mod1) % mod1
    next false if x1 != y1
    x2 = (h2[l + len] - (h2[l] * pow2[len]) % mod2) % mod2
    y2 = (h2[r + len] - (h2[r] * pow2[len]) % mod2) % mod2
    x2 == y2
  end

  dp = Array.new(n + 1, 0)
  dp[n] = 0
  i = n - 1
  while i >= 0
    best = 1
    max_len = (n - i) / 2
    l = 1
    while l <= max_len
      if equal.call(i, i + l, l)
        cand = 1 + dp[i + l]
        best = cand if cand > best
      end
      l += 1
    end
    dp[i] = best
    i -= 1
  end
  dp[0]
end
```

## Scala

```scala
object Solution {
    def deleteString(s: String): Int = {
        val n = s.length
        // Precompute longest common prefixes for all pairs of positions
        val lcp = Array.ofDim[Int](n + 1, n + 1)
        var i = n - 1
        while (i >= 0) {
            var j = n - 1
            while (j >= 0) {
                if (s.charAt(i) == s.charAt(j)) {
                    lcp(i)(j) = 1 + lcp(i + 1)(j + 1)
                } else {
                    lcp(i)(j) = 0
                }
                j -= 1
            }
            i -= 1
        }

        // dp[pos] = maximum operations to delete substring starting at pos
        val dp = Array.fill[Int](n + 1)(Int.MinValue)
        dp(n) = 0
        var pos = n - 1
        while (pos >= 0) {
            var best = 1 // delete the whole remaining part in one move
            var len = 1
            val maxLen = (n - pos) / 2
            while (len <= maxLen) {
                if (lcp(pos)(pos + len) >= len) {
                    val cand = 1 + dp(pos + len)
                    if (cand > best) best = cand
                }
                len += 1
            }
            dp(pos) = best
            pos -= 1
        }

        dp(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn delete_string(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        const BASE: u64 = 91138233;
        // prefix hash and powers
        let mut h = vec![0u64; n + 1];
        let mut p = vec![1u64; n + 1];
        for i in 0..n {
            h[i + 1] = h[i].wrapping_mul(BASE).wrapping_add(bytes[i] as u64);
            p[i + 1] = p[i].wrapping_mul(BASE);
        }

        let mut dp = vec![0i32; n + 1]; // dp[n] = 0
        for i in (0..n).rev() {
            let mut best = 1; // delete all remaining at once
            let max_len = (n - i) / 2;
            for len in 1..=max_len {
                // hash of s[i..i+len)
                let left = h[i + len]
                    .wrapping_sub(h[i].wrapping_mul(p[len]));
                // hash of s[i+len..i+2*len)
                let right = h[i + 2 * len]
                    .wrapping_sub(h[i + len].wrapping_mul(p[len]));
                if left == right {
                    let cand = 1 + dp[i + len];
                    if cand > best {
                        best = cand;
                    }
                }
            }
            dp[i] = best;
        }
        dp[0]
    }
}
```

## Racket

```racket
(define/contract (delete-string s)
  (-> string? exact-integer?)
  (let* ([base 91138233]
         [mod1 1000000007]
         [mod2 1000000009]
         [n (string-length s)]
         ;; precompute powers
         [pow1 (make-vector (+ n 1) 0)]
         [pow2 (make-vector (+ n 1) 0)]
         ;; prefix hashes
         [pref1 (make-vector (+ n 1) 0)]
         [pref2 (make-vector (+ n 1) 0)])
    ;; powers
    (vector-set! pow1 0 1)
    (vector-set! pow2 0 1)
    (for ([i (in-range n)])
      (vector-set! pow1 (add1 i)
                   (modulo (* (vector-ref pow1 i) base) mod1))
      (vector-set! pow2 (add1 i)
                   (modulo (* (vector-ref pow2 i) base) mod2)))
    ;; prefix hashes
    (for ([i (in-range n)])
      (let* ([c (char->integer (string-ref s i))]
             [h1 (modulo (+ (* (vector-ref pref1 i) base) c) mod1)]
             [h2 (modulo (+ (* (vector-ref pref2 i) base) c) mod2)])
        (vector-set! pref1 (add1 i) h1)
        (vector-set! pref2 (add1 i) h2)))
    ;; helper to get hash of s[l..r)
    (define (subhash pref pow l r mod)
      (modulo (- (vector-ref pref r)
                 (* (vector-ref pref l)
                    (vector-ref pow (- r l))))
               mod))
    ;; equality test for two consecutive substrings of equal length
    (define (equal-sub a b c)
      (and (= (subhash pref1 pow1 a b mod1)
              (subhash pref1 pow1 b c mod1))
           (= (subhash pref2 pow2 a b mod2)
              (subhash pref2 pow2 b c mod2))))
    ;; DP: dp[i] = max moves to delete suffix starting at i
    (let ([dp (make-vector (+ n 1) 0)])
      (vector-set! dp n 0)
      (for ([i (in-range (- n 1) -1 -1)])
        (let ([best 1]) ; delete all remaining in one move
          (define maxlen (quotient (- n i) 2))
          (for ([len (in-range 1 (add1 maxlen))])
            (when (equal-sub i (+ i len) (+ i (* 2 len)))
              (let ([cand (+ 1 (vector-ref dp (+ i len)))])
                (when (> cand best)
                  (set! best cand)))))
          (vector-set! dp i best)))
      (vector-ref dp 0))))
```

## Erlang

```erlang
-spec delete_string(S :: unicode:unicode_binary()) -> integer().
delete_string(S) ->
    Chars = binary_to_list(S),
    N = length(Chars),

    % Build prefix hashes and powers for two moduli
    {Pow1, Pow2, H1, H2} = build_hashes(Chars),

    Mod1 = 1000000007,
    Mod2 = 1000000009,

    % DP tuple: dp[i] = max operations to delete suffix starting at i (0‑based)
    InitDP = list_to_tuple(lists:duplicate(N + 1, 0)),
    DP = fill_dp(N - 1, N, Pow1, Pow2, H1, H2, Mod1, Mod2, InitDP),

    element(1, DP).   % dp[0]

%% Build power and prefix hash tuples (index i corresponds to length i)
build_hashes(Chars) ->
    Base = 91138233,
    Mod1 = 1000000007,
    Mod2 = 1000000009,
    build_hashes(Chars, 1, 1, 0, 0,
                 [1], [1], [0], [0]).

build_hashes([], _Pow1Prev, _Pow2Prev, _H1Prev, _H2Prev,
             Pow1Acc, Pow2Acc, H1Acc, H2Acc) ->
    {list_to_tuple(lists:reverse(Pow1Acc)),
     list_to_tuple(lists:reverse(Pow2Acc)),
     list_to_tuple(lists:reverse(H1Acc)),
     list_to_tuple(lists:reverse(H2Acc))};
build_hashes([C|Rest], Pow1Prev, Pow2Prev, H1Prev, H2Prev,
             Pow1Acc, Pow2Acc, H1Acc, H2Acc) ->
    Mod1 = 1000000007,
    Mod2 = 1000000009,
    NewPow1 = (Pow1Prev * Base) rem Mod1,
    NewPow2 = (Pow2Prev * Base) rem Mod2,
    Code = C - $a + 1,
    NewH1 = ((H1Prev * Base) + Code) rem Mod1,
    NewH2 = ((H2Prev * Base) + Code) rem Mod2,
    build_hashes(Rest, NewPow1, NewPow2, NewH1, NewH2,
                 [NewPow1|Pow1Acc], [NewPow2|Pow2Acc],
                 [NewH1|H1Acc], [NewH2|H2Acc]).

%% Fill DP from right to left
fill_dp(-1, _N, _Pow1, _Pow2, _H1, _H2, _Mod1, _Mod2, DP) ->
    DP;
fill_dp(Pos, N, Pow1, Pow2, H1, H2, Mod1, Mod2, DP) ->
    Best = 1,
    MaxBest = try_lengths(1, Pos, N, Pow1, Pow2, H1, H2, Mod1, Mod2, DP, Best),
    NewDP = setelement(Pos + 1, DP, MaxBest),
    fill_dp(Pos - 1, N, Pow1, Pow2, H1, H2, Mod1, Mod2, NewDP).

%% Try all possible lengths L where the prefix of length L repeats immediately
try_lengths(L, Pos, N, Pow1, Pow2, H1, H2, Mod1, Mod2, DP, Best)
    when Pos + 2 * L =< N ->
    case substr_equal(Pos, L, Pow1, Pow2, H1, H2, Mod1, Mod2) of
        true ->
            NextPos = Pos + L,
            Candidate = 1 + element(NextPos + 1, DP),
            NewBest = if Candidate > Best -> Candidate; true -> Best end;
        false ->
            NewBest = Best
    end,
    try_lengths(L + 1, Pos, N, Pow1, Pow2, H1, H2, Mod1, Mod2, DP, NewBest);
try_lengths(_, _, _, _, _, _, _, _, _, _, Best) ->
    Best.

%% Check equality of two substrings of length L starting at Pos and Pos+L
substr_equal(Pos, L, Pow1, Pow2, H1, H2, Mod1, Mod2) ->
    Hash1A = sub_hash(H1, Pow1, Pos, L, Mod1),
    Hash1B = sub_hash(H1, Pow1, Pos + L, L, Mod1),
    if
        Hash1A =:= Hash1B ->
            Hash2A = sub_hash(H2, Pow2, Pos, L, Mod2),
            Hash2B = sub_hash(H2, Pow2, Pos + L, L, Mod2),
            Hash2A =:= Hash2B;
        true -> false
    end.

%% Compute hash of substring [Start, Start+Len)
sub_hash(H, Pow, Start, Len, Mod) ->
    End = Start + Len,
    HS = element(End + 1, H),
    HL = element(Start + 1, H),
    PL = element(Len + 1, Pow),
    ((HS - (HL * PL) rem Mod) + Mod) rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @spec delete_string(String.t()) :: integer
  def delete_string(s) do
    n = String.length(s)
    bytes = String.to_charlist(s)

    base = 911382323
    mod = 1_000_000_007

    # prefix hashes and powers
    hash = :array.new(n + 1, default: 0)
    pow = :array.new(n + 1, default: 1)

    {hash, pow} =
      Enum.reduce(0..n - 1, {hash, pow}, fn i, {h_acc, p_acc} ->
        prev_h = :array.get(i, h_acc)
        val = Enum.at(bytes, i) - ?a + 1
        new_h = rem(prev_h * base + val, mod)

        prev_p = :array.get(i, p_acc)
        new_p = rem(prev_p * base, mod)

        { :array.set(i + 1, new_h, h_acc), :array.set(i + 1, new_p, p_acc) }
      end)

    # dp array: dp[i] = max operations to delete suffix starting at i
    dp_initial = :array.new(n + 1, default: 0)

    dp =
      Enum.reduce(Enum.reverse(0..n - 1), dp_initial, fn i, dp_acc ->
        max_ops = compute_max(i, n, hash, pow, dp_acc, mod)
        :array.set(i, max_ops, dp_acc)
      end)

    :array.get(0, dp)
  end

  defp get_hash(l, r, hash_arr, pow_arr, mod) do
    h_r = :array.get(r, hash_arr)
    h_l = :array.get(l, hash_arr)
    p = :array.get(r - l, pow_arr)
    rem(h_r - rem(h_l * p, mod) + mod, mod)
  end

  defp compute_max(i, n, hash, pow, dp, mod) do
    # at least one operation (delete all remaining)
    go_len = fn len, cur_max, fun ->
      if i + 2 * len <= n do
        h1 = get_hash(i, i + len, hash, pow, mod)
        h2 = get_hash(i + len, i + 2 * len, hash, pow, mod)

        new_max =
          if h1 == h2 do
            cand = 1 + :array.get(i + len, dp)
            max(cur_max, cand)
          else
            cur_max
          end

        fun.(len + 1, new_max, fun)
      else
        cur_max
      end
    end

    go_len.(1, 1, go_len)
  end
end
```
