# 0880. Decoded String at Index

## Cpp

```cpp
class Solution {
public:
    string decodeAtIndex(string s, int k) {
        unsigned long long size = 0;
        for (char c : s) {
            if (isdigit(c)) {
                size *= (c - '0');
            } else {
                ++size;
            }
        }
        for (int i = (int)s.size() - 1; i >= 0; --i) {
            char c = s[i];
            k %= (int)size;
            if (k == 0 && isalpha(c)) return string(1, c);
            if (isdigit(c)) {
                size /= (c - '0');
            } else {
                --size;
            }
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String decodeAtIndex(String s, int k) {
        long size = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                size += 1;
            } else { // digit
                size *= (c - '0');
            }
        }

        long kLong = k;
        for (int i = s.length() - 1; i >= 0; --i) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                if (kLong == size || kLong == 0) {
                    return String.valueOf(c);
                }
                size--;
            } else { // digit
                int d = c - '0';
                size /= d;
                kLong = ((kLong - 1) % size) + 1;
            }
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = 0
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        for ch in reversed(s):
            k %= size
            if k == 0 and ch.isalpha():
                return ch
            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1
        return ""
```

## Python3

```python
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        for ch in reversed(s):
            if ch.isdigit():
                d = int(ch)
                size //= d
                k %= size
                if k == 0:
                    k = size
            else:
                if k == size:
                    return ch
                size -= 1
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* decodeAtIndex(char* s, int k) {
    unsigned long long size = 0;
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        if (isdigit(s[i])) {
            size *= (unsigned long long)(s[i] - '0');
        } else {
            size += 1;
        }
    }

    for (int i = n - 1; i >= 0; --i) {
        char c = s[i];
        if (isdigit(c)) {
            unsigned int d = c - '0';
            size /= d;
            k = (int)((unsigned long long)k % size);
        } else {
            if (k == 0 || k == (int)size) {
                char* ans = (char*)malloc(2);
                ans[0] = c;
                ans[1] = '\0';
                return ans;
            }
            size--;
        }
    }

    return NULL; // Should never reach here
}
```

## Csharp

```csharp
public class Solution {
    public string DecodeAtIndex(string s, int k) {
        long size = 0;
        foreach (char c in s) {
            if (c >= '0' && c <= '9') {
                size *= c - '0';
            } else {
                size += 1;
            }
        }

        long kLong = k;
        for (int i = s.Length - 1; i >= 0; --i) {
            char c = s[i];
            if (c >= '0' && c <= '9') {
                int d = c - '0';
                size /= d;
                kLong %= size;
            } else {
                if (kLong == 0 || kLong == size) {
                    return c.ToString();
                }
                size -= 1;
            }
        }

        return "";
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
var decodeAtIndex = function(s, k) {
    let size = 0n;
    const bigK = BigInt(k);
    // First pass: compute total length using BigInt
    for (let ch of s) {
        if (ch >= '0' && ch <= '9') {
            size *= BigInt(ch);
        } else {
            size += 1n;
        }
    }

    let curK = bigK;
    // Reverse traversal to find the k-th character
    for (let i = s.length - 1; i >= 0; --i) {
        const ch = s[i];
        if (ch >= '0' && ch <= '9') {
            size /= BigInt(ch);
            curK %= size;
        } else {
            // letter case
            if (curK === 0n || curK === size) {
                return ch;
            }
            size -= 1n;
        }
    }
    return '';
};
```

## Typescript

