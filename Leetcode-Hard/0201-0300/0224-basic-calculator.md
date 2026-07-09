# 0224. Basic Calculator

## Cpp

```cpp
class Solution {
public:
    int calculate(string s) {
        long result = 0;
        long num = 0;
        int sign = 1;
        stack<long> resStack;
        stack<int> signStack;
        for (char c : s) {
            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            } else {
                result += sign * num;
                num = 0;
                if (c == '+') {
                    sign = 1;
                } else if (c == '-') {
                    sign = -1;
                } else if (c == '(') {
                    resStack.push(result);
                    signStack.push(sign);
                    result = 0;
                    sign = 1;
                } else if (c == ')') {
                    int prevSign = signStack.top(); signStack.pop();
                    long prevResult = resStack.top(); resStack.pop();
                    result = prevResult + prevSign * result;
                }
                // spaces are ignored
            }
        }
        result += sign * num;
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int calculate(String s) {
        int n = s.length();
        int result = 0;
        int sign = 1; // current sign
        int num = 0;
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                num = num * 10 + (c - '0');
            } else if (c == '+') {
                result += sign * num;
                num = 0;
                sign = 1;
            } else if (c == '-') {
                result += sign * num;
                num = 0;
                sign = -1;
            } else if (c == '(') {
                // push current result and sign
                stack.push(result);
                stack.push(sign);
                // reset for new sub-expression
                result = 0;
                sign = 1;
            } else if (c == ')') {
                result += sign * num;
                num = 0;
                int prevSign = stack.pop();
                int prevResult = stack.pop();
                result = prevResult + prevSign * result;
                // sign will be set by next operator
            }
            // ignore spaces and other chars
        }
        result += sign * num; // add any remaining number
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        sign = 1
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
                continue
            elif ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch == '(':
                # push current result and sign onto stack
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + prev_sign * res
            i += 1
        return res
```

## Python3

```python
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        sign = 1
        num = 0
        stack = []
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                total += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                total += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                # push current state
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
            elif ch == ')':
                total += sign * num
                num = 0
                prev_sign = stack.pop()
                prev_total = stack.pop()
                total = prev_total + prev_sign * total
                sign = 1
            # ignore spaces and other chars
            i += 1
        total += sign * num
        return total
```

## C

```c
#include <stdlib.h>
#include <string.h>

int calculate(char* s) {
    int n = strlen(s);
    int *stackRes = (int *)malloc(sizeof(int) * (n + 2));
    int *stackSign = (int *)malloc(sizeof(int) * (n + 2));
    int top = 0;
    int result = 0;
    int sign = 1;

    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (c >= '0' && c <= '9') {
            int num = 0;
            while (i < n && s[i] >= '0' && s[i] <= '9') {
                num = num * 10 + (s[i] - '0');
                ++i;
            }
            result += sign * num;
            --i; // adjust for the outer loop's increment
        } else if (c == '+') {
            sign = 1;
        } else if (c == '-') {
            sign = -1;
        } else if (c == '(') {
            stackRes[top] = result;
            stackSign[top] = sign;
            ++top;
            result = 0;
            sign = 1;
        } else if (c == ')') {
            int prevSign = stackSign[top - 1];
            int prevResult = stackRes[top - 1];
            --top;
            result = prevResult + prevSign * result;
        }
        // ignore spaces and any other characters
    }

    free(stackRes);
    free(stackSign);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int Calculate(string s) {
        int n = s.Length;
        int result = 0;
        int sign = 1; // current sign
        Stack<int> stack = new Stack<int>();
        
        for (int i = 0; i < n; i++) {
            char c = s[i];
            if (c >= '0' && c <= '9') {
                int num = 0;
                while (i < n && s[i] >= '0' && s[i] <= '9') {
                    num = num * 10 + (s[i] - '0');
                    i++;
                }
                result += sign * num;
                i--; // step back because for-loop will increment
            } else if (c == '+') {
                sign = 1;
            } else if (c == '-') {
                sign = -1;
            } else if (c == '(') {
                // push current result and sign onto stack
                stack.Push(result);
                stack.Push(sign);
                // reset for new subexpression
                result = 0;
                sign = 1;
            } else if (c == ')') {
                int prevSign = stack.Pop();   // sign before '('
                int prevResult = stack.Pop(); // result calculated before '('
                result = prevResult + prevSign * result;
            }
            // ignore spaces and other characters
        }
        
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    const stack = [];
    let result = 0;
    let sign = 1; // current sign: +1 or -1
    const n = s.length;
    
    for (let i = 0; i < n; i++) {
        const ch = s[i];
        if (ch >= '0' && ch <= '9') {
            let num = 0;
            while (i < n && s[i] >= '0' && s[i] <= '9') {
                num = num * 10 + (s.charCodeAt(i) - 48);
                i++;
            }
            result += sign * num;
            i--; // adjust for the outer loop's increment
        } else if (ch === '+') {
            sign = 1;
        } else if (ch === '-') {
            sign = -1;
        } else if (ch === '(') {
            // Push current state onto stack
            stack.push(result);
            stack.push(sign);
            // Reset for new sub-expression
            result = 0;
            sign = 1;
        } else if (ch === ')') {
            const prevSign = stack.pop();   // sign before '('
            const prevResult = stack.pop(); // result before '('
            result = prevResult + prevSign * result;
        }
        // ignore spaces and any other characters
    }
    
    return result;
};
```

