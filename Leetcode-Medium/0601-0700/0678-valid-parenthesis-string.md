# 0678. Valid Parenthesis String

## Cpp

```cpp
class Solution {
public:
    bool checkValidString(string s) {
        int low = 0, high = 0;
        for (char c : s) {
            if (c == '(') {
                ++low;
                ++high;
            } else if (c == ')') {
                --low;
                --high;
            } else { // '*'
                --low;      // treat as ')'
                ++high;     // treat as '('
            }
            if (high < 0) return false;   // too many ')'
            low = max(low, 0);             // cannot be negative
        }
        return low == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean checkValidString(String s) {
        int low = 0, high = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                low++;
                high++;
            } else if (c == ')') {
                low--;
                high--;
            } else { // '*'
                low--;      // treat as ')'
                high++;     // treat as '('
            }
            if (high < 0) return false;
            if (low < 0) low = 0; // we can treat some '*' as '(' to balance
        }
        return low == 0;
    }
}
```

## Python

```python
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1   # treat as ')'
                hi += 1   # treat as '('
            if hi < 0:
                return False
            if lo < 0:
                lo = 0
        return True
```

## Python3

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            if lo < 0:
                lo = 0
        return lo == 0
```

## C

```c
#include <stdbool.h>

bool checkValidString(char* s) {
    int low = 0, high = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        char c = s[i];
        if (c == '(') {
            low++;
            high++;
        } else if (c == ')') {
            low--;
            high--;
        } else { // '*'
            low--;   // treat as ')'
            high++;  // treat as '('
        }
        if (high < 0) return false;
        if (low < 0) low = 0;
    }
    return low == 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckValidString(string s) {
        int low = 0, high = 0;
        foreach (char c in s) {
            if (c == '(') {
                low++;
                high++;
            } else if (c == ')') {
                low--;
                high--;
            } else { // '*'
                low--;   // treat as ')'
                high++;  // treat as '('
            }
            if (high < 0) return false;
            if (low < 0) low = 0;
        }
        return low == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    let lo = 0, hi = 0; // lo: minimum possible '(' count, hi: maximum possible '(' count
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === '(') {
            lo++;
            hi++;
        } else if (ch === ')') {
            lo--;
            hi--;
        } else { // '*'
            lo--;      // treat as ')'
            hi++;      // treat as '('
        }
        if (hi < 0) return false;          // too many ')'
        if (lo < 0) lo = 0;                // we can ignore extra ')' by treating '*' as empty
    }
    return lo === 0;
};
```

## Typescript

```typescript
function checkValidString(s: string): boolean {
    let low = 0, high = 0;
    for (const ch of s) {
        if (ch === '(') {
            low++;
            high++;
        } else if (ch === ')') {
            low--;
            high--;
        } else { // '*'
            low--;      // treat as ')'
            high++;     // treat as '('
        }
        if (high < 0) return false;
        if (low < 0) low = 0;
    }
    return low === 0;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function checkValidString($s) {
        $low = 0;   // minimum possible open '(' count
        $high = 0;  // maximum possible open '(' count
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === '(') {
                $low++;
                $high++;
            } elseif ($c === ')') {
                $low--;
                $high--;
            } else { // '*'
                $low--;   // treat as ')'
                $high++;  // treat as '('
            }
            if ($high < 0) {
                return false;
            }
            if ($low < 0) {
                $low = 0;
            }
        }
        return $low === 0;
    }
}
```

## Swift

```swift
class Solution {
    func checkValidString(_ s: String) -> Bool {
        var low = 0
        var high = 0
        for ch in s {
            if ch == "(" {
                low += 1
                high += 1
            } else if ch == ")" {
                low = max(low - 1, 0)
                high -= 1
            } else { // '*'
                low = max(low - 1, 0)
                high += 1
            }
            if high < 0 {
                return false
            }
        }
        return low == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkValidString(s: String): Boolean {
        var minOpen = 0
        var maxOpen = 0
        for (ch in s) {
            when (ch) {
                '(' -> {
                    minOpen++
                    maxOpen++
                }
                ')' -> {
                    if (minOpen > 0) minOpen--
                    maxOpen--
                }
                '*' -> {
                    if (minOpen > 0) minOpen--
                    maxOpen++
                }
            }
            if (maxOpen < 0) return false
        }
        return minOpen == 0
    }
}
```

## Dart

```dart
class Solution {
  bool checkValidString(String s) {
    int low = 0, high = 0;
    for (int i = 0; i < s.length; i++) {
      final ch = s[i];
      if (ch == '(') {
        low++;
        high++;
      } else if (ch == ')') {
        low--;
        high--;
      } else { // '*'
        low--;       // treat as ')'
        high++;      // treat as '('
      }
      if (high < 0) return false;
      if (low < 0) low = 0;
    }
    return low == 0;
  }
}
```

## Golang

```go
func checkValidString(s string) bool {
	low, high := 0, 0
	for _, ch := range s {
		switch ch {
		case '(':
			low++
			high++
		case ')':
			low--
			high--
		case '*':
			low--   // treat as ')'
			high++ // treat as '('
		}
		if high < 0 {
			return false
		}
		if low < 0 {
			low = 0
		}
	}
	return low == 0
}
```

## Ruby

```ruby
def check_valid_string(s)
  lo = 0
  hi = 0
  s.each_char do |c|
    case c
    when '('
      lo += 1
      hi += 1
    when ')'
      lo -= 1
      hi -= 1
    else # '*'
      lo -= 1
      hi += 1
    end
    lo = 0 if lo < 0
    return false if hi < 0
  end
  lo == 0
end
```

## Scala

```scala
object Solution {
    def checkValidString(s: String): Boolean = {
        var lo = 0
        var hi = 0
        for (c <- s) {
            c match {
                case '(' => 
                    lo += 1
                    hi += 1
                case ')' => 
                    lo -= 1
                    hi -= 1
                case '*' => 
                    lo -= 1
                    hi += 1
                case _ => // ignore
            }
            if (hi < 0) return false
            if (lo < 0) lo = 0
        }
        lo == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut lo = 0i32; // minimum possible open '(' count
        let mut hi = 0i32; // maximum possible open '(' count

        for ch in s.chars() {
            match ch {
                '(' => {
                    lo += 1;
                    hi += 1;
                }
                ')' => {
                    if lo > 0 {
                        lo -= 1;
                    }
                    hi -= 1;
                }
                '*' => {
                    // '*' can be '(', ')' or empty
                    if lo > 0 {
                        lo -= 1; // treat as ')'
                    }
                    hi += 1; // treat as '('
                }
                _ => {}
            }
            if hi < 0 {
                return false;
            }
        }

        lo == 0
    }
}
```

## Racket

```racket
(define/contract (check-valid-string s)
  (-> string? boolean?)
  (let loop ((i 0) (lo 0) (hi 0))
    (if (= i (string-length s))
        (= lo 0)
        (let* ((c (string-ref s i))
               (new-lo (cond [(char=? c #\() (+ lo 1)]
                             [(char=? c #\)) (- lo 1)]
                             [else (- lo 1)]))
               (new-hi (cond [(char=? c #\() (+ hi 1)]
                             [(char=? c #\)) (- hi 1)]
                             [else (+ hi 1)]))
               (adj-lo (max new-lo 0)))
          (if (< new-hi 0)
              #false
              (loop (+ i 1) adj-lo new-hi))))))
```

## Erlang

```erlang
-module(solution).
-export([check_valid_string/1]).

-spec check_valid_string(S :: unicode:unicode_binary()) -> boolean().
check_valid_string(S) ->
    List = binary_to_list(S),
    case process(List, 0, [], []) of
        {_, _, true} -> true;
        _ -> false
    end.

process([], _Idx, Open, Star) ->
    Bool = match_remaining(Open, Star),
    {Open, Star, Bool};
process([C|Rest], Idx, Open, Star) ->
    case C of
        $( ->
            process(Rest, Idx + 1, [Idx | Open], Star);
        $* ->
            process(Rest, Idx + 1, Open, [Idx | Star]);
        $) ->
            case Open of
                [_|OpenRest] ->
                    process(Rest, Idx + 1, OpenRest, Star);
                [] ->
                    case Star of
                        [_|StarRest] ->
                            process(Rest, Idx + 1, Open, StarRest);
                        [] ->
                            {[], [], false}
                    end
            end;
        _ ->
            process(Rest, Idx + 1, Open, Star)
    end.

match_remaining([], _) -> true;
match_remaining(_, []) -> false;
match_remaining([O|Os], [S|Ss]) ->
    if O < S ->
            match_remaining(Os, Ss);
       true ->
            false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_valid_string(s :: String.t()) :: boolean()
  def check_valid_string(s) do
    case String.graphemes(s) |> Enum.reduce_while({0, 0}, fn ch, {min_o, max_o} ->
           case ch do
             "(" ->
               {:cont, {min_o + 1, max_o + 1}}

             ")" ->
               new_min = max(min_o - 1, 0)
               new_max = max_o - 1

               if new_max < 0,
                 do: {:halt, :invalid},
                 else: {:cont, {new_min, new_max}}

             "*" ->
               new_min = max(min_o - 1, 0)
               new_max = max_o + 1
               {:cont, {new_min, new_max}}
           end
         end) do
      :invalid -> false
      {min_o, _max_o} -> min_o == 0
    end
  end
end
```
