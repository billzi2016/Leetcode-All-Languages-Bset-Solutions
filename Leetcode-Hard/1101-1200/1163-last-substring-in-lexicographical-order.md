# 1163. Last Substring in Lexicographical Order

## Cpp

```cpp
class Solution {
public:
    string lastSubstring(string s) {
        int n = s.size();
        int i = 0, j = 1, k = 0;
        while (j + k < n) {
            if (s[i + k] == s[j + k]) {
                ++k;
                continue;
            }
            if (s[i + k] > s[j + k]) {
                // current best i is better, skip j forward
                j = j + k + 1;
            } else {
                // found a better start at j
                i = max(i + k + 1, j);
                j = i + 1;
            }
            k = 0;
        }
        return s.substr(i);
    }
};
```

## Java

```java
class Solution {
    public String lastSubstring(String s) {
        int n = s.length();
        int i = 0, j = 1, k = 0;
        while (j + k < n) {
            char a = s.charAt(i + k);
            char b = s.charAt(j + k);
            if (a == b) {
                k++;
            } else if (a > b) {
                // current best is better, skip the inferior start
                j = j + k + 1;
                k = 0;
            } else { // a < b
                i = Math.max(i + k + 1, j);
                j = i + 1;
                k = 0;
            }
        }
        return s.substring(i);
    }
}
```

## Python

```python
class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        i, j, k = 0, 1, 0
        while j + k < n:
            a = s[i + k]
            b = s[j + k]
            if a == b:
                k += 1
                continue
            if a > b:
                # skip the suffix starting at j
                j = j + k + 1
            else:
                # move i to the better candidate
                i = max(i + k + 1, j)
                j = i + 1
            k = 0
        return s[i:]
```

## Python3

```python
class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j, k = 0, 1, 0
        while j + k < n:
            a, b = s[i + k], s[j + k]
            if a == b:
                k += 1
                continue
            if a < b:
                i = max(i + k + 1, j)
                j = i + 1
            else:
                j = j + k + 1
            k = 0
        return s[i:]
```

## C

```c
#include <stdlib.h>
#include <string.h>

static inline int max_int(int a, int b) { return a > b ? a : b; }

char* lastSubstring(char* s) {
    int n = (int)strlen(s);
    int i = 0, j = 1, k = 0;
    while (j + k < n) {
        if (s[i + k] == s[j + k]) {
            ++k;
            continue;
        }
        if (s[i + k] > s[j + k]) {
            j = j + k + 1;
        } else {
            i = max_int(i + k + 1, j);
            j = i + 1;
        }
        k = 0;
    }
    int start = i;
    int len = n - start;
    char* res = (char*)malloc(len + 1);
    memcpy(res, s + start, len);
    res[len] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string LastSubstring(string s) {
        int n = s.Length;
        char[] a = s.ToCharArray();
        int i = 0, j = 1, k = 0;
        while (j + k < n) {
            if (a[i + k] == a[j + k]) {
                k++;
                continue;
            }
            if (a[i + k] > a[j + k]) {
                // substring at j is smaller
                j = j + k + 1;
            } else {
                // substring at i is smaller
                i = Math.Max(i + k + 1, j);
                j = i + 1;
            }
            k = 0;
        }
        return s.Substring(i);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var lastSubstring = function(s) {
    const n = s.length;
    let i = 0, j = 1, k = 0;
    while (j + k < n) {
        const a = s.charCodeAt(i + k);
        const b = s.charCodeAt(j + k);
        if (a === b) {
            k++;
        } else if (a < b) {
            i = Math.max(i + k + 1, j);
            j = i + 1;
            k = 0;
        } else { // a > b
            j = j + k + 1;
            k = 0;
        }
    }
    return s.substring(i);
};
```

## Typescript

```typescript
function lastSubstring(s: string): string {
    const n = s.length;
    let i = 0, j = 1, k = 0;
    while (j + k < n) {
        const a = s.charCodeAt(i + k);
        const b = s.charCodeAt(j + k);
        if (a === b) {
            k++;
        } else if (a < b) {
            i = Math.max(i + k + 1, j);
            j = i + 1;
            k = 0;
        } else { // a > b
            j = j + k + 1;
            k = 0;
        }
    }
    return s.substring(i);
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function lastSubstring($s) {
        $n = strlen($s);
        $i = 0;
        $j = 1;
        $k = 0;
        while ($j + $k < $n) {
            $a = $s[$i + $k];
            $b = $s[$j + $k];
            if ($a === $b) {
                $k++;
                continue;
            }
            if ($a < $b) {
                $i = max($i + $k + 1, $j);
                $j = $i + 1;
            } else {
                $j = $j + $k + 1;
            }
            $k = 0;
        }
        return substr($s, $i);
    }
}
```

## Swift

```swift
class Solution {
    func lastSubstring(_ s: String) -> String {
        let bytes = Array(s.utf8)
        let n = bytes.count
        var i = 0
        var j = 1
        var k = 0
        
        while j + k < n {
            if bytes[i + k] == bytes[j + k] {
                k += 1
            } else if bytes[i + k] < bytes[j + k] {
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            } else {
                j = j + k + 1
                k = 0
            }
        }
        
        return String(bytes: bytes[i...], encoding: .utf8)!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lastSubstring(s: String): String {
        val n = s.length
        var i = 0
        var j = 1
        var k = 0
        while (j + k < n) {
            val a = s[i + k]
            val b = s[j + k]
            if (a == b) {
                k++
                continue
            }
            if (a > b) {
                j = j + k + 1
            } else {
                i = maxOf(i + k + 1, j)
                j = i + 1
            }
            k = 0
        }
        return s.substring(i)
    }
}
```

