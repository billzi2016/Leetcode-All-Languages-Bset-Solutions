# 2434. Using a Robot to Print the Lexicographically Smallest String

## Cpp

```cpp
class Solution {
public:
    string robotWithString(string s) {
        int n = s.size();
        vector<char> minSuf(n);
        minSuf[n - 1] = s[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            minSuf[i] = std::min(s[i], minSuf[i + 1]);
        }
        string ans;
        vector<char> st;
        st.reserve(n);
        for (int i = 0; i < n; ++i) {
            st.push_back(s[i]);
            while (!st.empty() && (i == n - 1 || st.back() <= minSuf[i + 1])) {
                ans.push_back(st.back());
                st.pop_back();
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String robotWithString(String s) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            cnt[s.charAt(i) - 'a']++;
        }
        int minIdx = 0;
        while (minIdx < 26 && cnt[minIdx] == 0) minIdx++;

        StringBuilder stack = new StringBuilder();
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            stack.append(c);
            cnt[c - 'a']--;
            while (minIdx < 26 && cnt[minIdx] == 0) minIdx++;

            while (stack.length() > 0) {
                char top = stack.charAt(stack.length() - 1);
                if (minIdx == 26 || top <= (char) ('a' + minIdx)) {
                    res.append(top);
                    stack.deleteCharAt(stack.length() - 1);
                } else {
                    break;
                }
            }
        }

        while (stack.length() > 0) {
            res.append(stack.charAt(stack.length() - 1));
            stack.deleteCharAt(stack.length() - 1);
        }

        return res.toString();
    }
}
```

## Python

```python
class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # smallest character still remaining in s
        mi = 0
        while mi < 26 and cnt[mi] == 0:
            mi += 1

        stack = []
        res = []

        for ch in s:
            idx = ord(ch) - 97
            stack.append(ch)
            cnt[idx] -= 1

            if cnt[idx] == 0 and idx == mi:
                while mi < 26 and cnt[mi] == 0:
                    mi += 1

            # pop while top is <= smallest remaining character
            while stack and (mi == 26 or stack[-1] <= chr(97 + mi)):
                res.append(stack.pop())

        return ''.join(res)
```

## Python3

