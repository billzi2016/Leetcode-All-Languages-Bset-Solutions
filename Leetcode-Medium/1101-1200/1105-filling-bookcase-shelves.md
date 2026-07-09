# 1105. Filling Bookcase Shelves

## Cpp

```cpp
class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        int n = books.size();
        const int INF = 1e9;
        vector<int> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 1; i <= n; ++i) {
            int width = 0;
            int maxHeight = 0;
            for (int j = i; j >= 1; --j) {
                width += books[j - 1][0];
                if (width > shelfWidth) break;
                maxHeight = max(maxHeight, books[j - 1][1]);
                dp[i] = min(dp[i], dp[j - 1] + maxHeight);
            }
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int n = books.length;
        int[] dp = new int[n + 1];
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            int width = 0;
            int maxHeight = 0;
            dp[i] = Integer.MAX_VALUE;
            for (int j = i; j >= 1; j--) {
                width += books[j - 1][0];
                if (width > shelfWidth) break;
                maxHeight = Math.max(maxHeight, books[j - 1][1]);
                dp[i] = Math.min(dp[i], dp[j - 1] + maxHeight);
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [0] + [float('inf')] * n  # dp[i]: min height for first i books
        for i in range(1, n + 1):
            width_left = shelfWidth
            max_height = 0
            j = i
            while j > 0 and width_left >= books[j - 1][0]:
                width_left -= books[j - 1][0]
                max_height = max(max_height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + max_height)
                j -= 1
        return dp[n]
```

## Python3

```python
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [float('inf')] * n  # dp[i]: min height for first i books
        for i in range(1, n + 1):
            width_left = shelfWidth
            max_height = 0
            j = i
            while j > 0 and width_left >= books[j - 1][0]:
                width_left -= books[j - 1][0]
                max_height = max(max_height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + max_height)
                j -= 1
        return dp[n]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minHeightShelves(int** books, int booksSize, int* booksColSize, int shelfWidth) {
    int *dp = (int *)malloc((booksSize + 1) * sizeof(int));
    dp[0] = 0;
    for (int i = 1; i <= booksSize; ++i) {
        int remaining = shelfWidth;
        int maxHeight = 0;
        dp[i] = INT_MAX;
        for (int j = i; j >= 1; --j) {
            remaining -= books[j - 1][0];
            if (remaining < 0) break;
            if (books[j - 1][1] > maxHeight) maxHeight = books[j - 1][1];
            int candidate = dp[j - 1] + maxHeight;
            if (candidate < dp[i]) dp[i] = candidate;
        }
    }
    int result = dp[booksSize];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinHeightShelves(int[][] books, int shelfWidth)
    {
        int n = books.Length;
        int[] dp = new int[n + 1];
        dp[0] = 0;

        for (int i = 1; i <= n; i++)
        {
            int width = 0;
            int maxHeight = 0;
            dp[i] = int.MaxValue;

            for (int j = i; j >= 1; j--)
            {
                width += books[j - 1][0];
                if (width > shelfWidth)
                    break;

                maxHeight = Math.Max(maxHeight, books[j - 1][1]);
                dp[i] = Math.Min(dp[i], dp[j - 1] + maxHeight);
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} books
 * @param {number} shelfWidth
 * @return {number}
 */
var minHeightShelves = function(books, shelfWidth) {
    const n = books.length;
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;
    for (let i = 1; i <= n; i++) {
        let width = 0;
        let maxHeight = 0;
        // try placing books j..i-1 on the same shelf
        for (let j = i; j >= 1; j--) {
            width += books[j - 1][0];
            if (width > shelfWidth) break;
            maxHeight = Math.max(maxHeight, books[j - 1][1]);
            dp[i] = Math.min(dp[i], dp[j - 1] + maxHeight);
        }
    }
    return dp[n];
};
```

## Typescript

