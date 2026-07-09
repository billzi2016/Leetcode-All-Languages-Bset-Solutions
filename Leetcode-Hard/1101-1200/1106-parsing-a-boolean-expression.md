# 1106. Parsing A Boolean Expression

## Cpp

```cpp
class Solution {
public:
    bool parseBoolExpr(const std::string& expression) {
        int idx = 0;
        return evaluate(expression, idx);
    }
private:
    bool evaluate(const std::string& s, int& i) {
        char c = s[i];
        if (c == 't') { ++i; return true; }
        if (c == 'f') { ++i; return false; }
        // operator
        char op = c;
        i += 2; // skip operator and '('
        if (op == '!') {
            bool val = evaluate(s, i);
            ++i; // skip ')'
            return !val;
        } else if (op == '&') {
            bool res = true;
            while (true) {
                bool val = evaluate(s, i);
                res = res && val;
                if (s[i] == ',') { ++i; continue; }
                break; // ')'
            }
            ++i; // skip ')'
            return res;
        } else { // op == '|'
            bool res = false;
            while (true) {
                bool val = evaluate(s, i);
                res = res || val;
                if (s[i] == ',') { ++i; continue; }
                break; // ')'
            }
            ++i; // skip ')'
            return res;
        }
    }
};
```

## Java

```java
class Solution {
    private int idx;

    public boolean parseBoolExpr(String expression) {
        idx = 0;
        return evaluate(expression);
    }

    private boolean evaluate(String s) {
        char ch = s.charAt(idx++);
        if (ch == 't') return true;
        if (ch == 'f') return false;

        if (ch == '!') {
            // skip '('
            idx++;
            boolean val = evaluate(s);
            // skip ')'
            idx++;
            return !val;
        }

        // '&' or '|'
        boolean isAnd = ch == '&';
        // skip '('
        idx++;

        boolean result = isAnd; // true for AND, false for OR
        while (true) {
            char cur = s.charAt(idx);
            if (cur == ')') {
                idx++; // consume ')'
                break;
            }
            boolean val = evaluate(s);
            if (isAnd) {
                result &= val;
            } else {
                result |= val;
            }
            // skip ',' if present
            if (s.charAt(idx) == ',') idx++;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        self.s = expression
        idx = [0]
        return self._parse(idx)

    def _parse(self, idx):
        s = self.s
        i = idx[0]
        ch = s[i]

        # literals
        if ch == 't':
            idx[0] += 1
            return True
        if ch == 'f':
            idx[0] += 1
            return False

        # operator
        op = ch
        idx[0] += 2          # skip operator and '('

        if op == '!':        # NOT has exactly one operand
            val = not self._parse(idx)
            idx[0] += 1      # skip ')'
            return val

        if op == '&':        # AND
            result = True
            while True:
                sub = self._parse(idx)
                result = result and sub
                if s[idx[0]] == ',':
                    idx[0] += 1
                    continue
                break          # reached ')'
            idx[0] += 1      # skip ')'
            return result

        # op == '|'   OR
        result = False
        while True:
            sub = self._parse(idx)
            result = result or sub
            if s[idx[0]] == ',':
                idx[0] += 1
                continue
            break              # reached ')'
        idx[0] += 1          # skip ')'
        return result
```

## Python3

```python
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for ch in expression:
            if ch == ',' or ch == '(':
                continue
            if ch == ')':
                vals = []
                while stack and stack[-1] not in '!&|':
                    vals.append(stack.pop())
                op = stack.pop()
                if op == '!':
                    res = 't' if vals[0] == 'f' else 'f'
                elif op == '&':
                    res = 'f' if 'f' in vals else 't'
                else:  # '|'
                    res = 't' if 't' in vals else 'f'
                stack.append(res)
            else:
                stack.append(ch)
        return stack[-1] == 't'
```

## C

