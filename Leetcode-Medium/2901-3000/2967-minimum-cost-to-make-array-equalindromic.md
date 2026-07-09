# 2967. Minimum Cost to Make Array Equalindromic

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // construct palindrome from left part for total length len
    string makePal(const string& left, int len) {
        string rev = left;
        if (len % 2 == 1) rev.pop_back();
        reverse(rev.begin(), rev.end());
        return left + rev;
    }
    
    long long nextPalindrome(long long x) {
        if (x <= 0) return 1;
        string s = to_string(x);
        int n = s.size();
        string left = s.substr(0, (n + 1) / 2);
        string candStr = makePal(left, n);
        long long cand = stoll(candStr);
        if (cand >= x) return cand;
        // need to increment the left part
        long long leftNum = stoll(left) + 1;
        string leftInc = to_string(leftNum);
        if ((int)leftInc.size() > (int)left.size()) {
            // overflow, length increases by 1 -> form 100...001
            string res = "1";
            for (int i = 0; i < n - 1; ++i) res.push_back('0');
            res.push_back('1');
            return stoll(res);
        } else {
            string pal2 = makePal(leftInc, n);
            return stoll(pal2);
        }
    }
    
    long long prevPalindrome(long long x) {
        if (x <= 1) return 1;
        string s = to_string(x);
        int n = s.size();
        string left = s.substr(0, (n + 1) / 2);
        string candStr = makePal(left, n);
        long long cand = stoll(candStr);
        if (cand <= x) return cand;
        // need to decrement the left part
        long long leftNum = stoll(left) - 1;
        if (leftNum == 0) {
            string res(n - 1, '9');
            return res.empty() ? 1 : stoll(res);
        }
        string leftDec = to_string(leftNum);
        if ((int)leftDec.size() < (int)left.size()) {
            // length reduced
            string res(n - 1, '9');
            return stoll(res);
        } else {
            string pal2 = makePal(leftDec, n);
            return stoll(pal2);
        }
    }
    
    long long totalCost(const vector<int>& nums, long long y) {
        long long sum = 0;
        for (int v : nums) sum += llabs((long long)v - y);
        return sum;
    }
    
    long long minimumCost(vector<int>& nums) {
        const long long LIMIT = 1000000000LL; // y must be < 1e9
        int n = nums.size();
        sort(nums.begin(), nums.end());
        long long low = nums[(n - 1) / 2];
        long long high = nums[n / 2];
        
        // Check if there exists a palindrome inside [low, high]
        long long candIn = nextPalindrome(low);
        if (candIn <= high && candIn < LIMIT) {
            return totalCost(nums, candIn);
        }
        
        long long ans = LLONG_MAX;
        long long p1 = prevPalindrome(low);
        if (p1 >= 1 && p1 < LIMIT) ans = min(ans, totalCost(nums, p1));
        long long p2 = nextPalindrome(high);
        if (p2 < LIMIT) ans = min(ans, totalCost(nums, p2));
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minimumCost(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }

        List<Integer> pals = generatePalindromes();
        long best = Long.MAX_VALUE;

        for (int y : pals) {
            int idx = lowerBound(nums, y);
            long left = (long) y * idx - pref[idx];
            long right = (pref[n] - pref[idx]) - (long) y * (n - idx);
            long cost = left + right;
            if (cost < best) {
                best = cost;
            }
        }
        return best;
    }

    private int lowerBound(int[] arr, int target) {
        int l = 0, r = arr.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (arr[m] < target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }

    private List<Integer> generatePalindromes() {
        List<Integer> list = new ArrayList<>();
        int[] pow10 = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
        for (int len = 1; len <= 9; len++) {
            boolean odd = (len % 2 == 1);
            int halfLen = (len + 1) / 2;
            int start = pow10[halfLen - 1];
            int end = pow10[halfLen] - 1;
            for (int prefix = start; prefix <= end; prefix++) {
                int pal = createPalindrome(prefix, odd);
                if (pal < 1000000000) { // less than 1e9
                    list.add(pal);
                }
            }
        }
        return list;
    }

    private int createPalindrome(int prefix, boolean oddLength) {
        int pal = prefix;
        if (oddLength) {
            prefix /= 10;
        }
        while (prefix > 0) {
            pal = pal * 10 + (prefix % 10);
            prefix /= 10;
        }
        return pal;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sorted(nums)
        low = s[(n - 1) // 2]
        high = s[n // 2]

        candidates = set()

        # largest palindrome <= high
        p = high
        while p > 0 and str(p) != str(p)[::-1]:
            p -= 1
        if p > 0:
            candidates.add(p)

        # smallest palindrome >= low (and < 1e9)
        q = low
        while True:
            if str(q) == str(q)[::-1]:
                break
            q += 1
            if q >= 1000000000:   # limit for palindromic number
                q = None
                break
        if q is not None and q < 1000000000:
            candidates.add(q)

        best = float('inf')
        for y in candidates:
            total = 0
            for v in nums:
                total += abs(v - y)
                # early stop if already worse than current best
                if total >= best:
                    break
            if total < best:
                best = total

        return int(best)
```

## Python3

```python
import sys
from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        low = nums[(n - 1) // 2]
        high = nums[n // 2]

        # helper to check palindrome
        def is_pal(x: int) -> bool:
            s = str(x)
            return s == s[::-1]

        # nearest palindrome <= x (positive)
        def lower_pal(x: int) -> int:
            while x > 0 and not is_pal(x):
                x -= 1
            return x if x > 0 else None

        # nearest palindrome >= x (and < 1e9)
        def upper_pal(x: int) -> int:
            limit = 10 ** 9
            while x < limit and not is_pal(x):
                x += 1
            return x if x < limit else None

        mid = (low + high) // 2

        candidates = set()
        lp = lower_pal(mid)
        up = upper_pal(mid)
        if lp is not None:
            candidates.add(lp)
        if up is not None:
            candidates.add(up)

        # also consider palindromes exactly at low/high in case interval length zero
        if is_pal(low):
            candidates.add(low)
        if is_pal(high):
            candidates.add(high)

        best = sys.maxsize
        for y in candidates:
            cost = 0
            for v in nums:
                cost += abs(v - y)
                # early break if already worse than current best
                if cost >= best:
                    break
            if cost < best:
                best = cost

        return best
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int cmpInt(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

static int lowerBound(int *arr, int size, int target) {
    int l = 0, r = size;
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] < target)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

long long minimumCost(int* nums, int numsSize) {
    /* generate all palindromes less than 1e9 */
    int pow10[10];
    pow10[0] = 1;
    for (int i = 1; i < 10; ++i) pow10[i] = pow10[i - 1] * 10;

    int maxPalCount = 110000;
    int *pals = (int *)malloc(maxPalCount * sizeof(int));
    int pcnt = 0;
    for (int len = 1; len <= 9; ++len) {
        int half = (len + 1) >> 1;
        int start = pow10[half - 1];
        int end = pow10[half] - 1;
        for (int prefix = start; prefix <= end; ++prefix) {
            long long pal = prefix;
            int rev = prefix;
            if (len & 1) rev /= 10;
            while (rev > 0) {
                pal = pal * 10 + rev % 10;
                rev /= 10;
            }
            if (pal < 1000000000LL) {
                pals[pcnt++] = (int)pal;
            }
        }
    }

    /* sort a copy of nums to find median interval */
    int *arr = (int *)malloc(numsSize * sizeof(int));
    memcpy(arr, nums, numsSize * sizeof(int));
    qsort(arr, numsSize, sizeof(int), cmpInt);

    int L, R;
    if (numsSize & 1) {
        L = R = arr[numsSize / 2];
    } else {
        L = arr[numsSize / 2 - 1];
        R = arr[numsSize / 2];
    }

    /* find candidate palindromes */
    int idx = lowerBound(pals, pcnt, L);
    long long best = LLONG_MAX;

    if (idx < pcnt && pals[idx] <= R) {
        /* there exists a palindrome inside [L,R] */
        long long cost = 0;
        for (int i = 0; i < numsSize; ++i)
            cost += llabs((long long)nums[i] - (long long)pals[idx]);
        best = cost;
    } else {
        if (idx < pcnt) { /* smallest palindrome > R */
            long long cost = 0;
            for (int i = 0; i < numsSize; ++i)
                cost += llabs((long long)nums[i] - (long long)pals[idx]);
            if (cost < best) best = cost;
        }
        if (idx > 0) { /* largest palindrome < L */
            long long cost = 0;
            for (int i = 0; i < numsSize; ++i)
                cost += llabs((long long)nums[i] - (long long)pals[idx - 1]);
            if (cost < best) best = cost;
        }
    }

    free(pals);
    free(arr);
    return best;
}
```

## Csharp

```csharp
using System;
using System.Linq;

public class Solution {
    public long MinimumCost(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int median = nums[(n - 1) / 2];

        long lower = PrevPalindrome(median);
        long upper = NextPalindrome(median);
        const long LIMIT = 1000000000L; // 10^9
        if (upper >= LIMIT) upper = 999999999L;

        long costLower = ComputeCost(nums, lower);
        long costUpper = ComputeCost(nums, upper);

        return Math.Min(costLower, costUpper);
    }

    private static long ComputeCost(int[] nums, long target) {
        long sum = 0;
        foreach (int v in nums) {
            sum += Math.Abs((long)v - target);
        }
        return sum;
    }

    private static long PrevPalindrome(long x) {
        if (x <= 1) return 1; // smallest positive palindrome
        string s = x.ToString();
        int len = s.Length;
        int halfLen = (len + 1) / 2;
        long prefix = long.Parse(s.Substring(0, halfLen));
        long pal = BuildPalindrome(prefix, len);
        if (pal > x) {
            prefix--;
            if (prefix == 0) {
                // e.g., x=10 -> return 9
                string nine = new string('9', len - 1);
                return long.Parse(nine);
            }
            if (prefix.ToString().Length < halfLen) {
                // length reduces by one, largest palindrome with len-1 digits is all 9's
                string nine = new string('9', len - 1);
                return long.Parse(nine);
            }
            pal = BuildPalindrome(prefix, len);
        }
        return pal;
    }

    private static long NextPalindrome(long x) {
        const long LIMIT = 1000000000L; // 10^9
        if (x >= LIMIT - 1) return LIMIT - 1; // largest allowed palindrome is 999,999,999
        string s = x.ToString();
        int len = s.Length;
        int halfLen = (len + 1) / 2;
        long prefix = long.Parse(s.Substring(0, halfLen));
        long pal = BuildPalindrome(prefix, len);
        if (pal < x) {
            prefix++;
            string prefStr = prefix.ToString();
            if (prefStr.Length > halfLen) {
                // length increases by one
                int newLen = len + 1;
                string str = "1" + new string('0', newLen - 2) + "1";
                return long.Parse(str);
            }
            pal = BuildPalindrome(prefix, len);
        }
        if (pal >= LIMIT) {
            // cap to largest allowed palindrome
            return LIMIT - 1;
        }
        return pal;
    }

    private static long BuildPalindrome(long prefix, int totalLen) {
        string pre = prefix.ToString();
        char[] revPart;
        if (totalLen % 2 == 0) {
            revPart = pre.Reverse().ToArray();
        } else {
            revPart = pre.Substring(0, pre.Length - 1).Reverse().ToArray();
        }
        return long.Parse(pre + new string(revPart));
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumCost = function(nums) {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    const lower = nums[Math.floor((n - 1) / 2)];
    const upper = nums[Math.floor(n / 2)];

    const pals = getPalindromes();

    // binary search first palindrome >= lower
    let idx = lowerBound(pals, lower);
    // if there is a palindrome inside [lower, upper], it's optimal
    if (idx < pals.length && pals[idx] <= upper) {
        return computeCost(nums, pals[idx]);
    }

    const candidates = [];
    if (idx < pals.length) candidates.push(pals[idx]);      // first >= lower
    if (idx > 0) candidates.push(pals[idx - 1]);           // last < lower

    let best = Infinity;
    for (const y of candidates) {
        const cost = computeCost(nums, y);
        if (cost < best) best = cost;
    }
    return best;
};

function computeCost(arr, target) {
    let sum = 0;
    for (let v of arr) {
        sum += Math.abs(v - target);
    }
    return sum;
}

function lowerBound(arr, target) {
    let l = 0, r = arr.length;
    while (l < r) {
        const m = (l + r) >> 1;
        if (arr[m] < target) l = m + 1;
        else r = m;
    }
    return l;
}

function getPalindromes() {
    const limit = 1e9;
    const set = new Set();
    // single digit palindromes
    for (let d = 1; d <= 9; ++d) set.add(d);
    // generate using half part
    for (let i = 1; i < 100000; ++i) { // enough for up to 9 digits
        const s = i.toString();
        const rev = s.split('').reverse().join('');
        // odd length palindrome
        const odd = parseInt(s + rev.slice(1), 10);
        if (odd <= limit) set.add(odd);
        // even length palindrome
        const even = parseInt(s + rev, 10);
        if (even <= limit) set.add(even);
    }
    const arr = Array.from(set);
    arr.sort((a, b) => a - b);
    return arr;
}
```

## Typescript

```typescript
function minimumCost(nums: number[]): number {
    const LIMIT = 1_000_000_000;

    function isPalindrome(x: number): boolean {
        const s = x.toString();
        return s === s.split('').reverse().join('');
    }

    function buildPal(prefix: string, odd: boolean): string {
        const rev = prefix.split('').reverse().join('');
        return odd ? prefix + rev.slice(1) : prefix + rev;
    }

    function nextPalindrome(x: number): number {
        const s = x.toString();
        const len = s.length;
        const odd = len % 2 === 1;
        const halfLen = Math.ceil(len / 2);
        let prefix = s.slice(0, halfLen);
        let palStr = buildPal(prefix, odd);
        if (Number(palStr) >= x) return Number(palStr);

        // increment prefix
        let inc = (BigInt(prefix) + 1n).toString();
        if (inc.length > halfLen) {
            const newLen = len + 1;
            return Number('1' + '0'.repeat(newLen - 2) + '1');
        } else {
            palStr = buildPal(inc, odd);
            return Number(palStr);
        }
    }

    function prevPalindrome(x: number): number {
        const s = x.toString();
        const len = s.length;
        const odd = len % 2 === 1;
        const halfLen = Math.ceil(len / 2);
        let prefix = s.slice(0, halfLen);
        let palStr = buildPal(prefix, odd);
        if (Number(palStr) <= x) return Number(palStr);

        // decrement prefix
        let decBig = BigInt(prefix) - 1n;
        if (decBig <= 0n) {
            // largest palindrome with fewer digits: all 9's
            if (len === 1) return 0;
            return Number('9'.repeat(len - 1));
        }
        let dec = decBig.toString();
        if (dec.length < halfLen) {
            // length reduced
            return Number('9'.repeat(len - 1));
        } else {
            palStr = buildPal(dec, odd);
            return Number(palStr);
        }
    }

    const n = nums.length;
    const sorted = [...nums].sort((a, b) => a - b);
    const medianIdx = Math.floor(n / 2); // upper median
    const m = sorted[medianIdx];

    const candidates = new Set<number>();
    if (isPalindrome(m)) candidates.add(m);

    const low = prevPalindrome(m);
    if (low >= 1) candidates.add(low);

    const high = nextPalindrome(m);
    if (high < LIMIT) candidates.add(high);

    let minCost = Number.MAX_SAFE_INTEGER;
    for (const y of candidates) {
        let cost = 0;
        for (const v of nums) {
            cost += Math.abs(v - y);
        }
        if (cost < minCost) minCost = cost;
    }

    return minCost;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumCost($nums) {
        $n = count($nums);
        if ($n == 0) return 0;

        // sort a copy to find median interval
        $sorted = $nums;
        sort($sorted, SORT_NUMERIC);

        $lowIdx = intdiv($n - 1, 2);
        $highIdx = intdiv($n, 2);
        $low = $sorted[$lowIdx];
        $high = $sorted[$highIdx];

        // helper to check palindrome
        $isPal = function(int $x): bool {
            $s = (string)$x;
            return $s === strrev($s);
        };

        // compute total cost for a given target y
        $costFor = function(array $arr, int $y): int {
            $sum = 0;
            foreach ($arr as $v) {
                $diff = $v - $y;
                $sum += ($diff >= 0) ? $diff : -$diff;
            }
            return $sum;
        };

        // try to find a palindrome inside [low, high]
        $candidate = $low;
        while ($candidate <= $high && !$isPal($candidate)) {
            $candidate++;
        }
        if ($candidate <= $high) {
            return $costFor($nums, $candidate);
        }

        // largest palindrome <= low
        $palLow = null;
        $temp = $low;
        while ($temp >= 1 && !$isPal($temp)) {
            $temp--;
        }
        if ($temp >= 1) $palLow = $temp;

        // smallest palindrome >= high (and < 1e9)
        $palHigh = null;
        $limit = 1000000000; // exclusive upper bound
        $temp = $high;
        while ($temp < $limit && !$isPal($temp)) {
            $temp++;
        }
        if ($temp < $limit) $palHigh = $temp;

        $best = PHP_INT_MAX;
        if ($palLow !== null) {
            $best = min($best, $costFor($nums, $palLow));
        }
        if ($palHigh !== null) {
            $best = min($best, $costFor($nums, $palHigh));
        }

        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ nums: [Int]) -> Int {
        let n = nums.count
        var sortedNums = nums.sorted()
        let left = sortedNums[(n - 1) / 2]
        let right = sortedNums[n / 2]

        // generate all palindromes < 1_000_000_000
        let palindromes = generatePalindromes(limit: 1_000_000_000)

        func lowerBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let m = (l + r) >> 1
                if arr[m] < target {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }

        func totalCost(_ y: Int) -> Int {
            var sum: Int64 = 0
            for v in nums {
                sum += Int64(abs(v - y))
            }
            return Int(sum)
        }

        var best = Int.max

        // check if any palindrome lies within [left, right]
        let idxIn = lowerBound(palindromes, left)
        if idxIn < palindromes.count && palindromes[idxIn] <= right {
            best = min(best, totalCost(palindromes[idxIn]))
        } else {
            // candidate just below left
            if idxIn > 0 {
                let candLow = palindromes[idxIn - 1]
                best = min(best, totalCost(candLow))
            }
            // candidate just above right
            let idxHigh = lowerBound(palindromes, right)
            if idxHigh < palindromes.count {
                let candHigh = palindromes[idxHigh]
                best = min(best, totalCost(candHigh))
            }
        }

        return best
    }

    private func generatePalindromes(limit: Int) -> [Int] {
        var res = [Int]()
        // lengths from 1 to 9 (since limit < 10^9)
        for len in 1...9 {
            let halfLen = (len + 1) / 2
            var start = 1
            if halfLen > 1 {
                for _ in 1..<halfLen { start *= 10 } // 10^(halfLen-1)
            }
            var end = start * 10 - 1
            if halfLen == 1 {
                start = 1
                end = 9
            }
            for prefix in start...end {
                let s = String(prefix)
                var rev = String(s.reversed())
                if len % 2 == 1 {
                    rev.removeFirst()
                }
                let palStr = s + rev
                if let pal = Int(palStr), pal < limit {
                    res.append(pal)
                }
            }
        }
        return res.sorted()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(nums: IntArray): Long {
        val n = nums.size
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted)
        val median = if (n % 2 == 1) sorted[n / 2].toLong() else sorted[n / 2 - 1].toLong()

        val candidates = mutableSetOf<Long>()
        candidates.add(prevPalindrome(median))
        val nxt = nextPalindrome(median)
        if (nxt < 1_000_000_000L) candidates.add(nxt)

        var best = Long.MAX_VALUE
        for (target in candidates) {
            var sum = 0L
            for (v in nums) {
                sum += kotlin.math.abs(v.toLong() - target)
            }
            if (sum < best) best = sum
        }
        return best
    }

    private fun nextPalindrome(x: Long): Long {
        if (x <= 1L) return 1L
        val s = x.toString()
        val len = s.length
        val half = (len + 1) / 2
        var prefix = s.substring(0, half).toLong()

        fun makePal(prefixVal: Long, length: Int): Long {
            val pre = prefixVal.toString()
            val sb = StringBuilder(pre)
            val rev = if (length % 2 == 0) pre.reversed() else pre.dropLast(1).reversed()
            sb.append(rev)
            return sb.toString().toLong()
        }

        var pal = makePal(prefix, len)
        if (pal >= x) return pal

        prefix += 1
        val newPrefixStr = prefix.toString()
        // overflow case like 99 -> 101
        return if (newPrefixStr.length > half) {
            ("1" + "0".repeat(len - 1) + "1").toLong()
        } else {
            makePal(prefix, len)
        }
    }

    private fun prevPalindrome(x: Long): Long {
        if (x <= 1L) return 1L
        val s = x.toString()
        val len = s.length
        val half = (len + 1) / 2
        var prefix = s.substring(0, half).toLong()

        fun makePal(prefixVal: Long, length: Int): Long {
            val pre = prefixVal.toString()
            val sb = StringBuilder(pre)
            val rev = if (length % 2 == 0) pre.reversed() else pre.dropLast(1).reversed()
            sb.append(rev)
            return sb.toString().toLong()
        }

        var pal = makePal(prefix, len)
        if (pal <= x) return pal

        prefix -= 1
        if (prefix == 0L) {
            val nineStr = "9".repeat(len - 1)
            return if (nineStr.isEmpty()) 0L else nineStr.toLong()
        }
        val newPrefixStr = prefix.toString()
        // underflow case like 1000 -> 999
        return if (newPrefixStr.length < half) {
            ("9".repeat(len - 1)).toLong()
        } else {
            makePal(prefix, len)
        }
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(List<int> nums) {
    nums.sort();
    int n = nums.length;
    int low = nums[(n - 1) ~/ 2];
    int high = nums[n ~/ 2];

    int baseCost = _totalCost(nums, low);

    int candidateLower = _largestPalindromeLE(high);
    if (candidateLower >= low && candidateLower > 0) {
      return baseCost;
    }

    int candidateUpper = _smallestPalindromeGE(low);
    const int LIMIT = 1000000000; // y must be < 1e9
    const int INF = 1 << 60;

    int costLower = INF;
    if (candidateLower >= 1) {
      costLower = _totalCost(nums, candidateLower);
    }

    int costUpper = INF;
    if (candidateUpper > 0 && candidateUpper < LIMIT) {
      costUpper = _totalCost(nums, candidateUpper);
    }

    return costLower < costUpper ? costLower : costUpper;
  }

  int _totalCost(List<int> nums, int target) {
    int sum = 0;
    for (int v in nums) {
      sum += (v - target).abs();
    }
    return sum;
  }

  int _largestPalindromeLE(int x) {
    String s = x.toString();
    int n = s.length;
    int halfLen = (n + 1) >> 1;
    String left = s.substring(0, halfLen);
    String palStr = _makePal(left, n);
    int pal = int.parse(palStr);
    if (pal <= x) return pal;

    int leftNum = int.parse(left) - 1;
    if (leftNum == 0) {
      if (n == 1) return 0;
      return int.parse(_repeatChar('9', n - 1));
    }
    String newLeft = leftNum.toString();
    if (newLeft.length < halfLen) {
      if (n == 1) return 0;
      return int.parse(_repeatChar('9', n - 1));
    }
    return int.parse(_makePal(newLeft, n));
  }

  int _smallestPalindromeGE(int x) {
    String s = x.toString();
    int n = s.length;
    int halfLen = (n + 1) >> 1;
    String left = s.substring(0, halfLen);
    String palStr = _makePal(left, n);
    int pal = int.parse(palStr);
    if (pal >= x) return pal;

    int leftNum = int.parse(left) + 1;
    String newLeft = leftNum.toString();
    if (newLeft.length > halfLen) {
      // length increased, produce 1 followed by zeros and ending with 1
      return int.parse('1' + _repeatChar('0', n - 1) + '1');
    }
    return int.parse(_makePal(newLeft, n));
  }

  String _makePal(String left, int totalLen) {
    String rev = left.split('').reversed.join();
    if (totalLen % 2 == 1) {
      rev = rev.substring(1);
    }
    return left + rev;
  }

  String _repeatChar(String ch, int count) {
    if (count <= 0) return '';
    return List.filled(count, ch).join();
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func minimumCost(nums []int) int64 {
	if len(nums) == 0 {
		return 0
	}
	// generate all palindromes < 1e9
	pals := genPalindromes()

	// sort nums to find median
	sorted := make([]int, len(nums))
	copy(sorted, nums)
	sort.Ints(sorted)

	var median int
	n := len(sorted)
	if n%2 == 1 {
		median = sorted[n/2]
	} else {
		median = sorted[n/2-1] // any value between the two middles works; choose lower
	}

	// binary search for closest palindromes around median
	idx := sort.SearchInts(pals, median)

	const inf int64 = 1<<63 - 1
	best := inf

	if idx < len(pals) {
		cost := totalCost(nums, pals[idx])
		if cost < best {
			best = cost
		}
	}
	if idx > 0 {
		cost := totalCost(nums, pals[idx-1])
		if cost < best {
			best = cost
		}
	}
	return best
}

func totalCost(arr []int, target int) int64 {
	var sum int64
	for _, v := range arr {
		diff := v - target
		if diff < 0 {
			diff = -diff
		}
		sum += int64(diff)
	}
	return sum
}

func genPalindromes() []int {
	pow10 := [10]int{1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000}
	var pals []int
	for length := 1; length <= 9; length++ {
		half := (length + 1) / 2
		start := pow10[half-1]
		if length == 1 {
			start = 1 // single digit palindromes start from 1
		}
		end := pow10[half]
		for prefix := start; prefix < end; prefix++ {
			pal := buildPalindrome(prefix, length%2 == 1)
			if pal > 0 && pal < 1000000000 {
				pals = append(pals, pal)
			}
		}
	}
	sort.Ints(pals)
	return pals
}

func buildPalindrome(prefix int, odd bool) int {
	pal := prefix
	x := prefix
	if odd {
		x /= 10
	}
	for x > 0 {
		pal = pal*10 + x%10
		x /= 10
	}
	return pal
}
```

## Ruby

```ruby
def build_pal(prefix, even_len)
  rev = if even_len
          prefix.reverse
        else
          prefix[0...-1].reverse
        end
  (prefix + rev).to_i
end

def next_pal_ge(x)
  s = x.to_s
  len = s.length
  half_len = (len + 1) / 2
  prefix = s[0, half_len]
  even = len.even?
  pal = build_pal(prefix, even)
  return pal if pal >= x

  inc_int = prefix.to_i + 1
  inc_str = inc_int.to_s
  if inc_str.length > prefix.length
    new_len = len + 1
    return build_pal(inc_str, new_len.even?)
  else
    return build_pal(inc_str.rjust(prefix.length, '0'), even)
  end
end

def prev_pal_le(x)
  s = x.to_s
  len = s.length
  half_len = (len + 1) / 2
  prefix = s[0, half_len]
  even = len.even?
  pal = build_pal(prefix, even)
  return pal if pal <= x

  dec_int = prefix.to_i - 1
  return ('9' * (len - 1)).to_i if dec_int <= 0

  dec_str = dec_int.to_s
  if dec_str.length < prefix.length
    ('9' * (len - 1)).to_i
  else
    build_pal(dec_str.rjust(prefix.length, '0'), even)
  end
end

# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
  n = nums.size
  sorted = nums.sort
  candidates = []

  if n.odd?
    med = sorted[n / 2]
    candidates << prev_pal_le(med)
    candidates << next_pal_ge(med)
  else
    left = sorted[n / 2 - 1]
    right = sorted[n / 2]

    pal_in_range = next_pal_ge(left)
    if pal_in_range <= right
      candidates << pal_in_range
    else
      candidates << prev_pal_le(left)
      candidates << next_pal_ge(right)
    end
  end

  candidates.uniq!
  min_cost = nil
  candidates.each do |y|
    cost = 0
    nums.each { |v| cost += (v - y).abs }
    min_cost = cost if min_cost.nil? || cost < min_cost
  end
  min_cost
end
```

## Scala

```scala
object Solution {
    def minimumCost(nums: Array[Int]): Long = {
        val sorted = nums.sorted
        val n = sorted.length
        val a = sorted((n - 1) / 2).toLong
        val b = sorted(n / 2).toLong

        def tenPow(k: Int): Long = {
            var res = 1L
            var i = 0
            while (i < k) {
                res *= 10L
                i += 1
            }
            res
        }

        def makePal(prefix: String, odd: Boolean): Long = {
            val rev = if (odd) prefix.dropRight(1).reverse else prefix.reverse
            (prefix + rev).toLong
        }

        def prevPalindrome(x: Long): Long = {
            val s = x.toString
            val len = s.length
            val half = (len + 1) / 2
            var prefixStr = s.substring(0, half)
            var pal = makePal(prefixStr, len % 2 == 1)
            if (pal <= x) return pal
            var prefNum = prefixStr.toLong - 1
            if (prefNum <= 0) {
                return tenPow(len - 1) - 1
            }
            val newPrefixStr = prefNum.toString
            if (newPrefixStr.length < half) {
                return tenPow(len - 1) - 1
            }
            makePal(newPrefixStr, len % 2 == 1)
        }

        def nextPalindrome(x: Long): Long = {
            val s = x.toString
            val len = s.length
            val half = (len + 1) / 2
            var prefixStr = s.substring(0, half)
            var pal = makePal(prefixStr, len % 2 == 1)
            if (pal >= x) return pal
            var prefNum = prefixStr.toLong + 1
            val limit = tenPow(half)
            if (prefNum == limit) {
                return tenPow(len) + 1
            }
            val newPrefixStr = prefNum.toString
            makePal(newPrefixStr, len % 2 == 1)
        }

        def totalCost(y: Long): Long = {
            var sum = 0L
            var i = 0
            while (i < nums.length) {
                sum += math.abs(nums(i).toLong - y)
                i += 1
            }
            sum
        }

        val baseCost = totalCost(a)

        // check if there exists a palindrome within [a, b] and less than 1e9
        val candIn = nextPalindrome(a)
        if (candIn <= b && candIn < 1000000000L) {
            return baseCost
        }

        var answer = Long.MaxValue

        val lowPal = prevPalindrome(a)
        if (lowPal > 0 && lowPal < 1000000000L) {
            answer = math.min(answer, totalCost(lowPal))
        }

        val highPal = nextPalindrome(b)
        if (highPal > 0 && highPal < 1000000000L) {
            answer = math.min(answer, totalCost(highPal))
        }

        answer
    }
}
```

## Rust

```rust
use std::cmp::Ordering;

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // convert to i64 and sort
        let mut a: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        a.sort_unstable();

        let lower = a[(n - 1) / 2];
        let upper = a[n / 2];

        // candidates: largest palindrome <= upper, smallest palindrome >= lower
        let mut cand: Vec<i64> = Vec::new();

        let p_low = Self::prev_pal(upper);
        if p_low >= 1 {
            cand.push(p_low);
        }
        let p_high = Self::next_pal(lower);
        const LIMIT: i64 = 1_000_000_000; // y must be < 10^9
        if p_high < LIMIT {
            cand.push(p_high);
        }

        // deduplicate
        cand.sort_unstable();
        cand.dedup();

        let mut best = i64::MAX;
        for &target in &cand {
            let mut sum = 0i64;
            for &v in &a {
                sum += (v - target).abs();
            }
            if sum < best {
                best = sum;
            }
        }
        best
    }

    // construct palindrome from prefix string and total length
    fn construct_pal(prefix: &str, total_len: usize) -> i64 {
        let mut pal = String::from(prefix);
        let rev_part: String;
        if total_len % 2 == 0 {
            rev_part = prefix.chars().rev().collect();
        } else {
            // exclude the middle character
            rev_part = prefix[..prefix.len() - 1].chars().rev().collect();
        }
        pal.push_str(&rev_part);
        pal.parse::<i64>().unwrap()
    }

    fn next_pal(x: i64) -> i64 {
        let s = x.to_string();
        let n = s.len();
        let prefix_len = (n + 1) / 2;
        let prefix = &s[0..prefix_len];
        let p0 = Self::construct_pal(prefix, n);
        if p0 >= x {
            return p0;
        }
        // increment the prefix
        let mut pref_num: i64 = prefix.parse().unwrap();
        pref_num += 1;
        let new_prefix = pref_num.to_string();
        let total_len = if new_prefix.len() > prefix_len { n + 1 } else { n };
        Self::construct_pal(&new_prefix, total_len)
    }

    fn prev_pal(x: i64) -> i64 {
        let s = x.to_string();
        let n = s.len();
        let prefix_len = (n + 1) / 2;
        let prefix = &s[0..prefix_len];
        let p0 = Self::construct_pal(prefix, n);
        if p0 <= x {
            return p0;
        }
        // decrement the prefix
        let mut pref_num: i64 = prefix.parse().unwrap();
        if pref_num == 0 {
            // shouldn't happen for positive x
            return 0;
        }
        pref_num -= 1;
        if pref_num == 0 || pref_num.to_string().len() < prefix_len {
            // length reduced -> largest palindrome with one fewer digit (all 9's)
            if n == 1 {
                return 0;
            }
            let mut res = String::new();
            for _ in 0..(n - 1) {
                res.push('9');
            }
            return res.parse::<i64>().unwrap();
        } else {
            let new_prefix = pref_num.to_string();
            Self::construct_pal(&new_prefix, n)
        }
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/string)

(define (is-pal? x)
  (let* ((s (number->string x))
         (rev (string-reverse s)))
    (string=? s rev)))

(define (next-pal x)
  (let loop ((y x))
    (if (is-pal? y) y
        (loop (+ y 1)))))

(define (prev-pal x)
  (let loop ((y x))
    (if (or (= y 0) (is-pal? y)) y
        (loop (- y 1)))))

(define (cost lst target)
  (foldl (lambda (a acc) (+ acc (abs (- a target)))) 0 lst))

(define/contract (minimum-cost nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (median (list-ref sorted (quotient n 2))) ; pick upper median
         (p1 (prev-pal median))
         (p2 (next-pal median))
         (c1 (cost nums p1))
         (c2 (cost nums p2)))
    (min c1 c2)))
```

## Erlang

```erlang
-spec minimum_cost(Nums :: [integer()]) -> integer().
minimum_cost(Nums) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    MedianLowIdx = (N + 1) div 2,
    MedianLow = lists:nth(MedianLowIdx, Sorted),
    MedianHigh = case N rem 2 of
        0 -> lists:nth(MedianLowIdx + 1, Sorted);
        _ -> MedianLow
    end,
    Cand0 = [lower_pal(MedianLow), higher_pal(MedianLow)],
    Cand1 = if MedianHigh =:= MedianLow -> [] ; true -> [lower_pal(MedianHigh), higher_pal(MedianHigh)] end,
    AllCand = lists:usort(Cand0 ++ Cand1),
    ValidCand = [C || C <- AllCand, C > 0, C < 1000000000],
    lists:min([cost(Nums, C) || C <- ValidCand]).

%% compute total absolute difference cost
-spec cost([integer()], integer()) -> integer().
cost(List, Y) ->
    lists:foldl(fun(X, Acc) -> Acc + erlang:abs(X - Y) end, 0, List).

%% nearest palindrome <= X
-spec lower_pal(integer()) -> integer().
lower_pal(X) ->
    S = integer_to_list(X),
    L = length(S),
    K = (L + 1) div 2,
    PrefixStr = lists:sublist(S, K),
    PalStr = make_pal(PrefixStr, L),
    Pal = list_to_integer(PalStr),
    case Pal =< X of
        true -> Pal;
        false ->
            PrefixInt = list_to_integer(PrefixStr) - 1,
            case PrefixInt =< 0 of
                true ->
                    All9Len = L - 1,
                    case All9Len of
                        0 -> 0;
                        _ -> list_to_integer(lists:duplicate(All9Len, $9))
                    end;
                false ->
                    NewPrefixStr = integer_to_list(PrefixInt),
                    case length(NewPrefixStr) < K of
                        true ->
                            All9Len = L - 1,
                            case All9Len of
                                0 -> 0;
                                _ -> list_to_integer(lists:duplicate(All9Len, $9))
                            end;
                        false ->
                            Pal2Str = make_pal(NewPrefixStr, L),
                            list_to_integer(Pal2Str)
                    end
            end
    end.

%% nearest palindrome >= X
-spec higher_pal(integer()) -> integer().
higher_pal(X) ->
    S = integer_to_list(X),
    L = length(S),
    K = (L + 1) div 2,
    PrefixStr = lists:sublist(S, K),
    PalStr = make_pal(PrefixStr, L),
    Pal = list_to_integer(PalStr),
    case Pal >= X of
        true -> Pal;
        false ->
            PrefixInt = list_to_integer(PrefixStr) + 1,
            NewPrefixStr = integer_to_list(PrefixInt),
            case length(NewPrefixStr) > K of
                true ->
                    %% overflow, e.g., 999 -> 1001
                    list_to_integer([ $1 | lists:duplicate(L - 1, $0) ++ [$1] ]);
                false ->
                    Pal2Str = make_pal(NewPrefixStr, L),
                    list_to_integer(Pal2Str)
            end
    end.

%% construct palindrome string from prefix and total length
-spec make_pal(string(), integer()) -> string().
make_pal(PrefixStr, Len) ->
    case Len rem 2 of
        0 -> % even length
            lists:flatten([PrefixStr, lists:reverse(PrefixStr)]);
        1 -> % odd length
            PrefixLen = length(PrefixStr),
            Left = lists:sublist(PrefixStr, PrefixLen - 1),
            Mid = lists:nth(PrefixLen, PrefixStr),
            lists:flatten([Left, [Mid], lists:reverse(Left)])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(nums :: [integer]) :: integer
  def minimum_cost(nums) do
    palins = generate_palindromes()
    sorted_nums = Enum.sort(nums)
    n = length(sorted_nums)
    median = Enum.at(sorted_nums, div(n - 1, 2))

    {upper, lower} = find_candidates(palins, median)

    [upper, lower]
    |> Enum.filter(& &1)
    |> Enum.map(fn y -> total_cost(nums, y) end)
    |> Enum.min()
  end

  defp generate_palindromes do
    max = 1_000_000_000 - 1

    palins =
      for len <- 1..9,
          half_len = div(len + 1, 2),
          start = :math.pow(10, half_len - 1) |> trunc,
          finish = :math.pow(10, half_len) |> trunc - 1,
          prefix <- start..finish do
        build_palindrome(prefix, len)
      end

    palins
    |> Enum.filter(&(&1 <= max))
    |> Enum.sort()
  end

  defp build_palindrome(prefix, len) do
    s = Integer.to_string(prefix)
    rev = String.reverse(s)

    if rem(len, 2) == 0 do
      (s <> rev) |> String.to_integer()
    else
      trimmed_rev = String.slice(rev, 1..-1)
      (s <> trimmed_rev) |> String.to_integer()
    end
  end

  defp find_candidates(palins, median) do
    idx = Enum.find_index(palins, fn p -> p >= median end)

    cond do
      idx == nil ->
        {nil, List.last(palins)}

      true ->
        upper = Enum.at(palins, idx)
        lower = if idx == 0, do: nil, else: Enum.at(palins, idx - 1)
        {upper, lower}
    end
  end

  defp total_cost(nums, y) do
    Enum.reduce(nums, 0, fn v, acc -> acc + abs(v - y) end)
  end
end
```
