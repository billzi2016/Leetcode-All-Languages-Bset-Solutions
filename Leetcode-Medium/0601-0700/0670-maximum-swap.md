# 0670. Maximum Swap

## Cpp

```cpp
class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        vector<int> last(10, -1);
        for (int i = 0; i < (int)s.size(); ++i) {
            last[s[i] - '0'] = i;
        }
        for (int i = 0; i < (int)s.size(); ++i) {
            int cur = s[i] - '0';
            for (int d = 9; d > cur; --d) {
                if (last[d] > i) {
                    swap(s[i], s[last[d]]);
                    return stoi(s);
                }
            }
        }
        return num;
    }
};
```

## Java

```java
class Solution {
    public int maximumSwap(int num) {
        char[] digits = Integer.toString(num).toCharArray();
        int n = digits.length;
        int[] lastPos = new int[10];
        for (int i = 0; i < n; i++) {
            lastPos[digits[i] - '0'] = i;
        }
        for (int i = 0; i < n; i++) {
            int currentDigit = digits[i] - '0';
            for (int d = 9; d > currentDigit; d--) {
                if (lastPos[d] > i) {
                    char temp = digits[i];
                    digits[i] = digits[lastPos[d]];
                    digits[lastPos[d]] = temp;
                    return Integer.parseInt(new String(digits));
                }
            }
        }
        return num;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        last_pos = [0] * 10
        for i, ch in enumerate(digits):
            last_pos[int(ch)] = i

        for i, ch in enumerate(digits):
            cur = int(ch)
            for d in range(9, cur, -1):
                if last_pos[d] > i:
                    j = last_pos[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        return num
```

