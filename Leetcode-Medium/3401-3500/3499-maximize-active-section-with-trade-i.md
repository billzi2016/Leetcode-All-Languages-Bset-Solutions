# 3499. Maximize Active Section with Trade I

## Cpp

```cpp
class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int n = s.size();
        long long totalOnes = 0;
        vector<int> runLen;
        vector<char> runChar; // '0' or '1'
        for (int i = 0; i < n; ) {
            char c = s[i];
            int j = i;
            while (j < n && s[j] == c) ++j;
            int len = j - i;
            runLen.push_back(len);
            runChar.push_back(c);
            if (c == '1') totalOnes += len;
            i = j;
        }
        long long bestDelta = 0;
        for (int idx = 0; idx < (int)runChar.size(); ++idx) {
            if (runChar[idx] != '1') continue;
            // need zero runs on both sides
            if (idx == 0 || idx + 1 >= (int)runChar.size()) continue;
            if (runChar[idx-1] != '0' || runChar[idx+1] != '0') continue;
            long long delta = (long long)runLen[idx-1] + (long long)runLen[idx+1];
            if (delta > bestDelta) bestDelta = delta;
        }
        return (int)(totalOnes + bestDelta);
    }
};
```

## Java

```java
class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        int n = s.length();
        int totalOnes = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') totalOnes++;
        }

        // Build run-length encoding
        java.util.ArrayList<Integer> lengths = new java.util.ArrayList<>();
        java.util.ArrayList<Character> chars = new java.util.ArrayList<>();

        int i = 0;
        while (i < n) {
            char c = s.charAt(i);
            int j = i;
            while (j < n && s.charAt(j) == c) j++;
            lengths.add(j - i);
            chars.add(c);
            i = j;
        }

        int maxDelta = 0;
        for (int k = 0; k < chars.size(); k++) {
            if (chars.get(k) == '1') {
                // need zero runs on both sides
                if (k > 0 && k + 1 < chars.size()
                        && chars.get(k - 1) == '0' && chars.get(k + 1) == '0') {
                    int delta = lengths.get(k - 1) + lengths.get(k + 1);
                    if (delta > maxDelta) maxDelta = delta;
                }
            }
        }

        return totalOnes + maxDelta;
    }
}
```

## Python

```python
class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total_ones = s.count('1')
        # Build segments of consecutive characters
        seg_chars = []
        seg_lens = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            seg_chars.append(s[i])
            seg_lens.append(j - i)
            i = j

        max_delta = 0
        m = len(seg_chars)
        for idx in range(m):
            if seg_chars[idx] != '1':
                continue
            # need zero segment on both sides
            left_len = seg_lens[idx - 1] if idx > 0 and seg_chars[idx - 1] == '0' else 0
            right_len = seg_lens[idx + 1] if idx + 1 < m and seg_chars[idx + 1] == '0' else 0
            if left_len > 0 and right_len > 0:
                max_delta = max(max_delta, left_len + right_len)

        return total_ones + max_delta
```

## Python3

```python
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        total_ones = s.count('1')
        # Build runs of consecutive characters
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        max_delta = 0
        m = len(runs)
        for k in range(1, m - 1):
            if runs[k][0] == '1' and runs[k - 1][0] == '0' and runs[k + 1][0] == '0':
                delta = runs[k - 1][1] + runs[k + 1][1]
                if delta > max_delta:
                    max_delta = delta

        return total_ones + max_delta
```

## C

