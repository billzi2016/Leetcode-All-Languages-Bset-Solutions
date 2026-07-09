# 3533. Concatenated Divisibility

## Cpp

```cpp
class Solution {
public:
    vector<int> concatenatedDivisibility(vector<int>& nums, int k) {
        int n = nums.size();
        int fullMask = (1 << n) - 1;
        // digit lengths
        vector<int> len(n);
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            int l = 0;
            while (x > 0) { ++l; x /= 10; }
            if (l == 0) l = 1; // just in case, though nums[i] >= 1
            len[i] = l;
        }
        // pow10 modulo k up to max length (6)
        int maxLen = 0;
        for (int l : len) maxLen = max(maxLen, l);
        vector<int> pow10mod(maxLen + 1, 1 % k);
        for (int i = 1; i <= maxLen; ++i) {
            pow10mod[i] = (pow10mod[i - 1] * 10) % k;
        }
        // dp forward: reachable states
        vector<vector<char>> dp(1 << n, vector<char>(k, 0));
        dp[0][0] = 1;
        for (int mask = 0; mask <= fullMask; ++mask) {
            for (int rem = 0; rem < k; ++rem) if (dp[mask][rem]) {
                for (int i = 0; i < n; ++i) if (!(mask & (1 << i))) {
                    int newMask = mask | (1 << i);
                    long long newRem = (1LL * rem * pow10mod[len[i]] + nums[i] % k) % k;
                    dp[newMask][newRem] = 1;
                }
            }
        }
        if (!dp[fullMask][0]) return {};
        // memo for canFinish
        vector<vector<int>> memo(1 << n, vector<int>(k, -1));
        function<bool(int,int)> canFinish = [&](int mask, int rem) -> bool {
            if (mask == fullMask) return rem == 0;
            int &res = memo[mask][rem];
            if (res != -1) return res;
            for (int i = 0; i < n; ++i) if (!(mask & (1 << i))) {
                int newRem = (int)((1LL * rem * pow10mod[len[i]] + nums[i] % k) % k);
                if (canFinish(mask | (1 << i), newRem)) return res = 1;
            }
            return res = 0;
        };
        // reconstruct lexicographically smallest permutation
        vector<int> ans;
        int mask = 0, rem = 0;
        while (mask != fullMask) {
            vector<pair<int,int>> cand; // (value,index)
            for (int i = 0; i < n; ++i) if (!(mask & (1 << i))) {
                cand.emplace_back(nums[i], i);
            }
            sort(cand.begin(), cand.end());
            bool placed = false;
            for (auto [val, idx] : cand) {
                int newRem = (int)((1LL * rem * pow10mod[len[idx]] + nums[idx] % k) % k);
                if (canFinish(mask | (1 << idx), newRem)) {
                    ans.push_back(val);
                    mask |= (1 << idx);
                    rem = newRem;
                    placed = true;
                    break;
                }
            }
            if (!placed) break; // should not happen
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int[] nums;
    private int k;
    private int n;
    private int fullMask;
    private int[] len;
    private int[] powLenMod;
    private int[] modNum;
    private int[][] memo; // -1 unknown, 0 false, 1 true

    public int[] concatenatedDivisibility(int[] nums, int k) {
        this.nums = nums;
        this.k = k;
        this.n = nums.length;
        this.fullMask = (1 << n) - 1;

        len = new int[n];
        powLenMod = new int[n];
        modNum = new int[n];

        // precompute lengths, num % k and 10^{len} % k
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int digits = 0;
            while (x > 0) {
                digits++;
                x /= 10;
            }
            len[i] = digits;
            modNum[i] = nums[i] % k;
            powLenMod[i] = modPow(10, digits, k);
        }

        memo = new int[1 << n][k];
        for (int[] row : memo) {
            java.util.Arrays.fill(row, -1);
        }

        if (!can(0, 0)) {
            return new int[0];
        }

        // order indices by value then original index to ensure lexicographic minimality
        Integer[] orderIdx = new Integer[n];
        for (int i = 0; i < n; i++) orderIdx[i] = i;
        java.util.Arrays.sort(orderIdx, (a, b) -> {
            if (nums[a] != nums[b]) return Integer.compare(nums[a], nums[b]);
            return Integer.compare(a, b);
        });

        int[] result = new int[n];
        int mask = 0;
        int rem = 0;
        for (int pos = 0; pos < n; pos++) {
            boolean found = false;
            for (int idx : orderIdx) {
                if ((mask & (1 << idx)) != 0) continue;
                int newRem = (rem * powLenMod[idx] + modNum[idx]) % k;
                if (can(mask | (1 << idx), newRem)) {
                    result[pos] = nums[idx];
                    mask |= (1 << idx);
                    rem = newRem;
                    found = true;
                    break;
                }
            }
            if (!found) { // should not happen
                return new int[0];
            }
        }
        return result;
    }

    private boolean can(int mask, int rem) {
        if (mask == fullMask) {
            return rem == 0;
        }
        if (memo[mask][rem] != -1) {
            return memo[mask][rem] == 1;
        }
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) continue;
            int newRem = (rem * powLenMod[i] + modNum[i]) % k;
            if (can(mask | (1 << i), newRem)) {
                memo[mask][rem] = 1;
                return true;
            }
        }
        memo[mask][rem] = 0;
        return false;
    }

    private int modPow(int base, int exp, int mod) {
        int result = 1 % mod;
        int b = base % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * b) % mod;
            }
            b = (b * b) % mod;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def concatenatedDivisibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        # precompute digit lengths and 10^len % k
        lens = [len(str(x)) for x in nums]
        pow10_mod = [1] * (max(lens) + 1)
        for l in range(1, len(pow10_mod)):
            pow10_mod[l] = (pow10_mod[l-1] * 10) % k

        full_mask = (1 << n) - 1
        from functools import lru_cache

        @lru_cache(None)
        def dfs(mask, rem):
            if mask == full_mask:
                return rem == 0
            for i in range(n):
                if not (mask >> i) & 1:
                    new_rem = (rem * pow10_mod[lens[i]] + nums[i]) % k
                    if dfs(mask | (1 << i), new_rem):
                        return True
            return False

        if not dfs(0, 0):
            return []

        # indices sorted by value then index for lexicographic order
        sorted_idx = sorted(range(n), key=lambda i: (nums[i], i))

        mask = 0
        rem = 0
        res = []
        while mask != full_mask:
            for i in sorted_idx:
                if not (mask >> i) & 1:
                    new_rem = (rem * pow10_mod[lens[i]] + nums[i]) % k
                    if dfs(mask | (1 << i), new_rem):
                        res.append(nums[i])
                        mask |= (1 << i)
                        rem = new_rem
                        break
        return res
```

