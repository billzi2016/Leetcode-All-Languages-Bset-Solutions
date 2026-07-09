# 1395. Count Number of Teams

## Cpp

```cpp
class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int ans = 0;
        for (int j = 0; j < n; ++j) {
            int leftSmaller = 0, leftLarger = 0;
            for (int i = 0; i < j; ++i) {
                if (rating[i] < rating[j]) ++leftSmaller;
                else ++leftLarger;
            }
            int rightSmaller = 0, rightLarger = 0;
            for (int k = j + 1; k < n; ++k) {
                if (rating[k] > rating[j]) ++rightLarger;
                else ++rightSmaller;
            }
            ans += leftSmaller * rightLarger + leftLarger * rightSmaller;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numTeams(int[] rating) {
        int n = rating.length;
        int teams = 0;
        for (int mid = 0; mid < n; ++mid) {
            int leftLess = 0, leftGreater = 0;
            for (int i = 0; i < mid; ++i) {
                if (rating[i] < rating[mid]) {
                    leftLess++;
                } else {
                    leftGreater++;
                }
            }
            int rightLess = 0, rightGreater = 0;
            for (int k = mid + 1; k < n; ++k) {
                if (rating[k] > rating[mid]) {
                    rightGreater++;
                } else {
                    rightLess++;
                }
            }
            teams += leftLess * rightGreater + leftGreater * rightLess;
        }
        return teams;
    }
}
```

## Python

```python
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        ans = 0
        for i in range(n):
            left_smaller = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller += 1
            left_larger = i - left_smaller

            right_larger = 0
            for k in range(i + 1, n):
                if rating[k] > rating[i]:
                    right_larger += 1
            right_smaller = (n - i - 1) - right_larger

            ans += left_smaller * right_larger + left_larger * right_smaller
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total = 0
        for j in range(n):
            left_smaller = left_larger = right_smaller = right_larger = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_larger += 1
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                else:
                    right_smaller += 1
            total += left_smaller * right_larger + left_larger * right_smaller
        return total
```

## C

```c
#include <stddef.h>

int numTeams(int* rating, int ratingSize) {
    int total = 0;
    for (int i = 0; i < ratingSize; ++i) {
        int leftSmaller = 0, leftLarger = 0;
        for (int j = 0; j < i; ++j) {
            if (rating[j] < rating[i]) leftSmaller++;
            else leftLarger++;
        }
        int rightSmaller = 0, rightLarger = 0;
        for (int k = i + 1; k < ratingSize; ++k) {
            if (rating[k] > rating[i]) rightLarger++;
            else rightSmaller++;
        }
        total += leftSmaller * rightLarger + leftLarger * rightSmaller;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumTeams(int[] rating)
    {
        int n = rating.Length;
        int total = 0;
        for (int i = 0; i < n; i++)
        {
            int leftLess = 0, leftGreater = 0;
            for (int j = 0; j < i; j++)
            {
                if (rating[j] < rating[i]) leftLess++;
                else if (rating[j] > rating[i]) leftGreater++;
            }

            int rightLess = 0, rightGreater = 0;
            for (int k = i + 1; k < n; k++)
            {
                if (rating[k] < rating[i]) rightLess++;
                else if (rating[k] > rating[i]) rightGreater++;
            }

            total += leftLess * rightGreater + leftGreater * rightLess;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rating
 * @return {number}
 */
var numTeams = function(rating) {
    const n = rating.length;
    let total = 0;
    for (let j = 0; j < n; ++j) {
        let leftSmaller = 0, leftLarger = 0;
        for (let i = 0; i < j; ++i) {
            if (rating[i] < rating[j]) leftSmaller++;
            else leftLarger++;
        }
        let rightSmaller = 0, rightLarger = 0;
        for (let k = j + 1; k < n; ++k) {
            if (rating[k] > rating[j]) rightLarger++;
            else rightSmaller++;
        }
        total += leftSmaller * rightLarger + leftLarger * rightSmaller;
    }
    return total;
};
```

## Typescript

