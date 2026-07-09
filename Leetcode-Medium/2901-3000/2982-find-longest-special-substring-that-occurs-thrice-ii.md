# 2982. Find Longest Special Substring That Occurs Thrice II

## Cpp

```cpp
class Solution {
public:
    int maximumLength(string s) {
        array<array<int,3>,26> top;
        for (auto &arr : top) arr = {0,0,0};
        int curLen = 0;
        char prev = 0;
        for (char ch : s) {
            if (ch == prev) ++curLen;
            else {
                curLen = 1;
                prev = ch;
            }
            int idx = ch - 'a';
            auto &t = top[idx];
            if (curLen > t[0]) {
                t[2] = t[1];
                t[1] = t[0];
                t[0] = curLen;
            } else if (curLen > t[1]) {
                t[2] = t[1];
                t[1] = curLen;
            } else if (curLen > t[2]) {
                t[2] = curLen;
            }
        }
        int ans = 0;
        for (int i = 0; i < 26; ++i) ans = max(ans, top[i][2]);
        return ans == 0 ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumLength(String s) {
        int n = s.length();
        int[][] top = new int[26][3]; // descending order: top[c][0] >= top[c][1] >= top[c][2]
        int curLen = 0;
        char prev = '#';
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == prev) {
                curLen++;
            } else {
                curLen = 1;
                prev = ch;
            }
            int idx = ch - 'a';
            if (curLen > top[idx][0]) {
                top[idx][2] = top[idx][1];
                top[idx][1] = top[idx][0];
                top[idx][0] = curLen;
            } else if (curLen > top[idx][1]) {
                top[idx][2] = top[idx][1];
                top[idx][1] = curLen;
            } else if (curLen > top[idx][2]) {
                top[idx][2] = curLen;
            }
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            ans = Math.max(ans, top[i][2]);
        }
        return ans == 0 ? -1 : ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # top three lengths for each character (largest, second, third)
        top = [[0, 0, 0] for _ in range(26)]
        prev_char = ''
        cur_len = 0

        for ch in s:
            if ch == prev_char:
                cur_len += 1
            else:
                cur_len = 1
                prev_char = ch

            idx = ord(ch) - 97
            a, b, c = top[idx]
            if cur_len >= a:
                c = b
                b = a
                a = cur_len
            elif cur_len >= b:
                c = b
                b = cur_len
            elif cur_len > c:
                c = cur_len
            top[idx] = [a, b, c]

        ans = 0
        for a, b, c in top:
            if c > ans:
                ans = c

        return ans if ans > 0 else -1
```

## Python3

```python
class Solution:
    def maximumLength(self, s: str) -> int:
        top = [[0, 0, 0] for _ in range(26)]  # largest, second, third
        prev_char = ''
        cur_len = 0
        for ch in s:
            if ch == prev_char:
                cur_len += 1
            else:
                cur_len = 1
                prev_char = ch
            idx = ord(ch) - 97
            a, b, c = top[idx]
            if cur_len > a:
                top[idx] = [cur_len, a, b]
            elif cur_len > b:
                top[idx][1] = cur_len
                top[idx][2] = b
            elif cur_len > c:
                top[idx][2] = cur_len
        ans = max(arr[2] for arr in top)
        return ans if ans > 0 else -1
```

## C

