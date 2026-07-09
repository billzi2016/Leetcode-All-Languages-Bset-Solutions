# 3609. Minimum Moves to Reach Target in Grid

## Cpp

```cpp
class Solution {
public:
    int minMoves(int sx, int sy, int tx, int ty) {
        using int64 = long long;
        int64 a = max((int64)sx, (int64)sy);
        int64 b = min((int64)sx, (int64)sy);
        int64 x = max((int64)tx, (int64)ty);
        int64 y = min((int64)tx, (int64)ty);
        int64 moves = 0;
        while (true) {
            if (x == a && y == b) return (int)moves;
            if (x < a || y < b) return -1;
            if (y == 0) {                     // only halving possible
                if ((x & 1LL) != 0) return -1; // odd cannot be obtained by doubling
                x >>= 1;
                ++moves;
                continue;
            }
            if (x > 2 * y) {
                // try to halve if it is a valid previous move
                if ((x & 1LL) == 0 && x / 2 >= a) {
                    x >>= 1;
                    ++moves;
                } else {
                    // subtract multiples of y to get below 2*y or reach a
                    int64 target = max(a, 2 * y + 1);
                    if (x <= target) return -1; // cannot make progress
                    int64 cnt = (x - target) / y + 1;
                    moves += cnt;
                    x -= cnt * y;
                }
            } else {
                // must have come from an addition step
                x -= y;
                ++moves;
            }
            if (x < y) swap(x, y);
        }
    }
};
```

## Java

```java
class Solution {
    public int minMoves(int sx, int sy, int tx, int ty) {
        long x = tx, y = ty;
        long startX = sx, startY = sy;
        long moves = 0;
        while (true) {
            if (x == startX && y == startY) return (int) moves;
            if (x < startX || y < startY) return -1;

            if (x == y) {
                // can only reduce the coordinate that is larger than its start
                if (x > startX) {
                    x -= y; // makes x zero
                } else if (y > startY) {
                    y -= x;
                } else {
                    return -1;
                }
                moves++;
                continue;
            }

            if (x > y) {
                // try halving the larger coordinate
                if ((x & 1L) == 0 && x / 2 >= Math.max(y, startX)) {
                    x >>= 1;
                    moves++;
                } else {
                    long diff = x - y;
                    // subtraction is valid only if it makes x smaller than y (otherwise we would need another max)
                    if (diff < y) {
                        x = diff;
                        moves++;
                    } else {
                        return -1;
                    }
                }
            } else { // y > x
                if ((y & 1L) == 0 && y / 2 >= Math.max(x, startY)) {
                    y >>= 1;
                    moves++;
                } else {
                    long diff = y - x;
                    if (diff < x) {
                        y = diff;
                        moves++;
                    } else {
                        return -1;
                    }
                }
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def minMoves(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: int
        """
        moves = 0
        while tx > sx and ty > sy:
            if tx > ty:
                if ty == 0:
                    return -1
                moves += tx // ty
                tx %= ty
                if tx == 0:
                    tx = ty
            else:
                if tx == 0:
                    return -1
                moves += ty // tx
                ty %= tx
                if ty == 0:
                    ty = tx

        if tx == sx and ty == sy:
            return moves
        if tx == sx:
            if ty < sy or (ty - sy) % sx != 0:
                return -1
            return moves + (ty - sy) // sx
        if ty == sy:
            if tx < sx or (tx - sx) % sy != 0:
                return -1
            return moves + (tx - sx) // sy
        return -1
```

## Python3

```python
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        steps = 0
        while True:
            if tx == sx and ty == sy:
                return steps
            if tx < sx or ty < sy:
                return -1

            if tx == ty:
                # both equal but not the start point
                # one subtraction will make one coordinate zero
                tx -= ty
                steps += 1
                continue

            if tx > ty:
                L, S = tx, ty
                if L >= 2 * S and L % 2 == 0:
                    tx = L // 2
                else:
                    tx = L - S
                steps += 1
            else:  # ty > tx
                L, S = ty, tx
                if L >= 2 * S and L % 2 == 0:
                    ty = L // 2
                else:
                    ty = L - S
                steps += 1
```

