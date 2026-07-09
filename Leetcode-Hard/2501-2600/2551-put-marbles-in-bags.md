# 2551. Put Marbles in Bags

## Cpp

```cpp
class Solution {
public:
    long long putMarbles(std::vector<int>& weights, int k) {
        int n = weights.size();
        if (k == 1) return 0;
        std::vector<long long> pairSums;
        pairSums.reserve(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            pairSums.push_back((long long)weights[i] + weights[i + 1]);
        }
        std::sort(pairSums.begin(), pairSums.end());
        int m = k - 1;
        long long small = 0, large = 0;
        for (int i = 0; i < m; ++i) small += pairSums[i];
        for (int i = (int)pairSums.size() - m; i < (int)pairSums.size(); ++i) large += pairSums[i];
        return large - small;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long putMarbles(int[] weights, int k) {
        int n = weights.length;
        if (k == 1) return 0L;
        long[] pairSums = new long[n - 1];
        for (int i = 0; i < n - 1; i++) {
            pairSums[i] = (long) weights[i] + weights[i + 1];
        }
        Arrays.sort(pairSums);
        long diff = 0L;
        int splits = k - 1;
        for (int i = 0; i < splits; i++) {
            diff -= pairSums[i];                     // smallest sums
            diff += pairSums[n - 2 - i];             // largest sums
        }
        return diff;
    }
}
```

## Python

```python
class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0
        pair_sums = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        pair_sums.sort()
        small = sum(pair_sums[:k - 1])
        large = sum(pair_sums[-(k - 1):])
        return large - small
```

## Python3

```python
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:
            return 0
        pair_sums = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pair_sums.sort()
        small_sum = sum(pair_sums[:k - 1])
        large_sum = sum(pair_sums[-(k - 1):])
        return large_sum - small_sum
```

## C

```c
#include <stdlib.h>

static int cmp_ll(const void *a, const void *b) {
    long long va = *(const long long *)a;
    long long vb = *(const long long *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

long long putMarbles(int* weights, int weightsSize, int k) {
    int n = weightsSize;
    if (k <= 1 || n <= 1) return 0LL;

    int pairCount = n - 1;
    long long *pairSums = (long long *)malloc(pairCount * sizeof(long long));
    if (!pairSums) return 0LL; // allocation failure fallback

    for (int i = 0; i < pairCount; ++i) {
        pairSums[i] = (long long)weights[i] + (long long)weights[i + 1];
    }

    qsort(pairSums, pairCount, sizeof(long long), cmp_ll);

    long long sumSmall = 0, sumLarge = 0;
    int splits = k - 1;
    for (int i = 0; i < splits; ++i) {
        sumSmall += pairSums[i];
        sumLarge += pairSums[pairCount - 1 - i];
    }

    free(pairSums);
    return sumLarge - sumSmall;
}
```

## Csharp

```csharp
public class Solution
{
    public long PutMarbles(int[] weights, int k)
    {
        int n = weights.Length;
        if (k == 1) return 0L;

        int m = n - 1;
        long[] pairSums = new long[m];
        for (int i = 0; i < m; i++)
        {
            pairSums[i] = (long)weights[i] + weights[i + 1];
        }

        Array.Sort(pairSums);

        int splits = k - 1;
        long diff = 0L;

        // subtract smallest sums
        for (int i = 0; i < splits; i++)
        {
            diff -= pairSums[i];
        }

        // add largest sums
        for (int i = m - splits; i < m; i++)
        {
            diff += pairSums[i];
        }

        return diff;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} weights
 * @param {number} k
 * @return {number}
 */
var putMarbles = function(weights, k) {
    const n = weights.length;
    if (k === 1) return 0;
    const pairSums = new Array(n - 1);
    for (let i = 0; i < n - 1; ++i) {
        pairSums[i] = weights[i] + weights[i + 1];
    }
    pairSums.sort((a, b) => a - b);
    const m = k - 1;
    let minSum = 0, maxSum = 0;
    for (let i = 0; i < m; ++i) {
        minSum += pairSums[i];
        maxSum += pairSums[pairSums.length - 1 - i];
    }
    return maxSum - minSum;
};
```

