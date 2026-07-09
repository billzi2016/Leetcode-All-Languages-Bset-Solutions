# 1044. Longest Duplicate Substring

## Cpp

```cpp
class Solution {
public:
    string longestDupSubstring(string s) {
        int n = s.size();
        const long long mod1 = 1000000007LL;
        const long long mod2 = 1000000009LL;
        const long long base = 91138233LL; // random large base
        
        vector<long long> pow1(n + 1), pow2(n + 1);
        pow1[0] = pow2[0] = 1;
        for (int i = 1; i <= n; ++i) {
            pow1[i] = (pow1[i - 1] * base) % mod1;
            pow2[i] = (pow2[i - 1] * base) % mod2;
        }
        
        vector<long long> h1(n + 1), h2(n + 1);
        for (int i = 0; i < n; ++i) {
            h1[i + 1] = (h1[i] * base + s[i]) % mod1;
            h2[i + 1] = (h2[i] * base + s[i]) % mod2;
        }
        
        auto getHash = [&](int l, int r) -> pair<long long,long long> {
            // substring [l, r)
            long long x1 = (h1[r] - h1[l] * pow1[r - l]) % mod1;
            if (x1 < 0) x1 += mod1;
            long long x2 = (h2[r] - h2[l] * pow2[r - l]) % mod2;
            if (x2 < 0) x2 += mod2;
            return {x1, x2};
        };
        
        string ans = "";
        int low = 1, high = n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            unordered_map<unsigned long long, vector<int>> mp;
            bool found = false;
            for (int i = 0; i + mid <= n; ++i) {
                auto p = getHash(i, i + mid);
                unsigned long long key = ((unsigned long long)p.first << 32) ^ (unsigned long long)p.second;
                if (mp.count(key)) {
                    for (int idx : mp[key]) {
                        if (s.compare(idx, mid, s, i, mid) == 0) {
                            ans = s.substr(i, mid);
                            found = true;
                            break;
                        }
                    }
                    if (found) break;
                }
                mp[key].push_back(i);
            }
            if (found) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String longestDupSubstring(String s) {
        int n = s.length();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = s.charAt(i) - 'a' + 1;
        }
        final int base = 26;
        final int mod1 = 1000000007;
        final int mod2 = 1000000009;

        long[] pow1 = new long[n + 1];
        long[] pow2 = new long[n + 1];
        pow1[0] = pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow1[i] = (pow1[i - 1] * base) % mod1;
            pow2[i] = (pow2[i - 1] * base) % mod2;
        }

        int low = 1, high = n - 1;
        int startIdx = -1, maxLen = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int idx = check(mid, nums, base, mod1, mod2, pow1, pow2);
            if (idx != -1) { // found duplicate of length mid
                startIdx = idx;
                maxLen = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return startIdx == -1 ? "" : s.substring(startIdx, startIdx + maxLen);
    }

    private int check(int len, int[] nums, int base,
                      int mod1, int mod2,
                      long[] pow1, long[] pow2) {
        int n = nums.length;
        long hash1 = 0, hash2 = 0;
        for (int i = 0; i < len; i++) {
            hash1 = (hash1 * base + nums[i]) % mod1;
            hash2 = (hash2 * base + nums[i]) % mod2;
        }
        java.util.HashMap<Long, Integer> map = new java.util.HashMap<>();
        long key = (hash1 << 32) | (hash2 & 0xffffffffL);
        map.put(key, 0);

        for (int i = 1; i <= n - len; i++) {
            // remove leftmost character
            hash1 = (hash1 - nums[i - 1] * pow1[len - 1]) % mod1;
            if (hash1 < 0) hash1 += mod1;
            hash2 = (hash2 - nums[i - 1] * pow2[len - 1]) % mod2;
            if (hash2 < 0) hash2 += mod2;

            // add new rightmost character
            hash1 = (hash1 * base + nums[i + len - 1]) % mod1;
            hash2 = (hash2 * base + nums[i + len - 1]) % mod2;

            key = (hash1 << 32) | (hash2 & 0xffffffffL);
            Integer prevIdx = map.get(key);
            if (prevIdx != null) {
                // verify to avoid false positive due to hash collision
                // compare substrings directly
                // Since collisions are extremely rare with double hashing, this check is cheap
                // and guarantees correctness.
                // No need for extra loop if strings equal.
                // Use java substring comparison
                // Note: using String.regionMatches can be faster but simple equals works.
                // We'll use a manual compare to avoid creating substrings repeatedly.
                int p = prevIdx;
                boolean same = true;
                for (int k = 0; k < len; k++) {
                    if (nums[p + k] != nums[i + k]) {
                        same = false;
                        break;
                    }
                }
                if (same) return i;
            } else {
                map.put(key, i);
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        nums = [ord(c) - ord('a') + 1 for c in s]
        base = 256
        mod1 = 1000000007
        mod2 = 1000000009

        def search(L):
            if L == 0:
                return 0
            h1 = h2 = 0
            for i in range(L):
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2
            seen = {(h1, h2): 0}
            power1 = pow(base, L, mod1)
            power2 = pow(base, L, mod2)

            for start in range(1, n - L + 1):
                # remove leading char, add trailing char
                h1 = (h1 * base - nums[start - 1] * power1) % mod1
                h1 = (h1 + nums[start + L - 1]) % mod1
                h2 = (h2 * base - nums[start - 1] * power2) % mod2
                h2 = (h2 + nums[start + L - 1]) % mod2

                key = (h1, h2)
                if key in seen:
                    return start
                seen[key] = start
            return -1

        low, high = 1, n - 1
        ans_start, ans_len = 0, 0
        while low <= high:
            mid = (low + high) // 2
            idx = search(mid)
            if idx != -1:          # duplicate of length mid exists
                ans_start, ans_len = idx, mid
                low = mid + 1
            else:
                high = mid - 1

        return s[ans_start:ans_start + ans_len] if ans_len > 0 else ""
```