```typescript
function minHeightShelves(books: number[][], shelfWidth: number): number {
    const n = books.length;
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    for (let i = 1; i <= n; i++) {
        let width = 0;
        let maxHeight = 0;
        // try to place books j..i-1 on the same shelf
        for (let j = i; j >= 1; j--) {
            width += books[j - 1][0];
            if (width > shelfWidth) break;
            maxHeight = Math.max(maxHeight, books[j - 1][1]);
            dp[i] = Math.min(dp[i], dp[j - 1] + maxHeight);
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $books
     * @param Integer $shelfWidth
     * @return Integer
     */
    function minHeightShelves($books, $shelfWidth) {
        $n = count($books);
        $dp = array_fill(0, $n + 1, PHP_INT_MAX);
        $dp[0] = 0;

        for ($i = 1; $i <= $n; $i++) {
            $width = 0;
            $maxHeight = 0;
            // Try to place books j..i-1 on the same shelf
            for ($j = $i; $j >= 1; $j--) {
                $width += $books[$j - 1][0];
                if ($width > $shelfWidth) {
                    break;
                }
                $maxHeight = max($maxHeight, $books[$j - 1][1]);
                $dp[$i] = min($dp[$i], $dp[$j - 1] + $maxHeight);
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func minHeightShelves(_ books: [[Int]], _ shelfWidth: Int) -> Int {
        let n = books.count
        var dp = Array(repeating: Int.max / 2, count: n + 1)
        dp[0] = 0
        for i in 1...n {
            var width = 0
            var maxHeight = 0
            var j = i
            while j >= 1 {
                let book = books[j - 1]
                width += book[0]
                if width > shelfWidth { break }
                maxHeight = max(maxHeight, book[1])
                dp[i] = min(dp[i], dp[j - 1] + maxHeight)
                j -= 1
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minHeightShelves(books: Array<IntArray>, shelfWidth: Int): Int {
        val n = books.size
        val dp = IntArray(n + 1) { Int.MAX_VALUE / 2 }
        dp[0] = 0
        for (i in 1..n) {
            var width = 0
            var maxHeight = 0
            var j = i - 1
            while (j >= 0) {
                width += books[j][0]
                if (width > shelfWidth) break
                maxHeight = kotlin.math.max(maxHeight, books[j][1])
                dp[i] = kotlin.math.min(dp[i], dp[j] + maxHeight)
                j--
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int minHeightShelves(List<List<int>> books, int shelfWidth) {
    final n = books.length;
    const int INF = 1 << 60;
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= n; i++) {
      int widthSum = 0;
      int maxHeight = 0;
      // try to place books j..i on the same shelf
      for (int j = i; j >= 1; j--) {
        widthSum += books[j - 1][0];
        if (widthSum > shelfWidth) break;
        maxHeight = maxHeight > books[j - 1][1] ? maxHeight : books[j - 1][1];
        dp[i] = dp[i] < dp[j - 1] + maxHeight ? dp[i] : dp[j - 1] + maxHeight;
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
func minHeightShelves(books [][]int, shelfWidth int) int {
	n := len(books)
	const inf = int(^uint(0) >> 1) // MaxInt
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = inf
		widthLeft := shelfWidth
		maxHeight := 0
		for j := i; j >= 1; j-- {
			thick := books[j-1][0]
			if thick > widthLeft {
				break
			}
			widthLeft -= thick
			if books[j-1][1] > maxHeight {
				maxHeight = books[j-1][1]
			}
			if dp[j-1]+maxHeight < dp[i] {
				dp[i] = dp[j-1] + maxHeight
			}
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def min_height_shelves(books, shelf_width)
  n = books.length
  dp = Array.new(n + 1, Float::INFINITY)
  dp[0] = 0

  (1..n).each do |i|
    width = 0
    max_h = 0
    j = i - 1
    while j >= 0 && width + books[j][0] <= shelf_width
      width += books[j][0]
      max_h = [max_h, books[j][1]].max
      dp[i] = [dp[i], dp[j] + max_h].min
      j -= 1
    end
  end

  dp[n].to_i
end
```

## Scala

```scala
object Solution {
  def minHeightShelves(books: Array[Array[Int]], shelfWidth: Int): Int = {
    val n = books.length
    val dp = new Array[Int](n + 1)
    java.util.Arrays.fill(dp, Int.MaxValue / 2)
    dp(0) = 0

    for (i <- 1 to n) {
      var widthLeft = shelfWidth
      var maxHeight = 0
      var j = i
      while (j >= 1 && widthLeft >= books(j - 1)(0)) {
        widthLeft -= books(j - 1)(0)
        maxHeight = math.max(maxHeight, books(j - 1)(1))
        dp(i) = math.min(dp(i), dp(j - 1) + maxHeight)
        j -= 1
      }
    }

    dp(n)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_height_shelves(books: Vec<Vec<i32>>, shelf_width: i32) -> i32 {
        let n = books.len();
        let mut dp = vec![i32::MAX / 2; n + 1];
        dp[0] = 0;
        for i in 1..=n {
            let mut width = 0;
            let mut max_h = 0;
            for j in (1..=i).rev() {
                width += books[j - 1][0];
                if width > shelf_width {
                    break;
                }
                max_h = max_h.max(books[j - 1][1]);
                let candidate = dp[j - 1] + max_h;
                if candidate < dp[i] {
                    dp[i] = candidate;
                }
            }
        }
        dp[n]
    }
}
```