## Typescript

```typescript
function putMarbles(weights: number[], k: number): number {
    const n = weights.length;
    if (k === 1) return 0;

    const pairSums: number[] = new Array(n - 1);
    for (let i = 0; i < n - 1; ++i) {
        pairSums[i] = weights[i] + weights[i + 1];
    }

    pairSums.sort((a, b) => a - b);

    const m = k - 1;
    let diff = 0;
    for (let i = 0; i < m; ++i) {
        diff -= pairSums[i];                     // smallest sums
        diff += pairSums[pairSums.length - 1 - i]; // largest sums
    }
    return diff;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $weights
     * @param Integer $k
     * @return Integer
     */
    function putMarbles($weights, $k) {
        $n = count($weights);
        if ($k == 1) return 0;
        $pair = [];
        for ($i = 0; $i < $n - 1; ++$i) {
            $pair[] = $weights[$i] + $weights[$i + 1];
        }
        sort($pair); // ascending
        $m = count($pair);
        $ans = 0;
        for ($i = 0; $i < $k - 1; ++$i) {
            $ans -= $pair[$i];                 // smallest sums
            $ans += $pair[$m - 1 - $i];         // largest sums
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func putMarbles(_ weights: [Int], _ k: Int) -> Int {
        let n = weights.count
        if k == 1 { return 0 }
        var pairSums = [Int]()
        pairSums.reserveCapacity(n - 1)
        for i in 0..<(n - 1) {
            pairSums.append(weights[i] + weights[i + 1])
        }
        pairSums.sort()
        let need = k - 1
        var diff: Int64 = 0
        for i in 0..<need {
            diff -= Int64(pairSums[i])
            diff += Int64(pairSums[pairSums.count - 1 - i])
        }
        return Int(diff)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun putMarbles(weights: IntArray, k: Int): Long {
        val n = weights.size
        if (k == 1) return 0L
        val pairSums = LongArray(n - 1)
        for (i in 0 until n - 1) {
            pairSums[i] = weights[i].toLong() + weights[i + 1]
        }
        java.util.Arrays.sort(pairSums)
        var diff = 0L
        // add the largest k-1 sums
        for (i in n - 2 downTo n - k) {
            diff += pairSums[i]
        }
        // subtract the smallest k-1 sums
        for (i in 0 until k - 1) {
            diff -= pairSums[i]
        }
        return diff
    }
}
```

## Dart

```dart
class Solution {
  int putMarbles(List<int> weights, int k) {
    int n = weights.length;
    if (k == 1) return 0;
    List<int> pairSums = List<int>.filled(n - 1, 0);
    for (int i = 0; i < n - 1; ++i) {
      pairSums[i] = weights[i] + weights[i + 1];
    }
    pairSums.sort();
    int splits = k - 1;
    int minSum = 0, maxSum = 0;
    for (int i = 0; i < splits; ++i) {
      minSum += pairSums[i];
    }
    for (int i = pairSums.length - splits; i < pairSums.length; ++i) {
      maxSum += pairSums[i];
    }
    return maxSum - minSum;
  }
}
```

## Golang

```go
import "sort"

func putMarbles(weights []int, k int) int64 {
	n := len(weights)
	if k == 1 {
		return 0
	}
	pair := make([]int64, n-1)
	for i := 0; i < n-1; i++ {
		pair[i] = int64(weights[i]) + int64(weights[i+1])
	}
	sort.Slice(pair, func(i, j int) bool { return pair[i] < pair[j] })
	var ans int64
	for i := 0; i < k-1; i++ {
		ans -= pair[i]
		ans += pair[n-2-i]
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} weights
# @param {Integer} k
# @return {Integer}
def put_marbles(weights, k)
  n = weights.length
  return 0 if k == 1

  pair_sums = Array.new(n - 1) { |i| weights[i] + weights[i + 1] }
  pair_sums.sort!

  diff = 0
  (0...(k - 1)).each { |i| diff -= pair_sums[i] }
  ((pair_sums.length - (k - 1))...pair_sums.length).each { |i| diff += pair_sums[i] }

  diff
end
```

