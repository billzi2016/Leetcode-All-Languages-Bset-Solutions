# 2730. Find the Longest Semi-Repetitive Substring

## Cpp

```cpp
class Solution {
public:
    int longestSemiRepetitiveSubstring(string s) {
        int n = s.size();
        int left = 0, cnt = 0, ans = 0;
        for (int right = 0; right < n; ++right) {
            if (right > 0 && s[right] == s[right - 1]) ++cnt;
            while (cnt > 1) {
                if (left + 1 <= right && s[left] == s[left + 1]) --cnt;
                ++left;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestSemiRepetitiveSubstring(String s) {
        int n = s.length();
        int left = 0;
        int pairCount = 0;
        int maxLen = 1; // at least one character
        
        for (int right = 0; right < n; right++) {
            if (right > 0 && s.charAt(right) == s.charAt(right - 1)) {
                pairCount++;
            }
            while (pairCount > 1) {
                // If the left side is part of an equal adjacent pair, removing it reduces count
                if (left + 1 <= right && s.charAt(left) == s.charAt(left + 1)) {
                    pairCount--;
                }
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = 0
        cnt = 0  # number of adjacent equal pairs in current window
        ans = 0
        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                cnt += 1
            while cnt > 1:
                if left + 1 <= right and s[left] == s[left + 1]:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## Python3

```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        left = 0
        cnt = 0
        ans = 1
        for right in range(1, n):
            if s[right] == s[right - 1]:
                cnt += 1
            while cnt > 1:
                if left + 1 <= right and s[left] == s[left + 1]:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## C

```c
#include <string.h>

int longestSemiRepetitiveSubstring(char* s) {
    int n = strlen(s);
    int ans = 1; // at least one character
    
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        for (int j = i + 1; j < n; ++j) {
            if (s[j] == s[j - 1]) ++cnt;
            if (cnt > 1) break;
            int len = j - i + 1;
            if (len > ans) ans = len;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestSemiRepetitiveSubstring(string s) {
        int n = s.Length;
        int left = 0, cnt = 0, ans = 0;
        for (int right = 0; right < n; ++right) {
            if (right > 0 && s[right] == s[right - 1]) cnt++;
            while (cnt > 1) {
                if (left + 1 <= right && s[left] == s[left + 1]) cnt--;
                left++;
            }
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestSemiRepetitiveSubstring = function(s) {
    const n = s.length;
    if (n === 0) return 0;
    let left = 0, dupCount = 0, maxLen = 1;
    for (let right = 1; right < n; ++right) {
        if (s[right] === s[right - 1]) dupCount++;
        while (dupCount > 1) {
            if (left + 1 <= right && s[left] === s[left + 1]) dupCount--;
            left++;
        }
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
};
```

## Typescript

```typescript
function longestSemiRepetitiveSubstring(s: string): number {
    const n = s.length;
    let left = 0;
    let pairCount = 0;
    let maxLen = 0;

    for (let right = 0; right < n; right++) {
        if (right > 0 && s[right] === s[right - 1]) {
            pairCount++;
        }

        while (pairCount > 1) {
            // If the pair being removed starts at left
            if (left + 1 <= right && s[left] === s[left + 1]) {
                pairCount--;
            }
            left++;
        }

        const curLen = right - left + 1;
        if (curLen > maxLen) maxLen = curLen;
    }

    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestSemiRepetitiveSubstring($s) {
        $n = strlen($s);
        $left = 0;
        $cnt = 0; // number of adjacent equal pairs in current window
        $ans = 0;

        for ($right = 0; $right < $n; $right++) {
            if ($right > 0 && $s[$right] === $s[$right - 1]) {
                $cnt++;
            }

            while ($cnt > 1) {
                // The pair formed by positions left and left+1 will leave the window
                if ($left + 1 <= $right && $s[$left] === $s[$left + 1]) {
                    $cnt--;
                }
                $left++;
            }

            $ans = max($ans, $right - $left + 1);
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestSemiRepetitiveSubstring(_ s: String) -> Int {
        let chars = Array(s)
        var left = 0
        var repeatCount = 0
        var maxLen = 0
        
        for right in 0..<chars.count {
            if right > 0 && chars[right] == chars[right - 1] {
                repeatCount += 1
            }
            
            while repeatCount > 1 {
                if left + 1 <= right && chars[left] == chars[left + 1] {
                    repeatCount -= 1
                }
                left += 1
            }
            
            maxLen = max(maxLen, right - left + 1)
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSemiRepetitiveSubstring(s: String): Int {
        var left = 0
        var cnt = 0
        var ans = 0
        val n = s.length
        for (right in 0 until n) {
            if (right > 0 && s[right] == s[right - 1]) cnt++
            while (cnt > 1) {
                if (left + 1 <= right && s[left] == s[left + 1]) cnt--
                left++
            }
            ans = kotlin.math.max(ans, right - left + 1)
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestSemiRepetitiveSubstring(String s) {
    int n = s.length;
    if (n == 0) return 0;
    int left = 0;
    int cnt = 0; // number of adjacent equal pairs in current window
    int ans = 1;

    for (int right = 1; right < n; ++right) {
      if (s[right] == s[right - 1]) cnt++;

      while (cnt > 1 && left < right) {
        if (left + 1 <= right && s[left] == s[left + 1]) cnt--;
        left++;
      }

      ans = max(ans, right - left + 1);
    }
    return ans;
  }
}
```

