# 1893. Check if All the Integers in a Range Are Covered

## Cpp

```cpp
class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        const int MAXV = 51;
        vector<bool> covered(MAXV, false);
        for (const auto& r : ranges) {
            for (int x = r[0]; x <= r[1]; ++x) {
                covered[x] = true;
            }
        }
        for (int x = left; x <= right; ++x) {
            if (!covered[x]) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        boolean[] covered = new boolean[51]; // indices 0..50
        for (int[] r : ranges) {
            int start = r[0];
            int end = r[1];
            for (int i = start; i <= end; i++) {
                covered[i] = true;
            }
        }
        for (int i = left; i <= right; i++) {
            if (!covered[i]) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        covered = [False] * 51  # indices 0..50, we use 1..50
        for start, end in ranges:
            for x in range(start, end + 1):
                covered[x] = True
        for x in range(left, right + 1):
            if not covered[x]:
                return False
        return True
```

## Python3

```python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * 51
        for start, end in ranges:
            for x in range(start, end + 1):
                covered[x] = True
        for x in range(left, right + 1):
            if not covered[x]:
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool isCovered(int** ranges, int rangesSize, int* rangesColSize, int left, int right) {
    bool covered[51] = {false};
    
    for (int i = 0; i < rangesSize; ++i) {
        int start = ranges[i][0];
        int end   = ranges[i][1];
        for (int x = start; x <= end; ++x) {
            covered[x] = true;
        }
    }
    
    for (int x = left; x <= right; ++x) {
        if (!covered[x]) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsCovered(int[][] ranges, int left, int right) {
        bool[] covered = new bool[51];
        foreach (var range in ranges) {
            for (int i = range[0]; i <= range[1]; i++) {
                covered[i] = true;
            }
        }
        for (int i = left; i <= right; i++) {
            if (!covered[i]) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} ranges
 * @param {number} left
 * @param {number} right
 * @return {boolean}
 */
var isCovered = function(ranges, left, right) {
    const covered = new Array(51).fill(false);
    for (const [start, end] of ranges) {
        for (let i = start; i <= end; i++) {
            covered[i] = true;
        }
    }
    for (let x = left; x <= right; x++) {
        if (!covered[x]) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isCovered(ranges: number[][], left: number, right: number): boolean {
    const covered = new Array(51).fill(false);
    for (const [start, end] of ranges) {
        for (let i = start; i <= end; i++) {
            covered[i] = true;
        }
    }
    for (let i = left; i <= right; i++) {
        if (!covered[i]) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $ranges
     * @param Integer $left
     * @param Integer $right
     * @return Boolean
     */
    function isCovered($ranges, $left, $right) {
        // Since constraints are small (max value 50), use a simple boolean array.
        $covered = array_fill(0, 52, false); // indices 1..51 safe

        foreach ($ranges as $range) {
            $start = $range[0];
            $end   = $range[1];
            for ($i = $start; $i <= $end; $i++) {
                $covered[$i] = true;
            }
        }

        for ($i = $left; $i <= $right; $i++) {
            if (!$covered[$i]) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isCovered(_ ranges: [[Int]], _ left: Int, _ right: Int) -> Bool {
        var covered = [Bool](repeating: false, count: 51)
        for range in ranges {
            let start = range[0]
            let end = range[1]
            if start > 50 { continue }
            for i in start...end {
                covered[i] = true
            }
        }
        for x in left...right {
            if !covered[x] {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isCovered(ranges: Array<IntArray>, left: Int, right: Int): Boolean {
        val covered = BooleanArray(51)
        for (range in ranges) {
            val start = range[0]
            val end = range[1]
            for (i in start..end) {
                covered[i] = true
            }
        }
        for (i in left..right) {
            if (!covered[i]) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isCovered(List<List<int>> ranges, int left, int right) {
    const int maxVal = 51;
    List<bool> covered = List.filled(maxVal, false);
    for (var range in ranges) {
      int start = range[0];
      int end = range[1];
      for (int i = start; i <= end; ++i) {
        covered[i] = true;
      }
    }
    for (int x = left; x <= right; ++x) {
      if (!covered[x]) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isCovered(ranges [][]int, left int, right int) bool {
	covered := make([]bool, 52)
	for _, r := range ranges {
		start, end := r[0], r[1]
		for i := start; i <= end; i++ {
			covered[i] = true
		}
	}
	for i := left; i <= right; i++ {
		if !covered[i] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_covered(ranges, left, right)
  covered = Array.new(51, false)
  ranges.each do |start_i, end_i|
    (start_i..end_i).each { |x| covered[x] = true }
  end
  (left..right).all? { |x| covered[x] }
end
```

## Scala

```scala
object Solution {
    def isCovered(ranges: Array[Array[Int]], left: Int, right: Int): Boolean = {
        val covered = new Array[Boolean](51)
        for (range <- ranges) {
            var i = range(0)
            while (i <= range(1)) {
                covered(i) = true
                i += 1
            }
        }
        var x = left
        while (x <= right) {
            if (!covered(x)) return false
            x += 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_covered(ranges: Vec<Vec<i32>>, left: i32, right: i32) -> bool {
        let mut covered = vec![false; 51];
        for r in ranges.iter() {
            let start = r[0] as usize;
            let end = r[1] as usize;
            for x in start..=end {
                covered[x] = true;
            }
        }
        for x in left as usize..=right as usize {
            if !covered[x] {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-covered ranges left right)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  (let ([covered (make-vector 51 #f)])
    (for-each
     (lambda (rng)
       (define start (first rng))
       (define end (second rng))
       (for ([i (in-range start (+ end 1))])
         (vector-set! covered i #t)))
     ranges)
    (for/and ([x (in-range left (+ right 1))])
      (vector-ref covered x))))
```

## Erlang

```erlang
-spec is_covered(Ranges :: [[integer()]], Left :: integer(), Right :: integer()) -> boolean().
is_covered(Ranges, Left, Right) ->
    lists:all(fun(X) -> covered_by_any(Ranges, X) end,
              lists:seq(Left, Right)).

covered_by_any(Ranges, X) ->
    lists:any(fun([S, E]) -> S =< X andalso X =< E end, Ranges).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_covered(ranges :: [[integer]], left :: integer, right :: integer) :: boolean
  def is_covered(ranges, left, right) do
    Enum.all?(left..right, fn x ->
      Enum.any?(ranges, fn [s, e] -> s <= x and x <= e end)
    end)
  end
end
```