## Python3

```python
from typing import List

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        full_mask = (1 << n) - 1

        # precompute length and 10^len % k for each number
        pow10_mod = []
        num_mod = []
        for x in nums:
            l = len(str(x))
            pow10_mod.append(pow(10, l, k))
            num_mod.append(x % k)

        dp = [[False] * k for _ in range(1 << n)]
        dp[0][0] = True

        # forward DP: reachable remainders for each mask
        for mask in range(1 << n):
            for rem in range(k):
                if not dp[mask][rem]:
                    continue
                for i in range(n):
                    if mask >> i & 1:
                        continue
                    new_mask = mask | (1 << i)
                    new_rem = (rem * pow10_mod[i] + num_mod[i]) % k
                    dp[new_mask][new_rem] = True

        if not dp[full_mask][0]:
            return []

        # reverse DP: can we finish from this state to full_mask with remainder 0?
        can = [[False] * k for _ in range(1 << n)]
        can[full_mask][0] = True
        for mask in range(full_mask, -1, -1):
            for rem in range(k):
                if not dp[mask][rem]:
                    continue
                if mask == full_mask and rem == 0:
                    continue
                for i in range(n):
                    if mask >> i & 1:
                        continue
                    new_mask = mask | (1 << i)
                    new_rem = (rem * pow10_mod[i] + num_mod[i]) % k
                    if can[new_mask][new_rem]:
                        can[mask][rem] = True
                        break

        # reconstruct lexicographically smallest permutation
        result = []
        mask = 0
        rem = 0
        while mask != full_mask:
            candidates = [i for i in range(n) if not (mask >> i & 1)]
            candidates.sort(key=lambda idx: (nums[idx], idx))
            for i in candidates:
                new_mask = mask | (1 << i)
                new_rem = (rem * pow10_mod[i] + num_mod[i]) % k
                if can[new_mask][new_rem]:
                    result.append(nums[i])
                    mask, rem = new_mask, new_rem
                    break

        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int digit_len(int x) {
    int len = 0;
    while (x > 0) {
        len++;
        x /= 10;
    }
    return len ? len : 1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* concatenatedDivisibility(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int maxMask = 1 << n;

    static char dp[1 << 13][101];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;

    int len[13];
    int modNum[13];
    for (int i = 0; i < n; ++i) {
        len[i] = digit_len(nums[i]);
        modNum[i] = nums[i] % k;
    }

    int pow10_mod[7];
    pow10_mod[0] = 1 % k;
    for (int l = 1; l <= 6; ++l)
        pow10_mod[l] = (pow10_mod[l - 1] * 10) % k;

    for (int mask = 0; mask < maxMask; ++mask) {
        for (int rem = 0; rem < k; ++rem) {
            if (!dp[mask][rem]) continue;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) continue;
                int newMask = mask | (1 << i);
                int newRem = (rem * pow10_mod[len[i]] + modNum[i]) % k;
                dp[newMask][newRem] = 1;
            }
        }
    }

    int fullMask = maxMask - 1;
    if (!dp[fullMask][0]) {
        *returnSize = 0;
        return NULL;
    }

    int* ans = (int*)malloc(sizeof(int) * n);
    int usedMask = 0;
    int curRem = 0;

    for (int pos = 0; pos < n; ++pos) {
        int bestIdx = -1;
        for (int i = 0; i < n; ++i) {
            if (usedMask & (1 << i)) continue;
            int newRem = (curRem * pow10_mod[len[i]] + modNum[i]) % k;
            int newMask = usedMask | (1 << i);
            if (!dp[newMask][newRem]) continue;
            if (bestIdx == -1 ||
                nums[i] < nums[bestIdx] ||
                (nums[i] == nums[bestIdx] && i < bestIdx)) {
                bestIdx = i;
            }
        }
        ans[pos] = nums[bestIdx];
        usedMask |= (1 << bestIdx);
        curRem = (curRem * pow10_mod[len[bestIdx]] + modNum[bestIdx]) % k;
    }

    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] ConcatenatedDivisibility(int[] nums, int k) {
        int n = nums.Length;
        int fullMask = (1 << n) - 1;

        // precompute lengths and num % k
        int[] len = new int[n];
        int[] modNum = new int[n];
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int l = 0;
            while (x > 0) { l++; x /= 10; }
            if (l == 0) l = 1; // handle zero, though nums are positive per constraints
            len[i] = l;
            maxLen = Math.Max(maxLen, l);
            modNum[i] = nums[i] % k;
        }

        // precompute 10^p % k for p up to maxLen
        int[] pow10mod = new int[maxLen + 1];
        pow10mod[0] = 1 % k;
        for (int i = 1; i <= maxLen; i++) {
            pow10mod[i] = (pow10mod[i - 1] * 10) % k;
        }

        // memoization: -1 unknown, 0 false, 1 true
        int[,] memo = new int[1 << n, k];
        for (int i = 0; i < (1 << n); i++) {
            for (int j = 0; j < k; j++) memo[i, j] = -1;
        }

        bool Can(int mask, int rem) {
            if (mask == fullMask) return rem == 0;
            if (memo[mask, rem] != -1) return memo[mask, rem] == 1;

            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                int newRem = (rem * pow10mod[len[i]] + modNum[i]) % k;
                if (Can(mask | (1 << i), newRem)) {
                    memo[mask, rem] = 1;
                    return true;
                }
            }

            memo[mask, rem] = 0;
            return false;
        }

        if (!Can(0, 0)) return new int[0];

        List<int> answer = new List<int>();
        int curMask = 0, curRem = 0;

        for (int pos = 0; pos < n; pos++) {
            // collect unused indices
            List<int> candidates = new List<int>();
            for (int i = 0; i < n; i++) {
                if ((curMask & (1 << i)) == 0) candidates.Add(i);
            }
            // sort by value then original index to ensure lexicographic minimality
            candidates.Sort((a, b) => {
                int cmp = nums[a].CompareTo(nums[b]);
                return cmp != 0 ? cmp : a.CompareTo(b);
            });

            bool placed = false;
            foreach (int i in candidates) {
                int newRem = (curRem * pow10mod[len[i]] + modNum[i]) % k;
                if (Can(curMask | (1 << i), newRem)) {
                    answer.Add(nums[i]);
                    curMask |= 1 << i;
                    curRem = newRem;
                    placed = true;
                    break;
                }
            }

            if (!placed) return new int[0]; // safety, should not happen
        }

        return answer.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var concatenatedDivisibility = function(nums, k) {
    const n = nums.length;
    const fullMask = (1 << n) - 1;

    // precompute length and value mod k for each number
    const len = new Array(n);
    const modVal = new Array(n);
    let maxLen = 0;
    for (let i = 0; i < n; ++i) {
        const s = String(nums[i]);
        len[i] = s.length;
        if (len[i] > maxLen) maxLen = len[i];
        modVal[i] = nums[i] % k;
    }

    // precompute powers of 10 modulo k
    const pow10 = new Array(maxLen + 1);
    pow10[0] = 1 % k;
    for (let i = 1; i <= maxLen; ++i) {
        pow10[i] = (pow10[i - 1] * 10) % k;
    }

    // forward DP: dp[mask][rem] == true if reachable
    const dp = new Array(1 << n);
    for (let mask = 0; mask <= fullMask; ++mask) {
        dp[mask] = new Uint8Array(k);
    }
    dp[0][0] = 1;

    for (let mask = 0; mask <= fullMask; ++mask) {
        const cur = dp[mask];
        for (let rem = 0; rem < k; ++rem) {
            if (!cur[rem]) continue;
            for (let i = 0; i < n; ++i) {
                if ((mask >> i) & 1) continue;
                const newMask = mask | (1 << i);
                const newRem = (rem * pow10[len[i]] + modVal[i]) % k;
                dp[newMask][newRem] = 1;
            }
        }
    }

    if (!dp[fullMask][0]) return [];

    // memoization for canReachEnd(mask, rem)
    const memoSize = (fullMask + 1) * k;
    const memo = new Int8Array(memoSize);
    memo.fill(-1);

    function can(mask, rem) {
        const idx = mask * k + rem;
        if (memo[idx] !== -1) return memo[idx] === 1;
        if (mask === fullMask) {
            const ok = rem === 0 ? 1 : 0;
            memo[idx] = ok;
            return ok === 1;
        }
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) continue;
            const newMask = mask | (1 << i);
            const newRem = (rem * pow10[len[i]] + modVal[i]) % k;
            if (can(newMask, newRem)) {
                memo[idx] = 1;
                return true;
            }
        }
        memo[idx] = 0;
        return false;
    }

    // reconstruct lexicographically smallest permutation
    let curMask = 0;
    let curRem = 0;
    const result = [];

    while (curMask !== fullMask) {
        const candidates = [];
        for (let i = 0; i < n; ++i) {
            if ((curMask >> i) & 1) continue;
            candidates.push(i);
        }
        candidates.sort((a, b) => {
            if (nums[a] !== nums[b]) return nums[a] - nums[b];
            return a - b;
        });

        for (const i of candidates) {
            const newMask = curMask | (1 << i);
            const newRem = (curRem * pow10[len[i]] + modVal[i]) % k;
            if (can(newMask, newRem)) {
                result.push(nums[i]);
                curMask = newMask;
                curRem = newRem;
                break;
            }
        }
    }

    return result;
};
```

