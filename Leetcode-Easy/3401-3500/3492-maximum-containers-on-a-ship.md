# 3492. Maximum Containers on a Ship

## Cpp

```cpp
class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        long long totalCells = 1LL * n * n;
        long long possibleByWeight = maxWeight / w;
        long long ans = totalCells < possibleByWeight ? totalCells : possibleByWeight;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maxContainers(int n, int w, int maxWeight) {
        long totalCells = (long) n * n;
        long capacity = maxWeight / w;
        return (int) Math.min(totalCells, capacity);
    }
}
```

## Python

```python
class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        total_cells = n * n
        weight_limit = maxWeight // w
        return total_cells if total_cells < weight_limit else weight_limit
```

## Python3

```python
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_cells = n * n
        weight_limit = maxWeight // w
        return total_cells if total_cells < weight_limit else weight_limit
```

## C

```c
int maxContainers(int n, int w, int maxWeight) {
    long long cells = 1LL * n * n;
    long long byWeight = maxWeight / w;
    long long result = cells < byWeight ? cells : byWeight;
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxContainers(int n, int w, int maxWeight) {
        long totalCells = (long)n * n;
        long weightLimit = maxWeight / w;
        long result = Math.Min(totalCells, weightLimit);
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} w
 * @param {number} maxWeight
 * @return {number}
 */
var maxContainers = function(n, w, maxWeight) {
    const totalCells = n * n;
    const weightLimit = Math.floor(maxWeight / w);
    return totalCells < weightLimit ? totalCells : weightLimit;
};
```

## Typescript

```typescript
function maxContainers(n: number, w: number, maxWeight: number): number {
    const totalCells = n * n;
    const possibleByWeight = Math.floor(maxWeight / w);
    return Math.min(totalCells, possibleByWeight);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $w
     * @param Integer $maxWeight
     * @return Integer
     */
    function maxContainers($n, $w, $maxWeight) {
        $capacityBySpace = $n * $n;
        $capacityByWeight = intdiv($maxWeight, $w);
        return min($capacityBySpace, $capacityByWeight);
    }
}
```

## Swift

```swift
class Solution {
    func maxContainers(_ n: Int, _ w: Int, _ maxWeight: Int) -> Int {
        let totalCells = n * n
        let possibleByWeight = maxWeight / w
        return min(totalCells, possibleByWeight)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxContainers(n: Int, w: Int, maxWeight: Int): Int {
        val totalCells = n.toLong() * n
        val maxByWeight = maxWeight.toLong() / w
        return kotlin.math.min(totalCells, maxByWeight).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxContainers(int n, int w, int maxWeight) {
    int totalCells = n * n;
    int weightLimit = maxWeight ~/ w;
    return totalCells < weightLimit ? totalCells : weightLimit;
  }
}
```

## Golang

```go
func maxContainers(n int, w int, maxWeight int) int {
	totalCells := n * n
	capacity := maxWeight / w
	if totalCells < capacity {
		return totalCells
	}
	return capacity
}
```

## Ruby

```ruby
def max_containers(n, w, max_weight)
  [n * n, max_weight / w].min
end
```

## Scala

```scala
object Solution {
    def maxContainers(n: Int, w: Int, maxWeight: Int): Int = {
        val totalCells = n * n
        val capacity = maxWeight / w
        Math.min(totalCells, capacity)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_containers(n: i32, w: i32, max_weight: i32) -> i32 {
        let total_cells = (n as i64) * (n as i64);
        let capacity = (max_weight as i64) / (w as i64);
        std::cmp::min(total_cells, capacity) as i32
    }
}
```

## Racket

```racket
(define/contract (max-containers n w maxWeight)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([cells (* n n)]
         [cap   (quotient maxWeight w)])
    (min cells cap)))
```

## Erlang

```erlang
-spec max_containers(N :: integer(), W :: integer(), MaxWeight :: integer()) -> integer().
max_containers(N, W, MaxWeight) ->
    Cells = N * N,
    WeightLimit = MaxWeight div W,
    erlang:min(Cells, WeightLimit).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_containers(n :: integer, w :: integer, max_weight :: integer) :: integer
  def max_containers(n, w, max_weight) do
    total_cells = n * n
    capacity = div(max_weight, w)
    min(total_cells, capacity)
  end
end
```
