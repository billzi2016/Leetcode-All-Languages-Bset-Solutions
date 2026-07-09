# 3216. Lexicographically Smallest String After a Swap

## Cpp

```cpp
class Solution {
public:
    string getSmallestString(string s) {
        string best = s;
        int n = s.size();
        for (int i = 0; i + 1 < n; ++i) {
            int d1 = s[i] - '0';
            int d2 = s[i+1] - '0';
            if ((d1 & 1) == (d2 & 1)) { // same parity
                string t = s;
                swap(t[i], t[i+1]);
                if (t < best) best = t;
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public String getSmallestString(String s) {
        String best = s;
        int n = s.length();
        for (int i = 0; i < n - 1; i++) {
            char a = s.charAt(i);
            char b = s.charAt(i + 1);
            if (((a - '0') % 2) == ((b - '0') % 2)) {
                char[] arr = s.toCharArray();
                arr[i] = b;
                arr[i + 1] = a;
                String candidate = new String(arr);
                if (candidate.compareTo(best) < 0) {
                    best = candidate;
                }
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = s
        n = len(s)
        for i in range(n - 1):
            if (int(s[i]) % 2) == (int(s[i + 1]) % 2):
                lst = list(s)
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                cand = ''.join(lst)
                if cand < best:
                    best = cand
        return best
```

## Python3

```python
class Solution:
    def getSmallestString(self, s: str) -> str:
        best = s
        n = len(s)
        for i in range(n - 1):
            if (int(s[i]) % 2) == (int(s[i + 1]) % 2):
                lst = list(s)
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                cand = ''.join(lst)
                if cand < best:
                    best = cand
        return best
```

## C

```c
#include <stdlib.h>
#include <string.h>

static char* duplicate(const char *src) {
    size_t len = strlen(src);
    char *dst = (char*)malloc(len + 1);
    if (dst) memcpy(dst, src, len + 1);
    return dst;
}

char* getSmallestString(char* s) {
    int n = (int)strlen(s);
    char *best = duplicate(s);
    char tmp[101]; // max length is 100

    for (int i = 0; i < n - 1; ++i) {
        int d1 = s[i] - '0';
        int d2 = s[i + 1] - '0';
        if ((d1 % 2) == (d2 % 2)) {
            strcpy(tmp, s);
            char t = tmp[i];
            tmp[i] = tmp[i + 1];
            tmp[i + 1] = t;
            if (strcmp(tmp, best) < 0) {
                strcpy(best, tmp);
            }
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public string GetSmallestString(string s) {
        string best = s;
        char[] arr = s.ToCharArray();
        int n = arr.Length;
        for (int i = 0; i < n - 1; i++) {
            int d1 = arr[i] - '0';
            int d2 = arr[i + 1] - '0';
            if ((d1 % 2) == (d2 % 2)) {
                char[] copy = (char[])arr.Clone();
                char temp = copy[i];
                copy[i] = copy[i + 1];
                copy[i + 1] = temp;
                string candidate = new string(copy);
                if (string.CompareOrdinal(candidate, best) < 0) {
                    best = candidate;
                }
            }
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var getSmallestString = function(s) {
    let best = s;
    const n = s.length;
    for (let i = 0; i < n - 1; ++i) {
        const d1 = s.charCodeAt(i) - 48;
        const d2 = s.charCodeAt(i + 1) - 48;
        if ((d1 & 1) === (d2 & 1)) { // same parity
            const arr = s.split('');
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
            const cand = arr.join('');
            if (cand < best) best = cand;
        }
    }
    return best;
};
```

## Typescript

```typescript
function getSmallestString(s: string): string {
    let best = s;
    const n = s.length;
    for (let i = 0; i < n - 1; i++) {
        const d1 = s.charCodeAt(i) - 48;
        const d2 = s.charCodeAt(i + 1) - 48;
        if ((d1 & 1) === (d2 & 1)) { // same parity
            const candidate = s.slice(0, i) + s[i + 1] + s[i] + s.slice(i + 2);
            if (candidate < best) {
                best = candidate;
            }
        }
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function getSmallestString($s) {
        $n = strlen($s);
        $best = $s;
        for ($i = 0; $i < $n - 1; $i++) {
            $a = intval($s[$i]);
            $b = intval($s[$i + 1]);
            if (($a % 2) === ($b % 2)) {
                // swap adjacent characters
                $t = $s;
                $tmp = $t[$i];
                $t[$i] = $t[$i + 1];
                $t[$i + 1] = $tmp;
                if (strcmp($t, $best) < 0) {
                    $best = $t;
                }
            }
        }
        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func getSmallestString(_ s: String) -> String {
        let original = Array(s)
        var best = s
        let n = original.count
        for i in 0..<(n - 1) {
            guard let v1 = original[i].wholeNumberValue,
                  let v2 = original[i + 1].wholeNumberValue else { continue }
            if (v1 % 2) == (v2 % 2) {
                var temp = original
                temp.swapAt(i, i + 1)
                let candidate = String(temp)
                if candidate < best {
                    best = candidate
                }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getSmallestString(s: String): String {
        var best = s
        val n = s.length
        val original = s.toCharArray()
        for (i in 0 until n - 1) {
            if ((original[i] - '0') % 2 == (original[i + 1] - '0') % 2) {
                val swapped = original.clone()
                val tmp = swapped[i]
                swapped[i] = swapped[i + 1]
                swapped[i + 1] = tmp
                val candidate = String(swapped)
                if (candidate < best) {
                    best = candidate
                }
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  String getSmallestString(String s) {
    String best = s;
    int n = s.length;
    for (int i = 0; i < n - 1; i++) {
      int d1 = s.codeUnitAt(i) - 48;
      int d2 = s.codeUnitAt(i + 1) - 48;
      if ((d1 & 1) == (d2 & 1)) { // same parity
        String swapped = s.substring(0, i) + s[i + 1] + s[i] + s.substring(i + 2);
        if (swapped.compareTo(best) < 0) {
          best = swapped;
        }
      }
    }
    return best;
  }
}
```

