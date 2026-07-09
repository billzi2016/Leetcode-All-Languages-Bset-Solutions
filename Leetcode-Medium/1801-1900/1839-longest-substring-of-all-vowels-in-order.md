# 1839. Longest Substring Of All Vowels in Order

## Cpp

```cpp
class Solution {
public:
    int longestBeautifulSubstring(string word) {
        auto idx = [&](char c) -> int {
            switch(c) {
                case 'a': return 0;
                case 'e': return 1;
                case 'i': return 2;
                case 'o': return 3;
                case 'u': return 4;
                default: return -1;
            }
        };
        int ans = 0, stage = -1, curLen = 0;
        for (char c : word) {
            int v = idx(c);
            if (stage == -1) { // not in a candidate
                if (c == 'a') {
                    stage = 0;
                    curLen = 1;
                }
                continue;
            }
            if (v < stage) {
                // restart if current char is 'a'
                if (c == 'a') {
                    stage = 0;
                    curLen = 1;
                } else {
                    stage = -1;
                    curLen = 0;
                }
            } else if (v == stage) {
                ++curLen;
            } else if (v == stage + 1) {
                ++stage;
                ++curLen;
            } else { // jump over a vowel
                if (c == 'a') {
                    stage = 0;
                    curLen = 1;
                } else {
                    stage = -1;
                    curLen = 0;
                }
            }
            if (stage == 4) ans = max(ans, curLen);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestBeautifulSubstring(String word) {
        int maxLen = 0;
        int curLen = 0;
        int stage = -1; // -1: not started, 0:a,1:e,2:i,3:o,4:u
        char prev = 0;
        String order = "aeiou";
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == 'a') {
                // start a new candidate from this 'a'
                curLen = 1;
                stage = 0;
                prev = c;
            } else if (stage == -1) {
                // not in a valid substring, ignore
                continue;
            } else {
                if (c == prev) {
                    // same vowel, extend
                    curLen++;
                } else if (stage < 4 && c == order.charAt(stage + 1)) {
                    // move to next vowel in order
                    stage++;
                    curLen++;
                } else {
                    // invalid transition, reset
                    if (c == 'a') {
                        curLen = 1;
                        stage = 0;
                    } else {
                        curLen = 0;
                        stage = -1;
                    }
                }
                prev = c;
            }
            if (stage == 4) { // reached 'u'
                maxLen = Math.max(maxLen, curLen);
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        order = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        max_len = 0
        start = 0
        mask = 0
        prev_order = -1

        for i, ch in enumerate(word):
            cur = order[ch]
            if i > 0 and cur < prev_order:
                start = i
                mask = 0
            mask |= 1 << cur
            if mask == 31:  # all five vowels present
                max_len = max(max_len, i - start + 1)
            prev_order = cur

        return max_len
```

## Python3

```python
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        order = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        ans = 0
        cur_len = 0
        stage = -1  # last vowel index in current substring

        for ch in word:
            idx = order[ch]
            if cur_len == 0:
                if ch == 'a':
                    cur_len = 1
                    stage = 0
                continue

            if idx < stage:
                # break the sequence, maybe start new from this 'a'
                if ch == 'a':
                    cur_len = 1
                    stage = 0
                else:
                    cur_len = 0
                    stage = -1
            elif idx == stage or idx == stage + 1:
                cur_len += 1
                stage = idx
                if stage == 4:  # reached 'u'
                    ans = max(ans, cur_len)
            else:  # idx > stage + 1, skipped a required vowel
                if ch == 'a':
                    cur_len = 1
                    stage = 0
                else:
                    cur_len = 0
                    stage = -1

        return ans
```

## C

