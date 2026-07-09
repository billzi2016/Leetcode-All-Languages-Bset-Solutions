# 2182. Construct String With Repeat Limit

## Cpp

```cpp
class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        string ans;
        while (true) {
            int i = 25;
            while (i >= 0 && cnt[i] == 0) --i;
            if (i < 0) break; // no characters left
            int use = min(cnt[i], repeatLimit);
            ans.append(use, char('a' + i));
            cnt[i] -= use;
            if (cnt[i] == 0) continue; // can keep using next largest
            // need a smaller character to break the streak
            int j = i - 1;
            while (j >= 0 && cnt[j] == 0) --j;
            if (j < 0) break; // cannot insert breaker, stop
            ans.push_back(char('a' + j));
            cnt[j]--;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String repeatLimitedString(String s, int repeatLimit) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }
        StringBuilder sb = new StringBuilder();
        int cur = 25; // start from 'z'
        while (cur >= 0) {
            if (cnt[cur] == 0) {
                cur--;
                continue;
            }
            int use = Math.min(cnt[cur], repeatLimit);
            for (int i = 0; i < use; i++) {
                sb.append((char) ('a' + cur));
            }
            cnt[cur] -= use;
            if (cnt[cur] == 0) {
                continue;
            }
            int nxt = cur - 1;
            while (nxt >= 0 && cnt[nxt] == 0) {
                nxt--;
            }
            if (nxt < 0) {
                break; // no smaller character to break the streak
            }
            sb.append((char) ('a' + nxt));
            cnt[nxt]--;
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        res_parts = []
        cur = 25  # start from 'z'

        while True:
            while cur >= 0 and freq[cur] == 0:
                cur -= 1
            if cur < 0:
                break

            use = min(freq[cur], repeatLimit)
            res_parts.append(chr(cur + 97) * use)
            freq[cur] -= use

            if freq[cur] == 0:
                continue  # move to next character in the next iteration

            # need a smaller character as a breaker
            nxt = cur - 1
            while nxt >= 0 and freq[nxt] == 0:
                nxt -= 1
            if nxt < 0:
                break  # cannot insert any more characters without violating limit

            res_parts.append(chr(nxt + 97))
            freq[nxt] -= 1
            # cur remains the same for next loop (still has remaining count)

        return ''.join(res_parts)
```

## Python3

