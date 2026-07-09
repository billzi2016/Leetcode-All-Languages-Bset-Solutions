# 3170. Lexicographically Minimum String After Removing Stars

## Cpp

```cpp
class Solution {
public:
    string clearStars(string s) {
        int n = s.size();
        vector<bool> removed(n, false);
        vector<vector<int>> stacks(26);
        for (int i = 0; i < n; ++i) {
            char ch = s[i];
            if (ch == '*') {
                for (int c = 0; c < 26; ++c) {
                    if (!stacks[c].empty()) {
                        int idx = stacks[c].back();
                        stacks[c].pop_back();
                        removed[idx] = true;
                        break;
                    }
                }
            } else {
                stacks[ch - 'a'].push_back(i);
            }
        }
        string ans;
        ans.reserve(n);
        for (int i = 0; i < n; ++i) {
            if (s[i] != '*' && !removed[i]) ans.push_back(s[i]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String clearStars(String s) {
        int n = s.length();
        boolean[] removed = new boolean[n];
        @SuppressWarnings("unchecked")
        ArrayDeque<Integer>[] stacks = new ArrayDeque[26];
        for (int i = 0; i < 26; i++) {
            stacks[i] = new ArrayDeque<>();
        }
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == '*') {
                // find smallest character stack that is non-empty
                for (int c = 0; c < 26; c++) {
                    if (!stacks[c].isEmpty()) {
                        int idx = stacks[c].pollLast(); // remove most recent occurrence
                        removed[idx] = true;
                        break;
                    }
                }
            } else {
                stacks[ch - 'a'].addLast(i);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) != '*' && !removed[i]) {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        stacks = [[] for _ in range(26)]  # indices of each character not yet removed
        for i, ch in enumerate(chars):
            if ch == '*':
                for c in range(26):
                    if stacks[c]:
                        idx = stacks[c].pop()
                        chars[idx] = ''   # mark as deleted
                        break
                # the '*' itself will be ignored later
            else:
                stacks[ord(ch) - 97].append(i)
        return ''.join(c for c in chars if c not in ('', '*'))
```

## Python3

```python
class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        stacks = [[] for _ in range(26)]
        removed = [False] * n
        for i, ch in enumerate(s):
            if ch == '*':
                for c in range(26):
                    if stacks[c]:
                        idx = stacks[c].pop()
                        removed[idx] = True
                        break
            else:
                stacks[ord(ch) - 97].append(i)
        res = []
        for i, ch in enumerate(s):
            if ch != '*' and not removed[i]:
                res.append(ch)
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* clearStars(char* s) {
    int n = (int)strlen(s);
    int **stacks = (int**)malloc(26 * sizeof(int*));
    for (int c = 0; c < 26; ++c) {
        stacks[c] = (int*)malloc(n * sizeof(int));
    }
    int sz[26] = {0};

    for (int i = 0; i < n; ++i) {
        char ch = s[i];
        if (ch == '*') {
            int c;
            for (c = 0; c < 26; ++c) {
                if (sz[c] > 0) break;
            }
            int idx = stacks[c][--sz[c]];
            s[idx] = '*';
        } else {
            int ci = ch - 'a';
            stacks[ci][sz[ci]++] = i;
        }
    }

    char *res = (char*)malloc((n + 1) * sizeof(char));
    int p = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] != '*') {
            res[p++] = s[i];
        }
    }
    res[p] = '\0';

    for (int c = 0; c < 26; ++c) {
        free(stacks[c]);
    }
    free(stacks);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ClearStars(string s) {
        int n = s.Length;
        bool[] removed = new bool[n];
        Stack<int>[] stacks = new Stack<int>[26];
        for (int i = 0; i < 26; i++) stacks[i] = new Stack<int>();

        for (int i = 0; i < n; i++) {
            char ch = s[i];
            if (ch == '*') {
                for (int c = 0; c < 26; c++) {
                    if (stacks[c].Count > 0) {
                        int idx = stacks[c].Pop();
                        removed[idx] = true;
                        break;
                    }
                }
            } else {
                stacks[ch - 'a'].Push(i);
            }
        }

        var sb = new System.Text.StringBuilder();
        for (int i = 0; i < n; i++) {
            if (!removed[i] && s[i] != '*') sb.Append(s[i]);
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
var clearStars = function(s) {
    const n = s.length;
    const chars = s.split('');
    const stacks = Array.from({ length: 26 }, () => []);
    
    for (let i = 0; i < n; i++) {
        const ch = chars[i];
        if (ch === '*') {
            // find smallest existing character to delete
            for (let c = 0; c < 26; c++) {
                if (stacks[c].length > 0) {
                    const idx = stacks[c].pop();
                    chars[idx] = ''; // mark as removed
                    break;
                }
            }
        } else {
            const code = ch.charCodeAt(0) - 97;
            stacks[code].push(i);
        }
    }
    
    let result = '';
    for (let i = 0; i < n; i++) {
        const ch = chars[i];
        if (ch && ch !== '*') {
            result += ch;
        }
    }
    return result;
};
```

