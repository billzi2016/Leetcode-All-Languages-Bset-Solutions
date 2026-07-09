# 1208. Get Equal Substrings Within Budget

## Cpp

```cpp
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int n = s.size();
        int start = 0, curr = 0, ans = 0;
        for (int i = 0; i < n; ++i) {
            curr += abs(s[i] - t[i]);
            while (curr > maxCost) {
                curr -= abs(s[start] - t[start]);
                ++start;
            }
            ans = max(ans, i - start + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int n = s.length();
        int start = 0;
        int currCost = 0;
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            currCost += Math.abs(s.charAt(i) - t.charAt(i));
            while (currCost > maxCost) {
                currCost -= Math.abs(s.charAt(start) - t.charAt(start));
                start++;
            }
            int len = i - start + 1;
            if (len > maxLen) {
                maxLen = len;
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        start = 0
        curr_cost = 0
        max_len = 0
        for i in range(len(s)):
            curr_cost += abs(ord(s[i]) - ord(t[i]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, i - start + 1)
        return max_len
```

## Python3

```python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        curr_cost = 0
        max_len = 0
        for i in range(len(s)):
            curr_cost += abs(ord(s[i]) - ord(t[i]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, i - start + 1)
        return max_len
```

## C

```c
#include <stdlib.h>
#include <string.h>

int equalSubstring(char* s, char* t, int maxCost) {
    int n = (int)strlen(s);
    int start = 0;
    int maxLen = 0;
    int currCost = 0;

    for (int i = 0; i < n; ++i) {
        currCost += abs(s[i] - t[i]);
        while (currCost > maxCost) {
            currCost -= abs(s[start] - t[start]);
            ++start;
        }
        int len = i - start + 1;
        if (len > maxLen) maxLen = len;
    }

    return maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int EqualSubstring(string s, string t, int maxCost)
    {
        int n = s.Length;
        int start = 0;
        int currCost = 0;
        int maxLen = 0;

        for (int i = 0; i < n; i++)
        {
            currCost += Math.Abs(s[i] - t[i]);

            while (currCost > maxCost)
            {
                currCost -= Math.Abs(s[start] - t[start]);
                start++;
            }

            int windowLen = i - start + 1;
            if (windowLen > maxLen) maxLen = windowLen;
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function(s, t, maxCost) {
    let start = 0;
    let currCost = 0;
    let maxLen = 0;
    const n = s.length;
    for (let i = 0; i < n; i++) {
        currCost += Math.abs(s.charCodeAt(i) - t.charCodeAt(i));
        while (currCost > maxCost) {
            currCost -= Math.abs(s.charCodeAt(start) - t.charCodeAt(start));
            start++;
        }
        const len = i - start + 1;
        if (len > maxLen) maxLen = len;
    }
    return maxLen;
};
```

## Typescript

```typescript
function equalSubstring(s: string, t: string, maxCost: number): number {
    let start = 0;
    let currCost = 0;
    let maxLen = 0;
    const n = s.length;
    for (let i = 0; i < n; i++) {
        currCost += Math.abs(s.charCodeAt(i) - t.charCodeAt(i));
        while (currCost > maxCost) {
            currCost -= Math.abs(s.charCodeAt(start) - t.charCodeAt(start));
            start++;
        }
        const len = i - start + 1;
        if (len > maxLen) maxLen = len;
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer $maxCost
     * @return Integer
     */
    function equalSubstring($s, $t, $maxCost) {
        $n = strlen($s);
        $start = 0;
        $currCost = 0;
        $maxLen = 0;

        for ($i = 0; $i < $n; $i++) {
            $cost = abs(ord($s[$i]) - ord($t[$i]));
            $currCost += $cost;

            while ($currCost > $maxCost) {
                $removeCost = abs(ord($s[$start]) - ord($t[$start]));
                $currCost -= $removeCost;
                $start++;
            }

            $len = $i - $start + 1;
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
    func equalSubstring(_ s: String, _ t: String, _ maxCost: Int) -> Int {
        let sBytes = Array(s.utf8)
        let tBytes = Array(t.utf8)
        var start = 0
        var currentCost = 0
        var maxLen = 0
        
        for i in 0..<sBytes.count {
            currentCost += abs(Int(sBytes[i]) - Int(tBytes[i]))
            while currentCost > maxCost && start <= i {
                currentCost -= abs(Int(sBytes[start]) - Int(tBytes[start]))
                start += 1
            }
            let length = i - start + 1
            if length > maxLen {
                maxLen = length
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun equalSubstring(s: String, t: String, maxCost: Int): Int {
        var start = 0
        var currentCost = 0
        var maxLength = 0
        val n = s.length
        for (i in 0 until n) {
            currentCost += kotlin.math.abs(s[i].code - t[i].code)
            while (currentCost > maxCost) {
                currentCost -= kotlin.math.abs(s[start].code - t[start].code)
                start++
            }
            val length = i - start + 1
            if (length > maxLength) maxLength = length
        }
        return maxLength
    }
}
```

## Dart

