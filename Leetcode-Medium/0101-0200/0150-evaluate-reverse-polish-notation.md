# 0150. Evaluate Reverse Polish Notation

## Cpp

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::vector<int> st;
        st.reserve(tokens.size());
        for (const string& tok : tokens) {
            if (tok == "+" || tok == "-" || tok == "*" || tok == "/") {
                int b = st.back(); st.pop_back();
                int a = st.back(); st.pop_back();
                int res = 0;
                if (tok == "+") res = a + b;
                else if (tok == "-") res = a - b;
                else if (tok == "*") res = a * b;
                else /* "/" */ res = a / b; // truncates toward zero in C++
                st.push_back(res);
            } else {
                st.push_back(std::stoi(tok));
            }
        }
        return st.back();
    }
};
```

## Java

```java
class Solution {
    public int evalRPN(String[] tokens) {
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        for (String token : tokens) {
            if (token.length() == 1 && "+-*/".indexOf(token.charAt(0)) != -1) {
                int b = stack.pop();
                int a = stack.pop();
                int res;
                switch (token.charAt(0)) {
                    case '+': res = a + b; break;
                    case '-': res = a - b; break;
                    case '*': res = a * b; break;
                    default:  // '/'
                        res = a / b;
                }
                stack.push(res);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }
}
```

## Python

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:  # division truncates toward zero
                    res = int(a / b)
                stack.append(res)
        return stack[0]
```

## Python3

```python
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division
                    # Truncate toward zero
                    stack.append(int(a / b))
        return stack[0]
```

## C

```c
#include <stdlib.h>

int evalRPN(char** tokens, int tokensSize) {
    int *stack = (int *)malloc(sizeof(int) * tokensSize);
    int top = -1;
    for (int i = 0; i < tokensSize; ++i) {
        char *tok = tokens[i];
        if ((tok[0] == '+' && tok[1] == '\0') ||
            (tok[0] == '-' && tok[1] == '\0') ||
            (tok[0] == '*' && tok[1] == '\0') ||
            (tok[0] == '/' && tok[1] == '\0')) {
            int b = stack[top--];
            int a = stack[top--];
            int res = 0;
            switch (tok[0]) {
                case '+': res = a + b; break;
                case '-': res = a - b; break;
                case '*': res = a * b; break;
                case '/': res = a / b; break;
            }
            stack[++top] = res;
        } else {
            int val = atoi(tok);
            stack[++top] = val;
        }
    }
    int result = stack[top];
    free(stack);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int EvalRPN(string[] tokens) {
        var stack = new System.Collections.Generic.Stack<int>();
        foreach (var token in tokens) {
            if (token.Length == 1 && "+-*/".Contains(token)) {
                int b = stack.Pop();
                int a = stack.Pop();
                int res = token[0] switch {
                    '+' => a + b,
                    '-' => a - b,
                    '*' => a * b,
                    '/' => a / b, // integer division truncates toward zero in C#
                    _   => 0
                };
                stack.Push(res);
            } else {
                stack.Push(int.Parse(token));
            }
        }
        return stack.Pop();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const stack = [];
    for (const token of tokens) {
        if (token === '+' || token === '-' || token === '*' || token === '/') {
            const b = stack.pop();
            const a = stack.pop();
            let result;
            switch (token) {
                case '+':
                    result = a + b;
                    break;
                case '-':
                    result = a - b;
                    break;
                case '*':
                    result = a * b;
                    break;
                case '/':
                    // Truncate toward zero
                    result = Math.trunc(a / b);
                    break;
            }
            stack.push(result);
        } else {
            stack.push(parseInt(token, 10));
        }
    }
    return stack.pop();
};
```

## Typescript

```typescript
function evalRPN(tokens: string[]): number {
    const stack: number[] = [];
    for (const token of tokens) {
        if (token === '+' || token === '-' || token === '*' || token === '/') {
            const b = stack.pop()!;
            const a = stack.pop()!;
            let result: number;
            switch (token) {
                case '+':
                    result = a + b;
                    break;
                case '-':
                    result = a - b;
                    break;
                case '*':
                    result = a * b;
                    break;
                default: // '/'
                    result = Math.trunc(a / b);
            }
            stack.push(result);
        } else {
            stack.push(parseInt(token, 10));
        }
    }
    return stack.pop()!;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $tokens
     * @return Integer
     */
    function evalRPN($tokens) {
        $stack = [];
        foreach ($tokens as $token) {
            if ($token === '+' || $token === '-' || $token === '*' || $token === '/') {
                $b = array_pop($stack);
                $a = array_pop($stack);
                switch ($token) {
                    case '+':
                        $res = $a + $b;
                        break;
                    case '-':
                        $res = $a - $b;
                        break;
                    case '*':
                        $res = $a * $b;
                        break;
                    case '/':
                        $res = intdiv($a, $b);
                        break;
                }
                $stack[] = $res;
            } else {
                $stack[] = (int)$token;
            }
        }
        return array_pop($stack);
    }
}
```

## Swift

```swift
class Solution {
    func evalRPN(_ tokens: [String]) -> Int {
        var stack = [Int]()
        for token in tokens {
            switch token {
            case "+":
                let b = stack.removeLast()
                let a = stack.removeLast()
                stack.append(a + b)
            case "-":
                let b = stack.removeLast()
                let a = stack.removeLast()
                stack.append(a - b)
            case "*":
                let b = stack.removeLast()
                let a = stack.removeLast()
                stack.append(a * b)
            case "/":
                let b = stack.removeLast()
                let a = stack.removeLast()
                stack.append(a / b) // Swift truncates toward zero
            default:
                if let num = Int(token) {
                    stack.append(num)
                }
            }
        }
        return stack.last ?? 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun evalRPN(tokens: Array<String>): Int {
        val stack = java.util.ArrayDeque<Int>()
        for (t in tokens) {
            when (t) {
                "+" -> {
                    val b = stack.removeLast()
                    val a = stack.removeLast()
                    stack.addLast(a + b)
                }
                "-" -> {
                    val b = stack.removeLast()
                    val a = stack.removeLast()
                    stack.addLast(a - b)
                }
                "*" -> {
                    val b = stack.removeLast()
                    val a = stack.removeLast()
                    stack.addLast(a * b)
                }
                "/" -> {
                    val b = stack.removeLast()
                    val a = stack.removeLast()
                    stack.addLast(a / b)
                }
                else -> stack.addLast(t.toInt())
            }
        }
        return stack.removeLast()
    }
}
```

## Dart

```dart
class Solution {
  int evalRPN(List<String> tokens) {
    List<int> stack = [];
    for (var token in tokens) {
      if (token == '+' || token == '-' || token == '*' || token == '/') {
        int b = stack.removeLast();
        int a = stack.removeLast();
        int result;
        switch (token) {
          case '+':
            result = a + b;
            break;
          case '-':
            result = a - b;
            break;
          case '*':
            result = a * b;
            break;
          default: // '/'
            result = a ~/ b; // truncates toward zero
        }
        stack.add(result);
      } else {
        stack.add(int.parse(token));
      }
    }
    return stack.last;
  }
}
```

## Golang

```go
func evalRPN(tokens []string) int {
	stack := make([]int, 0, len(tokens))
	for _, t := range tokens {
		switch t {
		case "+", "-", "*", "/":
			n := len(stack)
			b, a := stack[n-1], stack[n-2]
			stack = stack[:n-2]
			var res int
			switch t {
			case "+":
				res = a + b
			case "-":
				res = a - b
			case "*":
				res = a * b
			case "/":
				res = a / b
			}
			stack = append(stack, res)
		default:
			// parse integer (may be negative)
			val := 0
			sign := 1
			i := 0
			if t[0] == '-' {
				sign = -1
				i = 1
			}
			for ; i < len(t); i++ {
				val = val*10 + int(t[i]-'0')
			}
			stack = append(stack, sign*val)
		}
	}
	return stack[0]
}
```

## Ruby

```ruby
def eval_rpn(tokens)
  stack = []
  tokens.each do |token|
    case token
    when '+'
      b = stack.pop
      a = stack.pop
      stack << a + b
    when '-'
      b = stack.pop
      a = stack.pop
      stack << a - b
    when '*'
      b = stack.pop
      a = stack.pop
      stack << a * b
    when '/'
      b = stack.pop
      a = stack.pop
      # Truncate toward zero
      stack << (a.to_f / b).to_i
    else
      stack << token.to_i
    end
  end
  stack[-1]
end
```

## Scala

```scala
object Solution {
    def evalRPN(tokens: Array[String]): Int = {
        val stack = new java.util.ArrayDeque[Int]()
        for (t <- tokens) {
            t match {
                case "+" =>
                    val b = stack.pop()
                    val a = stack.pop()
                    stack.push(a + b)
                case "-" =>
                    val b = stack.pop()
                    val a = stack.pop()
                    stack.push(a - b)
                case "*" =>
                    val b = stack.pop()
                    val a = stack.pop()
                    stack.push(a * b)
                case "/" =>
                    val b = stack.pop()
                    val a = stack.pop()
                    stack.push(a / b) // integer division truncates toward zero
                case num =>
                    stack.push(num.toInt)
            }
        }
        stack.pop()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        for token in tokens.iter() {
            match token.as_str() {
                "+" => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    stack.push(a + b);
                }
                "-" => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    stack.push(a - b);
                }
                "*" => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    stack.push(a * b);
                }
                "/" => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    stack.push(a / b);
                }
                _ => {
                    let num = token.parse::<i32>().unwrap();
                    stack.push(num);
                }
            }
        }
        stack[0]
    }
}
```

## Racket

```racket
(define/contract (eval-rpn tokens)
  (-> (listof string?) exact-integer?)
  (let ([stack
         (foldl
          (lambda (tok st)
            (if (member tok '("+" "-" "*" "/"))
                (let* ([b (car st)]
                       [a (cadr st)]
                       [rest (cddr st)]
                       [res (cond [(string=? tok "+") (+ a b)]
                                  [(string=? tok "-") (- a b)]
                                  [(string=? tok "*") (* a b)]
                                  [(string=? tok "/") (quotient a b)])])
                  (cons res rest))
                (cons (string->number tok) st)))
          '()
          tokens)])
    (car stack)))
```

## Erlang

```erlang
-spec eval_rpn(Tokens :: [unicode:unicode_binary()]) -> integer().
eval_rpn(Tokens) ->
    eval_rpn(Tokens, []).

%% internal recursive evaluator
eval_rpn([], [Result]) -> Result;
eval_rpn([Token|Rest], Stack) ->
    case Token of
        <<"+">> -> apply_op(fun(A,B) -> A + B end, Rest, Stack);
        <<"-">> -> apply_op(fun(A,B) -> A - B end, Rest, Stack);
        <<"*">> -> apply_op(fun(A,B) -> A * B end, Rest, Stack);
        <<"/">> -> apply_op(fun(A,B) -> A div B end, Rest, Stack);
        _ ->
            Int = erlang:list_to_integer(binary_to_list(Token)),
            eval_rpn(Rest, [Int|Stack])
    end.

apply_op(Fun, Tokens, [B,A|Rest]) ->
    Result = Fun(A, B),
    eval_rpn(Tokens, [Result|Rest]).
```

## Elixir

```elixir
defmodule Solution do
  @spec eval_rpn(tokens :: [String.t]) :: integer
  def eval_rpn(tokens) do
    [result | _] =
      Enum.reduce(tokens, [], fn token, stack ->
        case token do
          "+" -> apply_op(stack, &Kernel.+/2)
          "-" -> apply_op(stack, &Kernel.-/2)
          "*" -> apply_op(stack, &Kernel.*/2)
          "/" -> apply_op(stack, fn a, b -> div(a, b) end)
          _   -> [String.to_integer(token) | stack]
        end
      end)

    result
  end

  defp apply_op([a, b | rest], op) do
    [op.(b, a) | rest]
  end
end
```
