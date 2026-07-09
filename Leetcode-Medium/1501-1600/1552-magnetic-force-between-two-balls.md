# 1552. Magnetic Force Between Two Balls

## Cpp

```cpp
class Solution {
public:
    bool canPlace(const vector<int>& pos, int m, long long dist) {
        int count = 1;
        long long last = pos[0];
        for (size_t i = 1; i < pos.size(); ++i) {
            if ((long long)pos[i] - last >= dist) {
                ++count;
                last = pos[i];
                if (count == m) return true;
            }
        }
        return false;
    }

    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        long long low = 0;
        long long high = (long long)position.back() - position.front();
        long long ans = 0;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (canPlace(position, m, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxDistance(int[] position, int m) {
        java.util.Arrays.sort(position);
        int n = position.length;
        long low = 1;
        long high = (long)position[n - 1] - position[0];
        int answer = 0;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (canPlace(position, m, mid)) {
                answer = (int)mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return answer;
    }

    private boolean canPlace(int[] pos, int balls, long minDist) {
        int count = 1;
        long lastPos = pos[0];
        for (int i = 1; i < pos.length && count < balls; i++) {
            if ((long)pos[i] - lastPos >= minDist) {
                count++;
                lastPos = pos[i];
            }
        }
        return count >= balls;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        low, high = 1, (position[-1] - position[0]) // (m - 1)
        ans = 0

        def can_place(dist):
            count = 1
            last = position[0]
            for p in position[1:]:
                if p - last >= dist:
                    count += 1
                    last = p
                    if count == m:
                        return True
            return False

        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
```

## Python3

