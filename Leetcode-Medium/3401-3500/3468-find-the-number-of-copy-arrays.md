# 3468. Find the Number of Copy Arrays

## Cpp

```cpp
class Solution {
public:
    int countArrays(vector<int>& original, vector<vector<int>>& bounds) {
        int n = original.size();
        long long base = original[0];
        long long low = LLONG_MIN / 4;
        long long high = LLONG_MAX / 4;
        for (int i = 0; i < n; ++i) {
            long long delta = (long long)original[i] - base;
            long long curLow = (long long)bounds[i][0] - delta;
            long long curHigh = (long long)bounds[i][1] - delta;
            low = max(low, curLow);
            high = min(high, curHigh);
        }
        if (low > high) return 0;
        long long ans = high - low + 1;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countArrays(int[] original, int[][] bounds) {
        long low = Long.MIN_VALUE;
        long high = Long.MAX_VALUE;
        for (int i = 0; i < original.length; i++) {
            long l = (long)bounds[i][0] - original[i];
            long r = (long)bounds[i][1] - original[i];
            if (l > low) low = l;
            if (r < high) high = r;
        }
        long ans = high >= low ? (high - low + 1) : 0;
        return (int)ans;
    }
}
```

## Python

```python
class Solution(object):
    def countArrays(self, original, bounds):
        """
        :type original: List[int]
        :type bounds: List[List[int]]
        :rtype: int
        """
        n = len(original)
        base = original[0]
        low = -10**20  # sufficiently small
        high = 10**20   # sufficiently large
        for i in range(n):
            delta = original[i] - base
            lo = bounds[i][0] - delta
            hi = bounds[i][1] - delta
            if lo > low:
                low = lo
            if hi < high:
                high = hi
            if low > high:  # early exit
                return 0
        return max(0, high - low + 1)
```

## Python3

```python
from typing import List

class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        low = -10**20  # sufficiently small
        high = 10**20   # sufficiently large
        for o, (u, v) in zip(original, bounds):
            low = max(low, u - o)
            high = min(high, v - o)
        if low > high:
            return 0
        return high - low + 1
```

## C

```c
int countArrays(int* original, int originalSize, int** bounds, int boundsSize, int* boundsColSize) {
    long long low = LLONG_MIN;
    long long high = LLONG_MAX;
    for (int i = 0; i < originalSize; ++i) {
        long long l = (long long)bounds[i][0] - original[i];
        long long r = (long long)bounds[i][1] - original[i];
        if (l > low) low = l;
        if (r < high) high = r;
    }
    long long ans = (high >= low) ? (high - low + 1) : 0;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountArrays(int[] original, int[][] bounds) {
        int n = original.Length;
        long low = long.MinValue / 2;
        long high = long.MaxValue / 2;
        long delta = 0; // copy[i] = copy[0] + delta

        for (int i = 0; i < n; i++) {
            long u = bounds[i][0];
            long v = bounds[i][1];

            long curLow = u - delta;
            long curHigh = v - delta;

            if (curLow > low) low = curLow;
            if (curHigh < high) high = curHigh;

            if (i + 1 < n) {
                delta += original[i + 1] - original[i];
            }
        }

        if (high < low) return 0;
        long ans = high - low + 1;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} original
 * @param {number[][]} bounds
 * @return {number}
 */
var countArrays = function(original, bounds) {
    let low = -Infinity;
    let high = Infinity;
    const n = original.length;
    for (let i = 0; i < n; ++i) {
        const u = bounds[i][0];
        const v = bounds[i][1];
        const diffLow = u - original[i];
        const diffHigh = v - original[i];
        if (diffLow > low) low = diffLow;
        if (diffHigh < high) high = diffHigh;
    }
    if (low > high) return 0;
    // both low and high are integers because inputs are integers
    return Math.floor(high) - Math.ceil(low) + 1;
};
```

## Typescript

