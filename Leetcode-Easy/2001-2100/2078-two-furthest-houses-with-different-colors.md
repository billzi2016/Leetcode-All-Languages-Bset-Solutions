# 2078. Two Furthest Houses With Different Colors

## Cpp

```cpp
class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int n = colors.size();
        int ans = 0;
        // Compare with leftmost house
        for (int i = 0; i < n; ++i) {
            if (colors[i] != colors[0]) {
                ans = max(ans, i);
            }
        }
        // Compare with rightmost house
        for (int i = n - 1; i >= 0; --i) {
            if (colors[i] != colors[n - 1]) {
                ans = max(ans, (n - 1) - i);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxDistance(int[] colors) {
        int n = colors.length;
        int leftColor = colors[0];
        int rightColor = colors[n - 1];
        int ans = 0;
        // Pair leftmost house with a different colored house on the right
        for (int i = 0; i < n; i++) {
            if (colors[i] != rightColor) {
                ans = Math.max(ans, (n - 1) - i);
            }
        }
        // Pair rightmost house with a different colored house on the left
        for (int i = n - 1; i >= 0; i--) {
            if (colors[i] != leftColor) {
                ans = Math.max(ans, i);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        left_color = colors[0]
        right_color = colors[-1]

        # Find farthest house from the left with a different color
        i = n - 1
        while i >= 0 and colors[i] == left_color:
            i -= 1
        dist_left = i if i >= 0 else 0

        # Find farthest house from the right with a different color
        j = 0
        while j < n and colors[j] == right_color:
            j += 1
        dist_right = (n - 1) - j if j < n else 0

        return max(dist_left, dist_right)
```

## Python3

```python
from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        # compare with leftmost house
        for i in range(n):
            if colors[i] != colors[0]:
                ans = max(ans, i)
        # compare with rightmost house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[-1]:
                ans = max(ans, (n - 1) - i)
        return ans
```

## C

```c
int maxDistance(int* colors, int colorsSize){
    int n = colorsSize;
    int ans = 0;
    // Check from the leftmost house
    for (int j = n - 1; j >= 0; --j) {
        if (colors[j] != colors[0]) {
            ans = j; // distance = j - 0
            break;
        }
    }
    // Check from the rightmost house
    for (int i = 0; i < n; ++i) {
        if (colors[i] != colors[n - 1]) {
            int d = (n - 1) - i;
            if (d > ans) ans = d;
            break;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDistance(int[] colors) {
        int n = colors.Length;
        int maxDist = 0;
        
        // Check from the leftmost house
        for (int i = n - 1; i >= 0; i--) {
            if (colors[i] != colors[0]) {
                maxDist = Math.Max(maxDist, i);
                break;
            }
        }
        
        // Check from the rightmost house
        for (int i = 0; i < n; i++) {
            if (colors[i] != colors[n - 1]) {
                maxDist = Math.Max(maxDist, (n - 1) - i);
                break;
            }
        }
        
        return maxDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} colors
 * @return {number}
 */
var maxDistance = function(colors) {
    const n = colors.length;
    let ans = 0;
    const leftColor = colors[0];
    const rightColor = colors[n - 1];
    
    for (let i = 0; i < n; ++i) {
        if (colors[i] !== leftColor) {
            ans = Math.max(ans, i);
        }
        if (colors[i] !== rightColor) {
            ans = Math.max(ans, (n - 1) - i);
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function maxDistance(colors: number[]): number {
    const n = colors.length;
    let maxDist = 0;

    // Check farthest house from the leftmost house with a different color
    for (let i = n - 1; i >= 0; --i) {
        if (colors[i] !== colors[0]) {
            maxDist = Math.max(maxDist, i);
            break;
        }
    }

    // Check farthest house from the rightmost house with a different color
    for (let i = 0; i < n; ++i) {
        if (colors[i] !== colors[n - 1]) {
            maxDist = Math.max(maxDist, (n - 1) - i);
            break;
        }
    }

    return maxDist;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $colors
     * @return Integer
     */
    function maxDistance($colors) {
        $n = count($colors);
        $maxDist = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($colors[$i] !== $colors[$j]) {
                    $dist = $j - $i;
                    if ($dist > $maxDist) {
                        $maxDist = $dist;
                    }
                }
            }
        }
        return $maxDist;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistance(_ colors: [Int]) -> Int {
        let n = colors.count
        var result = 0
        
        // Check from the rightmost side for a different color than the first house
        for i in stride(from: n - 1, through: 0, by: -1) {
            if colors[i] != colors[0] {
                result = max(result, i)
                break
            }
        }
        
        // Check from the leftmost side for a different color than the last house
        for i in 0..<n {
            if colors[i] != colors[n - 1] {
                result = max(result, (n - 1) - i)
                break
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistance(colors: IntArray): Int {
        val n = colors.size
        var distFromLeft = 0
        for (i in n - 1 downTo 0) {
            if (colors[i] != colors[0]) {
                distFromLeft = i
                break
            }
        }
        var distFromRight = 0
        for (i in 0 until n) {
            if (colors[i] != colors[n - 1]) {
                distFromRight = (n - 1) - i
                break
            }
        }
        return maxOf(distFromLeft, distFromRight)
    }
}
```

