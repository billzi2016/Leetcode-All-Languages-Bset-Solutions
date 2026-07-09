# 0777. Swap Adjacent in LR String

## Cpp

```cpp
class Solution {
public:
    bool canTransform(string start, string result) {
        int n = start.size();
        int i = 0, j = 0;
        while (i < n && j < n) {
            while (i < n && start[i] == 'X') ++i;
            while (j < n && result[j] == 'X') ++j;
            if (i == n || j == n) break;
            if (start[i] != result[j]) return false;
            if (start[i] == 'L' && i < j) return false; // L moves left
            if (start[i] == 'R' && i > j) return false; // R moves right
            ++i;
            ++j;
        }
        while (i < n) {
            if (start[i] != 'X') return false;
            ++i;
        }
        while (j < n) {
            if (result[j] != 'X') return false;
            ++j;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canTransform(String start, String result) {
        int n = start.length();
        int i = 0, j = 0;
        while (i < n && j < n) {
            while (i < n && start.charAt(i) == 'X') i++;
            while (j < n && result.charAt(j) == 'X') j++;
            if (i == n || j == n) break;
            char c1 = start.charAt(i);
            char c2 = result.charAt(j);
            if (c1 != c2) return false;
            if (c1 == 'L' && i < j) return false; // L can only move left
            if (c1 == 'R' && i > j) return false; // R can only move right
            i++;
            j++;
        }
        while (i < n) {
            if (start.charAt(i) != 'X') return false;
            i++;
        }
        while (j < n) {
            if (result.charAt(j) != 'X') return false;
            j++;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        n = len(start)
        i = j = 0
        while True:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            if i == n or j == n:
                break
            if start[i] != result[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if result[j] != 'X':
                return False
            j += 1
        return True
```

## Python3

```python
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        i = j = 0
        while True:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            if i == n and j == n:
                return True
            if (i == n) != (j == n):
                return False
            if start[i] != result[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool canTransform(char* start, char* result) {
    int n = strlen(start);
    int i = 0, j = 0;
    while (i < n && j < n) {
        while (i < n && start[i] == 'X') i++;
        while (j < n && result[j] == 'X') j++;
        if (i == n || j == n) break;
        if (start[i] != result[j]) return false;
        if (start[i] == 'L' && i < j) return false; // L can't move right
        if (start[i] == 'R' && i > j) return false; // R can't move left
        i++;
        j++;
    }
    while (i < n) {
        if (start[i] != 'X') return false;
        i++;
    }
    while (j < n) {
        if (result[j] != 'X') return false;
        j++;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanTransform(string start, string result)
    {
        int n = start.Length;
        int i = 0, j = 0;

        while (i < n && j < n)
        {
            while (i < n && start[i] == 'X') i++;
            while (j < n && result[j] == 'X') j++;

            if (i == n || j == n) break;

            if (start[i] != result[j]) return false;

            if (start[i] == 'L' && i < j) return false; // L can only move left
            if (start[i] == 'R' && i > j) return false; // R can only move right

            i++;
            j++;
        }

        while (i < n)
        {
            if (start[i] != 'X') return false;
            i++;
        }
        while (j < n)
        {
            if (result[j] != 'X') return false;
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
 * @param {string} result
 * @return {boolean}
 */
var canTransform = function(start, result) {
    const n = start.length;
    let i = 0, j = 0;
    while (i < n && j < n) {
        while (i < n && start[i] === 'X') i++;
        while (j < n && result[j] === 'X') j++;
        if (i === n || j === n) break;
        if (start[i] !== result[j]) return false;
        if (start[i] === 'L' && i < j) return false; // L moves left only
        if (start[i] === 'R' && i > j) return false; // R moves right only
        i++;
        j++;
    }
    while (i < n) {
        if (start[i] !== 'X') return false;
        i++;
    }
    while (j < n) {
        if (result[j] !== 'X') return false;
        j++;
    }
    return true;
};
```

## Typescript

