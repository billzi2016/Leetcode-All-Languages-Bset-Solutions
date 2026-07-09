# 1815. Maximum Number of Groups Getting Fresh Donuts

## Cpp

```cpp
class Solution {
public:
    int batch;
    unordered_map<unsigned long long,int> memo;
    
    unsigned long long encode(const vector<int>& cnt, int cur) {
        unsigned long long key = cur; // fits in few bits
        for (int i = 1; i < batch; ++i) {
            key = (key << 5) | static_cast<unsigned long long>(cnt[i]); // each count <=30 fits in 5 bits
        }
        return key;
    }
    
    int dfs(vector<int>& cnt, int cur) {
        bool empty = true;
        for (int i = 1; i < batch; ++i) if (cnt[i]) { empty = false; break; }
        if (empty) return 0;
        
        unsigned long long key = encode(cnt, cur);
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;
        
        int best = 0;
        for (int i = 1; i < batch; ++i) {
            if (!cnt[i]) continue;
            cnt[i]--;
            int add = dfs(cnt, (cur + i) % batch);
            if (cur == 0) ++add; // this group gets fresh donuts
            best = max(best, add);
            cnt[i]++;
        }
        memo[key] = best;
        return best;
    }
    
    int maxHappyGroups(int batchSize, vector<int>& groups) {
        batch = batchSize;
        vector<int> cnt(batch, 0);
        for (int g : groups) ++cnt[g % batch];
        
        int ans = cnt[0]; // groups already divisible by batchSize are always happy
        memo.clear();
        ans += dfs(cnt, 0);
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int batchSize;
    private java.util.Map<Long, Integer> memo;

    public int maxHappyGroups(int batchSize, int[] groups) {
        this.batchSize = batchSize;
        int[] cnt = new int[batchSize];
        for (int g : groups) {
            cnt[g % batchSize]++;
        }
        int result = cnt[0]; // groups perfectly divisible are always happy
        memo = new java.util.HashMap<>();
        result += dfs(cnt, 0);
        return result;
    }

    private long encode(int[] cnt) {
        long key = 0L;
        for (int i = 1; i < batchSize; i++) {
            key |= ((long) cnt[i]) << (5 * (i - 1));
        }
        return key;
    }

    private int dfs(int[] cnt, int rem) {
        boolean empty = true;
        for (int i = 1; i < batchSize; i++) {
            if (cnt[i] != 0) {
                empty = false;
                break;
            }
        }
        if (empty) return 0;

        long key = encode(cnt);
        key = (key << 4) | rem; // enough bits for remainder (batchSize <= 9)
        Integer cached = memo.get(key);
        if (cached != null) return cached;

        int best = 0;
        for (int i = 1; i < batchSize; i++) {
            if (cnt[i] == 0) continue;
            cnt[i]--;
            int newRem = (rem + i) % batchSize;
            int add = dfs(cnt, newRem) + (rem == 0 ? 1 : 0);
            if (add > best) best = add;
            cnt[i]++;
        }
        memo.put(key, best);
        return best;
    }
}
```

## Python

```python
import functools

class Solution(object):
    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        # Groups whose size is divisible by batchSize are always happy
        base_happy = sum(1 for g in groups if g % batchSize == 0)

        # Count remainders for the rest
        freq = [0] * batchSize
        for g in groups:
            r = g % batchSize
            freq[r] += 1
        freq[0] = 0  # already accounted

        @functools.lru_cache(None)
        def dfs(state, cur_mod):
            if sum(state) == 0:
                return 0
            best = 0
            for r in range(1, batchSize):
                if state[r]:
                    lst = list(state)
                    lst[r] -= 1
                    new_state = tuple(lst)
                    add = 1 if cur_mod == 0 else 0
                    cand = add + dfs(new_state, (cur_mod + r) % batchSize)
                    if cand > best:
                        best = cand
            return best

        return base_happy + dfs(tuple(freq), 0)
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)
        
        cnt = [0] * batchSize
        for g in groups:
            cnt[g % batchSize] += 1
        
        # Groups with remainder 0 are always happy
        ans = cnt[0]
        init_state = tuple(cnt[1:])  # remainders 1..batchSize-1

        @lru_cache(None)
        def dp(state: tuple, cur: int) -> int:
            if not any(state):
                return 0
            best = 0
            for i, c in enumerate(state, start=1):
                if c == 0:
                    continue
                lst = list(state)
                lst[i - 1] -= 1
                new_state = tuple(lst)
                new_cur = (cur + i) % batchSize
                val = dp(new_state, new_cur)
                if cur == 0:   # the group we take now gets fresh donuts
                    val += 1
                if val > best:
                    best = val
            return best

        ans += dp(init_state, 0)
        return ans
```