```python
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        cur = 25
        res_parts = []
        while cur >= 0:
            if freq[cur] == 0:
                cur -= 1
                continue

            use = min(freq[cur], repeatLimit)
            res_parts.append(chr(cur + 97) * use)
            freq[cur] -= use

            if freq[cur] == 0:
                cur -= 1
                continue

            # need a smaller character to break the streak
            nxt = cur - 1
            while nxt >= 0 and freq[nxt] == 0:
                nxt -= 1
            if nxt < 0:   # no breaker available, stop
                break

            res_parts.append(chr(nxt + 97))
            freq[nxt] -= 1
            # continue with same cur (may still have remaining chars)

        return ''.join(res_parts)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* repeatLimitedString(char* s, int repeatLimit) {
    int freq[26] = {0};
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        freq[s[i] - 'a']++;
    }
    
    char *ans = (char *)malloc(n + 1);
    int pos = 0;
    
    while (1) {
        int i = 25;
        while (i >= 0 && freq[i] == 0) i--;
        if (i < 0) break; // no characters left
        
        int use = freq[i] < repeatLimit ? freq[i] : repeatLimit;
        for (int k = 0; k < use; ++k) {
            ans[pos++] = 'a' + i;
        }
        freq[i] -= use;
        
        if (freq[i] == 0) continue; // no need for a breaker
        
        int j = i - 1;
        while (j >= 0 && freq[j] == 0) j--;
        if (j < 0) break; // cannot insert a different character, stop
        
        ans[pos++] = 'a' + j;
        freq[j]--;
    }
    
    ans[pos] = '\0';
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public string RepeatLimitedString(string s, int repeatLimit) {
        int[] cnt = new int[26];
        foreach (char ch in s) cnt[ch - 'a']++;

        var sb = new System.Text.StringBuilder();
        int cur = 25; // start from 'z'

        while (cur >= 0) {
            if (cnt[cur] == 0) {
                cur--;
                continue;
            }

            int use = System.Math.Min(cnt[cur], repeatLimit);
            for (int i = 0; i < use; i++) {
                sb.Append((char)('a' + cur));
            }
            cnt[cur] -= use;

            if (cnt[cur] == 0) {
                // no more of this character, continue to next
                continue;
            }

            // need a smaller character as a breaker
            int nxt = cur - 1;
            while (nxt >= 0 && cnt[nxt] == 0) nxt--;

            if (nxt < 0) {
                // cannot place any more characters without breaking the limit
                break;
            }

            sb.Append((char)('a' + nxt));
            cnt[nxt]--;
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} repeatLimit
 * @return {string}
 */
var repeatLimitedString = function(s, repeatLimit) {
    const freq = new Array(26).fill(0);
    for (let ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    const res = [];
    let cur = 25; // start from 'z'
    while (cur >= 0) {
        if (freq[cur] === 0) {
            cur--;
            continue;
        }
        const use = Math.min(freq[cur], repeatLimit);
        for (let i = 0; i < use; i++) {
            res.push(String.fromCharCode(97 + cur));
        }
        freq[cur] -= use;
        if (freq[cur] > 0) {
            // need a smaller character to break the streak
            let nxt = cur - 1;
            while (nxt >= 0 && freq[nxt] === 0) nxt--;
            if (nxt < 0) break; // cannot place any more characters
            res.push(String.fromCharCode(97 + nxt));
            freq[nxt]--;
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function repeatLimitedString(s: string, repeatLimit: number): string {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    const res: string[] = [];
    while (true) {
        let i = 25;
        while (i >= 0 && freq[i] === 0) i--;
        if (i < 0) break;

        const use = Math.min(freq[i], repeatLimit);
        for (let k = 0; k < use; k++) {
            res.push(String.fromCharCode(97 + i));
        }
        freq[i] -= use;
        if (freq[i] === 0) continue;

        let j = i - 1;
        while (j >= 0 && freq[j] === 0) j--;
        if (j < 0) break;

        res.push(String.fromCharCode(97 + j));
        freq[j]--;
    }
    return res.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $repeatLimit
     * @return String
     */
    function repeatLimitedString($s, $repeatLimit) {
        $freq = array_fill(0, 26, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }

        $res = [];
        $curr = 25; // start from 'z'

        while ($curr >= 0) {
            if ($freq[$curr] == 0) {
                $curr--;
                continue;
            }

            $use = min($freq[$curr], $repeatLimit);
            $ch = chr($curr + 97);
            for ($i = 0; $i < $use; $i++) {
                $res[] = $ch;
            }
            $freq[$curr] -= $use;

            if ($freq[$curr] == 0) {
                $curr--;
                continue;
            }

            // need a smaller character to break the streak
            $next = $curr - 1;
            while ($next >= 0 && $freq[$next] == 0) {
                $next--;
            }
            if ($next < 0) {
                break; // cannot place any more characters
            }

            $breaker = chr($next + 97);
            $res[] = $breaker;
            $freq[$next]--;

            // continue with the same $curr (still has remaining chars)
        }

        return implode('', $res);
    }
}
```

## Swift

```swift
class Solution {
    func repeatLimitedString(_ s: String, _ repeatLimit: Int) -> String {
        var freq = [Int](repeating: 0, count: 26)
        let aVal = Int("a".unicodeScalars.first!.value)
        for scalar in s.unicodeScalars {
            let idx = Int(scalar.value) - aVal
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        var result = ""
        var cur = 25
        while cur >= 0 {
            if freq[cur] == 0 {
                cur -= 1
                continue
            }
            let use = min(freq[cur], repeatLimit)
            let ch = Character(UnicodeScalar(UInt32(aVal + cur))!)
            for _ in 0..<use {
                result.append(ch)
            }
            freq[cur] -= use
            if freq[cur] > 0 {
                var next = cur - 1
                while next >= 0 && freq[next] == 0 {
                    next -= 1
                }
                if next < 0 { break }
                let ch2 = Character(UnicodeScalar(UInt32(aVal + next))!)
                result.append(ch2)
                freq[next] -= 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun repeatLimitedString(s: String, repeatLimit: Int): String {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        val sb = StringBuilder()
        while (true) {
            var i = 25
            while (i >= 0 && freq[i] == 0) i--
            if (i < 0) break
            val use = kotlin.math.min(freq[i], repeatLimit)
            repeat(use) { sb.append(('a'.code + i).toChar()) }
            freq[i] -= use
            if (freq[i] == 0) continue
            var j = i - 1
            while (j >= 0 && freq[j] == 0) j--
            if (j < 0) break
            sb.append(('a'.code + j).toChar())
            freq[j]--
        }
        return sb.toString()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  String repeatLimitedString(String s, int repeatLimit) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      cnt[s.codeUnitAt(i) - 97]++;
    }

    StringBuffer sb = StringBuffer();
    int cur = 25;

    while (cur >= 0) {
      if (cnt[cur] == 0) {
        cur--;
        continue;
      }

      int use = min(cnt[cur], repeatLimit);
      for (int i = 0; i < use; i++) {
        sb.writeCharCode(97 + cur);
      }
      cnt[cur] -= use;

      if (cnt[cur] == 0) {
        continue;
      }

      int nxt = cur - 1;
      while (nxt >= 0 && cnt[nxt] == 0) {
        nxt--;
      }
      if (nxt < 0) {
        break;
      }

      sb.writeCharCode(97 + nxt);
      cnt[nxt]--;
    }

    return sb.toString();
  }
}
```

