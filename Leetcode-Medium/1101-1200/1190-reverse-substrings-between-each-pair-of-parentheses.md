# 1190. Reverse Substrings Between Each Pair of Parentheses

## Cpp

```cpp
class Solution {
public:
    string reverseParentheses(string s) {
        int n = s.size();
        vector<int> pairIdx(n);
        stack<int> st;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '(') {
                st.push(i);
            } else if (s[i] == ')') {
                int j = st.top(); st.pop();
                pairIdx[i] = j;
                pairIdx[j] = i;
            }
        }
        string res;
        for (int i = 0, dir = 1; i >= 0 && i < n; i += dir) {
            if (s[i] == '(' || s[i] == ')') {
                i = pairIdx[i];
                dir = -dir;
            } else {
                res.push_back(s[i]);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String reverseParentheses(String s) {
        int n = s.length();
        int[] pair = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else if (c == ')') {
                int j = stack.pop();
                pair[i] = j;
                pair[j] = i;
            }
        }

        StringBuilder sb = new StringBuilder();
        int i = 0, dir = 1;
        while (i < n) {
            char c = s.charAt(i);
            if (c == '(' || c == ')') {
                i = pair[i];
                dir = -dir;
            } else {
                sb.append(c);
            }
            i += dir;
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pair = [0] * n
        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i = 0
        d = 1
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)
```

## Python3

```python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i = 0
        direction = 1
        while 0 <= i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction

        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* reverseParentheses(char* s) {
    int n = (int)strlen(s);
    if (n == 0) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    int *pair = (int *)malloc(sizeof(int) * n);
    int *stack = (int *)malloc(sizeof(int) * n);
    int top = -1;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '(') {
            stack[++top] = i;
        } else if (s[i] == ')') {
            int j = stack[top--];
            pair[i] = j;
            pair[j] = i;
        }
    }

    char *res = (char *)malloc(n + 1);
    int idx = 0;
    int i = 0;
    int dir = 1;

    while (i >= 0 && i < n) {
        if (s[i] == '(' || s[i] == ')') {
            i = pair[i];
            dir = -dir;
        } else {
            res[idx++] = s[i];
        }
        i += dir;
    }

    res[idx] = '\0';
    free(pair);
    free(stack);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ReverseParentheses(string s)
    {
        int n = s.Length;
        int[] pair = new int[n];
        var stack = new Stack<int>();

        for (int i = 0; i < n; i++)
        {
            if (s[i] == '(')
                stack.Push(i);
            else if (s[i] == ')')
            {
                int j = stack.Pop();
                pair[i] = j;
                pair[j] = i;
            }
        }

        var sb = new System.Text.StringBuilder();
        int idx = 0, dir = 1;

        while (idx >= 0 && idx < n)
        {
            char c = s[idx];
            if (c == '(' || c == ')')
            {
                idx = pair[idx];
                dir = -dir;
            }
            else
            {
                sb.Append(c);
            }
            idx += dir;
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
var reverseParentheses = function(s) {
    const n = s.length;
    const pair = new Array(n).fill(0);
    const stack = [];
    for (let i = 0; i < n; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else if (s[i] === ')') {
            const j = stack.pop();
            pair[i] = j;
            pair[j] = i;
        }
    }
    const result = [];
    let i = 0, dir = 1;
    while (i < n) {
        if (s[i] === '(' || s[i] === ')') {
            i = pair[i];
            dir = -dir;
        } else {
            result.push(s[i]);
        }
        i += dir;
    }
    return result.join('');
};
```

## Typescript

