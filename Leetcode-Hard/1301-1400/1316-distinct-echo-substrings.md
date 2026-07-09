# 1316. Distinct Echo Substrings

## Cpp

```cpp
class Solution {
public:
    int distinctEchoSubstrings(string text) {
        int n = text.size();
        const unsigned long long B = 1315423911ULL;
        vector<unsigned long long> h(n + 1, 0), p(n + 1, 1);
        for (int i = 0; i < n; ++i) {
            h[i + 1] = h[i] * B + (unsigned long long)(text[i] - 'a' + 1);
            p[i + 1] = p[i] * B;
        }
        unordered_set<unsigned long long> seen;
        for (int k = 1; k * 2 <= n; ++k) {
            int len2 = k * 2;
            for (int i = 0; i + len2 <= n; ++i) {
                unsigned long long left = h[i + k] - h[i] * p[k];
                unsigned long long right = h[i + len2] - h[i + k] * p[k];
                if (left == right) {
                    unsigned long long whole = h[i + len2] - h[i] * p[len2];
                    seen.insert(whole);
                }
            }
        }
        return (int)seen.size();
    }
};
```

## Java

```java
class Solution {
    public int distinctEchoSubstrings(String text) {
        final long MOD1 = 1000000007L;
        final long MOD2 = 1000000009L;
        final long BASE = 91138233L;
        int n = text.length();
        char[] s = text.toCharArray();

        long[] pow1 = new long[n + 1];
        long[] pow2 = new long[n + 1];
        pow1[0] = 1;
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow1[i] = (pow1[i - 1] * BASE) % MOD1;
            pow2[i] = (pow2[i - 1] * BASE) % MOD2;
        }

        long[] pref1 = new long[n + 1];
        long[] pref2 = new long[n + 1];
        for (int i = 0; i < n; i++) {
            int val = s[i] - 'a' + 1;
            pref1[i + 1] = (pref1[i] * BASE + val) % MOD1;
            pref2[i + 1] = (pref2[i] * BASE + val) % MOD2;
        }

        java.util.HashSet<Long> set = new java.util.HashSet<>();

        for (int len = 2; len <= n; len += 2) {
            int half = len / 2;
            for (int i = 0; i + len <= n; i++) {
                if (hashEqual(i, i + half - 1, i + half, i + len - 1,
                              pref1, pref2, pow1, pow2, MOD1, MOD2)) {
                    long h1 = subHash(pref1, pow1, i, i + len - 1, MOD1);
                    long h2 = subHash(pref2, pow2, i, i + len - 1, MOD2);
                    long combined = (h1 << 32) ^ h2;
                    set.add(combined);
                }
            }
        }

        return set.size();
    }

    private static long subHash(long[] pref, long[] pow, int l, int r, long mod) {
        int len = r - l + 1;
        long res = (pref[r + 1] - (pref[l] * pow[len]) % mod);
        if (res < 0) res += mod;
        return res;
    }

    private static boolean hashEqual(int l1, int r1, int l2, int r2,
                                     long[] pref1, long[] pref2,
                                     long[] pow1, long[] pow2,
                                     long MOD1, long MOD2) {
        long h11 = subHash(pref1, pow1, l1, r1, MOD1);
        long h12 = subHash(pref1, pow1, l2, r2, MOD1);
        if (h11 != h12) return false;
        long h21 = subHash(pref2, pow2, l1, r1, MOD2);
        long h22 = subHash(pref2, pow2, l2, r2, MOD2);
        return h21 == h22;
    }
}
```

## Python

```python
class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        mod1, mod2 = 1000000007, 1000000009
        base = 91138233

        # prefix hashes
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)

        for i, ch in enumerate(text):
            code = ord(ch) - 96  # map 'a'..'z' to 1..26
            pref1[i + 1] = (pref1[i] * base + code) % mod1
            pref2[i + 1] = (pref2[i] * base + code) % mod2
            pow1[i + 1] = (pow1[i] * base) % mod1
            pow2[i + 1] = (pow2[i] * base) % mod2

        def get_hash(l, r):
            """return pair of hashes for substring text[l:r]"""
            h1 = pref1[r] - pref1[l] * pow1[r - l] % mod1
            if h1 < 0:
                h1 += mod1
            h2 = pref2[r] - pref2[l] * pow2[r - l] % mod2
            if h2 < 0:
                h2 += mod2
            return h1, h2

        seen = set()
        for length in range(2, n + 1, 2):
            half = length // 2
            for i in range(n - length + 1):
                j = i + length
                h_first = get_hash(i, i + half)
                h_second = get_hash(i + half, j)
                if h_first == h_second:
                    seen.add((h_first[0], h_first[1], length))
        return len(seen)
```

