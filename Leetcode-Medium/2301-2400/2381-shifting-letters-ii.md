# 2381. Shifting Letters II

## Cpp

```cpp
class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int n = s.size();
        vector<int> diff(n, 0);
        for (const auto& sh : shifts) {
            int start = sh[0];
            int end = sh[1];
            int dir = sh[2];
            int delta = dir ? 1 : -1;
            diff[start] += delta;
            if (end + 1 < n) diff[end + 1] -= delta;
        }
        string res(s);
        int cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            cur %= 26;
            if (cur < 0) cur += 26;
            int orig = s[i] - 'a';
            int shifted = (orig + cur) % 26;
            res[i] = char('a' + shifted);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int n = s.length();
        int[] diff = new int[n + 1];
        for (int[] sh : shifts) {
            int start = sh[0];
            int end = sh[1];
            int dir = sh[2];
            if (dir == 1) { // forward
                diff[start] += 1;
                diff[end + 1] -= 1;
            } else { // backward
                diff[start] -= 1;
                diff[end + 1] += 1;
            }
        }
        StringBuilder sb = new StringBuilder(n);
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            cur %= 26;
            if (cur < 0) cur += 26;
            char c = s.charAt(i);
            int shifted = (c - 'a' + cur) % 26;
            sb.append((char) ('a' + shifted));
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        diff = [0] * (n + 1)  # extra slot to avoid bounds check
        
        for start, end, direction in shifts:
            if direction == 1:          # forward shift
                diff[start] += 1
                diff[end + 1] -= 1
            else:                       # backward shift
                diff[start] -= 1
                diff[end + 1] += 1
        
        res = []
        cur = 0
        for i, ch in enumerate(s):
            cur = (cur + diff[i]) % 26   # cumulative shifts modulo 26
            new_char = chr((ord(ch) - ord('a') + cur) % 26 + ord('a'))
            res.append(new_char)
        
        return ''.join(res)
```

## Python3

```python
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  # extra slot to avoid bounds check
        
        for start, end, direction in shifts:
            if direction == 1:  # forward
                diff[start] += 1
                diff[end + 1] -= 1
            else:               # backward
                diff[start] -= 1
                diff[end + 1] += 1
        
        res = []
        cur = 0
        for i in range(n):
            cur += diff[i]
            shift = cur % 26
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)
        
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* shiftingLetters(char* s, int** shifts, int shiftsSize, int* shiftsColSize) {
    int n = strlen(s);
    int *diff = (int *)calloc(n, sizeof(int));
    
    for (int i = 0; i < shiftsSize; ++i) {
        int start = shifts[i][0];
        int end   = shifts[i][1];
        int dir   = shifts[i][2];
        if (dir == 1) { // forward
            diff[start] += 1;
            if (end + 1 < n) diff[end + 1] -= 1;
        } else { // backward
            diff[start] -= 1;
            if (end + 1 < n) diff[end + 1] += 1;
        }
    }
    
    char *res = (char *)malloc((n + 1) * sizeof(char));
    int cur = 0;
    for (int i = 0; i < n; ++i) {
        cur += diff[i];
        int shift = ((cur % 26) + 26) % 26;
        int orig = s[i] - 'a';
        res[i] = 'a' + (orig + shift) % 26;
    }
    res[n] = '\0';
    
    free(diff);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ShiftingLetters(string s, int[][] shifts) {
        int n = s.Length;
        int[] diff = new int[n];
        foreach (var sh in shifts) {
            int start = sh[0];
            int end = sh[1];
            int dir = sh[2];
            int delta = dir == 1 ? 1 : -1;
            diff[start] += delta;
            if (end + 1 < n) diff[end + 1] -= delta;
        }
        char[] result = new char[n];
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            int shift = cur % 26;
            if (shift < 0) shift += 26;
            int orig = s[i] - 'a';
            int newIdx = (orig + shift) % 26;
            result[i] = (char)('a' + newIdx);
        }
        return new string(result);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    const n = s.length;
    const diff = new Array(n).fill(0);
    
    for (const [start, end, dir] of shifts) {
        const delta = dir === 1 ? 1 : -1;
        diff[start] += delta;
        if (end + 1 < n) diff[end + 1] -= delta;
    }
    
    const result = [];
    let cur = 0;
    for (let i = 0; i < n; ++i) {
        cur += diff[i];
        const shift = ((cur % 26) + 26) % 26;
        const orig = s.charCodeAt(i) - 97;
        const newChar = String.fromCharCode(97 + (orig + shift) % 26);
        result.push(newChar);
    }
    
    return result.join('');
};
```