```typescript
function reverseParentheses(s: string): string {
    const n = s.length;
    const pair = new Array<number>(n).fill(-1);
    const stack: number[] = [];
    for (let i = 0; i < n; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else if (s[i] === ')') {
            const j = stack.pop()!;
            pair[i] = j;
            pair[j] = i;
        }
    }

    const result: string[] = [];
    let i = 0;
    let dir = 1; // forward

    while (i >= 0 && i < n) {
        const ch = s[i];
        if (ch === '(' || ch === ')') {
            i = pair[i];
            dir = -dir;
        } else {
            result.push(ch);
        }
        i += dir;
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
    function reverseParentheses($s) {
        $n = strlen($s);
        $pair = array_fill(0, $n, -1);
        $stack = [];

        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') {
                $stack[] = $i;
            } elseif ($s[$i] === ')') {
                $j = array_pop($stack);
                $pair[$i] = $j;
                $pair[$j] = $i;
            }
        }

        $res = '';
        $i = 0;
        $dir = 1;

        while ($i >= 0 && $i < $n) {
            $c = $s[$i];
            if ($c === '(' || $c === ')') {
                $i = $pair[$i];
                $dir = -$dir;
            } else {
                $res .= $c;
            }
            $i += $dir;
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func reverseParentheses(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        var pair = [Int](repeating: 0, count: n)
        var stack = [Int]()
        
        for i in 0..<n {
            if chars[i] == "(" {
                stack.append(i)
            } else if chars[i] == ")" {
                let j = stack.removeLast()
                pair[i] = j
                pair[j] = i
            }
        }
        
        var result = ""
        var index = 0
        var direction = 1
        
        while index >= 0 && index < n {
            let ch = chars[index]
            if ch == "(" || ch == ")" {
                index = pair[index]
                direction = -direction
            } else {
                result.append(ch)
            }
            index += direction
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseParentheses(s: String): String {
        val n = s.length
        val pair = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            when (s[i]) {
                '(' -> stack.push(i)
                ')' -> {
                    val j = stack.pop()
                    pair[i] = j
                    pair[j] = i
                }
            }
        }
        val sb = StringBuilder()
        var idx = 0
        var step = 1
        while (idx >= 0 && idx < n) {
            val ch = s[idx]
            if (ch == '(' || ch == ')') {
                idx = pair[idx]
                step = -step
            } else {
                sb.append(ch)
            }
            idx += step
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String reverseParentheses(String s) {
    int n = s.length;
    List<int> pair = List.filled(n, -1);
    List<int> stack = [];

    for (int i = 0; i < n; i++) {
      if (s[i] == '(') {
        stack.add(i);
      } else if (s[i] == ')') {
        int j = stack.removeLast();
        pair[i] = j;
        pair[j] = i;
      }
    }

    StringBuffer sb = StringBuffer();
    int i = 0;
    int dir = 1;

    while (i >= 0 && i < n) {
      if (s[i] == '(' || s[i] == ')') {
        i = pair[i];
        dir = -dir;
      } else {
        sb.write(s[i]);
      }
      i += dir;
    }

    return sb.toString();
  }
}
```

## Golang

```go
func reverseParentheses(s string) string {
	n := len(s)
	pair := make([]int, n)
	stack := []int{}
	for i := 0; i < n; i++ {
		switch s[i] {
		case '(':
			stack = append(stack, i)
		case ')':
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			pair[i] = j
			pair[j] = i
		}
	}
	var res []byte
	for i, dir := 0, 1; i >= 0 && i < n; {
		if s[i] == '(' || s[i] == ')' {
			i = pair[i]
			dir = -dir
		} else {
			res = append(res, s[i])
		}
		i += dir
	}
	return string(res)
}
```

## Ruby

```ruby
def reverse_parentheses(s)
  n = s.length
  pair = Array.new(n, -1)
  stack = []

  s.each_char.with_index do |ch, i|
    if ch == '('
      stack << i
    elsif ch == ')'
      j = stack.pop
      pair[i] = j
      pair[j] = i
    end
  end

  result = +''
  i = 0
  dir = 1
  while i >= 0 && i < n
    if s[i] == '(' || s[i] == ')'
      i = pair[i]
      dir = -dir
    else
      result << s[i]
    end
    i += dir
  end

  result
end
```

## Scala

```scala
object Solution {
  def reverseParentheses(s: String): String = {
    val n = s.length
    val pair = new Array[Int](n)
    val stack = new java.util.ArrayDeque[Int]()
    var i = 0
    while (i < n) {
      s.charAt(i) match {
        case '(' => stack.push(i)
        case ')' =>
          val j = stack.pop()
          pair(i) = j
          pair(j) = i
        case _ => // do nothing
      }
      i += 1
    }

    val sb = new StringBuilder()
    var idx = 0
    var dir = 1
    while (idx >= 0 && idx < n) {
      s.charAt(idx) match {
        case '(' | ')' =>
          idx = pair(idx)
          dir = -dir
        case c =>
          sb.append(c)
      }
      idx += dir
    }

    sb.toString()
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut pair = vec![0usize; n];
        let mut stack: Vec<usize> = Vec::new();

        for (i, &b) in bytes.iter().enumerate() {
            match b as char {
                '(' => stack.push(i),
                ')' => {
                    if let Some(open) = stack.pop() {
                        pair[open] = i;
                        pair[i] = open;
                    }
                }
                _ => {}
            }
        }

        let mut result = String::with_capacity(n);
        let mut idx: isize = 0;
        let mut dir: isize = 1;

        while idx >= 0 && (idx as usize) < n {
            let i = idx as usize;
            let ch = bytes[i] as char;
            if ch == '(' || ch == ')' {
                idx = pair[i] as isize;
                dir = -dir;
            } else {
                result.push(ch);
            }
            idx += dir;
        }

        result
    }
}
```