## C

```c
#include <stdint.h>
#include <string.h>

#define MAX_BATCH 9
#define BITS_PER_CNT 5               // enough for counts up to 31 (>30)
#define HASH_BITS 20                 // size = 2^20 ~ 1,048,576
#define HASH_SIZE (1U << HASH_BITS)

static int g_batchSize;
static int g_totalMod;

/* hash map for memoization: key -> mask, value -> best answer */
static uint64_t dp_key[HASH_SIZE];
static int      dp_val[HASH_SIZE];
static char     dp_used[HASH_SIZE];

/* compute current remainder (leftover donuts) from remaining mask */
static int cur_remainder(uint64_t mask) {
    int rem = 0;
    for (int i = 1; i < g_batchSize; ++i) {
        uint64_t cnt = (mask >> (BITS_PER_CNT * (i - 1))) & 31ULL;
        if (cnt)
            rem = (rem + (int)(cnt * i)) % g_batchSize;
    }
    int cur = g_totalMod - rem;
    if (cur < 0) cur += g_batchSize;
    else if (cur >= g_batchSize) cur %= g_batchSize;
    return cur;
}

/* recursive DP */
static int dfs(uint64_t mask) {
    /* hash lookup */
    uint64_t h = mask * 11400714819323198485ULL;
    unsigned idx = (unsigned)(h >> (64 - HASH_BITS)) & (HASH_SIZE - 1);
    while (dp_used[idx]) {
        if (dp_key[idx] == mask) return dp_val[idx];
        idx = (idx + 1) & (HASH_SIZE - 1);
    }

    if (mask == 0) {               // no groups left
        dp_used[idx] = 1;
        dp_key[idx] = mask;
        dp_val[idx] = 0;
        return 0;
    }

    int curR = cur_remainder(mask);
    int best = 0;

    for (int i = 1; i < g_batchSize; ++i) {
        uint64_t cnt = (mask >> (BITS_PER_CNT * (i - 1))) & 31ULL;
        if (cnt == 0) continue;
        uint64_t newMask = mask - (1ULL << (BITS_PER_CNT * (i - 1)));
        int tmp = dfs(newMask);
        if (curR == 0) ++tmp;      // this group becomes happy
        if (tmp > best) best = tmp;
    }

    dp_used[idx] = 1;
    dp_key[idx] = mask;
    dp_val[idx] = best;
    return best;
}

int maxHappyGroups(int batchSize, int* groups, int groupsSize) {
    g_batchSize = batchSize;

    int cnt[MAX_BATCH] = {0};
    int baseAns = 0;
    for (int i = 0; i < groupsSize; ++i) {
        int r = groups[i] % batchSize;
        if (r == 0) ++baseAns;
        else ++cnt[r];
    }

    uint64_t mask = 0;
    g_totalMod = 0;
    for (int i = 1; i < batchSize; ++i) {
        if (cnt[i]) {
            mask |= ((uint64_t)cnt[i]) << (BITS_PER_CNT * (i - 1));
            g_totalMod = (g_totalMod + cnt[i] * i) % batchSize;
        }
    }

    memset(dp_used, 0, sizeof(dp_used));
    int extra = dfs(mask);
    return baseAns + extra;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxHappyGroups(int batchSize, int[] groups) {
        if (batchSize == 1) return groups.Length;

        long[] freq = new long[batchSize];
        foreach (int g in groups) {
            int r = g % batchSize;
            freq[r]++;
        }

        int result = (int)freq[0];

        int[] cnt = new int[batchSize];
        for (int i = 1; i < batchSize; i++) cnt[i] = (int)freq[i];

        var memo = new Dictionary<string, int>();

        int Dfs(int[] c, int rem) {
            bool empty = true;
            for (int i = 1; i < batchSize; i++) {
                if (c[i] > 0) { empty = false; break; }
            }
            if (empty) return 0;

            long code = 0;
            for (int i = 1; i < batchSize; i++) {
                code = code * 31 + c[i];
            }
            string key = code + "_" + rem;
            if (memo.TryGetValue(key, out int cached)) return cached;

            int best = 0;
            for (int i = 1; i < batchSize; i++) {
                if (c[i] == 0) continue;
                c[i]--;
                int nxt = (rem + i) % batchSize;
                int add = Dfs(c, nxt);
                if (nxt == 0) add++;
                best = Math.Max(best, add);
                c[i]++;
            }

            memo[key] = best;
            return best;
        }

        result += Dfs(cnt, 0);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} batchSize
 * @param {number[]} groups
 * @return {number}
 */
var maxHappyGroups = function(batchSize, groups) {
    const cnt = new Array(batchSize).fill(0);
    for (const g of groups) {
        cnt[g % batchSize]++;
    }
    // Groups with remainder 0 are always happy
    let result = cnt[0];
    cnt[0] = 0;

    const memo = new Map();

    function dfs(curRemainder) {
        // check if all counts are zero
        let empty = true;
        for (let i = 1; i < batchSize; i++) {
            if (cnt[i] > 0) { empty = false; break; }
        }
        if (empty) return 0;

        const key = cnt.slice(1).join('#') + '|' + curRemainder;
        if (memo.has(key)) return memo.get(key);

        let best = 0;
        for (let i = 1; i < batchSize; i++) {
            if (cnt[i] === 0) continue;
            cnt[i]--;
            const nextRem = (curRemainder + i) % batchSize;
            const add = curRemainder === 0 ? 1 : 0;
            const val = add + dfs(nextRem);
            if (val > best) best = val;
            cnt[i]++;
        }
        memo.set(key, best);
        return best;
    }

    result += dfs(0);
    return result;
};
```