## Typescript

```typescript
function concatenatedDivisibility(nums: number[], k: number): number[] {
    const n = nums.length;
    const fullMask = (1 << n) - 1;

    // digit length of each number
    const len: number[] = new Array(n);
    let maxLen = 0;
    for (let i = 0; i < n; i++) {
        let x = nums[i];
        let cnt = 0;
        while (x > 0) {
            cnt++;
            x = Math.floor(x / 10);
        }
        len[i] = cnt === 0 ? 1 : cnt;
        if (len[i] > maxLen) maxLen = len[i];
    }

    // pow10 modulo k
    const powMod: number[] = new Array(maxLen + 1);
    powMod[0] = 1 % k;
    for (let i = 1; i <= maxLen; i++) {
        powMod[i] = (powMod[i - 1] * 10) % k;
    }

    const mul: number[] = len.map(l => powMod[l]);

    // memo[mask][rem] = -1 unknown, 0 false, 1 true
    const memo: Int8Array[] = Array.from({ length: 1 << n }, () => new Int8Array(k).fill(-1));

    function can(mask: number, rem: number): boolean {
        if (mask === fullMask) return rem === 0;
        const cached = memo[mask][rem];
        if (cached !== -1) return cached === 1;

        for (let i = 0; i < n; i++) {
            if ((mask >> i) & 1) continue;
            const newRem = (rem * mul[i] + nums[i]) % k;
            if (can(mask | (1 << i), newRem)) {
                memo[mask][rem] = 1;
                return true;
            }
        }
        memo[mask][rem] = 0;
        return false;
    }

    if (!can(0, 0)) return [];

    const result: number[] = [];
    let mask = 0;
    let rem = 0;

    for (let pos = 0; pos < n; pos++) {
        const candidates: number[] = [];
        for (let i = 0; i < n; i++) {
            if (((mask >> i) & 1) === 0) candidates.push(i);
        }
        candidates.sort((a, b) => {
            if (nums[a] !== nums[b]) return nums[a] - nums[b];
            return a - b;
        });

        let placed = false;
        for (const i of candidates) {
            const newRem = (rem * mul[i] + nums[i]) % k;
            if (can(mask | (1 << i), newRem)) {
                result.push(nums[i]);
                mask |= 1 << i;
                rem = newRem;
                placed = true;
                break;
            }
        }
        if (!placed) return []; // safety, should not happen
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function concatenatedDivisibility($nums, $k) {
        $n = count($nums);
        // lengths of each number
        $len = [];
        for ($i = 0; $i < $n; $i++) {
            $len[$i] = strlen((string)$nums[$i]);
        }
        $maxLen = max($len);
        // tenPow[l] = (10^l) % k
        $tenPow = array_fill(0, $maxLen + 1, 0);
        $tenPow[0] = 1 % $k;
        for ($l = 1; $l <= $maxLen; $l++) {
            $tenPow[$l] = ($tenPow[$l - 1] * 10) % $k;
        }

        $fullMask = (1 << $n) - 1;
        // memo[mask][rem] = -1 unknown, 0 false, 1 true
        $memo = array_fill(0, 1 << $n, array_fill(0, $k, -1));

        $can = function($mask, $rem) use (&$can, &$memo, $fullMask, $k, $nums, $len, $tenPow) {
            if ($mask === $fullMask) {
                return $rem === 0;
            }
            if ($memo[$mask][$rem] !== -1) {
                return $memo[$mask][$rem] === 1;
            }
            $n = count($nums);
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) === 0) {
                    $newRem = ($rem * $tenPow[$len[$i]] + $nums[$i]) % $k;
                    if ($can($mask | (1 << $i), $newRem)) {
                        $memo[$mask][$rem] = 1;
                        return true;
                    }
                }
            }
            $memo[$mask][$rem] = 0;
            return false;
        };

        // If no valid permutation exists, return empty list
        if (!$can(0, 0)) {
            return [];
        }

        // Greedy reconstruction of lexicographically smallest permutation
        $result = [];
        $mask = 0;
        $rem = 0;
        for ($pos = 0; $pos < $n; $pos++) {
            $candidates = [];
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) === 0) {
                    $candidates[] = $i;
                }
            }
            usort($candidates, function($a, $b) use ($nums) {
                if ($nums[$a] == $nums[$b]) {
                    return $a <=> $b;
                }
                return $nums[$a] <=> $nums[$b];
            });
            foreach ($candidates as $i) {
                $newRem = ($rem * $tenPow[$len[$i]] + $nums[$i]) % $k;
                if ($can($mask | (1 << $i), $newRem)) {
                    $result[] = $nums[$i];
                    $mask |= (1 << $i);
                    $rem = $newRem;
                    break;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func concatenatedDivisibility(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        if n == 0 { return [] }
        var len = [Int](repeating: 0, count: n)
        for i in 0..<n {
            var x = nums[i]
            var cnt = 0
            repeat {
                cnt += 1
                x /= 10
            } while x > 0
            len[i] = cnt
        }
        let maxLen = len.max() ?? 0
        var pow10 = [Int](repeating: 0, count: maxLen + 1)
        pow10[0] = 1 % k
        if maxLen >= 1 {
            for i in 1...maxLen {
                pow10[i] = (pow10[i - 1] * 10) % k
            }
        }
        let fullMask = (1 << n) - 1
        var memo = [Int8](repeating: -1, count: (fullMask + 1) * k)
        func can(_ mask: Int, _ rem: Int) -> Bool {
            if mask == fullMask { return rem == 0 }
            let idx = mask * k + rem
            if memo[idx] != -1 { return memo[idx] == 1 }
            var ok = false
            for i in 0..<n where (mask & (1 << i)) == 0 {
                let newRem = (rem * pow10[len[i]] + nums[i] % k) % k
                if can(mask | (1 << i), newRem) {
                    ok = true
                    break
                }
            }
            memo[idx] = ok ? 1 : 0
            return ok
        }
        if !can(0, 0) { return [] }
        let order = (0..<n).sorted { a, b in
            if nums[a] == nums[b] { return a < b }
            return nums[a] < nums[b]
        }
        var mask = 0
        var rem = 0
        var result = [Int]()
        while mask != fullMask {
            var chosen = -1
            for i in order where (mask & (1 << i)) == 0 {
                let newRem = (rem * pow10[len[i]] + nums[i] % k) % k
                if can(mask | (1 << i), newRem) {
                    chosen = i
                    break
                }
            }
            if chosen == -1 { return [] }
            result.append(nums[chosen])
            mask |= 1 << chosen
            rem = (rem * pow10[len[chosen]] + nums[chosen] % k) % k
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun concatenatedDivisibility(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        val len = IntArray(n)
        var maxLen = 0
        for (i in 0 until n) {
            var x = nums[i]
            var d = 0
            while (x > 0) {
                d++
                x /= 10
            }
            len[i] = d
            if (d > maxLen) maxLen = d
        }

        // pow10Mod[l] = 10^l % k
        val pow10Mod = IntArray(maxLen + 1)
        pow10Mod[0] = 1 % k
        for (i in 1..maxLen) {
            pow10Mod[i] = ((pow10Mod[i - 1].toLong() * 10L) % k).toInt()
        }

        val numMod = IntArray(n) { nums[it] % k }
        val fullMask = (1 shl n) - 1

        // memoization for dfs: can we finish from (mask, rem) to reach remainder 0 with all numbers used?
        val visited = Array(1 shl n) { BooleanArray(k) }
        val memo = Array(1 shl n) { BooleanArray(k) }

        fun dfs(mask: Int, rem: Int): Boolean {
            if (mask == fullMask) return rem == 0
            if (visited[mask][rem]) return memo[mask][rem]
            visited[mask][rem] = true
            for (i in 0 until n) {
                if ((mask and (1 shl i)) == 0) {
                    val newRem = ((rem * pow10Mod[len[i]]) % k + numMod[i]) % k
                    if (dfs(mask or (1 shl i), newRem)) {
                        memo[mask][rem] = true
                        return true
                    }
                }
            }
            memo[mask][rem] = false
            return false
        }

        if (!dfs(0, 0)) return intArrayOf()

        // indices sorted by value then original index for deterministic lexicographic order
        val sortedIdx = (0 until n).sortedWith(compareBy<Int> { nums[it] }.thenBy { it })

        var mask = 0
        var rem = 0
        val result = IntArray(n)
        for (pos in 0 until n) {
            var chosen = -1
            for (i in sortedIdx) {
                if ((mask and (1 shl i)) != 0) continue
                val newRem = ((rem * pow10Mod[len[i]]) % k + numMod[i]) % k
                if (dfs(mask or (1 shl i), newRem)) {
                    chosen = i
                    rem = newRem
                    mask = mask or (1 shl i)
                    result[pos] = nums[i]
                    break
                }
            }
            // chosen must be found because overall solution exists
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> concatenatedDivisibility(List<int> nums, int k) {
    int n = nums.length;
    int fullMask = (1 << n) - 1;

    // Precompute length of each number and its modulo k
    List<int> len = List.filled(n, 0);
    List<int> modNum = List.filled(n, 0);
    List<int> pow10Len = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int x = nums[i];
      int l = 0;
      while (x > 0) {
        l++;
        x ~/= 10;
      }
      len[i] = l;
      modNum[i] = nums[i] % k;

      int p = 1 % k;
      for (int j = 0; j < l; ++j) {
        p = (p * 10) % k;
      }
      pow10Len[i] = p;
    }

    // Precompute product of 10^{len} modulo k for each mask
    List<int> powMask = List.filled(1 << n, 0);
    powMask[0] = 1 % k;
    for (int mask = 1; mask <= fullMask; ++mask) {
      int lsb = mask & -mask;
      int idx = 0;
      while (((lsb >> idx) & 1) == 0) idx++;
      int prev = mask ^ lsb;
      powMask[mask] = (powMask[prev] * pow10Len[idx]) % k;
    }

    // DP: dp[mask][rem] = true if some ordering of mask yields remainder rem
    List<List<bool>> dp = List.generate(1 << n, (_) => List.filled(k, false));
    dp[0][0] = true;

    for (int mask = 0; mask <= fullMask; ++mask) {
      for (int rem = 0; rem < k; ++rem) {
        if (!dp[mask][rem]) continue;
        for (int i = 0; i < n; ++i) {
          if ((mask >> i) & 1 == 1) continue;
          int newMask = mask | (1 << i);
          int newRem = (rem * pow10Len[i] + modNum[i]) % k;
          dp[newMask][newRem] = true;
        }
      }
    }

    if (!dp[fullMask][0]) return [];

    // Reconstruct lexicographically smallest permutation
    List<int> result = [];
    int curRem = 0;
    int remainingMask = fullMask;

    while (remainingMask != 0) {
      // collect candidates and sort by value then index
      List<int> cand = [];
      for (int i = 0; i < n; ++i) {
        if ((remainingMask >> i) & 1 == 1) cand.add(i);
      }
      cand.sort((a, b) {
        int cmp = nums[a].compareTo(nums[b]);
        if (cmp != 0) return cmp;
        return a.compareTo(b);
      });

      bool placed = false;
      for (int i in cand) {
        int newRem = (curRem * pow10Len[i] + modNum[i]) % k;
        int restMask = remainingMask ^ (1 << i);
        int factor = powMask[restMask];
        for (int r = 0; r < k; ++r) {
          if (!dp[restMask][r]) continue;
          if ((newRem * factor + r) % k == 0) {
            result.add(nums[i]);
            curRem = newRem;
            remainingMask = restMask;
            placed = true;
            break;
          }
        }
        if (placed) break;
      }

      if (!placed) return []; // safety, should not happen
    }

    return result;
  }
}
```