```c
#include <string.h>

int longestBeautifulSubstring(char* word) {
    int n = strlen(word);
    int maxlen = 0;
    int start = 0;
    int mask = 0;
    int prevRank = -1; // rank of previous character in current segment

    for (int i = 0; i < n; ++i) {
        int rank;
        switch (word[i]) {
            case 'a': rank = 0; break;
            case 'e': rank = 1; break;
            case 'i': rank = 2; break;
            case 'o': rank = 3; break;
            case 'u': rank = 4; break;
            default: rank = -1; // should not happen
        }

        if (prevRank == -1 || rank < prevRank) {
            start = i;
            mask = 0;
        }
        mask |= (1 << rank);
        prevRank = rank;

        if (mask == 31) { // all five vowels present
            int len = i - start + 1;
            if (len > maxlen) maxlen = len;
        }
    }

    return maxlen;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestBeautifulSubstring(string word) {
        int[] order = new int[256];
        order['a'] = 0;
        order['e'] = 1;
        order['i'] = 2;
        order['o'] = 3;
        order['u'] = 4;

        int maxLen = 0;
        int start = 0;
        int last = -1;                     // previous vowel order in current segment
        bool[] seen = new bool[5];         // which vowels have appeared in current segment
        int distinct = 0;                  // count of different vowels seen

        for (int i = 0; i < word.Length; i++) {
            int cur = order[word[i]];
            if (last == -1 || cur < last) {          // order broken, start new segment
                start = i;
                Array.Clear(seen, 0, 5);
                seen[cur] = true;
                distinct = 1;
                last = cur;
            } else {
                if (!seen[cur]) {
                    seen[cur] = true;
                    distinct++;
                }
                last = cur;
            }

            if (distinct == 5) {                     // contains all vowels in order
                int len = i - start + 1;
                if (len > maxLen) maxLen = len;
            }
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var longestBeautifulSubstring = function(word) {
    const order = {a:0, e:1, i:2, o:3, u:4};
    let maxLen = 0;
    let start = 0;
    let mask = 0;
    let prev = -1; // previous vowel order
    
    for (let i = 0; i < word.length; ++i) {
        const c = word[i];
        const cur = order[c];
        
        if (cur < prev) {          // breaks non‑decreasing order
            start = i;
            mask = 0;
        }
        mask |= (1 << cur);
        if (mask === 31) {         // all five vowels present
            maxLen = Math.max(maxLen, i - start + 1);
        }
        prev = cur;
    }
    
    return maxLen;
};
```

## Typescript

```typescript
function longestBeautifulSubstring(word: string): number {
    const orderMap: { [k: string]: number } = { a: 0, e: 1, i: 2, o: 3, u: 4 };
    let maxLen = 0;
    let left = 0;
    let lastOrder = -1;
    const seen = [false, false, false, false, false];
    let distinct = 0;

    for (let i = 0; i < word.length; i++) {
        const ch = word[i];
        const ord = orderMap[ch];

        if (ord < lastOrder) {
            left = i;
            seen.fill(false);
            distinct = 0;
        }

        if (!seen[ord]) {
            seen[ord] = true;
            distinct++;
        }
        lastOrder = ord;

        if (distinct === 5) {
            const len = i - left + 1;
            if (len > maxLen) maxLen = len;
        }
    }

    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function longestBeautifulSubstring($word) {
        $order = ['a'=>0,'e'=>1,'i'=>2,'o'=>3,'u'=>4];
        $maxLen = 0;
        $currLen = 0;
        $stage = -1; // -1 indicates not in a valid segment
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $c = $word[$i];
            $idx = $order[$c];
            if ($stage == -1) {
                if ($c === 'a') {
                    $stage = 0;
                    $currLen = 1;
                }
            } else {
                if ($idx < $stage) {
                    // order broken, restart if current char is 'a'
                    if ($c === 'a') {
                        $stage = 0;
                        $currLen = 1;
                    } else {
                        $stage = -1;
                        $currLen = 0;
                    }
                } elseif ($idx == $stage) {
                    // same vowel
                    $currLen++;
                } else { // idx > stage
                    if ($idx == $stage + 1) {
                        // next expected vowel
                        $stage = $idx;
                        $currLen++;
                    } else {
                        // skipped a vowel, restart if 'a'
                        if ($c === 'a') {
                            $stage = 0;
                            $currLen = 1;
                        } else {
                            $stage = -1;
                            $currLen = 0;
                        }
                    }
                }
            }
            if ($stage == 4 && $currLen > $maxLen) {
                $maxLen = $currLen;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestBeautifulSubstring(_ word: String) -> Int {
        let chars = Array(word)
        var cnt = [Int](repeating: 0, count: 5)
        var start = 0
        var prevIdx = -1
        var ans = 0
        
        func vowelIndex(_ ch: Character) -> Int {
            switch ch {
            case "a": return 0
            case "e": return 1
            case "i": return 2
            case "o": return 3
            case "u": return 4
            default: return -1
            }
        }
        
        for i in 0..<chars.count {
            let idx = vowelIndex(chars[i])
            if i == 0 || idx >= prevIdx {
                // continue current segment
            } else {
                cnt = [Int](repeating: 0, count: 5)
                start = i
            }
            cnt[idx] += 1
            prevIdx = idx
            
            var ok = true
            for v in 0..<5 where cnt[v] == 0 {
                ok = false
                break
            }
            if ok {
                let length = i - start + 1
                if length > ans { ans = length }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestBeautifulSubstring(word: String): Int {
        var ans = 0
        val cnt = IntArray(5)
        var start = 0
        var prevIdx = -1
        for (i in word.indices) {
            val idx = when (word[i]) {
                'a' -> 0
                'e' -> 1
                'i' -> 2
                'o' -> 3
                else -> 4 // 'u'
            }
            if (prevIdx != -1 && idx < prevIdx) {
                start = i
                java.util.Arrays.fill(cnt, 0)
            }
            cnt[idx]++
            var ok = true
            for (j in 0..4) {
                if (cnt[j] == 0) {
                    ok = false
                    break
                }
            }
            if (ok) {
                val len = i - start + 1
                if (len > ans) ans = len
            }
            prevIdx = idx
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestBeautifulSubstring(String word) {
    List<int> cnt = List.filled(5, 0);
    int start = 0;
    int ans = 0;

    int idx(int codeUnit) {
      switch (codeUnit) {
        case 97: return 0; // 'a'
        case 101: return 1; // 'e'
        case 105: return 2; // 'i'
        case 111: return 3; // 'o'
        case 117: return 4; // 'u'
        default: return -1;
      }
    }

    for (int j = 0; j < word.length; ++j) {
      int cur = idx(word.codeUnitAt(j));
      if (j > 0) {
        int prev = idx(word.codeUnitAt(j - 1));
        if (cur < prev) {
          cnt = List.filled(5, 0);
          start = j;
        }
      }
      cnt[cur]++;

      if (cnt[0] > 0 && cnt[1] > 0 && cnt[2] > 0 && cnt[3] > 0 && cnt[4] > 0) {
        ans = max(ans, j - start + 1);
      }
    }

    return ans;
  }
}
```