## Python3

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        MOD1 = 1000000007
        MOD2 = 1000000009
        base = 91138233

        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)

        for i, ch in enumerate(text):
            x = ord(ch) - 96  # map 'a'->1
            pref1[i + 1] = (pref1[i] * base + x) % MOD1
            pref2[i + 1] = (pref2[i] * base + x) % MOD2
            pow1[i + 1] = (pow1[i] * base) % MOD1
            pow2[i + 1] = (pow2[i] * base) % MOD2

        def get_hash(l: int, r: int):
            h1 = (pref1[r] - pref1[l] * pow1[r - l]) % MOD1
            h2 = (pref2[r] - pref2[l] * pow2[r - l]) % MOD2
            return (h1, h2)

        seen = set()
        for length in range(2, n + 1, 2):
            half = length // 2
            limit = n - length + 1
            for i in range(limit):
                if get_hash(i, i + half) == get_hash(i + half, i + length):
                    seen.add(get_hash(i, i + length))
        return len(seen)
```

## C

```c
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static inline uint64_t getHash(const uint64_t *pref, const uint64_t *powb, int l, int r) {
    return pref[r] - pref[l] * powb[r - l];
}

int distinctEchoSubstrings(char* text) {
    size_t n = strlen(text);
    if (n < 2) return 0;

    const uint64_t BASE = 1315423911ULL;
    uint64_t *pref = (uint64_t *)malloc((n + 1) * sizeof(uint64_t));
    uint64_t *powb = (uint64_t *)malloc((n + 1) * sizeof(uint64_t));

    pref[0] = 0;
    powb[0] = 1;
    for (size_t i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] * BASE + (uint64_t)(text[i] - 'a' + 1);
        powb[i + 1] = powb[i] * BASE;
    }

    size_t maxHashes = n * n / 2 + 1;
    uint64_t *hashes = (uint64_t *)malloc(maxHashes * sizeof(uint64_t));
    size_t hcnt = 0;

    for (size_t len = 2; len <= n; len += 2) {
        size_t half = len / 2;
        for (size_t i = 0; i + len <= n; ++i) {
            if (getHash(pref, powb, i, i + half) == getHash(pref, powb, i + half, i + len)) {
                hashes[hcnt++] = getHash(pref, powb, i, i + len);
            }
        }
    }

    free(pref);
    free(powb);

    if (hcnt == 0) {
        free(hashes);
        return 0;
    }

    qsort(hashes, hcnt, sizeof(uint64_t), (int (*)(const void *, const void *))memcmp);

    size_t distinct = 1;
    for (size_t i = 1; i < hcnt; ++i) {
        if (hashes[i] != hashes[i - 1]) ++distinct;
    }

    free(hashes);
    return (int)distinct;
}
```

## Csharp

```csharp
public class Solution
{
    public int DistinctEchoSubstrings(string text)
    {
        int n = text.Length;
        const long mod1 = 1000000007L;
        const long mod2 = 1000000009L;
        const long baseVal = 91138233L;

        long[] pow1 = new long[n + 1];
        long[] pow2 = new long[n + 1];
        pow1[0] = pow2[0] = 1;
        for (int i = 1; i <= n; i++)
        {
            pow1[i] = (pow1[i - 1] * baseVal) % mod1;
            pow2[i] = (pow2[i - 1] * baseVal) % mod2;
        }

        long[] pref1 = new long[n + 1];
        long[] pref2 = new long[n + 1];
        for (int i = 0; i < n; i++)
        {
            int val = text[i] - 'a' + 1;
            pref1[i + 1] = (pref1[i] * baseVal + val) % mod1;
            pref2[i + 1] = (pref2[i] * baseVal + val) % mod2;
        }

        long GetHash(long[] pref, long[] pow, int start, int len, long mod)
        {
            long res = (pref[start + len] - (pref[start] * pow[len]) % mod);
            if (res < 0) res += mod;
            return res;
        }

        var seen = new HashSet<(long, long)>();

        for (int L = 2; L <= n; L += 2)
        {
            int half = L / 2;
            for (int i = 0; i + L <= n; i++)
            {
                long h1a = GetHash(pref1, pow1, i, half, mod1);
                long h1b = GetHash(pref1, pow1, i + half, half, mod1);
                if (h1a != h1b) continue;

                long h2a = GetHash(pref2, pow2, i, half, mod2);
                long h2b = GetHash(pref2, pow2, i + half, half, mod2);
                if (h2a != h2b) continue;

                long whole1 = GetHash(pref1, pow1, i, L, mod1);
                long whole2 = GetHash(pref2, pow2, i, L, mod2);
                seen.Add((whole1, whole2));
            }
        }

        return seen.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var distinctEchoSubstrings = function(text) {
    const n = text.length;
    const BASE = 91138233n;
    const MOD1 = 1000000007n;
    const MOD2 = 1000000009n;

    const pref1 = new Array(n + 1).fill(0n);
    const pref2 = new Array(n + 1).fill(0n);
    const pow1 = new Array(n + 1).fill(1n);
    const pow2 = new Array(n + 1).fill(1n);

    for (let i = 0; i < n; i++) {
        const code = BigInt(text.charCodeAt(i) - 96); // 'a' -> 1
        pref1[i + 1] = (pref1[i] * BASE + code) % MOD1;
        pref2[i + 1] = (pref2[i] * BASE + code) % MOD2;
        pow1[i + 1] = (pow1[i] * BASE) % MOD1;
        pow2[i + 1] = (pow2[i] * BASE) % MOD2;
    }

    const getHash = (l, r) => { // [l, r)
        const len = r - l;
        let h1 = pref1[r] - (pref1[l] * pow1[len]) % MOD1;
        if (h1 < 0) h1 += MOD1;
        let h2 = pref2[r] - (pref2[l] * pow2[len]) % MOD2;
        if (h2 < 0) h2 += MOD2;
        return [h1, h2];
    };

    const seen = new Set();

    for (let i = 0; i < n; i++) {
        // only even lengths can be echo substrings
        for (let len = 2; i + len <= n; len += 2) {
            const mid = i + len / 2;
            const leftHash = getHash(i, mid);
            const rightHash = getHash(mid, i + len);
            if (leftHash[0] === rightHash[0] && leftHash[1] === rightHash[1]) {
                // use hash and length as key to avoid collisions across lengths
                const key = `${leftHash[0]}_${leftHash[1]}_${len}`;
                seen.add(key);
            }
        }
    }

    return seen.size;
};
```

## Typescript

```typescript
function distinctEchoSubstrings(text: string): number {
    const n = text.length;
    const BASE = 91138233n;
    const MOD1 = 1000000007n;
    const MOD2 = 1000000009n;

    const pow1: bigint[] = new Array(n + 1);
    const pow2: bigint[] = new Array(n + 1);
    pow1[0] = 1n;
    pow2[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        pow1[i] = (pow1[i - 1] * BASE) % MOD1;
        pow2[i] = (pow2[i - 1] * BASE) % MOD2;
    }

    const pref1: bigint[] = new Array(n + 1);
    const pref2: bigint[] = new Array(n + 1);
    pref1[0] = 0n;
    pref2[0] = 0n;
    for (let i = 0; i < n; ++i) {
        const val = BigInt(text.charCodeAt(i) - 96); // 'a' -> 1
        pref1[i + 1] = (pref1[i] * BASE + val) % MOD1;
        pref2[i + 1] = (pref2[i] * BASE + val) % MOD2;
    }

    const getHash = (l: number, r: number): [bigint, bigint] => {
        const len = r - l;
        let h1 = pref1[r] - (pref1[l] * pow1[len]) % MOD1;
        if (h1 < 0) h1 += MOD1;
        let h2 = pref2[r] - (pref2[l] * pow2[len]) % MOD2;
        if (h2 < 0) h2 += MOD2;
        return [h1, h2];
    };

    const seen = new Set<string>();
    for (let len = 2; len <= n; len += 2) {
        const half = len >> 1;
        for (let i = 0; i + len <= n; ++i) {
            const first = getHash(i, i + half);
            const second = getHash(i + half, i + len);
            if (first[0] === second[0] && first[1] === second[1]) {
                const full = getHash(i, i + len);
                seen.add(full[0].toString() + '_' + full[1].toString());
            }
        }
    }

    return seen.size;
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function distinctEchoSubstrings($text) {
        $n = strlen($text);
        if ($n < 2) return 0;

        $base = 91138233;
        $mod1 = 1000000007;
        $mod2 = 1000000009;

        // powers
        $pow1 = array_fill(0, $n + 1, 0);
        $pow2 = array_fill(0, $n + 1, 0);
        $pow1[0] = 1;
        $pow2[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $pow1[$i] = (int)(($pow1[$i - 1] * $base) % $mod1);
            $pow2[$i] = (int)(($pow2[$i - 1] * $base) % $mod2);
        }

        // prefix hashes
        $pref1 = array_fill(0, $n + 1, 0);
        $pref2 = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($text[$i]) - 96; // map 'a'..'z' to 1..26
            $pref1[$i + 1] = (int)((($pref1[$i] * $base) + $c) % $mod1);
            $pref2[$i + 1] = (int)((($pref2[$i] * $base) + $c) % $mod2);
        }

        $set = [];

        for ($len = 2; $len <= $n; $len += 2) {
            $half = intdiv($len, 2);
            for ($i = 0; $i + $len <= $n; $i++) {
                // hash of first half
                $h1_left = $pref1[$i + $half] - (int)(($pref1[$i] * $pow1[$half]) % $mod1);
                if ($h1_left < 0) $h1_left += $mod1;
                $h2_left = $pref2[$i + $half] - (int)(($pref2[$i] * $pow2[$half]) % $mod2);
                if ($h2_left < 0) $h2_left += $mod2;

                // hash of second half
                $h1_right = $pref1[$i + $len] - (int)(($pref1[$i + $half] * $pow1[$half]) % $mod1);
                if ($h1_right < 0) $h1_right += $mod1;
                $h2_right = $pref2[$i + $len] - (int)(($pref2[$i + $half] * $pow2[$half]) % $mod2);
                if ($h2_right < 0) $h2_right += $mod2;

                if ($h1_left === $h1_right && $h2_left === $h2_right) {
                    // whole substring hash
                    $h1_full = $pref1[$i + $len] - (int)(($pref1[$i] * $pow1[$len]) % $mod1);
                    if ($h1_full < 0) $h1_full += $mod1;
                    $h2_full = $pref2[$i + $len] - (int)(($pref2[$i] * $pow2[$len]) % $mod2);
                    if ($h2_full < 0) $h2_full += $mod2;

                    $key = $h1_full . ':' . $h2_full;
                    $set[$key] = true;
                }
            }
        }

        return count($set);
    }
}
```

## Swift

```swift
class Solution {
    func distinctEchoSubstrings(_ text: String) -> Int {
        let chars = Array(text.utf8)
        let n = chars.count
        if n < 2 { return 0 }
        let base: Int64 = 91138233
        let mod1: Int64 = 1_000_000_007
        let mod2: Int64 = 1_000_000_009
        
        var pow1 = [Int64](repeating: 0, count: n + 1)
        var pow2 = [Int64](repeating: 0, count: n + 1)
        pow1[0] = 1
        pow2[0] = 1
        for i in 1...n {
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2
        }
        
        var pref1 = [Int64](repeating: 0, count: n + 1)
        var pref2 = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            let val = Int64(chars[i])
            pref1[i + 1] = (pref1[i] * base + val) % mod1
            pref2[i + 1] = (pref2[i] * base + val) % mod2
        }
        
