# 1936. Add Minimum Number of Rungs

## Cpp

```cpp
class Solution {
public:
    int addRungs(vector<int>& rungs, int dist) {
        long long added = 0;
        long long prev = 0;
        for (int h : rungs) {
            long long gap = (long long)h - prev;
            if (gap > dist) {
                added += (gap - 1) / dist;
            }
            prev = h;
        }
        return (int)added;
    }
};
```

## Java

```java
class Solution {
    public int addRungs(int[] rungs, int dist) {
        long added = 0;
        int prev = 0;
        for (int rung : rungs) {
            int gap = rung - prev;
            if (gap > dist) {
                added += (gap - 1) / dist;
            }
            prev = rung;
        }
        return (int) added;
    }
}
```

## Python

```python
class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        added = 0
        prev = 0
        for rung in rungs:
            gap = rung - prev
            if gap > dist:
                # number of extra rungs needed
                added += (gap - 1) // dist
            prev = rung
        return added
```

## Python3

```python
class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        added = 0
        prev = 0
        for h in rungs:
            diff = h - prev
            if diff > dist:
                added += (diff - 1) // dist
            prev = h
        return added
```

## C

```c
int addRungs(int* rungs, int rungsSize, int dist) {
    long long added = 0;
    long long prev = 0;
    long long d = dist;
    for (int i = 0; i < rungsSize; ++i) {
        long long cur = rungs[i];
        long long gap = cur - prev;
        if (gap > d) {
            added += (gap - 1) / d;
        }
        prev = cur;
    }
    return (int)added;
}
```

## Csharp

```csharp
public class Solution {
    public int AddRungs(int[] rungs, int dist) {
        long added = 0;
        int previous = 0;
        foreach (int rung in rungs) {
            int gap = rung - previous;
            if (gap > dist) {
                added += (gap - 1) / dist;
            }
            previous = rung;
        }
        return (int)added;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rungs
 * @param {number} dist
 * @return {number}
 */
var addRungs = function(rungs, dist) {
    let added = 0;
    let prev = 0;
    for (let h of rungs) {
        const diff = h - prev;
        if (diff > dist) {
            added += Math.floor((diff - 1) / dist);
        }
        prev = h;
    }
    return added;
};
```

## Typescript

```typescript
function addRungs(rungs: number[], dist: number): number {
    let added = 0;
    let prev = 0;
    for (const rung of rungs) {
        const gap = rung - prev;
        if (gap > dist) {
            added += Math.floor((gap - 1) / dist);
        }
        prev = rung;
    }
    return added;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rungs
     * @param Integer $dist
     * @return Integer
     */
    function addRungs($rungs, $dist) {
        $prev = 0;
        $added = 0;
        foreach ($rungs as $h) {
            $gap = $h - $prev;
            if ($gap > $dist) {
                $added += intdiv($gap - 1, $dist);
            }
            $prev = $h;
        }
        return $added;
    }
}
```

## Swift

```swift
class Solution {
    func addRungs(_ rungs: [Int], _ dist: Int) -> Int {
        var added = 0
        var prev = 0
        for rung in rungs {
            let diff = rung - prev
            if diff > dist {
                added += (diff - 1) / dist
            }
            prev = rung
        }
        return added
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addRungs(rungs: IntArray, dist: Int): Int {
        var prev = 0L
        val d = dist.toLong()
        var added = 0L
        for (r in rungs) {
            val cur = r.toLong()
            val gap = cur - prev
            if (gap > d) {
                added += (gap - 1) / d
            }
            prev = cur
        }
        return added.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int addRungs(List<int> rungs, int dist) {
    int added = 0;
    int prev = 0;
    for (int rung in rungs) {
      int gap = rung - prev;
      if (gap > dist) {
        added += (gap - 1) ~/ dist;
      }
      prev = rung;
    }
    return added;
  }
}
```

## Golang

```go
func addRungs(rungs []int, dist int) int {
    added := 0
    prev := 0
    for _, rung := range rungs {
        gap := rung - prev
        if gap > dist {
            added += (gap-1)/dist
        }
        prev = rung
    }
    return added
}
```

## Ruby

```ruby
def add_rungs(rungs, dist)
  added = 0
  prev = 0
  rungs.each do |h|
    gap = h - prev
    if gap > dist
      added += (gap - 1) / dist
    end
    prev = h
  end
  added
end
```

## Scala

```scala
object Solution {
    def addRungs(rungs: Array[Int], dist: Int): Int = {
        var prev = 0L
        var added = 0L
        val d = dist.toLong
        for (r <- rungs) {
            val gap = r.toLong - prev
            if (gap > d) {
                added += (gap - 1) / d
            }
            prev = r
        }
        added.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_rungs(rungs: Vec<i32>, dist: i32) -> i32 {
        let mut prev = 0i64;
        let d = dist as i64;
        let mut added = 0i64;
        for &r in rungs.iter() {
            let cur = r as i64;
            let diff = cur - prev;
            if diff > d {
                added += (diff - 1) / d;
            }
            prev = cur;
        }
        added as i32
    }
}
```

## Racket

```racket
(define/contract (add-rungs rungs dist)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((prev 0) (lst rungs) (added 0))
    (if (null? lst)
        added
        (let* ((curr (car lst))
               (gap (- curr prev))
               (extra (quotient (- gap 1) dist))) ; number of new rungs needed
          (loop curr (cdr lst) (+ added extra))))))
```

## Erlang

```erlang
-spec add_rungs(Rungs :: [integer()], Dist :: integer()) -> integer().
add_rungs(Rungs, Dist) ->
    add_rungs(Rungs, Dist, 0, 0).

add_rungs([], _Dist, _Prev, Acc) ->
    Acc;
add_rungs([H|T], Dist, Prev, Acc) ->
    Gap = H - Prev,
    Add = (Gap - 1) div Dist,
    add_rungs(T, Dist, H, Acc + Add).
```

## Elixir

```elixir
defmodule Solution do
  @spec add_rungs(rungs :: [integer], dist :: integer) :: integer
  def add_rungs(rungs, dist) do
    {count, _} =
      Enum.reduce(rings = rungs, {0, 0}, fn rung, {acc, prev} ->
        gap = rung - prev

        extra =
          if gap <= dist do
            0
          else
            div(gap + dist - 1, dist) - 1
          end

        {acc + extra, rung}
      end)

    count
  end
end
```
