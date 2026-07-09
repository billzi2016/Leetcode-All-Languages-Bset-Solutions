# 1736. Latest Time by Replacing Hidden Digits

## Cpp

```cpp
class Solution {
public:
    string maximumTime(string time) {
        // hour tens
        if (time[0] == '?') {
            if (time[1] == '?' || time[1] <= '3')
                time[0] = '2';
            else
                time[0] = '1';
        }
        // hour units
        if (time[1] == '?') {
            if (time[0] == '2')
                time[1] = '3';
            else
                time[1] = '9';
        }
        // minute tens
        if (time[3] == '?')
            time[3] = '5';
        // minute units
        if (time[4] == '?')
            time[4] = '9';
        return time;
    }
};
```

## Java

```java
class Solution {
    public String maximumTime(String time) {
        char[] t = time.toCharArray();
        // Hour tens
        if (t[0] == '?') {
            if (t[1] == '?' || t[1] <= '3') {
                t[0] = '2';
            } else {
                t[0] = '1';
            }
        }
        // Hour units
        if (t[1] == '?') {
            if (t[0] == '2') {
                t[1] = '3';
            } else {
                t[1] = '9';
            }
        }
        // Minute tens
        if (t[3] == '?') {
            t[3] = '5';
        }
        // Minute units
        if (t[4] == '?') {
            t[4] = '9';
        }
        return new String(t);
    }
}
```

## Python

```python
class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        t = list(time)
        # hour tens
        if t[0] == '?':
            if t[1] != '?' and t[1] > '3':
                t[0] = '1'
            else:
                t[0] = '2'
        # hour units
        if t[1] == '?':
            if t[0] == '2':
                t[1] = '3'
            else:
                t[1] = '9'
        # minute tens
        if t[3] == '?':
            t[3] = '5'
        # minute units
        if t[4] == '?':
            t[4] = '9'
        return "".join(t)
```

## Python3

```python
class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        # Hour tens
        if t[0] == '?':
            if t[1] != '?' and t[1] > '3':
                t[0] = '1'
            else:
                t[0] = '2'
        # Hour units
        if t[1] == '?':
            if t[0] == '2':
                t[1] = '3'
            else:
                t[1] = '9'
        # Minute tens
        if t[3] == '?':
            t[3] = '5'
        # Minute units
        if t[4] == '?':
            t[4] = '9'
        return "".join(t)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* maximumTime(char* time) {
    char *res = (char *)malloc(6 * sizeof(char));
    strcpy(res, time);
    
    if (res[0] == '?') {
        if (res[1] != '?' && res[1] > '3')
            res[0] = '1';
        else
            res[0] = '2';
    }
    if (res[1] == '?') {
        if (res[0] == '2')
            res[1] = '3';
        else
            res[1] = '9';
    }
    if (res[3] == '?')
        res[3] = '5';
    if (res[4] == '?')
        res[4] = '9';
    
    res[5] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string MaximumTime(string time) {
        char[] t = time.ToCharArray();

        // Hour tens
        if (t[0] == '?') {
            if (t[1] != '?' && t[1] > '3')
                t[0] = '1';
            else
                t[0] = '2';
        }

        // Hour units
        if (t[1] == '?') {
            if (t[0] == '2')
                t[1] = '3';
            else
                t[1] = '9';
        }

        // Minute tens
        if (t[3] == '?')
            t[3] = '5';

        // Minute units
        if (t[4] == '?')
            t[4] = '9';

        return new string(t);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} time
 * @return {string}
 */
var maximumTime = function(time) {
    const t = time.split('');
    // Hour tens
    if (t[0] === '?') {
        if (t[1] !== '?' && t[1] > '3') {
            t[0] = '1';
        } else {
            t[0] = '2';
        }
    }
    // Hour ones
    if (t[1] === '?') {
        t[1] = (t[0] === '2') ? '3' : '9';
    }
    // Minute tens
    if (t[3] === '?') t[3] = '5';
    // Minute ones
    if (t[4] === '?') t[4] = '9';
    return t.join('');
};
```

## Typescript

