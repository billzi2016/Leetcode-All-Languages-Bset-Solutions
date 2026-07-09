# 0514. Freedom Trail

## Cpp

```cpp
class Solution {
public:
    int n;
    string ring, key;
    vector<vector<int>> memo;
    unordered_map<char, vector<int>> pos;

    int dist(int i, int j) {
        int d = abs(i - j);
        return min(d, n - d);
    }

    int dfs(int i, int kIdx) {
        if (kIdx == key.size()) return 0;
        int &res = memo[i][kIdx];
        if (res != -1) return res;
        res = INT_MAX / 2;
        for (int idx : pos[key[kIdx]]) {
            int steps = dist(i, idx) + 1 + dfs(idx, kIdx + 1);
            res = min(res, steps);
        }
        return res;
    }

    int findRotateSteps(string ring_, string key_) {
        ring = ring_;
        key = key_;
        n = ring.size();
        memo.assign(n, vector<int>(key.size(), -1));
        for (int i = 0; i < n; ++i) {
            pos[ring[i]].push_back(i);
        }
        return dfs(0, 0);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int findRotateSteps(String ring, String key) {
        int n = ring.length();
        Map<Character, List<Integer>> posMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char c = ring.charAt(i);
            posMap.computeIfAbsent(c, k -> new ArrayList<>()).add(i);
        }
        final int INF = Integer.MAX_VALUE / 2;
        int[] dpPrev = new int[n];
        Arrays.fill(dpPrev, INF);
        dpPrev[0] = 0; // start at position 0

        for (int idx = 0; idx < key.length(); idx++) {
            char target = key.charAt(idx);
            List<Integer> targets = posMap.get(target);
            int[] dpCurr = new int[n];
            Arrays.fill(dpCurr, INF);
            for (int t : targets) {
                int best = INF;
                for (int p = 0; p < n; p++) {
                    if (dpPrev[p] == INF) continue;
                    int diff = Math.abs(p - t);
                    int step = Math.min(diff, n - diff);
                    int cand = dpPrev[p] + step;
                    if (cand < best) best = cand;
                }
                dpCurr[t] = best;
            }
            dpPrev = dpCurr;
        }

        int minRot = INF;
        for (int v : dpPrev) {
            if (v < minRot) minRot = v;
        }
        return minRot + key.length();
    }
}
```

## Python

```python
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        # map each character to its positions in the ring
        char_pos = {}
        for i, ch in enumerate(ring):
            char_pos.setdefault(ch, []).append(i)

        # dp maps current ring index (at 12:00) to minimal steps so far
        dp = {0: 0}
        for ch in key:
            ndp = {}
            for target in char_pos[ch]:
                best = float('inf')
                for prev_idx, cost in dp.items():
                    diff = abs(prev_idx - target)
                    step = min(diff, n - diff)
                    total = cost + step + 1  # +1 for pressing the button
                    if total < best:
                        best = total
                ndp[target] = best
            dp = ndp

        return min(dp.values())
```

## Python3