```typescript
function numTeams(rating: number[]): number {
    const n = rating.length;
    let total = 0;
    for (let j = 0; j < n; ++j) {
        let leftSmaller = 0, leftLarger = 0;
        let rightSmaller = 0, rightLarger = 0;
        for (let i = 0; i < j; ++i) {
            if (rating[i] < rating[j]) leftSmaller++;
            else leftLarger++;
        }
        for (let k = j + 1; k < n; ++k) {
            if (rating[k] > rating[j]) rightLarger++;
            else rightSmaller++;
        }
        total += leftSmaller * rightLarger + leftLarger * rightSmaller;
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $rating
     * @return Integer
     */
    function numTeams($rating) {
        $n = count($rating);
        $teams = 0;
        for ($j = 0; $j < $n; $j++) {
            $leftSmaller = 0;
            $leftLarger = 0;
            for ($i = 0; $i < $j; $i++) {
                if ($rating[$i] < $rating[$j]) {
                    $leftSmaller++;
                } else {
                    $leftLarger++;
                }
            }
            $rightLarger = 0;
            $rightSmaller = 0;
            for ($k = $j + 1; $k < $n; $k++) {
                if ($rating[$k] > $rating[$j]) {
                    $rightLarger++;
                } else {
                    $rightSmaller++;
                }
            }
            $teams += $leftSmaller * $rightLarger + $leftLarger * $rightSmaller;
        }
        return $teams;
    }
}
```

## Swift

```swift
class Solution {
    func numTeams(_ rating: [Int]) -> Int {
        let n = rating.count
        var total = 0
        for j in 0..<n {
            var leftSmaller = 0
            var leftLarger = 0
            for i in 0..<j {
                if rating[i] < rating[j] {
                    leftSmaller += 1
                } else {
                    leftLarger += 1
                }
            }
            var rightLarger = 0
            var rightSmaller = 0
            for k in (j + 1)..<n {
                if rating[k] > rating[j] {
                    rightLarger += 1
                } else {
                    rightSmaller += 1
                }
            }
            total += leftSmaller * rightLarger + leftLarger * rightSmaller
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numTeams(rating: IntArray): Int {
        val n = rating.size
        var total = 0L
        for (j in 0 until n) {
            var leftSmaller = 0
            var leftGreater = 0
            for (i in 0 until j) {
                if (rating[i] < rating[j]) leftSmaller++ else leftGreater++
            }
            var rightLarger = 0
            var rightSmaller = 0
            for (k in j + 1 until n) {
                if (rating[k] > rating[j]) rightLarger++ else rightSmaller++
            }
            total += leftSmaller.toLong() * rightLarger + leftGreater.toLong() * rightSmaller
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numTeams(List<int> rating) {
    int n = rating.length;
    int ans = 0;
    for (int j = 0; j < n; j++) {
      int leftSmaller = 0, leftLarger = 0;
      for (int i = 0; i < j; i++) {
        if (rating[i] < rating[j]) {
          leftSmaller++;
        } else {
          leftLarger++;
        }
      }
      int rightSmaller = 0, rightLarger = 0;
      for (int k = j + 1; k < n; k++) {
        if (rating[k] > rating[j]) {
          rightLarger++;
        } else {
          rightSmaller++;
        }
      }
      ans += leftSmaller * rightLarger + leftLarger * rightSmaller;
    }
    return ans;
  }
}
```

## Golang

```go
func numTeams(rating []int) int {
	n := len(rating)
	ans := 0
	for i := 0; i < n; i++ {
		leftLess, leftGreater := 0, 0
		for j := 0; j < i; j++ {
			if rating[j] < rating[i] {
				leftLess++
			} else if rating[j] > rating[i] {
				leftGreater++
			}
		}
		rightLess, rightGreater := 0, 0
		for k := i + 1; k < n; k++ {
			if rating[k] < rating[i] {
				rightLess++
			} else if rating[k] > rating[i] {
				rightGreater++
			}
		}
		ans += leftLess*rightGreater + leftGreater*rightLess
	}
	return ans
}
```

## Ruby

```ruby
def num_teams(rating)
  n = rating.length
  total = 0
  (0...n).each do |j|
    left_smaller = 0
    left_larger = 0
    (0...j).each do |i|
      if rating[i] < rating[j]
        left_smaller += 1
      else
        left_larger += 1
      end
    end

    right_larger = 0
    right_smaller = 0
    ((j + 1)...n).each do |k|
      if rating[k] > rating[j]
        right_larger += 1
      else
        right_smaller += 1
      end
    end

    total += left_smaller * right_larger + left_larger * right_smaller
  end
  total
end
```

## Scala

