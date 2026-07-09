# 2663. Lexicographically Smallest Beautiful String

## Cpp

```cpp
class Solution {
public:
    string smallestBeautifulString(string s, int k) {
        int n = s.size();
        const char maxChar = 'a' + k - 1;
        for (int i = n - 1; i >= 0; --i) {
            for (char c = s[i] + 1; c <= maxChar; ++c) {
                if ((i >= 1 && c == s[i - 1]) || (i >= 2 && c == s[i - 2]))
                    continue;
                string res = s.substr(0, i);
                res.push_back(c);
                bool ok = true;
                for (int j = i + 1; j < n; ++j) {
                    char ch = 'a';
                    while (true) {
                        if ((j >= 1 && ch == res[j - 1]) || (j >= 2 && ch == res[j - 2]))
                            ++ch;
                        else
                            break;
                    }
                    if (ch > maxChar) { ok = false; break; }
                    res.push_back(ch);
                }
                if (ok) return res;
            }
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String smallestBeautifulString(String s, int k) {
        int n = s.length();
        char[] ans = s.toCharArray();
        for (int i = n - 1; i >= 0; --i) {
            for (char c = (char) (ans[i] + 1); c < (char) ('a' + k); ++c) {
                if ((i >= 1 && c == ans[i - 1]) || (i >= 2 && c == ans[i - 2])) continue;
                ans[i] = c;
                boolean ok = true;
                for (int j = i + 1; j < n; ++j) {
                    char put = 'a';
                    while (put < (char) ('a' + k)) {
                        if ((j >= 1 && put == ans[j - 1]) || (j >= 2 && put == ans[j - 2])) {
                            ++put;
                        } else {
                            break;
                        }
                    }
                    if (put == (char) ('a' + k)) {
                        ok = false;
                        break;
                    }
                    ans[j] = put;
                }
                if (ok) return new String(ans);
            }
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def smallestBeautifulString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        base = [ord(ch) - ord('a') for ch in s]

        for i in range(n - 1, -1, -1):
            # try to increase position i
            for c in range(base[i] + 1, k):
                if (i >= 1 and c == base[i - 1]) or (i >= 2 and c == base[i - 2]):
                    continue
                # we can set this character, now build the rest
                res = base[:i] + [c]
                # fill positions after i with smallest possible chars
                for j in range(i + 1, n):
                    for cand in range(k):
                        if (j >= 1 and cand == res[j - 1]) or (j >= 2 and cand == res[j - 2]):
                            continue
                        res.append(cand)
                        break
                return ''.join(chr(ord('a') + x) for x in res)
        return ""
```

## Python3

```python
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        s_chars = list(s)
        max_ord = ord('a') + k
        for i in range(n - 1, -1, -1):
            start = ord(s_chars[i]) + 1
            for code in range(start, max_ord):
                c = chr(code)
                if (i >= 1 and c == s_chars[i - 1]) or (i >= 2 and c == s_chars[i - 2]):
                    continue
                # build result prefix up to i
                res = s_chars[:i] + [c]
                # fill the rest with smallest possible chars
                for j in range(i + 1, n):
                    placed = False
                    for code2 in range(ord('a'), max_ord):
                        ch = chr(code2)
                        if (j >= 1 and ch == res[j - 1]) or (j >= 2 and ch == res[j - 2]):
                            continue
                        res.append(ch)
                        placed = True
                        break
                    if not placed:
                        break
                else:
                    return ''.join(res)
        return ""
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* smallestBeautifulString(char* s, int k) {
    size_t n = strlen(s);
    char *res = (char*)malloc(n + 1);
    memcpy(res, s, n + 1); // copy including null terminator

    for (int i = (int)n - 1; i >= 0; --i) {
        for (char ch = res[i] + 1; ch < 'a' + k; ++ch) {
            if (i >= 1 && ch == res[i - 1]) continue;
            if (i >= 2 && ch == res[i - 2]) continue;

            res[i] = ch;
            int j;
            for (j = i + 1; j < (int)n; ++j) {
                char cand;
                int found = 0;
                for (cand = 'a'; cand < 'a' + k; ++cand) {
                    if (j >= 1 && cand == res[j - 1]) continue;
                    if (j >= 2 && cand == res[j - 2]) continue;
                    res[j] = cand;
                    found = 1;
                    break;
                }
                if (!found) break; // cannot fill further
            }
            if (j == (int)n) {
                return res; // successfully built answer
            }
            // otherwise, try next possible ch at position i
        }
        // restore original character before moving left
        res[i] = s[i];
    }

    free(res);
    char *empty = (char*)malloc(1);
    empty[0] = '\0';
    return empty;
}
```

