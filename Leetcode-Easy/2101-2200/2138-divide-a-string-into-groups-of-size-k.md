# 2138. Divide a String Into Groups of Size k

## Cpp

```cpp
class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int n = s.size();
        int groups = (n + k - 1) / k;
        vector<string> res;
        res.reserve(groups);
        for (int i = 0; i < groups; ++i) {
            int start = i * k;
            string part = s.substr(start, min(k, n - start));
            if ((int)part.size() < k) {
                part.append(k - part.size(), fill);
            }
            res.push_back(move(part));
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String[] divideString(String s, int k, char fill) {
        int n = s.length();
        int groups = (n + k - 1) / k;
        String[] res = new String[groups];
        for (int i = 0; i < groups; i++) {
            int start = i * k;
            int end = Math.min(start + k, n);
            StringBuilder sb = new StringBuilder(s.substring(start, end));
            while (sb.length() < k) {
                sb.append(fill);
            }
            res[i] = sb.toString();
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        for i in range(0, n, k):
            part = s[i:i + k]
            if len(part) < k:
                part += fill * (k - len(part))
            res.append(part)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        for i in range(0, n, k):
            chunk = s[i:i + k]
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            res.append(chunk)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** divideString(char* s, int k, char fill, int* returnSize) {
    int n = strlen(s);
    int groups = (n + k - 1) / k;  // ceil division
    *returnSize = groups;
    
    char **res = (char **)malloc(groups * sizeof(char *));
    for (int i = 0; i < groups; ++i) {
        char *group = (char *)malloc((k + 1) * sizeof(char));
        for (int j = 0; j < k; ++j) {
            int idx = i * k + j;
            if (idx < n)
                group[j] = s[idx];
            else
                group[j] = fill;
        }
        group[k] = '\0';
        res[i] = group;
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string[] DivideString(string s, int k, char fill) {
        int n = s.Length;
        int groups = (n + k - 1) / k;
        var result = new List<string>(groups);
        for (int i = 0; i < groups; i++) {
            int start = i * k;
            int len = Math.Min(k, n - start);
            string part = s.Substring(start, len);
            if (len < k) {
                part = part.PadRight(k, fill);
            }
            result.Add(part);
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function(s, k, fill) {
    const res = [];
    for (let i = 0; i < s.length; i += k) {
        let part = s.slice(i, i + k);
        if (part.length < k) {
            part += fill.repeat(k - part.length);
        }
        res.push(part);
    }
    return res;
};
```

## Typescript

```typescript
function divideString(s: string, k: number, fill: string): string[] {
    const res: string[] = [];
    for (let i = 0; i < s.length; i += k) {
        let part = s.slice(i, i + k);
        if (part.length < k) {
            part += fill.repeat(k - part.length);
        }
        res.push(part);
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @param String $fill
     * @return String[]
     */
    function divideString($s, $k, $fill) {
        $n = strlen($s);
        $result = [];
        for ($i = 0; $i < $n; $i += $k) {
            $part = substr($s, $i, $k);
            if (strlen($part) < $k) {
                $part .= str_repeat($fill, $k - strlen($part));
            }
            $result[] = $part;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func divideString(_ s: String, _ k: Int, _ fill: Character) -> [String] {
        let chars = Array(s)
        var result = [String]()
        var index = 0
        while index < chars.count {
            var group = [Character]()
            for offset in 0..<k {
                if index + offset < chars.count {
                    group.append(chars[index + offset])
                } else {
                    group.append(fill)
                }
            }
            result.append(String(group))
            index += k
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun divideString(s: String, k: Int, fill: Char): Array<String> {
        val result = mutableListOf<String>()
        var i = 0
        while (i < s.length) {
            val end = kotlin.math.min(i + k, s.length)
            var part = s.substring(i, end)
            if (part.length < k) {
                part += fill.toString().repeat(k - part.length)
            }
            result.add(part)
            i += k
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> divideString(String s, int k, String fill) {
    List<String> res = [];
    for (int i = 0; i < s.length; i += k) {
      int end = i + k <= s.length ? i + k : s.length;
      String part = s.substring(i, end);
      if (part.length < k) {
        part = part.padRight(k, fill);
      }
      res.add(part);
    }
    return res;
  }
}
```