## Golang

```go
func longestBeautifulSubstring(word string) int {
    var order [256]int
    for i := range order {
        order[i] = -1
    }
    order['a'] = 0
    order['e'] = 1
    order['i'] = 2
    order['o'] = 3
    order['u'] = 4

    curLen, lastIdx, mask, maxLen := 0, -1, 0, 0
    for i := 0; i < len(word); i++ {
        idx := order[word[i]]
        if idx == -1 {
            curLen, lastIdx, mask = 0, -1, 0
            continue
        }
        if curLen == 0 {
            if idx == 0 {
                curLen = 1
                lastIdx = 0
                mask = 1 << 0
            }
            continue
        }
        if idx < lastIdx {
            if idx == 0 {
                curLen = 1
                lastIdx = 0
                mask = 1 << 0
            } else {
                curLen, lastIdx, mask = 0, -1, 0
            }
            continue
        }
        curLen++
        lastIdx = idx
        mask |= 1 << idx
        if mask == 31 && curLen > maxLen {
            maxLen = curLen
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def longest_beautiful_substring(word)
  order = { 'a' => 0, 'e' => 1, 'i' => 2, 'o' => 3, 'u' => 4 }
  max_len = 0
  start = 0
  last = -1
  seen = 0

  word.each_char.with_index do |ch, i|
    cur = order[ch]
    if cur < last
      start = i
      seen = 1
    else
      seen += 1 if cur > last
    end
    last = cur
    max_len = [max_len, i - start + 1].max if seen == 5
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def longestBeautifulSubstring(word: String): Int = {
        var maxLen = 0
        var curLen = 0
        var stage = -1               // last vowel index seen in current window
        var mask = 0                 // bitmask of vowels present in current window

        for (c <- word) {
            val idx = c match {
                case 'a' => 0
                case 'e' => 1
                case 'i' => 2
                case 'o' => 3
                case 'u' => 4
            }

            if (idx < stage) {               // order broken, start new window
                curLen = 1
                stage = idx
                mask = 1 << idx
            } else {
                curLen += 1
                stage = idx
                mask |= 1 << idx
            }

            if (mask == 31) {                // all five vowels present
                if (curLen > maxLen) maxLen = curLen
            }
        }

        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_beautiful_substring(word: String) -> i32 {
        let bytes = word.as_bytes();
        let mut ans: usize = 0;
        let mut start: usize = 0;
        let mut prev_rank: i8 = -1;
        let mut mask: u8 = 0;

        for (i, &b) in bytes.iter().enumerate() {
            let rank = match b {
                b'a' => 0,
                b'e' => 1,
                b'i' => 2,
                b'o' => 3,
                b'u' => 4,
                _ => -1, // unreachable due to constraints
            };
            if (rank as i8) < prev_rank {
                start = i;
                mask = 0;
            }
            mask |= 1 << rank;
            prev_rank = rank as i8;

            if mask == 0b11111 {
                let len = i - start + 1;
                if len > ans {
                    ans = len;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (longest-beautiful-substring word)
  (-> string? exact-integer?)
  (let* ([n (string-length word)]
         [max-len 0]
         [start 0]
         [prev-idx -1]
         [mask 0]
         [vowel-index
          (lambda (ch)
            (cond [(char=? ch #\a) 0]
                  [(char=? ch #\e) 1]
                  [(char=? ch #\i) 2]
                  [(char=? ch #\o) 3]
                  [(char=? ch #\u) 4]))])
    (for ([i (in-range n)])
      (define idx (vowel-index (string-ref word i)))
      (if (< idx prev-idx)
          (begin
            (set! start i)
            (set! mask (arithmetic-shift 1 idx))
            (set! prev-idx idx))
          (begin
            (set! mask (bitwise-ior mask (arithmetic-shift 1 idx)))
            (set! prev-idx idx)))
      (when (= mask #b11111) ; all five vowels seen
        (define len (+ 1 (- i start)))
        (when (> len max-len)
          (set! max-len len))))
    max-len))
```