## Typescript

```typescript
function clearStars(s: string): string {
    const n = s.length;
    const stacks: number[][] = Array.from({ length: 26 }, () => []);
    const removed = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
        const code = s.charCodeAt(i);
        if (code === 42) { // '*'
            for (let c = 0; c < 26; c++) {
                const st = stacks[c];
                if (st.length > 0) {
                    const idx = st.pop() as number;
                    removed[idx] = 1;
                    break;
                }
            }
        } else {
            const ci = code - 97; // 'a' -> 0
            stacks[ci].push(i);
        }
    }
    const res: string[] = [];
    for (let i = 0; i < n; i++) {
        if (s.charCodeAt(i) === 42) continue;
        if (!removed[i]) res.push(s[i]);
    }
    return res.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function clearStars($s) {
        $n = strlen($s);
        $stacks = array_fill(0, 26, []);
        $removed = array_fill(0, $n, false);

        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === '*') {
                for ($k = 0; $k < 26; $k++) {
                    if (!empty($stacks[$k])) {
                        $idx = array_pop($stacks[$k]);
                        $removed[$idx] = true;
                        break;
                    }
                }
            } else {
                $idxChar = ord($c) - 97; // 'a' => 0
                $stacks[$idxChar][] = $i;
            }
        }

        $result = '';
        for ($i = 0; $i < $n; $i++) {
            if (!$removed[$i] && $s[$i] !== '*') {
                $result .= $s[$i];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func clearStars(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        var removed = [Bool](repeating: false, count: n)
        var stacks = [[Int]](repeating: [], count: 26)
        
        for i in 0..<n {
            let ch = chars[i]
            if ch == "*" {
                for j in 0..<26 {
                    if !stacks[j].isEmpty {
                        let idx = stacks[j].removeLast()
                        removed[idx] = true
                        break
                    }
                }
            } else {
                if let ascii = ch.asciiValue {
                    let idx = Int(ascii - Character("a").asciiValue!)
                    stacks[idx].append(i)
                }
            }
        }
        
        var result = ""
        for i in 0..<n {
            if !removed[i] && chars[i] != "*" {
                result.append(chars[i])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun clearStars(s: String): String {
        val n = s.length
        val removed = BooleanArray(n)
        val stacks = Array(26) { java.util.ArrayDeque<Int>() }
        for (i in 0 until n) {
            val ch = s[i]
            if (ch == '*') {
                var cIdx = -1
                for (c in 0 until 26) {
                    if (!stacks[c].isEmpty()) {
                        cIdx = c
                        break
                    }
                }
                // According to problem constraints, there will always be a character to delete.
                val delPos = stacks[cIdx].removeLast()
                removed[delPos] = true
            } else {
                val idx = ch - 'a'
                stacks[idx].addLast(i)
            }
        }
        val sb = StringBuilder()
        for (i in 0 until n) {
            if (!removed[i] && s[i] != '*') {
                sb.append(s[i])
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String clearStars(String s) {
    int n = s.length;
    List<List<int>> stacks = List.generate(26, (_) => []);
    List<bool> deleted = List.filled(n, false);
    for (int i = 0; i < n; ++i) {
      int code = s.codeUnitAt(i);
      if (code == 42) { // '*'
        for (int c = 0; c < 26; ++c) {
          if (stacks[c].isNotEmpty) {
            int idx = stacks[c].removeLast();
            deleted[idx] = true;
            break;
          }
        }
      } else {
        int ci = code - 97; // 'a'
        stacks[ci].add(i);
      }
    }
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < n; ++i) {
      if (!deleted[i] && s.codeUnitAt(i) != 42) {
        sb.writeCharCode(s.codeUnitAt(i));
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
func clearStars(s string) string {
	stack := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == '*' {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, c)
		}
	}
	return string(stack)
}
```

