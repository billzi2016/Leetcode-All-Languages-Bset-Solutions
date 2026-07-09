# 2734. Lexicographically Smallest String After Substring Operation

## Cpp

```cpp
class Solution {
public:
    string smallestString(string s) {
        int n = s.size();
        int i = 0;
        while (i < n && s[i] == 'a') ++i;
        if (i == n) {
            // all characters are 'a'
            s[n - 1] = 'z';
        } else {
            while (i < n && s[i] != 'a') {
                s[i] = char(s[i] - 1);
                ++i;
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String smallestString(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        int i = 0;
        while (i < n && arr[i] == 'a') {
            i++;
        }
        if (i == n) { // all characters are 'a'
            arr[n - 1] = 'z';
            return new String(arr);
        }
        int j = i;
        while (j < n && arr[j] != 'a') {
            arr[j] = (char) (arr[j] - 1);
            j++;
        }
        return new String(arr);
    }
}
```

## Python

```python
class Solution(object):
    def smallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s)
        n = len(lst)
        i = 0
        while i < n and lst[i] == 'a':
            i += 1
        if i == n:
            lst[-1] = 'z'
        else:
            while i < n and lst[i] != 'a':
                lst[i] = chr(ord(lst[i]) - 1)
                i += 1
        return ''.join(lst)
```

## Python3

```python
class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        i = 0
        while i < n and s[i] == 'a':
            i += 1
        if i == n:
            # all characters are 'a'
            return s[:-1] + 'z'
        res = list(s)
        while i < n and res[i] != 'a':
            res[i] = chr(ord(res[i]) - 1)
            i += 1
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* smallestString(char* s) {
    int n = strlen(s);
    char *res = (char*)malloc(n + 1);
    if (!res) return NULL;
    memcpy(res, s, n + 1); // copy including null terminator

    int i = 0;
    while (i < n && res[i] == 'a') {
        i++;
    }
    if (i == n) { // all characters are 'a'
        res[n - 1] = 'z';
    } else {
        while (i < n && res[i] != 'a') {
            res[i] = res[i] - 1; // previous character, safe because res[i] != 'a'
            i++;
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string SmallestString(string s) {
        char[] chars = s.ToCharArray();
        int n = chars.Length;
        int i = 0;
        while (i < n && chars[i] == 'a') i++;
        if (i == n) {
            // all characters are 'a'
            chars[n - 1] = 'z';
            return new string(chars);
        }
        while (i < n && chars[i] != 'a') {
            chars[i] = (char)(chars[i] - 1);
            i++;
        }
        return new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var smallestString = function(s) {
    const n = s.length;
    const arr = s.split('');
    let i = 0;
    while (i < n && arr[i] === 'a') i++;
    if (i === n) {
        // all characters are 'a'
        arr[n - 1] = 'z';
    } else {
        while (i < n && arr[i] !== 'a') {
            const code = arr[i].charCodeAt(0);
            arr[i] = String.fromCharCode(code - 1);
            i++;
        }
    }
    return arr.join('');
};
```

## Typescript

```typescript
function smallestString(s: string): string {
    const n = s.length;
    const arr = s.split('');
    let i = 0;
    while (i < n && arr[i] === 'a') i++;
    if (i === n) {
        // all characters are 'a'
        arr[n - 1] = 'z';
    } else {
        while (i < n && arr[i] !== 'a') {
            const code = arr[i].charCodeAt(0);
            arr[i] = String.fromCharCode(code - 1);
            i++;
        }
    }
    return arr.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function smallestString($s) {
        $n = strlen($s);
        $chars = str_split($s);
        $i = 0;
        while ($i < $n && $chars[$i] === 'a') {
            $i++;
        }
        if ($i == $n) { // all characters are 'a'
            $chars[$n - 1] = 'z';
        } else {
            while ($i < $n && $chars[$i] !== 'a') {
                $chars[$i] = chr(ord($chars[$i]) - 1);
                $i++;
            }
        }
        return implode('', $chars);
    }
}
```

## Swift

```swift
class Solution {
    func smallestString(_ s: String) -> String {
        var bytes = Array(s.utf8)
        let n = bytes.count
        var i = 0
        while i < n && bytes[i] == 97 { // 'a'
            i += 1
        }
        if i == n {
            // all characters are 'a'
            bytes[n - 1] = 122 // 'z'
        } else {
            var j = i
            while j < n && bytes[j] != 97 {
                bytes[j] -= 1
                j += 1
            }
        }
        return String(bytes: bytes, encoding: .utf8)!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestString(s: String): String {
        val n = s.length
        val chars = s.toCharArray()
        var i = 0
        while (i < n && chars[i] == 'a') i++
        if (i == n) {
            // all characters are 'a'
            chars[n - 1] = 'z'
        } else {
            while (i < n && chars[i] != 'a') {
                chars[i] = (chars[i] - 1).toChar()
                i++
            }
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String smallestString(String s) {
    List<int> chars = s.codeUnits;
    int n = chars.length;
    int i = 0;
    while (i < n && chars[i] == 97) { // 'a'
      i++;
    }
    if (i == n) {
      // all characters are 'a', change the last one to 'z'
      chars[n - 1] = 122; // 'z'
    } else {
      int j = i;
      while (j < n && chars[j] != 97) { // stop at next 'a'
        chars[j] = chars[j] - 1;
        if (chars[j] < 97) {
          chars[j] = 122; // wrap 'a' -> 'z', though this case won't occur here
        }
        j++;
      }
    }
    return String.fromCharCodes(chars);
  }
}
```

