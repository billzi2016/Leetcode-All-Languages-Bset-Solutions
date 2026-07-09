# 2024. Maximize the Confusion of an Exam

## Cpp

```cpp
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int n = answerKey.size();
        auto maxWindow = [&](char target) {
            int left = 0, flips = 0, best = 0;
            for (int right = 0; right < n; ++right) {
                if (answerKey[right] != target) ++flips;
                while (flips > k) {
                    if (answerKey[left] != target) --flips;
                    ++left;
                }
                best = max(best, right - left + 1);
            }
            return best;
        };
        return max(maxWindow('T'), maxWindow('F'));
    }
};
```

## Java

```java
class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        return Math.max(window(answerKey, k, 'T'), window(answerKey, k, 'F'));
    }
    
    private int window(String s, int k, char target) {
        int left = 0, maxLen = 0, oppositeCount = 0;
        for (int right = 0; right < s.length(); right++) {
            if (s.charAt(right) != target) {
                oppositeCount++;
            }
            while (oppositeCount > k) {
                if (s.charAt(left) != target) {
                    oppositeCount--;
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
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def longest(target):
            left = 0
            flips = 0
            best = 0
            for right, ch in enumerate(answerKey):
                if ch != target:
                    flips += 1
                while flips > k:
                    if answerKey[left] != target:
                        flips -= 1
                    left += 1
                best = max(best, right - left + 1)
            return best

        return max(longest('T'), longest('F'))
```

## Python3

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest(target: str) -> int:
            left = 0
            flips = 0
            best = 0
            for right, ch in enumerate(answerKey):
                if ch != target:
                    flips += 1
                while flips > k:
                    if answerKey[left] != target:
                        flips -= 1
                    left += 1
                best = max(best, right - left + 1)
            return best

        return max(longest('T'), longest('F'))
```

## C

```c
#include <string.h>