## C

```c
int minMoves(int sx, int sy, int tx, int ty) {
    long long X = tx, Y = ty;
    long long Sx = sx, Sy = sy;
    long long steps = 0;

    while (X > Sx && Y > Sy) {
        if (X == Y) return -1; // cannot change equal coordinates
        if (X > Y) {
            if (X >= 2 * Y) {
                X /= 2;
                ++steps;
            } else {
                X -= Y;
                ++steps;
            }
        } else { // Y > X
            if (Y >= 2 * X) {
                Y /= 2;
                ++steps;
            } else {
                Y -= X;
                ++steps;
            }
        }
    }

    if (X == Sx && Y == Sy) return (int)steps;

    if (X == Sx) {
        // Reduce Y to Sy
        while (Y > Sy) {
            if (Y >= 2 * X && X > 0) {
                Y /= 2;
                ++steps;
            } else {
                long long diff = Y - Sy;
                if (diff % X != 0) return -1;
                steps += diff / X;
                Y = Sy;
            }
        }
        return (Y == Sy) ? (int)steps : -1;
    }

    if (Y == Sy) {
        // Reduce X to Sx
        while (X > Sx) {
            if (X >= 2 * Y && Y > 0) {
                X /= 2;
                ++steps;
            } else {
                long long diff = X - Sx;
                if (diff % Y != 0) return -1;
                steps += diff / Y;
                X = Sx;
            }
        }
        return (X == Sx) ? (int)steps : -1;
    }

    return -1;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinMoves(int sx, int sy, int tx, int ty) {
        long sX = sx, sY = sy, tX = tx, tY = ty;
        if (sX > tX || sY > tY) return -1;
        long moves = 0;

        // Main reduction loop while both coordinates are larger than start
        while (tX > sX && tY > sY) {
            if (tX == tY) return -1; // stuck

            if (tX > tY) {
                if (sY == 0) {
                    // can only halve when possible
                    if ((tX & 1L) != 0) return -1;
                    tX >>= 1;
                    moves++;
                    continue;
                }
                if (tX >= 2 * tY && (tX & 1L) == 0) {
                    tX >>= 1; // halve
                } else {
                    tX -= tY; // subtract
                }
            } else { // tY > tX
                if (sX == 0) {
                    if ((tY & 1L) != 0) return -1;
                    tY >>= 1;
                    moves++;
                    continue;
                }
                if (tY >= 2 * tX && (tY & 1L) == 0) {
                    tY >>= 1; // halve
                } else {
                    tY -= tX; // subtract
                }
            }
            moves++;
        }

        // Helper to finish reduction when one coordinate already matches start
        bool Reduce(long larger, long target, long fixedCoord, ref long cnt) {
            while (larger > target) {
                if (fixedCoord == 0) {
                    if ((larger & 1L) != 0) return false;
                    larger >>= 1;
                    cnt++;
                    continue;
                }
                if (larger >= 2 * fixedCoord && (larger & 1L) == 0) {
                    larger >>= 1;
                    cnt++;
                } else {
                    long diff = larger - target;
                    if (diff % fixedCoord != 0) return false;
                    cnt += diff / fixedCoord;
                    larger = target;
                }
            }
            return larger == target;
        }

        if (tX == sX && tY == sY) return (int)moves;

        if (tX == sX) {
            long cnt = moves;
            if (!Reduce(tY, sY, sX, ref cnt)) return -1;
            return (int)cnt;
        }

        if (tY == sY) {
            long cnt = moves;
            if (!Reduce(tX, sX, sY, ref cnt)) return -1;
            return (int)cnt;
        }

        // One of the coordinates fell below its start value -> impossible
        return -1;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number} sx
 * @param {number} sy
 * @param {number} tx
 * @param {number} ty
 * @return {number}
 * /
var minMoves = function(sx, sy, tx, ty) {
    let moves = 0;
    while (tx > sx && ty > sy) {
        if (tx === ty) return -1;
        if (tx > ty) {
            if (tx >= 2 * ty && (tx & 1) === 0) {
                tx >>= 1; // halve
                moves++;
            } else {
                tx -= ty;
                moves++;
            }
        } else { // ty > tx
            if (ty >= 2 * tx && (ty & 1) === 0) {
                ty >>= 1; // halve
                moves++;
            } else {
                ty -= tx;
                moves++;
            }
        }
    }

    // If both coordinates match start
    if (tx === sx && ty === sy) return moves;

    // If any coordinate fell below start, impossible
    if (tx < sx || ty < sy) return -1;

    // One of the coordinates equals its start value; handle the remaining dimension
    if (tx === sx) {
        // Reduce ty to sy using reverse operations while x stays fixed
        while (ty > sy) {
            if (ty >= 2 * tx && (ty & 1) === 0) {
                ty >>= 1;
                moves++;
            } else {
                if (tx === 0) return -1; // cannot subtract zero
                const diff = ty - sy;
                if (diff % tx !== 0) return -1;
                moves += diff / tx;
                ty = sy;
            }
        }
        return ty === sy ? moves : -1;
    }

    if (ty === sy) {
        // Reduce tx to sx while y stays fixed
        while (tx > sx) {
            if (tx >= 2 * ty && (tx & 1) === 0) {
                tx >>= 1;
                moves++;
            } else {
                if (ty === 0) return -1; // cannot subtract zero
                const diff = tx - sx;
                if (diff % ty !== 0) return -1;
                moves += diff / ty;
                tx = sx;
            }
        }
        return tx === sx ? moves : -1;
    }

    return -1;
};
```

