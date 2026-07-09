# 2240. Number of Ways to Buy Pens and Pencils

## Cpp

```cpp
class Solution {
public:
    long long waysToBuyPensPencils(int total, int cost1, int cost2) {
        long long ans = 0;
        for (int pens = 0; pens <= total / cost1; ++pens) {
            int remaining = total - pens * cost1;
            ans += (remaining / cost2) + 1;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long waysToBuyPensPencils(int total, int cost1, int cost2) {
        // Iterate over the number of pens (cost1). Use the more expensive item for fewer iterations.
        if (cost1 < cost2) {
            // swap to make cost1 >= cost2
            int tmp = cost1;
            cost1 = cost2;
            cost2 = tmp;
        }
        long ways = 0L;
        int maxPens = total / cost1;
        for (int pens = 0; pens <= maxPens; pens++) {
            int remaining = total - pens * cost1;
            int maxPencils = remaining / cost2;
            ways += (long) maxPencils + 1; // include zero pencils
        }
        return ways;
    }
}
```

## Python

```python
class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        # Iterate over the item with larger cost to minimize loop count
        if cost1 > cost2:
            # iterate over pens (cost1) as they are more expensive
            max_pen = total // cost1
            ans = 0
            for p in range(max_pen + 1):
                remaining = total - p * cost1
                ans += remaining // cost2 + 1
            return ans
        else:
            # iterate over pencils (cost2) as they are more expensive or equal
            max_pencil = total // cost2
            ans = 0
            for q in range(max_pencil + 1):
                remaining = total - q * cost2
                ans += remaining // cost1 + 1
            return ans
```

## Python3

```python
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # Iterate over the item with larger cost to minimize loop count
        if cost1 > cost2:
            # swap so that we iterate over pens (cost1) which is now the cheaper or equal
            cost1, cost2 = cost2, cost1
        ways = 0
        max_pen = total // cost1
        for pens in range(max_pen + 1):
            remaining = total - pens * cost1
            ways += remaining // cost2 + 1
        return ways
```

## C

```c
long long waysToBuyPensPencils(int total, int cost1, int cost2) {
    long long ans = 0;
    int maxPens = total / cost1;
    for (int pens = 0; pens <= maxPens; ++pens) {
        int remaining = total - pens * cost1;
        ans += (remaining / cost2) + 1;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long WaysToBuyPensPencils(int total, int cost1, int cost2) {
        long ways = 0;
        int maxPens = total / cost1;
        for (int pens = 0; pens <= maxPens; pens++) {
            int remaining = total - pens * cost1;
            int maxPencils = remaining / cost2;
            ways += (long)maxPencils + 1;
        }
        return ways;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} total
 * @param {number} cost1
 * @param {number} cost2
 * @return {number}
 */
var waysToBuyPensPencils = function(total, cost1, cost2) {
    let ans = 0;
    for (let pens = 0; pens * cost1 <= total; pens++) {
        const remaining = total - pens * cost1;
        const maxPencils = Math.floor(remaining / cost2);
        ans += maxPencils + 1;
    }
    return ans;
};
```

## Typescript

