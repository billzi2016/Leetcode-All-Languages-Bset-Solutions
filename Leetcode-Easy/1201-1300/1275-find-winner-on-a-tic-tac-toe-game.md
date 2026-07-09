# 1275. Find Winner on a Tic Tac Toe Game

## Cpp

```cpp
class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        int rows[2][3] = {}, cols[2][3] = {};
        int diag[2] = {}, antiDiag[2] = {};
        for (int i = 0; i < moves.size(); ++i) {
            int player = i % 2; // 0 -> A, 1 -> B
            int r = moves[i][0], c = moves[i][1];
            rows[player][r]++;
            cols[player][c]++;
            if (r == c) diag[player]++;
            if (r + c == 2) antiDiag[player]++;
            if (rows[player][r] == 3 || cols[player][c] == 3 ||
                diag[player] == 3 || antiDiag[player] == 3) {
                return player == 0 ? "A" : "B";
            }
        }
        return moves.size() == 9 ? "Draw" : "Pending";
    }
};
```

## Java

```java
class Solution {
    public String tictactoe(int[][] moves) {
        int[][] rows = new int[2][3];
        int[][] cols = new int[2][3];
        int[] diag = new int[2];
        int[] antiDiag = new int[2];
        
        for (int i = 0; i < moves.length; i++) {
            int player = i % 2; // 0 -> A, 1 -> B
            int r = moves[i][0];
            int c = moves[i][1];
            
            rows[player][r]++;
            cols[player][c]++;
            if (r == c) diag[player]++;
            if (r + c == 2) antiDiag[player]++;
            
            if (rows[player][r] == 3 || cols[player][c] == 3 ||
                diag[player] == 3 || antiDiag[player] == 3) {
                return player == 0 ? "A" : "B";
            }
        }
        
        return moves.length == 9 ? "Draw" : "Pending";
    }
}
```

## Python

```python
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti = 0

        for i, (r, c) in enumerate(moves):
            player = 1 if i % 2 == 0 else -1  # A: +1, B: -1
            rows[r] += player
            cols[c] += player
            if r == c:
                diag += player
            if r + c == 2:
                anti += player

            if (abs(rows[r]) == 3 or abs(cols[c]) == 3 or
                abs(diag) == 3 or abs(anti) == 3):
                return "A" if player == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"
```

## Python3

```python
from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [[0] * 3 for _ in range(2)]
        cols = [[0] * 3 for _ in range(2)]
        diag = [0, 0]
        anti = [0, 0]

        for i, (r, c) in enumerate(moves):
            player = i % 2  # 0 for A, 1 for B
            rows[player][r] += 1
            cols[player][c] += 1
            if r == c:
                diag[player] += 1
            if r + c == 2:
                anti[player] += 1

            if (rows[player][r] == 3 or
                cols[player][c] == 3 or
                diag[player] == 3 or
                anti[player] == 3):
                return "A" if player == 0 else "B"

        return "Draw" if len(moves) == 9 else "Pending"
```

## C

```c
char* tictactoe(int** moves, int movesSize, int* movesColSize){
    int rowsA[3] = {0}, colsA[3] = {0}, diagA = 0, antiA = 0;
    int rowsB[3] = {0}, colsB[3] = {0}, diagB = 0, antiB = 0;
    for (int i = 0; i < movesSize; ++i) {
        int r = moves[i][0];
        int c = moves[i][1];
        if ((i & 1) == 0) { // Player A
            rowsA[r]++; colsA[c]++;
            if (r == c) diagA++;
            if (r + c == 2) antiA++;
            if (rowsA[r] == 3 || colsA[c] == 3 || diagA == 3 || antiA == 3)
                return "A";
        } else { // Player B
            rowsB[r]++; colsB[c]++;
            if (r == c) diagB++;
            if (r + c == 2) antiB++;
            if (rowsB[r] == 3 || colsB[c] == 3 || diagB == 3 || antiB == 3)
                return "B";
        }
    }
    return movesSize == 9 ? "Draw" : "Pending";
}
```

## Csharp

