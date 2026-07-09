# 0768. Max Chunks To Make Sorted II

## Cpp

```cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return 0;
        vector<int> prefixMax(n), suffixMin(n);
        prefixMax[0] = arr[0];
        for (int i = 1; i < n; ++i)
            prefixMax[i] = max(prefixMax[i - 1], arr[i]);
        suffixMin[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; --i)
            suffixMin[i] = min(suffixMin[i + 1], arr[i]);
        int chunks = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (prefixMax[i] <= suffixMin[i + 1])
                ++chunks;
        }
        return chunks + 1;
    }
};
```

## Java

```java
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int n = arr.length;
        int[] suffixMin = new int[n];
        suffixMin[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffixMin[i] = Math.min(arr[i], suffixMin[i + 1]);
        }
        int count = 0;
        int curMax = Integer.MIN_VALUE;
        for (int i = 0; i < n - 1; ++i) {
            curMax = Math.max(curMax, arr[i]);
            if (curMax <= suffixMin[i + 1]) {
                count++;
            }
        }
        return count + 1;
    }
}
```

## Python

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sorted_arr = sorted(arr)
        diff = {}
        chunks = 0
        for a, b in zip(arr, sorted_arr):
            diff[a] = diff.get(a, 0) + 1
            if diff[a] == 0:
                del diff[a]
            diff[b] = diff.get(b, 0) - 1
            if diff[b] == 0:
                del diff[b]
            if not diff:
                chunks += 1
        return chunks
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        diff = defaultdict(int)
        chunks = 0
        for a, b in zip(arr, sorted_arr):
            diff[a] += 1
            if diff[a] == 0:
                del diff[a]
            diff[b] -= 1
            if diff.get(b) == 0:
                del diff[b]
            if not diff:
                chunks += 1
        return chunks
