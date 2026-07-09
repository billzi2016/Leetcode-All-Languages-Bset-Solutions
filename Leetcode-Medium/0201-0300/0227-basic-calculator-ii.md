# 0227. Basic Calculator II

## Cpp

```cpp
class Solution {
public:
    int calculate(string s) {
        long long cur = 0;
        long long lastNumber = 0;
        long long result = 0;
        char op = '+';
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            if (isdigit(c)) {
                cur = cur * 10 + (c - '0');
            }
            if ((!isdigit(c) && !isspace(c)) || i == n - 1) {
                if (op == '+') {
                    result += lastNumber;
                    lastNumber = cur;
                } else if (op == '-') {
                    result += lastNumber;
                    lastNumber = -cur;
                } else if (op == '*') {
                    lastNumber = lastNumber * cur;
                } else if (op == '/') {
                    lastNumber = lastNumber / cur; // truncates toward zero
                }
                op = c;
                cur = 0;
            }
        }
        result += lastNumber;
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int calculate(String s) {
        int n = s.length();
        int currentNumber = 0;
        char operation = '+';
        int lastNumber = 0;
        int result = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                currentNumber = currentNumber * 10 + (c - '0');
            }
            if ((!Character.isDigit(c) && c != ' ') || i == n - 1) {
                switch (operation) {
                    case '+':
                        result += lastNumber;
                        lastNumber = currentNumber;
                        break;
                    case '-':
                        result += lastNumber;
                        lastNumber = -currentNumber;
                        break;
                    case '*':
                        lastNumber = lastNumber * currentNumber;
                        break;
                    case '/':
                        lastNumber = lastNumber / currentNumber;
                        break;
                }
                operation = c;
                currentNumber = 0;
            }
        }
        result += lastNumber;
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
        num = 0
        last_num = 0
        result = 0
        op = '+'
        n = len(s)
        i = 0
        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and not ch.isspace()) or i == n - 1:
                if op == '+':
                    result += last_num
                    last_num = num
                elif op == '-':
                    result += last_num
                    last_num = -num
                elif op == '*':
                    last_num = last_num * num
                else:  # op == '/'
                    # Truncate toward zero
                    last_num = int(last_num / num)
                op = ch
                num = 0
            i += 1
        result += last_num
        return result
```

## Python3

```python
class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        last_num = 0
        result = 0
        op = '+'
        n = len(s)
        for i, ch in enumerate(s):
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            if (not ch.isspace() and not ch.isdigit()) or i == n - 1:
                if op == '+':
                    result += last_num
                    last_num = cur
                elif op == '-':
                    result += last_num
                    last_num = -cur
                elif op == '*':
                    last_num = last_num * cur
                else:  # op == '/'
                    last_num = int(last_num / cur)
                op = ch
                cur = 0
        return result + last_num
```

## C

```c
int calculate(char* s) {
    long long cur = 0;
    long long lastNumber = 0;
    long long result = 0;
    char op = '+';
    for (int i = 0; s[i] != '\0'; ++i) {
        char c = s[i];
        if (c == ' ') continue;
        if (c >= '0' && c <= '9') {
            cur = cur * 10 + (c - '0');
        } else { // operator
            switch (op) {
                case '+':
                    result += lastNumber;
                    lastNumber = cur;
                    break;
                case '-':
                    result += lastNumber;
                    lastNumber = -cur;
                    break;
                case '*':
                    lastNumber = lastNumber * cur;
                    break;
                case '/':
                    lastNumber = lastNumber / cur; // truncates toward zero in C
                    break;
            }
            op = c;
            cur = 0;
        }
    }
    // process the final number
    switch (op) {
        case '+':
            result += lastNumber;
            lastNumber = cur;
            break;
        case '-':
            result += lastNumber;
            lastNumber = -cur;
            break;
        case '*':
            lastNumber = lastNumber * cur;
            break;
        case '/':
            lastNumber = lastNumber / cur;
            break;
    }
    result += lastNumber;
    return (int)result;
}
```

## Csharp