## Typescript

```typescript
function maxHappyGroups(batchSize: number, groups: number[]): number {
    const mod = batchSize;
    let baseHappy = 0;
    const freq = new Array(mod).fill(0);
    for (const g of groups) {
        const r = g % mod;
        if (r === 0) {
            baseHappy++;
        } else {
            freq[r]++;
        }
    }

    // If no remainder groups, all are happy.
    if (freq.every(v => v === 0)) return baseHappy;

    const memo = new Map<string, number>();

    function encode(arr: number[]): number {
        let key = 0;
        for (let i = 1; i < mod; i++) {
            key = key * 31 + arr[i];
        }
        return key;
    }

    function dfs(rem: number): number {
        const enc = encode(freq);
        const memoKey = enc + '|' + rem;
        if (memo.has(memoKey)) return memo.get(memoKey)!;

        let best = 0;
        for (let i = 1; i < mod; i++) {
            if (freq[i] === 0) continue;
            freq[i]--;
            const newRem = (rem + i) % mod;
            const add = newRem === 0 ? 1 : 0;
            const cand = dfs(newRem) + add;
            if (cand > best) best = cand;
            freq[i]++;
        }

        memo.set(memoKey, best);
        return best;
    }

    return baseHappy + dfs(0);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $batchSize
     * @param Integer[] $groups
     * @return Integer
     */
    function maxHappyGroups($batchSize, $groups) {
        $cnt = array_fill(0, $batchSize, 0);
        foreach ($groups as $g) {
            $r = $g % $batchSize;
            $cnt[$r]++;
        }

        // Groups that already have remainder 0 are always happy
        $ans = $cnt[0];

        // Pair complementary remainders
        for ($i = 1; $i * 2 < $batchSize; $i++) {
            $j = $batchSize - $i;
            $pair = min($cnt[$i], $cnt[$j]);
            $ans += $pair;
            $cnt[$i] -= $pair;
            $cnt[$j] -= $pair;
        }

        // If batchSize is even, handle the middle remainder
        if ($batchSize % 2 == 0) {
            $mid = intdiv($batchSize, 2);
            $pairsMid = intdiv($cnt[$mid], 2);
            $ans += $pairsMid;
            $cnt[$mid] -= $pairsMid * 2;
        }

        // DP with memoization over the remaining counts and current remainder
        $memo = [];

        $dfs = function ($cnt, $rem) use (&$dfs, &$batchSize, &$memo) {
            // Check if all counts are zero
            $allZero = true;
            foreach ($cnt as $c) {
                if ($c > 0) {
                    $allZero = false;
                    break;
                }
            }
            if ($allZero) {
                return 0;
            }

            $key = implode(',', $cnt) . '|' . $rem;
            if (isset($memo[$key])) {
                return $memo[$key];
            }

            $best = 0;
            for ($i = 1; $i < $batchSize; $i++) {
                if ($cnt[$i] > 0) {
                    $nextCnt = $cnt;
                    $nextCnt[$i]--;
                    $nextRem = ($rem + $i) % $batchSize;
                    $gain = ($rem == 0) ? 1 : 0; // current group is happy if we start fresh
                    $candidate = $gain + $dfs($nextCnt, $nextRem);
                    if ($candidate > $best) {
                        $best = $candidate;
                    }
                }
            }

            $memo[$key] = $best;
            return $best;
        };

        $ans += $dfs($cnt, 0);
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxHappyGroups(_ batchSize: Int, _ groups: [Int]) -> Int {
        let n = batchSize
        var cnt = Array(repeating: 0, count: n)
        for g in groups {
            cnt[g % n] += 1
        }
        var result = cnt[0]
        cnt[0] = 0
        
        var memo = [UInt64:Int]()
        let base: UInt64 = 31   // since each count <= 30
        
        func dfs(_ curRem: Int, _ counts: inout [Int]) -> Int {
            var key: UInt64 = UInt64(curRem)
            for i in 1..<n {
                key = key * base + UInt64(counts[i])
            }
            if let cached = memo[key] {
                return cached
            }
            var best = 0
            for i in 1..<n where counts[i] > 0 {
                counts[i] -= 1
                let nextRem = (curRem + i) % n
                let add = curRem == 0 ? 1 : 0
                let candidate = add + dfs(nextRem, &counts)
                if candidate > best { best = candidate }
                counts[i] += 1
            }
            memo[key] = best
            return best
        }
        
        var mutableCnt = cnt
        result += dfs(0, &mutableCnt)
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap

class Solution {
    private var batchSize = 0
    private val memo = HashMap<Long, Int>()

    fun maxHappyGroups(batchSize: Int, groups: IntArray): Int {
        this.batchSize = batchSize
        val cnt = IntArray(batchSize)
        for (g in groups) {
            cnt[g % batchSize]++
        }
        var result = cnt[0] // groups already divisible by batchSize are always happy

        // encode counts of remainders 1..batchSize-1 into a single int state
        var state = 0
        var shift = 0
        for (i in 1 until batchSize) {
            state = state or (cnt[i] shl (shift * 5))
            shift++
        }

        result += dfs(state, 0)
        return result
    }

    private fun dfs(state: Int, rem: Int): Int {
        if (state == 0) return 0
        val key = (state.toLong() shl 4) or rem.toLong()
        memo[key]?.let { return it }

        var best = 0
        for (i in 1 until batchSize) {
            val pos = i - 1
            val cnt = (state shr (pos * 5)) and 31
            if (cnt > 0) {
                val newState = state - (1 shl (pos * 5))
                val newRem = (rem + i) % batchSize
                var add = dfs(newState, newRem)
                if (newRem == 0) add += 1
                if (add > best) best = add
            }
        }

        memo[key] = best
        return best
    }
}
```

