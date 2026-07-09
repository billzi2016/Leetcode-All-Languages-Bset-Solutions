# 2243. Calculate Digit Sum of a String

## Cpp

```cpp
class Solution {
public:
    string digitSum(string s, int k) {
        while (s.size() > static_cast<size_t>(k)) {
            string ns;
            for (int i = 0; i < (int)s.size(); i += k) {
                int sum = 0;
                for (int j = i; j < min(i + k, (int)s.size()); ++j) {
                    sum += s[j] - '0';
                }
                ns += to_string(sum);
            }
            s.swap(ns);
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String digitSum(String s, int k) {
        while (s.length() > k) {
            StringBuilder next = new StringBuilder();
            for (int i = 0; i < s.length(); i += k) {
                int sum = 0;
                int end = Math.min(i + k, s.length());
                for (int j = i; j < end; ++j) {
                    sum += s.charAt(j) - '0';
                }
                next.append(sum);
            }
            s = next.toString();
        }
        return s;
    }
}
```

## Python

```python
class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            groups = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''.join(str(sum(int(ch) for ch in grp)) for grp in groups)
        return s
```

## Python3

```python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            parts = [s[i:i + k] for i in range(0, len(s), k)]
            s = ''.join(str(sum(int(ch) for ch in part)) for part in parts)
        return s
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* digitSum(char* s, int k) {
    // Make a mutable copy of the input string
    char *cur = strdup(s);
    if (!cur) return NULL;

    while ((int)strlen(cur) > k) {
        int n = strlen(cur);
        int groups = (n + k - 1) / k;
        // Each group can produce at most 3 digits (max sum 9*k <= 900)
        char *next = (char *)malloc(groups * 4 + 1); // extra space for safety
        if (!next) {
            free(cur);
            return NULL;
        }
        int pos = 0;
        for (int i = 0; i < n; i += k) {
            int sum = 0;
            for (int j = i; j < i + k && j < n; ++j) {
                sum += cur[j] - '0';
            }
            // Convert sum to string
            char buf[12];
            int len = sprintf(buf, "%d", sum);
            memcpy(next + pos, buf, len);
            pos += len;
        }
        next[pos] = '\0';
        free(cur);
        cur = next;
    }

    return cur;
}
```

## Csharp

```csharp
public class Solution {
    public string DigitSum(string s, int k) {
        while (s.Length > k) {
            var sb = new System.Text.StringBuilder();
            for (int i = 0; i < s.Length; i += k) {
                int sum = 0;
                int end = Math.Min(i + k, s.Length);
                for (int j = i; j < end; ++j) {
                    sum += s[j] - '0';
                }
                sb.Append(sum);
            }
            s = sb.ToString();
        }
        return s;
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
var digitSum = function(s, k) {
    while (s.length > k) {
        let next = '';
        for (let i = 0; i < s.length; i += k) {
            let sum = 0;
            const end = Math.min(i + k, s.length);
            for (let j = i; j < end; ++j) {
                sum += s.charCodeAt(j) - 48; // '0' char code is 48
            }
            next += sum.toString();
        }
        s = next;
    }
    return s;
};
```

## Typescript

```typescript
function digitSum(s: string, k: number): string {
    while (s.length > k) {
        let next = "";
        for (let i = 0; i < s.length; i += k) {
            let sum = 0;
            const end = Math.min(i + k, s.length);
            for (let j = i; j < end; ++j) {
                sum += s.charCodeAt(j) - 48; // '0' char code is 48
            }
            next += sum.toString();
        }
        s = next;
    }
    return s;
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
    function digitSum($s, $k) {
        while (strlen($s) > $k) {
            $new = '';
            $len = strlen($s);
            for ($i = 0; $i < $len; $i += $k) {
                $segment = substr($s, $i, $k);
                $sum = 0;
                $segLen = strlen($segment);
                for ($j = 0; $j < $segLen; $j++) {
                    $sum += intval($segment[$j]);
                }
                $new .= strval($sum);
            }
            $s = $new;
        }
        return $s;
    }
}
```

## Swift

```swift
class Solution {
    func digitSum(_ s: String, _ k: Int) -> String {
        var current = s
        while current.count > k {
            let chars = Array(current)
            var newStr = ""
            var idx = 0
            while idx < chars.count {
                var sum = 0
                var j = 0
                while j < k && idx + j < chars.count {
                    if let digit = Int(String(chars[idx + j])) {
                        sum += digit
                    }
                    j += 1
                }
                newStr += String(sum)
                idx += k
            }
            current = newStr
        }
        return current
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun digitSum(s: String, k: Int): String {
        var cur = s
        while (cur.length > k) {
            val sb = StringBuilder()
            var i = 0
            while (i < cur.length) {
                var sum = 0
                var cnt = 0
                while (cnt < k && i + cnt < cur.length) {
                    sum += cur[i + cnt] - '0'
                    cnt++
                }
                sb.append(sum)
                i += k
            }
            cur = sb.toString()
        }
        return cur
    }
}
```

