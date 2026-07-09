# 3001. Minimum Moves to Capture The Queen

## Cpp

```cpp
class Solution {
public:
    bool rookClear(int x1, int y1, int x2, int y2, int ox, int oy) {
        if (x1 == x2) { // same column
            if (ox != x1) return true;
            if ((oy > y1 && oy < y2) || (oy > y2 && oy < y1)) return false;
            return true;
        }
        if (y1 == y2) { // same row
            if (oy != y1) return true;
            if ((ox > x1 && ox < x2) || (ox > x2 && ox < x1)) return false;
            return true;
        }
        return false; // not a rook move
    }

    bool bishopClear(int x1, int y1, int x2, int y2, int ox, int oy) {
        if (abs(x1 - x2) != abs(y1 - y2)) return false;
        int dx = (x2 > x1) ? 1 : -1;
        int dy = (y2 > y1) ? 1 : -1;
        int cx = x1 + dx, cy = y1 + dy;
        while (cx != x2 && cy != y2) {
            if (cx == ox && cy == oy) return false;
            cx += dx;
            cy += dy;
        }
        return true;
    }

    int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        // rook capture in one move?
        if ((a == e || b == f) && rookClear(a, b, e, f, c, d)) return 1;
        // bishop capture in one move?
        if (abs(c - e) == abs(d - f) && bishopClear(c, d, e, f, a, b)) return 1;
        // otherwise two moves are sufficient
        return 2;
    }
};
```

## Java

```java
class Solution {
    public int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        // Check if rook can capture queen in one move
        boolean rookCan = false;
        if (a == e) { // same row
            if (!(c == a && isBetween(b, f, d))) {
                rookCan = true;
            }
        } else if (b == f) { // same column
            if (!(d == b && isBetween(a, e, c))) {
                rookCan = true;
            }
        }

        // Check if bishop can capture queen in one move
        boolean bishopCan = false;
        if (Math.abs(c - e) == Math.abs(d - f)) { // same diagonal
            boolean blocked = false;
            if (Math.abs(a - c) == Math.abs(b - d)) { // rook lies on that diagonal
                if (isBetween(c, e, a) && isBetween(d, f, b)) {
                    blocked = true;
                }
            }
            if (!blocked) {
                bishopCan = true;
            }
        }

        return (rookCan || bishopCan) ? 1 : 2;
    }

    private boolean isBetween(int x1, int x2, int y) {
        return y > Math.min(x1, x2) && y < Math.max(x1, x2);
    }
}
```

## Python

```python
class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        """
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :type e: int
        :type f: int
        :rtype: int
        """
        # Check rook capture possibility
        def rook_can():
            if a == e:
                # same row, check bishop blocking
                if c == a and min(b, f) < d < max(b, f):
                    return False
                return True
            if b == f:
                # same column, check bishop blocking
                if d == b and min(a, e) < c < max(a, e):
                    return False
                return True
            return False

        # Check bishop capture possibility
        def bishop_can():
            if abs(c - e) != abs(d - f):
                return False
            # same diagonal, check rook blocking
            if abs(a - c) == abs(b - d):
                if min(c, e) < a < max(c, e) and min(d, f) < b < max(d, f):
                    return False
            return True

        return 1 if rook_can() or bishop_can() else 2
```

## Python3

