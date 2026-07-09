# 3518. Smallest Palindromic Rearrangement II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // compute C(n,k) capped at limit+1
    unsigned long long combCapped(int n, int k, unsigned long long limit) {
        if (k < 0 || k > n) return 0;
        if (k == 0 || k == n) return 1;
        if (k > n - k) k = n - k;
        __int128 res = 1;
        for (int i = 1; i <= k; ++i) {
            res = res * (n - k + i);
            res /= i;
            if (res > limit) return limit + 1;
        }
        return (unsigned long long)res;
    }

    // total permutations of remaining half counts, capped at limit+1
    unsigned long long totalPerm(const vector<int>& cnt, unsigned long long limit) {
        int total = 0;
        for (int c : cnt) total += c;
        unsigned long long res = 1;
        int remain = total;
        for (int c : cnt) {
            if (c == 0) continue;
            unsigned long long comb = combCapped(remain, c, limit);
            if (comb > limit) return limit + 1;
            if (res > limit / comb) return limit + 1;
            res *= comb;
            if (res > limit) return limit + 1;
            remain -= c;
        }
        return res;
    }

    string smallestPalindrome(string s, int k) {
        vector<int> freq(26,0);
        for(char ch: s) freq[ch-'a']++;
        vector<int> halfCnt(26,0);
        char midChar = 0;
        for(int i=0;i<26;++i){
            halfCnt[i] = freq[i]/2;
            if(freq[i]%2) midChar = 'a'+i;
        }
        int halfLen = s.size()/2;
        unsigned long long total = totalPerm(halfCnt, (unsigned long long)k);
        if(total < (unsigned long long)k) return "";
        string left;
        unsigned long long kk = k;
        for(int pos=0; pos<halfLen; ++pos){
            for(int c=0;c<26;++c){
                if(halfCnt[c]==0) continue;
                halfCnt[c]--;
                unsigned long long cnt = totalPerm(halfCnt, kk);
                if(cnt >= kk){
                    left.push_back('a'+c);
                    break;
                }else{
                    kk -= cnt;
                    halfCnt[c]++;
                }
            }
        }
        string right = left;
        reverse(right.begin(), right.end());
        string ans = left;
        if(midChar) ans.push_back(midChar);
        ans += right;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String smallestPalindrome(String s, int k) {
        int n = s.length();
        int[] freq = new int[26];
        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
        }

        // middle character if length is odd
        String mid = "";
        for (int i = 0; i < 26; i++) {
            if ((freq[i] & 1) == 1) {
                mid = String.valueOf((char) ('a' + i));
                break;
            }
        }

        int halfLen = n / 2;
        int[] halfCnt = new int[26];
        for (int i = 0; i < 26; i++) {
            halfCnt[i] = freq[i] / 2;
        }

        // precompute factorials up to halfLen
        java.math.BigInteger[] fact = new java.math.BigInteger[halfLen + 1];
        fact[0] = java.math.BigInteger.ONE;
        for (int i = 1; i <= halfLen; i++) {
            fact[i] = fact[i - 1].multiply(java.math.BigInteger.valueOf(i));
        }

        // total number of distinct palindromes
        int[] origHalf = halfCnt.clone();
        java.math.BigInteger totalWays = multinomial(origHalf, halfLen, fact);
        if (totalWays.compareTo(java.math.BigInteger.valueOf(k)) < 0) {
            return "";
        }

        StringBuilder left = new StringBuilder();
        int remainingTotal = halfLen;
        long kk = k; // mutable copy

        for (int pos = 0; pos < halfLen; pos++) {
            boolean placed = false;
            for (int c = 0; c < 26; c++) {
                if (halfCnt[c] == 0) continue;
                halfCnt[c]--;
                int rem = remainingTotal - 1;
                java.math.BigInteger ways = multinomial(halfCnt, rem, fact);
                if (ways.compareTo(java.math.BigInteger.valueOf(kk)) >= 0) {
                    left.append((char) ('a' + c));
                    remainingTotal = rem;
                    placed = true;
                    break;
                } else {
                    kk -= ways.longValue(); // ways < kk <= 1e6, safe to cast
                    halfCnt[c]++; // revert
                }
            }
            if (!placed) { // should not happen
                return "";
            }
        }

        String leftStr = left.toString();
        StringBuilder sb = new StringBuilder();
        sb.append(leftStr);
        sb.append(mid);
        sb.append(new StringBuilder(leftStr).reverse());
        return sb.toString();
    }

    private static java.math.BigInteger multinomial(int[] cnt, int total,
                                                    java.math.BigInteger[] fact) {
        java.math.BigInteger res = fact[total];
        for (int c : cnt) {
            if (c > 1) { // factorial of 0 or 1 is 1
                res = res.divide(fact[c]);
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        from collections import Counter
        from math import comb

        freq = Counter(s)
        odd_char = ''
        half_counts = [0] * 26
        for ch, cnt in freq.items():
            if cnt % 2 == 1:
                odd_char = ch
            half_counts[ord(ch) - 97] = cnt // 2

        total_half = sum(half_counts)

        def perms(cnts, limit):
            # multinomial coefficient with early stop at limit+1
            rem = sum(cnts)
            res = 1
            for c in cnts:
                if c == 0:
                    continue
                res *= comb(rem, c)
                if res > limit:
                    return limit + 1
                rem -= c
            return res

        # check total number of distinct palindromes
        if perms(half_counts, k) < k:
            return ""

        half_res = []
        for _ in range(total_half):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                half_counts[i] -= 1
                cnt = perms(half_counts, k)
                if cnt >= k:
                    half_res.append(chr(i + 97))
                    break
                else:
                    k -= cnt
                    half_counts[i] += 1
        left = ''.join(half_res)
        right = left[::-1]
        return left + odd_char + right
```

## Python3

```python
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        half_counts = [c // 2 for c in freq]
        mid_char = ''
        for i, c in enumerate(freq):
            if c % 2 == 1:
                mid_char = chr(97 + i)
                break

        total_len = sum(half_counts)

        def count_perms(cnts, remaining, limit):
            res = 1
            for cnt in cnts:
                if cnt == 0:
                    continue
                comb = math.comb(remaining, cnt)
                if res > limit // comb:
                    return limit + 1
                res *= comb
                remaining -= cnt
                if res > limit:
                    return limit + 1
            return res

        # check total number of palindromes
        if count_perms(half_counts, total_len, k) < k:
            return ""

        half_res = []
        for pos in range(total_len):
            for idx in range(26):
                if half_counts[idx] == 0:
                    continue
                half_counts[idx] -= 1
                cnt = count_perms(half_counts, total_len - pos - 1, k)
                if cnt >= k:
                    half_res.append(chr(97 + idx))
                    break
                else:
                    k -= cnt
                    half_counts[idx] += 1
            else:
                return ""

        left = ''.join(half_res)
        right = left[::-1]
        return left + mid_char + right
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int spf[5005];
static int primes[700];
static int prime_cnt = 0;
static int spf_ready = 0;

static void build_spf(void) {
    for (int i = 2; i <= 5000; ++i) spf[i] = i;
    for (int i = 2; i * i <= 5000; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= 5000; j += i)
                if (spf[j] == j) spf[j] = i;
        }
    }
    for (int i = 2; i <= 5000; ++i)
        if (spf[i] == i) primes[prime_cnt++] = i;
    spf_ready = 1;
}

/* count permutations of multiset given by cnt[26], total length len.
   Returns a value capped at LIMIT (greater than any possible k). */
static unsigned long long countPerm(int cnt[26], int len) {
    const unsigned long long LIMIT = 2000000000ULL; // > max k
    static int expcnt[5005];
    memset(expcnt, 0, sizeof(expcnt));

    // add factorial(len)
    for (int i = 2; i <= len; ++i) {
        int x = i;
        while (x > 1) {
            int p = spf[x];
            int c = 0;
            while (x % p == 0) { x /= p; ++c; }
            expcnt[p] += c;
        }
    }

    // subtract factorials of each cnt[i]
    for (int i = 0; i < 26; ++i) {
        int c = cnt[i];
        for (int j = 2; j <= c; ++j) {
            int x = j;
            while (x > 1) {
                int p = spf[x];
                int cc = 0;
                while (x % p == 0) { x /= p; ++cc; }
                expcnt[p] -= cc;
            }
        }
    }

    unsigned long long res = 1ULL;
    for (int idx = 0; idx < prime_cnt; ++idx) {
        int p = primes[idx];
        int e = expcnt[p];
        while (e-- > 0) {
            if (res > LIMIT / (unsigned long long)p) return LIMIT;
            res *= (unsigned long long)p;
        }
    }
    return res;
}

char* smallestPalindrome(char* s, int k) {
    if (!spf_ready) build_spf();

    int n = strlen(s);
    int freq[26] = {0};
    for (int i = 0; i < n; ++i) freq[s[i]-'a']++;

    // Determine middle character (if any)
    char midChar = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] % 2 == 1) {
            midChar = 'a' + i;
            break;
        }
    }

    int halfCnt[26];
    int halfLen = 0;
    for (int i = 0; i < 26; ++i) {
        halfCnt[i] = freq[i] / 2;
        halfLen += halfCnt[i];
    }

    unsigned long long totalPerm = countPerm(halfCnt, halfLen);
    if ((unsigned long long)k > totalPerm) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    char* left = (char*)malloc(halfLen + 1);
    int pos = 0;
    while (pos < halfLen) {
        for (int c = 0; c < 26; ++c) {
            if (halfCnt[c] == 0) continue;
            halfCnt[c]--;
            unsigned long long cntPerm = countPerm(halfCnt, halfLen - pos - 1);
            if ((unsigned long long)k <= cntPerm) {
                left[pos++] = 'a' + c;
                break;
            } else {
                k -= (int)cntPerm;
                halfCnt[c]++; // restore
            }
        }
    }
    left[halfLen] = '\0';

    int totalSize = n;
    char* ans = (char*)malloc(totalSize + 1);
    int idx = 0;
    for (int i = 0; i < halfLen; ++i) ans[idx++] = left[i];
    if (midChar) ans[idx++] = midChar;
    for (int i = halfLen - 1; i >= 0; --i) ans[idx++] = left[i];
    ans[totalSize] = '\0';

    free(left);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Text;

