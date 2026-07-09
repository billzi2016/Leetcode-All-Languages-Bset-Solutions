# 2611. Mice and Cheese

## Cpp

```cpp
class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        int n = reward1.size();
        long long base = 0;
        vector<int> diff(n);
        for (int i = 0; i < n; ++i) {
            base += reward2[i];
            diff[i] = reward1[i] - reward2[i];
        }
        nth_element(diff.begin(), diff.begin() + k, diff.end(), greater<int>());
        long long add = 0;
        for (int i = 0; i < k; ++i) add += diff[i];
        return static_cast<int>(base + add);
    }
};
```

## Java

```java
class Solution {
    public int miceAndCheese(int[] reward1, int[] reward2, int k) {
        int n = reward1.length;
        long baseSum = 0;
        int[] diff = new int[n];
        for (int i = 0; i < n; i++) {
            baseSum += reward2[i];
            diff[i] = reward1[i] - reward2[i];
        }
        java.util.Arrays.sort(diff);
        long add = 0;
        for (int i = n - 1; i >= n - k && i >= 0; i--) {
            add += diff[i];
        }
        return (int) (baseSum + add);
    }
}
```

## Python

```python
class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(reward2)
        diffs = [a - b for a, b in zip(reward1, reward2)]
        diffs.sort(reverse=True)
        total += sum(diffs[:k])
        return total
```

## Python3

```python
from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        total = sum(reward2)
        diffs = [a - b for a, b in zip(reward1, reward2)]
        diffs.sort(reverse=True)
        total += sum(diffs[:k])
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return 1;   // descending order
    if (la > lb) return -1;
    return 0;
}

int miceAndCheese(int* reward1, int reward1Size, int* reward2, int reward2Size, int k) {
    int n = reward1Size; // reward1Size == reward2Size
    long long *delta = (long long *)malloc(sizeof(long long) * n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += reward2[i];
        delta[i] = (long long)reward1[i] - (long long)reward2[i];
    }
    if (k > 0) {
        qsort(delta, n, sizeof(long long), cmp_desc);
        for (int i = 0; i < k; ++i) {
            total += delta[i];
        }
    }
    free(delta);
    return (int)total;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MiceAndCheese(int[] reward1, int[] reward2, int k) {
        int n = reward1.Length;
        long total = 0;
        for (int i = 0; i < n; i++) {
            total += reward2[i];
        }

        int[] diff = new int[n];
        for (int i = 0; i < n; i++) {
            diff[i] = reward1[i] - reward2[i];
        }
        Array.Sort(diff);
        // take the largest k differences
        for (int i = n - 1; i >= n - k && i >= 0; i--) {
            total += diff[i];
        }

        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} reward1
 * @param {number[]} reward2
 * @param {number} k
 * @return {number}
 */
var miceAndCheese = function(reward1, reward2, k) {
    const n = reward1.length;
    let base = 0;
    const diffs = new Array(n);
    for (let i = 0; i < n; ++i) {
        base += reward2[i];
        diffs[i] = reward1[i] - reward2[i];
    }
    diffs.sort((a, b) => b - a); // descending
    let add = 0;
    for (let i = 0; i < k; ++i) {
        add += diffs[i];
    }
    return base + add;
};
```

## Typescript

```typescript
function miceAndCheese(reward1: number[], reward2: number[], k: number): number {
    const n = reward1.length;
    let total = 0;
    const diff: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        total += reward2[i];
        diff[i] = reward1[i] - reward2[i];
    }
    diff.sort((a, b) => b - a);
    for (let i = 0; i < k; i++) {
        total += diff[i];
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $reward1
     * @param Integer[] $reward2
     * @param Integer $k
     * @return Integer
     */
    function miceAndCheese($reward1, $reward2, $k) {
        $n = count($reward1);
        $base = array_sum($reward2);
        $diffs = [];
        for ($i = 0; $i < $n; $i++) {
            $diffs[] = $reward1[$i] - $reward2[$i];
        }
        rsort($diffs); // descending order
        $add = 0;
        for ($i = 0; $i < $k; $i++) {
            $add += $diffs[$i];
        }
        return $base + $add;
    }
}
```

## Swift

