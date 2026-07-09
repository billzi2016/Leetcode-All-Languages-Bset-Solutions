# 3614. Process String with Special Operations II

## Cpp

```cpp
class Solution {
public:
    char processStr(string s, long long k) {
        const long long INF = (long long)4e18;
        int n = s.size();
        vector<long long> lenAfter(n);
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            if ('a' <= c && c <= 'z') {
                if (cur < INF) ++cur;
            } else if (c == '#') {
                if (cur > INF/2) cur = INF;
                else cur = cur * 2;
            } else if (c == '%') {
                // length unchanged
            } else if (c == '*') {
                if (cur > 0) --cur;
            }
            lenAfter[i] = cur;
        }
        if (k >= cur) return '.';
        long long target = k;
        for (int i = n - 1; i >= 0; --i) {
            char c = s[i];
            long long afterLen = lenAfter[i];
            long long beforeLen = (i == 0 ? 0 : lenAfter[i - 1]);
            if ('a' <= c && c <= 'z') {
                // letter appended at the end
                if (target == beforeLen) return c;
                // otherwise target stays same
            } else if (c == '#') {
                if (beforeLen > 0)
                    target %= beforeLen;
            } else if (c == '%') {
                if (beforeLen > 0)
                    target = beforeLen - 1 - target;
            } else if (c == '*') {
                // backspace: no change to target
                // nothing needed
            }
        }
        return '.';
    }
};
```

## Java

```java
class Solution {
    public char processStr(String s, long k) {
        int n = s.length();
        long[] len = new long[n];
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            long prev = (i == 0) ? 0L : len[i - 1];
            long cur;
            if (ch == '#') { // duplicate
                cur = prev * 2;
            } else if (ch == '%') { // reverse, length unchanged
                cur = prev;
            } else if (ch == '*') { // backspace
                cur = prev > 0 ? prev - 1 : 0;
            } else { // letter
                cur = prev + 1;
            }
            len[i] = cur;
        }

        long totalLen = n == 0 ? 0L : len[n - 1];
        if (k >= totalLen) return '.';

        long curK = k;
        for (int i = n - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            long prev = (i == 0) ? 0L : len[i - 1];
            if (ch == '#') { // duplicate, undo by modulo
                if (prev > 0) {
                    curK %= prev;
                }
            } else if (ch == '%') { // reverse, mirror index
                curK = prev - 1 - curK;
            } else if (ch == '*') {
                // backspace, no change needed for indices within remaining string
            } else { // letter
                if (curK == prev) {
                    return ch;
                }
                // otherwise continue searching in earlier part
            }
        }
        return '.';
    }
}
```

## Python

```python
class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        lengths = [0] * n
        cur_len = 0
        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                cur_len += 1
            elif ch == '#':
                cur_len <<= 1  # double
            elif ch == '%':
                pass  # length unchanged
            elif ch == '*':
                if cur_len:
                    cur_len -= 1
            lengths[i] = cur_len

        if k >= cur_len:
            return '.'

        for i in range(n - 1, -1, -1):
            op = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0
            if 'a' <= op <= 'z':
                # letter added at the end
                if k == prev_len:
                    return op
                # otherwise continue with same k
            elif op == '#':
                if prev_len != 0:
                    k %= prev_len
            elif op == '%':
                # reverse whole string
                k = prev_len - 1 - k
            elif op == '*':
                # deletion does not affect indices of remaining characters
                pass

        return '.'
```

## Python3

```python
class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * (n + 1)
        cur_len = 0
        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                cur_len += 1
            elif ch == '*':
                if cur_len > 0:
                    cur_len -= 1
            elif ch == '#':
                cur_len *= 2
            # '%' does not change length
            lengths[i + 1] = cur_len

        total_len = lengths[n]
        if k >= total_len:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i]

            if ch == '#':
                if prev_len > 0:
                    k %= prev_len
            elif ch == '%':
                if prev_len > 0:
                    k = (prev_len - 1) - k
            elif ch == '*':
                # deletion does not affect index mapping
                pass
            else:  # letter
                if k == prev_len:
                    return ch
                # otherwise continue with same k

        return '.'
```

