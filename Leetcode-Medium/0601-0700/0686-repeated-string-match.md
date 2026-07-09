# 0686. Repeated String Match

## Cpp

```cpp
class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        int n = a.size(), m = b.size();
        int repeat = (m + n - 1) / n; // minimum repeats to cover b's length
        string s;
        s.reserve((repeat + 1) * n);
        for (int i = 0; i < repeat; ++i) s += a;
        if (s.find(b) != string::npos) return repeat;
        s += a;
        if (s.find(b) != string::npos) return repeat + 1;
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int repeatedStringMatch(String a, String b) {
        int lenA = a.length();
        int lenB = b.length();
        int repeat = (lenB + lenA - 1) / lenA; // ceil division
        
        StringBuilder sb = new StringBuilder(lenA * (repeat + 1));
        for (int i = 0; i < repeat; i++) {
            sb.append(a);
        }
        if (sb.indexOf(b) != -1) {
            return repeat;
        }
        sb.append(a);
        if (sb.indexOf(b) != -1) {
            return repeat + 1;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        la, lb = len(a), len(b)
        # Minimum repeats needed to reach length of b
        repeat = (lb + la - 1) // la  # ceil division
        s = a * repeat
        if b in s:
            return repeat
        s += a
        if b in s:
            return repeat + 1
        return -1
```

## Python3

```python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        la, lb = len(a), len(b)
        repeat = -(-lb // la)  # ceil division
        s = a * repeat
        if b in s:
            return repeat
        s += a
        if b in s:
            return repeat + 1
        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>

int repeatedStringMatch(char* a, char* b) {
    size_t la = strlen(a);
    size_t lb = strlen(b);
    if (la == 0) return -1;

    int repeat = (int)((lb + la - 1) / la); // ceil(lb/la)

    size_t max_len = (size_t)(repeat + 2) * la; // enough for repeat+1 copies
    char *s = (char *)malloc(max_len + 1);
    if (!s) return -1;

    size_t pos = 0;
    for (int i = 0; i < repeat; ++i) {
        memcpy(s + pos, a, la);
        pos += la;
    }
    s[pos] = '\0';

    if (strstr(s, b)) {
        free(s);
        return repeat;
    }

    // add one more copy
    memcpy(s + pos, a, la);
    pos += la;
    s[pos] = '\0';

    if (strstr(s, b)) {
        free(s);
        return repeat + 1;
    }

    free(s);
    return -1;
}
```

## Csharp

```csharp
using System.Text;

public class Solution {
    public int RepeatedStringMatch(string a, string b) {
        if (a.Length == 0) return -1;
        var sb = new StringBuilder();
        int repeat = (b.Length + a.Length - 1) / a.Length; // ceil division
        for (int i = 0; i < repeat; i++) sb.Append(a);
        string s = sb.ToString();
        if (s.Contains(b)) return repeat;
        sb.Append(a);
        s = sb.ToString();
        if (s.Contains(b)) return repeat + 1;
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var repeatedStringMatch = function(a, b) {
    const repeat = Math.ceil(b.length / a.length);
    let s = a.repeat(repeat);
    if (s.includes(b)) return repeat;
    s += a;
    if (s.includes(b)) return repeat + 1;
    return -1;
};
```

## Typescript

```typescript
function repeatedStringMatch(a: string, b: string): number {
    const repeatCount = Math.ceil(b.length / a.length);
    let combined = a.repeat(repeatCount);
    if (combined.includes(b)) return repeatCount;
    combined += a;
    if (combined.includes(b)) return repeatCount + 1;
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function repeatedStringMatch($a, $b) {
        $lenA = strlen($a);
        $lenB = strlen($b);
        // Minimum repeats needed to reach length of b
        $repeat = intdiv($lenB + $lenA - 1, $lenA);
        $candidate = str_repeat($a, $repeat);
        if (strpos($candidate, $b) !== false) {
            return $repeat;
        }
        // One extra repeat might be enough
        $candidate .= $a;
        if (strpos($candidate, $b) !== false) {
            return $repeat + 1;
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func repeatedStringMatch(_ a: String, _ b: String) -> Int {
        let aLen = a.count
        let bLen = b.count
        var repeats = (bLen + aLen - 1) / aLen   // ceil division
        
        var combined = ""
        combined.reserveCapacity(aLen * (repeats + 1))
        for _ in 0..<repeats {
            combined += a
        }
        if combined.contains(b) {
            return repeats
        }
        combined += a
        repeats += 1
        if combined.contains(b) {
            return repeats
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun repeatedStringMatch(a: String, b: String): Int {
        val sb = StringBuilder()
        var count = 0
        while (sb.length < b.length) {
            sb.append(a)
            count++
        }
        if (sb.indexOf(b) >= 0) return count
        sb.append(a)
        count++
        return if (sb.indexOf(b) >= 0) count else -1
    }
}
```