## Golang

```go
func smallestString(s string) string {
    b := []byte(s)
    n := len(b)

    // Find first non-'a' character
    i := 0
    for i < n && b[i] == 'a' {
        i++
    }

    if i == n { // all characters are 'a'
        b[n-1] = 'z'
        return string(b)
    }

    // Decrement contiguous non-'a' segment starting from i
    for i < n && b[i] != 'a' {
        b[i]--
        i++
    }

    return string(b)
}
```

## Ruby

```ruby
def smallest_string(s)
  bytes = s.bytes
  n = bytes.length
  i = 0
  while i < n && bytes[i] == 97 # 'a'
    i += 1
  end
  if i == n
    bytes[n - 1] = 122 # 'z'
  else
    while i < n && bytes[i] != 97
      bytes[i] -= 1
      i += 1
    end
  end
  bytes.pack('C*')
end
```

## Scala

```scala
object Solution {
    def smallestString(s: String): String = {
        val n = s.length
        val arr = s.toCharArray
        var i = 0
        while (i < n && arr(i) == 'a') i += 1
        if (i == n) {
            arr(n - 1) = 'z'
        } else {
            while (i < n && arr(i) != 'a') {
                arr(i) = ((arr(i) - 1).toChar)
                i += 1
            }
        }
        new String(arr)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_string(s: String) -> String {
        let mut bytes = s.into_bytes();
        let n = bytes.len();
        let mut i = 0;
        while i < n && bytes[i] == b'a' {
            i += 1;
        }
        if i == n {
            // all characters are 'a'
            *bytes.last_mut().unwrap() = b'z';
        } else {
            let mut j = i;
            while j < n && bytes[j] != b'a' {
                bytes[j] -= 1; // safe because bytes[j] > b'a'
                j += 1;
            }
        }
        unsafe { String::from_utf8_unchecked(bytes) }
    }
}
```

## Racket

```racket
(define/contract (smallest-string s)
  (-> string? string?)
  (let* ((n (string-length s))
         (first-non-a
          (let loop ((idx 0))
            (cond [(>= idx n) #f]
                  [(char=? (string-ref s idx) #\a) (loop (+ idx 1))]
                  [else idx]))))
    (cond
      [(not first-non-a)
       (string-set! s (- n 1) #\z)
       s]
      [else
       (let loop ((idx first-non-a))
         (when (< idx n)
           (define c (string-ref s idx))
           (if (char=? c #\a)
               (void)
               (begin
                 (string-set! s idx (integer->char (- (char->integer c) 1)))
                 (loop (+ idx 1))))))
       s])))
```

## Erlang

```erlang
-module(solution).
-export([smallest_string/1]).

-spec smallest_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_string(S) ->
    L = binary_to_list(S),
    Result = process(L),
    list_to_binary(Result).

process(L) ->
    go(L, before, [], false).

go([], _Mode, AccRev, Started) ->
    case Started of
        false ->
            NewAcc = replace_last_rev(AccRev, $z),
            lists:reverse(NewAcc);
        true ->
            lists:reverse(AccRev)
    end;
go([C|Rest], before, AccRev, _Started) when C == $a ->
    go(Rest, before, [C|AccRev], false);
go([C|Rest], before, AccRev, _Started) ->
    NewC = C - 1,
    go(Rest, dec, [NewC|AccRev], true);
go([C|Rest], dec, AccRev, _Started) when C == $a ->
    lists:reverse(AccRev) ++ [C] ++ Rest;
go([C|Rest], dec, AccRev, Started) ->
    NewC = C - 1,
    go(Rest, dec, [NewC|AccRev], Started).

replace_last_rev([_ | Tail], NewChar) ->
    [NewChar | Tail].
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_string(s :: String.t()) :: String.t()
  def smallest_string(s) do
    chars = String.to_charlist(s)
    n = length(chars)

    start_idx = Enum.find_index(chars, fn c -> c != ?a end)

    if start_idx == nil do
      # all characters are 'a'
      List.update_at(chars, n - 1, fn _ -> ?z end)
      |> List.to_string()
    else
      # find the length of the contiguous non-'a' segment starting at start_idx
      seg_len =
        chars
        |> Enum.slice(start_idx, n - start_idx)
        |> Enum.take_while(fn c -> c != ?a end)
        |> length()

      new_chars =
        Enum.with_index(chars)
        |> Enum.map(fn {c, i} ->
          if i >= start_idx and i < start_idx + seg_len do
            c - 1
          else
            c
          end
        end)

      List.to_string(new_chars)
    end
  end
end
```