```typescript
function countArrays(original: number[], bounds: number[][]): number {
    const n = original.length;
    const base = original[0];
    let left = -Infinity;
    let right = Infinity;
    for (let i = 0; i < n; i++) {
        const delta = original[i] - base;
        const low = bounds[i][0] - delta;
        const high = bounds[i][1] - delta;
        if (low > left) left = low;
        if (high < right) right = high;
    }
    if (left > right) return 0;
    // Since all inputs are integers, the count is integer.
    return Math.floor(right) - Math.ceil(left) + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $original
     * @param Integer[][] $bounds
     * @return Integer
     */
    function countArrays($original, $bounds) {
        $n = count($original);
        $base = $original[0];
        $L = -PHP_INT_MAX;
        $R = PHP_INT_MAX;

        for ($i = 0; $i < $n; ++$i) {
            $delta = $original[$i] - $base;
            $left = $bounds[$i][0] - $delta;
            $right = $bounds[$i][1] - $delta;

            if ($left > $L) {
                $L = $left;
            }
            if ($right < $R) {
                $R = $right;
            }
        }

        $ans = ($R >= $L) ? ($R - $L + 1) : 0;
        return (int)$ans;
    }
}
```

## Swift

```swift
class Solution {
    func countArrays(_ original: [Int], _ bounds: [[Int]]) -> Int {
        var low = Int.min
        var high = Int.max
        for i in 0..<original.count {
            let l = bounds[i][0] - original[i]
            let r = bounds[i][1] - original[i]
            if l > low { low = l }
            if r < high { high = r }
        }
        if low > high { return 0 }
        return high - low + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countArrays(original: IntArray, bounds: Array<IntArray>): Int {
        var low = Long.MIN_VALUE
        var high = Long.MAX_VALUE
        for (i in original.indices) {
            val li = bounds[i][0].toLong() - original[i].toLong()
            val ri = bounds[i][1].toLong() - original[i].toLong()
            if (li > low) low = li
            if (ri < high) high = ri
        }
        return if (low > high) 0 else (high - low + 1).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countArrays(List<int> original, List<List<int>> bounds) {
    int n = original.length;
    // Initialize with the first element's possible k range
    int low = bounds[0][0] - original[0];
    int high = bounds[0][1] - original[0];

    for (int i = 1; i < n; i++) {
      int curLow = bounds[i][0] - original[i];
      int curHigh = bounds[i][1] - original[i];
      if (curLow > low) low = curLow;
      if (curHigh < high) high = curHigh;
    }

    if (low > high) return 0;
    // Number of integer k in [low, high]
    return high - low + 1;
  }
}
```

## Golang

```go
func countArrays(original []int, bounds [][]int) int {
    n := len(original)
    base := original[0]
    low := int64(bounds[0][0])
    high := int64(bounds[0][1])

    for i := 1; i < n; i++ {
        diff := int64(original[i] - base)
        l := int64(bounds[i][0]) - diff
        r := int64(bounds[i][1]) - diff
        if l > low {
            low = l
        }
        if r < high {
            high = r
        }
    }

    if low > high {
        return 0
    }
    return int(high - low + 1)
}
```

## Ruby

```ruby
def count_arrays(original, bounds)
  low = -10**18
  high = 10**18
  original.each_with_index do |val, i|
    u, v = bounds[i]
    li = u - val
    ri = v - val
    low = li if li > low
    high = ri if ri < high
  end
  ans = high - low + 1
  ans < 0 ? 0 : ans
end
```

## Scala

```scala
object Solution {
    def countArrays(original: Array[Int], bounds: Array[Array[Int]]): Int = {
        var low: Long = Long.MinValue
        var high: Long = Long.MaxValue
        val n = original.length
        for (i <- 0 until n) {
            val u = bounds(i)(0).toLong
            val v = bounds(i)(1).toLong
            val o = original(i).toLong
            low = math.max(low, u - o)
            high = math.min(high, v - o)
        }
        if (low > high) 0 else ((high - low + 1).toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_arrays(original: Vec<i32>, bounds: Vec<Vec<i32>>) -> i32 {
        let mut low: i64 = i64::MIN;
        let mut high: i64 = i64::MAX;
        for (o, b) in original.iter().zip(bounds.iter()) {
            let o = *o as i64;
            let u = b[0] as i64;
            let v = b[1] as i64;
            low = low.max(u - o);
            high = high.min(v - o);
        }
        if low > high {
            0
        } else {
            (high - low + 1) as i32
        }
    }
}
```