```python
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        # map each character to its positions in the ring
        pos = {}
        for i, ch in enumerate(ring):
            pos.setdefault(ch, []).append(i)

        # dp maps current ring index to minimal steps taken so far (excluding press)
        dp = {0: 0}
        for ch in key:
            new_dp = {}
            for idx in pos[ch]:
                best = float('inf')
                for prev_idx, cost in dp.items():
                    diff = abs(idx - prev_idx)
                    step = min(diff, n - diff) + cost
                    if step < best:
                        best = step
                # add one step for pressing the button
                new_dp[idx] = best + 1
            dp = new_dp

        return min(dp.values())
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <limits.h>

int findRotateSteps(char* ring, char* key) {
    int n = strlen(ring);
    int m = strlen(key);
    if (m == 0) return 0;

    int pos[26][100];
    int cnt[26] = {0};

    for (int i = 0; i < n; ++i) {
        int c = ring[i] - 'a';
        pos[c][cnt[c]++] = i;
    }

    const int INF = INT_MAX / 2;
    int prev[101];
    int cur[101];

    for (int i = 0; i < n; ++i) prev[i] = INF;
    prev[0] = 0; // start at position 0

    for (int ki = 0; ki < m; ++ki) {
        int ci = key[ki] - 'a';
        for (int i = 0; i < n; ++i) cur[i] = INF;

        for (int p = 0; p < n; ++p) {
            if (prev[p] == INF) continue;
            for (int idx = 0; idx < cnt[ci]; ++idx) {
                int q = pos[ci][idx];
                int diff = abs(p - q);
                int step = diff < n - diff ? diff : n - diff;
                int total = prev[p] + step + 1; // +1 for pressing button
                if (total < cur[q]) cur[q] = total;
            }
        }

        for (int i = 0; i < n; ++i) prev[i] = cur[i];
    }

    int ans = INF;
    for (int i = 0; i < n; ++i)
        if (prev[i] < ans) ans = prev[i];

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindRotateSteps(string ring, string key)
    {
        int n = ring.Length;
        var posMap = new Dictionary<char, List<int>>();
        for (int i = 0; i < n; i++)
        {
            char c = ring[i];
            if (!posMap.ContainsKey(c)) posMap[c] = new List<int>();
            posMap[c].Add(i);
        }

        const int INF = int.MaxValue / 2;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) dp[i] = INF;

        // initialize for first character
        var prevPositions = posMap[key[0]];
        foreach (int p in prevPositions)
        {
            dp[p] = Math.Min(Math.Abs(p - 0), n - Math.Abs(p - 0));
        }

        // process remaining characters
        for (int idx = 1; idx < key.Length; idx++)
        {
            char curChar = key[idx];
            var curPositions = posMap[curChar];
            int[] newDp = new int[n];
            for (int i = 0; i < n; i++) newDp[i] = INF;

            foreach (int curPos in curPositions)
            {
                int best = INF;
                foreach (int prevPos in prevPositions)
                {
                    int dist = Math.Abs(curPos - prevPos);
                    dist = Math.Min(dist, n - dist);
                    int cand = dp[prevPos] + dist;
                    if (cand < best) best = cand;
                }
                newDp[curPos] = best;
            }

            dp = newDp;
            prevPositions = curPositions;
        }

        int minSteps = INF;
        foreach (int p in prevPositions)
        {
            if (dp[p] < minSteps) minSteps = dp[p];
        }

        // add presses for each character
        return minSteps + key.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} ring
 * @param {string} key
 * @return {number}
 */
var findRotateSteps = function(ring, key) {
    const n = ring.length;
    const charPos = {};
    for (let i = 0; i < n; ++i) {
        const ch = ring[i];
        if (!charPos[ch]) charPos[ch] = [];
        charPos[ch].push(i);
    }
    let dpPrev = new Array(n).fill(Infinity);
    dpPrev[0] = 0;
    for (const c of key) {
        const positions = charPos[c];
        const dpCurr = new Array(n).fill(Infinity);
        for (const pos of positions) {
            for (let prev = 0; prev < n; ++prev) {
                if (dpPrev[prev] === Infinity) continue;
                const diff = Math.abs(pos - prev);
                const step = Math.min(diff, n - diff);
                const val = dpPrev[prev] + step;
                if (val < dpCurr[pos]) dpCurr[pos] = val;
            }
        }
        dpPrev = dpCurr;
    }
    let minRot = Infinity;
    for (const v of dpPrev) {
        if (v < minRot) minRot = v;
    }
    return minRot + key.length;
};
```

## Typescript

```typescript
function findRotateSteps(ring: string, key: string): number {
    const n = ring.length;
    const posMap: { [c: string]: number[] } = {};
    for (let i = 0; i < n; i++) {
        const c = ring[i];
        if (!posMap[c]) posMap[c] = [];
        posMap[c].push(i);
    }

    const dist = (i: number, j: number): number => {
        const diff = Math.abs(i - j);
        return Math.min(diff, n - diff);
    };

    // positions and dp for the first character
    let prevPosArr = posMap[key[0]];
    let dpPrev = prevPosArr.map(p => dist(0, p));

    // process remaining characters
    for (let idx = 1; idx < key.length; idx++) {
        const curChar = key[idx];
        const curPosArr = posMap[curChar];
        const dpCurr = new Array(curPosArr.length).fill(Infinity);

        for (let ci = 0; ci < curPosArr.length; ci++) {
            const curPos = curPosArr[ci];
            for (let pi = 0; pi < prevPosArr.length; pi++) {
                const cost = dpPrev[pi] + dist(prevPosArr[pi], curPos);
                if (cost < dpCurr[ci]) dpCurr[ci] = cost;
            }
        }

        prevPosArr = curPosArr;
        dpPrev = dpCurr;
    }

    const minRotations = Math.min(...dpPrev);
    return minRotations + key.length; // add presses for each character
}
```

## Php

