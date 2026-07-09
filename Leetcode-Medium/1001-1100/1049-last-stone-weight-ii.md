# 1049. Last Stone Weight II

## Cpp

```cpp
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int total = accumulate(stones.begin(), stones.end(), 0);
        vector<char> dp(total + 1, 0);
        dp[0] = 1;
        for (int w : stones) {
            for (int s = total; s >= w; --s) {
                if (dp[s - w]) dp[s] = 1;
            }
        }
        int half = total / 2;
        for (int s = half; s >= 0; --s) {
            if (dp[s]) return total - 2 * s;
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int lastStoneWeightII(int[] stones) {
        int total = 0;
        for (int w : stones) total += w;
        boolean[] dp = new boolean[total + 1];
        dp[0] = true;
        for (int w : stones) {
            for (int j = total; j >= w; --j) {
                dp[j] |= dp[j - w];
            }
        }
        int half = total / 2;
        for (int i = half; i >= 0; --i) {
            if (dp[i]) return total - 2 * i;
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        reachable = {0}
        for w in stones:
            new_reachable = set()
            for s in reachable:
                new_reachable.add(s + w)
            reachable.update(new_reachable)
        half = total // 2
        best = max(s for s in reachable if s <= half)
        return total - 2 * best
```

## Python3

```python
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for w in stones:
            for s in range(target, w - 1, -1):
                if dp[s - w]:
                    dp[s] = True
        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s
        return 0
```

## C

```c
#include <stdlib.h>

int lastStoneWeightII(int* stones, int stonesSize) {
    int total = 0;
    for (int i = 0; i < stonesSize; ++i) {
        total += stones[i];
    }
    char *dp = (char *)calloc(total + 1, sizeof(char));
    dp[0] = 1;
    for (int i = 0; i < stonesSize; ++i) {
        int w = stones[i];
        for (int j = total; j >= w; --j) {
            if (dp[j - w]) dp[j] = 1;
        }
    }
    int half = total / 2;
    for (int j = half; j >= 0; --j) {
        if (dp[j]) {
            int result = total - 2 * j;
            free(dp);
            return result;
        }
    }
    free(dp);
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int LastStoneWeightII(int[] stones) {
        int total = 0;
        foreach (int w in stones) total += w;
        int target = total / 2;
        bool[] dp = new bool[target + 1];
        dp[0] = true;
        foreach (int w in stones) {
            for (int s = target; s >= w; s--) {
                if (dp[s - w]) dp[s] = true;
            }
        }
        int best = 0;
        for (int s = target; s >= 0; s--) {
            if (dp[s]) { best = s; break; }
        }
        return total - 2 * best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeightII = function(stones) {
    const total = stones.reduce((a, b) => a + b, 0);
    const target = Math.floor(total / 2);
    const dp = new Uint8Array(target + 1);
    dp[0] = 1;
    for (const w of stones) {
        for (let s = target; s >= w; --s) {
            if (dp[s - w]) dp[s] = 1;
        }
    }
    let best = 0;
    for (let s = target; s >= 0; --s) {
        if (dp[s]) { best = s; break; }
    }
    return total - 2 * best;
};
```

## Typescript

```typescript
function lastStoneWeightII(stones: number[]): number {
    const total = stones.reduce((sum, w) => sum + w, 0);
    const target = Math.floor(total / 2);
    const dp = new Uint8Array(target + 1);
    dp[0] = 1;
    for (const w of stones) {
        for (let j = target; j >= w; --j) {
            if (dp[j - w]) dp[j] = 1;
        }
    }
    let best = 0;
    for (let s = target; s >= 0; --s) {
        if (dp[s]) {
            best = s;
            break;
        }
    }
    return total - 2 * best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function lastStoneWeightII($stones) {
        $total = array_sum($stones);
        $dp = array_fill(0, $total + 1, false);
        $dp[0] = true;
        foreach ($stones as $w) {
            for ($i = $total; $i >= $w; $i--) {
                if ($dp[$i - $w]) {
                    $dp[$i] = true;
                }
            }
        }
        for ($i = intdiv($total, 2); $i >= 0; $i--) {
            if ($dp[$i]) {
                return $total - 2 * $i;
            }
        }
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func lastStoneWeightII(_ stones: [Int]) -> Int {
        let total = stones.reduce(0, +)
        var dp = Array(repeating: false, count: total + 1)
        dp[0] = true
        for w in stones {
            var i = total
            while i >= w {
                if dp[i - w] {
                    dp[i] = true
                }
                i -= 1
            }
        }
        var result = Int.max
        for s in 0...total where dp[s] {
            let diff = abs(total - 2 * s)
            if diff < result { result = diff }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lastStoneWeightII(stones: IntArray): Int {
        val total = stones.sum()
        val target = total / 2
        val dp = BooleanArray(target + 1)
        dp[0] = true
        for (stone in stones) {
            for (j in target downTo stone) {
                if (dp[j - stone]) dp[j] = true
            }
        }
        var best = 0
        for (i in target downTo 0) {
            if (dp[i]) {
                best = i
                break
            }
        }
        return total - 2 * best
    }
}
```

