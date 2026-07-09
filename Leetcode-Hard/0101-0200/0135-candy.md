# 0135. Candy

## Cpp

```cpp
class Solution {
public:
    int candy(std::vector<int>& ratings) {
        int n = ratings.size();
        std::vector<int> candies(n, 1);
        for (int i = 1; i < n; ++i) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for (int i = n - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = std::max(candies[i], candies[i + 1] + 1);
            }
        }
        int total = 0;
        for (int c : candies) total += c;
        return total;
    }
};
```

## Java

```java
class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        java.util.Arrays.fill(candies, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        int total = 0;
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
                candies[i] = candies[i + 1] + 1;
            }
        }
        for (int c : candies) total += c;
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0:
            return 0

        candies = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass and sum simultaneously
        total = candies[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            total += candies[i]

        return total
```

## Python3

```python
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)
```

## C

```c
int candy(int* ratings, int ratingsSize) {
    if (ratingsSize <= 0) return 0;
    int *candies = (int *)malloc(sizeof(int) * ratingsSize);
    if (!candies) return 0; // allocation failure fallback
    for (int i = 0; i < ratingsSize; ++i) candies[i] = 1;

    for (int i = 1; i < ratingsSize; ++i) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }

    for (int i = ratingsSize - 2; i >= 0; --i) {
        if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
            candies[i] = candies[i + 1] + 1;
        }
    }

    int total = 0;
    for (int i = 0; i < ratingsSize; ++i) {
        total += candies[i];
    }

    free(candies);
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int Candy(int[] ratings)
    {
        int n = ratings.Length;
        if (n == 0) return 0;

        int[] candies = new int[n];
        for (int i = 0; i < n; i++) candies[i] = 1;

        // Left to right pass
        for (int i = 1; i < n; i++)
        {
            if (ratings[i] > ratings[i - 1])
                candies[i] = candies[i - 1] + 1;
        }

        // Right to left pass
        for (int i = n - 2; i >= 0; i--)
        {
            if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1])
                candies[i] = candies[i + 1] + 1;
        }

        long total = 0;
        foreach (int c in candies) total += c;

        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    const n = ratings.length;
    if (n === 0) return 0;
    const candies = new Array(n).fill(1);
    
    // left to right pass
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }
    
    // right to left pass
    let total = candies[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
            candies[i] = candies[i + 1] + 1;
        }
        total += candies[i];
    }
    
    return total;
};
```

## Typescript

```typescript
function candy(ratings: number[]): number {
    const n = ratings.length;
    const candies = new Array(n).fill(1);
    
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }
    
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
            candies[i] = candies[i + 1] + 1;
        }
    }
    
    let total = 0;
    for (let c of candies) total += c;
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $ratings
     * @return Integer
     */
    function candy($ratings) {
        $n = count($ratings);
        if ($n == 0) return 0;
        $candies = array_fill(0, $n, 1);

        // Left to right pass
        for ($i = 1; $i < $n; $i++) {
            if ($ratings[$i] > $ratings[$i - 1]) {
                $candies[$i] = $candies[$i - 1] + 1;
            }
        }

        // Right to left pass and sum
        $total = $candies[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($ratings[$i] > $ratings[$i + 1] && $candies[$i] <= $candies[$i + 1]) {
                $candies[$i] = $candies[$i + 1] + 1;
            }
            $total += $candies[$i];
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func candy(_ ratings: [Int]) -> Int {
        let n = ratings.count
        if n == 0 { return 0 }
        var candies = Array(repeating: 1, count: n)
        for i in 1..<n {
            if ratings[i] > ratings[i - 1] {
                candies[i] = candies[i - 1] + 1
            }
        }
        for i in stride(from: n - 2, through: 0, by: -1) {
            if ratings[i] > ratings[i + 1] {
                candies[i] = max(candies[i], candies[i + 1] + 1)
            }
        }
        var total = 0
        for c in candies {
            total += c
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun candy(ratings: IntArray): Int {
        val n = ratings.size
        val candies = IntArray(n) { 1 }
        for (i in 1 until n) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1
            }
        }
        for (i in n - 2 downTo 0) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = maxOf(candies[i], candies[i + 1] + 1)
            }
        }
        var total = 0
        for (c in candies) total += c
        return total
    }
}
```

## Dart

```dart
class Solution {
  int candy(List<int> ratings) {
    int n = ratings.length;
    if (n == 0) return 0;
    List<int> candies = List.filled(n, 1);
    for (int i = 1; i < n; ++i) {
      if (ratings[i] > ratings[i - 1]) {
        candies[i] = candies[i - 1] + 1;
      }
    }
    for (int i = n - 2; i >= 0; --i) {
      if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
        candies[i] = candies[i + 1] + 1;
      }
    }
    int total = 0;
    for (int c in candies) {
      total += c;
    }
    return total;
  }
}
```

## Golang

