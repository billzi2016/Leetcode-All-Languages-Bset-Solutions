# 0925. Long Pressed Name

## Cpp

```cpp
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i = 0, j = 0;
        int n = name.size(), m = typed.size();
        while (j < m) {
            if (i < n && name[i] == typed[j]) {
                ++i;
                ++j;
            } else if (j > 0 && typed[j] == typed[j - 1]) {
                ++j;
            } else {
                return false;
            }
        }
        return i == n;
    }
};
```

## Java

```java
class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i = 0, j = 0;
        int n = name.length(), m = typed.length();
        while (j < m) {
            if (i < n && name.charAt(i) == typed.charAt(j)) {
                i++;
                j++;
            } else if (j > 0 && typed.charAt(j) == typed.charAt(j - 1)) {
                j++;
            } else {
                return false;
            }
        }
        return i == n;
    }
}
```

## Python

```python
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0
        n, m = len(name), len(typed)
        while i < m:
            if j < n and typed[i] == name[j]:
                i += 1
                j += 1
            elif i > 0 and typed[i] == typed[i - 1]:
                i += 1
            else:
                return False
        return j == n
```

## Python3

```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        n, m = len(name), len(typed)
        while j < m:
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == n
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool isLongPressedName(char* name, char* typed) {
    int n = strlen(name);
    int m = strlen(typed);
    int i = 0, j = 0;
    
    while (j < m) {
        if (i < n && name[i] == typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] == typed[j - 1]) {
            j++;
        } else {
            return false;
        }
    }
    
    return i == n;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsLongPressedName(string name, string typed)
    {
        int i = 0, j = 0;
        while (i < name.Length && j < typed.Length)
        {
            if (name[i] == typed[j])
            {
                i++;
                j++;
            }
            else if (j > 0 && typed[j] == typed[j - 1])
            {
                j++;
            }
            else
            {
                return false;
            }
        }

        if (i < name.Length)
            return false;

        while (j < typed.Length)
        {
            if (typed[j] != name[name.Length - 1])
                return false;
            j++;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} name
 * @param {string} typed
 * @return {boolean}
 */
var isLongPressedName = function(name, typed) {
    let i = 0, j = 0;
    const n = name.length, m = typed.length;
    while (i < m) {
        if (j < n && typed[i] === name[j]) {
            i++;
            j++;
        } else if (i > 0 && typed[i] === typed[i - 1]) {
            i++;
        } else {
            return false;
        }
    }
    return j === n;
};
```

## Typescript

```typescript
function isLongPressedName(name: string, typed: string): boolean {
    let i = 0;
    let j = 0;
    const n = name.length;
    const m = typed.length;

    while (j < m) {
        if (i < n && name[i] === typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] === typed[j - 1]) {
            // long press of previous character
            j++;
        } else {
            return false;
        }
    }

    return i === n;
}
```

## Php

```php
class Solution {

    /**
     * @param String $name
     * @param String $typed
     * @return Boolean
     */
    function isLongPressedName($name, $typed) {
        $i = 0;
        $j = 0;
        $lenName = strlen($name);
        $lenTyped = strlen($typed);

        while ($j < $lenTyped) {
            if ($i < $lenName && $name[$i] === $typed[$j]) {
                $i++;
                $j++;
            } elseif ($j > 0 && $typed[$j] === $typed[$j - 1]) {
                $j++;
            } else {
                return false;
            }
        }

        return $i === $lenName;
    }
}
```

## Swift

```swift
class Solution {
    func isLongPressedName(_ name: String, _ typed: String) -> Bool {
        var i = name.startIndex
        var j = typed.startIndex
        
        while j != typed.endIndex {
            if i != name.endIndex && name[i] == typed[j] {
                i = name.index(after: i)
                j = typed.index(after: j)
            } else if j != typed.startIndex && typed[typed.index(before: j)] == typed[j] {
                j = typed.index(after: j)
            } else {
                return false
            }
        }
        return i == name.endIndex
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isLongPressedName(name: String, typed: String): Boolean {
        var i = 0
        var j = 0
        val n = name.length
        val m = typed.length
        while (i < m) {
            if (j < n && name[j] == typed[i]) {
                i++
                j++
            } else if (i > 0 && typed[i] == typed[i - 1]) {
                i++
            } else {
                return false
            }
        }
        return j == n
    }
}
```

## Dart

```dart
class Solution {
  bool isLongPressedName(String name, String typed) {
    int i = 0, j = 0;
    while (j < typed.length) {
      if (i < name.length && name[i] == typed[j]) {
        i++;
        j++;
      } else if (j > 0 && typed[j] == typed[j - 1]) {
        j++;
      } else {
        return false;
      }
    }
    return i == name.length;
  }
}
```

