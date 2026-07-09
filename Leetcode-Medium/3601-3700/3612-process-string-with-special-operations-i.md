# 3612. Process String with Special Operations I

## Cpp

```cpp
class Solution {
public:
    string processStr(string s) {
        string result;
        vector<char> deleted;
        for (char ch : s) {
            if (ch == '#') {
                if (!result.empty()) {
                    deleted.push_back(result.back());
                    result.pop_back();
                }
            } else if (ch == '%') {
                if (!deleted.empty()) {
                    result.push_back(deleted.back());
                    deleted.pop_back();
                }
            } else if (ch == '*') {
                // No operation as per problem definition
                continue;
            } else {
                result.push_back(ch);
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String processStr(String s) {
        StringBuilder sb = new StringBuilder();
        java.util.Deque<Character> deleted = new java.util.ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch >= 'a' && ch <= 'z') {
                sb.append(ch);
            } else if (ch == '#') {
                int len = sb.length();
                if (len > 0) {
                    char removed = sb.charAt(len - 1);
                    sb.deleteCharAt(len - 1);
                    deleted.push(removed);
                }
            } else if (ch == '*') {
                if (!deleted.isEmpty()) {
                    sb.append(deleted.pop());
                }
            } else if (ch == '%') {
                sb.reverse();
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        deleted = []
        for ch in s:
            if 'a' <= ch <= 'z':
                result.append(ch)
            elif ch == '#':
                if result:
                    deleted.append(result.pop())
            elif ch == '*':
                if deleted:
                    result.append(deleted.pop())
            elif ch == '%':
                result.reverse()
        return ''.join(result)
```

## Python3

```python
class Solution:
    def processStr(self, s: str) -> str:
        res = []
        undone = []  # stack of characters removed by '#'
        for ch in s:
            if 'a' <= ch <= 'z':
                res.append(ch)
            elif ch == '#':
                if res:
                    undone.append(res.pop())
            elif ch == '%':
                if undone:
                    res.append(undone.pop())
            else:  # '*', no operation defined
                continue
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* processStr(char* s) {
    int n = strlen(s);
    // maximum possible length is n (all letters)
    char *buf = (char*)malloc(n + 1);
    int len = 0;      // current length of buffer
    int cursor = 0;   // position where next insertion occurs

    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (c >= 'a' && c <= 'z') {
            // insert character at cursor
            memmove(buf + cursor + 1, buf + cursor, len - cursor);
            buf[cursor] = c;
            cursor++;
            len++;
        } else if (c == '*') {
            // backspace: delete character before cursor
            if (cursor > 0) {
                memmove(buf + cursor - 1, buf + cursor, len - cursor);
                cursor--;
                len--;
            }
        } else if (c == '#' || c == '%') {
            // move cursor left
            if (cursor > 0) cursor--;
        }
    }

    buf[len] = '\0';
    // allocate exact sized result to return
    char *res = (char*)malloc(len + 1);
    memcpy(res, buf, len + 1);
    free(buf);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ProcessStr(string s) {
        var sb = new System.Text.StringBuilder();
        char? lastDeleted = null;
        foreach (char c in s) {
            if (c == '#') {
                if (sb.Length > 0) {
                    lastDeleted = sb[sb.Length - 1];
                    sb.Remove(sb.Length - 1, 1);
                }
            } else if (c == '*') {
                if (lastDeleted.HasValue) {
                    sb.Append(lastDeleted.Value);
                }
            } else if (c == '%') {
                // reverse the current string
                var arr = sb.ToString().ToCharArray();
                System.Array.Reverse(arr);
                sb.Clear();
                sb.Append(arr);
            } else {
                sb.Append(c);
            }
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var processStr = function(s) {
    const result = [];
    const deletedStack = [];
    for (const ch of s) {
        if (ch >= 'a' && ch <= 'z') {
            result.push(ch);
        } else if (ch === '#') {
            if (result.length > 0) {
                deletedStack.push(result.pop());
            }
        } else if (ch === '%') {
            if (deletedStack.length > 0) {
                result.push(deletedStack.pop());
            }
        } // '*' is ignored
    }
    return result.join('');
};
```