## Racket

```racket
(define/contract (reverse-parentheses s)
  (-> string? string?)
  (let* ((n (string-length s))
         (pair (make-vector n -1)))
    ;; First pass: match parentheses
    (let loop ((i 0) (stack '()))
      (when (< i n)
        (define ch (string-ref s i))
        (cond [(char=? ch #\()
               (loop (+ i 1) (cons i stack))]
              [(char=? ch #\))
               (define open (car stack))
               (vector-set! pair i open)
               (vector-set! pair open i)
               (loop (+ i 1) (cdr stack))]
              [else
               (loop (+ i 1) stack)])))
    ;; Second pass: build result
    (let build ((i 0) (dir 1) (acc '()))
      (if (or (< i 0) (>= i n))
          (list->string (reverse acc))
          (let ((ch (string-ref s i)))
            (if (or (char=? ch #\() (char=? ch #\)))
                (let* ((j (vector-ref pair i))
                       (new-dir (- dir))
                       (next-i (+ j new-dir)))
                  (build next-i new-dir acc))
                (build (+ i dir) dir (cons ch acc))))))))
```

## Erlang

```erlang
-spec reverse_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_parentheses(S) ->
    Chars = binary_to_list(S),
    Len = length(Chars),
    Tuple = list_to_tuple(Chars),
    PairMap = build_pairs(Tuple, Len, 0, [], #{}),
    RevAcc = traverse(Tuple, Len, PairMap, 0, 1, []),
    list_to_binary(lists:reverse(RevAcc)).

%% Build map of matching parentheses indices.
-spec build_pairs(tuple(), non_neg_integer(), non_neg_integer(),
                 [non_neg_integer()], map()) -> map().
build_pairs(_Tuple, Len, Index, _Stack, Map) when Index == Len ->
    Map;
build_pairs(Tuple, Len, Index, Stack, Map) ->
    Char = element(Index + 1, Tuple),
    case Char of
        $( ->
            build_pairs(Tuple, Len, Index + 1, [Index | Stack], Map);
        $) ->
            [OpenIdx | Rest] = Stack,
            NewMap1 = maps:put(OpenIdx, Index, Map),
            NewMap2 = maps:put(Index, OpenIdx, NewMap1),
            build_pairs(Tuple, Len, Index + 1, Rest, NewMap2);
        _ ->
            build_pairs(Tuple, Len, Index + 1, Stack, Map)
    end.

%% Traverse using wormhole technique to construct result.
-spec traverse(tuple(), non_neg_integer(), map(),
              integer(), integer(), [integer()]) -> [integer()].
traverse(_Tuple, Len, _PairMap, I, _Dir, Acc) when I < 0; I >= Len ->
    Acc;
traverse(Tuple, Len, PairMap, I, Dir, Acc) ->
    Char = element(I + 1, Tuple),
    case Char of
        $( ;
        $) ->
            MatchIdx = maps:get(I, PairMap),
            NewDir = -Dir,
            NextI = MatchIdx + NewDir,
            traverse(Tuple, Len, PairMap, NextI, NewDir, Acc);
        _ ->
            traverse(Tuple, Len, PairMap, I + Dir, Dir, [Char | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_parentheses(s :: String.t()) :: String.t()
  def reverse_parentheses(s) do
    chars = String.graphemes(s)
    n = length(chars)

    pair_map = build_pair(chars)
    arr = :array.from_list(chars)

    dfs(0, 1, n, arr, pair_map, [])
  end

  defp build_pair(chars) do
    {pair, _stack} =
      Enum.reduce(Enum.with_index(chars), {%{}, []}, fn {ch, idx}, {pair, stack} ->
        cond do
          ch == "(" -> {pair, [idx | stack]}
          ch == ")" ->
            [open | rest] = stack
            pair1 = Map.put(pair, open, idx)
            pair2 = Map.put(pair1, idx, open)
            {pair2, rest}
          true -> {pair, stack}
        end
      end)

    pair
  end

  defp dfs(i, dir, n, arr, pair, acc) do
    if i < 0 or i >= n do
      acc |> Enum.reverse() |> Enum.join()
    else
      ch = :array.get(i, arr)

      if ch == "(" or ch == ")" do
        j = Map.get(pair, i)
        dfs(j + -dir, -dir, n, arr, pair, acc)
      else
        dfs(i + dir, dir, n, arr, pair, [ch | acc])
      end
    end
  end
end
```