## Python3

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_pos = [-1] * 10
        for i, ch in enumerate(digits):
            last_pos[int(ch)] = i

        for i, ch in enumerate(digits):
            cur = int(ch)
            for d in range(9, cur, -1):
                if last_pos[d] > i:
                    j = last_pos[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        return num
```

## C

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int maximumSwap(int num) {
    char s[12];
    int len = snprintf(s, sizeof(s), "%d", num);
    if (len <= 1) return num;

    int lastSeen[10];
    for (int i = 0; i < 10; ++i) lastSeen[i] = -1;
    for (int i = 0; i < len; ++i) {
        lastSeen[s[i] - '0'] = i;
    }

    for (int i = 0; i < len; ++i) {
        int cur = s[i] - '0';
        for (int d = 9; d > cur; --d) {
            if (lastSeen[d] > i) {
                // swap
                char tmp = s[i];
                s[i] = s[lastSeen[d]];
                s[lastSeen[d]] = tmp;
                return atoi(s);
            }
        }
    }
    return num;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumSwap(int num) {
        char[] digits = num.ToString().ToCharArray();
        int n = digits.Length;
        int[] last = new int[10];
        for (int i = 0; i < n; i++) {
            last[digits[i] - '0'] = i;
        }
        for (int i = 0; i < n; i++) {
            int cur = digits[i] - '0';
            for (int d = 9; d > cur; d--) {
                if (last[d] > i) {
                    char temp = digits[i];
                    digits[i] = digits[last[d]];
                    digits[last[d]] = temp;
                    return int.Parse(new string(digits));
                }
            }
        }
        return num;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var maximumSwap = function(num) {
    const s = num.toString().split('');
    const lastPos = new Array(10).fill(-1);
    for (let i = 0; i < s.length; ++i) {
        lastPos[s[i].charCodeAt(0) - 48] = i;
    }
    for (let i = 0; i < s.length; ++i) {
        const curDigit = s[i].charCodeAt(0) - 48;
        for (let d = 9; d > curDigit; --d) {
            if (lastPos[d] > i) {
                // swap
                const tmp = s[i];
                s[i] = s[lastPos[d]];
                s[lastPos[d]] = tmp;
                return parseInt(s.join(''), 10);
            }
        }
    }
    return num;
};
```

## Typescript

```typescript
function maximumSwap(num: number): number {
    const digits = Array.from(String(num));
    const lastPos = new Array(10).fill(-1);
    for (let i = 0; i < digits.length; i++) {
        lastPos[digits[i].charCodeAt(0) - 48] = i;
    }
    for (let i = 0; i < digits.length; i++) {
        const cur = digits[i].charCodeAt(0) - 48;
        for (let d = 9; d > cur; d--) {
            if (lastPos[d] > i) {
                const j = lastPos[d];
                [digits[i], digits[j]] = [digits[j], digits[i]];
                return Number(digits.join(''));
            }
        }
    }
    return num;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function maximumSwap($num) {
        $s = strval($num);
        $n = strlen($s);
        // record last position of each digit 0-9
        $last = array_fill(0, 10, -1);
        for ($i = 0; $i < $n; $i++) {
            $digit = intval($s[$i]);
            $last[$digit] = $i;
        }
        // try to find the first position where a larger digit appears later
        for ($i = 0; $i < $n; $i++) {
            $curr = intval($s[$i]);
            for ($d = 9; $d > $curr; $d--) {
                if ($last[$d] > $i) {
                    // swap positions i and last[d]
                    $tmp = $s[$i];
                    $s[$i] = $s[$last[$d]];
                    $s[$last[$d]] = $tmp;
                    return intval($s);
                }
            }
        }
        return $num;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var digits = Array(String(num))
        let n = digits.count
        var lastPos = [Int](repeating: -1, count: 10)
        
        for i in 0..<n {
            if let val = digits[i].wholeNumberValue {
                lastPos[val] = i
            }
        }
        
        for i in 0..<n {
            guard let curVal = digits[i].wholeNumberValue else { continue }
            var d = 9
            while d > curVal {
                if lastPos[d] > i {
                    digits.swapAt(i, lastPos[d])
                    return Int(String(digits))!
                }
                d -= 1
            }
        }
        return num
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSwap(num: Int): Int {
        val chars = num.toString().toCharArray()
        val last = IntArray(10) { -1 }
        for (i in chars.indices) {
            last[chars[i] - '0'] = i
        }
        for (i in chars.indices) {
            val cur = chars[i] - '0'
            for (d in 9 downTo cur + 1) {
                if (last[d] > i) {
                    val j = last[d]
                    val temp = chars[i]
                    chars[i] = chars[j]
                    chars[j] = temp
                    return String(chars).toInt()
                }
            }
        }
        return num
    }
}
```

## Dart

```dart
class Solution {
  int maximumSwap(int num) {
    List<String> digits = num.toString().split('');
    int n = digits.length;
    List<int> last = List.filled(10, -1);
    for (int i = 0; i < n; ++i) {
      last[int.parse(digits[i])] = i;
    }
    for (int i = 0; i < n; ++i) {
      int cur = int.parse(digits[i]);
      for (int d = 9; d > cur; --d) {
        if (last[d] > i) {
          String temp = digits[i];
          digits[i] = digits[last[d]];
          digits[last[d]] = temp;
          return int.parse(digits.join());
        }
      }
    }
    return num;
  }
}
```

## Golang

```go
package main

import "strconv"

func maximumSwap(num int) int {
	s := []byte(strconv.Itoa(num))
	last := make([]int, 10)
	for i := 0; i < 10; i++ {
		last[i] = -1
	}
	for i, ch := range s {
		last[ch-'0'] = i
	}
	for i, ch := range s {
		cur := int(ch - '0')
		for d := 9; d > cur; d-- {
			if last[d] > i {
				s[i], s[last[d]] = s[last[d]], s[i]
				res, _ := strconv.Atoi(string(s))
				return res
			}
		}
	}
	return num
}
```

## Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def maximum_swap(num)
  s = num.to_s.chars
  last = Array.new(10, -1)

  s.each_with_index do |ch, i|
    digit = ch.ord - 48
    last[digit] = i
  end

  s.each_with_index do |ch, i|
    cur_digit = ch.ord - 48
    (9).downto(cur_digit + 1) do |d|
      if last[d] > i
        j = last[d]
        s[i], s[j] = s[j], s[i]
        return s.join.to_i
      end
    end
  end

  num
end
```

## Scala

```scala
object Solution {
    def maximumSwap(num: Int): Int = {
        val chars = num.toString.toCharArray
        val lastPos = Array.fill(10)(-1)
        for (i <- chars.indices) {
            lastPos(chars(i) - '0') = i
        }
        for (i <- chars.indices) {
            val currentDigit = chars(i) - '0'
            var d = 9
            while (d > currentDigit) {
                if (lastPos(d) > i) {
                    val j = lastPos(d)
                    val tmp = chars(i)
                    chars(i) = chars(j)
                    chars(j) = tmp
                    return new String(chars).toInt
                }
                d -= 1
            }
        }
        num
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_swap(num: i32) -> i32 {
        let mut digits = num.to_string().into_bytes();
        let n = digits.len();
        let mut last = [-1i32; 10];
        for (i, &b) in digits.iter().enumerate() {
            last[(b - b'0') as usize] = i as i32;
        }
        for i in 0..n {
            let cur = (digits[i] - b'0') as usize;
            for d in ((cur + 1)..10).rev() {
                if last[d] > i as i32 {
                    let j = last[d] as usize;
                    digits.swap(i, j);
                    return std::str::from_utf8(&digits).unwrap().parse::<i32>().unwrap();
                }
            }
        }
        num
    }
}
```

## Racket

```racket
(define/contract (maximum-swap num)
  (-> exact-integer? exact-integer?)
  (call/cc
    (lambda (return)
      (let* ((s (number->string num))
             (n (string-length s)))
        (if (= n 1) (return num))
        (let* ((last-seen (make-vector 10 -1))
               (chars (list->vector (string->list s))))
          ;; record last occurrence of each digit
          (for ([i (in-range n)])
            (let* ((c (vector-ref chars i))
                   (d (- (char->integer c) (char->integer #\0))))
              (vector-set! last-seen d i)))
          ;; find first beneficial swap
          (for ([i (in-range n)])
            (let* ((c (vector-ref chars i))
                   (cur (- (char->integer c) (char->integer #\0))))
              (for ([d (in-range 9 -1 -1)]) ; from 9 down to 0
                (when (> d cur)
                  (let ((j (vector-ref last-seen d)))
                    (when (> j i)
                      ;; swap and return result
                      (let ((temp (vector-ref chars i)))
                        (vector-set! chars i (vector-ref chars j))
                        (vector-set! chars j temp))
                      (return (string->number (list->string (vector->list chars))))))))))
          ;; no improving swap found
          (return num))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_swap/1]).

-spec maximum_swap(Num :: integer()) -> integer().
maximum_swap(Num) ->
    Digits = integer_to_list(Num),
    LastSeen = build_last_seen(Digits, 0, #{}),
    case find_swap(Digits, LastSeen, 0) of
        none ->
            Num;
        {I, J} ->
            Tuple = list_to_tuple(Digits),
            Di = element(I + 1, Tuple),
            Dj = element(J + 1, Tuple),
            NewTuple = setelement(I + 1, setelement(J + 1, Tuple, Di), Dj),
            list_to_integer(tuple_to_list(NewTuple))
    end.

build_last_seen([], _Idx, Acc) -> Acc;
build_last_seen([C | Rest], Idx, Acc) ->
    Digit = C - $0,
    NewAcc = maps:put(Digit, Idx, Acc),
    build_last_seen(Rest, Idx + 1, NewAcc).

find_swap([], _LastSeen, _Idx) -> none;
find_swap([C | Rest], LastSeen, I) ->
    Curr = C - $0,
    case find_higher(Curr, LastSeen, I, 9) of
        not_found ->
            find_swap(Rest, LastSeen, I + 1);
        {J} ->
            {I, J}
    end.

find_higher(_Curr, _LastSeen, _I, D) when D =< 0 -> not_found;
find_higher(Curr, _LastSeen, _I, D) when D =< Curr -> not_found;
find_higher(Curr, LastSeen, I, D) ->
    case maps:find(D, LastSeen) of
        {ok, J} when J > I -> {J};
        _ -> find_higher(Curr, LastSeen, I, D - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_swap(num :: integer) :: integer
  def maximum_swap(num) do
    digits = Integer.to_string(num) |> String.graphemes()

    last_pos =
      Enum.reduce(Enum.with_index(digits), :array.new(10, default: -1), fn {ch, idx}, acc ->
        digit = String.to_integer(ch)
        :array.set(digit, idx, acc)
      end)

    {final_digits, swapped} =
      Enum.with_index(digits)
      |> Enum.reduce_while({digits, false}, fn {ch, i}, {_list, _swapped} = state ->
        d = String.to_integer(ch)

        case find_swap(i, d, last_pos) do
          nil -> {:cont, state}
          j ->
            list = elem(state, 0)
            char_j = Enum.at(list, j)

            new_list =
              list
              |> List.replace_at(i, char_j)
              |> List.replace_at(j, ch)

            {:halt, {new_list, true}}
        end
      end)

    if swapped do
      final_digits |> Enum.join() |> String.to_integer()
    else
      num
    end
  end

  defp find_swap(i, d, last_pos), do: search_larger(9, i, d, last_pos)

  defp search_larger(larger, _i, d, _last_pos) when larger <= d, do: nil

  defp search_larger(larger, i, d, last_pos) do
    idx = :array.get(larger, last_pos)

    if idx > i do
      idx
    else
      search_larger(larger - 1, i, d, last_pos)
    end
  end
end
```