## Golang

```go
func concatenatedDivisibility(nums []int, k int) []int {
	n := len(nums)
	if n == 0 {
		return []int{}
	}
	// precompute length and pow10 mod k for each number
	lenArr := make([]int, n)
	powMod := make([]int, n)
	for i, v := range nums {
		l := 0
		x := v
		if x == 0 {
			l = 1
		} else {
			for x > 0 {
				l++
				x /= 10
			}
		}
		lenArr[i] = l
		p := 1 % k
		for j := 0; j < l; j++ {
			p = (p * 10) % k
		}
		powMod[i] = p
	}

	fullMask := 1<<n - 1

	// memo[mask][rem] = -1 unknown, 0 false, 1 true
	memo := make([][]int8, 1<<n)
	for i := 0; i < (1 << n); i++ {
		memo[i] = make([]int8, k)
		for j := 0; j < k; j++ {
			memo[i][j] = -1
		}
	}

	var dfs func(mask int, rem int) bool
	dfs = func(mask int, rem int) bool {
		if mask == fullMask {
			return rem == 0
		}
		if memo[mask][rem] != -1 {
			return memo[mask][rem] == 1
		}
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				newRem := (rem*powMod[i] + nums[i]) % k
				if dfs(mask|1<<i, newRem) {
					memo[mask][rem] = 1
					return true
				}
			}
		}
		memo[mask][rem] = 0
		return false
	}

	if !dfs(0, 0) {
		return []int{}
	}

	result := make([]int, 0, n)
	mask := 0
	rem := 0
	for len(result) < n {
		bestIdx := -1
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				newRem := (rem*powMod[i] + nums[i]) % k
				if dfs(mask|1<<i, newRem) {
					if bestIdx == -1 || nums[i] < nums[bestIdx] || (nums[i] == nums[bestIdx] && i < bestIdx) {
						bestIdx = i
					}
				}
			}
		}
		if bestIdx == -1 { // should not happen
			return []int{}
		}
		result = append(result, nums[bestIdx])
		mask |= 1 << bestIdx
		rem = (rem*powMod[bestIdx] + nums[bestIdx]) % k
	}
	return result
}
```

