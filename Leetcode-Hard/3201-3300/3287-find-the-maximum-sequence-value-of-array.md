# 3287. Find the Maximum Sequence Value of Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxValue(vector<int>& nums, int k) {
        int n = nums.size();
        vector<unordered_set<int>> leftOr(n), rightOr(n);
        
        // forward DP
        vector<unordered_set<int>> dp(k + 1);
        dp[0].insert(0);
        for (int i = 0; i < n; ++i) {
            int limit = min(i + 1, k);
            for (int c = limit; c >= 1; --c) {
                for (int val : dp[c - 1]) {
                    dp[c].insert(val | nums[i]);
                }
            }
            if (i + 1 >= k) leftOr[i] = dp[k];
        }
        
        // backward DP
        vector<unordered_set<int>> dp2(k + 1);
        dp2[0].insert(0);
        for (int i = n - 1; i >= 0; --i) {
            int limit = min(n - i, k);
            for (int c = limit; c >= 1; --c) {
                for (int val : dp2[c - 1]) {
                    dp2[c].insert(val | nums[i]);
                }
            }
            if (n - i >= k) rightOr[i] = dp2[k];
        }
        
        int ans = 0;
        for (int p = 0; p < n - 1; ++p) {
            if (p + 1 < k || n - p - 1 < k) continue;
            const auto& L = leftOr[p];
            const auto& R = rightOr[p + 1];
            if (L.empty() || R.empty()) continue;
            // iterate over smaller set outer
            if (L.size() <= R.size()) {
                for (int a : L) {
                    for (int b : R) {
                        ans = max(ans, a ^ b);
                    }
                }
            } else {
                for (int b : R) {
                    for (int a : L) {
                        ans = max(ans, a ^ b);
                    }
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
    public int maxValue(int[] nums, int k) {
        int n = nums.length;
        @SuppressWarnings("unchecked")
        HashSet<Integer>[] dpLeft = new HashSet[k + 1];
        for (int i = 0; i <= k; i++) dpLeft[i] = new HashSet<>();
        dpLeft[0].add(0);
        List<HashSet<Integer>> leftSets = new ArrayList<>(n);

        for (int idx = 0; idx < n; idx++) {
            int val = nums[idx];
            int maxT = Math.min(idx + 1, k);
            for (int t = maxT; t >= 1; t--) {
                HashSet<Integer> prev = dpLeft[t - 1];
                // snapshot to avoid concurrent modification
                for (int p : new ArrayList<>(prev)) {
                    dpLeft[t].add(p | val);
                }
            }
            leftSets.add(new HashSet<>(dpLeft[k]));
        }

        @SuppressWarnings("unchecked")
        HashSet<Integer>[] dpRight = new HashSet[k + 1];
        for (int i = 0; i <= k; i++) dpRight[i] = new HashSet<>();
        dpRight[0].add(0);
        List<HashSet<Integer>> rightSetsTemp = new ArrayList<>(n);

        for (int idx = n - 1; idx >= 0; idx--) {
            int val = nums[idx];
            int maxT = Math.min(n - idx, k);
            for (int t = maxT; t >= 1; t--) {
                HashSet<Integer> prev = dpRight[t - 1];
                for (int p : new ArrayList<>(prev)) {
                    dpRight[t].add(p | val);
                }
            }
            rightSetsTemp.add(new HashSet<>(dpRight[k])); // suffix starting at idx
        }
        Collections.reverse(rightSetsTemp);
        List<HashSet<Integer>> rightSets = rightSetsTemp;

        int answer = 0;
        for (int split = 0; split < n - 1; split++) {
            HashSet<Integer> left = leftSets.get(split);
            HashSet<Integer> right = rightSets.get(split + 1);
            if (left.isEmpty() || right.isEmpty()) continue;
            for (int a : left) {
                for (int b : right) {
                    int cur = a ^ b;
                    if (cur > answer) answer = cur;
                }
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # left DP: possible OR values for exactly k picks in prefix ending at i
        left_sets = [set() for _ in range(n)]
        dp = [set() for _ in range(k + 1)]
        dp[0].add(0)
        for i, val in enumerate(nums):
            upper = min(k, i + 1)
            for cnt in range(upper, 0, -1):
                new_vals = {prev | val for prev in dp[cnt - 1]}
                if new_vals:
                    dp[cnt] |= new_vals
            left_sets[i] = set(dp[k])   # copy current possibilities

        # right DP: possible OR values for exactly k picks in suffix starting at i
        right_sets = [set() for _ in range(n)]
        dp = [set() for _ in range(k + 1)]
        dp[0].add(0)
        for idx in range(n - 1, -1, -1):
            val = nums[idx]
            upper = min(k, n - idx)
            for cnt in range(upper, 0, -1):
                new_vals = {prev | val for prev in dp[cnt - 1]}
                if new_vals:
                    dp[cnt] |= new_vals
            right_sets[idx] = set(dp[k])

        ans = 0
        # split between i and i+1, left uses prefix [0..i], right uses suffix [i+1..n-1]
        for i in range(n - 1):
            L = left_sets[i]
            R = right_sets[i + 1]
            if not L or not R:
                continue
            # brute-force max xor between two sets (sizes are modest)
            for l in L:
                for r in R:
                    cur = l ^ r
                    if cur > ans:
                        ans = cur
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MAX_BIT = 27  # since nums[i] < 2^27

        # forward DP: L[i] = set of OR values using exactly k elements from nums[0..i]
        L = [set() for _ in range(n)]
        cur = [set() for _ in range(k + 1)]
        cur[0].add(0)
        for i, val in enumerate(nums):
            # update counts descending to avoid reuse within same element
            for cnt in range(min(i + 1, k), 0, -1):
                for prev in cur[cnt - 1]:
                    cur[cnt].add(prev | val)
            L[i] = set(cur[k])  # copy current possibilities

        # backward DP: suffix[i] = set of OR values using exactly k elements from nums[i..n-1]
        suffix = [set() for _ in range(n + 1)]
        cur = [set() for _ in range(k + 1)]
        cur[0].add(0)
        for i in range(n - 1, -1, -1):
            val = nums[i]
            for cnt in range(min(n - i, k), 0, -1):
                for prev in cur[cnt - 1]:
                    cur[cnt].add(prev | val)
            suffix[i] = set(cur[k])

        ans = 0

        # helper to build trie from a set of numbers
        def build_trie(values: set) -> dict:
            root = {}
            for v in values:
                node = root
                for b in range(MAX_BIT - 1, -1, -1):
                    bit = (v >> b) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
            return root

        # helper to query max xor with trie
        def query_trie(root: dict, num: int) -> int:
            node = root
            res = 0
            for b in range(MAX_BIT - 1, -1, -1):
                bit = (num >> b) & 1
                togg = 1 - bit
                if togg in node:
                    res |= (1 << b)
                    node = node[togg]
                else:
                    node = node.get(bit, {})
            return res

        for p in range(n - 1):
            left_set = L[p]
            right_set = suffix[p + 1]
            if not left_set or not right_set:
                continue
            trie = build_trie(right_set)
            for lval in left_set:
                ans = max(ans, query_trie(trie, lval))

        return ans
```

## C

```c
#include <string.h>

int maxValue(int* nums, int numsSize, int k) {
    const int MAXV = 128;                 // numbers are less than 2^7
    static unsigned char dp0[201][MAXV];
    static unsigned char ndp0[201][MAXV];
    static unsigned char dp1[201][MAXV][MAXV];
    static unsigned char ndp1[201][MAXV][MAXV];

    memset(dp0, 0, sizeof(dp0));
    memset(dp1, 0, sizeof(dp1));
    dp0[0][0] = 1;                         // no pairs selected, xor = 0

    for (int idx = 0; idx < numsSize; ++idx) {
        int cur = nums[idx];

        memcpy(ndp0, dp0, sizeof(dp0));   // skip current element
        memcpy(ndp1, dp1, sizeof(dp1));

        /* start a new pending pair with current element */
        for (int p = 0; p <= k; ++p) {
            for (int x = 0; x < MAXV; ++x) {
                if (dp0[p][x]) {
                    ndp1[p][x][cur] = 1;
                }
            }
        }

        /* close a pending pair */
        for (int p = 0; p < k; ++p) {     // we can add at most k pairs
            for (int x = 0; x < MAXV; ++x) {
                for (int v = 0; v < MAXV; ++v) {
                    if (dp1[p][x][v]) {
                        int newxor = x ^ (v | cur);
                        ndp0[p + 1][newxor] = 1;
                    }
                }
            }
        }

        memcpy(dp0, ndp0, sizeof(dp0));
        memcpy(dp1, ndp1, sizeof(dp1));
    }

    for (int ans = MAXV - 1; ans >= 0; --ans) {
        if (dp0[k][ans]) return ans;
    }
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxValue(int[] nums, int k) {
        int n = nums.Length;
        // Prefix DP: pref[i][t] = set of possible OR values using exactly t elements from nums[0..i]
        var pref = new HashSet<int>[n][];
        var dpPref = new List<HashSet<int>>(k + 1);
        for (int i = 0; i <= k; i++) dpPref.Add(new HashSet<int>());
        dpPref[0].Add(0);

        for (int idx = 0; idx < n; idx++) {
            int val = nums[idx];
            int maxTake = Math.Min(idx + 1, k);
            for (int t = maxTake; t >= 1; t--) {
                foreach (int prev in dpPref[t - 1]) {
                    dpPref[t].Add(prev | val);
                }
            }
            var copy = new HashSet<int>[k + 1];
            for (int t = 0; t <= k; t++) copy[t] = new HashSet<int>(dpPref[t]);
            pref[idx] = copy;
        }

        // Suffix DP: suff[i][t] = set of possible OR values using exactly t elements from nums[i..n-1]
        var suff = new HashSet<int>[n][];
        var dpSuf = new List<HashSet<int>>(k + 1);
        for (int i = 0; i <= k; i++) dpSuf.Add(new HashSet<int>());
        dpSuf[0].Add(0);

        for (int idx = n - 1; idx >= 0; idx--) {
            int val = nums[idx];
            int taken = n - idx;
            int maxTake = Math.Min(taken, k);
            for (int t = maxTake; t >= 1; t--) {
                foreach (int prev in dpSuf[t - 1]) {
                    dpSuf[t].Add(prev | val);
                }
            }
            var copy = new HashSet<int>[k + 1];
            for (int t = 0; t <= k; t++) copy[t] = new HashSet<int>(dpSuf[t]);
            suff[idx] = copy;
        }

        int answer = 0;
        // Split between split and split+1
        for (int split = 0; split < n - 1; split++) {
            if (split + 1 < k) continue;               // not enough elements on the left
            if (n - (split + 1) < k) continue;         // not enough elements on the right

            var leftSet = pref[split][k];
            var rightSet = suff[split + 1][k];

            foreach (int a in leftSet) {
                foreach (int b in rightSet) {
                    int val = a ^ b;
                    if (val > answer) answer = val;
                }
            }
        }

        return answer;
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
var maxValue = function(nums, k) {
    const n = nums.length;
    // forward DP: forward[i][c] = Set of possible OR values using c elements from prefix [0..i]
    const forward = Array.from({ length: n }, () => Array(k + 1).fill(null));
    for (let i = 0; i < n; ++i) {
        const prev = i > 0 ? forward[i - 1] : null;
        const maxC = Math.min(i + 1, k);
        for (let c = 0; c <= maxC; ++c) {
            const curSet = new Set();
            if (c === 0) {
                curSet.add(0);
            } else {
                // not take nums[i]
                if (prev && prev[c]) {
                    for (const v of prev[c]) curSet.add(v);
                }
                // take nums[i]
                if (i === 0) {
                    // only possible when c == 1
                    if (c === 1) curSet.add(nums[i]);
                } else {
                    const src = prev[c - 1];
                    if (src) {
                        for (const v of src) curSet.add(v | nums[i]);
                    }
                }
            }
            forward[i][c] = curSet;
        }
    }

    // backward DP: backward[i][c] = Set of possible OR values using c elements from suffix [i..n-1]
    const backward = Array.from({ length: n }, () => Array(k + 1).fill(null));
    for (let i = n - 1; i >= 0; --i) {
        const nxt = i < n - 1 ? backward[i + 1] : null;
        const maxC = Math.min(n - i, k);
        for (let c = 0; c <= maxC; ++c) {
            const curSet = new Set();
            if (c === 0) {
                curSet.add(0);
            } else {
                // not take nums[i]
                if (nxt && nxt[c]) {
                    for (const v of nxt[c]) curSet.add(v);
                }
                // take nums[i]
                if (i === n - 1) {
                    if (c === 1) curSet.add(nums[i]);
                } else {
                    const src = nxt[c - 1];
                    if (src) {
                        for (const v of src) curSet.add(v | nums[i]);
                    }
                }
            }
            backward[i][c] = curSet;
        }
    }

    let answer = 0;
    // split point s: last index of first half, second half starts at s+1
    for (let s = k - 1; s <= n - k - 1; ++s) {
        const leftSet = forward[s][k];
        const rightSet = backward[s + 1][k];
        if (!leftSet || !rightSet) continue;
        for (const a of leftSet) {
            for (const b of rightSet) {
                const val = a ^ b;
                if (val > answer) answer = val;
            }
        }
    }
    return answer;
};
```

## Typescript

```typescript
function maxValue(nums: number[], k: number): number {
    const n = nums.length;
    const MAX_BIT = 26; // since nums[i] < 2^27

    // forward[i]: set of possible OR values using exactly k elements from prefix [0..i]
    const forward: Set<number>[] = new Array(n);
    let dpPrev: Set<number>[] = Array.from({ length: k + 1 }, () => new Set<number>());
    dpPrev[0].add(0);
    for (let i = 0; i < n; ++i) {
        const x = nums[i];
        const dpNew: Set<number>[] = dpPrev.map(s => new Set(s));
        const limit = Math.min(i + 1, k);
        for (let t = limit; t >= 1; --t) {
            for (const val of dpPrev[t - 1]) {
                dpNew[t].add(val | x);
            }
        }
        dpPrev = dpNew;
        forward[i] = new Set(dpPrev[k]); // copy
    }

    // backward[i]: set of possible OR values using exactly k elements from suffix [i..n-1]
    const backward: Set<number>[] = new Array(n);
    dpPrev = Array.from({ length: k + 1 }, () => new Set<number>());
    dpPrev[0].add(0);
    for (let i = n - 1; i >= 0; --i) {
        const x = nums[i];
        const dpNew: Set<number>[] = dpPrev.map(s => new Set(s));
        const limit = Math.min(n - i, k);
        for (let t = limit; t >= 1; --t) {
            for (const val of dpPrev[t - 1]) {
                dpNew[t].add(val | x);
            }
        }
        dpPrev = dpNew;
        backward[i] = new Set(dpPrev[k]); // copy
    }

    let answer = 0;

    // Helper: trie node type
    interface TrieNode {
        child: [TrieNode | null, TrieNode | null];
    }

    for (let split = k - 1; split <= n - k - 1; ++split) {
        const setA = forward[split];
        const setB = backward[split + 1];
        if (!setA || !setB || setA.size === 0 || setB.size === 0) continue;

        // Build trie from setB
        const root: TrieNode = { child: [null, null] };
        for (const b of setB) {
            let node = root;
            for (let bit = MAX_BIT; bit >= 0; --bit) {
                const cur = (b >> bit) & 1;
                if (!node.child[cur]) {
                    node.child[cur] = { child: [null, null] };
                }
                node = node.child[cur] as TrieNode;
            }
        }

        // Query each a to find max xor
        for (const a of setA) {
            let node = root;
            let curXor = 0;
            for (let bit = MAX_BIT; bit >= 0; --bit) {
                const curBit = (a >> bit) & 1;
                const prefer = curBit ^ 1;
                if (node.child[prefer]) {
                    curXor |= (1 << bit);
                    node = node.child[prefer] as TrieNode;
                } else {
                    node = node.child[curBit] as TrieNode;
                }
            }
            if (curXor > answer) answer = curXor;
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
     * @return Integer
     */
    function maxValue($nums, $k) {
        $n = count($nums);
        $maxBit = 26; // numbers < 2^27

        // Prefix DP: possible OR values with exactly k elements up to each index
        $pre = array_fill(0, $n, null);
        $dp = array_fill(0, $k + 1, []);
        $dp[0] = [0 => true];
        for ($i = 0; $i < $n; $i++) {
            $num = $nums[$i];
            $limit = min($i + 1, $k);
            for ($c = $limit; $c >= 1; $c--) {
                foreach ($dp[$c - 1] as $val => $_) {
                    $new = $val | $num;
                    $dp[$c][$new] = true;
                }
            }
            if ($i >= $k - 1) {
                $pre[$i] = array_keys($dp[$k]);
            }
        }

        // Suffix DP: possible OR values with exactly k elements from each index to end
        $suf = array_fill(0, $n, null);
        $dp = array_fill(0, $k + 1, []);
        $dp[0] = [0 => true];
        for ($i = $n - 1; $i >= 0; $i--) {
            $num = $nums[$i];
            $limit = min($n - $i, $k);
            for ($c = $limit; $c >= 1; $c--) {
                foreach ($dp[$c - 1] as $val => $_) {
                    $new = $val | $num;
                    $dp[$c][$new] = true;
                }
            }
            if ($n - $i >= $k) {
                $suf[$i] = array_keys($dp[$k]);
            }
        }

        // Helper functions for trie
        $insertTrie = function (&$trie, $num, $maxBit) {
            $node = 0;
            for ($b = $maxBit; $b >= 0; $b--) {
                $bit = ($num >> $b) & 1;
                if ($trie[$node][$bit] === -1) {
                    $trie[$node][$bit] = count($trie);
                    $trie[] = [-1, -1];
                }
                $node = $trie[$node][$bit];
            }
        };
        $queryTrie = function (&$trie, $num, $maxBit) {
            $node = 0;
            $xor = 0;
            for ($b = $maxBit; $b >= 0; $b--) {
                $bit = ($num >> $b) & 1;
                $desired = 1 - $bit;
                if ($trie[$node][$desired] !== -1) {
                    $xor |= (1 << $b);
                    $node = $trie[$node][$desired];
                } else {
                    $node = $trie[$node][$bit];
                }
            }
            return $xor;
        };

        $ans = 0;
        for ($split = 0; $split < $n - 1; $split++) {
            if ($pre[$split] === null || $suf[$split + 1] === null) continue;

            // Build trie from suffix set
            $trie = [[-1, -1]];
            foreach ($suf[$split + 1] as $val) {
                $insertTrie($trie, $val, $maxBit);
            }

            foreach ($pre[$split] as $a) {
                $cand = $queryTrie($trie, $a, $maxBit);
                if ($cand > $ans) $ans = $cand;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxValue(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        // maximum possible OR value (nums[i] < 2^7)
        let maxOr = 128
        let size = (k + 1) * maxOr
        
        // DP for prefixes
        var leftDP = Array(repeating: Array(repeating: UInt8(0), count: size), count: n)
        leftDP[0][0] = 1   // select 0 elements, OR = 0
        for i in 0..<n {
            if i > 0 { leftDP[i] = leftDP[i - 1] }
            let val = nums[i]
            let maxC = min(i, k - 1)
            if maxC >= 0 {
                for c in stride(from: maxC, through: 0, by: -1) {
                    let baseIdx = c * maxOr
                    let nextIdx = (c + 1) * maxOr
                    var orVal = 0
                    while orVal < maxOr {
                        if leftDP[i][baseIdx + orVal] == 1 {
                            let newOr = orVal | val
                            leftDP[i][nextIdx + newOr] = 1
                        }
                        orVal += 1
                    }
                }
            }
        }
        
        // DP for suffixes
        var rightDP = Array(repeating: Array(repeating: UInt8(0), count: size), count: n)
        rightDP[n - 1][0] = 1
        if n >= 2 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                if i < n - 1 { rightDP[i] = rightDP[i + 1] }
                let val = nums[i]
                let maxC = min(n - 1 - i, k - 1)
                if maxC >= 0 {
                    for c in stride(from: maxC, through: 0, by: -1) {
                        let baseIdx = c * maxOr
                        let nextIdx = (c + 1) * maxOr
                        var orVal = 0
                        while orVal < maxOr {
                            if rightDP[i][baseIdx + orVal] == 1 {
                                let newOr = orVal | val
                                rightDP[i][nextIdx + newOr] = 1
                            }
                            orVal += 1
                        }
                    }
                }
            }
        }
        
        var answer = 0
        if n >= 2 * k {
            for split in 0..<(n - 1) {
                let leftArr = leftDP[split]
                let rightArr = rightDP[split + 1]
                for lOr in 0..<maxOr where leftArr[k * maxOr + lOr] == 1 {
                    for rOr in 0..<maxOr where rightArr[k * maxOr + rOr] == 1 {
                        let val = lOr ^ rOr
                        if val > answer { answer = val }
                    }
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxValue(nums: IntArray, k: Int): Int {
        val n = nums.size
        // Forward DP: possible ORs for exactly k elements in prefix [0..i]
        val forward = Array(n) { mutableSetOf<Int>() }
        var dpPrev = Array(k + 1) { mutableSetOf<Int>() }
        dpPrev[0].add(0)
        for (i in 0 until n) {
            val newDp = Array(k + 1) { mutableSetOf<Int>() }
            for (cnt in 0..k) {
                // not take nums[i]
                newDp[cnt].addAll(dpPrev[cnt])
                if (cnt > 0) {
                    for (v in dpPrev[cnt - 1]) {
                        newDp[cnt].add(v or nums[i])
                    }
                }
            }
            dpPrev = newDp
            forward[i] = HashSet(dpPrev[k])
        }

        // Backward DP: possible ORs for exactly k elements in suffix [i..n-1]
        val back = Array(n) { mutableSetOf<Int>() }
        dpPrev = Array(k + 1) { mutableSetOf<Int>() }
        dpPrev[0].add(0)
        for (i in n - 1 downTo 0) {
            val newDp = Array(k + 1) { mutableSetOf<Int>() }
            for (cnt in 0..k) {
                // not take nums[i]
                newDp[cnt].addAll(dpPrev[cnt])
                if (cnt > 0) {
                    for (v in dpPrev[cnt - 1]) {
                        newDp[cnt].add(v or nums[i])
                    }
                }
            }
            dpPrev = newDp
            back[i] = HashSet(dpPrev[k])
        }

        // Trie node for max xor queries
        class TrieNode {
            var child0: TrieNode? = null
            var child1: TrieNode? = null
        }

        var answer = 0
        for (p in 0 until n - 1) {
            val setA = forward[p]
            val setB = back[p + 1]
            if (setA.isEmpty() || setB.isEmpty()) continue

            // Build trie from setB
            val root = TrieNode()
            for (b in setB) {
                var node = root
                for (bit in 26 downTo 0) {
                    val bBit = (b shr bit) and 1
                    if (bBit == 0) {
                        if (node.child0 == null) node.child0 = TrieNode()
                        node = node.child0!!
                    } else {
                        if (node.child1 == null) node.child1 = TrieNode()
                        node = node.child1!!
                    }
                }
            }

            // Query max xor for each a in setA
            for (a in setA) {
                var node = root
                var curXor = 0
                for (bit in 26 downTo 0) {
                    val aBit = (a shr bit) and 1
                    if (aBit == 0) {
                        if (node.child1 != null) {
                            node = node.child1!!
                            curXor = curXor or (1 shl bit)
                        } else {
                            node = node.child0!!
                        }
                    } else {
                        if (node.child0 != null) {
                            node = node.child0!!
                            curXor = curXor or (1 shl bit)
                        } else {
                            node = node.child1!!
                        }
                    }
                }
                if (curXor > answer) answer = curXor
            }
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  int maxValue(List<int> nums, int k) {
    int n = nums.length;
    // Forward DP: OR values for exactly k elements using prefix up to i
    List<Set<int>> forwardK = List.filled(n, <int>{});
    List<Set<int>> cur = List.generate(k + 1, (_) => <int>{});
    cur[0].add(0);
    for (int i = 0; i < n; ++i) {
      int val = nums[i];
      int maxC = math.min(i + 1, k);
      for (int c = maxC; c >= 1; --c) {
        Set<int> addSet = {};
        for (int prev in cur[c - 1]) {
          addSet.add(prev | val);
        }
        cur[c].addAll(addSet);
      }
      forwardK[i] = Set.from(cur[k]);
    }

    // Backward DP: OR values for exactly k elements using suffix starting at i
    List<Set<int>> backwardK = List.filled(n, <int>{});
    cur = List.generate(k + 1, (_) => <int>{});
    cur[0].add(0);
    for (int i = n - 1; i >= 0; --i) {
      int val = nums[i];
      int maxC = math.min(n - i, k);
      for (int c = maxC; c >= 1; --c) {
        Set<int> addSet = {};
        for (int prev in cur[c - 1]) {
          addSet.add(prev | val);
        }
        cur[c].addAll(addSet);
      }
      backwardK[i] = Set.from(cur[k]);
    }

    int ans = 0;
    // Split point: first half ends at split, second half starts at split+1
    for (int split = 0; split < n - 1; ++split) {
      Set<int> setA = forwardK[split];
      Set<int> setB = backwardK[split + 1];
      if (setA.isEmpty || setB.isEmpty) continue;
      for (int a in setA) {
        for (int b in setB) {
          int val = a ^ b;
          if (val > ans) ans = val;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxValue(nums []int, k int) int {
    n := len(nums)
    // dp[t] maps xor value -> minimal last index used for achieving this xor with t pairs
    dp := make([]map[int]int, k+1)
    for i := 0; i <= k; i++ {
        dp[i] = make(map[int]int)
    }
    dp[0][0] = -1 // no elements used

    for i := 0; i < n; i++ {
        for p := 0; p < i; p++ {
            pairVal := nums[p] | nums[i]
            // iterate t descending to avoid using the same pair multiple times
            for t := k; t >= 1; t-- {
                prevMap := dp[t-1]
                curMap := dp[t]
                for xorPrev, lastIdx := range prevMap {
                    if lastIdx < p { // can form a new pair after previous selections
                        newXor := xorPrev ^ pairVal
                        if existing, ok := curMap[newXor]; !ok || i < existing {
                            curMap[newXor] = i
                        }
                    }
                }
            }
        }
    }

    ans := 0
    for v := range dp[k] {
        if v > ans {
            ans = v
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_value(nums, k)
  n = nums.length
  max_or = (1 << 7) - 1 # since nums[i] < 2^7, maximum OR value is 127

  # Left side DP: possible OR values with exactly k elements up to each index
  left_possible = Array.new(n) { Array.new(max_or + 1, false) }
  dp_left = Array.new(k + 1) { Array.new(max_or + 1, false) }
  dp_left[0][0] = true

  (0...n).each do |i|
    num = nums[i]
    upper_t = [k, i + 1].min
    t = upper_t
    while t >= 1
      prev = dp_left[t - 1]
      cur = dp_left[t]
      v = 0
      while v <= max_or
        if prev[v]
          cur[v | num] = true
        end
        v += 1
      end
      t -= 1
    end
    left_possible[i] = dp_left[k].dup
  end

  # Right side DP: possible OR values with exactly k elements from each index to the end
  right_possible = Array.new(n) { Array.new(max_or + 1, false) }
  dp_right = Array.new(k + 1) { Array.new(max_or + 1, false) }
  dp_right[0][0] = true

  (n - 1).downto(0) do |i|
    num = nums[i]
    upper_t = [k, n - i].min
    t = upper_t
    while t >= 1
      prev = dp_right[t - 1]
      cur = dp_right[t]
      v = 0
      while v <= max_or
        if prev[v]
          cur[v | num] = true
        end
        v += 1
      end
      t -= 1
    end
    right_possible[i] = dp_right[k].dup
  end

  answer = 0
  # split point: last index of the left group is 'split'
  (k - 1...(n - k)).each do |split|
    left_vals = left_possible[split]
    right_vals = right_possible[split + 1]

    lv = 0
    while lv <= max_or
      if left_vals[lv]
        rv = 0
        while rv <= max_or
          if right_vals[rv]
            xor_val = lv ^ rv
            answer = xor_val if xor_val > answer
          end
          rv += 1
        end
      end
      lv += 1
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  class TrieNode {
    val child = new Array[TrieNode](2)
  }

  class Trie {
    private val root = new TrieNode()
    private var hasAny = false
    def insert(num: Int): Unit = {
      var node = root
      for (i <- 26 to 0 by -1) {
        val bit = (num >> i) & 1
        if (node.child(bit) == null) node.child(bit) = new TrieNode()
        node = node.child(bit)
      }
      hasAny = true
    }
    def maxXor(num: Int): Int = {
      var node = root
      var res = 0
      for (i <- 26 to 0 by -1) {
        val bit = (num >> i) & 1
        val want = 1 - bit
        if (node.child(want) != null) {
          res |= (1 << i)
          node = node.child(want)
        } else {
          node = node.child(bit)
        }
      }
      res
    }
    def nonEmpty: Boolean = hasAny
  }

  def maxValue(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    // leftExact(i): possible OR values using exactly k elements from prefix [0..i]
    val leftExact = Array.ofDim[Set[Int]](n)
    val dpLeft = Array.fill(k + 1)(mutable.Set[Int]())
    dpLeft(0).add(0)

    for (i <- 0 until n) {
      val v = nums(i)
      val upper = math.min(k, i + 1)
      for (t <- upper to 1 by -1) {
        for (prev <- dpLeft(t - 1)) {
          dpLeft(t).add(prev | v)
        }
      }
      leftExact(i) = dpLeft(k).toSet
    }

    // rightExact(i): possible OR values using exactly k elements from suffix [i..n-1]
    val rightExact = Array.ofDim[Set[Int]](n)
    val dpRight = Array.fill(k + 1)(mutable.Set[Int]())
    dpRight(0).add(0)

    for (idx <- (n - 1) to 0 by -1) {
      val v = nums(idx)
      val remaining = n - idx
      val upper = math.min(k, remaining)
      for (t <- upper to 1 by -1) {
        for (prev <- dpRight(t - 1)) {
          dpRight(t).add(prev | v)
        }
      }
      rightExact(idx) = dpRight(k).toSet
    }

    val trie = new Trie()
    var answer = 0

    // iterate split point j where right part starts at j (j >= 1)
    for (j <- 1 until n) {
      // add left possibilities ending before j
      for (v <- leftExact(j - 1)) {
        trie.insert(v)
      }
      if (trie.nonEmpty && rightExact(j).nonEmpty) {
        for (r <- rightExact(j)) {
          val cur = trie.maxXor(r)
          if (cur > answer) answer = cur
        }
      }
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_value(nums: Vec<i32>, k: i32) -> i32 {
        // Maximum possible value for nums[i] based on constraints (< 2^7). Use 256 to be safe.
        const MAX_VAL: usize = 256; // values 0..255
        let none = MAX_VAL; // sentinel index for "no pending element"
        let pend_size = MAX_VAL + 1;
        let max_xor = MAX_VAL; // xor results also within 0..255

        let n = nums.len();
        let k_usize = k as usize;

        // dp[t][p][x] == reachable
        let mut dp = vec![vec![vec![false; max_xor]; pend_size]; k_usize + 1];
        dp[0][none][0] = true;

        for &val in nums.iter() {
            let a = val as usize;
            let mut ndp = vec![vec![vec![false; max_xor]; pend_size]; k_usize + 1];

            for t in 0..=k_usize {
                for p in 0..pend_size {
                    // fast skip if no reachable xor values
                    let row = &dp[t][p];
                    for x in 0..max_xor {
                        if !row[x] {
                            continue;
                        }
                        // option: skip current element
                        ndp[t][p][x] = true;

                        if p == none {
                            // start a new pair with this element as the first one
                            ndp[t][a][x] = true;
                        } else {
                            // complete the pending pair
                            if t < k_usize {
                                let new_xor = x ^ (p | a);
                                ndp[t + 1][none][new_xor] = true;
                            }
                        }
                    }
                }
            }

            dp = ndp;
        }

        // Find maximum xor value for exactly k pairs with no pending element
        for x in (0..max_xor).rev() {
            if dp[k_usize][none][x] {
                return x as i32;
            }
        }
        0
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define (max-value nums k)
  (let* ((arr (list->vector nums))
         (n (vector-length arr))
         (dp (make-vector (+ n 1) #f)))
    ;; initialize dp vectors
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ k 1) -1)))
    ;; base case: no elements, zero pairs, value 0
    (vector-set! (vector-ref dp 0) 0 0)
    ;; DP transitions
    (for ([i (in-range n)])
      (let ((dp-i (vector-ref dp i)))
        (for ([t (in-range (+ k 1))])
          (define cur (vector-ref dp-i t))
          (when (>= cur 0)
            ;; skip current element
            (let* ((nextvec (vector-ref dp (+ i 1)))
                   (old (vector-ref nextvec t)))
              (when (> cur old)
                (vector-set! nextvec t cur)))
            ;; start a new pair with current as first element
            (when (< t k)
              (for ([j (in-range (+ i 1) n)])
                (define pairval (bitwise-ior (vector-ref arr i) (vector-ref arr j)))
                (define newxor (bitwise-xor cur pairval))
                (let* ((destvec (vector-ref dp (+ j 1)))
                       (old2 (vector-ref destvec (+ t 1))))
                  (when (> newxor old2)
                    (vector-set! destvec (+ t 1) newxor))))))))))
    ;; answer is max over all positions with exactly k pairs
    (let ((ans -1))
      (for ([i (in-range (+ n 1))])
        (define val (vector-ref (vector-ref dp i) k))
        (when (> val ans)
          (set! ans val)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([max_value/2]).

-spec max_value(Nums :: [integer()], K :: integer()) -> integer().
max_value(Nums, K) ->
    Pref = build_prefix_sets(Nums, K),
    Suff = build_suffix_sets(Nums, K),
    compute_max(Pref, Suff, K).

%% Build prefix reachable OR sets for exactly K elements after each position
build_prefix_sets(Nums, K) ->
    DP0 = #{0 => #{0 => true}},
    build_prefix_sets(lists:seq(1, length(Nums)), Nums, K, DP0, []).

build_prefix_sets([], _Nums, _K, _DP, Acc) ->
    lists:reverse(Acc);
build_prefix_sets([Idx | Rest], Nums, K, DP, Acc) ->
    Num = lists:nth(Idx, Nums),
    MaxT = erlang:min(K, Idx),
    NewDP = update_dp_down(Num, MaxT, DP),
    PrefSet = maps:get(K, NewDP, #{}),
    build_prefix_sets(Rest, Nums, K, NewDP, [PrefSet | Acc]).

%% Build suffix reachable OR sets for exactly K elements starting at each position
build_suffix_sets(Nums, K) ->
    Rev = lists:reverse(Nums),
    DP0 = #{0 => #{0 => true}},
    build_suffix_rev(Rev, K, DP0, [], 0).

build_suffix_rev([], _K, _DP, Acc, _Cnt) ->
    lists:reverse(Acc);
build_suffix_rev([Num | Rest], K, DP, Acc, Cnt) ->
    NewCnt = Cnt + 1,
    MaxT = erlang:min(K, NewCnt),
    NewDP = update_dp_down(Num, MaxT, DP),
    SuffSet = maps:get(K, NewDP, #{}),
    build_suffix_rev(Rest, K, NewDP, [SuffSet | Acc], NewCnt).

%% Update DP for a new number, processing t from MaxT down to 1
update_dp_down(_Num, 0, DP) ->
    DP;
update_dp_down(Num, T, DP) ->
    Prev = maps:get(T - 1, DP, #{}),
    NewVals = [Val bor Num || Val <- maps:keys(Prev)],
    Existing = maps:get(T, DP, #{}),
    Updated = lists:foldl(fun(V, Acc) -> maps:put(V, true, Acc) end,
                          Existing, NewVals),
    DP1 = maps:put(T, Updated, DP),
    update_dp_down(Num, T - 1, DP1).

%% Compute the maximum XOR between any prefix set and suffix set across valid splits
compute_max(Pref, Suff, K) ->
    N = length(Pref),
    compute_max_loop(0, N, Pref, Suff, K, 0).

compute_max_loop(I, N, _Pref, _Suff, _K, Max) when I >= N ->
    Max;
compute_max_loop(I, N, Pref, Suff, K, Max) ->
    Valid = (I >= K - 1) andalso ((N - I - 1) >= K),
    NewMax =
        if
            Valid ->
                PSet = lists:nth(I + 1, Pref),
                SSet = lists:nth(I + 2, Suff), % suffix starts at position I+1
                max_xor_sets(PSet, SSet, Max);
            true -> Max
        end,
    compute_max_loop(I + 1, N, Pref, Suff, K, NewMax).

%% Compute maximum XOR between two sets represented as maps (keys are values)
max_xor_sets(PSet, SSet, Cur) ->
    case {maps:size(PSet), maps:size(SSet)} of
        {0, _} -> Cur;
        {_, 0} -> Cur;
        _ ->
            PKeys = maps:keys(PSet),
            SKeys = maps:keys(SSet),
            lists:foldl(
              fun(A, AccA) ->
                  lists:foldl(
                    fun(B, AccB) ->
                        X = A bxor B,
                        if X > AccB -> X; true -> AccB end
                    end, AccA, SKeys)
              end, Cur, PKeys)
    end.
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec max_value(nums :: [integer], k :: integer) :: integer
  def max_value(nums, k) do
    n = length(nums)

    # Prefix DP: subsequences ending at each position
    {_, pref_rev} =
      Enum.reduce(nums, {init_dp(k), []}, fn val, {dp, pref_acc} ->
        new_end =
          Enum.map(0..k, fn t ->
            cond do
              t == 0 ->
                MapSet.new()

              t == 1 ->
                MapSet.put(MapSet.new(), val)

              true ->
                prev = Enum.at(dp, t - 1)

                if MapSet.size(prev) == 0 do
                  MapSet.new()
                else
                  Enum.reduce(prev, MapSet.new(), fn v, acc ->
                    MapSet.put(acc, Bitwise.bor(v, val))
                  end)
                end
            end
          end)

        new_dp =
          Enum.map(0..k, fn t ->
            if t == 0 do
              MapSet.new()
            else
              MapSet.union(Enum.at(dp, t), Enum.at(new_end, t))
            end
          end)

        {new_dp, [new_end | pref_acc]}
      end)

    prefix = Enum.reverse(pref_rev)

    # Suffix DP: subsequences starting at each position
    rev_nums = Enum.reverse(nums)

    {_, suff_rev} =
      Enum.reduce(rev_nums, {init_dp(k), []}, fn val, {dp, suff_acc} ->
        new_start =
          Enum.map(0..k, fn t ->
            cond do
              t == 0 ->
                MapSet.new()

              t == 1 ->
                MapSet.put(MapSet.new(), val)

              true ->
                prev = Enum.at(dp, t - 1)

                if MapSet.size(prev) == 0 do
                  MapSet.new()
                else
                  Enum.reduce(prev, MapSet.new(), fn v, acc ->
                    MapSet.put(acc, Bitwise.bor(v, val))
                  end)
                end
            end
          end)

        new_dp =
          Enum.map(0..k, fn t ->
            if t == 0 do
              MapSet.new()
            else
              MapSet.union(Enum.at(dp, t), Enum.at(new_start, t))
            end
          end)

        {new_dp, [new_start | suff_acc]}
      end)

    suffix = Enum.reverse(suff_rev)

    # Compute maximum XOR between prefix and suffix groups of size k
    Enum.reduce(0..(n - 2), 0, fn i, cur_max ->
      set_a = Enum.at(prefix[i], k)
      set_b = Enum.at(suffix[i + 1], k)

      if MapSet.size(set_a) == 0 or MapSet.size(set_b) == 0 do
        cur_max
      else
        for a <- set_a, b <- set_b, reduce: cur_max do
          acc ->
            xor = Bitwise.bxor(a, b)
            if xor > acc, do: xor, else: acc
        end
      end
    end)
  end

  defp init_dp(k), do: List.duplicate(MapSet.new(), k + 1)
end
```
