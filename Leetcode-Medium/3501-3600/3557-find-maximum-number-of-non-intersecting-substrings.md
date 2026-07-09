# 3557. Find Maximum Number of Non Intersecting Substrings

## Cpp

```cpp
class Solution {
public:
    int maxSubstrings(string word) {
        int n = word.size();
        vector<int> dp(n, 0);
        vector<vector<int>> occ(26);
        vector<int> ptr(26, 0);
        
        for (int i = 0; i < n; ++i) {
            // default: not taking a substring ending at i
            dp[i] = (i > 0 ? dp[i - 1] : 0);
            
            int c = word[i] - 'a';
            // advance pointer to make all occurrences <= i-3 eligible
            while (ptr[c] < (int)occ[c].size() && occ[c][ptr[c]] <= i - 3) {
                ++ptr[c];
            }
            if (!occ[c].empty() && ptr[c] > 0) {
                int startIdx = occ[c][ptr[c] - 1]; // latest eligible start
                int prev = (startIdx == 0 ? 0 : dp[startIdx - 1]);
                dp[i] = max(dp[i], prev + 1);
            }
            
            occ[c].push_back(i);
        }
        return n ? dp[n - 1] : 0;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxSubstrings(String word) {
        int n = word.length();
        int[] dp = new int[n + 1];
        int[] best = new int[26];
        Arrays.fill(best, Integer.MIN_VALUE / 2);
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i];
            if (i >= 3) {
                int chPrev = word.charAt(i - 3) - 'a';
                best[chPrev] = Math.max(best[chPrev], dp[i - 3]);
            }
            int c = word.charAt(i) - 'a';
            if (best[c] > Integer.MIN_VALUE / 2) {
                dp[i + 1] = Math.max(dp[i + 1], best[c] + 1);
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def maxSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        last_pos = {}
        ans = 0
        last_end = -1
        for i, ch in enumerate(word):
            if ch in last_pos:
                start = last_pos[ch]
                if i - start >= 3 and start > last_end:
                    ans += 1
                    last_end = i
            last_pos[ch] = i
        return ans
```

## Python3

```python
class Solution:
    def maxSubstrings(self, word: str) -> int:
        from collections import defaultdict
        import bisect

        pos = defaultdict(list)
        for i, ch in enumerate(word):
            pos[ch].append(i)

        last_end = -1
        ans = 0
        for i, ch in enumerate(word):
            arr = pos[ch]
            idx = bisect.bisect_right(arr, i - 3) - 1
            if idx >= 0:
                j = arr[idx]
                if j > last_end:
                    ans += 1
                    last_end = i
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int maxSubstrings(char* word) {
    int n = strlen(word);
    vector<int> pos[26];
    for (int i = 0; i < n; ++i) {
        pos[word[i] - 'a'].push_back(i);
    }
    vector<int> dp(n, 0);
    for (int i = 0; i < n; ++i) {
        if (i > 0) dp[i] = dp[i - 1];
        int idx = word[i] - 'a';
        const auto& v = pos[idx];
        int target = i - 3;
        auto it = upper_bound(v.begin(), v.end(), target);
        if (it != v.begin()) {
            --it;
            int j = *it; // start index of substring
            int cand = (j > 0 ? dp[j - 1] : 0) + 1;
            if (cand > dp[i]) dp[i] = cand;
        }
    }
    return dp.empty() ? 0 : dp.back();
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSubstrings(string word) {
        int n = word.Length;
        if (n == 0) return 0;
        int[] dp = new int[n];
        int[] bestPos = new int[26];
        for (int i = 0; i < 26; i++) bestPos[i] = -1;

        for (int i = 0; i < n; i++) {
            if (i >= 3) {
                int idxPrev = word[i - 3] - 'a';
                bestPos[idxPrev] = i - 3;
            }

            int cur = i > 0 ? dp[i - 1] : 0;
            int cIdx = word[i] - 'a';
            int start = bestPos[cIdx];
            if (start != -1) {
                int prev = start == 0 ? 0 : dp[start - 1];
                cur = Math.Max(cur, prev + 1);
            }
            dp[i] = cur;
        }

        return dp[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var maxSubstrings = function(word) {
    const pos = Array.from({length: 26}, () => []);
    for (let i = 0; i < word.length; ++i) {
        pos[word.charCodeAt(i) - 97].push(i);
    }
    const intervals = [];
    for (const arr of pos) {
        if (arr.length === 0) continue;
        for (let idx = 0; idx < arr.length; ++idx) {
            const end = arr[idx];
            const target = end - 3; // need start <= target
            let l = 0, r = idx - 1, best = -1;
            while (l <= r) {
                const m = (l + r) >> 1;
                if (arr[m] <= target) {
                    best = m;
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            if (best !== -1) {
                intervals.push({ start: arr[best], end });
            }
        }
    }
    intervals.sort((a, b) => {
        if (a.end !== b.end) return a.end - b.end;
        return b.start - a.start; // shorter interval first when ends equal
    });
    let count = 0;
    let lastEnd = -1;
    for (const iv of intervals) {
        if (iv.start > lastEnd) {
            ++count;
            lastEnd = iv.end;
        }
    }
    return count;
};
```