## Typescript

```typescript
function calculate(s: string): number {
    const n = s.length;
    let result = 0;
    let sign = 1;
    const stack: number[] = [];
    let i = 0;

    while (i < n) {
        const ch = s[i];
        if (ch >= '0' && ch <= '9') {
            let num = 0;
            while (i < n && s[i] >= '0' && s[i] <= '9') {
                num = num * 10 + (s.charCodeAt(i) - 48);
                i++;
            }
            result += sign * num;
            continue; // already moved i to next non-digit character
        } else if (ch === '+') {
            sign = 1;
        } else if (ch === '-') {
            sign = -1;
        } else if (ch === '(') {
            // push current state onto stack
            stack.push(result);
            stack.push(sign);
            // reset for new sub-expression
            result = 0;
            sign = 1;
        } else if (ch === ')') {
            const prevSign = stack.pop()!;
            const prevResult = stack.pop()!;
            result = prevResult + prevSign * result;
        }
        // ignore spaces and any other characters
        i++;
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function calculate($s) {
        $len = strlen($s);
        $stack = [];
        $result = 0;
        $sign = 1;
        $num = 0;

        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (ctype_digit($c)) {
                $num = $num * 10 + intval($c);
            } elseif ($c === '+') {
                $result += $sign * $num;
                $num = 0;
                $sign = 1;
            } elseif ($c === '-') {
                $result += $sign * $num;
                $num = 0;
                $sign = -1;
            } elseif ($c === '(') {
                // push current result and sign onto stack
                array_push($stack, $result);
                array_push($stack, $sign);
                // reset for new sub-expression
                $result = 0;
                $sign = 1;
            } elseif ($c === ')') {
                $result += $sign * $num;
                $num = 0;
                // pop sign and previous result
                $prevSign = array_pop($stack);
                $prevResult = array_pop($stack);
                $result = $prevResult + $prevSign * $result;
            } else {
                // ignore spaces
            }
        }

        $result += $sign * $num;
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func calculate(_ s: String) -> Int {
        var stack = [Int]()
        var result = 0
        var number = 0
        var sign = 1
        
        for ch in s {
            if ch.isNumber {
                number = number * 10 + (ch.wholeNumberValue ?? 0)
            } else if ch == "+" {
                result += sign * number
                number = 0
                sign = 1
            } else if ch == "-" {
                result += sign * number
                number = 0
                sign = -1
            } else if ch == "(" {
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            } else if ch == ")" {
                result += sign * number
                number = 0
                let prevSign = stack.removeLast()
                let prevResult = stack.removeLast()
                result = prevResult + prevSign * result
            }
        }
        result += sign * number
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calculate(s: String): Int {
        var result = 0
        var sign = 1
        val stack = java.util.ArrayDeque<Int>()
        var i = 0
        while (i < s.length) {
            when (val c = s[i]) {
                ' ' -> {}
                '+' -> sign = 1
                '-' -> sign = -1
                '(' -> {
                    stack.push(result)
                    stack.push(sign)
                    result = 0
                    sign = 1
                }
                ')' -> {
                    val prevSign = stack.pop()
                    val prevResult = stack.pop()
                    result = prevResult + prevSign * result
                }
                else -> { // digit
                    var num = 0
                    var j = i
                    while (j < s.length && s[j].isDigit()) {
                        num = num * 10 + (s[j] - '0')
                        j++
                    }
                    result += sign * num
                    i = j - 1
                }
            }
            i++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int calculate(String s) {
    int n = s.length;
    List<int> stack = [1];
    int sign = 1;
    int result = 0;
    int i = 0;

    while (i < n) {
      String ch = s[i];
      if (ch == ' ') {
        i++;
        continue;
      }
      int code = ch.codeUnitAt(0);
      if (code >= 48 && code <= 57) { // digit
        int num = 0;
        while (i < n) {
          int c = s[i].codeUnitAt(0);
          if (c < 48 || c > 57) break;
          num = num * 10 + (c - 48);
          i++;
        }
        result += sign * num;
      } else if (ch == '+') {
        sign = stack.last;
        i++;
      } else if (ch == '-') {
        sign = -stack.last;
        i++;
      } else if (ch == '(') {
        stack.add(sign);
        i++;
      } else if (ch == ')') {
        stack.removeLast();
        i++;
      } else {
        i++; // safety, should not occur
      }
    }

    return result;
  }
}
```

