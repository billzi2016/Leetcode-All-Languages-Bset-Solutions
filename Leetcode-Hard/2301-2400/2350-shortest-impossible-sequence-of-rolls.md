# 2350. Shortest Impossible Sequence of Rolls

## Cpp

```cpp
class Solution {
public:
    int shortestSequence(vector<int>& rolls, int k) {
        const long long INF = (long long)4e18;
        vector<long long> need(k + 1, 1); // need for current length
        int len = 1;
        while (true) {
            vector<long long> cur = need; // mutable copy for this pass
            for (int x : rolls) {
                if (cur[x] > 0) --cur[x];
            }
            bool allSatisfied = true;
            for (int i = 1; i <= k; ++i) {
                if (cur[i] > 0) { allSatisfied = false; break; }
            }
            if (!allSatisfied) return len;
            // prepare need for next length
            ++len;
            for (int i = 1; i <= k; ++i) {
                __int128 prod = (__int128)need[i] * k;
                need[i] = prod > INF ? INF : (long long)prod;
            }
        }
    }
};
```

## Java

```java
class Solution {
    public int shortestSequence(int[] rolls, int k) {
        int[] seen = new int[k + 1];
        int needed = k;
        int segmentId = 1;
        int answer = 1; // at least length 1 is impossible if not all numbers appear

        for (int val : rolls) {
            if (seen[val] != segmentId) {
                seen[val] = segmentId;
                needed--;
            }
            if (needed == 0) {
                answer++;
                segmentId++;
                needed = k;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()
        complete_sets = 0
        for v in rolls:
            if v not in seen:
                seen.add(v)
                if len(seen) == k:
                    complete_sets += 1
                    seen.clear()
        return complete_sets + 1
```

## Python3

```python
class Solution:
    def shortestSequence(self, rolls, k):
        seen = [0] * (k + 1)
        cur_round = 1
        distinct = 0
        layers = 0
        for v in rolls:
            if seen[v] != cur_round:
                seen[v] = cur_round
                distinct += 1
                if distinct == k:
                    layers += 1
                    cur_round += 1
                    distinct = 0
        return layers + 1
```

## C

```c
int shortestSequence(int* rolls, int rollsSize, int k) {
    int *mark = (int*)calloc(k + 1, sizeof(int));
    int curRound = 1;
    int distinct = 0;
    int rounds = 0;
    for (int i = 0; i < rollsSize; ++i) {
        int v = rolls[i];
        if (mark[v] != curRound) {
            mark[v] = curRound;
            ++distinct;
            if (distinct == k) {
                ++rounds;
                ++curRound;
                distinct = 0;
            }
        }
    }
    free(mark);
    return rounds + 1;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int ShortestSequence(int[] rolls, int k) {
        int n = rolls.Length;
        int INF = n; // sentinel for no occurrence
        int[] lastSeen = new int[k + 1];
        for (int i = 1; i <= k; i++) lastSeen[i] = INF;

        int missingCount = k;               // values not appearing after current position
        int maxF = n + 2;                   // maximum possible f value (+ safety)
        int[] freq = new int[maxF];         // frequency of each f value in the multiset
        int curMin = maxF;                  // current minimal f present in multiset

        int[] f = new int[n];

        for (int idx = n - 1; idx >= 0; idx--) {
            if (missingCount > 0) {
                f[idx] = 1;
            } else {
                while (curMin <= n + 1 && freq[curMin] == 0) curMin++;
                f[idx] = 1 + curMin;
            }

            int v = rolls[idx];
            int oldPos = lastSeen[v];

            if (oldPos == INF) {
                // this value was missing after the next position
                missingCount--;
            } else {
                int valToRemove = f[oldPos];
                freq[valToRemove]--;
                // curMin will be adjusted lazily when needed
            }

            int valInsert = f[idx];
            freq[valInsert]++;
            if (valInsert < curMin) curMin = valInsert;

            lastSeen[v] = idx;
        }

        if (missingCount > 0) return 1;
        while (curMin <= n + 1 && freq[curMin] == 0) curMin++;
        return 1 + curMin;
    }
}
```

## Javascript