```python
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # positions
        rook = (a, b)
        bishop = (c, d)
        queen = (e, f)

        # check rook direct capture
        if rook[0] == queen[0] or rook[1] == queen[1]:
            blocked = False
            if rook[0] == queen[0]:  # same row
                if bishop[0] == rook[0] and min(rook[1], queen[1]) < bishop[1] < max(rook[1], queen[1]):
                    blocked = True
            else:  # same column
                if bishop[1] == rook[1] and min(rook[0], queen[0]) < bishop[0] < max(rook[0], queen[0]):
                    blocked = True
            if not blocked:
                return 1

        # check bishop direct capture
        if abs(bishop[0] - queen[0]) == abs(bishop[1] - queen[1]):
            blocked = False
            # rook blocks diagonal?
            if (abs(rook[0] - bishop[0]) == abs(rook[1] - bishop[1]) and
                abs(queen[0] - rook[0]) == abs(queen[1] - rook[1])):
                # ensure rook is between bishop and queen
                if (min(bishop[0], queen[0]) < rook[0] < max(bishop[0], queen[0]) and
                    min(bishop[1], queen[1]) < rook[1] < max(bishop[1], queen[1])):
                    blocked = True
            if not blocked:
                return 1

        # otherwise two moves are sufficient
        return 2
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
    bool rookAttack = false;
    if (a == e) { // same row
        bool blocked = (c == a) && ((d > b && d < f) || (d > f && d < b));
        if (!blocked) rookAttack = true;
    } else if (b == f) { // same column
        bool blocked = (d == b) && ((c > a && c < e) || (c > e && c < a));
        if (!blocked) rookAttack = true;
    }

    bool bishopAttack = false;
    if (abs(c - e) == abs(d - f)) { // same diagonal
        bool blocked = (abs(a - e) == abs(b - f)) &&
                       ((a > e && a < c) || (a > c && a < e)) &&
                       ((b > f && b < d) || (b > d && b < f));
        if (!blocked) bishopAttack = true;
    }

    return (rookAttack || bishopAttack) ? 1 : 2;
}
```

## Csharp

```csharp
public class Solution {
    public int MinMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        // Rook at (a,b), Bishop at (c,d), Queen at (e,f)

        // Check rook capture
        if (a == e) { // same row
            bool blocked = false;
            int minCol = Math.Min(b, f);
            int maxCol = Math.Max(b, f);
            if (c == a && d > minCol && d < maxCol) {
                blocked = true;
            }
            if (!blocked) return 1;
        }
        if (b == f) { // same column
            bool blocked = false;
            int minRow = Math.Min(a, e);
            int maxRow = Math.Max(a, e);
            if (d == b && c > minRow && c < maxRow) {
                blocked = true;
            }
            if (!blocked) return 1;
        }

        // Check bishop capture
        if (Math.Abs(c - e) == Math.Abs(d - f)) { // same diagonal
            int dx = Math.Sign(e - c);
            int dy = Math.Sign(f - d);
            int x = c + dx, y = d + dy;
            bool blocked = false;
            while (x != e && y != f) {
                if (x == a && y == b) {
                    blocked = true;
                    break;
                }
                x += dx;
                y += dy;
            }
            if (!blocked) return 1;
        }

        // Otherwise, it can be done in two moves
        return 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @param {number} d
 * @param {number} e
 * @param {number} f
 * @return {number}
 */
var minMovesToCaptureTheQueen = function(a, b, c, d, e, f) {
    const between = (x, y1, y2) => x > Math.min(y1, y2) && x < Math.max(y1, y2);
    
    // Rook can capture in one move?
    if (a === e) { // same column
        // blocked by bishop?
        if (!(c === a && between(d, b, f))) {
            return 1;
        }
    }
    if (b === f) { // same row
        if (!(d === b && between(c, a, e))) {
            return 1;
        }
    }
    
    // Bishop can capture in one move?
    if (Math.abs(c - e) === Math.abs(d - f)) { // queen on bishop diagonal
        // blocked by rook?
        const rookOnDiagonal = Math.abs(a - c) === Math.abs(b - d);
        const rookBetween = between(a, c, e) && between(b, d, f);
        if (!(rookOnDiagonal && rookBetween)) {
            return 1;
        }
    }
    
    // Otherwise needs two moves
    return 2;
};
```

## Typescript

