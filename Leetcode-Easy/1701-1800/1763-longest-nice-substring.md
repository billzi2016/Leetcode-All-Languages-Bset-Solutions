# 1763. Longest Nice Substring

## Cpp

```cpp
class Solution {
public:
    string longestNiceSubstring(string s) {
        return helper(s, 0, s.size());
    }
private:
    string helper(const string& s, int l, int r) {
        if (r - l < 2) return "";
        bool lower[26] = {false}, upper[26] = {false};
        for (int i = l; i < r; ++i) {
            char c = s[i];
            if ('a' <= c && c <= 'z') lower[c - 'a'] = true;
            else upper[c - 'A'] = true;
        }
        int split = -1;
        for (int i = l; i < r; ++i) {
            char c = s[i];
            if ('a' <= c && c <= 'z') {
                if (!upper[c - 'a']) { split = i; break; }
            } else {
                if (!lower[c - 'A']) { split = i; break; }
            }
        }
        if (split == -1) return s.substr(l, r - l);
        string left = helper(s, l, split);
        string right = helper(s, split + 1, r);
        return left.size() >= right.size() ? left : right;
    }
};
```

## Java

```java
class Solution {
    public String longestNiceSubstring(String s) {
        return helper(s, 0, s.length());
    }
    
    private String helper(String s, int l, int r) { // [l, r)
        if (r - l < 2) {
            return "";
        }
        int lowerMask = 0;
        int upperMask = 0;
        for (int i = l; i < r; i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                lowerMask |= 1 << (c - 'a');
            } else { // uppercase
                upperMask |= 1 << (c - 'A');
            }
        }
        for (int i = l; i < r; i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                int bit = 1 << (c - 'a');
                if ((upperMask & bit) == 0) { // missing uppercase counterpart
                    String left = helper(s, l, i);
                    String right = helper(s, i + 1, r);
                    return left.length() >= right.length() ? left : right;
                }
            } else {
                int bit = 1 << (c - 'A');
                if ((lowerMask & bit) == 0) { // missing lowercase counterpart
                    String left = helper(s, l, i);
                    String right = helper(s, i + 1, r);
                    return left.length() >= right.length() ? left : right;
                }
            }
        }
        // substring is nice
        return s.substring(l, r);
    }
}
```

## Python

```python
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(sub):
            if len(sub) < 2:
                return ""
            chars = set(sub)
            for i, ch in enumerate(sub):
                if ch.swapcase() not in chars:
                    left = helper(sub[:i])
                    right = helper(sub[i+1:])
                    return left if len(left) >= len(right) else right
            return sub
        return helper(s)
```

## Python3

```python
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(sub: str) -> str:
            if len(sub) < 2:
                return ""
            chars = set(sub)
            for i, ch in enumerate(sub):
                if (ch.islower() and ch.upper() not in chars) or (ch.isupper() and ch.lower() not in chars):
                    left = helper(sub[:i])
                    right = helper(sub[i + 1 :])
                    return left if len(left) >= len(right) else right
            return sub

        return helper(s)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static char* copy_substr(const char *s, int l, int r) {
    int len = r - l;
    char *res = (char*)malloc(len + 1);
    memcpy(res, s + l, len);
    res[len] = '\0';
    return res;
}

static char* solve(const char *s, int l, int r) {
    if (r - l < 2) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    int lower[26] = {0}, upper[26] = {0};
    for (int i = l; i < r; ++i) {
        if (islower(s[i]))
            lower[s[i] - 'a'] = 1;
        else
            upper[s[i] - 'A'] = 1;
    }
    int split = -1;
    for (int i = l; i < r; ++i) {
        char c = s[i];
        if (islower(c) && !upper[c - 'a']) { split = i; break; }
        if (isupper(c) && !lower[c - 'A']) { split = i; break; }
    }
    if (split == -1) {
        return copy_substr(s, l, r);
    }
    char *left = solve(s, l, split);
    char *right = solve(s, split + 1, r);
    size_t lenL = strlen(left), lenR = strlen(right);
    char *result;
    if (lenL >= lenR) {
        result = left;
        free(right);
    } else {
        result = right;
        free(left);
    }
    return result;
}

char* longestNiceSubstring(char* s) {
    int n = (int)strlen(s);
    return solve(s, 0, n);
}
```

## Csharp