```csharp
public class Solution
{
    public int Calculate(string s)
    {
        int n = s.Length;
        int currentNumber = 0;
        char operation = '+';
        int lastNumber = 0;
        int result = 0;

        for (int i = 0; i < n; i++)
        {
            char c = s[i];
            if (c >= '0' && c <= '9')
            {
                currentNumber = currentNumber * 10 + (c - '0');
            }

            if ((c < '0' || c > '9') && c != ' ' || i == n - 1)
            {
                switch (operation)
                {
                    case '+':
                        result += lastNumber;
                        lastNumber = currentNumber;
                        break;
                    case '-':
                        result += lastNumber;
                        lastNumber = -currentNumber;
                        break;
                    case '*':
                        lastNumber = lastNumber * currentNumber;
                        break;
                    case '/':
                        lastNumber = lastNumber / currentNumber;
                        break;
                }

                operation = c;
                currentNumber = 0;
            }
        }

        result += lastNumber;
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
    let n = s.length;
    let currentNumber = 0;
    let lastNumber = 0;
    let result = 0;
    let operation = '+';
    
    for (let i = 0; i < n; i++) {
        const c = s[i];
        if (c >= '0' && c <= '9') {
            currentNumber = currentNumber * 10 + (c.charCodeAt(0) - 48);
        }
        if ((c !== ' ' && (c < '0' || c > '9')) || i === n - 1) {
            if (operation === '+') {
                result += lastNumber;
                lastNumber = currentNumber;
            } else if (operation === '-') {
                result += lastNumber;
                lastNumber = -currentNumber;
            } else if (operation === '*') {
                lastNumber = lastNumber * currentNumber;
            } else if (operation === '/') {
                lastNumber = Math.trunc(lastNumber / currentNumber);
            }
            operation = c;
            currentNumber = 0;
        }
    }
    
    result += lastNumber;
    return result;
};
```

## Typescript

```typescript
function calculate(s: string): number {
    let currentNumber = 0;
    let lastNumber = 0;
    let result = 0;
    let operation = '+';
    const n = s.length;

    for (let i = 0; i < n; i++) {
        const c = s[i];
        if (c === ' ') continue;

        if (c >= '0' && c <= '9') {
            currentNumber = currentNumber * 10 + (c.charCodeAt(0) - 48);
        }

        if ((c < '0' || c > '9') && c !== ' ' || i === n - 1) {
            if (operation === '+') {
                result += lastNumber;
                lastNumber = currentNumber;
            } else if (operation === '-') {
                result += lastNumber;
                lastNumber = -currentNumber;
            } else if (operation === '*') {
                lastNumber = lastNumber * currentNumber;
            } else if (operation === '/') {
                lastNumber = Math.trunc(lastNumber / currentNumber);
            }
            operation = c;
            currentNumber = 0;
        }
    }

    result += lastNumber;
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
        $s = trim($s);
        $len = strlen($s);
        $num = 0;
        $lastNumber = 0;
        $result = 0;
        $operation = '+';
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (ctype_digit($c)) {
                $num = $num * 10 + intval($c);
            }
            if ((!ctype_digit($c) && $c !== ' ') || $i === $len - 1) {
                switch ($operation) {
                    case '+':
                        $result += $lastNumber;
                        $lastNumber = $num;
                        break;
                    case '-':
                        $result += $lastNumber;
                        $lastNumber = -$num;
                        break;
                    case '*':
                        $lastNumber = $lastNumber * $num;
                        break;
                    case '/':
                        $lastNumber = intdiv($lastNumber, $num);
                        break;
                }
                $operation = $c;
                $num = 0;
            }
        }
        $result += $lastNumber;
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func calculate(_ s: String) -> Int {
        let chars = Array(s)
        var num = 0
        var lastNum = 0
        var result = 0
        var op: Character = "+"
        
        for i in 0..<chars.count {
            let c = chars[i]
            if c.isNumber, let digit = c.wholeNumberValue {
                num = num * 10 + digit
            }
            
            if (!c.isNumber && c != " ") || i == chars.count - 1 {
                switch op {
                case "+":
                    result += lastNum
                    lastNum = num
                case "-":
                    result += lastNum
                    lastNum = -num
                case "*":
                    lastNum = lastNum * num
                case "/":
                    // Swift integer division truncates toward zero
                    lastNum = lastNum / num
                default:
                    break
                }
                op = c
                num = 0
            }
        }
        result += lastNum
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calculate(s: String): Int {
        var num = 0
        var lastNum = 0
        var result = 0
        var op = '+'
        val n = s.length
        for (i in 0 until n) {
            val c = s[i]
            if (c.isDigit()) {
                num = num * 10 + (c - '0')
            }
            if (!c.isWhitespace() && !c.isDigit()) {
                when (op) {
                    '+' -> {
                        result += lastNum
                        lastNum = num
                    }
                    '-' -> {
                        result += lastNum
                        lastNum = -num
                    }
                    '*' -> {
                        lastNum = lastNum * num
                    }
                    '/' -> {
                        lastNum = lastNum / num
                    }
                }
                op = c
                num = 0
            } else if (i == n - 1) {
                when (op) {
                    '+' -> {
                        result += lastNum
                        lastNum = num
                    }
                    '-' -> {
                        result += lastNum
                        lastNum = -num
                    }
                    '*' -> {
                        lastNum = lastNum * num
                    }
                    '/' -> {
                        lastNum = lastNum / num
                    }
                }
            }
        }
        return result + lastNum
    }
}
```