## Typescript

```typescript
function maxSubstrings(word: string): number {
    const n = word.length;
    const pending: { charIdx: number; val: number }[][] = Array.from({ length: n }, () => []);
    const INF_NEG = -1e9;
    const latestDP = new Int32Array(26);
    for (let i = 0; i < 26; ++i) latestDP[i] = INF_NEG;

    let dpPrev = 0; // dp value for prefix ending at i-1
    for (let i = 0; i < n; ++i) {
        // Apply pending updates that become eligible at position i
        const list = pending[i];
        for (const item of list) {
            if (item.val > latestDP[item.charIdx]) latestDP[item.charIdx] = item.val;
        }

        const idx = word.charCodeAt(i) - 97;
        let cand = INF_NEG;
        if (latestDP[idx] !== INF_NEG) {
            cand = latestDP[idx] + 1;
        }
        const dpCurr = Math.max(dpPrev, cand);

        // This position can serve as a start for future substrings after distance >=3
        const readyPos = i + 3;
        if (readyPos < n) {
            pending[readyPos].push({ charIdx: idx, val: dpPrev });
        }

        dpPrev = dpCurr;
    }
    return dpPrev;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function maxSubstrings($word) {
        $n = strlen($word);
        $dp = array_fill(0, $n + 1, 0);
        $best = array_fill(0, 26, -1); // best dp value for each character when start is at least 3 positions before current

        for ($i = 0; $i < $n; $i++) {
            // make position i-3 eligible as a possible start
            $eligiblePos = $i - 3;
            if ($eligiblePos >= 0) {
                $cIdx2 = ord($word[$eligiblePos]) - 97;
                $val = $dp[$eligiblePos];
                if ($val > $best[$cIdx2]) {
                    $best[$cIdx2] = $val;
                }
            }

            // default: inherit previous best count
            $dp[$i + 1] = $dp[$i];

            // try to end a substring at i
            $cIdx = ord($word[$i]) - 97;
            if ($best[$cIdx] != -1) {
                $candidate = $best[$cIdx] + 1;
                if ($candidate > $dp[$i + 1]) {
                    $dp[$i + 1] = $candidate;
                }
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func maxSubstrings(_ word: String) -> Int {
        let chars = Array(word.utf8)
        let n = chars.count
        if n < 4 { return 0 }
        
        var positions = [[Int]](repeating: [], count: 26)
        for i in 0..<n {
            let idx = Int(chars[i] - 97) // 'a' ascii is 97
            positions[idx].append(i)
        }
        
        var intervals = [(start: Int, end: Int)]()
        intervals.reserveCapacity(n)
        
        for list in positions {
            let m = list.count
            if m < 2 { continue }
            for iIdx in 0..<m {
                let endPos = list[iIdx]
                // binary search for the latest start <= endPos - 3
                var left = 0
                var right = iIdx - 1
                var best = -1
                while left <= right {
                    let mid = (left + right) >> 1
                    if list[mid] <= endPos - 3 {
                        best = mid
                        left = mid + 1
                    } else {
                        right = mid - 1
                    }
                }
                if best != -1 {
                    intervals.append((list[best], endPos))
                }
            }
        }
        
        intervals.sort { $0.end < $1.end }
        
        var count = 0
        var lastEnd = -1
        for interval in intervals {
            if interval.start > lastEnd {
                count += 1
                lastEnd = interval.end
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubstrings(word: String): Int {
        val n = word.length
        if (n < 4) return 0
        val occ = Array(26) { mutableListOf<Int>() }
        val dp = IntArray(n)
        for (i in 0 until n) {
            val cIdx = word[i] - 'a'
            var cand = 0
            val list = occ[cIdx]
            if (list.isNotEmpty()) {
                // find rightmost index <= i-3
                var l = 0
                var r = list.size - 1
                var pos = -1
                while (l <= r) {
                    val m = (l + r) ushr 1
                    if (list[m] <= i - 3) {
                        pos = m
                        l = m + 1
                    } else {
                        r = m - 1
                    }
                }
                if (pos != -1) {
                    val j = list[pos]
                    cand = (if (j > 0) dp[j - 1] else 0) + 1
                }
            }
            dp[i] = if (i == 0) cand else kotlin.math.max(dp[i - 1], cand)
            occ[cIdx].add(i)
        }
        return dp[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int maxSubstrings(String word) {
    int n = word.length;
    List<List<int>> occ = List.generate(26, (_) => []);
    for (int i = 0; i < n; i++) {
      int c = word.codeUnitAt(i) - 97;
      occ[c].add(i);
    }

    List<int> bestStart = List.filled(n, -1);
    for (var list in occ) {
      int m = list.length;
      for (int pos = 0; pos < m; pos++) {
        int endIdx = list[pos];
        int lo = 0, hi = pos - 1, ans = -1;
        while (lo <= hi) {
          int mid = (lo + hi) >> 1;
          if (endIdx - list[mid] >= 3) {
            ans = list[mid];
            lo = mid + 1; // try to find a later start
          } else {
            hi = mid - 1;
          }
        }
        if (ans != -1) bestStart[endIdx] = ans;
      }
    }

    List<int> dp = List.filled(n + 1, 0);
    for (int i = 1; i <= n; i++) {
      dp[i] = dp[i - 1];
      int start = bestStart[i - 1];
      if (start != -1) {
        int cand = dp[start] + 1;
        if (cand > dp[i]) dp[i] = cand;
      }
    }
    return dp[n];
  }
}
```

