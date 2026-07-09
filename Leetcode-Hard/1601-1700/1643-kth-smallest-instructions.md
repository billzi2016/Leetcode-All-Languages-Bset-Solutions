# 1643. Kth Smallest Instructions

## Cpp

```cpp
class Solution {
public:
    string kthSmallestPath(vector<int>& destination, int k) {
        int row = destination[0];
        int col = destination[1];
        const int MAXN = 31;
        long long C[MAXN][MAXN] = {};
        for (int i = 0; i < MAXN; ++i) {
            C[i][0] = C[i][i] = 1;
            for (int j = 1; j < i; ++j) {
                C[i][j] = C[i-1][j-1] + C[i-1][j];
            }
        }
        long long kk = k;
        string ans;
        while (row > 0 || col > 0) {
            if (col == 0) { // only V moves left
                ans.push_back('V');
                --row;
                continue;
            }
            if (row == 0) { // only H moves left
                ans.push_back('H');
                --col;
                continue;
            }
            long long cnt = C[row + col - 1][row]; // ways if we place 'H' now
            if (kk <= cnt) {
                ans.push_back('H');
                --col;
            } else {
                ans.push_back('V');
                kk -= cnt;
                --row;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final long[][] C = new long[31][31];
    
    static {
        for (int n = 0; n <= 30; n++) {
            C[n][0] = C[n][n] = 1;
            for (int k = 1; k < n; k++) {
                C[n][k] = C[n - 1][k - 1] + C[n - 1][k];
                if (C[n][k] > Long.MAX_VALUE) C[n][k] = Long.MAX_VALUE;
            }
        }
    }
    
    public String kthSmallestPath(int[] destination, int k) {
        int row = destination[0];   // number of 'V'
        int col = destination[1];   // number of 'H'
        long kk = k;                // use long for safety
        StringBuilder sb = new StringBuilder();
        
        while (row > 0 && col > 0) {
            long cnt = C[row + col - 1][row]; // ways if we put 'H' now
            if (kk <= cnt) {
                sb.append('H');
                col--;
            } else {
                sb.append('V');
                kk -= cnt;
                row--;
            }
        }
        while (col > 0) {
            sb.append('H');
            col--;
        }
        while (row > 0) {
            sb.append('V');
            row--;
        }
        return sb.toString();
    }
}
```

## Python

```python
import math

class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        row, col = destination[0], destination[1]  # vertical moves (V) and horizontal moves (H)
        v, h = row, col
        res = []
        while v > 0 and h > 0:
            cnt = math.comb(v + h - 1, h - 1)  # sequences starting with 'H'
            if k <= cnt:
                res.append('H')
                h -= 1
            else:
                res.append('V')
                k -= cnt
                v -= 1
        res.extend(['H'] * h)
        res.extend(['V'] * v)
        return ''.join(res)
```

## Python3

```python
import math
from typing import List

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, col = destination[0], destination[1]  # V moves, H moves
        res = []
        while row > 0 or col > 0:
            if col == 0:
                res.append('V')
                row -= 1
                continue
            if row == 0:
                res.append('H')
                col -= 1
                continue
            # number of sequences that start with 'H'
            cnt = math.comb(row + col - 1, row)
            if k <= cnt:
                res.append('H')
                col -= 1
            else:
                res.append('V')
                k -= cnt
                row -= 1
        return ''.join(res)
```

## C

```c
#include <stdlib.h>

static unsigned long long C[31][31];

static void init_comb(void) {
    for (int n = 0; n <= 30; ++n) {
        C[n][0] = C[n][n] = 1ULL;
        for (int r = 1; r < n; ++r) {
            C[n][r] = C[n-1][r-1] + C[n-1][r];
        }
    }
}

/* Return the k-th lexicographically smallest path consisting of
   'H' (right) and 'V' (down) moves that reaches (row, column). */
char* kthSmallestPath(int* destination, int destinationSize, int k) {
    if (C[0][0] == 0) init_comb();          // lazy initialization

    int row = destination[0];
    int col = destination[1];
    int total = row + col;

    char *res = (char *)malloc((total + 1) * sizeof(char));
    int pos = 0;
    unsigned long long kk = (unsigned long long)k;   // use 64‑bit for safety

    while (row > 0 || col > 0) {
        if (col == 0) {               // only 'V' moves remain
            res[pos++] = 'V';
            --row;
        } else if (row == 0) {        // only 'H' moves remain
            res[pos++] = 'H';
            --col;
        } else {
            unsigned long long cnt = C[row + col - 1][col - 1]; // paths starting with 'H'
            if (kk <= cnt) {
                res[pos++] = 'H';
                --col;
            } else {
                kk -= cnt;
                res[pos++] = 'V';
                --row;
            }
        }
    }

    res[total] = '\0';
    return res;
}
```