## C

```c
char processStr(char* s, long long k) {
    int n = 0;
    while (s[n] != '\0') ++n;
    unsigned long long *pref = (unsigned long long*)malloc((n + 1) * sizeof(unsigned long long));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (c >= 'a' && c <= 'z') {
            pref[i + 1] = pref[i] + 1;
        } else if (c == '%' || c == '#') {
            pref[i + 1] = pref[i] * 2;
        } else { // '*'
            pref[i + 1] = pref[i];
        }
    }
    unsigned long long total = pref[n];
    if (k < 0 || (unsigned long long)k >= total) {
        free(pref);
        return '.';
    }
    unsigned long long idx = (unsigned long long)k;
    for (int i = n - 1; i >= 0; --i) {
        char c = s[i];
        unsigned long long curLen = pref[i + 1];
        unsigned long long prevLen = pref[i];
        if (c >= 'a' && c <= 'z') {
            if (idx == prevLen) {
                free(pref);
                return c;
            }
        } else if (c == '*') {
            idx = curLen - 1 - idx;
        } else if (c == '%') { // duplicate
            unsigned long long half = prevLen; // curLen = 2 * prevLen
            if (idx >= half) idx -= half;
        } else if (c == '#') { // append reverse copy
            unsigned long long half = prevLen;
            if (idx >= half) idx = curLen - 1 - idx;
        }
    }
    free(pref);
    return '.';
}
```

## Csharp

```csharp
using System;

public class Solution {
    public char ProcessStr(string s, long k) {
        int n = s.Length;
        long[] len = new long[n];
        for (int i = 0; i < n; i++) {
            char c = s[i];
            long prev = i == 0 ? 0L : len[i - 1];
            long cur;
            if (c == '#') {
                cur = prev * 2;
            } else if (c == '%') {
                cur = prev;
            } else if (c == '*') {
                cur = prev > 0 ? prev - 1 : 0;
            } else { // letter
                cur = prev + 1;
            }
            len[i] = cur;
        }

        long totalLen = n == 0 ? 0L : len[n - 1];
        if (k < 0 || k >= totalLen) return '.';

        long idx = k;
        for (int i = n - 1; i >= 0; i--) {
            char c = s[i];
            long before = i == 0 ? 0L : len[i - 1];

            if (c == '#') {
                if (idx >= before) {
                    idx %= before;
                }
            } else if (c == '%') {
                idx = before - 1 - idx;
            } else if (c == '*') {
                // no change needed
            } else { // letter
                if (idx == before) {
                    return c;
                }
                // otherwise continue with same idx
            }
        }

        return '.';
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {character}
 */
var processStr = function(s, k) {
    const n = s.length;
    const INF = 1e15; // maximum possible length per constraints
    const len = new Array(n + 1);
    len[0] = 0;
    for (let i = 0; i < n; ++i) {
        const ch = s[i];
        const prev = len[i];
        let cur;
        if (ch === '#') {
            // duplicate the current string
            cur = prev * 2;
        } else if (ch === '%') {
            // reverse does not change length
            cur = prev;
        } else if (ch === '*') {
            // delete last character if any
            cur = Math.max(prev - 1, 0);
        } else {
            // regular letter
            cur = prev + 1;
        }
        len[i + 1] = cur > INF ? INF : cur;
    }

    const totalLen = len[n];
    if (k >= totalLen) return '.';

    for (let i = n - 1; i >= 0; --i) {
        const ch = s[i];
        const prev = len[i];
        if (ch === '#') {
            // second copy maps back to first via modulo
            if (k >= prev) {
                k %= prev;
            }
        } else if (ch === '%') {
            // reverse: mirror index
            k = prev - 1 - k;
        } else if (ch === '*') {
            // backspace: nothing to adjust, indices stay the same
        } else {
            // letter
            if (k === prev) {
                return ch;
            }
            // otherwise continue; k unchanged
        }
    }
    return '.';
};
```