## Python3

```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return ""
        base = 256
        mod1 = 1000000007
        mod2 = 1000000009

        # precompute powers
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2

        # prefix hashes
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        for i, ch in enumerate(s):
            o = ord(ch)
            pref1[i + 1] = (pref1[i] * base + o) % mod1
            pref2[i + 1] = (pref2[i] * base + o) % mod2

        def search(L: int) -> int:
            """return start index of a duplicate substring of length L, or -1"""
            seen = {}
            for i in range(0, n - L + 1):
                cur1 = (pref1[i + L] - pref1[i] * pow1[L]) % mod1
                cur2 = (pref2[i + L] - pref2[i] * pow2[L]) % mod2
                key = (cur1, cur2)
                if key in seen:
                    j = seen[key]
                    # verify to avoid false positive due to hash collision
                    if s[j:j + L] == s[i:i + L]:
                        return i
                else:
                    seen[key] = i
            return -1

        lo, hi = 1, n - 1
        ans_start, ans_len = -1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = search(mid)
            if idx != -1:
                ans_start, ans_len = idx, mid
                lo = mid + 1
            else:
                hi = mid - 1

        return s[ans_start:ans_start + ans_len] if ans_len > 0 else ""
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef unsigned long long ull;

static const ull MOD1 = 1000000007ULL;
static const ull MOD2 = 1000000009ULL;
static const ull BASE = 256ULL;   // works for lowercase letters

struct Node {
    ull h1, h2;
    int idx;
};

static int cmpNode(const void *a, const void *b) {
    const struct Node *na = (const struct Node *)a;
    const struct Node *nb = (const struct Node *)b;
    if (na->h1 != nb->h1) return (na->h1 < nb->h1) ? -1 : 1;
    if (na->h2 != nb->h2) return (na->h2 < nb->h2) ? -1 : 1;
    return 0;
}

/* Return starting index of a duplicate substring of length L, or -1 if none */
static int checkLen(const char *s, int n, int L,
                    const ull *pref1, const ull *pref2,
                    const ull *pow1, const ull *pow2,
                    struct Node *buf) {
    int cnt = n - L + 1;
    for (int i = 0; i < cnt; ++i) {
        ull h1 = pref1[i + L] + MOD1 - (pref1[i] * pow1[L]) % MOD1;
        if (h1 >= MOD1) h1 -= MOD1;
        ull h2 = pref2[i + L] + MOD2 - (pref2[i] * pow2[L]) % MOD2;
        if (h2 >= MOD2) h2 -= MOD2;
        buf[i].h1 = h1;
        buf[i].h2 = h2;
        buf[i].idx = i;
    }
    qsort(buf, cnt, sizeof(struct Node), cmpNode);
    for (int i = 1; i < cnt; ++i) {
        if (buf[i].h1 == buf[i - 1].h1 && buf[i].h2 == buf[i - 1].h2) {
            int a = buf[i - 1].idx;
            int b = buf[i].idx;
            if (memcmp(s + a, s + b, L) == 0)
                return a < b ? a : b;   // any occurrence
        }
    }
    return -1;
}

char* longestDupSubstring(char* s) {
    int n = (int)strlen(s);
    if (n <= 1) {
        char *res = (char *)malloc(1);
        res[0] = '\0';
        return res;
    }

    /* Precompute powers and prefix hashes */
    ull *pow1 = (ull *)malloc((n + 1) * sizeof(ull));
    ull *pow2 = (ull *)malloc((n + 1) * sizeof(ull));
    ull *pref1 = (ull *)malloc((n + 1) * sizeof(ull));
    ull *pref2 = (ull *)malloc((n + 1) * sizeof(ull));

    pow1[0] = pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
        pow1[i] = (pow1[i - 1] * BASE) % MOD1;
        pow2[i] = (pow2[i - 1] * BASE) % MOD2;
    }

    pref1[0] = pref2[0] = 0;
    for (int i = 0; i < n; ++i) {
        int val = s[i] - 'a' + 1;   // map to 1..26
        pref1[i + 1] = (pref1[i] * BASE + val) % MOD1;
        pref2[i + 1] = (pref2[i] * BASE + val) % MOD2;
    }

    struct Node *buf = (struct Node *)malloc(n * sizeof(struct Node));

    int low = 1, high = n - 1;
    int bestLen = 0, bestPos = -1;

    while (low <= high) {
        int mid = (low + high) / 2;
        int pos = checkLen(s, n, mid, pref1, pref2, pow1, pow2, buf);
        if (pos != -1) {
            bestLen = mid;
            bestPos = pos;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    free(pow1);
    free(pow2);
    free(pref1);
    free(pref2);
    free(buf);

    if (bestLen == 0) {
        char *res = (char *)malloc(1);
        res[0] = '\0';
        return res;
    } else {
        char *res = (char *)malloc(bestLen + 1);
        memcpy(res, s + bestPos, bestLen);
        res[bestLen] = '\0';
        return res;
    }
}
```