## Dart

```dart
class Solution {
  late int _batchSize;
  final Map<int, int> _memo = {};

  int maxHappyGroups(int batchSize, List<int> groups) {
    if (batchSize == 1) return groups.length;
    _batchSize = batchSize;
    List<int> cnt = List.filled(batchSize, 0);
    for (int g in groups) {
      cnt[g % batchSize]++;
    }
    int base = cnt[0];
    cnt[0] = 0; // not needed further
    int extra = _dfs(cnt, 0);
    return base + extra;
  }

  int _encode(List<int> cnt) {
    int key = 0;
    for (int i = 1; i < _batchSize; i++) {
      key = (key << 5) | cnt[i];
    }
    return key;
  }

  int _dfs(List<int> cnt, int rem) {
    bool empty = true;
    for (int i = 1; i < _batchSize; i++) {
      if (cnt[i] != 0) {
        empty = false;
        break;
      }
    }
    if (empty) return 0;

    int key = (_encode(cnt) << 4) | rem;
    var cached = _memo[key];
    if (cached != null) return cached;

    int best = 0;
    for (int i = 1; i < _batchSize; i++) {
      if (cnt[i] == 0) continue;
      cnt[i]--;
      int newRem = (rem + i) % _batchSize;
      int add = _dfs(cnt, newRem);
      if (rem == 0) add += 1;
      if (add > best) best = add;
      cnt[i]++;
    }
    _memo[key] = best;
    return best;
  }
}
```