        func getHash(_ l: Int, _ r: Int) -> (Int64, Int64) {
            let len = r - l
            var h1 = pref1[r] - (pref1[l] * pow1[len]) % mod1
            if h1 < 0 { h1 += mod1 }
            var h2 = pref2[r] - (pref2[l] * pow2[len]) % mod2
            if h2 < 0 { h2 += mod2 }
            return (h1, h2)
        }
        
        var seen = Set<UInt64>()
        var len = 2
        while len <= n {
            let half = len / 2
            for i in 0...(n - len) {
                let first = getHash(i, i + half)
                let second = getHash(i + half, i + len)
                if first.0 == second.0 && first.1 == second.1 {
                    let full = getHash(i, i + len)
                    let key = (UInt64(full.0) << 32) | UInt64(full.1)
                    seen.insert(key)
                }
            }
            len += 2
        }
        return seen.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distinctEchoSubstrings(text: String): Int {
        val n = text.length
        val base = 91138233L
        val mod1 = 1000000007L
        val mod2 = 1000000009L

        val pow1 = LongArray(n + 1)
        val pow2 = LongArray(n + 1)
        pow1[0] = 1L
        pow2[0] = 1L
        for (i in 1..n) {
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2
        }

        val pref1 = LongArray(n + 1)
        val pref2 = LongArray(n + 1)
        for (i in 0 until n) {
            val v = (text[i] - 'a' + 1).toLong()
            pref1[i + 1] = (pref1[i] * base + v) % mod1
            pref2[i + 1] = (pref2[i] * base + v) % mod2
        }

        fun getHash(l: Int, r: Int): Long {
            var x1 = (pref1[r] - (pref1[l] * pow1[r - l]) % mod1)
            if (x1 < 0) x1 += mod1
            var x2 = (pref2[r] - (pref2[l] * pow2[r - l]) % mod2)
            if (x2 < 0) x2 += mod2
            return (x1 shl 32) xor x2
        }

        val set = HashSet<Long>()
        for (i in 0 until n) {
            var k = 1
            while (i + 2 * k <= n) {
                if (getHash(i, i + k) == getHash(i + k, i + 2 * k)) {
                    set.add(getHash(i, i + 2 * k))
                }
                k++
            }
        }
        return set.size
    }
}
```

## Dart

```dart
class Solution {
  int distinctEchoSubstrings(String text) {
    final n = text.length;
    const int mod1 = 1000000007;
    const int mod2 = 1000000009;
    const int base = 91138233;

    List<int> pow1 = List.filled(n + 1, 0);
    List<int> pow2 = List.filled(n + 1, 0);
    pow1[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pow1[i] = ((pow1[i - 1] * base) % mod1).toInt();
      pow2[i] = ((pow2[i - 1] * base) % mod2).toInt();
    }

    List<int> pref1 = List.filled(n + 1, 0);
    List<int> pref2 = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      int code = text.codeUnitAt(i) - 96; // 'a' -> 1
      pref1[i + 1] = ((pref1[i] * base + code) % mod1).toInt();
      pref2[i + 1] = ((pref2[i] * base + code) % mod2).toInt();
    }

