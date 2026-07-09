# 3316. Find Maximum Removals From Source String

## Cpp

```cpp
class Solution {
public:
    int maxRemovals(string source, string pattern, vector<int>& targetIndices) {
        int n = source.size();
        int m = pattern.size();
        vector<char> isOptional(n, 0);
        for (int idx : targetIndices) isOptional[idx] = 1;
        
        const int INF = 1e9;
        vector<int> dp(m + 1, INF), ndp(m + 1);
        dp[0] = 0; // no characters matched, no optional kept
        
        for (int i = 0; i < n; ++i) {
            ndp = dp; // case of skipping source[i]
            int add = isOptional[i] ? 1 : 0;
            for (int j = 1; j <= m; ++j) {
                if (source[i] == pattern[j - 1]) {
                    if (dp[j - 1] + add < ndp[j])
                        ndp[j] = dp[j - 1] + add;
                }
            }
            dp.swap(ndp);
        }
        
        int minKeptOptional = dp[m];
        return (int)targetIndices.size() - minKeptOptional;
    }
};
```

## Java

```java
class Solution {
    public int maxRemovals(String source, String pattern, int[] targetIndices) {
        int n = source.length();
        int m = pattern.length();
        boolean[] removable = new boolean[n];
        for (int idx : targetIndices) {
            removable[idx] = true;
        }
        final int NEG = -1_000_000; // sufficiently small
        int[] dp = new int[m + 1];
        for (int j = 1; j <= m; ++j) dp[j] = NEG;
        dp[0] = 0;

        for (int i = 0; i < n; ++i) {
            int[] ndp = dp.clone(); // keep current character
            if (removable[i]) {
                for (int j = 0; j <= m; ++j) {
                    if (dp[j] != NEG) {
                        ndp[j] = Math.max(ndp[j], dp[j] + 1); // delete this char
                    }
                }
            }
            char c = source.charAt(i);
            for (int j = m; j >= 1; --j) {
                if (c == pattern.charAt(j - 1) && dp[j - 1] != NEG) {
                    ndp[j] = Math.max(ndp[j], dp[j - 1]); // match this char
                }
            }
            dp = ndp;
        }
        return dp[m];
    }
}
```

## Python

```python
class Solution(object):
    def maxRemovals(self, source, pattern, targetIndices):
        """
        :type source: str
        :type pattern: str
        :type targetIndices: List[int]
        :rtype: int
        """
        n = len(source)
        m = len(pattern)
        removable = [False] * n
        for idx in targetIndices:
            removable[idx] = True

        NEG_INF = -10**9
        dp = [NEG_INF] * (m + 1)
        dp[0] = 0

        for i, ch in enumerate(source):
            ndp = [NEG_INF] * (m + 1)
            for j in range(m + 1):
                if dp[j] == NEG_INF:
                    continue
                # keep the character (skip it for pattern)
                if ndp[j] < dp[j]:
                    ndp[j] = dp[j]
                # use it to match next char of pattern
                if j < m and ch == pattern[j]:
                    if ndp[j + 1] < dp[j]:
                        ndp[j + 1] = dp[j]
                # delete if allowed
                if removable[i]:
                    if ndp[j] < dp[j] + 1:
                        ndp[j] = dp[j] + 1
            dp = ndp

        return dp[m]
```

## Python3

```python
from typing import List

class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        m = len(pattern)
        deletable = [False] * n
        for idx in targetIndices:
            deletable[idx] = True

        INF = 10 ** 9
        dp = [INF] * (m + 1)
        dp[0] = 0

        for i, ch in enumerate(source):
            cost = 1 if deletable[i] else 0
            for j in range(m, 0, -1):
                if ch == pattern[j - 1]:
                    cand = dp[j - 1] + cost
                    if cand < dp[j]:
                        dp[j] = cand

        min_needed = dp[m]
        return len(targetIndices) - min_needed
```

## C