## Golang

```go
func getSmallestString(s string) string {
	best := s
	b := []byte(s)
	n := len(b)
	for i := 0; i+1 < n; i++ {
		if (b[i]-'0')%2 == (b[i+1]-'0')%2 {
			nb := make([]byte, n)
			copy(nb, b)
			nb[i], nb[i+1] = nb[i+1], nb[i]
			cand := string(nb)
			if cand < best {
				best = cand
			}
		}
	}
	return best
}
```

## Ruby

```ruby
def get_smallest_string(s)
  best = s
  n = s.length
  chars = s.chars
  (0...n-1).each do |i|
    if (chars[i].ord - 48) % 2 == (chars[i+1].ord - 48) % 2
      swapped = chars.clone
      swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
      candidate = swapped.join
      best = candidate if candidate < best
    end
  end
  best
end
```

## Scala

```scala
object Solution {
    def getSmallestString(s: String): String = {
        var best = s
        val n = s.length
        for (i <- 0 until n - 1) {
            val a = s.charAt(i)
            val b = s.charAt(i + 1)
            if (((a - '0') % 2) == ((b - '0') % 2)) {
                val sb = new StringBuilder(s)
                sb.setCharAt(i, b)
                sb.setCharAt(i + 1, a)
                val cand = sb.toString()
                if (cand.compareTo(best) < 0) best = cand
            }
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_smallest_string(s: String) -> String {
        let n = s.len();
        let orig_bytes = s.as_bytes();
        let mut best = s.clone();

        // digits are ASCII, so we can work with u8 values directly
        let chars: Vec<u8> = orig_bytes.to_vec();

        for i in 0..n - 1 {
            if chars[i] % 2 == chars[i + 1] % 2 {
                let mut cand = chars.clone();
                cand.swap(i, i + 1);
                // SAFETY: all bytes are valid ASCII digits
                let cand_str = unsafe { String::from_utf8_unchecked(cand) };
                if cand_str < best {
                    best = cand_str;
                }
            }
        }

        best
    }
}
```

## Racket

```racket
(define (same-parity? a b)
  (= (modulo (char->integer a) 2)
     (modulo (char->integer b) 2)))

(define (swap-at str i)
  (let ((len (string-length str)))
    (list->string
     (for/list ([idx (in-range len)])
       (cond [(= idx i) (string-ref str (+ i 1))]
             [(= idx (+ i 1)) (string-ref str i)]
             [else (string-ref str idx)])))))

(define/contract (get-smallest-string s)
  (-> string? string?)
  (let* ((n (string-length s))
         (best s))
    (for ([i (in-range (- n 1))])
      (when (same-parity? (string-ref s i) (string-ref s (+ i 1)))
        (define cand (swap-at s i))
        (when (string<? cand best)
          (set! best cand))))
    best))
```

## Erlang

```erlang
-module(solution).
-export([get_smallest_string/1]).

-spec get_smallest_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
get_smallest_string(S) ->
    List = binary_to_list(S),
    Len = length(List),
    loop_swap(0, Len, List, S).

loop_swap(I, Len, _List, Best) when I >= Len - 1 ->
    Best;
loop_swap(I, Len, List, Best) ->
    {Prefix, Rest} = lists:split(I, List),
    case Rest of
        [A,B|Tail] ->
            ParA = ((A - $0) band 1),
            ParB = ((B - $0) band 1),
            NewBest =
                if ParA =:= ParB ->
                    NewList = Prefix ++ [B,A] ++ Tail,
                    NewBin = list_to_binary(NewList),
                    case NewBin < Best of
                        true -> NewBin;
                        false -> Best
                    end;
                   true -> Best
                end,
            loop_swap(I + 1, Len, List, NewBest);
        _ ->
            loop_swap(I + 1, Len, List, Best)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_smallest_string(s :: String.t) :: String.t
  def get_smallest_string(s) do
    list = String.graphemes(s)
    len = length(list)

    0..(len - 2)
    |> Enum.reduce(s, fn i, best ->
      a = String.to_integer(Enum.at(list, i))
      b = String.to_integer(Enum.at(list, i + 1))

      if rem(a, 2) == rem(b, 2) and b < a do
        swapped =
          list
          |> List.replace_at(i, Integer.to_string(b))
          |> List.replace_at(i + 1, Integer.to_string(a))

        cand = Enum.join(swapped)

        if cand < best, do: cand, else: best
      else
        best
      end
    end)
  end
end
```
