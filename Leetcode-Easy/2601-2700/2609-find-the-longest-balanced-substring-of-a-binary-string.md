# 2609. Find the Longest Balanced Substring of a Binary String

## Cpp

```cpp
class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        int n = s.size();
        vector<int> runLen;
        vector<char> runChar;
        for (int i = 0; i < n; ) {
            char c = s[i];
            int j = i;
            while (j < n && s[j] == c) ++j;
            runChar.push_back(c);
            runLen.push_back(j - i);
            i = j;
        }
        int ans = 0;
        for (int i = 0; i + 1 < (int)runLen.size(); ++i) {
            if (runChar[i] == '0' && runChar[i+1] == '1') {
                ans = max(ans, 2 * min(runLen[i], runLen[i+1]));
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findTheLongestBalancedSubstring(String s) {
        int n = s.length();
        int maxLen = 0;
        char prevChar = ' ';
        int prevLen = 0;
        int i = 0;
        while (i < n) {
            char curChar = s.charAt(i);
            int j = i;
            while (j < n && s.charAt(j) == curChar) {
                j++;
            }
            int curLen = j - i;
            if (prevChar == '0' && curChar == '1') {
                maxLen = Math.max(maxLen, 2 * Math.min(prevLen, curLen));
            }
            prevChar = curChar;
            prevLen = curLen;
            i = j;
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        left_zeros = [0] * n
        cnt = 0
        for i in range(n):
            if s[i] == '0':
                cnt += 1
            else:
                cnt = 0
            left_zeros[i] = cnt

        right_ones = [0] * n
        cnt = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                cnt += 1
            else:
                cnt = 0
            right_ones[i] = cnt

        ans = 0
        for i in range(n - 1):
            if s[i] == '0' and s[i + 1] == '1':
                ans = max(ans, 2 * min(left_zeros[i], right_ones[i + 1]))
        return ans
```

## Python3

```python
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        prev_char = ''
        prev_len = 0
        ans = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            cur_len = j - i
            cur_char = s[i]
            if prev_char == '0' and cur_char == '1':
                ans = max(ans, 2 * min(prev_len, cur_len))
            prev_char = cur_char
            prev_len = cur_len
            i = j
        return ans
```

## C