## Golang

```go
func maxHappyGroups(batchSize int, groups []int) int {
    freq := make([]int, batchSize)
    for _, g := range groups {
        r := g % batchSize
        freq[r]++
    }
    // Groups with remainder 0 are always happy.
    result := freq[0]

    const bitsPer = 6 // enough to store counts up to 30
    var initKey uint64
    for i := 1; i < batchSize; i++ {
        if cnt := freq[i]; cnt > 0 {
            shift := uint((i - 1) * bitsPer)
            initKey |= uint64(cnt) << shift
        }
    }

    memo := make(map[uint64]int)

    var dfs func(key uint64, cur int) int
    dfs = func(key uint64, cur int) int {
        if key == 0 {
            return 0
        }
        fullKey := (key << 4) | uint64(cur)
        if v, ok := memo[fullKey]; ok {
            return v
        }
        best := 0
        for i := 1; i < batchSize; i++ {
            shift := uint((i - 1) * bitsPer)
            cnt := int((key >> shift) & 0x3F)
            if cnt == 0 {
                continue
            }
            newKey := key - (1 << shift) // decrement count of remainder i
            nextR := (cur + i) % batchSize
            add := 0
            if cur == 0 {
                add = 1
            }
            cand := add + dfs(newKey, nextR)
            if cand > best {
                best = cand
            }
        }
        memo[fullKey] = best
        return best
    }

    result += dfs(initKey, 0)
    return result
}
```

## Ruby

```ruby
def max_happy_groups(batch_size, groups)
  # Count remainders
  cnt = Array.new(batch_size, 0)
  groups.each do |g|
    r = g % batch_size
    cnt[r] += 1
  end

  # Groups perfectly divisible are always happy
  base_ans = cnt[0]
  cnt[0] = 0

  memo = {}

  dfs = lambda do |state, cur_mod|
    key = state.join(',') + '|' + cur_mod.to_s
    return memo[key] if memo.key?(key)

    # If no groups left
    if state.all? { |c| c.zero? }
      memo[key] = 0
      return 0
    end

    best = 0
    (1...batch_size).each do |i|
      next if state[i].zero?
      state[i] -= 1
      new_mod = (cur_mod + i) % batch_size
      add = dfs.call(state, new_mod)
      add += 1 if cur_mod.zero?   # this group gets fresh donuts
      best = add if add > best
      state[i] += 1
    end

    memo[key] = best
    best
  end

  base_ans + dfs.call(cnt, 0)
end
```

## Scala