public class Solution {
    public string SmallestPalindrome(string s, int k) {
        int[] freq = new int[26];
        foreach (char ch in s) freq[ch - 'a']++;

        int oddIdx = -1;
        for (int i = 0; i < 26; i++) {
            if ((freq[i] & 1) == 1) oddIdx = i;
        }

        int[] halfCnt = new int[26];
        int totalHalf = 0;
        for (int i = 0; i < 26; i++) {
            halfCnt[i] = freq[i] >> 1;
            totalHalf += halfCnt[i];
        }

        StringBuilder left = new StringBuilder();
        long curK = k;

        for (int pos = 0; pos < totalHalf; pos++) {
            bool placed = false;
            for (int c = 0; c < 26; c++) {
                if (halfCnt[c] == 0) continue;
                halfCnt[c]--;
                long cnt = CountPermutations(halfCnt, totalHalf - pos - 1, curK);
                if (cnt >= curK) {
                    left.Append((char)('a' + c));
                    placed = true;
                    break;
                } else {
                    curK -= cnt;
                    halfCnt[c]++; // revert
                }
            }
            if (!placed) return "";
        }

        StringBuilder result = new StringBuilder();
        result.Append(left);
        if (oddIdx != -1) result.Append((char)('a' + oddIdx));
        for (int i = left.Length - 1; i >= 0; i--) result.Append(left[i]);
        return result.ToString();
    }

