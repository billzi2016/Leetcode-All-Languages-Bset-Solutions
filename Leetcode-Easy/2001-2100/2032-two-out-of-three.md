# 2032. Two Out of Three

## Cpp

```cpp
class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        int cnt[101] = {0};
        bool seen[101];
        
        // Process first array
        memset(seen, 0, sizeof(seen));
        for (int x : nums1) {
            if (!seen[x]) {
                cnt[x]++;
                seen[x] = true;
            }
        }
        // Process second array
        memset(seen, 0, sizeof(seen));
        for (int x : nums2) {
            if (!seen[x]) {
                cnt[x]++;
                seen[x] = true;
            }
        }
        // Process third array
        memset(seen, 0, sizeof(seen));
        for (int x : nums3) {
            if (!seen[x]) {
                cnt[x]++;
                seen[x] = true;
            }
        }
        
        vector<int> res;
        for (int i = 1; i <= 100; ++i) {
            if (cnt[i] >= 2) res.push_back(i);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        java.util.Set<Integer> set1 = new java.util.HashSet<>();
        java.util.Set<Integer> set2 = new java.util.HashSet<>();
        java.util.Set<Integer> set3 = new java.util.HashSet<>();
        for (int x : nums1) set1.add(x);
        for (int x : nums2) set2.add(x);
        for (int x : nums3) set3.add(x);
        
        java.util.Map<Integer, Integer> count = new java.util.HashMap<>();
        for (int x : set1) count.put(x, count.getOrDefault(x, 0) + 1);
        for (int x : set2) count.put(x, count.getOrDefault(x, 0) + 1);
        for (int x : set3) count.put(x, count.getOrDefault(x, 0) + 1);
        
        java.util.List<Integer> result = new java.util.ArrayList<>();
        for (java.util.Map.Entry<Integer, Integer> e : count.entrySet()) {
            if (e.getValue() >= 2) {
                result.add(e.getKey());
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        cnt = Counter()
        for s in (set(nums1), set(nums2), set(nums3)):
            cnt.update(s)
        return [num for num, c in cnt.items() if c >= 2]
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        cnt = Counter()
        for s in (set(nums1), set(nums2), set(nums3)):
            cnt.update(s)
        return [num for num, c in cnt.items() if c >= 2]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoOutOfThree(int* nums1, int nums1Size, int* nums2, int nums2Size,
                   int* nums3, int nums3Size, int* returnSize) {
    int freq[101] = {0};
    bool seen[101];

    // Process nums1
    for (int i = 0; i < 101; ++i) seen[i] = false;
    for (int i = 0; i < nums1Size; ++i) {
        int v = nums1[i];
        if (!seen[v]) {
            freq[v]++;
            seen[v] = true;
        }
    }

    // Process nums2
    for (int i = 0; i < 101; ++i) seen[i] = false;
    for (int i = 0; i < nums2Size; ++i) {
        int v = nums2[i];
        if (!seen[v]) {
            freq[v]++;
            seen[v] = true;
        }
    }

    // Process nums3
    for (int i = 0; i < 101; ++i) seen[i] = false;
    for (int i = 0; i < nums3Size; ++i) {
        int v = nums3[i];
        if (!seen[v]) {
            freq[v]++;
            seen[v] = true;
        }
    }

    // Collect results
    int *result = (int *)malloc(101 * sizeof(int));
    int cnt = 0;
    for (int v = 1; v <= 100; ++v) {
        if (freq[v] >= 2) {
            result[cnt++] = v;
        }
    }

    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> TwoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        var set1 = new HashSet<int>(nums1);
        var set2 = new HashSet<int>(nums2);
        var set3 = new HashSet<int>(nums3);

        var count = new Dictionary<int, int>();

        foreach (var x in set1) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        foreach (var x in set2) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        foreach (var x in set3) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }

        var result = new List<int>();
        foreach (var kvp in count) {
            if (kvp.Value >= 2) {
                result.Add(kvp.Key);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @return {number[]}
 */
var twoOutOfThree = function(nums1, nums2, nums3) {
    const countMap = new Map();
    const process = (arr) => {
        const uniq = new Set(arr);
        for (const num of uniq) {
            countMap.set(num, (countMap.get(num) || 0) + 1);
        }
    };
    process(nums1);
    process(nums2);
    process(nums3);
    
    const result = [];
    for (const [num, cnt] of countMap.entries()) {
        if (cnt >= 2) result.push(num);
    }
    return result;
};
```

## Typescript

