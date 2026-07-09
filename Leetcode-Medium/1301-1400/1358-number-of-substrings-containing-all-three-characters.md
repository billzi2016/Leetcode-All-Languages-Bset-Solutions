# 1358. Number of Substrings Containing All Three Characters

## Cpp

```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        int last[3] = {-1, -1, -1};
        long long total = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            int idx = s[i] - 'a'; // 'a'->0, 'b'->1, 'c'->2
            last[idx] = i;
            int minPos = min({last[0], last[1], last[2]});
            if (minPos != -1) {
                total += minPos + 1;
            }
        }
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    public int numberOfSubstrings(String s) {
        int[] last = new int[3];
        for (int i = 0; i < 3; i++) last[i] = -1;
        long total = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            last[ch - 'a'] = i;
            int minPos = Math.min(last[0], Math.min(last[1], last[2]));
            if (minPos != -1) {
                total += (long) minPos + 1;
            }
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1, -1, -1]  # positions of 'a', 'b', 'c'
        total = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            last[idx] = i
            min_last = min(last)
            if min_last != -1:
                total += min_last + 1
        return total
```

## Python3

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]  # positions of 'a', 'b', 'c'
        total = 0
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
            m = min(last)
            if m != -1:
                total += m + 1
        return total
```

## C

```c
#include <stddef.h>