## Csharp

```csharp
using System;
using System.Text;

public class Solution {
    public string KthSmallestPath(int[] destination, int k) {
        int v = destination[0];
        int h = destination[1];
        int n = h + v;
        long[,] comb = new long[n + 1, n + 1];
        for (int i = 0; i <= n; i++) {
            comb[i, 0] = comb[i, i] = 1;
            for (int j = 1; j < i; j++) {
                comb[i, j] = comb[i - 1, j - 1] + comb[i - 1, j];
            }
        }

        StringBuilder sb = new StringBuilder();
        long kk = k;
        while (h > 0 || v > 0) {
            if (h == 0) {
                sb.Append('V');
                v--;
                continue;
            }
            if (v == 0) {
                sb.Append('H');
                h--;
                continue;
            }

            long cnt = comb[h + v - 1, h - 1];
            if (kk <= cnt) {
                sb.Append('H');
                h--;
            } else {
                sb.Append('V');
                kk -= cnt;
                v--;
            }
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} destination
 * @param {number} k
 * @return {string}
 */
var kthSmallestPath = function(destination, k) {
    const rows = destination[0];
    const cols = destination[1];
    const total = rows + cols;
    
    // Precompute binomial coefficients up to total (<=30)
    const comb = Array.from({length: total + 1}, () => Array(total + 1).fill(0));
    for (let i = 0; i <= total; i++) {
        comb[i][0] = comb[i][i] = 1;
        for (let j = 1; j < i; j++) {
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
        }
    }
    
    let r = rows, c = cols;
    let kk = k;
    const res = [];
    
    while (r > 0 || c > 0) {
        if (c === 0) { // only V's left
            res.push('V');
            r--;
            continue;
        }
        if (r === 0) { // only H's left
            res.push('H');
            c--;
            continue;
        }
        const countIfH = comb[r + c - 1][r]; // ways after placing 'H'
        if (kk <= countIfH) {
            res.push('H');
            c--;
        } else {
            res.push('V');
            kk -= countIfH;
            r--;
        }
    }
    
    return res.join('');
};
```

## Typescript