## Csharp

```csharp
public class Solution {
    public string LongestDupSubstring(string s) {
        int n = s.Length;
        if (n == 0) return "";
        const long mod1 = 1000000007L;
        const long mod2 = 1000000009L;
        const long base1 = 91138233L;
        const long base2 = 97266353L;

        long[] pow1 = new long[n + 1];
        long[] pow2 = new long[n + 1];
        pow1[0] = 1;
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow1[i] = (pow1[i - 1] * base1) % mod1;
            pow2[i] = (pow2[i - 1] * base2) % mod2;
        }

        long[] h1 = new long[n + 1];
        long[] h2 = new long[n + 1];
        for (int i = 0; i < n; i++) {
            int val = s[i] - 'a' + 1;
            h1[i + 1] = (h1[i] * base1 + val) % mod1;
            h2[i + 1] = (h2[i] * base2 + val) % mod2;
        }

        int resultLen = 0;
        int resultStart = -1;

        int Check(int len) {
            var seen = new HashSet<(long, long)>();
            for (int i = 0; i <= n - len; i++) {
                long cur1 = (h1[i + len] - (h1[i] * pow1[len]) % mod1 + mod1) % mod1;
                long cur2 = (h2[i + len] - (h2[i] * pow2[len]) % mod2 + mod2) % mod2;
                var key = (cur1, cur2);
                if (!seen.Add(key)) {
                    return i; // duplicate found
                }
            }
            return -1;
        }

        int low = 1, high = n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int idx = Check(mid);
            if (idx != -1) {
                resultLen = mid;
                resultStart = idx;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return resultLen == 0 ? "" : s.Substring(resultStart, resultLen);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestDupSubstring = function(s) {
    const n = s.length;
    if (n <= 1) return "";
    const base = 256;
    const mod = 2147483647; // 2^31 - 1, fits in JS integer precision

    // convert chars to numbers (1..26)
    const nums = new Array(n);
    for (let i = 0; i < n; ++i) {
        nums[i] = s.charCodeAt(i) - 96;
    }

    // precompute powers of base modulo mod
    const power = new Array(n + 1);
    power[0] = 1;
    for (let i = 1; i <= n; ++i) {
        power[i] = (power[i - 1] * base) % mod;
    }

    // check if there is a duplicate substring of length L, return start index or -1
    const search = (L) => {
        let hash = 0;
        for (let i = 0; i < L; ++i) {
            hash = (hash * base + nums[i]) % mod;
        }
        const seen = new Map();
        seen.set(hash, [0]);

        for (let start = 1; start <= n - L; ++start) {
            // remove leading char
            const leftVal = (nums[start - 1] * power[L]) % mod;
            hash = (hash - leftVal + mod) % mod;
            // add trailing char
            hash = (hash * base + nums[start + L - 1]) % mod;

            if (seen.has(hash)) {
                const list = seen.get(hash);
                for (const prev of list) {
                    // verify to avoid false positive due to collision
                    let match = true;
                    for (let k = 0; k < L; ++k) {
                        if (s.charCodeAt(prev + k) !== s.charCodeAt(start + k)) {
                            match = false;
                            break;
                        }
                    }
                    if (match) return start;
                }
                list.push(start);
            } else {
                seen.set(hash, [start]);
            }
        }
        return -1;
    };

    let low = 1, high = n - 1;
    let bestStart = -1, bestLen = 0;

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const idx = search(mid);
        if (idx !== -1) {
            bestStart = idx;
            bestLen = mid;
            low = mid + 1; // try longer
        } else {
            high = mid - 1;
        }
    }

    return bestLen > 0 ? s.substring(bestStart, bestStart + bestLen) : "";
};
```

## Typescript