## Typescript

```typescript
function minMoves(sx: number, sy: number, tx: number, ty: number): number {
    if (sx === tx && sy === ty) return 0;
    let moves = 0;

    // main reduction while both coordinates are still larger than start
    while (tx > sx && ty > sy) {
        if (tx === ty) return -1;
        if (tx > ty) {
            // try halving tx
            if (tx % 2 === 0 && tx / 2 >= ty) {
                tx = tx / 2;
                moves++;
            } else {
                const diff = tx - sx;
                let k = Math.max(1, Math.floor(diff / ty));
                if (tx - k * ty < sx) {
                    k = Math.ceil((tx - sx) / ty);
                }
                tx -= k * ty;
                moves += k;
            }
        } else { // ty > tx
            if (ty % 2 === 0 && ty / 2 >= tx) {
                ty = ty / 2;
                moves++;
            } else {
                const diff = ty - sy;
                let k = Math.max(1, Math.floor(diff / tx));
                if (ty - k * tx < sy) {
                    k = Math.ceil((ty - sy) / tx);
                }
                ty -= k * tx;
                moves += k;
            }
        }
    }

    // one of the coordinates has reached its start value
    if (tx === sx && ty === sy) return moves;

    if (tx === sx) {
        while (ty > sy) {
            if (ty % 2 === 0 && ty / 2 >= tx) {
                ty = ty / 2;
                moves++;
            } else {
                if (tx === 0) return -1;
                const diff = ty - sy;
                let k = Math.max(1, Math.floor(diff / tx));
                if (ty - k * tx < sy) {
                    k = Math.ceil((ty - sy) / tx);
                }
                ty -= k * tx;
                moves += k;
            }
        }
        return ty === sy ? moves : -1;
    }

    if (ty === sy) {
        while (tx > sx) {
            if (tx % 2 === 0 && tx / 2 >= ty) {
                tx = tx / 2;
                moves++;
            } else {
                if (ty === 0) return -1;
                const diff = tx - sx;
                let k = Math.max(1, Math.floor(diff / ty));
                if (tx - k * ty < sx) {
                    k = Math.ceil((tx - sx) / ty);
                }
                tx -= k * ty;
                moves += k;
            }
        }
        return tx === sx ? moves : -1;
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $sx
     * @param Integer $sy
     * @param Integer $tx
     * @param Integer $ty
     * @return Integer
     */
    function minMoves($sx, $sy, $tx, $ty) {
        if ($sx == $tx && $sy == $ty) return 0;
        if ($sx > $tx || $sy > $ty) return -1;
        if ($sx == 0 && $sy == 0) return -1; // cannot move from (0,0)

        $cnt = 0;

        while ($tx > $sx && $ty > $sy) {
            if ($tx == $ty) return -1;
            if ($tx > $ty) {
                if ($tx >= 2 * $ty) {
                    // halve the larger coordinate
                    $tx = intdiv($tx, 2);
                    $cnt++;
                } else {
                    $tx -= $ty;
                    $cnt++;
                }
            } else { // $ty > $tx
                if ($ty >= 2 * $tx) {
                    $ty = intdiv($ty, 2);
                    $cnt++;
                } else {
                    $ty -= $tx;
                    $cnt++;
                }
            }
        }

        // One of the coordinates matches its start value now
        if ($tx == $sx && $ty == $sy) return $cnt;

        if ($tx == $sx) {
            while ($ty > $sy) {
                if ($ty % 2 == 0 && intdiv($ty, 2) >= $sx) {
                    $ty = intdiv($ty, 2);
                    $cnt++;
                } else {
                    if ($sx == 0) return -1;
                    $diff = $ty - $sy;
                    if ($diff % $sx != 0) return -1;
                    $cnt += intdiv($diff, $sx);
                    $ty = $sy;
                }
            }
            return $ty == $sy ? $cnt : -1;
        }

        if ($ty == $sy) {
            while ($tx > $sx) {
                if ($tx % 2 == 0 && intdiv($tx, 2) >= $sy) {
                    $tx = intdiv($tx, 2);
                    $cnt++;
                } else {
                    if ($sy == 0) return -1;
                    $diff = $tx - $sx;
                    if ($diff % $sy != 0) return -1;
                    $cnt += intdiv($diff, $sy);
                    $tx = $sx;
                }
            }
            return $tx == $sx ? $cnt : -1;
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minMoves(_ sx: Int, _ sy: Int, _ tx: Int, _ ty: Int) -> Int {
        var x = tx
        var y = ty
        var moves = 0
        
        while true {
            if x == sx && y == sy { return moves }
            if x < sx || y < sy { return -1 }
            
            if x == y {
                // Equality can only arise from a zero coordinate before the last move.
                if sx == 0 && sy == x { return moves + 1 }
                if sy == 0 && sx == x { return moves + 1 }
                return -1
            }
            
            if x > y {
                if x >= 2 * y && x % 2 == 0 {
                    x /= 2
                    moves += 1
                } else {
                    x -= y
                    moves += 1
                }
            } else { // y > x
                if y >= 2 * x && y % 2 == 0 {
                    y /= 2
                    moves += 1
                } else {
                    y -= x
                    moves += 1
                }
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves(sx: Int, sy: Int, tx: Int, ty: Int): Int {
        var x = tx.toLong()
        var y = ty.toLong()
        val startX = sx.toLong()
        val startY = sy.toLong()
        var moves = 0L

        while (x > startX && y > startY) {
            if (x == y) return -1
            if (x > y) {
                // x is larger
                if (x >= 2 * y && x % 2L == 0L) {
                    x /= 2
                } else {
                    x -= y
                }
            } else {
                // y is larger
                if (y >= 2 * x && y % 2L == 0L) {
                    y /= 2
                } else {
                    y -= x
                }
            }
            moves++
        }

        // One of the coordinates has reached its start value
        if (x == startX && y == startY) return moves.toInt()

        if (x == startX) {
            var curY = y
            while (curY > startY) {
                if (curY % 2L != 0L || curY / 2 < startX) return -1
                curY /= 2
                moves++
            }
            return if (curY == startY) moves.toInt() else -1
        }

        if (y == startY) {
            var curX = x
            while (curX > startX) {
                if (curX % 2L != 0L || curX / 2 < startY) return -1
                curX /= 2
                moves++
            }
            return if (curX == startX) moves.toInt() else -1
        }

        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minMoves(int sx, int sy, int tx, int ty) {
    int moves = 0;
    while (tx > sx && ty > sy) {
      if (tx == ty) return -1;
      if (tx > ty) {
        if (tx >= 2 * ty && tx % 2 == 0) {
          tx ~/= 2;
          moves++;
        } else {
          tx -= ty;
          moves++;
        }
      } else {
        if (ty >= 2 * tx && ty % 2 == 0) {
          ty ~/= 2;
          moves++;
        } else {
          ty -= tx;
          moves++;
        }
      }
    }

    if (tx == sx && ty == sy) return moves;

    int extra = -1;
    if (tx == sx) {
      extra = _reduce(ty, sx, sy);
    } else if (ty == sy) {
      extra = _reduce(tx, sy, sx);
    } else {
      return -1;
    }

    if (extra == -1) return -1;
    return moves + extra;
  }

  int _reduce(int larger, int fixedSmall, int target) {
    int moves = 0;
    while (larger > target) {
      if (fixedSmall == 0) {
        if (larger % 2 != 0) return -1;
        larger ~/= 2;
        moves++;
      } else if (larger >= 2 * fixedSmall && larger % 2 == 0) {
        larger ~/= 2;
        moves++;
      } else {
        int diff = larger - target;
        if (diff % fixedSmall != 0) return -1;
        moves += diff ~/ fixedSmall;
        larger = target;
      }
    }
    return larger == target ? moves : -1;
  }
}
```

