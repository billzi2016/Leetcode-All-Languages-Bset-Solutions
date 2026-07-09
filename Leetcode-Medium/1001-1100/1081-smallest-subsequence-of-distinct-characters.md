# 1081. Smallest Subsequence of Distinct Characters

## Cpp

```cpp
class Solution {
public:
    string smallestSubsequence(string s) {
        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        vector<bool> inStack(26, false);
        string st;
        for (char c : s) {
            int idx = c - 'a';
            cnt[idx]--;
            if (inStack[idx]) continue;
            while (!st.empty() && c < st.back() && cnt[st.back() - 'a'] > 0) {
                inStack[st.back() - 'a'] = false;
                st.pop_back();
            }
            st.push_back(c);
            inStack[idx] = true;
        }
        return st;
    }
};
```

## Java

```java
class Solution {
    public String smallestSubsequence(String s) {
        int[] remaining = new int[26];
        for (int i = 0; i < s.length(); i++) {
            remaining[s.charAt(i) - 'a']++;
        }
        boolean[] inStack = new boolean[26];
        char[] stack = new char[26];
        int top = -1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = c - 'a';
            remaining[idx]--;
            if (inStack[idx]) continue;
            while (top >= 0 && stack[top] > c && remaining[stack[top] - 'a'] > 0) {
                inStack[stack[top] - 'a'] = false;
                top--;
            }
            stack[++top] = c;
            inStack[idx] = true;
        }
        return new String(stack, 0, top + 1);
    }
}
```

## Python

```python
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count remaining occurrences of each character
        remain = [0] * 26
        for ch in s:
            remain[ord(ch) - ord('a')] += 1

        visited = [False] * 26
        stack = []

        for ch in s:
            idx = ord(ch) - ord('a')
            # this character is now being processed, so decrement its remaining count
            remain[idx] -= 1

            if visited[idx]:
                continue

            # maintain increasing order while we can still find the popped char later
            while stack and ch < stack[-1] and remain[ord(stack[-1]) - ord('a')] > 0:
                removed = stack.pop()
                visited[ord(removed) - ord('a')] = False

            stack.append(ch)
            visited[idx] = True

        return ''.join(stack)
```

