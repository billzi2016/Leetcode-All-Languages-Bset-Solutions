# 1556. Thousand Separator

## Cpp

```cpp
class Solution {
public:
    std::string thousandSeparator(int n) {
        std::string s = std::to_string(n);
        int len = s.size();
        std::string res;
        for (int i = 0; i < len; ++i) {
            if (i > 0 && (len - i) % 3 == 0) {
                res.push_back('.');
            }
            res.push_back(s[i]);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String thousandSeparator(int n) {
        String s = Integer.toString(n);
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            sb.append(s.charAt(i));
            cnt++;
            if (cnt == 3 && i != 0) {
                sb.append('.');
                cnt = 0;
            }
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        parts = []
        for i, ch in enumerate(reversed(s)):
            if i and i % 3 == 0:
                parts.append('.')
            parts.append(ch)
        return ''.join(reversed(parts))
```

## Python3

```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        parts = []
        while s:
            parts.append(s[-3:])
            s = s[:-3]
        return '.'.join(reversed(parts))
```

## C

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* thousandSeparator(int n) {
    // Convert integer to string without separators
    char numStr[12]; // enough for 32-bit int and null terminator
    sprintf(numStr, "%d", n);
    int len = strlen(numStr);
    
    // Calculate number of dots needed
    int dotCount = (len - 1) / 3;
    int newLen = len + dotCount;
    
    char *res = (char *)malloc(newLen + 1); // +1 for null terminator
    if (!res) return NULL;
    
    int i = len - 1;      // index in original string
    int j = newLen - 1;   // index in result string
    int cnt = 0;          // count of digits placed since last dot
    
    while (i >= 0) {
        res[j--] = numStr[i--];
        cnt++;
        if (cnt == 3 && i >= 0) {
            res[j--] = '.';
            cnt = 0;
        }
    }
    
    res[newLen] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ThousandSeparator(int n) {
        string s = n.ToString();
        var sb = new System.Text.StringBuilder();
        int count = 0;
        for (int i = s.Length - 1; i >= 0; i--) {
            sb.Append(s[i]);
            count++;
            if (count == 3 && i != 0) {
                sb.Append('.');
                count = 0;
            }
        }
        char[] arr = sb.ToString().ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function(n) {
    const s = n.toString();
    let result = '';
    let count = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        result = s[i] + result;
        count++;
        if (count % 3 === 0 && i !== 0) {
            result = '.' + result;
        }
    }
    return result;
};
```

## Typescript

```typescript
function thousandSeparator(n: number): string {
    const s = n.toString();
    let result = "";
    let cnt = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        result = s[i] + result;
        cnt++;
        if (cnt === 3 && i !== 0) {
            result = "." + result;
            cnt = 0;
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function thousandSeparator($n) {
        $s = (string)$n;
        $len = strlen($s);
        $result = '';
        $cnt = 0;
        for ($i = $len - 1; $i >= 0; $i--) {
            $result = $s[$i] . $result;
            $cnt++;
            if ($cnt % 3 == 0 && $i != 0) {
                $result = '.' . $result;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func thousandSeparator(_ n: Int) -> String {
        let s = String(n)
        var result = ""
        var count = 0
        for ch in s.reversed() {
            if count == 3 {
                result.append(".")
                count = 0
            }
            result.append(ch)
            count += 1
        }
        return String(result.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun thousandSeparator(n: Int): String {
        val s = n.toString()
        val sb = StringBuilder()
        var cnt = 0
        for (i in s.length - 1 downTo 0) {
            sb.append(s[i])
            cnt++
            if (cnt == 3 && i != 0) {
                sb.append('.')
                cnt = 0
            }
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String thousandSeparator(int n) {
    String s = n.toString();
    List<String> parts = [];
    for (int i = s.length; i > 0; i -= 3) {
      int start = i - 3 >= 0 ? i - 3 : 0;
      parts.add(s.substring(start, i));
    }
    return parts.reversed.join('.');
  }
}
```

## Golang

```go
package main

import "strconv"

func thousandSeparator(n int) string {
	s := strconv.Itoa(n)
	var b []byte
	cnt := 0
	for i := len(s) - 1; i >= 0; i-- {
		b = append(b, s[i])
		cnt++
		if cnt == 3 && i != 0 {
			b = append(b, '.')
			cnt = 0
		}
	}
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}
```

## Ruby

```ruby
def thousand_separator(n)
  s = n.to_s
  parts = s.reverse.scan(/.{1,3}/)
  parts.join('.').reverse
end
```

## Scala

```scala
object Solution {
    def thousandSeparator(n: Int): String = {
        val s = n.toString
        val sb = new java.lang.StringBuilder()
        var count = 0
        for (i <- s.length - 1 to 0 by -1) {
            sb.append(s.charAt(i))
            count += 1
            if (count == 3 && i != 0) {
                sb.append('.')
                count = 0
            }
        }
        sb.reverse.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn thousand_separator(n: i32) -> String {
        let s = n.to_string();
        let mut parts: Vec<&str> = Vec::new();
        let mut i = s.len();
        while i > 0 {
            let start = if i >= 3 { i - 3 } else { 0 };
            parts.push(&s[start..i]);
            i = start;
        }
        parts.reverse();
        parts.join(".")
    }
}
```

## Racket

```racket
(define/contract (thousand-separator n)
  (-> exact-integer? string?)
  (let* ([s (number->string n)]
         [len (string-length s)])
    (if (<= len 3)
        s
        (let* ([first-mod (remainder len 3)]
               [first-size (if (= first-mod 0) 3 first-mod)])
          (let loop ((pos first-size)
                     (acc (substring s 0 first-size)))
            (if (>= pos len)
                acc
                (loop (+ pos 3)
                      (string-append acc "." (substring s pos (+ pos 3))))))))))
```

## Erlang

```erlang
-module(solution).
-export([thousand_separator/1]).

-spec thousand_separator(N :: integer()) -> unicode:unicode_binary().
thousand_separator(N) ->
    Digits = integer_to_list(N),
    RevDigits = lists:reverse(Digits),
    ProcessedRev = insert_dots(RevDigits, 0),
    FormattedList = lists:reverse(ProcessedRev),
    unicode:characters_to_binary(FormattedList).

insert_dots([], _Count) -> [];
insert_dots([H|T], Count) ->
    case Count of
        3 ->
            ['.' , H] ++ insert_dots(T, 1);
        _ ->
            [H] ++ insert_dots(T, Count + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec thousand_separator(n :: integer) :: String.t()
  def thousand_separator(n) do
    n
    |> Integer.to_string()
    |> String.graphemes()
    |> Enum.reverse()
    |> Enum.chunk_every(3, 3, [])
    |> Enum.map(&Enum.join/1)
    |> Enum.join(".")
    |> String.reverse()
  end
end
```