## Golang

```go
func maxSubstrings(word string) int {
    n := len(word)
    if n == 0 {
        return 0
    }
    dp := make([]int, n)
    firstIdx := make([]int, 26)
    best := make([]int, 26)
    for i := 0; i < 26; i++ {
        firstIdx[i] = -1
        best[i] = -1
    }

    for i := 0; i < n; i++ {
        c := word[i] - 'a'

        // candidate using a previous occurrence of the same character
        cand := -1
        if firstIdx[c] != -1 && i-firstIdx[c] >= 3 && best[c] != -1 {
            cand = best[c] + 1
        }

        if i > 0 {
            dp[i] = dp[i-1]
        } else {
            dp[i] = 0
        }
        if cand > dp[i] {
            dp[i] = cand
        }

        // update first occurrence index
        if firstIdx[c] == -1 {
            firstIdx[c] = i
        }

        // store max dp before this position for future intervals
        prev := 0
        if i > 0 {
            prev = dp[i-1]
        }
        if prev > best[c] {
            best[c] = prev
        }
    }
    return dp[n-1]
}
```

## Ruby

```ruby
def max_substrings(word)
  n = word.length
  return 0 if n < 4

  dp = Array.new(n, 0)
  last = Array.new(26, nil)

  (0...n).each do |i|
    dp[i] = i > 0 ? dp[i - 1] : 0
    idx = word.getbyte(i) - 97
    prev = last[idx]
    if !prev.nil? && i - prev >= 3
      before = prev > 0 ? dp[prev - 1] : 0
      cand = before + 1
      dp[i] = cand if cand > dp[i]
    end
    last[idx] = i
  end

  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def maxSubstrings(word: String): Int = {
        val n = word.length
        val dp = new Array[Int](n + 1)
        val best = Array.fill(26)(Int.MinValue)

        var i = 0
        while (i < n) {
            // inherit previous value
            dp(i + 1) = dp(i)

            // make position i-3 eligible as a start
            val eligibleIdx = i - 3
            if (eligibleIdx >= 0) {
                val chIdx = word.charAt(eligibleIdx) - 'a'
                best(chIdx) = math.max(best(chIdx), dp(eligibleIdx))
            }

            // try to end a substring at i
            val cIdx = word.charAt(i) - 'a'
            if (best(cIdx) != Int.MinValue) {
                dp(i + 1) = math.max(dp(i + 1), best(cIdx) + 1)
            }

            i += 1
        }
        dp(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_substrings(word: String) -> i32 {
        let bytes = word.as_bytes();
        let mut pos: Vec<Vec<usize>> = vec![Vec::new(); 26];
        for (i, &b) in bytes.iter().enumerate() {
            pos[(b - b'a') as usize].push(i);
        }

        let mut intervals: Vec<(usize, usize)> = Vec::new();

        for v in pos.iter() {
            let m = v.len();
            if m < 2 {
                continue;
            }
            for i in 0..m {
                // need first j > i with v[j] - v[i] >= 3
                let target = v[i] + 3;
                let mut lo = i + 1;
                let mut hi = m;
                while lo < hi {
                    let mid = (lo + hi) / 2;
                    if v[mid] < target {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                if lo < m {
                    intervals.push((v[i], v[lo]));
                }
            }
        }

        intervals.sort_by(|a, b| {
            if a.1 == b.1 {
                a.0.cmp(&b.0)
            } else {
                a.1.cmp(&b.1)
            }
        });

        let mut count = 0;
        let mut last_end: isize = -1;
        for (l, r) in intervals {
            if (l as isize) > last_end {
                count += 1;
                last_end = r as isize;
            }
        }

        count as i32
    }
}
```