```php
class Solution {
    /**
     * @param String $ring
     * @param String $key
     * @return Integer
     */
    function findRotateSteps($ring, $key) {
        $n = strlen($ring);
        $m = strlen($key);
        if ($m == 0) return 0;

        // map each character to its positions in the ring
        $pos = [];
        for ($i = 0; $i < $n; $i++) {
            $c = $ring[$i];
            if (!isset($pos[$c])) {
                $pos[$c] = [];
            }
            $pos[$c][] = $i;
        }

        // dp[i] = minimal rotation steps to have ring aligned at position i after processing current prefix of key
        $dp = array_fill(0, $n, PHP_INT_MAX);
        $dp[0] = 0; // start at index 0

        for ($k = 0; $k < $m; $k++) {
            $c = $key[$k];
            $newDp = array_fill(0, $n, PHP_INT_MAX);
            foreach ($pos[$c] as $t) { // target positions for current character
                $best = PHP_INT_MAX;
                for ($p = 0; $p < $n; $p++) {
                    if ($dp[$p] === PHP_INT_MAX) continue;
                    $diff = abs($p - $t);
                    $step = min($diff, $n - $diff);
                    $candidate = $dp[$p] + $step;
                    if ($candidate < $best) {
                        $best = $candidate;
                    }
                }
                $newDp[$t] = $best;
            }
            $dp = $newDp;
        }

        $minSteps = min($dp);
        return $minSteps + $m; // add button presses
    }
}
```

## Swift

```swift
class Solution {
    func findRotateSteps(_ ring: String, _ key: String) -> Int {
        let ringArr = Array(ring)
        let keyArr = Array(key)
        let n = ringArr.count
        
        // Map each character to its positions in the ring
        var posMap = [Character: [Int]]()
        for (i, ch) in ringArr.enumerated() {
            posMap[ch, default: []].append(i)
        }
        
        // Large sentinel value
        let INF = Int.max / 4
        
        // dpPrev[i] = minimal steps to have ring aligned at position i after processing previous characters
        var dpPrev = [Int](repeating: INF, count: n)
        dpPrev[0] = 0   // initially at position 0
        
        for ch in keyArr {
            guard let targets = posMap[ch] else { continue }
            var dpCurr = [Int](repeating: INF, count: n)
            
            for t in targets {
                var best = INF
                for p in 0..<n {
                    let prev = dpPrev[p]
                    if prev < INF {
                        let diff = abs(t - p)
                        let step = min(diff, n - diff)
                        let cand = prev + step
                        if cand < best { best = cand }
                    }
                }
                dpCurr[t] = best + 1   // press the button
            }
            dpPrev = dpCurr
        }
        
        return dpPrev.min() ?? 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRotateSteps(ring: String, key: String): Int {
        val n = ring.length
        val pos = Array(26) { mutableListOf<Int>() }
        for (i in 0 until n) {
            pos[ring[i] - 'a'].add(i)
        }

        val INF = Int.MAX_VALUE / 2
        var dpPrev = IntArray(n) { INF }
        dpPrev[0] = 0

        for (ch in key) {
            val curList = pos[ch - 'a']
            val dpCurr = IntArray(n) { INF }
            for (nextPos in curList) {
                var best = INF
                for (prevPos in 0 until n) {
                    if (dpPrev[prevPos] < INF) {
                        val diff = kotlin.math.abs(nextPos - prevPos)
                        val step = kotlin.math.min(diff, n - diff)
                        val cost = dpPrev[prevPos] + step + 1
                        if (cost < best) best = cost
                    }
                }
                dpCurr[nextPos] = best
            }
            dpPrev = dpCurr
        }

        var answer = INF
        for (v in dpPrev) {
            if (v < answer) answer = v
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int findRotateSteps(String ring, String key) {
    if (key.isEmpty) return 0;
    int n = ring.length;
    Map<String, List<int>> posMap = {};
    for (int i = 0; i < n; i++) {
      String ch = ring[i];
      posMap.putIfAbsent(ch, () => []).add(i);
    }
    const int INF = 1 << 30;
    List<int> dpPrev = List.filled(n, INF);
    dpPrev[0] = 0;

    for (int ki = 0; ki < key.length; ki++) {
      String c = key[ki];
      List<int> positions = posMap[c] ?? [];
      List<int> dpCurr = List.filled(n, INF);
      for (int p in positions) {
        int best = INF;
        for (int prev = 0; prev < n; prev++) {
          if (dpPrev[prev] == INF) continue;
          int diff = (p - prev).abs();
          int step = diff < n - diff ? diff : n - diff;
          int total = dpPrev[prev] + step + 1; // +1 for pressing button
          if (total < best) best = total;
        }
        dpCurr[p] = best;
      }
      dpPrev = dpCurr;
    }

    int ans = INF;
    for (int v in dpPrev) {
      if (v < ans) ans = v;
    }
    return ans;
  }
}
```

## Golang