```csharp
public class Solution
{
    public string LongestNiceSubstring(string s)
    {
        return Helper(s, 0, s.Length);
    }

    private string Helper(string s, int start, int end)
    {
        if (end - start < 2) return "";

        int lowerMask = 0;
        int upperMask = 0;

        for (int i = start; i < end; i++)
        {
            char c = s[i];
            if (char.IsLower(c))
                lowerMask |= 1 << (c - 'a');
            else
                upperMask |= 1 << (c - 'A');
        }

        int diffMask = lowerMask ^ upperMask;
        if (diffMask == 0)
            return s.Substring(start, end - start);

        // Find a split position at a character whose case is mismatched
        for (int i = start; i < end; i++)
        {
            char c = s[i];
            int bit = char.IsLower(c) ? (c - 'a') : (c - 'A');
            if (((diffMask >> bit) & 1) == 1)
            {
                string left = Helper(s, start, i);
                string right = Helper(s, i + 1, end);
                return left.Length >= right.Length ? left : right;
            }
        }

        // Should not reach here
        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestNiceSubstring = function(s) {
    const n = s.length;
    if (n < 2) return "";
    
    const chars = new Set(s);
    for (let i = 0; i < n; i++) {
        const ch = s[i];
        const opposite = isUpper(ch) ? ch.toLowerCase() : ch.toUpperCase();
        if (chars.has(opposite)) continue;
        
        const left = longestNiceSubstring(s.substring(0, i));
        const right = longestNiceSubstring(s.substring(i + 1));
        return left.length >= right.length ? left : right;
    }
    // All characters have both cases
    return s;
};

function isUpper(c) {
    return c >= 'A' && c <= 'Z';
}
```

## Typescript

```typescript
function longestNiceSubstring(s: string): string {
    const n = s.length;
    function isUpper(ch: string): boolean {
        return ch >= 'A' && ch <= 'Z';
    }
    function helper(l: number, r: number): string {
        if (r - l < 2) return "";
        const present = new Set<string>();
        for (let i = l; i < r; ++i) {
            present.add(s[i]);
        }
        for (let i = l; i < r; ++i) {
            const ch = s[i];
            const counterpart = isUpper(ch) ? ch.toLowerCase() : ch.toUpperCase();
            if (!present.has(counterpart)) {
                const left = helper(l, i);
                const right = helper(i + 1, r);
                return left.length >= right.length ? left : right;
            }
        }
        return s.slice(l, r);
    }
    return helper(0, n);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestNiceSubstring($s) {
        return $this->helper($s);
    }

    private function helper(string $s): string {
        $len = strlen($s);
        if ($len < 2) {
            return "";
        }
        $maskLower = 0;
        $maskUpper = 0;
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (ctype_lower($c)) {
                $maskLower |= 1 << (ord($c) - 97);
            } else {
                $maskUpper |= 1 << (ord($c) - 65);
            }
        }

        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (ctype_lower($c)) {
                $bit = 1 << (ord($c) - 97);
                if (($maskUpper & $bit) == 0) {
                    $left = $this->helper(substr($s, 0, $i));
                    $right = $this->helper(substr($s, $i + 1));
                    return strlen($left) >= strlen($right) ? $left : $right;
                }
            } else {
                $bit = 1 << (ord($c) - 65);
                if (($maskLower & $bit) == 0) {
                    $left = $this->helper(substr($s, 0, $i));
                    $right = $this->helper(substr($s, $i + 1));
                    return strlen($left) >= strlen($right) ? $left : $right;
                }
            }
        }

        // All characters have both cases present
        return $s;
    }
}
```

## Swift

```swift
class Solution {
    func longestNiceSubstring(_ s: String) -> String {
        let chars = Array(s)
        return helper(chars, 0, chars.count)
    }
    
    private func helper(_ arr: [Character], _ start: Int, _ end: Int) -> String {
        if end - start < 2 { return "" }
        var present = Set<Character>()
        for i in start..<end {
            present.insert(arr[i])
        }
        for i in start..<end {
            let c = arr[i]
            let opposite: Character
            if c.isUppercase {
                opposite = Character(String(c).lowercased())
            } else {
                opposite = Character(String(c).uppercased())
            }
            if !present.contains(opposite) {
                let left = helper(arr, start, i)
                let right = helper(arr, i + 1, end)
                return left.count >= right.count ? left : right
            }
        }
        return String(arr[start..<end])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestNiceSubstring(s: String): String {
        return helper(s, 0, s.length)
    }

    private fun helper(s: String, start: Int, end: Int): String {
        if (end - start < 2) return ""
        var mask = 0
        for (i in start until end) {
            val c = s[i]
            if (c.isUpperCase()) {
                mask = mask or (1 shl (c - 'A'))
            } else {
                mask = mask or (1 shl (c - 'a' + 26))
            }
        }
        for (i in start until end) {
            val c = s[i]
            if (c.isUpperCase()) {
                val lowerBit = 1 shl (c - 'A' + 26)
                if ((mask and lowerBit) == 0) {
                    val left = helper(s, start, i)
                    val right = helper(s, i + 1, end)
                    return if (left.length >= right.length) left else right
                }
            } else {
                val upperBit = 1 shl (c - 'a')
                if ((mask and upperBit) == 0) {
                    val left = helper(s, start, i)
                    val right = helper(s, i + 1, end)
                    return if (left.length >= right.length) left else right
                }
            }
        }
        return s.substring(start, end)
    }
}
```

