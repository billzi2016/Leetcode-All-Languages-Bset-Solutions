# 1791. Find Center of Star Graph

## Cpp

```cpp
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int a = edges[0][0], b = edges[0][1];
        int c = edges[1][0], d = edges[1][1];
        if (a == c || a == d) return a;
        return b;
    }
};
```

## Java

```java
class Solution {
    public int findCenter(int[][] edges) {
        int a = edges[0][0];
        int b = edges[0][1];
        int c = edges[1][0];
        int d = edges[1][1];
        return (a == c || a == d) ? a : b;
    }
}
```

## Python

```python
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        a, b = edges[0]
        c, d = edges[1]
        return a if a == c or a == d else b
```

## Python3

```python
from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        if u1 == u2 or u1 == v2:
            return u1
        return v1
```

## C

```c
int findCenter(int** edges, int edgesSize, int* edgesColSize){
    int a = edges[0][0];
    int b = edges[0][1];
    int c = edges[1][0];
    int d = edges[1][1];
    
    if (a == c || a == d) return a;
    return b;
}
```

## Csharp

```csharp
public class Solution {
    public int FindCenter(int[][] edges) {
        int a = edges[0][0];
        int b = edges[0][1];
        int c = edges[1][0];
        int d = edges[1][1];
        if (a == c || a == d) return a;
        return b;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function(edges) {
    const [a, b] = edges[0];
    const [c, d] = edges[1];
    return (a === c || a === d) ? a : b;
};
```

## Typescript

```typescript
function findCenter(edges: number[][]): number {
    const [a, b] = edges[0];
    const [c, d] = edges[1];
    return a === c || a === d ? a : b;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function findCenter($edges) {
        $a = $edges[0][0];
        $b = $edges[0][1];
        $c = $edges[1][0];
        $d = $edges[1][1];

        if ($a == $c || $a == $d) {
            return $a;
        }
        return $b;
    }
}
```

## Swift

```swift
class Solution {
    func findCenter(_ edges: [[Int]]) -> Int {
        let first = edges[0]
        let second = edges[1]
        if first[0] == second[0] || first[0] == second[1] {
            return first[0]
        } else {
            return first[1]
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findCenter(edges: Array<IntArray>): Int {
        val first = edges[0]
        val second = edges[1]
        return if (first[0] == second[0] || first[0] == second[1]) first[0] else first[1]
    }
}
```

## Dart

```dart
class Solution {
  int findCenter(List<List<int>> edges) {
    int a = edges[0][0];
    int b = edges[0][1];
    int c = edges[1][0];
    int d = edges[1][1];
    if (a == c || a == d) return a;
    return b;
  }
}
```

## Golang

```go
func findCenter(edges [][]int) int {
    a, b := edges[0][0], edges[0][1]
    c, d := edges[1][0], edges[1][1]
    if a == c || a == d {
        return a
    }
    return b
}
```

## Ruby

```ruby
def find_center(edges)
  u1, v1 = edges[0]
  u2, v2 = edges[1]
  if u1 == u2 || u1 == v2
    u1
  else
    v1
  end
end
```

## Scala

```scala
object Solution {
    def findCenter(edges: Array[Array[Int]]): Int = {
        val first = edges(0)
        val second = edges(1)
        if (first(0) == second(0) || first(0) == second(1)) first(0)
        else first(1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_center(edges: Vec<Vec<i32>>) -> i32 {
        let e1 = &edges[0];
        let e2 = &edges[1];
        if e1[0] == e2[0] || e1[0] == e2[1] {
            e1[0]
        } else {
            e1[1]
        }
    }
}
```

## Racket

```racket
(define/contract (find-center edges)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((first-edge (car edges))
         (second-edge (cadr edges))
         (a (list-ref first-edge 0))
         (b (list-ref first-edge 1))
         (c (list-ref second-edge 0))
         (d (list-ref second-edge 1)))
    (cond [(or (= a c) (= a d)) a]
          [else b])))
```

## Erlang

```erlang
-spec find_center(Edges :: [[integer()]]) -> integer().
find_center([[U1, V1], [U2, V2] | _]) ->
    case (U1 =:= U2) orelse (U1 =:= V2) of
        true -> U1;
        false -> V1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_center(edges :: [[integer]]) :: integer
  def find_center([[u1, v1], [u2, v2] | _]) do
    if u1 == u2 or u1 == v2 do
      u1
    else
      v1
    end
  end
end
```
