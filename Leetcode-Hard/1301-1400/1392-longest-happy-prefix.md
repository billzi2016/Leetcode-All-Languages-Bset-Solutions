# 1392. Longest Happy Prefix

## Cpp

```cpp
class Solution {
public:
    string longestPrefix(string s) {
        int n = s.size();
        vector<int> pi(n, 0);
        for (int i = 1; i < n; ++i) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) {
                j = pi[j - 1];
            }
            if (s[i] == s[j]) ++j;
            pi[i] = j;
        }
        int len = pi[n - 1];
        return s.substr(0, len);
    }
};
```

## Java

```java
class Solution {
    public String longestPrefix(String s) {
        int n = s.length();
        int[] pi = new int[n];
        for (int i = 1; i < n; i++) {
            int j = pi[i - 1];
            while (j > 0 && s.charAt(i) != s.charAt(j)) {
                j = pi[j - 1];
            }
            if (s.charAt(i) == s.charAt(j)) {
                j++;
            }
            pi[i] = j;
        }
        int len = pi[n - 1];
        return len > 0 ? s.substring(0, len) : "";
    }
}
```

## Python

```python
class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        lps = [0] * n
        length = 0  # length of the previous longest prefix suffix

        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        longest = lps[-1]
        return s[:longest] if longest > 0 else ""
```

## Python3

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        length = 0  # length of the previous longest prefix suffix

        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return s[:lps[-1]] if n > 0 else ""
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* longestPrefix(char* s) {
    int n = strlen(s);
    int *pi = (int*)malloc(n * sizeof(int));
    if (!pi) return NULL;
    pi[0] = 0;
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) {
            j = pi[j - 1];
        }
        if (s[i] == s[j]) ++j;
        pi[i] = j;
    }
    int len = n ? pi[n - 1] : 0;
    char *res = (char*)malloc(len + 1);
    if (!res) {
        free(pi);
        return NULL;
    }
    memcpy(res, s, len);
    res[len] = '\0';
    free(pi);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string LongestPrefix(string s) {
        int n = s.Length;
        if (n == 0) return "";
        int[] pi = new int[n];
        for (int i = 1; i < n; i++) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) {
                j = pi[j - 1];
            }
            if (s[i] == s[j]) j++;
            pi[i] = j;
        }
        int len = pi[n - 1];
        return s.Substring(0, len);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestPrefix = function(s) {
    const n = s.length;
    if (n === 0) return "";
    const lps = new Array(n).fill(0);
    let len = 0;
    for (let i = 1; i < n; i++) {
        while (len > 0 && s[i] !== s[len]) {
            len = lps[len - 1];
        }
        if (s[i] === s[len]) {
            len++;
            lps[i] = len;
        } else {
            lps[i] = 0;
        }
    }
    const longest = lps[n - 1];
    return s.substring(0, longest);
};
```

## Typescript

```typescript
function longestPrefix(s: string): string {
    const n = s.length;
    if (n === 0) return "";
    const pi = new Array<number>(n).fill(0);
    for (let i = 1; i < n; i++) {
        let j = pi[i - 1];
        while (j > 0 && s[i] !== s[j]) {
            j = pi[j - 1];
        }
        if (s[i] === s[j]) {
            j++;
        }
        pi[i] = j;
    }
    const len = pi[n - 1];
    return len > 0 ? s.slice(0, len) : "";
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPrefix($s) {
        $n = strlen($s);
        if ($n == 0) return "";
        $lps = array_fill(0, $n, 0);
        $len = 0;
        for ($i = 1; $i < $n; $i++) {
            while ($len > 0 && $s[$i] !== $s[$len]) {
                $len = $lps[$len - 1];
            }
            if ($s[$i] === $s[$len]) {
                $len++;
                $lps[$i] = $len;
            } else {
                $lps[$i] = 0;
            }
        }
        $ansLen = $lps[$n - 1];
        return $ansLen > 0 ? substr($s, 0, $ansLen) : "";
    }
}
```

## Swift

```swift
class Solution {
    func longestPrefix(_ s: String) -> String {
        let chars = Array(s.utf8)
        let n = chars.count
        if n == 0 { return "" }
        var lps = [Int](repeating: 0, count: n)
        var j = 0
        for i in 1..<n {
            while j > 0 && chars[i] != chars[j] {
                j = lps[j - 1]
            }
            if chars[i] == chars[j] {
                j += 1
                lps[i] = j
            } else {
                lps[i] = j
            }
        }
        let len = lps[n - 1]
        if len == 0 { return "" }
        let endIdx = s.index(s.startIndex, offsetBy: len)
        return String(s[s.startIndex..<endIdx])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPrefix(s: String): String {
        val n = s.length
        if (n == 0) return ""
        val lps = IntArray(n)
        var j = 0
        for (i in 1 until n) {
            while (j > 0 && s[i] != s[j]) {
                j = lps[j - 1]
            }
            if (s[i] == s[j]) {
                j++
            }
            lps[i] = j
        }
        val len = lps[n - 1]
        return if (len > 0) s.substring(0, len) else ""
    }
}
```

## Dart

```dart
class Solution {
  String longestPrefix(String s) {
    int n = s.length;
    List<int> lps = List.filled(n, 0);
    int len = 0;
    for (int i = 1; i < n; i++) {
      while (len > 0 && s[i] != s[len]) {
        len = lps[len - 1];
      }
      if (s[i] == s[len]) {
        len++;
        lps[i] = len;
      } else {
        lps[i] = len;
      }
    }
    int ansLen = lps[n - 1];
    return ansLen > 0 ? s.substring(0, ansLen) : "";
  }
}
```

## Golang

```go
func longestPrefix(s string) string {
	n := len(s)
	if n == 0 {
		return ""
	}
	pi := make([]int, n)
	for i := 1; i < n; i++ {
		j := pi[i-1]
		for j > 0 && s[i] != s[j] {
			j = pi[j-1]
		}
		if s[i] == s[j] {
			j++
		}
		pi[i] = j
	}
	l := pi[n-1]
	return s[:l]
}
```

## Ruby

```ruby
# @param {String} s
# @return {String}
def longest_prefix(s)
  n = s.length
  return "" if n <= 1