## Ruby

```ruby
def concatenated_divisibility(nums, k)
  n = nums.length
  return [] if n == 0

  # digit lengths
  lens = nums.map { |x| x.to_s.length }

  max_len = lens.sum
  pow10_exp = Array.new(max_len + 1, 0)
  pow10_exp[0] = 1 % k
  (1..max_len).each { |i| pow10_exp[i] = (pow10_exp[i - 1] * 10) % k }

  ten_pow_mod = lens.map { |l| pow10_exp[l] }

  full_mask = (1 << n) - 1

  # total length for each subset
  total_len = Array.new(1 << n, 0)
  (1..full_mask).each do |mask|
    i = 0
    i += 1 while ((mask >> i) & 1) == 0
    prev = mask ^ (1 << i)
    total_len[mask] = total_len[prev] + lens[i]
  end

  # 10^{total_len} % k for each subset
  pow10_mask = Array.new(1 << n, 0)
  (0..full_mask).each { |mask| pow10_mask[mask] = pow10_exp[total_len[mask]] }

  # dp[mask][rem] = reachable
  dp = Array.new(1 << n) { Array.new(k, false) }
  dp[0][0] = true

  (0..full_mask).each do |mask|
    k.times do |rem|
      next unless dp[mask][rem]
      n.times do |i|
        next if ((mask >> i) & 1) == 1
        new_mask = mask | (1 << i)
        new_rem = (rem * ten_pow_mod[i] + nums[i]) % k
        dp[new_mask][new_rem] = true
      end
    end
  end

  return [] unless dp[full_mask][0]

  # reconstruction for lexicographically smallest permutation
  ans = []
  mask = 0
  cur_rem = 0

  while mask != full_mask
    candidates = (0...n).select { |i| ((mask >> i) & 1) == 0 }
    candidates.sort_by! { |i| [nums[i], i] }

    chosen = nil
    candidates.each do |i|
      new_mask = mask | (1 << i)
      new_rem = (cur_rem * ten_pow_mod[i] + nums[i]) % k
      remaining = full_mask ^ new_mask
      suffix_pow = pow10_mask[remaining]

      feasible = false
      k.times do |r|
        if dp[remaining][r]
          if (new_rem * suffix_pow + r) % k == 0
            feasible = true
            break
          end
        end
      end

      if feasible
        chosen = i
        cur_rem = new_rem
        mask = new_mask
        ans << nums[i]
        break
      end
    end
    # safety check (should never happen)
    break unless chosen
  end

  ans
end
```

