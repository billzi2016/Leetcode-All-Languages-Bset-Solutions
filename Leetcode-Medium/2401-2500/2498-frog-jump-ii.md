# 2498. Frog Jump II

## Cpp

```cpp
class Solution {
public:
    int maxJump(vector<int>& stones) {
        int n = stones.size();
        if (n == 2) return stones[1] - stones[0];
        long long ans = 0;
        for (int i = 0; i + 2 < n; ++i) {
            ans = max(ans, static_cast<long long>(stones[i + 2]) - stones[i]);
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maxJump(int[] stones) {
        int n = stones.length;
        if (n == 2) {
            return stones[1] - stones[0];
        }
        int ans = Math.max(stones[1] - stones[0], stones[n - 1] - stones[n - 2]);
        for (int i = 0; i + 2 < n; i++) {
            ans = Math.max(ans, stones[i + 2] - stones[i]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        if n <= 2:
            return stones[-1] - stones[0]
        ans = 0
        for i in range(n - 2):
            jump = stones[i + 2] - stones[i]
            if jump > ans:
                ans = jump
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 2:
            return stones[1] - stones[0]
        ans = 0
        for i in range(n - 2):
            jump = stones[i + 2] - stones[i]
            if jump > ans:
                ans = jump
        return ans
```

## C

```c
int maxJump(int* stones, int stonesSize) {
    if (stonesSize <= 2) {
        return stones[stonesSize - 1] - stones[0];
    }
    int ans = 0;
    for (int i = 0; i + 2 < stonesSize; ++i) {
        int diff = stones[i + 2] - stones[i];
        if (diff > ans) ans = diff;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxJump(int[] stones)
    {
        int n = stones.Length;
        if (n == 2)
            return stones[1] - stones[0];

        int maxJump = 0;
        for (int i = 2; i < n; i++)
        {
            int jump = stones[i] - stones[i - 2];
            if (jump > maxJump) maxJump = jump;
        }
        return maxJump;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var maxJump = function(stones) {
    const n = stones.length;
    if (n <= 2) return stones[n - 1] - stones[0];
    let ans = 0;
    for (let i = 2; i < n; ++i) {
        const diff = stones[i] - stones[i - 2];
        if (diff > ans) ans = diff;
    }
    return ans;
};
```

## Typescript

```typescript
function maxJump(stones: number[]): number {
    const n = stones.length;
    if (n === 2) return stones[1] - stones[0];
    let ans = 0;
    for (let i = 2; i < n; ++i) {
        const diff = stones[i] - stones[i - 2];
        if (diff > ans) ans = diff;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function maxJump($stones) {
        $n = count($stones);
        if ($n <= 2) {
            return $stones[1] - $stones[0];
        }
        $ans = 0;
        for ($i = 0; $i + 2 < $n; $i++) {
            $jump = $stones[$i + 2] - $stones[$i];
            if ($jump > $ans) {
                $ans = $jump;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxJump(_ stones: [Int]) -> Int {
        let n = stones.count
        if n == 2 { return stones[1] - stones[0] }
        var answer = 0
        for i in 0..<(n - 2) {
            let diff = stones[i + 2] - stones[i]
            if diff > answer {
                answer = diff
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxJump(stones: IntArray): Int {
        val n = stones.size
        if (n <= 2) return stones[n - 1] - stones[0]
        var answer = 0
        for (i in 0 until n - 2) {
            val diff = stones[i + 2] - stones[i]
            if (diff > answer) answer = diff
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxJump(List<int> stones) {
    int n = stones.length;
    if (n == 2) return stones[1] - stones[0];
    int ans = 0;
    for (int i = 0; i + 2 < n; ++i) {
      int diff = stones[i + 2] - stones[i];
      if (diff > ans) ans = diff;
    }
    return ans;
  }
}
```

## Golang

```go
func maxJump(stones []int) int {
    n := len(stones)
    if n == 2 {
        return stones[1] - stones[0]
    }
    ans := 0
    for i := 0; i+2 < n; i++ {
        d := stones[i+2] - stones[i]
        if d > ans {
            ans = d
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_jump(stones)
  n = stones.length
  return stones[-1] - stones[0] if n <= 2

  max_gap = 0
  (2...n).each do |i|
    gap = stones[i] - stones[i - 2]
    max_gap = gap if gap > max_gap
  end
  max_gap
end
```

## Scala

```scala
object Solution {
    def maxJump(stones: Array[Int]): Int = {
        val n = stones.length
        if (n == 2) return stones(1) - stones(0)
        var ans = 0
        for (i <- 0 until n - 2) {
            val diff = stones(i + 2) - stones(i)
            if (diff > ans) ans = diff
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_jump(stones: Vec<i32>) -> i32 {
        let n = stones.len();
        if n == 2 {
            return stones[1] - stones[0];
        }
        let mut ans = 0;
        for i in 0..n - 2 {
            let diff = stones[i + 2] - stones[i];
            if diff > ans {
                ans = diff;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-jump stones)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector stones))
         (n   (vector-length vec)))
    (if (= n 2)
        (- (vector-ref vec 1) (vector-ref vec 0))
        (let loop ((i 0) (mx 0))
          (if (> i (- n 3))
              mx
              (let ((diff (- (vector-ref vec (+ i 2))
                             (vector-ref vec i))))
                (loop (+ i 1) (if (> diff mx) diff mx))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_jump/1]).

-spec max_jump(Stones :: [integer()]) -> integer().
max_jump(Stones) ->
    case Stones of
        [_] -> 0;
        [_ , _] = L -> hd(tl(L)) - hd(L);
        _ -> max_gap(Stones, 0)
    end.

max_gap([A,B,C|Rest], CurMax) ->
    Diff = C - A,
    NewMax = case Diff > CurMax of
                true -> Diff;
                false -> CurMax
             end,
    max_gap([B,C|Rest], NewMax);
max_gap(_, Max) -> Max.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_jump(stones :: [integer]) :: integer
  def max_jump(stones) do
    n = length(stones)

    if n == 2 do
      List.last(stones) - hd(stones)
    else
      [first, second | rest] = stones

      {max_diff, _, _} =
        Enum.reduce(rest, {0, first, second}, fn cur, {mx, prev2, prev1} ->
          diff = cur - prev2
          new_mx = if diff > mx, do: diff, else: mx
          {new_mx, prev1, cur}
        end)

      max_diff
    end
  end
end
```