```typescript
function minMovesToCaptureTheQueen(a: number, b: number, c: number, d: number, e: number, f: number): number {
    // Check rook capture
    let rookCan = false;
    if (a === e || b === f) {
        let blocked = false;
        if (a === e) { // same row
            if (c === a && d > Math.min(b, f) && d < Math.max(b, f)) {
                blocked = true;
            }
        } else { // same column
            if (d === b && c > Math.min(a, e) && c < Math.max(a, e)) {
                blocked = true;
            }
        }
        if (!blocked) rookCan = true;
    }

    // Check bishop capture
    let bishopCan = false;
    if (Math.abs(c - e) === Math.abs(d - f)) {
        let blocked = false;
        // Rook could block the diagonal path
        if (
            Math.abs(a - e) === Math.abs(b - f) &&
            a > Math.min(c, e) && a < Math.max(c, e) &&
            b > Math.min(d, f) && b < Math.max(d, f)
        ) {
            blocked = true;
        }
        if (!blocked) bishopCan = true;
    }

    return rookCan || bishopCan ? 1 : 2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @param Integer $d
     * @param Integer $e
     * @param Integer $f
     * @return Integer
     */
    function minMovesToCaptureTheQueen($a, $b, $c, $d, $e, $f) {
        // Check rook capture in one move
        if ($a == $e) { // same row
            $blocked = false;
            if ($c == $a && $d > min($b, $f) && $d < max($b, $f)) {
                $blocked = true; // bishop blocks the rook
            }
            if (!$blocked) return 1;
        }
        if ($b == $f) { // same column
            $blocked = false;
            if ($d == $b && $c > min($a, $e) && $c < max($a, $e)) {
                $blocked = true; // bishop blocks the rook
            }
            if (!$blocked) return 1;
        }

        // Check bishop capture in one move
        if (abs($c - $e) == abs($d - $f)) { // same diagonal
            $dr = ($e > $c) ? 1 : -1;
            $dc = ($f > $d) ? 1 : -1;
            $x = $c + $dr;
            $y = $d + $dc;
            $blocked = false;
            while ($x != $e && $y != $f) {
                if ($x == $a && $y == $b) { // rook blocks the bishop
                    $blocked = true;
                    break;
                }
                $x += $dr;
                $y += $dc;
            }
            if (!$blocked) return 1;
        }

        // Otherwise, it can be done in two moves
        return 2;
    }
}
```

## Swift

```swift
class Solution {
    func minMovesToCaptureTheQueen(_ a: Int, _ b: Int, _ c: Int, _ d: Int, _ e: Int, _ f: Int) -> Int {
        var canCaptureInOne = false
        
        // Rook capture
        if a == e { // same column
            let blocked = (c == a) && ((b < d && d < f) || (f < d && d < b))
            if !blocked { canCaptureInOne = true }
        }
        if b == f { // same row
            let blocked = (d == b) && ((a < c && c < e) || (e < c && c < a))
            if !blocked { canCaptureInOne = true }
        }
        
        // Bishop capture
        if abs(c - e) == abs(d - f) {
            var blocked = false
            // check if rook lies on the diagonal between bishop and queen
            if abs(a - c) == abs(b - d) {
                if (min(c, e) < a && a < max(c, e)) &&
                    (min(d, f) < b && b < max(d, f)) {
                    blocked = true
                }
            }
            if !blocked { canCaptureInOne = true }
        }
        
        return canCaptureInOne ? 1 : 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMovesToCaptureTheQueen(a: Int, b: Int, c: Int, d: Int, e: Int, f: Int): Int {
        // Direct capture by rook
        if ((a == e || b == f) && isClearRook(a, b, e, f, c, d)) return 1
        // Direct capture by bishop
        if (kotlin.math.abs(a - e) == kotlin.math.abs(b - f) && isClearBishop(a, b, e, f, c, d)) return 1
        return 2
    }

    private fun isClearRook(ax: Int, ay: Int, qx: Int, qy: Int, ox: Int, oy: Int): Boolean {
        if (ax != qx && ay != qy) return false
        val stepX = Integer.compare(qx, ax)
        val stepY = Integer.compare(qy, ay)
        var x = ax + stepX
        var y = ay + stepY
        while (x != qx || y != qy) {
            if (x == ox && y == oy) return false
            x += stepX
            y += stepY
        }
        return true
    }

    private fun isClearBishop(ax: Int, ay: Int, qx: Int, qy: Int, ox: Int, oy: Int): Boolean {
        if (kotlin.math.abs(ax - qx) != kotlin.math.abs(ay - qy)) return false
        val stepX = Integer.compare(qx, ax)
        val stepY = Integer.compare(qy, ay)
        var x = ax + stepX
        var y = ay + stepY
        while (x != qx || y != qy) {
            if (x == ox && y == oy) return false
            x += stepX
            y += stepY
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
    // Check rook capture
    bool rookCan = false;
    if (a == e) {
      // same row
      bool blocked = false;
      if (c == a) {
        if ((d > b && d < f) || (d < b && d > f)) blocked = true;
      }
      if (!blocked) rookCan = true;
    } else if (b == f) {
      // same column
      bool blocked = false;
      if (d == b) {
        if ((c > a && c < e) || (c < a && c > e)) blocked = true;
      }
      if (!blocked) rookCan = true;
    }

    // Check bishop capture
    bool bishopCan = false;
    if ((c - e).abs() == (d - f).abs()) {
      bool blocked = false;
      // Is the rook on the same diagonal between bishop and queen?
      if ((a - c).abs() == (b - d).abs()) {
        int drBishopToQueen = e - c;
        int dcBishopToQueen = f - d;
        int drBishopToRook = a - c;
        int dcBishopToRook = b - d;
        // Rook must be in the same direction and closer than queen
        if ((drBishopToQueen > 0 && drBishopToRook > 0 ||
                drBishopToQueen < 0 && drBishopToRook < 0) &&
            (dcBishopToQueen > 0 && dcBishopToRook > 0 ||
                dcBishopToQueen < 0 && dcBishopToRook < 0)) {
          if ((drBishopToRook).abs() < (drBishopToQueen).abs()) {
            blocked = true;
          }
        }
      }
      if (!blocked) bishopCan = true;
    }

    return (rookCan || bishopCan) ? 1 : 2;
  }
}
```

