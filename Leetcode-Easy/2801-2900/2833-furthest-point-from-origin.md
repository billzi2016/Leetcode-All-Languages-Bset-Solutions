# 2833. Furthest Point From Origin

## Cpp

```cpp
class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int left = 0, right = 0, underscore = 0;
        for (char c : moves) {
            if (c == 'L') ++left;
            else if (c == 'R') ++right;
            else ++underscore; // '_'
        }
        return abs(right - left) + underscore;
    }
};
```

## Java

```java
class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        int left = 0, right = 0, underscore = 0;
        for (char c : moves.toCharArray()) {
            if (c == 'L') left++;
            else if (c == 'R') right++;
            else underscore++; // '_'
        }
        return Math.abs(right - left) + underscore;
    }
}
```

## Python

```python
class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        cntL = moves.count('L')
        cntR = moves.count('R')
        u = moves.count('_')
        diff = cntR - cntL
        return max(abs(diff + u), abs(diff - u))
```

## Python3

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cntL = moves.count('L')
        cntR = moves.count('R')
        cntU = moves.count('_')
        net = cntR - cntL
        return max(abs(net + cntU), abs(net - cntU))
```

## C

```c
int furthestDistanceFromOrigin(char* moves) {
    int countL = 0, countR = 0, countU = 0;
    for (char *p = moves; *p; ++p) {
        if (*p == 'L') countL++;
        else if (*p == 'R') countR++;
        else if (*p == '_') countU++;
    }
    int diff = countR - countL;
    int d1 = diff - countU;
    if (d1 < 0) d1 = -d1;
    int d2 = diff + countU;
    if (d2 < 0) d2 = -d2;
    return d1 > d2 ? d1 : d2;
}
```

## Csharp

```csharp
public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        int countL = 0, countR = 0, countU = 0;
        foreach (char c in moves) {
            if (c == 'L') countL++;
            else if (c == 'R') countR++;
            else if (c == '_') countU++;
        }
        int diff = countR - countL;
        int option1 = Math.Abs(diff + countU);
        int option2 = Math.Abs(diff - countU);
        return Math.Max(option1, option2);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} moves
 * @return {number}
 */
var furthestDistanceFromOrigin = function(moves) {
    let left = 0, right = 0, underscore = 0;
    for (let ch of moves) {
        if (ch === 'L') left++;
        else if (ch === 'R') right++;
        else underscore++; // '_'
    }
    const distIfAllLeft = Math.abs(right - (left + underscore));
    const distIfAllRight = Math.abs((right + underscore) - left);
    return Math.max(distIfAllLeft, distIfAllRight);
};
```

## Typescript

```typescript
function furthestDistanceFromOrigin(moves: string): number {
    let cntL = 0, cntR = 0, cntU = 0;
    for (const ch of moves) {
        if (ch === 'L') cntL++;
        else if (ch === 'R') cntR++;
        else cntU++; // '_'
    }
    const distAllR = (cntR + cntU) - cntL;
    const distAllL = cntR - (cntL + cntU);
    return Math.max(Math.abs(distAllR), Math.abs(distAllL));
}
```

## Php

```php
class Solution {

