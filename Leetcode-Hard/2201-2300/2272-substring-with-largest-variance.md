# 2272. Substring With Largest Variance

## Cpp

```cpp
class Solution {
public:
    int largestVariance(string s) {
        int n = s.size();
        vector<int> total(26, 0);
        for (char c : s) total[c - 'a']++;
        
        int answer = 0;
        // iterate over ordered pairs (major, minor)
        for (int major = 0; major < 26; ++major) {
            if (total[major] == 0) continue;
            for (int minor = 0; minor < 26; ++minor) {
                if (major == minor || total[minor] == 0) continue;
                
                int majorCount = 0, minorCount = 0;
                int restMinor = total[minor];
                
                for (char ch : s) {
                    if (ch - 'a' == major) {
                        ++majorCount;
                    } else if (ch - 'a' == minor) {
                        ++minorCount;
                        --restMinor;
                    }
                    
                    if (minorCount > 0) {
                        answer = max(answer, majorCount - minorCount);
                    }
                    
                    // reset when current diff is negative and we can still find a future minor
                    if (majorCount < minorCount && restMinor > 0) {
                        majorCount = 0;
                        minorCount = 0;
                    }
                }
            }
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int largestVariance(String s) {
        int n = s.length();
        int[] freq = new int[26];
        for (int i = 0; i < n; i++) {
            freq[s.charAt(i) - 'a']++;
        }
        int answer = 0;
        // iterate over ordered pairs (major, minor)
        for (int major = 0; major < 26; major++) {
            if (freq[major] == 0) continue;
            for (int minor = 0; minor < 26; minor++) {
                if (major == minor || freq[minor] == 0) continue;
                int majorCount = 0, minorCount = 0;
                int restMinor = freq[minor];
                int bestForPair = 0;
                for (int k = 0; k < n; k++) {
                    char ch = s.charAt(k);
                    int idx = ch - 'a';
                    if (idx == major) {
                        majorCount++;
                    } else if (idx == minor) {
                        minorCount++;
                        restMinor--;
                    } else {
                        continue;
                    }
                    if (minorCount > 0) {
                        bestForPair = Math.max(bestForPair, majorCount - minorCount);
                    }
                    if (majorCount - minorCount < 0 && restMinor > 0) {
                        majorCount = 0;
                        minorCount = 0;
                    }
                }
                answer = Math.max(answer, bestForPair);
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count total occurrences of each character
        total = [0] * 26
        for ch in s:
            total[ord(ch) - 97] += 1

        # list of characters that actually appear
        chars = [chr(i + 97) for i in range(26) if total[i] > 0]

        ans = 0
        for major in chars:
            for minor in chars:
                if major == minor:
                    continue
                rest_minor = total[ord(minor) - 97]
                major_cnt = minor_cnt = 0
                for ch in s:
                    if ch == major:
                        major_cnt += 1
                    if ch == minor:
                        minor_cnt += 1
                        rest_minor -= 1

                    # valid substring must contain at least one minor
                    if minor_cnt > 0:
                        ans = max(ans, major_cnt - minor_cnt)

                    # reset when current diff is negative and we can still find a minor later
                    if major_cnt - minor_cnt < 0 and rest_minor > 0:
                        major_cnt = minor_cnt = 0
        return ans
```

## Python3

```python
class Solution:
    def largestVariance(self, s: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        n = len(s)
        ans = 0

        for major_idx in range(26):
            for minor_idx in range(26):
                if major_idx == minor_idx or freq[major_idx] == 0 or freq[minor_idx] == 0:
                    continue
                major_char = chr(97 + major_idx)
                minor_char = chr(97 + minor_idx)

                rest_minor = freq[minor_idx]
                major_cnt = 0
                minor_cnt = 0

                for ch in s:
                    if ch == major_char:
                        major_cnt += 1
                    elif ch == minor_char:
                        minor_cnt += 1
                        rest_minor -= 1

                    if minor_cnt > 0:
                        ans = max(ans, major_cnt - minor_cnt)

                    if major_cnt - minor_cnt < 0 and rest_minor > 0:
                        major_cnt = 0
                        minor_cnt = 0

        return ans
```

## C