## Racket

```racket
(define/contract (min-height-shelves books shelfWidth)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (length books))
         (book-vec (list->vector books))
         (dp (make-vector (+ n 1) 0))
         (INF 1000000000))
    (vector-set! dp 0 0)
    (for ([i (in-range 1 (+ n 1))])
      (let loop ((j i) (width shelfWidth) (maxh 0) (best INF))
        (if (= j 0)
            (vector-set! dp i best)
            (let* ((book (vector-ref book-vec (- j 1)))
                   (thick (first book))
                   (ht (second book)))
              (if (> thick width)
                  (vector-set! dp i best)
                  (let ((new-width (- width thick))
                        (new-maxh (max maxh ht))
                        (candidate (+ (vector-ref dp (- j 1)) new-maxh)))
                    (loop (- j 1) new-width new-maxh (min best candidate))))))))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([min_height_shelves/2]).
-spec min_height_shelves(Books :: [[integer()]], ShelfWidth :: integer()) -> integer().
min_height_shelves(Books, ShelfWidth) ->
    N = length(Books),
    BooksArr = array:from_list(Books),
    DP0 = array:new(N + 1, {default, 0}),
    DP1 = array:set(0, 0, DP0),
    DPF = fill_dp(BooksArr, ShelfWidth, 1, N, DP1),
    array:get(N, DPF).

fill_dp(_BooksArr, _ShelfWidth, I, N, DP) when I > N ->
    DP;
fill_dp(BooksArr, ShelfWidth, I, N, DP) ->
    {ThickI, HeightI} = array:get(I - 1, BooksArr),
    Prev = array:get(I - 1, DP),
    Min0 = Prev + HeightI,
    {MinVal, _} = pack_loop(BooksArr, ShelfWidth, I - 1, ThickI, HeightI, Min0, DP),
    DP2 = array:set(I, MinVal, DP),
    fill_dp(BooksArr, ShelfWidth, I + 1, N, DP2).

pack_loop(_BooksArr, _ShelfWidth, J, _WidthSum, _MaxHeight, MinVal, _DP) when J < 1 ->
    {MinVal, ok};
pack_loop(BooksArr, ShelfWidth, J, WidthSum, MaxHeight, MinVal, DP) ->
    {ThickJ, HeightJ} = array:get(J - 1, BooksArr),
    NewWidth = WidthSum + ThickJ,
    if
        NewWidth =< ShelfWidth ->
            NewMax = erlang:max(MaxHeight, HeightJ),
            PrevDP = array:get(J - 1, DP),
            Candidate = PrevDP + NewMax,
            NewMin = erlang:min(MinVal, Candidate),
            pack_loop(BooksArr, ShelfWidth, J - 1, NewWidth, NewMax, NewMin, DP);
        true ->
            {MinVal, ok}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_height_shelves(books :: [[integer]], shelf_width :: integer) :: integer
  def min_height_shelves(books, shelf_width) do
    n = length(books)
    dp0 = :array.new(n + 1, default: 0)

    final_dp =
      Enum.reduce(1..n, dp0, fn i, dp_acc ->
        {thick_i, height_i} = Enum.at(books, i - 1)
        best_initial = :array.get(i - 1, dp_acc) + height_i

        {best_final, _} =
          inner(i - 1, thick_i, height_i, best_initial, books, shelf_width, dp_acc)

        :array.set(i, best_final, dp_acc)
      end)

    :array.get(n, final_dp)
  end

  defp inner(0, _total_w, _cur_max, best, _books, _shelf_width, _dp), do: {best, nil}

  defp inner(j, total_w, cur_max, best, books, shelf_width, dp) when j > 0 do
    {thk, h} = Enum.at(books, j - 1)
    new_w = total_w + thk

    if new_w > shelf_width do
      {best, nil}
    else
      new_max = max(cur_max, h)
      candidate = :array.get(j - 1, dp) + new_max
      best2 = min(best, candidate)

      inner(j - 1, new_w, new_max, best2, books, shelf_width, dp)
    end
  end
end
```