```go
func findRotateSteps(ring string, key string) int {
	n := len(ring)
	// map each character to its positions in the ring
	posMap := make(map[byte][]int)
	for i := 0; i < n; i++ {
		c := ring[i]
		posMap[c] = append(posMap[c], i)
	}
	const INF = int(^uint(0) >> 1) // max int
	prev := make([]int, n)
	for i := 0; i < n; i++ {
		prev[i] = INF
	}
	prev[0] = 0 // start at position 0 with no steps taken

	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	for i := 0; i < len(key); i++ {
		ch := key[i]
		cur := make([]int, n)
		for j := 0; j < n; j++ {
			cur[j] = INF
		}
		targets := posMap[ch]
		for _, t := range targets {
			best := INF
			for p := 0; p < n; p++ {
				if prev[p] == INF {
					continue
				}
				diff := abs(p - t)
				rot := min(diff, n-diff) + 1 // rotation steps plus press
				total := prev[p] + rot
				if total < best {
					best = total
				}
			}
			cur[t] = best
		}
		prev = cur
	}

	ans := INF
	for _, v := range prev {
		if v < ans {
			ans = v
		}
	}
	return ans
}
```

## Ruby

```ruby
def find_rotate_steps(ring, key)
  n = ring.length
  pos = Hash.new { |h, k| h[k] = [] }
  ring.chars.each_with_index { |c, i| pos[c] << i }

  prev = Array.new(n, Float::INFINITY)
  prev[0] = 0

  key.each_char do |ch|
    cur = Array.new(n, Float::INFINITY)
    pos[ch].each do |t|
      best = Float::INFINITY
      (0...n).each do |i|
        next if prev[i] == Float::INFINITY
        diff = (i - t).abs
        step = [diff, n - diff].min
        total = prev[i] + step + 1
        best = total if total < best
      end
      cur[t] = best
    end
    prev = cur
  end

  prev.min.to_i
end
```

## Scala

```scala
object Solution {
    def findRotateSteps(ring: String, key: String): Int = {
        val n = ring.length
        val pos = Array.fill(26)(scala.collection.mutable.ArrayBuffer[Int]())
        for (i <- 0 until n) {
            pos(ring(i) - 'a') += i
        }
        val INF = Int.MaxValue / 4
        var prev = Array.fill(n)(INF)

        // Initialize dp for the first character of key
        val firstList = pos(key(0) - 'a')
        for (p <- firstList) {
            val dist = Math.min(p, n - p) // distance from index 0 to p
            prev(p) = dist + 1 // include button press
        }

        // Process remaining characters of key
        for (kIdx <- 1 until key.length) {
            val curr = Array.fill(n)(INF)
            val curList = pos(key(kIdx) - 'a')
            for (p <- curList) {
                var best = INF
                for (prevPos <- 0 until n if prev(prevPos) < INF) {
                    val diff = Math.abs(p - prevPos)
                    val step = Math.min(diff, n - diff)
                    val total = prev(prevPos) + step + 1 // include button press
                    if (total < best) best = total
                }
                curr(p) = best
            }
            prev = curr
        }

        // Minimum steps after processing all characters
        var ans = INF
        for (p <- 0 until n) {
            if (prev(p) < ans) ans = prev(p)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_rotate_steps(ring: String, key: String) -> i32 {
        let n = ring.len();
        let mut pos: Vec<Vec<usize>> = vec![Vec::new(); 26];
        for (i, ch) in ring.chars().enumerate() {
            pos[(ch as u8 - b'a') as usize].push(i);
        }
        let mut dp = vec![i32::MAX; n];
        dp[0] = 0;
        for ch in key.chars() {
            let idx = (ch as u8 - b'a') as usize;
            let mut next_dp = vec![i32::MAX; n];
            for &target in pos[idx].iter() {
                let mut best = i32::MAX;
                for p in 0..n {
                    if dp[p] == i32::MAX {
                        continue;
                    }
                    let diff = ((p as i32) - (target as i32)).abs();
                    let step = diff.min((n as i32) - diff);
                    let cand = dp[p] + step;
                    if cand < best {
                        best = cand;
                    }
                }
                next_dp[target] = best;
            }
            dp = next_dp;
        }
        let min_rot = dp.into_iter().min().unwrap_or(i32::MAX);
        min_rot + key.len() as i32
    }
}
```

## Racket