```typescript
function longestDupSubstring(s: string): string {
    const n = s.length;
    if (n <= 1) return "";
    const base = 256n;
    const mod = 1000000007n; // a large prime

    function check(len: number): number {
        if (len === 0) return 0;
        let hash = 0n;
        for (let i = 0; i < len; i++) {
            hash = (hash * base + BigInt(s.charCodeAt(i))) % mod;
        }
        const seen = new Map<bigint, number>();
        seen.set(hash, 0);

        // power = base^(len-1) % mod
        let power = 1n;
        for (let i = 0; i < len - 1; i++) {
            power = (power * base) % mod;
        }

        for (let start = 1; start + len <= n; start++) {
            const leftChar = BigInt(s.charCodeAt(start - 1));
            const rightChar = BigInt(s.charCodeAt(start + len - 1));

            // remove leftmost char
            hash = (hash - leftChar * power % mod + mod) % mod;
            // shift and add new char
            hash = (hash * base + rightChar) % mod;

            if (seen.has(hash)) {
                return start;
            }
            seen.set(hash, start);
        }
        return -1;
    }

    let low = 1, high = n - 1;
    let bestLen = 0, bestPos = -1;

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const pos = check(mid);
        if (pos !== -1) {
            bestLen = mid;
            bestPos = pos;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return bestLen === 0 ? "" : s.substring(bestPos, bestPos + bestLen);
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function longestDupSubstring($s) {
        $n = strlen($s);
        if ($n == 0) return "";
        $base = 256;
        $mod1 = 1000000007;
        $mod2 = 1000000009;

        // precompute powers
        $pow1 = array_fill(0, $n + 1, 0);
        $pow2 = array_fill(0, $n + 1, 0);
        $pow1[0] = 1;
        $pow2[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $pow1[$i] = (int)(($pow1[$i - 1] * $base) % $mod1);
            $pow2[$i] = (int)(($pow2[$i - 1] * $base) % $mod2);
        }

        $low = 1;
        $high = $n - 1;
        $ansStart = -1;
        $ansLen = 0;

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            $start = $this->search($mid, $s, $n, $base, $mod1, $mod2, $pow1, $pow2);
            if ($start != -1) {
                $ansStart = $start;
                $ansLen = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }

        return $ansLen == 0 ? "" : substr($s, $ansStart, $ansLen);
    }

    private function search($len, $s, $n, $base, $mod1, $mod2, $pow1, $pow2) {
        if ($len == 0) return -1;
        $h1 = 0;
        $h2 = 0;
        for ($i = 0; $i < $len; $i++) {
            $c = ord($s[$i]) - 96; // 'a' -> 1
            $h1 = (int)((($h1 * $base) + $c) % $mod1);
            $h2 = (int)((($h2 * $base) + $c) % $mod2);
        }
        $hashes = [];
        $key = $h1 . ':' . $h2;
        $hashes[$key] = 0;

        for ($i = 1; $i <= $n - $len; $i++) {
            $leftChar = ord($s[$i - 1]) - 96;
            $rightChar = ord($s[$i + $len - 1]) - 96;

            $h1 = (int)(($h1 - ($leftChar * $pow1[$len - 1]) % $mod1 + $mod1) % $mod1);
            $h1 = (int)((($h1 * $base) + $rightChar) % $mod1);

            $h2 = (int)(($h2 - ($leftChar * $pow2[$len - 1]) % $mod2 + $mod2) % $mod2);
            $h2 = (int)((($h2 * $base) + $rightChar) % $mod2);

            $key = $h1 . ':' . $h2;
            if (isset($hashes[$key])) {
                // double hash collision probability is negligible; return current index
                return $i;
            }
            $hashes[$key] = $i;
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func longestDupSubstring(_ s: String) -> String {
        let n = s.count
        if n <= 1 { return "" }
        // Convert string to array of Int values (ASCII codes)
        let bytes = Array(s.utf8)
        var nums = [Int64]()
        nums.reserveCapacity(n)
        for b in bytes {
            nums.append(Int64(b))
        }

        let base: Int64 = 256
        let mod1: Int64 = 1_000_000_007
        let mod2: Int64 = 1_000_000_009

        // Precompute powers of base modulo both mods
        var pow1 = [Int64](repeating: 0, count: n + 1)
        var pow2 = [Int64](repeating: 0, count: n + 1)
        pow1[0] = 1
        pow2[0] = 1
        for i in 1...n {
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2
        }

        // Helper: check if there is a duplicate substring of length L, return its start index if exists
        func search(_ L: Int) -> Int? {
            if L == 0 { return 0 }
            var h1: Int64 = 0
            var h2: Int64 = 0
            for i in 0..<L {
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2
            }
            var seen = [UInt64:Int]()
            let key0 = (UInt64(h1) << 32) | UInt64(h2)
            seen[key0] = 0

            let powerL1 = pow1[L - 1]
            let powerL2 = pow2[L - 1]

            for start in 1...n - L {
                // remove leftmost character
                h1 = (h1 - nums[start - 1] * powerL1 % mod1 + mod1) % mod1
                h2 = (h2 - nums[start - 1] * powerL2 % mod2 + mod2) % mod2
                // add new rightmost character
                h1 = (h1 * base + nums[start + L - 1]) % mod1
                h2 = (h2 * base + nums[start + L - 1]) % mod2

                let key = (UInt64(h1) << 32) | UInt64(h2)
                if let prev = seen[key] {
                    // verify to avoid false positive due to hash collision
                    var match = true
                    for k in 0..<L {
                        if nums[prev + k] != nums[start + k] {
                            match = false
                            break
                        }
                    }
                    if match { return start }
                } else {
                    seen[key] = start
                }
            }
            return nil
        }

        var left = 1
        var right = n - 1
        var ansStart = 0
        var ansLen = 0

        while left <= right {
            let mid = (left + right) / 2
            if let start = search(mid) {
                ansStart = start
                ansLen = mid
                left = mid + 1
            } else {
                right = mid - 1
            }
        }

        if ansLen == 0 { return "" }
        let startIdx = s.index(s.startIndex, offsetBy: ansStart)
        let endIdx = s.index(startIdx, offsetBy: ansLen)
        return String(s[startIdx..<endIdx])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestDupSubstring(s: String): String {
        val n = s.length
        if (n == 0) return ""
        val base = 256L
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

        val h1 = LongArray(n + 1)
        val h2 = LongArray(n + 1)
        for (i in 0 until n) {
            val c = (s[i].code - 'a'.code + 1).toLong()
            h1[i + 1] = (h1[i] * base + c) % mod1
            h2[i + 1] = (h2[i] * base + c) % mod2
        }

        fun getHash(l: Int, r: Int): Long {
            val cur1 = ((h1[r] - (h1[l] * pow1[r - l]) % mod1) + mod1) % mod1
            val cur2 = ((h2[r] - (h2[l] * pow2[r - l]) % mod2) + mod2) % mod2
            return (cur1 shl 32) + cur2
        }

        fun search(len: Int): Int {
            if (len == 0) return 0
            val seen = HashMap<Long, Int>()
            for (i in 0..n - len) {
                val key = getHash(i, i + len)
                val prev = seen[key]
                if (prev != null) {
                    // verify to avoid rare hash collision
                    if (s.regionMatches(prev, s, i, len)) {
                        return i
                    }
                } else {
                    seen[key] = i
                }
            }
            return -1
        }

        var low = 1
        var high = n - 1
        var start = -1
        var bestLen = 0
        while (low <= high) {
            val mid = (low + high) ushr 1
            val idx = search(mid)
            if (idx != -1) {
                start = idx
                bestLen = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }

        return if (start == -1) "" else s.substring(start, start + bestLen)
    }
}
```