```c
#include <string.h>

int largestVariance(char* s) {
    int n = strlen(s);
    int total[26] = {0};
    for (int i = 0; i < n; ++i) {
        total[s[i] - 'a']++;
    }

    int ans = 0;
    for (int major = 0; major < 26; ++major) {
        for (int minor = 0; minor < 26; ++minor) {
            if (major == minor) continue;

            int majorCount = 0, minorCount = 0;
            int restMinor = total[minor];

            for (int i = 0; i < n; ++i) {
                int c = s[i] - 'a';
                if (c == major) {
                    ++majorCount;
                }
                if (c == minor) {
                    ++minorCount;
                    --restMinor;
                }

                if (minorCount > 0) {
                    int diff = majorCount - minorCount;
                    if (diff > ans) ans = diff;
                }

                if ((majorCount - minorCount) < 0 && restMinor > 0) {
                    majorCount = 0;
                    minorCount = 0;
                }
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int LargestVariance(string s)
    {
        int[] total = new int[26];
        foreach (char c in s) total[c - 'a']++;

        int ans = 0;
        for (int major = 0; major < 26; ++major)
        {
            if (total[major] == 0) continue;
            for (int minor = 0; minor < 26; ++minor)
            {
                if (major == minor || total[minor] == 0) continue;

                int majorCount = 0, minorCount = 0;
                int restMinor = total[minor];

                foreach (char ch in s)
                {
                    int idx = ch - 'a';
                    if (idx == major)
                    {
                        majorCount++;
                    }
                    else if (idx == minor)
                    {
                        minorCount++;
                        restMinor--;
                    }

                    if (minorCount > 0)
                    {
                        ans = Math.Max(ans, majorCount - minorCount);
                    }

                    if (majorCount - minorCount < 0 && restMinor > 0)
                    {
                        majorCount = 0;
                        minorCount = 0;
                    }
                }
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var largestVariance = function(s) {
    const n = s.length;
    const total = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        total[s.charCodeAt(i) - 97]++;
    }

    let ans = 0;

    for (let major = 0; major < 26; ++major) {
        for (let minor = 0; minor < 26; ++minor) {
            if (major === minor) continue;
            if (total[major] === 0 || total[minor] === 0) continue;

            let majorCount = 0, minorCount = 0;
            let restMinor = total[minor];

            for (let i = 0; i < n; ++i) {
                const idx = s.charCodeAt(i) - 97;
                if (idx === major) {
                    majorCount++;
                } else if (idx === minor) {
                    minorCount++;
                    restMinor--;
                }

                if (minorCount > 0) {
                    ans = Math.max(ans, majorCount - minorCount);
                }

                if (majorCount - minorCount < 0 && restMinor > 0) {
                    majorCount = 0;
                    minorCount = 0;
                }
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function largestVariance(s: string): number {
    const n = s.length;
    const freq = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }

    let answer = 0;

    for (let major = 0; major < 26; ++major) {
        if (freq[major] === 0) continue;
        for (let minor = 0; minor < 26; ++minor) {
            if (major === minor || freq[minor] === 0) continue;

            let majorCount = 0;
            let minorCount = 0;
            let restMinor = freq[minor];
            let best = 0;

            for (let i = 0; i < n; ++i) {
                const c = s.charCodeAt(i) - 97;
                if (c === major) majorCount++;
                if (c === minor) {
                    minorCount++;
                    restMinor--;
                }

                if (minorCount > 0) {
                    best = Math.max(best, majorCount - minorCount);
                }

                if (majorCount - minorCount < 0 && restMinor > 0) {
                    majorCount = 0;
                    minorCount = 0;
                }
            }

            answer = Math.max(answer, best);
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function largestVariance($s) {
        $n = strlen($s);
        // frequency of each character
        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }

        $ans = 0;

        // iterate over all ordered pairs (major, minor)
        for ($major = 0; $major < 26; $major++) {
            if ($freq[$major] == 0) continue;
            for ($minor = 0; $minor < 26; $minor++) {
                if ($major == $minor || $freq[$minor] == 0) continue;

                $restMinor = $freq[$minor];
                $majorCount = 0;
                $minorCount = 0;

                for ($i = 0; $i < $n; $i++) {
                    $c = ord($s[$i]) - 97;
                    if ($c == $major) {
                        $majorCount++;
                    } elseif ($c == $minor) {
                        $minorCount++;
                        $restMinor--;
                    } else {
                        continue;
                    }

                    // update answer only when we have at least one minor in the current window
                    if ($minorCount > 0) {
                        $ans = max($ans, $majorCount - $minorCount);
                    }

                    // reset counts if the current difference is negative and there are still minors ahead
                    if (($majorCount - $minorCount) < 0 && $restMinor > 0) {
                        $majorCount = 0;
                        $minorCount = 0;
                    }
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func largestVariance(_ s: String) -> Int {
        let chars = Array(s.utf8)               // ASCII codes of characters
        var freq = [Int](repeating: 0, count: 26)
        for ch in chars {
            let idx = Int(ch) - 97
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        
        var result = 0
        
        for major in 0..<26 {
            for minor in 0..<26 where major != minor && freq[major] > 0 && freq[minor] > 0 {
                var majorCount = 0
                var minorCount = 0
                var restMinor = freq[minor]
                var bestForPair = 0
                
                for ch in chars {
                    let idx = Int(ch) - 97
                    if idx == major {
                        majorCount += 1
                    } else if idx == minor {
                        minorCount += 1
                        restMinor -= 1
                    }
                    
                    // Update answer only when at least one minor has been seen
                    if minorCount > 0 {
                        let diff = majorCount - minorCount
                        if diff > bestForPair { bestForPair = diff }
                    }
                    
                    // Reset counts if current difference is negative and we can still find a minor later
                    if (majorCount - minorCount) < 0 && restMinor > 0 {
                        majorCount = 0
                        minorCount = 0
                    }
                }
                
                if bestForPair > result { result = bestForPair }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestVariance(s: String): Int {
        val freq = IntArray(26)
        for (c in s) {
            freq[c - 'a']++
        }
        var ans = 0
        for (majorIdx in 0 until 26) {
            for (minorIdx in 0 until 26) {
                if (majorIdx == minorIdx) continue
                var majorCount = 0
                var minorCount = 0
                var restMinor = freq[minorIdx]
                for (ch in s) {
                    val idx = ch - 'a'
                    if (idx == majorIdx) {
                        majorCount++
                    } else if (idx == minorIdx) {
                        minorCount++
                        restMinor--
                    }
                    if (minorCount > 0) {
                        val diff = majorCount - minorCount
                        if (diff > ans) ans = diff
                    }
                    if (majorCount - minorCount < 0 && restMinor > 0) {
                        majorCount = 0
                        minorCount = 0
                    }
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int largestVariance(String s) {
    List<int> total = List.filled(26, 0);
    for (int code in s.codeUnits) {
      total[code - 97]++;
    }

    int answer = 0;
    for (int major = 0; major < 26; major++) {
      if (total[major] == 0) continue;
      for (int minor = 0; minor < 26; minor++) {
        if (major == minor || total[minor] == 0) continue;

        int restMinor = total[minor];
        int majorCount = 0, minorCount = 0;

        for (int code in s.codeUnits) {
          int ch = code - 97;
          if (ch == major) {
            majorCount++;
          } else if (ch == minor) {
            minorCount++;
            restMinor--;
          }

          if (minorCount > 0) {
            int diff = majorCount - minorCount;
            if (diff > answer) answer = diff;
          }

          if (majorCount - minorCount < 0 && restMinor > 0) {
            majorCount = 0;
            minorCount = 0;
          }
        }
      }
    }
    return answer;
  }
}
```