## Typescript

```typescript
function processStr(s: string): string {
    const res: string[] = [];
    const deletedStack: string[] = [];

    for (const ch of s) {
        if (ch >= 'a' && ch <= 'z') {
            res.push(ch);
        } else if (ch === '#') {
            if (res.length > 0) {
                const removed = res.pop() as string;
                deletedStack.push(removed);
            }
        } else if (ch === '%') {
            if (deletedStack.length > 0) {
                const restored = deletedStack.pop() as string;
                res.push(restored);
            }
        } // '*' does nothing
    }

    return res.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function processStr($s) {
        $res = [];
        $deleted = [];

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch === '#') {
                if (!empty($res)) {
                    $deleted[] = array_pop($res);
                }
            } elseif ($ch === '%') {
                if (!empty($deleted)) {
                    $res[] = array_pop($deleted);
                }
            } elseif ($ch === '*') {
                // no operation
                continue;
            } else {
                $res[] = $ch;
            }
        }

        return implode('', $res);
    }
}
```

## Swift

```swift
class Solution {
    func processStr(_ s: String) -> String {
        var result = [Character]()
        var deletedStack = [Character]()
        
        for ch in s {
            switch ch {
            case "#":
                if let removed = result.popLast() {
                    deletedStack.append(removed)
                }
            case "%":
                if result.count >= 2 {
                    let n = result.count
                    result.swapAt(n - 1, n - 2)
                }
            case "*":
                if let restored = deletedStack.popLast() {
                    result.append(restored)
                }
            default:
                result.append(ch)
            }
        }
        
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun processStr(s: String): String {
        val result = mutableListOf<Char>()
        val deleted = mutableListOf<Char>()
        for (ch in s) {
            when (ch) {
                '#' -> {
                    if (result.isNotEmpty()) {
                        deleted.add(result.removeAt(result.size - 1))
                    }
                }
                '%' -> {
                    if (deleted.isNotEmpty()) {
                        result.add(deleted.removeAt(deleted.size - 1))
                    }
                }
                '*' -> {
                    // no operation
                }
                else -> {
                    result.add(ch)
                }
            }
        }
        return result.joinToString("")
    }
}
```

## Dart

```dart
class Solution {
  String processStr(String s) {
    List<String> result = [];
    String? buffer;
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (ch == '#') {
        if (result.isNotEmpty) {
          buffer = result.removeLast();
        } else {
          buffer = null;
        }
      } else if (ch == '%') {
        if (buffer != null) {
          result.add(buffer);
        }
      } else if (ch == '*') {
        // No operation for '*'
      } else {
        result.add(ch);
      }
    }
    return result.join();
  }
}
```

## Golang

```go
func processStr(s string) string {
    var result []byte
    var deleted []byte

    for i := 0; i < len(s); i++ {
        ch := s[i]
        switch ch {
        case '#':
            if len(result) > 0 {
                // pop last character and store it for possible restore
                c := result[len(result)-1]
                result = result[:len(result)-1]
                deleted = append(deleted, c)
            }
        case '%':
            if len(deleted) > 0 {
                // restore most recently deleted character
                c := deleted[len(deleted)-1]
                deleted = deleted[:len(deleted)-1]
                result = append(result, c)
            }
        case '*':
            // clear the history of deleted characters
            deleted = nil
        default:
            // regular lowercase letter
            result = append(result, ch)
        }
    }

    return string(result)
}
```

## Ruby