```c
#include <stddef.h>

int maximumLength(char* s) {
    if (!s) return -1;
    int top[26][3] = {0}; // top[i][0]>=top[i][1]>=top[i][2]
    int curLen = 0;
    char prev = 0;
    for (size_t i = 0; s[i]; ++i) {
        char c = s[i];
        if (i > 0 && c == prev) {
            curLen++;
        } else {
            curLen = 1;
        }
        int idx = c - 'a';
        // insert curLen into top[idx] maintaining descending order
        if (curLen > top[idx][0]) {
            top[idx][2] = top[idx][1];
            top[idx][1] = top[idx][0];
            top[idx][0] = curLen;
        } else if (curLen > top[idx][1]) {
            top[idx][2] = top[idx][1];
            top[idx][1] = curLen;
        } else if (curLen > top[idx][2]) {
            top[idx][2] = curLen;
        }
        prev = c;
    }
    int ans = 0;
    for (int i = 0; i < 26; ++i) {
        if (top[i][2] > ans) ans = top[i][2];
    }
    return ans == 0 ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumLength(string s) {
        int[][] top = new int[26][];
        for (int i = 0; i < 26; i++) top[i] = new int[3]; // initialized to 0

        int curLen = 0;
        char prevChar = '#';

        foreach (char ch in s) {
            if (ch == prevChar) {
                curLen++;
            } else {
                curLen = 1;
                prevChar = ch;
            }

            int idx = ch - 'a';
            int[] t = top[idx];

            if (curLen > t[0]) {
                t[2] = t[1];
                t[1] = t[0];
                t[0] = curLen;
            } else if (curLen > t[1]) {
                t[2] = t[1];
                t[1] = curLen;
            } else if (curLen > t[2]) {
                t[2] = curLen;
            }
        }

        int ans = 0;
        for (int i = 0; i < 26; i++) {
            ans = Math.Max(ans, top[i][2]);
        }

        return ans == 0 ? -1 : ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maximumLength = function(s) {
    const tops = Array.from({length: 26}, () => [0, 0, 0]); // [max, second, third]
    let curLen = 0;
    for (let i = 0; i < s.length; ++i) {
        if (i > 0 && s[i] === s[i - 1]) {
            curLen += 1;
        } else {
            curLen = 1;
        }
        const idx = s.charCodeAt(i) - 97;
        const arr = tops[idx];
        if (curLen > arr[0]) {
            arr[2] = arr[1];
            arr[1] = arr[0];
            arr[0] = curLen;
        } else if (curLen > arr[1]) {
            arr[2] = arr[1];
            arr[1] = curLen;
        } else if (curLen > arr[2]) {
            arr[2] = curLen;
        }
    }
    let ans = -1;
    for (let i = 0; i < 26; ++i) {
        const third = tops[i][2];
        if (third > ans) ans = third;
    }
    return ans > 0 ? ans : -1;
};
```

## Typescript