```dart
class Solution {
  int equalSubstring(String s, String t, int maxCost) {
    int n = s.length;
    int start = 0;
    int currCost = 0;
    int maxLen = 0;

    for (int i = 0; i < n; i++) {
      int diff = (s.codeUnitAt(i) - t.codeUnitAt(i)).abs();
      currCost += diff;

      while (currCost > maxCost && start <= i) {
        int leftDiff = (s.codeUnitAt(start) - t.codeUnitAt(start)).abs();
        currCost -= leftDiff;
        start++;
      }

      int windowLen = i - start + 1;
      if (windowLen > maxLen) {
        maxLen = windowLen;
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func equalSubstring(s string, t string, maxCost int) int {
	n := len(s)
	start, currCost, maxLen := 0, 0, 0
	for i := 0; i < n; i++ {
		diff := int(s[i]) - int(t[i])
		if diff < 0 {
			diff = -diff
		}
		currCost += diff
		for currCost > maxCost {
			leftDiff := int(s[start]) - int(t[start])
			if leftDiff < 0 {
				leftDiff = -leftDiff
			}
			currCost -= leftDiff
			start++
		}
		if length := i - start + 1; length > maxLen {
			maxLen = length
		}
	}
	return maxLen
}
```

## Ruby

```ruby
def equal_substring(s, t, max_cost)
  left = 0
  curr = 0
  max_len = 0
  n = s.length
  (0...n).each do |right|
    curr += (s.getbyte(right) - t.getbyte(right)).abs
    while curr > max_cost
      curr -= (s.getbyte(left) - t.getbyte(left)).abs
      left += 1
    end
    len = right - left + 1
    max_len = len if len > max_len
  end
  max_len
end
```

## Scala

```scala
object Solution {
  def equalSubstring(s: String, t: String, maxCost: Int): Int = {
    var start = 0
    var currCost = 0L
    var maxLen = 0
    val n = s.length
    for (i <- 0 until n) {
      currCost += Math.abs(s.charAt(i) - t.charAt(i))
      while (currCost > maxCost && start <= i) {
        currCost -= Math.abs(s.charAt(start) - t.charAt(start))
        start += 1
      }
      val len = i - start + 1
      if (len > maxLen) maxLen = len
    }
    maxLen
  }
}
```

## Rust

```rust
impl Solution {
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let n = s_bytes.len();
        let mut start = 0usize;
        let mut cur_cost: i32 = 0;
        let mut max_len = 0usize;

        for end in 0..n {
            let diff = (s_bytes[end] as i32 - t_bytes[end] as i32).abs();
            cur_cost += diff;

            while cur_cost > max_cost && start <= end {
                let left_diff = (s_bytes[start] as i32 - t_bytes[start] as i32).abs();
                cur_cost -= left_diff;
                start += 1;
            }

            let len = end - start + 1;
            if len > max_len {
                max_len = len;
            }
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (equal-substring s t maxCost)
  (-> string? string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (start 0)
         (curr-cost 0)
         (max-len 0))
    (for ([i (in-range n)])
      (let* ((cost (abs (- (char->integer (string-ref s i))
                           (char->integer (string-ref t i))))))
        (set! curr-cost (+ curr-cost cost))
        ;; shrink window while over budget
        (let loop ()
          (when (and (> curr-cost maxCost) (<= start i))
            (let ((remove-cost (abs (- (char->integer (string-ref s start))
                                       (char->integer (string-ref t start))))))
              (set! curr-cost (- curr-cost remove-cost))
              (set! start (+ start 1)))
            (loop)))
        (when (> (+ (- i start) 1) max-len)
          (set! max-len (+ (- i start) 1)))))
    max-len))
```

## Erlang

```erlang
-module(solution).
-export([equal_substring/3]).

-spec equal_substring(unicode:unicode_binary(), unicode:unicode_binary(), integer()) -> integer().
equal_substring(S, T, MaxCost) ->
    N = byte_size(S),
    loop(0, 0, 0, 0, S, T, MaxCost, N).

loop(I, Start, CurrCost, MaxLen, _S, _T, _MaxCost, N) when I == N ->
    MaxLen;
loop(I, Start, CurrCost, MaxLen, S, T, MaxCost, N) ->
    Cost = abs(binary:at(S, I) - binary:at(T, I)),
    NewCurr0 = CurrCost + Cost,
    {NewStart, NewCurr} = shrink(S, T, MaxCost, Start, NewCurr0),
    Len = I - NewStart + 1,
    NewMax = if Len > MaxLen -> Len; true -> MaxLen end,
    loop(I + 1, NewStart, NewCurr, NewMax, S, T, MaxCost, N).

shrink(_S, _T, MaxCost, Start, Curr) when Curr =< MaxCost ->
    {Start, Curr};
shrink(S, T, MaxCost, Start, Curr) ->
    Diff = abs(binary:at(S, Start) - binary:at(T, Start)),
    shrink(S, T, MaxCost, Start + 1, Curr - Diff).
```

## Elixir

```elixir
defmodule Solution do
  @spec equal_substring(s :: String.t(), t :: String.t(), max_cost :: integer) :: integer
  def equal_substring(s, t, max_cost) do
    s_bytes = :binary.bin_to_list(s)
    t_bytes = :binary.bin_to_list(t)

    costs =
      Enum.zip(s_bytes, t_bytes)
      |> Enum.map(fn {a, b} -> abs(a - b) end)

    costs_tuple = List.to_tuple(costs)
    n = tuple_size(costs_tuple)

    {max_len, _start, _curr} =
      0..(n - 1)
      |> Enum.reduce({0, 0, 0}, fn i, {cur_max, start, curr_sum} ->
        new_curr = curr_sum + elem(costs_tuple, i)

        {new_start, final_curr} = shrink(start, new_curr, max_cost, costs_tuple)

        window_len = i - new_start + 1
        new_max = if window_len > cur_max, do: window_len, else: cur_max

        {new_max, new_start, final_curr}
      end)

    max_len
  end

  defp shrink(start, curr, max_cost, costs_tuple) do
    if curr <= max_cost do
      {start, curr}
    else
      shrink(start + 1, curr - elem(costs_tuple, start), max_cost, costs_tuple)
    end
  end
end
```