    /**
     * @param String $moves
     * @return Integer
     */
    function furthestDistanceFromOrigin($moves) {
        $cntL = 0;
        $cntR = 0;
        $cntU = 0;
        $len = strlen($moves);
        for ($i = 0; $i < $len; $i++) {
            $ch = $moves[$i];
            if ($ch === 'L') {
                $cntL++;
            } elseif ($ch === 'R') {
                $cntR++;
            } else { // '_'
                $cntU++;
            }
        }
        return abs($cntR - $cntL) + $cntU;
    }
}
```

## Swift

```swift
class Solution {
    func furthestDistanceFromOrigin(_ moves: String) -> Int {
        var leftCount = 0
        var rightCount = 0
        var underscoreCount = 0
        
        for ch in moves {
            switch ch {
            case "L":
                leftCount += 1
            case "R":
                rightCount += 1
            default: // "_"
                underscoreCount += 1
            }
        }
        
        let diff = rightCount - leftCount
        let option1 = abs(diff + underscoreCount)
        let option2 = abs(diff - underscoreCount)
        return max(option1, option2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun furthestDistanceFromOrigin(moves: String): Int {
        var left = 0
        var right = 0
        var underscore = 0
        for (c in moves) {
            when (c) {
                'L' -> left++
                'R' -> right++
                '_' -> underscore++
            }
        }
        return kotlin.math.abs(right - left) + underscore
    }
}
```

## Dart

```dart
class Solution {
  int furthestDistanceFromOrigin(String moves) {
    int left = 0, right = 0, underscore = 0;
    for (int i = 0; i < moves.length; i++) {
      switch (moves[i]) {
        case 'L':
          left++;
          break;
        case 'R':
          right++;
          break;
        case '_':
          underscore++;
          break;
      }
    }
    return (right - left).abs() + underscore;
  }
}
```

## Golang

```go
func furthestDistanceFromOrigin(moves string) int {
    diff := 0
    underscore := 0
    for _, ch := range moves {
        switch ch {
        case 'L':
            diff--
        case 'R':
            diff++
        case '_':
            underscore++
        }
    }
    // Replace all '_' with 'R' => diff + underscore
    // Replace all '_' with 'L' => diff - underscore
    d1 := diff + underscore
    if d1 < 0 {
        d1 = -d1
    }
    d2 := diff - underscore
    if d2 < 0 {
        d2 = -d2
    }
    if d1 > d2 {
        return d1
    }
    return d2
}
```

## Ruby

```ruby
def furthest_distance_from_origin(moves)
  l = moves.count('L')
  r = moves.count('R')
  u = moves.count('_')
  (r - l).abs + u
end
```

## Scala

```scala
object Solution {
    def furthestDistanceFromOrigin(moves: String): Int = {
        var left = 0
        var right = 0
        var underscore = 0
        for (c <- moves) {
            c match {
                case 'L' => left += 1
                case 'R' => right += 1
                case '_' => underscore += 1
                case _   =>
            }
        }
        Math.abs(right - left) + underscore
    }
}
```

## Rust

```rust
impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        let mut r = 0;
        let mut l = 0;
        let mut u = 0;
        for ch in moves.chars() {
            match ch {
                'R' => r += 1,
                'L' => l += 1,
                '_' => u += 1,
                _ => {}
            }
        }
        ((r as i32 - l as i32).abs() + u as i32)
    }
}
```

## Racket

```racket
(define/contract (furthest-distance-from-origin moves)
  (-> string? exact-integer?)
  (let-values ([(l r u)
                (for/fold ([l 0] [r 0] [u 0])
                          ([i (in-range (string-length moves))])
                  (define ch (string-ref moves i))
                  (cond [(char=? ch #\L) (values (+ l 1) r u)]
                        [(char=? ch #\R) (values l (+ r 1) u)]
                        [else               (values l r (+ u 1))]))])
    (let* ((base (- r l))                 ; net displacement from fixed moves
           (dist-with-L (abs (- base u))) ; all '_' become 'L'
           (dist-with-R (abs (+ base u)))) ; all '_' become 'R'
      (max dist-with-L dist-with-R))))
```

## Erlang

```erlang
-module(solution).
-export([furthest_distance_from_origin/1]).

-spec furthest_distance_from_origin(unicode:unicode_binary()) -> integer().
furthest_distance_from_origin(Moves) ->
    {CntL, CntR, CntU} = count_chars(binary_to_list(Moves), 0, 0, 0),
    Diff = CntR - CntL,
    abs(Diff) + CntU.

count_chars([], L, R, U) -> {L, R, U};
count_chars([H|T], L, R, U) ->
    case H of
        $L -> count_chars(T, L+1, R,   U);
        $R -> count_chars(T, L,   R+1, U);
        $_ -> count_chars(T, L,   R,   U+1);
        _  -> count_chars(T, L,   R,   U)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec furthest_distance_from_origin(moves :: String.t()) :: integer()
  def furthest_distance_from_origin(moves) do
    {l, r, u} =
      moves
      |> String.graphemes()
      |> Enum.reduce({0, 0, 0}, fn
        "L", {l, r, u} -> {l + 1, r, u}
        "R", {l, r, u} -> {l, r + 1, u}
        "_", {l, r, u} -> {l, r, u + 1}
      end)

    abs(r - l) + u
  end
end
```
