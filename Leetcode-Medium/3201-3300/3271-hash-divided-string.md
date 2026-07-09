# 3271. Hash Divided String

## Cpp

```cpp
class Solution {
public:
    string stringHash(string s, int k) {
        string result;
        for (int i = 0; i < (int)s.size(); i += k) {
            int sum = 0;
            for (int j = i; j < i + k; ++j) {
                sum += s[j] - 'a';
            }
            result.push_back('a' + (sum % 26));
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String stringHash(String s, int k) {
        int n = s.length();
        int groups = n / k;
        StringBuilder result = new StringBuilder(groups);
        for (int i = 0; i < groups; i++) {
            int sum = 0;
            int start = i * k;
            for (int j = 0; j < k; j++) {
                sum += s.charAt(start + j) - 'a';
            }
            char hashedChar = (char) ('a' + (sum % 26));
            result.append(hashedChar);
        }
        return result.toString();
    }
}
```

## Python

```python
class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        base = ord('a')
        for i in range(0, len(s), k):
            total = 0
            segment = s[i:i + k]
            for ch in segment:
                total += ord(ch) - base
            hashed_char = chr(base + (total % 26))
            res.append(hashed_char)
        return ''.join(res)
```

## Python3

```python
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), k):
            total = 0
            for ch in s[i:i + k]:
                total += ord(ch) - 97
            hashed_char = chr((total % 26) + 97)
            res.append(hashed_char)
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* stringHash(char* s, int k) {
    int n = strlen(s);
    int groups = n / k;
    char *res = (char*)malloc(groups + 1);
    for (int i = 0; i < groups; ++i) {
        int sum = 0;
        for (int j = 0; j < k; ++j) {
            sum += s[i * k + j] - 'a';
        }
        res[i] = 'a' + (sum % 26);
    }
    res[groups] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string StringHash(string s, int k) {
        var sb = new System.Text.StringBuilder();
        for (int i = 0; i < s.Length; i += k) {
            int sum = 0;
            for (int j = i; j < i + k; ++j) {
                sum += s[j] - 'a';
            }
            char c = (char)('a' + (sum % 26));
            sb.Append(c);
        }
        return sb.ToString();
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
var stringHash = function(s, k) {
    const n = s.length;
    let result = '';
    for (let i = 0; i < n; i += k) {
        let sum = 0;
        for (let j = 0; j < k; ++j) {
            sum += s.charCodeAt(i + j) - 97;
        }
        const idx = sum % 26;
        result += String.fromCharCode(97 + idx);
    }
    return result;
};
```

## Typescript

```typescript
function stringHash(s: string, k: number): string {
    const base = 'a'.charCodeAt(0);
    let result = '';
    for (let i = 0; i < s.length; i += k) {
        let sum = 0;
        for (let j = i; j < i + k; ++j) {
            sum += s.charCodeAt(j) - base;
        }
        const idx = sum % 26;
        result += String.fromCharCode(base + idx);
    }
    return result;
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
    function stringHash($s, $k) {
        $n = strlen($s);
        $result = '';
        for ($i = 0; $i < $n; $i += $k) {
            $sum = 0;
            for ($j = $i; $j < $i + $k; $j++) {
                $sum += ord($s[$j]) - 97;
            }
            $hash = $sum % 26;
            $result .= chr($hash + 97);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func stringHash(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        var result = [Character]()
        let base = 97 // ASCII value of 'a'
        var i = 0
        while i < chars.count {
            var sum = 0
            for j in 0..<k {
                let c = chars[i + j]
                if let val = c.unicodeScalars.first?.value {
                    sum += Int(val) - base
                }
            }
            let idx = sum % 26
            let hashedScalar = UnicodeScalar(base + idx)!
            result.append(Character(hashedScalar))
            i += k
        }
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stringHash(s: String, k: Int): String {
        val sb = StringBuilder()
        var idx = 0
        while (idx < s.length) {
            var sum = 0
            for (j in idx until idx + k) {
                sum += s[j] - 'a'
            }
            sb.append(('a'.code + (sum % 26)).toChar())
            idx += k
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String stringHash(String s, int k) {
    const int base = 97; // ASCII code for 'a'
    final buffer = StringBuffer();
    for (int i = 0; i < s.length; i += k) {
      int sum = 0;
      for (int j = i; j < i + k; ++j) {
        sum += s.codeUnitAt(j) - base;
      }
      int idx = sum % 26;
      buffer.writeCharCode(base + idx);
    }
    return buffer.toString();
  }
}
```