## Dart

```dart
class Solution {
  String lastSubstring(String s) {
    int n = s.length;
    int i = 0, j = 1;
    while (i < n && j < n) {
      int k = 0;
      // compare characters of the two candidate suffixes
      while (i + k < n &&
          j + k < n &&
          s.codeUnitAt(i + k) == s.codeUnitAt(j + k)) {
        k++;
      }
      if (j + k >= n) break; // suffix at j exhausted, cannot be better
      if (i + k >= n) {
        i = j;
        break; // suffix at i exhausted, j is better
      }
      if (s.codeUnitAt(i + k) > s.codeUnitAt(j + k)) {
        // suffix starting at j is smaller
        j = j + k + 1;
      } else {
        // suffix starting at i is smaller
        i = i + k + 1;
        if (i <= j) i = j + 1;
      }
    }
    int start = i < j ? i : j;
    return s.substring(start);
  }
}
```

## Golang

```go
func lastSubstring(s string) string {
	n := len(s)
	if n == 0 {
		return ""
	}
	i, j, k := 0, 1, 0
	for j+k < n {
		a := s[i+k]
		b := s[j+k]
		if a == b {
			k++
			continue
		}
		if a < b {
			// move i forward past the inferior segment
			if i+k+1 > j {
				i = i + k + 1
			} else {
				i = j
			}
			j = i + 1
			k = 0
		} else { // a > b
			j = j + k + 1
			k = 0
		}
	}
	return s[i:]
}
```

## Ruby

```ruby
def last_substring(s)
  n = s.length
  i = 0
  j = 1
  k = 0
  while j + k < n
    a = s.getbyte(i + k)
    b = s.getbyte(j + k)
    if a == b
      k += 1
    elsif a > b
      j = j + k + 1
      k = 0
    else
      i = [i + k + 1, j].max
      j = i + 1
      k = 0
    end
  end
  s[i..-1]
end
```

## Scala

```scala
object Solution {
    def lastSubstring(s: String): String = {
        val n = s.length
        var i = 0
        var j = 1
        var k = 0
        while (j + k < n) {
            val a = s.charAt(i + k)
            val b = s.charAt(j + k)
            if (a == b) {
                k += 1
            } else if (a > b) {
                j = j + k + 1
                k = 0
            } else {
                i = Math.max(i + k + 1, j)
                j = i + 1
                k = 0
            }
        }
        s.substring(i)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn last_substring(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return "".to_string();
        }
        let mut i = 0usize;
        let mut j = 1usize;
        let mut k = 0usize;
        while j + k < n {
            if bytes[i + k] == bytes[j + k] {
                k += 1;
                continue;
            }
            if bytes[i + k] > bytes[j + k] {
                j = j + k + 1;
            } else {
                i = j;
                j = i + 1;
            }
            k = 0;
        }
        s[i..].to_string()
    }
}
```

## Racket

```racket
(define/contract (last-substring s)
  (-> string? string?)
  (let* ((n (string-length s)))
    (let loop ((i 0) (j 1) (k 0))
      (if (>= (+ j k) n)
          (substring s i n)
          (let ((a (string-ref s (+ i k)))
                (b (string-ref s (+ j k))))
            (cond
              [(char=? a b) (loop i j (+ k 1))]
              [(char<? a b)
               (let* ((new-i (max (+ i k 1) j))
                      (new-j (+ new-i 1)))
                 (if (>= new-i n)
                     (substring s new-i n)
                     (loop new-i new-j 0)))]
              [else
               (let ((new-j (+ j k 1)))
                 (if (>= new-j n)
                     (substring s i n)
                     (loop i new-j 0)))]))))))
```

## Erlang

```erlang
-module(solution).
-export([last_substring/1]).

-spec last_substring(unicode:unicode_binary()) -> unicode:unicode_binary().
last_substring(S) ->
    N = byte_size(S),
    Start = loop(S, N, 0, 1, 0),
    binary:part(S, Start, N - Start).

loop(_S, _N, I, J, _K) when J >= _N -> I;
loop(S, N, I, J, K) ->
    case J + K >= N of
        true -> I;
        false ->
            CharI = binary:at(S, I + K),
            CharJ = binary:at(S, J + K),
            if
                CharI == CharJ ->
                    loop(S, N, I, J, K + 1);
                CharI < CharJ ->
                    NewI0 = I + K + 1,
                    NewI = case NewI0 > J of
                               true -> NewI0;
                               false -> J
                           end,
                    NewJ = NewI + 1,
                    loop(S, N, NewI, NewJ, 0);
                true ->
                    NewJ = J + K + 1,
                    loop(S, N, I, NewJ, 0)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec last_substring(String.t()) :: String.t()
  def last_substring(s) do
    start = max_suffix(s)
    n = byte_size(s)
    :binary.part(s, start, n - start)
  end

  defp max_suffix(s) do
    n = byte_size(s)
    loop(0, 1, 0, s, n)
  end

  defp loop(i, j, k, _s, n) when j + k >= n, do: i

  defp loop(i, j, k, s, n) do
    ci = :binary.at(s, i + k)
    cj = :binary.at(s, j + k)

    cond do
      ci == cj ->
        loop(i, j, k + 1, s, n)

      ci < cj ->
        # start new candidate at j
        loop(j, j + 1, 0, s, n)

      true ->
        new_j = j + k + 1
        new_j = if new_j <= i, do: i + 1, else: new_j
        loop(i, new_j, 0, s, n)
    end
  end
end
```
