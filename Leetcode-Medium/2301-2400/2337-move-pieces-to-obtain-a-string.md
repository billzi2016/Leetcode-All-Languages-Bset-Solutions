# 2337. Move Pieces to Obtain a String

## Cpp

```cpp
class Solution {
public:
    bool canChange(string start, string target) {
        int n = start.size();
        int i = 0, j = 0;
        while (i < n || j < n) {
            while (i < n && start[i] == '_') ++i;
            while (j < n && target[j] == '_') ++j;
            if (i == n && j == n) return true;
            if (i == n || j == n) return false;
            if (start[i] != target[j]) return false;
            if (start[i] == 'L' && i < j) return false; // L can only move left
            if (start[i] == 'R' && i > j) return false; // R can only move right
            ++i;
            ++j;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canChange(String start, String target) {
        int n = start.length();
        int i = 0, j = 0;
        while (i < n || j < n) {
            while (i < n && start.charAt(i) == '_') i++;
            while (j < n && target.charAt(j) == '_') j++;
            if (i == n && j == n) return true;
            if (i == n || j == n) return false;
            char c1 = start.charAt(i);
            char c2 = target.charAt(j);
            if (c1 != c2) return false;
            if (c1 == 'L' && i < j) return false;
            if (c1 == 'R' && i > j) return false;
            i++;
            j++;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        i = j = 0
        while True:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            if i == n or j == n:
                # both should be at the end simultaneously
                return i == n and j == n

            if start[i] != target[j]:
                return False

            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1
```

## Python3

```python
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n or j < n:
            # skip '_' in start
            while i < n and start[i] == '_':
                i += 1
            # skip '_' in target
            while j < n and target[j] == '_':
                j += 1

            if i == n and j == n:
                return True
            if (i == n) != (j == n):
                return False

            if start[i] != target[j]:
                return False

            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool canChange(char* start, char* target) {
    int n = (int)strlen(start);
    int i = 0, j = 0;
    while (i < n || j < n) {
        while (i < n && start[i] == '_') i++;
        while (j < n && target[j] == '_') j++;

        if ((i == n) != (j == n)) return false;
        if (i == n && j == n) break;

        if (start[i] != target[j]) return false;

        if (start[i] == 'L' && i < j) return false;
        if (start[i] == 'R' && i > j) return false;

        i++;
        j++;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanChange(string start, string target)
    {
        int n = start.Length;
        int i = 0, j = 0;
        while (i < n || j < n)
        {
            while (i < n && start[i] == '_') i++;
            while (j < n && target[j] == '_') j++;

            if (i == n && j == n) return true;
            if (i == n || j == n) return false;

            if (start[i] != target[j]) return false;

            if (start[i] == 'L' && i < j) return false;
            if (start[i] == 'R' && i > j) return false;

            i++;
            j++;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} start
 * @param {string} target
 * @return {boolean}
 */
var canChange = function(start, target) {
    const n = start.length;
    let i = 0, j = 0;
    while (true) {
        while (i < n && start[i] === '_') i++;
        while (j < n && target[j] === '_') j++;
        if (i === n && j === n) return true;
        if (i === n || j === n) return false;
        const s = start[i];
        const t = target[j];
        if (s !== t) return false;
        if (s === 'L' && i < j) return false; // L can only move left
        if (s === 'R' && i > j) return false; // R can only move right
        i++;
        j++;
    }
};
```

## Typescript

```typescript
function canChange(start: string, target: string): boolean {
    const n = start.length;
    let i = 0, j = 0;
    while (i < n || j < n) {
        while (i < n && start[i] === '_') i++;
        while (j < n && target[j] === '_') j++;

        if (i === n && j === n) return true;
        if ((i === n) !== (j === n)) return false;

        const s = start[i];
        const t = target[j];

        if (s !== t) return false;
        if (s === 'L' && i < j) return false; // L can only move left
        if (s === 'R' && i > j) return false; // R can only move right

        i++;
        j++;
    }
    return true;
}
```

## Php

