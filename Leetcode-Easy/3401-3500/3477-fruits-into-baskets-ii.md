# 3477. Fruits Into Baskets II

## Cpp

```cpp
class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size();
        int unplaced = 0;
        for (int i = 0; i < n; ++i) {
            bool placed = false;
            for (int j = 0; j < n; ++j) {
                if (baskets[j] >= fruits[i]) {
                    baskets[j] = 0; // mark basket as used
                    placed = true;
                    break;
                }
            }
            if (!placed) ++unplaced;
        }
        return unplaced;
    }
};
```

## Java

```java
class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = fruits.length;
        int unplaced = 0;
        boolean[] used = new boolean[n];
        for (int i = 0; i < n; i++) {
            boolean placed = false;
            for (int j = 0; j < n; j++) {
                if (!used[j] && baskets[j] >= fruits[i]) {
                    used[j] = true;
                    placed = true;
                    break;
                }
            }
            if (!placed) {
                unplaced++;
            }
        }
        return unplaced;
    }
}
```

## Python

```python
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        unplaced = 0
        for f in fruits:
            placed = False
            for i in range(len(baskets)):
                if baskets[i] >= f:
                    baskets[i] = 0  # mark as used
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced
```

## Python3

```python
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for fruit in fruits:
            placed = False
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = 0  # mark basket as used
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced
```

## C

```c
int numOfUnplacedFruits(int* fruits, int fruitsSize, int* baskets, int basketsSize) {
    int unplaced = 0;
    for (int i = 0; i < fruitsSize; ++i) {
        int placed = 0;
        for (int j = 0; j < basketsSize; ++j) {
            if (baskets[j] >= fruits[i]) {
                baskets[j] = 0; // mark as used
                placed = 1;
                break;
            }
        }
        if (!placed) {
            ++unplaced;
        }
    }
    return unplaced;
}
```

## Csharp

```csharp
public class Solution {
    public int NumOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = fruits.Length;
        int unplaced = 0;
        for (int i = 0; i < n; i++) {
            bool placed = false;
            for (int j = 0; j < n; j++) {
                if (baskets[j] >= fruits[i]) {
                    baskets[j] = 0; // mark basket as used
                    placed = true;
                    break;
                }
            }
            if (!placed) unplaced++;
        }
        return unplaced;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function(fruits, baskets) {
    let unplaced = 0;
    const m = baskets.length;
    for (let i = 0; i < fruits.length; ++i) {
        let placed = false;
        for (let j = 0; j < m; ++j) {
            if (baskets[j] >= fruits[i]) {
                // use this basket
                baskets[j] = 0; // mark as used
                placed = true;
                break;
            }
        }
        if (!placed) unplaced++;
    }
    return unplaced;
};
```

## Typescript

```typescript
function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
    let unplaced = 0;
    const m = fruits.length;
    for (let i = 0; i < m; i++) {
        let placed = false;
        for (let j = 0; j < m; j++) {
            if (baskets[j] >= fruits[i]) {
                baskets[j] = 0; // mark as used
                placed = true;
                break;
            }
        }
        if (!placed) unplaced++;
    }
    return unplaced;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $fruits
     * @param Integer[] $baskets
     * @return Integer
     */
    function numOfUnplacedFruits($fruits, $baskets) {
        $n = count($fruits);
        $unplaced = 0;
        for ($i = 0; $i < $n; $i++) {
            $found = false;
            for ($j = 0; $j < $n; $j++) {
                if ($baskets[$j] >= $fruits[$i]) {
                    $baskets[$j] = 0; // mark basket as used
                    $found = true;
                    break;
                }
            }
            if (!$found) {
                $unplaced++;
            }
        }
        return $unplaced;
    }
}
```

## Swift

```swift
class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        var basketCap = baskets
        var unplaced = 0
        for fruit in fruits {
            var placed = false
            for i in 0..<basketCap.count {
                if basketCap[i] >= fruit {
                    basketCap[i] = 0
                    placed = true
                    break
                }
            }
            if !placed { unplaced += 1 }
        }
        return unplaced
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfUnplacedFruits(fruits: IntArray, baskets: IntArray): Int {
        var unplaced = 0
        for (fruit in fruits) {
            var placed = false
            for (i in baskets.indices) {
                if (baskets[i] >= fruit) {
                    baskets[i] = 0
                    placed = true
                    break
                }
            }
            if (!placed) unplaced++
        }
        return unplaced
    }
}
```

