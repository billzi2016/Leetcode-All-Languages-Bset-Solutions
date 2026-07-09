# 1957. Delete Characters to Make Fancy String

## Cpp

```cpp
class Solution {
public:
    string makeFancyString(string s) {
        string ans;
        ans.reserve(s.size());
        char prev = 0;
        int cnt = 0;
        for (char c : s) {
            if (c == prev) {
                ++cnt;
            } else {
                prev = c;
                cnt = 1;
            }
            if (cnt < 3) ans.push_back(c);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String makeFancyString(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int len = sb.length();
            if (len >= 2 && sb.charAt(len - 1) == c && sb.charAt(len - 2) == c) {
                continue;
            }
            sb.append(c);
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        res = []
        count = 0
        prev = ''
        for ch in s:
            if ch == prev:
                count += 1
            else:
                prev = ch
                count = 1
            if count < 3:
                res.append(ch)
        return ''.join(res)
```

## Python3

```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for c in s:
            if len(result) >= 2 and result[-1] == c and result[-2] == c:
                continue
            result.append(c)
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* makeFancyString(char* s) {
    int n = strlen(s);
    char *res = (char*)malloc(n + 1);
    if (!res) return NULL;
    
    int j = 0;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (i == 0 || s[i] != s[i - 1]) {
            cnt = 1;
        } else {
            cnt++;
        }
        if (cnt <= 2) {
            res[j++] = s[i];
        }
    }
    res[j] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string MakeFancyString(string s)
    {
        var result = new System.Text.StringBuilder(s.Length);
        char prevChar = '\0';
        int consecutive = 0;

        foreach (char c in s)
        {
            if (c == prevChar)
                consecutive++;
            else
            {
                prevChar = c;
                consecutive = 1;
            }

            if (consecutive < 3)
                result.Append(c);
        }

        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
    if (s.length < 3) return s;
    let res = [];
    // keep track of consecutive count of last character in result
    for (let i = 0; i < s.length; ++i) {
        const ch = s[i];
        const len = res.length;
        if (len >= 2 && res[len - 1] === ch && res[len - 2] === ch) {
            // would create three in a row, skip
            continue;
        }
        res.push(ch);
    }
    return res.join('');
};
```

## Typescript

```typescript
function makeFancyString(s: string): string {
    let result = "";
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        if (i > 0 && s[i] === s[i - 1]) {
            count++;
        } else {
            count = 1;
        }
        if (count <= 2) {
            result += s[i];
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function makeFancyString($s) {
        $n = strlen($s);
        if ($n < 3) {
            return $s;
        }
        $res = '';
        $prevChar = '';
        $count = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === $prevChar) {
                $count++;
            } else {
                $prevChar = $c;
                $count = 1;
            }
            if ($count < 3) {
                $res .= $c;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func makeFancyString(_ s: String) -> String {
        var result = ""
        var prevChar: Character? = nil
        var count = 0
        
        for ch in s {
            if ch == prevChar {
                count += 1
            } else {
                prevChar = ch
                count = 1
            }
            if count < 3 {
                result.append(ch)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeFancyString(s: String): String {
        val result = StringBuilder()
        var prevChar = '\u0000'
        var count = 0
        for (c in s) {
            if (c == prevChar) {
                count++
            } else {
                prevChar = c
                count = 1
            }
            if (count < 3) {
                result.append(c)
            }
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String makeFancyString(String s) {
    List<String> ans = [];
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      int n = ans.length;
      if (n >= 2 && ans[n - 1] == ch && ans[n - 2] == ch) continue;
      ans.add(ch);
    }
    return ans.join();
  }
}
```

## Golang

```go
func makeFancyString(s string) string {
    res := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        n := len(res)
        if n >= 2 && s[i] == res[n-1] && s[i] == res[n-2] {
            continue
        }
        res = append(res, s[i])
    }
    return string(res)
}
```

## Ruby

```ruby
# @param {String} s
# @return {String}
def make_fancy_string(s)
  result = +""
  prev_char = nil
  count = 0

  s.each_char do |ch|
    if ch == prev_char
      count += 1
    else
      prev_char = ch
      count = 1
    end
    result << ch if count < 3
  end

  result
end
```

## Scala

```scala
object Solution {
    def makeFancyString(s: String): String = {
        val sb = new StringBuilder
        var prevChar: Char = 0
        var count = 0
        for (c <- s) {
            if (c == prevChar) {
                count += 1
            } else {
                prevChar = c
                count = 1
            }
            if (count < 3) sb.append(c)
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut result = String::with_capacity(s.len());
        let mut prev_char = '\0';
        let mut count = 0usize;

        for ch in s.chars() {
            if ch == prev_char {
                count += 1;
            } else {
                prev_char = ch;
                count = 1;
            }
            if count < 3 {
                result.push(ch);
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (make-fancy-string s)
  (-> string? string?)
  (let* ((chars (string->list s))
         (result
          (let loop ((lst chars) (prev #\null) (cnt 0) (acc '()))
            (if (null? lst)
                (reverse acc)
                (let* ((c (car lst))
                       (new-cnt (if (char=? c prev) (+ cnt 1) 1)))
                  (if (< new-cnt 3)
                      (loop (cdr lst) c new-cnt (cons c acc))
                      (loop (cdr lst) c new-cnt acc)))))))
    (list->string result)))
```

## Erlang

```erlang
-spec make_fancy_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_fancy_string(S) ->
    make_fancy_string(S, -1, 0, []).

%% Recursive helper:
%%   Rest  - remaining binary to process
%%   Prev  - previous character code (or -1 for none)
%%   Cnt   - consecutive count of Prev seen so far
%%   Acc   - accumulator list of kept characters (in reverse order)
make_fancy_string(<<>>, _Prev, _Cnt, Acc) ->
    list_to_binary(lists:reverse(Acc));
make_fancy_string(<<C, Rest/binary>>, Prev, Cnt, Acc) ->
    NewCnt = if
        C =:= Prev -> Cnt + 1;
        true       -> 1
    end,
    case NewCnt =< 2 of
        true  -> make_fancy_string(Rest, C, NewCnt, [C | Acc]);
        false -> make_fancy_string(Rest, C, NewCnt, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec make_fancy_string(s :: String.t()) :: String.t()
  def make_fancy_string(s) do
    s
    |> String.graphemes()
    |> Enum.reduce({nil, 0, []}, fn ch, {prev, cnt, acc} ->
      if prev == ch do
        new_cnt = cnt + 1

        if new_cnt <= 2 do
          {ch, new_cnt, [ch | acc]}
        else
          {ch, new_cnt, acc}
        end
      else
        {ch, 1, [ch | acc]}
      end
    end)
    |> elem(2)
    |> Enum.reverse()
    |> Enum.join()
  end
end
```
