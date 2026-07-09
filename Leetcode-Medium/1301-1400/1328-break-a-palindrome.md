# 1328. Break a Palindrome

## Cpp

```cpp
class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.size();
        if (n == 1) return "";
        for (int i = 0; i < n / 2; ++i) {
            if (palindrome[i] != 'a') {
                palindrome[i] = 'a';
                return palindrome;
            }
        }
        palindrome[n - 1] = 'b';
        return palindrome;
    }
};
```

## Java

```java
class Solution {
    public String breakPalindrome(String palindrome) {
        int n = palindrome.length();
        if (n == 1) return "";
        char[] chars = palindrome.toCharArray();
        for (int i = 0; i < n / 2; i++) {
            if (chars[i] != 'a') {
                chars[i] = 'a';
                return new String(chars);
            }
        }
        chars[n - 1] = 'b';
        return new String(chars);
    }
}
```

## Python

```python
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        n = len(palindrome)
        if n == 1:
            return ""
        # Convert to list for mutability
        chars = list(palindrome)
        # Find first non-'a' in the first half and replace with 'a'
        for i in range(n // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return "".join(chars)
        # All characters in first half are 'a', change last character to 'b'
        chars[-1] = 'b'
        return "".join(chars)
```

## Python3

```python
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        # try to replace first non-'a' in the left half with 'a'
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        # all characters in the left half are 'a', change the last character to 'b'
        return palindrome[:-1] + 'b'
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* breakPalindrome(char* palindrome) {
    size_t n = strlen(palindrome);
    char *res = (char*)malloc(n + 1);
    if (!res) return NULL;
    strcpy(res, palindrome);
    
    if (n == 1) {
        res[0] = '\0';
        return res;
    }
    
    for (size_t i = 0; i < n / 2; ++i) {
        if (res[i] != 'a') {
            res[i] = 'a';
            return res;
        }
    }
    
    // All characters in the first half are 'a'
    res[n - 1] = 'b';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string BreakPalindrome(string palindrome) {
        int n = palindrome.Length;
        if (n == 1) return "";
        char[] chars = palindrome.ToCharArray();
        for (int i = 0; i < n / 2; i++) {
            if (chars[i] != 'a') {
                chars[i] = 'a';
                return new string(chars);
            }
        }
        chars[n - 1] = 'b';
        return new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    const n = palindrome.length;
    if (n === 1) return "";
    
    const chars = palindrome.split('');
    for (let i = 0; i < Math.floor(n / 2); i++) {
        if (chars[i] !== 'a') {
            chars[i] = 'a';
            return chars.join('');
        }
    }
    // All first half are 'a', change the last character to 'b'
    chars[n - 1] = 'b';
    return chars.join('');
};
```

## Typescript

```typescript
function breakPalindrome(palindrome: string): string {
    const n = palindrome.length;
    if (n === 1) return "";
    
    const chars = palindrome.split('');
    for (let i = 0; i < Math.floor(n / 2); i++) {
        if (chars[i] !== 'a') {
            chars[i] = 'a';
            return chars.join('');
        }
    }
    // All characters in the first half are 'a'
    chars[n - 1] = 'b';
    return chars.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $palindrome
     * @return String
     */
    function breakPalindrome($palindrome) {
        $n = strlen($palindrome);
        if ($n == 1) {
            return "";
        }
        $chars = str_split($palindrome);
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            if ($chars[$i] !== 'a') {
                $chars[$i] = 'a';
                return implode('', $chars);
            }
        }
        // All characters in the first half are 'a'
        $chars[$n - 1] = 'b';
        return implode('', $chars);
    }
}
```

## Swift

```swift
class Solution {
    func breakPalindrome(_ palindrome: String) -> String {
        let n = palindrome.count
        if n == 1 { return "" }
        var chars = Array(palindrome)
        for i in 0..<(n / 2) {
            if chars[i] != "a" {
                chars[i] = "a"
                return String(chars)
            }
        }
        // All characters are 'a'
        chars[n - 1] = "b"
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun breakPalindrome(palindrome: String): String {
        val n = palindrome.length
        if (n == 1) return ""
        val chars = palindrome.toCharArray()
        for (i in 0 until n / 2) {
            if (chars[i] != 'a') {
                chars[i] = 'a'
                return String(chars)
            }
        }
        chars[n - 1] = 'b'
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String breakPalindrome(String palindrome) {
    int n = palindrome.length;
    if (n == 1) return "";
    List<int> chars = palindrome.codeUnits;
    for (int i = 0; i < n ~/ 2; ++i) {
      if (chars[i] != 97) { // 'a'
        chars[i] = 97;
        return String.fromCharCodes(chars);
      }
    }
    chars[n - 1] = 98; // 'b'
    return String.fromCharCodes(chars);
  }
}
```