```typescript
function decodeAtIndex(s: string, k: number): string {
    let size = 0n;
    for (const ch of s) {
        if (ch >= 'a' && ch <= 'z') {
            size += 1n;
        } else { // digit
            const d = BigInt(ch.charCodeAt(0) - 48);
            size *= d;
        }
    }

    let K = BigInt(k);
    for (let i = s.length - 1; i >= 0; --i) {
        const ch = s[i];
        if (ch >= '2' && ch <= '9') {
            const d = BigInt(ch.charCodeAt(0) - 48);
            size /= d;
            K %= size;
            if (K === 0n) K = size;
        } else { // letter
            if (K === size) return ch;
            size -= 1n;
        }
    }
    return "";
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
    function decodeAtIndex($s, $k) {
        $size = 0;
        $len = strlen($s);
        // Compute the length of the decoded string (may be huge)
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c >= '0' && $c <= '9') {
                $size *= intval($c);
            } else {
                $size += 1;
            }
        }

        // Iterate backwards to find the k-th character
        for ($i = $len - 1; $i >= 0; $i--) {
            $c = $s[$i];
            $k %= $size;
            if ($k == 0 && $c >= 'a' && $c <= 'z') {
                return $c;
            }

            if ($c >= '0' && $c <= '9') {
                $size = intdiv($size, intval($c));
            } else {
                $size -= 1;
            }
        }

        return '';
    }
}
```

## Swift

```swift
class Solution {
    func decodeAtIndex(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        var size: UInt64 = 0
        for ch in chars {
            if let val = ch.wholeNumberValue {
                size *= UInt64(val)
            } else {
                size += 1
            }
        }
        var k64 = UInt64(k)
        for i in stride(from: chars.count - 1, through: 0, by: -1) {
            let ch = chars[i]
            if let val = ch.wholeNumberValue {
                k64 %= size
                size /= UInt64(val)
            } else {
                k64 %= size
                if k64 == 0 {
                    return String(ch)
                }
                size -= 1
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decodeAtIndex(s: String, k: Int): String {
        var size = 0L
        for (ch in s) {
            if (ch.isDigit()) {
                val d = (ch - '0').toLong()
                size *= d
            } else {
                size += 1
            }
        }

        var kk = k.toLong()
        for (i in s.length - 1 downTo 0) {
            val ch = s[i]
            if (ch.isDigit()) {
                val d = (ch - '0').toLong()
                size /= d
                kk %= size
                if (kk == 0L) kk = size
            } else {
                if (kk == size || kk == 0L) return ch.toString()
                size--
            }
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String decodeAtIndex(String s, int k) {
    int size = 0;
    // Compute the length of the decoded string (may be huge)
    for (int i = 0; i < s.length; ++i) {
      int code = s.codeUnitAt(i);
      if (code >= 48 && code <= 57) { // digit
        size *= (code - 48);
      } else { // letter
        size += 1;
      }
    }

    for (int i = s.length - 1; i >= 0; --i) {
      int code = s.codeUnitAt(i);
      k %= size;
      if (k == 0 && !(code >= 48 && code <= 57)) {
        return String.fromCharCode(code);
      }
      if (code >= 48 && code <= 57) { // digit
        size ~/= (code - 48);
      } else { // letter
        size -= 1;
      }
    }

    return "";
  }
}
```

## Golang

```go
func decodeAtIndex(s string, k int) string {
	var size int64 = 0
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c >= '0' && c <= '9' {
			size *= int64(c - '0')
		} else {
			size++
		}
	}
	kk := int64(k)
	for i := len(s) - 1; i >= 0; i-- {
		c := s[i]
		if c >= '2' && c <= '9' {
			d := int64(c - '0')
			size /= d
			kk %= size
			if kk == 0 {
				kk = size
			}
		} else {
			if kk == size || kk == 0 {
				return string(c)
			}
			size--
		}
	}
	return ""
}
```

## Ruby

```ruby
def decode_at_index(s, k)
  total_len = 0
  s.each_char do |c|
    if c >= '0' && c <= '9'
      total_len *= c.to_i
    else
      total_len += 1
    end
  end

  i = s.length - 1
  while i >= 0
    c = s[i]
    if c >= '0' && c <= '9'
      d = c.to_i
      total_len /= d
      k %= total_len
      k = total_len if k == 0
    else
      return c if k == total_len
      total_len -= 1
    end
    i -= 1
  end
end
```