```c
int maxActiveSectionsAfterTrade(char* s) {
    int totalOnes = 0;
    int maxDelta = 0;
    int n = 0;
    while (s[n]) ++n;

    int i = 0;
    while (i < n) {
        // zeros to the left of a ones block
        int leftZero = 0;
        while (i < n && s[i] == '0') {
            ++leftZero;
            ++i;
        }
        if (i >= n) break; // no more ones

        // count the ones in this block
        while (i < n && s[i] == '1') {
            ++totalOnes;
            ++i;
        }

        // zeros to the right of this ones block
        int rightZero = 0;
        int j = i;
        while (j < n && s[j] == '0') {
            ++rightZero;
            ++j;
        }

        if (leftZero > 0 && rightZero > 0) {
            int delta = leftZero + rightZero;
            if (delta > maxDelta) maxDelta = delta;
        }

        i = j; // move to the next segment
    }

    return totalOnes + maxDelta;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxActiveSectionsAfterTrade(string s)
    {
        int n = s.Length;
        long totalOnes = 0;
        var zeroRuns = new System.Collections.Generic.List<int>();
        int i = 0;

        // Leading zeros (or zero length if string starts with '1')
        if (i < n && s[i] == '0')
        {
            int cnt = 0;
            while (i < n && s[i] == '0')
            {
                cnt++;
                i++;
            }
            zeroRuns.Add(cnt);
        }
        else
        {
            zeroRuns.Add(0);
        }

        // Process remaining segments
        while (i < n)
        {
            int onesCnt = 0;
            while (i < n && s[i] == '1')
            {
                onesCnt++;
                i++;
            }
            totalOnes += onesCnt;

            int zerosCnt = 0;
            while (i < n && s[i] == '0')
            {
                zerosCnt++;
                i++;
            }
            zeroRuns.Add(zerosCnt);
        }

        int maxDelta = 0;
        for (int idx = 0; idx + 1 < zeroRuns.Count; idx++)
        {
            int left = zeroRuns[idx];
            int right = zeroRuns[idx + 1];
            if (left > 0 && right > 0)
            {
                int delta = left + right;
                if (delta > maxDelta) maxDelta = delta;
            }
        }

        return (int)(totalOnes + maxDelta);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxActiveSectionsAfterTrade = function(s) {
    const n = s.length;
    let totalOnes = 0;
    for (let ch of s) if (ch === '1') totalOnes++;
    
    // Build runs of consecutive characters
    const runs = [];
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        runs.push({c: s[i], l: j - i});
        i = j;
    }
    
    let maxDelta = 0;
    for (let k = 1; k + 1 < runs.length; ++k) {
        if (runs[k].c === '1' && runs[k-1].c === '0' && runs[k+1].c === '0') {
            const delta = runs[k-1].l + runs[k+1].l;
            if (delta > maxDelta) maxDelta = delta;
        }
    }
    
    return totalOnes + maxDelta;
};
```

## Typescript

```typescript
function maxActiveSectionsAfterTrade(s: string): number {
    let totalOnes = 0;
    const runsChar: string[] = [];
    const runsLen: number[] = [];

    for (let i = 0; i < s.length;) {
        const ch = s[i];
        let j = i;
        while (j < s.length && s[j] === ch) j++;
        const len = j - i;
        runsChar.push(ch);
        runsLen.push(len);
        if (ch === '1') totalOnes += len;
        i = j;
    }

    let maxDelta = 0;
    for (let idx = 0; idx < runsChar.length; idx++) {
        if (runsChar[idx] === '1' && idx > 0 && idx + 1 < runsChar.length &&
            runsChar[idx - 1] === '0' && runsChar[idx + 1] === '0') {
            const delta = runsLen[idx - 1] + runsLen[idx + 1];
            if (delta > maxDelta) maxDelta = delta;
        }
    }

    return totalOnes + maxDelta;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxActiveSectionsAfterTrade($s) {
        $n = strlen($s);
        $segments = [];
        $i = 0;
        while ($i < $n) {
            $ch = $s[$i];
            $len = 0;
            while ($i < $n && $s[$i] === $ch) {
                $len++;
                $i++;
            }
            $segments[] = [$ch, $len];
        }

        $totalOnes = 0;
        $maxDelta = 0;
        $m = count($segments);
        for ($idx = 0; $idx < $m; $idx++) {
            if ($segments[$idx][0] === '1') {
                $totalOnes += $segments[$idx][1];
                if ($idx - 1 >= 0 && $idx + 1 < $m &&
                    $segments[$idx - 1][0] === '0' && $segments[$idx + 1][0] === '0') {
                    $delta = $segments[$idx - 1][1] + $segments[$idx + 1][1];
                    if ($delta > $maxDelta) {
                        $maxDelta = $delta;
                    }
                }
            }
        }

        return $totalOnes + $maxDelta;
    }
}
```