## Csharp

```csharp
public class Solution {
    public string SmallestBeautifulString(string s, int k) {
        char[] arr = s.ToCharArray();
        int n = arr.Length;
        for (int i = n - 1; i >= 0; --i) {
            char original = arr[i];
            for (char c = (char)(original + 1); c < (char)('a' + k); ++c) {
                if (i > 0 && c == arr[i - 1]) continue;
                if (i > 1 && c == arr[i - 2]) continue;
                arr[i] = c;
                bool ok = true;
                for (int j = i + 1; j < n; ++j) {
                    bool placed = false;
                    for (char ch = 'a'; ch < (char)('a' + k); ++ch) {
                        if (j > 0 && ch == arr[j - 1]) continue;
                        if (j > 1 && ch == arr[j - 2]) continue;
                        arr[j] = ch;
                        placed = true;
                        break;
                    }
                    if (!placed) { ok = false; break; }
                }
                if (ok) return new string(arr);
                arr[i] = original; // revert for next candidate
            }
        }
        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var smallestBeautifulString = function(s, k) {
    const n = s.length;
    const baseCode = 'a'.charCodeAt(0);
    const maxCode = baseCode + k - 1;
    const res = s.split('');
    
    for (let i = n - 1; i >= 0; i--) {
        // original previous characters (remain unchanged)
        const prev1 = i > 0 ? res[i - 1] : null;
        const prev2 = i > 1 ? res[i - 2] : null;
        for (let code = res[i].charCodeAt(0) + 1; code <= maxCode; code++) {
            const ch = String.fromCharCode(code);
            if (ch === prev1 || ch === prev2) continue;
            // place candidate at position i
            res[i] = ch;
            let ok = true;
            // fill the rest with smallest possible characters
            for (let j = i + 1; j < n; j++) {
                let placed = false;
                for (let ccode = baseCode; ccode <= maxCode; ccode++) {
                    const c = String.fromCharCode(ccode);
                    if (j > 0 && c === res[j - 1]) continue;
                    if (j > 1 && c === res[j - 2]) continue;
                    res[j] = c;
                    placed = true;
                    break;
                }
                if (!placed) {
                    ok = false;
                    break;
                }
            }
            if (ok) return res.join('');
        }
    }
    return "";
};
```

## Typescript

```typescript
function smallestBeautifulString(s: string, k: number): string {
    const n = s.length;
    const base = 'a'.charCodeAt(0);
    const arr: number[] = new Array(n);
    for (let i = 0; i < n; ++i) arr[i] = s.charCodeAt(i) - base;

    for (let i = n - 1; i >= 0; --i) {
        for (let c = arr[i] + 1; c < k; ++c) {
            if (i >= 1 && c === arr[i - 1]) continue;
            if (i >= 2 && c === arr[i - 2]) continue;

            const res: number[] = arr.slice(0, i);
            res.push(c);

            // fill the rest with smallest possible characters
            for (let j = i + 1; j < n; ++j) {
                for (let d = 0; d < k; ++d) {
                    if (j >= 1 && d === res[j - 1]) continue;
                    if (j >= 2 && d === res[j - 2]) continue;
                    res.push(d);
                    break;
                }
            }

            // convert to string
            return String.fromCharCode(...res.map(v => v + base));
        }
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function smallestBeautifulString($s, $k) {
        $n = strlen($s);
        $maxCharCode = ord('a') + $k - 1;
        $arr = str_split($s);

        for ($i = $n - 1; $i >= 0; --$i) {
            for ($c = ord($arr[$i]) + 1; $c <= $maxCharCode; ++$c) {
                $ch = chr($c);
                if ($i > 0 && $ch === $arr[$i - 1]) continue;
                if ($i > 1 && $ch === $arr[$i - 2]) continue;

                // create a copy to build the answer
                $temp = $arr;
                $temp[$i] = $ch;

                // fill the rest with the smallest possible characters
                for ($j = $i + 1; $j < $n; ++$j) {
                    for ($cand = ord('a'); $cand <= $maxCharCode; ++$cand) {
                        $cch = chr($cand);
                        if ($cch === $temp[$j - 1]) continue;
                        if ($j > 1 && $cch === $temp[$j - 2]) continue;
                        $temp[$j] = $cch;
                        break;
                    }
                }

                return implode('', $temp);
            }
        }

        return "";
    }
}
```

## Swift

