# 2818. Apply Operations to Maximize Score

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modPow(long long a, long long e) {
        long long res = 1 % MOD;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
    
    vector<int> spf; // smallest prime factor
    
    void buildSPF(int limit) {
        spf.assign(limit + 1, 0);
        for (int i = 2; i <= limit; ++i) {
            if (!spf[i]) {
                spf[i] = i;
                if ((long long)i * i <= limit)
                    for (int j = i * i; j <= limit; j += i)
                        if (!spf[j]) spf[j] = i;
            }
        }
        spf[1] = 1;
    }
    
    int primeScore(int x) {
        if (x == 1) return 0;
        int cnt = 0;
        while (x > 1) {
            int p = spf[x];
            ++cnt;
            while (x % p == 0) x /= p;
        }
        return cnt;
    }
    
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        int maxVal = *max_element(nums.begin(), nums.end());
        buildSPF(maxVal);
        
        vector<int> score(n);
        for (int i = 0; i < n; ++i) score[i] = primeScore(nums[i]);
        
        // left: previous index with score >= current
        vector<int> left(n, -1), right(n, n);
        vector<int> st;
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && score[st.back()] < score[i]) st.pop_back();
            if (!st.empty()) left[i] = st.back();
            st.push_back(i);
        }
        // right: next index with score > current
        st.clear();
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && score[st.back()] <= score[i]) st.pop_back();
            if (!st.empty()) right[i] = st.back();
            st.push_back(i);
        }
        
        vector<long long> ranges(n);
        for (int i = 0; i < n; ++i) {
            long long l = i - left[i];
            long long r = right[i] - i;
            ranges[i] = l * r;
        }
        
        // indices sorted by nums value descending
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return nums[a] > nums[b];
        });
        
        long long remaining = k;
        long long ans = 1;
        for (int id : idx) {
            if (remaining == 0) break;
            long long use = min(ranges[id], remaining);
            if (use > 0) {
                ans = ans * modPow(nums[id], use) % MOD;
                remaining -= use;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;

    public int maximumScore(List<Integer> numsList, int k) {
        int n = numsList.size();
        int[] nums = new int[n];
        int maxVal = 0;
        for (int i = 0; i < n; i++) {
            nums[i] = numsList.get(i);
            if (nums[i] > maxVal) maxVal = nums[i];
        }

        // smallest prime factor sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long) i * i <= maxVal) {
                    for (int j = i * i; j <= maxVal; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        // prime scores
        int[] score = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int cnt = 0;
            while (x > 1) {
                int p = spf[x];
                cnt++;
                while (x % p == 0) x /= p;
            }
            score[i] = cnt;
        }

        // left: nearest index with score >= current
        int[] left = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && score[stack.peek()] < score[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        // right: nearest index with score > current
        int[] right = new int[n];
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && score[stack.peek()] <= score[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        long[] ranges = new long[n];
        for (int i = 0; i < n; i++) {
            long leftChoices = i - left[i];
            long rightChoices = right[i] - i;
            ranges[i] = leftChoices * rightChoices;
        }

        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(nums[b], nums[a]));

        long remainingK = k;
        long ans = 1L;
        for (int id : idx) {
            if (remainingK == 0) break;
            long use = Math.min(ranges[id], remainingK);
            if (use > 0) {
                ans = ans * modPow(nums[id], use) % MOD;
                remainingK -= use;
            }
        }

        return (int) ans;
    }

    private long modPow(long base, long exp) {
        long res = 1L;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0:
            return 1

        max_val = max(nums)

        # smallest prime factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        def distinct_prime_cnt(x):
            cnt = 0
            prev = 0
            while x > 1:
                p = spf[x]
                if p != prev:
                    cnt += 1
                    prev = p
                while x % p == 0:
                    x //= p
            return cnt

        # prime scores
        s = [distinct_prime_cnt(v) for v in nums]

        # left: nearest index with score >= current (or -1)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and s[stack[-1]] < s[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # right: nearest index with score > current (or n)
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and s[stack[-1]] < s[i]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)

        # number of subarrays where i is the chosen element
        ranges = [(i - left[i]) * (right[i] - i) for i in range(n)]

        # process numbers in decreasing order of value
        indices = sorted(range(n), key=lambda i: nums[i], reverse=True)
        ans = 1
        remaining = k
        for idx in indices:
            if remaining == 0:
                break
            cnt = ranges[idx]
            if cnt <= 0:
                continue
            use = cnt if cnt < remaining else remaining
            ans = (ans * pow(nums[idx], use, MOD)) % MOD
            remaining -= use

        return ans
```

## Python3

```python
import sys
from typing import List

MOD = 10**9 + 7

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_val = max(nums)

        # smallest prime factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        # compute distinct prime factor counts (prime scores)
        scores = [0] * n
        for idx, val in enumerate(nums):
            x = val
            cnt = 0
            while x > 1:
                p = spf[x]
                cnt += 1
                while x % p == 0:
                    x //= p
            scores[idx] = cnt

        # left: nearest index with score >= current
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # right: nearest index with score > current
        right = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # number of subarrays where each index is chosen
        ranges = [(i - left[i]) * (right[i] - i) for i in range(n)]

        # process indices by descending nums value
        order = sorted(range(n), key=lambda i: nums[i], reverse=True)

        ans = 1
        remaining = k
        for idx in order:
            if remaining == 0:
                break
            use = ranges[idx]
            if use > remaining:
                use = remaining
            if use:
                ans = (ans * pow(nums[idx], use, MOD)) % MOD
                remaining -= use

        return ans
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

typedef long long ll;

static ll modpow(ll a, ll e) {
    ll res = 1 % MOD;
    a %= MOD;
    while (e > 0) {
        if (e & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return res;
}

typedef struct {
    int val;
    int idx;
} Pair;

static int cmpPairDesc(const void *p1, const void *p2) {
    const Pair *a = (const Pair *)p1;
    const Pair *b = (const Pair *)p2;
    if (a->val < b->val) return 1;
    if (a->val > b->val) return -1;
    return 0;
}

int maximumScore(int* nums, int numsSize, int k) {
    int n = numsSize;
    /* find max value for SPF sieve */
    int maxVal = 0;
    for (int i = 0; i < n; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];

    /* smallest prime factor array */
    int *spf = (int *)calloc(maxVal + 1, sizeof(int));
    for (int i = 2; i <= maxVal; ++i) {
        if (spf[i] == 0) {
            spf[i] = i;
            if ((ll)i * i <= maxVal) {
                for (int j = i * i; j <= maxVal; j += i)
                    if (spf[j] == 0) spf[j] = i;
            }
        }
    }

    /* prime scores */
    int *score = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int x = nums[i];
        int cnt = 0;
        while (x > 1) {
            int p = spf[x];
            cnt++;
            while (x % p == 0) x /= p;
        }
        score[i] = cnt;
    }

    free(spf);

    /* left: previous index with score >= current */
    int *left = (int *)malloc(n * sizeof(int));
    int *stack = (int *)malloc(n * sizeof(int));
    int top = -1;
    for (int i = 0; i < n; ++i) {
        while (top >= 0 && score[stack[top]] < score[i]) top--;
        left[i] = (top == -1) ? -1 : stack[top];
        stack[++top] = i;
    }

    /* right: next index with score > current */
    int *right = (int *)malloc(n * sizeof(int));
    top = -1;
    for (int i = n - 1; i >= 0; --i) {
        while (top >= 0 && score[stack[top]] <= score[i]) top--;
        right[i] = (top == -1) ? n : stack[top];
        stack[++top] = i;
    }

    free(stack);
    free(score);

    /* ranges count for each index */
    ll *ranges = (ll *)malloc(n * sizeof(ll));
    for (int i = 0; i < n; ++i) {
        ll leftCnt = i - left[i];
        ll rightCnt = right[i] - i;
        ranges[i] = leftCnt * rightCnt;
    }

    /* sort indices by nums value descending */
    Pair *arr = (Pair *)malloc(n * sizeof(Pair));
    for (int i = 0; i < n; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
    }
    qsort(arr, n, sizeof(Pair), cmpPairDesc);

    ll remainingK = k;
    ll ans = 1LL;

    for (int i = 0; i < n && remainingK > 0; ++i) {
        int idx = arr[i].idx;
        if (ranges[idx] == 0) continue;
        ll use = ranges[idx];
        if (use > remainingK) use = remainingK;
        ans = (ans * modpow((ll)arr[i].val, use)) % MOD;
        remainingK -= use;
    }

    free(left);
    free(right);
    free(ranges);
    free(arr);

    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1_000_000_007L;

    private static int PrimeScore(int x) {
        int cnt = 0;
        for (int p = 2; p * p <= x; ++p) {
            if (x % p == 0) {
                cnt++;
                while (x % p == 0) x /= p;
            }
        }
        if (x > 1) cnt++;
        return cnt;
    }

    private static long ModPow(long @base, long exp) {
        long result = 1L;
        long b = @base % MOD;
        while (exp > 0) {
            if ((exp & 1L) == 1L) result = (result * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return result;
    }

    public int MaximumScore(IList<int> nums, int k) {
        int n = nums.Count;
        int[] a = new int[n];
        for (int i = 0; i < n; ++i) a[i] = nums[i];

        // compute prime scores
        int[] s = new int[n];
        for (int i = 0; i < n; ++i) {
            s[i] = PrimeScore(a[i]);
        }

        // left: nearest index with score >= current
        int[] left = new int[n];
        var stack = new Stack<int>();
        for (int i = 0; i < n; ++i) {
            while (stack.Count > 0 && s[stack.Peek()] < s[i]) stack.Pop();
            left[i] = stack.Count == 0 ? -1 : stack.Peek();
            stack.Push(i);
        }

        // right: nearest index with score > current
        int[] right = new int[n];
        stack.Clear();
        for (int i = n - 1; i >= 0; --i) {
            while (stack.Count > 0 && s[stack.Peek()] <= s[i]) stack.Pop();
            right[i] = stack.Count == 0 ? n : stack.Peek();
            stack.Push(i);
        }

        long[] cnt = new long[n];
        for (int i = 0; i < n; ++i) {
            cnt[i] = (long)(i - left[i]) * (right[i] - i);
        }

        // indices sorted by value descending
        int[] idx = new int[n];
        for (int i = 0; i < n; ++i) idx[i] = i;
        Array.Sort(idx, (i1, i2) => {
            int cmp = a[i2].CompareTo(a[i1]); // descending by value
            if (cmp != 0) return cmp;
            return i1.CompareTo(i2);
        });

        long remaining = k;
        long answer = 1L;

        foreach (int i in idx) {
            if (remaining == 0) break;
            long use = Math.Min(cnt[i], remaining);
            if (use > 0) {
                answer = (answer * ModPow(a[i], use)) % MOD;
                remaining -= use;
            }
        }

        return (int)answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumScore = function(nums, k) {
    const MOD = 1000000007n;
    const n = nums.length;

    // ---------- prime scores ----------
    let maxVal = 0;
    for (let v of nums) if (v > maxVal) maxVal = v;
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; ++i) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxVal) {
                for (let j = i * i; j <= maxVal; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }
    const primeScore = new Array(n);
    for (let i = 0; i < n; ++i) {
        let x = nums[i];
        let cnt = 0;
        while (x > 1) {
            const p = spf[x];
            cnt++;
            while (x % p === 0) x = Math.trunc(x / p);
        }
        primeScore[i] = cnt;
    }

    // ---------- left (>=) ----------
    const left = new Array(n);
    let stack = [];
    for (let i = 0; i < n; ++i) {
        while (stack.length && primeScore[stack[stack.length - 1]] < primeScore[i]) {
            stack.pop();
        }
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // ---------- right (>) ----------
    const right = new Array(n);
    stack = [];
    for (let i = n - 1; i >= 0; --i) {
        while (stack.length && primeScore[stack[stack.length - 1]] <= primeScore[i]) {
            stack.pop();
        }
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }

    // ---------- modular exponent ----------
    function modPow(base, exp) {
        let b = BigInt(base) % MOD;
        let e = BigInt(exp);
        let res = 1n;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    }

    // ---------- process in decreasing value ----------
    const order = Array.from({ length: n }, (_, i) => i);
    order.sort((a, b) => nums[b] - nums[a]);

    let remaining = k;
    let ans = 1n;

    for (const idx of order) {
        if (remaining === 0) break;
        const cnt = (idx - left[idx]) * (right[idx] - idx); // number of subarrays where idx is chosen
        if (cnt <= 0) continue;
        const use = Math.min(remaining, cnt);
        ans = (ans * modPow(nums[idx], use)) % MOD;
        remaining -= use;
    }

    return Number(ans);
};
```

## Typescript

```typescript
function maximumScore(nums: number[], k: number): number {
    const MOD = 1000000007n;
    const n = nums.length;

    // ---------- Sieve for smallest prime factor ----------
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;
    const spf = new Uint32Array(maxVal + 1);
    const primes: number[] = [];
    for (let i = 2; i <= maxVal; i++) {
        if (spf[i] === 0) {
            spf[i] = i;
            primes.push(i);
        }
        for (let j = 0; j < primes.length && primes[j] <= spf[i] && i * primes[j] <= maxVal; j++) {
            spf[i * primes[j]] = primes[j];
        }
    }

    // ---------- Compute prime scores ----------
    const score: number[] = new Array(n);
    for (let idx = 0; idx < n; idx++) {
        let x = nums[idx];
        let cnt = 0;
        while (x > 1) {
            const p = spf[x];
            cnt++;
            while (x % p === 0) x = Math.floor(x / p);
        }
        score[idx] = cnt;
    }

    // ---------- Compute left boundaries (prev >=) ----------
    const left: number[] = new Array(n).fill(-1);
    const stackL: number[] = [];
    for (let i = 0; i < n; i++) {
        while (stackL.length && score[stackL[stackL.length - 1]] < score[i]) {
            stackL.pop();
        }
        left[i] = stackL.length ? stackL[stackL.length - 1] : -1;
        stackL.push(i);
    }

    // ---------- Compute right boundaries (next >) ----------
    const right: number[] = new Array(n).fill(n);
    const stackR: number[] = [];
    for (let i = 0; i < n; i++) {
        while (stackR.length && score[i] > score[stackR[stackR.length - 1]]) {
            const idx = stackR.pop() as number;
            right[idx] = i;
        }
        stackR.push(i);
    }

    // ---------- Number of subarrays where each index is chosen ----------
    const ranges: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        const leftCount = i - left[i];
        const rightCount = right[i] - i;
        ranges[i] = leftCount * rightCount;
    }

    // ---------- Sort indices by nums value descending ----------
    const idxs = Array.from({ length: n }, (_, i) => i);
    idxs.sort((a, b) => nums[b] - nums[a]);

    // ---------- Modular exponentiation ----------
    function modPow(base: bigint, exp: number): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if (e & 1) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1;
        }
        return result;
    }

    // ---------- Apply operations ----------
    let remaining = k;
    let ans = 1n;
    for (const id of idxs) {
        if (remaining === 0) break;
        const use = Math.min(ranges[id], remaining);
        if (use > 0) {
            ans = (ans * modPow(BigInt(nums[id]), use)) % MOD;
            remaining -= use;
        }
    }

    return Number(ans);
}
```

## Php

```php
class Solution {

    const MOD = 1000000007;

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumScore($nums, $k) {
        $n = count($nums);
        if ($n == 0) return 1;

        // ---------- smallest prime factor sieve ----------
        $maxVal = max($nums);
        $spf = range(0, $maxVal); // spf[i] = i initially
        for ($i = 2; $i * $i <= $maxVal; $i++) {
            if ($spf[$i] == $i) { // i is prime
                for ($j = $i * $i; $j <= $maxVal; $j += $i) {
                    if ($spf[$j] == $j) {
                        $spf[$j] = $i;
                    }
                }
            }
        }

        // ---------- compute prime scores ----------
        $score = array_fill(0, $n, 0);
        for ($idx = 0; $idx < $n; $idx++) {
            $x = $nums[$idx];
            $cnt = 0;
            while ($x > 1) {
                $p = $spf[$x];
                $cnt++;
                while ($x % $p == 0) {
                    $x = intdiv($x, $p);
                }
            }
            $score[$idx] = $cnt;
        }

        // ---------- left boundaries (nearest >=) ----------
        $left = array_fill(0, $n, -1);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $score[end($stack)] < $score[$i]) {
                array_pop($stack);
            }
            $left[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }

        // ---------- right boundaries (nearest >) ----------
        $right = array_fill(0, $n, $n);
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (!empty($stack) && $score[end($stack)] <= $score[$i]) {
                array_pop($stack);
            }
            $right[$i] = empty($stack) ? $n : end($stack);
            $stack[] = $i;
        }

        // ---------- number of subarrays where each index is chosen ----------
        $ranges = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $l = $i - $left[$i];
            $r = $right[$i] - $i;
            $ranges[$i] = $l * $r; // fits in 64-bit
        }

        // ---------- sort indices by value descending ----------
        $pairs = [];
        for ($i = 0; $i < $n; $i++) {
            $pairs[] = [$nums[$i], $i];
        }
        usort($pairs, function($a, $b) {
            if ($a[0] == $b[0]) return 0;
            return ($a[0] > $b[0]) ? -1 : 1; // descending by value
        });

        // ---------- apply operations ----------
        $result = 1;
        foreach ($pairs as $pair) {
            if ($k <= 0) break;
            [$val, $idx] = $pair;
            $use = min($ranges[$idx], $k);
            if ($use == 0) continue;
            $result = ($result * $this->modPow($val, $use)) % self::MOD;
            $k -= $use;
        }

        return $result;
    }

    private function modPow($base, $exp) {
        $mod = self::MOD;
        $base %= $mod;
        $res = 1;
        while ($exp > 0) {
            if ($exp & 1) {
                $res = ($res * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $res;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 0 { return 1 }
        
        // Sieve for smallest prime factor up to max(nums)
        let maxVal = nums.max()!
        var spf = Array(repeating: 0, count: maxVal + 1)
        var primes = [Int]()
        for i in 2...maxVal {
            if spf[i] == 0 {
                spf[i] = i
                primes.append(i)
            }
            for p in primes {
                let v = i * p
                if v > maxVal { break }
                spf[v] = p
                if p == spf[i] { break }
            }
        }
        
        // Compute distinct prime counts (prime scores)
        var score = Array(repeating: 0, count: n)
        for idx in 0..<n {
            var x = nums[idx]
            var cnt = 0
            var lastPrime = 0
            while x > 1 {
                let p = spf[x]
                if p != lastPrime {
                    cnt += 1
                    lastPrime = p
                }
                while x % p == 0 {
                    x /= p
                }
            }
            score[idx] = cnt
        }
        
        // Compute left boundaries (previous index with score >= current)
        var left = Array(repeating: -1, count: n)
        var stack = [Int]()
        for i in 0..<n {
            while let last = stack.last, score[last] < score[i] {
                stack.removeLast()
            }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        
        // Compute right boundaries (next index with score > current)
        var right = Array(repeating: n, count: n)
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, score[last] <= score[i] {
                stack.removeLast()
            }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        
        // Number of subarrays where each index is dominant
        var ranges = Array(repeating: Int64(0), count: n)
        for i in 0..<n {
            let leftCount = Int64(i - left[i])
            let rightCount = Int64(right[i] - i)
            ranges[i] = leftCount * rightCount
        }
        
        // Sort indices by nums value descending
        var order = Array(0..<n)
        order.sort { nums[$0] > nums[$1] }
        
        var remaining = Int64(k)
        var result: Int64 = 1
        for idx in order {
            if remaining == 0 { break }
            let cnt = min(ranges[idx], remaining)
            if cnt == 0 { continue }
            result = (result * Int64(modPow(nums[idx], cnt))) % Int64(MOD)
            remaining -= cnt
        }
        return Int(result)
    }
    
    private func modPow(_ base: Int, _ exp: Int64) -> Int {
        var result: Int64 = 1
        var b: Int64 = Int64(base % MOD)
        var e = exp
        let m = Int64(MOD)
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % m
            }
            b = (b * b) % m
            e >>= 1
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import kotlin.math.min

class Solution {
    private val MOD = 1_000_000_007L

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) {
                res = (res * b) % MOD
            }
            b = (b * b) % MOD
            e = e shr 1
        }
        return res
    }

    fun maximumScore(nums: List<Int>, k: Int): Int {
        val n = nums.size
        if (n == 0) return 1

        val maxVal = nums.maxOrNull() ?: 0
        // smallest prime factor sieve
        val spf = IntArray(maxVal + 1)
        for (i in 2..maxVal) {
            if (spf[i] == 0) {
                spf[i] = i
                if (i.toLong() * i <= maxVal) {
                    var j = i * i
                    while (j <= maxVal) {
                        if (spf[j] == 0) spf[j] = i
                        j += i
                    }
                }
            }
        }

        // prime scores (distinct prime factors)
        val score = IntArray(n)
        for (idx in 0 until n) {
            var x = nums[idx]
            var cnt = 0
            while (x > 1) {
                val p = spf[x]
                cnt++
                while (x % p == 0) {
                    x /= p
                }
            }
            score[idx] = cnt
        }

        // left: nearest index with score >= current
        val left = IntArray(n)
        val stackL = ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stackL.isEmpty() && score[stackL.peekLast()] < score[i]) {
                stackL.pollLast()
            }
            left[i] = if (stackL.isEmpty()) -1 else stackL.peekLast()
            stackL.addLast(i)
        }

        // right: nearest index with score > current
        val right = IntArray(n) { n }
        val stackR = ArrayDeque<Int>()
        for (i in n - 1 downTo 0) {
            while (!stackR.isEmpty() && score[stackR.peekLast()] <= score[i]) {
                stackR.pollLast()
            }
            right[i] = if (stackR.isEmpty()) n else stackR.peekLast()
            stackR.addLast(i)
        }

        // number of subarrays where each index is chosen
        val ranges = LongArray(n)
        for (i in 0 until n) {
            val leftCnt = i - left[i]
            val rightCnt = right[i] - i
            ranges[i] = leftCnt.toLong() * rightCnt.toLong()
        }

        // indices sorted by nums descending
        val order = (0 until n).toMutableList()
        order.sortWith { a, b ->
            if (nums[b] != nums[a]) nums[b] - nums[a] else a - b
        }

        var remaining = k.toLong()
        var ans = 1L
        for (idx in order) {
            if (remaining == 0L) break
            val use = min(ranges[idx], remaining)
            if (use > 0) {
                ans = ans * modPow(nums[idx].toLong(), use) % MOD
                remaining -= use
            }
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int maximumScore(List<int> nums, int k) {
    final int n = nums.length;
    int maxVal = 0;
    for (var v in nums) if (v > maxVal) maxVal = v;

    // Smallest prime factor sieve
    final List<int> spf = List.filled(maxVal + 1, 0);
    for (int i = 2; i <= maxVal; ++i) {
      if (spf[i] == 0) {
        spf[i] = i;
        if (i * i <= maxVal) {
          for (int j = i * i; j <= maxVal; j += i) {
            if (spf[j] == 0) spf[j] = i;
          }
        }
      }
    }

    // Prime scores
    final List<int> score = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int x = nums[i];
      int cnt = 0;
      while (x > 1) {
        final int p = spf[x];
        cnt++;
        while (x % p == 0) x ~/= p;
      }
      score[i] = cnt;
    }

    // left: nearest index with score >= current
    final List<int> left = List.filled(n, -1);
    final List<int> stack = [];
    for (int i = 0; i < n; ++i) {
      while (stack.isNotEmpty && score[stack.last] < score[i]) {
        stack.removeLast();
      }
      left[i] = stack.isEmpty ? -1 : stack.last;
      stack.add(i);
    }

    // right: nearest index with score > current
    final List<int> right = List.filled(n, n);
    stack.clear();
    for (int i = n - 1; i >= 0; --i) {
      while (stack.isNotEmpty && score[stack.last] <= score[i]) {
        stack.removeLast();
      }
      right[i] = stack.isEmpty ? n : stack.last;
      stack.add(i);
    }

    // number of subarrays where each element is chosen
    final List<int> ranges = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int leftCnt = i - left[i];
      int rightCnt = right[i] - i;
      ranges[i] = leftCnt * rightCnt;
    }

    // indices sorted by nums descending
    final List<int> idx = List.generate(n, (i) => i);
    idx.sort((a, b) => nums[b].compareTo(nums[a]));

    int remaining = k;
    int ans = 1;

    for (final id in idx) {
      if (remaining == 0) break;
      int cnt = ranges[id];
      if (cnt > remaining) cnt = remaining;
      if (cnt == 0) continue;
      ans = (ans * _modPow(nums[id] % _mod, cnt)) % _mod;
      remaining -= cnt;
    }

    return ans;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    int e = exp;
    while (e > 0) {
      if ((e & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      e >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

const MOD int64 = 1000000007

func maximumScore(nums []int, k int) int {
	n := len(nums)
	if n == 0 {
		return 1
	}
	maxVal := 0
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}
	// smallest prime factor sieve
	spf := make([]int, maxVal+1)
	for i := 2; i <= maxVal; i++ {
		if spf[i] == 0 {
			for j := i; j <= maxVal; j += i {
				if spf[j] == 0 {
					spf[j] = i
				}
			}
		}
	}
	// prime scores (distinct prime factors)
	score := make([]int, n)
	for idx, v := range nums {
		x := v
		cnt := 0
		for x > 1 {
			p := spf[x]
			cnt++
			for x%p == 0 {
				x /= p
			}
		}
		score[idx] = cnt
	}
	// left: nearest index with score >= current
	left := make([]int, n)
	stack := []int{}
	for i := 0; i < n; i++ {
		for len(stack) > 0 && score[stack[len(stack)-1]] < score[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	// right: nearest index with score > current
	right := make([]int, n)
	stack = []int{}
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && score[stack[len(stack)-1]] <= score[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = n
		} else {
			right[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	// number of subarrays where each index is chosen
	ranges := make([]int64, n)
	for i := 0; i < n; i++ {
		l := int64(i - left[i])
		r := int64(right[i] - i)
		ranges[i] = l * r
	}
	// indices sorted by nums value descending
	indices := make([]int, n)
	for i := 0; i < n; i++ {
		indices[i] = i
	}
	sort.Slice(indices, func(i, j int) bool {
		return nums[indices[i]] > nums[indices[j]]
	})
	remaining := int64(k)
	ans := int64(1)
	for _, idx := range indices {
		if remaining == 0 {
			break
		}
		cnt := ranges[idx]
		if cnt > remaining {
			cnt = remaining
		}
		if cnt > 0 {
			ans = ans * powMod(nums[idx], cnt) % MOD
			remaining -= cnt
		}
	}
	return int(ans)
}

func powMod(a int, e int64) int64 {
	base := int64(a % int(MOD))
	res := int64(1)
	for e > 0 {
		if e&1 == 1 {
			res = res * base % MOD
		}
		base = base * base % MOD
		e >>= 1
	}
	return res
}
```

## Ruby

```ruby
def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = (result * b) % mod if (e & 1) == 1
    b = (b * b) % mod
    e >>= 1
  end
  result
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
  mod = 1_000_000_007
  n = nums.length
  max_val = nums.max

  # smallest prime factor sieve
  spf = Array.new(max_val + 1, 0)
  (2..max_val).each do |i|
    if spf[i] == 0
      spf[i] = i
      if i * i <= max_val
        j = i * i
        while j <= max_val
          spf[j] = i if spf[j] == 0
          j += i
        end
      end
    end
  end

  # prime scores (distinct prime factors)
  prime_scores = Array.new(n, 0)
  nums.each_with_index do |val, idx|
    x = val
    cnt = 0
    while x > 1
      p = spf[x]
      p = x if p == 0
      cnt += 1
      while (x % p).zero?
        x /= p
      end
    end
    prime_scores[idx] = cnt
  end

  # left boundaries: previous index with score >= current
  left = Array.new(n, -1)
  stack = []
  (0...n).each do |i|
    while !stack.empty? && prime_scores[stack[-1]] < prime_scores[i]
      stack.pop
    end
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end

  # right boundaries: next index with score > current
  right = Array.new(n, n)
  stack.clear
  (n - 1).downto(0) do |i|
    while !stack.empty? && prime_scores[stack[-1]] <= prime_scores[i]
      stack.pop
    end
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end

  # number of subarrays where each index is chosen
  ranges = Array.new(n, 0)
  (0...n).each do |i|
    left_cnt = i - left[i]
    right_cnt = right[i] - i
    ranges[i] = left_cnt * right_cnt
  end

  # process numbers in decreasing order
  idxs = (0...n).to_a.sort_by { |i| -nums[i] }

  ans = 1
  remaining = k
  idxs.each do |i|
    break if remaining <= 0
    use = ranges[i]
    use = remaining if use > remaining
    next if use == 0
    ans = (ans * mod_pow(nums[i], use, mod)) % mod
    remaining -= use
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumScore(nums: List[Int], k: Int): Int = {
        val MOD = 1000000007L
        val n = nums.length
        val arr = nums.toArray

        // Find max value for sieve
        var maxVal = 0
        var i = 0
        while (i < n) {
            if (arr(i) > maxVal) maxVal = arr(i)
            i += 1
        }

        // Smallest prime factor sieve
        val spf = new Array[Int](maxVal + 1)
        var p = 2
        while (p <= maxVal) {
            if (spf(p) == 0) {
                var j = p
                while (j <= maxVal) {
                    if (spf(j) == 0) spf(j) = p
                    j += p
                }
            }
            p += 1
        }

        // Compute distinct prime factor count for each number
        val score = new Array[Int](n)
        i = 0
        while (i < n) {
            var x = arr(i)
            var cnt = 0
            var last = 0
            while (x > 1) {
                val prime = spf(x)
                if (prime != last) {
                    cnt += 1
                    last = prime
                }
                while (x % prime == 0) x /= prime
            }
            score(i) = cnt
            i += 1
        }

        // left[i]: nearest index to the left with score >= current
        val left = new Array[Int](n)
        val stackL = new java.util.ArrayDeque[Int]()
        i = 0
        while (i < n) {
            while (!stackL.isEmpty && score(stackL.peekLast()) < score(i)) stackL.pollLast()
            left(i) = if (stackL.isEmpty) -1 else stackL.peekLast()
            stackL.addLast(i)
            i += 1
        }

        // right[i]: nearest index to the right with score > current
        val right = Array.fill[Int](n)(n)
        val stackR = new java.util.ArrayDeque[Int]()
        i = 0
        while (i < n) {
            while (!stackR.isEmpty && score(stackR.peekLast()) < score(i)) {
                val idx = stackR.pollLast()
                right(idx) = i
            }
            // equal scores are not popped
            stackR.addLast(i)
            i += 1
        }

        // Number of subarrays where each index is chosen
        val ranges = new Array[Long](n)
        i = 0
        while (i < n) {
            val leftCnt = i - left(i)
            val rightCnt = right(i) - i
            ranges(i) = leftCnt.toLong * rightCnt.toLong
            i += 1
        }

        // Indices sorted by value descending
        val idxArray = (0 until n).toArray
        java.util.Arrays.sort(idxArray, new java.util.Comparator[Int] {
            override def compare(a: Int, b: Int): Int = {
                if (arr(b) != arr(a)) Integer.compare(arr(b), arr(a))
                else Integer.compare(a, b)
            }
        })

        // Fast modular exponentiation
        def modPow(base: Long, exp: Long): Long = {
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

        var remaining = k.toLong
        var result = 1L
        var pos = 0
        while (remaining > 0 && pos < n) {
            val idx = idxArray(pos)
            val use = math.min(ranges(idx), remaining)
            if (use > 0) {
                result = (result * modPow(arr(idx).toLong, use)) % MOD
                remaining -= use
            }
            pos += 1
        }

        ((result % MOD).toInt)
    }
}
```

## Rust

```rust
use std::cmp::Reverse;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res: i64 = 1;
    base %= MOD;
    while exp > 0 {
        if exp & 1 == 1 {
            res = res * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    res
}

pub struct Solution;

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 1;
        }

        // ---------- prime scores ----------
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut spf = vec![0usize; max_val + 1];
        for i in 2..=max_val {
            if spf[i] == 0 {
                for j in (i..=max_val).step_by(i) {
                    if spf[j] == 0 {
                        spf[j] = i;
                    }
                }
            }
        }

        let mut prime_score = vec![0usize; n];
        for (idx, &val) in nums.iter().enumerate() {
            let mut x = val as usize;
            let mut cnt = 0usize;
            while x > 1 {
                let p = spf[x];
                cnt += 1;
                while x % p == 0 {
                    x /= p;
                }
            }
            prime_score[idx] = cnt;
        }

        // ---------- left (>=) ----------
        let mut left: Vec<isize> = vec![-1; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..n {
            while let Some(&top) = stack.last() {
                if prime_score[top] < prime_score[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            left[i] = if let Some(&top) = stack.last() {
                top as isize
            } else {
                -1
            };
            stack.push(i);
        }

        // ---------- right (>) ----------
        let mut right: Vec<usize> = vec![n; n];
        stack.clear();
        for i in (0..n).rev() {
            while let Some(&top) = stack.last() {
                if prime_score[top] <= prime_score[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            right[i] = if let Some(&top) = stack.last() {
                top
            } else {
                n
            };
            stack.push(i);
        }

        // ---------- ranges ----------
        let mut ranges: Vec<i64> = vec![0; n];
        for i in 0..n {
            let l = (i as isize - left[i]) as i64;
            let r = (right[i] as i64 - i as i64) as i64;
            ranges[i] = l * r;
        }

        // ---------- process in descending nums ----------
        let mut indices: Vec<usize> = (0..n).collect();
        indices.sort_by_key(|&i| Reverse(nums[i]));

        let mut remaining = k as i64;
        let mut ans: i64 = 1;

        for &idx in &indices {
            if remaining == 0 {
                break;
            }
            let take = std::cmp::min(ranges[idx], remaining);
            if take > 0 {
                ans = ans * mod_pow(nums[idx] as i64, take) % MOD;
                remaining -= take;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; fast exponentiation modulo MOD
(define (pow-mod base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) MOD)
              (quotient e 2)
              (if (odd? e) (modulo (* res b) MOD) res)))))

;; build smallest prime factor array up to limit
(define (build-spf limit)
  (let ((spf (make-vector (+ limit 1) 0)))
    (for ([i (in-range 2 (add1 limit))])
      (when (= (vector-ref spf i) 0)
        (vector-set! spf i i)
        (let ((start (* i i)))
          (when (<= start limit)
            (for ([j (in-range start (add1 limit) i)])
              (when (= (vector-ref spf j) 0)
                (vector-set! spf j i))))))
    spf))

;; distinct prime factor count using spf
(define (prime-score num spf)
  (let loop ((x num) (cnt 0))
    (if (= x 1)
        cnt
        (let ((p (vector-ref spf x)))
          (let inner ((y x))
            (if (zero? (remainder y p))
                (inner (/ y p))
                y))
          => (let ((new-x (let inner ((y x))
                            (if (zero? (remainder y p))
                                (inner (/ y p))
                                y))))
              (loop new-x (+ cnt 1)))))))

;; main function
(define/contract (maximum-score nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (max-val (apply max nums))
         (spf (build-spf max-val))
         ;; compute prime scores
         (s (make-vector n 0))
         (left (make-vector n -1))
         (right (make-vector n n))
         (ranges (make-vector n 0)))
    ;; fill s
    (for ([i (in-range n)])
      (vector-set! s i (prime-score (vector-ref nums-vec i) spf)))
    ;; compute left: previous index with score >= current
    (let ((stack '()))
      (for ([i (in-range n)])
        (let ((cur (vector-ref s i)))
          (let loop ()
            (when (and (not (null? stack))
                       (< (vector-ref s (car stack)) cur))
              (set! stack (cdr stack))
              (loop))))
          (if (null? stack)
              (vector-set! left i -1)
              (vector-set! left i (car stack)))
          (set! stack (cons i stack))))
    ;; compute right: next index with score > current
    (let ((stack '()))
      (for ([i (in-range (sub1 n) -1 -1)])
        (let ((cur (vector-ref s i)))
          (let loop ()
            (when (and (not (null? stack))
                       (<= (vector-ref s (car stack)) cur))
              (set! stack (cdr stack))
              (loop))))
          (if (null? stack)
              (vector-set! right i n)
              (vector-set! right i (car stack)))
          (set! stack (cons i stack))))
    ;; compute ranges
    (for ([i (in-range n)])
      (let* ((l (vector-ref left i))
             (r (vector-ref right i))
             (cnt (* (- i l) (- r i))))
        (vector-set! ranges i cnt)))
    ;; create list of (value . index) pairs and sort descending by value
    (require racket/list)
    (define pairs
      (for/list ([i (in-range n)])
        (cons (vector-ref nums-vec i) i)))
    (define sorted-pairs
      (sort pairs (lambda (a b) (> (car a) (car b)))))
    ;; iterate and accumulate answer
    (let loop ((lst sorted-pairs) (remaining k) (ans 1))
      (if (or (= remaining 0) (null? lst))
          ans
          (let* ((pair (car lst))
                 (val (car pair))
                 (idx (cdr pair))
                 (cnt (min remaining (vector-ref ranges idx))))
            (define new-ans
              (if (> cnt 0)
                  (modulo (* ans (pow-mod val cnt)) MOD)
                  ans))
            (loop (cdr lst) (- remaining cnt) new-ans))))))
```

## Erlang

```erlang
-module(solution).
-compile(export_all).
-define(MOD, 1000000007).

-spec maximum_score(Nums :: [integer()], K :: integer()) -> integer().
maximum_score(Nums, K) ->
    Scores = [prime_score(N) || N <- Nums],
    Pairs = lists:zip(lists:seq(0, length(Nums) - 1), Scores),
    Left = compute_left(Pairs),
    Right = compute_right(Pairs),
    Indices = lists:seq(0, length(Nums) - 1),
    Counts = [ (I - L) * (R - I)
               || {I, L, R} <- lists:zip3(Indices, Left, Right) ],
    Indexed = [{Num, Idx, Cnt}
                || {Num, Idx, Cnt} <- lists:zip3(Nums, Indices, Counts)],
    Sorted = lists:sort(fun({N1,_,_}, {N2,_,_}) -> N1 > N2 end, Indexed),
    compute_answer(Sorted, K, 1).

%% prime score (number of distinct prime factors)
prime_score(N) -> prime_score(N, 2, 0).

prime_score(1, _P, Cnt) -> Cnt;
prime_score(N, P, Cnt) when P * P > N ->
    case N of
        1 -> Cnt;
        _ -> Cnt + 1
    end;
prime_score(N, P, Cnt) ->
    case N rem P of
        0 ->
            NewN = divide_out(N, P),
            prime_score(NewN, P + 1, Cnt + 1);
        _ ->
            prime_score(N, P + 1, Cnt)
    end.

divide_out(N, P) when N rem P == 0 -> divide_out(N div P, P);
divide_out(N, _) -> N.

%% compute left boundaries where s[left] >= s[i]
compute_left(Pairs) ->
    {RevLeft, _} = lists:foldl(
        fun({Idx, Score}, {Stack, Acc}) ->
            NewStack = pop_left(Stack, Score),
            LeftIdx = case NewStack of
                [] -> -1;
                [{LIdx,_}|_] -> LIdx
            end,
            {[{Idx,Score}|NewStack], [LeftIdx|Acc]}
        end,
        {[], []},
        Pairs),
    lists:reverse(RevLeft).

pop_left([], _Score) -> [];
pop_left([{_, S}=Top|Rest], Score) when S < Score ->
    pop_left(Rest, Score);
pop_left(Stack, _) -> Stack.

%% compute right boundaries where s[right] > s[i]
compute_right(Pairs) ->
    RevPairs = lists:reverse(Pairs),
    N = length(Pairs),
    {RevRight, _} = lists:foldl(
        fun({Idx, Score}, {Stack, Acc}) ->
            NewStack = pop_right(Stack, Score),
            RightIdx = case NewStack of
                [] -> N;
                [{RIdx,_}|_] -> RIdx
            end,
            {[{Idx,Score}|NewStack], [RightIdx|Acc]}
        end,
        {[], []},
        RevPairs),
    lists:reverse(RevRight).

pop_right([], _Score) -> [];
pop_right([{_, S}=Top|Rest], Score) when S =< Score ->
    pop_right(Rest, Score);
pop_right(Stack, _) -> Stack.

%% compute final answer using sorted elements
compute_answer(_, 0, Ans) -> Ans;
compute_answer([], _, Ans) -> Ans;
compute_answer([{Num,_Idx,Cnt}|Rest], K, Ans) ->
    Use = if Cnt < K -> Cnt; true -> K end,
    NewAns = (Ans * pow_mod(Num rem ?MOD, Use)) rem ?MOD,
    compute_answer(Rest, K - Use, NewAns).

%% fast modular exponentiation
pow_mod(_, 0) -> 1;
pow_mod(Base, Exp) ->
    pow_mod_loop(Base, Exp, 1).

pow_mod_loop(_Base, 0, Acc) -> Acc;
pow_mod_loop(Base, Exp, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem ?MOD,
    pow_mod_loop((Base * Base) rem ?MOD, Exp bsr 1, NewAcc);
pow_mod_loop(Base, Exp, Acc) ->
    pow_mod_loop((Base * Base) rem ?MOD, Exp bsr 1, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec maximum_score(nums :: [integer], k :: integer) :: integer
  def maximum_score(nums, k) do
    n = length(nums)

    # prime scores for each number
    ps = Enum.map(nums, &prime_score/1)

    left_arr = compute_left(ps)
    right_arr = compute_right(ps)

    # build list of {value, index, rangeCount}
    items =
      for i <- 0..(n - 1) do
        left = :array.get(i, left_arr)
        right = :array.get(i, right_arr)
        range = (i - left) * (right - i)
        {Enum.at(nums, i), i, range}
      end

    # sort by value descending
    sorted = Enum.sort_by(items, fn {val, _, _} -> -val end)

    mod = 1_000_000_007
    process(sorted, k, 1, mod)
  end

  # ---------- prime score ----------
  defp prime_score(num), do: count_factors(num, 2, 0)

  defp count_factors(1, _i, cnt), do: cnt

  defp count_factors(n, i, cnt) when i * i > n do
    cnt + 1
  end

  defp count_factors(n, i, cnt) do
    if rem(n, i) == 0 do
      n2 = divide_out(n, i)
      count_factors(n2, i + 1, cnt + 1)
    else
      count_factors(n, i + 1, cnt)
    end
  end

  defp divide_out(n, p) do
    if rem(n, p) == 0 do
      divide_out(div(n, p), p)
    else
      n
    end
  end

  # ---------- left boundaries ----------
  defp compute_left(ps) do
    n = length(ps)

    {left_arr, _stack} =
      Enum.with_index(ps)
      |> Enum.reduce({:array.new(n, default: -1), []}, fn {s, i},
                                                         {arr, stack} ->
        new_stack = pop_while_lt(stack, s)

        left_i =
          case new_stack do
            [] -> -1
            [{_, idx} | _] -> idx
          end

        arr2 = :array.set(i, left_i, arr)
        {arr2, [{s, i} | new_stack]}
      end)

    left_arr
  end

  defp pop_while_lt([], _s), do: []

  defp pop_while_lt([{score, _} = top | rest] = stack, s) when score < s,
    do: pop_while_lt(rest, s)

  defp pop_while_lt(stack, _s), do: stack

  # ---------- right boundaries ----------
  defp compute_right(ps) do
    n = length(ps)

    {right_arr, _stack} =
      Enum.with_index(Enum.reverse(ps))
      |> Enum.reduce({:array.new(n, default: n), []}, fn {s_rev, rev_i},
                                                         {arr, stack} ->
        i = n - 1 - rev_i
        new_stack = pop_while_le(stack, s_rev)

        right_i =
          case new_stack do
            [] -> n
            [{_, idx} | _] -> idx
          end

        arr2 = :array.set(i, right_i, arr)
        {arr2, [{s_rev, i} | new_stack]}
      end)

    right_arr
  end

  defp pop_while_le([], _s), do: []

  defp pop_while_le([{score, _} = top | rest] = stack, s) when score <= s,
    do: pop_while_le(rest, s)

  defp pop_while_le(stack, _s), do: stack

  # ---------- processing ----------
  defp process([], _k, acc, _mod), do: acc
  defp process(_, 0, acc, _mod), do: acc

  defp process([{val, _idx, range} | rest], k, acc, mod) do
    cnt = if range < k, do: range, else: k
    pow = mod_pow(val, cnt, mod)
    new_acc = rem(acc * pow, mod)
    process(rest, k - cnt, new_acc, mod)
  end

  # ---------- modular exponentiation ----------
  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) when exp > 0 do
    pow_mod(rem(base, mod), exp, mod, 1)
  end

  defp pow_mod(_b, 0, _m, acc), do: acc

  defp pow_mod(b, e, m, acc) do
    acc = if rem(e, 2) == 1, do: rem(acc * b, m), else: acc
    b = rem(b * b, m)
    pow_mod(b, div(e, 2), m, acc)
  end
end
```