```typescript
function maximumLength(s: string): number {
    const tops = Array.from({ length: 26 }, () => [0, 0, 0]); // max1, max2, max3
    let curLen = 0;
    for (let i = 0; i < s.length; i++) {
        if (i > 0 && s.charCodeAt(i) === s.charCodeAt(i - 1)) {
            curLen++;
        } else {
            curLen = 1;
        }
        const idx = s.charCodeAt(i) - 97;
        const arr = tops[idx];
        if (curLen > arr[0]) {
            arr[2] = arr[1];
            arr[1] = arr[0];
            arr[0] = curLen;
        } else if (curLen > arr[1]) {
            arr[2] = arr[1];
            arr[1] = curLen;
        } else if (curLen > arr[2]) {
            arr[2] = curLen;
        }
    }
    let ans = -1;
    for (let i = 0; i < 26; i++) {
        const third = tops[i][2];
        if (third > ans) ans = third;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maximumLength($s) {
        $n = strlen($s);
        // top three lengths for each character, descending order
        $top = array_fill(0, 26, [0, 0, 0]);
        $prevChar = '';
        $curLen = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === $prevChar) {
                $curLen++;
            } else {
                $curLen = 1;
                $prevChar = $c;
            }
            $idx = ord($c) - 97;
            $a = $top[$idx];
            if ($curLen > $a[0]) {
                $a[2] = $a[1];
                $a[1] = $a[0];
                $a[0] = $curLen;
            } elseif ($curLen > $a[1]) {
                $a[2] = $a[1];
                $a[1] = $curLen;
            } elseif ($curLen > $a[2]) {
                $a[2] = $curLen;
            }
            $top[$idx] = $a;
        }
        $ans = -1;
        for ($i = 0; $i < 26; $i++) {
            if ($top[$i][2] > 0) {
                $ans = max($ans, $top[$i][2]);
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumLength(_ s: String) -> Int {
        let chars = Array(s)
        var top = Array(repeating: [Int](repeating: 0, count: 3), count: 26)
        var curLen = 0
        for i in 0..<chars.count {
            if i > 0 && chars[i] == chars[i - 1] {
                curLen += 1
            } else {
                curLen = 1
            }
            let idx = Int(chars[i].unicodeScalars.first!.value - 97)
            var arr = top[idx]
            if curLen > arr[0] {
                arr[2] = arr[1]
                arr[1] = arr[0]
                arr[0] = curLen
            } else if curLen > arr[1] {
                arr[2] = arr[1]
                arr[1] = curLen
            } else if curLen > arr[2] {
                arr[2] = curLen
            }
            top[idx] = arr
        }
        var ans = -1
        for i in 0..<26 {
            let third = top[i][2]
            if third > 0 {
                ans = max(ans, third)
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLength(s: String): Int {
        val top = Array(26) { IntArray(3) }
        var curLen = 0
        for (i in s.indices) {
            if (i > 0 && s[i] == s[i - 1]) {
                curLen++
            } else {
                curLen = 1
            }
            val idx = s[i] - 'a'
            val arr = top[idx]
            when {
                curLen > arr[0] -> {
                    arr[2] = arr[1]
                    arr[1] = arr[0]
                    arr[0] = curLen
                }
                curLen > arr[1] -> {
                    arr[2] = arr[1]
                    arr[1] = curLen
                }
                curLen > arr[2] -> {
                    arr[2] = curLen
                }
            }
        }
        var ans = -1
        for (i in 0 until 26) {
            val third = top[i][2]
            if (third > 0 && third > ans) ans = third
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumLength(String s) {
    // top[char][0] = largest, [1] = second, [2] = third
    List<List<int>> top = List.generate(26, (_) => [0, 0, 0]);
    int curLen = 0;
    for (int i = 0; i < s.length; ++i) {
      if (i > 0 && s.codeUnitAt(i) == s.codeUnitAt(i - 1)) {
        curLen += 1;
      } else {
        curLen = 1;
      }
      int idx = s.codeUnitAt(i) - 97; // 'a' -> 0
      List<int> arr = top[idx];
      if (curLen > arr[0]) {
        arr[2] = arr[1];
        arr[1] = arr[0];
        arr[0] = curLen;
      } else if (curLen > arr[1]) {
        arr[2] = arr[1];
        arr[1] = curLen;
      } else if (curLen > arr[2]) {
        arr[2] = curLen;
      }
    }

    int ans = -1;
    for (var arr in top) {
      if (arr[2] > 0 && arr[2] > ans) {
        ans = arr[2];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maximumLength(s string) int {
    const K = 3
    var tops [26][K]int // descending order: tops[0] >= tops[1] >= tops[2]
    curLen := 0
    n := len(s)
    for i := 0; i < n; i++ {
        if i > 0 && s[i] == s[i-1] {
            curLen++
        } else {
            curLen = 1
        }
        idx := s[i] - 'a'
        a := &tops[idx]
        if curLen > a[0] {
            a[2] = a[1]
            a[1] = a[0]
            a[0] = curLen
        } else if curLen > a[1] {
            a[2] = a[1]
            a[1] = curLen
        } else if curLen > a[2] {
            a[2] = curLen
        }
    }
    ans := -1
    for _, arr := range tops {
        if arr[2] > 0 && arr[2] > ans {
            ans = arr[2]
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_length(s)
  top = Array.new(26) { [0, 0, 0] } # store three largest lengths for each character
  cur_len = 0
  prev_char = nil

  s.each_char do |ch|
    if ch == prev_char
      cur_len += 1
    else
      cur_len = 1
      prev_char = ch
    end

    idx = ch.ord - 97
    a, b, c = top[idx]

    if cur_len > a
      top[idx][2] = b
      top[idx][1] = a
      top[idx][0] = cur_len
    elsif cur_len > b
      top[idx][2] = b
      top[idx][1] = cur_len
    elsif cur_len > c
      top[idx][2] = cur_len
    end
  end

  ans = -1
  top.each do |arr|
    ans = [ans, arr[2]].max if arr[2] > 0
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maximumLength(s: String): Int = {
        val top = Array.ofDim[Int](26, 3) // top(c)(0)=max, (1)=second, (2)=third
        var i = 0
        val n = s.length
        while (i < n) {
            val chIdx = s.charAt(i) - 'a'
            var j = i
            while (j < n && s.charAt(j) == s.charAt(i)) j += 1
            val len = j - i
            if (len > top(chIdx)(0)) {
                top(chIdx)(2) = top(chIdx)(1)
                top(chIdx)(1) = top(chIdx)(0)
                top(chIdx)(0) = len
            } else if (len > top(chIdx)(1)) {
                top(chIdx)(2) = top(chIdx)(1)
                top(chIdx)(1) = len
            } else if (len > top(chIdx)(2)) {
                top(chIdx)(2) = len
            }
            i = j
        }
        var ans = -1
        for (c <- 0 until 26) {
            val third = top(c)(2)
            if (third > 0 && third > ans) ans = third
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_length(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut tops = [[0i32; 3]; 26];
        let mut prev: u8 = 0;
        let mut cur_len: i32 = 0;

        for (i, &b) in bytes.iter().enumerate() {
            if i > 0 && b == prev {
                cur_len += 1;
            } else {
                cur_len = 1;
            }
            prev = b;
            let idx = (b - b'a') as usize;
            let arr = &mut tops[idx];
            if cur_len > arr[0] {
                arr[2] = arr[1];
                arr[1] = arr[0];
                arr[0] = cur_len;
            } else if cur_len > arr[1] {
                arr[2] = arr[1];
                arr[1] = cur_len;
            } else if cur_len > arr[2] {
                arr[2] = cur_len;
            }
        }

        let mut ans = 0i32;
        for arr in tops.iter() {
            if arr[2] > ans {
                ans = arr[2];
            }
        }
        if ans == 0 { -1 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (maximum-length s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (topVec (make-vector 26)))
    ;; initialize each entry to a vector of three zeros
    (for ([i (in-range 26)])
      (vector-set! topVec i (vector 0 0 0)))
    (let loop ((i 0) (prev #\space) (run 0))
      (if (= i n)
          (let ((ans -1))
            (for ([idx (in-range 26)])
              (let* ((vec (vector-ref topVec idx))
                     (third (vector-ref vec 2)))
                (when (> third 0)
                  (set! ans (max ans third)))))
            ans)
          (let* ((c (string-ref s i))
                 (new-run (if (char=? c prev) (+ run 1) 1))
                 (idx (- (char->integer c) (char->integer #\a)))
                 (vec (vector-ref topVec idx))
                 (a (vector-ref vec 0))
                 (b (vector-ref vec 1))
                 (c3 (vector-ref vec 2)))
            (cond
              [(> new-run a)
               (vector-set! vec 2 b)
               (vector-set! vec 1 a)
               (vector-set! vec 0 new-run)]
              [(> new-run b)
               (vector-set! vec 2 b)
               (vector-set! vec 1 new-run)]
              [(> new-run c3)
               (vector-set! vec 2 new-run)])
            (loop (+ i 1) c new-run))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_length/1]).

-spec maximum_length(S :: unicode:unicode_binary()) -> integer().
maximum_length(S) ->
    List = binary_to_list(S),
    EmptyTop = {0,0,0},
    Tops0 = erlang:make_tuple(26, EmptyTop),
    Tops = process(List, -1, 0, Tops0),
    MaxThird = max_third(Tops, 1),
    case MaxThird of
        0 -> -1;
        V -> V
    end.

process([], _Prev, _CurLen, Tops) ->
    Tops;
process([C|Rest], Prev, CurLen, Tops) ->
    NewCur = if C == Prev -> CurLen + 1; true -> 1 end,
    CharIdx = C - $a,
    OldTop = element(CharIdx+1, Tops),
    NewTop = insert_top(OldTop, NewCur),
    NewTops = setelement(CharIdx+1, Tops, NewTop),
    process(Rest, C, NewCur, NewTops).

insert_top({A,B,C}, L) ->
    if
        L >= A -> {L,A,B};
        L >= B -> {A,L,B};
        L >= C -> {A,B,L};
        true   -> {A,B,C}
    end.

max_third(Tuple, Index) when Index > 26 ->
    0;
max_third(Tuple, Index) ->
    {_,_,C} = element(Index, Tuple),
    Rest = max_third(Tuple, Index+1),
    if C > Rest -> C; true -> Rest end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length(s :: String.t()) :: integer
  def maximum_length(s) do
    bytes = :binary.bin_to_list(s)

    {top_map, _prev_char, _cur_len} =
      Enum.reduce(bytes, {%{}, nil, 0}, fn byte, {map, prev, len} ->
        new_len = if byte == prev, do: len + 1, else: 1
        idx = byte - ?a

        {max1, max2, max3} = Map.get(map, idx, {0, 0, 0})

        {new_max1, new_max2, new_max3} =
          cond do
            new_len > max1 -> {new_len, max1, max2}
            new_len > max2 -> {max1, new_len, max2}
            new_len > max3 -> {max1, max2, new_len}
            true -> {max1, max2, max3}
          end

        new_map = Map.put(map, idx, {new_max1, new_max2, new_max3})
        {new_map, byte, new_len}
      end)

    ans =
      top_map
      |> Map.values()
      |> Enum.reduce(0, fn {_a, _b, c}, acc -> if c > acc, do: c, else: acc end)

    if ans == 0, do: -1, else: ans
  end
end
```