## Dart

```dart
class Solution {
  String longestDupSubstring(String s) {
    const int mod1 = 1000000007;
    const int mod2 = 1000000009;
    const int base = 256;

    List<int> chars = s.codeUnits;
    int n = chars.length;

    // precompute powers
    List<int> pow1 = List.filled(n + 1, 0);
    List<int> pow2 = List.filled(n + 1, 0);
    pow1[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pow1[i] = (pow1[i - 1] * base) % mod1;
      pow2[i] = (pow2[i - 1] * base) % mod2;
    }

    // prefix hashes
    List<int> pref1 = List.filled(n + 1, 0);
    List<int> pref2 = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pref1[i + 1] = ((pref1[i] * base) + chars[i]) % mod1;
      pref2[i + 1] = ((pref2[i] * base) + chars[i]) % mod2;
    }

    int start = -1;
    int maxLen = 0;

    bool check(int len) {
      Set<int> seen = <int>{};
      for (int i = 0; i <= n - len; ++i) {
        int cur1 = pref1[i + len] -
            ((pref1[i] * pow1[len]) % mod1);
        if (cur1 < 0) cur1 += mod1;
        int cur2 = pref2[i + len] -
            ((pref2[i] * pow2[len]) % mod2);
        if (cur2 < 0) cur2 += mod2;

        int combined = (cur1 << 32) ^ cur2;
        if (seen.contains(combined)) {
          start = i;
          return true;
        }
        seen.add(combined);
      }
      return false;
    }

    int low = 1, high = n - 1;
    while (low <= high) {
      int mid = (low + high) >> 1;
      if (check(mid)) {
        maxLen = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return maxLen == 0 ? "" : s.substring(start, start + maxLen);
  }
}
```

## Golang

```go
func longestDupSubstring(s string) string {
    n := len(s)
    if n == 0 {
        return ""
    }
    const mod1 int64 = 1000000007
    const mod2 int64 = 1000000009
    const base int64 = 256

    pow1 := make([]int64, n+1)
    pow2 := make([]int64, n+1)
    pow1[0], pow2[0] = 1, 1
    for i := 1; i <= n; i++ {
        pow1[i] = (pow1[i-1] * base) % mod1
        pow2[i] = (pow2[i-1] * base) % mod2
    }

    pref1 := make([]int64, n+1)
    pref2 := make([]int64, n+1)
    for i := 0; i < n; i++ {
        c := int64(s[i])
        pref1[i+1] = (pref1[i]*base + c) % mod1
        pref2[i+1] = (pref2[i]*base + c) % mod2
    }

    getHash := func(l, r int) uint64 {
        h1 := (pref1[r] - (pref1[l]*pow1[r-l])%mod1 + mod1) % mod1
        h2 := (pref2[r] - (pref2[l]*pow2[r-l])%mod2 + mod2) % mod2
        return uint64(h1)<<32 | uint64(h2)
    }

    var ansStart, ansLen int

    check := func(L int) int {
        seen := make(map[uint64]int)
        for i := 0; i+L <= n; i++ {
            h := getHash(i, i+L)
            if prev, ok := seen[h]; ok {
                if s[prev:prev+L] == s[i:i+L] {
                    return i
                }
            } else {
                seen[h] = i
            }
        }
        return -1
    }

    low, high := 1, n-1
    for low <= high {
        mid := (low + high) / 2
        idx := check(mid)
        if idx != -1 {
            ansStart = idx
            ansLen = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    if ansLen == 0 {
        return ""
    }
    return s[ansStart : ansStart+ansLen]
}
```