```typescript
function twoOutOfThree(nums1: number[], nums2: number[], nums3: number[]): number[] {
    const count = new Map<number, number>();
    for (const arr of [nums1, nums2, nums3]) {
        const unique = new Set(arr);
        for (const v of unique) {
            count.set(v, (count.get(v) ?? 0) + 1);
        }
    }
    const result: number[] = [];
    for (const [num, freq] of count.entries()) {
        if (freq >= 2) result.push(num);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer[] $nums3
     * @return Integer[]
     */
    function twoOutOfThree($nums1, $nums2, $nums3) {
        $count = [];

        foreach ([$nums1, $nums2, $nums3] as $arr) {
            $seen = [];
            foreach ($arr as $num) {
                if (!isset($seen[$num])) {
                    $seen[$num] = true;
                    if (!isset($count[$num])) {
                        $count[$num] = 0;
                    }
                    $count[$num]++;
                }
            }
        }

        $result = [];
        foreach ($count as $num => $freq) {
            if ($freq >= 2) {
                $result[] = $num;
            }
        }

        sort($result);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func twoOutOfThree(_ nums1: [Int], _ nums2: [Int], _ nums3: [Int]) -> [Int] {
        var freq = [Int: Int]()
        for n in Set(nums1) { freq[n, default: 0] += 1 }
        for n in Set(nums2) { freq[n, default: 0] += 1 }
        for n in Set(nums3) { freq[n, default: 0] += 1 }
        var result = [Int]()
        for (num, count) in freq where count >= 2 {
            result.append(num)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun twoOutOfThree(nums1: IntArray, nums2: IntArray, nums3: IntArray): List<Int> {
        val count = HashMap<Int, Int>()
        for (set in arrayOf(nums1.toSet(), nums2.toSet(), nums3.toSet())) {
            for (v in set) {
                count[v] = (count[v] ?: 0) + 1
            }
        }
        val result = ArrayList<Int>()
        for ((k, v) in count) {
            if (v >= 2) result.add(k)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> twoOutOfThree(List<int> nums1, List<int> nums2, List<int> nums3) {
    final Map<int, int> count = {};
    for (var set in [nums1.toSet(), nums2.toSet(), nums3.toSet()]) {
      for (var num in set) {
        count[num] = (count[num] ?? 0) + 1;
      }
    }
    List<int> result = [];
    count.forEach((key, value) {
      if (value >= 2) result.add(key);
    });
    return result;
  }
}
```

## Golang

```go
func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	cnt := make(map[int]int)

	add := func(arr []int) {
		seen := make(map[int]struct{})
		for _, v := range arr {
			if _, ok := seen[v]; !ok {
				cnt[v]++
				seen[v] = struct{}{}
			}
		}
	}

	add(nums1)
	add(nums2)
	add(nums3)

	res := []int{}
	for k, v := range cnt {
		if v >= 2 {
			res = append(res, k)
		}
	}
	return res
}
```

## Ruby

```ruby
def two_out_of_three(nums1, nums2, nums3)
  counts = Hash.new(0)
  [nums1, nums2, nums3].each do |arr|
    arr.uniq.each { |v| counts[v] += 1 }
  end
  result = []
  counts.each { |k, v| result << k if v >= 2 }
  result
end
```

## Scala

```scala
object Solution {
    def twoOutOfThree(nums1: Array[Int], nums2: Array[Int], nums3: Array[Int]): List[Int] = {
        val count = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        for (arr <- Seq(nums1, nums2, nums3)) {
            arr.toSet.foreach(v => count(v) += 1)
        }
        count.filter(_._2 >= 2).keys.toList
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn two_out_of_three(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>) -> Vec<i32> {
        let mut count = [0; 101];
        for arr in [&nums1, &nums2, &nums3].iter() {
            let set: HashSet<_> = arr.iter().cloned().collect();
            for v in set {
                count[v as usize] += 1;
            }
        }
        let mut res = Vec::new();
        for i in 1..=100 {
            if count[i] >= 2 {
                res.push(i as i32);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (two-out-of-three nums1 nums2 nums3)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ([cnt (make-hash)]
         [process
          (lambda (lst)
            (for ([x (in-list (remove-duplicates lst))])
              (hash-update! cnt x (lambda (old) (+ old 1)) 0)))])
    (process nums1)
    (process nums2)
    (process nums3)
    (let ([res (for/list ([pair (in-hash cnt)]
                           #:when (>= (cdr pair) 2))
                 (car pair))])
      (sort res <))))
```

## Erlang

```erlang
-spec two_out_of_three([integer()], [integer()], [integer()]) -> [integer()].
two_out_of_three(Nums1, Nums2, Nums3) ->
    Unique1 = lists:usort(Nums1),
    Unique2 = lists:usort(Nums2),
    Unique3 = lists:usort(Nums3),
    CountMap0 = increment_counts(Unique1, #{}),
    CountMap1 = increment_counts(Unique2, CountMap0),
    CountMap2 = increment_counts(Unique3, CountMap1),
    Result = [K || {K, V} <- maps:to_list(CountMap2), V >= 2],
    lists:sort(Result).

increment_counts([], Map) -> Map;
increment_counts([H|T], Map) ->
    NewMap = maps:update_with(H,
                fun(C) -> C + 1 end,
                1,
                Map),
    increment_counts(T, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec two_out_of_three(nums1 :: [integer], nums2 :: [integer], nums3 :: [integer]) :: [integer]
  def two_out_of_three(nums1, nums2, nums3) do
    counts =
      Enum.reduce([nums1, nums2, nums3], %{}, fn list, acc ->
        Enum.reduce(MapSet.new(list), acc, fn x, a ->
          Map.update(a, x, 1, &(&1 + 1))
        end)
      end)

    counts
    |> Enum.filter(fn {_k, v} -> v >= 2 end)
    |> Enum.map(fn {k, _v} -> k end)
  end
end
```