```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def can_place(dist: int) -> bool:
            cnt = 1
            last = position[0]
            for p in position[1:]:
                if p - last >= dist:
                    cnt += 1
                    last = p
                    if cnt == m:
                        return True
            return False
        
        low, high = 1, position[-1] - position[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    if (av < bv) return -1;
    if (av > bv) return 1;
    return 0;
}

static int canPlace(int *pos, int n, int m, int dist) {
    int count = 1;
    int last = pos[0];
    for (int i = 1; i < n; ++i) {
        if (pos[i] - last >= dist) {
            ++count;
            last = pos[i];
            if (count >= m) return 1;
        }
    }
    return 0;
}

int maxDistance(int* position, int positionSize, int m) {
    qsort(position, positionSize, sizeof(int), cmp_int);
    int low = 1;
    int high = position[positionSize - 1] - position[0];
    int ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (canPlace(position, positionSize, m, mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxDistance(int[] position, int m)
    {
        Array.Sort(position);
        int n = position.Length;
        int low = 1;
        int high = position[n - 1] - position[0];
        int ans = 0;

        while (low <= high)
        {
            int mid = low + (high - low) / 2;
            if (CanPlace(position, m, mid))
            {
                ans = mid;
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }

        return ans;
    }

    private bool CanPlace(int[] pos, int m, int dist)
    {
        int count = 1;
        int lastPos = pos[0];
        for (int i = 1; i < pos.Length && count < m; i++)
        {
            if (pos[i] - lastPos >= dist)
            {
                count++;
                lastPos = pos[i];
            }
        }
        return count >= m;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} position
 * @param {number} m
 * @return {number}
 */
var maxDistance = function(position, m) {
    position.sort((a, b) => a - b);
    const n = position.length;
    
    const canPlace = (dist) => {
        let count = 1;
        let last = position[0];
        for (let i = 1; i < n && count < m; i++) {
            if (position[i] - last >= dist) {
                count++;
                last = position[i];
            }
        }
        return count >= m;
    };
    
    let low = 1;
    let high = position[n - 1] - position[0];
    let ans = 0;
    
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (canPlace(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function maxDistance(position: number[], m: number): number {
    position.sort((a, b) => a - b);
    let low = 1;
    let high = position[position.length - 1] - position[0];
    let ans = 0;

    const canPlace = (dist: number): boolean => {
        let count = 1;
        let lastPos = position[0];
        for (let i = 1; i < position.length; i++) {
            if (position[i] - lastPos >= dist) {
                count++;
                lastPos = position[i];
                if (count >= m) return true;
            }
        }
        return false;
    };

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (canPlace(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $position
     * @param Integer $m
     * @return Integer
     */
    function maxDistance($position, $m) {
        sort($position);
        $n = count($position);
        $low = 1;
        $high = $position[$n - 1] - $position[0];
        $ans = 0;

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canPlace($position, $m, $mid)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }

        return $ans;
    }

    private function canPlace($pos, $m, $dist) {
        $count = 1;
        $last = $pos[0];
        $n = count($pos);
        for ($i = 1; $i < $n; $i++) {
            if ($pos[$i] - $last >= $dist) {
                $count++;
                $last = $pos[$i];
                if ($count >= $m) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistance(_ position: [Int], _ m: Int) -> Int {
        let sortedPos = position.sorted()
        var low = 0
        var high = (sortedPos.last! - sortedPos.first!) / (m - 1)
        var answer = 0

        func canPlace(_ dist: Int) -> Bool {
            var count = 1
            var last = sortedPos[0]
            for i in 1..<sortedPos.count {
                if sortedPos[i] - last >= dist {
                    count += 1
                    last = sortedPos[i]
                    if count == m { return true }
                }
            }
            return false
        }

        while low <= high {
            let mid = (low + high) / 2
            if canPlace(mid) {
                answer = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistance(position: IntArray, m: Int): Int {
        position.sort()
        var low = 1
        var high = (position.last() - position.first()) / (m - 1)
        var answer = 0

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (canPlace(mid, position, m)) {
                answer = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return answer
    }

    private fun canPlace(dist: Int, pos: IntArray, m: Int): Boolean {
        var count = 1
        var lastPos = pos[0]
        for (i in 1 until pos.size) {
            if (pos[i] - lastPos >= dist) {
                count++
                lastPos = pos[i]
                if (count >= m) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  int maxDistance(List<int> position, int m) {
    position.sort();
    int low = 1;
    int high = position.last - position.first;
    int ans = 0;

    bool canPlace(int dist) {
      int count = 1;
      int lastPos = position[0];
      for (int i = 1; i < position.length && count < m; ++i) {
        if (position[i] - lastPos >= dist) {
          count++;
          lastPos = position[i];
        }
      }
      return count >= m;
    }

    while (low <= high) {
      int mid = low + ((high - low) >> 1);
      if (canPlace(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func maxDistance(position []int, m int) int {
	sort.Ints(position)
	low, high := 1, position[len(position)-1]-position[0]
	ans := 0
	for low <= high {
		mid := low + (high-low)/2
		if canPlace(position, m, mid) {
			ans = mid
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return ans
}

func canPlace(pos []int, m int, dist int) bool {
	count := 1
	last := pos[0]
	for i := 1; i < len(pos); i++ {
		if pos[i]-last >= dist {
			count++
			last = pos[i]
			if count >= m {
				return true
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def max_distance(position, m)
  position.sort!
  left = 0
  right = position[-1] - position[0]
  ans = 0

  while left <= right
    mid = (left + right) / 2
    if can_place?(position, m, mid)
      ans = mid
      left = mid + 1
    else
      right = mid - 1
    end
  end

  ans
end

def can_place?(pos, m, dist)
  count = 1
  last = pos[0]
  pos.each do |p|
    if p - last >= dist
      count += 1
      last = p
      return true if count >= m
    end
  end
  false
end
```

## Scala