```c
#include <stdbool.h>

static bool parseExpr(const char *s, int *pos) {
    char c = s[(*pos)++];
    if (c == 't') return true;
    if (c == 'f') return false;

    if (c == '!') {
        (*pos)++;                     // skip '('
        bool val = !parseExpr(s, pos);
        (*pos)++;                     // skip ')'
        return val;
    }

    if (c == '&' || c == '|') {
        char op = c;
        (*pos)++;                     // skip '('
        bool result = (op == '&');    // true for AND, false for OR

        while (1) {
            bool v = parseExpr(s, pos);
            if (op == '&')
                result = result && v;
            else
                result = result || v;

            char next = s[*pos];
            if (next == ',') {
                (*pos)++;             // skip comma
                continue;
            }
            if (next == ')') {
                (*pos)++;             // skip closing parenthesis
                break;
            }
        }
        return result;
    }

    return false; // unreachable for valid input
}

bool parseBoolExpr(char* expression) {
    int pos = 0;
    return parseExpr(expression, &pos);
}
```

## Csharp

```csharp
public class Solution
{
    private string expr;
    private int pos;

    public bool ParseBoolExpr(string expression)
    {
        expr = expression;
        pos = 0;
        return Eval();
    }

    private bool Eval()
    {
        char ch = expr[pos++];
        if (ch == 't') return true;
        if (ch == 'f') return false;

        // Operator handling
        if (ch == '!')
        {
            // skip '('
            pos++; 
            bool val = Eval();
            // skip ')'
            pos++;
            return !val;
        }
        else if (ch == '&' || ch == '|')
        {
            // skip '('
            pos++;

            bool result;
            if (ch == '&')
            {
                result = true; // AND starts as true
                while (true)
                {
                    bool v = Eval();
                    if (!v) result = false;

                    char next = expr[pos];
                    if (next == ',')
                    {
                        pos++; // skip comma
                        continue;
                    }
                    else // ')'
                    {
                        pos++; // skip closing parenthesis
                        break;
                    }
                }
            }
            else // '|'
            {
                result = false; // OR starts as false
                while (true)
                {
                    bool v = Eval();
                    if (v) result = true;

                    char next = expr[pos];
                    if (next == ',')
                    {
                        pos++; // skip comma
                        continue;
                    }
                    else // ')'
                    {
                        pos++; // skip closing parenthesis
                        break;
                    }
                }
            }

            return result;
        }

        // Should never reach here for valid input
        return false;
    }
}
```

## Javascript

```javascript
var parseBoolExpr = function(expression) {
    let idx = 0;
    const n = expression.length;
    
    function parse() {
        const ch = expression[idx++];
        if (ch === 't') return true;
        if (ch === 'f') return false;
        
        // operator: &, |, or !
        const op = ch;          // current operator
        idx++;                  // skip '('
        
        if (op === '!') {
            const val = parse(); // only one subexpression
            idx++;               // skip ')'
            return !val;
        }
        
        if (op === '&') {
            let res = true;
            while (true) {
                const v = parse();
                res = res && v;
                const nxt = expression[idx];
                if (nxt === ',') {
                    idx++; // skip comma
                } else { // ')'
                    idx++; // skip closing parenthesis
                    break;
                }
            }
            return res;
        } else { // op === '|'
            let res = false;
            while (true) {
                const v = parse();
                res = res || v;
                const nxt = expression[idx];
                if (nxt === ',') {
                    idx++; // skip comma
                } else { // ')'
                    idx++; // skip closing parenthesis
                    break;
                }
            }
            return res;
        }
    }
    
    return parse();
};
```

## Typescript

```typescript
function parseBoolExpr(expression: string): boolean {
    let idx = 0;
    const n = expression.length;

    function evalExpr(): boolean {
        const ch = expression[idx++];
        if (ch === 't') return true;
        if (ch === 'f') return false;

        // NOT operation
        if (ch === '!') {
            // skip '('
            idx++; 
            const val = !evalExpr();
            // skip ')'
            idx++;
            return val;
        }

        // AND or OR operation
        const op = ch; // '&' or '|'
        // skip '('
        idx++;

        let result: boolean = op === '&';
        while (true) {
            const v = evalExpr();
            if (op === '&') {
                result = result && v;
            } else { // '|'
                result = result || v;
            }

            if (expression[idx] === ')') break; // end of this sub‑expression
            // skip ','
            idx++;
        }
        // skip ')'
        idx++;
        return result;
    }

    return evalExpr();
}
```