```python
class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        stack = []
        res = []
        min_idx = 0  # smallest character index still present in the remaining part of s

        for ch in s:
            idx = ord(ch) - 97
            stack.append(ch)
            cnt[idx] -= 1

            while min_idx < 26 and cnt[min_idx] == 0:
                min_idx += 1

            while stack and (min_idx == 26 or ord(stack[-1]) - 97 <= min_idx):
                res.append(stack.pop())

        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* robotWithString(char* s) {
    int n = strlen(s);
    if (n == 0) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    
    // min suffix characters
    char *minSuf = (char*)malloc(n * sizeof(char));
    for (int i = n - 1; i >= 0; --i) {
        if (i == n - 1)
            minSuf[i] = s[i];
        else
            minSuf[i] = s[i] < minSuf[i + 1] ? s[i] : minSuf[i + 1];
    }
    
    char *stack = (char*)malloc(n * sizeof(char));
    int top = -1;
    
    char *res = (char*)malloc((n + 1) * sizeof(char));
    int idx = 0;
    
    for (int i = 0; i < n; ++i) {
        stack[++top] = s[i];
        char nextMin = (i + 1 < n) ? minSuf[i + 1] : '{'; // character after 'z'
        while (top >= 0 && stack[top] <= nextMin) {
            res[idx++] = stack[top--];
        }
    }
    
    while (top >= 0) {
        res[idx++] = stack[top--];
    }
    res[idx] = '\0';
    
    free(minSuf);
    free(stack);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string RobotWithString(string s) {
        int n = s.Length;
        char[] minSuf = new char[n + 1];
        minSuf[n] = '{'; // character after 'z' in ASCII
        for (int i = n - 1; i >= 0; --i) {
            minSuf[i] = (char)Math.Min(s[i], minSuf[i + 1]);
        }

        var stack = new System.Collections.Generic.Stack<char>();
        var sb = new System.Text.StringBuilder();

        for (int i = 0; i < n; ++i) {
            stack.Push(s[i]);
            while (stack.Count > 0 && stack.Peek() <= minSuf[i + 1]) {
                sb.Append(stack.Pop());
            }
        }

        while (stack.Count > 0) {
            sb.Append(stack.Pop());
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var robotWithString = function(s) {
    const n = s.length;
    const minSuf = new Array(n);
    let cur = 'z';
    for (let i = n - 1; i >= 0; --i) {
        if (s[i] < cur) cur = s[i];
        minSuf[i] = cur;
    }
    const stack = [];
    const res = [];
    for (let i = 0; i < n; ++i) {
        stack.push(s[i]);
        while (
            stack.length &&
            (i === n - 1 || stack[stack.length - 1] <= minSuf[i + 1])
        ) {
            res.push(stack.pop());
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function robotWithString(s: string): string {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    let minIdx = 0;
    while (minIdx < 26 && freq[minIdx] === 0) minIdx++;

    const stack: string[] = [];
    const result: string[] = [];

    for (const ch of s) {
        stack.push(ch);
        const idx = ch.charCodeAt(0) - 97;
        freq[idx]--;
        while (minIdx < 26 && freq[minIdx] === 0) minIdx++;

        while (
            stack.length > 0 &&
            (minIdx === 26 ||
                stack[stack.length - 1] <= String.fromCharCode(97 + minIdx))
        ) {
            result.push(stack.pop()!);
        }
    }

    while (stack.length > 0) {
        result.push(stack.pop()!);
    }

    return result.join('');
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function robotWithString($s) {
        $n = strlen($s);
        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }
        $minIdx = 0;
        while ($minIdx < 26 && $freq[$minIdx] == 0) {
            $minIdx++;
        }
        $stack = [];
        $result = '';
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $idx = ord($c) - 97;
            $stack[] = $c;
            $freq[$idx]--;
            if ($freq[$idx] == 0 && $idx == $minIdx) {
                while ($minIdx < 26 && $freq[$minIdx] == 0) {
                    $minIdx++;
                }
            }
            while (!empty($stack)) {
                $topChar = end($stack);
                $topIdx = ord($topChar) - 97;
                if ($minIdx == 26 || $topIdx <= $minIdx) {
                    $result .= array_pop($stack);
                } else {
                    break;
                }
            }
        }
        while (!empty($stack)) {
            $result .= array_pop($stack);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func robotWithString(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return "" }
        
        // suffix minimum characters
        var suffixMin = [Character](repeating: "a", count: n)
        var curMin = chars[n - 1]
        suffixMin[n - 1] = curMin
        if n > 1 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                if chars[i] < curMin {
                    curMin = chars[i]
                }
                suffixMin[i] = curMin
            }
        }
        
        var stack = [Character]()
        var result = ""
        
        for i in 0..<n {
            stack.append(chars[i])
            let minRemaining: Character = (i + 1 < n) ? suffixMin[i + 1] : "{"
            while let last = stack.last, last <= minRemaining {
                result.append(last)
                stack.removeLast()
            }
        }
        
        // any remaining characters in the stack
        while let last = stack.popLast() {
            result.append(last)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun robotWithString(s: String): String {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        var minIdx = 0
        while (minIdx < 26 && freq[minIdx] == 0) minIdx++

        val stack = CharArray(s.length)
        var top = 0
        val result = StringBuilder()

        for (ch in s) {
            // push current character onto the stack
            stack[top++] = ch
            freq[ch - 'a']--
            while (minIdx < 26 && freq[minIdx] == 0) minIdx++

            // pop while top of stack is <= smallest remaining character
            while (top > 0 && (minIdx == 26 || stack[top - 1] <= ('a'.code + minIdx).toChar())) {
                result.append(stack[--top])
            }
        }

        // empty the remaining stack
        while (top > 0) {
            result.append(stack[--top])
        }

        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String robotWithString(String s) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      cnt[s.codeUnitAt(i) - 97]++;
    }
    int curMin = 0;
    while (curMin < 26 && cnt[curMin] == 0) curMin++;

    List<int> stack = [];
    StringBuffer sb = StringBuffer();

    for (int i = 0; i < s.length; i++) {
      int ch = s.codeUnitAt(i) - 97;
      stack.add(ch);
      cnt[ch]--;
      while (curMin < 26 && cnt[curMin] == 0) curMin++;

      while (stack.isNotEmpty) {
        int top = stack.last;
        if (curMin == 26 || top <= curMin) {
          sb.writeCharCode(top + 97);
          stack.removeLast();
        } else {
          break;
        }
      }
    }

    while (stack.isNotEmpty) {
      sb.writeCharCode(stack.removeLast() + 97);
    }

    return sb.toString();
  }
}
```

## Golang

