# 0780. Reaching Points

## Cpp

```cpp
class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        long long x = tx, y = ty;
        long long sX = sx, sY = sy;
        while (x > sX && y > sY) {
            if (x > y) {
                x %= y;
                if (x == 0) x = y; // avoid zero
            } else {
                y %= x;
                if (y == 0) y = x;
            }
        }
        if (x == sX && y == sY) return true;
        if (x == sX) {
            return (y > sY) && ((y - sY) % sX == 0);
        }
        if (y == sY) {
            return (x > sX) && ((x - sX) % sY == 0);
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx > sx && ty > sy) {
            if (tx > ty) {
                tx %= ty;
                if (tx == 0) tx = ty;
            } else {
                ty %= tx;
                if (ty == 0) ty = tx;
            }
        }
        if (tx == sx && ty == sy) return true;
        if (tx == sx) {
            return ty >= sy && (ty - sy) % sx == 0;
        }
        if (ty == sy) {
            return tx >= sx && (tx - sx) % sy == 0;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                if ty > sy:
                    tx %= ty
                    if tx == 0:
                        tx = ty
                else:
                    # ty == sy, can only subtract multiples of ty from tx
                    return (tx - sx) % ty == 0
            else:  # ty >= tx
                if tx > sx:
                    ty %= tx
                    if ty == 0:
                        ty = tx
                else:
                    # tx == sx, can only subtract multiples of tx from ty
                    return (ty - sy) % tx == 0
        return False
```

## Python3

```python
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
                if tx == 0:
                    tx = ty
            else:
                ty %= tx
                if ty == 0:
                    ty = tx

        if tx == sx and ty == sy:
            return True
        if tx == sx:
            return ty >= sy and (ty - sy) % sx == 0
        if ty == sy:
            return tx >= sx and (tx - sx) % sy == 0
        return False
```

## C

```c
bool reachingPoints(int sx, int sy, int tx, int ty) {
    long long sxl = sx, syl = sy, txl = tx, tyl = ty;
    while (txl > sxl && tyl > syl) {
        if (txl > tyl) {
            txl %= tyl;
            if (txl == 0) txl = tyl;
        } else {
            tyl %= txl;
            if (tyl == 0) tyl = txl;
        }
    }
    if (txl == sxl && tyl == syl) return true;
    if (txl == sxl && tyl >= syl && (tyl - syl) % sxl == 0) return true;
    if (tyl == syl && txl >= sxl && (txl - sxl) % syl == 0) return true;
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool ReachingPoints(int sx, int sy, int tx, int ty) {
        long sX = sx, sY = sy, tX = tx, tY = ty;
        while (tX >= sX && tY >= sY) {
            if (tX == sX && tY == sY) return true;
            if (tX == sX) return (tY - sY) % sX == 0;
            if (tY == sY) return (tX - sX) % sY == 0;

            if (tX > tY) {
                if (tY > sY)
                    tX %= tY;
                else
                    return (tX - sX) % tY == 0;
            } else { // tY >= tX
                if (tX > sX)
                    tY %= tX;
                else
                    return (tY - sY) % tX == 0;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} sx
 * @param {number} sy
 * @param {number} tx
 * @param {number} ty
 * @return {boolean}
 */
var reachingPoints = function(sx, sy, tx, ty) {
    while (tx > sx && ty > sy && tx !== ty) {
        if (tx > ty) {
            tx %= ty;
            if (tx === 0) tx = ty;
        } else {
            ty %= tx;
            if (ty === 0) ty = tx;
        }
    }
    if (tx === sx && ty === sy) return true;
    if (tx === sx) {
        return ty >= sy && (ty - sy) % sx === 0;
    }
    if (ty === sy) {
        return tx >= sx && (tx - sx) % sy === 0;
    }
    return false;
};
```

## Typescript