```scala
object Solution {
  def maxDistance(position: Array[Int], m: Int): Int = {
    java.util.Arrays.sort(position)
    val n = position.length
    var low = 1
    var high = position(n - 1) - position(0)
    var ans = 0

    def canPlace(gap: Int): Boolean = {
      var count = 1
      var lastPos = position(0)
      var i = 1
      while (i < n && count < m) {
        if (position(i) - lastPos >= gap) {
          count += 1
          lastPos = position(i)
        }
        i += 1
      }
      count >= m
    }

    while (low <= high) {
      val mid = low + (high - low) / 2
      if (canPlace(mid)) {
        ans = mid
        low = mid + 1
      } else {
        high = mid - 1
      }
    }
    ans
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn max_distance(position: Vec<i32>, m: i32) -> i32 {
        let mut pos = position;
        pos.sort_unstable();
        let n = pos.len();
        if m as usize <= 1 {
            return 0;
        }
        let mut low: i64 = 1;
        let mut high: i64 = (pos[n - 1] - pos[0]) as i64;
        let mut ans: i64 = 0;
        while low <= high {
            let mid = (low + high) / 2;
            if Self::can_place(&pos, m as usize, mid) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        ans as i32
    }

    fn can_place(pos: &Vec<i32>, balls: usize, dist: i64) -> bool {
        let mut count = 1usize;
        let mut last = pos[0] as i64;
        for &p in pos.iter().skip(1) {
            if (p as i64 - last) >= dist {
                count += 1;
                last = p as i64;
                if count >= balls {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract
         racket/list)

(define/contract (max-distance position m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort position <))
         (n (length sorted))
         (low 0)
         (high (- (last sorted) (first sorted)))
         (can-place?
          (lambda (dist)
            (let loop ((cnt 1)
                       (prev (car sorted))
                       (rest (cdr sorted)))
              (cond
                [(>= cnt m) #t]
                [(null? rest) #f]
                [else
                 (define p (car rest))
                 (if (>= (- p prev) dist)
                     (loop (+ cnt 1) p (cdr rest))
                     (loop cnt prev (cdr rest)))])))))
    (let search ((lo low) (hi high) (best 0))
      (if (> lo hi)
          best
          (let* ((mid (quotient (+ lo hi) 2)))
            (if (can-place? mid)
                (search (+ mid 1) hi mid)
                (search lo (- mid 1) best)))))))
```

## Erlang

```erlang
-spec max_distance([integer()], integer()) -> integer().
max_distance(Position, M) ->
    Sorted = lists:sort(Position),
    MinPos = hd(Sorted),
    MaxPos = lists:last(Sorted),
    binary_search(1, MaxPos - MinPos, Sorted, M, 0).

binary_search(Low, High, _Sorted, _M, Ans) when Low > High ->
    Ans;
binary_search(Low, High, Sorted, M, Ans) ->
    Mid = (Low + High) div 2,
    case can_place(Mid, Sorted, M) of
        true -> binary_search(Mid + 1, High, Sorted, M, Mid);
        false -> binary_search(Low, Mid - 1, Sorted, M, Ans)
    end.

can_place(Gap, [First|Rest], M) ->
    can_place_loop(Rest, First, Gap, 1, M).

can_place_loop(_PosList, _LastPos, _Gap, Count, M) when Count >= M ->
    true;
can_place_loop([], _LastPos, _Gap, _Count, _M) ->
    false;
can_place_loop([Pos|Tail], LastPos, Gap, Count, M) ->
    if Pos - LastPos >= Gap ->
            can_place_loop(Tail, Pos, Gap, Count + 1, M);
       true ->
            can_place_loop(Tail, LastPos, Gap, Count, M)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distance(position :: [integer], m :: integer) :: integer
  def max_distance(position, m) do
    sorted = Enum.sort(position)
    low = 1
    high = List.last(sorted) - hd(sorted)
    binary_search(low, high, sorted, m, 0)
  end

  defp binary_search(low, high, _positions, _m, ans) when low > high, do: ans

  defp binary_search(low, high, positions, m, _ans) do
    mid = div(low + high, 2)

    if can_place?(mid, positions, m) do
      binary_search(mid + 1, high, positions, m, mid)
    else
      binary_search(low, mid - 1, positions, m, 0)
    end
  end

  defp can_place?(dist, positions, m) do
    {count, _} =
      Enum.reduce_while(tl(positions), {1, hd(positions)}, fn pos, {c, last} ->
        cond do
          c >= m -> {:halt, {c, last}}
          pos - last >= dist -> {:cont, {c + 1, pos}}
          true -> {:cont, {c, last}}
        end
      end)

    count >= m
  end
end
```