## Golang

```go
func divideString(s string, k int, fill byte) []string {
	n := len(s)
	var res []string
	for i := 0; i < n; i += k {
		end := i + k
		if end > n {
			end = n
		}
		part := s[i:end]
		if len(part) < k {
			b := make([]byte, k)
			copy(b, part)
			for j := len(part); j < k; j++ {
				b[j] = fill
			}
			part = string(b)
		}
		res = append(res, part)
	}
	return res
}
```

## Ruby

```ruby
def divide_string(s, k, fill)
  res = []
  i = 0
  n = s.length
  while i < n
    part = s[i, k]
    if part.length < k
      part += fill * (k - part.length)
    end
    res << part
    i += k
  end
  res
end
```

## Scala

```scala
object Solution {
    def divideString(s: String, k: Int, fill: Char): Array[String] = {
        val n = s.length
        val res = scala.collection.mutable.ArrayBuffer[String]()
        var i = 0
        while (i < n) {
            val end = math.min(i + k, n)
            var part = s.substring(i, end)
            if (part.length < k) {
                part = part + fill.toString * (k - part.length)
            }
            res += part
            i += k
        }
        // If the original string is empty (not possible per constraints), handle by adding a filled group.
        if (res.isEmpty && k > 0) {
            res += fill.toString * k
        }
        res.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn divide_string(s: String, k: i32, fill: char) -> Vec<String> {
        let n = s.len();
        let k_usize = k as usize;
        let mut res = Vec::new();
        let bytes = s.as_bytes();
        let mut i = 0;
        while i < n {
            let end = std::cmp::min(i + k_usize, n);
            // SAFETY: the string consists of ASCII lowercase letters,
            // so slicing by byte indices is valid UTF-8.
            let mut part = unsafe { std::str::from_utf8_unchecked(&bytes[i..end]) }.to_string();
            if part.len() < k_usize {
                part.extend(std::iter::repeat(fill).take(k_usize - part.len()));
            }
            res.push(part);
            i += k_usize;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (divide-string s k fill)
  (-> string? exact-integer? char? (listof string?))
  (let* ((n (string-length s))
         (full-groups (quotient n k))
         (has-remainder (> (remainder n k) 0))
         (total-groups (if has-remainder (add1 full-groups) full-groups)))
    (for/list ([i (in-range total-groups)])
      (let* ((start (* i k))
             (end (min (* (+ i 1) k) n))
             (part (substring s start end))
             (len (string-length part)))
        (if (= len k)
            part
            (string-append part (make-string (- k len) fill)))))))
```

## Erlang

```erlang
-spec divide_string(S :: unicode:unicode_binary(), K :: integer(), Fill :: char()) -> [unicode:unicode_binary()].
divide_string(S, K, Fill) ->
    divide_string(S, K, Fill, []).

%% When no more characters left, return accumulated groups in correct order.
divide_string(<<>>, _K, _Fill, Acc) ->
    lists:reverse(Acc);
%% Take a full group of size K.
divide_string(Bin, K, Fill, Acc) when byte_size(Bin) >= K ->
    <<Chunk:K/binary, Rest/binary>> = Bin,
    divide_string(Rest, K, Fill, [Chunk | Acc]);
%% Last partial group, pad with fill character.
divide_string(Remaining, K, Fill, Acc) ->
    Missing = K - byte_size(Remaining),
    Pad = binary:copy(<<Fill>>, Missing),
    Chunk = <<Remaining/binary, Pad/binary>>,
    lists:reverse([Chunk | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec divide_string(s :: String.t(), k :: integer, fill :: char) :: [String.t()]
  def divide_string(s, k, fill) do
    n = String.length(s)
    groups = div(n + k - 1, k)

    Enum.map(0..groups - 1, fn i ->
      start = i * k
      part = String.slice(s, start, k)

      if String.length(part) < k do
        part <> String.duplicate(fill, k - String.length(part))
      else
        part
      end
    end)
  end
end
```