## Golang

```go
func minMoves(sx int, sy int, tx int, ty int) int {
	if sx == tx && sy == ty {
		return 0
	}
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	moves := 0
	for tx > sx && ty > sy {
		if tx >= ty {
			if tx%2 == 0 && tx/2 >= max(sx, ty) {
				tx /= 2
				moves++
			} else {
				tx -= ty
				moves++
			}
		} else { // ty > tx
			if ty%2 == 0 && ty/2 >= max(sy, tx) {
				ty /= 2
				moves++
			} else {
				ty -= tx
				moves++
			}
		}
	}
	if tx == sx && ty == sy {
		return moves
	}
	if tx == sx {
		for ty > sy {
			if ty%2 == 0 && ty/2 >= sx {
				ty /= 2
				moves++
			} else {
				if sx == 0 { // cannot subtract zero
					return -1
				}
				if ty-sx < sy {
					return -1
				}
				ty -= sx
				moves++
			}
		}
		if ty == sy {
			return moves
		}
		return -1
	}
	if ty == sy {
		for tx > sx {
			if tx%2 == 0 && tx/2 >= sy {
				tx /= 2
				moves++
			} else {
				if sy == 0 { // cannot subtract zero
					return -1
				}
				if tx-sy < sx {
					return -1
				}
				tx -= sy
				moves++
			}
		}
		if tx == sx {
			return moves
		}
		return -1
	}
	return -1
}
```