## Typescript

```typescript
function processStr(s: string, k: number): string {
    const n = s.length;
    const pref = new Array<number>(n + 1);
    pref[0] = 0;
    for (let i = 0; i < n; i++) {
        const ch = s[i];
        let len = pref[i];
        if (ch >= 'a' && ch <= 'z') {
            len += 1;
        } else if (ch === '#') {
            len = len * 2;
        } else if (ch === '*') {
            if (len > 0) len -= 1;
        } // '%' does nothing to length
        pref[i + 1] = len;
    }
    const totalLen = pref[n];
    if (k < 0 || k >= totalLen) return '.';
    let idx = k;
    let curLen = totalLen;
    for (let i = n - 1; i >= 0; i--) {
        const ch = s[i];
        const prevLen = pref[i];
        if (ch >= 'a' && ch <= 'z') {
            // letter appended at the end
            if (idx === curLen - 1) return ch;
            curLen = prevLen; // move to previous length
        } else if (ch === '#') {
            const half = prevLen;
            if (idx >= half) idx %= half;
            curLen = prevLen;
        } else if (ch === '%') {
            idx = curLen - 1 - idx;
            curLen = prevLen;
        } else if (ch === '*') {
            // revert deletion
            curLen = prevLen;
        }
    }
    return '.';
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
    function processStr($s, $k) {
        $n = strlen($s);
        $lens = [];
        $len = 0;
        for ($i = 0; $i < $n; ++$i) {
            $c = $s[$i];
            if ($c >= 'a' && $c <= 'z') {
                $len += 1;
            } elseif ($c === '#') {
                $len *= 2;
            } elseif ($c === '%') {
                // reverse does not change length
            } elseif ($c === '*') {
                if ($len > 0) $len -= 1;
            }
            $lens[$i] = $len;
        }

        if ($k >= $len) return '.';

        $curK = $k;
        for ($i = $n - 1; $i >= 0; --$i) {
            $c = $s[$i];
            $prevLen = ($i > 0) ? $lens[$i - 1] : 0;

            if ($c >= 'a' && $c <= 'z') {
                if ($curK == $prevLen) {
                    return $c;
                }
                // otherwise continue with same curK
            } elseif ($c === '#') {
                if ($prevLen > 0) {
                    $curK = $curK % $prevLen;
                }
            } elseif ($c === '%') {
                if ($prevLen > 0) {
                    $curK = $prevLen - 1 - $curK;
                }
            } elseif ($c === '*') {
                // deletion does not affect index mapping for remaining characters
                // nothing to do
            }
        }

        return '.';
    }
}
```

## Swift