## Php

```php
class Solution {
    /**
     * @param string $expression
     * @return bool
     */
    function parseBoolExpr($expression) {
        $idx = 0;
        return $this->evaluate($expression, $idx);
    }

    private function evaluate(string $s, int &$i): bool {
        $c = $s[$i];
        if ($c === 't') {
            $i++;
            return true;
        }
        if ($c === 'f') {
            $i++;
            return false;
        }

        // operator: ! & |
        $op = $c;
        $i++;          // skip operator
        $i++;          // skip '('

        if ($op === '!') {
            $val = $this->evaluate($s, $i);
            $i++;      // skip ')'
            return !$val;
        }

        $result = ($op === '&'); // true for AND start, false for OR start
        while (true) {
            $val = $this->evaluate($s, $i);
            if ($op === '&') {
                $result = $result && $val;
            } else { // '|'
                $result = $result || $val;
            }

            if ($s[$i] === ',') {
                $i++; // skip comma and continue
                continue;
            }
            if ($s[$i] === ')') {
                $i++; // skip closing parenthesis
                break;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func parseBoolExpr(_ expression: String) -> Bool {
        let chars = Array(expression)
        var idx = 0
        
        func eval() -> Bool {
            let ch = chars[idx]
            idx += 1
            
            if ch == "t" { return true }
            if ch == "f" { return false }
            
            if ch == "!" {
                // skip '('
                idx += 1
                let value = !eval()
                // skip ')'
                idx += 1
                return value
            }
            
            // '&' or '|'
            let op = ch
            // skip '('
            idx += 1
            
            var result: Bool
            if op == "&" {
                result = true
                while chars[idx] != ")" {
                    let v = eval()
                    if !v { result = false }
                    if chars[idx] == "," { idx += 1 }
                }
            } else { // '|'
                result = false
                while chars[idx] != ")" {
                    let v = eval()
                    if v { result = true }
                    if chars[idx] == "," { idx += 1 }
                }
            }
            // skip ')'
            idx += 1
            return result
        }
        
        return eval()
    }
}
```

## Kotlin

```kotlin
class Solution {
    private var idx = 0
    fun parseBoolExpr(expression: String): Boolean {
        idx = 0
        return parse(expression)
    }

    private fun parse(s: String): Boolean {
        val ch = s[idx++]
        return when (ch) {
            't' -> true
            'f' -> false
            '!' -> {
                idx++ // skip '('
                val inner = parse(s)
                idx++ // skip ')'
                !inner
            }
            '&', '|' -> {
                val op = ch
                idx++ // skip '('
                var result = if (op == '&') true else false
                while (true) {
                    val v = parse(s)
                    result = if (op == '&') result && v else result || v
                    when (s[idx]) {
                        ',' -> idx++
                        ')' -> {
                            idx++
                            break
                        }
                    }
                }
                result
            }
            else -> false
        }
    }
}
```

## Dart

```dart
class Solution {
  bool parseBoolExpr(String expression) {
    int i = 0;

    bool eval() {
      String c = expression[i];
      // literals
      if (c == 't') {
        i++;
        return true;
      }
      if (c == 'f') {
        i++;
        return false;
      }

      // NOT operator
      if (c == '!') {
        i++; // skip '!'
        i++; // skip '('
        bool val = eval();
        i++; // skip ')'
        return !val;
      }

      // AND or OR operators
      bool isAnd = c == '&';
      i++; // skip operator
      i++; // skip '('

      bool result = isAnd ? true : false;

      while (true) {
        bool val = eval();
        if (isAnd) {
          if (!val) result = false;
        } else {
          if (val) result = true;
        }

        if (expression[i] == ')') {
          i++; // skip ')'
          break;
        }
        // skip comma
        i++;
      }

      return result;
    }

    return eval();
  }
}
```