## Ruby

```ruby
def min_moves(sx, sy, tx, ty)
  moves = 0

  while tx > sx && ty > sy
    if tx > ty
      if tx >= 2 * ty
        if (tx & 1) == 0
          tx >>= 1
          moves += 1
        else
          tx -= ty
          moves += 1
        end
      else
        tx -= ty
        moves += 1
      end
    else
      if ty >= 2 * tx
        if (ty & 1) == 0
          ty >>= 1
          moves += 1
        else
          ty -= tx
          moves += 1
        end
      else
        ty -= tx
        moves += 1
      end
    end
  end

  if tx == sx && ty >= sy
    while ty > sy
      if sx == 0
        return -1 unless (ty & 1) == 0
        ty >>= 1
        moves += 1
      else
        if ty >= 2 * sx && (ty & 1) == 0
          ty >>= 1
          moves += 1
        else
          diff = ty - sy
          return -1 unless diff % sx == 0
          moves += diff / sx
          ty = sy
        end
      end
    end
    return moves
  elsif ty == sy && tx >= sx
    while tx > sx
      if sy == 0
        return -1 unless (tx & 1) == 0
        tx >>= 1
        moves += 1
      else
        if tx >= 2 * sy && (tx & 1) == 0
          tx >>= 1
          moves += 1
        else
          diff = tx - sx
          return -1 unless diff % sy == 0
          moves += diff / sy
          tx = sx
        end
      end
    end
    return moves
  else
    -1
  end
end
```