## Erlang

```erlang
-module(solution).
-export([longest_beautiful_substring/1]).

-spec longest_beautiful_substring(Word :: unicode:unicode_binary()) -> integer().
longest_beautiful_substring(Word) ->
    Bytes = binary_to_list(Word),
    loop(Bytes, 0, 0, 0, 0).

loop([], _CurLen, _Mask, _LastOrder, Max) ->
    Max;
loop([C|Rest], CurLen, Mask, LastOrder, Max) ->
    Order = char_order(C),
    case Order >= LastOrder of
        true ->
            NewLen = CurLen + 1,
            NewMask = Mask bor (1 bsl (Order - 1)),
            NewMax = if NewMask == 31 -> erlang:max(NewLen, Max); true -> Max end,
            loop(Rest, NewLen, NewMask, Order, NewMax);
        false ->
            case Order of
                1 ->
                    % start new segment with 'a'
                    loop(Rest, 1, 1, 1, Max);
                _ ->
                    % reset and discard current character
                    loop(Rest, 0, 0, 0, Max)
            end
    end.

char_order($a) -> 1;
char_order($e) -> 2;
char_order($i) -> 3;
char_order($o) -> 4;
char_order($u) -> 5.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_beautiful_substring(word :: String.t()) :: integer()
  def longest_beautiful_substring(word) do
    import Bitwise

    bytes = :binary.bin_to_list(word)

    {_cur_start, _last_idx, _mask, best} =
      Enum.reduce(Enum.with_index(bytes), {nil, -1, 0, 0}, fn {b, i},
          {cur_start, last_idx, mask, best} ->
        order =
          case b do
            ?a -> 0
            ?e -> 1
            ?i -> 2
            ?o -> 3
            ?u -> 4
          end

        cond do
          cur_start == nil ->
            if b == ?a do
              new_mask = 1 <<< order
              new_best = if new_mask == 31, do: max(best, 1), else: best
              {i, order, new_mask, new_best}
            else
              {nil, -1, 0, best}
            end

          order < last_idx ->
            if b == ?a do
              new_mask = 1 <<< order
              new_best = if new_mask == 31, do: max(best, 1), else: best
              {i, order, new_mask, new_best}
            else
              {nil, -1, 0, best}
            end

          true ->
            new_mask = mask ||| (1 <<< order)

            new_best =
              if new_mask == 31 do
                len = i - cur_start + 1
                max(best, len)
              else
                best
              end

            {cur_start, order, new_mask, new_best}
        end
      end)

    best
  end
end
```