```

## C

```c
int maxChunksToSorted(int* arr, int arrSize) {
    if (arrSize == 0) return 0;
    int *suffixMin = (int *)malloc(arrSize * sizeof(int));
    suffixMin[arrSize - 1] = arr[arrSize - 1];
    for (int i = arrSize - 2; i >= 0; --i) {
        suffixMin[i] = arr[i] < suffixMin[i + 1] ? arr[i] : suffixMin[i + 1];
    }
    int chunks = 1;
    int prefixMax = arr[0];
    for (int i = 0; i < arrSize - 1; ++i) {
        if (arr[i] > prefixMax) prefixMax = arr[i];
        else if (arr[i] == prefixMax) {} // no change
        // ensure prefixMax is max up to i
        if (prefixMax <= suffixMin[i + 1]) {
            ++chunks;
        }
    }
    free(suffixMin);
    return chunks;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxChunksToSorted(int[] arr) {
        int n = arr.Length;
        if (n == 0) return 0;

        int[] prefMax = new int[n];
        int[] suffMin = new int[n];

        prefMax[0] = arr[0];
        for (int i = 1; i < n; i++) {
            prefMax[i] = Math.Max(prefMax[i - 1], arr[i]);
        }

        suffMin[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.Min(suffMin[i + 1], arr[i]);
        }

        int chunks = 1;
        for (int i = 0; i < n - 1; i++) {
            if (prefMax[i] <= suffMin[i + 1]) {
                chunks++;
            }
        }

        return chunks;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    const n = arr.length;
    if (n === 0) return 0;
    const prefixMax = new Array(n);
    let curMax = -Infinity;
    for (let i = 0; i < n; i++) {
        curMax = Math.max(curMax, arr[i]);
        prefixMax[i] = curMax;
    }
    const suffixMin = new Array(n);
    let curMin = Infinity;
    for (let i = n - 1; i >= 0; i--) {
        curMin = Math.min(curMin, arr[i]);
        suffixMin[i] = curMin;
    }
    let chunks = 0;
    for (let i = 0; i < n - 1; i++) {
        if (prefixMax[i] <= suffixMin[i + 1]) {
            chunks++;
        }
    }
    return chunks + 1;
};
```

## Typescript

```typescript
function maxChunksToSorted(arr: number[]): number {
    const n = arr.length;
    if (n === 0) return 0;

    const prefixMax = new Array<number>(n);
    let curMax = -Infinity;
    for (let i = 0; i < n; i++) {
        curMax = Math.max(curMax, arr[i]);
        prefixMax[i] = curMax;
    }

    const suffixMin = new Array<number>(n);
    let curMin = Infinity;
    for (let i = n - 1; i >= 0; i--) {
        curMin = Math.min(curMin, arr[i]);
        suffixMin[i] = curMin;
    }

    let chunks = 1;
    for (let i = 0; i < n - 1; i++) {
        if (prefixMax[i] <= suffixMin[i + 1]) {
            chunks++;
        }
    }
    return chunks;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maxChunksToSorted($arr) {
        $n = count($arr);
        if ($n == 0) return 0;

        $prefMax = [];
        $maxVal = $arr[0];
        for ($i = 0; $i < $n; $i++) {
            if ($arr[$i] > $maxVal) {
                $maxVal = $arr[$i];
            }
            $prefMax[$i] = $maxVal;
        }

        $suffMin = array_fill(0, $n, 0);
        $minVal = $arr[$n - 1];
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($arr[$i] < $minVal) {
                $minVal = $arr[$i];
            }
            $suffMin[$i] = $minVal;
        }

        $chunks = 1; // at least one chunk
        for ($i = 0; $i < $n - 1; $i++) {
            if ($prefMax[$i] <= $suffMin[$i + 1]) {
                $chunks++;
            }
        }

        return $chunks;
    }
}
```

## Swift

```swift
class Solution {
    func maxChunksToSorted(_ arr: [Int]) -> Int {
        let n = arr.count
        if n == 0 { return 0 }
        var prefixMax = [Int](repeating: 0, count: n)
        var curMax = arr[0]
        for i in 0..<n {
            curMax = max(curMax, arr[i])
            prefixMax[i] = curMax
        }
        var suffixMin = [Int](repeating: 0, count: n)
        var curMin = arr[n - 1]
        for i in stride(from: n - 1, through: 0, by: -1) {
            curMin = min(curMin, arr[i])
            suffixMin[i] = curMin
        }
        var chunks = 1
        if n > 1 {
            for i in 0..<(n - 1) {
                if prefixMax[i] <= suffixMin[i + 1] {
                    chunks += 1
                }
            }
        }
        return chunks
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxChunksToSorted(arr: IntArray): Int {
        val n = arr.size
        if (n == 0) return 0
        val suffixMin = IntArray(n)
        var curMin = Int.MAX_VALUE
        for (i in n - 1 downTo 0) {
            curMin = kotlin.math.min(curMin, arr[i])
            suffixMin[i] = curMin
        }
        var count = 0
        var curMax = Int.MIN_VALUE
        for (i in 0 until n - 1) {
            curMax = kotlin.math.max(curMax, arr[i])
            if (curMax <= suffixMin[i + 1]) {
                count++
            }
        }
        return count + 1
    }
}
```

## Dart

```dart
class Solution {
  int maxChunksToSorted(List<int> arr) {
    int n = arr.length;
    if (n == 0) return 0;

    List<int> prefixMax = List.filled(n, 0);
    int curMax = arr[0];
    for (int i = 0; i < n; i++) {
      if (arr[i] > curMax) curMax = arr[i];
      prefixMax[i] = curMax;
    }

    List<int> suffixMin = List.filled(n, 0);
    int curMin = arr[n - 1];
    for (int i = n - 1; i >= 0; i--) {
      if (arr[i] < curMin) curMin = arr[i];
      suffixMin[i] = curMin;
    }

    int chunks = 0;
    for (int i = 0; i < n - 1; i++) {
      if (prefixMax[i] <= suffixMin[i + 1]) {
        chunks++;
      }
    }
    return chunks + 1; // last chunk
  }
}
```

## Golang

```go
func maxChunksToSorted(arr []int) int {
    n := len(arr)
    if n == 0 {
        return 0
    }
    // suffixMin[i] = minimum of arr[i..n-1]
    suffixMin := make([]int, n)
    suffixMin[n-1] = arr[n-1]
    for i := n - 2; i >= 0; i-- {
        if arr[i] < suffixMin[i+1] {
            suffixMin[i] = arr[i]
        } else {
            suffixMin[i] = suffixMin[i+1]
        }
    }

    count := 0
    curMax := arr[0]
    for i := 0; i < n-1; i++ {
        if arr[i] > curMax {
            curMax = arr[i]
        }
        if curMax <= suffixMin[i+1] {
            count++
        }
    }
    return count + 1
}
```

## Ruby

```ruby
def max_chunks_to_sorted(arr)
  n = arr.length
  pref_max = Array.new(n)
  cur_max = -Float::INFINITY
  arr.each_with_index do |v, i|
    cur_max = v > cur_max ? v : cur_max
    pref_max[i] = cur_max
  end

  suff_min = Array.new(n)
  cur_min = Float::INFINITY
  (n - 1).downto(0) do |i|
    cur_min = arr[i] < cur_min ? arr[i] : cur_min
    suff_min[i] = cur_min
  end

