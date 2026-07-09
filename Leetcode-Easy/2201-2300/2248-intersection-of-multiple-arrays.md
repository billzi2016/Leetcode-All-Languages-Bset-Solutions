# 2248. Intersection of Multiple Arrays

## Cpp

```cpp
class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        const int MAX_VAL = 1000;
        vector<int> cnt(MAX_VAL + 1, 0);
        int m = nums.size();
        for (const auto& arr : nums) {
            for (int x : arr) {
                ++cnt[x];
            }
        }
        vector<int> res;
        for (int i = 1; i <= MAX_VAL; ++i) {
            if (cnt[i] == m) res.push_back(i);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> intersection(int[][] nums) {
        int n = nums.length;
        int[] count = new int[1001];
        for (int[] arr : nums) {
            for (int v : arr) {
                count[v]++;
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= 1000; i++) {
            if (count[i] == n) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        total_arrays = len(nums)
        freq = {}
        for arr in nums:
            for x in arr:
                freq[x] = freq.get(x, 0) + 1
        result = [x for x, cnt in freq.items() if cnt == total_arrays]
        result.sort()
        return result
```

## Python3

```python
from typing import List
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        total_arrays = len(nums)
        freq = {}
        for arr in nums:
            for x in arr:
                freq[x] = freq.get(x, 0) + 1
        result = [x for x, cnt in freq.items() if cnt == total_arrays]
        result.sort()
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    int count[1001] = {0};
    
    for (int i = 0; i < numsSize; ++i) {
        int len = numsColSize[i];
        for (int j = 0; j < len; ++j) {
            int val = nums[i][j];
            count[val]++;
        }
    }
    
    int* res = (int*)malloc(sizeof(int) * 1000);
    int idx = 0;
    for (int v = 1; v <= 1000; ++v) {
        if (count[v] == numsSize) {
            res[idx++] = v;
        }
    }
    
    *returnSize = idx;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> Intersection(int[][] nums)
    {
        int n = nums.Length;
        int[] count = new int[1001]; // values are in range [1, 1000]

        foreach (var arr in nums)
        {
            foreach (int x in arr)
            {
                count[x]++;
            }
        }

        List<int> result = new List<int>();
        for (int i = 1; i <= 1000; i++)
        {
            if (count[i] == n)
                result.Add(i);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var intersection = function(nums) {
    const countMap = new Map();
    const totalArrays = nums.length;
    
    for (const arr of nums) {
        for (const num of arr) {
            countMap.set(num, (countMap.get(num) || 0) + 1);
        }
    }
    
    const result = [];
    for (const [num, cnt] of countMap.entries()) {
        if (cnt === totalArrays) result.push(num);
    }
    
    result.sort((a, b) => a - b);
    return result;
};
```

## Typescript

```typescript
function intersection(nums: number[][]): number[] {
    const count = new Map<number, number>();
    const totalArrays = nums.length;
    for (const arr of nums) {
        for (const num of arr) {
            count.set(num, (count.get(num) ?? 0) + 1);
        }
    }
    const result: number[] = [];
    for (const [num, cnt] of count.entries()) {
        if (cnt === totalArrays) {
            result.push(num);
        }
    }
    result.sort((a, b) => a - b);
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer[]
     */
    function intersection($nums) {
        $count = [];
        $totalArrays = count($nums);
        foreach ($nums as $arr) {
            foreach ($arr as $num) {
                if (!isset($count[$num])) {
                    $count[$num] = 0;
                }
                $count[$num]++;
            }
        }
        $result = [];
        foreach ($count as $num => $freq) {
            if ($freq === $totalArrays) {
                $result[] = (int)$num;
            }
        }
        sort($result, SORT_NUMERIC);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func intersection(_ nums: [[Int]]) -> [Int] {
        var count = [Int: Int]()
        let totalArrays = nums.count
        
        for array in nums {
            for num in array {
                count[num, default: 0] += 1
            }
        }
        
        var result = [Int]()
        for (num, freq) in count where freq == totalArrays {
            result.append(num)
        }
        
        return result.sorted()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun intersection(nums: Array<IntArray>): List<Int> {
        val n = nums.size
        val freq = IntArray(1001)
        for (arr in nums) {
            for (v in arr) {
                freq[v]++
            }
        }
        val result = mutableListOf<Int>()
        for (i in 1..1000) {
            if (freq[i] == n) result.add(i)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> intersection(List<List<int>> nums) {
    int n = nums.length;
    const int maxVal = 1000;
    List<int> count = List.filled(maxVal + 1, 0);
    for (var arr in nums) {
      for (int v in arr) {
        count[v]++;
      }
    }
    List<int> result = [];
    for (int v = 1; v <= maxVal; v++) {
      if (count[v] == n) result.add(v);
    }
    return result;
  }
}
```

## Golang

```go
package main

import "sort"

func intersection(nums [][]int) []int {
	count := make(map[int]int)
	total := len(nums)

	for _, arr := range nums {
		for _, v := range arr {
			count[v]++
		}
	}

	res := make([]int, 0)
	for k, c := range count {
		if c == total {
			res = append(res, k)
		}
	}
	sort.Ints(res)
	return res
}
```

## Ruby

```ruby
def intersection(nums)
  counts = Hash.new(0)
  total = nums.size
  nums.each { |arr| arr.each { |v| counts[v] += 1 } }
  result = []
  counts.each { |k, v| result << k if v == total }
  result.sort
end
```

## Scala

```scala
object Solution {
    def intersection(nums: Array[Array[Int]]): List[Int] = {
        val n = nums.length
        val freq = new Array[Int](1001)
        for (arr <- nums; v <- arr) {
            freq(v) += 1
        }
        val result = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 1 to 1000) {
            if (freq(i) == n) result += i
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut cnt = vec![0i32; 1001];
        for arr in &nums {
            for &v in arr {
                cnt[v as usize] += 1;
            }
        }
        let mut res = Vec::new();
        for i in 1..=1000 {
            if cnt[i] == n {
                res.push(i as i32);
            }
        }
        res
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (intersection nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (if (null? nums)
      '()
      (let ((common
              (foldl (lambda (lst acc)
                       (set-intersect acc (list->set lst)))
                     (list->set (car nums))
                     (cdr nums))))
        (sort (set->list common) <))))
```

## Erlang

```erlang
-module(solution).
-export([intersection/1]).

-spec intersection(Nums :: [[integer()]]) -> [integer()].
intersection(Nums) ->
    N = length(Nums),
    CountMap = lists:foldl(fun(Sub, Acc) -> add_counts(Sub, Acc) end, #{}, Nums),
    Result = [K || {K, V} <- maps:to_list(CountMap), V == N],
    lists:sort(Result).

add_counts([], Map) ->
    Map;
add_counts([H|T], Map) ->
    NewMap = maps:update_with(H,
                              fun(C) -> C + 1 end,
                              1,
                              Map),
    add_counts(T, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec intersection(nums :: [[integer]]) :: [integer]
  def intersection(nums) do
    total = length(nums)

    freq =
      Enum.reduce(nums, %{}, fn arr, acc ->
        Enum.reduce(arr, acc, fn x, a ->
          Map.update(a, x, 1, &(&1 + 1))
        end)
      end)

    freq
    |> Enum.filter(fn {_k, v} -> v == total end)
    |> Enum.map(fn {k, _v} -> k end)
    |> Enum.sort()
  end
end
```