## Golang

```go
func minMovesToCaptureTheQueen(a int, b int, c int, d int, e int, f int) int {
	// rook at (a,b), bishop at (c,d), queen at (e,f)

	// Rook can capture in one move if same row or column and not blocked by bishop
	if a == e {
		// same row
		if !(c == a && ((b < d && d < f) || (f < d && d < b))) {
			return 1
		}
	}
	if b == f {
		// same column
		if !(d == b && ((a < c && c < e) || (e < c && c < a))) {
			return 1
		}
	}

	// Bishop can capture in one move if on the same diagonal and not blocked by rook
	if abs(c-e) == abs(d-f) {
		blocked := false
		// check if rook lies on that diagonal between bishop and queen
		if abs(a-c) == abs(b-d) { // rook is on the same diagonal as bishop
			if (c < a && a < e) || (e < a && a < c) {
				if (d < b && b < f) || (f < b && b < d) {
					blocked = true
				}
			}
		}
		if !blocked {
			return 1
		}
	}

	// Otherwise, it can always be done in two moves
	return 2
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
```

## Ruby

```ruby
def min_moves_to_capture_the_queen(a, b, c, d, e, f)
  # helper to check if the line from (x1,y1) to (x2,y2) is free of the blocker
  def clear_path?(x1, y1, x2, y2, bx, by)
    dx = x2 <=> x1
    dy = y2 <=> y1
    cx = x1 + dx
    cy = y1 + dy
    while cx != x2 || cy != y2
      return false if cx == bx && cy == by
      cx += dx
      cy += dy
    end
    true
  end

  # rook can capture in one move?
  if a == e || b == f
    return 1 if clear_path?(a, b, e, f, c, d)
  end

  # bishop can capture in one move?
  if (c - e).abs == (d - f).abs
    return 1 if clear_path?(c, d, e, f, a, b)
  end

  2
end
```

## Scala

```scala
object Solution {
    def minMovesToCaptureTheQueen(a: Int, b: Int, c: Int, d: Int, e: Int, f: Int): Int = {
        def between(x: Int, y: Int, z: Int): Boolean =
            (x < y && y < z) || (z < y && y < x)

        // rook can capture in one move?
        if (a == e) { // same row
            val blocked = c == a && between(b, d, f)
            if (!blocked) return 1
        }
        if (b == f) { // same column
            val blocked = d == b && between(a, c, e)
            if (!blocked) return 1
        }

        // bishop can capture in one move?
        if (math.abs(c - e) == math.abs(d - f)) {
            val onSameDiagonal = math.abs(a - e) == math.abs(b - f)
            val blocked = onSameDiagonal && between(c, a, e) && between(d, b, f)
            if (!blocked) return 1
        }

        // otherwise two moves are enough
        2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves_to_capture_the_queen(a: i32, b: i32, c: i32, d: i32, e: i32, f: i32) -> i32 {
        // helper to check if v is strictly between x and y
        let between = |v: i32, x: i32, y: i32| -> bool {
            let lo = x.min(y);
            let hi = x.max(y);
            v > lo && v < hi
        };

        // Check rook capture in one move
        let mut rook_one = false;
        if a == e {
            // same row
            if !(c == a && between(d, b, f)) {
                rook_one = true;
            }
        } else if b == f {
            // same column
            if !(d == b && between(c, a, e)) {
                rook_one = true;
            }
        }

        // Check bishop capture in one move
        let mut bishop_one = false;
        if (c - e).abs() == (d - f).abs() {
            // bishop and queen are on same diagonal
            let blocked = (a - e).abs() == (b - f).abs()
                && between(a, c, e)
                && between(b, d, f);
            if !blocked {
                bishop_one = true;
            }
        }

        if rook_one || bishop_one { 1 } else { 2 }
    }
}
```