## Golang

```go
func calculate(s string) int {
	stack := []int{}
	result, sign := 0, 1
	n := len(s)
	for i := 0; i < n; i++ {
		c := s[i]
		switch {
		case c >= '0' && c <= '9':
			num := 0
			for i < n && s[i] >= '0' && s[i] <= '9' {
				num = num*10 + int(s[i]-'0')
				i++
			}
			result += sign * num
			i-- // adjust for outer loop increment
		case c == '+':
			sign = 1
		case c == '-':
			sign = -1
		case c == '(':
			stack = append(stack, result)
			stack = append(stack, sign)
			result, sign = 0, 1
		case c == ')':
			m := len(stack)
			prevSign := stack[m-1]
			prevResult := stack[m-2]
			result = prevResult + prevSign*result
			stack = stack[:m-2]
		}
	}
	return result
}
```

## Ruby

```ruby
def calculate(s)
  stack = []
  result = 0
  sign = 1
  i = 0
  n = s.length
  while i < n
    ch = s[i]
    if ch >= '0' && ch <= '9'
      num = 0
      while i < n && (c = s[i]) >= '0' && c <= '9'
        num = num * 10 + (s[i].ord - 48)
        i += 1
      end
      result += sign * num
      next
    elsif ch == '+'
      sign = 1
    elsif ch == '-'
      sign = -1
    elsif ch == '('
      stack << result
      stack << sign
      result = 0
      sign = 1
    elsif ch == ')'
      prev_sign = stack.pop
      prev_result = stack.pop
      result = prev_result + prev_sign * result
    end
    i += 1
  end
  result
end
```

## Scala

```scala
object Solution {
    def calculate(s: String): Int = {
        val n = s.length
        var i = 0
        var result = 0
        var sign = 1
        val stack = new scala.collection.mutable.Stack[Int]()

        while (i < n) {
            val ch = s.charAt(i)
            if (ch >= '0' && ch <= '9') {
                var num = 0
                while (i < n && s.charAt(i).isDigit) {
                    num = num * 10 + (s.charAt(i) - '0')
                    i += 1
                }
                result += sign * num
            } else if (ch == '+') {
                sign = 1
                i += 1
            } else if (ch == '-') {
                sign = -1
                i += 1
            } else if (ch == '(') {
                stack.push(result)
                stack.push(sign)
                result = 0
                sign = 1
                i += 1
            } else if (ch == ')') {
                val prevSign = stack.pop()
                val prevResult = stack.pop()
                result = prevResult + prevSign * result
                i += 1
            } else { // space or other ignored characters
                i += 1
            }
        }

        result
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let mut result: i32 = 0;
        let mut sign: i32 = 1;
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut i = 0usize;

        while i < n {
            match bytes[i] as char {
                '0'..='9' => {
                    let mut num: i32 = 0;
                    while i < n && (bytes[i] as char).is_ascii_digit() {
                        num = num * 10 + (bytes[i] - b'0') as i32;
                        i += 1;
                    }
                    result += sign * num;
                    continue;
                }
                '+' => sign = 1,
                '-' => sign = -1,
                '(' => {
                    stack.push(result);
                    stack.push(sign);
                    result = 0;
                    sign = 1;
                }
                ')' => {
                    if let Some(prev_sign) = stack.pop() {
                        if let Some(prev_result) = stack.pop() {
                            result = prev_result + prev_sign * result;
                        }
                    }
                }
                _ => {} // ignore spaces
            }
            i += 1;
        }

        result
    }
}
```

## Racket