## Golang

```go
func stringHash(s string, k int) string {
	n := len(s)
	blocks := n / k
	res := make([]byte, blocks)
	for i := 0; i < blocks; i++ {
		sum := 0
		start := i * k
		for j := 0; j < k; j++ {
			sum += int(s[start+j] - 'a')
		}
		res[i] = byte('a' + (sum % 26))
	}
	return string(res)
}
```

## Ruby

```ruby
def string_hash(s, k)
  result = +""
  (0...s.length).step(k) do |i|
    sum = 0
    s[i, k].each_byte { |b| sum += b - 97 }
    result << ((sum % 26) + 97).chr
  end
  result
end
```

## Scala

```scala
object Solution {
    def stringHash(s: String, k: Int): String = {
        val n = s.length
        val result = new StringBuilder
        var i = 0
        while (i < n) {
            var sum = 0
            var j = i
            val end = i + k
            while (j < end) {
                sum += s.charAt(j) - 'a'
                j += 1
            }
            val ch = ((sum % 26) + 'a'.toInt).toChar
            result.append(ch)
            i += k
        }
        result.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn string_hash(s: String, k: i32) -> String {
        let bytes = s.as_bytes();
        let k_usize = k as usize;
        let mut result = String::new();

        for start in (0..bytes.len()).step_by(k_usize) {
            let mut sum: u32 = 0;
            for &b in &bytes[start..start + k_usize] {
                sum += (b - b'a') as u32;
            }
            let ch = ((sum % 26) as u8 + b'a') as char;
            result.push(ch);
        }

        result
    }
}
```

## Racket

```racket
(define/contract (string-hash s k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length s))
         (chunks (/ n k)))
    (let loop ((i 0) (acc '()))
      (if (= i chunks)
          (list->string (reverse acc))
          (let* ((start (* i k))
                 (sum (let sum-loop ((j start) (total 0))
                        (if (= j (+ start k))
                            total
                            (let ((c (char->integer (string-ref s j))))
                              (sum-loop (+ j 1) (+ total (- c 97)))))))
                 (hashed (remainder sum 26))
                 (ch (integer->char (+ hashed 97))))
            (loop (+ i 1) (cons ch acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([string_hash/2]).

-spec string_hash(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
string_hash(S, K) ->
    List = binary_to_list(S),
    CharsRev = hash_chunks(List, K, []),
    list_to_binary(lists:reverse(CharsRev)).

hash_chunks([], _K, Acc) -> Acc;
hash_chunks(L, K, Acc) ->
    {Chunk, Rest} = lists:split(K, L),
    Sum = sum_chunk(Chunk, 0),
    V = Sum rem 26,
    Char = $a + V,
    hash_chunks(Rest, K, [Char | Acc]).

sum_chunk([], Acc) -> Acc;
sum_chunk([C|Cs], Acc) ->
    sum_chunk(Cs, Acc + (C - $a)).
```

## Elixir

```elixir
defmodule Solution do
  @spec string_hash(s :: String.t(), k :: integer) :: String.t()
  def string_hash(s, k) do
    s
    |> :unicode.characters_to_list()
    |> Enum.chunk_every(k)
    |> Enum.map(fn chunk ->
      sum = Enum.reduce(chunk, 0, fn cp, acc -> acc + (cp - ?a) end)
      hashed = rem(sum, 26) + ?a
      <<hashed::utf8>>
    end)
    |> List.to_string()
  end
end
```
