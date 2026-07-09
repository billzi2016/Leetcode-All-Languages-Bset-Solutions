# 0005. Longest Palindromic Substring

## Cpp

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n == 0) return "";
        int start = 0, maxLen = 1;
        auto expand = [&](int left, int right) -> int {
            while (left >= 0 && right < n && s[left] == s[right]) {
                --left;
                ++right;
            }
            return right - left - 1; // length of palindrome
        };
        for (int i = 0; i < n; ++i) {
            int len1 = expand(i, i);       // odd length
            int len2 = expand(i, i + 1);   // even length
            int len = max(len1, len2);
            if (len > maxLen) {
                maxLen = len;
                start = i - (len - 1) / 2;
            }
        }
        return s.substr(start, maxLen);
    }
};
```

## Java

```java
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 2) {
            return s;
        }
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start + 1) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private int expand(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```

## Python

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        start, max_len = 0, 1

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # after loop, left and right are one step beyond palindrome bounds
            return left + 1, right - 1

        for i in range(n):
            # odd length palindrome
            l, r = expand(i, i)
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            # even length palindrome
            l, r = expand(i, i + 1)
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1

        return s[start:start + max_len]
```

## Python3

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start = 0
        max_len = 1

        def expand(l: int, r: int) -> int:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(n):
            len1 = expand(i, i)
            if len1 > max_len:
                max_len = len1
                start = i - (len1 // 2)

            len2 = expand(i, i + 1)
            if len2 > max_len:
                max_len = len2
                start = i - (len2 // 2) + 1

        return s[start:start + max_len]
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int expand(const char *s, int left, int right, int n) {
    while (left >= 0 && right < n && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

char* longestPalindrome(char* s) {
    if (!s) {
        char *empty = (char *)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    int n = (int)strlen(s);
    if (n == 0) {
        char *empty = (char *)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    int start = 0, maxLen = 1;

    for (int i = 0; i < n; ++i) {
        int len1 = expand(s, i, i, n);       // odd length
        if (len1 > maxLen) {
            maxLen = len1;
            start = i - (len1 - 1) / 2;
        }

        int len2 = expand(s, i, i + 1, n);   // even length
        if (len2 > maxLen) {
            maxLen = len2;
            start = i - (len2 / 2 - 1);
        }
    }

    char *res = (char *)malloc(maxLen + 1);
    memcpy(res, s + start, maxLen);
    res[maxLen] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string LongestPalindrome(string s) {
        int n = s.Length;
        if (n < 2) return s;

        int start = 0, maxLen = 1;

        for (int i = 0; i < n; i++) {
            int lenOdd = ExpandAroundCenter(s, i, i);
            int lenEven = ExpandAroundCenter(s, i, i + 1);
            int len = lenOdd > lenEven ? lenOdd : lenEven;

            if (len > maxLen) {
                start = i - (len - 1) / 2;
                maxLen = len;
            }
        }

        return s.Substring(start, maxLen);
    }

    private int ExpandAroundCenter(string s, int left, int right) {
        while (left >= 0 && right < s.Length && s[left] == s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    const n = s.length;
    if (n < 2) return s;

    let start = 0, end = 0;

    const expand = (left, right) => {
        while (left >= 0 && right < n && s[left] === s[right]) {
            left--;
            right++;
        }
        // length of palindrome
        return right - left - 1;
    };

    for (let i = 0; i < n; i++) {
        const len1 = expand(i, i);       // odd length
        const len2 = expand(i, i + 1);   // even length
        const len = Math.max(len1, len2);
        if (len > end - start + 1) {
            start = i - Math.floor((len - 1) / 2);
            end = start + len - 1;
        }
    }

    return s.substring(start, end + 1);
};
```

## Typescript

```typescript
function longestPalindrome(s: string): string {
    const n = s.length;
    if (n < 2) return s;

    let bestStart = 0;
    let bestEnd = 0; // inclusive

    const expand = (left: number, right: number): [number, number] => {
        while (left >= 0 && right < n && s[left] === s[right]) {
            left--;
            right++;
        }
        return [left + 1, right - 1];
    };

    for (let i = 0; i < n; i++) {
        const [l1, r1] = expand(i, i);
        if (r1 - l1 > bestEnd - bestStart) {
            bestStart = l1;
            bestEnd = r1;
        }

        const [l2, r2] = expand(i, i + 1);
        if (r2 - l2 > bestEnd - bestStart) {
            bestStart = l2;
            bestEnd = r2;
        }
    }

    return s.substring(bestStart, bestEnd + 1);
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        $n = strlen($s);
        if ($n < 2) {
            return $s;
        }

        $start = 0;
        $maxLen = 1;

        for ($i = 0; $i < $n; $i++) {
            // odd length palindrome
            $l = $i;
            $r = $i;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                $l--;
                $r++;
            }
            $len = $r - $l - 1;
            if ($len > $maxLen) {
                $start = $l + 1;
                $maxLen = $len;
            }

            // even length palindrome
            $l = $i;
            $r = $i + 1;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                $l--;
                $r++;
            }
            $len = $r - $l - 1;
            if ($len > $maxLen) {
                $start = $l + 1;
                $maxLen = $len;
            }
        }

        return substr($s, $start, $maxLen);
    }
}
?>
```

## Swift

```swift
class Solution {
    func longestPalindrome(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return "" }
        var start = 0, end = 0

        func expand(_ left: Int, _ right: Int) -> (Int, Int) {
            var l = left
            var r = right
            while l >= 0 && r < n && chars[l] == chars[r] {
                l -= 1
                r += 1
            }
            return (l + 1, r - 1)
        }

        for i in 0..<n {
            let (oddL, oddR) = expand(i, i)
            if oddR - oddL > end - start {
                start = oddL
                end = oddR
            }
            if i + 1 < n {
                let (evenL, evenR) = expand(i, i + 1)
                if evenR - evenL > end - start {
                    start = evenL
                    end = evenR
                }
            }
        }

        return String(chars[start...end])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindrome(s: String): String {
        val n = s.length
        if (n < 2) return s

        var start = 0
        var end = 0

        fun expand(leftStart: Int, rightStart: Int): Int {
            var left = leftStart
            var right = rightStart
            while (left >= 0 && right < n && s[left] == s[right]) {
                left--
                right++
            }
            return right - left - 1 // length of palindrome
        }

        for (i in 0 until n) {
            val lenOdd = expand(i, i)
            if (lenOdd > end - start + 1) {
                start = i - (lenOdd - 1) / 2
                end = i + lenOdd / 2
            }
            val lenEven = expand(i, i + 1)
            if (lenEven > end - start + 1) {
                start = i - (lenEven - 1) / 2
                end = i + lenEven / 2
            }
        }

        return s.substring(start, end + 1)
    }
}
```

## Dart

```dart
class Solution {
  String longestPalindrome(String s) {
    int n = s.length;
    if (n < 2) return s;

    int start = 0, maxLen = 1;

    void expand(int left, int right) {
      while (left >= 0 && right < n && s[left] == s[right]) {
        left--;
        right++;
      }
      int len = right - left - 1;
      if (len > maxLen) {
        start = left + 1;
        maxLen = len;
      }
    }

    for (int i = 0; i < n; ++i) {
      expand(i, i);       // odd length
      expand(i, i + 1);   // even length
    }

    return s.substring(start, start + maxLen);
  }
}
```

## Golang

```go
func expandAroundCenter(s []byte, left, right int) int {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left--
		right++
	}
	return right - left - 1
}

func longestPalindrome(s string) string {
	n := len(s)
	if n <= 1 {
		return s
	}
	bs := []byte(s)
	start, end := 0, 0
	for i := 0; i < n; i++ {
		len1 := expandAroundCenter(bs, i, i)
		len2 := expandAroundCenter(bs, i, i+1)
		maxLen := len1
		if len2 > maxLen {
			maxLen = len2
		}
		if maxLen > end-start+1 {
			start = i - (maxLen-1)/2
			end = i + maxLen/2
		}
	}
	return s[start : end+1]
}
```

## Ruby

```ruby
def expand_center(s, left, right)
  while left >= 0 && right < s.length && s[left] == s[right]
    left -= 1
    right += 1
  end
  [left + 1, right - 1]
end

# @param {String} s
# @return {String}
def longest_palindrome(s)
  n = s.length
  return "" if n == 0

  start = 0
  max_len = 1
  i = 0
  while i < n
    l, r = expand_center(s, i, i) # odd length
    len = r - l + 1
    if len > max_len
      start = l
      max_len = len
    end

    if i + 1 < n
      l2, r2 = expand_center(s, i, i + 1) # even length
      len2 = r2 - l2 + 1
      if len2 > max_len
        start = l2
        max_len = len2
      end
    end

    i += 1
  end

  s[start, max_len]
end
```

## Scala

```scala
object Solution {
    def longestPalindrome(s: String): String = {
        if (s == null || s.length <= 1) return s
        var start = 0
        var end = 0

        def expand(leftInit: Int, rightInit: Int): Int = {
            var left = leftInit
            var right = rightInit
            while (left >= 0 && right < s.length && s.charAt(left) == s.charAt(right)) {
                left -= 1
                right += 1
            }
            right - left - 1
        }

        for (i <- 0 until s.length) {
            val len1 = expand(i, i)
            val len2 = expand(i, i + 1)
            val len = math.max(len1, len2)
            if (len > end - start + 1) {
                start = i - (len - 1) / 2
                end = i + len / 2
            }
        }

        s.substring(start, end + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return String::new();
        }

        fn expand_center(left: i32, right: i32, b: &[u8]) -> (i32, i32) {
            let mut l = left;
            let mut r = right;
            let len = b.len() as i32;
            while l >= 0 && r < len && b[l as usize] == b[r as usize] {
                l -= 1;
                r += 1;
            }
            (l + 1, r - 1)
        }

        let mut start: usize = 0;
        let mut max_len: usize = 1;

        for i in 0..n {
            // odd length palindrome
            let (l, r) = expand_center(i as i32, i as i32, bytes);
            let cur_len = (r - l + 1) as usize;
            if cur_len > max_len {
                start = l as usize;
                max_len = cur_len;
            }

            // even length palindrome
            if i + 1 < n {
                let (l2, r2) = expand_center(i as i32, i as i32 + 1, bytes);
                let cur_len2 = (r2 - l2 + 1) as usize;
                if cur_len2 > max_len {
                    start = l2 as usize;
                    max_len = cur_len2;
                }
            }
        }

        s[start..start + max_len].to_string()
    }
}
```

## Racket

```racket
(define/contract (longest-palindrome s)
  (-> string? string?)
  (let* ((n (string-length s)))
    (if (<= n 1)
        s
        (let ((best-start 0)
              (maxlen 1))
          (define (expand l r)
            (let loop ((left l) (right r))
              (if (and (>= left 0) (< right n)
                       (char=? (string-ref s left) (string-ref s right)))
                  (loop (- left 1) (+ right 1))
                  (- right left 1))))
          (for ([i (in-range n)])
            ;; odd length palindrome centered at i
            (let ((len (expand i i)))
              (when (> len maxlen)
                (set! maxlen len)
                (set! best-start (- i (quotient len 2)))))
            ;; even length palindrome centered between i and i+1
            (let ((len (expand i (+ i 1))))
              (when (> len maxlen)
                (set! maxlen len)
                (set! best-start (- (+ i 1) (quotient len 2))))))
          (substring s best-start (+ best-start maxlen))))))
```

## Erlang

```erlang
-spec longest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
longest_palindrome(S) when is_binary(S) ->
    case S of
        <<>> -> <<>>;
        _ ->
            List = unicode:characters_to_list(S),
            Tuple = list_to_tuple(List),
            N = tuple_size(Tuple),
            {Start, End} = loop(0, N, Tuple, 0, 0),
            Len = End - Start + 1,
            PalList = lists:sublist(List, Start + 1, Len),
            unicode:characters_to_binary(PalList)
    end.

%% expand from center (L,R) inclusive, returns {NewLeft, NewRight} of the longest palindrome
-spec expand(tuple(), integer(), integer(), integer()) -> {integer(), integer()}.
expand(_Tuple, L, R, N) when L < 0; R >= N ->
    {L + 1, R - 1};
expand(Tuple, L, R, N) ->
    CharL = element(L + 1, Tuple),
    CharR = element(R + 1, Tuple),
    if
        CharL =:= CharR -> expand(Tuple, L - 1, R + 1, N);
        true -> {L + 1, R - 1}
    end.

%% iterate over all centers to find the best palindrome bounds
-spec loop(integer(), integer(), tuple(), integer(), integer()) -> {integer(), integer()}.
loop(I, N, _Tuple, BestStart, BestEnd) when I >= N ->
    {BestStart, BestEnd};
loop(I, N, Tuple, BestStart, BestEnd) ->
    %% odd length palindrome
    {S1, E1} = expand(Tuple, I, I, N),
    Len1 = E1 - S1 + 1,
    CurLen = BestEnd - BestStart + 1,
    {TmpStart, TmpEnd} =
        if Len1 > CurLen -> {S1, E1};
           true -> {BestStart, BestEnd}
        end,
    %% even length palindrome
    {S2, E2} = expand(Tuple, I, I + 1, N),
    Len2 = E2 - S2 + 1,
    NewCurLen = TmpEnd - TmpStart + 1,
    {NewStart, NewEnd} =
        if Len2 > NewCurLen -> {S2, E2};
           true -> {TmpStart, TmpEnd}
        end,
    loop(I + 1, N, Tuple, NewStart, NewEnd).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(s :: String.t()) :: String.t()
  def longest_palindrome(s) do
    n = byte_size(s)

    {best_l, best_r} =
      Enum.reduce(0..(n - 1), {0, 0}, fn i, {bl, br} ->
        # odd length palindrome centered at i,i
        {l1, r1} = expand(s, i, i, n)
        len1 = r1 - l1 + 1
        best_len = br - bl + 1

        {cur_l, cur_r} =
          if len1 > best_len do
            {l1, r1}
          else
            {bl, br}
          end

        # even length palindrome centered at i,i+1
        {l2, r2} = expand(s, i, i + 1, n)
        len2 = r2 - l2 + 1
        best_len2 = cur_r - cur_l + 1

        if len2 > best_len2 do
          {l2, r2}
        else
          {cur_l, cur_r}
        end
      end)

    String.slice(s, best_l, best_r - best_l + 1)
  end

  defp expand(s, left, right, n) do
    cond do
      left < 0 or right >= n ->
        {left + 1, right - 1}

      true ->
        if :binary.at(s, left) == :binary.at(s, right) do
          expand(s, left - 1, right + 1, n)
        else
          {left + 1, right - 1}
        end
    end
  end
end
```