## Scala

```scala
import scala.util.control.Breaks.{breakable, break}

object Solution {
  def concatenatedDivisibility(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val totalMask = (1 << n) - 1

    // precompute length of each number and 10^len % k
    val powMod = new Array[Int](n)
    val numMod = new Array[Int](n)
    for (i <- 0 until n) {
      var x = nums(i)
      var len = 0
      while (x > 0) {
        len += 1
        x /= 10
      }
      var p = 1 % k
      var cnt = len
      var base = 10 % k
      while (cnt > 0) {
        if ((cnt & 1) == 1) p = (p * base) % k
        base = (base * base) % k
        cnt >>= 1
      }
      powMod(i) = p
      numMod(i) = nums(i) % k
    }

    // dp[mask][rem] = can achieve final remainder 0 starting from 'rem' with remaining numbers mask
    val dp = Array.ofDim[Boolean](totalMask + 1, k)
    for (r <- 0 until k) dp(0)(r) = r == 0

    for (mask <- 1 to totalMask) {
      var i = 0
      while (i < n) {
        if ((mask & (1 << i)) != 0) {
          val prevMask = mask ^ (1 << i)
          var rem = 0
          while (rem < k) {
            if (!dp(mask)(rem)) {
              val newRem = ((rem * powMod(i)) % k + numMod(i)) % k
              if (dp(prevMask)(newRem)) dp(mask)(rem) = true
            }
            rem += 1
          }
        }
        i += 1
      }
    }

    if (!dp(totalMask)(0)) return Array.emptyIntArray

    val result = scala.collection.mutable.ArrayBuffer[Int]()
    var mask = totalMask
    var rem = 0
    while (mask != 0) {
      // candidates sorted by value to ensure lexicographically smallest permutation
      val candidates = (0 until n).filter(i => (mask & (1 << i)) != 0).sortBy(nums(_))
      breakable {
        for (i <- candidates) {
          val newRem = ((rem * powMod(i)) % k + numMod(i)) % k
          if (dp(mask ^ (1 << i))(newRem)) {
            result += nums(i)
            mask ^= (1 << i)
            rem = newRem
            break
          }
        }
      }
    }

    result.toArray
  }
}
```

## Rust

