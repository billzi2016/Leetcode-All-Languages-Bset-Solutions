# 0052. N-Queens II

## Cpp

```cpp
class Solution {
public:
    int totalNQueens(int n) {
        int limit = (1 << n) - 1;
        return solve(0, 0, 0, limit);
    }
private:
    int solve(int cols, int d1, int d2, int limit) {
        if (cols == limit) return 1; // all rows filled
        int count = 0;
        int available = ~(cols | d1 | d2) & limit;
        while (available) {
            int bit = available & -available;
            available -= bit;
            count += solve(cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1, limit);
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    private int size;
    private int solutions;

    public int totalNQueens(int n) {
        this.size = n;
        this.solutions = 0;
        solve(0, 0, 0, 0);
        return solutions;
    }

    private void solve(int row, int cols, int diag1, int diag2) {
        if (row == size) {
            solutions++;
            return;
        }
        int available = ((1 << size) - 1) & ~(cols | diag1 | diag2);
        while (available != 0) {
            int bit = available & -available; // rightmost 1-bit
            available -= bit;
            solve(row + 1,
                  cols | bit,
                  (diag1 | bit) << 1,
                  (diag2 | bit) >> 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        limit = (1 << n) - 1

        def backtrack(cols, diags, anti_diags):
            nonlocal count
            if cols == limit:
                # all rows filled
                count += 1
                return
            # positions available for current row
            avail = ~(cols | diags | anti_diags) & limit
            while avail:
                bit = avail & -avail
                avail -= bit
                backtrack(cols | bit,
                          (diags | bit) << 1,
                          (anti_diags | bit) >> 1)

        backtrack(0, 0, 0)
        return count
```

## Python3

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        limit = (1 << n) - 1
        count = 0

        def dfs(row: int, cols: int, d1: int, d2: int):
            nonlocal count
            if row == n:
                count += 1
                return
            avail = limit & ~(cols | d1 | d2)
            while avail:
                bit = avail & -avail
                avail -= bit
                dfs(row + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)

        dfs(0, 0, 0, 0)
        return count
```

## C

```c
int dfs(int n, int row, int cols, int d1, int d2) {
    if (row == n) return 1;
    int mask = (1 << n) - 1;
    int available = mask & ~(cols | d1 | d2);
    int count = 0;
    while (available) {
        int bit = available & -available;
        available -= bit;
        count += dfs(n, row + 1,
                     cols | bit,
                     (d1 | bit) << 1,
                     (d2 | bit) >> 1);
    }
    return count;
}

