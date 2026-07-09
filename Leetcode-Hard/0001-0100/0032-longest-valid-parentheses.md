# 0032. Longest Valid Parentheses

## Cpp

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLen = 0;
        vector<int> st;
        st.push_back(-1); // sentinel
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] == '(') {
                st.push_back(i);
            } else {
                st.pop_back();
                if (st.empty()) {
                    st.push_back(i);
                } else {
                    maxLen = max(maxLen, i - st.back());
                }
            }
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int longestValidParentheses(String s) {
        int maxLen = 0;
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    maxLen = Math.max(maxLen, i - stack.peek());
                }
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        left = right = 0

        # Left to right scan
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        # Right to left scan
        left = right = 0
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len
```

## Python3

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # sentinel for base index
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
```

## C

```c
#include <string.h>
#include <stdlib.h>

int longestValidParentheses(char* s) {
    if (!s) return 0;
    int n = strlen(s);
    int *stack = (int*)malloc((n + 2) * sizeof(int));
    int top = -1;
    stack[++top] = -1; // base index
    int maxlen = 0;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '(') {
            stack[++top] = i;
        } else { // ')'
            if (top >= 0) top--; // pop matching '(' or base
            if (top < 0) {
                stack[++top] = i; // new base
            } else {
                int len = i - stack[top];
                if (len > maxlen) maxlen = len;
            }
        }
    }

    free(stack);
    return maxlen;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestValidParentheses(string s)
    {
        int maxLen = 0;
        var stack = new System.Collections.Generic.Stack<int>();
        stack.Push(-1); // base for the first valid substring

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '(')
            {
                stack.Push(i);
            }
            else
            {
                stack.Pop();
                if (stack.Count == 0)
                {
                    // No matching '(', set new base
                    stack.Push(i);
                }
                else
                {
                    maxLen = System.Math.Max(maxLen, i - stack.Peek());
                }
            }
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let maxLen = 0;
    const stack = [-1]; // base for the first valid substring
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.length === 0) {
                stack.push(i); // new base
            } else {
                maxLen = Math.max(maxLen, i - stack[stack.length - 1]);
            }
        }
    }
    
    return maxLen;
};
```

## Typescript

```typescript
function longestValidParentheses(s: string): number {
    let maxLen = 0;
    const stack: number[] = [-1];
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.length === 0) {
                stack.push(i);
            } else {
                const len = i - stack[stack.length - 1];
                if (len > maxLen) maxLen = len;
            }
        }
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestValidParentheses($s) {
        $maxLen = 0;
        $stack = [-1]; // sentinel index
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') {
                $stack[] = $i;
            } else {
                array_pop($stack); // pop matching '(' or sentinel
                if (empty($stack)) {
                    // no base to compare, set current index as new sentinel
                    $stack[] = $i;
                } else {
                    $currentLen = $i - $stack[count($stack) - 1];
                    if ($currentLen > $maxLen) {
                        $maxLen = $currentLen;
                    }
                }
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        var maxLen = 0
        var stack = [Int]()
        stack.append(-1)
        let chars = Array(s)
        for i in 0..<chars.count {
            if chars[i] == "(" {
                stack.append(i)
            } else {
                _ = stack.popLast()
                if stack.isEmpty {
                    stack.append(i)
                } else {
                    maxLen = max(maxLen, i - stack.last!)
                }
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestValidParentheses(s: String): Int {
        var maxLen = 0
        val stack = java.util.ArrayDeque<Int>()
        stack.push(-1)
        for (i in s.indices) {
            if (s[i] == '(') {
                stack.push(i)
            } else {
                if (!stack.isEmpty()) {
                    stack.pop()
                }
                if (stack.isEmpty()) {
                    stack.push(i)
                } else {
                    val len = i - stack.peek()
                    if (len > maxLen) maxLen = len
                }
            }
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestValidParentheses(String s) {
    List<int> stack = [-1];
    int maxLen = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        stack.add(i);
      } else {
        if (stack.isNotEmpty) {
          stack.removeLast();
        }
        if (stack.isEmpty) {
          stack.add(i);
        } else {
          int len = i - stack.last;
          if (len > maxLen) maxLen = len;
        }
      }
    }
    return maxLen;
  }
}
```

## Golang