```rust
use std::vec::Vec;

fn digit_len(mut x: i32) -> usize {
    let mut len = 0;
    while x > 0 {
        len += 1;
        x /= 10;
    }
    if len == 0 { 1 } else { len }
}

fn dfs(
    mask: usize,
    rem: i32,
    nums: &Vec<i32>,
    pow10_mod_len: &Vec<i32>,
    k: i32,
    memo: &mut Vec<Vec<i8>>,
    full_mask: usize,
) -> bool {
    if mask == full_mask {
        return rem % k == 0;
    }
    let r = rem as usize;
    if memo[mask][r] != -1 {
        return memo[mask][r] == 1;
    }
    for i in 0..nums.len() {
        if (mask >> i) & 1 == 0 {
            let new_rem = ((rem * pow10_mod_len[i]) % k + nums[i] % k) % k;
            if dfs(mask | (1 << i), new_rem, nums, pow10_mod_len, k, memo, full_mask) {
                memo[mask][r] = 1;
                return true;
            }
        }
    }
    memo[mask][r] = 0;
    false
}

impl Solution {
    pub fn concatenated_divisibility(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }

        // precompute 10^{len_i} % k for each number
        let mut pow10_mod_len = Vec::with_capacity(n);
        for &num in &nums {
            let len = digit_len(num);
            let mut cur = 1 % k;
            for _ in 0..len {
                cur = (cur * 10) % k;
            }
            pow10_mod_len.push(cur);
        }

        let full_mask = (1usize << n) - 1;
        let mut memo = vec![vec![-1i8; k as usize]; 1usize << n];

        if !dfs(0, 0, &nums, &pow10_mod_len, k, &mut memo, full_mask) {
            return vec![];
        }

        // indices sorted by value then original index for lexicographic order
        let mut idxs: Vec<usize> = (0..n).collect();
        idxs.sort_by_key(|&i| (nums[i], i));

        let mut mask = 0usize;
        let mut rem = 0i32;
        let mut result = Vec::with_capacity(n);

        for _ in 0..n {
            for &i in &idxs {
                if (mask >> i) & 1 == 0 {
                    let new_rem = ((rem * pow10_mod_len[i]) % k + nums[i] % k) % k;
                    if dfs(mask | (1 << i), new_rem, &nums, &pow10_mod_len, k, &mut memo, full_mask) {
                        result.push(nums[i]);
                        mask |= 1 << i;
                        rem = new_rem;
                        break;
                    }
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (concatenated-divisibility nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((n (length nums))
         (full-mask (sub1 (arithmetic-shift 1 n)))
         (numsV (list->vector nums))
         ;; digit count for each number
         (digit-count
          (lambda (x)
            (let loop ((cnt 0) (v x))
              (if (= v 0)
                  (if (= cnt 0) 1 cnt)
                  (loop (+ cnt 1) (quotient v 10))))))
         (lenV (make-vector n))
         (pow10V (make-vector n)))
    ;; pre‑compute lengths and 10^len mod k
    (for ([i (in-range n)])
      (let* ((num (vector-ref numsV i))
             (len (digit-count num))
             (pmod (modulo (expt 10 len) k)))
        (vector-set! lenV i len)
        (vector-set! pow10V i pmod)))
    ;; memo table: -1 = unknown, 0 = false, 1 = true
    (define memo
      (let ((tbl (make-vector (arithmetic-shift 1 n))))
        (for ([m (in-range (arithmetic-shift 1 n))])
          (vector-set! tbl m (make-vector k -1)))
        tbl))
    ;; recursive DP: can we finish from (mask, rem) to fullMask with remainder 0 ?
    (letrec ((possible
              (lambda (mask rem)
                (let* ((row (vector-ref memo mask))
                       (cached (vector-ref row rem)))
                  (if (not (= cached -1))
                      (= cached 1)
                      (begin
                        (define result
                          (if (= mask full-mask)
                              (= rem 0)
                              (let loop ((i 0) (found #f))
                                (cond
                                  [(or found (= i n)) found]
                                  [(zero? (bitwise-and mask (arithmetic-shift 1 i)))
                                   (let* ((newMask (bitwise-ior mask (arithmetic-shift 1 i)))
                                          (newRem (modulo (+ (* rem (vector-ref pow10V i))
                                                            (modulo (vector-ref numsV i) k))
                                                         k)))
                                     (if (possible newMask newRem)
                                         #t
                                         (loop (+ i 1) #f)))]
                                  [else (loop (+ i 1) found)])))))
                        (vector-set! row rem (if result 1 0))
                        result))))))
      ;; if no solution, return empty list
      (if (not (possible 0 0))
          '()
          ;; otherwise reconstruct lexicographically smallest permutation
          (let* ((indices (for/list ([i (in-range n)]) i))
                 (order (sort indices
                              (lambda (a b)
                                (let ((va (vector-ref numsV a))
                                      (vb (vector-ref numsV b)))
                                  (or (< va vb) (and (= va vb) (< a b))))))))
            (let rec ((mask 0) (rem 0) (acc '()))
              (if (= mask full-mask)
                  (reverse acc)
                  (let find-next ((lst order))
                    (cond
                      [(null? lst) (error "unexpected: no valid continuation")]
                      [else
                       (define i (car lst))
                       (if (zero? (bitwise-and mask (arithmetic-shift 1 i)))
                           (let* ((newMask (bitwise-ior mask (arithmetic-shift 1 i)))
                                  (newRem (modulo (+ (* rem (vector-ref pow10V i))
                                                    (modulo (vector-ref numsV i) k))
                                                   k)))
                             (if (possible newMask newRem)
                                 (rec newMask newRem
                                      (cons (vector-ref numsV i) acc))
                                 (find-next (cdr lst))))
                           (find-next (cdr lst)))])))))))))))
```

## Erlang

