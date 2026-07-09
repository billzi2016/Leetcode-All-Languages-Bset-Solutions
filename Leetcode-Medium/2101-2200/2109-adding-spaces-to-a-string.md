# 2109. Adding Spaces to a String

## Cpp

```cpp
class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string result;
        result.reserve(s.size() + spaces.size());
        size_t idx = 0, n = spaces.size();
        for (size_t i = 0; i < s.size(); ++i) {
            if (idx < n && static_cast<int>(i) == spaces[idx]) {
                result.push_back(' ');
                ++idx;
            }
            result.push_back(s[i]);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder sb = new StringBuilder(s.length() + spaces.length);
        int idx = 0; // pointer for spaces array
        for (int i = 0; i < s.length(); i++) {
            if (idx < spaces.length && i == spaces[idx]) {
                sb.append(' ');
                idx++;
            }
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        res = []
        space_idx = 0
        m = len(spaces)
        for i, ch in enumerate(s):
            if space_idx < m and i == spaces[space_idx]:
                res.append(' ')
                space_idx += 1
            res.append(ch)
        return ''.join(res)
```

## Python3

```python
from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_idx = 0
        m = len(spaces)
        for i, ch in enumerate(s):
            if space_idx < m and i == spaces[space_idx]:
                result.append(' ')
                space_idx += 1
            result.append(ch)
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* addSpaces(char* s, int* spaces, int spacesSize) {
    size_t len = strlen(s);
    char *res = (char *)malloc(len + spacesSize + 1); // extra space for inserted spaces and null terminator
    if (!res) return NULL;

    size_t i = 0;          // index in original string
    size_t k = 0;          // index in result string
    int spIdx = 0;         // index in spaces array

    while (i < len) {
        if (spIdx < spacesSize && (int)i == spaces[spIdx]) {
            res[k++] = ' ';
            spIdx++;
        }
        res[k++] = s[i++];
    }

    // In case there are remaining spaces after the last character (should not happen per constraints)
    while (spIdx < spacesSize) {
        res[k++] = ' ';
        spIdx++;
    }

    res[k] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string AddSpaces(string s, int[] spaces)
    {
        var result = new System.Text.StringBuilder(s.Length + spaces.Length);
        int spaceIdx = 0;
        for (int i = 0; i < s.Length; i++)
        {
            if (spaceIdx < spaces.Length && i == spaces[spaceIdx])
            {
                result.Append(' ');
                spaceIdx++;
            }
            result.Append(s[i]);
        }
        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    const n = s.length;
    const m = spaces.length;
    let res = new Array(n + m);
    let si = 0; // index in spaces
    let ri = 0; // index in result array

    for (let i = 0; i < n; ++i) {
        if (si < m && i === spaces[si]) {
            res[ri++] = ' ';
            si++;
        }
        res[ri++] = s[i];
    }

    return res.join('');
};
```

## Typescript

```typescript
function addSpaces(s: string, spaces: number[]): string {
    const n = s.length;
    const m = spaces.length;
    const result: string[] = [];
    let spaceIdx = 0;

    for (let i = 0; i < n; i++) {
        if (spaceIdx < m && i === spaces[spaceIdx]) {
            result.push(' ');
            spaceIdx++;
        }
        result.push(s[i]);
    }

    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $spaces
     * @return String
     */
    function addSpaces($s, $spaces) {
        $n = strlen($s);
        $m = count($spaces);
        $spaceIdx = 0;
        $result = [];

        for ($i = 0; $i < $n; $i++) {
            if ($spaceIdx < $m && $i == $spaces[$spaceIdx]) {
                $result[] = ' ';
                $spaceIdx++;
            }
            $result[] = $s[$i];
        }

        return implode('', $result);
    }
}
```

## Swift