```swift
class Solution {
    func processStr(_ s: String, _ k: Int) -> Character {
        let chars = Array(s)
        let n = chars.count
        var preLen = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            let ch = chars[i]
            var len = preLen[i]
            if ch == "#" {
                len = len * 2
            } else if ch == "%" {
                // length unchanged
            } else if ch == "*" {
                if len > 0 { len -= 1 }
            } else {
                // lowercase letter
                len += 1
            }
            preLen[i + 1] = len
        }
        var curK = Int64(k)
        let finalLen = preLen[n]
        if curK < 0 || curK >= finalLen {
            return Character(".")
        }
        for i in stride(from: n - 1, through: 0, by: -1) {
            let ch = chars[i]
            let before = preLen[i]
            switch ch {
            case "#":
                if before > 0 && curK >= before {
                    curK = curK % before
                }
            case "%":
                if before > 0 {
                    curK = before - 1 - curK
                }
            case "*":
                // deletion does not affect index mapping when walking backwards
                break
            default:
                // lowercase letter
                if curK == before {
                    return ch
                }
            }
        }
        return Character(".")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun processStr(s: String, k: Long): Char {
        val n = s.length
        val len = LongArray(n)
        var cur = 0L
        for (i in 0 until n) {
            when (s[i]) {
                '*' -> if (cur > 0) cur--
                '#' -> cur = cur * 2
                '%' -> { /* length unchanged */ }
                else -> cur++
            }
            len[i] = cur
        }
        if (k >= cur) return '.'
        var pos = k
        for (i in n - 1 downTo 0) {
            val ch = s[i]
            val prevLen = if (i == 0) 0L else len[i - 1]
            when (ch) {
                '*' -> {
                    // deletion, position unchanged
                }
                '#' -> {
                    if (prevLen > 0) {
                        pos %= prevLen
                    }
                }
                '%' -> {
                    if (prevLen > 0) {
                        pos = prevLen - 1 - pos
                    }
                }
                else -> { // letter
                    val addedIdx = prevLen
                    if (pos == addedIdx) return ch
                    // otherwise continue with same pos
                }
            }
        }
        return '.'
    }
}
```

## Dart

```dart
class Solution {
  String processStr(String s, int k) {
    const int INF = 1 << 60;
    int n = s.length;
    List<int> lens = List.filled(n, 0);
    int cur = 0;
    for (int i = 0; i < n; i++) {
      String ch = s[i];
      if (ch != '#' && ch != '%' && ch != '*') {
        cur += 1;
      } else if (ch == '*') {
        if (cur > 0) cur -= 1;
      } else { // '#' or '%'
        if (ch == '#') {
          if (cur > INF) {
            cur = INF;
          } else {
            cur = cur * 2;
            if (cur > INF) cur = INF;
          }
        }
        // '%' does not change length
      }
      lens[i] = cur;
    }

    int total = cur;
    if (k < 0 || k >= total) return '.';

    for (int i = n - 1; i >= 0; i--) {
      String ch = s[i];
      int lenAfter = lens[i];
      if (ch != '#' && ch != '%' && ch != '*') {
        int lenBefore = lenAfter - 1;
        if (k == lenBefore) return ch;
        // else continue, k unchanged
      } else if (ch == '*') {
        // before deletion length was one more; indices of remaining chars stay same
        // no change to k
      } else if (ch == '#') {
        int prev = lenAfter ~/ 2;
        if (k >= prev) {
          k %= prev;
        }
        // continue with reduced length
      } else { // '%'
        // reversal: mirror index
        k = (lenAfter - 1) - k;
      }
    }
    return '.';
  }
}
```

## Golang

```go
func processStr(s string, k int64) byte {
    n := len(s)
    const INF int64 = 1 << 60
    lens := make([]int64, n+1)

    for i := 0; i < n; i++ {
        ch := s[i]
        prev := lens[i]
        switch ch {
        case '*':
            if prev > 0 {
                lens[i+1] = prev - 1
            } else {
                lens[i+1] = 0
            }
        case '#':
            if prev > INF/2 {
                lens[i+1] = INF
            } else {
                lens[i+1] = prev * 2
            }
        case '%':
            lens[i+1] = prev
        default: // letter
            lens[i+1] = prev + 1
        }
    }

    total := lens[n]
    if k < 0 || k >= total {
        return '.'
    }

    curK := k
    for i := n - 1; i >= 0; i-- {
        ch := s[i]
        prev := lens[i]

        switch ch {
        case '*':
            // deletion does not affect index mapping backward
        case '#':
            if prev == 0 {
                continue
            }
            if curK >= prev {
                curK -= prev
            }
        case '%':
            if prev > 0 {
                curK = prev - 1 - curK
            }
        default: // letter
            if curK == prev {
                return ch
            }
        }
    }

    return '.'
}
```

## Ruby