  pi = Array.new(n, 0)
  (1...n).each do |i|
    j = pi[i - 1]
    while j > 0 && s[i] != s[j]
      j = pi[j - 1]
    end
    j += 1 if s[i] == s[j]
    pi[i] = j
  end

  len = pi[-1]
  len.zero? ? "" : s[0, len]
end
```

## Scala

```scala
object Solution {
    def longestPrefix(s: String): String = {
        val n = s.length
        if (n == 0) return ""
        val lps = new Array[Int](n)
        var length = 0
        var i = 1
        while (i < n) {
            if (s.charAt(i) == s.charAt(length)) {
                length += 1
                lps(i) = length
                i += 1
            } else {
                if (length != 0) {
                    length = lps(length - 1)
                } else {
                    lps(i) = 0
                    i += 1
                }
            }
        }
        val resLen = lps(n - 1)
        if (resLen > 0) s.substring(0, resLen) else ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_prefix(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return "".to_string();
        }
        let mut pi = vec![0usize; n];
        for i in 1..n {
            let mut j = pi[i - 1];
            while j > 0 && bytes[i] != bytes[j] {
                j = pi[j - 1];
            }
            if bytes[i] == bytes[j] {
                j += 1;
            }
            pi[i] = j;
        }
        let len = pi[n - 1];
        s[..len].to_string()
    }
}
```

## Racket

```racket
(define/contract (longest-prefix s)
  (-> string? string?)
  (let* ([n (string-length s)]
         [pi (make-vector n 0)])
    (let loop ((i 1) (j 0))
      (when (< i n)
        (let ([j
               (let adjust ((j j))
                 (if (and (> j 0)
                          (not (char=? (string-ref s i) (string-ref s j))))
                     (adjust (vector-ref pi (- j 1)))
                     j))])
          (define new-j
            (if (char=? (string-ref s i) (string-ref s j))
                (+ j 1)
                j))
          (vector-set! pi i new-j)
          (loop (+ i 1) new-j))))
    (let ([len (if (= n 0) 0 (vector-ref pi (- n 1)))])
      (if (> len 0)
          (substring s 0 len)
          ""))))
```

## Erlang

```erlang
-spec longest_prefix(unicode:unicode_binary()) -> unicode:unicode_binary().
longest_prefix(S) ->
    N = byte_size(S),
    if N =< 1 ->
            <<>>;
       true ->
            Arr0 = array:new(N, {default, 0}),
            {Len,_} = loop(1, 0, Arr0, S, N),
            case Len of
                0 -> <<>>;
                _ -> binary:part(S, {0, Len})
            end
    end.

loop(I, K, Arr, S, N) when I >= N ->
    {K, Arr};
loop(I, K, Arr, S, N) ->
    CharI = binary:at(S, I),
    case K > 0 of
        true ->
            CharK = binary:at(S, K),
            if CharI == CharK ->
                    NewK = K + 1,
                    Arr2 = array:set(I+1, NewK, Arr),
                    loop(I+1, NewK, Arr2, S, N);
               true ->
                    K2 = array:get(K, Arr),
                    loop(I, K2, Arr, S, N)
            end;
        false ->
            Char0 = binary:at(S, 0),
            if CharI == Char0 ->
                    NewK = 1,
                    Arr2 = array:set(I+1, NewK, Arr),
                    loop(I+1, NewK, Arr2, S, N);
               true ->
                    Arr2 = array:set(I+1, 0, Arr),
                    loop(I+1, 0, Arr2, S, N)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_prefix(s :: String.t) :: String.t
  def longest_prefix(s) do
    n = byte_size(s)

    if n == 0 do
      ""
    else
      pi = :array.new(n, default: 0)
      pi_final = build_pi(s, n, 1, 0, pi)
      len = :array.get(n - 1, pi_final)

      if len > 0 do
        String.slice(s, 0, len)
      else
        ""
      end
    end
  end

  defp build_pi(_s, _n, i, _j, pi) when i >= _n do
    pi
  end

  defp build_pi(s, n, i, j, pi) do
    c_i = :binary.at(s, i)
    j_adj = adjust_j(s, pi, j, c_i)

    new_j =
      if c_i == :binary.at(s, j_adj) do
        j_adj + 1
      else
        j_adj
      end

    pi_updated = :array.set(i, new_j, pi)
    build_pi(s, n, i + 1, new_j, pi_updated)
  end

  defp adjust_j(_s, _pi, 0, _c_i), do: 0

  defp adjust_j(s, pi, j, c_i) do
    if c_i == :binary.at(s, j) do
      j
    else
      new_j = :array.get(j - 1, pi)
      adjust_j(s, pi, new_j, c_i)
    end
  end
end
```