    int getHash1(int l, int r) {
      int val = (pref1[r] - (pref1[l] * pow1[r - l]) % mod1);
      if (val < 0) val += mod1;
      return val;
    }

    int getHash2(int l, int r) {
      int val = (pref2[r] - (pref2[l] * pow2[r - l]) % mod2);
      if (val < 0) val += mod2;
      return val;
    }

    Set<String> seen = {};

    for (int k = 1; k <= n ~/ 2; ++k) {
      int len = k * 2;
      for (int i = 0; i + len <= n; ++i) {
        if (getHash1(i, i + k) == getHash1(i + k, i + len) &&
            getHash2(i, i + k) == getHash2(i + k, i + len)) {
          int h1 = getHash1(i, i + len);
          int h2 = getHash2(i, i + len);
          seen.add('$h1#$h2');
        }
      }
    }

    return seen.length;
  }
}
```

## Golang

```go
func distinctEchoSubstrings(text string) int {
    n := len(text)
    if n < 2 {
        return 0
    }
    const base uint64 = 1315423911
    pow := make([]uint64, n+1)
    pref := make([]uint64, n+1)
    pow[0] = 1
    for i := 0; i < n; i++ {
        pow[i+1] = pow[i] * base
        pref[i+1] = pref[i]*base + uint64(text[i])
    }
    hash := func(l, r int) uint64 { // [l,r)
        return pref[r] - pref[l]*pow[r-l]
    }

    seen := make(map[uint64]struct{})
    for length := 2; length <= n; length += 2 {
        half := length / 2
        for i := 0; i+length <= n; i++ {
            if hash(i, i+half) == hash(i+half, i+length) {
                key := hash(i, i+length) ^ (uint64(length) << 32)
                seen[key] = struct{}{}
            }
        }
    }
    return len(seen)
}
```

## Ruby

```ruby
require 'set'