```scala
object Solution {
    def numTeams(rating: Array[Int]): Int = {
        val n = rating.length
        var total: Long = 0L
        var j = 0
        while (j < n) {
            var leftSmaller = 0
            var leftLarger = 0
            var rightSmaller = 0
            var rightLarger = 0

            var i = 0
            while (i < j) {
                if (rating(i) < rating(j)) leftSmaller += 1 else leftLarger += 1
                i += 1
            }

            var k = j + 1
            while (k < n) {
                if (rating(k) > rating(j)) rightLarger += 1 else rightSmaller += 1
                k += 1
            }

            total += leftSmaller.toLong * rightLarger + leftLarger.toLong * rightSmaller
            j += 1
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_teams(rating: Vec<i32>) -> i32 {
        let n = rating.len();
        let mut ans: i64 = 0;
        for j in 0..n {
            let mut left_smaller: i64 = 0;
            let mut left_larger: i64 = 0;
            for i in 0..j {
                if rating[i] < rating[j] {
                    left_smaller += 1;
                } else {
                    left_larger += 1;
                }
            }
            let mut right_larger: i64 = 0;
            let mut right_smaller: i64 = 0;
            for k in (j + 1)..n {
                if rating[k] > rating[j] {
                    right_larger += 1;
                } else {
                    right_smaller += 1;
                }
            }
            ans += left_smaller * right_larger + left_larger * right_smaller;
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (num-teams rating)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector rating))
         (n (vector-length v)))
    (let loop-j ((j 0) (total 0))
      (if (= j n)
          total
          (let* ((mid (vector-ref v j))
                 (left-smaller (for/sum ([i (in-range 0 j)]
                                         #:when (< (vector-ref v i) mid)) 1))
                 (left-larger (for/sum ([i (in-range 0 j)]
                                        #:when (> (vector-ref v i) mid)) 1))
                 (right-smaller (for/sum ([k (in-range (+ j 1) n)]
                                          #:when (< (vector-ref v k) mid)) 1))
                 (right-larger (for/sum ([k (in-range (+ j 1) n)]
                                         #:when (> (vector-ref v k) mid)) 1)))
            (loop-j (+ j 1)
                    (+ total
                       (* left-smaller right-larger)
                       (* left-larger right-smaller))))))))
```

## Erlang

```erlang
-module(solution).
-export([num_teams/1]).

-spec num_teams([integer()]) -> integer().
num_teams(Rating) ->
    Tuple = list_to_tuple(Rating),
    N = tuple_size(Tuple),
    loop(Tuple, N, 1, 0).

loop(_Tuple, N, I, Acc) when I > N -> Acc;
loop(Tuple, N, I, Acc) ->
    MidVal = element(I, Tuple),
    {LeftSmaller, LeftLarger} = count_left(Tuple, I - 1, MidVal, 0, 0),
    {RightLarger, RightSmaller} = count_right(Tuple, I + 1, N, MidVal, 0, 0),
    NewAcc = Acc + LeftSmaller * RightLarger + LeftLarger * RightSmaller,
    loop(Tuple, N, I + 1, NewAcc).

count_left(_Tuple, 0, _MidVal, LS, LL) -> {LS, LL};
count_left(Tuple, Index, MidVal, LS, LL) ->
    Val = element(Index, Tuple),
    if
        Val < MidVal ->
            count_left(Tuple, Index - 1, MidVal, LS + 1, LL);
        true ->
            count_left(Tuple, Index - 1, MidVal, LS, LL + 1)
    end.

count_right(_Tuple, StartIdx, EndIdx, _MidVal, RL, RS) when StartIdx > EndIdx -> {RL, RS};
count_right(Tuple, Index, EndIdx, MidVal, RL, RS) ->
    Val = element(Index, Tuple),
    if
        Val > MidVal ->
            count_right(Tuple, Index + 1, EndIdx, MidVal, RL + 1, RS);
        true ->
            count_right(Tuple, Index + 1, EndIdx, MidVal, RL, RS + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_teams(rating :: [integer]) :: integer
  def num_teams(rating) do
    t = List.to_tuple(rating)
    n = tuple_size(t)

    0..(n - 1)
    |> Enum.reduce(0, fn mid, acc ->
      val_mid = elem(t, mid)

      left_smaller =
        if mid == 0 do
          0
        else
          0..(mid - 1)
          |> Enum.count(fn i -> elem(t, i) < val_mid end)
        end

      right_larger =
        if mid == n - 1 do
          0
        else
          (mid + 1)..(n - 1)
          |> Enum.count(fn j -> elem(t, j) > val_mid end)
        end

      left_larger = mid - left_smaller
      right_smaller = (n - mid - 1) - right_larger

      acc + left_smaller * right_larger + left_larger * right_smaller
    end)
  end
end
```