```javascript
/****
 * @param {number[]} rolls
 * @param {number} k
 * @return {number}
 */
var shortestSequence = function(rolls, k) {
    const n = rolls.length;
    // freq of each value
    const cnt = new Array(k + 1).fill(0);
    for (const v of rolls) cnt[v]++;

    // If some number never appears -> answer is 1
    for (let i = 1; i <= k; ++i) {
        if (cnt[i] === 0) return 1;
    }

    // For length 2: need every ordered pair (a,b)
    // Compute for each a how many distinct values appear after some occurrence of a
    const outCnt = new Array(k + 1).fill(0);
    const seen = new Uint8Array(k + 1); // suffix distinct marker
    let distinctSuffix = 0;
    for (let i = n - 1; i >= 0; --i) {
        const a = rolls[i];
        outCnt[a] = Math.max(outCnt[a], distinctSuffix);
        if (!seen[a]) {
            seen[a] = 1;
            ++distinctSuffix;
        }
    }
    for (let i = 1; i <= k; ++i) {
        // self-pair requires at least two occurrences, which is already reflected
        // because a later occurrence of the same value contributes to outCnt.
        if (outCnt[i] < k) return 2;
    }

    // For length >=3 we can use iterative DP based on the observation that
    // the answer cannot be large: when k^len exceeds n, some sequence must be missing.
    // Since n ≤ 1e5, len will be at most ~17 for k = 2 and even smaller for larger k.
    // We'll simulate building all possible sequences of current length using a map
    // from hash to earliest position where that sequence can end.
    // The number of distinct subsequences of length L is bounded by n choose L,
    // which stays manageable for the small L we will encounter.

    const maxLen = 20; // safe upper bound given constraints
    // dp maps a string representation of a sequence to earliest ending index
    let prevMap = new Map(); // sequences of length len-1
    // initialize with empty sequence at position -1
    prevMap.set('', -1);

    for (let len = 1; len <= maxLen; ++len) {
        const curMap = new Map();
        // For each position, try to extend all sequences from previous map that end before this index.
        // To keep it efficient we iterate over rolls once and update a temporary structure.
        // Since the total number of stored sequences never exceeds n (each sequence is created
        // at its first possible ending position), the overall complexity stays O(n * answer).

        const seqsEndingAt = new Array(n).fill(null);
        for (let i = 0; i < n; ++i) {
            const val = rolls[i];
            // extend sequences from prevMap whose end index < i
            for (const [seq, pos] of prevMap.entries()) {
                if (pos < i) {
                    const newSeq = seq + ',' + val;
                    if (!curMap.has(newSeq)) {
                        curMap.set(newSeq, i);
                    }
                }
            }
        }

        // If we have generated all k^len sequences, continue; otherwise answer is len.
        // To avoid huge memory when k^len is massive, we stop early as soon as
        // curMap size < Math.pow(k, len) (which will happen quickly for large k).
        const totalNeeded = Math.pow(k, len);
        if (curMap.size < totalNeeded) return len;

        prevMap = curMap;
    }

    // Fallback (should never reach here)
    return maxLen + 1;
};
```

## Typescript

```typescript
function shortestSequence(rolls: number[], k: number): number {
    const pos: number[][] = Array.from({ length: k + 1 }, () => []);
    for (let i = 0; i < rolls.length; i++) {
        pos[rolls[i]].push(i);
    }
    const idx = new Uint32Array(k + 1); // pointers to first occurrence > cur
    let cur = -1;
    let len = 0;
    while (true) {
        let maxPos = -1;
        for (let v = 1; v <= k; v++) {
            const arr = pos[v];
            let i = idx[v];
            while (i < arr.length && arr[i] <= cur) i++;
            idx[v] = i;
            if (i === arr.length) {
                return len + 1;
            }
            const nxt = arr[i];
            if (nxt > maxPos) maxPos = nxt;
        }
        cur = maxPos;
        len++;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rolls
     * @param Integer $k
     * @return Integer
     */
    function shortestSequence($rolls, $k) {
        $n = count($rolls);
        $INF = PHP_INT_MAX;

        // dp[i] = length of shortest missing subsequence in suffix starting at i
        $dp = array_fill(0, $n + 1, 0);
        $dp[$n] = 1; // empty suffix

        // segment tree for min candidate over values 1..k
        $size = 1;
        while ($size < $k) {
            $size <<= 1;
        }
        $tree = array_fill(0, $size * 2, $INF);

        // helper to update leaf at position (value-1)
        $segUpdate = function(&$tree, $size, $pos, $val) {
            $i = $pos + $size;
            $tree[$i] = $val;
            while ($i > 1) {
                $i >>= 1;
                $left = $tree[$i << 1];
                $right = $tree[($i << 1) | 1];
                $tree[$i] = ($left < $right) ? $left : $right;
            }
        };

        // first occurrence position for each value, -1 means not seen yet
        $firstPos = array_fill(0, $k + 1, -1);
        $missingCount = $k; // number of values not present in current suffix

        for ($i = $n - 1; $i >= 0; --$i) {
            $val = $rolls[$i];
            $oldPos = $firstPos[$val];

            if ($oldPos == -1) {
                // this value becomes present in the suffix
                $missingCount--;
            }
            // update first position to current index
            $firstPos[$val] = $i;
            // new candidate for this value is dp[i+1]
            $newCand = $dp[$i + 1];
            $segUpdate($tree, $size, $val - 1, $newCand);

            if ($missingCount > 0) {
                $dp[$i] = 1;
            } else {
                // all values appear in suffix, take min candidate
                $minCand = $tree[1];
                $dp[$i] = 1 + $minCand;
            }
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func shortestSequence(_ rolls: [Int], _ k: Int) -> Int {
        var occ = [[Int]](repeating: [], count: k + 1)
        for (i, v) in rolls.enumerated() {
            occ[v].append(i)
        }
        var ptr = [Int](repeating: 0, count: k + 1)
        var pos = -1
        var length = 1
        while true {
            var maxNext = -1
            for v in 1...k {
                let list = occ[v]
                var p = ptr[v]
                while p < list.count && list[p] <= pos {
                    p += 1
                }
                if p == list.count {
                    return length
                }
                let nxt = list[p]
                if nxt > maxNext { maxNext = nxt }
                ptr[v] = p
            }
            pos = maxNext
            length += 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestSequence(rolls: IntArray, k: Int): Int {
        val seen = IntArray(k + 1)
        var version = 1
        var cnt = 0
        var sets = 0
        for (v in rolls) {
            if (seen[v] != version) {
                seen[v] = version
                cnt++
            }
            if (cnt == k) {
                sets++
                version++
                cnt = 0
            }
        }
        return sets + 1
    }
}
```