## Dart

```dart
class Solution {
  int numOfUnplacedFruits(List<int> fruits, List<int> baskets) {
    int unplaced = 0;
    for (int fruit in fruits) {
      bool placed = false;
      for (int i = 0; i < baskets.length; i++) {
        if (baskets[i] >= fruit) {
          baskets[i] = 0; // mark as used
          placed = true;
          break;
        }
      }
      if (!placed) unplaced++;
    }
    return unplaced;
  }
}
```

## Golang

```go
func numOfUnplacedFruits(fruits []int, baskets []int) int {
	unplaced := 0
	for _, f := range fruits {
		placed := false
		for i, b := range baskets {
			if b >= f && b > 0 {
				baskets[i] = 0
				placed = true
				break
			}
		}
		if !placed {
			unplaced++
		}
	}
	return unplaced
}
```

## Ruby

```ruby
def num_of_unplaced_fruits(fruits, baskets)
  unplaced = 0
  fruits.each do |fruit|
    placed = false
    baskets.each_with_index do |cap, i|
      if cap >= fruit && cap > 0
        baskets[i] = 0
        placed = true
        break
      end
    end
    unplaced += 1 unless placed
  end
  unplaced
end
```

## Scala

```scala
object Solution {
    def numOfUnplacedFruits(fruits: Array[Int], baskets: Array[Int]): Int = {
        var unplaced = 0
        val used = new Array[Boolean](baskets.length)
        for (fruit <- fruits) {
            var placed = false
            var i = 0
            while (i < baskets.length && !placed) {
                if (!used(i) && baskets(i) >= fruit) {
                    used(i) = true
                    placed = true
                }
                i += 1
            }
            if (!placed) unplaced += 1
        }
        unplaced
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        let mut baskets = baskets;
        let mut unplaced = 0;
        for fruit in fruits.iter() {
            let mut placed = false;
            for cap in baskets.iter_mut() {
                if *cap >= *fruit {
                    *cap = 0; // mark basket as used
                    placed = true;
                    break;
                }
            }
            if !placed {
                unplaced += 1;
            }
        }
        unplaced
    }
}
```

## Racket

```racket
(define/contract (num-of-unplaced-fruits fruits baskets)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((bvec (list->vector baskets))
         (n (vector-length bvec)))
    (define (try-place! fruit)
      (let loop ((i 0))
        (cond [(>= i n) #f]
              [(>= (vector-ref bvec i) fruit)
               (vector-set! bvec i 0)
               #t]
              [else (loop (+ i 1))])))
    (let rec ((fs fruits) (cnt 0))
      (if (null? fs)
          cnt
          (let ((placed (try-place! (car fs))))
            (rec (cdr fs) (if placed cnt (+ cnt 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([num_of_unplaced_fruits/2]).

-spec num_of_unplaced_fruits(Fruits :: [integer()], Baskets :: [integer()]) -> integer().
num_of_unplaced_fruits(Fruits, Baskets) ->
    num_of_unplaced_fruits(Fruits, Baskets, 0).

num_of_unplaced_fruits([], _Baskets, Count) ->
    Count;
num_of_unplaced_fruits([F|Fs], Baskets, Count) ->
    case place_fruit(F, Baskets) of
        {NewBaskets, true} ->
            num_of_unplaced_fruits(Fs, NewBaskets, Count);
        {UnchangedBaskets, false} ->
            num_of_unplaced_fruits(Fs, UnchangedBaskets, Count + 1)
    end.

place_fruit(_F, []) ->
    {[], false};
place_fruit(F, [Cap|Rest]) when Cap >= F ->
    {[0|Rest], true};
place_fruit(F, [Cap|Rest]) ->
    case place_fruit(F, Rest) of
        {NewRest, Placed} ->
            {[Cap|NewRest], Placed}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_unplaced_fruits(fruits :: [integer], baskets :: [integer]) :: integer
  def num_of_unplaced_fruits(fruits, baskets) do
    {unplaced, _} =
      Enum.reduce(fruits, {0, baskets}, fn fruit, {cnt, cur_baskets} ->
        case Enum.find_index(cur_baskets, &(&1 >= fruit)) do
          nil -> {cnt + 1, cur_baskets}
          idx ->
            new_baskets = List.replace_at(cur_baskets, idx, 0)
            {cnt, new_baskets}
        end
      end)

    unplaced
  end
end
```
