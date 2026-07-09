# 0394. Decode String

## Cpp

```cpp
class Solution {
public:
    string decodeString(string s) {
        stack<int> countStack;
        stack<string> stringStack;
        string cur = "";
        int k = 0;
        for (char ch : s) {
            if (isdigit(ch)) {
                k = k * 10 + (ch - '0');
            } else if (ch == '[') {
                countStack.push(k);
                stringStack.push(cur);
                cur.clear();
                k = 0;
            } else if (ch == ']') {
                int repeat = countStack.top(); countStack.pop();
                string prev = stringStack.top(); stringStack.pop();
                string expanded;
                expanded.reserve(prev.size() + cur.size() * repeat);
                expanded += prev;
                for (int i = 0; i < repeat; ++i) {
                    expanded += cur;
                }
                cur.swap(expanded);
            } else {
                cur.push_back(ch);
            }
        }
        return cur;
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public String decodeString(String s) {
        Deque<Integer> countStack = new ArrayDeque<>();
        Deque<StringBuilder> stringStack = new ArrayDeque<>();
        StringBuilder current = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                int num = 0;
                while (i < s.length() && Character.isDigit(s.charAt(i))) {
                    num = num * 10 + (s.charAt(i) - '0');
                    i++;
                }
                countStack.push(num);
            } else if (ch == '[') {
                stringStack.push(current);
                current = new StringBuilder();
                i++;
            } else if (ch == ']') {
                int repeat = countStack.pop();
                StringBuilder prev = stringStack.pop();
                for (int r = 0; r < repeat; r++) {
                    prev.append(current);
                }
                current = prev;
                i++;
            } else { // letter
                current.append(ch);
                i++;
            }
        }
        return current.toString();
    }
}
```

## Python

```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        string_stack = []
        cur_num = 0
        cur_str = ''
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                count_stack.append(cur_num)
                string_stack.append(cur_str)
                cur_num = 0
                cur_str = ''
            elif ch == ']':
                repeat = count_stack.pop()
                prev_str = string_stack.pop()
                cur_str = prev_str + cur_str * repeat
            else:
                cur_str += ch
        return cur_str
```

## Python3

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ""
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif ch == ']':
                prev_str, repeat = stack.pop()
                cur_str = prev_str + cur_str * repeat
            else:  # letter
                cur_str += ch
        return cur_str
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static char* decode(char **p) {
    int cap = 128;
    char *buf = (char *)malloc(cap);
    int len = 0;

    while (**p && **p != ']') {
        if (isdigit(**p)) {
            int k = 0;
            while (isdigit(**p)) {
                k = k * 10 + (**p - '0');
                (*p)++;
            }
            // skip '['
            (*p)++; 
            char *sub = decode(p);
            int sublen = strlen(sub);
            long need = (long)k * sublen;
            while ((long)len + need >= cap) {
                cap *= 2;
                buf = (char *)realloc(buf, cap);
            }
            for (int i = 0; i < k; ++i) {
                memcpy(buf + len, sub, sublen);
                len += sublen;
            }
            free(sub);
        } else { // letter
            if (len + 1 >= cap) {
                cap *= 2;
                buf = (char *)realloc(buf, cap);
            }
            buf[len++] = **p;
            (*p)++;
        }
    }

    if (**p == ']') (*p)++; // skip closing bracket

    if (len + 1 >= cap) {
        cap += 1;
        buf = (char *)realloc(buf, cap);
    }
    buf[len] = '\0';
    return buf;
}

