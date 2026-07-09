# 1725. Number Of Rectangles That Can Form The Largest Square

## Cpp

```cpp
class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int maxLen = 0;
        for (const auto& rec : rectangles) {
            int side = min(rec[0], rec[1]);
            if (side > maxLen) maxLen = side;
        }
        int cnt = 0;
        for (const auto& rec : rectangles) {
            if (min(rec[0], rec[1]) == maxLen) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int maxSide = 0;
        for (int[] rect : rectangles) {
            int side = Math.min(rect[0], rect[1]);
            if (side > maxSide) {
                maxSide = side;
            }
        }
        int count = 0;
        for (int[] rect : rectangles) {
            if (Math.min(rect[0], rect[1]) == maxSide) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        max_len = 0
        count = 0
        for l, w in rectangles:
            side = l if l < w else w
            if side > max_len:
                max_len = side
                count = 1
            elif side == max_len:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        count = 0
        for l, w in rectangles:
            side = l if l < w else w
            if side > max_len:
                max_len = side
                count = 1
            elif side == max_len:
                count += 1
        return count
```

## C

```c
#include <stddef.h>

int countGoodRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    int maxLen = 0;
    for (int i = 0; i < rectanglesSize; ++i) {
        int a = rectangles[i][0];
        int b = rectangles[i][1];
        int side = a < b ? a : b;
        if (side > maxLen) {
            maxLen = side;
        }
    }
    
    int count = 0;
    for (int i = 0; i < rectanglesSize; ++i) {
        int a = rectangles[i][0];
        int b = rectangles[i][1];
        int side = a < b ? a : b;
        if (side == maxLen) {
            ++count;
        }
    }
    
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountGoodRectangles(int[][] rectangles) {
        int maxSide = 0;
        foreach (var rect in rectangles) {
            int side = Math.Min(rect[0], rect[1]);
            if (side > maxSide) maxSide = side;
        }
        int count = 0;
        foreach (var rect in rectangles) {
            if (Math.Min(rect[0], rect[1]) == maxSide) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    let maxSide = 0;
    for (const [l, w] of rectangles) {
        const side = Math.min(l, w);
        if (side > maxSide) maxSide = side;
    }
    let count = 0;
    for (const [l, w] of rectangles) {
        if (Math.min(l, w) === maxSide) count++;
    }
    return count;
};
```

## Typescript

```typescript
function countGoodRectangles(rectangles: number[][]): number {
    let maxLen = 0;
    for (const [l, w] of rectangles) {
        const side = Math.min(l, w);
        if (side > maxLen) maxLen = side;
    }
    let count = 0;
    for (const [l, w] of rectangles) {
        if (Math.min(l, w) === maxLen) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function countGoodRectangles($rectangles) {
        $maxLen = 0;
        foreach ($rectangles as $rect) {
            $side = min($rect[0], $rect[1]);
            if ($side > $maxLen) {
                $maxLen = $side;
            }
        }

        $count = 0;
        foreach ($rectangles as $rect) {
            if (min($rect[0], $rect[1]) == $maxLen) {
                $count++;
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countGoodRectangles(_ rectangles: [[Int]]) -> Int {
        var maxLen = 0
        var count = 0
        for rect in rectangles {
            let side = min(rect[0], rect[1])
            if side > maxLen {
                maxLen = side
                count = 1
            } else if side == maxLen {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countGoodRectangles(rectangles: Array<IntArray>): Int {
        var maxLen = 0
        for (rect in rectangles) {
            val side = minOf(rect[0], rect[1])
            if (side > maxLen) maxLen = side
        }
        var count = 0
        for (rect in rectangles) {
            if (minOf(rect[0], rect[1]) == maxLen) count++
        }
        return count
    }
}
```

## Golang

```go
func countGoodRectangles(rectangles [][]int) int {
    maxLen := 0
    count := 0
    for _, r := range rectangles {
        side := r[0]
        if r[1] < side {
            side = r[1]
        }
        if side > maxLen {
            maxLen = side
            count = 1
        } else if side == maxLen {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def count_good_rectangles(rectangles)
  max_len = 0
  count = 0
  rectangles.each do |l, w|
    side = l < w ? l : w
    if side > max_len
      max_len = side
      count = 1
    elsif side == max_len
      count += 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def countGoodRectangles(rectangles: Array[Array[Int]]): Int = {
        var maxSide = 0
        var count = 0
        for (rect <- rectangles) {
            val side = if (rect(0) < rect(1)) rect(0) else rect(1)
            if (side > maxSide) {
                maxSide = side
                count = 1
            } else if (side == maxSide) {
                count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_good_rectangles(rectangles: Vec<Vec<i32>>) -> i32 {
        let mut max_len = 0;
        for rect in &rectangles {
            let side = std::cmp::min(rect[0], rect[1]);
            if side > max_len {
                max_len = side;
            }
        }
        let mut count = 0;
        for rect in rectangles {
            let side = std::cmp::min(rect[0], rect[1]);
            if side == max_len {
                count += 1;
            }
        }
        count
    }
}
```