```racket
(define/contract (find-rotate-steps ring key)
  (-> string? string? exact-integer?)
  (let* ((n (string-length ring))
         ;; map each character to the list of its positions in `ring`
         (pos-map (let ((h (make-hash)))
                    (for ([i (in-range n)])
                      (let* ((c (string-ref ring i))
                             (lst (hash-ref h c '())))
                        (hash-set! h c (cons i lst))))
                    h))
         ;; minimal rotation distance between two indices on the ring
         (dist (lambda (a b)
                 (let ((d (abs (- a b))))
                   (min d (- n d)))))
         (memo (make-hash)))
    (define (dp cur idx)
      (if (= idx (string-length key))
          0
          (let* ((kch (string-ref key idx))
                 (targets (hash-ref pos-map kch '()))
                 (mkey (format "~a#~a" cur idx)))
            (or (hash-ref memo mkey #f)
                (let ((best (apply min
                                   (map (lambda (t)
                                          (+ (dist cur t)
                                             (dp t (add1 idx))))
                                        targets))))
                  (hash-set! memo mkey best)
                  best)))))
    (+ (dp 0 0) (string-length key))))
```

## Erlang

```erlang
-spec find_rotate_steps(Ring :: unicode:unicode_binary(), Key :: unicode:unicode_binary()) -> integer().
find_rotate_steps(Ring, Key) ->
    RingList = binary_to_list(Ring),
    N = length(RingList),

    CharPosMap =
        element(2,
            lists:foldl(
                fun(Char, {Idx, Acc}) ->
                    Updated = maps:put(Char, [Idx | maps:get(Char, Acc, [])], Acc),
                    {Idx + 1, Updated}
                end,
                {0, #{}},
                RingList)),

    KeyList = binary_to_list(Key),

    [FirstChar | RestChars] = KeyList,
    FirstPositions = maps:get(FirstChar, CharPosMap),
    PrevMap0 = maps:from_list(
        lists:map(fun(Pos) -> {Pos, distance(0, Pos, N)} end, FirstPositions)),

    FinalMap =
        lists:foldl(
            fun(Char, PrevMap) ->
                Positions = maps:get(Char, CharPosMap),
                NewMap =
                    lists:foldl(
                        fun(Pos2, Acc) ->
                            MinDist = min_dist_to_pos(Pos2, PrevMap, N),
                            maps:put(Pos2, MinDist, Acc)
                        end,
                        #{},
                        Positions),
                NewMap
            end,
            PrevMap0,
            RestChars),

    MinimalRotations = lists:min(maps:values(FinalMap)),
    MinimalRotations + length(KeyList).

min_dist_to_pos(Pos2, PrevMap, N) ->
    lists:min(
        [Dist1 + distance(Pos1, Pos2, N) || {Pos1, Dist1} <- maps:to_list(PrevMap)]).

distance(A, B, N) ->
    D = erlang:abs(A - B),
    if
        D > N - D -> N - D;
        true -> D
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_rotate_steps(ring :: String.t(), key :: String.t()) :: integer()
  def find_rotate_steps(ring, key) do
    n = String.length(ring)
    ring_chars = String.graphemes(ring)

    # map each character to the list of its positions in the ring
    pos_map =
      Enum.reduce(Enum.with_index(ring_chars), %{}, fn {ch, idx}, acc ->
        Map.update(acc, ch, [idx], &[idx | &1])
      end)
      |> Enum.map(fn {k, v} -> {k, Enum.reverse(v)} end)
      |> Enum.into(%{})

    key_chars = String.graphemes(key)
    inf = 1_000_000

    # initial dp for the first character of the key
    first_char = hd(key_chars)

    init_dp =
      for i <- 0..(n - 1), into: %{} do
        if i in Map.get(pos_map, first_char, []) do
          {i, min(i, n - i)}
        else
          {i, inf}
        end
      end

    final_dp =
      Enum.reduce(tl(key_chars), init_dp, fn ch, prev_dp ->
        # prepare new dp filled with INF
        new_dp = for i <- 0..(n - 1), into: %{}, do: {i, inf}

        target_idxs = Map.get(pos_map, ch, [])
        source_idxs = Enum.filter(Map.keys(prev_dp), fn idx -> prev_dp[idx] < inf end)

        Enum.reduce(target_idxs, new_dp, fn t_idx, acc ->
          min_cost =
            Enum.reduce(source_idxs, inf, fn s_idx, cur_min ->
              steps = prev_dp[s_idx] + distance(s_idx, t_idx, n)
              if steps < cur_min, do: steps, else: cur_min
            end)

          Map.put(acc, t_idx, min(min_cost, acc[t_idx]))
        end)
      end)

    min_rotations = final_dp |> Map.values() |> Enum.min()
    min_rotations + String.length(key)
  end

  defp distance(a, b, n) do
    diff = abs(a - b)
    min(diff, n - diff)
  end
end
```