## Dart

```dart
class Solution {
  String longestNiceSubstring(String s) {
    int n = s.length;
    if (n < 2) return "";
    return _helper(s, 0, n);
  }

  String _helper(String s, int l, int r) {
    if (r - l <= 1) return "";
    int lowerMask = 0;
    int upperMask = 0;
    for (int i = l; i < r; i++) {
      int code = s.codeUnitAt(i);
      if (code >= 97) { // 'a'..'z'
        lowerMask |= 1 << (code - 97);
      } else { // 'A'..'Z'
        upperMask |= 1 << (code - 65);
      }
    }

    for (int i = l; i < r; i++) {
      int code = s.codeUnitAt(i);
      if (code >= 97) {
        int bit = 1 << (code - 97);
        if ((upperMask & bit) == 0) {
          String left = _helper(s, l, i);
          String right = _helper(s, i + 1, r);
          return left.length >= right.length ? left : right;
        }
      } else {
        int bit = 1 << (code - 65);
        if ((lowerMask & bit) == 0) {
          String left = _helper(s, l, i);
          String right = _helper(s, i + 1, r);
          return left.length >= right.length ? left : right;
        }
      }
    }

    // All characters have both cases in this segment.
    return s.substring(l, r);
  }
}
```

## Golang

```go
func longestNiceSubstring(s string) string {
	var helper func(l, r int) string
	helper = func(l, r int) string {
		if r-l < 2 {
			return ""
		}
		lowerMask, upperMask := 0, 0
		for i := l; i < r; i++ {
			c := s[i]
			if c >= 'a' && c <= 'z' {
				lowerMask |= 1 << (c - 'a')
			} else {
				upperMask |= 1 << (c - 'A')
			}
		}
		for i := l; i < r; i++ {
			c := s[i]
			if c >= 'a' && c <= 'z' {
				bit := 1 << (c - 'a')
				if upperMask&bit == 0 {
					left := helper(l, i)
					right := helper(i+1, r)
					if len(left) >= len(right) {
						return left
					}
					return right
				}
			} else {
				bit := 1 << (c - 'A')
				if lowerMask&bit == 0 {
					left := helper(l, i)
					right := helper(i+1, r)
					if len(left) >= len(right) {
						return left
					}
					return right
				}
			}
		}
		return s[l:r]
	}
	return helper(0, len(s))
}
```

## Ruby

```ruby
def longest_nice_substring(s)
  def helper(str)
    return "" if str.length < 2
    lower = 0
    upper = 0
    str.each_char do |c|
      if c >= 'a' && c <= 'z'
        lower |= 1 << (c.ord - 97)
      else
        upper |= 1 << (c.ord - 65)
      end
    end

    split_idx = nil
    str.each_char.with_index do |c, i|
      if c >= 'a' && c <= 'z'
        bit = 1 << (c.ord - 97)
        unless (upper & bit) != 0
          split_idx = i
          break
        end
      else
        bit = 1 << (c.ord - 65)
        unless (lower & bit) != 0
          split_idx = i
          break
        end
      end
    end

    return str if split_idx.nil?

    left = helper(str[0...split_idx])
    right = helper(str[(split_idx + 1)..-1] || "")
    left.length >= right.length ? left : right
  end

  helper(s)
end
```

## Scala

```scala
object Solution {
    def longestNiceSubstring(s: String): String = {
        val n = s.length
        def helper(l: Int, r: Int): String = {
            if (r - l < 2) return ""
            var lowerMask = 0
            var upperMask = 0
            var i = l
            while (i < r) {
                val c = s.charAt(i)
                if (c >= 'a' && c <= 'z') {
                    lowerMask |= 1 << (c - 'a')
                } else {
                    upperMask |= 1 << (c - 'A')
                }
                i += 1
            }
            i = l
            while (i < r) {
                val c = s.charAt(i)
                if (c >= 'a' && c <= 'z') {
                    if ((upperMask & (1 << (c - 'a'))) == 0) {
                        val left = helper(l, i)
                        val right = helper(i + 1, r)
                        return if (left.length >= right.length) left else right
                    }
                } else {
                    if ((lowerMask & (1 << (c - 'A'))) == 0) {
                        val left = helper(l, i)
                        val right = helper(i + 1, r)
                        return if (left.length >= right.length) left else right
                    }
                }
                i += 1
            }
            s.substring(l, r)
        }
        helper(0, n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_nice_substring(s: String) -> String {
        fn helper(slice: &[u8]) -> String {
            let n = slice.len();
            if n == 0 {
                return String::new();
            }
            let mut lower_mask: u32 = 0;
            let mut upper_mask: u32 = 0;
            for &c in slice {
                if c >= b'a' && c <= b'z' {
                    lower_mask |= 1 << (c - b'a');
                } else {
                    upper_mask |= 1 << (c - b'A');
                }
            }
            let mut split_idx: Option<usize> = None;
            for i in 0..n {
                let c = slice[i];
                if c >= b'a' && c <= b'z' {
                    let bit = 1 << (c - b'a');
                    if upper_mask & bit == 0 {
                        split_idx = Some(i);
                        break;
                    }
                } else {
                    let bit = 1 << (c - b'A');
                    if lower_mask & bit == 0 {
                        split_idx = Some(i);
                        break;
                    }
                }
            }
            match split_idx {
                None => String::from_utf8(slice.to_vec()).unwrap(),
                Some(idx) => {
                    let left = helper(&slice[0..idx]);
                    let right = helper(&slice[idx + 1..]);
                    if left.len() >= right.len() { left } else { right }
                }
            }
        }

        helper(s.as_bytes())
    }
}
```

