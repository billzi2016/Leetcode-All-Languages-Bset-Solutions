# 3163. String Compression III

## Cpp

```cpp
class Solution {
public:
    string compressedString(string word) {
        int n = word.size();
        string res;
        res.reserve(2 * n);
        for (int i = 0; i < n; ) {
            char c = word[i];
            int cnt = 0;
            while (i < n && word[i] == c && cnt < 9) {
                ++cnt;
                ++i;
            }
            res.push_back('0' + cnt);
            res.push_back(c);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String compressedString(String word) {
        StringBuilder sb = new StringBuilder();
        int n = word.length();
        int i = 0;
        while (i < n) {
            char c = word.charAt(i);
            int cnt = 0;
            while (i < n && word.charAt(i) == c && cnt < 9) {
                cnt++;
                i++;
            }
            sb.append(cnt).append(c);
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        n = len(word)
        i = 0
        parts = []
        while i < n:
            cnt = 1
            # count up to 9 same chars
            while cnt < 9 and i + cnt < n and word[i + cnt] == word[i]:
                cnt += 1
            parts.append(str(cnt))
            parts.append(word[i])
            i += cnt
        return "".join(parts)
```

## Python3

```python
class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        i = 0
        parts = []
        while i < n:
            ch = word[i]
            cnt = 0
            while i < n and word[i] == ch and cnt < 9:
                cnt += 1
                i += 1
            parts.append(str(cnt))
            parts.append(ch)
        return ''.join(parts)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* compressedString(char* word) {
    int n = strlen(word);
    char *res = (char *)malloc(2 * n + 1);
    int out = 0;
    int i = 0;
    while (i < n) {
        char c = word[i];
        int cnt = 0;
        while (i < n && word[i] == c && cnt < 9) {
            ++cnt;
            ++i;
        }
        res[out++] = '0' + cnt;
        res[out++] = c;
    }
    res[out] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string CompressedString(string word) {
        var sb = new System.Text.StringBuilder();
        int n = word.Length;
        int i = 0;
        while (i < n) {
            char c = word[i];
            int cnt = 0;
            while (i < n && word[i] == c && cnt < 9) {
                cnt++;
                i++;
            }
            sb.Append(cnt);
            sb.Append(c);
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {string}
 */
var compressedString = function(word) {
    const n = word.length;
    let i = 0;
    const res = [];
    while (i < n) {
        const ch = word[i];
        let cnt = 0;
        while (i < n && word[i] === ch && cnt < 9) {
            cnt++;
            i++;
        }
        res.push(cnt.toString(), ch);
    }
    return res.join('');
};
```

## Typescript

```typescript
function compressedString(word: string): string {
    const n = word.length;
    let i = 0;
    const parts: string[] = [];
    while (i < n) {
        const ch = word[i];
        let cnt = 0;
        while (i < n && word[i] === ch && cnt < 9) {
            cnt++;
            i++;
        }
        parts.push(cnt.toString() + ch);
    }
    return parts.join('');
}
```

## Php

```php
class Solution {
    /**
     * @param String $word
     * @return String
     */
    function compressedString($word) {
        $n = strlen($word);
        $i = 0;
        $parts = [];
        while ($i < $n) {
            $ch = $word[$i];
            $cnt = 0;
            while ($i < $n && $cnt < 9 && $word[$i] === $ch) {
                $i++;
                $cnt++;
            }
            $parts[] = $cnt . $ch;
        }
        return implode('', $parts);
    }
}
```

## Swift

```swift
class Solution {
    func compressedString(_ word: String) -> String {
        let bytes = Array(word.utf8)
        var result = [UInt8]()
        var i = 0
        while i < bytes.count {
            let ch = bytes[i]
            var cnt = 0
            while i < bytes.count && bytes[i] == ch && cnt < 9 {
                cnt += 1
                i += 1
            }
            result.append(UInt8(cnt) + 48) // '0' ascii is 48
            result.append(ch)
        }
        return String(bytes: result, encoding: .utf8)!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun compressedString(word: String): String {
        val n = word.length
        val sb = StringBuilder()
        var i = 0
        while (i < n) {
            val ch = word[i]
            var cnt = 0
            while (i < n && word[i] == ch && cnt < 9) {
                cnt++
                i++
            }
            sb.append(cnt).append(ch)
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String compressedString(String word) {
    int n = word.length;
    StringBuffer sb = StringBuffer();
    int i = 0;
    while (i < n) {
      String ch = word[i];
      int cnt = 0;
      while (i < n && word[i] == ch && cnt < 9) {
        cnt++;
        i++;
      }
      sb.write(cnt);
      sb.write(ch);
    }
    return sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func compressedString(word string) string {
	var builder strings.Builder
	n := len(word)
	for i := 0; i < n; {
		cnt := 1
		for i+cnt < n && word[i+cnt] == word[i] && cnt < 9 {
			cnt++
		}
		builder.WriteByte(byte('0' + cnt))
		builder.WriteByte(word[i])
		i += cnt
	}
	return builder.String()
}
```