## Golang

```go
import "strings"

func repeatLimitedString(s string, repeatLimit int) string {
    var freq [26]int
    for _, ch := range s {
        freq[ch-'a']++
    }
    var sb strings.Builder
    for i := 25; i >= 0; i-- {
        for freq[i] > 0 {
            use := repeatLimit
            if freq[i] < use {
                use = freq[i]
            }
            for k := 0; k < use; k++ {
                sb.WriteByte(byte('a' + i))
            }
            freq[i] -= use
            if freq[i] == 0 {
                break
            }
            // find next smaller character to break the streak
            j := -1
            for t := i - 1; t >= 0; t-- {
                if freq[t] > 0 {
                    j = t
                    break
                }
            }
            if j == -1 {
                return sb.String()
            }
            sb.WriteByte(byte('a' + j))
            freq[j]--
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
def repeat_limited_string(s, repeat_limit)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }

  result = +""
  i = 25
  while true
    i -= 1 while i >= 0 && freq[i] == 0
    break if i < 0

    use = [freq[i], repeat_limit].min
    result << (('a'.ord + i).chr * use)
    freq[i] -= use

    if freq[i] > 0
      j = i - 1
      j -= 1 while j >= 0 && freq[j] == 0
      break if j < 0
      result << (('a'.ord + j).chr)
      freq[j] -= 1
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def repeatLimitedString(s: String, repeatLimit: Int): String = {
        val freq = new Array[Int](26)
        for (c <- s) {
            freq(c - 'a') += 1
        }
        val sb = new StringBuilder
        var cur = 25
        while (cur >= 0) {
            if (freq(cur) == 0) {
                cur -= 1
            } else {
                val use = math.min(freq(cur), repeatLimit)
                for (_ <- 0 until use) {
                    sb.append(('a' + cur).toChar)
                }
                freq(cur) -= use
                if (freq(cur) > 0) {
                    var next = cur - 1
                    while (next >= 0 && freq(next) == 0) {
                        next -= 1
                    }
                    if (next < 0) {
                        // No smaller character to break the streak
                        return sb.toString()
                    }
                    sb.append(('a' + next).toChar)
                    freq[next] -= 1
                } else {
                    cur -= 1
                }
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn repeat_limited_string(s: String, repeat_limit: i32) -> String {
        let mut freq = [0i32; 26];
        for b in s.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let limit = repeat_limit as usize;
        let mut result = String::with_capacity(s.len());
        loop {
            // find the largest character available
            let cur_opt = (0..26).rev().find(|&i| freq[i] > 0);
            let cur = match cur_opt {
                Some(c) => c,
                None => break,
            };
            // number of times we can use it consecutively
            let use_cnt = std::cmp::min(freq[cur] as usize, limit);
            for _ in 0..use_cnt {
                result.push((b'a' + cur as u8) as char);
            }
            freq[cur] -= use_cnt as i32;
            if freq[cur] == 0 {
                continue; // no need for a breaker
            }
            // need a smaller character to break the streak
            let next_opt = (0..cur).rev().find(|&i| freq[i] > 0);
            let next = match next_opt {
                Some(n) => n,
                None => break, // cannot place any more characters
            };
            result.push((b'a' + next as u8) as char);
            freq[next] -= 1;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (repeat-limited-string s repeatLimit)
  (-> string? exact-integer? string?)
  (let* ((freq (make-vector 26 0))
         (base (char->integer #\a)))
    ;; count frequencies
    (for ([i (in-range (string-length s))])
      (let* ((c (char->integer (string-ref s i)))
             (idx (- c base)))
        (vector-set! freq idx (+ (vector-ref freq idx) 1))))
    (define (add-chars n ch lst)
      (if (= n 0)
          lst
          (add-chars (- n 1) ch (cons ch lst))))
    (let loop ((cur 25) (out '()))
      (if (< cur 0)
          (list->string (reverse out))
          (let ((cnt (vector-ref freq cur)))
            (if (= cnt 0)
                (loop (- cur 1) out)
                (let* ((use (min cnt repeatLimit))
                       (ch (integer->char (+ base cur)))
                       (out2 (add-chars use ch out))
                       (remaining (- cnt use)))
                  (vector-set! freq cur remaining)
                  (if (> remaining 0)
                      ;; need a smaller breaker character
                      (let find ((j (- cur 1)))
                        (cond [(< j 0) (list->string (reverse out2))]
                              [(> (vector-ref freq j) 0)
                               (let* ((breaker-ch (integer->char (+ base j)))
                                      (out3 (cons breaker-ch out2)))
                                 (vector-set! freq j (- (vector-ref freq j) 1))
                                 (loop cur out3))]
                              [else (find (- j 1))]))
                      ;; no remaining of current char, continue with next
                      (loop cur out2)))))))))
```

