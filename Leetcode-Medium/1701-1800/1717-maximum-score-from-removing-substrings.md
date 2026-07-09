# 1717. Maximum Score From Removing Substrings

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // removes all occurrences of the pattern first+second using a stack
    pair<string,int> removePattern(const string& s, char first, char second) {
        vector<char> st;
        int removed = 0;
        for (char c : s) {
            if (!st.empty() && st.back() == first && c == second) {
                st.pop_back();
                ++removed;
            } else {
                st.push_back(c);
            }
        }
        string remaining(st.begin(), st.end());
        return {remaining, removed};
    }

    int maximumGain(string s, int x, int y) {
        long long total = 0;
        if (x >= y) {
            auto [s1, cnt1] = removePattern(s, 'a', 'b');
            total += 1LL * cnt1 * x;
            auto [s2, cnt2] = removePattern(s1, 'b', 'a');
            total += 1LL * cnt2 * y;
        } else {
            auto [s1, cnt1] = removePattern(s, 'b', 'a');
            total += 1LL * cnt1 * y; // y points for "ba"
            auto [s2, cnt2] = removePattern(s1, 'a', 'b');
            total += 1LL * cnt2 * x;
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int maximumGain(String s, int x, int y) {
        int total = 0;
        if (x >= y) {
            String afterFirst = remove(s, 'a', 'b');
            int removedFirst = (s.length() - afterFirst.length()) / 2;
            total += removedFirst * x;

            String afterSecond = remove(afterFirst, 'b', 'a');
            int removedSecond = (afterFirst.length() - afterSecond.length()) / 2;
            total += removedSecond * y;
        } else {
            // Remove "ba" first because it gives higher points
            String afterFirst = remove(s, 'b', 'a');
            int removedFirst = (s.length() - afterFirst.length()) / 2;
            total += removedFirst * y;

            String afterSecond = remove(afterFirst, 'a', 'b');
            int removedSecond = (afterFirst.length() - afterSecond.length()) / 2;
            total += removedSecond * x;
        }
        return total;
    }

    private String remove(String s, char first, char second) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == first && c == second) {
                sb.deleteCharAt(sb.length() - 1); // remove the matching pair
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_and_score(st, first, second, pts):
            stack = []
            score = 0
            for ch in st:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += pts
                else:
                    stack.append(ch)
            return ''.join(stack), score

        total = 0
        # Remove higher scoring substring first
        if x >= y:
            s, gain = remove_and_score(s, 'a', 'b', x)
            total += gain
            s, gain = remove_and_score(s, 'b', 'a', y)
            total += gain
        else:
            s, gain = remove_and_score(s, 'b', 'a', y)
            total += gain
            s, gain = remove_and_score(s, 'a', 'b', x)
            total += gain

        return total
```

## Python3

```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(st: str, pair: str):
            first, second = pair[0], pair[1]
            stack = []
            cnt = 0
            for ch in st:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    cnt += 1
                else:
                    stack.append(ch)
            return ''.join(stack), cnt

        total = 0
        if x >= y:
            s, c = remove_substring(s, "ab")
            total += c * x
            s, c = remove_substring(s, "ba")
            total += c * y
        else:
            s, c = remove_substring(s, "ba")
            total += c * y
            s, c = remove_substring(s, "ab")
            total += c * x
        return total
```

## C

```c
#include <stdlib.h>
#include <string.h>

int maximumGain(char* s, int x, int y) {
    int n = (int)strlen(s);
    char *stack1 = (char*)malloc(n * sizeof(char));
    char *stack2 = (char*)malloc(n * sizeof(char));
    if (!stack1 || !stack2) return 0;

    char highFirst, highSecond, lowFirst, lowSecond;
    int highScore, lowScore;

    if (x >= y) {
        highFirst = 'a'; highSecond = 'b'; highScore = x;
        lowFirst = 'b'; lowSecond = 'a'; lowScore = y;
    } else {
        highFirst = 'b'; highSecond = 'a'; highScore = y;
        lowFirst = 'a'; lowSecond = 'b'; lowScore = x;
    }

    int top = 0, removedHigh = 0;
    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (top > 0 && stack1[top - 1] == highFirst && c == highSecond) {
            --top;
            ++removedHigh;
        } else {
            stack1[top++] = c;
        }
    }

    int top2 = 0, removedLow = 0;
    for (int i = 0; i < top; ++i) {
        char c = stack1[i];
        if (top2 > 0 && stack2[top2 - 1] == lowFirst && c == lowSecond) {
            --top2;
            ++removedLow;
        } else {
            stack2[top2++] = c;
        }
    }

    int total = removedHigh * highScore + removedLow * lowScore;

    free(stack1);
    free(stack2);
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumGain(string s, int x, int y)
    {
        int total = 0;
        if (x >= y)
        {
            var firstPass = Remove(s, 'a', 'b', x);
            total += firstPass.gain;
            var secondPass = Remove(firstPass.remaining, 'b', 'a', y);
            total += secondPass.gain;
        }
        else
        {
            var firstPass = Remove(s, 'b', 'a', y);
            total += firstPass.gain;
            var secondPass = Remove(firstPass.remaining, 'a', 'b', x);
            total += secondPass.gain;
        }
        return total;
    }

    private (string remaining, int gain) Remove(string s, char first, char second, int points)
    {
        var stack = new System.Collections.Generic.Stack<char>();
        int gain = 0;
        foreach (char c in s)
        {
            if (stack.Count > 0 && stack.Peek() == first && c == second)
            {
                stack.Pop();
                gain += points;
            }
            else
            {
                stack.Push(c);
            }
        }

        char[] arr = new char[stack.Count];
        int idx = arr.Length - 1;
        while (stack.Count > 0)
        {
            arr[idx--] = stack.Pop();
        }

        return (new string(arr), gain);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var maximumGain = function(s, x, y) {
    const removePair = (str, pair) => {
        const stack = [];
        const first = pair[0], second = pair[1];
        for (const ch of str) {
            if (stack.length && stack[stack.length - 1] === first && ch === second) {
                stack.pop(); // remove the pair
            } else {
                stack.push(ch);
            }
        }
        return stack.join('');
    };
    
    let total = 0;
    if (x >= y) {
        const afterFirst = removePair(s, "ab");
        total += ((s.length - afterFirst.length) >> 1) * x; // each removal reduces length by 2
        const afterSecond = removePair(afterFirst, "ba");
        total += ((afterFirst.length - afterSecond.length) >> 1) * y;
    } else {
        const afterFirst = removePair(s, "ba");
        total += ((s.length - afterFirst.length) >> 1) * y;
        const afterSecond = removePair(afterFirst, "ab");
        total += ((afterFirst.length - afterSecond.length) >> 1) * x;
    }
    return total;
};
```

## Typescript

```typescript
function maximumGain(s: string, x: number, y: number): number {
    const remove = (input: string, first: string, second: string): { remaining: string; count: number } => {
        const stack: string[] = [];
        let cnt = 0;
        for (const ch of input) {
            if (stack.length && stack[stack.length - 1] === first && ch === second) {
                stack.pop();
                cnt++;
            } else {
                stack.push(ch);
            }
        }
        return { remaining: stack.join(''), count: cnt };
    };

    let total = 0;
    if (x >= y) {
        const firstPass = remove(s, 'a', 'b');
        total += firstPass.count * x;
        const secondPass = remove(firstPass.remaining, 'b', 'a');
        total += secondPass.count * y;
    } else {
        const firstPass = remove(s, 'b', 'a');
        total += firstPass.count * y;
        const secondPass = remove(firstPass.remaining, 'a', 'b');
        total += secondPass.count * x;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function maximumGain($s, $x, $y) {
        if ($x >= $y) {
            list($remaining, $score1) = $this->removeAndScore($s, 'ab', $x);
            list($_, $score2) = $this->removeAndScore($remaining, 'ba', $y);
        } else {
            list($remaining, $score1) = $this->removeAndScore($s, 'ba', $y);
            list($_, $score2) = $this->removeAndScore($remaining, 'ab', $x);
        }
        return $score1 + $score2;
    }

    /**
     * Removes all occurrences of $pair from $s using a stack and returns the remaining string
     * together with the total points earned.
     *
     * @param String $s
     * @param String $pair Two‑character substring to remove (e.g., "ab" or "ba")
     * @param Integer $points Points earned per removal of $pair
     * @return array [remaining string, total points]
     */
    private function removeAndScore($s, $pair, $points) {
        $stack = [];
        $score = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; ++$i) {
            $c = $s[$i];
            if (!empty($stack)) {
                $top = end($stack);
                if ($top . $c === $pair) {
                    array_pop($stack);   // remove the matching previous character
                    $score += $points;    // gain points for this removal
                    continue;             // current char is also removed, skip pushing
                }
            }
            $stack[] = $c;
        }
        $remaining = implode('', $stack);
        return [$remaining, $score];
    }
}
```

## Swift

```swift
class Solution {
    func maximumGain(_ s: String, _ x: Int, _ y: Int) -> Int {
        let chars = Array(s)
        
        // Helper to remove target substring using a stack
        func remove(_ arr: [Character], _ first: Character, _ second: Character) -> ([Character], Int) {
            var stack = [Character]()
            var removed = 0
            for ch in arr {
                if let last = stack.last, last == first && ch == second {
                    stack.removeLast()
                    removed += 1
                } else {
                    stack.append(ch)
                }
            }
            return (stack, removed)
        }
        
        if x >= y {
            // Remove "ab" first, then "ba"
            let (afterFirst, cnt1) = remove(chars, "a", "b")
            let (afterSecond, cnt2) = remove(afterFirst, "b", "a")
            return cnt1 * x + cnt2 * y
        } else {
            // Remove "ba" first, then "ab"
            let (afterFirst, cnt1) = remove(chars, "b", "a")
            let (afterSecond, cnt2) = remove(afterFirst, "a", "b")
            return cnt1 * y + cnt2 * x
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumGain(s: String, x: Int, y: Int): Int {
        var total = 0
        if (x >= y) {
            val firstPass = removeAndScore(s, 'a', 'b', x)
            total += firstPass.second
            val secondPass = removeAndScore(firstPass.first, 'b', 'a', y)
            total += secondPass.second
        } else {
            val firstPass = removeAndScore(s, 'b', 'a', y)
            total += firstPass.second
            val secondPass = removeAndScore(firstPass.first, 'a', 'b', x)
            total += secondPass.second
        }
        return total
    }

    private fun removeAndScore(str: String, first: Char, second: Char, gain: Int): Pair<String, Int> {
        val stack = CharArray(str.length)
        var size = 0
        var score = 0
        for (c in str) {
            if (size > 0 && stack[size - 1] == first && c == second) {
                size--
                score += gain
            } else {
                stack[size++] = c
            }
        }
        return Pair(String(stack, 0, size), score)
    }
}
```

## Dart

```dart
class Solution {
  int maximumGain(String s, int x, int y) {
    String firstTarget;
    String secondTarget;
    int firstScore;
    int secondScore;

    if (x >= y) {
      firstTarget = 'ab';
      firstScore = x;
      secondTarget = 'ba';
      secondScore = y;
    } else {
      firstTarget = 'ba';
      firstScore = y;
      secondTarget = 'ab';
      secondScore = x;
    }

    String afterFirst = _remove(s, firstTarget);
    int removedFirst = (s.length - afterFirst.length) ~/ 2;
    int total = removedFirst * firstScore;

    String afterSecond = _remove(afterFirst, secondTarget);
    int removedSecond = (afterFirst.length - afterSecond.length) ~/ 2;
    total += removedSecond * secondScore;

    return total;
  }

  String _remove(String s, String target) {
    List<int> stack = [];
    int t0 = target.codeUnitAt(0);
    int t1 = target.codeUnitAt(1);

    for (int i = 0; i < s.length; i++) {
      int ch = s.codeUnitAt(i);
      if (stack.isNotEmpty && stack.last == t0 && ch == t1) {
        stack.removeLast();
      } else {
        stack.add(ch);
      }
    }

    return String.fromCharCodes(stack);
  }
}
```

## Golang

```go
func maximumGain(s string, x int, y int) int {
    total := 0
    if x >= y {
        var cnt int
        s, cnt = removePairs(s, 'a', 'b')
        total += cnt * x
        s, cnt = removePairs(s, 'b', 'a')
        total += cnt * y
    } else {
        var cnt int
        s, cnt = removePairs(s, 'b', 'a')
        total += cnt * y
        s, cnt = removePairs(s, 'a', 'b')
        total += cnt * x
    }
    return total
}

func removePairs(str string, first, second byte) (string, int) {
    stack := make([]byte, 0, len(str))
    removed := 0
    for i := 0; i < len(str); i++ {
        c := str[i]
        if len(stack) > 0 && stack[len(stack)-1] == first && c == second {
            stack = stack[:len(stack)-1]
            removed++
        } else {
            stack = append(stack, c)
        }
    }
    return string(stack), removed
}
```

## Ruby

```ruby
def maximum_gain(s, x, y)
  # Helper that removes all occurrences of the target pair (first, second) using a stack.
  # Returns the resulting string and the number of removals performed.
  remove_pair = lambda do |str, first_char, second_char|
    stack = []
    removed = 0
    str.each_char do |ch|
      if !stack.empty? && stack[-1] == first_char && ch == second_char
        stack.pop
        removed += 1
      else
        stack << ch
      end
    end
    [stack.join, removed]
  end

  total = 0

  if x >= y
    # Remove "ab" first (higher or equal points), then "ba"
    s, cnt = remove_pair.call(s, 'a', 'b')
    total += cnt * x
    s, cnt = remove_pair.call(s, 'b', 'a')
    total += cnt * y
  else
    # Remove "ba" first (higher points), then "ab"
    s, cnt = remove_pair.call(s, 'b', 'a')
    total += cnt * y
    s, cnt = remove_pair.call(s, 'a', 'b')
    total += cnt * x
  end

  total
end
```

## Scala

```scala
object Solution {
    def maximumGain(s: String, x: Int, y: Int): Int = {
        // helper that removes all occurrences of the pair (c1,c2) and returns
        // the resulting string together with how many pairs were removed
        def remove(str: String, c1: Char, c2: Char): (String, Int) = {
            val sb = new java.lang.StringBuilder()
            var cnt = 0
            var i = 0
            while (i < str.length) {
                val ch = str.charAt(i)
                if (sb.length() > 0 && sb.charAt(sb.length() - 1) == c1 && ch == c2) {
                    sb.setLength(sb.length() - 1) // pop the matching c1
                    cnt += 1
                } else {
                    sb.append(ch)
                }
                i += 1
            }
            (sb.toString, cnt)
        }

        if (x >= y) {
            val (afterFirst, firstCnt) = remove(s, 'a', 'b')
            val scoreFirst = firstCnt * x
            val (afterSecond, secondCnt) = remove(afterFirst, 'b', 'a')
            val scoreSecond = secondCnt * y
            scoreFirst + scoreSecond
        } else {
            // prioritize removing "ba" first
            val (afterFirst, firstCnt) = remove(s, 'b', 'a')
            val scoreFirst = firstCnt * y
            val (afterSecond, secondCnt) = remove(afterFirst, 'a', 'b')
            val scoreSecond = secondCnt * x
            scoreFirst + scoreSecond
        }
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    fn remove_substring(s: String, first: char, second: char) -> (String, i32) {
        let mut stack: Vec<char> = Vec::with_capacity(s.len());
        let mut cnt: i32 = 0;
        for ch in s.chars() {
            if let Some(&last) = stack.last() {
                if last == first && ch == second {
                    stack.pop();
                    cnt += 1;
                    continue;
                }
            }
            stack.push(ch);
        }
        let new_s: String = stack.iter().collect();
        (new_s, cnt)
    }

    pub fn maximum_gain(s: String, x: i32, y: i32) -> i32 {
        let mut total: i64 = 0;
        if x >= y {
            // remove "ab" first
            let (s1, c1) = Self::remove_substring(s, 'a', 'b');
            total += c1 as i64 * x as i64;
            let (s2, c2) = Self::remove_substring(s1, 'b', 'a');
            total += c2 as i64 * y as i64;
        } else {
            // remove "ba" first
            let (s1, c1) = Self::remove_substring(s, 'b', 'a');
            total += c1 as i64 * y as i64;
            let (s2, c2) = Self::remove_substring(s1, 'a', 'b');
            total += c2 as i64 * x as i64;
        }
        total as i32
    }
}
```

## Racket

```racket
#lang racket

(define (remove-substring str first second)
  (let loop ((i 0) (stack '()))
    (if (= i (string-length str))
        (list->string (reverse stack))
        (let ((c (string-ref str i)))
          (if (and (pair? stack)
                   (char=? (car stack) first)
                   (char=? c second))
              (loop (+ i 1) (cdr stack)) ; pop the matching pair
              (loop (+ i 1) (cons c stack)))))))

(define/contract (maximum-gain s x y)
  (-> string? exact-integer? exact-integer? exact-integer?)
  (let* ((high-first (if (>= x y) #\a #\b))
         (high-second (if (>= x y) #\b #\a))
         (low-first (if (>= x y) #\b #\a))
         (low-second (if (>= x y) #\a #\b))
         (high-val (max x y))
         (low-val (min x y)))
    (let* ((s1 (remove-substring s high-first high-second))
           (removed-high (/ (- (string-length s) (string-length s1)) 2))
           (score-high (* removed-high high-val))
           (s2 (remove-substring s1 low-first low-second))
           (removed-low (/ (- (string-length s1) (string-length s2)) 2))
           (score-low (* removed-low low-val)))
      (+ score-high score-low))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_gain/3]).

-spec maximum_gain(S :: unicode:unicode_binary(), X :: integer(), Y :: integer()) -> integer().
maximum_gain(S, X, Y) ->
    Chars = binary_to_list(S),
    case X >= Y of
        true ->
            {AfterAB, CountAB} = remove_substring(Chars, $a, $b),
            ScoreAB = CountAB * X,
            {AfterBA, CountBA} = remove_substring(AfterAB, $b, $a),
            ScoreBA = CountBA * Y,
            ScoreAB + ScoreBA;
        false ->
            {AfterBA, CountBA} = remove_substring(Chars, $b, $a),
            ScoreBA = CountBA * Y,
            {AfterAB, CountAB} = remove_substring(AfterBA, $a, $b),
            ScoreAB = CountAB * X,
            ScoreAB + ScoreBA
    end.

remove_substring(Chars, C1, C2) ->
    remove_substring(Chars, [], 0, C1, C2).

remove_substring([], Stack, Count, _C1, _C2) ->
    {lists:reverse(Stack), Count};
remove_substring([H|T], Stack, Count, C1, C2) ->
    case Stack of
        [Top|Rest] when Top =:= C1, H =:= C2 ->
            remove_substring(T, Rest, Count + 1, C1, C2);
        _ ->
            remove_substring(T, [H|Stack], Count, C1, C2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_gain(s :: String.t(), x :: integer, y :: integer) :: integer
  def maximum_gain(s, x, y) do
    if x >= y do
      {s1, cnt1} = remove_pair(s, {?a, ?b})
      score1 = cnt1 * x

      {s2, cnt2} = remove_pair(s1, {?b, ?a})
      score2 = cnt2 * y

      score1 + score2
    else
      {s1, cnt1} = remove_pair(s, {?b, ?a})
      score1 = cnt1 * y

      {s2, cnt2} = remove_pair(s1, {?a, ?b})
      score2 = cnt2 * x

      score1 + score2
    end
  end

  defp remove_pair(str, {first, second}) do
    chars = String.to_charlist(str)

    {stack, removed} =
      Enum.reduce(chars, {[], 0}, fn ch, {stk, cnt} ->
        case stk do
          [^first | rest] when ch == second -> {rest, cnt + 1}
          _ -> {[ch | stk], cnt}
        end
      end)

    new_str = stack |> Enum.reverse() |> to_string()
    {new_str, removed}
  end
end
```