## Racket

```racket
(define/contract (longest-nice-substring s)
  (-> string? string?)
  (let* ([n (string-length s)]
         [best-start 0]
         [best-len 0])
    (for ([i (in-range n)])
      (let ([lower-mask 0]
            [upper-mask 0])
        (for ([j (in-range i n)])
          (define ch (string-ref s j))
          (define idx (- (char->integer (char-downcase ch))
                         (char->integer #\a)))
          (if (char=? (char-downcase ch) ch)
              (set! lower-mask (bitwise-ior lower-mask (arithmetic-shift 1 idx)))
              (set! upper-mask (bitwise-ior upper-mask (arithmetic-shift 1 idx))))
          (when (= lower-mask upper-mask)
            (define len (+ 1 (- j i)))
            (when (> len best-len)
              (set! best-start i)
              (set! best-len len))))))
    (if (= best-len 0)
        ""
        (substring s best-start (+ best-start best-len)))))
```

## Erlang

```erlang
-spec longest_nice_substring(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
longest_nice_substring(S) ->
    Len = byte_size(S),
    longest_nice_substring(0, Len, S, <<>>, 0).

longest_nice_substring(Start, Len, _S, Best, _BestLen) when Start >= Len ->
    Best;
longest_nice_substring(Start, Len, S, Best, BestLen) ->
    {NewBest, NewBestLen} = longest_from_start(Start, Len, S, Best, BestLen),
    longest_nice_substring(Start + 1, Len, S, NewBest, NewBestLen).

longest_from_start(Start, Len, S, Best, BestLen) ->
    longest_from_start(Start, Start + 1, Len, S, Best, BestLen).

longest_from_start(_Start, End, Len, _S, Best, BestLen) when End > Len ->
    {Best, BestLen};
longest_from_start(Start, End, Len, S, Best, BestLen) ->
    Sub = binary:part(S, {Start, End - Start}),
    {TmpBest, TmpLen} =
        if
            (End - Start) > BestLen andalso is_nice(Sub) ->
                {Sub, End - Start};
            true ->
                {Best, BestLen}
        end,
    longest_from_start(Start, End + 1, Len, S, TmpBest, TmpLen).

is_nice(Bin) ->
    is_nice(Bin, 0, 0).

is_nice(<<>>, LowerMask, UpperMask) ->
    (LowerMask bxor UpperMask) =:= 0;
is_nice(<<C, Rest/binary>>, LowerMask, UpperMask) when C >= $a, C =< $z ->
    NewL = LowerMask bor (1 bsl (C - $a)),
    is_nice(Rest, NewL, UpperMask);
is_nice(<<C, Rest/binary>>, LowerMask, UpperMask) when C >= $A, C =< $Z ->
    NewU = UpperMask bor (1 bsl (C - $A)),
    is_nice(Rest, LowerMask, NewU).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec longest_nice_substring(s :: String.t) :: String.t
  def longest_nice_substring(s) do
    len = String.length(s)

    0..(len - 1)
    |> Enum.reduce("", fn i, best ->
      (i + 1)..len
      |> Enum.reduce(best, fn j, acc ->
        sub = String.slice(s, i, j - i)

        if nice?(sub) and String.length(sub) > String.length(acc) do
          sub
        else
          acc
        end
      end)
    end)
  end

  defp nice?(sub) do
    {lower_mask, upper_mask} =
      sub
      |> String.to_charlist()
      |> Enum.reduce({0, 0}, fn c, {l, u} ->
        cond do
          c >= ?a and c <= ?z -> {l ||| (1 <<< (c - ?a)), u}
          c >= ?A and c <= ?Z -> {l, u ||| (1 <<< (c - ?A))}
          true -> {l, u}
        end
      end)

    lower_mask == upper_mask
  end
end
```
