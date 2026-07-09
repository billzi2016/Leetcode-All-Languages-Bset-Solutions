# 1147. Longest Chunked Palindrome Decomposition

## Cpp

```cpp
class Solution {
public:
    int longestDecomposition(string text) {
        int n = text.size();
        int i = 0, j = n - 1;
        int ans = 0;
        while (i < j) {
            bool matched = false;
            for (int len = 1; i + len - 1 < j; ++len) {
                bool ok = true;
                for (int k = 0; k < len; ++k) {
                    if (text[i + k] != text[j - len + 1 + k]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    ans += 2;
                    i += len;
                    j -= len;
                    matched = true;
                    break;
                }
            }
            if (!matched) break;
        }
        if (i <= j) ++ans; // remaining middle part
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestDecomposition(String text) {
        int n = text.length();
        int left = 0, right = n - 1;
        int chunks = 0;
        while (left < right) {
            boolean matched = false;
            // try increasing length of the chunk
            for (int len = 1; left + len - 1 < right - len + 1; len++) {
                if (text.substring(left, left + len).equals(text.substring(right - len + 1, right + 1))) {
                    chunks += 2;
                    left += len;
                    right -= len;
                    matched = true;
                    break;
                }
            }
            if (!matched) {
                break;
            }
        }
        // any remaining middle part forms one chunk
        if (left <= right) {
            chunks += 1;
        }
        return chunks;
    }
}
```

## Python

```python
class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            # find smallest length l where prefix equals suffix
            l = 1
            found = False
            while i + l - 1 < j - l + 1:
                if text[i:i+l] == text[j-l+1:j+1]:
                    ans += 2
                    i += l
                    j -= l
                    found = True
                    break
                l += 1
            if not found:
                # cannot find matching pair, the remaining middle is one chunk
                ans += 1
                return ans
        # when loop ends, either i == j (one char left) or i > j (no chars left)
        if i == j:
            ans += 1
        elif i > j:
            # all characters are paired already, nothing to add
            pass
        else:  # i < j but loop exited, shouldn't happen
            ans += 1
        return ans
```

## Python3

```python
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            l = 1
            # expand until prefix of length l equals suffix of length l
            while i + l - 1 < j - l + 1 and text[i:i + l] != text[j - l + 1:j + 1]:
                l += 1
            # if they overlap or cross, break
            if i + l - 1 >= j - l + 1:
                break
            ans += 2
            i += l
            j -= l
        # remaining middle part (could be empty)
        if i <= j:
            ans += 1
        return ans
```

## C

```c
#include <string.h>

int longestDecomposition(char* text) {
    int n = (int)strlen(text);
    int l = 0, r = n - 1;
    int ans = 0;

    while (l < r) {
        int len = 1;
        int found = 0;
        while (l + len - 1 < r - len + 1) {
            if (strncmp(text + l, text + r - len + 1, len) == 0) {
                found = 1;
                break;
            }
            ++len;
        }
        if (!found) break;
        ans += 2;
        l += len;
        r -= len;
    }

    if (l <= r) ++ans;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestDecomposition(string text) {
        int n = text.Length;
        int i = 0, j = n - 1;
        int ans = 0;
        while (i <= j) {
            bool matched = false;
            // try to find the smallest matching prefix/suffix pair
            for (int len = 1; i + len - 1 < j - len + 1; ++len) {
                if (text.Substring(i, len) == text.Substring(j - len + 1, len)) {
                    matched = true;
                    ans += 2;
                    i += len;
                    j -= len;
                    break;
                }
            }
            if (!matched) {
                // remaining part is a single middle chunk
                ans += 1;
                break;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var longestDecomposition = function(text) {
    let n = text.length;
    let l = 0, r = n - 1;
    let ans = 0;
    while (l < r) {
        let found = false;
        // maximum possible length for a matching chunk
        const maxLen = Math.floor((r - l + 1) / 2);
        for (let len = 1; len <= maxLen; ++len) {
            if (text.slice(l, l + len) === text.slice(r - len + 1, r + 1)) {
                ans += 2;
                l += len;
                r -= len;
                found = true;
                break;
            }
        }
        if (!found) {
            return ans + 1; // the remaining middle part is one chunk
        }
    }
    // when l == r, there's a single character left as a chunk
    if (l === r) ans += 1;
    return ans;
};
```