## Dart

```dart
class Solution {
  int lastStoneWeightII(List<int> stones) {
    int total = stones.fold(0, (sum, v) => sum + v);
    int target = total ~/ 2;
    List<bool> dp = List.filled(target + 1, false);
    dp[0] = true;
    for (int w in stones) {
      for (int s = target; s >= w; s--) {
        if (dp[s - w]) dp[s] = true;
      }
    }
    int best = 0;
    for (int s = target; s >= 0; s--) {
      if (dp[s]) {
        best = s;
        break;
      }
    }
    return total - 2 * best;
  }
}
```

## Golang

```go
func lastStoneWeightII(stones []int) int {
    total := 0
    for _, w := range stones {
        total += w
    }
    target := total / 2
    dp := make([]bool, target+1)
    dp[0] = true
    for _, w := range stones {
        for j := target; j >= w; j-- {
            if dp[j-w] {
                dp[j] = true
            }
        }
    }
    best := 0
    for i := target; i >= 0; i-- {
        if dp[i] {
            best = i
            break
        }
    }
    return total - 2*best
}
```

## Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight_ii(stones)
  total = stones.sum
  target = total / 2
  dp = Array.new(target + 1, false)
  dp[0] = true

  stones.each do |w|
    (target).downto(w) do |j|
      dp[j] ||= dp[j - w]
    end
  end

  i = target.downto(0).find { |idx| dp[idx] }
  total - 2 * i
end
```

## Scala

```scala
object Solution {
    def lastStoneWeightII(stones: Array[Int]): Int = {
        val total = stones.sum
        val target = total / 2
        val dp = new Array[Boolean](target + 1)
        dp(0) = true
        for (stone <- stones) {
            var s = target
            while (s >= stone) {
                if (dp(s - stone)) dp(s) = true
                s -= 1
            }
        }
        var i = target
        while (i >= 0 && !dp(i)) i -= 1
        total - 2 * i
    }
}
```

## Rust

```rust
impl Solution {
    pub fn last_stone_weight_ii(stones: Vec<i32>) -> i32 {
        let total: usize = stones.iter().map(|&x| x as usize).sum();
        let mut dp = vec![false; total + 1];
        dp[0] = true;
        for &stone in stones.iter() {
            let w = stone as usize;
            for j in (w..=total).rev() {
                if dp[j - w] {
                    dp[j] = true;
                }
            }
        }
        let half = total / 2;
        for j in (0..=half).rev() {
            if dp[j] {
                return (total - 2 * j) as i32;
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (last-stone-weight-ii stones)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((total (apply + stones))
         (target (quotient total 2))
         (dp (make-vector (+ target 1) #f)))
    (vector-set! dp 0 #t)
    (for ([w stones])
      (when (<= w target)
        (for ([j (in-range target (- w 1) -1)])
          (when (vector-ref dp (- j w))
            (vector-set! dp j #t)))))
    (let loop ((j target))
      (if (vector-ref dp j)
          (- total (* 2 j))
          (loop (- j 1))))))
```

## Erlang

```erlang
-module(solution).
-export([last_stone_weight_ii/1]).

-spec last_stone_weight_ii(Stones :: [integer()]) -> integer().
last_stone_weight_ii(Stones) ->
    Total = lists:sum(Stones),
    Mask = build_bitmask(Stones, 1),
    Half = Total div 2,
    S = find_best(Mask, Half),
    Total - 2 * S.

build_bitmask([], Mask) -> Mask;
build_bitmask([W|Rest], Mask) ->
    NewMask = (Mask bsl W) bor Mask,
    build_bitmask(Rest, NewMask).

find_best(_Mask, -1) -> 0;
find_best(Mask, S) ->
    case (Mask band (1 bsl S)) of
        0 -> find_best(Mask, S-1);
        _ -> S
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec last_stone_weight_ii(stones :: [integer]) :: integer
  def last_stone_weight_ii(stones) do
    total = Enum.sum(stones)
    target = div(total, 2)

    reachable =
      Enum.reduce(stones, MapSet.new([0]), fn w, acc ->
        added = Enum.map(acc, &(&1 + w)) |> MapSet.new()
        MapSet.union(acc, added)
      end)

    best =
      reachable
      |> Enum.filter(&(&1 <= target))
      |> Enum.max(fn -> 0 end)

    total - 2 * best
  end
end
```
