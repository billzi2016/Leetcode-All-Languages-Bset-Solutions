# 2042. Check if Numbers Are Ascending in a Sentence

## Cpp

```cpp
class Solution {
public:
    bool areNumbersAscending(string s) {
        stringstream ss(s);
        string token;
        int prev = -1;
        while (ss >> token) {
            if (!token.empty() && isdigit(token[0])) {
                int cur = stoi(token);
                if (cur <= prev) return false;
                prev = cur;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean areNumbersAscending(String s) {
        String[] tokens = s.split(" ");
        int prev = -1;
        for (String token : tokens) {
            if (!token.isEmpty() && Character.isDigit(token.charAt(0))) {
                int cur = Integer.parseInt(token);
                if (cur <= prev) {
                    return false;
                }
                prev = cur;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = -1
        for token in s.split():
            if token[0].isdigit():
                cur = int(token)
                if cur <= prev:
                    return False
                prev = cur
        return True
```

## Python3

```python
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for token in s.split():
            if token.isdigit():
                cur = int(token)
                if cur <= prev:
                    return False
                prev = cur
        return True
```

## C

```c
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool areNumbersAscending(char* s) {
    int prev = -1;
    char *token = strtok(s, " ");
    while (token) {
        if (isdigit((unsigned char)token[0])) {
            int num = 0;
            for (int i = 0; token[i]; ++i) {
                num = num * 10 + (token[i] - '0');
            }
            if (num <= prev) return false;
            prev = num;
        }
        token = strtok(NULL, " ");
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool AreNumbersAscending(string s)
    {
        var tokens = s.Split(' ');
        int prev = -1;
        foreach (var token in tokens)
        {
            if (char.IsDigit(token[0]))
            {
                int cur = int.Parse(token);
                if (cur <= prev) return false;
                prev = cur;
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
var areNumbersAscending = function(s) {
    const tokens = s.split(' ');
    let prev = -1;
    for (const token of tokens) {
        // Check if the first character is a digit; all numeric tokens consist only of digits.
        if (token[0] >= '0' && token[0] <= '9') {
            const num = parseInt(token, 10);
            if (num <= prev) return false;
            prev = num;
        }
    }
    return true;
};
```

## Typescript

```typescript
function areNumbersAscending(s: string): boolean {
    const tokens = s.split(' ');
    let prev = -1;
    for (const token of tokens) {
        // Check if the token is a number (all characters are digits)
        if (token.length > 0 && token[0] >= '0' && token[0] <= '9') {
            const num = parseInt(token, 10);
            if (num <= prev) return false;
            prev = num;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function areNumbersAscending($s) {
        $tokens = explode(' ', $s);
        $prev = -1;
        foreach ($tokens as $token) {
            if (ctype_digit($token)) {
                $num = intval($token);
                if ($num <= $prev) {
                    return false;
                }
                $prev = $num;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func areNumbersAscending(_ s: String) -> Bool {
        var prev = -1
        for token in s.split(separator: " ") {
            if let first = token.first, first.isNumber {
                if let num = Int(token) {
                    if num <= prev { return false }
                    prev = num
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun areNumbersAscending(s: String): Boolean {
        var prev = -1
        for (token in s.split(' ')) {
            if (token[0].isDigit()) {
                val cur = token.toInt()
                if (cur <= prev) return false
                prev = cur
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool areNumbersAscending(String s) {
    int prev = -1;
    for (var token in s.split(' ')) {
      if (token.isNotEmpty && token.codeUnitAt(0) >= 48 && token.codeUnitAt(0) <= 57) {
        int cur = int.parse(token);
        if (cur <= prev) return false;
        prev = cur;
      }
    }
    return true;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func areNumbersAscending(s string) bool {
	tokens := strings.Split(s, " ")
	prev := -1
	for _, t := range tokens {
		if len(t) == 0 {
			continue
		}
		if t[0] >= '0' && t[0] <= '9' {
			num, _ := strconv.Atoi(t)
			if num <= prev {
				return false
			}
			prev = num
		}
	}
	return true
}
```

## Ruby

```ruby
def are_numbers_ascending(s)
  prev = -1
  s.split.each do |token|
    if token[0] >= '0' && token[0] <= '9'
      num = token.to_i
      return false if num <= prev
      prev = num
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def areNumbersAscending(s: String): Boolean = {
        var prev = -1
        for (token <- s.split(" ")) {
            if (token.nonEmpty && token.head.isDigit) {
                val cur = token.toInt
                if (cur <= prev) return false
                prev = cur
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn are_numbers_ascending(s: String) -> bool {
        let mut prev = -1i32;
        for token in s.split_whitespace() {
            if token.as_bytes()[0].is_ascii_digit() {
                // Token is a number according to problem constraints
                let cur: i32 = token.parse().unwrap();
                if cur <= prev {
                    return false;
                }
                prev = cur;
            }
        }
        true
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (are-numbers-ascending s)
  (-> string? boolean?)
  (let ([tokens (string-split s)])
    (let loop ((prev -1) (ts tokens))
      (cond [(empty? ts) #true]
            [else
             (define t (first ts))
             (define n (string->number t))
             (if n
                 (if (> n prev)
                     (loop n (rest ts))
                     #false)
                 (loop prev (rest ts)))]))))
```

## Erlang

```erlang
-spec are_numbers_ascending(S :: unicode:unicode_binary()) -> boolean().
are_numbers_ascending(S) ->
    Tokens = string:tokens(S, <<" ">>),
    check_tokens(Tokens, 0).

check_tokens([], _Prev) -> 
    true;
check_tokens([H|T], Prev) ->
    case is_number_token(H) of
        true ->
            {ok, N} = string:to_integer(H),
            if N > Prev -> 
                    check_tokens(T, N);
               true -> 
                    false
            end;
        false ->
            check_tokens(T, Prev)
    end.

is_number_token(Token) when is_binary(Token) ->
    case Token of
        <<C,_/binary>> when C >= $0, C =< $9 -> true;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec are_numbers_ascending(s :: String.t) :: boolean
  def are_numbers_ascending(s) do
    s
    |> String.split(" ")
    |> Enum.reduce_while({-1, true}, fn token, {prev, _} ->
      if String.match?(token, ~r/^\d+$/) do
        num = String.to_integer(token)

        if num > prev do
          {:cont, {num, true}}
        else
          {:halt, {prev, false}}
        end
      else
        {:cont, {prev, true}}
      end
    end)
    |> elem(1)
  end
end
```