```typescript
function canTransform(start: string, result: string): boolean {
    const n = start.length;
    let i = 0, j = 0;
    while (i < n || j < n) {
        while (i < n && start[i] === 'X') i++;
        while (j < n && result[j] === 'X') j++;
        if (i === n && j === n) return true;
        if ((i === n) !== (j === n)) return false;
        const c1 = start[i];
        const c2 = result[j];
        if (c1 !== c2) return false;
        if (c1 === 'L' && i < j) return false; // L can only move left
        if (c1 === 'R' && i > j) return false; // R can only move right
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
     * @param String $result
     * @return Boolean
     */
    function canTransform($start, $result) {
        $n = strlen($start);
        $i = 0;
        $j = 0;

        while ($i < $n && $j < $n) {
            // skip 'X' in start
            while ($i < $n && $start[$i] === 'X') {
                $i++;
            }
            // skip 'X' in result
            while ($j < $n && $result[$j] === 'X') {
                $j++;
            }

            if ($i == $n || $j == $n) {
                break;
            }

            if ($start[$i] !== $result[$j]) {
                return false;
            }

            // L can only move left: start index must be >= result index
            if ($start[$i] === 'L' && $i < $j) {
                return false;
            }
            // R can only move right: start index must be <= result index
            if ($start[$i] === 'R' && $i > $j) {
                return false;
            }

            $i++;
            $j++;
        }

        // remaining characters in start should all be 'X'
        while ($i < $n) {
            if ($start[$i] !== 'X') {
                return false;
            }
            $i++;
        }

        // remaining characters in result should all be 'X'
        while ($j < $n) {
            if ($result[$j] !== 'X') {
                return false;
            }
            $j++;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canTransform(_ start: String, _ result: String) -> Bool {
        let s = Array(start)
        let t = Array(result)
        let n = s.count
        var i = 0
        var j = 0
        
        while true {
            while i < n && s[i] == "X" { i += 1 }
            while j < n && t[j] == "X" { j += 1 }
            
            if i == n || j == n { break }
            
            if s[i] != t[j] { return false }
            
            if s[i] == "L" && i < j { return false }
            if s[i] == "R" && i > j { return false }
            
            i += 1
            j += 1
        }
        
        while i < n && s[i] == "X" { i += 1 }
        while j < n && t[j] == "X" { j += 1 }
        
        return i == n && j == n
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canTransform(start: String, result: String): Boolean {
        val n = start.length
        var i = 0
        var j = 0
        while (i < n && j < n) {
            while (i < n && start[i] == 'X') i++
            while (j < n && result[j] == 'X') j++
            if (i == n && j == n) return true
            if (i == n || j == n) return false
            if (start[i] != result[j]) return false
            when (start[i]) {
                'L' -> if (i < j) return false
                'R' -> if (i > j) return false
            }
            i++
            j++
        }
        while (i < n) {
            if (start[i] != 'X') return false
            i++
        }
        while (j < n) {
            if (result[j] != 'X') return false
            j++
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canTransform(String start, String result) {
    int n = start.length;
    int i = 0, j = 0;
    while (true) {
      while (i < n && start[i] == 'X') i++;
      while (j < n && result[j] == 'X') j++;
      if (i == n && j == n) return true;
      if ((i == n) != (j == n)) return false;
      if (start[i] != result[j]) return false;
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
func canTransform(start string, result string) bool {
	n := len(start)
	i, j := 0, 0
	for i < n && j < n {
		for i < n && start[i] == 'X' {
			i++
		}
		for j < n && result[j] == 'X' {
			j++
		}
		if i == n && j == n {
			return true
		}
		if (i == n) != (j == n) {
			return false
		}
		if start[i] != result[j] {
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
	for i < n {
		if start[i] != 'X' {
			return false
		}
		i++
	}
	for j < n {
		if result[j] != 'X' {
			return false
		}
		j++
	}
	return true
}
```

## Ruby

```ruby
def can_transform(start, result)
  n = start.length
  i = 0
  j = 0
  x = 'X'.ord
  l = 'L'.ord
  r = 'R'.ord
  while i < n && j < n
    i += 1 while i < n && start.getbyte(i) == x
    j += 1 while j < n && result.getbyte(j) == x
    break if i == n || j == n
    s = start.getbyte(i)
    t = result.getbyte(j)
    return false if s != t
    if s == l
      return false if i < j
    else # r
      return false if i > j
    end
    i += 1
    j += 1
  end
  i += 1 while i < n && start.getbyte(i) == x
  j += 1 while j < n && result.getbyte(j) == x
  i == n && j == n
end
```

## Scala