```go
func candy(ratings []int) int {
	n := len(ratings)
	if n == 0 {
		return 0
	}
	candies := make([]int, n)
	for i := range candies {
		candies[i] = 1
	}
	// left to right
	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i-1] && candies[i] <= candies[i-1] {
			candies[i] = candies[i-1] + 1
		}
	}
	// right to left
	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] && candies[i] <= candies[i+1] {
			candies[i] = candies[i+1] + 1
		}
	}
	total := 0
	for _, c := range candies {
		total += c
	}
	return total
}
```

## Ruby

```ruby
def candy(ratings)
  n = ratings.length
  return 0 if n == 0
  candies = Array.new(n, 1)

  (1...n).each do |i|
    candies[i] = candies[i - 1] + 1 if ratings[i] > ratings[i - 1]
  end

  (n - 2).downto(0) do |i|
    if ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]
      candies[i] = candies[i + 1] + 1
    end
  end

  candies.sum
end
```

## Scala

```scala
object Solution {
    def candy(ratings: Array[Int]): Int = {
        val n = ratings.length
        if (n == 0) return 0
        val candies = new Array[Int](n)
        java.util.Arrays.fill(candies, 1)

        // Left to right pass
        var i = 1
        while (i < n) {
            if (ratings(i) > ratings(i - 1)) {
                candies(i) = candies(i - 1) + 1
            }
            i += 1
        }

        // Right to left pass
        i = n - 2
        while (i >= 0) {
            if (ratings(i) > ratings(i + 1) && candies(i) <= candies(i + 1)) {
                candies(i) = candies(i + 1) + 1
            }
            i -= 1
        }

        var total: Long = 0L
        for (c <- candies) total += c
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        if n == 0 {
            return 0;
        }
        let mut candies = vec![1i32; n];
        for i in 1..n {
            if ratings[i] > ratings[i - 1] {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for i in (0..n - 1).rev() {
            if ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1] {
                candies[i] = candies[i + 1] + 1;
            }
        }
        candies.iter().sum()
    }
}
```

## Racket

```racket
(define/contract (candy ratings)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length ratings)))
    (if (= n 0)
        0
        (let* ((r (list->vector ratings))
               (candies (make-vector n 1)))
          ;; left-to-right pass
          (for ([i (in-range 1 n)])
            (when (> (vector-ref r i) (vector-ref r (- i 1)))
              (vector-set! candies i (+ 1 (vector-ref candies (- i 1))))))
          ;; right-to-left pass
          (for ([i (in-range (- n 2) -1 -1)])
            (when (and (> (vector-ref r i) (vector-ref r (+ i 1)))
                       (<= (vector-ref candies i) (vector-ref candies (+ i 1))))
              (vector-set! candies i (+ 1 (vector-ref candies (+ i 1))))))
          ;; total candies
          (for/sum ([i (in-range n)]) (vector-ref candies i))))))
```

## Erlang

```erlang
-module(solution).
-export([candy/1]).

-spec candy(Ratings :: [integer()]) -> integer().
candy(Ratings) ->
    Left = left_pass(Ratings),
    RightRev = left_pass(lists:reverse(Ratings)),
    Right = lists:reverse(RightRev),
    sum_max_lists(Left, Right, 0).

left_pass([First|Rest]) ->
    left_pass(Rest, First, 1, [1]);
left_pass([]) -> [].

left_pass([], _PrevRating, _PrevCandy, Acc) ->
    lists:reverse(Acc);
left_pass([R|Rest], PrevRating, PrevCandy, Acc) ->
    Candy = if R > PrevRating -> PrevCandy + 1; true -> 1 end,
    left_pass(Rest, R, Candy, [Candy | Acc]).

sum_max_lists([], [], Acc) -> Acc;
sum_max_lists([A|As], [B|Bs], Acc) ->
    sum_max_lists(As, Bs, Acc + erlang:max(A, B)).
```

## Elixir

```elixir
defmodule Solution do
  @spec candy(ratings :: [integer]) :: integer
  def candy(ratings) do
    # Left-to-right pass: assign minimum candies respecting left neighbor
    {left_rev, _prev_rating, _prev_candy} =
      Enum.reduce(ratings, {[], nil, 0}, fn rating, {candies_rev, prev_rating, prev_candy} ->
        candy =
          if prev_rating != nil and rating > prev_rating do
            prev_candy + 1
          else
            1
          end

        {[candy | candies_rev], rating, candy}
      end)

    left = Enum.reverse(left_rev)

    # Right-to-left pass while computing total candies needed
    rev_ratings = Enum.reverse(ratings)
    rev_left = Enum.reverse(left)

    {total, _, _} =
      Enum.reduce(Enum.zip(rev_ratings, rev_left), {0, nil, 0}, fn {rating, left_candy},
                                                                 {sum, next_rating, next_candy} ->
        candy =
          if next_rating != nil and rating > next_rating do
            max(left_candy, next_candy + 1)
          else
            left_candy
          end

        {sum + candy, rating, candy}
      end)

    total
  end
end
```
