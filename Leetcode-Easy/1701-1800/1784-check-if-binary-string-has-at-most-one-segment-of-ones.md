# 1784. Check if Binary String Has at Most One Segment of Ones

## Cpp

```cpp
class Solution {
public:
    bool checkOnesSegment(string s) {
        int segments = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] == '1' && (i == 0 || s[i-1] == '0')) {
                ++segments;
                if (segments > 1) return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkOnesSegment(String s) {
        boolean zeroSeen = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '0') {
                zeroSeen = true;
            } else { // c == '1'
                if (zeroSeen) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        zero_seen = False
        for ch in s:
            if ch == '0':
                zero_seen = True
            elif zero_seen and ch == '1':
                return False
        return True
```

## Python3

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segments = 0
        prev = '0'
        for ch in s:
            if ch == '1' and prev != '1':
                segments += 1
                if segments > 1:
                    return False
            prev = ch
        return True
```

## C

```c
#include <stdbool.h>

bool checkOnesSegment(char* s) {
    int segments = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '1' && (i == 0 || s[i - 1] == '0')) {
            if (++segments > 1)
                return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckOnesSegment(string s) {
        bool zeroSeen = false;
        foreach (char c in s) {
            if (c == '0') {
                zeroSeen = true;
            } else { // c == '1'
                if (zeroSeen) return false;
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkOnesSegment = function(s) {
    let segments = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1' && (i === 0 || s[i - 1] === '0')) {
            segments++;
            if (segments > 1) return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkOnesSegment(s: string): boolean {
    const segments = s.split('0').filter(segment => segment.length > 0);
    return segments.length <= 1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkOnesSegment($s) {
        $len = strlen($s);
        $segments = 0;
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '1' && ($i == 0 || $s[$i - 1] === '0')) {
                $segments++;
                if ($segments > 1) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkOnesSegment(_ s: String) -> Bool {
        var segments = 0
        var previous: Character = "0"
        for ch in s {
            if ch == "1" && previous != "1" {
                segments += 1
                if segments > 1 { return false }
            }
            previous = ch
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkOnesSegment(s: String): Boolean {
        var zeroSeen = false
        for (ch in s) {
            if (ch == '0') {
                zeroSeen = true
            } else { // ch == '1'
                if (zeroSeen) return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkOnesSegment(String s) {
    int segments = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '1') {
        segments++;
        while (i + 1 < s.length && s[i + 1] == '1') {
          i++;
        }
        if (segments > 1) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func checkOnesSegment(s string) bool {
    seen := false
    for i := 0; i < len(s); i++ {
        if s[i] == '1' {
            if !seen {
                // first segment of ones starts here
                seen = true
                // skip the rest of this contiguous segment
                for i+1 < len(s) && s[i+1] == '1' {
                    i++
                }
            } else {
                // a second segment of ones encountered
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_ones_segment(s)
  s.split('0').reject(&:empty?).size <= 1
end
```

## Scala

```scala
object Solution {
    def checkOnesSegment(s: String): Boolean = {
        val firstZero = s.indexOf('0')
        if (firstZero == -1) true
        else !s.substring(firstZero).contains('1')
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        let mut groups = 0;
        let mut in_one = false;
        for ch in s.bytes() {
            if ch == b'1' {
                if !in_one {
                    groups += 1;
                    if groups > 1 {
                        return false;
                    }
                    in_one = true;
                }
            } else {
                in_one = false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-ones-segment s)
  (-> string? boolean?)
  (let loop ((i 0)
             (in-seg #f)
             (segments 0))
    (if (= i (string-length s))
        (<= segments 1)
        (let ((c (string-ref s i)))
          (cond
            [(char=? c #\1)
             (if in-seg
                 (loop (+ i 1) #t segments)
                 (loop (+ i 1) #t (+ segments 1)))]
            [else ; c is #\0
             (loop (+ i 1) #f segments)])))))
```

## Erlang

```erlang
-module(solution).
-export([check_ones_segment/1]).

-spec check_ones_segment(S :: unicode:unicode_binary()) -> boolean().
check_ones_segment(<<First, Rest/binary>>) ->
    count_segments(Rest, First, 1).

count_segments(<<>>, _Prev, Count) ->
    Count =< 1;
count_segments(<<C, Rest/binary>>, Prev, Count) ->
    NewCount = case {Prev, C} of
        {$0, $1} -> Count + 1;
        _ -> Count
    end,
    if NewCount > 1 ->
            false;
       true ->
            count_segments(Rest, C, NewCount)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_ones_segment(s :: String.t()) :: boolean()
  def check_ones_segment(s) do
    {segments, _in_one} =
      String.graphemes(s)
      |> Enum.reduce({0, false}, fn ch, {cnt, in_one} ->
        case {ch, in_one} do
          {"1", false} -> {cnt + 1, true}
          {"1", true} -> {cnt, true}
          {"0", _} -> {cnt, false}
        end
      end)

    segments <= 1
  end
end
```
