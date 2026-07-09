# 1899. Merge Triplets to Form Target Triplet

## Cpp

```cpp
class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        int x = target[0], y = target[1], z = target[2];
        bool haveX = false, haveY = false, haveZ = false;
        for (const auto& t : triplets) {
            int a = t[0], b = t[1], c = t[2];
            if (a <= x && b <= y && c <= z) {
                if (a == x) haveX = true;
                if (b == y) haveY = true;
                if (c == z) haveZ = true;
            }
        }
        return haveX && haveY && haveZ;
    }
};
```

## Java

```java
class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int needA = target[0], needB = target[1], needC = target[2];
        int curA = 0, curB = 0, curC = 0;
        for (int[] t : triplets) {
            int a = t[0], b = t[1], c = t[2];
            if (a <= needA && b <= needB && c <= needC) {
                if (a > curA) curA = a;
                if (b > curB) curB = b;
                if (c > curC) curC = c;
            }
        }
        return curA == needA && curB == needB && curC == needC;
    }
}
```

## Python

```python
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        x, y, z = target
        have_x = have_y = have_z = False
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                if a == x:
                    have_x = True
                if b == y:
                    have_y = True
                if c == z:
                    have_z = True
                if have_x and have_y and have_z:
                    return True
        return False
```

## Python3

```python
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        need = [False, False, False]
        tx, ty, tz = target
        for a, b, c in triplets:
            if a <= tx and b <= ty and c <= tz:
                if a == tx:
                    need[0] = True
                if b == ty:
                    need[1] = True
                if c == tz:
                    need[2] = True
        return all(need)
```

## C

```c
#include <stdbool.h>

bool mergeTriplets(int** triplets, int tripletsSize, int* tripletsColSize, int* target, int targetSize) {
    int best0 = 0, best1 = 0, best2 = 0;
    for (int i = 0; i < tripletsSize; ++i) {
        int *t = triplets[i];
        if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
            if (t[0] > best0) best0 = t[0];
            if (t[1] > best1) best1 = t[1];
            if (t[2] > best2) best2 = t[2];
        }
    }
    return best0 == target[0] && best1 == target[1] && best2 == target[2];
}
```

## Csharp

```csharp
public class Solution {
    public bool MergeTriplets(int[][] triplets, int[] target) {
        int x = target[0], y = target[1], z = target[2];
        bool haveX = false, haveY = false, haveZ = false;
        foreach (var t in triplets) {
            if (t[0] <= x && t[1] <= y && t[2] <= z) {
                if (t[0] == x) haveX = true;
                if (t[1] == y) haveY = true;
                if (t[2] == z) haveZ = true;
            }
        }
        return haveX && haveY && haveZ;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} triplets
 * @param {number[]} target
 * @return {boolean}
 */
var mergeTriplets = function(triplets, target) {
    const [x, y, z] = target;
    let cur0 = 0, cur1 = 0, cur2 = 0;
    for (const t of triplets) {
        const a = t[0], b = t[1], c = t[2];
        if (a <= x && b <= y && c <= z) {
            if (a > cur0) cur0 = a;
            if (b > cur1) cur1 = b;
            if (c > cur2) cur2 = c;
        }
    }
    return cur0 === x && cur1 === y && cur2 === z;
};
```

## Typescript

```typescript
function mergeTriplets(triplets: number[][], target: number[]): boolean {
    const [tx, ty, tz] = target;
    let hasX = false, hasY = false, hasZ = false;
    for (const [a, b, c] of triplets) {
        if (a > tx || b > ty || c > tz) continue;
        if (a === tx) hasX = true;
        if (b === ty) hasY = true;
        if (c === tz) hasZ = true;
    }
    return hasX && hasY && hasZ;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $triplets
     * @param Integer[] $target
     * @return Boolean
     */
    function mergeTriplets($triplets, $target) {
        $mx = [0, 0, 0];
        foreach ($triplets as $t) {
            if ($t[0] <= $target[0] && $t[1] <= $target[1] && $t[2] <= $target[2]) {
                if ($t[0] > $mx[0]) $mx[0] = $t[0];
                if ($t[1] > $mx[1]) $mx[1] = $t[1];
                if ($t[2] > $mx[2]) $mx[2] = $t[2];
            }
        }
        return $mx[0] == $target[0] && $mx[1] == $target[1] && $mx[2] == $target[2];
    }
}
```

## Swift