```swift
class Solution {
    func miceAndCheese(_ reward1: [Int], _ reward2: [Int], _ k: Int) -> Int {
        let n = reward1.count
        var base = 0
        var diffs = [Int]()
        diffs.reserveCapacity(n)
        for i in 0..<n {
            base += reward2[i]
            diffs.append(reward1[i] - reward2[i])
        }
        diffs.sort(by: >)
        var add = 0
        for i in 0..<k {
            add += diffs[i]
        }
        return base + add
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun miceAndCheese(reward1: IntArray, reward2: IntArray, k: Int): Int {
        val n = reward1.size
        var baseSum = 0L
        val diff = IntArray(n)
        for (i in 0 until n) {
            baseSum += reward2[i].toLong()
            diff[i] = reward1[i] - reward2[i]
        }
        diff.sort() // ascending
        var extra = 0L
        if (k > 0) {
            for (i in n - k until n) {
                extra += diff[i].toLong()
            }
        }
        return (baseSum + extra).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int miceAndCheese(List<int> reward1, List<int> reward2, int k) {
    int n = reward1.length;
    List<int> diffs = List.filled(n, 0);
    int total = 0;
    for (int i = 0; i < n; i++) {
      total += reward2[i];
      diffs[i] = reward1[i] - reward2[i];
    }
    diffs.sort((a, b) => b.compareTo(a));
    for (int i = 0; i < k; i++) {
      total += diffs[i];
    }
    return total;
  }
}
```

## Golang

```go
import "sort"

func miceAndCheese(reward1 []int, reward2 []int, k int) int {
	n := len(reward1)
	diffs := make([]int, n)
	sum := 0
	for i := 0; i < n; i++ {
		sum += reward2[i]
		diffs[i] = reward1[i] - reward2[i]
	}
	sort.Slice(diffs, func(i, j int) bool { return diffs[i] > diffs[j] })
	for i := 0; i < k; i++ {
		sum += diffs[i]
	}
	return sum
}
```

## Ruby

```ruby
def mice_and_cheese(reward1, reward2, k)
  base = reward2.sum
  diffs = reward1.each_with_index.map { |r1, i| r1 - reward2[i] }
  diffs.sort!.reverse!
  base + diffs[0, k].sum
end
```

## Scala

```scala
object Solution {
    def miceAndCheese(reward1: Array[Int], reward2: Array[Int], k: Int): Int = {
        val n = reward1.length
        var baseSum: Long = 0L
        val diff = new Array[Int](n)
        var i = 0
        while (i < n) {
            baseSum += reward2(i)
            diff(i) = reward1(i) - reward2(i)
            i += 1
        }
        java.util.Arrays.sort(diff) // ascending
        var extra: Long = 0L
        var taken = 0
        while (taken < k) {
            extra += diff(n - 1 - taken)
            taken += 1
        }
        (baseSum + extra).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn mice_and_cheese(reward1: Vec<i32>, reward2: Vec<i32>, k: i32) -> i32 {
        let n = reward1.len();
        let mut diffs = Vec::with_capacity(n);
        let mut total: i64 = 0;
        for i in 0..n {
            total += reward2[i] as i64;
            diffs.push(reward1[i] - reward2[i]);
        }
        diffs.sort_unstable_by(|a, b| b.cmp(a)); // descending
        let k_usize = k as usize;
        for i in 0..k_usize {
            total += diffs[i] as i64;
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (mice-and-cheese reward1 reward2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sum2 (foldl + 0 reward2))
         (diffs (map - reward1 reward2))
         (sorted-diffs (sort diffs >)))
    (+ sum2
       (let loop ((i 0) (acc 0) (lst sorted-diffs))
         (if (or (= i k) (null? lst))
             acc
             (loop (+ i 1) (+ acc (car lst)) (cdr lst)))))))
```

## Erlang

```erlang
-module(solution).
-export([mice_and_cheese/3]).

-spec mice_and_cheese(Reward1 :: [integer()], Reward2 :: [integer()], K :: integer()) -> integer().
mice_and_cheese(Reward1, Reward2, K) ->
    Total2 = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Reward2),
    Diffs = [R1 - R2 || {R1, R2} <- lists:zip(Reward1, Reward2)],
    SortedDesc = lists:reverse(lists:sort(Diffs)),
    TopK = lists:sublist(SortedDesc, K),
    SumTopK = lists:foldl(fun(X, Acc) -> X + Acc end, 0, TopK),
    Total2 + SumTopK.
```

## Elixir

```elixir
defmodule Solution do
  @spec mice_and_cheese(reward1 :: [integer], reward2 :: [integer], k :: integer) :: integer
  def mice_and_cheese(reward1, reward2, k) do
    total_reward2 = Enum.reduce(reward2, 0, &+/2)

    diffs =
      Enum.zip(reward1, reward2)
      |> Enum.map(fn {r1, r2} -> r1 - r2 end)

    top_k_sum =
      diffs
      |> Enum.sort(:desc)
      |> Enum.take(k)
      |> Enum.sum()

    total_reward2 + top_k_sum
  end
end
```