```go
func longestValidParentheses(s string) int {
    maxLen := 0
    stack := []int{-1}
    for i, ch := range s {
        if ch == '(' {
            stack = append(stack, i)
        } else {
            // pop the previous index
            stack = stack[:len(stack)-1]
            if len(stack) == 0 {
                // no matching '(', set new base
                stack = append(stack, i)
            } else {
                cur := i - stack[len(stack)-1]
                if cur > maxLen {
                    maxLen = cur
                }
            }
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def longest_valid_parentheses(s)
  max_len = 0
  stack = [-1]
  s.each_char.with_index do |ch, i|
    if ch == '('
      stack << i
    else
      stack.pop
      if stack.empty?
        stack << i
      else
        len = i - stack[-1]
        max_len = len if len > max_len
      end
    end
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestValidParentheses(s: String): Int = {
        var maxLen = 0
        val stack = new scala.collection.mutable.Stack[Int]()
        stack.push(-1)
        for (i <- s.indices) {
            if (s(i) == '(') {
                stack.push(i)
            } else {
                if (!stack.isEmpty) stack.pop()
                if (stack.isEmpty) {
                    stack.push(i)
                } else {
                    val len = i - stack.top
                    if (len > maxLen) maxLen = len
                }
            }
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut stack: Vec<isize> = Vec::new();
        stack.push(-1);
        let mut max_len: isize = 0;
        for (i, &c) in bytes.iter().enumerate() {
            if c == b'(' {
                stack.push(i as isize);
            } else {
                stack.pop();
                if stack.is_empty() {
                    stack.push(i as isize);
                } else {
                    let len = i as isize - *stack.last().unwrap();
                    if len > max_len {
                        max_len = len;
                    }
                }
            }
        }
        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (longest-valid-parentheses s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (maxlen 0)
         (left 0)
         (right 0))
    ;; left to right scan
    (for ([i (in-range n)])
      (let ((c (string-ref s i)))
        (cond [(char=? c #\()
               (set! left (+ left 1))]
              [else
               (set! right (+ right 1))]))
      (cond [(= left right)
             (set! maxlen (max maxlen (* 2 right)))]
            [(> right left)
             (set! left 0)
             (set! right 0)]))
    ;; reset counters for reverse scan
    (set! left 0)
    (set! right 0)
    ;; right to left scan
    (for ([i (in-range (sub1 n) -1 -1)])
      (let ((c (string-ref s i)))
        (cond [(char=? c #\()
               (set! left (+ left 1))]
              [else
               (set! right (+ right 1))]))
      (cond [(= left right)
             (set! maxlen (max maxlen (* 2 left)))]
            [(> left right)
             (set! left 0)
             (set! right 0)]))
    maxlen))
```

## Erlang

```erlang
-spec longest_valid_parentheses(S :: unicode:unicode_binary()) -> integer().
longest_valid_parentheses(S) ->
    List = binary_to_list(S),
    longest_valid_parentheses(List, 0, [-1], 0).

%% private recursive helper
longest_valid_parentheses([], _Idx, _Stack, Max) ->
    Max;
longest_valid_parentheses([Char|Rest], Idx, Stack, Max) ->
    case Char of
        $( ->
            longest_valid_parentheses(Rest, Idx + 1, [Idx | Stack], Max);
        $) ->
            case Stack of
                [_|RestStack] ->
                    NewStack = RestStack,
                    case NewStack of
                        [] ->
                            longest_valid_parentheses(Rest, Idx + 1, [Idx], Max);
                        [Top|_] ->
                            Len = Idx - Top,
                            NewMax = if Len > Max -> Len; true -> Max end,
                            longest_valid_parentheses(Rest, Idx + 1, NewStack, NewMax)
                    end;
                [] ->
                    longest_valid_parentheses(Rest, Idx + 1, [Idx], Max)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_valid_parentheses(s :: String.t()) :: integer
  def longest_valid_parentheses(s) do
    {max_len, _stack} =
      s
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({0, [-1]}, fn {ch, i}, {max_len, stack} ->
        if ch == "(" do
          {max_len, [i | stack]}
        else
          case stack do
            [_pop | rest] ->
              new_stack = rest

              if new_stack == [] do
                {max_len, [i]}
              else
                len = i - hd(new_stack)
                new_max = if len > max_len, do: len, else: max_len
                {new_max, new_stack}
              end
          end
        end
      end)

    max_len
  end
end
```