## Typescript

```typescript
function longestDecomposition(text: string): number {
    let i = 0;
    let j = text.length - 1;
    let ans = 0;

    while (i < j) {
        let found = false;
        // maximum possible length for a matching chunk is limited by remaining distance
        const maxLen = Math.floor((j - i + 1) / 2);
        for (let len = 1; len <= maxLen; ++len) {
            if (text.substr(i, len) === text.substr(j - len + 1, len)) {
                ans += 2;
                i += len;
                j -= len;
                found = true;
                break;
            }
        }
        if (!found) {
            // remaining middle part forms one chunk
            return ans + 1;
        }
    }

    // If pointers meet exactly at a character, it forms an additional chunk
    if (i === j) ans += 1;

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function longestDecomposition($text) {
        $n = strlen($text);
        $i = 0;
        $j = $n - 1;
        $ans = 0;

        while ($i < $j) {
            $found = false;
            // try increasing length of the chunk
            for ($len = 1; $i + $len - 1 < $j - $len + 1; $len++) {
                if (substr($text, $i, $len) === substr($text, $j - $len + 1, $len)) {
                    $ans += 2;
                    $i += $len;
                    $j -= $len;
                    $found = true;
                    break;
                }
            }
            if (!$found) {
                break;
            }
        }

        if ($i <= $j) {
            $ans += 1; // the middle part
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestDecomposition(_ text: String) -> Int {
        let chars = Array(text)
        var i = 0
        var j = chars.count - 1
        var answer = 0
        var left = ""
        var right = ""
        
        while i <= j {
            left.append(chars[i])
            right = String(chars[j]) + right
            i += 1
            j -= 1
            
            if left == right {
                if i > j {
                    // No characters remain, this chunk is the middle one.
                    answer += 1
                } else {
                    // Matched a pair of chunks on both sides.
                    answer += 2
                }
                left = ""
                right = ""
            }
        }
        
        // If there is an unmatched middle part left.
        if !left.isEmpty {
            answer += 1
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestDecomposition(text: String): Int {
        var i = 0
        var j = text.length - 1
        var ans = 0
        while (i < j) {
            var found = false
            val maxLen = (j - i + 1) / 2
            for (len in 1..maxLen) {
                if (text.regionMatches(i, text, j - len + 1, len)) {
                    ans += 2
                    i += len
                    j -= len
                    found = true
                    break
                }
            }
            if (!found) {
                // Remaining middle part forms a single chunk
                ans += 1
                return ans
            }
        }
        if (i == j) ans += 1
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int longestDecomposition(String text) {
    int n = text.length;
    int i = 0, j = n - 1;
    int ans = 0;
    while (i < j) {
      bool found = false;
      for (int len = 1; i + len - 1 < j - len + 1; ++len) {
        if (text.substring(i, i + len) == text.substring(j - len + 1, j + 1)) {
          ans += 2;
          i += len;
          j -= len;
          found = true;
          break;
        }
      }
      if (!found) {
        return ans + 1; // the remaining middle part counts as one chunk
      }
    }
    if (i == j) ans += 1; // single character left in the middle
    return ans;
  }
}
```

## Golang

```go
func longestDecomposition(text string) int {
	n := len(text)
	i, j := 0, n-1
	count := 0
	for i <= j {
		found := false
		for l := 1; i+l-1 < j-l+1; l++ {
			if text[i:i+l] == text[j-l+1:j+1] {
				count += 2
				i += l
				j -= l
				found = true
				break
			}
		}
		if !found {
			count++
			break
		}
	}
	return count
}
```

## Ruby

```ruby
def longest_decomposition(text)
  i = 0
  j = text.length - 1
  ans = 0

  while i < j
    found = false
    len = 1
    # ensure the two parts do not cross each other
    while i + len <= j - len + 1
      if text[i, len] == text[j - len + 1, len]
        ans += 2
        i += len
        j -= len
        found = true
        break
      end
      len += 1
    end

    unless found
      # remaining middle part counts as one chunk
      ans += 1
      return ans
    end
  end

  # If there is a single character left, it forms its own chunk
  ans += 1 if i == j
  ans
end
```