## Dart

```dart
class Solution {
  int calculate(String s) {
    int n = s.length;
    int currentNumber = 0;
    int lastNumber = 0;
    int result = 0;
    String operation = '+';
    for (int i = 0; i < n; i++) {
      String ch = s[i];
      if (ch == ' ') continue;
      int code = ch.codeUnitAt(0);
      bool isDigit = code >= 48 && code <= 57;
      if (isDigit) {
        currentNumber = currentNumber * 10 + (code - 48);
      }
      if (!isDigit || i == n - 1) {
        switch (operation) {
          case '+':
            result += lastNumber;
            lastNumber = currentNumber;
            break;
          case '-':
            result += lastNumber;
            lastNumber = -currentNumber;
            break;
          case '*':
            lastNumber = lastNumber * currentNumber;
            break;
          case '/':
            // Dart's integer division truncates toward zero.
            if (lastNumber < 0) {
              lastNumber = -((-lastNumber) ~/ currentNumber);
            } else {
              lastNumber = lastNumber ~/ currentNumber;
            }
            break;
        }
        operation = ch;
        currentNumber = 0;
      }
    }
    result += lastNumber;
    return result;
  }
}
```

## Golang

```go
func calculate(s string) int {
    var cur, lastNum, result int
    op := byte('+')
    n := len(s)
    for i := 0; i < n; i++ {
        c := s[i]
        if c == ' ' {
            continue
        }
        if c >= '0' && c <= '9' {
            cur = cur*10 + int(c-'0')
        }
        if (c < '0' || c > '9') && c != ' ' || i == n-1 {
            switch op {
            case '+':
                result += lastNum
                lastNum = cur
            case '-':
                result += lastNum
                lastNum = -cur
            case '*':
                lastNum = lastNum * cur
            case '/':
                lastNum = lastNum / cur
            }
            op = c
            cur = 0
        }
    }
    return result + lastNum
}
```

## Ruby

```ruby
def calculate(s)
  num = 0
  last_num = 0
  result = 0
  op = '+'
  n = s.length
  i = 0
  while i < n
    ch = s[i]
    if ch >= '0' && ch <= '9'
      num = num * 10 + (ch.ord - 48)
    end
    if (ch != ' ' && !(ch >= '0' && ch <= '9')) || i == n - 1
      case op
      when '+'
        result += last_num
        last_num = num
      when '-'
        result += last_num
        last_num = -num
      when '*'
        last_num = last_num * num
      when '/'
        last_num = (last_num.fdiv(num)).to_i
      end
      op = ch
      num = 0
    end
    i += 1
  end
  result + last_num
end
```

## Scala

```scala
object Solution {
  def calculate(s: String): Int = {
    var num = 0
    var lastNumber = 0
    var result = 0
    var op: Char = '+'
    val n = s.length
    for (i <- 0 until n) {
      val ch = s.charAt(i)
      if (ch >= '0' && ch <= '9') {
        num = num * 10 + (ch - '0')
      }
      if (((ch < '0' || ch > '9') && ch != ' ') || i == n - 1) {
        op match {
          case '+' =>
            result += lastNumber
            lastNumber = num
          case '-' =>
            result += lastNumber
            lastNumber = -num
          case '*' =>
            lastNumber = lastNumber * num
          case '/' =>
            lastNumber = lastNumber / num // truncates toward zero
        }
        op = ch
        num = 0
      }
    }
    result + lastNumber
  }
}
```

## Rust

