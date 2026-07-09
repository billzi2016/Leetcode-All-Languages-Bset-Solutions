# 0832. Flipping an Image

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int n = image.size();
        for (int i = 0; i < n; ++i) {
            int l = 0, r = n - 1;
            while (l <= r) {
                if (l == r) {
                    image[i][l] ^= 1;
                } else {
                    int leftVal = image[i][l];
                    int rightVal = image[i][r];
                    // swap and invert
                    image[i][l] = rightVal ^ 1;
                    image[i][r] = leftVal ^ 1;
                }
                ++l;
                --r;
            }
        }
        return image;
    }
};
```

## Java

```java
class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for (int[] row : image) {
            int left = 0, right = row.length - 1;
            while (left <= right) {
                if (left == right) {
                    row[left] ^= 1;
                } else {
                    int leftVal = row[left] ^ 1;
                    int rightVal = row[right] ^ 1;
                    row[left] = rightVal;
                    row[right] = leftVal;
                }
                left++;
                right--;
            }
        }
        return image;
    }
}
```

## Python

```python
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                if left == right:
                    row[left] ^= 1
                else:
                    # swap and invert both ends
                    row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                left += 1
                right -= 1
        return image
```

## Python3

```python
from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i, j = 0, len(row) - 1
            while i <= j:
                if i == j:
                    row[i] ^= 1
                else:
                    left_inv = row[i] ^ 1
                    right_inv = row[j] ^ 1
                    row[i], row[j] = right_inv, left_inv
                i += 1
                j -= 1
        return image
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** flipAndInvertImage(int** image, int imageSize, int* imageColSize, int* returnSize, int** returnColumnSizes) {
    if (imageSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    int cols = imageColSize[0];
    int **result = (int **)malloc(imageSize * sizeof(int *));
    *returnColumnSizes = (int *)malloc(imageSize * sizeof(int));
    for (int i = 0; i < imageSize; ++i) {
        (*returnColumnSizes)[i] = cols;
        result[i] = (int *)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; ++j) {
            int val = image[i][cols - 1 - j];   // flip horizontally
            result[i][j] = val ^ 1;             // invert (0->1, 1->0)
        }
    }
    
    *returnSize = imageSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] FlipAndInvertImage(int[][] image)
    {
        foreach (var row in image)
        {
            int n = row.Length;
            for (int i = 0; i < (n + 1) / 2; i++)
            {
                int j = n - 1 - i;
                if (i == j)
                {
                    // Invert the middle element for odd-length rows
                    row[i] ^= 1;
                }
                else
                {
                    // Swap and invert both elements
                    int leftInverted = row[i] ^ 1;
                    int rightInverted = row[j] ^ 1;
                    row[i] = rightInverted;
                    row[j] = leftInverted;
                }
            }
        }
        return image;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    for (let row of image) {
        const n = row.length;
        for (let i = 0; i <= Math.floor((n - 1) / 2); i++) {
            const j = n - 1 - i;
            if (i === j) {
                // invert the middle element
                row[i] ^= 1;
            } else {
                // swap and invert both ends
                const leftInverted = row[j] ^ 1;
                const rightInverted = row[i] ^ 1;
                row[i] = leftInverted;
                row[j] = rightInverted;
            }
        }
    }
    return image;
};
```

## Typescript

```typescript
function flipAndInvertImage(image: number[][]): number[][] {
    for (let row of image) {
        let left = 0;
        let right = row.length - 1;
        while (left <= right) {
            if (left === right) {
                // Invert the middle element
                row[left] ^= 1;
            } else {
                const leftVal = row[left] ^ 1;   // invert original left
                const rightVal = row[right] ^ 1; // invert original right
                row[left] = rightVal;
                row[right] = leftVal;
            }
            left++;
            right--;
        }
    }
    return image;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $image
     * @return Integer[][]
     */
    function flipAndInvertImage($image) {
        $n = count($image);
        for ($i = 0; $i < $n; $i++) {
            $row =& $image[$i];
            $len = count($row);
            $l = 0;
            $r = $len - 1;
            while ($l <= $r) {
                $leftVal = $row[$l] ^ 1;
                $rightVal = $row[$r] ^ 1;
                $row[$l] = $rightVal;
                $row[$r] = $leftVal;
                $l++;
                $r--;
            }
        }
        return $image;
    }
}
```

## Swift

```swift
class Solution {
    func flipAndInvertImage(_ image: [[Int]]) -> [[Int]] {
        var result = image
        for r in 0..<result.count {
            var i = 0
            var j = result[r].count - 1
            while i <= j {
                let leftInverted = result[r][i] ^ 1
                let rightInverted = result[r][j] ^ 1
                result[r][i] = rightInverted
                result[r][j] = leftInverted
                i += 1
                j -= 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun flipAndInvertImage(image: Array<IntArray>): Array<IntArray> {
        for (row in image) {
            val n = row.size
            var i = 0
            while (i <= (n - 1) / 2) {
                val j = n - 1 - i
                if (i == j) {
                    row[i] = row[i] xor 1
                } else {
                    val leftInverted = row[i] xor 1
                    val rightInverted = row[j] xor 1
                    row[i] = rightInverted
                    row[j] = leftInverted
                }
                i++
            }
        }
        return image
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> flipAndInvertImage(List<List<int>> image) {
    for (var row in image) {
      int n = row.length;
      int half = n ~/ 2;
      for (int j = 0; j < half; ++j) {
        int leftInverted = row[j] ^ 1;
        int rightInverted = row[n - 1 - j] ^ 1;
        row[j] = rightInverted;
        row[n - 1 - j] = leftInverted;
      }
      if (n.isOdd) {
        row[half] ^= 1;
      }
    }
    return image;
  }
}
```

## Golang

```go
func flipAndInvertImage(image [][]int) [][]int {
    for _, row := range image {
        left, right := 0, len(row)-1
        for left <= right {
            if left == right {
                // Invert the middle element
                row[left] ^= 1
            } else {
                // Swap and invert both ends
                leftVal, rightVal := row[left], row[right]
                row[left] = rightVal ^ 1
                row[right] = leftVal ^ 1
            }
            left++
            right--
        }
    }
    return image
}
```

## Ruby

```ruby
def flip_and_invert_image(image)
  image.each do |row|
    i = 0
    j = row.length - 1
    while i < j
      left = row[i] ^ 1
      right = row[j] ^ 1
      row[i] = right
      row[j] = left
      i += 1
      j -= 1
    end
    row[i] ^= 1 if i == j
  end
  image
end
```

## Scala

```scala
object Solution {
    def flipAndInvertImage(image: Array[Array[Int]]): Array[Array[Int]] = {
        for (row <- image) {
            var l = 0
            var r = row.length - 1
            while (l <= r) {
                if (l == r) {
                    row(l) = 1 - row(l)
                } else {
                    val leftInverted = 1 - row(r)
                    val rightInverted = 1 - row(l)
                    row(l) = leftInverted
                    row(r) = rightInverted
                }
                l += 1
                r -= 1
            }
        }
        image
    }
}
```

## Rust

```rust
impl Solution {
    pub fn flip_and_invert_image(mut image: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        for row in image.iter_mut() {
            let mut l = 0usize;
            let mut r = row.len() - 1;
            while l <= r {
                let left_val = row[l];
                let right_val = row[r];
                row[l] = 1 - right_val;
                row[r] = 1 - left_val;
                if l == r {
                    break;
                }
                l += 1;
                r -= 1;
            }
        }
        image
    }
}
```

## Racket

```racket
(define/contract (flip-and-invert-image image)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (map (lambda (row)
         (map (lambda (v) (- 1 v))
              (reverse row)))
       image))
```

## Erlang

```erlang
-spec flip_and_invert_image(Image :: [[integer()]]) -> [[integer()]].
flip_and_invert_image(Image) ->
    lists:map(fun(Row) ->
        [ invert_bit(Bit) || Bit <- lists:reverse(Row) ]
    end, Image).

invert_bit(0) -> 1;
invert_bit(1) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec flip_and_invert_image(image :: [[integer]]) :: [[integer]]
  def flip_and_invert_image(image) do
    Enum.map(image, fn row ->
      row
      |> Enum.reverse()
      |> Enum.map(fn x -> 1 - x end)
    end)
  end
end
```