## Scala

```scala
object Solution {
    def minMoves(sx: Int, sy: Int, tx: Int, ty: Int): Int = {
        var sxL = sx.toLong
        var syL = sy.toLong
        var txL = tx.toLong
        var tyL = ty.toLong
        var moves: Long = 0

        // main reduction while both coordinates are still larger than start
        while (txL > sxL && tyL > syL) {
            if (txL > tyL) {
                if (txL >= 2 * tyL && (txL & 1L) == 0L) {
                    txL >>= 1
                } else {
                    txL -= tyL
                }
            } else {
                if (tyL >= 2 * txL && (tyL & 1L) == 0L) {
                    tyL >>= 1
                } else {
                    tyL -= txL
                }
            }
            moves += 1
        }

        // helper to finish when one coordinate already matches start
        def finish(fixed: Long, varCoord: Long, fixedStart: Long, varStart: Long): Long = {
            var v = varCoord
            while (v > varStart) {
                if (fixed == 0L) {
                    // only halving possible when the other side is zero
                    if ((v & 1L) == 0L) {
                        v >>= 1
                    } else return -1L
                } else {
                    if (v >= 2 * fixed && (v & 1L) == 0L) {
                        v >>= 1
                    } else {
                        v -= fixed
                    }
                }
                moves += 1
            }
            if (v == varStart) moves else -1L
        }

        if (txL == sxL && tyL == syL) return moves.toInt

        if (txL == sxL) {
            val res = finish(sxL, tyL, sxL, syL)
            if (res == -1L) -1 else moves.toInt
        } else if (tyL == syL) {
            val res = finish(syL, txL, syL, sxL)
            if (res == -1L) -1 else moves.toInt
        } else {
            -1
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves(sx: i32, sy: i32, tx: i32, ty: i32) -> i32 {
        let mut x = tx as i64;
        let mut y = ty as i64;
        let sx = sx as i64;
        let sy = sy as i64;
        let mut steps: i64 = 0;

        loop {
            if x == sx && y == sy {
                return steps as i32;
            }
            if x < sx || y < sy {
                return -1;
            }

            // If both coordinates are equal but not the start, we can only subtract one from the other
            if x == y {
                // cannot make progress if they are already zero and not at start
                if x == 0 {
                    return -1;
                }
                // turn one of them to zero (subtract)
                x = 0;
                steps += 1;
                continue;
            }

            if x > y {
                // larger is x, smaller is y
                if x >= 2 * y && x % 2 == 0 {
                    x /= 2;
                } else {
                    x -= y;
                }
            } else { // y > x
                if y >= 2 * x && y % 2 == 0 {
                    y /= 2;
                } else {
                    y -= x;
                }
            }
            steps += 1;
        }
    }
}
```

## Racket

```racket
(define/contract (min-moves sx sy tx ty)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  
  ;; helper: number of doublings needed to turn `a` into `b`
  (define (doublings-needed a b)
    (let loop ((cur b) (cnt 0))
      (cond [(= cur a) cnt]
            [(< cur a) -1]
            [(even? cur) (loop (/ cur 2) (+ cnt 1))]
            [else -1])))
  
  (let rec ((tx tx) (ty ty) (moves 0))
    (cond
      ;; reached the start
      [(and (= tx sx) (= ty sy)) moves]
      
      ;; overshoot -> impossible
      [(or (< tx sx) (< ty sy)) -1]
      
      ;; x already matches start
      [(= tx sx)
       (if (= sx 0)
           (let ((extra (doublings-needed sy ty)))
             (if (= extra -1) -1 (+ moves extra)))
           (let ((diff (- ty sy)))
             (if (zero? (modulo diff sx))
                 (+ moves (/ diff sx))
                 -1)))]
      
      ;; y already matches start
      [(= ty sy)
       (if (= sy 0)
           (let ((extra (doublings-needed sx tx)))
             (if (= extra -1) -1 (+ moves extra)))
           (let ((diff (- tx sx)))
             (if (zero? (modulo diff sy))
                 (+ moves (/ diff sy))
                 -1)))]
      
      ;; both coordinates larger than start
      [(> tx ty)
       (if (>= tx (* 2 ty))
           (if (even? tx)
               (rec (/ tx 2) ty (+ moves 1))
               (rec (- tx ty) ty (+ moves 1)))
           (rec (- tx ty) ty (+ moves 1)))]
      
      [(> ty tx)
       (if (>= ty (* 2 tx))
           (if (even? ty)
               (rec tx (/ ty 2) (+ moves 1))
               (rec tx (- ty tx) (+ moves 1)))
           (rec tx (- ty tx) (+ moves 1)))]
      
      [else -1])))
```