## Ruby

```ruby
def longest_dup_substring(s)
  n = s.length
  return "" if n <= 1

  base = 256
  mod1 = 1_000_000_007
  mod2 = 1_000_000_009

  bytes = s.bytes
  pow1 = Array.new(n + 1, 0)
  pow2 = Array.new(n + 1, 0)
  pow1[0] = 1
  pow2[0] = 1
  (1..n).each do |i|
    pow1[i] = (pow1[i - 1] * base) % mod1
    pow2[i] = (pow2[i - 1] * base) % mod2
  end

  search = lambda do |len|
    return nil if len == 0
    h1 = 0
    h2 = 0
    (0...len).each do |i|
      h1 = (h1 * base + bytes[i]) % mod1
      h2 = (h2 * base + bytes[i]) % mod2
    end
    seen = {}
    seen[[h1, h2]] = 0

    (1..(n - len)).each do |i|
      h1 = (h1 - bytes[i - 1] * pow1[len - 1]) % mod1
      h1 = (h1 * base + bytes[i + len - 1]) % mod1
      h1 += mod1 if h1 < 0

      h2 = (h2 - bytes[i - 1] * pow2[len - 1]) % mod2
      h2 = (h2 * base + bytes[i + len - 1]) % mod2
      h2 += mod2 if h2 < 0

      key = [h1, h2]
      if seen.key?(key)
        prev = seen[key]
        return i if s[prev, len] == s[i, len]
      else
        seen[key] = i
      end
    end
    nil
  end

  low = 1
  high = n - 1
  best_start = 0
  best_len = 0

  while low <= high
    mid = (low + high) / 2
    idx = search.call(mid)
    if idx
      best_start = idx
      best_len = mid
      low = mid + 1
    else
      high = mid - 1
    end
  end

  return "" if best_len == 0
  s[best_start, best_len]
end
```

## Scala

```scala
object Solution {
    def longestDupSubstring(s: String): String = {
        val n = s.length
        if (n <= 1) return ""
        val base = 256L
        val mod1 = 1000000007L
        val mod2 = 1000000009L

        val h1 = new Array[Long](n + 1)
        val h2 = new Array[Long](n + 1)
        val pow1 = new Array[Long](n + 1)
        val pow2 = new Array[Long](n + 1)

        pow1(0) = 1L
        pow2(0) = 1L
        var i = 0
        while (i < n) {
            val c = s.charAt(i).toInt - 'a'.toInt + 1
            h1(i + 1) = (h1(i) * base + c) % mod1
            h2(i + 1) = (h2(i) * base + c) % mod2
            pow1(i + 1) = (pow1(i) * base) % mod1
            pow2(i + 1) = (pow2(i) * base) % mod2
            i += 1
        }

        import scala.collection.mutable

        def check(len: Int): Int = {
            val seen = mutable.HashMap[Long, Int]()
            var start = 0
            while (start + len <= n) {
                var hash1 = (h1(start + len) - h1(start) * pow1(len)) % mod1
                if (hash1 < 0) hash1 += mod1
                var hash2 = (h2(start + len) - h2(start) * pow2(len)) % mod2
                if (hash2 < 0) hash2 += mod2
                val key = (hash1 << 32) | hash2
                seen.get(key) match {
                    case Some(prev) => return start
                    case None => seen.put(key, start)
                }
                start += 1
            }
            -1
        }

        var low = 1
        var high = n - 1
        var ansLen = 0
        var ansIdx = -1

        while (low <= high) {
            val mid = low + (high - low) / 2
            val idx = check(mid)
            if (idx != -1) {
                ansLen = mid
                ansIdx = idx
                low = mid + 1
            } else {
                high = mid - 1
            }
        }

        if (ansLen == 0) "" else s.substring(ansIdx, ansIdx + ansLen)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_dup_substring(s: String) -> String {
        const BASE: u64 = 256;
        let bytes = s.as_bytes();
        let n = bytes.len();

        fn search(bytes: &[u8], len: usize, base: u64) -> Option<usize> {
            use std::collections::HashMap;
            if len == 0 {
                return Some(0);
            }
            let n = bytes.len();
            let mut hash: u64 = 0;
            for i in 0..len {
                hash = hash.wrapping_mul(base).wrapping_add(bytes[i] as u64);
            }
            // base^(len-1)
            let mut power: u64 = 1;
            for _ in 0..len - 1 {
                power = power.wrapping_mul(base);
            }

            let mut map: HashMap<u64, usize> = HashMap::new();
            map.insert(hash, 0);

            for i in 1..=n - len {
                // remove leading byte
                let left = (bytes[i - 1] as u64).wrapping_mul(power);
                hash = hash.wrapping_sub(left);
                hash = hash.wrapping_mul(base);
                hash = hash.wrapping_add(bytes[i + len - 1] as u64);

                if let Some(&prev) = map.get(&hash) {
                    if &bytes[prev..prev + len] == &bytes[i..i + len] {
                        return Some(i);
                    }
                }
                map.entry(hash).or_insert(i);
            }
            None
        }

        let mut left = 1usize;
        let mut right = n - 1;
        let mut ans_start = 0usize;
        let mut ans_len = 0usize;

        while left <= right {
            let mid = left + (right - left) / 2;
            if let Some(start) = search(bytes, mid, BASE) {
                ans_start = start;
                ans_len = mid;
                left = mid + 1;
            } else {
                if mid == 0 {
                    break;
                }
                right = mid - 1;
            }
        }

        if ans_len == 0 {
            "".to_string()
        } else {
            s[ans_start..ans_start + ans_len].to_string()
        }
    }
}
```