    private static long CountPermutations(int[] cnt, int remaining, long limit) {
        long res = 1;
        int rem = remaining;
        for (int i = 0; i < 26; i++) {
            int c = cnt[i];
            if (c == 0) continue;
            long comb = NCrCapped(rem, c, limit);
            res = MulCap(res, comb, limit);
            if (res > limit) return limit + 1;
            rem -= c;
        }
        return res;
    }

    private static long NCrCapped(int n, int r, long limit) {
        if (r < 0 || r > n) return 0;
        if (r > n - r) r = n - r;
        long result = 1;
        for (int i = 1; i <= r; i++) {
            long numerator = n - r + i;
            long denominator = i;

            long g = Gcd(numerator, denominator);
            numerator /= g;
            denominator /= g;

            long g2 = Gcd(result, denominator);
            result /= g2;
            denominator /= g2;

            if (result > limit / numerator) return limit + 1;
            result *= numerator;
        }
        return result;
    }

    private static long MulCap(long a, long b, long limit) {
        if (a == 0 || b == 0) return 0;
        if (a > limit / b) return limit + 1;
        long res = a * b;
        return res > limit ? limit + 1 : res;
    }

    private static long Gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var smallestPalindrome = function(s, k) {
    const n = s.length;
    const freq = new Array(26).fill(0);
    for (let ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    let middleChar = '';
    for (let i = 0; i < 26; i++) {
        if (freq[i] % 2 === 1) {
            middleChar = String.fromCharCode(97 + i);
            break;
        }
    }
    const halfCnt = new Array(26).fill(0);
    let totalHalf = 0;
    for (let i = 0; i < 26; i++) {
        halfCnt[i] = Math.floor(freq[i] / 2);
        totalHalf += halfCnt[i];
    }

    // precompute factorials as BigInt
    const fact = new Array(totalHalf + 1);
    fact[0] = 1n;
    for (let i = 1; i <= totalHalf; i++) {
        fact[i] = fact[i - 1] * BigInt(i);
    }

    const countPermutations = (cntArr, remaining) => {
        let numerator = fact[remaining];
        let denom = 1n;
        for (let i = 0; i < 26; i++) {
            denom *= fact[cntArr[i]];
        }
        return numerator / denom;
    };

    const totalPerm = countPermutations(halfCnt, totalHalf);
    let K = BigInt(k);
    if (totalPerm < K) return "";

    let left = [];
    for (let pos = 0; pos < totalHalf; pos++) {
        for (let c = 0; c < 26; c++) {
            if (halfCnt[c] === 0) continue;
            halfCnt[c]--;
            const remaining = totalHalf - pos - 1;
            const cnt = countPermutations(halfCnt, remaining);
            if (cnt >= K) {
                left.push(String.fromCharCode(97 + c));
                break;
            } else {
                K -= cnt;
                halfCnt[c]++; // restore and try next char
            }
        }
    }

    const leftStr = left.join('');
    const rightStr = leftStr.split('').reverse().join('');
    return middleChar ? leftStr + middleChar + rightStr : leftStr + rightStr;
};
```

## Typescript

```typescript
function smallestPalindrome(s: string, k: number): string {
    const n = s.length;
    const freq = new Array(26).fill(0);
    for (let ch of s) freq[ch.charCodeAt(0) - 97]++;

    let middleChar = '';
    for (let i = 0; i < 26; i++) {
        if (freq[i] % 2 === 1) {
            middleChar = String.fromCharCode(97 + i);
            break;
        }
    }

    const halfCnt = new Array(26).fill(0);
    let totalHalf = 0;
    for (let i = 0; i < 26; i++) {
        halfCnt[i] = Math.floor(freq[i] / 2);
        totalHalf += halfCnt[i];
    }

    // helper: multiply with cap
    const mulCap = (a: number, b: number, limit: number): number => {
        if (a > limit || b > limit) return limit + 1;
        const prod = a * b;
        return prod > limit ? limit + 1 : prod;
    };

    // helper: nCr with early stop when exceeding limit
    const nCrCap = (nVal: number, kVal: number, limit: number): number => {
        if (kVal < 0 || kVal > nVal) return 0;
        if (kVal === 0 || kVal === nVal) return 1;
        let k = Math.min(kVal, nVal - kVal);
        let res = 1;
        for (let i = 1; i <= k; i++) {
            res = res * (nVal - k + i) / i;
            if (res > limit) return limit + 1;
        }
        // result is integer and ≤ limit, safe to round
        return Math.round(res);
    };

    // helper: count permutations of remaining multiset with cap = k
    const countPerm = (cnts: number[], total: number, limit: number): number => {
        let remaining = total;
        let ans = 1;
        for (let i = 0; i < 26; i++) {
            const c = cnts[i];
            if (c === 0) continue;
            const comb = nCrCap(remaining, c, limit);
            ans = mulCap(ans, comb, limit);
            if (ans > limit) return limit + 1;
            remaining -= c;
        }
        return ans;
    };

    // total number of distinct palindromes
    const totalPerm = countPerm(halfCnt, totalHalf, k);
    if (totalPerm < k) return "";

    const halfBuilder: string[] = [];
    for (let pos = 0; pos < totalHalf; pos++) {
        for (let i = 0; i < 26; i++) {
            if (halfCnt[i] === 0) continue;
            halfCnt[i]--;
            const cnt = countPerm(halfCnt, totalHalf - pos - 1, k);
            if (cnt >= k) {
                halfBuilder.push(String.fromCharCode(97 + i));
                break;
            } else {
                k -= cnt;
                halfCnt[i]++; // revert
            }
        }
    }

    const left = halfBuilder.join('');
    const right = left.split('').reverse().join('');
    return left + middleChar + right;
}
```

## Php

```php
class Solution {
    private $limit;

    private function combCapped(int $n, int $r): int {
        $limit = $this->limit;
        if ($r < 0 || $r > $n) return 0;
        if ($r == 0 || $r == $n) return 1;
        $r = min($r, $n - $r);
        $res = 1.0;
        for ($i = 1; $i <= $r; $i++) {
            $res *= ($n - $r + $i) / $i;
            if ($res > $limit) return $limit + 1;
        }
        return (int)floor($res + 1e-9);
    }

    private function totalPerm(array $counts): int {
        $limit = $this->limit;
        $total = 0;
        $res = 1.0;
        foreach ($counts as $c) {
            if ($c == 0) continue;
            $comb = $this->combCapped($total + $c, $c);
            $res *= $comb;
            if ($res > $limit) return $limit + 1;
            $total += $c;
        }
        return (int)floor($res + 1e-9);
    }

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function smallestPalindrome(string $s, int $k): string {
        $this->limit = $k;
        $freq = array_fill(0, 26, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $freq[ord($s[$i]) - 97]++;
        }

        $mid = '';
        $halfCounts = [];
        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] % 2 == 1) {
                $mid = chr(97 + $i);
            }
            $halfCounts[$i] = intdiv($freq[$i], 2);
        }

