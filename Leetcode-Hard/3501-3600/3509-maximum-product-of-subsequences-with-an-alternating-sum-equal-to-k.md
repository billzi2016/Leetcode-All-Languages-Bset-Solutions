# 3509. Maximum Product of Subsequences With an Alternating Sum Equal to K

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        const int MAX_VAL = 12;
        const int N_MAX = 150;
        const int MAX_SUM = MAX_VAL * N_MAX; // 1800
        const int OFFSET = MAX_SUM;
        const int SZ = 2 * MAX_SUM + 1;      // 3601

        using Bitset = bitset<SZ>;

        vector<unordered_map<int, Bitset>> dp(2); // parity 0 or 1

        for (int x : nums) {
            auto olddp = dp; // snapshot before using current element

            // start new subsequence with only this element
            if (x <= limit) {
                int idx = OFFSET + x; // first element has positive sign
                dp[1][x].set(idx);
            }

            for (int p = 0; p < 2; ++p) {
                int sign = (p == 0) ? 1 : -1;
                int np = 1 - p;
                for (const auto& kv : olddp[p]) {
                    int prod = kv.first;
                    const Bitset& bs = kv.second;

                    long long newProdLL = 1LL * prod * x;
                    if (newProdLL > limit) continue;
                    int newProd = (int)newProdLL;

                    int shift = sign * x;
                    Bitset shifted;
                    if (shift >= 0)
                        shifted = (bs << shift);
                    else
                        shifted = (bs >> (-shift));

                    dp[np][newProd] |= shifted;
                }
            }
        }

        int targetIdx = OFFSET + k;
        if (targetIdx < 0 || targetIdx >= SZ) return -1;

        int ans = -1;
        for (int p = 0; p < 2; ++p) {
            for (const auto& kv : dp[p]) {
                int prod = kv.first;
                const Bitset& bs = kv.second;
                if (bs.test(targetIdx)) {
                    ans = max(ans, prod);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxProduct(int[] nums, int k, int limit) {
        int n = nums.length;
        int maxSum = n * 12; // maximum possible absolute alternating sum
        int offset = maxSum;
        int range = maxSum * 2 + 1;

        BitSet[][] dpCurr = new BitSet[2][range];
        BitSet[][] dpNext = new BitSet[2][range];
        for (int p = 0; p < 2; ++p) {
            for (int i = 0; i < range; ++i) {
                dpCurr[p][i] = new BitSet(limit + 1);
                dpNext[p][i] = new BitSet(limit + 1);
            }
        }

        for (int val : nums) {
            // clear next layer
            for (int p = 0; p < 2; ++p) {
                for (int i = 0; i < range; ++i) {
                    dpNext[p][i].clear();
                }
            }

            // start a new subsequence with this element alone
            if (val <= limit) {
                int idx = offset + val; // first element is at even index -> added
                if (idx >= 0 && idx < range) {
                    dpNext[1][idx].set(val); // length becomes 1, next parity = 1
                }
            }

            for (int par = 0; par < 2; ++par) {
                for (int sumIdx = 0; sumIdx < range; ++sumIdx) {
                    BitSet bs = dpCurr[par][sumIdx];
                    if (bs.isEmpty()) continue;

                    // skip current element: keep existing states
                    dpNext[par][sumIdx].or(bs);

                    // take current element
                    int newPar = 1 - par;
                    int delta = (par == 0) ? val : -val;
                    int newIdx = sumIdx + delta;
                    if (newIdx < 0 || newIdx >= range) continue;

                    for (int p = bs.nextSetBit(0); p >= 0; p = bs.nextSetBit(p + 1)) {
                        long prodLong = (long) p * val;
                        if (prodLong > limit) continue;
                        int newProd = (int) prodLong;
                        dpNext[newPar][newIdx].set(newProd);
                    }
                }
            }

            // swap layers
            BitSet[][] tmp = dpCurr;
            dpCurr = dpNext;
            dpNext = tmp;
        }

        int targetIdx = k + offset;
        if (targetIdx < 0 || targetIdx >= range) return -1;

        for (int p = limit; p >= 0; --p) {
            if (dpCurr[0][targetIdx].get(p) || dpCurr[1][targetIdx].get(p)) {
                return p;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def maxProduct(self, nums, k, limit):
        """
        :type nums: List[int]
        :type k: int
        :type limit: int
        :rtype: int
        """
        from collections import defaultdict

        # dp[parity][sum] = set of achievable products (<=limit)
        # parity 0 -> next element will be added (+), parity 1 -> next element will be subtracted (-)
        dp = [defaultdict(set), defaultdict(set)]

        for num in nums:
            new_dp = [defaultdict(set), defaultdict(set)]

            # start a new subsequence with current number
            if num <= limit:
                new_dp[1][num].add(num)   # length becomes 1, next parity is odd (1)

            # extend existing subsequences
            for p in (0, 1):
                for s, prod_set in dp[p].items():
                    for prod in prod_set:
                        new_sum = s + num if p == 0 else s - num
                        new_prod = prod * num
                        if new_prod <= limit:
                            np = 1 - p
                            new_dp[np][new_sum].add(new_prod)

            # keep old subsequences (skip current element)
            for p in (0, 1):
                for s, prod_set in dp[p].items():
                    if s in new_dp[p]:
                        new_dp[p][s].update(prod_set)
                    else:
                        new_dp[p][s] = set(prod_set)

            dp = new_dp

        best = -1
        for p in (0, 1):
            if k in dp[p]:
                best = max(best, max(dp[p][k]))
        return best
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        dp = [defaultdict(set), defaultdict(set)]  # parity 0 (next even), 1 (next odd)
        for x in nums:
            ndp0 = defaultdict(set)
            ndp1 = defaultdict(set)

            # skip current element
            for s, prods in dp[0].items():
                ndp0[s].update(prods)
            for s, prods in dp[1].items():
                ndp1[s].update(prods)

            if x == 0:
                # product becomes 0 regardless of previous product
                for p in (0, 1):
                    src = dp[p]
                    dst = ndp1 if p == 0 else ndp0
                    sign = 1 if p == 0 else -1
                    for s in src:
                        ns = s + sign * x  # unchanged
                        dst[ns].add(0)
            else:
                for p in (0, 1):
                    src = dp[p]
                    dst = ndp1 if p == 0 else ndp0  # parity flips after inclusion
                    sign = 1 if p == 0 else -1
                    for s, prods in src.items():
                        ns = s + sign * x
                        for v in prods:
                            nv = v * x
                            if nv <= limit:
                                dst[ns].add(nv)

            # start a new subsequence with only this element
            if x <= limit:
                ndp1[x].add(x)  # after first element, next index is odd (parity 1)

            dp = [ndp0, ndp1]

        ans = -1
        for p in (0, 1):
            if k in dp[p]:
                ans = max(ans, max(dp[p][k]))
        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int maxProduct(int* nums, int numsSize, int k, int limit) {
    const int MAX_VAL = 12;
    const int MAX_N = 150;
    const int MAX_SUM = MAX_VAL * MAX_N;               // 1800
    const int SHIFT = MAX_SUM;
    const int S = 2 * MAX_SUM + 1;                     // range of possible sums

    int totalStates = 2 * S;                          // parity * sum index

    // each state stores reachable products (0..limit)
    typedef struct {
        unsigned char used;   // flag to know if set is non‑empty
        unsigned short *vals;
        int cap, sz;
    } ProdSet;

    // simple dynamic array for small integers (product values)
    #define INIT_CAP 4
    ProdSet *cur = (ProdSet*)calloc(totalStates, sizeof(ProdSet));
    ProdSet *nxt = (ProdSet*)calloc(totalStates, sizeof(ProdSet));

    int *active_cur = (int*)malloc(totalStates * sizeof(int));
    int active_cur_sz = 0;
    int *active_nxt = (int*)malloc(totalStates * sizeof(int));
    int active_nxt_sz = 0;

    // helper to ensure capacity and insert value if not present
    #define INSERT(setPtr, val)                         \
        do {                                             \
            ProdSet *ps = setPtr;                        \
            int found = 0;                               \
            for (int i = 0; i < ps->sz; ++i) {           \
                if (ps->vals[i] == (val)) { found = 1; break; }\
            }                                            \
            if (!found) {                                \
                if (ps->sz == ps->cap) {                 \
                    int newCap = ps->cap ? ps->cap * 2 : INIT_CAP; \
                    ps->vals = (unsigned short*)realloc(ps->vals, newCap * sizeof(unsigned short));\
                    ps->cap = newCap;                   \
                }                                        \
                ps->vals[ps->sz++] = (val);              \
                if (!ps->used) {                         \
                    ps->used = 1;                        \
                    active_nxt[active_nxt_sz++] = ((char*)ps - (char*)nxt) / sizeof(ProdSet); \
                }                                        \
            }                                            \
        } while (0)

    for (int idx = 0; idx < numsSize; ++idx) {
        int num = nums[idx];
        active_nxt_sz = 0;
        // transition from existing states
        for (int i = 0; i < active_cur_sz; ++i) {
            int stateIdx = active_cur[i];
            int parity = stateIdx / S;
            int sumIdx = stateIdx % S;
            ProdSet *psCur = &cur[stateIdx];

            // skip: keep same state
            for (int pi = 0; pi < psCur->sz; ++pi) {
                INSERT(&nxt[stateIdx], psCur->vals[pi]);
            }

            // take current number
            int newParity = 1 - parity;
            int delta = (parity == 0) ? num : -num;
            int newSumIdx = sumIdx + delta;
            if (newSumIdx < 0 || newSumIdx >= S) continue;
            int newStateIdx = newParity * S + newSumIdx;

            for (int pi = 0; pi < psCur->sz; ++pi) {
                unsigned short prod = psCur->vals[pi];
                if (num == 0) {
                    INSERT(&nxt[newStateIdx], 0);
                } else {
                    long long np = (long long)prod * num;
                    if (np <= limit) INSERT(&nxt[newStateIdx], (unsigned short)np);
                }
            }
        }

        // start new subsequence with only this element
        int startParity = 1;                     // after taking one element length is odd
        int startSumIdx = SHIFT + num;           // first element contributes positively
        if (startSumIdx >= 0 && startSumIdx < S) {
            int startStateIdx = startParity * S + startSumIdx;
            if (num <= limit) INSERT(&nxt[startStateIdx], (unsigned short)num);
            if (num == 0) INSERT(&nxt[startStateIdx], 0);
        }

        // swap cur and nxt
        ProdSet *tmp = cur; cur = nxt; nxt = tmp;
        int *tmpAct = active_cur; active_cur = active_nxt; active_nxt = tmpAct;
        active_cur_sz = active_nxt_sz;
    }

    int targetIdx = SHIFT + k;
    if (targetIdx < 0 || targetIdx >= S) {
        // clean up
        for (int i = 0; i < totalStates; ++i) { free(cur[i].vals); free(nxt[i].vals); }
        free(cur); free(nxt);
        free(active_cur); free(active_nxt);
        return -1;
    }

    int answer = -1;
    for (int parity = 0; parity <= 1; ++parity) {
        int idxState = parity * S + targetIdx;
        ProdSet *ps = &cur[idxState];
        if (!ps->used) continue;
        for (int i = 0; i < ps->sz; ++i) {
            if (ps->vals[i] > answer) answer = ps->vals[i];
        }
    }

    // clean up
    for (int i = 0; i < totalStates; ++i) { free(cur[i].vals); free(nxt[i].vals); }
    free(cur); free(nxt);
    free(active_cur); free(active_nxt);

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxProduct(int[] nums, int k, int limit) {
        int n = nums.Length;
        int maxSum = 12 * n; // maximum possible absolute sum
        int offset = maxSum;
        int sumSize = 2 * maxSum + 1;
        if (k < -maxSum || k > maxSum) return -1;

        bool[][] even = new bool[limit + 1][];
        bool[][] odd = new bool[limit + 1][];

        List<int> activeEven = new List<int>();
        HashSet<int> setEven = new HashSet<int>();
        List<int> activeOdd = new List<int>();
        HashSet<int> setOdd = new HashSet<int>();

        foreach (int val in nums) {
            // start a new subsequence with this element
            int prodStart = val;
            if (prodStart <= limit) {
                if (odd[prodStart] == null) odd[prodStart] = new bool[sumSize];
                int idx = offset + val; // sum = val
                odd[prodStart][idx] = true;
                if (!setOdd.Contains(prodStart)) {
                    setOdd.Add(prodStart);
                    activeOdd.Add(prodStart);
                }
            }

            // snapshot current active lists to avoid using newly added states in this iteration
            var curEven = new List<int>(activeEven);
            foreach (int prod in curEven) {
                int newProd = prod * val;
                if (newProd > limit) continue;
                bool[] src = even[prod];
                if (src == null) continue;
                if (odd[newProd] == null) odd[newProd] = new bool[sumSize];
                bool[] dst = odd[newProd];

                // shift left by val (add to sum)
                for (int i = 0, limitIdx = sumSize - val; i < limitIdx; ++i) {
                    if (src[i]) dst[i + val] = true;
                }
                if (!setOdd.Contains(newProd)) {
                    setOdd.Add(newProd);
                    activeOdd.Add(newProd);
                }
            }

            var curOdd = new List<int>(activeOdd);
            foreach (int prod in curOdd) {
                int newProd = prod * val;
                if (newProd > limit) continue;
                bool[] src = odd[prod];
                if (src == null) continue;
                if (even[newProd] == null) even[newProd] = new bool[sumSize];
                bool[] dst = even[newProd];

                // shift right by val (subtract from sum)
                for (int i = val; i < sumSize; ++i) {
                    if (src[i]) dst[i - val] = true;
                }
                if (!setEven.Contains(newProd)) {
                    setEven.Add(newProd);
                    activeEven.Add(newProd);
                }
            }
        }

        int targetIdx = offset + k;
        for (int prod = limit; prod >= 0; --prod) {
            if (even[prod] != null && even[prod][targetIdx]) return prod;
            if (odd[prod] != null && odd[prod][targetIdx]) return prod;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} limit
 * @return {number}
 */
var maxProduct = function(nums, k, limit) {
    const n = nums.length;
    const maxSum = 12 * Math.ceil(n / 2); // maximum absolute alternating sum possible
    if (k < -maxSum || k > maxSum) return -1;
    const offset = maxSum;
    const size = 2 * maxSum + 1;

    // dp[parity][sumIdx] -> Set of reachable products (<= limit)
    let dp = [new Array(size), new Array(size)];
    // initially empty, no subsequence taken

    for (const num of nums) {
        const ndp0 = new Array(size);
        const ndp1 = new Array(size);
        const ndp = [ndp0, ndp1];

        // helper to add product into ndp
        const add = (par, idx, prod) => {
            if (prod > limit) return;
            let set = ndp[par][idx];
            if (!set) {
                set = new Set();
                ndp[par][idx] = set;
            }
            set.add(prod);
        };

        // start a new subsequence with this element alone
        const idxStart = offset + num; // position 0 (even), contribution +num
        add(1, idxStart, num); // length becomes 1 => parity 1

        // extend existing subsequences
        for (let par = 0; par <= 1; ++par) {
            const curArr = dp[par];
            for (let idx = 0; idx < size; ++idx) {
                const set = curArr[idx];
                if (!set) continue;
                const curSum = idx - offset;
                for (const prod of set) {
                    // place current num at position indicated by parity 'par'
                    const newParity = par ^ 1;
                    const newSum = (par === 0) ? curSum + num : curSum - num;
                    if (newSum < -maxSum || newSum > maxSum) continue; // out of reachable range
                    const newIdx = newSum + offset;
                    const newProd = prod * num;
                    add(newParity, newIdx, newProd);
                }
            }
        }

        dp = ndp;
    }

    let ans = -1;
    const targetIdx = k + offset;
    if (targetIdx >= 0 && targetIdx < size) {
        for (let par = 0; par <= 1; ++par) {
            const set = dp[par][targetIdx];
            if (!set) continue;
            for (const prod of set) {
                if (prod <= limit && prod > ans) ans = prod;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxProduct(nums: number[], k: number, limit: number): number {
    const n = nums.length;
    const maxSum = 12 * n; // maximum possible absolute alternating sum
    const shift = maxSum;   // to handle negative sums as indices

    // dp[parity] maps sumIdx -> Set of reachable products (<= limit)
    const dp: Array<Map<number, Set<number>>> = [new Map(), new Map()];

    for (const x of nums) {
        // Start a new subsequence with the current element alone
        if (x <= limit) {
            const sumIdx = shift + x; // parity after taking one element becomes 1 (next index odd)
            let set = dp[1].get(sumIdx);
            if (!set) {
                set = new Set<number>();
                dp[1].set(sumIdx, set);
            }
            set.add(x);
        }

        // Snapshot current states to avoid using newly added ones in this iteration
        const oldDP0 = new Map(dp[0]);
        const oldDP1 = new Map(dp[1]);

        // Transitions from parity 0 (next position is even)
        for (const [sumIdx, prodSet] of oldDP0.entries()) {
            for (const prod of prodSet) {
                const newProd = prod * x;
                if (newProd > limit) continue;
                const newParity = 1; // flip parity
                const newSumIdx = sumIdx + x; // even position adds the value
                let set = dp[newParity].get(newSumIdx);
                if (!set) {
                    set = new Set<number>();
                    dp[newParity].set(newSumIdx, set);
                }
                set.add(newProd);
            }
        }

        // Transitions from parity 1 (next position is odd)
        for (const [sumIdx, prodSet] of oldDP1.entries()) {
            for (const prod of prodSet) {
                const newProd = prod * x;
                if (newProd > limit) continue;
                const newParity = 0; // flip parity
                const newSumIdx = sumIdx - x; // odd position subtracts the value
                let set = dp[newParity].get(newSumIdx);
                if (!set) {
                    set = new Set<number>();
                    dp[newParity].set(newSumIdx, set);
                }
                set.add(newProd);
            }
        }
    }

    const targetIdx = k + shift;
    if (targetIdx < 0 || targetIdx > 2 * maxSum) return -1;

    let answer = -1;
    for (const parity of [0, 1] as const) {
        const set = dp[parity].get(targetIdx);
        if (!set) continue;
        for (const prod of set) {
            if (prod > answer) answer = prod;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $limit
     * @return Integer
     */
    function maxProduct($nums, $k, $limit) {
        $n = count($nums);
        $maxNum = 12; // given constraint
        $MAX_SUM = $n * $maxNum;               // maximum absolute alternating sum
        $OFFSET   = $MAX_SUM;
        $SIZE     = $MAX_SUM * 2 + 1;

        // dp[parity][sumIndex] = max product (<= limit) achieving this sum with given parity
        $dp = [
            array_fill(0, $SIZE, -1), // parity 0: next element will be added with '+'
            array_fill(0, $SIZE, -1)  // parity 1: next element will be added with '-'
        ];

        foreach ($nums as $num) {
            // start new subsequence consisting only of current number
            $newParity = 1; // length becomes odd, so next sign will be '-'
            $sumIdx    = $OFFSET + $num; // sum = +num
            if ($num <= $limit) {
                if ($dp[$newParity][$sumIdx] < $num) {
                    $dp[$newParity][$sumIdx] = $num;
                }
            }

            // copy current dp to work on extensions without affecting iteration
            $next = [
                $dp[0],
                $dp[1]
            ];

            for ($parity = 0; $parity <= 1; ++$parity) {
                $sign = ($parity == 0) ? 1 : -1;
                $newParityExt = 1 - $parity;

                for ($s = 0; $s < $SIZE; ++$s) {
                    $currProd = $dp[$parity][$s];
                    if ($currProd === -1) continue;

                    $newSumIdx = $s + $sign * $num;
                    if ($newSumIdx < 0 || $newSumIdx >= $SIZE) continue;

                    // compute new product
                    if ($num == 0) {
                        $newProd = 0;
                    } else {
                        $newProd = $currProd * $num;
                        if ($newProd > $limit) continue; // cannot use, exceeds limit
                    }

                    if ($next[$newParityExt][$newSumIdx] < $newProd) {
                        $next[$newParityExt][$newSumIdx] = $newProd;
                    }
                }
            }

            // update dp for next iteration
            $dp = $next;
        }

        // retrieve answer for required alternating sum k
        if ($k < -$MAX_SUM || $k > $MAX_SUM) {
            return -1;
        }
        $idx = $k + $OFFSET;
        $ans = max($dp[0][$idx], $dp[1][$idx]);

        return $ans === -1 ? -1 : $ans;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func maxProduct(_ nums: [Int], _ k: Int, _ limit: Int) -> Int {
        let n = nums.count
        let maxSum = n * 12
        let offset = maxSum
        let sumRange = 2 * maxSum + 1
        let wordSize = 64
        let words = (limit + wordSize) / wordSize
        
        func setBit(_ arr: inout [UInt64], _ value: Int) {
            let idx = value >> 6          // value / 64
            let pos = value & 63          // value % 64
            arr[idx] |= (1 << UInt64(pos))
        }
        
        var dp = Array(repeating: Array(repeating: [UInt64](repeating: 0, count: words), count: sumRange), count: 2)
        
        for num in nums {
            let oldDP = dp
            var newDP = dp   // start with previous states (skip current element)
            
            // start a new subsequence consisting only of this element
            if num <= limit {
                let sIdx = num + offset
                setBit(&newDP[1][sIdx], num)   // length becomes 1 -> parity 1 (odd)
            }
            
            for parity in 0...1 {
                let sign = (parity == 0) ? 1 : -1
                let nextParity = 1 - parity
                for sIdx in 0..<sumRange {
                    let bitArray = oldDP[parity][sIdx]
                    var hasAny = false
                    for w in bitArray where w != 0 { hasAny = true; break }
                    if !hasAny { continue }
                    
                    let newSumValBase = (sIdx - offset) + sign * num
                    if newSumValBase < -maxSum || newSumValBase > maxSum {
                        continue
                    }
                    let newSIdx = newSumValBase + offset
                    
                    for wIdx in 0..<words {
                        var word = bitArray[wIdx]
                        while word != 0 {
                            let tz = word.trailingZeroBitCount
                            let prod = (wIdx << 6) + tz   // wIdx*64 + tz
                            
                            var newProd: Int
                            if num == 0 {
                                newProd = 0
                            } else {
                                let mult = prod * num
                                if mult > limit {
                                    word &= word - 1
                                    continue
                                }
                                newProd = mult
                            }
                            setBit(&newDP[nextParity][newSIdx], newProd)
                            
                            word &= word - 1   // clear lowest set bit
                        }
                    }
                }
            }
            dp = newDP
        }
        
        let targetIdx = k + offset
        if targetIdx < 0 || targetIdx >= sumRange { return -1 }
        var best = -1
        for parity in 0...1 {
            let bits = dp[parity][targetIdx]
            for wIdx in 0..<words {
                var word = bits[wIdx]
                while word != 0 {
                    let tz = word.trailingZeroBitCount
                    let prod = (wIdx << 6) + tz
                    if prod > best { best = prod }
                    word &= word - 1
                }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProduct(nums: IntArray, k: Int, limit: Int): Int {
        val n = nums.size
        val shift = n * 12
        val size = shift * 2 + 1
        var cur = Array(2) { IntArray(size) { -1 } }

        for (num in nums) {
            val next = Array(2) { IntArray(size) { -1 } }
            // not taking current element
            for (p in 0..1) {
                for (i in 0 until size) {
                    val v = cur[p][i]
                    if (v != -1 && next[p][i] < v) {
                        next[p][i] = v
                    }
                }
            }
            // extend existing subsequences with current element
            for (p in 0..1) {
                for (i in 0 until size) {
                    val prod = cur[p][i]
                    if (prod == -1) continue
                    val newParity = 1 - p
                    var newIdx = i + if (p == 0) num else -num
                    if (newIdx < 0 || newIdx >= size) continue
                    val newProd = prod * num
                    if (newProd <= limit && next[newParity][newIdx] < newProd) {
                        next[newParity][newIdx] = newProd
                    }
                }
            }
            // start a new subsequence with only current element
            if (num <= limit) {
                val sumIdx = shift + num
                if (sumIdx in 0 until size && next[1][sumIdx] < num) {
                    next[1][sumIdx] = num
                }
            }
            cur = next
        }

        val targetIdx = k + shift
        var ans = -1
        if (targetIdx >= 0 && targetIdx < size) {
            for (p in 0..1) {
                val v = cur[p][targetIdx]
                if (v != -1 && v > ans) ans = v
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxProduct(List<int> nums, int k, int limit) {
    int n = nums.length;
    int maxSum = n * 12; // maximum possible absolute alternating sum
    int offset = maxSum;
    int size = 2 * maxSum + 1;

    List<List<int>> dp = [
      List.filled(size, -1), // parity 0 (next element will be added at even index)
      List.filled(size, -1)  // parity 1
    ];

    for (int x in nums) {
      // copy current states to next (skip case)
      List<List<int>> ndp = [
        List.from(dp[0]),
        List.from(dp[1])
      ];

      // start a new subsequence with only this element (sign +)
      if (x <= limit) {
        int idx = x + offset;
        ndp[1][idx] = max(ndp[1][idx], x);
      }

      for (int parity = 0; parity < 2; ++parity) {
        List<int> curRow = dp[parity];
        for (int idx = 0; idx < size; ++idx) {
          int prod = curRow[idx];
          if (prod == -1) continue;
          int sign = (parity == 0) ? 1 : -1;
          int newSum = (idx - offset) + sign * x;
          int newIdx = newSum + offset;
          if (newIdx < 0 || newIdx >= size) continue;
          int newProd = prod * x;
          if (newProd <= limit) {
            ndp[parity ^ 1][newIdx] = max(ndp[parity ^ 1][newIdx], newProd);
          }
        }
      }

      dp = ndp;
    }

    int targetIdx = k + offset;
    if (targetIdx < 0 || targetIdx >= size) return -1;

    int ans = max(dp[0][targetIdx], dp[1][targetIdx]);
    return ans == -1 ? -1 : ans;
  }
}
```

## Golang

```go
func maxProduct(nums []int, k int, limit int) int {
    n := len(nums)
    maxSum := n * 12
    shift := maxSum
    sumSize := 2*maxSum + 1

    words := (limit + 64) >> 6 // number of uint64 needed

    // dp[parity][sumIdx] -> bitset of reachable products
    dp := make([][][]uint64, 2)
    for p := 0; p < 2; p++ {
        dp[p] = make([][]uint64, sumSize)
        for i := 0; i < sumSize; i++ {
            dp[p][i] = make([]uint64, words)
        }
    }

    // empty subsequence: even length (parity 0), sum=0, product=1
    idx := 1 >> 6
    dp[0][shift][idx] |= 1 << (uint(1 & 63))

    hasOne := false
    for _, v := range nums {
        if v == 1 {
            hasOne = true
        }
    }

    // temporary DP for each iteration
    for _, val := range nums {
        dpNext := make([][][]uint64, 2)
        for p := 0; p < 2; p++ {
            dpNext[p] = make([][]uint64, sumSize)
            for i := 0; i < sumSize; i++ {
                dpNext[p][i] = make([]uint64, words)
                copy(dpNext[p][i], dp[p][i])
            }
        }

        for parity := 0; parity < 2; parity++ {
            nextParity := 1 - parity
            sign := val
            if parity == 1 { // odd length -> subtract
                sign = -val
            }
            for sIdx := 0; sIdx < sumSize; sIdx++ {
                srcBits := dp[parity][sIdx]
                // quick skip if empty
                empty := true
                for _, w := range srcBits {
                    if w != 0 {
                        empty = false
                        break
                    }
                }
                if empty {
                    continue
                }
                newSIdx := sIdx + sign
                if newSIdx < 0 || newSIdx >= sumSize {
                    continue
                }
                destBits := dpNext[nextParity][newSIdx]

                for wIdx, word := range srcBits {
                    for word != 0 {
                        b := bits.TrailingZeros64(word)
                        prod := wIdx*64 + b
                        if prod > limit {
                            break
                        }
                        newProd := prod * val
                        if newProd <= limit {
                            dw := newProd >> 6
                            dbit := uint(newProd & 63)
                            destBits[dw] |= 1 << dbit
                        }
                        word &= word - 1 // clear lowest set bit
                    }
                }
            }
        }

        dp = dpNext
    }

    targetIdx := k + shift
    if targetIdx < 0 || targetIdx >= sumSize {
        return -1
    }

    for p := limit; p >= 0; p-- {
        w := p >> 6
        mask := uint64(1) << (uint(p & 63))
        if dp[0][targetIdx][w]&mask != 0 {
            if !(p == 1 && k == 0 && !hasOne) { // exclude empty subsequence case
                return p
            }
        }
        if dp[1][targetIdx][w]&mask != 0 {
            return p
        }
    }
    return -1
}
```

## Ruby

```ruby
require 'set'

def max_product(nums, k, limit)
  OFFSET = 2000
  SHIFT_SUM = 13          # bits for sum offset
  SHIFT_PROD = 13         # bits for product (limit <= 5000 < 2^13)
  MASK = (1 << SHIFT_SUM) - 1
  LOW_BITS = SHIFT_SUM + SHIFT_PROD   # 26 bits for sum+product

  states = Set.new

  nums.each do |num|
    next_states = states.dup

    if num <= limit
      sum = num
      prod = num
      parity = 1                     # next operation will be subtraction
      key = (parity << LOW_BITS) | ((sum + OFFSET) << SHIFT_SUM) | prod
      next_states.add(key)
    end

    states.each do |key|
      parity = (key >> LOW_BITS) & 1
      sum = ((key >> SHIFT_SUM) & MASK) - OFFSET
      prod = key & ((1 << SHIFT_PROD) - 1)

      new_parity = 1 - parity
      new_sum = parity == 0 ? sum + num : sum - num
      new_prod = prod * num
      if new_prod <= limit
        new_key = (new_parity << LOW_BITS) | ((new_sum + OFFSET) << SHIFT_SUM) | new_prod
        next_states.add(new_key)
      end
    end

    states = next_states
  end

  max_product = -1
  states.each do |key|
    sum = ((key >> SHIFT_SUM) & MASK) - OFFSET
    prod = key & ((1 << SHIFT_PROD) - 1)
    if sum == k && prod <= limit && prod > max_product
      max_product = prod
    end
  end

  max_product
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def maxProduct(nums: Array[Int], k: Int, limit: Int): Int = {
    val maxSum = nums.sum
    val offset = maxSum
    val size = 2 * maxSum + 1

    // dp(parity)(sumIdx) -> set of reachable products (non‑empty subsequences)
    var dp = Array.ofDim[mutable.BitSet](2, size)
    for (p <- 0 until 2; s <- 0 until size) {
      dp(p)(s) = mutable.BitSet.empty
    }

    for (num <- nums) {
      val ndp = Array.ofDim[mutable.BitSet](2, size)
      for (p <- 0 until 2; s <- 0 until size) {
        ndp(p)(s) = mutable.BitSet.empty
      }

      // extend existing subsequences or skip them
      for (p <- 0 until 2) {
        val deltaSign = if (p == 0) num else -num
        for (sIdx <- 0 until size) {
          val curSet = dp(p)(sIdx)
          if (curSet.nonEmpty) {
            // skip: keep current state
            ndp(p)(sIdx) ++= curSet

            // take current number, extending subsequence
            val newP = 1 - p
            val newS = sIdx + deltaSign
            if (newS >= 0 && newS < size) {
              var it = curSet.iterator
              while (it.hasNext) {
                val prod = it.next()
                val newProd = prod * num
                if (newProd <= limit) ndp(newP)(newS) += newProd
              }
            }
          }
        }
      }

      // start a new subsequence consisting only of current number
      val startSumIdx = offset + num // first element is at even position => plus
      if (num <= limit && startSumIdx >= 0 && startSumIdx < size) {
        ndp(1)(startSumIdx) += num
      }

      dp = ndp
    }

    val targetIdx = k + offset
    if (targetIdx < 0 || targetIdx >= size) return -1

    var ans = -1
    for (p <- 0 until 2) {
      val set = dp(p)(targetIdx)
      if (set.nonEmpty) {
        val maxProd = set.max
        if (maxProd > ans) ans = maxProd
      }
    }
    ans
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn max_product(nums: Vec<i32>, k: i32, limit: i32) -> i32 {
        let n = nums.len();
        let max_sum = (n * 12) as i32;
        let offset = max_sum;
        let sz = (2 * max_sum + 1) as usize;

        // dp[parity][sum_index] = set of reachable products (<= limit)
        let mut dp: Vec<Vec<HashSet<u16>>> = vec![vec![HashSet::new(); sz]; 2];

        for &num_i in nums.iter() {
            let num = num_i as i32;
            // start with a copy of previous states (skip using the new element)
            let mut next = vec![vec![HashSet::new(); sz]; 2];
            for p in 0..2 {
                for s_idx in 0..sz {
                    if !dp[p][s_idx].is_empty() {
                        next[p][s_idx].extend(dp[p][s_idx].iter().cloned());
                    }
                }
            }

            // start a new subsequence with this element
            let sum_idx = (num + offset) as usize;
            if num <= limit && num >= 0 {
                next[1][sum_idx].insert(num as u16);
            }

            // transitions from existing states by taking current element
            for p in 0..2 {
                let new_p = 1 - p;
                for s_idx in 0..sz {
                    if dp[p][s_idx].is_empty() {
                        continue;
                    }
                    let cur_sum = s_idx as i32 - offset;
                    let delta = if p == 0 { num } else { -num };
                    let new_sum = cur_sum + delta;
                    if new_sum < -offset || new_sum > offset {
                        continue;
                    }
                    let new_s_idx = (new_sum + offset) as usize;
                    for &prod in dp[p][s_idx].iter() {
                        let new_prod_i = prod as i32 * num;
                        if new_prod_i <= limit && new_prod_i >= 0 {
                            next[new_p][new_s_idx].insert(new_prod_i as u16);
                        }
                    }
                }
            }

            dp = next;
        }

        if k < -offset || k > offset {
            return -1;
        }
        let target_idx = (k + offset) as usize;
        let mut ans: i32 = -1;
        for p in 0..2 {
            for &prod_u16 in dp[p][target_idx].iter() {
                let prod_i = prod_u16 as i32;
                if prod_i <= limit && prod_i > ans {
                    ans = prod_i;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-product nums k limit)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let ((dp-even (make-hash))
        (dp-odd (make-hash)))
    (define (add-state! parity sum prod)
      (when (<= prod limit)
        (let ((target (if (= parity 0) dp-even dp-odd)))
          (let ((s (hash-ref target sum
                             (lambda ()
                               (let ((new (make-hash))) (hash-set! target sum new) new)))))
            (hash-set! s prod #t)))))
    (for ([x nums])
      (define even-entries (hash->list dp-even))
      (define odd-entries (hash->list dp-odd))
      ;; extend subsequences whose next index is even (sign +)
      (for ([pair even-entries])
        (define sum (car pair))
        (define prod-set (cdr pair))
        (for ([prod (hash-keys prod-set)])
          (let ((new-prod (* prod x)))
            (when (<= new-prod limit)
              (add-state! 1 (+ sum x) new-prod)))))
      ;; extend subsequences whose next index is odd (sign -)
      (for ([pair odd-entries])
        (define sum (car pair))
        (define prod-set (cdr pair))
        (for ([prod (hash-keys prod-set)])
          (let ((new-prod (* prod x)))
            (when (<= new-prod limit)
              (add-state! 0 (- sum x) new-prod)))))
      ;; start a new subsequence with the current element
      (add-state! 1 x x))
    (define candidates '())
    (let ((set-even (hash-ref dp-even k (lambda () #f))))
      (when set-even
        (set! candidates (append candidates (hash-keys set-even)))))
    (let ((set-odd (hash-ref dp-odd k (lambda () #f))))
      (when set-odd
        (set! candidates (append candidates (hash-keys set-odd)))))
    (if (null? candidates)
        -1
        (apply max candidates))))
```

## Erlang

```erlang
-spec max_product(Nums :: [integer()], K :: integer(), Limit :: integer()) -> integer().
max_product(Nums, K, Limit) ->
    MaxSum = length(Nums) * 12,
    Shift = MaxSum,
    {DP0, DP1} = lists:foldl(fun(X, {D0, D1}) ->
        process_num(X, D0, D1, Shift, Limit)
    end, {#{}, #{}}, Nums),
    TargetIdx = K + Shift,
    Val0 = maps:get(TargetIdx, DP0, -1),
    Val1 = maps:get(TargetIdx, DP1, -1),
    Ans = erlang:max(Val0, Val1),
    if
        Ans == -1 -> -1;
        true -> Ans
    end.

-spec process_num(integer(), map(), map(), integer(), integer()) -> {map(), map()}.
process_num(X, DP0, DP1, Shift, Limit) ->
    % start a new subsequence with X (parity becomes 1)
    NewDP1 = if
        X =< Limit ->
            SumIdx = Shift + X,
            Prev = maps:get(SumIdx, DP1, -1),
            maps:put(SumIdx, erlang:max(Prev, X), DP1);
        true -> DP1
    end,
    % extend subsequences with even length (parity 0) by adding X (sum increases)
    NewDP1b = maps:fold(fun(SumIdx, Prod, Acc) ->
        NewProd = Prod * X,
        if
            NewProd =< Limit ->
                NewSumIdx = SumIdx + X,
                Prev2 = maps:get(NewSumIdx, Acc, -1),
                maps:put(NewSumIdx, erlang:max(Prev2, NewProd), Acc);
            true -> Acc
        end
    end, NewDP1, DP0),
    % extend subsequences with odd length (parity 1) by subtracting X (sum decreases)
    NewDP0b = maps:fold(fun(SumIdx, Prod, Acc) ->
        NewProd = Prod * X,
        if
            NewProd =< Limit ->
                NewSumIdx = SumIdx - X,
                Prev2 = maps:get(NewSumIdx, Acc, -1),
                maps:put(NewSumIdx, erlang:max(Prev2, NewProd), Acc);
            true -> Acc
        end
    end, DP0, DP1),
    {NewDP0b, NewDP1b}.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_product(nums :: [integer], k :: integer, limit :: integer) :: integer
  def max_product(nums, k, limit) do
    # Helper to add a product to the dp map
    add_prod = fn dp, parity, sum, prod ->
      key = {parity, sum}
      Map.update(dp, key, MapSet.new([prod]), fn set -> MapSet.put(set, prod) end)
    end

    # Initial empty dp (no subsequence yet)
    dp = %{}

    # Process each number
    dp =
      Enum.reduce(nums, dp, fn x, dp_acc ->
        new_dp = dp_acc

        # Start a new subsequence with this element alone
        if x <= limit do
          # After adding first element, next index parity is 1 (odd)
          new_dp = add_prod.(new_dp, 1, x, x)
        end

        # Extend existing subsequences
        Enum.reduce(dp_acc, new_dp, fn {{parity, sum}, prod_set}, dp_cur ->
          contribution = if parity == 0, do: x, else: -x
          new_sum = sum + contribution
          new_parity = 1 - parity

          Enum.reduce(prod_set, dp_cur, fn prod, acc_dp ->
            new_prod = prod * x
            if new_prod <= limit do
              add_prod.(acc_dp, new_parity, new_sum, new_prod)
            else
              acc_dp
            end
          end)
        end)
      end)

    # Find the maximum product with alternating sum equal to k
    answer =
      dp
      |> Enum.filter(fn {{_parity, sum}, _set} -> sum == k end)
      |> Enum.reduce(-1, fn {_key, set}, best ->
        max_in_set = Enum.max(set)
        if max_in_set > best, do: max_in_set, else: best
      end)

    answer
  end
end
```