```php
class Solution {
    /**
     * @param String $start
     * @param String $target
     * @return Boolean
     */
    function canChange($start, $target) {
        $n = strlen($start);
        $i = 0;
        $j = 0;
        while (true) {
            while ($i < $n && $start[$i] === '_') {
                $i++;
            }
            while ($j < $n && $target[$j] === '_') {
                $j++;
            }

            if ($i == $n && $j == $n) {
                return true;
            }
            if ($i == $n || $j == $n) {
                return false;
            }

            if ($start[$i] !== $target[$j]) {
                return false;
            }

            if ($start[$i] === 'L' && $i < $j) {
                return false;
            }
            if ($start[$i] === 'R' && $i > $j) {
                return false;
            }

            $i++;
            $j++;
        }
    }
}
```

## Swift

```swift
class Solution {
    func canChange(_ start: String, _ target: String) -> Bool {
        let n = start.count
        if n != target.count { return false }
        let s = Array(start)
        let t = Array(target)
        var i = 0, j = 0
        while true {
            while i < n && s[i] == "_" { i += 1 }
            while j < n && t[j] == "_" { j += 1 }
            if i == n && j == n {
                return true
            }
            if (i == n) != (j == n) {
                return false
            }
            if s[i] != t[j] {
                return false
            }
            if s[i] == "L" && i < j {
                return false
            }
            if s[i] == "R" && i > j {
                return false
            }
            i += 1
            j += 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canChange(start: String, target: String): Boolean {
        val n = start.length
        var i = 0
        var j = 0
        while (i < n || j < n) {
            while (i < n && start[i] == '_') i++
            while (j < n && target[j] == '_') j++
            if (i == n && j == n) return true
            if (i == n || j == n) return false
            val c1 = start[i]
            val c2 = target[j]
            if (c1 != c2) return false
            if (c1 == 'L' && i < j) return false
            if (c1 == 'R' && i > j) return false
            i++
            j++
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canChange(String start, String target) {
    int n = start.length;
    int i = 0, j = 0;
    while (true) {
      while (i < n && start[i] == '_') i++;
      while (j < n && target[j] == '_') j++;
      if (i == n && j == n) return true;
      if (i == n || j == n) return false;
      if (start[i] != target[j]) return false;
      if (start[i] == 'L' && i < j) return false;
      if (start[i] == 'R' && i > j) return false;
      i++;
      j++;
    }
  }
}
```

## Golang

```go
func canChange(start string, target string) bool {
    n := len(start)
    i, j := 0, 0
    for i < n || j < n {
        for i < n && start[i] == '_' {
            i++
        }
        for j < n && target[j] == '_' {
            j++
        }

        if i == n && j == n {
            return true
        }
        if (i == n) != (j == n) {
            return false
        }

        if start[i] != target[j] {
            return false
        }

        if start[i] == 'L' && i < j {
            return false
        }
        if start[i] == 'R' && i > j {
            return false
        }

        i++
        j++
    }
    return true
}
```

## Ruby

```ruby
def can_change(start, target)
  n = start.length
  i = 0
  j = 0
  while i < n || j < n
    while i < n && start.getbyte(i) == ?_
      i += 1
    end
    while j < n && target.getbyte(j) == ?_
      j += 1
    end
    if (i == n) ^ (j == n)
      return false
    end
    break if i == n && j == n
    c1 = start.getbyte(i)
    c2 = target.getbyte(j)
    return false unless c1 == c2
    if c1 == ?L && i < j
      return false
    elsif c1 == ?R && i > j
      return false
    end
    i += 1
    j += 1
  end
  true
end
```

## Scala

```scala
object Solution {
  def canChange(start: String, target: String): Boolean = {
    val n = start.length
    var i = 0
    var j = 0

    while (i < n && j < n) {
      while (i < n && start.charAt(i) == '_') i += 1
      while (j < n && target.charAt(j) == '_') j += 1

      if ((i == n) != (j == n)) return false
      if (i == n && j == n) return true

      val cStart = start.charAt(i)
      val cTarget = target.charAt(j)

      if (cStart != cTarget) return false

      if (cStart == 'L' && i < j) return false
      if (cStart == 'R' && i > j) return false

      i += 1
      j += 1
    }

    while (i < n && start.charAt(i) == '_') i += 1
    while (j < n && target.charAt(j) == '_') j += 1

    i == n && j == n
  }
}
```

## Rust

