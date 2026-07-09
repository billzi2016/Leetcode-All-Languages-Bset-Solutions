# 0821. Shortest Distance to a Character

## Cpp

```cpp
class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        int n = s.size();
        vector<int> ans(n, INT_MAX);
        const int INF = 1e9;
        int prev = -INF;
        for (int i = 0; i < n; ++i) {
            if (s[i] == c) prev = i;
            ans[i] = i - prev;
        }
        prev = INF;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == c) prev = i;
            ans[i] = min(ans[i], prev - i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] shortestToChar(String s, char c) {
        int n = s.length();
        int[] ans = new int[n];
        int prev = Integer.MIN_VALUE / 2;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == c) {
                prev = i;
            }
            ans[i] = i - prev;
        }
        prev = Integer.MAX_VALUE / 2;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == c) {
                prev = i;
            }
            ans[i] = Math.min(ans[i], prev - i);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [0] * n
        prev = -10**6  # sufficiently small sentinel
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
        prev = 10**6   # sufficiently large sentinel
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
        next_pos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_pos = i
            ans[i] = min(ans[i], next_pos - i)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestToChar(char* s, char c, int* returnSize) {
    int n = (int)strlen(s);
    int *ans = (int *)malloc(n * sizeof(int));
    if (!ans) {
        *returnSize = 0;
        return NULL;
    }
    *returnSize = n;

    const int INF = INT_MAX / 2; // avoid overflow when adding
    int prev = -INF;
    for (int i = 0; i < n; ++i) {
        if (s[i] == c) prev = i;
        ans[i] = (prev == -INF) ? INF : i - prev;
    }

    int next = INF * 2; // still large positive
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == c) next = i;
        int dist = (next == INF * 2) ? INF : next - i;
        if (dist < ans[i]) ans[i] = dist;
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] ShortestToChar(string s, char c)
    {
        int n = s.Length;
        int[] ans = new int[n];
        int prev = -n * 2; // sentinel far left

        for (int i = 0; i < n; i++)
        {
            if (s[i] == c) prev = i;
            ans[i] = i - prev;
        }

        prev = n * 2; // sentinel far right
        for (int i = n - 1; i >= 0; i--)
        {
            if (s[i] == c) prev = i;
            int dist = prev - i;
            if (dist < ans[i]) ans[i] = dist;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    const n = s.length;
    const ans = new Array(n);
    let prev = -Infinity;
    
    // Left to right pass
    for (let i = 0; i < n; i++) {
        if (s[i] === c) prev = i;
        ans[i] = i - prev;
    }
    
    // Right to left pass
    let next = Infinity;
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === c) next = i;
        const dist = next - i;
        if (dist < ans[i]) ans[i] = dist;
    }
    
    return ans;
};
```

## Typescript

```typescript
function shortestToChar(s: string, c: string): number[] {
    const n = s.length;
    const res = new Array<number>(n);
    let prev = -Infinity;

    // Left to right pass
    for (let i = 0; i < n; i++) {
        if (s[i] === c) prev = i;
        res[i] = i - prev;
    }

    // Right to left pass
    let next = Infinity;
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === c) next = i;
        const dist = next - i;
        if (dist < res[i]) res[i] = dist;
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $c
     * @return Integer[]
     */
    function shortestToChar($s, $c) {
        $n = strlen($s);
        $ans = array_fill(0, $n, PHP_INT_MAX);

        // Left to right pass
        $prev = -PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === $c) {
                $prev = $i;
            }
            if ($prev != -PHP_INT_MAX) {
                $ans[$i] = $i - $prev;
            }
        }

        // Right to left pass
        $prev = PHP_INT_MAX;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === $c) {
                $prev = $i;
            }
            if ($prev != PHP_INT_MAX) {
                $dist = $prev - $i;
                if ($dist < $ans[$i]) {
                    $ans[$i] = $dist;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func shortestToChar(_ s: String, _ c: Character) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var answer = Array(repeating: n, count: n)
        
        var dist = n
        for i in 0..<n {
            if chars[i] == c {
                dist = 0
            } else {
                dist += 1
            }
            answer[i] = dist
        }
        
        dist = n
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == c {
                dist = 0
            } else {
                dist += 1
            }
            answer[i] = min(answer[i], dist)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestToChar(s: String, c: Char): IntArray {
        val n = s.length
        val res = IntArray(n)
        var prev = -1_000_000
        for (i in 0 until n) {
            if (s[i] == c) prev = i
            res[i] = i - prev
        }
        var next = 1_000_000
        for (i in n - 1 downTo 0) {
            if (s[i] == c) next = i
            val dist = next - i
            if (dist < res[i]) res[i] = dist
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> shortestToChar(String s, String c) {
    int n = s.length;
    List<int> ans = List.filled(n, 0);
    int prev = -1000000; // sufficiently small
    for (int i = 0; i < n; i++) {
      if (s[i] == c) {
        prev = i;
      }
      ans[i] = i - prev;
    }
    int next = 1000000; // sufficiently large
    for (int i = n - 1; i >= 0; i--) {
      if (s[i] == c) {
        next = i;
      }
      int dist = next - i;
      if (dist < ans[i]) {
        ans[i] = dist;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func shortestToChar(s string, c byte) []int {
	n := len(s)
	ans := make([]int, n)

	const inf = int(^uint(0) >> 1) // MaxInt
	prev := -inf
	for i := 0; i < n; i++ {
		if s[i] == c {
			prev = i
		}
		ans[i] = i - prev
	}

	next := inf * 2
	for i := n - 1; i >= 0; i-- {
		if s[i] == c {
			next = i
		}
		if d := next - i; d < ans[i] {
			ans[i] = d
		}
	}
	return ans
}
```