## Typescript

```typescript
function shiftingLetters(s: string, shifts: number[][]): string {
    const n = s.length;
    const diff = new Int32Array(n + 1);
    for (const [start, end, dir] of shifts) {
        if (dir === 1) {
            diff[start] += 1;
            diff[end + 1] -= 1;
        } else {
            diff[start] -= 1;
            diff[end + 1] += 1;
        }
    }
    let cur = 0;
    const result: string[] = new Array(n);
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        const shift = ((cur % 26) + 26) % 26;
        const orig = s.charCodeAt(i) - 97;
        const newChar = String.fromCharCode(97 + (orig + shift) % 26);
        result[i] = newChar;
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $shifts
     * @return String
     */
    function shiftingLetters($s, $shifts) {
        $n = strlen($s);
        // difference array of size n+1 to avoid bounds checks
        $diff = array_fill(0, $n + 1, 0);

        foreach ($shifts as $shift) {
            [$start, $end, $dir] = $shift;
            if ($dir == 1) { // forward
                $diff[$start] += 1;
                $diff[$end + 1] -= 1;
            } else { // backward
                $diff[$start] -= 1;
                $diff[$end + 1] += 1;
            }
        }

        $result = '';
        $curr = 0;
        for ($i = 0; $i < $n; ++$i) {
            $curr += $diff[$i];
            // normalize shift to [0,25]
            $shiftVal = $curr % 26;
            if ($shiftVal < 0) {
                $shiftVal += 26;
            }
            $origIdx = ord($s[$i]) - ord('a');
            $newIdx = ($origIdx + $shiftVal) % 26;
            $result .= chr(ord('a') + $newIdx);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func shiftingLetters(_ s: String, _ shifts: [[Int]]) -> String {
        let sBytes = Array(s.utf8)
        let n = sBytes.count
        var diff = [Int](repeating: 0, count: n + 1)
        
        for shift in shifts {
            let start = shift[0]
            let end = shift[1]
            let dir = shift[2]
            if dir == 1 {
                diff[start] += 1
                if end + 1 < n { diff[end + 1] -= 1 }
            } else {
                diff[start] -= 1
                if end + 1 < n { diff[end + 1] += 1 }
            }
        }
        
        var result = [UInt8]()
        result.reserveCapacity(n)
        var cur = 0
        
        for i in 0..<n {
            cur += diff[i]
            var shiftVal = cur % 26
            if shiftVal < 0 { shiftVal += 26 }
            let original = Int(sBytes[i]) - 97
            let newChar = UInt8((original + shiftVal) % 26 + 97)
            result.append(newChar)
        }
        
        return String(bytes: result, encoding: .utf8)!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shiftingLetters(s: String, shifts: Array<IntArray>): String {
        val n = s.length
        val diff = IntArray(n + 1)
        for (sh in shifts) {
            val start = sh[0]
            val end = sh[1]
            val dir = sh[2]
            if (dir == 1) {
                diff[start] += 1
                if (end + 1 < n) diff[end + 1] -= 1
            } else {
                diff[start] -= 1
                if (end + 1 < n) diff[end + 1] += 1
            }
        }
        val result = CharArray(n)
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            var shift = cur % 26
            if (shift < 0) shift += 26
            val orig = s[i] - 'a'
            val newChar = ((orig + shift) % 26 + 'a'.code).toChar()
            result[i] = newChar
        }
        return String(result)
    }
}
```

## Dart