```c
#include <string.h>
#include <stdbool.h>

int maxRemovals(char* source, char* pattern, int* targetIndices, int targetIndicesSize) {
    int n = strlen(source);
    int m = strlen(pattern);
    
    bool removable[3005] = {false};
    for (int i = 0; i < targetIndicesSize; ++i) {
        removable[targetIndices[i]] = true;
    }
    
    const int NEG = -1000000;
    static int dp[3005];
    static int ndp[3005];
    
    for (int j = 0; j <= m; ++j) dp[j] = NEG;
    dp[0] = 0;
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= m; ++j) ndp[j] = NEG;
        bool rem = removable[i];
        char c = source[i];
        for (int j = 0; j <= m; ++j) {
            if (dp[j] == NEG) continue;
            
            // keep character, stay at same matched length
            if (ndp[j] < dp[j]) ndp[j] = dp[j];
            
            // use character to match next pattern char
            if (j < m && c == pattern[j]) {
                if (ndp[j + 1] < dp[j]) ndp[j + 1] = dp[j];
            }
            
            // delete character if allowed
            if (rem) {
                if (ndp[j] < dp[j] + 1) ndp[j] = dp[j] + 1;
            }
        }
        for (int j = 0; j <= m; ++j) dp[j] = ndp[j];
    }
    
    return dp[m];
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxRemovals(string source, string pattern, int[] targetIndices)
    {
        int left = 0;
        int right = targetIndices.Length;

        while (left < right)
        {
            int mid = (left + right + 1) / 2; // try to remove 'mid' characters
            if (CanRemove(source, pattern, targetIndices, mid))
                left = mid;
            else
                right = mid - 1;
        }

        return left;
    }

    private bool CanRemove(string source, string pattern, int[] indices, int k)
    {
        var removed = new bool[source.Length];
        for (int i = 0; i < k; i++)
            removed[indices[i]] = true;

        int pIdx = 0;
        for (int sIdx = 0; sIdx < source.Length && pIdx < pattern.Length; sIdx++)
        {
            if (removed[sIdx])
                continue;
            if (source[sIdx] == pattern[pIdx])
                pIdx++;
        }

        return pIdx == pattern.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} source
 * @param {string} pattern
 * @param {number[]} targetIndices
 * @return {number}
 */
var maxRemovals = function(source, pattern, targetIndices) {
    const n = source.length;
    const m = pattern.length;
    const removableSet = new Set(targetIndices);
    
    const INF = 1e9;
    let prev = new Array(m + 1).fill(INF);
    prev[0] = 0; // empty pattern needs 0 removables
    
    for (let i = 1; i <= n; ++i) {
        const cur = new Array(m + 1).fill(INF);
        cur[0] = 0; // empty pattern
        const chS = source[i - 1];
        const isRemovable = removableSet.has(i - 1) ? 1 : 0;
        for (let j = 1; j <= m; ++j) {
            // skip current character
            cur[j] = Math.min(cur[j], prev[j]);
            // try to match if characters equal
            if (chS === pattern[j - 1]) {
                const cost = prev[j - 1] + isRemovable;
                if (cost < cur[j]) cur[j] = cost;
            }
        }
        prev = cur;
    }
    
    const minKept = prev[m]; // minimal number of removable chars that must stay
    const totalAllowed = targetIndices.length;
    return totalAllowed - minKept;
};
```

## Typescript

```typescript
function maxRemovals(source: string, pattern: string, targetIndices: number[]): number {
    const n = source.length;
    const m = pattern.length;
    const removable = new Set<number>(targetIndices);
    const INF = Number.MAX_SAFE_INTEGER >> 1; // sufficiently large
    const dp = new Array(m + 1).fill(INF);
    dp[0] = 0;

    for (let i = 0; i < n; ++i) {
        const cost = removable.has(i) ? 1 : 0;
        for (let j = m; j >= 1; --j) {
            if (source[i] === pattern[j - 1]) {
                const cand = dp[j - 1] + cost;
                if (cand < dp[j]) dp[j] = cand;
            }
        }
    }

    const minNeeded = dp[m];
    return targetIndices.length - minNeeded;
}
```

## Php