```swift
class Solution {
    func addSpaces(_ s: String, _ spaces: [Int]) -> String {
        let chars = Array(s)
        var result = [Character]()
        result.reserveCapacity(chars.count + spaces.count)
        var spaceIdx = 0
        for i in 0..<chars.count {
            if spaceIdx < spaces.count && i == spaces[spaceIdx] {
                result.append(" ")
                spaceIdx += 1
            }
            result.append(chars[i])
        }
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addSpaces(s: String, spaces: IntArray): String {
        val result = StringBuilder(s.length + spaces.size)
        var spaceIdx = 0
        for (i in s.indices) {
            if (spaceIdx < spaces.size && i == spaces[spaceIdx]) {
                result.append(' ')
                spaceIdx++
            }
            result.append(s[i])
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String addSpaces(String s, List<int> spaces) {
    var result = StringBuffer();
    int spaceIdx = 0;
    for (int i = 0; i < s.length; i++) {
      if (spaceIdx < spaces.length && i == spaces[spaceIdx]) {
        result.write(' ');
        spaceIdx++;
      }
      result.write(s[i]);
    }
    return result.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func addSpaces(s string, spaces []int) string {
	var builder strings.Builder
	builder.Grow(len(s) + len(spaces))

	spaceIdx := 0
	for i := 0; i < len(s); i++ {
		if spaceIdx < len(spaces) && i == spaces[spaceIdx] {
			builder.WriteByte(' ')
			spaceIdx++
		}
		builder.WriteByte(s[i])
	}
	return builder.String()
}
```

## Ruby

```ruby
def add_spaces(s, spaces)
  result = +""
  space_idx = 0
  total_spaces = spaces.length
  s.each_char.with_index do |ch, i|
    if space_idx < total_spaces && i == spaces[space_idx]
      result << ' '
      space_idx += 1
    end
    result << ch
  end
  result
end
```

## Scala

```scala
object Solution {
    def addSpaces(s: String, spaces: Array[Int]): String = {
        val sb = new java.lang.StringBuilder(s.length + spaces.length)
        var spaceIdx = 0
        var i = 0
        while (i < s.length) {
            if (spaceIdx < spaces.length && i == spaces(spaceIdx)) {
                sb.append(' ')
                spaceIdx += 1
            }
            sb.append(s.charAt(i))
            i += 1
        }
        sb.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_spaces(s: String, spaces: Vec<i32>) -> String {
        let bytes = s.as_bytes();
        let mut result = String::with_capacity(bytes.len() + spaces.len());
        let mut space_idx = 0usize;
        for i in 0..bytes.len() {
            if space_idx < spaces.len() && i == spaces[space_idx] as usize {
                result.push(' ');
                space_idx += 1;
            }
            result.push(bytes[i] as char);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (add-spaces s spaces)
  (-> string? (listof exact-integer?) string?)
  (let* ([n (string-length s)]
         [spaces-vec (list->vector spaces)]
         [m (vector-length spaces-vec)]
         [res (make-string (+ n m))])
    (let loop ((i 0) (j 0) (k 0))
      (if (= i n)
          res
          (let* ((need-space (and (< k m) (= i (vector-ref spaces-vec k))))
                 (pos (if need-space
                          (begin
                            (string-set! res j #\space)
                            (+ j 1))
                          j))
                 (new-k (if need-space (+ k 1) k)))
            (string-set! res pos (string-ref s i))
            (loop (+ i 1) (+ pos 1) new-k))))))
```

## Erlang

```erlang
-module(solution).
-export([add_spaces/2]).

-spec add_spaces(S :: unicode:unicode_binary(), Spaces :: [integer()]) -> unicode:unicode_binary().
add_spaces(S, Spaces) ->
    add_spaces_loop(S, Spaces, 0, []).

add_spaces_loop(<<>>, _Spaces, _Idx, Acc) ->
    iolist_to_binary(lists:reverse(Acc));
add_spaces_loop(Bin, Spaces, Idx, Acc) ->
    case Spaces of
        [Idx|RestSpaces] ->
            <<Char, Rest/binary>> = Bin,
            NewAcc = [<<Char>>, <<" ">> | Acc],
            add_spaces_loop(Rest, RestSpaces, Idx + 1, NewAcc);
        _ ->
            <<Char, Rest/binary>> = Bin,
            NewAcc = [<<Char>> | Acc],
            add_spaces_loop(Rest, Spaces, Idx + 1, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec add_spaces(String.t(), [integer]) :: String.t()
  def add_spaces(s, spaces) do
    len = byte_size(s)

    {parts_rev, _} =
      Enum.reduce(0..(len - 1), {[], spaces}, fn i, {acc, remaining} ->
        case remaining do
          [next | rest] when i == next ->
            {[<<32>>, :binary.part(s, i, 1) | acc], rest}

          _ ->
            {[ :binary.part(s, i, 1) | acc], remaining}
        end
      end)

    parts_rev
    |> Enum.reverse()
    |> IO.iodata_to_binary()
  end
end
```
