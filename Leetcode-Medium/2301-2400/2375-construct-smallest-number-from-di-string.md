# 2375. Construct Smallest Number From DI String

## Cpp

```cpp
class Solution {
public:
    string smallestNumber(string pattern) {
        int n = pattern.size();
        string result;
        vector<int> stk;
        for (int i = 0; i <= n; ++i) {
            stk.push_back(i + 1);
            if (i == n || pattern[i] == 'I') {
                while (!stk.empty()) {
                    result += char('0' + stk.back());
                    stk.pop_back();
                }
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String smallestNumber(String pattern) {
        int n = pattern.length();
        StringBuilder sb = new StringBuilder();
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i <= n; i++) {
            stack.push(i + 1);
            if (i == n || pattern.charAt(i) == 'I') {
                while (!stack.isEmpty()) {
                    sb.append(stack.pop());
                }
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        stack = []
        result = []
        n = len(pattern)
        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return ''.join(result)
```

## Python3

```python
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []
        n = len(pattern)
        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* smallestNumber(char* pattern) {
    int n = strlen(pattern);
    char *res = (char*)malloc(n + 2); // length n+1 plus null terminator
    int pos = 0;
    int stack[10];
    int top = 0;

    for (int i = 0; i <= n; ++i) {
        stack[top++] = i + 1;
        if (i == n || pattern[i] == 'I') {
            while (top > 0) {
                int val = stack[--top];
                res[pos++] = (char)('0' + val);
            }
        }
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string SmallestNumber(string pattern)
    {
        var result = new System.Text.StringBuilder();
        var stack = new System.Collections.Generic.Stack<int>();
        int n = pattern.Length;
        for (int i = 0; i <= n; i++)
        {
            stack.Push(i + 1);
            if (i == n || pattern[i] == 'I')
            {
                while (stack.Count > 0)
                    result.Append(stack.Pop());
            }
        }
        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} pattern
 * @return {string}
 */
var smallestNumber = function(pattern) {
    const n = pattern.length;
    const stack = [];
    let result = '';
    for (let i = 0; i <= n; i++) {
        stack.push(i + 1);
        if (i === n || pattern[i] === 'I') {
            while (stack.length) {
                result += stack.pop();
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function smallestNumber(pattern: string): string {
    const n = pattern.length;
    const stack: number[] = [];
    let result = "";
    for (let i = 0; i <= n; i++) {
        stack.push(i + 1);
        if (i === n || pattern[i] === 'I') {
            while (stack.length) {
                result += stack.pop()!.toString();
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $pattern
     * @return String
     */
    function smallestNumber($pattern) {
        $n = strlen($pattern);
        $stack = [];
        $result = '';
        for ($i = 0; $i <= $n; $i++) {
            $stack[] = $i + 1;
            if ($i == $n || $pattern[$i] === 'I') {
                while (!empty($stack)) {
                    $result .= array_pop($stack);
                }
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func smallestNumber(_ pattern: String) -> String {
        let chars = Array(pattern)
        var stack = [Int]()
        var result = ""
        let n = chars.count
        for i in 0...n {
            stack.append(i + 1)
            if i == n || (i < n && chars[i] == "I") {
                while !stack.isEmpty {
                    result += String(stack.removeLast())
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestNumber(pattern: String): String {
        val n = pattern.length
        val result = StringBuilder()
        val stack = mutableListOf<Int>()
        for (i in 0..n) {
            stack.add(i + 1)
            if (i == n || pattern[i] == 'I') {
                while (stack.isNotEmpty()) {
                    result.append(stack.removeAt(stack.size - 1))
                }
            }
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String smallestNumber(String pattern) {
    List<int> stack = [];
    StringBuffer result = StringBuffer();
    int n = pattern.length;
    for (int i = 0; i <= n; ++i) {
      stack.add(i + 1);
      if (i == n || pattern[i] == 'I') {
        while (stack.isNotEmpty) {
          result.write(stack.removeLast());
        }
      }
    }
    return result.toString();
  }
}
```

## Golang

```go
func smallestNumber(pattern string) string {
    n := len(pattern)
    stack := []int{}
    result := make([]byte, 0, n+1)

    for i := 0; i <= n; i++ {
        stack = append(stack, i+1)
        if i == n || pattern[i] == 'I' {
            for len(stack) > 0 {
                top := stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                result = append(result, byte('0'+top))
            }
        }
    }

    return string(result)
}
```

## Ruby

```ruby
def smallest_number(pattern)
  n = pattern.length
  stack = []
  result = +""
  (0..n).each do |i|
    stack << i + 1
    if i == n || pattern[i] == 'I'
      while !stack.empty?
        result << stack.pop.to_s
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def smallestNumber(pattern: String): String = {
        val n = pattern.length
        val sb = new StringBuilder()
        val stack = scala.collection.mutable.Stack[Int]()
        for (i <- 0 to n) {
            stack.push(i + 1)
            if (i == n || pattern.charAt(i) == 'I') {
                while (stack.nonEmpty) {
                    sb.append(stack.pop())
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
    pub fn smallest_number(pattern: String) -> String {
        let bytes = pattern.as_bytes();
        let n = bytes.len();
        let mut stack: Vec<u8> = Vec::new();
        let mut result = String::new();

        for i in 0..=n {
            stack.push((i + 1) as u8);
            if i == n || (i < n && bytes[i] == b'I') {
                while let Some(num) = stack.pop() {
                    result.push((b'0' + num) as char);
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (smallest-number pattern)
  (-> string? string?)
  (let* ([n (string-length pattern)]
         [stack '()]
         [result ""])
    (for ([i (in-range (add1 n))])
      (set! stack (cons (+ i 1) stack))
      (when (or (= i n)
                (char=? (string-ref pattern i) #\I))
        (let loop ()
          (unless (null? stack)
            (let ([num (car stack)])
              (set! result (string-append result (number->string num)))
              (set! stack (cdr stack))
              (loop))))))
    result))
```

## Erlang

```erlang
-spec smallest_number(Pattern :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_number(Pattern) ->
    Len = byte_size(Pattern),
    ResultList = process(0, Len, Pattern, [], []),
    list_to_binary(ResultList).

process(Index, Len, _Pattern, _Stack, Res) when Index > Len ->
    Res;
process(Index, Len, Pattern, Stack, Res) ->
    Num = Index + 1,
    NewStack = [Num | Stack],
    Cond = (Index == Len) orelse (binary:at(Pattern, Index) =:= $I),
    if
        Cond ->
            NewRes = pop_all(NewStack, Res),
            process(Index + 1, Len, Pattern, [], NewRes);
        true ->
            process(Index + 1, Len, Pattern, NewStack, Res)
    end.

pop_all([], Res) -> Res;
pop_all([H|T], Res) ->
    Char = $0 + H,
    pop_all(T, Res ++ [Char]).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_number(pattern :: String.t) :: String.t
  def smallest_number(pattern) do
    n = String.length(pattern)
    chars = String.graphemes(pattern)

    {result, _} =
      Enum.reduce(0..n, {"", []}, fn i, {res, stack} ->
        new_stack = [i + 1 | stack]

        cond do
          i == n or (i < n && Enum.at(chars, i) == "I") ->
            new_res =
              Enum.reduce(new_stack, res, fn num, acc ->
                acc <> Integer.to_string(num)
              end)

            {new_res, []}

          true ->
            {res, new_stack}
        end
      end)

    result
  end
end
```