## Dart

```dart
class Solution {
  int maxDistance(List<int> colors) {
    int n = colors.length;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (colors[i] != colors[0]) {
        ans = ans > i ? ans : i;
      }
      if (colors[i] != colors[n - 1]) {
        int dist = (n - 1) - i;
        ans = ans > dist ? ans : dist;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxDistance(colors []int) int {
	n := len(colors)
	ans := 0
	for i, c := range colors {
		if c != colors[0] && i > ans {
			ans = i
		}
		if c != colors[n-1] {
			d := n - 1 - i
			if d > ans {
				ans = d
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_distance(colors)
  n = colors.length
  left_color = colors[0]
  right_color = colors[-1]
  max_dist = 0

  # Farthest house from the leftmost with a different color
  (n - 1).downto(0) do |i|
    if colors[i] != left_color
      max_dist = i
      break
    end
  end

  # Farthest house from the rightmost with a different color
  (0...n).each do |i|
    if colors[i] != right_color
      dist = n - 1 - i
      max_dist = [max_dist, dist].max
      break
    end
  end

  max_dist
end
```

## Scala

```scala
object Solution {
    def maxDistance(colors: Array[Int]): Int = {
        val n = colors.length
        var ans = 0
        // Check distances from the leftmost house (index 0)
        for (i <- (n - 1) to 0 by -1) {
            if (colors(i) != colors(0)) {
                ans = math.max(ans, i) // distance i - 0 = i
            }
        }
        // Check distances from the rightmost house (index n-1)
        for (i <- 0 until n) {
            if (colors(i) != colors(n - 1)) {
                ans = math.max(ans, (n - 1) - i)
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_distance(colors: Vec<i32>) -> i32 {
        let n = colors.len();
        let first = colors[0];
        let last = colors[n - 1];
        let mut ans = 0usize;

        // farthest house from the leftmost with different color
        for i in (0..n).rev() {
            if colors[i] != first {
                ans = ans.max(i);
                break;
            }
        }

        // farthest house from the rightmost with different color
        for i in 0..n {
            if colors[i] != last {
                ans = ans.max(n - 1 - i);
                break;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-distance colors)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length colors))
         (vec (list->vector colors))
         (first-color (vector-ref vec 0))
         (last-color (vector-ref vec (- n 1)))
         ;; farthest index from the left that differs from first color
         (i (let loop ((idx (- n 1)))
              (if (= idx 0)
                  0
                  (if (not (= (vector-ref vec idx) first-color))
                      idx
                      (loop (- idx 1))))))
         ;; nearest index from the left that differs from last color
         (j (let loop ((idx 0))
              (if (= idx (- n 1))
                  (- n 1)
                  (if (not (= (vector-ref vec idx) last-color))
                      idx
                      (loop (+ idx 1))))))
         (dist1 (- i 0))
         (dist2 (- (- n 1) j)))
    (max dist1 dist2)))
```

## Erlang

```erlang
-spec max_distance([integer()]) -> integer().
max_distance(Colors) ->
    N = length(Colors),
    First = hd(Colors),
    Last = lists:last(Colors),
    Dist1 = find_right(N - 1, Colors, First),
    Dist2 = find_left(0, N - 1, Colors, Last),
    if
        Dist1 > Dist2 -> Dist1;
        true -> Dist2
    end.

find_right(-1, _Colors, _First) ->
    0;
find_right(Index, Colors, First) ->
    case lists:nth(Index + 1, Colors) of
        C when C =/= First -> Index;
        _ -> find_right(Index - 1, Colors, First)
    end.

find_left(Idx, NMinus1, Colors, Last) ->
    case lists:nth(Idx + 1, Colors) of
        C when C =/= Last -> NMinus1 - Idx;
        _ -> find_left(Idx + 1, NMinus1, Colors, Last)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distance(colors :: [integer]) :: integer
  def max_distance(colors) do
    t = List.to_tuple(colors)
    n = tuple_size(t)

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      Enum.reduce((i + 1)..(n - 1), acc, fn j, inner_acc ->
        if elem(t, i) != elem(t, j) do
          max(inner_acc, j - i)
        else
          inner_acc
        end
      end)
    end)
  end
end
```