## Scala

```scala
object Solution {
    def decodeAtIndex(s: String, k: Int): String = {
        var size: Long = 0L
        for (ch <- s) {
            if (ch.isDigit) {
                size *= (ch - '0')
            } else {
                size += 1
            }
        }

        var kk: Long = k.toLong
        var i = s.length - 1
        while (i >= 0) {
            val ch = s.charAt(i)
            if (ch.isDigit) {
                val d = ch - '0'
                size /= d
                kk = ((kk - 1) % size) + 1
            } else {
                if (kk == size) return ch.toString
                size -= 1
            }
            i -= 1
        }
        ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn decode_at_index(s: String, k: i32) -> String {
        let mut size: u128 = 0;
        for ch in s.chars() {
            if ch.is_ascii_digit() {
                let d = ch.to_digit(10).unwrap() as u128;
                size *= d;
            } else {
                size += 1;
            }
        }

        let mut k = k as u128;

        for ch in s.chars().rev() {
            // bring k within current size
            k = (k - 1) % size + 1;
            if ch.is_ascii_digit() {
                let d = ch.to_digit(10).unwrap() as u128;
                size /= d;
            } else {
                if k == size {
                    return ch.to_string();
                }
                size -= 1;
            }
        }

        unreachable!()
    }
}
```

## Racket

```racket
(define/contract (decode-at-index s k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length s))
         (total
          (let loop ((i 0) (len 0))
            (if (= i n)
                len
                (let ((c (string-ref s i)))
                  (if (char-alphabetic? c)
                      (loop (+ i 1) (+ len 1))
                      (let ((d (- (char->integer c) (char->integer #\0))))
                        (loop (+ i 1) (* len d)))))))))
    (let rec ((i (- n 1)) (len total) (k k))
      (if (< i 0)
          ""
          (let ((c (string-ref s i)))
            (if (char-alphabetic? c)
                (if (= k len)
                    (string c)
                    (rec (- i 1) (- len 1) k))
                (let* ((d (- (char->integer c) (char->integer #\0)))
                       (len-div (quotient len d))
                       (k-mod (+ (modulo (- k 1) len-div) 1)))
                  (rec (- i 1) len-div k-mod))))))))
```

## Erlang

```erlang
-module(solution).
-export([decode_at_index/2]).

-spec decode_at_index(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
decode_at_index(S, K) ->
    List = binary_to_list(S),
    Len = lists:foldl(fun(C, L) ->
        if C >= $a, C =< $z -> L + 1;
           true -> D = C - $0, L * D
        end
    end, 0, List),
    find_char(lists:reverse(List), Len, K).

find_char([C|Rest], Len, K) ->
    case C of
        $0..$9 ->
            D = C - $0,
            NewLen = Len div D,
            Rem = K rem NewLen,
            NewK = if Rem == 0 -> NewLen; true -> Rem end,
            find_char(Rest, NewLen, NewK);
        _ ->
            case K of
                Len -> <<C>>;
                _ -> find_char(Rest, Len - 1, K)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec decode_at_index(s :: String.t(), k :: integer()) :: String.t()
  def decode_at_index(s, k) do
    chars = String.graphemes(s)

    total_len =
      Enum.reduce(chars, 0, fn ch, acc ->
        case Integer.parse(ch) do
          {digit, ""} -> acc * digit
          :error -> acc + 1
        end
      end)

    find_char(Enum.reverse(chars), total_len, k)
  end

  defp find_char([ch | rest], cur_len, k) do
    case Integer.parse(ch) do
      {digit, ""} ->
        new_len = div(cur_len, digit)
        new_k = rem(k - 1, new_len) + 1
        find_char(rest, new_len, new_k)

      :error ->
        if k == cur_len do
          ch
        else
          find_char(rest, cur_len - 1, k)
        end
    end
  end

  defp find_char([], _cur_len, _k), do: nil
end
```