## Racket

```racket
(define/contract (max-substrings word)
  (-> string? exact-integer?)
  (let* ([n (string-length word)]
         [dp (make-vector (+ n 1) 0)]
         [last (make-vector 26 -1)])
    (for ([i (in-range n)])
      (define ch-index (- (char->integer (string-ref word i))
                          (char->integer #\a)))
      (define last-pos (vector-ref last ch-index))
      (define candidate
        (if (and (>= last-pos 0) (>= (- i last-pos) 3))
            (+ (vector-ref dp last-pos) 1)
            -1))
      (vector-set! dp (+ i 1)
                   (max (vector-ref dp i) candidate))
      (vector-set! last ch-index i))
    (vector-ref dp n)))
```

## Erlang

```erlang
-spec max_substrings(Word :: unicode:unicode_binary()) -> integer().
max_substrings(Word) ->
    N = byte_size(Word),
    DP0 = array:new(N + 1, {default, 0}),
    Best0 = lists:duplicate(26, -1),
    loop(0, N, Word, DP0, Best0).

loop(I, N, _Word, DPArr, _Best) when I == N ->
    array:get(N, DPArr);
loop(I, N, Word, DPArr, Best) ->
    PrevDP = array:get(I, DPArr),
    CharCode = binary:at(Word, I) - $a,
    BestVal = lists:nth(CharCode + 1, Best),
    Candidate = case BestVal of
        B when B >= 0 -> B + 1;
        _ -> -1
    end,
    CurrDP = erlang:max(PrevDP, Candidate),
    DPArr2 = array:set(I + 1, CurrDP, DPArr),

    AddIdx = I - 2,
    Best2 = if
        AddIdx >= 0 ->
            StartCharCode = binary:at(Word, AddIdx) - $a,
            StartDP = array:get(AddIdx, DPArr),
            OldBest = lists:nth(StartCharCode + 1, Best),
            NewBest = erlang:max(OldBest, StartDP),
            lists:replace_at(StartCharCode + 1, NewBest, Best);
        true ->
            Best
    end,
    loop(I + 1, N, Word, DPArr2, Best2).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_substrings(String.t()) :: integer
  def max_substrings(word) do
    chars = String.to_charlist(word)
    n = length(chars)

    # positions of each character in ascending order, stored as :array
    pos_map =
      Enum.with_index(chars)
      |> Enum.reduce(%{}, fn {c, idx}, acc ->
        key = c - ?a
        Map.update(acc, key, [idx], fn lst -> [idx | lst] end)
      end)
      |> Enum.map(fn {k, lst} -> {k, :array.from_list(Enum.reverse(lst))} end)
      |> Map.new()

    dp = :array.new(n + 1, default: 0)
    ptr_map = %{}

    {dp_final, _} =
      Enum.reduce(0..(n - 1), {dp, ptr_map}, fn i, {dp_arr, pmap} ->
        c = Enum.at(chars, i)
        key = c - ?a
        positions_arr = Map.get(pos_map, key)

        # current pointer for this character
        ptr = Map.get(pmap, key, -1)
        limit = i - 3

        new_ptr =
          if limit >= 0 do
            advance_ptr(positions_arr, ptr, limit)
          else
            ptr
          end

        pmap = Map.put(pmap, key, new_ptr)

        dp_i = :array.get(i, dp_arr)
        best = max(dp_i, :array.get(i + 1, dp_arr))

        if new_ptr >= 0 do
          j = :array.get(new_ptr, positions_arr)
          candidate = :array.get(j, dp_arr) + 1
          best = max(best, candidate)
        end

        dp_arr = :array.set(i + 1, best, dp_arr)
        {dp_arr, pmap}
      end)

    :array.get(n, dp_final)
  end

  defp advance_ptr(arr, ptr, limit) do
    size = :array.size(arr)

    cond do
      ptr + 1 < size ->
        pos = :array.get(ptr + 1, arr)

        if pos <= limit do
          advance_ptr(arr, ptr + 1, limit)
        else
          ptr
        end

      true ->
        ptr
    end
  end
end
```