```typescript
function kthSmallestPath(destination: number[], k: number): string {
    const [row, col] = destination;
    const maxN = row + col;
    const comb: number[][] = Array.from({ length: maxN + 1 }, () => Array(maxN + 1).fill(0));
    for (let i = 0; i <= maxN; i++) {
        comb[i][0] = comb[i][i] = 1;
        for (let j = 1; j < i; j++) {
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
        }
    }

    let h = col, v = row;
    let result = '';
    while (h > 0 || v > 0) {
        if (h === 0) {
            result += 'V';
            v--;
        } else if (v === 0) {
            result += 'H';
            h--;
        } else {
            const cnt = comb[h + v - 1][h - 1];
            if (k <= cnt) {
                result += 'H';
                h--;
            } else {
                result += 'V';
                v--;
                k -= cnt;
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $destination
     * @param Integer $k
     * @return String
     */
    function kthSmallestPath($destination, $k) {
        $row = $destination[0];
        $col = $destination[1];
        $max = $row + $col;

        // Precompute binomial coefficients up to max using Pascal's triangle
        $comb = array_fill(0, $max + 1, []);
        for ($i = 0; $i <= $max; $i++) {
            $comb[$i][0] = 1;
            $comb[$i][$i] = 1;
            for ($j = 1; $j < $i; $j++) {
                $comb[$i][$j] = $comb[$i - 1][$j - 1] + $comb[$i - 1][$j];
            }
        }

        $result = '';
        while ($row > 0 && $col > 0) {
            // Number of sequences if we place 'H' now
            $cnt = $comb[$row + $col - 1][$row]; // choose positions for remaining V's
            if ($k <= $cnt) {
                $result .= 'H';
                $col--;
            } else {
                $result .= 'V';
                $k -= $cnt;
                $row--;
            }
        }

        if ($col > 0) {
            $result .= str_repeat('H', $col);
        }
        if ($row > 0) {
            $result .= str_repeat('V', $row);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func kthSmallestPath(_ destination: [Int], _ k: Int) -> String {
        let row = destination[0]
        let col = destination[1]
        var comb = Array(repeating: Array(repeating: UInt64(0), count: 31), count: 31)
        for i in 0...30 {
            comb[i][0] = 1
            comb[i][i] = 1
            if i > 0 {
                for j in 1..<i {
                    comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
                }
            }
        }
        
        var h = col
        var v = row
        var kVar = UInt64(k)
        var result = ""
        
        while h > 0 || v > 0 {
            if h == 0 {
                result.append("V")
                v -= 1
            } else if v == 0 {
                result.append("H")
                h -= 1
            } else {
                let count = comb[h + v - 1][v] // sequences starting with 'H'
                if kVar <= count {
                    result.append("H")
                    h -= 1
                } else {
                    result.append("V")
                    kVar -= count
                    v -= 1
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthSmallestPath(destination: IntArray, k: Int): String {
        val row = destination[0]
        val col = destination[1]
        val n = row + col
        val comb = Array(n + 1) { LongArray(n + 1) }
        for (i in 0..n) {
            comb[i][0] = 1L
            comb[i][i] = 1L
            for (j in 1 until i) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
            }
        }

        var h = col
        var v = row
        var kk = k.toLong()
        val sb = StringBuilder()
        while (h > 0 && v > 0) {
            val count = comb[h + v - 1][h - 1] // strings starting with 'H'
            if (kk <= count) {
                sb.append('H')
                h--
            } else {
                sb.append('V')
                v--
                kk -= count
            }
        }
        repeat(h) { sb.append('H') }
        repeat(v) { sb.append('V') }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String kthSmallestPath(List<int> destination, int k) {
    const int maxN = 30;
    List<List<int>> comb = List.generate(maxN + 1,
        (_) => List.filled(maxN + 1, 0, growable: false),
        growable: false);
    for (int i = 0; i <= maxN; ++i) {
      comb[i][0] = comb[i][i] = 1;
      for (int j = 1; j < i; ++j) {
        comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
      }
    }

    int row = destination[0];
    int col = destination[1];
    StringBuffer sb = StringBuffer();

    while (row > 0 && col > 0) {
      // number of paths that start with 'H'
      int count = comb[row + col - 1][row];
      if (k <= count) {
        sb.write('H');
        col--;
      } else {
        sb.write('V');
        k -= count;
        row--;
      }
    }

    while (col > 0) {
      sb.write('H');
      col--;
    }
    while (row > 0) {
      sb.write('V');
      row--;
    }

    return sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func kthSmallestPath(destination []int, k int) string {
	row, col := destination[0], destination[1]
	n := row + col
	comb := make([][]int64, n+1)
	for i := 0; i <= n; i++ {
		comb[i] = make([]int64, i+1)
		comb[i][0], comb[i][i] = 1, 1
		for j := 1; j < i; j++ {
			comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
		}
	}

	var sb strings.Builder
	r, c := row, col
	kk := int64(k)
	for r > 0 && c > 0 {
		cnt := comb[r+c-1][r] // ways if we put 'H' now
		if kk <= cnt {
			sb.WriteByte('H')
			c--
		} else {
			sb.WriteByte('V')
			r--
			kk -= cnt
		}
	}
	for c > 0 {
		sb.WriteByte('H')
		c--
	}
	for r > 0 {
		sb.WriteByte('V')
		r--
	}
	return sb.String()
}
```

## Ruby

```ruby
def kth_smallest_path(destination, k)
  row, col = destination
  n = row + col
  comb = Array.new(n + 1) { Array.new(n + 1, 0) }
  (0..n).each do |i|
    comb[i][0] = comb[i][i] = 1
    (1...i).each do |j|
      comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
    end
  end

  result = +''
  while row > 0 && col > 0
    count_h = comb[row + col - 1][row]
    if k <= count_h
      result << 'H'
      col -= 1
    else
      result << 'V'
      k -= count_h
      row -= 1
    end
  end

  result << 'H' * col
  result << 'V' * row
  result
end
```

## Scala