```php
class Solution {
    /**
     * @param String $source
     * @param String $pattern
     * @param Integer[] $targetIndices
     * @return Integer
     */
    function maxRemovals($source, $pattern, $targetIndices) {
        $n = strlen($source);
        $m = strlen($pattern);
        
        // mark removable positions
        $removable = array_fill(0, $n, false);
        foreach ($targetIndices as $idx) {
            $removable[$idx] = true;
        }
        
        $INF = 1 << 30;
        $prev = array_fill(0, $m + 1, $INF);
        $prev[0] = 0; // empty pattern needs no removals
        
        for ($i = 0; $i < $n; $i++) {
            $curr = $prev; // option: skip current character
            $cSource = $source[$i];
            $costIfUsed = $removable[$i] ? 1 : 0;
            
            // try to match pattern[j-1] with source[i]
            for ($j = 1; $j <= $m; $j++) {
                if ($cSource === $pattern[$j - 1]) {
                    $candidate = $prev[$j - 1] + $costIfUsed;
                    if ($candidate < $curr[$j]) {
                        $curr[$j] = $candidate;
                    }
                }
            }
            $prev = $curr;
        }
        
        $minUsedRemovable = $prev[$m];
        return count($targetIndices) - $minUsedRemovable;
    }
}
```

## Swift

```swift
class Solution {
    func maxRemovals(_ source: String, _ pattern: String, _ targetIndices: [Int]) -> Int {
        let n = source.count
        let p = pattern.count
        let srcArr = Array(source)
        let patArr = Array(pattern)
        var allowed = Set<Int>()
        for idx in targetIndices { allowed.insert(idx) }
        
        var dpPrev = Array(repeating: -1, count: p + 1)
        dpPrev[0] = 0
        var dpCurr = Array(repeating: -1, count: p + 1)
        
        for i in 0..<n {
            // reset current row
            for j in 0...p { dpCurr[j] = -1 }
            let ch = srcArr[i]
            for j in 0...p {
                let cur = dpPrev[j]
                if cur < 0 { continue }
                
                // keep character without matching pattern
                if dpCurr[j] < cur { dpCurr[j] = cur }
                
                // match current character to pattern
                if j < p && ch == patArr[j] {
                    if dpCurr[j + 1] < cur { dpCurr[j + 1] = cur }
                }
                
                // delete character if allowed
                if allowed.contains(i) {
                    let delVal = cur + 1
                    if dpCurr[j] < delVal { dpCurr[j] = delVal }
                }
            }
            swap(&dpPrev, &dpCurr)
        }
        
        return dpPrev[p]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxRemovals(source: String, pattern: String, targetIndices: IntArray): Int {
        val n = source.length
        val m = pattern.length
        val removable = BooleanArray(n)
        for (idx in targetIndices) {
            if (idx in 0 until n) removable[idx] = true
        }
        val INF = 1_000_000_000
        val dp = IntArray(m + 1) { INF }
        dp[0] = 0
        for (i in 0 until n) {
            val ch = source[i]
            var j = m
            while (j >= 1) {
                if (ch == pattern[j - 1]) {
                    val add = if (removable[i]) 1 else 0
                    val cand = dp[j - 1] + add
                    if (cand < dp[j]) dp[j] = cand
                }
                j--
            }
        }
        val minKept = dp[m]
        return targetIndices.size - minKept
    }
}
```

## Dart

```dart
class Solution {
  int maxRemovals(String source, String pattern, List<int> targetIndices) {
    int n = source.length;
    int m = pattern.length;

    // Mark removable positions
    List<bool> removable = List.filled(n, false);
    for (int idx in targetIndices) {
      removable[idx] = true;
    }

    const int INF = 1 << 30;

    // dp[i][j]: minimal number of removed characters used to match first i chars of pattern
    // using first j chars of source.
    List<List<int>> dp = List.generate(m + 1, (_) => List.filled(n + 1, INF));
    for (int j = 0; j <= n; ++j) {
      dp[0][j] = 0; // empty pattern needs no removals
    }

    for (int i = 1; i <= m; ++i) {
      int pChar = pattern.codeUnitAt(i - 1);
      for (int j = 1; j <= n; ++j) {
        // Option 1: skip source[j-1]
        int best = dp[i][j - 1];

        // Option 2: match if characters equal
        if (source.codeUnitAt(j - 1) == pChar && dp[i - 1][j - 1] != INF) {
          int cost = dp[i - 1][j - 1] + (removable[j - 1] ? 1 : 0);
          if (cost < best) best = cost;
        }

        dp[i][j] = best;
      }
    }

    int minRemovedInMatch = dp[m][n];
    return targetIndices.length - minRemovedInMatch;
  }
}
```