## Dart

```dart
class Solution {
  int repeatedStringMatch(String a, String b) {
    int repeat = (b.length + a.length - 1) ~/ a.length; // ceil division
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < repeat; i++) {
      sb.write(a);
    }
    String s = sb.toString();
    if (s.contains(b)) return repeat;
    sb.write(a);
    s = sb.toString();
    if (s.contains(b)) return repeat + 1;
    return -1;
  }
}
```

## Golang

```go
package main

import "strings"

func repeatedStringMatch(a string, b string) int {
	lenA := len(a)
	lenB := len(b)

	// Minimum repeats to reach length of b
	repeat := (lenB + lenA - 1) / lenA
	s := strings.Repeat(a, repeat)

	if strings.Contains(s, b) {
		return repeat
	}
	// One extra repeat might be needed for overlap
	s += a
	if strings.Contains(s, b) {
		return repeat + 1
	}
	return -1
}
```

## Ruby

```ruby
def repeated_string_match(a, b)
  repeats = (b.length + a.length - 1) / a.length
  s = a * repeats
  return repeats if s.include?(b)
  s << a
  repeats += 1
  return repeats if s.include?(b)
  -1
end
```

## Scala

```scala
object Solution {
    def repeatedStringMatch(a: String, b: String): Int = {
        val lenA = a.length
        val lenB = b.length
        // Minimum repetitions to reach length >= lenB
        var times = (lenB + lenA - 1) / lenA
        var sb = new StringBuilder()
        for (_ <- 0 until times) sb.append(a)
        if (sb.toString.contains(b)) return times
        sb.append(a) // one more repetition
        if (sb.toString.contains(b)) return times + 1
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn repeated_string_match(a: String, b: String) -> i32 {
        let a_len = a.len();
        let b_len = b.len();

        // Minimum repetitions needed so that the length of repeated a >= length of b
        let mut repeat = (b_len + a_len - 1) / a_len; // ceil division

        let mut s = a.clone().repeat(repeat);
        if s.contains(&b) {
            return repeat as i32;
        }

        // One more repetition might be necessary to cover the overlap case
        s.push_str(&a);
        repeat += 1;
        if s.contains(&b) {
            return repeat as i32;
        }

        -1
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (repeated-string-match a b)
  (-> string? string? exact-integer?)
  (let* ([len-a (string-length a)]
         [len-b (string-length b)]
         [repeat-count (ceiling (/ len-b len-a))])
    (define (make-rep n)
      (apply string-append (build-list n (λ (_) a))))
    (let ([s1 (make-rep repeat-count)])
      (cond
        [(string-contains? s1 b) repeat-count]
        [else
         (let ([s2 (make-rep (+ repeat-count 1))])
           (if (string-contains? s2 b)
               (+ repeat-count 1)
               -1))]))))
```

## Erlang

```erlang
-export([repeated_string_match/2]).

-spec repeated_string_match(A :: unicode:unicode_binary(),
                            B :: unicode:unicode_binary()) -> integer().
repeated_string_match(A, B) ->
    LenA = byte_size(A),
    LenB = byte_size(B),
    Repeats0 = (LenB + LenA - 1) div LenA,
    case has_substring(A, B, Repeats0) of
        true -> Repeats0;
        false ->
            case has_substring(A, B, Repeats0 + 1) of
                true -> Repeats0 + 1;
                false -> -1
            end
    end.

has_substring(A, B, Count) ->
    S = repeat_binary(A, Count),
    case binary:match(S, B) of
        nomatch -> false;
        _ -> true
    end.

repeat_binary(A, Count) when Count >= 0 ->
    repeat_binary(A, Count, <<>>).

repeat_binary(_A, 0, Acc) -> Acc;
repeat_binary(A, N, Acc) when N > 0 ->
    repeat_binary(A, N - 1, <<Acc/binary, A/binary>>).
```

## Elixir

```elixir
defmodule Solution do
  @spec repeated_string_match(a :: String.t(), b :: String.t()) :: integer()
  def repeated_string_match(a, b) do
    len_a = byte_size(a)
    len_b = byte_size(b)

    repeats = div(len_b + len_a - 1, len_a)
    s = String.duplicate(a, repeats)

    cond do
      String.contains?(s, b) -> repeats
      String.contains?(s <> a, b) -> repeats + 1
      true -> -1
    end
  end
end
```