## Golang

```go
func largestVariance(s string) int {
    n := len(s)
    if n == 0 {
        return 0
    }
    maxAns := 0

    for major := byte('a'); major <= 'z'; major++ {
        for minor := byte('a'); minor <= 'z'; minor++ {
            if major == minor {
                continue
            }

            // total count of minor in the whole string
            restMinor := 0
            for i := 0; i < n; i++ {
                if s[i] == minor {
                    restMinor++
                }
            }
            if restMinor == 0 { // no minor, cannot form a valid substring
                continue
            }

            majorCount, minorCount := 0, 0
            for i := 0; i < n; i++ {
                ch := s[i]
                if ch == major {
                    majorCount++
                }
                if ch == minor {
                    minorCount++
                    restMinor--
                }

                if minorCount > 0 {
                    diff := majorCount - minorCount
                    if diff > maxAns {
                        maxAns = diff
                    }
                }

                if majorCount-minorCount < 0 && restMinor > 0 {
                    majorCount = 0
                    minorCount = 0
                }
            }
        }
    }
    return maxAns
}
```

## Ruby

```ruby
def largest_variance(s)
  # total counts of each character
  total = Array.new(26, 0)
  s.each_char { |c| total[c.ord - 97] += 1 }

  max_var = 0
  letters = ('a'..'z').to_a

  letters.each do |major|
    letters.each do |minor|
      next if major == minor

      rest_minor = total[minor.ord - 97]
      major_cnt = 0
      minor_cnt = 0

      s.each_char do |ch|
        if ch == major
          major_cnt += 1
        elsif ch == minor
          minor_cnt += 1
          rest_minor -= 1
        else
          next
        end

        if minor_cnt > 0
          diff = major_cnt - minor_cnt
          max_var = diff if diff > max_var
        end

        if (major_cnt - minor_cnt) < 0 && rest_minor > 0
          major_cnt = 0
          minor_cnt = 0
        end
      end
    end
  end

  max_var
end
```

