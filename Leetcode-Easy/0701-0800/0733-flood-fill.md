# 0733. Flood Fill

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int m = image.size();
        int n = image[0].size();
        int orig = image[sr][sc];
        if (orig == newColor) return image;
        function<void(int,int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= m || c < 0 || c >= n) return;
            if (image[r][c] != orig) return;
            image[r][c] = newColor;
            dfs(r + 1, c);
            dfs(r - 1, c);
            dfs(r, c + 1);
            dfs(r, c - 1);
        };
        dfs(sr, sc);
        return image;
    }
};
```

## Java

```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        if (original == color) return image;
        dfs(image, sr, sc, original, color);
        return image;
    }
    
    private void dfs(int[][] img, int r, int c, int targetColor, int newColor) {
        int m = img.length, n = img[0].length;
        if (r < 0 || c < 0 || r >= m || c >= n) return;
        if (img[r][c] != targetColor) return;
        img[r][c] = newColor;
        dfs(img, r + 1, c, targetColor, newColor);
        dfs(img, r - 1, c, targetColor, newColor);
        dfs(img, r, c + 1, targetColor, newColor);
        dfs(img, r, c - 1, targetColor, newColor);
    }
}
```

## Python

```python
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        orig = image[sr][sc]
        if orig == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
```

## Python3

```python
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        m, n = len(image), len(image[0])

        def dfs(r: int, c: int):
            if image[r][c] != original:
                return
            image[r][c] = color
            if r > 0:
                dfs(r - 1, c)
            if r < m - 1:
                dfs(r + 1, c)
            if c > 0:
                dfs(r, c - 1)
            if c < n - 1:
                dfs(r, c + 1)

        dfs(sr, sc)
        return image
```

## C

```c
#include <stdlib.h>