## Swift

```swift
class Solution {
    func maxActiveSectionsAfterTrade(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var i = 0
        var totalOnes = 0
        var maxDelta = 0
        var leftZeros = 0
        
        while i < n {
            if chars[i] == "0" {
                var cnt = 0
                while i < n && chars[i] == "0" {
                    cnt += 1
                    i += 1
                }
                leftZeros = cnt
            } else { // '1'
                var oneCnt = 0
                while i < n && chars[i] == "1" {
                    oneCnt += 1
                    i += 1
                }
                totalOnes += oneCnt
                
                var rightZeros = 0
                var j = i
                while j < n && chars[j] == "0" {
                    rightZeros += 1
                    j += 1
                }
                
                if leftZeros > 0 && rightZeros > 0 {
                    maxDelta = max(maxDelta, leftZeros + rightZeros)
                }
                
                leftZeros = rightZeros
                i = j
            }
        }
        
        return totalOnes + maxDelta
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxActiveSectionsAfterTrade(s: String): Int {
        val n = s.length
        var totalOnes = 0
        val runChars = mutableListOf<Char>()
        val runLengths = mutableListOf<Int>()
        var i = 0
        while (i < n) {
            val c = s[i]
            var j = i
            while (j < n && s[j] == c) j++
            val len = j - i
            runChars.add(c)
            runLengths.add(len)
            if (c == '1') totalOnes += len
            i = j
        }
        var maxDelta = 0
        for (idx in runChars.indices) {
            if (runChars[idx] == '1' && idx > 0 && idx + 1 < runChars.size &&
                runChars[idx - 1] == '0' && runChars[idx + 1] == '0') {
                val delta = runLengths[idx - 1] + runLengths[idx + 1]
                if (delta > maxDelta) maxDelta = delta
            }
        }
        return totalOnes + maxDelta
    }
}
```

## Dart

```dart
class Solution {
  int maxActiveSectionsAfterTrade(String s) {
    int totalOnes = 0;
    List<int> segLen = [];
    List<int> segType = []; // 0 for zero, 1 for one

    int i = 0;
    while (i < s.length) {
      int j = i;
      while (j < s.length && s[j] == s[i]) {
        j++;
      }
      int len = j - i;
      segLen.add(len);
      if (s[i] == '0') {
        segType.add(0);
      } else {
        segType.add(1);
        totalOnes += len;
      }
      i = j;
    }

    int maxDelta = 0;
    for (int idx = 0; idx < segLen.length; idx++) {
      if (segType[idx] == 1) {
        if (idx - 1 >= 0 &&
            idx + 1 < segLen.length &&
            segType[idx - 1] == 0 &&
            segType[idx + 1] == 0) {
          int delta = segLen[idx - 1] + segLen[idx + 1];
          if (delta > maxDelta) maxDelta = delta;
        }
      }
    }

    return totalOnes + maxDelta;
  }
}
```

## Golang

```go
func maxActiveSectionsAfterTrade(s string) int {
    n := len(s)
    if n == 0 {
        return 0
    }

    // Build runs of consecutive characters.
    type run struct {
        ch byte
        cnt int
    }
    runs := make([]run, 0, n)

    i := 0
    for i < n {
        j := i + 1
        for j < n && s[j] == s[i] {
            j++
        }
        runs = append(runs, run{ch: s[i], cnt: j - i})
        i = j
    }

    totalOnes := 0
    for _, r := range runs {
        if r.ch == '1' {
            totalOnes += r.cnt
        }
    }

    maxDelta := 0
    // For each one-run that has zero-runs on both sides.
    for idx, r := range runs {
        if r.ch != '1' {
            continue
        }
        if idx > 0 && idx+1 < len(runs) &&
            runs[idx-1].ch == '0' && runs[idx+1].ch == '0' {
            delta := runs[idx-1].cnt + runs[idx+1].cnt
            if delta > maxDelta {
                maxDelta = delta
            }
        }
    }

    return totalOnes + maxDelta
}
```