## Scala

```scala
object Solution {
    def putMarbles(weights: Array[Int], k: Int): Long = {
        val n = weights.length
        if (k == 1) return 0L
        val m = n - 1
        val pair = new Array[Long](m)
        var i = 0
        while (i < m) {
            pair(i) = weights(i).toLong + weights(i + 1).toLong
            i += 1
        }
        java.util.Arrays.sort(pair)
        var ans: Long = 0L
        var j = 0
        while (j < k - 1) {
            ans -= pair(j)
            ans += pair(m - j - 1)
            j += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        let n = weights.len();
        if k == 1 || n <= 1 {
            return 0;
        }
        let mut pairs: Vec<i64> = Vec::with_capacity(n - 1);
        for i in 0..n - 1 {
            pairs.push(weights[i] as i64 + weights[i + 1] as i64);
        }
        pairs.sort_unstable();
        let take = (k as usize) - 1;
        let mut small_sum: i64 = 0;
        for i in 0..take {
            small_sum += pairs[i];
        }
        let len = pairs.len();
        let mut large_sum: i64 = 0;
        for i in len - take..len {
            large_sum += pairs[i];
        }
        large_sum - small_sum
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (put-marbles weights k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((pair-sums
          (let loop ((lst weights) (prev #f) (acc '()))
            (if (null? lst)
                (reverse acc)
                (if prev
                    (loop (cdr lst) (car lst) (cons (+ prev (car lst)) acc))
                    (loop (cdr lst) (car lst) acc)))))
         (sorted (sort pair-sums <))
         (m (- k 1)))
    (if (zero? m)
        0
        (let* ((small-sum (apply + (take sorted m)))
               (large-sum (apply + (drop sorted (- (length sorted) m)))))
          (- large-sum small-sum)))))
```

## Erlang

```erlang
-module(solution).
-export([put_marbles/2]).

-spec put_marbles(Weights :: [integer()], K :: integer()) -> integer().
put_marbles(Weights, K) ->
    PairSums = pair_sums(Weights),
    Sorted = lists:sort(PairSums),
    diff_k_minus_one(Sorted, K - 1).

pair_sums([_]) -> [];
pair_sums([A,B|Rest]) ->
    [A + B | pair_sums([B|Rest])].

diff_k_minus_one(_Sorted, 0) -> 0;
diff_k_minus_one(Sorted, Count) ->
    {Small, _} = lists:split(Count, Sorted),
    SmallSum = sum_list(Small),
    Rev = lists:reverse(Sorted),
    {Large, _} = lists:split(Count, Rev),
    LargeSum = sum_list(Large),
    LargeSum - SmallSum.

sum_list(List) ->
    lists:foldl(fun(X, Acc) -> X + Acc end, 0, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec put_marbles(weights :: [integer], k :: integer) :: integer
  def put_marbles(weights, k) do
    if k == 1 do
      0
    else
      pair_sums = compute_pair_sums(weights, [])
      sorted = Enum.sort(pair_sums)

      small_sum = sorted |> Enum.take(k - 1) |> Enum.sum()
      large_sum = sorted |> Enum.slice(- (k - 1), k - 1) |> Enum.sum()

      large_sum - small_sum
    end
  end

  defp compute_pair_sums([_], acc), do: Enum.reverse(acc)
  defp compute_pair_sums([], acc), do: Enum.reverse(acc)
  defp compute_pair_sums([a, b | rest], acc) do
    compute_pair_sums([b | rest], [a + b | acc])
  end
end
```