## Python3

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        in_stack = [False] * 26
        stack = []

        for ch in s:
            idx = ord(ch) - 97
            cnt[idx] -= 1
            if in_stack[idx]:
                continue
            while stack and ch < stack[-1] and cnt[ord(stack[-1]) - 97] > 0:
                removed = stack.pop()
                in_stack[ord(removed) - 97] = False
            stack.append(ch)
            in_stack[idx] = True

        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* smallestSubsequence(char* s) {
    int n = strlen(s);
    int last[26];
    for (int i = 0; i < 26; ++i) last[i] = -1;
    for (int i = 0; i < n; ++i) {
        last[s[i] - 'a'] = i;
    }

    bool inStack[26] = {false};
    char stack[27];
    int top = 0;

    for (int i = 0; i < n; ++i) {
        char c = s[i];
        int idx = c - 'a';
        if (inStack[idx]) continue;
        while (top > 0 && stack[top - 1] > c && last[stack[top - 1] - 'a'] > i) {
            inStack[stack[top - 1] - 'a'] = false;
            --top;
        }
        stack[top++] = c;
        inStack[idx] = true;
    }

    char* res = (char*)malloc(top + 1);
    for (int i = 0; i < top; ++i) res[i] = stack[i];
    res[top] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string SmallestSubsequence(string s)
    {
        int[] remaining = new int[26];
        foreach (char c in s) remaining[c - 'a']++;

        bool[] inStack = new bool[26];
        char[] stack = new char[s.Length];
        int top = 0;

        foreach (char ch in s)
        {
            int idx = ch - 'a';
            remaining[idx]--;

            if (inStack[idx]) continue;

            while (top > 0 && ch < stack[top - 1] && remaining[stack[top - 1] - 'a'] > 0)
            {
                inStack[stack[top - 1] - 'a'] = false;
                top--;
            }

            stack[top++] = ch;
            inStack[idx] = true;
        }

        return new string(stack, 0, top);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var smallestSubsequence = function(s) {
    const cnt = new Array(26).fill(0);
    const visited = new Array(26).fill(false);
    const aCharCode = 'a'.charCodeAt(0);
    
    for (let i = 0; i < s.length; ++i) {
        cnt[s.charCodeAt(i) - aCharCode]++;
    }
    
    const stack = [];
    
    for (let i = 0; i < s.length; ++i) {
        const idx = s.charCodeAt(i) - aCharCode;
        cnt[idx]--;
        if (visited[idx]) continue;
        
        while (stack.length > 0) {
            const topIdx = stack[stack.length - 1];
            if (topIdx > idx && cnt[topIdx] > 0) {
                visited[topIdx] = false;
                stack.pop();
            } else {
                break;
            }
        }
        stack.push(idx);
        visited[idx] = true;
    }
    
    return String.fromCharCode(...stack.map(i => i + aCharCode));
};
```

## Typescript

```typescript
function smallestSubsequence(s: string): string {
    const cnt = new Array(26).fill(0);
    for (const ch of s) cnt[ch.charCodeAt(0) - 97]++;

    const visited = new Array(26).fill(false);
    const stack: string[] = [];

    for (const ch of s) {
        const idx = ch.charCodeAt(0) - 97;
        cnt[idx]--;
        if (visited[idx]) continue;

        while (stack.length) {
            const last = stack[stack.length - 1];
            const lastIdx = last.charCodeAt(0) - 97;
            if (last > ch && cnt[lastIdx] > 0) {
                visited[lastIdx] = false;
                stack.pop();
            } else break;
        }

        stack.push(ch);
        visited[idx] = true;
    }

    return stack.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function smallestSubsequence($s) {
        $n = strlen($s);
        $cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
        }

        $inStack = array_fill(0, 26, false);
        $stack = [];

        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $idx = ord($c) - 97;
            $cnt[$idx]--;

            if ($inStack[$idx]) {
                continue;
            }

            while (!empty($stack)) {
                $lastChar = end($stack);
                $lastIdx = ord($lastChar) - 97;
                if ($lastChar > $c && $cnt[$lastIdx] > 0) {
                    array_pop($stack);
                    $inStack[$lastIdx] = false;
                } else {
                    break;
                }
            }

            $stack[] = $c;
            $inStack[$idx] = true;
        }

        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func smallestSubsequence(_ s: String) -> String {
        var freq = [Int](repeating: 0, count: 26)
        for ch in s {
            let idx = Int(ch.asciiValue! - 97)
            freq[idx] += 1
        }
        var visited = [Bool](repeating: false, count: 26)
        var stack = [Character]()
        
        for ch in s {
            let idx = Int(ch.asciiValue! - 97)
            freq[idx] -= 1
            if visited[idx] { continue }
            
            while let last = stack.last {
                let lastIdx = Int(last.asciiValue! - 97)
                if last > ch && freq[lastIdx] > 0 {
                    stack.removeLast()
                    visited[lastIdx] = false
                } else {
                    break
                }
            }
            stack.append(ch)
            visited[idx] = true
        }
        return String(stack)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestSubsequence(s: String): String {
        val count = IntArray(26)
        for (ch in s) {
            count[ch - 'a']++
        }
        val visited = BooleanArray(26)
        val stack = java.util.ArrayDeque<Char>()
        for (ch in s) {
            val idx = ch - 'a'
            count[idx]--
            if (visited[idx]) continue
            while (!stack.isEmpty()) {
                val last = stack.peekLast()
                val lastIdx = last - 'a'
                if (last > ch && count[lastIdx] > 0) {
                    visited[lastIdx] = false
                    stack.pollLast()
                } else break
            }
            stack.addLast(ch)
            visited[idx] = true
        }
        val sb = StringBuilder()
        for (c in stack) sb.append(c)
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String smallestSubsequence(String s) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      cnt[s.codeUnitAt(i) - 97]++;
    }

    List<bool> visited = List.filled(26, false);
    List<String> stack = [];

    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      cnt[idx]--;

      if (visited[idx]) continue;

      while (stack.isNotEmpty) {
        int lastIdx = stack.last.codeUnitAt(0) - 97;
        if (lastIdx > idx && cnt[lastIdx] > 0) {
          visited[lastIdx] = false;
          stack.removeLast();
        } else {
          break;
        }
      }

      stack.add(s[i]);
      visited[idx] = true;
    }

    return stack.join();
  }
}
```

## Golang

```go
func smallestSubsequence(s string) string {
	cnt := [26]int{}
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	visited := [26]bool{}
	stack := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		idx := c - 'a'
		cnt[idx]--
		if visited[idx] {
			continue
		}
		for len(stack) > 0 && stack[len(stack)-1] > c && cnt[stack[len(stack)-1]-'a'] > 0 {
			topIdx := stack[len(stack)-1] - 'a'
			visited[topIdx] = false
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, c)
		visited[idx] = true
	}
	return string(stack)
}
```

## Ruby

```ruby
def smallest_subsequence(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  in_stack = Array.new(26, false)
  stack = []

  s.each_char do |c|
    idx = c.ord - 97
    cnt[idx] -= 1
    next if in_stack[idx]

    while !stack.empty? && c < stack[-1] && cnt[stack[-1].ord - 97] > 0
      removed = stack.pop
      in_stack[removed.ord - 97] = false
    end

    stack << c
    in_stack[idx] = true
  end

  stack.join
end
```

## Scala

```scala
object Solution {
  def smallestSubsequence(s: String): String = {
    val cnt = new Array[Int](26)
    for (ch <- s) cnt(ch - 'a') += 1

    val visited = new Array[Boolean](26)
    val stack = new scala.collection.mutable.ArrayDeque[Char]()

    for (ch <- s) {
      val idx = ch - 'a'
      cnt(idx) -= 1
      if (!visited(idx)) {
        while (stack.nonEmpty && ch < stack.last && cnt(stack.last - 'a') > 0) {
          val removed = stack.removeLast()
          visited(removed - 'a') = false
        }
        stack.append(ch)
        visited(idx) = true
      }
    }

    val sb = new StringBuilder
    for (c <- stack) sb.append(c)
    sb.toString()
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn smallest_subsequence(s: String) -> String {
        let mut cnt = [0usize; 26];
        for &b in s.as_bytes() {
            cnt[(b - b'a') as usize] += 1;
        }

        let mut visited = [false; 26];
        let mut stack: Vec<u8> = Vec::with_capacity(s.len());

        for &c in s.as_bytes() {
            let idx = (c - b'a') as usize;
            cnt[idx] -= 1;

            if visited[idx] {
                continue;
            }

            while let Some(&last) = stack.last() {
                let last_idx = (last - b'a') as usize;
                if last > c && cnt[last_idx] > 0 {
                    stack.pop();
                    visited[last_idx] = false;
                } else {
                    break;
                }
            }

            stack.push(c);
            visited[idx] = true;
        }

        // SAFETY: stack contains only valid lowercase ASCII letters.
        unsafe { String::from_utf8_unchecked(stack) }
    }
}
```

## Racket

```racket
(define/contract (smallest-subsequence s)
  (-> string? string?)
  (let* ((n (string-length s))
         (cnt (make-vector 26 0)))
    ;; count occurrences of each character
    (for ([i (in-range n)])
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        (vector-set! cnt idx (+ (vector-ref cnt idx) 1))))
    (define visited (make-vector 26 #f))
    (define stack '())
    (for ([i (in-range n)])
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        ;; one less occurrence remaining
        (vector-set! cnt idx (- (vector-ref cnt idx) 1))
        (unless (vector-ref visited idx)
          ;; pop larger chars that will appear later again
          (let loop ()
            (when (and (pair? stack)
                       (char>? (car stack) c)
                       (> (vector-ref cnt
                                      (- (char->integer (car stack))
                                         (char->integer #\a))) 0))
              (let ((top (car stack)))
                (vector-set! visited
                             (- (char->integer top) (char->integer #\a))
                             #f)
                (set! stack (cdr stack))
                (loop))))
          ;; push current char
          (set! stack (cons c stack))
          (vector-set! visited idx #t))))
    (list->string (reverse stack))))
```

## Erlang

```erlang
-spec smallest_subsequence(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_subsequence(S) ->
    CountMap = count_chars(S, #{}),
    {StackRev, _Visited} = process(S, [], CountMap, #{}),
    iolist_to_binary(lists:reverse(StackRev)).

%% Count occurrences of each character in the binary string.
count_chars(<<>>, M) -> M;
count_chars(<<C, Rest/binary>>, M) ->
    NewM =
        case maps:get(C, M, undefined) of
            undefined -> maps:put(C, 1, M);
            V -> maps:put(C, V + 1, M)
        end,
    count_chars(Rest, NewM).

%% Main processing loop.
process(<<>>, StackRev, _CountMap, Visited) ->
    {StackRev, Visited};
process(<<C, Rest/binary>>, StackRev, CountMap0, Visited0) ->
    %% Decrease remaining count for current character
    CurCnt = maps:get(C, CountMap0),
    NewCountMap =
        if CurCnt =:= 1 -> maps:remove(C, CountMap0);
           true       -> maps:put(C, CurCnt - 1, CountMap0)
        end,
    %% If already in stack, skip
    case maps:is_key(C, Visited0) of
        true ->
            process(Rest, StackRev, NewCountMap, Visited0);
        false ->
            {PoppedStack, UpdatedVisited} = pop_while(StackRev, C, NewCountMap, Visited0),
            NewVisited = maps:put(C, true, UpdatedVisited),
            process(Rest, [C | PoppedStack], NewCountMap, NewVisited)
    end.

%% Pop elements from the stack while they are larger than current char
%% and still have remaining occurrences later.
pop_while([], _Curr, _CountMap, Visited) ->
    {[], Visited};
pop_while([Top | Rest] = Stack, Curr, CountMap, Visited) ->
    case (Top > Curr) andalso maps:is_key(Top, CountMap) of
        true ->
            NewVisited = maps:remove(Top, Visited),
            pop_while(Rest, Curr, CountMap, NewVisited);
        false ->
            {Stack, Visited}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_subsequence(s :: String.t()) :: String.t()
  def smallest_subsequence(s) do
    chars = String.graphemes(s)

    freq =
      Enum.reduce(chars, %{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    {stack, _visited, _freq} =
      Enum.reduce(chars, {[], %{}, freq}, fn ch, {stk, visited, freq_map} ->
        cnt = Map.get(freq_map, ch) - 1
        freq_map = Map.put(freq_map, ch, cnt)

        if Map.get(visited, ch, false) do
          {stk, visited, freq_map}
        else
          {new_stk, new_visited} = pop_while(stk, visited, ch, freq_map)
          {[ch | new_stk], Map.put(new_visited, ch, true), freq_map}
        end
      end)

    stack
    |> Enum.reverse()
    |> Enum.join()
  end

  defp pop_while([], visited, _c, _freq), do: {[], visited}

  defp pop_while([top | rest] = stk, visited, c, freq) do
    if top > c and Map.get(freq, top, 0) > 0 do
      visited = Map.put(visited, top, false)
      pop_while(rest, visited, c, freq)
    else
      {stk, visited}
    end
  end
end
```