## Ruby

```ruby
def max_active_sections_after_trade(s)
  n = s.length
  segs = []
  i = 0
  while i < n
    ch = s[i]
    j = i + 1
    j += 1 while j < n && s[j] == ch
    segs << [ch, j - i]
    i = j
  end

  total_ones = 0
  max_delta = 0

  segs.each_with_index do |(c, len), idx|
    if c == '1'
      total_ones += len
      if idx > 0 && idx + 1 < segs.size &&
         segs[idx - 1][0] == '0' && segs[idx + 1][0] == '0'
        delta = segs[idx - 1][1] + segs[idx + 1][1]
        max_delta = delta if delta > max_delta
      end
    end
  end

  total_ones + max_delta
end
```

## Scala

```scala
object Solution {
    def maxActiveSectionsAfterTrade(s: String): Int = {
        var totalOnes = 0
        var maxDelta = 0
        val n = s.length
        val chars = scala.collection.mutable.ArrayBuffer[Char]()
        val lens = scala.collection.mutable.ArrayBuffer[Int]()

        var i = 0
        while (i < n) {
            val c = s.charAt(i)
            var j = i
            while (j < n && s.charAt(j) == c) j += 1
            val len = j - i
            chars += c
            lens += len
            if (c == '1') totalOnes += len
            i = j
        }

        for (k <- 0 until chars.length) {
            if (chars(k) == '1' && k > 0 && k + 1 < chars.length &&
                chars(k - 1) == '0' && chars(k + 1) == '0') {
                val delta = lens(k - 1) + lens(k + 1)
                if (delta > maxDelta) maxDelta = delta
            }
        }

        totalOnes + maxDelta
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_active_sections_after_trade(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        // Build runs of consecutive characters
        let mut runs: Vec<(bool, usize)> = Vec::new(); // (is_one, length)
        let mut i = 0;
        while i < n {
            let cur = bytes[i];
            let is_one = cur == b'1';
            let mut j = i;
            while j < n && bytes[j] == cur {
                j += 1;
            }
            runs.push((is_one, j - i));
            i = j;
        }

        // Total number of '1's
        let total_ones: usize = runs.iter().filter(|&&(is_one, _)| is_one).map(|&(_, len)| len).sum();

        // Find best trade delta
        let mut max_delta: usize = 0;
        for idx in 0..runs.len() {
            if runs[idx].0 && idx > 0 && idx + 1 < runs.len()
                && !runs[idx - 1].0 && !runs[idx + 1].0
            {
                let delta = runs[idx - 1].1 + runs[idx + 1].1;
                if delta > max_delta {
                    max_delta = delta;
                }
            }
        }

        (total_ones + max_delta) as i32
    }
}
```

## Racket

```racket
(define/contract (max-active-sections-after-trade s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         ;; count total number of '1's
         (total-ones
          (let loop ((i 0) (cnt 0))
            (if (= i n) cnt
                (loop (+ i 1)
                      (if (char=? (string-ref s i) #\1) (+ cnt 1) cnt)))))
         ;; build runs as list of (cons char length) in order
         (runs-rev
          (let loop ((i 0) (curr #\space) (len 0) (acc '()))
            (if (= i n)
                (if (> len 0) (cons (cons curr len) acc) acc)
                (let ((c (string-ref s i)))
                  (if (or (= len 0) (char=? c curr))
                      (loop (+ i 1) c (+ len 1) acc)
                      (loop (+ i 1) c 1 (cons (cons curr len) acc)))))))
         (runs (reverse runs-rev))
         (run-count (length runs)))
    (let ((max-delta 0))
      (for ([idx (in-range run-count)])
        (define pair (list-ref runs idx))
        (when (char=? (car pair) #\1)
          (define left-zero
            (if (> idx 0)
                (let ((p (list-ref runs (- idx 1))))
                  (if (char=? (car p) #\0) (cdr p) 0))
                0))
          (define right-zero
            (if (< (+ idx 1) run-count)
                (let ((p (list-ref runs (+ idx 1))))
                  (if (char=? (car p) #\0) (cdr p) 0))
                0))
          (when (and (> left-zero 0) (> right-zero 0))
            (set! max-delta (max max-delta (+ left-zero right-zero))))))
      (+ total-ones max-delta))))
```