## Scala

```scala
object Solution {
    def largestVariance(s: String): Int = {
        val freq = new Array[Int](26)
        for (ch <- s) {
            freq(ch - 'a') += 1
        }
        var answer = 0
        for (major <- 0 until 26 if freq(major) > 0) {
            for (minor <- 0 until 26 if minor != major && freq(minor) > 0) {
                var majorCount = 0
                var minorCount = 0
                var restMinor = freq(minor)
                for (ch <- s) {
                    val idx = ch - 'a'
                    if (idx == major) {
                        majorCount += 1
                    } else if (idx == minor) {
                        minorCount += 1
                        restMinor -= 1
                    }
                    if (minorCount > 0) {
                        answer = math.max(answer, majorCount - minorCount)
                    }
                    if (majorCount - minorCount < 0 && restMinor > 0) {
                        majorCount = 0
                        minorCount = 0
                    }
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
    pub fn largest_variance(s: String) -> i32 {
        let bytes = s.as_bytes();
        // total count of each character
        let mut total = [0i32; 26];
        for &b in bytes {
            total[(b - b'a') as usize] += 1;
        }

        let mut answer = 0i32;

        for major in 0..26 {
            for minor in 0..26 {
                if major == minor {
                    continue;
                }
                // both characters must appear at least once
                if total[major] == 0 || total[minor] == 0 {
                    continue;
                }

                let mut rest_minor = total[minor];
                let mut major_cnt = 0i32;
                let mut minor_cnt = 0i32;

                for &b in bytes {
                    let idx = (b - b'a') as usize;
                    if idx == major {
                        major_cnt += 1;
                    }
                    if idx == minor {
                        minor_cnt += 1;
                        rest_minor -= 1;
                    }

                    if minor_cnt > 0 {
                        answer = answer.max(major_cnt - minor_cnt);
                    }

                    if major_cnt - minor_cnt < 0 && rest_minor > 0 {
                        major_cnt = 0;
                        minor_cnt = 0;
                    }
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (largest-variance s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (total (make-vector 26 0)))
    ;; total counts of each character
    (for ([i (in-range n)])
      (let* ((c (char->integer (string-ref s i)))
             (idx (- c (char->integer #\a))))
        (vector-set! total idx (+ 1 (vector-ref total idx)))))
    (define ans 0)
    ;; consider every ordered pair of distinct letters
    (for ([major (in-range 26)])
      (for ([minor (in-range 26)])
        (when (not (= major minor))
          (let ((rest-minor (vector-ref total minor)))
            (define major-cnt 0)
            (define minor-cnt 0)
            (for ([i (in-range n)])
              (let ((idx (- (char->integer (string-ref s i))
                            (char->integer #\a))))
                (cond
                  [(= idx major) (set! major-cnt (+ major-cnt 1))]
                  [(= idx minor)
                   (set! minor-cnt (+ minor-cnt 1))
                   (set! rest-minor (- rest-minor 1))]))
              ;; update answer if at least one minor seen
              (when (> minor-cnt 0)
                (set! ans (max ans (- major-cnt minor-cnt))))
              ;; reset when current diff negative and there are remaining minors
              (when (and (< (- major-cnt minor-cnt) 0) (> rest-minor 0))
                (set! major-cnt 0)
                (set! minor-cnt 0))))))
    ans)))
```

