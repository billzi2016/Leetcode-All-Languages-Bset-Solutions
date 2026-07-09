# 3210. Find the Encrypted String

## Cpp

```cpp
class Solution {
public:
    string getEncryptedString(string s, int k) {
        int n = s.size();
        k %= n;
        string res;
        res.reserve(n);
        for (int i = 0; i < n; ++i) {
            res.push_back(s[(i + k) % n]);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String getEncryptedString(String s, int k) {
        int n = s.length();
        int shift = k % n;
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            sb.append(s.charAt((i + shift) % n));
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        k %= n
        return ''.join(s[(i + k) % n] for i in range(n))
```

## Python3

```python
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        return ''.join(s[(i + k) % n] for i in range(n))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* getEncryptedString(char* s, int k) {
    int n = strlen(s);
    char *res = (char*)malloc((n + 1) * sizeof(char));
    if (!res) return NULL;
    k %= n;
    for (int i = 0; i < n; ++i) {
        res[i] = s[(i + k) % n];
    }
    res[n] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string GetEncryptedString(string s, int k) {
        int n = s.Length;
        if (n == 0) return "";
        k %= n;
        char[] res = new char[n];
        for (int i = 0; i < n; i++) {
            int srcIdx = (i + k) % n;
            res[i] = s[srcIdx];
        }
        return new string(res);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var getEncryptedString = function(s, k) {
    const n = s.length;
    k %= n;
    let result = '';
    for (let i = 0; i < n; i++) {
        result += s[(i + k) % n];
    }
    return result;
};
```

## Typescript

```typescript
function getEncryptedString(s: string, k: number): string {
    const n = s.length;
    const shift = k % n;
    if (shift === 0) return s;
    return s.slice(n - shift) + s.slice(0, n - shift);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function getEncryptedString($s, $k) {
        $n = strlen($s);
        if ($n == 0) return "";
        $k %= $n;
        $result = '';
        for ($i = 0; $i < $n; $i++) {
            $idx = ($i + $k) % $n;
            $result .= $s[$idx];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getEncryptedString(_ s: String, _ k: Int) -> String {
        let n = s.count
        if n == 0 { return "" }
        let shift = k % n
        let chars = Array(s)
        var result = [Character]()
        result.reserveCapacity(n)
        for i in 0..<n {
            let idx = (i + shift) % n
            result.append(chars[idx])
        }
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getEncryptedString(s: String, k: Int): String {
        val n = s.length
        if (n == 0) return ""
        val shift = k % n
        val sb = StringBuilder(n)
        for (i in 0 until n) {
            sb.append(s[(i + shift) % n])
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String getEncryptedString(String s, int k) {
    int n = s.length;
    if (n == 0) return "";
    int shift = k % n;
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < n; i++) {
      int idx = (i + shift) % n;
      sb.write(s[idx]);
    }
    return sb.toString();
  }
}
```

## Golang

```go
func getEncryptedString(s string, k int) string {
	n := len(s)
	if n == 0 {
		return ""
	}
	shift := k % n
	res := make([]byte, n)
	for i := 0; i < n; i++ {
		idx := (i + shift) % n
		res[i] = s[idx]
	}
	return string(res)
}
```

## Ruby

```ruby
def get_encrypted_string(s, k)
  n = s.length
  k %= n
  Array.new(n) { |i| s[(i + k) % n] }.join
end
```

## Scala

```scala
object Solution {
    def getEncryptedString(s: String, k: Int): String = {
        val n = s.length
        if (n == 0) return ""
        val shift = k % n
        val sb = new StringBuilder(n)
        var i = 0
        while (i < n) {
            sb.append(s.charAt((i + shift) % n))
            i += 1
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_encrypted_string(s: String, k: i32) -> String {
        let n = s.len();
        if n == 0 {
            return s;
        }
        let shift = (k as usize) % n;
        let bytes = s.as_bytes();
        let mut res = Vec::with_capacity(n);
        for i in 0..n {
            let idx = (i + shift) % n;
            res.push(bytes[idx]);
        }
        unsafe { String::from_utf8_unchecked(res) }
    }
}
```

## Racket

```racket
(define/contract (get-encrypted-string s k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length s))
         (kmod (modulo k n)))
    (list->string
     (for/list ([i (in-range n)])
       (string-ref s (modulo (+ i kmod) n))))))
```

## Erlang

```erlang
-spec get_encrypted_string(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
get_encrypted_string(S, K) ->
    N = byte_size(S),
    Kmod = K rem N,
    case Kmod of
        0 -> S;
        _ ->
            <<Prefix:Kmod/binary, Rest/binary>> = S,
            <<Rest/binary, Prefix/binary>>
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_encrypted_string(s :: String.t(), k :: integer) :: String.t()
  def get_encrypted_string(s, k) do
    n = String.length(s)
    km = rem(k, n)
    chars = String.graphemes(s)

    rotated =
      Enum.drop(chars, km) ++
        Enum.take(chars, km)

    Enum.join(rotated)
  end
end
```