## Erlang

```erlang
-spec repeat_limited_string(S :: unicode:unicode_binary(), RepeatLimit :: integer()) -> unicode:unicode_binary().
repeat_limited_string(S, RepeatLimit) ->
    FreqMap = build_freq_map(S, #{}),
    StartIdx = find_start(25, FreqMap),
    IolistRev = loop(StartIdx, FreqMap, RepeatLimit, []),
    iolist_to_binary(lists:reverse(IolistRev)).

build_freq_map(<<>>, Map) ->
    Map;
build_freq_map(<<Char, Rest/binary>>, Map) ->
    Index = Char - $a,
    Count = maps:get(Index, Map, 0),
    NewMap = maps:put(Index, Count + 1, Map),
    build_freq_map(Rest, NewMap).

find_start(-1, _) -> -1;
find_start(Idx, Map) ->
    case maps:get(Idx, Map, 0) of
        0 -> find_start(Idx - 1, Map);
        _ -> Idx
    end.

find_next(-1, _) -> -1;
find_next(Idx, Map) ->
    case maps:get(Idx, Map, 0) of
        0 -> find_next(Idx - 1, Map);
        _ -> Idx
    end.

loop(CurrentIdx, _Map, _RepeatLimit, Acc) when CurrentIdx < 0 ->
    Acc;
loop(CurrentIdx, Map, RepeatLimit, Acc) ->
    Count = maps:get(CurrentIdx, Map, 0),
    if Count == 0 ->
            loop(CurrentIdx - 1, Map, RepeatLimit, Acc);
       true ->
            Use = erlang:min(Count, RepeatLimit),
            CharCode = $a + CurrentIdx,
            BinUse = list_to_binary(lists:duplicate(Use, CharCode)),
            NewAcc = [BinUse | Acc],
            Remain = Count - Use,
            Map1 = maps:put(CurrentIdx, Remain, Map),
            case Remain of
                0 ->
                    loop(CurrentIdx - 1, Map1, RepeatLimit, NewAcc);
                _ ->
                    NextIdx = find_next(CurrentIdx - 1, Map1),
                    if NextIdx == -1 ->
                            NewAcc;
                       true ->
                            Char2 = $a + NextIdx,
                            BinBreaker = <<Char2>>,
                            Acc2 = [BinBreaker | NewAcc],
                            Count2 = maps:get(NextIdx, Map1) - 1,
                            Map2 = maps:put(NextIdx, Count2, Map1),
                            loop(CurrentIdx, Map2, RepeatLimit, Acc2)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec repeat_limited_string(s :: String.t(), repeat_limit :: integer()) :: String.t()
  def repeat_limited_string(s, repeat_limit) do
    freq =
      String.to_charlist(s)
      |> Enum.reduce(List.duplicate(0, 26), fn c, acc ->
        idx = c - ?a
        List.update_at(acc, idx, &(&1 + 1))
      end)

    build(freq, repeat_limit, [])
  end

  defp build(freq, limit, acc_rev) do
    case find_next(freq, 25) do
      nil ->
        Enum.reverse(acc_rev) |> List.to_string()

      curr_idx ->
        cnt = Enum.at(freq, curr_idx)
        use = min(cnt, limit)

        acc1 = add_chars(acc_rev, curr_idx, use)
        freq1 = List.update_at(freq, curr_idx, &(&1 - use))

        if Enum.at(freq1, curr_idx) > 0 do
          case find_next(freq1, curr_idx - 1) do
            nil ->
              Enum.reverse(acc1) |> List.to_string()

            next_idx ->
              acc2 = [next_idx + ?a | acc1]
              freq2 = List.update_at(freq1, next_idx, &(&1 - 1))
              build(freq2, limit, acc2)
          end
        else
          build(freq1, limit, acc1)
        end
    end
  end

  defp find_next(_freq, idx) when idx < 0, do: nil

  defp find_next(freq, idx) do
    if Enum.at(freq, idx) > 0, do: idx, else: find_next(freq, idx - 1)
  end

  defp add_chars(acc_rev, idx, use) do
    char = idx + ?a

    Enum.reduce(1..use, acc_rev, fn _, a -> [char | a] end)
  end
end
```