## Racket

```racket
(define/contract (min-moves-to-capture-the-queen a b c d e f)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((rook-r a) (rook-c b)
         (bishop-r c) (bishop-c d)
         (queen-r e) (queen-c f))
    (define (between? x y z)
      (< (min y z) x (max y z)))
    (define rook-direct?
      (or (and (= rook-r queen-r)
               (not (and (= bishop-r rook-r)
                         (between? bishop-c rook-c queen-c))))
          (and (= rook-c queen-c)
               (not (and (= bishop-c rook-c)
                         (between? bishop-r rook-r queen-r))))))
    (define bishop-direct?
      (and (= (abs (- bishop-r queen-r))
              (abs (- bishop-c queen-c)))
           (not (and (= (abs (- rook-r bishop-r))
                       (abs (- rook-c bishop-c))) ; rook on same diagonal line
                     (between? rook-r bishop-r queen-r)
                     (between? rook-c bishop-c queen-c)))))
    (if (or rook-direct? bishop-direct?) 1 2)))
```

## Erlang

```erlang
-spec min_moves_to_capture_the_queen(integer(), integer(), integer(), integer(), integer(), integer()) -> integer().
min_moves_to_capture_the_queen(A, B, C, D, E, F) ->
    if
        can_capture_in_one(A, B, C, D, E, F) -> 1;
        true -> 2
    end.

can_capture_in_one(A, B, C, D, E, F) ->
    rook_can(A, B, C, D, E, F) orelse bishop_can(A, B, C, D, E, F).

rook_can(A, B, C, D, E, F) ->
    (A =:= E andalso not row_blocked(A, B, C, D, F)) orelse
    (B =:= F andalso not col_blocked(B, A, D, C, E)).

row_blocked(Row, B, C, D, QCol) ->
    C =:= Row andalso between(B, D, QCol).

col_blocked(Col, A, D, C, QRow) ->
    D =:= Col andalso between(A, C, QRow).

bishop_can(A, B, C, D, E, F) ->
    (erlang:abs(A - E) =:= erlang:abs(B - F)) andalso not bishop_path_blocked(A, B, C, D, E, F).

bishop_path_blocked(A, B, C, D, E, F) ->
    (erlang:abs(C - E) =:= erlang:abs(D - F)) andalso
    (erlang:abs(A - C) =:= erlang:abs(B - D)) andalso
    between(C, A, E) andalso between(D, B, F).

between(X, Y, Z) ->
    Y > erlang:min(X, Z) andalso Y < erlang:max(X, Z).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves_to_capture_the_queen(a :: integer, b :: integer, c :: integer, d :: integer, e :: integer, f :: integer) :: integer
  def min_moves_to_capture_the_queen(a, b, c, d, e, f) do
    cond do
      rook_can_capture?(a, b, c, d, e, f) -> 1
      bishop_can_capture?(a, b, c, d, e, f) -> 1
      true -> 2
    end
  end

  defp between(x1, x2, y) do
    min = if x1 < x2, do: x1, else: x2
    max = if x1 > x2, do: x1, else: x2
    y > min and y < max
  end

  defp rook_can_capture?(a, b, c, d, e, f) do
    cond do
      a == e ->
        blocked = c == a and between(b, f, d)
        not blocked

      b == f ->
        blocked = d == b and between(a, e, c)
        not blocked

      true -> false
    end
  end

  defp bishop_can_capture?(a, b, c, d, e, f) do
    if abs(c - e) == abs(d - f) do
      blocked = (abs(a - e) == abs(b - f)) and between(c, e, a) and between(d, f, b)
      not blocked
    else
      false
    end
  end
end
```