```dart
class Solution {
  String shiftingLetters(String s, List<List<int>> shifts) {
    int n = s.length;
    List<int> diff = List.filled(n + 1, 0);
    for (var shift in shifts) {
      int start = shift[0];
      int end = shift[1];
      int dir = shift[2];
      if (dir == 1) {
        diff[start] += 1;
        if (end + 1 < n) diff[end + 1] -= 1;
      } else {
        diff[start] -= 1;
        if (end + 1 < n) diff[end + 1] += 1;
      }
    }

    StringBuffer sb = StringBuffer();
    int cur = 0;
    for (int i = 0; i < n; i++) {
      cur = (cur + diff[i]) % 26;
      if (cur < 0) cur += 26;
      int original = s.codeUnitAt(i) - 97;
      int shifted = (original + cur) % 26;
      sb.writeCharCode(shifted + 97);
    }
    return sb.toString();
  }
}
```

## Golang

```go
func shiftingLetters(s string, shifts [][]int) string {
	n := len(s)
	if n == 0 {
		return ""
	}
	diff := make([]int, n+1)

	for _, sh := range shifts {
		start, end, dir := sh[0], sh[1], sh[2]
		if dir == 1 { // forward
			diff[start]++
			if end+1 < n {
				diff[end+1]--
			}
		} else { // backward
			diff[start]--
			if end+1 < n {
				diff[end+1]++
			}
		}
	}

	res := make([]byte, n)
	cur := 0
	for i := 0; i < n; i++ {
		cur += diff[i]
		shift := cur % 26
		if shift < 0 {
			shift += 26
		}
		newChar := (int(s[i]-'a') + shift) % 26
		res[i] = byte('a' + newChar)
	}
	return string(res)
}
```

## Ruby

```ruby
def shifting_letters(s, shifts)
  n = s.length
  diff = Array.new(n, 0)

  shifts.each do |start_i, end_i, direction|
    if direction == 1
      diff[start_i] += 1
      diff[end_i + 1] -= 1 if end_i + 1 < n
    else
      diff[start_i] -= 1
      diff[end_i + 1] += 1 if end_i + 1 < n
    end
  end

  cur = 0
  result_bytes = []

  s.each_byte.with_index do |c, i|
    cur = (cur + diff[i]) % 26
    new_c = ((c - 97 + cur) % 26) + 97
    result_bytes << new_c
  end

  result_bytes.pack('C*')
end
```

## Scala

```scala
object Solution {
    def shiftingLetters(s: String, shifts: Array[Array[Int]]): String = {
        val n = s.length
        val diff = new Array[Int](n + 1)
        var i = 0
        while (i < shifts.length) {
            val arr = shifts(i)
            val start = arr(0)
            val end = arr(1)
            val dir = arr(2)
            if (dir == 1) {
                diff(start) += 1
                if (end + 1 < n) diff(end + 1) -= 1
            } else {
                diff(start) -= 1
                if (end + 1 < n) diff(end + 1) += 1
            }
            i += 1
        }
        val sb = new StringBuilder(n)
        var cum = 0
        var idx = 0
        while (idx < n) {
            cum += diff(idx)
            var shift = cum % 26
            if (shift < 0) shift += 26
            val ch = ((s.charAt(idx) - 'a' + shift) % 26 + 'a').toChar
            sb.append(ch)
            idx += 1
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shifting_letters(s: String, shifts: Vec<Vec<i32>>) -> String {
        let n = s.len();
        let mut diff = vec![0i32; n + 1];
        for sh in shifts.iter() {
            let start = sh[0] as usize;
            let end = sh[1] as usize;
            if sh[2] == 1 {
                diff[start] += 1;
                diff[end + 1] -= 1;
            } else {
                diff[start] -= 1;
                diff[end + 1] += 1;
            }
        }
        let bytes = s.as_bytes();
        let mut result = String::with_capacity(n);
        let mut cur = 0i32;
        for i in 0..n {
            cur += diff[i];
            let mut shift = cur % 26;
            if shift < 0 {
                shift += 26;
            }
            let orig = (bytes[i] - b'a') as i32;
            let new_char = ((orig + shift) % 26) as u8 + b'a';
            result.push(new_char as char);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (shifting-letters s shifts)
  (-> string? (listof (listof exact-integer?)) string?)
  (let* ([n (string-length s)]
         [diff (make-vector n 0)])
    ;; Apply difference updates
    (for ([triple shifts])
      (match triple
        [(list start end dir)
         (cond
           [(= dir 1) ; forward shift
            (vector-set! diff start (+ 1 (vector-ref diff start)))
            (when (< (+ end 1) n)
              (vector-set! diff (+ end 1) (- (vector-ref diff (+ end 1)) 1)))]
           [else       ; backward shift (dir = 0)
            (vector-set! diff start (- (vector-ref diff start) 1))
            (when (< (+ end 1) n)
              (vector-set! diff (+ end 1) (+ (vector-ref diff (+ end 1)) 1)))])]))
    ;; Build the final string
    (let ([result (make-string n)]
          [cur 0])
      (for ([i (in-range n)])
        (set! cur (modulo (+ cur (vector-ref diff i)) 26))
        (define ch (string-ref s i))
        (define base (char->integer #\a))
        (define offset (- (char->integer ch) base))
        (define newoffset (modulo (+ offset cur) 26))
        (string-set! result i (integer->char (+ base newoffset))))
      result)))
```