```typescript
function maximumTime(time: string): string {
    const arr = time.split('');
    
    // Hour tens (index 0)
    if (arr[0] === '?') {
        if (arr[1] === '?' || arr[1] <= '3') {
            arr[0] = '2';
        } else {
            arr[0] = '1';
        }
    }
    
    // Hour units (index 1)
    if (arr[1] === '?') {
        if (arr[0] === '2') {
            arr[1] = '3';
        } else {
            arr[1] = '9';
        }
    }
    
    // Minute tens (index 3)
    if (arr[3] === '?') {
        arr[3] = '5';
    }
    
    // Minute units (index 4)
    if (arr[4] === '?') {
        arr[4] = '9';
    }
    
    return arr.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $time
     * @return String
     */
    function maximumTime($time) {
        $c = str_split($time);
        // hour tens
        if ($c[0] === '?') {
            if ($c[1] !== '?' && $c[1] > '3') {
                $c[0] = '1';
            } else {
                $c[0] = '2';
            }
        }
        // hour units
        if ($c[1] === '?') {
            $c[1] = ($c[0] === '2') ? '3' : '9';
        }
        // minute tens
        if ($c[3] === '?') {
            $c[3] = '5';
        }
        // minute units
        if ($c[4] === '?') {
            $c[4] = '9';
        }
        return implode('', $c);
    }
}
```

## Swift

```swift
class Solution {
    func maximumTime(_ time: String) -> String {
        var chars = Array(time)
        
        // Hour tens
        if chars[0] == "?" {
            if chars[1] != "?" {
                if chars[1] <= "3" {
                    chars[0] = "2"
                } else {
                    chars[0] = "1"
                }
            } else {
                chars[0] = "2"
            }
        }
        
        // Hour units
        if chars[1] == "?" {
            if chars[0] == "2" {
                chars[1] = "3"
            } else {
                chars[1] = "9"
            }
        }
        
        // Minute tens
        if chars[3] == "?" {
            chars[3] = "5"
        }
        
        // Minute units
        if chars[4] == "?" {
            chars[4] = "9"
        }
        
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTime(time: String): String {
        val ch = time.toCharArray()
        if (ch[0] == '?') {
            ch[0] = if (ch[1] != '?' && ch[1] > '3') '1' else '2'
        }
        if (ch[1] == '?') {
            ch[1] = if (ch[0] == '2') '3' else '9'
        }
        if (ch[3] == '?') {
            ch[3] = '5'
        }
        if (ch[4] == '?') {
            ch[4] = '9'
        }
        return String(ch)
    }
}
```

## Dart

```dart
class Solution {
  String maximumTime(String time) {
    List<String> ch = time.split('');
    // Hour tens
    if (ch[0] == '?') {
      if (ch[1] == '?') {
        ch[0] = '2';
      } else {
        // If the known hour units is 0-3, we can use '2' as tens digit.
        if (ch[1].compareTo('4') < 0) { // <= '3'
          ch[0] = '2';
        } else {
          ch[0] = '1';
        }
      }
    }
    // Hour units
    if (ch[1] == '?') {
      ch[1] = (ch[0] == '2') ? '3' : '9';
    }
    // Minute tens
    if (ch[3] == '?') {
      ch[3] = '5';
    }
    // Minute units
    if (ch[4] == '?') {
      ch[4] = '9';
    }
    return ch.join();
  }
}
```

## Golang

```go
func maximumTime(time string) string {
    b := []byte(time)
    // Hour tens
    if b[0] == '?' {
        if b[1] != '?' && b[1] > '3' {
            b[0] = '1'
        } else {
            b[0] = '2'
        }
    }
    // Hour units
    if b[1] == '?' {
        if b[0] == '2' {
            b[1] = '3'
        } else {
            b[1] = '9'
        }
    }
    // Minute tens
    if b[3] == '?' {
        b[3] = '5'
    }
    // Minute units
    if b[4] == '?' {
        b[4] = '9'
    }
    return string(b)
}
```

## Ruby

```ruby
def maximum_time(time)
  chars = time.chars
  if chars[0] == '?'
    if chars[1] != '?' && chars[1] > '3'
      chars[0] = '1'
    else
      chars[0] = '2'
    end
  end
  if chars[1] == '?'
    chars[1] = (chars[0] == '2') ? '3' : '9'
  end
  chars[3] = '5' if chars[3] == '?'
  chars[4] = '9' if chars[4] == '?'
  chars.join
end
```