## Golang

```go
func breakPalindrome(palindrome string) string {
    n := len(palindrome)
    if n == 1 {
        return ""
    }
    b := []byte(palindrome)
    for i := 0; i < n/2; i++ {
        if b[i] != 'a' {
            b[i] = 'a'
            return string(b)
        }
    }
    b[n-1] = 'b'
    return string(b)
}
```

## Ruby

```ruby
def break_palindrome(palindrome)
  n = palindrome.length
  return "" if n == 1

  chars = palindrome.chars
  (0...(n / 2)).each do |i|
    if chars[i] != 'a'
      chars[i] = 'a'
      return chars.join
    end
  end

  chars[-1] = 'b'
  chars.join
end
```

## Scala

```scala
object Solution {
    def breakPalindrome(palindrome: String): String = {
        val n = palindrome.length
        if (n == 1) return ""
        val sb = new StringBuilder(palindrome)
        for (i <- 0 until n / 2) {
            if (sb.charAt(i) != 'a') {
                sb.setCharAt(i, 'a')
                return sb.toString()
            }
        }
        sb.setCharAt(n - 1, 'b')
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn break_palindrome(palindrome: String) -> String {
        let n = palindrome.len();
        if n == 1 {
            return "".to_string();
        }
        let mut chars: Vec<char> = palindrome.chars().collect();
        for i in 0..n / 2 {
            if chars[i] != 'a' {
                chars[i] = 'a';
                return chars.iter().collect();
            }
        }
        // all characters in the first half are 'a'
        chars[n - 1] = 'b';
        chars.iter().collect()
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (break-palindrome palindrome)
  (-> string? string?)
  (let ([n (string-length palindrome)])
    (if (= n 1)
        ""
        (let* ([vec (list->vector (string->list palindrome))])
          (let loop ([i 0] [changed #f])
            (cond
              [(>= i (quotient n 2))
               (if changed
                   (vector->string vec)
                   (begin
                     (vector-set! vec (- n 1) #\b)
                     (vector->string vec)))]
              [else
               (let ([c (vector-ref vec i)])
                 (if (char=? c #\a)
                     (loop (+ i 1) changed)
                     (begin
                       (vector-set! vec i #\a)
                       (vector->string vec))))]))))))
```

## Erlang

```erlang
-module(solution).
-export([break_palindrome/1]).

-spec break_palindrome(Palindrome :: unicode:unicode_binary()) -> unicode:unicode_binary().
break_palindrome(Palindrome) ->
    Len = byte_size(Palindrome),
    case Len of
        1 -> <<>>;
        _ ->
            List = binary_to_list(Palindrome),
            Half = Len div 2,
            NewList = replace_first_non_a(List, Half),
            list_to_binary(NewList)
    end.

replace_first_non_a(Lst, Half) ->
    replace_first_non_a(Lst, 0, Half).

replace_first_non_a([], _Idx, _Half) ->
    [];
replace_first_non_a([H|T], Idx, Half) when Idx < Half ->
    case H of
        $a -> [H | replace_first_non_a(T, Idx + 1, Half)];
        _  -> [$a | T]
    end;
replace_first_non_a(Lst, _Idx, _Half) ->
    replace_last_char_with_b(Lst).

replace_last_char_with_b(L) ->
    Rev = lists:reverse(L),
    case Rev of
        [_|Rest] -> lists:reverse([ $b | Rest ]);
        [] -> []
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec break_palindrome(palindrome :: String.t) :: String.t
  def break_palindrome(palindrome) do
    len = String.length(palindrome)

    if len == 1 do
      ""
    else
      chars = String.graphemes(palindrome)
      mid = div(len, 2)

      {updated_chars, changed} =
        Enum.reduce_while(0..mid - 1, {chars, false}, fn i, {arr, _} ->
          if Enum.at(arr, i) != "a" do
            {:halt, {List.replace_at(arr, i, "a"), true}}
          else
            {:cont, {arr, false}}
          end
        end)

      final_chars =
        if changed do
          updated_chars
        else
          List.replace_at(updated_chars, len - 1, "b")
        end

      Enum.join(final_chars)
    end
  end
end
```