# @param {String} text
# @return {Integer}
def distinct_echo_substrings(text)
  n = text.length
  base = 91138233
  mod1 = 1_000_000_007
  mod2 = 1_000_000_009

  h1 = Array.new(n + 1, 0)
  h2 = Array.new(n + 1, 0)
  p1 = Array.new(n + 1, 1)
  p2 = Array.new(n + 1, 1)

  n.times do |i|
    c = text.getbyte(i) - 96 # 'a' -> 1
    h1[i + 1] = (h1[i] * base + c) % mod1
    h2[i + 1] = (h2[i] * base + c) % mod2
    p1[i + 1] = (p1[i] * base) % mod1
    p2[i + 1] = (p2[i] * base) % mod2
  end

  get_hash = lambda do |l, r|
    x1 = h1[r] - (h1[l] * p1[r - l]) % mod1
    x1 += mod1 if x1 < 0
    x2 = h2[r] - (h2[l] * p2[r - l]) % mod2
    x2 += mod2 if x2 < 0
    [x1, x2]
  end

  seen = Set.new

  i = 0
  while i < n
    max_len = n - i
    len = 2
    while len <= max_len
      mid = i + (len >> 1)
      if get_hash.call(i, mid) == get_hash.call(mid, i + len)
        seen.add(get_hash.call(i, i + len))
      end
      len += 2
    end
    i += 1
  end

  seen.size