char* decodeString(char* s) {
    char *ptr = s;
    return decode(&ptr);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string DecodeString(string s) {
        var countStack = new Stack<int>();
        var resultStack = new Stack<StringBuilder>();
        var currentNum = 0;
        var currentStr = new StringBuilder();

        foreach (char ch in s) {
            if (char.IsDigit(ch)) {
                currentNum = currentNum * 10 + (ch - '0');
            } else if (ch == '[') {
                countStack.Push(currentNum);
                resultStack.Push(currentStr);
                currentNum = 0;
                currentStr = new StringBuilder();
            } else if (ch == ']') {
                int repeat = countStack.Pop();
                var prevStr = resultStack.Pop();
                for (int i = 0; i < repeat; i++) {
                    prevStr.Append(currentStr);
                }
                currentStr = prevStr;
            } else {
                currentStr.Append(ch);
            }
        }

        return currentStr.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    const numStack = [];
    const strStack = [];
    let curNum = 0;
    let curStr = '';
    
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch >= '0' && ch <= '9') {
            curNum = curNum * 10 + (ch.charCodeAt(0) - 48);
        } else if (ch === '[') {
            numStack.push(curNum);
            strStack.push(curStr);
            curNum = 0;
            curStr = '';
        } else if (ch === ']') {
            const repeat = numStack.pop();
            const prev = strStack.pop();
            curStr = prev + curStr.repeat(repeat);
        } else {
            curStr += ch;
        }
    }
    
    return curStr;
};
```

## Typescript

```typescript
function decodeString(s: string): string {
    const numStack: number[] = [];
    const strStack: string[] = [];
    let curNum = 0;
    let curStr = '';
    
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch >= '0' && ch <= '9') {
            curNum = curNum * 10 + (ch.charCodeAt(0) - 48);
        } else if (ch === '[') {
            numStack.push(curNum);
            strStack.push(curStr);
            curNum = 0;
            curStr = '';
        } else if (ch === ']') {
            const repeat = numStack.pop()!;
            const prevStr = strStack.pop()!;
            curStr = prevStr + curStr.repeat(repeat);
        } else {
            curStr += ch;
        }
    }
    
    return curStr;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function decodeString($s) {
        $countStack = [];
        $stringStack = [];
        $currentNum = 0;
        $currentStr = '';
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (ctype_digit($ch)) {
                $currentNum = $currentNum * 10 + intval($ch);
            } elseif ($ch === '[') {
                array_push($stringStack, $currentStr);
                array_push($countStack, $currentNum);
                $currentStr = '';
                $currentNum = 0;
            } elseif ($ch === ']') {
                $repeat = array_pop($countStack);
                $prevStr = array_pop($stringStack);
                $currentStr = $prevStr . str_repeat($currentStr, $repeat);
            } else { // letter
                $currentStr .= $ch;
            }
        }
        return $currentStr;
    }
}
```

## Swift

```swift
class Solution {
    func decodeString(_ s: String) -> String {
        var countStack = [Int]()
        var stringStack = [String]()
        var currentNum = 0
        var currentStr = ""
        
        for ch in s {
            if let digit = ch.wholeNumberValue {
                currentNum = currentNum * 10 + digit
            } else if ch == "[" {
                countStack.append(currentNum)
                stringStack.append(currentStr)
                currentNum = 0
                currentStr = ""
            } else if ch == "]" {
                let repeatCount = countStack.removeLast()
                let prevStr = stringStack.removeLast()
                var repeated = ""
                for _ in 0..<repeatCount {
                    repeated += currentStr
                }
                currentStr = prevStr + repeated
            } else {
                currentStr.append(ch)
            }
        }
        
        return currentStr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decodeString(s: String): String {
        val countStack = ArrayDeque<Int>()
        val stringStack = ArrayDeque<StringBuilder>()
        var curNum = 0
        var curStr = StringBuilder()
        for (ch in s) {
            when {
                ch.isDigit() -> {
                    curNum = curNum * 10 + (ch - '0')
                }
                ch == '[' -> {
                    countStack.addLast(curNum)
                    stringStack.addLast(curStr)
                    curNum = 0
                    curStr = StringBuilder()
                }
                ch == ']' -> {
                    val repeatTimes = countStack.removeLast()
                    val prevStr = stringStack.removeLast()
                    val repeated = curStr.toString().repeat(repeatTimes)
                    curStr = prevStr.append(repeated)
                }
                else -> {
                    curStr.append(ch)
                }
            }
        }
        return curStr.toString()
    }
}
```

## Dart

```dart
class Solution {
  String decodeString(String s) {
    List<int> countStack = [];
    List<String> stringStack = [];
    StringBuffer cur = StringBuffer();
    int i = 0;
    while (i < s.length) {
      String c = s[i];
      if (c.compareTo('0') >= 0 && c.compareTo('9') <= 0) {
        int num = 0;
        while (i < s.length &&
            s[i].compareTo('0') >= 0 &&
            s[i].compareTo('9') <= 0) {
          num = num * 10 + (s.codeUnitAt(i) - 48);
          i++;
        }
        countStack.add(num);
      } else if (c == '[') {
        stringStack.add(cur.toString());
        cur = StringBuffer();
        i++;
      } else if (c == ']') {
        int repeat = countStack.removeLast();
        String prev = stringStack.removeLast();
        StringBuffer sb = StringBuffer(prev);
        for (int k = 0; k < repeat; k++) {
          sb.write(cur);
        }
        cur = sb;
        i++;
      } else {
        cur.write(c);
        i++;
      }
    }
    return cur.toString();
  }
}
```

## Golang

```go
func decodeString(s string) string {
    var countStack []int
    var strStack []string
    cur := ""
    i, n := 0, len(s)
    for i < n {
        ch := s[i]
        if ch >= '0' && ch <= '9' {
            num := 0
            for i < n && s[i] >= '0' && s[i] <= '9' {
                num = num*10 + int(s[i]-'0')
                i++
            }
            countStack = append(countStack, num)
        } else if ch == '[' {
            strStack = append(strStack, cur)
            cur = ""
            i++
        } else if ch == ']' {
            k := countStack[len(countStack)-1]
            countStack = countStack[:len(countStack)-1]
            prev := strStack[len(strStack)-1]
            strStack = strStack[:len(strStack)-1]

            repeated := ""
            for j := 0; j < k; j++ {
                repeated += cur
            }
            cur = prev + repeated
            i++
        } else { // letter
            cur += string(ch)
            i++
        }
    }
    return cur
}
```

## Ruby

```ruby
def decode_string(s)
  num_stack = []
  str_stack = []
  cur_num = 0
  cur_str = ''
  s.each_char do |ch|
    if ch >= '0' && ch <= '9'
      cur_num = cur_num * 10 + (ch.ord - 48)
    elsif ch == '['
      num_stack << cur_num
      str_stack << cur_str
      cur_num = 0
      cur_str = ''
    elsif ch == ']'
      repeat = num_stack.pop
      prev = str_stack.pop
      cur_str = prev + cur_str * repeat
    else
      cur_str << ch
    end
  end
  cur_str
end
```

## Scala

```scala
object Solution {
  def decodeString(s: String): String = {
    val countStack = scala.collection.mutable.Stack[Int]()
    val stringStack = scala.collection.mutable.Stack[StringBuilder]()
    var curr = new StringBuilder
    var i = 0
    while (i < s.length) {
      val ch = s.charAt(i)
      if (ch.isDigit) {
        var num = 0
        while (i < s.length && s.charAt(i).isDigit) {
          num = num * 10 + (s.charAt(i) - '0')
          i += 1
        }
        countStack.push(num)
      } else if (ch == '[') {
        stringStack.push(curr)
        curr = new StringBuilder
        i += 1
      } else if (ch == ']') {
        val repeat = countStack.pop()
        val prev = stringStack.pop()
        for (_ <- 0 until repeat) {
          prev.append(curr)
        }
        curr = prev
        i += 1
      } else {
        curr.append(ch)
        i += 1
      }
    }
    curr.toString
  }
}
```

## Rust

```rust
impl Solution {
    pub fn decode_string(s: String) -> String {
        let mut count_stack: Vec<usize> = Vec::new();
        let mut string_stack: Vec<String> = Vec::new();
        let mut cur = String::new();
        let mut num = 0usize;

        for ch in s.chars() {
            if ch.is_ascii_digit() {
                num = num * 10 + (ch as u8 - b'0') as usize;
            } else if ch == '[' {
                count_stack.push(num);
                string_stack.push(cur.clone());
                cur.clear();
                num = 0;
            } else if ch == ']' {
                let repeat = count_stack.pop().unwrap();
                let prev = string_stack.pop().unwrap();
                let mut expanded = String::new();
                for _ in 0..repeat {
                    expanded.push_str(&cur);
                }
                cur = prev + &expanded;
            } else {
                cur.push(ch);
            }
        }

        cur
    }
}
```

## Racket

```racket
(define/contract (decode-string s)
  (-> string? string?)
  (let* ((len (string-length s))
         ;; repeat a string n times
         (repeat (lambda (str n)
                   (for/fold ([acc ""]) ([i (in-range n)])
                     (string-append acc str))))
         ;; recursive parser returning two values: decoded substring and next index
         (parse
          (letrec ((parse
                    (lambda (i)
                      (let loop ((idx i) (res ""))
                        (if (>= idx len)
                            (values res idx)
                            (let ((ch (string-ref s idx)))
                              (cond
                                [(char-numeric? ch)
                                 ;; parse the repeat count
                                 (let-values (((num j)
                                               (let loop-number ((j idx) (num 0))
                                                 (if (and (< j len)
                                                          (char-numeric?
                                                           (string-ref s j)))
                                                     (loop-number (+ j 1)
                                                                  (+ (* num 10)
                                                                     (- (char->integer
                                                                         (string-ref s j))
                                                                        (char->integer #\0))))
                                                     (values num j)))))
                                   ;; skip the '['
                                   (let ((start (+ j 1)))
                                     (let-values (((sub next-idx) (parse start)))
                                       (let ((rep (repeat sub num)))
                                         (loop next-idx
                                               (string-append res rep))))))]
                                [(char=? ch #\])
                                 (values res (+ idx 1))]
                                [else
                                 (loop (+ idx 1)
                                       (string-append res (string ch)))]))))))))
            parse))
    (let-values (((result _) (parse 0)))
      result)))
```

## Erlang

```erlang
-spec decode_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
decode_string(S) ->
    {Result, _} = parse(binary_to_list(S), []),
    list_to_binary(Result).

%% Parses the character list until end or a closing bracket.
parse([], Acc) ->
    {lists:reverse(Acc), []};
parse([C|Rest], Acc) when C >= $0, C =< $9 ->
    {Num, RestAfterNum} = get_number([C|Rest]),
    case RestAfterNum of
        [$[ | AfterBracket] ->
            {SubDecoded, AfterClose} = parse(AfterBracket, []),
            Repeated = repeat_decode(SubDecoded, Num),
            NewAcc = lists:reverse(Repeated) ++ Acc,
            parse(AfterClose, NewAcc);
        _ ->
            {lists:reverse(Acc), RestAfterNum}
    end;
parse([$] | Rest], Acc) ->
    {lists:reverse(Acc), Rest};
parse([C|Rest], Acc) ->
    parse(Rest, [C|Acc]).

%% Consumes consecutive digits and returns the number and remaining chars.
get_number([C|Rest]) when C >= $0, C =< $9 ->
    get_number(Rest, C - $0).

get_number([], Num) -> {Num, []};
get_number([D|Rs], Num) when D >= $0, D =< $9 ->
    NewNum = Num * 10 + (D - $0),
    get_number(Rs, NewNum);
get_number(Rest, Num) ->
    {Num, Rest}.

%% Repeats a decoded sublist N times.
repeat_decode(Sub, N) ->
    lists:flatten(lists:duplicate(N, Sub)).
```

## Elixir

```elixir
defmodule Solution do
  @spec decode_string(s :: String.t) :: String.t
  def decode_string(s) do
    chars = String.to_charlist(s)
    {result, _rest} = parse(chars, [])
    result
  end

  # Main parser: accumulates parts in reverse order for efficiency.
  defp parse([], acc), do: {Enum.reverse(acc) |> Enum.join(), []}
  defp parse([?\] | rest], acc), do: {Enum.reverse(acc) |> Enum.join(), rest}

  defp parse([c | _] = chars, acc) when c in ?0..?9 do
    {num, after_num} = parse_number(chars, 0)
    # skip the '[' character
    [_open_bracket | after_bracket] = after_num
    {inner_str, after_inner} = parse(after_bracket, [])
    repeated = String.duplicate(inner_str, num)
    parse(after_inner, [repeated | acc])
  end

  defp parse([c | rest], acc) when c in ?a..?z do
    parse(rest, [<<c>> | acc])
  end

  # Parse a multi-digit number and return {number, remaining_chars}
  defp parse_number([], num), do: {num, []}
  defp parse_number([c | rest], num) when c in ?0..?9 do
    new_num = num * 10 + (c - ?0)
    parse_number(rest, new_num)
  end
  defp parse_number(chars, num), do: {num, chars}
end
```