int numberOfSubstrings(char* s) {
    int last[3] = { -1, -1, -1 };
    long long total = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        int idx = s[i] - 'a';          // 'a'->0, 'b'->1, 'c'->2
        if (idx >= 0 && idx < 3)
            last[idx] = i;
        int minPos = last[0];
        if (last[1] < minPos) minPos = last[1];
        if (last[2] < minPos) minPos = last[2];
        if (minPos != -1)
            total += (long long)(minPos + 1);
    }
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfSubstrings(string s) {
        int[] last = new int[3] { -1, -1, -1 };
        long total = 0;
        for (int i = 0; i < s.Length; i++) {
            char ch = s[i];
            if (ch == 'a') last[0] = i;
            else if (ch == 'b') last[1] = i;
            else if (ch == 'c') last[2] = i;

            int minPos = Math.Min(last[0], Math.Min(last[1], last[2]));
            if (minPos != -1) {
                total += minPos + 1;
            }
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const last = [-1, -1, -1]; // positions of 'a', 'b', 'c'
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - 97; // map 'a'->0, 'b'->1, 'c'->2
        last[idx] = i;
        const minPos = Math.min(last[0], last[1], last[2]);
        if (minPos !== -1) {
            total += minPos + 1;
        }
    }
    return total;
};
```

## Typescript

```typescript
function numberOfSubstrings(s: string): number {
    const last = [-1, -1, -1]; // positions of 'a', 'b', 'c'
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s.charCodeAt(i) - 97; // 'a' -> 0, 'b' -> 1, 'c' -> 2
        last[ch] = i;
        const minPos = Math.min(last[0], last[1], last[2]);
        if (minPos !== -1) {
            total += minPos + 1;
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $lastPos = [-1, -1, -1]; // a, b, c
        $total = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch === 'a') {
                $lastPos[0] = $i;
            } elseif ($ch === 'b') {
                $lastPos[1] = $i;
            } else { // 'c'
                $lastPos[2] = $i;
            }
            $minPos = min($lastPos);
            if ($minPos != -1) {
                $total += $minPos + 1;
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        var last = [-1, -1, -1]   // positions of 'a', 'b', 'c'
        var total = 0
        for (i, ch) in s.enumerated() {
            switch ch {
            case "a":
                last[0] = i
            case "b":
                last[1] = i
            case "c":
                last[2] = i
            default:
                break
            }
            let minPos = min(last[0], min(last[1], last[2]))
            if minPos != -1 {
                total += minPos + 1
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSubstrings(s: String): Int {
        var lastA = -1
        var lastB = -1
        var lastC = -1
        var total = 0L
        for (i in s.indices) {
            when (s[i]) {
                'a' -> lastA = i
                'b' -> lastB = i
                'c' -> lastC = i
            }
            val minPos = kotlin.math.min(lastA, kotlin.math.min(lastB, lastC))
            if (minPos != -1) {
                total += (minPos + 1)
            }
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSubstrings(String s) {
    List<int> last = [-1, -1, -1];
    int total = 0;
    for (int i = 0; i < s.length; ++i) {
      int idx;
      switch (s[i]) {
        case 'a':
          idx = 0;
          break;
        case 'b':
          idx = 1;
          break;
        default:
          idx = 2; // 'c'
      }
      last[idx] = i;
      int minPos = last[0];
      if (last[1] < minPos) minPos = last[1];
      if (last[2] < minPos) minPos = last[2];
      if (minPos != -1) {
        total += minPos + 1;
      }
    }
    return total;
  }
}
```

## Golang

```go
func numberOfSubstrings(s string) int {
    last := [3]int{-1, -1, -1}
    total := 0
    for i, ch := range s {
        switch ch {
        case 'a':
            last[0] = i
        case 'b':
            last[1] = i
        case 'c':
            last[2] = i
        }
        minPos := last[0]
        if last[1] < minPos {
            minPos = last[1]
        }
        if last[2] < minPos {
            minPos = last[2]
        }
        if minPos != -1 {
            total += minPos + 1
        }
    }
    return total
}
```

## Ruby

```ruby
def number_of_substrings(s)
  last = [-1, -1, -1]
  total = 0
  s.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    last[idx] = i
    min_last = [last[0], last[1], last[2]].min
    total += min_last + 1 if min_last != -1
  end
  total
end
```

## Scala

```scala
object Solution {
    def numberOfSubstrings(s: String): Int = {
        val last = Array.fill(3)(-1)
        var total: Long = 0L
        for (i <- s.indices) {
            s.charAt(i) match {
                case 'a' => last(0) = i
                case 'b' => last(1) = i
                case 'c' => last(2) = i
                case _   => // do nothing, input guarantees only a,b,c
            }
            val minPos = math.min(last(0), math.min(last(1), last(2)))
            if (minPos != -1) total += minPos + 1
        }
        total.toInt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let mut last = [-1i32; 3];
        let mut total: i64 = 0;
        for (i, ch) in s.bytes().enumerate() {
            let idx = match ch {
                b'a' => 0,
                b'b' => 1,
                b'c' => 2,
                _ => continue,
            };
            last[idx] = i as i32;
            let min_last = *last.iter().min().unwrap();
            if min_last >= 0 {
                total += (min_last + 1) as i64;
            }
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-substrings s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [last-pos (make-vector 3 -1)])
    (let loop ((i 0) (total 0))
      (if (= i n)
          total
          (begin
            (let ([ch (string-ref s i)])
              (cond [(char=? ch #\a) (vector-set! last-pos 0 i)]
                    [(char=? ch #\b) (vector-set! last-pos 1 i)]
                    [(char=? ch #\c) (vector-set! last-pos 2 i)]))
            (let ([min-pos (min (vector-ref last-pos 0)
                                (vector-ref last-pos 1)
                                (vector-ref last-pos 2))])
              (if (>= min-pos 0)
                  (loop (+ i 1) (+ total (+ min-pos 1)))
                  (loop (+ i 1) total))))))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_substrings/1]).

-spec number_of_substrings(unicode:unicode_binary()) -> integer().
number_of_substrings(S) ->
    List = binary_to_list(S),
    loop(0, List, -1, -1, -1, 0).

loop(_Idx, [], _A, _B, _C, Acc) ->
    Acc;
loop(Index, [Char|Rest], APos, BPos, CPos, Acc) ->
    case Char of
        $a -> NewAPos = Index,
               NewBPos = BPos,
               NewCPos = CPos;
        $b -> NewAPos = APos,
               NewBPos = Index,
               NewCPos = CPos;
        $c -> NewAPos = APos,
               NewBPos = BPos,
               NewCPos = Index
    end,
    Min = erlang:min(NewAPos, erlang:min(NewBPos, NewCPos)),
    NewAcc = if Min >= 0 -> Acc + Min + 1; true -> Acc end,
    loop(Index + 1, Rest, NewAPos, NewBPos, NewCPos, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_substrings(s :: String.t()) :: integer
  def number_of_substrings(s) do
    chars = String.to_charlist(s)

    {_a, _b, _c, total, _idx} =
      Enum.reduce(chars, {-1, -1, -1, 0, 0}, fn ch, {a, b, c, total, idx} ->
        {na, nb, nc} =
          case ch do
            ?a -> {idx, b, c}
            ?b -> {a, idx, c}
            ?c -> {a, b, idx}
          end

        min_pos = Enum.min([na, nb, nc])

        new_total = if min_pos >= 0, do: total + min_pos + 1, else: total

        {na, nb, nc, new_total, idx + 1}
      end)

    total
  end
end
```