## Ruby

```ruby
def clear_stars(s)
  n = s.length
  removed = Array.new(n, false)
  stacks = Array.new(26) { [] }

  s.each_char.with_index do |ch, i|
    if ch == '*'
      (0...26).each do |c|
        unless stacks[c].empty?
          idx = stacks[c].pop
          removed[idx] = true
          break
        end
      end
    else
      stacks[ch.ord - 97] << i
    end
  end

  result = []
  s.each_char.with_index do |ch, i|
    next if ch == '*'
    next if removed[i]
    result << ch
  end
  result.join
end
```

## Scala

```scala
object Solution {
  def clearStars(s: String): String = {
    val n = s.length
    val arr = s.toCharArray
    val stacks = Array.fill(26)(new scala.collection.mutable.Stack[Int]())
    var i = 0
    while (i < n) {
      val ch = arr(i)
      if (ch == '*') {
        var j = 0
        var removed = false
        while (j < 26 && !removed) {
          if (stacks(j).nonEmpty) {
            val idx = stacks(j).pop()
            arr(idx) = '*'
            removed = true
          }
          j += 1
        }
      } else {
        stacks(ch - 'a').push(i)
      }
      i += 1
    }
    val sb = new StringBuilder
    var k = 0
    while (k < n) {
      if (arr(k) != '*') sb.append(arr(k))
      k += 1
    }
    sb.toString()
  }
}
```

## Rust