```ruby
def process_str(s)
  result = ""
  s.each_char do |ch|
    case ch
    when '*'
      result.chop! unless result.empty?
    when '#'
      result << result[-1] unless result.empty?
    when '%'
      result = result.reverse
    else
      result << ch
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def processStr(s: String): String = {
        val sb = new java.lang.StringBuilder()
        var deleted = List.empty[Char]

        for (ch <- s) {
            if (ch >= 'a' && ch <= 'z') {
                sb.append(ch)
            } else {
                ch match {
                    case '#' =>
                        if (sb.length > 0) {
                            val removed = sb.charAt(sb.length - 1)
                            sb.deleteCharAt(sb.length - 1)
                            deleted = removed :: deleted
                        }
                    case '*' =>
                        if (deleted.nonEmpty) {
                            sb.append(deleted.head)
                            deleted = deleted.tail
                        }
                    case '%' =>
                        sb.reverse()
                    case _ => // ignore other characters
                }
            }
        }

        sb.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn process_str(s: String) -> String {
        let mut result: Vec<char> = Vec::new();
        let mut deleted: Vec<char> = Vec::new(); // stack of removed characters

        for ch in s.chars() {
            match ch {
                '#' => {
                    if let Some(c) = result.pop() {
                        deleted.push(c);
                    }
                }
                '*' => {
                    if let Some(c) = deleted.pop() {
                        result.push(c);
                    }
                }
                '%' => { /* no operation */ }
                _ => result.push(ch),
            }
        }

        result.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (process-str s)
  (-> string? string?)
  (let loop ((i 0) (res ""))
    (if (= i (string-length s))
        res
        (let ((ch (string-ref s i)))
          (cond
            [(or (char>=? ch #\a) (char<=? ch #\z)) ; letter
             (loop (+ i 1) (string-append res (string ch)))]
            [(char=? ch #\#)
             (if (> (string-length res) 0)
                 (let ((last (substring res (- (string-length res) 1))))
                   (loop (+ i 1) (string-append res last)))
                 (loop (+ i 1) res))]
            [(char=? ch #\*)
             (if (> (string-length res) 0)
                 (loop (+ i 1) (substring res 0 (- (string-length res) 1)))
                 (loop (+ i 1) res))]
            [(char=? ch #\%)
             (let ((rev (list->string (reverse (string->list res)))))
               (loop (+ i 1) rev))]
            [else
             (loop (+ i 1) res)])))))
```

## Erlang

```erlang
-spec process_str(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
process_str(S) ->
    process_string(unicode:characters_to_list(S), [], []).

process_string([], ResAcc, _DelStack) ->
    list_to_binary(lists:reverse(ResAcc));
process_string([C|Rest], ResAcc, DelStack) when C >= $a, C =< $z ->
    process_string(Rest, [C|ResAcc], DelStack);
process_string([$#|Rest], ResAcc, DelStack) ->
    case ResAcc of
        [] -> process_string(Rest, [], DelStack);
        [Last|Tail] -> process_string(Rest, Tail, [Last|DelStack])
    end;
process_string([ $% | Rest], ResAcc, DelStack) ->
    case DelStack of
        [] -> process_string(Rest, ResAcc, []);
        [Del|DelTail] -> process_string(Rest, [Del|ResAcc], DelTail)
    end;
process_string([ $* | Rest], ResAcc, DelStack) ->
    % '*' has no effect in this specification
    process_string(Rest, ResAcc, DelStack).
```

## Elixir

```elixir
defmodule Solution do
  @spec process_str(s :: String.t) :: String.t
  def process_str(s) do
    {chars, _} =
      String.to_charlist(s)
      |> Enum.reduce({[], 0}, fn c, {list, cursor} ->
        cond do
          c in ?a..?z ->
            {List.insert_at(list, cursor, c), cursor + 1}
          c == ?* ->
            if cursor > 0 do
              {List.delete_at(list, cursor - 1), cursor - 1}
            else
              {list, cursor}
            end
          c == ?# ->
            if cursor > 0, do: {list, cursor - 1}, else: {list, cursor}
          c == ?% ->
            {list, 0}
          true ->
            {list, cursor}
        end
      end)

    List.to_string(chars)
  end
end
```