        $L = array_sum($halfCounts);
        $total = $this->totalPerm($halfCounts);
        if ($total < $k) return "";

        $firstHalf = '';
        for ($pos = 0; $pos < $L; $pos++) {
            for ($c = 0; $c < 26; $c++) {
                if ($halfCounts[$c] == 0) continue;
                $halfCounts[$c]--;
                $cnt = $this->totalPerm($halfCounts);
                if ($cnt >= $k) {
                    $firstHalf .= chr(97 + $c);
                    break;
                } else {
                    $k -= $cnt;
                    $halfCounts[$c]++;
                }
            }
        }

        return $firstHalf . $mid . strrev($firstHalf);
    }
}
```

## Swift

```swift
class Solution {
    private let INF = 1_000_001

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a, y = b
        while y != 0 {
            let t = x % y
            x = y
            y = t
        }
        return x
    }

    private func comb(_ n: Int, _ rInput: Int) -> Int {
        if rInput < 0 || rInput > n { return 0 }
        var r = min(rInput, n - rInput)
        if r == 0 { return 1 }
        var numerator = [Int]()
        for i in 0..<r {
            numerator.append(n - i)
        }
        var denominator = [Int]()
        for i in 1...r {
            denominator.append(i)
        }
        for i in 0..<denominator.count {
            var d = denominator[i]
            if d == 1 { continue }
            for j in 0..<numerator.count {
                let g = gcd(numerator[j], d)
                if g > 1 {
                    numerator[j] /= g
                    d /= g
                    if d == 1 { break }
                }
            }
            denominator[i] = d // should become 1
        }
        var result = 1
        for v in numerator {
            if result > INF / v { return INF }
            result *= v
        }
        return result
    }

    private func countPermutations(_ counts: [Int]) -> Int {
        var total = counts.reduce(0, +)
        var res = 1
        for cnt in counts where cnt > 0 {
            let c = comb(total, cnt)
            if c >= INF { return INF }
            if res > INF / c { return INF }
            res *= c
            total -= cnt
        }
        return res
    }

    func smallestPalindrome(_ s: String, _ kInput: Int) -> String {
        var freq = [Int](repeating: 0, count: 26)
        for scalar in s.unicodeScalars {
            let idx = Int(scalar.value - 97)
            freq[idx] += 1
        }

        var oddIdx = -1
        for i in 0..<26 where freq[i] % 2 == 1 {
            oddIdx = i
            break
        }

        var halfCounts = [Int](repeating: 0, count: 26)
        var totalHalf = 0
        for i in 0..<26 {
            halfCounts[i] = freq[i] / 2
            totalHalf += halfCounts[i]
        }

        if totalHalf == 0 { // string length is 1
            return kInput == 1 ? s : ""
        }

        var k = kInput
        var resultHalf = ""

        var counts = halfCounts
        for _ in 0..<totalHalf {
            var placed = false
            for cIdx in 0..<26 where counts[cIdx] > 0 {
                counts[cIdx] -= 1
                let cnt = countPermutations(counts)
                if cnt >= k {
                    resultHalf.append(Character(UnicodeScalar(cIdx + 97)!))
                    placed = true
                    break
                } else {
                    k -= cnt
                    counts[cIdx] += 1
                }
            }
            if !placed { return "" } // not enough permutations
        }

        var middle = ""
        if oddIdx != -1 {
            middle = String(Character(UnicodeScalar(oddIdx + 97)!))
        }

        let right = String(resultHalf.reversed())
        return resultHalf + middle + right
    }
}
```

## Kotlin

```kotlin
import java.math.BigInteger

class Solution {
    fun smallestPalindrome(s: String, k: Int): String {
        val n = s.length
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }

        var middleChar: Char? = null
        if (n % 2 == 1) {
            for (i in 0 until 26) {
                if (freq[i] % 2 == 1) {
                    middleChar = ('a' + i)
                    break
                }
            }
        }