## Golang

```go
func isLongPressedName(name string, typed string) bool {
    i, j := 0, 0
    n, m := len(name), len(typed)
    for i < m {
        if j < n && name[j] == typed[i] {
            i++
            j++
        } else if i > 0 && typed[i] == typed[i-1] {
            i++
        } else {
            return false
        }
    }
    return j == n
}
```

## Ruby

```ruby
def is_long_pressed_name(name, typed)
  i = 0
  j = 0
  n_len = name.length
  t_len = typed.length

  while j < t_len
    if i < n_len && name[i] == typed[j]
      i += 1
      j += 1
    elsif j > 0 && typed[j] == typed[j - 1]
      j += 1
    else
      return false
    end
  end

  i == n_len
end
```

## Scala

```scala
object Solution {
    def isLongPressedName(name: String, typed: String): Boolean = {
        var i = 0
        var j = 0
        val n = name.length
        val m = typed.length
        while (j < m) {
            if (i < n && name.charAt(i) == typed.charAt(j)) {
                i += 1
                j += 1
            } else if (j > 0 && typed.charAt(j) == typed.charAt(j - 1)) {
                j += 1
            } else {
                return false
            }
        }
        i == n
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_long_pressed_name(name: String, typed: String) -> bool {
        let name_bytes = name.as_bytes();
        let typed_bytes = typed.as_bytes();
        let mut i = 0usize;
        let mut j = 0usize;

        while j < typed_bytes.len() {
            if i < name_bytes.len() && typed_bytes[j] == name_bytes[i] {
                i += 1;
                j += 1;
            } else if i > 0 && typed_bytes[j] == name_bytes[i - 1] {
                j += 1;
            } else {
                return false;
            }
        }

        i == name_bytes.len()
    }
}
```

## Racket

```racket
(define/contract (is-long-pressed-name name typed)
  (-> string? string? boolean?)
  (let* ((nlen (string-length name))
         (tlen (string-length typed)))
    (let loop ((i 0) (j 0))
      (cond
        [(and (= i nlen) (= j tlen)) #t]
        [(= i nlen)
         (if (zero? nlen)
             #f
             (let ((last (string-ref name (- nlen 1))))
               (let inner ((k j))
                 (cond [(= k tlen) #t]
                       [(char=? (string-ref typed k) last)
                        (inner (+ k 1))]
                       [else #f]))))]
        [(= j tlen) #f]
        [else
         (let ((cname (string-ref name i))
               (ctyped (string-ref typed j)))
           (cond
             [(char=? cname ctyped) (loop (+ i 1) (+ j 1))]
             [(and (> i 0)
                   (char=? ctyped (string-ref name (- i 1))))
              (loop i (+ j 1))]
             [else #f]))]))) )
```

## Erlang

```erlang
-spec is_long_pressed_name(Name :: unicode:unicode_binary(), Typed :: unicode:unicode_binary()) -> boolean().
is_long_pressed_name(Name, Typed) ->
    NameList = binary_to_list(Name),
    TypedList = binary_to_list(Typed),
    check(NameList, TypedList, undefined).

check([], [], _Prev) -> true;
check([], [T|Ts], Prev) when T =:= Prev ->
    check([], Ts, Prev);
check([], [_|_], _) -> false;
check([N|Ns] = NameRest, [T|Ts] = TypedRest, _Prev) ->
    if N =:= T ->
            check(Ns, Ts, T);
       true ->
            case Prev of
                undefined -> false;
                Prev when Prev =:= T ->
                    check(NameRest, Ts, Prev);
                _ -> false
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_long_pressed_name(name :: String.t(), typed :: String.t()) :: boolean()
  def is_long_pressed_name(name, typed) do
    name_chars = :binary.bin_to_list(name)
    typed_chars = :binary.bin_to_list(typed)

    helper(name_chars, typed_chars, nil)
  end

  defp helper([], [], _prev), do: true

  # When the original name is exhausted, remaining typed chars must be repeats of the last matched char
  defp helper([], [h | t], prev) do
    if h == prev do
      helper([], t, prev)
    else
      false
    end
  end

  # Characters match directly
  defp helper([n | ns], [t | ts], _prev) when n == t do
    helper(ns, ts, n)
  end

  # Typed char is a long press of the previous character
  defp helper(name_rest, [t | ts], prev) when not is_nil(prev) and t == prev do
    helper(name_rest, ts, prev)
  end

  defp helper(_, _, _), do: false
end
```
