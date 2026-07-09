# 0316. Remove Duplicate Letters

## Cpp

```cpp
class Solution {
public:
    string removeDuplicateLetters(string s) {
        int cnt[26] = {0};
        for (char c : s) ++cnt[c - 'a'];
        bool inStack[26] = {false};
        vector<char> st;
        for (char c : s) {
            --cnt[c - 'a'];
            if (inStack[c - 'a']) continue;
            while (!st.empty() && c < st.back() && cnt[st.back() - 'a'] > 0) {
                inStack[st.back() - 'a'] = false;
                st.pop_back();
            }
            st.push_back(c);
            inStack[c - 'a'] = true;
        }
        return string(st.begin(), st.end());
    }
};
```

## Java

```java
class Solution {
    public String removeDuplicateLetters(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }
        boolean[] inStack = new boolean[26];
        char[] stack = new char[26];
        int top = -1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = c - 'a';
            count[idx]--;
            if (inStack[idx]) continue;
            while (top >= 0 && c < stack[top] && count[stack[top] - 'a'] > 0) {
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
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        count = Counter(s)
        in_stack = set()
        stack = []
        for ch in s:
            count[ch] -= 1
            if ch in in_stack:
                continue
            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(ch)
            in_stack.add(ch)
        return ''.join(stack)
```

