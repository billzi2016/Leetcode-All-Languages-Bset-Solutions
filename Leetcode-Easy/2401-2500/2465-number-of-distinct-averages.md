# 2465. Number of Distinct Averages

## Cpp

```cpp
class Solution {
public:
    int distinctAverages(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_set<int> sums;
        int i = 0, j = nums.size() - 1;
        while (i < j) {
            sums.insert(nums[i] + nums[j]);
            ++i;
            --j;
        }
        return sums.size();
    }
};
```

## Java

```java
class Solution {
    public int distinctAverages(int[] nums) {
        java.util.Arrays.sort(nums);
        java.util.HashSet<Integer> sums = new java.util.HashSet<>();
        int i = 0, j = nums.length - 1;
        while (i < j) {
            sums.add(nums[i] + nums[j]);
            i++;
            j--;
        }
        return sums.size();
    }
}
```

## Python

```python
class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        seen = set()
        i, j = 0, len(nums) - 1
        while i < j:
            seen.add(nums[i] + nums[j])
            i += 1
            j -= 1
        return len(seen)
```

## Python3

```python
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        i, j = 0, len(nums) - 1
        while i < j:
            seen.add(nums[i] + nums[j])
            i += 1
            j -= 1
        return len(seen)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int distinctAverages(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    bool seen[201] = {false};
    int count = 0;
    for (int i = 0; i < numsSize / 2; ++i) {
        int sum = nums[i] + nums[numsSize - 1 - i];
        if (!seen[sum]) {
            seen[sum] = true;
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int DistinctAverages(int[] nums) {
        Array.Sort(nums);
        var seen = new HashSet<int>();
        int n = nums.Length;
        for (int i = 0; i < n / 2; i++) {
            int sum = nums[i] + nums[n - 1 - i];
            seen.Add(sum);
        }
        return seen.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var distinctAverages = function(nums) {
    nums.sort((a, b) => a - b);
    const sums = new Set();
    let i = 0, j = nums.length - 1;
    while (i < j) {
        sums.add(nums[i] + nums[j]);
        i++;
        j--;
    }
    return sums.size;
};
```

## Typescript

```typescript
function distinctAverages(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const sums = new Set<number>();
    let i = 0, j = nums.length - 1;
    while (i < j) {
        sums.add(nums[i] + nums[j]);
        i++;
        j--;
    }
    return sums.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function distinctAverages($nums) {
        sort($nums);
        $n = count($nums);
        $uniqueSums = [];
        for ($i = 0; $i < $n / 2; $i++) {
            $sum = $nums[$i] + $nums[$n - 1 - $i];
            $uniqueSums[$sum] = true;
        }
        return count($uniqueSums);
    }
}
```

## Swift

```swift
class Solution {
    func distinctAverages(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var i = 0
        var j = sorted.count - 1
        var averages = Set<Double>()
        while i < j {
            let avg = Double(sorted[i] + sorted[j]) / 2.0
            averages.insert(avg)
            i += 1
            j -= 1
        }
        return averages.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distinctAverages(nums: IntArray): Int {
        nums.sort()
        val set = HashSet<Int>()
        var i = 0
        var j = nums.lastIndex
        while (i < j) {
            set.add(nums[i] + nums[j])
            i++
            j--
        }
        return set.size
    }
}
```

## Dart

```dart
class Solution {
  int distinctAverages(List<int> nums) {
    nums.sort();
    final Set<int> sums = {};
    int i = 0, j = nums.length - 1;
    while (i < j) {
      sums.add(nums[i] + nums[j]);
      i++;
      j--;
    }
    return sums.length;
  }
}
```

## Golang

```go
func distinctAverages(nums []int) int {
    sort.Ints(nums)
    seen := make(map[int]struct{})
    n := len(nums)
    for i := 0; i < n/2; i++ {
        sum := nums[i] + nums[n-1-i]
        seen[sum] = struct{}{}
    }
    return len(seen)
}

import "sort"
```

## Ruby

```ruby
def distinct_averages(nums)
  nums.sort!
  seen = {}
  i = 0
  j = nums.length - 1
  while i < j
    sum = nums[i] + nums[j]
    seen[sum] = true
    i += 1
    j -= 1
  end
  seen.size
end
```

## Scala

```scala
object Solution {
    def distinctAverages(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        val n = sorted.length
        val sums = scala.collection.mutable.HashSet[Int]()
        var i = 0
        var j = n - 1
        while (i < j) {
            sums.add(sorted(i) + sorted(j))
            i += 1
            j -= 1
        }
        sums.size
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn distinct_averages(nums: Vec<i32>) -> i32 {
        let mut v = nums;
        v.sort();
        let n = v.len();
        let mut set = HashSet::new();
        for i in 0..n / 2 {
            set.insert(v[i] + v[n - 1 - i]);
        }
        set.len() as i32
    }
}
```

## Racket

```racket
(define/contract (distinct-averages nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (set (make-hash)))
    (for ([i (in-range (/ n 2))])
      (define a (list-ref sorted i))
      (define b (list-ref sorted (- n 1 i)))
      (hash-set! set (/ (+ a b) 2) #t))
    (hash-count set)))
```

## Erlang

```erlang
-spec distinct_averages(Nums :: [integer()]) -> integer().
distinct_averages(Nums) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    Half = N div 2,
    First = lists:sublist(Sorted, Half),
    RevSorted = lists:reverse(Sorted),
    Second = lists:sublist(RevSorted, Half),
    Map = sums_map(First, Second, #{}),
    maps:size(Map).

sums_map([], [], Acc) -> Acc;
sums_map([A|As], [B|Bs], Acc) ->
    Sum = A + B,
    NewAcc = maps:put(Sum, true, Acc),
    sums_map(As, Bs, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec distinct_averages(nums :: [integer]) :: integer
  def distinct_averages(nums) do
    sorted = Enum.sort(nums)
    len = length(sorted)
    half = div(len, 2)

    sums =
      0..(half - 1)
      |> Enum.reduce(MapSet.new(), fn i, acc ->
        sum = Enum.at(sorted, i) + Enum.at(sorted, len - 1 - i)
        MapSet.put(acc, sum)
      end)

    MapSet.size(sums)
  end
end
```