```scala
object Solution {
    def maxHappyGroups(batchSize: Int, groups: Array[Int]): Int = {
        val freq = new Array[Int](batchSize)
        for (g <- groups) {
            freq(g % batchSize) += 1
        }
        var result = freq(0)

        def encode(arr: Array[Int]): Long = {
            var code = 0L
            for (i <- 1 until batchSize) {
                code = (code << 5) | arr(i).toLong
            }
            code
        }

        val memo = scala.collection.mutable.Map[(Long, Int), Int]()

        def dfs(code: Long, rem: Int): Int = {
            if (code == 0L) return 0
            val key = (code, rem)
            memo.getOrElseUpdate(key, {
                var tmp = code
                val cnt = new Array[Int](batchSize)
                for (i <- batchSize - 1 until 1 by -1) {
                    cnt(i) = (tmp & 31L).toInt
                    tmp >>= 5
                }
                var best = 0
                for (i <- 1 until batchSize if cnt(i) > 0) {
                    cnt(i) -= 1
                    val newCode = encode(cnt)
                    cnt(i) += 1
                    val add = if (rem == 0) 1 else 0
                    val newRem = (rem + i) % batchSize
                    val cand = add + dfs(newCode, newRem)
                    if (cand > best) best = cand
                }
                best
            })
        }

        val startCode = encode(freq)
        result + dfs(startCode, 0)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn max_happy_groups(batch_size: i32, groups: Vec<i32>) -> i32 {
        let k = batch_size as usize;
        // frequency of each remainder
        let mut freq = vec![0usize; k];
        for g in groups {
            let r = (g % batch_size) as usize;
            freq[r] += 1;
        }
        // groups with remainder 0 are always happy
        let base_happy = freq[0] as i32;

        // encode frequencies of remainders 1..k-1 into a u64 key (5 bits per count)
        let mut start_key: u64 = 0;
        for r in 1..k {
            let cnt = freq[r];
            start_key |= (cnt as u64) << ((r - 1) * 5);
        }

        fn get_cnt(key: u64, idx: usize) -> usize {
            ((key >> (idx * 5)) & 31) as usize
        }
        fn set_cnt(key: u64, idx: usize, new_cnt: usize) -> u64 {
            let mask = !(31u64 << (idx * 5));
            (key & mask) | ((new_cnt as u64) << (idx * 5))
        }

        fn dfs(
            key: u64,
            cur_rem: usize,
            k: usize,
            memo: &mut HashMap<(u64, usize), i32>,
        ) -> i32 {
            if let Some(&v) = memo.get(&(key, cur_rem)) {
                return v;
            }
            if key == 0 {
                // no groups left
                return 0;
            }
            let mut best = 0i32;
            for r in 1..k {
                let idx = r - 1;
                let cnt = get_cnt(key, idx);
                if cnt == 0 {
                    continue;
                }
                let new_key = set_cnt(key, idx, cnt - 1);
                let next_rem = (cur_rem + r) % k;
                let add = dfs(new_key, next_rem, k, memo);
                let gain = if cur_rem == 0 { 1 } else { 0 };
                best = best.max(add + gain);
            }
            memo.insert((key, cur_rem), best);
            best
        }

        let mut memo: HashMap<(u64, usize), i32> = HashMap::new();
        let extra = dfs(start_key, 0, k, &mut memo);

        base_happy + extra
    }
}
```

## Racket

```racket
(define/contract (max-happy-groups batchSize groups)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((b batchSize)
         (bits-per 6)                         ; enough for counts up to 30
         (mask (sub1 (arithmetic-shift 1 bits-per)))
         ;; frequency of remainders
         (freq (make-vector b 0))
         (_ (for-each (lambda (g)
                        (let ((r (modulo g b)))
                          (vector-set! freq r (+ (vector-ref freq r) 1))))
                      groups))
         ;; groups with remainder 0 are always happy
         (base-happy (vector-ref freq 0))
         (_ (vector-set! freq 0 0))
         ;; encode state as integer key
         (encode
          (lambda ()
            (let loop ((i 0) (acc 0))
              (if (= i b)
                  acc
                  (loop (+ i 1)
                        (bitwise-ior acc
                                     (arithmetic-shift (vector-ref freq i)
                                                        (* i bits-per))))))))
         (init-key (encode))
         (memo (make-hash)))
    ;; helper to get count of remainder i from key
    (define (count-at key i)
      (bitwise-and (arithmetic-shift key (- (* i bits-per))) mask))
    ;; DP function: returns max additional happy groups from this state with current remainder r
    (define (dp key r)
      (if (= key 0)
          0
          (let ((cached (hash-ref memo (cons key r) #f)))
            (if cached
                cached
                (let loop ((i 0) (best -1000000))
                  (if (= i b)
                      (begin
                        (hash-set! memo (cons key r) best)
                        best)
                      (let ((cnt (count-at key i)))
                        (if (= cnt 0)
                            (loop (+ i 1) best)
                            (let* ((new-key (- key (arithmetic-shift 1 (* i bits-per))))
                                   (new-r (modulo (+ r i) b))
                                   (val (dp new-key new-r))
                                   (add (if (= r 0) 1 0))
                                   (cand (+ val add)))
                              (loop (+ i 1) (max best cand))))))))))
    (+ base-happy (dp init-key 0)))
```