```swift
class Solution {
    func mergeTriplets(_ triplets: [[Int]], _ target: [Int]) -> Bool {
        var hasX = false, hasY = false, hasZ = false
        let x = target[0], y = target[1], z = target[2]
        for t in triplets {
            if t[0] <= x && t[1] <= y && t[2] <= z {
                if t[0] == x { hasX = true }
                if t[1] == y { hasY = true }
                if t[2] == z { hasZ = true }
            }
        }
        return hasX && hasY && hasZ
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mergeTriplets(triplets: Array<IntArray>, target: IntArray): Boolean {
        var hasX = false
        var hasY = false
        var hasZ = false
        val x = target[0]
        val y = target[1]
        val z = target[2]
        for (t in triplets) {
            if (t[0] > x || t[1] > y || t[2] > z) continue
            if (t[0] == x) hasX = true
            if (t[1] == y) hasY = true
            if (t[2] == z) hasZ = true
        }
        return hasX && hasY && hasZ
    }
}
```

## Dart

```dart
class Solution {
  bool mergeTriplets(List<List<int>> triplets, List<int> target) {
    bool first = false, second = false, third = false;
    for (var t in triplets) {
      if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
        if (t[0] == target[0]) first = true;
        if (t[1] == target[1]) second = true;
        if (t[2] == target[2]) third = true;
      }
    }
    return first && second && third;
  }
}
```

## Golang

```go
func mergeTriplets(triplets [][]int, target []int) bool {
	x, y, z := target[0], target[1], target[2]
	hasX, hasY, hasZ := false, false, false
	for _, t := range triplets {
		a, b, c := t[0], t[1], t[2]
		if a <= x && b <= y && c <= z {
			if a == x {
				hasX = true
			}
			if b == y {
				hasY = true
			}
			if c == z {
				hasZ = true
			}
		}
	}
	return hasX && hasY && hasZ
}
```

## Ruby

```ruby
def merge_triplets(triplets, target)
  x, y, z = target
  have_x = have_y = have_z = false
  triplets.each do |a, b, c|
    next if a > x || b > y || c > z
    have_x ||= (a == x)
    have_y ||= (b == y)
    have_z ||= (c == z)
  end
  have_x && have_y && have_z
end
```

## Scala

```scala
object Solution {
    def mergeTriplets(triplets: Array[Array[Int]], target: Array[Int]): Boolean = {
        val x = target(0)
        val y = target(1)
        val z = target(2)
        var hasX = false
        var hasY = false
        var hasZ = false

        for (t <- triplets) {
            if (t(0) <= x && t(1) <= y && t(2) <= z) {
                if (t(0) == x) hasX = true
                if (t(1) == y) hasY = true
                if (t(2) == z) hasZ = true
            }
        }

        hasX && hasY && hasZ
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge_triplets(triplets: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let mut have = [false; 3];
        for t in triplets.iter() {
            if t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2] {
                if t[0] == target[0] { have[0] = true; }
                if t[1] == target[1] { have[1] = true; }
                if t[2] == target[2] { have[2] = true; }
            }
        }
        have.iter().all(|&v| v)
    }
}
```

## Racket

```racket
(define/contract (merge-triplets triplets target)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) boolean?)
  (let* ((x (first target))
         (y (second target))
         (z (third target)))
    (let loop ((lst triplets) (fx #f) (fy #f) (fz #f))
      (cond
        [(null? lst) (and fx fy fz)]
        [else
         (define t (first lst))
         (define a (first t))
         (define b (second t))
         (define c (third t))
         (if (and (<= a x) (<= b y) (<= c z))
             (loop (rest lst)
                   (or fx (= a x))
                   (or fy (= b y))
                   (or fz (= c z)))
             (loop (rest lst) fx fy fz))]))))
```

## Erlang

```erlang
-spec merge_triplets(Triplets :: [[integer()]], Target :: [integer()]) -> boolean().
merge_triplets(Triplets, [X,Y,Z]) ->
    {Fx,Fy,Fz} = lists:foldl(
        fun([A,B,C], {F1,F2,F3}) ->
            if A =< X andalso B =< Y andalso C =< Z ->
                    {F1 orelse (A == X), F2 orelse (B == Y), F3 orelse (C == Z)};
               true -> {F1,F2,F3}
            end
        end,
        {false,false,false},
        Triplets),
    Fx andalso Fy andalso Fz.
```

## Elixir

```elixir
defmodule Solution do
  @spec merge_triplets(triplets :: [[integer]], target :: [integer]) :: boolean
  def merge_triplets(triplets, target) do
    [x, y, z] = target

    {has_x, has_y, has_z} =
      Enum.reduce(triplets, {false, false, false}, fn [a, b, c], {fx, fy, fz} ->
        if a <= x and b <= y and c <= z do
          {
            fx or a == x,
            fy or b == y,
            fz or c == z
          }
        else
          {fx, fy, fz}
        end
      end)

    has_x and has_y and has_z
  end
end
```