int totalNQueens(int n) {
    if (n <= 0) return 0;
    return dfs(n, 0, 0, 0, 0);
}
```

## Csharp

```csharp
public class Solution
{
    public int TotalNQueens(int n)
    {
        int count = 0;
        int limitMask = (1 << n) - 1;

        void Backtrack(int row, int cols, int d1, int d2)
        {
            if (row == n)
            {
                count++;
                return;
            }

            int available = (~(cols | d1 | d2)) & limitMask;
            while (available != 0)
            {
                int position = available & -available;
                available -= position;
                Backtrack(row + 1, cols | position, (d1 | position) << 1, (d2 | position) >> 1);
            }
        }

        Backtrack(0, 0, 0, 0);
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    let count = 0;
    const limit = (1 << n) - 1; // mask with lower n bits set to 1

    function backtrack(row, cols, d1, d2) {
        if (row === n) {
            count++;
            return;
        }
        // positions available for this row
        let avail = (~(cols | d1 | d2)) & limit;
        while (avail) {
            const bit = avail & -avail; // pick rightmost 1-bit
            avail ^= bit; // remove the picked bit
            backtrack(row + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1);
        }
    }

    backtrack(0, 0, 0, 0);
    return count;
};
```

## Typescript

```typescript
function totalNQueens(n: number): number {
    let count = 0;
    const limit = (1 << n) - 1;

    function backtrack(columns: number, diag1: number, diag2: number): void {
        if (columns === limit) {
            count++;
            return;
        }
        let available = ~(columns | diag1 | diag2) & limit;
        while (available) {
            const bit = available & -available;
            available -= bit;
            backtrack(columns | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1);
        }
    }

    backtrack(0, 0, 0);
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function totalNQueens($n) {
        $mask = (1 << $n) - 1;
        $count = 0;

        $dfs = function ($col, $diagL, $diagR) use (&$dfs, $mask, &$count) {
            if ($col == $mask) {
                $count++;
                return;
            }
            $available = $mask & (~($col | $diagL | $diagR));
            while ($available) {
                $bit = $available & (-$available);
                $available ^= $bit;
                $dfs($col | $bit, ($diagL | $bit) << 1, ($diagR | $bit) >> 1);
            }
        };

        $dfs(0, 0, 0);
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func totalNQueens(_ n: Int) -> Int {
        var count = 0
        let allOnes = (1 << n) - 1

        func solve(_ cols: Int, _ ld: Int, _ rd: Int) {
            if cols == allOnes {
                count += 1
                return
            }
            var available = (~(cols | ld | rd)) & allOnes
            while available != 0 {
                let bit = available & -available
                available ^= bit
                solve(cols | bit, (ld | bit) << 1, (rd | bit) >> 1)
            }
        }

        solve(0, 0, 0)
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalNQueens(n: Int): Int {
        var count = 0
        val limit = (1 shl n) - 1

        fun backtrack(columns: Int, diag1: Int, diag2: Int) {
            if (columns == limit) {
                count++
                return
            }
            var available = limit and (columns or diag1 or diag2).inv()
            while (available != 0) {
                val position = available and -available
                backtrack(columns or position,
                          (diag1 or position) shl 1,
                          (diag2 or position) ushr 1)
                available -= position
            }
        }

        backtrack(0, 0, 0)
        return count
    }
}
```

## Dart

```dart
class Solution {
  int totalNQueens(int n) {
    int count = 0;
    final int mask = (1 << n) - 1;

    void backtrack(int row, int cols, int d1, int d2) {
      if (row == n) {
        count++;
        return;
      }
      int available = mask & ~(cols | d1 | d2);
      while (available != 0) {
        int bit = available & -available;
        available ^= bit;
        backtrack(row + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1);
      }
    }

    backtrack(0, 0, 0, 0);
    return count;
  }
}
```

## Golang

```go
func totalNQueens(n int) int {
	var count int
	all := (1 << n) - 1

	var solve func(row, cols, diag, anti int)
	solve = func(row, cols, diag, anti int) {
		if row == n {
			count++
			return
		}
		available := ^(cols | diag | anti) & all
		for available != 0 {
			pos := available & -available
			available -= pos
			solve(row+1, cols|pos, (diag|pos)<<1, (anti|pos)>>1)
		}
	}

	solve(0, 0, 0, 0)
	return count
}
```

## Ruby

```ruby
def total_n_queens(n)
  limit = (1 << n) - 1
  count = 0
  dfs = nil
  dfs = ->(row, cols, d1, d2) do
    if row == n
      count += 1
      next
    end
    avail = ~(cols | d1 | d2) & limit
    while avail != 0
      bit = avail & -avail
      avail -= bit
      dfs.call(row + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)
    end
  end
  dfs.call(0, 0, 0, 0)
  count
end
```

## Scala

```scala
object Solution {
    def totalNQueens(n: Int): Int = {
        if (n == 0) return 0
        var count = 0
        val limit = (1 << n) - 1

        def backtrack(cols: Int, diag1: Int, diag2: Int): Unit = {
            if (cols == limit) {
                count += 1
                return
            }
            var available = ~(cols | diag1 | diag2) & limit
            while (available != 0) {
                val bit = available & -available
                available ^= bit
                backtrack(cols | bit, (diag1 | bit) << 1, (diag2 | bit) >>> 1)
            }
        }

        backtrack(0, 0, 0)
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn total_n_queens(n: i32) -> i32 {
        let n = n as usize;
        if n == 0 {
            return 0;
        }
        // bitmask with lowest n bits set to 1
        let all: u32 = (1u32 << n) - 1;

        fn dfs(row: usize, cols: u32, d1: u32, d2: u32, all: u32, n: usize, cnt: &mut i32) {
            if row == n {
                *cnt += 1;
                return;
            }
            let mut bits = !(cols | d1 | d2) & all;
            while bits != 0 {
                // isolate lowest set bit
                let bit = bits & (!bits).wrapping_add(1);
                bits ^= bit;
                dfs(
                    row + 1,
                    cols | bit,
                    (d1 | bit) << 1,
                    (d2 | bit) >> 1,
                    all,
                    n,
                    cnt,
                );
            }
        }

        let mut ans = 0;
        dfs(0, 0, 0, 0, all, n, &mut ans);
        ans
    }
}
```

## Racket

```racket
(define/contract (total-n-queens n)
  (-> exact-integer? exact-integer?)
  (let* ((all (- (arithmetic-shift 1 n) 1))) ; mask with n low bits set
    (letrec ((solve (lambda (row cols d1 d2)
                      (if (= row n)
                          1
                          (let loop ((pos (bitwise-and (bitwise-not (bitwise-ior cols d1 d2)) all))
                                     (cnt 0))
                            (if (= pos 0)
                                cnt
                                (let* ((bit (bitwise-and pos (- pos))) ; lowest set bit
                                       (next-pos (bitwise-xor pos bit)))
                                  (loop next-pos
                                        (+ cnt
                                           (solve (+ row 1)
                                                  (bitwise-ior cols bit)
                                                  (bitwise-ior (arithmetic-shift d1 1) bit)
                                                  (bitwise-ior (arithmetic-shift d2 -1) bit)))))))))))
      (solve 0 0 0 0))))
```

## Erlang

```erlang
-module(solution).
-export([total_n_queens/1]).

-spec total_n_queens(N :: integer()) -> integer().
total_n_queens(N) ->
    count(N, 0, 0, 0, 0).

count(N, Row, _Columns, _DiagL, _DiagR) when Row == N ->
    1;
count(N, Row, Columns, DiagL, DiagR) ->
    All = (1 bsl N) - 1,
    Available = All band bnot(Columns bor DiagL bor DiagR),
    count_positions(Available, N, Row, Columns, DiagL, DiagR).

count_positions(0, _N, _Row, _Columns, _DiagL, _DiagR) ->
    0;
count_positions(Avail, N, Row, Columns, DiagL, DiagR) ->
    P = Avail band -Avail,
    Rest = Avail band bnot(P),
    CountHere = count(N, Row + 1, Columns bor P, (DiagL bor P) bsl 1, (DiagR bor P) bsr 1),
    CountRest = count_positions(Rest, N, Row, Columns, DiagL, DiagR),
    CountHere + CountRest.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec total_n_queens(n :: integer) :: integer
  def total_n_queens(n) when n >= 1 do
    all = (1 <<< n) - 1
    backtrack(0, n, 0, 0, 0, all)
  end

  defp backtrack(row, n, _cols, _d1, _d2, _all) when row == n, do: 1

  defp backtrack(row, n, cols, d1, d2, all) do
    available = all &&& bnot (cols ||| d1 ||| d2)
    count_available(available, row, n, cols, d1, d2, all, 0)
  end

  defp count_available(0, _row, _n, _cols, _d1, _d2, _all, acc), do: acc

  defp count_available(avail, row, n, cols, d1, d2, all, acc) do
    p = avail &&& -avail
    new_avail = avail &&& (avail - 1)

    acc =
      acc +
        backtrack(
          row + 1,
          n,
          cols ||| p,
          (d1 ||| p) <<< 1,
          (d2 ||| p) >>> 1,
          all
        )

    count_available(new_avail, row, n, cols, d1, d2, all, acc)
  end
end
```