```swift
class Solution {
    func smallestBeautifulString(_ s: String, _ k: Int) -> String {
        // Convert string to array of integer codes (0 for 'a', 1 for 'b', ...)
        var arr = s.unicodeScalars.map { Int($0.value - UnicodeScalar("a").value) }
        let n = arr.count
        
        // Iterate from right to left trying to increase a position
        for i in stride(from: n - 1, through: 0, by: -1) {
            if arr[i] + 1 >= k { continue } // no larger character possible here
            var candidateFound = false
            for c in (arr[i] + 1)..<k {
                // Check palindrome constraints with previous two characters
                if i >= 1 && c == arr[i - 1] { continue }
                if i >= 2 && c == arr[i - 2] { continue }
                
                // Set the increased character
                arr[i] = c
                // Fill the suffix with the smallest possible characters
                var j = i + 1
                while j < n {
                    for d in 0..<k {
                        if j >= 1 && d == arr[j - 1] { continue }
                        if j >= 2 && d == arr[j - 2] { continue }
                        arr[j] = d
                        break
                    }
                    j += 1
                }
                
                candidateFound = true
                break
            }
            if candidateFound {
                // Build result string from integer codes
                let result = String(arr.map { Character(UnicodeScalar($0 + 97)!) })
                return result
            }
        }
        // No valid larger beautiful string exists
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestBeautifulString(s: String, k: Int): String {
        val n = s.length
        val maxCode = 'a'.code + k - 1

        for (i in n - 1 downTo 0) {
            val startCode = s[i].code + 1
            for (cCode in startCode..maxCode) {
                val c = cCode.toChar()
                if (i >= 1 && c == s[i - 1]) continue
                if (i >= 2 && c == s[i - 2]) continue

                val res = CharArray(n)
                // copy prefix unchanged
                for (p in 0 until i) {
                    res[p] = s[p]
                }
                res[i] = c

                var possible = true
                for (j in i + 1 until n) {
                    var placed = false
                    for (chCode in 'a'.code..maxCode) {
                        val ch = chCode.toChar()
                        if (j >= 1 && ch == res[j - 1]) continue
                        if (j >= 2 && ch == res[j - 2]) continue
                        res[j] = ch
                        placed = true
                        break
                    }
                    if (!placed) {
                        possible = false
                        break
                    }
                }

                if (possible) return String(res)
            }
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String smallestBeautifulString(String s, int k) {
    List<int> arr = s.codeUnits;
    int n = arr.length;
    int base = 'a'.codeUnitAt(0);
    for (int i = n - 1; i >= 0; --i) {
      int original = arr[i];
      for (int nxt = original + 1; nxt < base + k; ++nxt) {
        if ((i - 1 >= 0 && nxt == arr[i - 1]) ||
            (i - 2 >= 0 && nxt == arr[i - 2])) continue;
        arr[i] = nxt;
        bool ok = true;
        for (int j = i + 1; j < n; ++j) {
          int chosen = -1;
          for (int c = base; c < base + k; ++c) {
            if ((j - 1 >= 0 && c == arr[j - 1]) ||
                (j - 2 >= 0 && c == arr[j - 2])) continue;
            chosen = c;
            break;
          }
          if (chosen == -1) {
            ok = false;
            break;
          }
          arr[j] = chosen;
        }
        if (ok) return String.fromCharCodes(arr);
      }
    }
    return "";
  }
}
```

## Golang

```go
func smallestBeautifulString(s string, k int) string {
    n := len(s)
    maxChar := byte('a' + k - 1)
    arr := []byte(s)

    for i := n - 1; i >= 0; i-- {
        for c := arr[i] + 1; c <= maxChar; c++ {
            if (i >= 1 && c == arr[i-1]) || (i >= 2 && c == arr[i-2]) {
                continue
            }
            arr[i] = c
            ok := true
            for j := i + 1; j < n; j++ {
                placed := false
                for ch := byte('a'); ch <= maxChar; ch++ {
                    if (j >= 1 && ch == arr[j-1]) || (j >= 2 && ch == arr[j-2]) {
                        continue
                    }
                    arr[j] = ch
                    placed = true
                    break
                }
                if !placed {
                    ok = false
                    break
                }
            }
            if ok {
                return string(arr)
            }
        }
    }
    return ""
}
```

## Ruby