static void dfs(int **img, int rows, int *cols, int r, int c, int origColor, int newColor) {
    if (r < 0 || r >= rows || c < 0 || c >= cols[r]) return;
    if (img[r][c] != origColor) return;
    img[r][c] = newColor;
    dfs(img, rows, cols, r - 1, c, origColor, newColor);
    dfs(img, rows, cols, r + 1, c, origColor, newColor);
    dfs(img, rows, cols, r, c - 1, origColor, newColor);
    dfs(img, rows, cols, r, c + 1, origColor, newColor);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {
    if (imageSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int origColor = image[sr][sc];
    if (origColor != color) {
        dfs(image, imageSize, imageColSize, sr, sc, origColor, color);
    }

    *returnSize = imageSize;
    *returnColumnSizes = (int *)malloc(imageSize * sizeof(int));
    for (int i = 0; i < imageSize; ++i) {
        (*returnColumnSizes)[i] = imageColSize[i];
    }
    return image;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        if (original == color) return image;
        int rows = image.Length;
        int cols = image[0].Length;

        void Dfs(int r, int c) {
            if (r < 0 || r >= rows || c < 0 || c >= cols) return;
            if (image[r][c] != original) return;
            image[r][c] = color;
            Dfs(r + 1, c);
            Dfs(r - 1, c);
            Dfs(r, c + 1);
            Dfs(r, c - 1);
        }

        Dfs(sr, sc);
        return image;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    const m = image.length;
    const n = image[0].length;
    const origColor = image[sr][sc];
    if (origColor === newColor) return image;

    const dfs = (r, c) => {
        if (r < 0 || r >= m || c < 0 || c >= n) return;
        if (image[r][c] !== origColor) return;
        image[r][c] = newColor;
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };

    dfs(sr, sc);
    return image;
};
```

## Typescript

```typescript
function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    const m = image.length;
    const n = image[0].length;
    const originalColor = image[sr][sc];
    if (originalColor === color) return image;

    const dfs = (r: number, c: number): void => {
        if (r < 0 || r >= m || c < 0 || c >= n) return;
        if (image[r][c] !== originalColor) return;
        image[r][c] = color;
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };

    dfs(sr, sc);
    return image;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $image
     * @param Integer $sr
     * @param Integer $sc
     * @param Integer $color
     * @return Integer[][]
     */
    function floodFill($image, $sr, $sc, $color) {
        $orig = $image[$sr][$sc];
        if ($orig === $color) {
            return $image;
        }
        $m = count($image);
        $n = count($image[0]);
        $stack = [[$sr, $sc]];
        while (!empty($stack)) {
            [$r, $c] = array_pop($stack);
            if ($r < 0 || $r >= $m || $c < 0 || $c >= $n) {
                continue;
            }
            if ($image[$r][$c] !== $orig) {
                continue;
            }
            $image[$r][$c] = $color;
            $stack[] = [$r - 1, $c];
            $stack[] = [$r + 1, $c];
            $stack[] = [$r, $c - 1];
            $stack[] = [$r, $c + 1];
        }
        return $image;
    }
}
```

## Swift

```swift
class Solution {
    func floodFill(_ image: [[Int]], _ sr: Int, _ sc: Int, _ color: Int) -> [[Int]] {
        var img = image
        let originalColor = img[sr][sc]
        if originalColor == color { return img }
        let rows = img.count
        let cols = img[0].count

        func dfs(_ r: Int, _ c: Int) {
            if r < 0 || r >= rows || c < 0 || c >= cols { return }
            if img[r][c] != originalColor { return }
            img[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        }

        dfs(sr, sc)
        return img
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {
        val m = image.size
        val n = image[0].size
        val originalColor = image[sr][sc]
        if (originalColor == color) return image

        fun dfs(r: Int, c: Int) {
            if (r !in 0 until m || c !in 0 until n) return
            if (image[r][c] != originalColor) return
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        }

        dfs(sr, sc)
        return image
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> floodFill(List<List<int>> image, int sr, int sc, int color) {
    final int m = image.length;
    final int n = image[0].length;
    final int original = image[sr][sc];
    if (original == color) return image;

    void dfs(int r, int c) {
      if (r < 0 || r >= m || c < 0 || c >= n) return;
      if (image[r][c] != original) return;
      image[r][c] = color;
      dfs(r + 1, c);
      dfs(r - 1, c);
      dfs(r, c + 1);
      dfs(r, c - 1);
    }

    dfs(sr, sc);
    return image;
  }
}
```

## Golang

```go
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    original := image[sr][sc]
    if original == color {
        return image
    }
    rows, cols := len(image), len(image[0])
    var dfs func(r, c int)
    dfs = func(r, c int) {
        if r < 0 || r >= rows || c < 0 || c >= cols {
            return
        }
        if image[r][c] != original {
            return
        }
        image[r][c] = color
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
    }
    dfs(sr, sc)
    return image
}
```

## Ruby

```ruby
def flood_fill(image, sr, sc, color)
  original = image[sr][sc]
  return image if original == color

  m = image.length
  n = image[0].length

  stack = [[sr, sc]]
  while !stack.empty?
    i, j = stack.pop
    next unless i.between?(0, m - 1) && j.between?(0, n - 1) && image[i][j] == original

    image[i][j] = color
    stack << [i + 1, j]
    stack << [i - 1, j]
    stack << [i, j + 1]
    stack << [i, j - 1]
  end

  image
end
```

## Scala

```scala
object Solution {
    def floodFill(image: Array[Array[Int]], sr: Int, sc: Int, color: Int): Array[Array[Int]] = {
        val original = image(sr)(sc)
        if (original != color) {
            val rows = image.length
            val cols = image(0).length
            def dfs(r: Int, c: Int): Unit = {
                if (r < 0 || r >= rows || c < 0 || c >= cols) return
                if (image(r)(c) != original) return
                image(r)(c) = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            }
            dfs(sr, sc)
        }
        image
    }
}
```

## Rust

```rust
impl Solution {
    pub fn flood_fill(mut image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        let m = image.len();
        if m == 0 {
            return image;
        }
        let n = image[0].len();
        let sr_usize = sr as usize;
        let sc_usize = sc as usize;
        let original = image[sr_usize][sc_usize];
        if original == color {
            return image;
        }

        fn dfs(img: &mut Vec<Vec<i32>>, r: i32, c: i32, m: usize, n: usize, orig: i32, newc: i32) {
            if r < 0 || c < 0 {
                return;
            }
            let (ur, uc) = (r as usize, c as usize);
            if ur >= m || uc >= n {
                return;
            }
            if img[ur][uc] != orig {
                return;
            }
            img[ur][uc] = newc;
            dfs(img, r - 1, c, m, n, orig, newc);
            dfs(img, r + 1, c, m, n, orig, newc);
            dfs(img, r, c - 1, m, n, orig, newc);
            dfs(img, r, c + 1, m, n, orig, newc);
        }

        dfs(&mut image, sr, sc, m, n, original, color);
        image
    }
}
```

## Racket

```racket
(define/contract (flood-fill image sr sc color)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?
      (listof (listof exact-integer?)))
  (let* ((m (length image))
         (n (if (null? image) 0 (length (car image))))
         (orig-color (list-ref (list-ref image sr) sc)))
    (if (= orig-color color)
        image
        (let* ((vec-rows (list->vector (map list->vector image))))
          (define (dfs r c)
            (when (and (>= r 0) (< r m) (>= c 0) (< c n))
              (let ((row (vector-ref vec-rows r)))
                (when (= (vector-ref row c) orig-color)
                  (vector-set! row c color)
                  (dfs (- r 1) c)
                  (dfs (+ r 1) c)
                  (dfs r (- c 1))
                  (dfs r (+ c 1))))))

          (dfs sr sc)

          (map vector->list (vector->list vec-rows))))) )
```

## Erlang

```erlang
-spec flood_fill(Image :: [[integer()]], Sr :: integer(), Sc :: integer(), Color :: integer()) -> [[integer()]].
flood_fill(Image, Sr, Sc, Color) ->
    RowsTuple = list_to_tuple([list_to_tuple(Row) || Row <- Image]),
    OrigColor = element(Sc + 1, element(Sr + 1, RowsTuple)),
    case OrigColor == Color of
        true -> Image;
        false ->
            Rcnt = tuple_size(RowsTuple),
            Ccnt = tuple_size(element(1, RowsTuple)),
            UpdatedRows = bfs(RowsTuple, [{Sr, Sc}], #{}, OrigColor, Color, Rcnt, Ccnt),
            [tuple_to_list(Row) || Row <- tuple_to_list(UpdatedRows)]
    end.

bfs(Rows, [], _Visited, _Orig, _New, _Rcnt, _Ccnt) ->
    Rows;
bfs(Rows, [{R, C} | Rest], Visited, Orig, New, Rcnt, Ccnt) ->
    case maps:is_key({R, C}, Visited) of
        true ->
            bfs(Rows, Rest, Visited, Orig, New, Rcnt, Ccnt);
        false ->
            RowTuple = element(R + 1, Rows),
            CurColor = element(C + 1, RowTuple),
            if CurColor =:= Orig ->
                    NewRowTuple = setelement(C + 1, RowTuple, New),
                    NewRows = setelement(R + 1, Rows, NewRowTuple),
                    NewVisited = maps:put({R, C}, true, Visited),
                    Neighbors = [{R - 1, C}, {R + 1, C}, {R, C - 1}, {R, C + 1}],
                    Valid = [ {Nr, Nc} ||
                              {Nr, Nc} <- Neighbors,
                              Nr >= 0, Nc >= 0,
                              Nr < Rcnt, Nc < Ccnt ],
                    bfs(NewRows, Valid ++ Rest, NewVisited, Orig, New, Rcnt, Ccnt);
               true ->
                    bfs(Rows, Rest, Visited, Orig, New, Rcnt, Ccnt)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec flood_fill(image :: [[integer]], sr :: integer, sc :: integer, color :: integer) :: [[integer]]
  def flood_fill(image, sr, sc, color) do
    orig = get_pixel(image, sr, sc)

    if orig == color do
      image
    else
      dfs(image, sr, sc, orig, color)
    end
  end

  defp dfs(img, r, c, orig, new) do
    rows = length(img)
    cols = img |> hd() |> length()

    cond do
      r < 0 or r >= rows or c < 0 or c >= cols ->
        img

      true ->
        cur = get_pixel(img, r, c)

        if cur != orig do
          img
        else
          img1 = set_pixel(img, r, c, new)
          img2 = dfs(img1, r + 1, c, orig, new)
          img3 = dfs(img2, r - 1, c, orig, new)
          img4 = dfs(img3, r, c + 1, orig, new)
          dfs(img4, r, c - 1, orig, new)
        end
    end
  end

  defp get_pixel(image, r, c) do
    image |> Enum.at(r) |> Enum.at(c)
  end

  defp set_pixel(image, r, c, val) do
    row = Enum.at(image, r)
    new_row = List.replace_at(row, c, val)
    List.replace_at(image, r, new_row)
  end
end
```