```scala
object Solution {
    def canTransform(start: String, result: String): Boolean = {
        val n = start.length
        var i = 0
        var j = 0
        while (i < n && j < n) {
            while (i < n && start.charAt(i) == 'X') i += 1
            while (j < n && result.charAt(j) == 'X') j += 1
            if (i == n && j == n) return true
            if ((i == n) != (j == n)) return false
            val c1 = start.charAt(i)
            val c2 = result.charAt(j)
            if (c1 != c2) return false
            if (c1 == 'L' && i < j) return false
            if (c1 == 'R' && i > j) return false
            i += 1
            j += 1
        }
        while (i < n && start.charAt(i) == 'X') i += 1
        while (j < n && result.charAt(j) == 'X') j += 1
        i == n && j == n
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_transform(start: String, result: String) -> bool {
        let s = start.as_bytes();
        let t = result.as_bytes();
        let n = s.len();
        let mut i = 0usize;
        let mut j = 0usize;

        while i < n && j < n {
            while i < n && s[i] == b'X' {
                i += 1;
            }
            while j < n && t[j] == b'X' {
                j += 1;
            }

            if i == n || j == n {
                break;
            }

            if s[i] != t[j] {
                return false;
            }

            if s[i] == b'L' && i < j {
                return false;
            }
            if s[i] == b'R' && i > j {
                return false;
            }

            i += 1;
            j += 1;
        }

        while i < n {
            if s[i] != b'X' {
                return false;
            }
            i += 1;
        }
        while j < n {
            if t[j] != b'X' {
                return false;
            }
            j += 1;
        }

        true
    }
}
```

## Racket

```racket
(define/contract (can-transform start result)
  (-> string? string? boolean?)
  (let* ((n (string-length start)))
    (if (not (= n (string-length result)))
        #f
        (let loop ((i 0) (j 0))
          (cond
            [(and (= i n) (= j n)) #t]
            [else
             (define (advance-i k)
               (if (or (= k n) (not (char=? (string-ref start k) #\X)))
                   k
                   (advance-i (+ k 1))))
             (define (advance-j k)
               (if (or (= k n) (not (char=? (string-ref result k) #\X)))
                   k
                   (advance-j (+ k 1))))
             (let ((i2 (advance-i i))
                   (j2 (advance-j j)))
               (cond
                 [(and (= i2 n) (= j2 n)) #t]
                 [(or (= i2 n) (= j2 n)) #f] ; one string has extra non‑X chars
                 [else
                  (let ((c1 (string-ref start i2))
                        (c2 (string-ref result j2)))
                    (if (not (char=? c1 c2))
                        #f
                        (cond
                          [(char=? c1 #\L)
                           (if (> i2 j2) ; L cannot move right
                               #f
                               (loop (+ i2 1) (+ j2 1)))]
                          [(char=? c1 #\R)
                           (if (< i2 j2) ; R cannot move left
                               #f
                               (loop (+ i2 1) (+ j2 1)))]
                          [else ; should never happen
                           (loop (+ i2 1) (+ j2 1))])))])))))))))))
```

## Erlang

```erlang
-module(solution).
-export([can_transform/2]).

-spec can_transform(unicode:unicode_binary(), unicode:unicode_binary()) -> boolean().
can_transform(Start, Result) ->
    LenS = byte_size(Start),
    LenR = byte_size(Result),
    if
        LenS =/= LenR -> false;
        true -> go(0, 0, Start, Result, LenS)
    end.

go(I, J, Start, Result, Len) ->
    I1 = skipX(I, Start, Len),
    J1 = skipX(J, Result, Len),
    if
        I1 == Len andalso J1 == Len -> true;
        I1 == Len orelse J1 == Len -> false;
        true ->
            CharS = binary:at(Start, I1),
            CharR = binary:at(Result, J1),
            case CharS == CharR of
                false -> false;
                true ->
                    case CharS of
                        $L when I1 < J1 -> false;
                        $R when I1 > J1 -> false;
                        _ -> go(I1 + 1, J1 + 1, Start, Result, Len)
                    end
            end
    end.

skipX(Index, Bin, Len) ->
    case Index >= Len of
        true -> Index;
        false ->
            case binary:at(Bin, Index) of
                $X -> skipX(Index + 1, Bin, Len);
                _ -> Index
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_transform(start :: String.t(), result :: String.t()) :: boolean()
  def can_transform(start, result) do
    s = String.to_charlist(start)
    r = String.to_charlist(result)
    check(s, 0, r, 0)
  end

  defp check(s_list, s_idx, r_list, r_idx) do
    {s_rest, s_i} = skip_x(s_list, s_idx)
    {r_rest, r_j} = skip_x(r_list, r_idx)

    cond do
      s_rest == [] and r_rest == [] ->
        true

      s_rest == [] or r_rest == [] ->
        false

      true ->
        [c1 | tail_s] = s_rest
        [c2 | tail_r] = r_rest

        if c1 != c2 do
          false
        else
          case c1 do
            ?L when s_i < r_j -> false
            ?R when s_i > r_j -> false
            _ ->
              check(tail_s, s_i + 1, tail_r, r_j + 1)
          end
        end
    end
  end

  defp skip_x([], idx), do: {[], idx}
  defp skip_x([?X | rest], idx), do: skip_x(rest, idx + 1)
  defp skip_x(list, idx), do: {list, idx}
end
```