## Golang

```go
func parseBoolExpr(expression string) bool {
    i := 0
    var eval func() bool
    eval = func() bool {
        ch := expression[i]
        i++
        if ch == 't' {
            return true
        }
        if ch == 'f' {
            return false
        }
        // operator: '&', '|', '!'
        op := ch
        // skip '('
        i++ // assume current char is '('
        switch op {
        case '!':
            val := eval()
            i++ // skip ')'
            return !val
        case '&':
            res := true
            for {
                v := eval()
                if !v {
                    res = false
                }
                if expression[i] == ')' {
                    i++ // skip ')'
                    break
                }
                i++ // skip ','
            }
            return res
        case '|':
            res := false
            for {
                v := eval()
                if v {
                    res = true
                }
                if expression[i] == ')' {
                    i++ // skip ')'
                    break
                }
                i++ // skip ','
            }
            return res
        }
        return false
    }
    return eval()
}
```

## Ruby

```ruby
def parse_bool_expr(expression)
  i = 0
  s = expression

  eval = lambda do
    ch = s[i]
    i += 1
    case ch
    when 't'
      true
    when 'f'
      false
    when '!'
      i += 1 # skip '('
      val = !eval.call
      i += 1 # skip ')'
      val
    when '&', '|'
      op = ch
      i += 1 # skip '('
      vals = []
      loop do
        vals << eval.call
        break if s[i] == ')'
        i += 1 # skip ','
      end
      i += 1 # skip ')'
      if op == '&'
        vals.all?
      else
        vals.any?
      end
    else
      nil
    end
  end

  eval.call
end
```

## Scala

```scala
object Solution {
    def parseBoolExpr(expression: String): Boolean = {
        var idx = 0
        val n = expression.length

        def parse(): Boolean = {
            val c = expression.charAt(idx)
            idx += 1
            c match {
                case 't' => true
                case 'f' => false
                case '!' =>
                    // skip '('
                    idx += 1
                    val v = !parse()
                    // skip ')'
                    idx += 1
                    v
                case '&' | '|' =>
                    val op = c
                    // skip '('
                    idx += 1
                    var result = if (op == '&') true else false
                    var continue = true
                    while (continue) {
                        val sub = parse()
                        op match {
                            case '&' => if (!sub) result = false
                            case '|' => if (sub) result = true
                        }
                        if (idx < n && expression.charAt(idx) == ',') {
                            idx += 1 // skip comma
                        } else {
                            continue = false
                        }
                    }
                    // skip ')'
                    idx += 1
                    result
            }
        }

        parse()
    }
}
```

## Rust