## Erlang

```erlang
-module(solution).
-export([max_active_sections_after_trade/1]).

-spec max_active_sections_after_trade(S :: unicode:unicode_binary()) -> integer().
max_active_sections_after_trade(S) ->
    Runs = build_runs(binary_to_list(S)),
    TotalOnes = total_ones(Runs),
    MaxDelta = max_delta(Runs, 0),
    TotalOnes + MaxDelta.

build_runs([]) -> [];
build_runs([H|T]) ->
    build_runs(T, H, 1, []).

build_runs([], Char, Len, Acc) ->
    lists:reverse([{Char, Len} | Acc]);
build_runs([H|T], Char, Len, Acc) when H =:= Char ->
    build_runs(T, Char, Len + 1, Acc);
build_runs([H|T], Char, Len, Acc) ->
    build_runs(T, H, 1, [{Char, Len} | Acc]).

total_ones(Runs) -> total_ones(Runs, 0).
total_ones([], Sum) -> Sum;
total_ones([{C, L} | Rest], Sum) when C =:= $1 ->
    total_ones(Rest, Sum + L);
total_ones([_ | Rest], Sum) ->
    total_ones(Rest, Sum).

max_delta(Runs, Max) ->
    case Runs of
        [{C1, L1}, {C2, L2} | Rest] when C1 =:= $0, C2 =:= $1 ->
            case Rest of
                [{C3, L3} | Tail] when C3 =:= $0 ->
                    Delta = L1 + L3,
                    NewMax = if Delta > Max -> Delta; true -> Max end,
                    max_delta([{C2, L2}, {C3, L3} | Tail], NewMax);
                _ ->
                    max_delta([{C2, L2} | Rest], Max)
            end;
        [_ | Rest] ->
            max_delta(Rest, Max);
        [] ->
            Max
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_active_sections_after_trade(s :: String.t) :: integer
  def max_active_sections_after_trade(s) do
    runs = build_runs(String.to_charlist(s))

    total_ones =
      Enum.reduce(runs, 0, fn {type, len}, acc ->
        if type == ?1, do: acc + len, else: acc
      end)

    max_delta =
      runs
      |> Enum.chunk_every(3, 1, [])
      |> Enum.reduce(0, fn
        [{prev_type, prev_len}, {cur_type, _cur_len}, {next_type, next_len}], best
        when cur_type == ?1 and prev_type == ?0 and next_type == ?0 ->
          delta = prev_len + next_len
          if delta > best, do: delta, else: best

        _, best ->
          best
      end)

    total_ones + max_delta
  end

  defp build_runs(chars) do
    {runs_rev, cur_type, cur_len} =
      Enum.reduce(chars, {[], nil, 0}, fn c, {runs_acc, ct, cl} ->
        cond do
          ct == nil ->
            {runs_acc, c, 1}

          c == ct ->
            {runs_acc, ct, cl + 1}

          true ->
            new_runs = [{ct, cl} | runs_acc]
            {new_runs, c, 1}
        end
      end)

    runs =
      case cur_type do
        nil -> runs_rev
        _ -> [{cur_type, cur_len} | runs_rev]
      end

    Enum.reverse(runs)
  end
end
```