## Scala

```scala
object Solution {
    def maximumTime(time: String): String = {
        val arr = time.toCharArray
        // Hour tens position 0
        if (arr(0) == '?') {
            if (arr(1) == '?') {
                arr(0) = '2'
            } else {
                if (arr(1) <= '3') arr(0) = '2' else arr(0) = '1'
            }
        }
        // Hour units position 1
        if (arr(1) == '?') {
            if (arr(0) == '2') arr(1) = '3' else arr(1) = '9'
        }
        // Minute tens position 3
        if (arr(3) == '?') arr(3) = '5'
        // Minute units position 4
        if (arr(4) == '?') arr(4) = '9'
        new String(arr)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_time(time: String) -> String {
        let mut c: Vec<char> = time.chars().collect();
        // hour tens
        if c[0] == '?' {
            if c[1] == '?' || c[1] <= '3' {
                c[0] = '2';
            } else {
                c[0] = '1';
            }
        }
        // hour ones
        if c[1] == '?' {
            if c[0] == '2' {
                c[1] = '3';
            } else {
                c[1] = '9';
            }
        }
        // minute tens
        if c[3] == '?' {
            c[3] = '5';
        }
        // minute ones
        if c[4] == '?' {
            c[4] = '9';
        }
        c.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (maximum-time time)
  (-> string? string?)
  (let* ((c0 (string-ref time 0))
         (c1 (string-ref time 1))
         (c3 (string-ref time 3))
         (c4 (string-ref time 4))
         (d0 (if (char=? c0 #\?) #\2 c0))
         (d1 (cond [(char=? c1 #\?)
                    (if (char=? d0 #\2) #\3 #\9)]
                   [else c1]))
         (d3 (if (char=? c3 #\?) #\5 c3))
         (d4 (if (char=? c4 #\?) #\9 c4)))
    (string d0 d1 #\: d3 d4)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_time/1]).

-spec maximum_time(Time :: unicode:unicode_binary()) -> unicode:unicode_binary().
maximum_time(Time) ->
    Pattern = binary_to_list(Time),
    {Hour, Minute} = find_time(Pattern, 23),
    ResultStr = format2(Hour) ++ ":" ++ format2(Minute),
    list_to_binary(ResultStr).

%% Find the latest valid hour starting from H downwards
find_time(_Pattern, -1) ->
    erlang:error(no_valid_time);
find_time(Pattern, H) ->
    case find_minute_for_hour(Pattern, H, 59) of
        {ok, M} -> {H, M};
        no      -> find_time(Pattern, H - 1)
    end.

%% Find the latest valid minute for a given hour
find_minute_for_hour(_Pattern, _Hour, -1) ->
    no;
find_minute_for_hour(Pattern, Hour, Minute) ->
    HourStr = format2(Hour),
    MinuteStr = format2(Minute),
    Candidate = HourStr ++ ":" ++ MinuteStr,
    case matches(Pattern, Candidate) of
        true -> {ok, Minute};
        false -> find_minute_for_hour(Pattern, Hour, Minute - 1)
    end.

%% Check if candidate string fits the pattern (allowing '?' in pattern)
matches([], []) ->
    true;
matches([P|Ps], [C|Cs]) when P =:= $? ->
    matches(Ps, Cs);
matches([P|Ps], [C|Cs]) ->
    (P =:= C) andalso matches(Ps, Cs).

%% Format integer as two-digit zero-padded string
format2(N) ->
    lists:flatten(io_lib:format("~2..0B", [N])).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_time(time :: String.t) :: String.t
  def maximum_time(time) do
    [h1, h2, ":", m1, m2] = String.codepoints(time)

    h1 =
      if h1 == "?" do
        cond do
          h2 == "?" -> "2"
          h2 in ["0", "1", "2", "3"] -> "2"
          true -> "1"
        end
      else
        h1
      end

    h2 =
      if h2 == "?" do
        if h1 == "2", do: "3", else: "9"
      else
        h2
      end

    m1 = if m1 == "?", do: "5", else: m1
    m2 = if m2 == "?", do: "9", else: m2

    Enum.join([h1, h2, ":", m1, m2])
  end
end
```