## Ruby

```ruby
def shortest_to_char(s, c)
  n = s.length
  ans = Array.new(n, n + 1)

  prev = nil
  s.each_char.with_index do |ch, i|
    if ch == c
      prev = i
      ans[i] = 0
    else
      ans[i] = prev ? i - prev : n + 1
    end
  end

  next_pos = nil
  (n - 1).downto(0) do |i|
    if s.getbyte(i) == c.ord
      next_pos = i
      ans[i] = 0
    else
      if next_pos
        dist = next_pos - i
        ans[i] = [ans[i], dist].min
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def shortestToChar(s: String, c: Char): Array[Int] = {
        val n = s.length
        val ans = new Array[Int](n)
        var prev = -2 * n
        for (i <- 0 until n) {
            if (s(i) == c) prev = i
            ans(i) = i - prev
        }
        var next = 2 * n
        for (i <- (n - 1) to 0 by -1) {
            if (s(i) == c) next = i
            val dist = next - i
            if (dist < ans(i)) ans(i) = dist
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_to_char(s: String, c: char) -> Vec<i32> {
        let n = s.len();
        let mut ans = vec![i32::MAX; n];
        let mut prev = -1_000_000_i32;
        for (i, ch) in s.chars().enumerate() {
            if ch == c {
                prev = i as i32;
            }
            ans[i] = (i as i32 - prev).abs();
        }
        let mut next = 1_000_000_i32;
        for (rev_i, ch) in s.chars().rev().enumerate() {
            let i = n - 1 - rev_i;
            if ch == c {
                next = i as i32;
            }
            let dist = (next - i as i32).abs();
            if dist < ans[i] {
                ans[i] = dist;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (shortest-to-char s c)
  (-> string? char? (listof exact-integer?))
  (let* ((n (string-length s))
         (vec (make-vector n (+ n 1)))) ; initialize with a large value
    ;; left‑to‑right pass: distance to the nearest previous `c`
    (let ((prev -1000000))
      (for ([i (in-range n)])
        (if (char=? (string-ref s i) c)
            (begin
              (vector-set! vec i 0)
              (set! prev i))
            (when (>= prev 0)
              (vector-set! vec i (- i prev))))))
    ;; right‑to‑left pass: combine with distance to the nearest next `c`
    (let ((next (* 2 n))) ; a sentinel larger than any possible distance
      (for ([i (in-range (sub1 n) -1 -1)])
        (if (char=? (string-ref s i) c)
            (set! next i)
            (let ((dist (- next i)))
              (vector-set! vec i (min (vector-ref vec i) dist))))))
    (vector->list vec)))
```

## Erlang

```erlang
-spec shortest_to_char(S :: unicode:unicode_binary(), C :: char()) -> [integer()].
shortest_to_char(S, C) ->
    List = unicode:characters_to_list(S),
    Len = length(List),
    MaxDist = Len + 1,
    CharCode = to_int(C),
    Left = left_pass(List, CharCode, 0, -1, [], MaxDist),
    Right = right_pass(lists:reverse(List), CharCode, 0, -1, [], MaxDist),
    lists:zipwith(fun(L, R) -> if L < R -> L; true -> R end end, Left, Right).

to_int(C) when is_integer(C) -> C;
to_int(C) when is_binary(C) ->
    case unicode:characters_to_list(C) of
        [Code] -> Code;
        _ -> erlang:error(badarg)
    end.

left_pass([], _C, _Idx, _Prev, Acc, _Max) ->
    lists:reverse(Acc);
left_pass([H|T], C, Idx, Prev, Acc, Max) ->
    NewPrev = if H =:= C -> Idx; true -> Prev end,
    Dist = case NewPrev of
        -1 -> Max;
        _ -> Idx - NewPrev
    end,
    left_pass(T, C, Idx + 1, NewPrev, [Dist | Acc], Max).

right_pass([], _C, _Idx, _Next, Acc, _Max) ->
    lists:reverse(Acc);
right_pass([H|T], C, Idx, Next, Acc, Max) ->
    NewNext = if H =:= C -> Idx; true -> Next end,
    Dist = case NewNext of
        -1 -> Max;
        _ -> NewNext - Idx
    end,
    right_pass(T, C, Idx + 1, NewNext, [Dist | Acc], Max).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_to_char(s :: String.t, c :: char) :: [integer]
  def shortest_to_char(s, c) do
    chars = String.graphemes(s)
    n = length(chars)

    # left-to-right pass
    {left_rev, _} =
      Enum.reduce(Enum.with_index(chars), {[], nil}, fn {ch, i}, {acc, last_pos} ->
        new_last = if ch == c, do: i, else: last_pos

        dist =
          case new_last do
            nil -> n
            pos -> i - pos
          end

        {[dist | acc], new_last}
      end)

    left = Enum.reverse(left_rev)

    # right-to-left pass
    {right_rev, _} =
      Enum.reduce(Enum.with_index(Enum.reverse(chars)), {[], nil}, fn {ch, rev_i},
                                                                      {acc, last_pos} ->
        i = n - 1 - rev_i
        new_last = if ch == c, do: i, else: last_pos

        dist =
          case new_last do
            nil -> n
            pos -> pos - i
          end

        {[dist | acc], new_last}
      end)

    right = Enum.reverse(right_rev)

    # combine minima from both passes
    Enum.zip(left, right)
    |> Enum.map(fn {l, r} -> min(l, r) end)
  end
end
```