```c
#include <string.h>

int findTheLongestBalancedSubstring(char* s) {
    int n = strlen(s);
    int left[55] = {0};
    int right[55] = {0};

    for (int i = 0; i < n; ++i) {
        if (s[i] == '0')
            left[i] = (i > 0 ? left[i - 1] : 0) + 1;
        else
            left[i] = 0;
    }

    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == '1')
            right[i] = (i + 1 < n ? right[i + 1] : 0) + 1;
        else
            right[i] = 0;
    }

    int ans = 0;
    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == '0' && s[i + 1] == '1') {
            int len = left[i] < right[i + 1] ? left[i] : right[i + 1];
            ans = ans > (len * 2) ? ans : (len * 2);
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FindTheLongestBalancedSubstring(string s) {
        int n = s.Length;
        var counts = new System.Collections.Generic.List<int>();
        var chars = new System.Collections.Generic.List<char>();
        int i = 0;
        while (i < n) {
            char c = s[i];
            int j = i;
            while (j < n && s[j] == c) j++;
            counts.Add(j - i);
            chars.Add(c);
            i = j;
        }
        int ans = 0;
        for (int k = 0; k + 1 < counts.Count; k++) {
            if (chars[k] == '0' && chars[k + 1] == '1') {
                int len = System.Math.Min(counts[k], counts[k + 1]) * 2;
                if (len > ans) ans = len;
            }
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
var findTheLongestBalancedSubstring = function(s) {
    const n = s.length;
    if (n === 0) return 0;

    const runs = [];
    const chars = [];

    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        runs.push(j - i);
        chars.push(s[i]);
        i = j;
    }

    let ans = 0;
    for (let k = 0; k < runs.length - 1; k++) {
        if (chars[k] === '0' && chars[k + 1] === '1') {
            ans = Math.max(ans, Math.min(runs[k], runs[k + 1]) * 2);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function findTheLongestBalancedSubstring(s: string): number {
    let n = s.length;
    let i = 0;
    let maxLen = 0;

    while (i < n) {
        // count consecutive zeros
        let zeroCount = 0;
        while (i < n && s[i] === '0') {
            zeroCount++;
            i++;
        }
        // count consecutive ones immediately after the zeros
        let oneCount = 0;
        while (i < n && s[i] === '1') {
            oneCount++;
            i++;
        }
        maxLen = Math.max(maxLen, 2 * Math.min(zeroCount, oneCount));
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
    function findTheLongestBalancedSubstring($s) {
        $n = strlen($s);
        if ($n == 0) return 0;

        $leftZero = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                $leftZero[$i] = ($i > 0 ? $leftZero[$i - 1] : 0) + 1;
            } else {
                $leftZero[$i] = 0;
            }
        }

        $rightOne = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === '1') {
                $rightOne[$i] = ($i + 1 < $n ? $rightOne[$i + 1] : 0) + 1;
            } else {
                $rightOne[$i] = 0;
            }
        }

        $maxLen = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $len = 2 * min($leftZero[$i], $rightOne[$i + 1]);
            if ($len > $maxLen) {
                $maxLen = $len;
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func findTheLongestBalancedSubstring(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return 0 }
        
        var leftZero = [Int](repeating: 0, count: n)
        for i in 0..<n {
            if chars[i] == "0" {
                leftZero[i] = (i > 0 ? leftZero[i - 1] : 0) + 1
            }
        }
        
        var rightOne = [Int](repeating: 0, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == "1" {
                rightOne[i] = (i + 1 < n ? rightOne[i + 1] : 0) + 1
            }
        }
        
        var ans = 0
        for i in 1..<n { // split between i-1 and i
            let k = min(leftZero[i - 1], rightOne[i])
            ans = max(ans, 2 * k)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findTheLongestBalancedSubstring(s: String): Int {
        val n = s.length
        if (n == 0) return 0
        val leftZero = IntArray(n)
        for (i in 0 until n) {
            leftZero[i] = if (s[i] == '0') {
                if (i > 0) leftZero[i - 1] + 1 else 1
            } else {
                0
            }
        }
        val rightOne = IntArray(n)
        for (i in n - 1 downTo 0) {
            rightOne[i] = if (s[i] == '1') {
                if (i + 1 < n) rightOne[i + 1] + 1 else 1
            } else {
                0
            }
        }
        var ans = 0
        for (i in 0 until n - 1) {
            if (s[i] == '0' && s[i + 1] == '1') {
                val len = kotlin.math.min(leftZero[i], rightOne[i + 1]) * 2
                if (len > ans) ans = len
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int findTheLongestBalancedSubstring(String s) {
    int n = s.length;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int zero = 0, one = 0;
      int j = i;
      while (j < n && s[j] == '0') {
        zero++;
        j++;
      }
      while (j < n && s[j] == '1') {
        one++;
        j++;
      }
      ans = max(ans, 2 * min(zero, one));
    }
    return ans;
  }
}
```

## Golang