```rust
impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut num: i32 = 0;
        let mut last_num: i32 = 0;
        let mut result: i32 = 0;
        let mut op: char = '+';
        for ch in s.chars() {
            if ch.is_ascii_digit() {
                num = num * 10 + (ch as i32 - '0' as i32);
            } else if ch == ' ' {
                continue;
            } else {
                match op {
                    '+' => {
                        result += last_num;
                        last_num = num;
                    }
                    '-' => {
                        result += last_num;
                        last_num = -num;
                    }
                    '*' => {
                        last_num = last_num * num;
                    }
                    '/' => {
                        last_num = last_num / num; // truncates toward zero
                    }
                    _ => {}
                }
                op = ch;
                num = 0;
            }
        }
        // process the final number
        match op {
            '+' => {
                result += last_num;
                last_num = num;
            }
            '-' => {
                result += last_num;
                last_num = -num;
            }
            '*' => {
                last_num = last_num * num;
            }
            '/' => {
                last_num = last_num / num;
            }
            _ => {}
        }
        result + last_num
    }
}
```

## Racket

```racket
(define/contract (calculate s)
  (-> string? exact-integer?)
  (define (process op result last-number cur)
    (cond [(eq? op #\+) (values (+ result last-number) cur)]
          [(eq? op #\-) (values (+ result last-number) (- cur))]
          [(eq? op #\*) (values result (* last-number cur))]
          [(eq? op #\/) (values result (quotient last-number cur))]))
  (let loop ((i 0)
             (result 0)
             (last-number 0)
             (current-number 0)
             (op #\+))
    (if (= i (string-length s))
        (let-values ([(res ln) (process op result last-number current-number)])
          (+ res ln))
        (let ((c (string-ref s i)))
          (cond [(char-whitespace? c)
                 (loop (+ i 1) result last-number current-number op)]
                [(char-numeric? c)
                 (let ((digit (- (char->integer c) (char->integer #\0))))
                   (loop (+ i 1) result last-number
                         (+ (* current-number 10) digit) op))]
                [else ; operator '+', '-', '*', '/'
                 (let-values ([(new-result new-last)
                               (process op result last-number current-number)])
                   (loop (+ i 1) new-result new-last 0 c))))))))
```

## Erlang

```erlang
-spec calculate(S :: unicode:unicode_binary()) -> integer().
calculate(S) ->
    Bin = <<S/binary, $+>>,
    {Res, Last} = process(Bin, 0, 0, $+, 0),
    Res + Last.

process(<<>>, _Cur, LastNum, _Op, Result) ->
    {Result, LastNum};
process(<<Char, Rest/binary>>, Cur, LastNum, Op, Result) when Char >= $0, Char =< $9 ->
    Digit = Char - $0,
    process(Rest, Cur * 10 + Digit, LastNum, Op, Result);
process(<<Char, Rest/binary>>, Cur, LastNum, Op, Result) 
        when Char == $\s; Char == $\t; Char == $\r; Char == $\n ->
    process(Rest, Cur, LastNum, Op, Result);
process(<<OpChar, Rest/binary>>, Cur, LastNum, PrevOp, Result) ->
    {NewResult, NewLast} = case PrevOp of
        $+ -> {Result + LastNum, Cur};
        $- -> {Result + LastNum, -Cur};
        $* -> {Result, LastNum * Cur};
        $/ -> {Result, trunc_div(LastNum, Cur)}
    end,
    process(Rest, 0, NewLast, OpChar, NewResult).

trunc_div(A, B) ->
    A div B.
```

## Elixir

```elixir
defmodule Solution do
  @spec calculate(s :: String.t()) :: integer
  def calculate(s) do
    chars = String.to_charlist(s) ++ [?+]

    {result, last_num, _num, _op} =
      Enum.reduce(chars, {0, 0, 0, ?+}, fn c, {res, last, cur, prev_op} ->
        cond do
          c == ?\s ->
            {res, last, cur, prev_op}

          c >= ?0 and c <= ?9 ->
            digit = c - ?0
            {res, last, cur * 10 + digit, prev_op}

          true ->
            {new_res, new_last} =
              case prev_op do
                ?+ -> {res + last, cur}
                ?- -> {res + last, -cur}
                ?* -> {res, last * cur}
                ?/ -> {res, trunc(last / cur)}
              end

            {new_res, new_last, 0, c}
        end
      end)

    result + last_num
  end
end
```