```rust
impl Solution {
    pub fn clear_stars(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut stacks: Vec<Vec<usize>> = vec![Vec::new(); 26];
        let mut removed = vec![false; n];

        for (i, &b) in bytes.iter().enumerate() {
            if b == b'*' {
                for c in 0..26 {
                    if let Some(&idx) = stacks[c].last() {
                        stacks[c].pop();
                        removed[idx] = true;
                        break;
                    }
                }
            } else {
                let ci = (b - b'a') as usize;
                stacks[ci].push(i);
            }
        }

        let mut result = String::with_capacity(n);
        for (i, &b) in bytes.iter().enumerate() {
            if !removed[i] && b != b'*' {
                result.push(b as char);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (clear-stars s)
  (-> string? string?)
  (let* ((n (string-length s))
         (removed (make-vector n #f))
         (stacks (for/vector ([i 26]) '()))) ; each stack holds indices of that character
    ;; process the string
    (for ([i (in-range n)])
      (let ((ch (string-ref s i)))
        (if (char=? ch #\*)
            (let loop ((c 0))
              (when (< c 26)
                (let ((stk (vector-ref stacks c)))
                  (if (null? stk)
                      (loop (+ c 1))
                      (begin
                        (define idx (car stk))
                        (vector-set! stacks c (cdr stk))
                        (vector-set! removed idx #t))))))
            (let* ((c (- (char->integer ch) (char->integer #\a)))
                   (stk (vector-ref stacks c)))
              (vector-set! stacks c (cons i stk))))))
    ;; build the resulting string
    (let build ((i 0) (acc '()))
      (if (= i n)
          (list->string (reverse acc))
          (let ((ch (string-ref s i)))
            (if (or (char=? ch #\*) (vector-ref removed i))
                (build (+ i 1) acc)
                (build (+ i 1) (cons ch acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([clear_stars/1]).

-spec clear_stars(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
clear_stars(S) ->
    List = binary_to_list(S),
    EmptyStacks = erlang:make_tuple(26, []),
    {_, DeletedMap} = process(List, 1, EmptyStacks, #{}),
    ResultList = build_result(List, 1, DeletedMap, []),
    list_to_binary(lists:reverse(ResultList)).

process([], _Idx, Stacks, Del) ->
    {Stacks, Del};
process([C|Rest], Idx, Stacks, Del) ->
    case C of
        $* ->
            SmallIdx = find_smallest(Stacks),
            case SmallIdx of
                undefined ->
                    process(Rest, Idx + 1, Stacks, Del);
                CharIdx ->
                    Stack = element(CharIdx + 1, Stacks),
                    [Pos | NewStack] = Stack,
                    NewStacks = setelement(CharIdx + 1, Stacks, NewStack),
                    NewDel = maps:put(Pos, true, Del),
                    process(Rest, Idx + 1, NewStacks, NewDel)
            end;
        _ ->
            CharIdx = C - $a,
            Stack = element(CharIdx + 1, Stacks),
            NewStack = [Idx | Stack],
            NewStacks = setelement(CharIdx + 1, Stacks, NewStack),
            process(Rest, Idx + 1, NewStacks, Del)
    end.

find_smallest(Stacks) -> find_smallest(0, Stacks).

find_smallest(26, _Stacks) ->
    undefined;
find_smallest(I, Stacks) ->
    case element(I + 1, Stacks) of
        [] -> find_smallest(I + 1, Stacks);
        [_|_] -> I
    end.

build_result([], _Idx, _Del, Acc) ->
    Acc;
build_result([C|Rest], Idx, Del, Acc) ->
    if C =:= $* ->
            build_result(Rest, Idx + 1, Del, Acc);
       true ->
            case maps:is_key(Idx, Del) of
                true -> build_result(Rest, Idx + 1, Del, Acc);
                false -> build_result(Rest, Idx + 1, Del, [C | Acc])
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec clear_stars(s :: String.t()) :: String.t()
  def clear_stars(s) do
    chars = String.to_charlist(s)
    n = length(chars)

    {del_arr, stacks} =
      Enum.reduce(Enum.with_index(chars), {:array.new(n, default: false), :erlang.make_tuple(26, [])},
        fn {ch, idx}, {del_arr, stacks} ->
          if ch == ?* do
            {del_idx, new_stacks} = pop_smallest(stacks)
            {:array.set(del_idx, true, del_arr), new_stacks}
          else
            ci = ch - ?a
            cur = elem(stacks, ci)
            stacks = put_elem(stacks, ci, [idx | cur])
            {del_arr, stacks}
          end
        end)

    chars
    |> Enum.with_index()
    |> Enum.filter(fn {ch, i} -> ch != ?* and not :array.get(i, del_arr) end)
    |> Enum.map(fn {ch, _} -> <<ch>> end)
    |> Enum.join()
  end

  defp pop_smallest(stacks) do
    result =
      Enum.reduce_while(0..25, nil, fn i, _acc ->
        stack = elem(stacks, i)

        if stack == [] do
          {:cont, nil}
        else
          [idx | rest] = stack
          new_stacks = put_elem(stacks, i, rest)
          {:halt, {idx, new_stacks}}
        end
      end)

    case result do
      nil -> raise "No character to delete"
      {idx, new_stacks} -> {idx, new_stacks}
    end
  end
end
```
