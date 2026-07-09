# 1209. Remove All Adjacent Duplicates in String II

## Cpp

```cpp
class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char,int>> st;
        for (char c : s) {
            if (!st.empty() && st.back().first == c) {
                ++st.back().second;
                if (st.back().second == k) {
                    st.pop_back();
                }
            } else {
                st.emplace_back(c, 1);
            }
        }
        string res;
        res.reserve(s.size());
        for (auto &p : st) {
            res.append(p.second, p.first);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String removeDuplicates(String s, int k) {
        int n = s.length();
        char[] chars = new char[n];
        int[] counts = new int[n];
        int top = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (top > 0 && chars[top - 1] == c) {
                counts[top - 1]++;
            } else {
                chars[top] = c;
                counts[top] = 1;
                top++;
            }
            if (top > 0 && counts[top - 1] == k) {
                top--;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < top; i++) {
            for (int j = 0; j < counts[i]; j++) {
                sb.append(chars[i]);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []  # each element is [char, count]
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        # reconstruct result
        return ''.join(ch * cnt for ch, cnt in stack)
```

## Python3

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # each element is [char, count]
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        return ''.join(ch * cnt for ch, cnt in stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* removeDuplicates(char* s, int k) {
    int n = strlen(s);
    struct Node { char ch; int cnt; };
    struct Node *stack = (struct Node*)malloc(sizeof(struct Node) * n);
    int top = -1;
    
    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (top >= 0 && stack[top].ch == c) {
            stack[top].cnt++;
            if (stack[top].cnt == k) {
                --top;
            }
        } else {
            ++top;
            stack[top].ch = c;
            stack[top].cnt = 1;
        }
    }
    
    int total = 0;
    for (int i = 0; i <= top; ++i) {
        total += stack[i].cnt;
    }
    
    char *res = (char*)malloc(total + 1);
    int idx = 0;
    for (int i = 0; i <= top; ++i) {
        for (int j = 0; j < stack[i].cnt; ++j) {
            res[idx++] = stack[i].ch;
        }
    }
    res[idx] = '\0';
    
    free(stack);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string RemoveDuplicates(string s, int k)
    {
        int n = s.Length;
        char[] chars = new char[n];
        int[] counts = new int[n];
        int top = -1;

        foreach (char c in s)
        {
            if (top >= 0 && chars[top] == c)
            {
                counts[top]++;
                if (counts[top] == k)
                {
                    top--;
                }
            }
            else
            {
                top++;
                chars[top] = c;
                counts[top] = 1;
            }
        }

        var result = new System.Text.StringBuilder();
        for (int i = 0; i <= top; i++)
        {
            result.Append(new string(chars[i], counts[i]));
        }

        return result.ToString();
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
var removeDuplicates = function(s, k) {
    const stack = [];
    for (const ch of s) {
        if (stack.length && stack[stack.length - 1][0] === ch) {
            stack[stack.length - 1][1]++;
            if (stack[stack.length - 1][1] === k) {
                stack.pop();
            }
        } else {
            stack.push([ch, 1]);
        }
    }
    let result = '';
    for (const [char, cnt] of stack) {
        result += char.repeat(cnt);
    }
    return result;
};
```

## Typescript

```typescript
function removeDuplicates(s: string, k: number): string {
    const stack: { ch: string; cnt: number }[] = [];
    for (const c of s) {
        if (stack.length && stack[stack.length - 1].ch === c) {
            stack[stack.length - 1].cnt += 1;
            if (stack[stack.length - 1].cnt === k) {
                stack.pop();
            }
        } else {
            stack.push({ ch: c, cnt: 1 });
        }
    }
    const result: string[] = [];
    for (const { ch, cnt } of stack) {
        result.push(ch.repeat(cnt));
    }
    return result.join('');
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
    function removeDuplicates($s, $k) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (!empty($stack) && $stack[count($stack) - 1][0] === $c) {
                $stack[count($stack) - 1][1]++;
                if ($stack[count($stack) - 1][1] == $k) {
                    array_pop($stack);
                }
            } else {
                $stack[] = [$c, 1];
            }
        }

        $result = '';
        foreach ($stack as $pair) {
            $result .= str_repeat($pair[0], $pair[1]);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func removeDuplicates(_ s: String, _ k: Int) -> String {
        var stack: [(char: Character, count: Int)] = []
        for ch in s {
            if let last = stack.last, last.char == ch {
                let newCount = last.count + 1
                stack[stack.count - 1].count = newCount
                if newCount == k {
                    stack.removeLast()
                }
            } else {
                stack.append((ch, 1))
            }
        }
        var result = ""
        for (ch, cnt) in stack {
            for _ in 0..<cnt {
                result.append(ch)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeDuplicates(s: String, k: Int): String {
        val n = s.length
        val chars = CharArray(n)
        val counts = IntArray(n)
        var size = 0
        for (ch in s) {
            if (size > 0 && chars[size - 1] == ch) {
                counts[size - 1]++
                if (counts[size - 1] == k) {
                    size--
                }
            } else {
                chars[size] = ch
                counts[size] = 1
                size++
            }
        }
        val sb = StringBuilder()
        for (i in 0 until size) {
            repeat(counts[i]) { sb.append(chars[i]) }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String removeDuplicates(String s, int k) {
    List<String> chars = [];
    List<int> counts = [];

    for (int i = 0; i < s.length; i++) {
      String c = s[i];
      if (chars.isNotEmpty && chars.last == c) {
        counts[counts.length - 1] += 1;
        if (counts.last == k) {
          chars.removeLast();
          counts.removeLast();
        }
      } else {
        chars.add(c);
        counts.add(1);
      }
    }

    StringBuffer sb = StringBuffer();
    for (int i = 0; i < chars.length; i++) {
      for (int j = 0; j < counts[i]; j++) {
        sb.write(chars[i]);
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
func removeDuplicates(s string, k int) string {
	type pair struct {
		ch  byte
		cnt int
	}
	stack := make([]pair, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		if len(stack) > 0 && stack[len(stack)-1].ch == c {
			stack[len(stack)-1].cnt++
		} else {
			stack = append(stack, pair{ch: c, cnt: 1})
		}
		if stack[len(stack)-1].cnt == k {
			stack = stack[:len(stack)-1]
		}
	}
	var sb []byte
	for _, p := range stack {
		for i := 0; i < p.cnt; i++ {
			sb = append(sb, p.ch)
		}
	}
	return string(sb)
}
```

## Ruby

```ruby
def remove_duplicates(s, k)
  stack = []
  s.each_char do |ch|
    if !stack.empty? && stack[-1][0] == ch
      stack[-1][1] += 1
      stack.pop if stack[-1][1] == k
    else
      stack << [ch, 1]
    end
  end
  result = +""
  stack.each { |char, cnt| result << char * cnt }
  result
end
```

## Scala

```scala
object Solution {
  def removeDuplicates(s: String, k: Int): String = {
    val n = s.length
    val chars = new Array[Char](n)
    val cnt = new Array[Int](n)
    var top = -1
    for (c <- s) {
      if (top >= 0 && chars(top) == c) {
        cnt(top) += 1
        if (cnt(top) == k) {
          top -= 1
        }
      } else {
        top += 1
        chars(top) = c
        cnt(top) = 1
      }
    }
    val sb = new StringBuilder
    for (i <- 0 to top) {
      sb.append(chars(i).toString * cnt(i))
    }
    sb.toString()
  }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_duplicates(s: String, k: i32) -> String {
        let k = k as usize;
        let mut stack: Vec<(char, usize)> = Vec::new();
        for ch in s.chars() {
            if let Some(last) = stack.last_mut() {
                if last.0 == ch {
                    last.1 += 1;
                    if last.1 == k {
                        stack.pop();
                    }
                    continue;
                }
            }
            stack.push((ch, 1));
        }

        let mut result = String::with_capacity(s.len());
        for (ch, cnt) in stack {
            for _ in 0..cnt {
                result.push(ch);
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket/base

(require racket/contract)

(define/contract (remove-duplicates s k)
  (-> string? exact-integer? string?)
  (let ((len (string-length s))
        (stack '()))
    (for ([i (in-range len)])
      (let ((c (string-ref s i)))
        (if (and (pair? stack) (char=? (car (car stack)) c))
            (let* ((top (car stack))
                   (new-count (+ (cdr top) 1))
                   (new-top (cons c new-count)))
              (set! stack (cons new-top (cdr stack))) ; replace top
              (when (= new-count k)
                (set! stack (cdr stack)))) ; pop when count reaches k
            (set! stack (cons (cons c 1) stack)))))
    ;; Build the resulting string from the stack
    (let* ((pairs (reverse stack))
           (total (for/sum ([p pairs]) (cdr p)))
           (result (make-string total))
           (pos 0))
      (for ([p pairs])
        (define c (car p))
        (define cnt (cdr p))
        (for ([i (in-range cnt)])
          (string-set! result pos c)
          (set! pos (+ pos 1))))
      result)))
```

## Erlang

```erlang
-module(solution).
-export([remove_duplicates/2]).

-spec remove_duplicates(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
remove_duplicates(S, K) ->
    Stack = process(S, K, []),
    rebuild(Stack).

process(<<>>, _K, Stack) ->
    Stack;
process(<<C, Rest/binary>>, K, []) ->
    process(Rest, K, [{C, 1}]);
process(<<C, Rest/binary>>, K, [{C, Cnt}|Tail]) ->
    NewCnt = Cnt + 1,
    if
        NewCnt == K ->
            process(Rest, K, Tail);
        true ->
            process(Rest, K, [{C, NewCnt}|Tail])
    end;
process(<<C, Rest/binary>>, K, Stack=[{Top,_}|_]) when C =/= Top ->
    process(Rest, K, [{C, 1}|Stack]).

rebuild(Stack) ->
    Iolist = [binary:copy(<<Char>>, Count) || {Char, Count} <- lists:reverse(Stack)],
    iolist_to_binary(Iolist).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_duplicates(s :: String.t(), k :: integer()) :: String.t()
  def remove_duplicates(s, k) do
    chars = String.to_charlist(s)

    stack =
      Enum.reduce(chars, [], fn ch, acc ->
        case acc do
          [{c, cnt} | rest] when c == ch ->
            if cnt + 1 == k do
              rest
            else
              [{c, cnt + 1} | rest]
            end

          _ ->
            [{ch, 1} | acc]
        end
      end)

    stack
    |> Enum.reverse()
    |> Enum.flat_map(fn {c, cnt} -> List.duplicate(c, cnt) end)
    |> to_string()
  end
end
```