```ruby
def process_str(s, k)
  n = s.length
  len = Array.new(n + 1, 0)

  (0...n).each do |i|
    ch = s[i]
    case ch
    when '#', '%'
      len[i + 1] = len[i] * 2
    when '*'
      len[i + 1] = len[i] > 0 ? len[i] - 1 : 0
    else
      len[i + 1] = len[i] + 1
    end
  end

  return '.' if k >= len[n]

  i = n - 1
  while i >= 0
    ch = s[i]
    prev_len = len[i]

    case ch
    when 'a'..'z'
      return ch if k == prev_len
    when '#'
      if prev_len > 0 && k >= prev_len
        k %= prev_len
      end
    when '%'
      if prev_len > 0 && k >= prev_len
        k = prev_len - 1 - (k - prev_len)
      end
    else # '*'
      # no change to k
    end

    i -= 1
  end

  '.'
end
```

## Scala

```scala
object Solution {
    def processStr(s: String, k: Long): Char = {
        val n = s.length
        val lens = new Array[Long](n)
        var curLen = 0L
        for (i <- 0 until n) {
            s.charAt(i) match {
                case c if c >= 'a' && c <= 'z' =>
                    curLen += 1
                case '#' =>
                    curLen = curLen * 2
                case '%' => // reverse, length unchanged
                case '*' =>
                    if (curLen > 0) curLen -= 1
            }
            lens(i) = curLen
        }
        if (k >= curLen) return '.'
        var idx = k
        for (i <- (n - 1) to 0 by -1) {
            val c = s.charAt(i)
            val lenPrev = if (i > 0) lens(i - 1) else 0L
            c match {
                case ch if ch >= 'a' && ch <= 'z' =>
                    if (idx == lenPrev) return ch
                case '#' =>
                    if (lenPrev != 0) idx = idx % lenPrev
                case '%' =>
                    idx = lenPrev - 1 - idx
                case '*' => // no change needed
            }
        }
        '.'
    }
}
```

## Rust

```rust
impl Solution {
    pub fn process_str(s: String, k: i64) -> char {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut lens = vec![0i64; n];
        let mut cur: i64 = 0;
        for (i, &ch) in chars.iter().enumerate() {
            match ch {
                'a'..='z' => {
                    cur += 1;
                }
                '#' => {
                    cur *= 2;
                }
                '%' => {
                    // length unchanged
                }
                '*' => {
                    if cur > 0 {
                        cur -= 1;
                    }
                }
                _ => {}
            }
            lens[i] = cur;
        }
        let total_len = cur;
        if k < 0 || k >= total_len {
            return '.';
        }
        let mut idx = k;
        for i in (0..n).rev() {
            let ch = chars[i];
            let prev_len = if i == 0 { 0 } else { lens[i - 1] };
            match ch {
                'a'..='z' => {
                    if idx == prev_len {
                        return ch;
                    }
                }
                '#' => {
                    if idx >= prev_len {
                        idx -= prev_len;
                    }
                }
                '%' => {
                    idx = prev_len - 1 - idx;
                }
                '*' => {
                    // no change needed
                }
                _ => {}
            }
        }
        '.'
    }
}
```

## Racket

