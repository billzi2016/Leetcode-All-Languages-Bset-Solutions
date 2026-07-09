# 2810. Faulty Keyboard

## Cpp

```cpp
class Solution {
public:
    string finalString(string s) {
        string res;
        for (char c : s) {
            if (c == 'i') {
                reverse(res.begin(), res.end());
            } else {
                res.push_back(c);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String finalString(String s) {
        java.util.Deque<Character> dq = new java.util.ArrayDeque<>();
        boolean reversed = false;
        for (char c : s.toCharArray()) {
            if (c == 'i') {
                reversed = !reversed;
            } else {
                if (!reversed) {
                    dq.addLast(c);
                } else {
                    dq.addFirst(c);
                }
            }
        }
        StringBuilder sb = new StringBuilder(dq.size());
        if (!reversed) {
            for (char ch : dq) {
                sb.append(ch);
            }
        } else {
            java.util.Iterator<Character> it = dq.descendingIterator();
            while (it.hasNext()) {
                sb.append(it.next());
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import deque
        dq = deque()
        rev = False
        for ch in s:
            if ch == 'i':
                rev = not rev
            else:
                if not rev:
                    dq.append(ch)
                else:
                    dq.appendleft(ch)
        return ''.join(reversed(dq)) if rev else ''.join(dq)
```

## Python3

```python
class Solution:
    def finalString(self, s: str) -> str:
        from collections import deque
        dq = deque()
        rev = False
        for ch in s:
            if ch == 'i':
                rev = not rev
            else:
                if not rev:
                    dq.append(ch)
                else:
                    dq.appendleft(ch)
        return ''.join(dq) if not rev else ''.join(reversed(dq))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* finalString(char* s) {
    int n = strlen(s);
    char *ans = (char*)malloc(n + 1);
    int len = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == 'i') {
            for (int l = 0, r = len - 1; l < r; ++l, --r) {
                char tmp = ans[l];
                ans[l] = ans[r];
                ans[r] = tmp;
            }
        } else {
            ans[len++] = s[i];
        }
    }
    ans[len] = '\0';
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public string FinalString(string s)
    {
        var chars = new System.Collections.Generic.List<char>();
        foreach (char c in s)
        {
            if (c == 'i')
                chars.Reverse();
            else
                chars.Add(c);
        }
        return new string(chars.ToArray());
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var finalString = function(s) {
    let reversed = false;
    const result = [];
    for (const ch of s) {
        if (ch === 'i') {
            reversed = !reversed;
        } else {
            if (!reversed) {
                result.push(ch);
            } else {
                result.unshift(ch);
            }
        }
    }
    if (reversed) result.reverse();
    return result.join('');
};
```

## Typescript

```typescript
function finalString(s: string): string {
    const result: string[] = [];
    let reversed = false;
    for (const ch of s) {
        if (ch === 'i') {
            reversed = !reversed;
        } else {
            if (!reversed) {
                result.push(ch);
            } else {
                result.unshift(ch);
            }
        }
    }
    if (reversed) {
        result.reverse();
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function finalString($s) {
        $result = "";
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch === 'i') {
                $result = strrev($result);
            } else {
                $result .= $ch;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func finalString(_ s: String) -> String {
        var result = ""
        for ch in s {
            if ch == "i" {
                result = String(result.reversed())
            } else {
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
    fun finalString(s: String): String {
        val deque = java.util.ArrayDeque<Char>()
        var rev = false
        for (ch in s) {
            if (ch == 'i') {
                rev = !rev
            } else {
                if (!rev) {
                    deque.addLast(ch)
                } else {
                    deque.addFirst(ch)
                }
            }
        }
        val sb = StringBuilder()
        if (!rev) {
            for (c in deque) sb.append(c)
        } else {
            while (deque.isNotEmpty()) {
                sb.append(deque.removeLast())
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String finalString(String s) {
    List<String> dq = [];
    bool normal = true;
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (ch == 'i') {
        normal = !normal;
      } else {
        if (normal) {
          dq.add(ch);
        } else {
          dq.insert(0, ch);
        }
      }
    }
    StringBuffer res = StringBuffer();
    if (normal) {
      for (var c in dq) {
        res.write(c);
      }
    } else {
      for (int i = dq.length - 1; i >= 0; i--) {
        res.write(dq[i]);
      }
    }
    return res.toString();
  }
}
```

## Golang

```go
func finalString(s string) string {
    res := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        if s[i] == 'i' {
            for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
                res[l], res[r] = res[r], res[l]
            }
        } else {
            res = append(res, s[i])
        }
    }
    return string(res)
}
```

## Ruby

```ruby
def final_string(s)
  res = []
  rev = false
  s.each_char do |ch|
    if ch == 'i'
      rev = !rev
    else
      if rev
        res.unshift(ch)
      else
        res << ch
      end
    end
  end
  res.reverse! if rev
  res.join
end
```

## Scala

```scala
object Solution {
    def finalString(s: String): String = {
        val sb = new java.lang.StringBuilder
        for (c <- s) {
            if (c == 'i') sb.reverse()
            else sb.append(c)
        }
        sb.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn final_string(s: String) -> String {
        let mut result = String::new();
        for ch in s.chars() {
            if ch == 'i' {
                let reversed: String = result.chars().rev().collect();
                result = reversed;
            } else {
                result.push(ch);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (final-string s)
  (-> string? string?)
  (let loop ((idx 0) (cur ""))
    (if (= idx (string-length s))
        cur
        (let ((ch (string-ref s idx)))
          (if (char=? ch #\i)
              (loop (+ idx 1) (list->string (reverse (string->list cur))))
              (loop (+ idx 1) (string-append cur (string ch))))))))
```

## Erlang

```erlang
-spec final_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
final_string(S) ->
    Chars = binary_to_list(S),
    FinalList = process(Chars, []),
    list_to_binary(FinalList).

process([], Acc) ->
    Acc;
process([C | Rest], Acc) ->
    NewAcc =
        case C of
            $i -> lists:reverse(Acc);
            _  -> Acc ++ [C]
        end,
    process(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec final_string(s :: String.t) :: String.t
  def final_string(s) do
    s
    |> String.graphemes()
    |> Enum.reduce([], fn
      "i", acc -> Enum.reverse(acc)
      ch, acc -> acc ++ [ch]
    end)
    |> Enum.join("")
  end
end
```