## Golang

```go
func maxRemovals(source string, pattern string, targetIndices []int) int {
	n := len(source)
	m := len(pattern)

	removable := make([]bool, n)
	for _, idx := range targetIndices {
		removable[idx] = true
	}

	const INF = int(1 << 30)
	dp := make([]int, m+1)
	for i := 1; i <= m; i++ {
		dp[i] = INF
	}
	// dp[0] is already 0

	for i := 0; i < n; i++ {
		ch := source[i]
		for j := m - 1; j >= 0; j-- {
			if dp[j] == INF {
				continue
			}
			if ch == pattern[j] {
				cost := dp[j]
				if removable[i] {
					cost++
				}
				if cost < dp[j+1] {
					dp[j+1] = cost
				}
			}
		}
	}

	minKept := dp[m]
	return len(targetIndices) - minKept
}
```

## Ruby

```ruby
def max_removals(source, pattern, target_indices)
  n = source.length
  m = pattern.length
  allowed = Array.new(n, false)
  target_indices.each { |idx| allowed[idx] = true }

  inf = 1 << 60

  prev = Array.new(n + 1, 0) # empty pattern matches with 0 kept deletable
  (1..m).each do |i|
    cur = Array.new(n + 1, inf)
    cur[0] = inf
    p_char = pattern[i - 1]
    (1..n).each do |j|
      best = cur[j - 1] # skip source[j-1]
      if source.getbyte(j - 1) == p_char.ord && prev[j - 1] != inf
        keep = prev[j - 1] + (allowed[j - 1] ? 1 : 0)
        best = keep if keep < best
      end
      cur[j] = best
    end
    prev = cur
  end

  min_kept = prev[n]
  target_indices.length - min_kept
end
```

## Scala

```scala
object Solution {
    def maxRemovals(source: String, pattern: String, targetIndices: Array[Int]): Int = {
        val n = source.length
        val m = pattern.length
        val removable = new Array[Boolean](n)
        for (idx <- targetIndices) removable(idx) = true

        val INF = 1_000_000
        val dp = Array.fill(m + 1)(INF)
        dp(0) = 0

        var j = 0
        while (j < n) {
            val cost = if (removable(j)) 1 else 0
            var i = m
            while (i >= 1) {
                if (source.charAt(j) == pattern.charAt(i - 1)) {
                    val cand = dp(i - 1) + cost
                    if (cand < dp(i)) dp(i) = cand
                }
                i -= 1
            }
            j += 1
        }

        val totalRemovable = targetIndices.length
        totalRemovable - dp(m)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_removals(source: String, pattern: String, target_indices: Vec<i32>) -> i32 {
        let n = source.len();
        let m = pattern.len();
        let s_bytes = source.as_bytes();
        let p_bytes = pattern.as_bytes();

        // mark which positions are in target_indices
        let mut is_target = vec![false; n];
        for &idx in &target_indices {
            is_target[idx as usize] = true;
        }

        const INF: i32 = 1_000_000_000;
        let mut dp_prev = vec![INF; m + 1];
        dp_prev[0] = 0;

        for i in 0..n {
            // start with the option of skipping current character
            let mut dp_cur = dp_prev.clone();
            let cost = if is_target[i] { 1 } else { 0 };
            let c = s_bytes[i];

            // try to use current character to match pattern[j-1]
            for j in (1..=m).rev() {
                if c == p_bytes[j - 1] && dp_prev[j - 1] != INF {
                    let val = dp_prev[j - 1] + cost;
                    if val < dp_cur[j] {
                        dp_cur[j] = val;
                    }
                }
            }

            dp_prev = dp_cur;
        }

        let min_kept = dp_prev[m];
        let total_target = target_indices.len() as i32;
        total_target - min_kept
    }
}
```

## Racket