## Dart

```dart
class Solution {
  String digitSum(String s, int k) {
    while (s.length > k) {
      final buffer = StringBuffer();
      for (int i = 0; i < s.length; i += k) {
        int sum = 0;
        int end = (i + k < s.length) ? i + k : s.length;
        for (int j = i; j < end; ++j) {
          sum += s.codeUnitAt(j) - 48; // '0' ascii code is 48
        }
        buffer.write(sum.toString());
      }
      s = buffer.toString();
    }
    return s;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func digitSum(s string, k int) string {
	for len(s) > k {
		var sb strings.Builder
		for i := 0; i < len(s); i += k {
			end := i + k
			if end > len(s) {
				end = len(s)
			}
			sum := 0
			for _, ch := range s[i:end] {
				sum += int(ch - '0')
			}
			sb.WriteString(strconv.Itoa(sum))
		}
		s = sb.String()
	}
	return s
}
```

## Ruby

```ruby
def digit_sum(s, k)
  while s.length > k
    new_s = +""
    i = 0
    while i < s.length
      group = s[i, k]
      sum = 0
      group.each_byte { |b| sum += b - 48 }
      new_s << sum.to_s
      i += k
    end
    s = new_s
  end
  s
end
```

## Scala

```scala
object Solution {
    def digitSum(s: String, k: Int): String = {
        var cur = s
        while (cur.length > k) {
            val sb = new StringBuilder
            var i = 0
            while (i < cur.length) {
                var sum = 0
                var cnt = 0
                while (cnt < k && i + cnt < cur.length) {
                    sum += cur.charAt(i + cnt) - '0'
                    cnt += 1
                }
                sb.append(sum.toString)
                i += k
            }
            cur = sb.toString()
        }
        cur
    }
}
```

## Rust

```rust
impl Solution {
    pub fn digit_sum(s: String, k: i32) -> String {
        let mut cur = s;
        let k_usize = k as usize;
        while cur.len() > k_usize {
            let bytes = cur.as_bytes();
            let mut next = String::new();
            let mut i = 0;
            while i < cur.len() {
                let end = std::cmp::min(i + k_usize, cur.len());
                let mut sum: u32 = 0;
                for &b in &bytes[i..end] {
                    sum += (b - b'0') as u32;
                }
                next.push_str(&sum.to_string());
                i = end;
            }
            cur = next;
        }
        cur
    }
}
```

## Racket

```racket
(define/contract (digit-sum s k)
  (-> string? exact-integer? string?)
  (let loop ((cur s))
    (if (<= (string-length cur) k)
        cur
        (let* ((len (string-length cur)))
          (let process ((i 0) (parts '()))
            (if (>= i len)
                (loop (apply string-append (reverse parts)))
                (let* ((end (min (+ i k) len))
                       (sub (substring cur i end))
                       (sum (for/sum ([c (in-string sub)])
                              (- (char->integer c) (char->integer #\0))))
                       (sum-str (number->string sum)))
                  (process (+ i k) (cons sum-str parts)))))))))
```

## Erlang

```erlang
-spec digit_sum(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
digit_sum(S, K) ->
    case byte_size(S) =< K of
        true -> S;
        false -> digit_sum(process(S, K), K)
    end.

process(S, K) ->
    L = binary_to_list(S),
    Groups = chunks(L, K),
    SumBins = [int_to_bin(sum_digits(G)) || G <- Groups],
    list_to_binary(lists:flatten([binary_to_list(B) || B <- SumBins])).

chunks([], _K) -> [];
chunks(List, K) ->
    {Chunk, Rest} = lists:split(K, List),
    [Chunk | chunks(Rest, K)].

sum_digits(Chars) ->
    lists:foldl(fun(C, Acc) -> (C - $0) + Acc end, 0, Chars).

int_to_bin(N) ->
    list_to_binary(integer_to_list(N)).
```

## Elixir

```elixir
defmodule Solution do
  @spec digit_sum(s :: String.t(), k :: integer) :: String.t()
  def digit_sum(s, k) do
    if String.length(s) <= k do
      s
    else
      new_s =
        s
        |> String.graphemes()
        |> Enum.chunk_every(k)
        |> Enum.map(fn chunk ->
          chunk
          |> Enum.map(&String.to_integer/1)
          |> Enum.sum()
          |> Integer.to_string()
        end)
        |> Enum.join()

      digit_sum(new_s, k)
    end
  end
end
```
