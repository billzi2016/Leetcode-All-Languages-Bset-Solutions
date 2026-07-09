# 0917. Reverse Only Letters

## Cpp

```cpp
class Solution {
public:
    string reverseOnlyLetters(string s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            if (!isalpha(s[i])) {
                ++i;
            } else if (!isalpha(s[j])) {
                --j;
            } else {
                swap(s[i], s[j]);
                ++i;
                --j;
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String reverseOnlyLetters(String s) {
        char[] chars = s.toCharArray();
        int i = 0, j = chars.length - 1;
        while (i < j) {
            if (!Character.isLetter(chars[i])) {
                i++;
            } else if (!Character.isLetter(chars[j])) {
                j--;
            } else {
                char tmp = chars[i];
                chars[i] = chars[j];
                chars[j] = tmp;
                i++;
                j--;
            }
        }
        return new String(chars);
    }
}
```

## Python

```python
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            if not chars[i].isalpha():
                i += 1
            elif not chars[j].isalpha():
                j -= 1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return ''.join(chars)
```

## Python3

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            if not chars[i].isalpha():
                i += 1
            elif not chars[j].isalpha():
                j -= 1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return ''.join(chars)
```

## C

```c
#include <string.h>
#include <ctype.h>

char* reverseOnlyLetters(char* s) {
    int left = 0;
    int right = (int)strlen(s) - 1;
    while (left < right) {
        if (!isalpha((unsigned char)s[left])) {
            ++left;
        } else if (!isalpha((unsigned char)s[right])) {
            --right;
        } else {
            char tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            ++left;
            --right;
        }
    }
    return s;
}
```

## Csharp

```csharp
public class Solution
{
    public string ReverseOnlyLetters(string s)
    {
        char[] chars = s.ToCharArray();
        int i = 0, j = chars.Length - 1;
        while (i < j)
        {
            if (!char.IsLetter(chars[i]))
            {
                i++;
            }
            else if (!char.IsLetter(chars[j]))
            {
                j--;
            }
            else
            {
                char temp = chars[i];
                chars[i] = chars[j];
                chars[j] = temp;
                i++;
                j--;
            }
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
var reverseOnlyLetters = function(s) {
    const arr = s.split('');
    let i = 0, j = arr.length - 1;
    
    const isLetter = (c) => {
        const code = c.charCodeAt(0);
        return (code >= 65 && code <= 90) || (code >= 97 && code <= 122);
    };
    
    while (i < j) {
        if (!isLetter(arr[i])) {
            i++;
            continue;
        }
        if (!isLetter(arr[j])) {
            j--;
            continue;
        }
        // swap letters
        const temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;
        j--;
    }
    
    return arr.join('');
};
```

## Typescript

```typescript
function reverseOnlyLetters(s: string): string {
    const chars = s.split('');
    let left = 0, right = chars.length - 1;
    const isLetter = (c: string) => 
        (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    
    while (left < right) {
        if (!isLetter(chars[left])) {
            left++;
            continue;
        }
        if (!isLetter(chars[right])) {
            right--;
            continue;
        }
        const temp = chars[left];
        chars[left] = chars[right];
        chars[right] = temp;
        left++;
        right--;
    }
    
    return chars.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseOnlyLetters($s) {
        $arr = str_split($s);
        $i = 0;
        $j = count($arr) - 1;

        while ($i < $j) {
            if (!ctype_alpha($arr[$i])) {
                $i++;
                continue;
            }
            if (!ctype_alpha($arr[$j])) {
                $j--;
                continue;
            }
            // swap
            $temp = $arr[$i];
            $arr[$i] = $arr[$j];
            $arr[$j] = $temp;

            $i++;
            $j--;
        }

        return implode('', $arr);
    }
}
```

## Swift

```swift
class Solution {
    func reverseOnlyLetters(_ s: String) -> String {
        var chars = Array(s)
        var i = 0
        var j = chars.count - 1
        while i < j {
            if !isLetter(chars[i]) {
                i += 1
            } else if !isLetter(chars[j]) {
                j -= 1
            } else {
                chars.swapAt(i, j)
                i += 1
                j -= 1
            }
        }
        return String(chars)
    }
    
    private func isLetter(_ c: Character) -> Bool {
        for scalar in c.unicodeScalars {
            let v = scalar.value
            if (v >= 65 && v <= 90) || (v >= 97 && v <= 122) {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseOnlyLetters(s: String): String {
        val chars = s.toCharArray()
        var i = 0
        var j = chars.lastIndex
        while (i < j) {
            if (!chars[i].isLetter()) {
                i++
            } else if (!chars[j].isLetter()) {
                j--
            } else {
                val tmp = chars[i]
                chars[i] = chars[j]
                chars[j] = tmp
                i++
                j--
            }
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String reverseOnlyLetters(String s) {
    List<String> chars = s.split('');
    int i = 0, j = chars.length - 1;

    bool isLetter(String c) {
      int code = c.codeUnitAt(0);
      return (code >= 65 && code <= 90) || (code >= 97 && code <= 122);
    }

    while (i < j) {
      if (!isLetter(chars[i])) {
        i++;
      } else if (!isLetter(chars[j])) {
        j--;
      } else {
        String temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
        i++;
        j--;
      }
    }

    return chars.join();
  }
}
```

## Golang

```go
func reverseOnlyLetters(s string) string {
    b := []byte(s)
    i, j := 0, len(b)-1
    isLetter := func(c byte) bool {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')
    }
    for i < j {
        if !isLetter(b[i]) {
            i++
        } else if !isLetter(b[j]) {
            j--
        } else {
            b[i], b[j] = b[j], b[i]
            i++
            j--
        }
    }
    return string(b)
}
```

## Ruby

```ruby
# @param {String} s
# @return {String}
def reverse_only_letters(s)
  chars = s.chars
  i = 0
  j = chars.length - 1
  while i < j
    if !(chars[i] =~ /[A-Za-z]/)
      i += 1
    elsif !(chars[j] =~ /[A-Za-z]/)
      j -= 1
    else
      chars[i], chars[j] = chars[j], chars[i]
      i += 1
      j -= 1
    end
  end
  chars.join
end
```

## Scala

```scala
object Solution {
    def reverseOnlyLetters(s: String): String = {
        val arr = s.toCharArray
        var i = 0
        var j = arr.length - 1
        while (i < j) {
            if (!Character.isLetter(arr(i))) {
                i += 1
            } else if (!Character.isLetter(arr(j))) {
                j -= 1
            } else {
                val temp = arr(i)
                arr(i) = arr(j)
                arr(j) = temp
                i += 1
                j -= 1
            }
        }
        new String(arr)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_only_letters(s: String) -> String {
        let mut bytes = s.into_bytes();
        let mut i: usize = 0;
        let mut j: usize = if bytes.is_empty() { 0 } else { bytes.len() - 1 };
        while i < j {
            while i < j && !bytes[i].is_ascii_alphabetic() {
                i += 1;
            }
            while i < j && !bytes[j].is_ascii_alphabetic() {
                if j == 0 { break; }
                j -= 1;
            }
            if i < j {
                bytes.swap(i, j);
                i += 1;
                if j > 0 { j -= 1; }
            }
        }
        unsafe { String::from_utf8_unchecked(bytes) }
    }
}
```

## Racket

```racket
(define/contract (reverse-only-letters s)
  (-> string? string?)
  (let* ([chars (string->list s)]
         [len (length chars)]
         [vec (list->vector chars)])
    (define (letter? ch)
      (or (and (char>=? ch #\a) (char<=? ch #\z))
          (and (char>=? ch #\A) (char<=? ch #\Z))))
    (let loop ([i 0] [j (- len 1)])
      (when (< i j)
        (define ci (vector-ref vec i))
        (define cj (vector-ref vec j))
        (cond
          [(not (letter? ci)) (loop (+ i 1) j)]
          [(not (letter? cj)) (loop i (- j 1))]
          [else
           (vector-set! vec i cj)
           (vector-set! vec j ci)
           (loop (+ i 1) (- j 1))])))
    (list->string (vector->list vec))))
```

## Erlang

```erlang
-spec reverse_only_letters(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_only_letters(S) ->
    List = binary_to_list(S),
    Letters = [C || C <- List, is_letter(C)],
    RevLetters = lists:reverse(Letters),
    NewList = replace(List, RevLetters),
    list_to_binary(NewList).

is_letter(C) when C >= $a, C =< $z -> true;
is_letter(C) when C >= $A, C =< $Z -> true;
is_letter(_) -> false.

replace([], _) ->
    [];
replace([H|T], Rev) when is_letter(H) ->
    [hd(Rev) | replace(T, tl(Rev))];
replace([H|T], Rev) ->
    [H | replace(T, Rev)].
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_only_letters(s :: String.t) :: String.t
  def reverse_only_letters(s) do
    graphemes = String.graphemes(s)

    letters =
      graphemes
      |> Enum.filter(&letter?/1)
      |> Enum.reverse()

    {result, _} =
      Enum.map_reduce(graphemes, letters, fn ch, acc ->
        if letter?(ch) do
          [h | t] = acc
          {h, t}
        else
          {ch, acc}
        end
      end)

    Enum.join(result)
  end

  defp letter?(<<code>>) when is_integer(code) do
    (code >= ?A and code <= ?Z) or (code >= ?a and code <= ?z)
  end
end
```