```racket
(define/contract (process-str s k)
  (-> string? exact-integer? char?)
  (let* ([n (string-length s)]
         [len (make-vector (+ n 1) 0)])
    ;; forward pass: compute lengths after each operation
    (for ([i (in-range n)])
      (let* ([ch (string-ref s i)]
             [prev (vector-ref len i)]
             [new
              (cond [(char-alphabetic? ch) (+ prev 1)]
                    [(char=? ch #\*) (if (> prev 0) (- prev 1) 0)]
                    [(char=? ch #\#) (* prev 2)]
                    [(char=? ch #\%) prev]
                    [else prev])])
        (vector-set! len (+ i 1) new)))
    (let ([total (vector-ref len n)])
      (if (>= k total)
          #\.
          ;; backward walk to locate the character
          (let loop ((i n) (idx k))
            (if (= i 0)
                #\. ; should not happen
                (let* ([ch (string-ref s (- i 1))]
                       [prev (vector-ref len (- i 1))])
                  (cond [(char-alphabetic? ch)
                         (if (= idx prev)
                             ch
                             (loop (- i 1) idx))]
                        [(char=? ch #\*)
                         (loop (- i 1) idx)]
                        [(char=? ch #\#)
                         (let ([new-idx (modulo idx prev)])
                           (loop (- i 1) new-idx))]
                        [(char=? ch #\%)
                         (let ([new-idx (- prev 1 idx)])
                           (loop (- i 1) new-idx))]
                        [else
                         (loop (- i 1) idx)])))))))))
```

## Erlang

```erlang
-spec process_str(S :: unicode:unicode_binary(), K :: integer()) -> char().
process_str(S, K) ->
    Ops = build_ops(S, 0, []),
    TotalLen =
        case Ops of
            [] -> 0;
            [{_, L} | _] -> L
        end,
    if
        K >= TotalLen -> $.;
        true -> find_char(lists:reverse(Ops), K)
    end.

build_ops(<<>>, _Len, Acc) ->
    lists:reverse(Acc);
build_ops(<<C, Rest/binary>>, Len, Acc) when C >= $a, C =< $z ->
    NewLen = Len + 1,
    build_ops(Rest, NewLen, [{ {letter, C}, NewLen } | Acc]);
build_ops(<<$#, Rest/binary>>, Len, Acc) ->
    NewLen = Len * 2,
    build_ops(Rest, NewLen, [{ hash, NewLen } | Acc]);
build_ops(<<$%, Rest/binary>>, Len, Acc) ->
    NewLen = Len,
    build_ops(Rest, NewLen, [{ percent, NewLen } | Acc]);
build_ops(<<$*, Rest/binary>>, Len, Acc) ->
    NewLen = Len - 1,
    build_ops(Rest, NewLen, [{ star, NewLen } | Acc]).

find_char([], _K) -> $.;
find_char([{Op, CurLen} | Rest], K) ->
    case Op of
        {letter, Char} ->
            PrevLen = CurLen - 1,
            if K == PrevLen -> Char; true -> find_char(Rest, K) end;
        hash ->
            PrevLen = CurLen div 2,
            NewK = 
                case PrevLen of
                    0 -> 0;
                    _ -> K rem PrevLen
                end,
            find_char(Rest, NewK);
        percent ->
            NewK = CurLen - 1 - K,
            find_char(Rest, NewK);
        star ->
            find_char(Rest, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec process_str(String.t(), integer()) :: char()
  def process_str(s, k) do
    # Build list of steps with previous length for each character (in reverse order)
    {steps_rev, total_len} =
      String.graphemes(s)
      |> Enum.reduce({[], 0}, fn ch, {acc, len_before} ->
        prev = len_before

        new_len =
          case ch do
            "#" -> prev * 2
            "%" -> prev
            "*" -> if prev > 0, do: prev - 1, else: 0
            _ -> prev + 1
          end

        {[{ch, prev} | acc], new_len}
      end)

    if k >= total_len do
      "."
    else
      resolve(steps_rev, k)
    end
  end

  defp resolve([], _k), do: "."

  defp resolve([{ch, prev_len} | rest], k) do
    cond do
      ch == "#" ->
        new_k = if prev_len == 0, do: 0, else: rem(k, prev_len)
        resolve(rest, new_k)

      ch == "%" ->
        new_k = prev_len - 1 - k
        resolve(rest, new_k)

      ch == "*" ->
        resolve(rest, k)

      true -> # lowercase letter
        if k == prev_len do
          ch
        else
          resolve(rest, k)
        end
    end
  end
end
```