## Golang

```go
func longestSemiRepetitiveSubstring(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	left, cnt, ans := 0, 0, 0
	for right := 0; right < n; right++ {
		if right > 0 && s[right] == s[right-1] {
			cnt++
		}
		for cnt > 1 {
			if left+1 <= right && s[left] == s[left+1] {
				cnt--
			}
			left++
		}
		if cur := right - left + 1; cur > ans {
			ans = cur
		}
	}
	return ans
}
```

## Ruby

```ruby
def longest_semi_repetitive_substring(s)
  n = s.length
  return 0 if n == 0
  left = 0
  dup_cnt = 0
  max_len = 1

  (1...n).each do |right|
    dup_cnt += 1 if s[right] == s[right - 1]

    while dup_cnt > 1
      dup_cnt -= 1 if left + 1 <= right && s[left] == s[left + 1]
      left += 1
    end

    max_len = [max_len, right - left + 1].max
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def longestSemiRepetitiveSubstring(s: String): Int = {
        val n = s.length
        var left = 0
        var cnt = 0
        var ans = if (n > 0) 1 else 0
        for (right <- 1 until n) {
            if (s.charAt(right) == s.charAt(right - 1)) cnt += 1
            while (cnt > 1) {
                if (left + 1 < n && s.charAt(left) == s.charAt(left + 1)) cnt -= 1
                left += 1
            }
            ans = math.max(ans, right - left + 1)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_semi_repetitive_substring(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let mut left = 0usize;
        let mut cnt = 0i32; // number of adjacent equal pairs in current window
        let mut ans = 1i32;

        for right in 0..n {
            if right > 0 && bytes[right] == bytes[right - 1] {
                cnt += 1;
            }
            while cnt > 1 {
                if left + 1 <= right && bytes[left] == bytes[left + 1] {
                    cnt -= 1;
                }
                left += 1;
            }
            let len = (right - left + 1) as i32;
            if len > ans {
                ans = len;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (longest-semi-repetitive-substring s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (maxlen 0))
    (for ([i (in-range n)])
      (let loop ((j i) (cnt 0))
        (when (< j n)
          (define new-cnt
            (if (and (> j i)
                     (char=? (string-ref s j) (string-ref s (- j 1))))
                (+ cnt 1)
                cnt))
          (when (<= new-cnt 1)
            (set! maxlen (max maxlen (+ 1 (- j i)))))
          (if (<= new-cnt 1)
              (loop (+ j 1) new-cnt)
              (void)))))
    maxlen))
```

## Erlang

```erlang
-spec longest_semi_repetitive_substring(S :: unicode:unicode_binary()) -> integer().
longest_semi_repetitive_substring(S) ->
    Str = binary:bin_to_list(S),
    N = length(Str),
    loop_start(0, N, Str, 0).

loop_start(I, N, _Str, Max) when I >= N ->
    Max;
loop_start(I, N, Str, Max) ->
    NewMax = loop_end(I, I, N, Str, Max),
    loop_start(I + 1, N, Str, NewMax).

loop_end(_Start, End, N, _Str, Max) when End >= N ->
    Max;
loop_end(Start, End, N, Str, Max) ->
    SubLen = End - Start + 1,
    Sub = lists:sublist(Str, Start + 1, SubLen),
    Count = count_adjacent(Sub),
    NewMax = case Count =< 1 of
        true when SubLen > Max -> SubLen;
        _ -> Max
    end,
    loop_end(Start, End + 1, N, Str, NewMax).

count_adjacent([]) -> 0;
count_adjacent([_]) -> 0;
count_adjacent([A, B | Rest]) ->
    (if A =:= B -> 1; true -> 0 end) + count_adjacent([B | Rest]).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_semi_repetitive_substring(s :: String.t()) :: integer()
  def longest_semi_repetitive_substring(s) do
    chars = String.graphemes(s)
    n = length(chars)

    {_left, _cnt, ans} =
      Enum.reduce(0..(n - 1), {0, 0, 0}, fn right, {left, cnt, best} ->
        cnt =
          if right > 0 and Enum.at(chars, right) == Enum.at(chars, right - 1) do
            cnt + 1
          else
            cnt
          end

        {left, cnt} = shrink(left, right, chars, cnt)
        best = max(best, right - left + 1)
        {left, cnt, best}
      end)

    ans
  end

  defp shrink(left, right, chars, cnt) do
    if cnt <= 1 do
      {left, cnt}
    else
      cnt =
        if left + 1 <= right and Enum.at(chars, left) == Enum.at(chars, left + 1) do
          cnt - 1
        else
          cnt
        end

      shrink(left + 1, right, chars, cnt)
    end
  end
end
```
