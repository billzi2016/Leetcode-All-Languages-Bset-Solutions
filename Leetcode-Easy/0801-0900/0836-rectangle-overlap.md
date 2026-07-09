# 0836. Rectangle Overlap

## Cpp

```cpp
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        // If one rectangle is on left side of the other
        if (rec1[2] <= rec2[0] || rec2[2] <= rec1[0]) return false;
        // If one rectangle is above the other
        if (rec1[3] <= rec2[1] || rec2[3] <= rec1[1]) return false;
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        // If one rectangle is to the left of the other
        if (rec1[2] <= rec2[0] || rec2[2] <= rec1[0]) {
            return false;
        }
        // If one rectangle is above the other
        if (rec1[3] <= rec2[1] || rec2[3] <= rec1[1]) {
            return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # No overlap if one rectangle is completely to the left/right/up/down of the other.
        return not (rec1[2] <= rec2[0] or   # rec1 is left of rec2
                    rec2[2] <= rec1[0] or   # rec2 is left of rec1
                    rec1[3] <= rec2[1] or   # rec1 is below rec2
                    rec2[3] <= rec1[1])     # rec2 is below rec1
```

## Python3

```python
from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or
                    rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
```

## C

```c
#include <stdbool.h>

bool isRectangleOverlap(int* rec1, int rec1Size, int* rec2, int rec2Size) {
    if (rec1[2] <= rec2[0] || rec2[2] <= rec1[0]) return false;
    if (rec1[3] <= rec2[1] || rec2[3] <= rec1[1]) return false;
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsRectangleOverlap(int[] rec1, int[] rec2) {
        // If one rectangle is to the left of the other
        if (rec1[2] <= rec2[0] || rec2[2] <= rec1[0])
            return false;
        // If one rectangle is above the other
        if (rec1[3] <= rec2[1] || rec2[3] <= rec1[1])
            return false;
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
    // If one rectangle is to the left/right/up/down of the other, they do not overlap.
    return !(rec1[2] <= rec2[0] ||   // rec1 is left of rec2
             rec2[2] <= rec1[0] ||   // rec2 is left of rec1
             rec1[3] <= rec2[1] ||   // rec1 is below rec2
             rec2[3] <= rec1[1]);    // rec2 is below rec1
};
```

## Typescript

```typescript
function isRectangleOverlap(rec1: number[], rec2: number[]): boolean {
    // If one rectangle is on left side of the other
    if (rec1[2] <= rec2[0] || rec2[2] <= rec1[0]) return false;
    // If one rectangle is above the other
    if (rec1[3] <= rec2[1] || rec2[3] <= rec1[1]) return false;
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rec1
     * @param Integer[] $rec2
     * @return Boolean
     */
    function isRectangleOverlap($rec1, $rec2) {
        if ($rec1[2] <= $rec2[0] || $rec2[2] <= $rec1[0] || $rec1[3] <= $rec2[1] || $rec2[3] <= $rec1[1]) {
            return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isRectangleOverlap(_ rec1: [Int], _ rec2: [Int]) -> Bool {
        // If one rectangle is to the left, right, above, or below the other, they do not overlap.
        if rec1[2] <= rec2[0] || rec2[2] <= rec1[0] ||
           rec1[3] <= rec2[1] || rec2[3] <= rec1[1] {
            return false
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isRectangleOverlap(rec1: IntArray, rec2: IntArray): Boolean {
        // If one rectangle is to the left of the other
        if (rec1[2] <= rec2[0] || rec2[2] <= rec1[0]) return false
        // If one rectangle is above the other
        if (rec1[3] <= rec2[1] || rec2[3] <= rec1[1]) return false
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isRectangleOverlap(List<int> rec1, List<int> rec2) {
    // If one rectangle is to the left of the other
    if (rec1[2] <= rec2[0] || rec2[2] <= rec1[0]) return false;
    // If one rectangle is above the other
    if (rec1[3] <= rec2[1] || rec2[3] <= rec1[1]) return false;
    return true;
  }
}
```

## Golang

```go
func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	if rec1[2] <= rec2[0] || rec2[2] <= rec1[0] || rec1[3] <= rec2[1] || rec2[3] <= rec1[1] {
		return false
	}
	return true
}
```

## Ruby

```ruby
def is_rectangle_overlap(rec1, rec2)
  !(rec1[2] <= rec2[0] || rec2[2] <= rec1[0] || rec1[3] <= rec2[1] || rec2[3] <= rec1[1])
end
```

## Scala

```scala
object Solution {
    def isRectangleOverlap(rec1: Array[Int], rec2: Array[Int]): Boolean = {
        !(rec1(2) <= rec2(0) || rec2(2) <= rec1(0) ||
          rec1(3) <= rec2(1) || rec2(3) <= rec1(1))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_rectangle_overlap(rec1: Vec<i32>, rec2: Vec<i32>) -> bool {
        !(rec1[2] <= rec2[0] || rec2[2] <= rec1[0] || rec1[3] <= rec2[1] || rec2[3] <= rec1[1])
    }
}
```

## Racket

```racket
(define/contract (is-rectangle-overlap rec1 rec2)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  (let* ([x1 (list-ref rec1 0)]
         [y1 (list-ref rec1 1)]
         [x2 (list-ref rec1 2)]
         [y2 (list-ref rec1 3)]
         [X1 (list-ref rec2 0)]
         [Y1 (list-ref rec2 1)]
         [X2 (list-ref rec2 2)]
         [Y2 (list-ref rec2 3)])
    (not (or (<= x2 X1)          ; rec1 is left of rec2
             (<= X2 x1)          ; rec2 is left of rec1
             (<= y2 Y1)          ; rec1 is below rec2
             (<= Y2 y1)))))      ; rec2 is below rec1
```

## Erlang

```erlang
-module(solution).
-export([is_rectangle_overlap/2]).

-spec is_rectangle_overlap(Rec1 :: [integer()], Rec2 :: [integer()]) -> boolean().
is_rectangle_overlap([X1, Y1, X2, Y2], [A1, B1, A2, B2]) ->
    not (X2 =< A1 orelse A2 =< X1 orelse Y2 =< B1 orelse B2 =< Y1).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_rectangle_overlap(rec1 :: [integer], rec2 :: [integer]) :: boolean
  def is_rectangle_overlap([x1a, y1a, x2a, y2a], [x1b, y1b, x2b, y2b]) do
    not (x2a <= x1b or x2b <= x1a or y2a <= y1b or y2b <= y1a)
  end
end
```