```typescript
function reachingPoints(sx: number, sy: number, tx: number, ty: number): boolean {
    while (tx > sx && ty > sy) {
        if (tx > ty) {
            tx %= ty;
        } else {
            ty %= tx;
        }
    }
    if (tx === sx && ty === sy) return true;
    if (tx === sx) {
        return ty >= sy && (ty - sy) % sx === 0;
    }
    if (ty === sy) {
        return tx >= sx && (tx - sx) % sy === 0;
    }
    return false;
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
     * @return Boolean
     */
    function reachingPoints($sx, $sy, $tx, $ty) {
        while ($tx > $sx && $ty > $sy && $tx != $ty) {
            if ($tx > $ty) {
                $tx %= $ty;
            } else {
                $ty %= $tx;
            }
        }

        if ($tx == $sx && $ty == $sy) {
            return true;
        }

        if ($tx == $sx && $ty >= $sy && ($ty - $sy) % $sx == 0) {
            return true;
        }

        if ($ty == $sy && $tx >= $sx && ($tx - $sx) % $sy == 0) {
            return true;
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func reachingPoints(_ sx: Int, _ sy: Int, _ tx: Int, _ ty: Int) -> Bool {
        var curTx = tx
        var curTy = ty
        
        while curTx > sx && curTy > sy {
            if curTx > curTy {
                curTx %= curTy
                if curTx == 0 { curTx = curTy }
            } else {
                curTy %= curTx
                if curTy == 0 { curTy = curTx }
            }
        }
        
        if curTx == sx && curTy == sy {
            return true
        }
        if curTx == sx && curTy >= sy && (curTy - sy) % sx == 0 {
            return true
        }
        if curTy == sy && curTx >= sx && (curTx - sx) % sy == 0 {
            return true
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean {
        var tX = tx.toLong()
        var tY = ty.toLong()
        val sX = sx.toLong()
        val sY = sy.toLong()

        while (tX > sX && tY > sY) {
            if (tX > tY) {
                val mod = tX % tY
                tX = if (mod == 0L) tY else mod
            } else {
                val mod = tY % tX
                tY = if (mod == 0L) tX else mod
            }
        }

        if (tX == sX && tY >= sY && (tY - sY) % sX == 0L) return true
        if (tY == sY && tX >= sX && (tX - sX) % sY == 0L) return true
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool reachingPoints(int sx, int sy, int tx, int ty) {
    while (tx > sx && ty > sy && tx != ty) {
      if (tx > ty) {
        tx %= ty;
        if (tx == 0) tx = ty;
      } else {
        ty %= tx;
        if (ty == 0) ty = tx;
      }
    }
    if (tx == sx && ty == sy) return true;
    if (tx == sx) {
      return (ty - sy) % sx == 0 && ty >= sy;
    }
    if (ty == sy) {
      return (tx - sx) % sy == 0 && tx >= sx;
    }
    return false;
  }
}
```

## Golang