```csharp
public class Solution
{
    public string Tictactoe(int[][] moves)
    {
        // rows[player][row], cols[player][col]
        int[,] rows = new int[2, 3];
        int[,] cols = new int[2, 3];
        int[] diag = new int[2];
        int[] antiDiag = new int[2];

        for (int i = 0; i < moves.Length; i++)
        {
            int player = i % 2; // 0 for A, 1 for B
            int r = moves[i][0];
            int c = moves[i][1];

            rows[player, r]++;
            cols[player, c]++;

            if (r == c) diag[player]++;
            if (r + c == 2) antiDiag[player]++;

            if (rows[player, r] == 3 || cols[player, c] == 3 ||
                diag[player] == 3 || antiDiag[player] == 3)
            {
                return player == 0 ? "A" : "B";
            }
        }

        return moves.Length == 9 ? "Draw" : "Pending";
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function(moves) {
    const rowsA = [0, 0, 0];
    const colsA = [0, 0, 0];
    let diagA = 0;
    let antiDiagA = 0;

    const rowsB = [0, 0, 0];
    const colsB = [0, 0, 0];
    let diagB = 0;
    let antiDiagB = 0;

    for (let i = 0; i < moves.length; i++) {
        const [r, c] = moves[i];
        if (i % 2 === 0) { // A's move
            rowsA[r]++; colsA[c]++;
            if (r === c) diagA++;
            if (r + c === 2) antiDiagA++;
            if (rowsA[r] === 3 || colsA[c] === 3 || diagA === 3 || antiDiagA === 3) {
                return "A";
            }
        } else { // B's move
            rowsB[r]++; colsB[c]++;
            if (r === c) diagB++;
            if (r + c === 2) antiDiagB++;
            if (rowsB[r] === 3 || colsB[c] === 3 || diagB === 3 || antiDiagB === 3) {
                return "B";
            }
        }
    }

    return moves.length === 9 ? "Draw" : "Pending";
};
```

## Typescript

```typescript
function tictactoe(moves: number[][]): string {
    const rows = Array.from({ length: 2 }, () => [0, 0, 0]);
    const cols = Array.from({ length: 2 }, () => [0, 0, 0]);
    const diag = [0, 0];
    const anti = [0, 0];

    for (let i = 0; i < moves.length; i++) {
        const player = i % 2; // 0 -> A, 1 -> B
        const [r, c] = moves[i];
        rows[player][r]++;
        cols[player][c]++;
        if (r === c) diag[player]++;
        if (r + c === 2) anti[player]++;

        if (
            rows[player][r] === 3 ||
            cols[player][c] === 3 ||
            diag[player] === 3 ||
            anti[player] === 3
        ) {
            return player === 0 ? "A" : "B";
        }
    }

    return moves.length === 9 ? "Draw" : "Pending";
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $moves
     * @return String
     */
    function tictactoe($moves) {
        $rows = [array_fill(0, 3, 0), array_fill(0, 3, 0)];
        $cols = [array_fill(0, 3, 0), array_fill(0, 3, 0)];
        $diag = [0, 0];
        $anti = [0, 0];

        foreach ($moves as $i => $move) {
            $player = $i % 2; // 0 for A, 1 for B
            $r = $move[0];
            $c = $move[1];

            $rows[$player][$r]++;
            $cols[$player][$c]++;

            if ($r == $c) {
                $diag[$player]++;
            }
            if ($r + $c == 2) {
                $anti[$player]++;
            }

            if (
                $rows[$player][$r] == 3 ||
                $cols[$player][$c] == 3 ||
                $diag[$player] == 3 ||
                $anti[$player] == 3
            ) {
                return $player === 0 ? "A" : "B";
            }
        }

        return count($moves) == 9 ? "Draw" : "Pending";
    }
}
```

## Swift

```swift
class Solution {
    func tictactoe(_ moves: [[Int]]) -> String {
        var rows = Array(repeating: Array(repeating: 0, count: 3), count: 2)
        var cols = Array(repeating: Array(repeating: 0, count: 3), count: 2)
        var diag = [0, 0]
        var antiDiag = [0, 0]
        
        for (i, move) in moves.enumerated() {
            let player = i % 2   // 0 for A, 1 for B
            let r = move[0]
            let c = move[1]
            
            rows[player][r] += 1
            cols[player][c] += 1
            if r == c { diag[player] += 1 }
            if r + c == 2 { antiDiag[player] += 1 }
            
            if rows[player][r] == 3 || cols[player][c] == 3 || diag[player] == 3 || antiDiag[player] == 3 {
                return player == 0 ? "A" : "B"
            }
        }
        
        return moves.count == 9 ? "Draw" : "Pending"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun tictactoe(moves: Array<IntArray>): String {
        val rows = Array(2) { IntArray(3) }
        val cols = Array(2) { IntArray(3) }
        val diag = IntArray(2)
        val antiDiag = IntArray(2)

        for (i in moves.indices) {
            val player = i % 2 // 0 for A, 1 for B
            val r = moves[i][0]
            val c = moves[i][1]

            rows[player][r]++
            cols[player][c]++

            if (r == c) diag[player]++
            if (r + c == 2) antiDiag[player]++

            if (rows[player][r] == 3 ||
                cols[player][c] == 3 ||
                diag[player] == 3 ||
                antiDiag[player] == 3) {
                return if (player == 0) "A" else "B"
            }
        }

        return if (moves.size == 9) "Draw" else "Pending"
    }
}
```

## Dart