```typescript
function waysToBuyPensPencils(total: number, cost1: number, cost2: number): number {
    let ans = 0;
    // Iterate over the item with larger cost to minimize loop iterations
    if (cost1 > cost2) {
        for (let pens = 0; pens * cost1 <= total; pens++) {
            const remaining = total - pens * cost1;
            ans += Math.floor(remaining / cost2) + 1;
        }
    } else {
        for (let pencils = 0; pencils * cost2 <= total; pencils++) {
            const remaining = total - pencils * cost2;
            ans += Math.floor(remaining / cost1) + 1;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $total
     * @param Integer $cost1
     * @param Integer $cost2
     * @return Integer
     */
    function waysToBuyPensPencils($total, $cost1, $cost2) {
        $ans = 0;
        for ($pens = 0; $pens * $cost1 <= $total; $pens++) {
            $remaining = $total - $pens * $cost1;
            $maxPencils = intdiv($remaining, $cost2);
            $ans += $maxPencils + 1; // include zero pencils
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func waysToBuyPensPencils(_ total: Int, _ cost1: Int, _ cost2: Int) -> Int {
        var result = 0
        let maxPens = total / cost1
        for pens in 0...maxPens {
            let remaining = total - pens * cost1
            let maxPencils = remaining / cost2
            result += maxPencils + 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun waysToBuyPensPencils(total: Int, cost1: Int, cost2: Int): Long {
        var result = 0L
        val maxPens = total / cost1
        for (pens in 0..maxPens) {
            val spent = pens.toLong() * cost1
            val remaining = total.toLong() - spent
            val maxPencils = (remaining / cost2).toInt()
            result += (maxPencils + 1).toLong()
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int waysToBuyPensPencils(int total, int cost1, int cost2) {
    int ans = 0;
    for (int pens = 0; pens * cost1 <= total; pens++) {
      int remaining = total - pens * cost1;
      int maxPencils = remaining ~/ cost2;
      ans += maxPencils + 1;
    }
    return ans;
  }
}
```

## Golang

```go
func waysToBuyPensPencils(total int, cost1 int, cost2 int) int64 {
	var ways int64 = 0
	for pens := 0; pens*cost1 <= total; pens++ {
		remaining := total - pens*cost1
		maxPencils := remaining / cost2
		ways += int64(maxPencils + 1)
	}
	return ways
}
```

## Ruby

```ruby
def ways_to_buy_pens_pencils(total, cost1, cost2)
  # Iterate over the item with larger cost to minimize iterations
  if cost1 > cost2
    cost1, cost2 = cost2, cost1
  end

  count = 0
  max_first = total / cost1
  i = 0
  while i <= max_first
    remaining = total - i * cost1
    count += (remaining / cost2) + 1
    i += 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def waysToBuyPensPencils(total: Int, cost1: Int, cost2: Int): Long = {
        var ans: Long = 0L
        val maxPens = total / cost1
        var pens = 0
        while (pens <= maxPens) {
            val remaining = total.toLong - pens.toLong * cost1.toLong
            val pencilsMax = remaining / cost2.toLong
            ans += pencilsMax + 1L
            pens += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn ways_to_buy_pens_pencils(total: i32, cost1: i32, cost2: i32) -> i64 {
        let total = total as i64;
        let cost1 = cost1 as i64;
        let cost2 = cost2 as i64;
        let mut ans: i64 = 0;
        let mut pens = 0i64;
        while pens * cost1 <= total {
            let remaining = total - pens * cost1;
            ans += remaining / cost2 + 1;
            pens += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (ways-to-buy-pens-pencils total cost1 cost2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let loop ((i 0) (acc 0))
    (if (> (* i cost1) total)
        acc
        (let* ((remaining (- total (* i cost1)))
               (max-pencils (quotient remaining cost2))
               (new-acc (+ acc (add1 max-pencils))))
          (loop (add1 i) new-acc)))))
```

## Erlang

```erlang
-spec ways_to_buy_pens_pencils(Total :: integer(), Cost1 :: integer(), Cost2 :: integer()) -> integer().
ways_to_buy_pens_pencils(Total, Cost1, Cost2) ->
    MaxPens = Total div Cost1,
    loop(0, MaxPens, Total, Cost1, Cost2, 0).

loop(I, Max, Total, Cost1, Cost2, Acc) when I =< Max ->
    Remaining = Total - I * Cost1,
    Ymax = Remaining div Cost2,
    NewAcc = Acc + Ymax + 1,
    loop(I + 1, Max, Total, Cost1, Cost2, NewAcc);
loop(_, _, _, _, _, Acc) -> 
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec ways_to_buy_pens_pencils(total :: integer, cost1 :: integer, cost2 :: integer) :: integer
  def ways_to_buy_pens_pencils(total, cost1, cost2) do
    max_pen = div(total, cost1)

    Enum.reduce(0..max_pen, 0, fn pens, acc ->
      remaining = total - pens * cost1
      max_pencil = div(remaining, cost2)
      acc + max_pencil + 1
    end)
  end
end
```