```racket
(define/contract (max-removals source pattern targetIndices)
  (-> string? string? (listof exact-integer?) exact-integer?)
  (let* ((n (string-length source))
         (m (string-length pattern))
         (removable (make-vector n #f)))
    (for ([idx targetIndices])
      (vector-set! removable idx #t))
    (define INF 1000000)
    (define dpPrev (make-vector n 0)) ; empty pattern costs 0
    (let loop-i ((i 0) (dpPrev dpPrev))
      (if (= i m)
          (let ((min-kept (vector-ref dpPrev (- n 1))))
            (- (length targetIndices) min-kept))
          (let ((dpCurr (make-vector n INF)))
            (for ([j (in-range n)])
              ;; try to match pattern[i] at position j
              (when (char=? (string-ref source j)
                            (string-ref pattern i))
                (define prev
                  (if (= j 0)
                      (if (= i 0) 0 INF)
                      (vector-ref dpPrev (- j 1))))
                (when (< prev INF)
                  (define cand (+ prev (if (vector-ref removable j) 1 0)))
                  (when (< cand (vector-ref dpCurr j))
                    (vector-set! dpCurr j cand))))
              ;; propagate minimum from the left
              (when (> j 0)
                (define left (vector-ref dpCurr (- j 1)))
                (when (< left (vector-ref dpCurr j))
                  (vector-set! dpCurr j left))))
            (loop-i (+ i 1) dpCurr))))))
```

## Erlang

```erlang
-module(solution).
-export([max_removals/3]).

-spec max_removals(Source :: unicode:unicode_binary(),
                   Pattern :: unicode:unicode_binary(),
                   TargetIndices :: [integer()]) -> integer().
max_removals(Source, Pattern, TargetIndices) ->
    SourceList = string:to_charlist(Source),
    PatternList = string:to_charlist(Pattern),
    M = length(PatternList),
    PatternTuple = list_to_tuple(PatternList),
    TargetSet = maps:from_keys(TargetIndices, true),
    Inf = 1 bsl 30,
    DP0 = #{0 => 0},
    FinalDP = process(SourceList, 0, M, PatternTuple, TargetSet, Inf, DP0),
    MinUsed = maps:get(M, FinalDP, Inf),
    length(TargetIndices) - MinUsed.

process([], _Idx, _M, _PatternTuple, _TargetSet, _Inf, DP) ->
    DP;
process([C|Rest], Idx, M, PatternTuple, TargetSet, Inf, DP) ->
    IsTarget = case maps:is_key(Idx, TargetSet) of
        true -> 1;
        false -> 0
    end,
    NewDP = update_dp(M, C, PatternTuple, IsTarget, Inf, DP),
    process(Rest, Idx + 1, M, PatternTuple, TargetSet, Inf, NewDP).

update_dp(0, _C, _PatternTuple, _IsTarget, _Inf, DP) ->
    DP;
update_dp(J, C, PatternTuple, IsTarget, Inf, DP) when J > 0 ->
    PatChar = element(J, PatternTuple),
    DP1 = if C == PatChar ->
            PrevCost = maps:get(J-1, DP, Inf),
            NewCost = PrevCost + IsTarget,
            OldCost = maps:get(J, DP, Inf),
            UpdatedCost = erlang:min(OldCost, NewCost),
            case UpdatedCost < OldCost of
                true -> maps:put(J, UpdatedCost, DP);
                false -> DP
            end;
          true ->
            DP
        end,
    update_dp(J-1, C, PatternTuple, IsTarget, Inf, DP1).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_removals(source :: String.t, pattern :: String.t, target_indices :: [integer]) :: integer
  def max_removals(source, pattern, target_indices) do
    total_targets = length(target_indices)
    target_set = MapSet.new(target_indices)

    source_chars = String.to_charlist(source)
    pattern_chars = String.to_charlist(pattern)
    m = length(pattern_chars)

    sentinel = 1_000_000

    dp = :array.new(m + 1, sentinel) |> :array.set(0, 0)
    pattern_arr = :array.from_list(pattern_chars)

    final_dp =
      Enum.with_index(source_chars)
      |> Enum.reduce(dp, fn {c, idx}, acc_dp ->
        Enum.reduce(m..1, acc_dp, fn j, dp2 ->
          pat_c = :array.get(j - 1, pattern_arr)

          if c == pat_c do
            prev = :array.get(j - 1, dp2)
            add = if MapSet.member?(target_set, idx), do: 1, else: 0
            cur = :array.get(j, dp2)
            new_val = min(cur, prev + add)
            :array.set(j, new_val, dp2)
          else
            dp2
          end
        end)
      end)

    min_kept = :array.get(m, final_dp)
    total_targets - min_kept
  end
end
```