## Racket

```racket
(define/contract (longest-dup-substring s)
  (-> string? string?)
  (let* ([n (string-length s)]
         [base 256]
         [mod1 1000000007]
         [mod2 1000000009]
         [pow1 (make-vector (+ n 1) 0)]
         [pow2 (make-vector (+ n 1) 0)]
         [pref1 (make-vector (+ n 1) 0)]
         [pref2 (make-vector (+ n 1) 0)])
    ;; pre‑compute powers and prefix hashes
    (vector-set! pow1 0 1)
    (vector-set! pow2 0 1)
    (for ([i (in-range n)])
      (let* ([val (+ 1 (- (char->integer (string-ref s i))
                         (char->integer #\a)))])
        (vector-set! pow1 (add1 i)
                     (modulo (* (vector-ref pow1 i) base) mod1))
        (vector-set! pow2 (add1 i)
                     (modulo (* (vector-ref pow2 i) base) mod2))
        (vector-set! pref1 (add1 i)
                     (modulo (+ (* (vector-ref pref1 i) base) val) mod1))
        (vector-set! pref2 (add1 i)
                     (modulo (+ (* (vector-ref pref2 i) base) val) mod2))))
    ;; helper: check if a duplicate of length k exists, return one such substring or #f
    (define (check k)
      (if (= k 0) "" #f)
      (let ([seen (make-hash)]
            [found #f])
        (let loop ((i 0))
          (when (and (< i (- n k)) (not found))
            (let* ([j (+ i k)]
                   [h1 (modulo (- (vector-ref pref1 j)
                                 (* (vector-ref pref1 i) (vector-ref pow1 k))) mod1)]
                   [h2 (modulo (- (vector-ref pref2 j)
                                 (* (vector-ref pref2 i) (vector-ref pow2 k))) mod2)]
                   [key (cons h1 h2)])
              (if (hash-has-key? seen key)
                  (let ([prev (hash-ref seen key)])
                    (when (for/and ([off (in-range k)])
                            (char=? (string-ref s (+ i off))
                                    (string-ref s (+ prev off))))
                      (set! found (substring s i (+ i k)))))
                  (hash-set! seen key i)))
            (loop (add1 i))))
        found))
    ;; binary search for maximal length
    (let loop ((lo 0) (hi n) (best ""))
      (if (= lo hi)
          best
          (let* ([mid (quotient (+ lo hi 1) 2)]   ; ceil((lo+hi)/2)
                 [cand (check mid)])
            (if cand
                (loop mid hi cand)
                (loop lo (- mid 1) best)))))))
```

## Erlang