## Racket

```racket
(define/contract (count-arrays original bounds)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length original))
         (uvec (make-vector n))
         (vvec (make-vector n)))
    (for ([b bounds] [i (in-range n)])
      (vector-set! uvec i (list-ref b 0))
      (vector-set! vvec i (list-ref b 1)))
    (let loop ((i 1)
               (low (vector-ref uvec 0))
               (high (vector-ref vvec 0))
               (cnt (make-hash)))
      (if (= i n)
          (let* ((generic-size (if (> low high) 0 (+ 1 (- high low))))
                 (sum-cnt (let ((vals (hash-values cnt)))
                            (if (null? vals) 0 (apply + vals)))))
            (+ generic-size sum-cnt))
          (let* ((u (vector-ref uvec i))
                 (v (vector-ref vvec i))
                 (prev-generic-size (if (> low high) 0 (+ 1 (- high low))))
                 (sum-cnt-prev (let ((vals (hash-values cnt)))
                                 (if (null? vals) 0 (apply + vals))))
                 (totalPrev (+ prev-generic-size sum-cnt-prev))
                 (new-low (max low u))
                 (new-high (min high v))
                 (newcnt (make-hash)))
            ;; keep existing counts that survive current bounds
            (for ([kv (hash->list cnt)])
              (let ((val (car kv)) (c (cdr kv)))
                (when (and (>= val u) (<= val v))
                  (hash-set! newcnt val (+ (hash-ref newcnt val 0) c)))))
            (define orig (list-ref original i))
            ;; number of previous states already having value = orig after processing i
            (define prior-same
              (+ (if (and (<= new-low new-high)
                          (>= orig new-low) (<= orig new-high)) 1 0)
                 (hash-ref cnt orig 0)))
            ;; add ways that switch to orig at position i
            (when (and (>= orig u) (<= orig v))
              (let ((add (- totalPrev prior-same)))
                (when (> add 0)
                  (hash-set! newcnt orig (+ (hash-ref newcnt orig 0) add)))))
            (loop (+ i 1) new-low new-high newcnt))))))
```

## Erlang

```erlang
-spec count_arrays(Original :: [integer()], Bounds :: [[integer()]]) -> integer().
count_arrays(Original, Bounds) ->
    Orig0 = hd(Original),
    [U0, V0] = hd(Bounds),
    Low0 = U0,
    High0 = V0,
    {Low, High} = loop(tl(Original), tl(Bounds), Orig0, Low0, High0),
    if
        Low > High -> 0;
        true -> High - Low + 1
    end.

loop([], [], _Orig0, Low, High) ->
    {Low, High};
loop([O|Os], [[U, V]|Bs], Orig0, CurLow, CurHigh) ->
    Offset = O - Orig0,
    L = U - Offset,
    H = V - Offset,
    NewLow = max(CurLow, L),
    NewHigh = min(CurHigh, H),
    loop(Os, Bs, Orig0, NewLow, NewHigh).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_arrays(original :: [integer], bounds :: [[integer]]) :: integer
  def count_arrays(original, bounds) do
    # Extract the first original value and its bound
    [first_orig | _] = original
    [[l0, h0] | rest_bounds] = bounds

    # Initial possible range for copy[0] and previous original value
    init = {l0, h0, first_orig}

    # Pair each subsequent original element with its corresponding bound
    pairs = Enum.zip(Enum.drop(original, 1), rest_bounds)

    {low, high, _} =
      Enum.reduce(pairs, init, fn {orig_i, [b_low, b_high]}, {cur_low, cur_high, prev_orig} ->
        delta = orig_i - prev_orig
        new_low = cur_low + delta
        new_high = cur_high + delta

        low2 = max(b_low, new_low)
        high2 = min(b_high, new_high)

        {low2, high2, orig_i}
      end)

    if low > high do
      0
    else
      high - low + 1
    end
  end
end
```