## Scala

```scala
object Solution {
    def longestDecomposition(text: String): Int = {
        var i = 0
        var j = text.length - 1
        var ans = 0
        while (i <= j) {
            var found = false
            var len = 1
            val maxLen = (j - i + 1) / 2
            while (len <= maxLen && !found) {
                if (text.regionMatches(i, text, j - len + 1, len)) {
                    found = true
                } else {
                    len += 1
                }
            }
            if (found) {
                ans += 2
                i += len
                j -= len
            } else {
                ans += 1
                i = j + 1 // exit loop
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_decomposition(text: String) -> i32 {
        let bytes = text.as_bytes();
        let n = bytes.len();
        let mut left = 0usize;
        let mut right = n;
        let mut ans: i32 = 0;

        while left < right {
            let mut found = false;
            // maximum possible length for a matching chunk without overlapping
            let max_len = (right - left) / 2;
            for len in 1..=max_len {
                if &bytes[left..left + len] == &bytes[right - len..right] {
                    ans += 2;
                    left += len;
                    right -= len;
                    found = true;
                    break;
                }
            }
            if !found {
                // the remaining middle part forms one chunk
                return ans + 1;
            }
        }

        // If pointers meet exactly, there is a single middle chunk left
        if left == right && left < n {
            ans += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (longest-decomposition text)
  (-> string? exact-integer?)
  (let* ((n (string-length text)))
    (let loop ((i 0) (j (- n 1)) (cnt 0))
      (if (< i j)
          (let search ((l 1))
            (if (> l (+ (- j i) 1))
                (+ cnt 1) ; no matching pair, middle chunk
                (let* ((pref (substring text i (+ i l)))
                       (suf-start (+ (- j l) 1))
                       (suf (substring text suf-start (+ j 1))))
                  (if (string=? pref suf)
                      (loop (+ i l) (- j l) (+ cnt 2))
                      (search (+ l 1))))))
          (+ cnt (if (= i j) 1 0))))))
```

## Erlang

```erlang
-module(solution).
-export([longest_decomposition/1]).

-spec longest_decomposition(Text :: unicode:unicode_binary()) -> integer().
longest_decomposition(Text) ->
    N = byte_size(Text),
    longest_decomp(Text, 0, N - 1, 0).

%% Recursive helper
longest_decomp(_Text, L, R, Ans) when L > R ->
    Ans;
longest_decomp(_Text, L, R, Ans) when L == R ->
    Ans + 1;
longest_decomp(Text, L, R, Ans) ->
    MaxLen = (R - L + 1) div 2,
    case find_len(Text, L, R, 1, MaxLen) of
        undefined ->
            Ans + 1;                     % remaining part is a single chunk
        Len ->
            NewL = L + Len,
            NewR = R - Len,
            if NewL > NewR ->
                    Ans + 2;              % consumed everything with this pair
               true ->
                    longest_decomp(Text, NewL, NewR, Ans + 2)
            end
    end.

%% Find the smallest length where prefix == suffix
find_len(_Text, _L, _R, CurLen, MaxLen) when CurLen > MaxLen ->
    undefined;
find_len(Text, L, R, CurLen, MaxLen) ->
    Prefix = binary:part(Text, L, CurLen),
    SuffixStart = R - CurLen + 1,
    Suffix = binary:part(Text, SuffixStart, CurLen),
    if Prefix =:= Suffix ->
            CurLen;
       true ->
            find_len(Text, L, R, CurLen + 1, MaxLen)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_decomposition(text :: String.t()) :: integer
  def longest_decomposition(text) do
    n = byte_size(text)
    go(text, 0, n - 1, 0)
  end

  defp go(_text, i, j, cnt) when i > j, do: cnt
  defp go(_text, i, j, cnt) when i == j, do: cnt + 1

  defp go(text, i, j, cnt) do
    max_len = div(j - i + 1, 2)

    len =
      Enum.find(1..max_len, fn l ->
        :binary.part(text, i, l) == :binary.part(text, j - l + 1, l)
      end)

    case len do
      nil -> cnt + 1
      l -> go(text, i + l, j - l, cnt + 2)
    end
  end
end
```