```ruby
def smallest_beautiful_string(s, k)
  n = s.length
  letters = (0...k).map { |i| ('a'.ord + i).chr }
  s_arr = s.chars
  max_ord = 'a'.ord + k - 1

  (n - 1).downto(0) do |i|
    cur_ord = s_arr[i].ord
    ((cur_ord + 1)..max_ord).each do |new_ord|
      c = new_ord.chr
      next if i >= 1 && c == s_arr[i - 1]
      next if i >= 2 && c == s_arr[i - 2]

      res = s_arr[0...i] + [c]
      success = true

      (i + 1).upto(n - 1) do |j|
        placed = false
        letters.each do |ch|
          next if j >= 1 && ch == res[j - 1]
          next if j >= 2 && ch == res[j - 2]
          res << ch
          placed = true
          break
        end
        unless placed
          success = false
          break
        end
      end

      return res.join if success
    end
  end

  ""
end
```

## Scala

```scala
object Solution {
    def smallestBeautifulString(s: String, k: Int): String = {
        val n = s.length
        val arr = s.toCharArray
        val aCode = 'a'.toInt
        for (i <- (n - 1) to 0 by -1) {
            var nextCode = arr(i).toInt + 1
            while (nextCode < aCode + k) {
                val c = nextCode.toChar
                if ((i >= 1 && c == arr(i - 1)) || (i >= 2 && c == arr(i - 2))) {
                    // invalid, try next character
                } else {
                    val res = new Array[Char](n)
                    var p = 0
                    while (p < i) { res(p) = arr(p); p += 1 }
                    res(i) = c
                    var j = i + 1
                    while (j < n) {
                        var chCode = aCode
                        var placed = false
                        while (!placed && chCode < aCode + k) {
                            val ch = chCode.toChar
                            if ((j >= 1 && ch == res(j - 1)) || (j >= 2 && ch == res(j - 2))) {
                                // skip
                            } else {
                                res(j) = ch
                                placed = true
                            }
                            chCode += 1
                        }
                        j += 1
                    }
                    return new String(res)
                }
                nextCode += 1
            }
        }
        ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_beautiful_string(s: String, k: i32) -> String {
        let n = s.len();
        let mut bytes = s.into_bytes();
        let max_c = b'a' + (k as u8) - 1;
        for i in (0..n).rev() {
            let start = bytes[i] + 1;
            if start > max_c {
                continue;
            }
            for ch in start..=max_c {
                if i >= 1 && ch == bytes[i - 1] {
                    continue;
                }
                if i >= 2 && ch == bytes[i - 2] {
                    continue;
                }
                bytes[i] = ch;
                for j in i + 1..n {
                    for c in b'a'..=max_c {
                        if j >= 1 && c == bytes[j - 1] {
                            continue;
                        }
                        if j >= 2 && c == bytes[j - 2] {
                            continue;
                        }
                        bytes[j] = c;
                        break;
                    }
                }
                return String::from_utf8(bytes).unwrap();
            }
        }
        "".to_string()
    }
}
```

## Racket

