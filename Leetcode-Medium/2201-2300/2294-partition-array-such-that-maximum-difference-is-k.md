# 2294. Partition Array Such That Maximum Difference Is K

## Cpp

```cpp
class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int groups = 0;
        for (int i = 0, n = nums.size(); i < n; ) {
            ++groups;
            int start = nums[i];
            while (i < n && nums[i] - start <= k) ++i;
        }
        return groups;
    }
};
```

## Java

```java
class Solution {
    public int partitionArray(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        int groups = 0;
        int i = 0;
        while (i < nums.length) {
            int start = nums[i];
            groups++;
            i++;
            while (i < nums.length && nums[i] - start <= k) {
                i++;
            }
        }
        return groups;
    }
}
```

## Python

```python
class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        groups = 0
        i = 0
        n = len(nums)
        while i < n:
            groups += 1
            start = nums[i]
            i += 1
            while i < n and nums[i] - start <= k:
                i += 1
        return groups
```

## Python3

```python
from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = 0
        i = 0
        n = len(nums)
        while i < n:
            groups += 1
            start = nums[i]
            i += 1
            while i < n and nums[i] - start <= k:
                i += 1
        return groups
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int partitionArray(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    
    int groups = 0;
    int i = 0;
    while (i < numsSize) {
        int start = nums[i];
        ++groups;
        while (i < numsSize && nums[i] - start <= k) {
            ++i;
        }
    }
    return groups;
}
```

## Csharp

```csharp
public class Solution {
    public int PartitionArray(int[] nums, int k) {
        Array.Sort(nums);
        int groups = 0;
        int i = 0;
        while (i < nums.Length) {
            groups++;
            int start = nums[i];
            i++;
            while (i < nums.Length && nums[i] - start <= k) {
                i++;
            }
        }
        return groups;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var partitionArray = function(nums, k) {
    nums.sort((a, b) => a - b);
    let groups = 0;
    let i = 0;
    const n = nums.length;
    while (i < n) {
        groups++;
        const start = nums[i];
        i++;
        while (i < n && nums[i] - start <= k) {
            i++;
        }
    }
    return groups;
};
```

## Typescript

```typescript
function partitionArray(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let groups = 0;
    let i = 0;
    const n = nums.length;
    while (i < n) {
        groups++;
        const start = nums[i];
        i++;
        while (i < n && nums[i] - start <= k) {
            i++;
        }
    }
    return groups;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function partitionArray($nums, $k) {
        sort($nums);
        $cnt = 0;
        $n = count($nums);
        $i = 0;
        while ($i < $n) {
            $cnt++;
            $start = $nums[$i];
            $i++;
            while ($i < $n && $nums[$i] - $start <= $k) {
                $i++;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func partitionArray(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        var groups = 0
        var i = 0
        let n = sorted.count
        while i < n {
            let start = sorted[i]
            groups += 1
            while i < n && sorted[i] - start <= k {
                i += 1
            }
        }
        return groups
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun partitionArray(nums: IntArray, k: Int): Int {
        val arr = nums.clone()
        arr.sort()
        var groups = 0
        var i = 0
        while (i < arr.size) {
            groups++
            val start = arr[i]
            i++
            while (i < arr.size && arr[i] - start <= k) {
                i++
            }
        }
        return groups
    }
}
```

## Dart

```dart
class Solution {
  int partitionArray(List<int> nums, int k) {
    if (nums.isEmpty) return 0;
    nums.sort();
    int groups = 1;
    int start = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] - start > k) {
        groups++;
        start = nums[i];
      }
    }
    return groups;
  }
}
```

## Golang

```go
package main

import "sort"

func partitionArray(nums []int, k int) int {
	sort.Ints(nums)
	groups := 0
	i, n := 0, len(nums)
	for i < n {
		groups++
		start := nums[i]
		i++
		for i < n && nums[i]-start <= k {
			i++
		}
	}
	return groups
}
```

## Ruby

```ruby
def partition_array(nums, k)
  nums.sort!
  groups = 0
  i = 0
  n = nums.length
  while i < n
    start = nums[i]
    groups += 1
    i += 1
    while i < n && nums[i] - start <= k
      i += 1
    end
  end
  groups
end
```

## Scala

```scala
object Solution {
  def partitionArray(nums: Array[Int], k: Int): Int = {
    if (nums.isEmpty) return 0
    val sorted = nums.sorted
    var groups = 0
    var i = 0
    while (i < sorted.length) {
      groups += 1
      val start = sorted(i)
      var j = i + 1
      while (j < sorted.length && sorted(j) - start <= k) {
        j += 1
      }
      i = j
    }
    groups
  }
}
```

## Rust

```rust
impl Solution {
    pub fn partition_array(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut groups = 0;
        let mut i = 0usize;
        while i < nums.len() {
            groups += 1;
            let start = nums[i];
            i += 1;
            while i < nums.len() && nums[i] - start <= k {
                i += 1;
            }
        }
        groups as i32
    }
}
```

## Racket

```racket
(define/contract (partition-array nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ((sorted (sort nums <)))
    (let loop ((lst sorted) (cnt 0) (group-min #f))
      (cond
        [(null? lst) cnt]
        [else
         (define cur (car lst))
         (if (or (not group-min) (> (- cur group-min) k))
             (loop (cdr lst) (+ cnt 1) cur)
             (loop (cdr lst) cnt group-min))]))))
```

## Erlang

```erlang
-module(solution).
-export([partition_array/2]).

-spec partition_array(Nums :: [integer()], K :: integer()) -> integer().
partition_array([], _K) ->
    0;
partition_array(Nums, K) ->
    Sorted = lists:sort(Nums),
    [First | Rest] = Sorted,
    count_groups(Rest, First, K, 1).

count_groups([], _Min, _K, Acc) ->
    Acc;
count_groups([H|T], Min, K, Acc) ->
    case H - Min > K of
        true -> count_groups(T, H, K, Acc + 1);
        false -> count_groups(T, Min, K, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec partition_array(nums :: [integer], k :: integer) :: integer
  def partition_array(nums, k) do
    sorted = Enum.sort(nums)

    {groups, _} =
      Enum.reduce(sorted, {0, nil}, fn x, {cnt, cur_min} ->
        if cur_min == nil or x - cur_min > k do
          {cnt + 1, x}
        else
          {cnt, cur_min}
        end
      end)

    groups
  end
end
```