```erlang
-module(solution).
-export([concatenated_divisibility/2]).

%% Entry function
-spec concatenated_divisibility(Nums :: [integer()], K :: integer()) -> [integer()].
concatenated_divisibility(Nums, K) ->
    N = length(Nums),
    LenList = [digit_len(Ni) || Ni <- Nums],
    MaxLen = lists:max(LenList),
    TenPowMod = precompute_pow10(MaxLen, K),
    FullMask = (1 bsl N) - 1,
    Indexed = [{Num, Idx} || {Num, Idx} <- lists:zip(Nums, lists:seq(0, N-1))],
    Sorted = lists:keysort(1, Indexed),   % sort by value then index
    case possible(0, 0, FullMask, Nums, LenList, TenPowMod, K) of
        true -> build(0, 0, FullMask, Nums, LenList, TenPowMod, K, Sorted);
        false -> []
    end.

%% Digit length helper
-spec digit_len(integer()) -> integer().
digit_len(N) when N < 10 -> 1;
digit_len(N) -> 1 + digit_len(N div 10).

%% Precompute 10^L mod K for L = 0..MaxLen
-spec precompute_pow10(Max :: integer(), K :: integer()) -> map().
precompute_pow10(Max, K) ->
    lists:foldl(fun(L, Acc) ->
                        maps:put(L, powmod(10, L, K), Acc)
                end,
                #{},
                lists:seq(0, Max)).

%% Fast modular exponentiation
-spec powmod(Base :: integer(), Exp :: integer(), Mod :: integer()) -> integer().
powmod(_, 0, _) -> 1;
powmod(B, E, M) when E band 1 =:= 1 ->
    (B * powmod((B * B) rem M, E bsr 1, M)) rem M;
powmod(B, E, M) ->
    powmod((B * B) rem M, E bsr 1, M).

%% DP memoization: can we reach final remainder 0 from state (Mask, Rem)?
-spec possible(Mask :: integer(), Rem :: integer(),
               FullMask :: integer(),
               Nums :: [integer()], LenList :: [integer()],
               TenPowMod :: map(), K :: integer()) -> boolean().
possible(Mask, Rem, FullMask, Nums, LenList, TenPowMod, K) ->
    case Mask == FullMask of
        true -> Rem == 0;
        false ->
            Key = {Mask, Rem},
            case get(Key) of
                undefined ->
                    Res = try_candidates(Mask, Rem, FullMask,
                                         Nums, LenList, TenPowMod, K),
                    put(Key, Res),
                    Res;
                Val -> Val
            end
    end.

%% Try all unused numbers to see if any leads to a solution
-spec try_candidates(Mask :: integer(), Rem :: integer(),
                     FullMask :: integer(),
                     Nums :: [integer()], LenList :: [integer()],
                     TenPowMod :: map(), K :: integer()) -> boolean().
try_candidates(Mask, Rem, FullMask, Nums, LenList, TenPowMod, K) ->
    try_candidates_loop(0, Mask, Rem, FullMask,
                        Nums, LenList, TenPowMod, K).

-spec try_candidates_loop(Index :: integer(), Mask :: integer(),
                          Rem :: integer(), FullMask :: integer(),
                          Nums :: [integer()], LenList :: [integer()],
                          TenPowMod :: map(), K :: integer()) -> boolean().
try_candidates_loop(I, _Mask, _Rem, FullMask, _Nums, _LenList, _TenPowMod, _K)
  when I >= (FullMask + 1) -> false; % all bits checked
try_candidates_loop(I, Mask, Rem, FullMask,
                    Nums, LenList, TenPowMod, K) ->
    Bit = 1 bsl I,
    case (Mask band Bit) of
        0 ->
            NewMask = Mask bor Bit,
            L = lists:nth(I + 1, LenList),
            Pow = maps:get(L, TenPowMod),
            Num = lists:nth(I + 1, Nums),
            NewRem = (Rem * Pow + Num) rem K,
            case possible(NewMask, NewRem, FullMask,
                          Nums, LenList, TenPowMod, K) of
                true -> true;
                false -> try_candidates_loop(I + 1, Mask, Rem,
                                             FullMask, Nums, LenList,
                                             TenPowMod, K)
            end;
        _ ->
            try_candidates_loop(I + 1, Mask, Rem,
                                 FullMask, Nums, LenList,
                                 TenPowMod, K)
    end.

%% Build the lexicographically smallest permutation using the DP table
-spec build(Mask :: integer(), Rem :: integer(),
            FullMask :: integer(),
            Nums :: [integer()], LenList :: [integer()],
            TenPowMod :: map(), K :: integer(),
            Sorted :: [{integer(), integer()}]) -> [integer()].
build(Mask, _Rem, FullMask, _Nums, _LenList, _TenPowMod, _K, _Sorted)
  when Mask == FullMask ->
    [];
build(Mask, Rem, FullMask, Nums, LenList, TenPowMod, K, Sorted) ->
    case pick_candidate(Sorted, Mask, Rem,
                        FullMask, Nums, LenList, TenPowMod, K) of
        {Num, NewMask, NewRem} ->
            [Num | build(NewMask, NewRem, FullMask,
                         Nums, LenList, TenPowMod, K, Sorted)];
        none -> []  % should not happen if a solution exists
    end.

%% Find the smallest unused number that can lead to a solution
-spec pick_candidate(Sorted :: [{integer(), integer()}],
                    Mask :: integer(), Rem :: integer(),
                    FullMask :: integer(),
                    Nums :: [integer()], LenList :: [integer()],
                    TenPowMod :: map(), K :: integer())
    -> {integer(), integer(), integer()} | none.
pick_candidate([], _Mask, _Rem, _FullMask,
               _Nums, _LenList, _TenPowMod, _K) ->
    none;
pick_candidate([{Num, Idx}|Rest], Mask, Rem,
               FullMask, Nums, LenList, TenPowMod, K) ->
    Bit = 1 bsl Idx,
    case (Mask band Bit) of
        0 ->
            L = lists:nth(Idx + 1, LenList),
            Pow = maps:get(L, TenPowMod),
            NewRem = (Rem * Pow + Num) rem K,
            NewMask = Mask bor Bit,
            case possible(NewMask, NewRem, FullMask,
                          Nums, LenList, TenPowMod, K) of
                true -> {Num, NewMask, NewRem};
                false -> pick_candidate(Rest, Mask, Rem,
                                        FullMask, Nums, LenList,
                                        TenPowMod, K)
            end;
        _ ->
            pick_candidate(Rest, Mask, Rem,
                           FullMask, Nums, LenList,
                           TenPowMod, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec concatenated_divisibility(nums :: [integer], k :: integer) :: [integer]
  def concatenated_divisibility(nums, k) do
    import Bitwise

    n = length(nums)

    lens =
      Enum.map(nums, fn x ->
        Integer.to_string(x) |> String.length()
      end)

    ten_pow_mod = Enum.map(lens, &pow10_mod(&1, k))
    nums_mod = Enum.map(nums, &rem(&1, k))

    max_mask = 1 <<< n

    dp_initial = %{{0 => %{0 => []}}}

    dp_final =
      0..(max_mask - 1)
      |> Enum.reduce(dp_initial, fn mask, acc_dp ->
        case Map.get(acc_dp, mask) do
          nil ->
            acc_dp

          rem_map ->
            Enum.reduce(rem_map, acc_dp, fn {rem, seq}, dp2 ->
              0..(n - 1)
              |> Enum.reduce(dp2, fn i, dp3 ->
                bit = 1 <<< i

                if (mask &&& bit) == 0 do
                  new_mask = mask ||| bit

                  new_rem =
                    ((rem * ten_pow_mod[i]) % k + nums_mod[i]) % k

                  new_seq = seq ++ [Enum.at(nums, i)]

                  update_dp(dp3, new_mask, new_rem, new_seq)
                else
                  dp3
                end
              end)
            end)
        end
      end)

    full_mask = max_mask - 1

    case Map.get(dp_final, full_mask) do
      nil -> []
      rem_map -> Map.get(rem_map, 0, [])
    end
  end

  defp pow10_mod(len, k) do
    1..len |> Enum.reduce(1, fn _, acc -> rem(acc * 10, k) end)
  end

  defp update_dp(dp, mask, rem, seq) do
    inner = Map.get(dp, mask, %{})

    case Map.get(inner, rem) do
      nil ->
        Map.put(dp, mask, Map.put(inner, rem, seq))

      existing_seq ->
        if lex_less?(seq, existing_seq) do
          Map.put(dp, mask, Map.put(inner, rem, seq))
        else
          dp
        end
    end
  end

  defp lex_less?(a, b) do
    Enum.reduce_while(Enum.zip(a, b), false, fn {x, y}, _acc ->
      cond do
        x < y -> {:halt, true}
        x > y -> {:halt, false}
        true -> {:cont, false}
      end
    end)
  end
end
```