```scala
object Solution {
    private val MAX = 31
    private val comb: Array[Array[Long]] = Array.ofDim[Long](MAX + 1, MAX + 1)

    // Precompute binomial coefficients up to 30 choose 15 (fits in Long)
    init()

    private def init(): Unit = {
        for (i <- 0 to MAX) {
            comb(i)(0) = 1L
            comb(i)(i) = 1L
            var j = 1
            while (j < i) {
                comb(i)(j) = comb(i - 1)(j - 1) + comb(i - 1)(j)
                j += 1
            }
        }
    }

    def kthSmallestPath(destination: Array[Int], k: Int): String = {
        var h = destination(1) // number of 'H' moves (right)
        var v = destination(0) // number of 'V' moves (down)
        var kk = k.toLong
        val sb = new StringBuilder

        while (h > 0 || v > 0) {
            if (h == 0) {
                sb.append('V')
                v -= 1
            } else if (v == 0) {
                sb.append('H')
                h -= 1
            } else {
                // Number of sequences that start with 'H' given remaining moves
                val count = comb(h + v - 1)(v)
                if (kk <= count) {
                    sb.append('H')
                    h -= 1
                } else {
                    sb.append('V')
                    kk -= count
                    v -= 1
                }
            }
        }

        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_smallest_path(destination: Vec<i32>, k: i32) -> String {
        let rows = destination[0] as usize;
        let cols = destination[1] as usize;
        let max_n = rows + cols;

        // Pascal's triangle for combinations
        let mut comb = vec![vec![0u64; max_n + 1]; max_n + 1];
        for i in 0..=max_n {
            comb[i][0] = 1;
            comb[i][i] = 1;
            for j in 1..i {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            }
        }

        let mut v = rows;
        let mut h = cols;
        let mut kk = k as u64;
        let mut result = String::new();

        while v > 0 && h > 0 {
            // Number of paths if we place 'H' now
            let cnt = comb[v + h - 1][h - 1];
            if kk <= cnt {
                result.push('H');
                h -= 1;
            } else {
                result.push('V');
                v -= 1;
                kk -= cnt;
            }
        }

        // Append remaining moves
        for _ in 0..h {
            result.push('H');
        }
        for _ in 0..v {
            result.push('V');
        }

        result
    }
}
```

## Racket

```racket
(define (comb n r)
  (if (< r 0) 0
      (let ((r (min r (- n r))))
        (let loop ((i 1) (res 1))
          (if (> i r) res
              (loop (+ i 1) (/ (* res (+ (- n r) i)) i))))))

(define/contract (kth-smallest-path destination k)
  (-> (listof exact-integer?) exact-integer? string?)
  (let* ((row (first destination))
         (col (second destination)))
    (let build ((r row) (c col) (k k) (acc '()))
      (cond
        [(zero? r) (string-append (list->string (reverse acc)) (make-string c #\H))]
        [(zero? c) (string-append (list->string (reverse acc)) (make-string r #\V))]
        [else
         (define cnt (comb (- (+ r c) 1) (- c 1))) ; C(r+c-1, c-1)
         (if (<= k cnt)
             (build r (- c 1) k (cons #\H acc))
             (build (- r 1) c (- k cnt) (cons #\V acc)))]))))
```

## Erlang

```erlang
-module(solution).
-export([kth_smallest_path/2]).

-spec kth_smallest_path(Destination :: [integer()], K :: integer()) -> unicode:unicode_binary().
kth_smallest_path(Destination, K) ->
    [Row, Col] = Destination,
    List = build(Row, Col, K),
    list_to_binary(List).

build(0, C, _K) ->
    lists:duplicate(C, $H);
build(R, 0, _K) ->
    lists:duplicate(R, $V);
build(R, C, K) ->
    Count = comb(R + C - 1, R),
    if
        K =< Count ->
            [$H | build(R, C - 1, K)];
        true ->
            [$V | build(R - 1, C, K - Count)]
    end.

comb(N, K) when K < 0; K > N -> 0;
comb(N, K) ->
    K1 = if K > N - K -> N - K; true -> K end,
    comb_iter(1, 1, N, K1).

comb_iter(I, Acc, _N, K) when I > K ->
    Acc;
comb_iter(I, Acc, N, K) ->
    Num = N - K + I,
    NewAcc = (Acc * Num) div I,
    comb_iter(I + 1, NewAcc, N, K).
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_smallest_path(destination :: [integer], k :: integer) :: String.t()
  def kth_smallest_path([row, col], k) do
    build(row, col, k, [])
    |> Enum.reverse()
    |> List.to_string()
  end

  defp build(0, col, _k, acc) do
    Enum.reduce(1..col, acc, fn _, a -> [?H | a] end)
  end

  defp build(row, 0, _k, acc) do
    Enum.reduce(1..row, acc, fn _, a -> [?V | a] end)
  end

  defp build(row, col, k, acc) do
    count = comb(row + col - 1, row - 1)

    if k <= count do
      build(row, col - 1, k, [?H | acc])
    else
      build(row - 1, col, k - count, [?V | acc])
    end
  end

  defp comb(n, k) when k < 0 or k > n, do: 0

  defp comb(n, k) do
    k = min(k, n - k)

    Enum.reduce(1..k, 1, fn i, acc ->
      div(acc * (n - k + i), i)
    end)
  end
end
```