        val halfCnt = IntArray(26)
        var halfLen = 0
        for (i in 0 until 26) {
            halfCnt[i] = freq[i] / 2
            halfLen += halfCnt[i]
        }

        // precompute factorials up to halfLen
        val fact = Array(halfLen + 1) { BigInteger.ONE }
        for (i in 1..halfLen) {
            fact[i] = fact[i - 1].multiply(BigInteger.valueOf(i.toLong()))
        }

        fun countPerm(cnt: IntArray, rem: Int, limit: Long): Long {
            var denom = BigInteger.ONE
            for (c in cnt) {
                if (c > 0) denom = denom.multiply(fact[c])
            }
            val res = fact[rem].divide(denom)
            return if (res.compareTo(BigInteger.valueOf(limit)) > 0) limit + 1 else res.longValueExact()
        }

        var totalPerm = countPerm(halfCnt, halfLen, k.toLong())
        if (totalPerm < k.toLong()) return ""

        val resultHalf = CharArray(halfLen)
        var remaining = halfLen
        var kk = k.toLong()
        for (pos in 0 until halfLen) {
            for (chIdx in 0 until 26) {
                if (halfCnt[chIdx] == 0) continue
                halfCnt[chIdx]--
                val cnt = countPerm(halfCnt, remaining - 1, kk)
                if (cnt >= kk) {
                    resultHalf[pos] = ('a' + chIdx)
                    break
                } else {
                    kk -= cnt
                    halfCnt[chIdx]++ // revert
                }
            }
            remaining--
        }

        val left = String(resultHalf)
        val right = left.reversed()
        return if (middleChar != null) left + middleChar + right else left + right
    }
}
```

## Dart

```dart
class Solution {
  String smallestPalindrome(String s, int k) {
    const int INF = 1000001; // any value > 1e6
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      freq[s.codeUnitAt(i) - 97]++;
    }

    // half counts
    List<int> half = List.filled(26, 0);
    int totalHalf = 0;
    String middle = '';
    for (int i = 0; i < 26; ++i) {
      half[i] = freq[i] ~/ 2;
      totalHalf += half[i];
      if (freq[i] % 2 == 1) middle = String.fromCharCode(i + 97);
    }

    // helper gcd
    int _gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a.abs();
    }

    // combination capped at limit+1
    int combCapped(int n, int k, int limit) {
      if (k < 0 || k > n) return 0;
      if (k > n - k) k = n - k;
      int result = 1;
      for (int i = 1; i <= k; ++i) {
        int a = n - k + i;
        int b = i;

        int g = _gcd(a, b);
        a ~/= g;
        b ~/= g;

        int g2 = _gcd(result, b);
        result ~/= g2;
        b ~/= g2;

        if (result > limit ~/ a) return limit + 1;
        result *= a;

        // b should now be 1
        if (b != 1) {
          result ~/= b; // exact division
        }
      }
      return result;
    }

    // count total permutations of remaining multiset, capped at limit+1
    int countWays(List<int> cnt, int len, int limit) {
      int remaining = len;
      int ans = 1;
      for (int i = 0; i < 26; ++i) {
        int c = cnt[i];
        if (c == 0) continue;
        int ways = combCapped(remaining, c, limit);
        if (ans > limit ~/ ways) return limit + 1;
        ans *= ways;
        remaining -= c;
        if (ans > limit) return limit + 1;
      }
      return ans;
    }

    StringBuffer leftBuilder = StringBuffer();
    for (int pos = 0; pos < totalHalf; ++pos) {
      bool placed = false;
      for (int ch = 0; ch < 26; ++ch) {
        if (half[ch] == 0) continue;
        half[ch]--;
        int ways = countWays(half, totalHalf - pos - 1, k);
        if (ways >= k) {
          leftBuilder.writeCharCode(ch + 97);
          placed = true;
          break;
        } else {
          k -= ways;
          half[ch]++; // revert
        }
      }
      if (!placed) return "";
    }

    String left = leftBuilder.toString();
    StringBuffer rightBuilder = StringBuffer();
    for (int i = left.length - 1; i >= 0; --i) {
      rightBuilder.write(left[i]);
    }
    return left + middle + rightBuilder.toString();
  }
}
```

## Golang

```go
func smallestPalindrome(s string, k int) string {
    const alphabet = 26
    cnt := make([]int, alphabet)
    for i := 0; i < len(s); i++ {
        cnt[s[i]-'a']++
    }

    oddChar := -1
    halfCnt := make([]int, alphabet)
    totalHalf := 0
    for i := 0; i < alphabet; i++ {
        if cnt[i]%2 == 1 {
            oddChar = i
        }
        halfCnt[i] = cnt[i] / 2
        totalHalf += halfCnt[i]
    }

    // helper functions
    var gcd func(int64, int64) int64
    gcd = func(a, b int64) int64 {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }

    // combination limited to limit (if exceeds, returns limit+1)
    combLimited := func(n, r int, limit int64) int64 {
        if r < 0 || r > n {
            return 0
        }
        if r > n-r {
            r = n - r
        }
        res := int64(1)
        for i := 1; i <= r; i++ {
            num := int64(n - r + i)
            den := int64(i)

            g := gcd(num, den)
            num /= g
            den /= g

            g2 := gcd(res, den)
            res /= g2
            den /= g2

            if res > limit/num {
                return limit + 1
            }
            res *= num
        }
        return res
    }

    // number of permutations for current multiset (total elements = total)
    permCount := func(cnt []int, total int, limit int64) int64 {
        rem := total
        res := int64(1)
        for _, c := range cnt {
            if c == 0 {
                continue
            }
            comb := combLimited(rem, c, limit)
            if comb > limit/res {
                return limit + 1
            }
            res *= comb
            if res > limit {
                return limit + 1
            }
            rem -= c
        }
        return res
    }

    // total number of distinct palindromes
    totalPerm := permCount(halfCnt, totalHalf, int64(k))
    if int64(k) > totalPerm {
        return ""
    }

    // build left half lexicographically
    left := make([]byte, totalHalf)
    for pos := 0; pos < totalHalf; pos++ {
        for ch := 0; ch < alphabet; ch++ {
            if halfCnt[ch] == 0 {
                continue
            }
            halfCnt[ch]--
            cntRem := permCount(halfCnt, totalHalf-pos-1, int64(k))
            if int64(k) <= cntRem {
                left[pos] = byte('a' + ch)
                break
            } else {
                k -= int(cntRem)
                halfCnt[ch]++
            }
        }
    }

    // construct full palindrome
    var sb []byte
    sb = append(sb, left...)
    if oddChar != -1 {
        sb = append(sb, byte('a'+oddChar))
    }
    for i := len(left) - 1; i >= 0; i-- {
        sb = append(sb, left[i])
    }
    return string(sb)
}
```

## Ruby

```ruby
def smallest_palindrome(s, k)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }

  odd_idx = nil
  freq.each_with_index do |cnt, i|
    odd_idx = i if cnt.odd?
  end

  half_counts = freq.map { |c| c / 2 }
  total_len = half_counts.sum
  limit = k

  comb = lambda do |n, r|
    r = [r, n - r].min
    res = 1
    (1..r).each do |i|
      res = res * (n - r + i) / i
      return limit + 1 if res > limit
    end
    res
  end

  count_perms = lambda do |cnts, remaining|
    ans = 1
    cnts.each do |c|
      next if c == 0
      ans = ans * comb.call(remaining, c)
      return limit + 1 if ans > limit
      remaining -= c
    end
    ans
  end

  total_perms = count_perms.call(half_counts.dup, total_len)
  return "" if total_perms < k

  half_str = +""
  (0...total_len).each do |pos|
    found = false
    (0...26).each do |ci|
      next if half_counts[ci] == 0
      half_counts[ci] -= 1
      perms = count_perms.call(half_counts, total_len - pos - 1)
      if k <= perms
        half_str << (ci + 97).chr
        found = true
        break
      else
        k -= perms
        half_counts[ci] += 1
      end
    end
    return "" unless found
  end

  middle = odd_idx ? ((odd_idx + 97).chr) : ''
  half_str + middle + half_str.reverse