## Erlang

```erlang
-spec shifting_letters(S :: unicode:unicode_binary(), Shifts :: [[integer()]]) -> unicode:unicode_binary().
shifting_letters(S, Shifts) ->
    N = byte_size(S),
    Diff0 = array:new(N + 1, {default, 0}),
    Diff = lists:foldl(
        fun([Start, End, Dir], Acc) ->
            case Dir of
                1 ->
                    A1 = update(Acc, Start, 1),
                    if End + 1 < N -> update(A1, End + 1, -1); true -> A1 end;
                0 ->
                    A1 = update(Acc, Start, -1),
                    if End + 1 < N -> update(A1, End + 1, 1); true -> A1 end
            end
        end,
        Diff0,
        Shifts
    ),
    ResultChars = build(N, 0, 0, Diff, S, []),
    iolist_to_binary(ResultChars).

-spec update(array:array(integer()), integer(), integer()) -> array:array(integer()).
update(Array, Index, Delta) ->
    Old = array:get(Index, Array),
    array:set(Index, Old + Delta, Array).

-spec build(non_neg_integer(), non_neg_integer(), integer(), array:array(integer()), binary(), [integer()]) -> iolist().
build(N, I, ShiftAcc, Diff, S, Acc) when I == N ->
    lists:reverse(Acc);
build(N, I, ShiftAcc, Diff, S, Acc) ->
    Delta = array:get(I, Diff),
    NewShift0 = (ShiftAcc + Delta) rem 26,
    NewShift = if NewShift0 < 0 -> NewShift0 + 26; true -> NewShift0 end,
    CharCode = binary:at(S, I),
    Shifted = ((CharCode - $a + NewShift) rem 26) + $a,
    build(N, I + 1, NewShift, Diff, S, [Shifted | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec shifting_letters(s :: String.t(), shifts :: [[integer]]) :: String.t()
  def shifting_letters(s, shifts) do
    n = String.length(s)

    diff =
      Enum.reduce(shifts, :array.new(n, default: 0), fn [l, r, d], acc ->
        inc = if d == 1, do: 1, else: -1
        acc = :array.set(l, (:array.get(l, acc) + inc), acc)

        if r + 1 < n do
          acc = :array.set(r + 1, (:array.get(r + 1, acc) - inc), acc)
        end

        acc
      end)

    chars = String.to_charlist(s)

    {rev_res, _} =
      Enum.reduce(Enum.with_index(chars), {[], 0}, fn {c, i}, {out, cur} ->
        cur = cur + :array.get(i, diff)
        shift_mod = rem(cur, 26)
        shift_mod = if shift_mod < 0, do: shift_mod + 26, else: shift_mod
        new_c = ?a + rem(c - ?a + shift_mod, 26)
        {[new_c | out], cur}
      end)

    rev_res |> Enum.reverse() |> List.to_string()
  end
end
```