```erlang
-module(solution).
-export([longest_dup_substring/1]).
-define(BASE, 256).
-define(MOD1, 1000000007).
-define(MOD2, 1000000009).

-spec longest_dup_substring(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
longest_dup_substring(S) ->
    List = binary:bin_to_list(S),
    N = length(List),
    case N of
        0 -> <<>>;
        1 -> <<>>
    end,
    {Pref1, Pref2, Pow1, Pow2} = build_arrays(List),
    {AnsLen, AnsStart} = binary_search(1, N - 1, N, Pref1, Pref2, Pow1, Pow2, 0, -1),
    case AnsLen of
        0 -> <<>>;
        _ -> binary:part(S, AnsStart, AnsLen)
    end.

build_arrays(List) ->
    Base = ?BASE,
    Mod1 = ?MOD1,
    Mod2 = ?MOD2,
    FoldFun =
        fun(C, {P1Acc, P2Acc, W1Acc, W2Acc, PrevPref1, PrevPref2, PrevPow1, PrevPow2}) ->
            NewPref1 = (PrevPref1 * Base + C) rem Mod1,
            NewPref2 = (PrevPref2 * Base + C) rem Mod2,
            NewPow1  = (PrevPow1 * Base) rem Mod1,
            NewPow2  = (PrevPow2 * Base) rem Mod2,
            {[NewPref1 | P1Acc],
             [NewPref2 | P2Acc],
             [NewPow1  | W1Acc],
             [NewPow2  | W2Acc],
             NewPref1, NewPref2, NewPow1, NewPow2}
        end,
    {P1Rev, P2Rev, W1Rev, W2Rev, _, _, _, _} =
        lists:foldl(FoldFun, {[], [], [], [], 0, 0, 1, 1}, List),
    Pref1 = list_to_tuple(lists:reverse([0 | P1Rev])),
    Pref2 = list_to_tuple(lists:reverse([0 | P2Rev])),
    Pow1  = list_to_tuple(lists:reverse([1 | W1Rev])),
    Pow2  = list_to_tuple(lists:reverse([1 | W2Rev])),
    {Pref1, Pref2, Pow1, Pow2}.

hash(Pref, Pow, L, Len, Mod) ->
    R = L + Len,
    H1 = element(R + 1, Pref),
    H0 = element(L + 1, Pref),
    P  = element(Len + 1, Pow),
    ((H1 - (H0 * P) rem Mod) + Mod) rem Mod.

exists(K, N, Pref1, Pref2, Pow1, Pow2) ->
    exists_loop(0, K, N, Pref1, Pref2, Pow1, Pow2, #{}).

exists_loop(I, K, N, Pref1, Pref2, Pow1, Pow2, Map) when I =< N - K ->
    H1 = hash(Pref1, Pow1, I, K, ?MOD1),
    H2 = hash(Pref2, Pow2, I, K, ?MOD2),
    Key = {H1, H2},
    case maps:is_key(Key, Map) of
        true -> {true, maps:get(Key, Map)};
        false ->
            NewMap = Map#{Key => I},
            exists_loop(I + 1, K, N, Pref1, Pref2, Pow1, Pow2, NewMap)
    end;
exists_loop(_, _, _, _, _, _, _, _) -> false.

binary_search(Low, High, N, Pref1, Pref2, Pow1, Pow2, AnsLen, AnsStart) when Low =< High ->
    Mid = (Low + High) div 2,
    case exists(Mid, N, Pref1, Pref2, Pow1, Pow2) of
        {true, Start} ->
            binary_search(Mid + 1, High, N, Pref1, Pref2, Pow1, Pow2, Mid, Start);
        false ->
            binary_search(Low, Mid - 1, N, Pref1, Pref2, Pow1, Pow2, AnsLen, AnsStart)
    end;
binary_search(_, _, _, _, _, _, _, AnsLen, AnsStart) -> {AnsLen, AnsStart}.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_dup_substring(s :: String.t) :: String.t
  def longest_dup_substring(s) do
    n = byte_size(s)

    if n <= 1 do
      ""
    else
      base1 = 91_138_233
      mod1 = 1_000_000_007
      base2 = 97_266_353
      mod2 = 1_000_000_009

      pow1 = build_pow(base1, mod1, n)
      pow2 = build_pow(base2, mod2, n)

      pref1 = build_prefix(s, base1, mod1)
      pref2 = build_prefix(s, base2, mod2)

      {start, len} =
        binary_search(
          s,
          1,
          n - 1,
          pow1,
          pow2,
          pref1,
          pref2,
          mod1,
          mod2,
          -1,
          0
        )

      if len == 0 do
        ""
      else
        :binary.part(s, start, len)
      end
    end
  end

  defp build_pow(base, mod, n) do
    list =
      Enum.reduce(0..n, [1], fn i, acc ->
        if i == 0 do
          acc
        else
          prev = hd(acc)
          [rem(prev * base, mod) | acc]
        end
      end)

    :array.from_list(Enum.reverse(list))
  end

  defp build_prefix(s, base, mod) do
    n = byte_size(s)

    {hashes, _} =
      Enum.map_reduce(0..(n - 1), 0, fn i, prev ->
        val = :binary.at(s, i)
        h = rem(prev * base + val, mod)
        {h, h}
      end)

    pref_list = [0 | hashes]
    :array.from_list(pref_list)
  end

  defp sub_hash(pref_arr, pow_arr, l, len, mod) do
    a = :array.get(l, pref_arr)
    b = :array.get(l + len, pref_arr)
    p = :array.get(len, pow_arr)
    rem(b - rem(a * p, mod) + mod, mod)
  end

  defp check(s, len, pow1, pow2, pref1, pref2, mod1, mod2) do
    n = byte_size(s)

    max_start = n - len

    result =
      Enum.reduce_while(0..max_start, %{}, fn i, acc ->
        h1 = sub_hash(pref1, pow1, i, len, mod1)
        h2 = sub_hash(pref2, pow2, i, len, mod2)
        key = {h1, h2}

        case Map.get(acc, key) do
          nil ->
            {:cont, Map.put(acc, key, i)}

          prev_i ->
            if :binary.part(s, i, len) == :binary.part(s, prev_i, len) do
              {:halt, i}
            else
              {:cont, Map.put(acc, key, i)}
            end
        end
      end)

    case result do
      %{} -> nil
      i when is_integer(i) -> i
    end
  end

  defp binary_search(
         s,
         low,
         high,
         pow1,
         pow2,
         pref1,
         pref2,
         mod1,
         mod2,
         ans_start,
         ans_len
       ) do
    if low > high do
      {ans_start, ans_len}
    else
      mid = div(low + high, 2)

      start = check(s, mid, pow1, pow2, pref1, pref2, mod1, mod2)

      if start != nil do
        binary_search(
          s,
          mid + 1,
          high,
          pow1,
          pow2,
          pref1,
          pref2,
          mod1,
          mod2,
          start,
          mid
        )
      else
        binary_search(
          s,
          low,
          mid - 1,
          pow1,
          pow2,
          pref1,
          pref2,
          mod1,
          mod2,
          ans_start,
          ans_len
        )
      end
    end
  end
end
```