```dart
class Solution {
  String tictactoe(List<List<int>> moves) {
    var rows = List.generate(2, (_) => List.filled(3, 0));
    var cols = List.generate(2, (_) => List.filled(3, 0));
    var diag = List.filled(2, 0);
    var antiDiag = List.filled(2, 0);

    for (int i = 0; i < moves.length; i++) {
      int player = i % 2; // 0 -> A, 1 -> B
      int r = moves[i][0];
      int c = moves[i][1];

      rows[player][r]++;
      cols[player][c]++;

      if (r == c) diag[player]++;
      if (r + c == 2) antiDiag[player]++;

      if (rows[player][r] == 3 ||
          cols[player][c] == 3 ||
          diag[player] == 3 ||
          antiDiag[player] == 3) {
        return player == 0 ? "A" : "B";
      }
    }

    return moves.length == 9 ? "Draw" : "Pending";
  }
}
```

## Golang

```go
func tictactoe(moves [][]int) string {
	rowsA := [3]int{}
	colsA := [3]int{}
	diagA, antiDiagA := 0, 0
	rowsB := [3]int{}
	colsB := [3]int{}
	diagB, antiDiagB := 0, 0

	for i, mv := range moves {
		r, c := mv[0], mv[1]
		if i%2 == 0 { // Player A
			rowsA[r]++
			colsA[c]++
			if r == c {
				diagA++
			}
			if r+c == 2 {
				antiDiagA++
			}
			if rowsA[r] == 3 || colsA[c] == 3 || diagA == 3 || antiDiagA == 3 {
				return "A"
			}
		} else { // Player B
			rowsB[r]++
			colsB[c]++
			if r == c {
				diagB++
			}
			if r+c == 2 {
				antiDiagB++
			}
			if rowsB[r] == 3 || colsB[c] == 3 || diagB == 3 || antiDiagB == 3 {
				return "B"
			}
		}
	}

	if len(moves) == 9 {
		return "Draw"
	}
	return "Pending"
}
```

## Ruby

```ruby
def tictactoe(moves)
  rows = Array.new(2) { [0, 0, 0] }
  cols = Array.new(2) { [0, 0, 0] }
  diag = [0, 0]
  anti = [0, 0]

  moves.each_with_index do |(r, c), i|
    p = i % 2
    rows[p][r] += 1
    cols[p][c] += 1
    diag[p] += 1 if r == c
    anti[p] += 1 if r + c == 2
    return p.zero? ? "A" : "B" if rows[p][r] == 3 || cols[p][c] == 3 || diag[p] == 3 || anti[p] == 3
  end

  moves.size == 9 ? "Draw" : "Pending"
end
```

## Scala

```scala
object Solution {
    def tictactoe(moves: Array[Array[Int]]): String = {
        val rows = Array.ofDim[Int](2, 3)
        val cols = Array.ofDim[Int](2, 3)
        val diag = Array(0, 0)
        val anti = Array(0, 0)

        for (i <- moves.indices) {
            val player = i % 2 // 0 -> A, 1 -> B
            val r = moves(i)(0)
            val c = moves(i)(1)

            rows(player)(r) += 1
            cols(player)(c) += 1
            if (r == c) diag(player) += 1
            if (r + c == 2) anti(player) += 1

            if (rows(player)(r) == 3 || cols(player)(c) == 3 || diag(player) == 3 || anti(player) == 3) {
                return if (player == 0) "A" else "B"
            }
        }

        if (moves.length == 9) "Draw" else "Pending"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn tictactoe(moves: Vec<Vec<i32>>) -> String {
        let mut rows = [[0i32; 3]; 2];
        let mut cols = [[0i32; 3]; 2];
        let mut diag = [0i32; 2];
        let mut anti = [0i32; 2];

        for (i, mv) in moves.iter().enumerate() {
            let r = mv[0] as usize;
            let c = mv[1] as usize;
            let p = i % 2; // 0 -> A, 1 -> B

            rows[p][r] += 1;
            cols[p][c] += 1;
            if r == c {
                diag[p] += 1;
            }
            if r + c == 2 {
                anti[p] += 1;
            }

            if rows[p][r] == 3 || cols[p][c] == 3 || diag[p] == 3 || anti[p] == 3 {
                return if p == 0 { "A".to_string() } else { "B".to_string() };
            }
        }

        if moves.len() == 9 {
            "Draw".to_string()
        } else {
            "Pending".to_string()
        }
    }
}
```

## Racket