```racket
#lang racket

(define/contract (calculate s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         (stack '())
         (sign 1)
         (num 0)
         (result 0))
    (let loop ((i 0) (sign sign) (num num) (result result) (stack stack))
      (if (= i len)
          (+ result (* sign num))
          (let ((ch (string-ref s i)))
            (cond
              [(char-numeric? ch)
               (define digit (- (char->integer ch) (char->integer #\0)))
               (loop (+ i 1) sign (+ (* num 10) digit) result stack)]
              [(char-whitespace? ch)
               (loop (+ i 1) sign num result stack)]
              [(char=? ch #\+)
               (loop (+ i 1) 1 0 (+ result (* sign num)) stack)]
              [(char=? ch #\-)
               (loop (+ i 1) -1 0 (+ result (* sign num)) stack)]
              [(char=? ch #\()
               (loop (+ i 1) 1 0 0 (cons (list result sign) stack))]
              [(char=? ch #\))
               (let* ((temp (+ result (* sign num)))
                      (prev (car stack))
                      (prev-result (first prev))
                      (prev-sign (second prev))
                      (new-result (+ prev-result (* prev-sign temp))))
                 (loop (+ i 1) 1 0 new-result (cdr stack)))]
              [else
               (error "invalid character")]))))))
```

## Erlang

```erlang
-module(solution).
-export([calculate/1]).

-spec calculate(S :: unicode:unicode_binary()) -> integer().
calculate(S) ->
    CharList = unicode:characters_to_list(S),
    {Result, _} = parse_expr(CharList),
    Result.

%% internal helpers

skip_spaces([]) -> [];
skip_spaces([C|Rest]) when C == $\s; C == $\t; C == $\n; C == $\r ->
    skip_spaces(Rest);
skip_spaces(L) -> L.

parse_number(Chars) -> parse_number(Chars, 0).

parse_number([], Acc) -> {Acc, []};
parse_number([C|Rest], Acc) when C >= $0, C =< $9 ->
    NewAcc = Acc * 10 + (C - $0),
    parse_number(Rest, NewAcc);
parse_number(L, Acc) -> {Acc, L}.

parse_factor(Chars) ->
    Rest = skip_spaces(Chars),
    case Rest of
        [$- | Tail] ->
            {Val, Rest2} = parse_factor(Tail),
            {-Val, Rest2};
        [$+ | Tail] ->
            parse_factor(Tail);
        [$( | Tail] ->
            {InnerVal, AfterInner} = parse_expr(Tail),
            AfterSpaces = skip_spaces(AfterInner),
            case AfterSpaces of
                [$) | RestAfterParen] -> {InnerVal, RestAfterParen};
                _ -> erlang:error(bad_expression)
            end;
        [C|Tail] when C >= $0, C =< $9 ->
            parse_number(Rest);
        [] -> {0, []}
    end.

parse_expr(Chars) ->
    {Term, Rest} = parse_factor(Chars),
    parse_expr_rest(Term, Rest).

parse_expr_rest(Acc, Chars) ->
    Rest = skip_spaces(Chars),
    case Rest of
        [$+ | Tail] ->
            {Val, Rest2} = parse_factor(Tail),
            parse_expr_rest(Acc + Val, Rest2);
        [$- | Tail] ->
            {Val, Rest2} = parse_factor(Tail),
            parse_expr_rest(Acc - Val, Rest2);
        _ -> {Acc, Rest}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec calculate(s :: String.t()) :: integer
  def calculate(s) do
    chars = String.to_charlist(s)
    {result, _, _, _} = eval(chars, 0, 1, 0, [])
    result
  end

  defp eval([], result, sign, num, stack) do
    {result + sign * num, sign, num, stack}
  end

  # digit
  defp eval([c | rest], result, sign, num, stack) when c in ?0..?9 do
    digit = c - ?0
    eval(rest, result, sign, num * 10 + digit, stack)
  end

  # plus
  defp eval([?+ | rest], result, _sign, num, stack) do
    new_result = result + _sign * num
    eval(rest, new_result, 1, 0, stack)
  end

  # minus
  defp eval([?- | rest], result, _sign, num, stack) do
    new_result = result + _sign * num
    eval(rest, new_result, -1, 0, stack)
  end

  # open parenthesis
  defp eval([?( | rest], result, sign, _num, stack) do
    eval(rest, 0, 1, 0, [{result, sign} | stack])
  end

  # close parenthesis
  defp eval([?) | rest], result, sign, num, [{prev_res, prev_sign} | stack]) do
    inner = result + sign * num
    new_result = prev_res + prev_sign * inner
    eval(rest, new_result, 1, 0, stack)
  end

  # whitespace
  defp eval([c | rest], result, sign, num, stack) when c in [? , ?\t, ?\r, ?\n] do
    eval(rest, result, sign, num, stack)
  end

  # any other character (should not occur)
  defp eval([_ | rest], result, sign, num, stack) do
    eval(rest, result, sign, num, stack)
  end
end
```