```racket
(define/contract (smallest-beautiful-string s k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length s))
         (a-code (char->integer #\a)))
    (let loop-i ((i (- n 1)))
      (if (< i 0)
          ""                                   ; no answer
          (let ((orig (+ (- (char->integer (string-ref s i)) a-code) 0))))
            (let try-c ((c (+ orig 1)))
              (cond
                [(> c (- k 1))
                 (loop-i (- i 1))]
                [else
                 (if (or (and (>= i 1)
                              (= c (+ (- (char->integer (string-ref s (- i 1))) a-code) 0)))
                         (and (>= i 2)
                              (= c (+ (- (char->integer (string-ref s (- i 2))) a-code) 0))))
                     (try-c (+ c 1))               ; violates palindrome condition
                     (let ((res (make-vector n #\a))) ; placeholder init
                       ;; copy unchanged prefix
                       (for ([idx i])
                         (vector-set! res idx (string-ref s idx)))
                       ;; set increased character at position i
                       (vector-set! res i (integer->char (+ a-code c)))
                       ;; fill the rest with minimal valid characters
                       (let fill ((j (+ i 1)))
                         (when (< j n)
                           (let inner ((cand 0))
                             (cond
                               [(>= cand k) (error "unreachable")]
                               [else
                                (if (or (and (>= j 1)
                                             (= cand (+ (- (char->integer (vector-ref res (- j 1))) a-code) 0)))
                                        (and (>= j 2)
                                             (= cand (+ (- (char->integer (vector-ref res (- j 2))) a-code) 0))))
                                    (inner (+ cand 1))
                                    (begin
                                      (vector-set! res j (integer->char (+ a-code cand)))
                                      (fill (+ j 1))))]))))
                       ;; convert vector to string and return
                       (list->string (vector->list res)))]))]))))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_beautiful_string/2]).

-spec smallest_beautiful_string(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
smallest_beautiful_string(S, K) ->
    Chars = binary_to_list(S),
    N = length(Chars),
    MaxChar = $a + K - 1,
    Arr = array:from_list(Chars), % zero‑based indexing
    case find_i(N-1, Arr, MaxChar, Chars) of
        {ok, ResultList} -> list_to_binary(ResultList);
        error -> <<>>
    end.

%% search position from right to left
find_i(-1, _Arr, _MaxChar, _Orig) ->
    error;
find_i(I, Arr, MaxChar, Orig) ->
    OrigChar = array:get(I, Arr),
    Prev = if I >= 1 -> array:get(I-1, Arr); true -> -1 end,
    Prev2 = if I >= 2 -> array:get(I-2, Arr); true -> -1 end,
    try_candidates(OrigChar + 1, MaxChar, I, Prev, Prev2, Arr, Orig).

%% try increasing current position with possible candidates
try_candidates(Cand, MaxChar, _I, _Prev, _Prev2, _Arr, _Orig) when Cand > MaxChar ->
    % no candidate works here, move left
    find_i(_I-1, _Arr, MaxChar, _Orig);
try_candidates(Cand, MaxChar, I, Prev, Prev2, Arr, Orig) ->
    case invalid_candidate(Cand, Prev, Prev2) of
        true ->
            try_candidates(Cand + 1, MaxChar, I, Prev, Prev2, Arr, Orig);
        false ->
            N = length(Orig),
            case fill_rest_rev(I + 1, N, Cand, Prev, MaxChar, []) of
                {ok, Filled} ->
                    Prefix = lists:sublist(Orig, I),
                    Result = Prefix ++ [Cand] ++ Filled,
                    {ok, Result};
                error ->
                    try_candidates(Cand + 1, MaxChar, I, Prev, Prev2, Arr, Orig)
            end
    end.

invalid_candidate(C, Prev, Prev2) ->
    (C =:= Prev) orelse (Prev2 =/= -1 andalso C =:= Prev2).

%% fill the suffix greedily, building list in reverse for tail recursion
fill_rest_rev(Pos, N, _PrevChar, _PrevPrev, _MaxChar, Acc) when Pos == N ->
    {ok, lists:reverse(Acc)};
fill_rest_rev(Pos, N, PrevChar, PrevPrev, MaxChar, Acc) ->
    C = smallest_valid($a, MaxChar, PrevChar, PrevPrev),
    if
        C =:= -1 -> error;
        true -> fill_rest_rev(Pos + 1, N, C, PrevChar, MaxChar, [C | Acc])
    end.

%% find the smallest character not equal to the two previous ones
smallest_valid(Cur, MaxChar, _Prev, _Prev2) when Cur > MaxChar ->
    -1;
smallest_valid(Cur, MaxChar, Prev, Prev2) ->
    case (Cur =/= Prev) andalso (Prev2 == -1 orelse Cur =/= Prev2) of
        true -> Cur;
        false -> smallest_valid(Cur + 1, MaxChar, Prev, Prev2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_beautiful_string(s :: String.t(), k :: integer) :: String.t()
  def smallest_beautiful_string(s, k) do
    chars = String.to_charlist(s)
    tup = List.to_tuple(chars)
    n = tuple_size(tup)
    max_c = ?a + k - 1

    result =
      Enum.reduce_while((n - 1)..0, nil, fn i, _acc ->
        prev1 = get_char(tup, i - 1)
        prev2 = get_char(tup, i - 2)
        cur = get_char(tup, i)

        candidate =
          Enum.find((cur + 1)..max_c, fn c -> c != prev1 and c != prev2 end)

        if candidate do
          prefix =
            if i > 0 do
              for idx <- 0..(i - 1), do: elem(tup, idx + 1)
            else
              []
            end

          tail = build_tail(i + 1, n, max_c, candidate, prev1, [])
          final = prefix ++ [candidate] ++ tail
          {:halt, List.to_string(final)}
        else
          {:cont, nil}
        end
      end)

    case result do
      nil -> ""
      str -> str
    end
  end

  defp get_char(_tup, idx) when idx < 0, do: nil
  defp get_char(tup, idx), do: elem(tup, idx + 1)

  defp build_tail(pos, total_len, max_c, prev1, prev2, acc) do
    if pos == total_len do
      Enum.reverse(acc)
    else
      c = find_smallest(prev1, prev2, max_c)
      build_tail(pos + 1, total_len, max_c, c, prev1, [c | acc])
    end
  end

  defp find_smallest(prev1, prev2, max_c) do
    Enum.find(?a..max_c, fn c -> c != prev1 and c != prev2 end)
  end
end
```