```rust
fn dfs(s: &[u8], idx: &mut usize) -> bool {
    let c = s[*idx] as char;
    *idx += 1;
    match c {
        't' => true,
        'f' => false,
        '!' => {
            // skip '('
            *idx += 1;
            let val = dfs(s, idx);
            // skip ')'
            *idx += 1;
            !val
        }
        '&' | '|' => {
            let op = c;
            // skip '('
            *idx += 1;
            let mut result = if op == '&' { true } else { false };
            loop {
                let val = dfs(s, idx);
                match op {
                    '&' => {
                        if !val {
                            result = false;
                        }
                    }
                    '|' => {
                        if val {
                            result = true;
                        }
                    }
                    _ => {}
                }
                if s[*idx] == b',' {
                    *idx += 1; // skip comma
                } else if s[*idx] == b')' {
                    break;
                }
            }
            // skip ')'
            *idx += 1;
            result
        }
        _ => false,
    }
}

impl Solution {
    pub fn parse_bool_expr(expression: String) -> bool {
        let bytes = expression.as_bytes();
        let mut idx = 0;
        dfs(bytes, &mut idx)
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (parse-bool-expr expression)
  (-> string? boolean?)
  (letrec
      ((s expression)
       (len (string-length s))
       (parse
        (lambda (i)
          (let ((c (string-ref s i)))
            (cond
              [(char=? c #\t) (values #t (+ i 1))]
              [(char=? c #\f) (values #f (+ i 1))]
              [(char=? c #\!)
               (let-values (((val next) (parse (+ i 2)))) ; skip "!("
                 (values (not val) (+ next 1)))]          ; skip ")"
              [(or (char=? c #\&) (char=? c #\|))
               (let ((op c)
                     (idx (+ i 2)))                       ; skip "op("
                 (letrec ((parse-args
                           (lambda (j)
                             (let-values (((val next) (parse j)))
                               (if (char=? (string-ref s next) #\,)
                                   (let-values (((rest end) (parse-args (+ next 1))))
                                     (values (cons val rest) end))
                                   (values (list val) next))))))
                   (let-values (((vals end-idx) (parse-args idx)))
                     (define result
                       (if (char=? op #\&)
                           (andmap identity vals)
                           (ormap identity vals)))
                     (values result (+ end-idx 1)))))]
              [else (error "invalid character")]))))
    (let-values (((res _) (parse 0))) res)))
```

## Erlang

```erlang
-module(solution).
-export([parse_bool_expr/1]).

-spec parse_bool_expr(Expression :: unicode:unicode_binary()) -> boolean().
parse_bool_expr(Expression) ->
    Stack = process_expression(binary_to_list(Expression), []),
    case Stack of
        [$t|_] -> true;
        [_|_] -> false
    end.

process_expression([], Stack) ->
    Stack;
process_expression([Char | Rest], Stack) ->
    case Char of
        $!; $&; $|; $t; $f ->
            process_expression(Rest, [Char | Stack]);
        $) ->
            NewStack = handle_close(Stack),
            process_expression(Rest, NewStack);
        $(; $, ->
            process_expression(Rest, Stack)
    end.

handle_close(Stack) ->
    {Op, RestAfterValues, HasTrue, HasFalse} = pop_until_operator(Stack, false, false),
    ResultChar =
        case Op of
            $! -> if HasTrue -> $f; true -> $t end;
            $& -> if HasFalse -> $f; true -> $t end;
            $| -> if HasTrue -> $t; true -> $f end
        end,
    [ResultChar | RestAfterValues].

pop_until_operator([Top | Rest], HasT, HasF) ->
    case Top of
        $t -> pop_until_operator(Rest, true, HasF);
        $f -> pop_until_operator(Rest, HasT, true);
        Op when Op == $!; Op == $&; Op == $| ->
            {Op, Rest, HasT, HasF}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec parse_bool_expr(expression :: String.t()) :: boolean()
  def parse_bool_expr(expression) do
    chars = :binary.bin_to_list(expression)

    final_stack =
      Enum.reduce(chars, [], fn ch, stack ->
        cond do
          ch == ?, -> stack
          ch == ?) ->
            {values, rest_with_paren} = pop_until_left_paren(stack, [])
            # rest_with_paren starts with '(' followed by the operator
            [_paren | rest] = rest_with_paren
            [op | remaining] = rest
            result = compute(op, values)
            [result | remaining]

          true ->
            [ch | stack]
        end
      end)

    case final_stack do
      [?t | _] -> true
      [_f | _] -> false
    end
  end

  defp pop_until_left_paren([h | t], acc) do
    if h == ?( do
      {Enum.reverse(acc), [h | t]}
    else
      pop_until_left_paren(t, [h | acc])
    end
  end

  defp compute(?!, [val]) do
    case val do
      ?t -> ?f
      ?f -> ?t
    end
  end

  defp compute(?&, vals) do
    if Enum.any?(vals, fn v -> v == ?f end), do: ?f, else: ?t
  end

  defp compute(?|, vals) do
    if Enum.any?(vals, fn v -> v == ?t end), do: ?t, else: ?f
  end
end
```