```go
func reachingPoints(sx int, sy int, tx int, ty int) bool {
	for tx >= sx && ty >= sy {
		if tx == sx && ty == sy {
			return true
		}
		if tx == sx {
			return (ty-sy)%sx == 0
		}
		if ty == sy {
			return (tx-sx)%sy == 0
		}
		if tx > ty {
			tx %= ty
			if tx == 0 {
				tx = ty
			}
		} else {
			ty %= tx
			if ty == 0 {
				ty = tx
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def reaching_points(sx, sy, tx, ty)
  while tx >= sx && ty >= sy
    return true if tx == sx && ty == sy

    if tx == sx
      return (ty - sy) % sx == 0
    end
    if ty == sy
      return (tx - sx) % sy == 0
    end

    if tx > ty
      tx %= ty
      tx = ty if tx == 0
    else
      ty %= tx
      ty = tx if ty == 0
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean = {
        var tX = tx.toLong
        var tY = ty.toLong
        val sX = sx.toLong
        val sY = sy.toLong

        while (tX > sX && tY > sY) {
            if (tX > tY) {
                tX %= tY
                if (tX == 0L) tX = tY
            } else {
                tY %= tX
                if (tY == 0L) tY = tX
            }
        }

        if (tX == sX && tY >= sY && ((tY - sY) % sX == 0)) true
        else if (tY == sY && tX >= sX && ((tX - sX) % sY == 0)) true
        else false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reaching_points(sx: i32, sy: i32, tx: i32, ty: i32) -> bool {
        let (mut sx, mut sy, mut tx, mut ty) = (sx as i64, sy as i64, tx as i64, ty as i64);
        while tx >= sx && ty >= sy {
            if tx == sx && ty == sy {
                return true;
            }
            if tx == sx {
                return (ty - sy) % sx == 0;
            }
            if ty == sy {
                return (tx - sx) % sy == 0;
            }
            if tx > ty {
                let r = tx % ty;
                tx = if r == 0 { ty } else { r };
            } else {
                let r = ty % tx;
                ty = if r == 0 { tx } else { r };
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (reaching-points sx sy tx ty)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? boolean?)
  (let loop ((tx tx) (ty ty))
    (cond
      [(and (= tx sx) (= ty sy)) #t]
      [(or (< tx sx) (< ty sy)) #f]
      [(= tx ty) #f]
      [(> tx ty)
       (if (> ty sy)
           (let ((r (remainder tx ty)))
             (loop (if (= r 0) ty r) ty))
           (and (= ty sy)
                (= (remainder (- tx sx) ty) 0)))]
      [(> ty tx)
       (if (> tx sx)
           (let ((r (remainder ty tx)))
             (loop tx (if (= r 0) tx r)))
           (and (= tx sx)
                (= (remainder (- ty sy) tx) 0)))))))
```

## Erlang

```erlang
-module(solution).
-export([reaching_points/4]).

-spec reaching_points(Sx :: integer(), Sy :: integer(), Tx :: integer(), Ty :: integer()) -> boolean().
reaching_points(Sx, Sy, Tx, Ty) ->
    if
        Tx < Sx orelse Ty < Sy ->
            false;
        true ->
            backtrack(Tx, Ty, Sx, Sy)
    end.

backtrack(Tx, Ty, Sx, Sy) when Tx > Sx, Ty > Sy, Tx =/= Ty ->
    case Tx > Ty of
        true ->
            NewTx = Tx rem Ty,
            case NewTx of
                0 -> backtrack(Ty, Ty, Sx, Sy);
                _ -> backtrack(NewTx, Ty, Sx, Sy)
            end;
        false ->
            NewTy = Ty rem Tx,
            case NewTy of
                0 -> backtrack(Tx, Tx, Sx, Sy);
                _ -> backtrack(Tx, NewTy, Sx, Sy)
            end
    end;
backtrack(Tx, Ty, Sx, Sy) ->
    (Tx =:= Sx andalso Ty >= Sy andalso ((Ty - Sy) rem Sx) =:= 0) orelse
    (Ty =:= Sy andalso Tx >= Sx andalso ((Tx - Sx) rem Sy) =:= 0).
```

## Elixir

```elixir
defmodule Solution do
  @spec reaching_points(sx :: integer, sy :: integer, tx :: integer, ty :: integer) :: boolean
  def reaching_points(sx, sy, tx, ty) do
    go(sx, sy, tx, ty)
  end

  defp go(sx, sy, tx, ty) do
    cond do
      tx == sx and ty == sy ->
        true

      tx < sx or ty < sy ->
        false

      tx == sx ->
        rem(ty - sy, sx) == 0

      ty == sy ->
        rem(tx - sx, sy) == 0

      tx > ty ->
        new_tx = rem(tx, ty)
        new_tx = if new_tx == 0, do: ty, else: new_tx
        go(sx, sy, new_tx, ty)

      true -> # ty > tx
        new_ty = rem(ty, tx)
        new_ty = if new_ty == 0, do: tx, else: new_ty
        go(sx, sy, tx, new_ty)
    end
  end
end
```