## Erlang

```erlang
-module(solution).
-export([largest_variance/1]).

largest_variance(S) ->
    Str = binary:bin_to_list(S),
    loop_major(0, Str, 0).

loop_major(26, _Str, Acc) -> Acc;
loop_major(Major, Str, Acc) ->
    Acc1 = loop_minor(0, Major, Str, Acc),
    loop_major(Major + 1, Str, Acc1).

loop_minor(26, _Major, _Str, Acc) -> Acc;
loop_minor(Minor, Major, Str, Acc) when Minor == Major ->
    loop_minor(Minor + 1, Major, Str, Acc);
loop_minor(Minor, Major, Str, Acc) ->
    TotalMinor = count_char(Str, Minor),
    case TotalMinor of
        0 -> loop_minor(Minor + 1, Major, Str, Acc);
        _ ->
            MaxForPair = kadane_pair(Str, Major, Minor, TotalMinor, 0, 0, 0),
            NewAcc = if MaxForPair > Acc -> MaxForPair; true -> Acc end,
            loop_minor(Minor + 1, Major, Str, NewAcc)
    end.

count_char([], _Idx) -> 0;
count_char([C|Cs], Idx) ->
    Rest = count_char(Cs, Idx),
    if (C - $a) == Idx -> Rest + 1; true -> Rest end.

kadane_pair([], _Major, _Minor, _RestMinor, _MajCnt, _MinCnt, Max) -> Max;
kadane_pair([C|Cs], Major, Minor, RestMinor, MajCnt, MinCnt, Max) ->
    IsMajor = ((C - $a) == Major),
    IsMinor = ((C - $a) == Minor),
    MajCnt1 = if IsMajor -> MajCnt + 1; true -> MajCnt end,
    MinCnt1 = if IsMinor -> MinCnt + 1; true -> MinCnt end,
    RestMinor1 = if IsMinor -> RestMinor - 1; true -> RestMinor end,
    NewMax = case MinCnt1 > 0 of
        true ->
            Diff = MajCnt1 - MinCnt1,
            if Diff > Max -> Diff; true -> Max end;
        false -> Max
    end,
    {MajCnt2, MinCnt2, RestMinor2} =
        if (MajCnt1 - MinCnt1) < 0 andalso RestMinor1 > 0 ->
                {0, 0, RestMinor1};
           true ->
                {MajCnt1, MinCnt1, RestMinor1}
        end,
    kadane_pair(Cs, Major, Minor, RestMinor2, MajCnt2, MinCnt2, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_variance(s :: String.t()) :: integer
  def largest_variance(s) do
    chars = String.to_charlist(s)

    counts =
      Enum.reduce(chars, %{}, fn c, acc ->
        Map.update(acc, c, 1, &(&1 + 1))
      end)

    pairs =
      for major <- ?a..?z,
          minor <- ?a..?z,
          major != minor,
          do: {major, minor}

    Enum.reduce(pairs, 0, fn {major, minor}, acc ->
      total_minor = Map.get(counts, minor, 0)
      best = process_pair(major, minor, chars, total_minor)
      max(acc, best)
    end)
  end

  defp process_pair(major, minor, chars, total_minor) do
    {_maj_cnt, _min_cnt, _rest, best} =
      Enum.reduce(chars, {0, 0, total_minor, 0}, fn ch,
                                                   {maj_cnt, min_cnt, rest, best} ->
        maj_cnt = if ch == major, do: maj_cnt + 1, else: maj_cnt

        {min_cnt, rest} =
          if ch == minor do
            {min_cnt + 1, rest - 1}
          else
            {min_cnt, rest}
          end

        best = if min_cnt > 0, do: max(best, maj_cnt - min_cnt), else: best

        if (maj_cnt - min_cnt) < 0 and rest > 0 do
          {0, 0, rest, best}
        else
          {maj_cnt, min_cnt, rest, best}
        end
      end)

    best
  end
end
```