```racket
(define/contract (tictactoe moves)
  (-> (listof (listof exact-integer?)) string?)
  (let* ([len (length moves)]
         [rows (make-vector 3 0)]
         [cols (make-vector 3 0)]
         [diag 0]
         [anti 0])
    (for ([i (in-range len)])
      (define move (list-ref moves i))
      (define r (first move))
      (define c (second move))
      (define player (if (even? i) 1 -1))
      (vector-set! rows r (+ (vector-ref rows r) player))
      (vector-set! cols c (+ (vector-ref cols c) player))
      (when (= r c)
        (set! diag (+ diag player)))
      (when (= (+ r c) 2)
        (set! anti (+ anti player))))
    (define (check-val v)
      (cond [(= v 3) "A"]
            [(= v -3) "B"]
            [else #f]))
    (let loop ((idx 0) (result #f))
      (if result
          result
          (if (< idx 3)
              (let ([rval (check-val (vector-ref rows idx))]
                    [cval (check-val (vector-ref cols idx))])
                (cond [rval rval]
                      [cval cval]
                      [else (loop (add1 idx) #f)]))
              (let ([dval (check-val diag)]
                    [aval (check-val anti)])
                (cond [dval dval]
                      [aval aval]
                      [(= len 9) "Draw"]
                      [else "Pending"])))))))
```

## Erlang

```erlang
-export([tictactoe/1]).
-spec tictactoe(Moves :: [[integer()]]) -> unicode:unicode_binary().
tictactoe(Moves) ->
    Len = length(Moves),
    EmptyCounts = #{rows => [0,0,0], cols => [0,0,0], diag => 0, anti => 0},
    tictactoe_loop(Moves, 0, Len, EmptyCounts, EmptyCounts).

tictactoe_loop([], _Idx, Len, _A, _B) ->
    case Len of
        9 -> <<"Draw">>;
        _ -> <<"Pending">>
    end;
tictactoe_loop([[R,C]|Rest], Idx, Len, ACounts, BCounts) ->
    Player = if (Idx rem 2) =:= 0 -> a; true -> b end,
    case Player of
        a ->
            NewA = update_counts(ACounts, R, C),
            case check_win(NewA) of
                true -> <<"A">>;
                false -> tictactoe_loop(Rest, Idx+1, Len, NewA, BCounts)
            end;
        b ->
            NewB = update_counts(BCounts, R, C),
            case check_win(NewB) of
                true -> <<"B">>;
                false -> tictactoe_loop(Rest, Idx+1, Len, ACounts, NewB)
            end
    end.

update_counts(Counts, R, C) ->
    Rows = maps:get(rows, Counts),
    Cols = maps:get(cols, Counts),
    Diag = maps:get(diag, Counts),
    Anti = maps:get(anti, Counts),

    NewRows = inc_nth(Rows, R+1),
    NewCols = inc_nth(Cols, C+1),
    NewDiag = if R =:= C -> Diag + 1; true -> Diag end,
    NewAnti = if R + C =:= 2 -> Anti + 1; true -> Anti end,

    #{rows => NewRows, cols => NewCols, diag => NewDiag, anti => NewAnti}.

inc_nth([H|T], 1) ->
    [H+1|T];
inc_nth([H|T], N) when N > 1 ->
    [H|inc_nth(T, N-1)].

check_win(Counts) ->
    Rows = maps:get(rows, Counts),
    Cols = maps:get(cols, Counts),
    Diag = maps:get(diag, Counts),
    Anti = maps:get(anti, Counts),

    lists:any(fun(X) -> X =:= 3 end, Rows) orelse
    lists:any(fun(X) -> X =:= 3 end, Cols) orelse
    Diag =:= 3 orelse
    Anti =:= 3.
```

## Elixir

```elixir
defmodule Solution do
  @spec tictactoe(moves :: [[integer]]) :: String.t()
  def tictactoe(moves) do
    rows = %{0 => 0, 1 => 0, 2 => 0}
    cols = %{0 => 0, 1 => 0, 2 => 0}

    result =
      Enum.reduce_while(Enum.with_index(moves), {rows, cols, 0, 0}, fn {[r, c], idx},
                                                                   {rows_acc, cols_acc,
                                                                    diag_acc, anti_acc} ->
        delta = if rem(idx, 2) == 0, do: 1, else: -1

        rows_acc = Map.update!(rows_acc, r, &(&1 + delta))
        cols_acc = Map.update!(cols_acc, c, &(&1 + delta))

        diag_acc = if r == c, do: diag_acc + delta, else: diag_acc
        anti_acc = if r + c == 2, do: anti_acc + delta, else: anti_acc

        if abs(rows_acc[r]) == 3 or abs(cols_acc[c]) == 3 or abs(diag_acc) == 3 or
             abs(anti_acc) == 3 do
          winner = if delta == 1, do: "A", else: "B"
          {:halt, {winner}}
        else
          {:cont, {rows_acc, cols_acc, diag_acc, anti_acc}}
        end
      end)

    case result do
      {winner} when winner in ["A", "B"] -> winner
      _ ->
        if length(moves) == 9, do: "Draw", else: "Pending"
    end
  end
end
```