  chunks = 1
  (0...n - 1).each do |i|
    chunks += 1 if pref_max[i] <= suff_min[i + 1]
  end
  chunks
end
```

## Scala

```scala
object Solution {
    def maxChunksToSorted(arr: Array[Int]): Int = {
        val n = arr.length
        if (n == 0) return 0

        val leftMax = new Array[Int](n)
        var curMax = Int.MinValue
        for (i <- 0 until n) {
            curMax = math.max(curMax, arr(i))
            leftMax(i) = curMax
        }

        val suffixMin = new Array[Int](n)
        var curMin = Int.MaxValue
        for (i <- (n - 1) to 0 by -1) {
            suffixMin(i) = curMin          // min of elements after i
            curMin = math.min(curMin, arr(i))
        }

        var chunks = 0
        for (i <- 0 until n - 1) {
            if (leftMax(i) <= suffixMin(i)) chunks += 1
        }
        chunks + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n == 0 {
            return 0;
        }
        let mut pref = vec![0i32; n];
        let mut cur_max = arr[0];
        for i in 0..n {
            if arr[i] > cur_max {
                cur_max = arr[i];
            }
            pref[i] = cur_max;
        }

        let mut suff = vec![0i32; n];
        let mut cur_min = arr[n - 1];
        for i in (0..n).rev() {
            if arr[i] < cur_min {
                cur_min = arr[i];
            }
            suff[i] = cur_min;
        }

        let mut chunks = 0i32;
        for i in 0..n - 1 {
            if pref[i] <= suff[i + 1] {
                chunks += 1;
            }
        }
        chunks + 1
    }
}
```

## Racket

```racket
(define/contract (max-chunks-to-sorted arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort arr <)))
    (let loop ((orig arr) (srt sorted) (orig-sum 0) (srt-sum 0) (chunks 0))
      (if (null? orig)
          chunks
          (let* ((new-orig (+ orig-sum (car orig)))
                 (new-srt (+ srt-sum (car srt))))
            (loop (cdr orig)
                  (cdr srt)
                  new-orig
                  new-srt
                  (if (= new-orig new-srt) (+ chunks 1) chunks)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_chunks_to_sorted/1]).

max_chunks_to_sorted(Arr) ->
    Prefix = prefix_maxes(Arr),
    Suffix = suffix_mins(Arr),
    count_cuts(Prefix, Suffix).

prefix_maxes(Arr) ->
    {_, Rev} = lists:foldl(
        fun(X, {Prev, Acc}) ->
            Curr = case Prev of
                undefined -> X;
                _ -> erlang:max(X, Prev)
            end,
            {Curr, [Curr | Acc]}
        end,
        {undefined, []},
        Arr),
    lists:reverse(Rev).

suffix_mins(Arr) ->
    RevArr = lists:reverse(Arr),
    {_, Rev} = lists:foldl(
        fun(X, {Prev, Acc}) ->
            Curr = case Prev of
                undefined -> X;
                _ -> erlang:min(X, Prev)
            end,
            {Curr, [Curr | Acc]}
        end,
        {undefined, []},
        RevArr),
    lists:reverse(Rev).

count_cuts(Prefix, Suffix) ->
    Pairs = lists:zip(Prefix, tl(Suffix)),
    Count = lists:foldl(
        fun({Pref, Suff}, Acc) ->
            if Pref =< Suff -> Acc + 1; true -> Acc end
        end,
        0,
        Pairs),
    Count + 1.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_chunks_to_sorted(arr :: [integer]) :: integer
  def max_chunks_to_sorted(arr) do
    # prefix maximums
    {prefix, _} =
      Enum.map_reduce(arr, -1_000_000_001, fn x, cur_max ->
        new_max = if x > cur_max, do: x, else: cur_max
        {new_max, new_max}
      end)

    # suffix minimums
    {suffix_rev, _} =
      Enum.map_reduce(Enum.reverse(arr), 1_000_000_001, fn x, cur_min ->
        new_min = if x < cur_min, do: x, else: cur_min
        {new_min, new_min}
      end)

    suffix = Enum.reverse(suffix_rev)
    inf = 1_000_000_001

    # shift suffix left by one and append INF at the end
    suffix_shifted =
      case suffix do
        [] -> [inf]
        [_first | rest] -> rest ++ [inf]
      end

    Enum.zip(prefix, suffix_shifted)
    |> Enum.reduce(0, fn {lmax, rmin}, acc ->
      if lmax <= rmin, do: acc + 1, else: acc
    end)
  end
end
```