## Dart

```dart
class Solution {
  int shortestSequence(List<int> rolls, int k) {
    List<int> cnt = List.filled(k + 1, 0);
    int distinct = 0;
    int ans = 1;
    for (int v in rolls) {
      if (cnt[v] == 0) distinct++;
      cnt[v]++;
      if (distinct == k) {
        ans++;
        cnt = List.filled(k + 1, 0);
        distinct = 0;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func shortestSequence(rolls []int, k int) int {
    last := make([]int, k+1)
    segID := 1
    distinct := 0
    fullSegments := 0

    for _, v := range rolls {
        if last[v] != segID {
            last[v] = segID
            distinct++
        }
        if distinct == k {
            fullSegments++
            segID++
            distinct = 0
        }
    }
    return fullSegments + 1
}
```

## Ruby

```ruby
class SegmentTree
  INF = (1 << 60)

  def initialize(size)
    @size = size
    @n = 1
    @n <<= 1 while @n < size
    @tree = Array.new(@n * 2, INF)
  end

  def update(pos, value) # pos is 1-indexed
    idx = pos - 1 + @n
    @tree[idx] = value
    while idx > 1
      idx >>= 1
      left = idx << 1
      right = left | 1
      @tree[idx] = @tree[left] < @tree[right] ? @tree[left] : @tree[right]
    end
  end

  def min_all
    @tree[1]
  end
end

# @param {Integer[]} rolls
# @param {Integer} k
# @return {Integer}
def shortest_sequence(rolls, k)
  n = rolls.length
  seg = SegmentTree.new(k)
  leaf_vals = Array.new(k + 1, SegmentTree::INF)
  missing = k

  f_i = 0
  (n - 1).downto(0) do |i|
    v = rolls[i]
    if missing > 0
      f_i = 0
    else
      min_f = seg.min_all
      f_i = 1 + min_f
    end

    prev = leaf_vals[v]
    missing -= 1 if prev == SegmentTree::INF
    leaf_vals[v] = f_i
    seg.update(v, f_i)
  end

  return 1 if missing > 0
  seg.min_all + 2
end
```

## Scala

```scala
object Solution {
    def shortestSequence(rolls: Array[Int], k: Int): Int = {
        val cnt = new Array[Int](k + 1)
        var need = 1
        var cur = 0
        for (x <- rolls) {
            cnt(x) += 1
            if (cnt(x) == need) cur += 1
            if (cur == k) {
                need += 1
                cur = 0
            }
        }
        need
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn shortest_sequence(rolls: Vec<i32>, k: i32) -> i32 {
        let n = rolls.len();
        let k_usize = k as usize;
        // best[v] = dp value for the first occurrence of v in the current suffix,
        // -1 means v does not appear in the suffix.
        let mut best = vec![-1i32; k_usize + 1];
        let mut heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut defined = 0usize; // number of values that have appeared in the suffix

        for &roll in rolls.iter().rev() {
            // compute dp for the current position (suffix after this index)
            let dp_i: i32;
            if defined < k_usize {
                dp_i = 1;
            } else {
                // clean up stale entries
                while let Some(&Reverse((val, idx))) = heap.peek() {
                    if best[idx] == val {
                        break;
                    }
                    heap.pop();
                }
                let min_val = match heap.peek() {
                    Some(&Reverse((val, _))) => val,
                    None => 1, // should not happen when defined == k
                };
                dp_i = 1 + min_val;
            }

            // update structures with the current roll value
            let v = roll as usize;
            if best[v] == -1 {
                defined += 1;
            }
            best[v] = dp_i;
            heap.push(Reverse((dp_i, v)));
        }

        // answer corresponds to the state before any element (full array suffix)
        if defined < k_usize {
            1
        } else {
            while let Some(&Reverse((val, idx))) = heap.peek() {
                if best[idx] == val {
                    break;
                }
                heap.pop();
            }
            let min_val = match heap.peek() {
                Some(&Reverse((val, _))) => val,
                None => 1,
            };
            1 + min_val
        }
    }
}
```