## Python3

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        in_stack = [False] * 26
        stack = []

        for ch in s:
            idx = ord(ch) - ord('a')
            cnt[idx] -= 1
            if in_stack[idx]:
                continue
            while stack and ch < stack[-1] and cnt[ord(stack[-1]) - ord('a')] > 0:
                removed = stack.pop()
                in_stack[ord(removed) - ord('a')] = False
            stack.append(ch)
            in_stack[idx] = True

        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* removeDuplicateLetters(char* s) {
    int n = strlen(s);
    int cnt[26] = {0};
    for (int i = 0; i < n; ++i) {
        cnt[s[i] - 'a']++;
    }
    
    bool inStack[26] = {false};
    char stack[26];
    int top = 0;
    
    for (int i = 0; i < n; ++i) {
        char c = s[i];
        int idx = c - 'a';
        cnt[idx]--;
        if (inStack[idx]) continue;
        
        while (top > 0 && c < stack[top - 1] && cnt[stack[top - 1] - 'a'] > 0) {
            inStack[stack[top - 1] - 'a'] = false;
            top--;
        }
        stack[top++] = c;
        inStack[idx] = true;
    }
    
    char* res = (char*)malloc(top + 1);
    for (int i = 0; i < top; ++i) {
        res[i] = stack[i];
    }
    res[top] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string RemoveDuplicateLetters(string s) {
        int[] count = new int[26];
        foreach (char ch in s) count[ch - 'a']++;

        bool[] visited = new bool[26];
        var stack = new List<char>();

        foreach (char c in s) {
            int idx = c - 'a';
            count[idx]--;
            if (visited[idx]) continue;

            while (stack.Count > 0 && stack[stack.Count - 1] > c && count[stack[stack.Count - 1] - 'a'] > 0) {
                char removed = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);
                visited[removed - 'a'] = false;
            }

            stack.Add(c);
            visited[idx] = true;
        }

        return new string(stack.ToArray());
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
    const count = new Array(26).fill(0);
    for (let ch of s) {
        count[ch.charCodeAt(0) - 97]++;
    }
    const inStack = new Array(26).fill(false);
    const stack = [];
    
    for (let ch of s) {
        const idx = ch.charCodeAt(0) - 97;
        count[idx]--;
        if (inStack[idx]) continue;
        
        while (stack.length) {
            const lastChar = stack[stack.length - 1];
            const lastIdx = lastChar.charCodeAt(0) - 97;
            if (ch < lastChar && count[lastIdx] > 0) {
                stack.pop();
                inStack[lastIdx] = false;
            } else {
                break;
            }
        }
        
        stack.push(ch);
        inStack[idx] = true;
    }
    
    return stack.join('');
};
```

## Typescript

```typescript
function removeDuplicateLetters(s: string): string {
    const count = new Array(26).fill(0);
    for (const ch of s) {
        count[ch.charCodeAt(0) - 97]++;
    }

    const visited = new Array(26).fill(false);
    const stack: string[] = [];

    for (const ch of s) {
        const idx = ch.charCodeAt(0) - 97;
        count[idx]--;

        if (visited[idx]) continue;

        while (
            stack.length > 0 &&
            stack[stack.length - 1] > ch &&
            count[stack[stack.length - 1].charCodeAt(0) - 97] > 0
        ) {
            const removed = stack.pop()!;
            visited[removed.charCodeAt(0) - 97] = false;
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
    function removeDuplicateLetters($s) {
        $len = strlen($s);
        $cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
        }

        $inStack = array_fill(0, 26, false);
        $stack = [];

        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            $ci = ord($c) - 97;
            // decrement remaining count
            $cnt[$ci]--;

            if ($inStack[$ci]) {
                continue;
            }

            while (!empty($stack)) {
                $top = end($stack);
                $ti = ord($top) - 97;
                if ($top > $c && $cnt[$ti] > 0) {
                    array_pop($stack);
                    $inStack[$ti] = false;
                } else {
                    break;
                }
            }

            $stack[] = $c;
            $inStack[$ci] = true;
        }

        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func removeDuplicateLetters(_ s: String) -> String {
        let aAscii = Character("a").asciiValue!
        var count = [Int](repeating: 0, count: 26)
        for ch in s {
            let idx = Int(ch.asciiValue! - aAscii)
            count[idx] += 1
        }
        
        var visited = [Bool](repeating: false, count: 26)
        var stack = [Character]()
        
        for ch in s {
            let idx = Int(ch.asciiValue! - aAscii)
            count[idx] -= 1
            if visited[idx] { continue }
            
            while let last = stack.last {
                let lastIdx = Int(last.asciiValue! - aAscii)
                if ch < last && count[lastIdx] > 0 {
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
    fun removeDuplicateLetters(s: String): String {
        val count = IntArray(26)
        for (c in s) {
            count[c - 'a']++
        }
        val visited = BooleanArray(26)
        val stack = CharArray(s.length)
        var top = 0
        for (c in s) {
            val idx = c - 'a'
            count[idx]--
            if (visited[idx]) continue
            while (top > 0 && c < stack[top - 1] && count[stack[top - 1] - 'a'] > 0) {
                visited[stack[top - 1] - 'a'] = false
                top--
            }
            stack[top++] = c
            visited[idx] = true
        }
        return String(stack, 0, top)
    }
}
```

## Dart

```dart
class Solution {
  String removeDuplicateLetters(String s) {
    List<int> count = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      count[s.codeUnitAt(i) - 97]++;
    }

    List<bool> visited = List.filled(26, false);
    List<int> stack = [];

    for (int i = 0; i < s.length; i++) {
      int c = s.codeUnitAt(i) - 97;
      count[c]--;
      if (visited[c]) continue;

      while (stack.isNotEmpty && c < stack.last && count[stack.last] > 0) {
        visited[stack.removeLast()] = false;
      }

      stack.add(c);
      visited[c] = true;
    }

    StringBuffer sb = StringBuffer();
    for (int v in stack) {
      sb.writeCharCode(v + 97);
    }
    return sb.toString();
  }
}
```

## Golang

```go
func removeDuplicateLetters(s string) string {
    cnt := [26]int{}
    for i := 0; i < len(s); i++ {
        cnt[s[i]-'a']++
    }
    inStack := [26]bool{}
    stack := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        c := s[i]
        idx := c - 'a'
        cnt[idx]--
        if inStack[idx] {
            continue
        }
        for len(stack) > 0 && c < stack[len(stack)-1] && cnt[stack[len(stack)-1]-'a'] > 0 {
            removed := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            inStack[removed-'a'] = false
        }
        stack = append(stack, c)
        inStack[idx] = true
    }
    return string(stack)
}
```

## Ruby

```ruby
def remove_duplicate_letters(s)
  cnt = Array.new(26, 0)
  s.each_byte { |b| cnt[b - 97] += 1 }
  visited = Array.new(26, false)
  stack = []

  s.each_byte do |b|
    idx = b - 97
    cnt[idx] -= 1
    next if visited[idx]

    while !stack.empty? && b < stack[-1] && cnt[stack[-1] - 97] > 0
      removed = stack.pop
      visited[removed - 97] = false
    end

    stack << b
    visited[idx] = true
  end

  stack.pack('C*')
end
```

## Scala

```scala
object Solution {
    def removeDuplicateLetters(s: String): String = {
        val cnt = Array.fill(26)(0)
        for (c <- s) cnt(c - 'a') += 1

        val visited = Array.fill(26)(false)
        import scala.collection.mutable.ArrayBuffer
        val stack = new ArrayBuffer[Char]()

        for (c <- s) {
            val idx = c - 'a'
            cnt(idx) -= 1
            if (!visited(idx)) {
                while (stack.nonEmpty && c < stack.last && cnt(stack.last - 'a') > 0) {
                    val removed = stack.remove(stack.size - 1)
                    visited(removed - 'a') = false
                }
                stack.append(c)
                visited(idx) = true
            }
        }

        stack.mkString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_duplicate_letters(s: String) -> String {
        let mut cnt = [0usize; 26];
        for &b in s.as_bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut visited = [false; 26];
        let mut stack: Vec<u8> = Vec::new();

        for &b in s.as_bytes() {
            let idx = (b - b'a') as usize;
            cnt[idx] -= 1;
            if visited[idx] {
                continue;
            }
            while let Some(&last) = stack.last() {
                let last_idx = (last - b'a') as usize;
                if last > b && cnt[last_idx] > 0 {
                    stack.pop();
                    visited[last_idx] = false;
                } else {
                    break;
                }
            }
            stack.push(b);
            visited[idx] = true;
        }

        String::from_utf8(stack).unwrap()
    }
}
```

## Racket

```racket
(define/contract (remove-duplicate-letters s)
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
        ;; one occurrence processed
        (vector-set! cnt idx (- (vector-ref cnt idx) 1))
        (when (not (vector-ref visited idx))
          ;; pop larger chars that will appear later again
          (let loop ()
            (when (and (pair? stack)
                       (< (char->integer c) (char->integer (car stack)))
                       (> (vector-ref cnt (- (char->integer (car stack)) (char->integer #\a))) 0))
              (let ((top-idx (- (char->integer (car stack)) (char->integer #\a))))
                (vector-set! visited top-idx #f)
                (set! stack (cdr stack))
                (loop))))
          ;; push current char
          (set! stack (cons c stack))
          (vector-set! visited idx #t))))
    (list->string (reverse stack))))
```

## Erlang

```erlang
-spec remove_duplicate_letters(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_duplicate_letters(S) ->
    CharList = binary_to_list(S),
    CountMap0 = lists:foldl(fun(C, Acc) ->
        case maps:is_key(C, Acc) of
            true -> maps:put(C, maps:get(C, Acc) + 1, Acc);
            false -> maps:put(C, 1, Acc)
        end
    end, #{}, CharList),
    Stack = process(CharList, CountMap0, [], #{}),
    ResultList = lists:reverse(Stack),
    list_to_binary(ResultList).

process([], _CountMap, Stack, _Visited) ->
    Stack;
process([C | Rest], CountMap, Stack, Visited) ->
    Curr = maps:get(C, CountMap),
    NewCountMap = maps:put(C, Curr - 1, CountMap),
    case maps:is_key(C, Visited) of
        true ->
            process(Rest, NewCountMap, Stack, Visited);
        false ->
            {NewStack, NewVisited} = pop_while(Stack, C, NewCountMap, Visited),
            FinalStack = [C | NewStack],
            FinalVisited = maps:put(C, true, NewVisited),
            process(Rest, NewCountMap, FinalStack, FinalVisited)
    end.

pop_while([], _C, _CountMap, Visited) ->
    {[], Visited};
pop_while([Top | Rest] = Stack, C, CountMap, Visited) ->
    case (Top > C) andalso (maps:get(Top, CountMap) > 0) of
        true ->
            NewVisited = maps:remove(Top, Visited),
            pop_while(Rest, C, CountMap, NewVisited);
        false ->
            {Stack, Visited}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_duplicate_letters(s :: String.t) :: String.t
  def remove_duplicate_letters(s) do
    chars = String.graphemes(s)

    freq =
      Enum.reduce(chars, %{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    {stack_rev, _visited, _freq} =
      Enum.reduce(chars, {[], MapSet.new(), freq}, fn ch,
                                                      {stack, visited, freq_map} ->
        # decrement remaining count for current character
        cnt = Map.get(freq_map, ch) - 1
        freq_map = Map.put(freq_map, ch, cnt)

        if MapSet.member?(visited, ch) do
          {stack, visited, freq_map}
        else
          {new_stack, new_visited} = pop_while(stack, visited, ch, freq_map)
          {[ch | new_stack], MapSet.put(new_visited, ch), freq_map}
        end
      end)

    stack_rev |> Enum.reverse() |> Enum.join()
  end

  defp pop_while([], visited, _cur, _freq), do: {[], visited}

  defp pop_while([top | rest] = stack, visited, cur, freq) do
    if top > cur and Map.get(freq, top) > 0 do
      new_visited = MapSet.delete(visited, top)
      pop_while(rest, new_visited, cur, freq)
    else
      {stack, visited}
    end
  end
end
```