end
```

## Scala

```scala
object Solution {
    def distinctEchoSubstrings(text: String): Int = {
        val n = text.length
        val base: Long = 91138233L
        val h = new Array[Long](n + 1)
        val pow = new Array[Long](n + 1)
        pow(0) = 1L
        for (i <- 0 until n) {
            h(i + 1) = h(i) * base + (text.charAt(i) - 'a' + 1)
            pow(i + 1) = pow(i) * base
        }
        def getHash(l: Int, r: Int): Long = { // [l, r)
            h(r) - h(l) * pow(r - l)
        }

        val seen = scala.collection.mutable.HashSet[(Long, Int)]()
        for (i <- 0 until n) {
            var k = 1
            while (i + 2 * k <= n) {
                if (getHash(i, i + k) == getHash(i + k, i + 2 * k)) {
                    seen.add((getHash(i, i + 2 * k), 2 * k))
                }
                k += 1
            }
        }
        seen.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distinct_echo_substrings(text: String) -> i32 {
        let bytes = text.as_bytes();
        let n = bytes.len();
        const MOD1: u64 = 1_000_000_007;
        const MOD2: u64 = 1_000_000_009;
        let base: u64 = 91138233;

        // powers
        let mut pow1 = vec![0u64; n + 1];
        let mut pow2 = vec![0u64; n + 1];
        pow1[0] = 1;
        pow2[0] = 1;
        for i in 1..=n {
            pow1[i] = ((pow1[i - 1] as u128 * base as u128) % MOD1 as u128) as u64;
            pow2[i] = ((pow2[i - 1] as u128 * base as u128) % MOD2 as u128) as u64;
        }

        // prefix hashes
        let mut pref1 = vec![0u64; n + 1];
        let mut pref2 = vec![0u64; n + 1];
        for i in 0..n {
            let val = (bytes[i] - b'a' + 1) as u64;
            pref1[i + 1] =
                ((pref1[i] as u128 * base as u128 + val as u128) % MOD1 as u128) as u64;
            pref2[i + 1] =
                ((pref2[i] as u128 * base as u128 + val as u128) % MOD2 as u128) as u64;
        }

        // hash getter
        let get_hash = |l: usize, r: usize| -> (u64, u64) {
            let len = r - l;
            let mut h1 = pref1[r];
            let sub1 = ((pref1[l] as u128 * pow1[len] as u128) % MOD1 as u128) as u64;
            if h1 >= sub1 {
                h1 -= sub1;
            } else {
                h1 = h1 + MOD1 - sub1;
            }
            let mut h2 = pref2[r];
            let sub2 = ((pref2[l] as u128 * pow2[len] as u128) % MOD2 as u128) as u64;
            if h2 >= sub2 {
                h2 -= sub2;
            } else {
                h2 = h2 + MOD2 - sub2;
            }
            (h1, h2)
        };

        use std::collections::HashSet;
        let mut set: HashSet<(u64, u64)> = HashSet::new();

        for len in (2..=n).step_by(2) {
            let half = len / 2;
            for i in 0..=n - len {
                if get_hash(i, i + half) == get_hash(i + half, i + len) {
                    set.insert(get_hash(i, i + len));
                }
            }
        }

        set.len() as i32
    }
}
```

## Racket

```racket
(define/contract (distinct-echo-substrings text)
  (-> string? exact-integer?)
  (let* ((n (string-length text))
         (mod 1000000007)
         (base 91138233)
         (pref (make-vector (+ n 1) 0))
         (powv (make-vector (+ n 1) 0)))
    (vector-set! powv 0 1)
    ;; build prefix hashes and powers
    (for ([i (in-range n)])
      (let* ((c (string-ref text i))
             (val (+ (- (char->integer c) (char->integer #\a)) 1))
             (prev (vector-ref pref i))
             (newh (modulo (+ (* prev base) val) mod)))
        (vector-set! pref (add1 i) newh)
        (let* ((prevp (vector-ref powv i))
               (newp (modulo (* prevp base) mod)))
          (vector-set! powv (add1 i) newp))))
    ;; helper to get hash of substring [l, r)
    (define (hash-sub l r)
      (let* ((len (- r l))
             (h1 (vector-ref pref r))
             (h2 (vector-ref pref l))
             (p (vector-ref powv len))
             (res (- h1 (modulo (* h2 p) mod))))
        (if (< res 0) (+ res mod) res)))
    (define seen (make-hash))
    ;; enumerate even lengths
    (for ([len (in-range 2 (add1 n) 2)])
      (let ((max-i (- n len)))
        (when (>= max-i 0)
          (for ([i (in-range 0 (add1 max-i))])
            (let* ((mid (+ i (quotient len 2)))
                   (h1 (hash-sub i mid))
                   (h2 (hash-sub mid (+ i len))))
              (when (= h1 h2)
                (let ((sub (substring text i (+ i len))))
                  (hash-set! seen sub #t)))))))))
    (length (hash-keys seen))))
```

## Erlang

```erlang
-spec distinct_echo_substrings(Text :: unicode:unicode_binary()) -> integer().
distinct_echo_substrings(Text) ->
    Bytes = binary_to_list(Text),
    N = length(Bytes),
    Base = 91138233,
    Mod1 = 1000000007,
    Mod2 = 1000000009,
    Pow1 = build_pow(N, Base, Mod1),
    Pow2 = build_pow(N, Base, Mod2),
    Pref1 = build_prefix(Bytes, Base, Mod1),
    Pref2 = build_prefix(Bytes, Base, Mod2),
    MaxL = N div 2,
    Set0 = maps:new(),
    FinalSet = iter_len(1, MaxL, N, Pref1, Pow1, Pref2, Pow2, Set0),
    maps:size(FinalSet).

build_pow(N, Base, Mod) ->
    build_pow(0, N, Base, Mod, [1]).

build_pow(I, N, _Base, _Mod, Acc) when I =:= N ->
    list_to_tuple(lists:reverse(Acc));
build_pow(I, N, Base, Mod, Acc) ->
    Prev = hd(Acc),
    Next = (Prev * Base) rem Mod,
    build_pow(I + 1, N, Base, Mod, [Next | Acc]).

build_prefix(Bytes, Base, Mod) ->
    build_prefix(Bytes, Base, Mod, [0]).

build_prefix([], _Base, _Mod, Acc) ->
    list_to_tuple(lists:reverse(Acc));
build_prefix([C | Rest], Base, Mod, Acc) ->
    Prev = hd(Acc),
    Val = C - $a + 1,
    Next = (Prev * Base + Val) rem Mod,
    build_prefix(Rest, Base, Mod, [Next | Acc]).

hash_sub(Pref, Pow, L, R, Mod) ->
    PrefR = element(R + 1, Pref),
    PrefL = element(L + 1, Pref),
    PowLen = element(R - L + 1, Pow),
    H0 = (PrefR - (PrefL * PowLen) rem Mod) rem Mod,
    if H0 < 0 -> H0 + Mod; true -> H0 end.

iter_len(L, MaxL, _N, _Pref1, _Pow1, _Pref2, _Pow2, Set) when L > MaxL ->
    Set;
iter_len(L, MaxL, N, Pref1, Pow1, Pref2, Pow2, Set) ->
    MaxStart = N - 2 * L,
    Set1 = iter_start(0, MaxStart, L, Pref1, Pow1, Pref2, Pow2, Set),
    iter_len(L + 1, MaxL, N, Pref1, Pow1, Pref2, Pow2, Set1).

iter_start(I, MaxI, _L, _Pref1, _Pow1, _Pref2, _Pow2, Set) when I > MaxI ->
    Set;
iter_start(I, MaxI, L, Pref1, Pow1, Pref2, Pow2, Set) ->
    J = I + L,
    K = I + 2 * L,
    H1a = hash_sub(Pref1, Pow1, I, J, 1000000007),
    H1b = hash_sub(Pref1, Pow1, J, K, 1000000007),
    case H1a == H1b of
        true ->
            H2a = hash_sub(Pref2, Pow2, I, J, 1000000009),
            H2b = hash_sub(Pref2, Pow2, J, K, 1000000009),
            NewSet = case H2a == H2b of
                true -> maps:put({H1a, H2a}, true, Set);
                false -> Set
            end,
            iter_start(I + 1, MaxI, L, Pref1, Pow1, Pref2, Pow2, NewSet);
        false ->
            iter_start(I + 1, MaxI, L, Pref1, Pow1, Pref2, Pow2, Set)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec distinct_echo_substrings(text :: String.t()) :: integer
  def distinct_echo_substrings(text) do
    base = 91138233
    mod1 = 1_000_000_007
    mod2 = 1_000_000_009

    codes =
      text
      |> String.to_charlist()
      |> Enum.map(&(&1 - ?a + 1))

    n = length(codes)

    # prefix hashes and powers for mod1
    {pref1_list, _} =
      Enum.reduce(codes, {[0], 0}, fn c, {list, prev} ->
        h = rem(prev * base + c, mod1)
        {[h | list], h}
      end)

    pref1 = List.to_tuple(Enum.reverse(pref1_list))

    {pow1_list, _} =
      Enum.reduce(1..n, {[1], 1}, fn _, {list, prev} ->
        p = rem(prev * base, mod1)
        {[p | list], p}
      end)

    pow1 = List.to_tuple(Enum.reverse(pow1_list))

    # prefix hashes and powers for mod2
    {pref2_list, _} =
      Enum.reduce(codes, {[0], 0}, fn c, {list, prev} ->
        h = rem(prev * base + c, mod2)
        {[h | list], h}
      end)

    pref2 = List.to_tuple(Enum.reverse(pref2_list))

    {pow2_list, _} =
      Enum.reduce(1..n, {[1], 1}, fn _, {list, prev} ->
        p = rem(prev * base, mod2)
        {[p | list], p}
      end)

    pow2 = List.to_tuple(Enum.reverse(pow2_list))

    # helper to get hash of substring [l, r)
    get_hash = fn pref, l, r, pow, mod ->
      h_r = elem(pref, r)
      h_l = elem(pref, l)
      p = elem(pow, r - l)
      res = rem(h_r - rem(h_l * p, mod), mod)
      if res < 0, do: res + mod, else: res
    end

    hashes =
      for len <- 2..n, rem(len, 2) == 0,
          i <- 0..(n - len),
          half = div(len, 2),
          j = i + half,
          h1a = get_hash.(pref1, i, j, pow1, mod1),
          h1b = get_hash.(pref1, j, i + len, pow1, mod1),
          h1a == h1b,
          h2a = get_hash.(pref2, i, j, pow2, mod2),
          h2b = get_hash.(pref2, j, i + len, pow2, mod2),
          h2a == h2b do
        {h1a, h2a}
      end

    hashes |> MapSet.new() |> MapSet.size()
  end
end
```