int maxConsecutiveAnswers(char* answerKey, int k) {
    int n = strlen(answerKey);
    int res = 0;

    // Target 'T'
    int left = 0, opp = 0;
    for (int right = 0; right < n; ++right) {
        if (answerKey[right] != 'T') opp++;
        while (opp > k) {
            if (answerKey[left] != 'T') opp--;
            left++;
        }
        int len = right - left + 1;
        if (len > res) res = len;
    }

    // Target 'F'
    left = 0; opp = 0;
    for (int right = 0; right < n; ++right) {
        if (answerKey[right] != 'F') opp++;
        while (opp > k) {
            if (answerKey[left] != 'F') opp--;
            left++;
        }
        int len = right - left + 1;
        if (len > res) res = len;
    }

    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxConsecutiveAnswers(string answerKey, int k) {
        int left = 0, maxLen = 0;
        int countT = 0, countF = 0;
        for (int right = 0; right < answerKey.Length; right++) {
            if (answerKey[right] == 'T') countT++;
            else countF++;

            while ((right - left + 1) - System.Math.Max(countT, countF) > k) {
                if (answerKey[left] == 'T') countT--;
                else countF--;
                left++;
            }

            maxLen = System.Math.Max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} answerKey
 * @param {number} k
 * @return {number}
 */
var maxConsecutiveAnswers = function(answerKey, k) {
    const n = answerKey.length;
    let result = 0;
    for (const target of ['T', 'F']) {
        let left = 0, flips = 0;
        for (let right = 0; right < n; ++right) {
            if (answerKey[right] !== target) flips++;
            while (flips > k) {
                if (answerKey[left] !== target) flips--;
                left++;
            }
            result = Math.max(result, right - left + 1);
        }
    }
    return result;
};
```

## Typescript

```typescript
function maxConsecutiveAnswers(answerKey: string, k: number): number {
    const n = answerKey.length;
    let best = 0;

    const slide = (target: string) => {
        let left = 0;
        let changes = 0;
        for (let right = 0; right < n; ++right) {
            if (answerKey[right] !== target) changes++;
            while (changes > k) {
                if (answerKey[left] !== target) changes--;
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
    };

    slide('T');
    slide('F');

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param String $answerKey
     * @param Integer $k
     * @return Integer
     */
    function maxConsecutiveAnswers($answerKey, $k) {
        $n = strlen($answerKey);
        $left = 0;
        $countT = 0;
        $countF = 0;
        $maxLen = 0;

        for ($right = 0; $right < $n; $right++) {
            if ($answerKey[$right] === 'T') {
                $countT++;
            } else {
                $countF++;
            }

            while (min($countT, $countF) > $k) {
                if ($answerKey[$left] === 'T') {
                    $countT--;
                } else {
                    $countF--;
                }
                $left++;
            }

            $currentLen = $right - $left + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func maxConsecutiveAnswers(_ answerKey: String, _ k: Int) -> Int {
        let chars = Array(answerKey)
        let n = chars.count
        
        func maxLen(target: Character) -> Int {
            var left = 0
            var flips = 0
            var best = 0
            for right in 0..<n {
                if chars[right] != target { flips += 1 }
                while flips > k {
                    if chars[left] != target { flips -= 1 }
                    left += 1
                }
                let length = right - left + 1
                if length > best { best = length }
            }
            return best
        }
        
        let ansT = maxLen(target: "T")
        let ansF = maxLen(target: "F")
        return max(ansT, ansF)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxConsecutiveAnswers(answerKey: String, k: Int): Int {
        return kotlin.math.max(longest(answerKey, 'T', k), longest(answerKey, 'F', k))
    }

    private fun longest(s: String, target: Char, k: Int): Int {
        var left = 0
        var maxLen = 0
        var changes = 0
        for (right in s.indices) {
            if (s[right] != target) changes++
            while (changes > k) {
                if (s[left] != target) changes--
                left++
            }
            val len = right - left + 1
            if (len > maxLen) maxLen = len
        }
        return maxLen
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxConsecutiveAnswers(String answerKey, int k) {
    return max(_maxLen(answerKey, 'T', k), _maxLen(answerKey, 'F', k));
  }

  int _maxLen(String s, String target, int k) {
    int left = 0;
    int diffCount = 0;
    int best = 0;
    for (int right = 0; right < s.length; ++right) {
      if (s[right] != target) diffCount++;
      while (diffCount > k) {
        if (s[left] != target) diffCount--;
        left++;
      }
      best = max(best, right - left + 1);
    }
    return best;
  }
}
```

## Golang

```go
func maxConsecutiveAnswers(answerKey string, k int) int {
	n := len(answerKey)
	maxLen := func(target byte) int {
		left, changes, best := 0, 0, 0
		for right := 0; right < n; right++ {
			if answerKey[right] != target {
				changes++
			}
			for changes > k {
				if answerKey[left] != target {
					changes--
				}
				left++
			}
			if cur := right - left + 1; cur > best {
				best = cur
			}
		}
		return best
	}
	tmax := maxLen('T')
	fmax := maxLen('F')
	if tmax > fmax {
		return tmax
	}
	return fmax
}
```

## Ruby

```ruby
def max_consecutive_answers(answer_key, k)
  n = answer_key.length
  max_len = 0
  ['T', 'F'].each do |target|
    left = 0
    diff = 0
    (0...n).each do |right|
      diff += 1 if answer_key[right] != target
      while diff > k
        diff -= 1 if answer_key[left] != target
        left += 1
      end
      max_len = [max_len, right - left + 1].max
    end
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def maxConsecutiveAnswers(answerKey: String, k: Int): Int = {
        val n = answerKey.length
        def maxWindow(target: Char): Int = {
            var left = 0
            var opposite = 0
            var best = 0
            var right = 0
            while (right < n) {
                if (answerKey.charAt(right) != target) opposite += 1
                while (opposite > k) {
                    if (answerKey.charAt(left) != target) opposite -= 1
                    left += 1
                }
                best = math.max(best, right - left + 1)
                right += 1
            }
            best
        }
        math.max(maxWindow('T'), maxWindow('F'))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        let bytes = answer_key.as_bytes();
        let n = bytes.len();
        let k_usize = k as usize;
        let mut best = 0usize;

        for &target in &[b'T', b'F'] {
            let mut left = 0usize;
            let mut diff = 0usize; // count of chars not equal to target
            for right in 0..n {
                if bytes[right] != target {
                    diff += 1;
                }
                while diff > k_usize {
                    if bytes[left] != target {
                        diff -= 1;
                    }
                    left += 1;
                }
                let len = right - left + 1;
                if len > best {
                    best = len;
                }
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(define/contract (max-consecutive-answers answerKey k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length answerKey))
         (char-vec (for/vector ([i (in-range n)]) (string-ref answerKey i))))
    (define (longest target)
      (let loop ((left 0) (right 0) (opp 0) (best 0))
        (if (= right n)
            best
            (let* ((c (vector-ref char-vec right))
                   (new-opp (if (char=? c target) opp (+ opp 1))))
              (let-values ([(new-left new-opp2)
                            (let recur ((l left) (o new-opp))
                              (if (> o k)
                                  (let ((c-left (vector-ref char-vec l)))
                                    (recur (+ l 1) (if (char=? c-left target) o (- o 1))))
                                  (values l o)))])
                (loop new-left (+ right 1) new-opp2
                      (max best (- (+ right 1) new-left))))))))
    (max (longest #\T) (longest #\F))))
```

## Erlang

```erlang
-module(solution).
-export([max_consecutive_answers/2]).

-spec max_consecutive_answers(AnswerKey :: unicode:unicode_binary(), K :: integer()) -> integer().
max_consecutive_answers(AnswerKey, K) ->
    List = binary_to_list(AnswerKey),
    Tuple = list_to_tuple(List),
    N = tuple_size(Tuple),
    MaxT = max_len($T, Tuple, N, K),
    MaxF = max_len($F, Tuple, N, K),
    if MaxT > MaxF -> MaxT; true -> MaxF end.

max_len(Target, Tuple, N, K) ->
    Loop = fun(F, Right, Left, Count, Max) ->
        case Right == N of
            true -> Max;
            false ->
                Char = element(Right + 1, Tuple),
                NewCount = if Char =:= Target -> Count; true -> Count + 1 end,
                {NewLeft, AdjCount} =
                    if NewCount =< K ->
                        {Left, NewCount};
                       true ->
                        shrink(Target, Tuple, Left, NewCount, K)
                    end,
                NewMax = erlang:max(Max, Right - NewLeft + 1),
                F(F, Right + 1, NewLeft, AdjCount, NewMax)
        end
    end,
    Loop(Loop, 0, 0, 0, 0).

shrink(Target, Tuple, Left, Count, K) ->
    case Count =< K of
        true -> {Left, Count};
        false ->
            CharL = element(Left + 1, Tuple),
            NewCount = if CharL =:= Target -> Count; true -> Count - 1 end,
            shrink(Target, Tuple, Left + 1, NewCount, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_consecutive_answers(answer_key :: String.t(), k :: integer) :: integer
  def max_consecutive_answers(answer_key, k) do
    n = byte_size(answer_key)
    iterate(0, 0, 0, 0, 0, n, answer_key, k)
  end

  # right, left, count_T, count_F, current_max, total_len, string, k
  defp iterate(right, left, cnt_t, cnt_f, cur_max, n, s, k) when right == n do
    cur_max
  end

  defp iterate(right, left, cnt_t, cnt_f, cur_max, n, s, k) do
    c = :binary.at(s, right)

    {cnt_t, cnt_f} =
      if c == ?T do
        {cnt_t + 1, cnt_f}
      else
        {cnt_t, cnt_f + 1}
      end

    {left, cnt_t, cnt_f} = shrink(left, cnt_t, cnt_f, k, s)

    len = right - left + 1
    new_max = if len > cur_max, do: len, else: cur_max

    iterate(right + 1, left, cnt_t, cnt_f, new_max, n, s, k)
  end

  defp shrink(left, cnt_t, cnt_f, k, s) do
    if min(cnt_t, cnt_f) <= k do
      {left, cnt_t, cnt_f}
    else
      cl = :binary.at(s, left)

      {cnt_t, cnt_f} =
        if cl == ?T do
          {cnt_t - 1, cnt_f}
        else
          {cnt_t, cnt_f - 1}
        end

      shrink(left + 1, cnt_t, cnt_f, k, s)
    end
  end
end
```