## Racket

```racket
(define (shortest-sequence rolls k)
  (let* ((n (length rolls))
         (rollsV (list->vector rolls))
         (posLists (make-vector (+ k 1) '())))
    ;; build position lists
    (for ([i (in-range n)])
      (let* ((v (vector-ref rollsV i))
             (old (vector-ref posLists v)))
        (vector-set! posLists v (cons i old))))
    ;; early exit if any value missing, and convert to vectors
    (let/ec return
      (for ([v (in-range 1 (+ k 1))])
        (let ((lst (vector-ref posLists v)))
          (if (null? lst)
              (return 1)
              (vector-set! posLists v (list->vector (reverse lst))))))
      ;; binary search: first position > cur
      (define (next-pos vec cur)
        (let loop ((lo 0) (hi (vector-length vec)))
          (if (= lo hi)
              #f
              (let* ((mid (quotient (+ lo hi) 2))
                     (val (vector-ref vec mid)))
                (if (> val cur)
                    (let ((left (loop lo mid)))
                      (if left left mid))
                    (loop (+ mid 1) hi))))))
      ;; main iterative check
      (let recur ((cur -1) (len 1))
        (define maxPos -1)
        (for ([v (in-range 1 (+ k 1))])
          (let* ((vec (vector-ref posLists v))
                 (idx (next-pos vec cur)))
            (if (eq? idx #f)
                (return len))
            (let ((pos (vector-ref vec idx)))
              (when (> pos maxPos) (set! maxPos pos)))))
        (recur maxPos (+ len 1))))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_sequence/2]).

-spec shortest_sequence(Rolls :: [integer()], K :: integer()) -> integer().
shortest_sequence(Rolls, K) ->
    PosMap = build_pos_map(Rolls, 0, #{}),
    CurrLists = [{V, lists:reverse(maps:get(V, PosMap, []))} || V <- lists:seq(1, K)],
    loop(CurrLists, -1, 0).

build_pos_map([], _Idx, Map) -> Map;
build_pos_map([H|T], Idx, Map) ->
    List = maps:get(H, Map, []),
    NewMap = maps:put(H, [Idx | List], Map),
    build_pos_map(T, Idx + 1, NewMap).

loop(CurrLists, Ptr, Len) ->
    case process_values(CurrLists, Ptr) of
        {error} -> Len + 1;
        {ok, NewCurrLists, MaxPos} ->
            loop(NewCurrLists, MaxPos, Len + 1)
    end.

process_values(Pairs, Ptr) ->
    process_values(Pairs, Ptr, [], -1).

process_values([], _Ptr, Acc, Max) ->
    {ok, lists:reverse(Acc), Max};
process_values([{_V, []}|_Rest], _Ptr, _Acc, _Max) ->
    {error};
process_values([{V, L0} | Rest], Ptr, Acc, Max) ->
    NewL = drop_leq(L0, Ptr),
    case NewL of
        [] -> {error};
        [Head|_] ->
            NewMax = if Head > Max -> Head; true -> Max end,
            process_values(Rest, Ptr, [{V, NewL} | Acc], NewMax)
    end.

drop_leq([], _Ptr) -> [];
drop_leq([H|T] = List, Ptr) when H =< Ptr ->
    drop_leq(T, Ptr);
drop_leq(List, _Ptr) -> List.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_sequence(rolls :: [integer], k :: integer) :: integer
  def shortest_sequence(rolls, k) do
    {full_blocks, _distinct, _ver, _map} =
      Enum.reduce(rolls, {0, 0, 1, %{}}, fn v, {blocks, distinct, ver, map} ->
        seen_ver = Map.get(map, v, 0)

        if seen_ver == ver do
          # already counted in current segment
          {blocks, distinct, ver, map}
        else
          new_distinct = distinct + 1
          new_map = Map.put(map, v, ver)

          if new_distinct == k do
            # completed a full set of all numbers
            {blocks + 1, 0, ver + 1, new_map}
          else
            {blocks, new_distinct, ver, new_map}
          end
        end
      end)

    full_blocks + 1
  end
end
```