## Erlang

```erlang
-spec min_moves(Sx :: integer(), Sy :: integer(), Tx :: integer(), Ty :: integer()) -> integer().
min_moves(Sx, Sy, Tx, Ty) ->
    go(Sx, Sy, Tx, Ty, 0).

go(Sx, Sy, Sx, Sy, Ans) ->
    Ans;
go(_, _, Tx, _Ty, _Ans) when Tx < 0 ->
    -1;
go(_, _, _Tx, Ty, _Ans) when Ty < 0 ->
    -1;
go(Sx, Sy, Tx, Ty, _Ans) when Tx < Sx; Ty < Sy ->
    -1;
go(_Sx, _Sy, Tx, Ty, Ans) when Tx == Ty ->
    if
        _Sx =:= 0 andalso _Sy =:= Ty -> Ans + 1;
        _Sy =:= 0 andalso _Sx =:= Tx -> Ans + 1;
        true -> -1
    end;
go(Sx, Sy, Tx, Ty, Ans) when Tx > Ty ->
    if
        Ty == Sy ->
            case Tx rem 2 of
                0 when (Tx div 2) >= Sx ->
                    go(Sx, Sy, Tx div 2, Ty, Ans + 1);
                _ ->
                    go(Sx, Sy, Tx - Ty, Ty, Ans + 1)
            end;
        true ->
            if
                Tx >= 2 * Ty andalso (Tx rem 2) =:= 0 ->
                    go(Sx, Sy, Tx div 2, Ty, Ans + 1);
                true ->
                    go(Sx, Sy, Tx - Ty, Ty, Ans + 1)
            end
    end;
go(Sx, Sy, Tx, Ty, Ans) -> % Ty > Tx
    if
        Tx == Sx ->
            case Ty rem 2 of
                0 when (Ty div 2) >= Sy ->
                    go(Sx, Sy, Tx, Ty div 2, Ans + 1);
                _ ->
                    go(Sx, Sy, Tx, Ty - Tx, Ans + 1)
            end;
        true ->
            if
                Ty >= 2 * Tx andalso (Ty rem 2) =:= 0 ->
                    go(Sx, Sy, Tx, Ty div 2, Ans + 1);
                true ->
                    go(Sx, Sy, Tx, Ty - Tx, Ans + 1)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves(sx :: integer, sy :: integer, tx :: integer, ty :: integer) :: integer
  def min_moves(sx, sy, tx, ty) do
    go(sx, sy, tx, ty, 0)
  end

  defp go(sx, sy, tx, ty, moves) do
    cond do
      tx == sx and ty == sy ->
        moves

      tx < sx or ty < sy ->
        -1

      tx == ty ->
        cond do
          sx == 0 and tx >= sy ->
            go(sx, sy, 0, ty, moves + 1)

          sy == 0 and ty >= sx ->
            go(sx, sy, tx, 0, moves + 1)

          true ->
            -1
        end

      tx > ty ->
        if tx >= 2 * ty do
          go(sx, sy, div(tx, 2), ty, moves + 1)
        else
          go(sx, sy, tx - ty, ty, moves + 1)
        end

      true -> # ty > tx
        if ty >= 2 * tx do
          go(sx, sy, tx, div(ty, 2), moves + 1)
        else
          go(sx, sy, tx, ty - tx, moves + 1)
        end
    end
  end
end
```