```rust
impl Solution {
    pub fn can_change(start: String, target: String) -> bool {
        let s = start.as_bytes();
        let t = target.as_bytes();
        let n = s.len();
        let mut i = 0usize;
        let mut j = 0usize;

        while i < n || j < n {
            while i < n && s[i] == b'_' {
                i += 1;
            }
            while j < n && t[j] == b'_' {
                j += 1;
            }

            if i == n && j == n {
                return true;
            }
            if (i == n) != (j == n) {
                return false;
            }

            let cs = s[i];
            let ct = t[j];

            if cs != ct {
                return false;
            }
            if cs == b'L' && i < j {
                return false;
            }
            if cs == b'R' && i > j {
                return false;
            }

            i += 1;
            j += 1;
        }

        true
    }
}
```

## Racket

```racket
(define/contract (can-change start target)
  (-> string? string? boolean?)
  (let ((n (string-length start)))
    (let loop ((i 0) (j 0))
      (cond
        [(and (= i n) (= j n)) #t]                     ; both strings fully processed
        [else
         ;; advance i to next non '_' in start
         (define i2
           (let skip ((k i))
             (if (or (= k n) (not (char=? (string-ref start k) #\_)))
                 k
                 (skip (+ k 1)))))
         ;; advance j to next non '_' in target
         (define j2
           (let skip ((k j))
             (if (or (= k n) (not (char=? (string-ref target k) #\_)))
                 k
                 (skip (+ k 1)))))
         (cond
           [(and (= i2 n) (= j2 n)) #t]                ; both reached end after skipping underscores
           [(or (= i2 n) (= j2 n)) #f]                 ; one ends earlier than the other
           [else
            (let ((c1 (string-ref start i2))
                  (c2 (string-ref target j2)))
              (if (not (char=? c1 c2))
                  #f                                   ; different piece types
                  (cond
                    [(char=? c1 #\L)
                     (if (< i2 j2)                      ; L cannot move right
                         #f
                         (loop (+ i2 1) (+ j2 1)))]
                    [(char=? c1 #\R)
                     (if (> i2 j2)                      ; R cannot move left
                         #f
                         (loop (+ i2 1) (+ j2 1)))]
                    [else                               ; should never happen for '_' as they are skipped
                     (loop (+ i2 1) (+ j2 1))])))])))))))
```

## Erlang

```erlang
-spec can_change(unicode:unicode_binary(), unicode:unicode_binary()) -> boolean().
can_change(Start, Target) ->
    Len = byte_size(Start),
    case byte_size(Target) of
        Len -> loop(0, 0, Start, Target, Len);
        _   -> false
    end.

loop(I, J, S, T, N) when I >= N, J >= N ->
    true;
loop(I, J, S, T, N) ->
    I1 = skip_underscores(S, I, N),
    J1 = skip_underscores(T, J, N),
    case {I1 >= N, J1 >= N} of
        {true, true}   -> true;
        {true, false}  -> false;
        {false, true}  -> false;
        {false, false} ->
            CharS = binary:at(S, I1),
            CharT = binary:at(T, J1),
            if
                CharS =/= CharT -> false;
                CharS == $L, I1 < J1 -> false;   % L can only move left
                CharS == $R, I1 > J1 -> false;   % R can only move right
                true ->
                    loop(I1 + 1, J1 + 1, S, T, N)
            end
    end.

skip_underscores(Bin, Idx, Len) when Idx >= Len ->
    Idx;
skip_underscores(Bin, Idx, Len) ->
    case binary:at(Bin, Idx) of
        $_ -> skip_underscores(Bin, Idx + 1, Len);
        _  -> Idx
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_change(start :: String.t(), target :: String.t()) :: boolean()
  def can_change(start, target) do
    s = start |> String.to_charlist() |> Enum.with_index()
    t = target |> String.to_charlist() |> Enum.with_index()

    s_filtered = Enum.filter(s, fn {c, _} -> c != ?_ end)
    t_filtered = Enum.filter(t, fn {c, _} -> c != ?_ end)

    if length(s_filtered) != length(t_filtered) do
      false
    else
      Enum.reduce_while(Enum.zip(s_filtered, t_filtered), true, fn
        {{cs, is}, {ct, it}}, _acc ->
          cond do
            cs != ct -> {:halt, false}
            cs == ?L and is < it -> {:halt, false}
            cs == ?R and is > it -> {:halt, false}
            true -> {:cont, true}
          end
      end)
    end
  end
end
```