```go
func robotWithString(s string) string {
    freq := [26]int{}
    for i := 0; i < len(s); i++ {
        freq[s[i]-'a']++
    }

    // find initial smallest remaining character index
    minIdx := 0
    for minIdx < 26 && freq[minIdx] == 0 {
        minIdx++
    }

    stack := make([]byte, 0, len(s))
    res := make([]byte, 0, len(s))

    for i := 0; i < len(s); i++ {
        ch := s[i]
        idx := ch - 'a'
        stack = append(stack, ch)
        freq[idx]--

        // update minIdx to the next smallest character still present
        for minIdx < 26 && freq[minIdx] == 0 {
            minIdx++
        }

        // pop while top of stack is <= current minimal remaining char
        for len(stack) > 0 {
            top := stack[len(stack)-1]
            if minIdx == 26 || top <= byte('a'+minIdx) {
                res = append(res, top)
                stack = stack[:len(stack)-1]
            } else {
                break
            }
        }
    }

    // any remaining characters in the stack are popped (should already be empty)
    for len(stack) > 0 {
        res = append(res, stack[len(stack)-1])
        stack = stack[:len(stack)-1]
    }

    return string(res)
}
```

## Ruby

```ruby
def robot_with_string(s)
  cnt = Array.new(26, 0)
  s.each_byte { |b| cnt[b - 97] += 1 }

  stack = []
  result = []

  # smallest character index still remaining in s
  min_idx = 0
  min_idx += 1 while min_idx < 26 && cnt[min_idx].zero?

  s.each_char do |ch|
    idx = ch.ord - 97
    cnt[idx] -= 1
    stack << ch

    # update smallest remaining character
    min_idx += 1 while min_idx < 26 && cnt[min_idx].zero?

    # pop while top of stack is <= smallest remaining char (or no chars left)
    while !stack.empty? && (min_idx == 26 || (stack[-1].ord - 97) <= min_idx)
      result << stack.pop
    end
  end

  # empty the rest of the stack
  result.concat(stack.reverse)

  result.join
end
```

## Scala

```scala
object Solution {
    def robotWithString(s: String): String = {
        val freq = new Array[Int](26)
        for (ch <- s) {
            freq(ch - 'a') += 1
        }
        var curMin = 0
        while (curMin < 26 && freq(curMin) == 0) curMin += 1

        val stack = new java.util.ArrayDeque[Char]()
        val sb = new StringBuilder

        for (ch <- s) {
            stack.push(ch)
            val idx = ch - 'a'
            freq(idx) -= 1
            while (curMin < 26 && freq(curMin) == 0) curMin += 1
            while (!stack.isEmpty && (curMin == 26 || stack.peek() <= ('a' + curMin).toChar)) {
                sb.append(stack.pop())
            }
        }

        while (!stack.isEmpty) {
            sb.append(stack.pop())
        }

        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn robot_with_string(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut cnt = [0usize; 26];
        for &b in bytes {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut cur_min = 0;
        while cur_min < 26 && cnt[cur_min] == 0 {
            cur_min += 1;
        }

        let mut stack: Vec<u8> = Vec::new();
        let mut res: Vec<u8> = Vec::with_capacity(n);

        for &b in bytes {
            stack.push(b);
            let idx = (b - b'a') as usize;
            cnt[idx] -= 1;

            while cur_min < 26 && cnt[cur_min] == 0 {
                cur_min += 1;
            }

            while let Some(&top) = stack.last() {
                if cur_min == 26 || ((top - b'a') as usize) <= cur_min {
                    res.push(top);
                    stack.pop();
                } else {
                    break;
                }
            }
        }

        while let Some(ch) = stack.pop() {
            res.push(ch);
        }

        unsafe { String::from_utf8_unchecked(res) }
    }
}
```

## Racket

```racket
(define/contract (robot-with-string s)
  (-> string? string?)
  (let* ((n (string-length s))
         (cnt (make-vector 26 0)))
    ;; count frequencies
    (for ([i (in-range n)])
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        (vector-set! cnt idx (+ (vector-ref cnt idx) 1))))
    ;; initial smallest remaining character index
    (define curMin
      (let loop ((i 0))
        (if (>= i 26)
            26
            (if (> (vector-ref cnt i) 0) i (loop (+ i 1))))))
    (define (advance-min!)
      (let loop ()
        (when (and (< curMin 26) (= (vector-ref cnt curMin) 0))
          (set! curMin (+ curMin 1))
          (loop))))
    (define stack '())
    (define out '())
    ;; process each character
    (for ([i (in-range n)])
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        ;; push onto stack
        (set! stack (cons c stack))
        ;; decrement remaining count
        (vector-set! cnt idx (- (vector-ref cnt idx) 1))
        ;; update smallest remaining character
        (advance-min!)
        ;; pop while top <= current minimum remaining char
        (let loop ()
          (when (and (not (null? stack))
                     (let ((top (car stack))
                           (minCode (if (= curMin 26)
                                        (char->integer #\{) ; character after 'z'
                                        (+ (char->integer #\a) curMin))))
                       (<= (char->integer top) minCode)))
            (let ((top (car stack)))
              (set! stack (cdr stack))
              (set! out (cons top out))
              (loop))))))
    ;; pop any remaining characters
    (let loop ()
      (when (not (null? stack))
        (set! out (cons (car stack) out))
        (set! stack (cdr stack))
        (loop)))
    ;; build result string
    (list->string (reverse out))))
```

