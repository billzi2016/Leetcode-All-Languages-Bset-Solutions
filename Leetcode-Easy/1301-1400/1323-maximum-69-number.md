# 1323. Maximum 69 Number

## Cpp

```cpp
class Solution {
public:
    int maximum69Number(int num) {
        std::string s = std::to_string(num);
        for (char &c : s) {
            if (c == '6') {
                c = '9';
                break;
            }
        }
        return std::stoi(s);
    }
};
```

## Java

```java
class Solution {
    public int maximum69Number(int num) {
        char[] chars = Integer.toString(num).toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '6') {
                chars[i] = '9';
                break;
            }
        }
        return Integer.parseInt(new String(chars));
    }
}
```

## Python

```python
class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        return int(''.join(s))
```

## Python3

```python
class Solution:
    def maximum69Number(self, num: int) -> int:
        s = list(str(num))
        for i, ch in enumerate(s):
            if ch == '6':
                s[i] = '9'
                break
        return int(''.join(s))
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

int maximum69Number(int num) {
    char s[12];
    sprintf(s, "%d", num);
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '6') {
            s[i] = '9';
            break;
        }
    }
    return atoi(s);
}
```

## Csharp

```csharp
public class Solution {
    public int Maximum69Number(int num) {
        char[] chars = num.ToString().ToCharArray();
        for (int i = 0; i < chars.Length; i++) {
            if (chars[i] == '6') {
                chars[i] = '9';
                break;
            }
        }
        return int.Parse(new string(chars));
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function(num) {
    const digits = num.toString().split('');
    for (let i = 0; i < digits.length; i++) {
        if (digits[i] === '6') {
            digits[i] = '9';
            break;
        }
    }
    return parseInt(digits.join(''), 10);
};
```

## Typescript

```typescript
function maximum69Number (num: number): number {
    const s = num.toString().split('');
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '6') {
            s[i] = '9';
            break;
        }
    }
    return parseInt(s.join(''), 10);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function maximum69Number ($num) {
        $s = strval($num);
        $pos = strpos($s, '6');
        if ($pos !== false) {
            $s[$pos] = '9';
        }
        return intval($s);
    }
}
```

## Swift

```swift
class Solution {
    func maximum69Number(_ num: Int) -> Int {
        var digits = Array(String(num))
        for i in 0..<digits.count {
            if digits[i] == "6" {
                digits[i] = "9"
                break
            }
        }
        return Int(String(digits))!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximum69Number(num: Int): Int {
        val chars = num.toString().toCharArray()
        for (i in chars.indices) {
            if (chars[i] == '6') {
                chars[i] = '9'
                break
            }
        }
        return String(chars).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maximum69Number(int num) {
    List<String> digits = num.toString().split('');
    for (int i = 0; i < digits.length; i++) {
      if (digits[i] == '6') {
        digits[i] = '9';
        break;
      }
    }
    return int.parse(digits.join());
  }
}
```

## Golang

```go
import "strconv"

func maximum69Number(num int) int {
    s := []byte(strconv.Itoa(num))
    for i, c := range s {
        if c == '6' {
            s[i] = '9'
            break
        }
    }
    res, _ := strconv.Atoi(string(s))
    return res
}
```

## Ruby

```ruby
def maximum69_number (num)
  s = num.to_s
  i = s.index('6')
  return num unless i
  s[i] = '9'
  s.to_i
end
```

## Scala

```scala
object Solution {
    def maximum69Number(num: Int): Int = {
        val s = num.toString
        val idx = s.indexOf('6')
        if (idx == -1) num
        else {
            val sb = new StringBuilder(s)
            sb.setCharAt(idx, '9')
            sb.toString.toInt
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum69_number(num: i32) -> i32 {
        let mut s = num.to_string();
        if let Some(pos) = s.find('6') {
            s.replace_range(pos..pos + 1, "9");
        }
        s.parse().unwrap()
    }
}
```

## Racket

```racket
(define/contract (maximum69-number num)
  (-> exact-integer? exact-integer?)
  (let* ((s (number->string num))
         (len (string-length s))
         (pos
          (let loop ((i 0))
            (cond [(= i len) #f]
                  [(char=? (string-ref s i) #\6) i]
                  [else (loop (+ i 1))]))))
    (if pos
        (string->number
         (string-append
          (substring s 0 pos)
          "9"
          (substring s (+ pos 1))))
        num)))
```

## Erlang

```erlang
-module(solution).
-export([maximum69_number/1]).

-spec maximum69_number(integer()) -> integer().
maximum69_number(Num) ->
    Digits = integer_to_list(Num),
    NewDigits = replace_first_six(Digits),
    list_to_integer(NewDigits).

replace_first_six([]) -> [];
replace_first_six([$6 | Rest]) -> [$9 | Rest];
replace_first_six([H | Rest]) -> [H | replace_first_six(Rest)].
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum69_number(num :: integer) :: integer
  def maximum69_number(num) do
    s = Integer.to_string(num)

    if String.contains?(s, "6") do
      new_s = String.replace(s, "6", "9", global: false)
      String.to_integer(new_s)
    else
      num
    end
  end
end
```