end
```

## Scala

```scala
object Solution {
    def smallestPalindrome(s: String, kInput: Int): String = {
        val n = s.length
        val cnt = Array.fill(26)(0)
        for (ch <- s) cnt(ch - 'a') += 1

        var middleChar = ""
        for (i <- 0 until 26) {
            if ((cnt(i) & 1) == 1) middleChar = ('a' + i).toChar.toString
        }

        val halfCounts = new Array[Int](26)
        var totalHalf = 0
        for (i <- 0 until 26) {
            halfCounts(i) = cnt(i) / 2
            totalHalf += halfCounts(i)
        }

        def combLimited(n: Int, k: Int, limit: Long): Long = {
            if (k < 0 || k > n) return 0L
            var kk = math.min(k, n - k)
            var res = BigInt(1)
            for (i <- 1 to kk) {
                res = res * (n - kk + i) / i
                if (res > limit) return limit + 1
            }
            val v = res.longValue()
            if (v > limit) limit + 1 else v
        }

        def permutations(counts: Array[Int], total: Int, limit: Long): Long = {
            var rem = total
            var result: Long = 1L
            for (i <- 0 until 26) {
                val c = counts(i)
                if (c > 0) {
                    val comb = combLimited(rem, c, limit)
                    if (comb == 0) return 0L
                    if (result > limit / comb) return limit + 1
                    result *= comb
                    if (result > limit) return limit + 1
                    rem -= c
                }
            }
            result
        }

        var k = kInput.toLong
        val totalPerm = permutations(halfCounts, totalHalf, k)
        if (totalPerm < k) return ""

        val sb = new StringBuilder()
        for (pos <- 0 until totalHalf) {
            var placed = false
            for (i <- 0 until 26 if !placed && halfCounts(i) > 0) {
                halfCounts(i) -= 1
                val cntPerm = permutations(halfCounts, totalHalf - pos - 1, k)
                if (cntPerm >= k) {
                    sb.append(('a' + i).toChar)
                    placed = true
                } else {
                    k -= cntPerm
                    halfCounts(i) += 1
                }
            }
        }

        val firstHalf = sb.toString()
        val secondHalf = firstHalf.reverse
        if (n % 2 == 0) firstHalf + secondHalf else firstHalf + middleChar + secondHalf
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_palindrome(s: String, mut k: i32) -> String {
        const LIMIT: u64 = 1_000_000; // k <= 1e6
        let bytes = s.as_bytes();
        let mut cnt = [0i32; 26];
        for &b in bytes {
            cnt[(b - b'a') as usize] += 1;
        }

        // half counts and middle character
        let mut half_cnt = [0i32; 26];
        let mut mid_char: Option<u8> = None;
        for i in 0..26 {
            if cnt[i] % 2 == 1 {
                mid_char = Some((b'a' + i as u8));
            }
            half_cnt[i] = cnt[i] / 2;
        }

        let half_len: i32 = half_cnt.iter().sum();

        // helper to compute nCr with cap
        fn ncr_cap(n: u64, r: u64, limit: u64) -> u64 {
            if r == 0 || n == r {
                return 1;
            }
            let r = if r > n - r { n - r } else { r };
            let mut res: u128 = 1;
            for i in 0..r {
                res = res * (n - i) as u128 / (i + 1) as u128;
                if res > limit as u128 {
                    return limit + 1;
                }
            }
            res as u64
        }

        // multiply with cap
        fn mul_cap(a: u64, b: u64, limit: u64) -> u64 {
            let prod = (a as u128) * (b as u128);
            if prod > limit as u128 {
                limit + 1
            } else {
                prod as u64
            }
        }

        // count permutations for current half counts
        fn count_perms(cnt: &[i32; 26], remaining: i32, limit: u64) -> u64 {
            let mut total = remaining as i32;
            let mut ans: u64 = 1;
            for &c in cnt.iter() {
                if c == 0 {
                    continue;
                }
                let comb = ncr_cap(total as u64, c as u64, limit);
                ans = mul_cap(ans, comb, limit);
                total -= c;
                if ans > limit {
                    return limit + 1;
                }
            }
            ans
        }

        // total number of distinct palindromes
        let total_perm = count_perms(&half_cnt, half_len, LIMIT);
        if (k as u64) > total_perm {
            return String::new();
        }

        let mut left: Vec<u8> = Vec::with_capacity(half_len as usize);

        for _ in 0..half_len {
            // try each character
            let mut chosen = false;
            for ch in 0..26 {
                if half_cnt[ch] == 0 {
                    continue;
                }
                half_cnt[ch] -= 1;
                let cnt_perm = count_perms(&half_cnt, (half_len - left.len() as i32 - 1), LIMIT);
                if (k as u64) <= cnt_perm {
                    left.push(b'a' + ch as u8);
                    chosen = true;
                    break;
                } else {
                    k -= cnt_perm as i32;
                    half_cnt[ch] += 1; // revert
                }
            }
            if !chosen {
                // should not happen
                return String::new();
            }
        }

        let mut result = String::with_capacity(s.len());
        for &c in &left {
            result.push(c as char);
        }
        if let Some(m) = mid_char {
            result.push(m as char);
        }
        for &c in left.iter().rev() {
            result.push(c as char);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (smallest-palindrome s k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length s))
         (freq (make-vector 26 0)))
    ;; count frequencies
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! freq idx (+ (vector-ref freq idx) 1))))
    ;; find middle character if any
    (define middle-char "")
    (for ([i (in-range 26)])
      (when (= (remainder (vector-ref freq i) 2) 1)
        (set! middle-char (string (integer->char (+ i (char->integer #\a)))))))
    ;; half counts
    (define half-counts (make-vector 26 0))
    (define total-half 0)
    (for ([i (in-range 26)])
      (let ((h (/ (vector-ref freq i) 2)))
        (vector-set! half-counts i h)
        (set! total-half (+ total-half h))))
    ;; helper: binomial coefficient capped at limit+1
    (define (binom-cap n k limit)
      (if (= k 0) 1
          (let* ((k (min k (- n k))))
            (let loop ((i 1) (res 1))
              (if (> i k) res
                  (let* ((num (+ (- n k) i))
                         (new (* res num)))
                    (if (> new (* limit i))
                        (+ limit 1)
                        (loop (+ i 1) (/ new i)))))))))
    ;; helper: count permutations of remaining multiset, capped at limit+1
    (define (count-perms cnt-list rem limit)
      (let loop ((lst cnt-list) (remaining rem) (acc 1))
        (if (null? lst) acc
            (let* ((c (car lst))
                   (b (binom-cap remaining c limit)))
              (if (> b limit)
                  (+ limit 1)
                  (let ((new (* acc b)))
                    (if (> new limit)
                        (+ limit 1)
                        (loop (cdr lst) (- remaining c) new))))))))
    ;; total permutations check
    (define init-counts (vector->list half-counts))
    (when (< (count-perms init-counts total-half k) k)
      (return ""))
    ;; build first half string
    (define first-half (make-string total-half))
    (let loop ((pos 0) (remaining total-half) (krem k))
      (if (= remaining 0)
          (let* ((rev (list->string (reverse (string->list first-half))))
                 (result (string-append first-half middle-char rev)))
            result)
          (let inner ((idx 0) (found #f) (new-k krem))
            (cond
              [(= idx 26) (error "should not happen")]
              [else
               (define cnt (vector-ref half-counts idx))
               (if (= cnt 0)
                   (inner (+ idx 1) found new-k)
                   (begin
                     (vector-set! half-counts idx (- cnt 1))
                     (define perms (count-perms (vector->list half-counts) (- remaining 1) k))
                     (if (>= perms new-k)
                         (begin
                           (string-set! first-half pos (integer->char (+ idx (char->integer #\a))))
                           (loop (+ pos 1) (- remaining 1) new-k))
                         (begin
                           (set! new-k (- new-k perms))
                           (vector-set! half-counts idx cnt)
                           (inner (+ idx 1) found new-k))))))])))))
```

## Erlang

```erlang
-spec smallest_palindrome(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
smallest_palindrome(S, K) ->
    CharList = binary_to_list(S),
    CountMap0 = lists:foldl(fun(C, M) -> maps:update_with(C, fun(V) -> V + 1 end, 1, M) end, #{}, CharList),
    Counts = [maps:get(Char, CountMap0, 0) || Char <- lists:seq($a, $z)],
    % find odd character (if any)
    {OddIdx, _} = 
        lists:foldl(fun(Cnt, {IdxAcc, I}) ->
                            case Cnt rem 2 of
                                1 -> {I, I+1};
                                0 -> {IdxAcc, I+1}
                            end
                    end,
                    {undefined, 0},
                    Counts),
    HalfCounts = [Cnt div 2 || Cnt <- Counts],
    LenHalf = lists:sum(HalfCounts),

    % pre‑compute factorials up to LenHalf
    FactMap = 
        lists:foldl(fun(I, {Prev, M}) ->
                            New = Prev * I,
                            {New, maps:put(I, New, M)}
                    end,
                    {1, #{0 => 1}},
                    lists:seq(1, LenHalf)),
    % total number of distinct palindromes
    TotalPerms = multinomial(HalfCounts, FactMap, K),
    if TotalPerms < K ->
            <<>>;
       true ->
            LeftHalf = build_half(HalfCounts, FactMap, K, []),
            Middle = case OddIdx of
                         undefined -> [];
                         Idx -> [$a + Idx]
                     end,
            Full = LeftHalf ++ Middle ++ lists:reverse(LeftHalf),
            list_to_binary(Full)
    end.

%% Build the k‑th lexicographic permutation of the half multiset.
build_half(_Counts, _FactMap, _K, Acc) when length(Acc) == 0 -> Acc. % placeholder (never used)

build_half(Counts, FactMap, K, Acc) ->
    LenRem = lists:sum(Counts),
    if LenRem == 0 ->
            lists:reverse(Acc);
       true ->
            build_step(0, Counts, FactMap, K, Acc)
    end.

%% Try characters from smallest to largest.
build_step(26, _Counts, _FactMap, _K, _Acc) -> 
    <<>>; % should never happen

build_step(CharIdx, Counts, FactMap, K, Acc) ->
    case lists:nth(CharIdx + 1, Counts) of
        0 ->
            build_step(CharIdx + 1, Counts, FactMap, K, Acc);
        Cnt when Cnt > 0 ->
            NewCounts = decr_at(CharIdx, Counts),
            Perms = multinomial(NewCounts, FactMap, K),
            if Perms >= K ->
                    Char = $a + CharIdx,
                    build_half(NewCounts, FactMap, K, [Char | Acc]);
               true ->
                    build_step(CharIdx + 1, Counts, FactMap, K - Perms, Acc)
            end
    end.

%% Decrement count at position Idx (0‑based).
decr_at(Idx, List) -> decr_at(Idx, List, 0).

decr_at(_Idx, [], _Pos) -> [];
decr_at(Idx, [H|T], Pos) when Pos == Idx ->
    [H - 1 | T];
decr_at(Idx, [H|T], Pos) ->
    [H | decr_at(Idx, T, Pos + 1)].

%% Multinomial coefficient with early cut‑off at K+1.
multinomial(Counts, FactMap, K) ->
    Len = lists:sum(Counts),
    Num = maps:get(Len, FactMap),
    Den = lists:foldl(fun(Cnt, Acc) -> Acc * maps:get(Cnt, FactMap) end,
                      1,
                      Counts),
    Res = Num div Den,
    if Res > K -> K + 1; true -> Res end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_palindrome(s :: String.t(), k :: integer) :: String.t()
  def smallest_palindrome(s, k) do
    bytes = :binary.bin_to_list(s)

    # frequency of each character
    freq =
      Enum.reduce(bytes, %{}, fn b, acc ->
        Map.update(acc, b, 1, &(&1 + 1))
      end)

    # odd character (if any)
    odd_char =
      case Enum.find(freq, fn {_b, cnt} -> rem(cnt, 2) == 1 end) do
        {b, _cnt} -> b
        nil -> nil
      end

    # half counts for building the left part of palindrome
    half_counts =
      Enum.reduce(freq, %{}, fn {b, cnt}, acc ->
        Map.put(acc, b, div(cnt, 2))
      end)

    total_len_half = Enum.reduce(half_counts, 0, fn {_b, c}, sum -> sum + c end)

    # pre‑compute factorials up to total_len_half
    facts =
      Enum.reduce(0..total_len_half, [1], fn i, list ->
        prev = hd(list)
        [prev * i | list]
      end)
      |> :lists.reverse()

    fact = fn n -> Enum.at(facts, n) end

    denom =
      Enum.reduce(half_counts, 1, fn {_b, c}, acc ->
        acc * fact.(c)
      end)

    total_perms = div(fact.(total_len_half), denom)

    if total_perms < k do
      ""
    else
      half_codes = build_half(total_len_half, half_counts, total_perms, k, [])

      first_half =
        half_codes
        |> Enum.map(&<<&1>>)
        |> Enum.join()

      middle = if odd_char, do: <<odd_char>>, else: ""

      first_half <> middle <> String.reverse(first_half)
    end
  end

  defp build_half(0, _counts, _perms, _k, acc), do: Enum.reverse(acc)

  defp build_half(pos, counts, perms, k, acc) do
    rem = pos

    {chosen_char, new_counts, new_perms, new_k} =
      Enum.reduce_while(?a..?z, {nil, counts, perms, k}, fn ch_code,
                                                            {_c, cnts, cur_perms, cur_k} ->
        c = Map.get(cnts, ch_code, 0)

        if c == 0 do
          {:cont, {nil, cnts, cur_perms, cur_k}}
        else
          perms_if_choose = div(cur_perms * c, rem)

          if cur_k <= perms_if_choose do
            {:halt,
             {
               ch_code,
               Map.update!(cnts, ch_code, &(&1 - 1)),
               perms_if_choose,
               cur_k
             }}
          else
            {:cont, {nil, cnts, cur_perms, cur_k - perms_if_choose}}
          end
        end
      end)

    build_half(pos - 1, new_counts, new_perms, new_k, [chosen_char | acc])
  end
end
```