```go
func findTheLongestBalancedSubstring(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	type run struct {
		ch byte
		len int
	}
	var runs []run
	for i := 0; i < n; {
		j := i
		for j < n && s[j] == s[i] {
			j++
		}
		runs = append(runs, run{ch: s[i], len: j - i})
		i = j
	}
	maxLen := 0
	for i := 0; i+1 < len(runs); i++ {
		if runs[i].ch == '0' && runs[i+1].ch == '1' {
			if candidate := 2 * min(runs[i].len, runs[i+1].len); candidate > maxLen {
				maxLen = candidate
			}
		}
	}
	return maxLen
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def find_the_longest_balanced_substring(s)
  n = s.length
  ans = 0
  (0...n).each do |i|
    zeros = 0
    ones = 0
    seen_one = false
    (i...n).each do |j|
      if s[j] == '0'
        break if seen_one
        zeros += 1
      else
        seen_one = true
        ones += 1
      end
      ans = [ans, zeros * 2].max if zeros == ones
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findTheLongestBalancedSubstring(s: String): Int = {
        var maxLen = 0
        var i = 0
        val n = s.length
        var prevChar: Char = ' '
        var prevRunLen = 0

        while (i < n) {
            val currChar = s.charAt(i)
            var j = i
            while (j < n && s.charAt(j) == currChar) {
                j += 1
            }
            val currRunLen = j - i

            if (prevChar == '0' && currChar == '1') {
                val balancedLen = 2 * Math.min(prevRunLen, currRunLen)
                if (balancedLen > maxLen) maxLen = balancedLen
            }

            prevChar = currChar
            prevRunLen = currRunLen
            i = j
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_the_longest_balanced_substring(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans = 0usize;
        for len in (2..=n).step_by(2) {
            for start in 0..=n - len {
                let mid = start + len / 2;
                if bytes[start..mid].iter().all(|&c| c == b'0')
                    && bytes[mid..start + len].iter().all(|&c| c == b'1')
                {
                    ans = ans.max(len);
                }
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (find-the-longest-balanced-substring s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (maxlen (box 0)))
    (for ([i (in-range n)])
      (for ([len (in-range 2 (+ (- n i) 1) 2)]) ; even lengths only
        (define half (/ len 2))
        (define ok #t)
        ;; first half must be all '0'
        (for ([j (in-range half)]
              #:break (not ok))
          (when (not (char=? (string-ref s (+ i j)) #\0))
            (set! ok #f)))
        ;; second half must be all '1'
        (when ok
          (for ([j (in-range half)]
                #:break (not ok))
            (when (not (char=? (string-ref s (+ i half j)) #\1))
              (set! ok #f))))
        (when ok
          (when (> len (unbox maxlen))
            (set-box! maxlen len)))))
    (unbox maxlen)))
```

## Erlang

```erlang
-spec find_the_longest_balanced_substring(S :: unicode:unicode_binary()) -> integer().
find_the_longest_balanced_substring(S) ->
    Str = binary_to_list(S),
    N = length(Str),
    longest(N, Str).

longest(Len, _Str) when Len < 2 -> 0;
longest(Len, Str) ->
    case Len rem 2 of
        1 -> longest(Len-1, Str);
        0 ->
            if has_balanced(Len, Str) -> Len;
               true -> longest(Len-1, Str)
            end
    end.

has_balanced(Len, Str) ->
    MaxStart = length(Str) - Len + 1,
    lists:any(fun(Start) -> is_balanced_at(Start, Len, Str) end,
              lists:seq(1, MaxStart)).

is_balanced_at(Start, Len, Str) ->
    Sub = lists:sublist(Str, Start, Len),
    Half = Len div 2,
    First = lists:sublist(Sub, 1, Half),
    Second = lists:nthtail(Half, Sub),
    all_zero(First) andalso all_one(Second).

all_zero([]) -> true;
all_zero([H|T]) when H =:= $0 -> all_zero(T);
all_zero(_) -> false.

all_one([]) -> true;
all_one([H|T]) when H =:= $1 -> all_one(T);
all_one(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_longest_balanced_substring(s :: String.t()) :: integer()
  def find_the_longest_balanced_substring(s) do
    chars = String.graphemes(s)
    len = length(chars)

    0..(len - 1)
    |> Enum.reduce(0, fn i, acc ->
      if Enum.at(chars, i) == "0" do
        {zero_cnt, idx_after_zeros} = count_while(chars, i, "0")
        {one_cnt, _} = count_while(chars, idx_after_zeros, "1")
        cur = 2 * min(zero_cnt, one_cnt)
        max(acc, cur)
      else
        acc
      end
    end)
  end

  defp count_while(chars, idx, target) do
    len = length(chars)

    if idx < len and Enum.at(chars, idx) == target do
      {cnt_rest, next_idx} = count_while(chars, idx + 1, target)
      {cnt_rest + 1, next_idx}
    else
      {0, idx}
    end
  end
end
```
