# 1636. Sort Array by Increasing Frequency

## Cpp

```cpp
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int,int> freq;
        for (int x : nums) ++freq[x];
        sort(nums.begin(), nums.end(),
            [&](int a, int b) {
                if (freq[a] == freq[b]) return a > b;
                return freq[a] < freq[b];
            });
        return nums;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) {
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        Integer[] boxed = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            boxed[i] = nums[i];
        }
        Arrays.sort(boxed, (a, b) -> {
            int fa = freq.get(a);
            int fb = freq.get(b);
            if (fa != fb) {
                return Integer.compare(fa, fb); // increasing frequency
            }
            return Integer.compare(b, a); // decreasing value when frequencies equal
        });
        for (int i = 0; i < nums.length; i++) {
            nums[i] = boxed[i];
        }
        return nums;
    }
}
```

## Python

```python
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
```

## C

```c
#include <stdlib.h>

/* Frequency array accessible by the comparator */
static int freq[201];

static int cmp(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    int fx = freq[x + 100];
    int fy = freq[y + 100];
    if (fx == fy)
        return y - x;          // same frequency -> larger value first
    return fx - fy;            // lower frequency first
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* frequencySort(int* nums, int numsSize, int* returnSize) {
    for (int i = 0; i < 201; ++i)
        freq[i] = 0;
    for (int i = 0; i < numsSize; ++i)
        ++freq[nums[i] + 100];

    int *res = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i)
        res[i] = nums[i];

    qsort(res, numsSize, sizeof(int), cmp);

    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FrequencySort(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (int n in nums) {
            if (freq.ContainsKey(n))
                freq[n]++;
            else
                freq[n] = 1;
        }

        Array.Sort(nums, (a, b) => {
            int fa = freq[a];
            int fb = freq[b];
            if (fa == fb)
                return b.CompareTo(a); // descending value when frequencies equal
            return fa.CompareTo(fb);   // ascending frequency
        });

        return nums;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
    const freq = new Map();
    for (const n of nums) {
        freq.set(n, (freq.get(n) || 0) + 1);
    }
    nums.sort((a, b) => {
        const fa = freq.get(a), fb = freq.get(b);
        if (fa === fb) return b - a; // same frequency -> larger value first
        return fa - fb; // lower frequency first
    });
    return nums;
};
```

## Typescript

```typescript
function frequencySort(nums: number[]): number[] {
    const freq = new Map<number, number>();
    for (const n of nums) {
        freq.set(n, (freq.get(n) ?? 0) + 1);
    }
    nums.sort((a, b) => {
        const fa = freq.get(a)!;
        const fb = freq.get(b)!;
        if (fa === fb) return b - a; // same frequency: larger value first
        return fa - fb; // lower frequency first
    });
    return nums;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function frequencySort($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (isset($freq[$num])) {
                $freq[$num]++;
            } else {
                $freq[$num] = 1;
            }
        }

        usort($nums, function($a, $b) use ($freq) {
            if ($freq[$a] == $freq[$b]) {
                // same frequency: larger value first
                return $b <=> $a;
            }
            // lower frequency first
            return $freq[$a] <=> $freq[$b];
        });

        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func frequencySort(_ nums: [Int]) -> [Int] {
        var freq = [Int: Int]()
        for n in nums {
            freq[n, default: 0] += 1
        }
        return nums.sorted { a, b in
            let fa = freq[a]!
            let fb = freq[b]!
            if fa == fb {
                return a > b
            } else {
                return fa < fb
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun frequencySort(nums: IntArray): IntArray {
        val freq = HashMap<Int, Int>()
        for (num in nums) {
            freq[num] = freq.getOrDefault(num, 0) + 1
        }
        return nums.sortedWith { a, b ->
            val fa = freq[a]!!
            val fb = freq[b]!!
            if (fa == fb) {
                b - a
            } else {
                fa - fb
            }
        }.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> frequencySort(List<int> nums) {
    final Map<int, int> freq = {};
    for (var n in nums) {
      freq[n] = (freq[n] ?? 0) + 1;
    }
    nums.sort((a, b) {
      final fa = freq[a]!;
      final fb = freq[b]!;
      if (fa == fb) {
        return b.compareTo(a); // descending value when frequencies equal
      }
      return fa.compareTo(fb); // ascending frequency
    });
    return nums;
  }
}
```

## Golang

```go
package main

import "sort"

func frequencySort(nums []int) []int {
	freq := make(map[int]int)
	for _, v := range nums {
		freq[v]++
	}
	sort.Slice(nums, func(i, j int) bool {
		a, b := nums[i], nums[j]
		if freq[a] == freq[b] {
			return a > b
		}
		return freq[a] < freq[b]
	})
	return nums
}
```

## Ruby

```ruby
def frequency_sort(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  nums.sort_by { |x| [freq[x], -x] }
end
```

## Scala

```scala
object Solution {
    def frequencySort(nums: Array[Int]): Array[Int] = {
        val freq = nums.groupBy(identity).view.mapValues(_.length).toMap
        nums.sortWith { (a, b) =>
            val fa = freq(a)
            val fb = freq(b)
            if (fa == fb) a > b else fa < fb
        }
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn frequency_sort(nums: Vec<i32>) -> Vec<i32> {
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for &num in &nums {
            *freq.entry(num).or_insert(0) += 1;
        }
        let mut res = nums.clone();
        res.sort_by(|a, b| {
            let fa = freq.get(a).unwrap();
            let fb = freq.get(b).unwrap();
            if fa == fb {
                b.cmp(a)
            } else {
                fa.cmp(fb)
            }
        });
        res
    }
}
```

## Racket

```racket
(define/contract (frequency-sort nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ((freq (make-hash)))
    (for ([x nums])
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    (sort nums
          (lambda (a b)
            (let ((fa (hash-ref freq a))
                  (fb (hash-ref freq b)))
              (if (= fa fb)
                  (> a b)        ; same frequency → larger value first
                  (< fa fb)))))))
```

## Erlang

```erlang
-spec frequency_sort([integer()]) -> [integer()].
frequency_sort(Nums) ->
    FreqMap = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N,
                fun(C) -> C + 1 end,
                1,
                Acc)
        end,
        #{},
        Nums),
    Comp = fun(A, B) ->
        FA = maps:get(A, FreqMap),
        FB = maps:get(B, FreqMap),
        case FA == FB of
            true -> A > B;
            false -> FA < FB
        end
    end,
    lists:sort(Comp, Nums).
```

## Elixir

```elixir
defmodule Solution do
  @spec frequency_sort(nums :: [integer]) :: [integer]
  def frequency_sort(nums) do
    freq = Enum.reduce(nums, %{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)

    Enum.sort_by(nums, fn x -> {Map.get(freq, x), -x} end)
  end
end
```