## Erlang

```erlang
-define(ALPHABET_SIZE, 26).

-spec robot_with_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
robot_with_string(S) ->
    Chars = binary_to_list(S),
    Freq0 = build_freq(Chars, make_tuple(?ALPHABET_SIZE, 0)),
    OutList = process(Chars, Freq0, [], []),
    list_to_binary(OutList).

build_freq([], Tuple) -> Tuple;
build_freq([C|Rest], Tuple) ->
    Idx = C - $a,
    Old = element(Idx + 1, Tuple),
    NewTuple = setelement(Idx + 1, Tuple, Old + 1),
    build_freq(Rest, NewTuple).

find_min(Freq) -> find_min(Freq, 0).
find_min(Freq, I) when I < ?ALPHABET_SIZE ->
    case element(I + 1, Freq) of
        Count when Count > 0 -> $a + I;
        _ -> find_min(Freq, I + 1)
    end;
find_min(_, _) -> 123.

pop_while(Stack, OutAcc, MinChar) ->
    case Stack of
        [Top | Rest] when Top =< MinChar ->
            pop_while(Rest, [Top | OutAcc], MinChar);
        _ -> {Stack, OutAcc}
    end.

pop_all([], OutAcc) -> OutAcc;
pop_all([Top | Rest], OutAcc) -> pop_all(Rest, [Top | OutAcc]).

process([], _Freq, Stack, OutAcc) ->
    Final = pop_all(Stack, OutAcc),
    lists:reverse(Final);
process([C | Rest], Freq0, Stack0, OutAcc0) ->
    Idx = C - $a,
    OldCount = element(Idx + 1, Freq0),
    NewFreq = setelement(Idx + 1, Freq0, OldCount - 1),
    Stack1 = [C | Stack0],
    MinChar = find_min(NewFreq),
    {Stack2, OutAcc1} = pop_while(Stack1, OutAcc0, MinChar),
    process(Rest, NewFreq, Stack2, OutAcc1).
```

## Elixir

```elixir
defmodule Solution do
  @spec robot_with_string(s :: String.t) :: String.t
  def robot_with_string(s) do
    chars = String.to_charlist(s)
    freq = build_freq(chars, %{})
    cur_min = find_min(freq)

    init_state = %{freq: freq, cur_min: cur_min, stack: [], res: []}

    final_state =
      Enum.reduce(chars, init_state, fn ch, acc ->
        # push current character onto the stack
        stack = [ch | acc.stack]

        # decrease its remaining count
        cnt = Map.get(acc.freq, ch) - 1
        freq = if cnt == 0, do: Map.delete(acc.freq, ch), else: Map.put(acc.freq, ch, cnt)

        # update the smallest character still in s
        cur_min = advance_min(acc.cur_min, freq)

        {stack2, res2} = pop_while(stack, cur_min, acc.res)

        %{freq: freq, cur_min: cur_min, stack: stack2, res: res2}
      end)

    # pop any remaining characters from the stack
    final_res =
      Enum.reduce(final_state.stack, final_state.res, fn ch, acc -> [ch | acc] end)

    final_res
    |> Enum.reverse()
    |> List.to_string()
  end

  defp build_freq([], freq), do: freq
  defp build_freq([c | rest], freq) do
    cnt = Map.get(freq, c, 0) + 1
    build_freq(rest, Map.put(freq, c, cnt))
  end

  defp find_min(freq) do
    Enum.find_value(?a..?z, fn code ->
      if Map.get(freq, code, 0) > 0, do: code, else: nil
    end) || (?z + 1)
  end

  defp advance_min(cur_min, freq) do
    cond do
      cur_min > ?z -> cur_min
      Map.get(freq, cur_min, 0) > 0 -> cur_min
      true -> advance_min(cur_min + 1, freq)
    end
  end

  defp pop_while(stack, cur_min, res) do
    case stack do
      [] ->
        {[], res}

      [top | rest] ->
        if cur_min > ?z or top <= cur_min do
          pop_while(rest, cur_min, [top | res])
        else
          {stack, res}
        end
    end
  end
end
```