## Ruby

```ruby
# @param {String} word
# @return {String}
def compressed_string(word)
  n = word.length
  i = 0
  result = +""
  while i < n
    ch = word[i]
    cnt = 0
    while i < n && word[i] == ch && cnt < 9
      cnt += 1
      i += 1
    end
    result << cnt.to_s << ch
  end
  result
end
```

## Scala

```scala
object Solution {
    def compressedString(word: String): String = {
        val n = word.length
        val sb = new StringBuilder(n * 2) // approximate size
        var i = 0
        while (i < n) {
            val ch = word.charAt(i)
            var cnt = 0
            while (i < n && word.charAt(i) == ch && cnt < 9) {
                cnt += 1
                i += 1
            }
            sb.append(cnt).append(ch)
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn compressed_string(word: String) -> String {
        let bytes = word.as_bytes();
        let n = bytes.len();
        let mut i = 0;
        let mut result = String::with_capacity(n * 2); // worst case each char becomes "1x"
        while i < n {
            let cur = bytes[i];
            let mut cnt = 0usize;
            while i < n && bytes[i] == cur && cnt < 9 {
                cnt += 1;
                i += 1;
            }
            result.push_str(&cnt.to_string());
            result.push(cur as char);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (compressed-string word)
  (-> string? string?)
  (let* ((n (string-length word)))
    (let loop ((i 0) (parts '()))
      (if (= i n)
          (apply string-append (reverse parts))
          (let ((c (string-ref word i)))
            (let-values (((j cnt)
                          (let inner-loop ((pos i) (cnt 0))
                            (if (or (= pos n)
                                    (>= cnt 9)
                                    (not (char=? (string-ref word pos) c)))
                                (values pos cnt)
                                (inner-loop (+ pos 1) (+ cnt 1))))))
              (loop j (cons (string-append (number->string cnt) (string c)) parts))))))))
```

## Erlang

```erlang
-module(solution).
-export([compressed_string/1]).

-spec compressed_string(Word :: unicode:unicode_binary()) -> unicode:unicode_binary().
compressed_string(Word) ->
    case Word of
        <<>> -> <<>>;
        <<FirstChar, Rest/binary>> ->
            build(Rest, FirstChar, 1, [])
    end.

build(<<>>, PrevChar, Count, Acc) ->
    Segment = <<$0 + Count, PrevChar>>,
    iolist_to_binary(lists:reverse([Segment | Acc]));
build(<<Char, Rest/binary>>, PrevChar, Count, Acc) when Char == PrevChar, Count < 9 ->
    build(Rest, PrevChar, Count + 1, Acc);
build(<<Char, Rest/binary>>, PrevChar, Count, Acc) ->
    Segment = <<$0 + Count, PrevChar>>,
    NewAcc = [Segment | Acc],
    build(Rest, Char, 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec compressed_string(word :: String.t()) :: String.t()
  def compressed_string(word) do
    <<first, rest::binary>> = word
    iolist_rev = go(rest, first, 1, [])
    iolist = :lists.reverse(iolist_rev)
    :erlang.iolist_to_binary(iolist)
  end

  defp go(<<>>, curr_char, cnt, acc) do
    [Integer.to_string(cnt), <<curr_char>> | acc]
  end

  defp go(<<c, rest::binary>>, curr_char, cnt, acc) when c == curr_char and cnt < 9 do
    go(rest, curr_char, cnt + 1, acc)
  end

  defp go(<<c, rest::binary>>, curr_char, cnt, acc) do
    new_acc = [Integer.to_string(cnt), <<curr_char>> | acc]
    go(rest, c, 1, new_acc)
  end
end
```