## Erlang

```erlang
-module(solution).
-export([max_happy_groups/2]).

-spec max_happy_groups(integer(), [integer()]) -> integer().
max_happy_groups(BatchSize, Groups) ->
    Remainders = [G rem BatchSize || G <- Groups],
    Count0 = length([R || R <- Remainders, R == 0]),
    FreqMap = lists:foldl(
        fun(R, M) ->
            if
                R == 0 -> M;
                true -> maps:update_with(R, fun(C) -> C + 1 end, 1, M)
            end
        end,
        #{},
        Remainders),
    CountsList = [maps:get(I, FreqMap, 0) || I <- lists:seq(0, BatchSize - 1)],
    CountsTuple = list_to_tuple(CountsList),
    {Add, _} = dp(0, CountsTuple, BatchSize, #{}),
    Count0 + Add.

dp(R, CountsTuple, BatchSize, Memo) ->
    Key = {R, CountsTuple},
    case maps:get(Key, Memo, undefined) of
        Value when Value =/= undefined ->
            {Value, Memo};
        _ ->
            Zero = lists:all(fun(X) -> X == 0 end, tuple_to_list(CountsTuple)),
            if
                Zero ->
                    NewMemo = maps:put(Key, 0, Memo),
                    {0, NewMemo};
                true ->
                    Fun =
                        fun(I, {CurMax, CurMemo}) ->
                            CountI = element(I + 1, CountsTuple), % remainder I (tuple index starts at 1)
                            if
                                CountI > 0 ->
                                    NewCounts = setelement(I + 1, CountsTuple, CountI - 1),
                                    NewR = (R + I) rem BatchSize,
                                    {SubRes, SubMemo} = dp(NewR, NewCounts, BatchSize, CurMemo),
                                    Add = if R == 0 -> 1; true -> 0 end,
                                    Total = Add + SubRes,
                                    if
                                        Total > CurMax ->
                                            {Total, SubMemo};
                                        true ->
                                            {CurMax, SubMemo}
                                    end;
                                true ->
                                    {CurMax, CurMemo}
                            end
                        end,
                    {BestVal, MemoAfter} = lists:foldl(Fun, {-1, Memo}, lists:seq(1, BatchSize - 1)),
                    FinalMemo = maps:put(Key, BestVal, MemoAfter),
                    {BestVal, FinalMemo}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_happy_groups(batch_size :: integer, groups :: [integer]) :: integer
  def max_happy_groups(batch_size, groups) do
    {base_happy, freq_list} =
      Enum.reduce(groups, {0, List.duplicate(0, batch_size)}, fn g, {b, acc} ->
        r = rem(g, batch_size)

        if r == 0 do
          {b + 1, acc}
        else
          updated = List.update_at(acc, r, &(&1 + 1))
          {b, updated}
        end
      end)

    freq_tuple = List.to_tuple(freq_list)
    {extra_happy, _} = dfs(freq_tuple, 0, batch_size, %{})
    base_happy + extra_happy
  end

  defp dfs(freq, cur_rem, batch_size, memo) do
    key = {freq, cur_rem}

    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        if all_zero?(freq) do
          {0, Map.put(memo, key, 0)}
        else
          {best, new_memo} =
            Enum.reduce(1..batch_size - 1, {-1_000_000, memo}, fn i, {cur_best, mem_acc} ->
              cnt = elem(freq, i)

              if cnt > 0 do
                new_freq = put_elem(freq, i, cnt - 1)
                new_rem = rem(cur_rem + i, batch_size)
                {sub_res, mem_next} = dfs(new_freq, new_rem, batch_size, mem_acc)
                add = if cur_rem == 0, do: 1, else: 0
                cand = sub_res + add

                if cand > cur_best do
                  {cand, mem_next}
                else
                  {cur_best, mem_next}
                end
              else
                {cur_best, mem_acc}
              end
            end)

          memo_final = Map.put(new_memo, key, best)
          {best, memo_final}
        end
    end
  end

  defp all_zero?(tuple) do
    tuple
    |> Tuple.to_list()
    |> Enum.all?(&(&1 == 0))
  end
end
```
