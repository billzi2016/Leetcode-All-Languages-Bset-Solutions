# 2164. Sort Even and Odd Indices Independently

## Cpp

```cpp
class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        vector<int> evens, odds;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (i % 2 == 0)
                evens.push_back(nums[i]);
            else
                odds.push_back(nums[i]);
        }
        sort(evens.begin(), evens.end());                 // non-decreasing
        sort(odds.rbegin(), odds.rend());                 // non-increasing
        
        int ei = 0, oi = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (i % 2 == 0)
                nums[i] = evens[ei++];
            else
                nums[i] = odds[oi++];
        }
        return nums;
    }
};
```

## Java

```java
class Solution {
    public int[] sortEvenOdd(int[] nums) {
        int n = nums.length;
        java.util.List<Integer> evens = new java.util.ArrayList<>();
        java.util.List<Integer> odds = new java.util.ArrayList<>();
        for (int i = 0; i < n; i++) {
            if ((i & 1) == 0) {
                evens.add(nums[i]);
            } else {
                odds.add(nums[i]);
            }
        }
        java.util.Collections.sort(evens);
        odds.sort(java.util.Collections.reverseOrder());
        int[] result = new int[n];
        int eIdx = 0, oIdx = 0;
        for (int i = 0; i < n; i++) {
            if ((i & 1) == 0) {
                result[i] = evens.get(eIdx++);
            } else {
                result[i] = odds.get(oIdx++);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = sorted(nums[0::2])
        odds = sorted(nums[1::2], reverse=True)
        res = []
        e_idx = o_idx = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(evens[e_idx])
                e_idx += 1
            else:
                res.append(odds[o_idx])
                o_idx += 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted([nums[i] for i in range(0, len(nums), 2)])
        odds = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)
        res = []
        e_idx = o_idx = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(evens[e_idx])
                e_idx += 1
            else:
                res.append(odds[o_idx])
                o_idx += 1
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
static int cmpAsc(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

static int cmpDesc(const void *a, const void *b) {
    return (*(int *)b) - (*(int *)a);
}

int* sortEvenOdd(int* nums, int numsSize, int* returnSize) {
    int *result = (int *)malloc(numsSize * sizeof(int));
    if (!result) return NULL;
    
    // Count even and odd positions
    int evCount = (numsSize + 1) / 2;          // indices 0,2,...
    int odCount = numsSize / 2;                // indices 1,3,...
    
    int *evens = (int *)malloc(evCount * sizeof(int));
    int *odds  = (int *)malloc(odCount * sizeof(int));
    if (!evens || !odds) {
        free(result);
        free(evens);
        free(odds);
        return NULL;
    }
    
    // Separate values
    int evIdx = 0, odIdx = 0;
    for (int i = 0; i < numsSize; ++i) {
        if ((i & 1) == 0)
            evens[evIdx++] = nums[i];
        else
            odds[odIdx++] = nums[i];
    }
    
    // Sort groups
    qsort(evens, evCount, sizeof(int), cmpAsc);
    qsort(odds, odCount, sizeof(int), cmpDesc);
    
    // Merge back
    evIdx = 0;
    odIdx = 0;
    for (int i = 0; i < numsSize; ++i) {
        if ((i & 1) == 0)
            result[i] = evens[evIdx++];
        else
            result[i] = odds[odIdx++];
    }
    
    free(evens);
    free(odds);
    
    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] SortEvenOdd(int[] nums) {
        List<int> even = new List<int>();
        List<int> odd = new List<int>();
        
        for (int i = 0; i < nums.Length; i++) {
            if ((i & 1) == 0)
                even.Add(nums[i]);
            else
                odd.Add(nums[i]);
        }
        
        even.Sort(); // non-decreasing
        odd.Sort((a, b) => b.CompareTo(a)); // non-increasing
        
        int e = 0, o = 0;
        for (int i = 0; i < nums.Length; i++) {
            if ((i & 1) == 0)
                nums[i] = even[e++];
            else
                nums[i] = odd[o++];
        }
        
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
var sortEvenOdd = function(nums) {
    const evens = [];
    const odds = [];
    
    for (let i = 0; i < nums.length; i++) {
        if ((i & 1) === 0) {
            evens.push(nums[i]);
        } else {
            odds.push(nums[i]);
        }
    }
    
    evens.sort((a, b) => a - b);
    odds.sort((a, b) => b - a);
    
    const result = new Array(nums.length);
    let eIdx = 0, oIdx = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if ((i & 1) === 0) {
            result[i] = evens[eIdx++];
        } else {
            result[i] = odds[oIdx++];
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function sortEvenOdd(nums: number[]): number[] {
    const evens: number[] = [];
    const odds: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) evens.push(nums[i]);
        else odds.push(nums[i]);
    }
    evens.sort((a, b) => a - b);
    odds.sort((a, b) => b - a);
    const result: number[] = new Array(nums.length);
    let e = 0, o = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) result[i] = evens[e++];
        else result[i] = odds[o++];
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortEvenOdd($nums) {
        $evens = [];
        $odds = [];

        foreach ($nums as $i => $val) {
            if ($i % 2 == 0) {
                $evens[] = $val;
            } else {
                $odds[] = $val;
            }
        }

        sort($evens);   // non-decreasing
        rsort($odds);   // non-increasing

        $eIdx = 0;
        $oIdx = 0;

        foreach ($nums as $i => $_) {
            if ($i % 2 == 0) {
                $nums[$i] = $evens[$eIdx++];
            } else {
                $nums[$i] = $odds[$oIdx++];
            }
        }

        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func sortEvenOdd(_ nums: [Int]) -> [Int] {
        var evenVals = [Int]()
        var oddVals = [Int]()
        for (i, v) in nums.enumerated() {
            if i % 2 == 0 {
                evenVals.append(v)
            } else {
                oddVals.append(v)
            }
        }
        evenVals.sort()
        oddVals.sort(by: >)
        var result = nums
        var eIdx = 0, oIdx = 0
        for i in 0..<nums.count {
            if i % 2 == 0 {
                result[i] = evenVals[eIdx]
                eIdx += 1
            } else {
                result[i] = oddVals[oIdx]
                oIdx += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortEvenOdd(nums: IntArray): IntArray {
        val even = mutableListOf<Int>()
        val odd = mutableListOf<Int>()
        for (i in nums.indices) {
            if (i % 2 == 0) even.add(nums[i]) else odd.add(nums[i])
        }
        even.sort()
        odd.sortDescending()
        var eIdx = 0
        var oIdx = 0
        for (i in nums.indices) {
            if (i % 2 == 0) {
                nums[i] = even[eIdx++]
            } else {
                nums[i] = odd[oIdx++]
            }
        }
        return nums
    }
}
```

## Dart

```dart
class Solution {
  List<int> sortEvenOdd(List<int> nums) {
    List<int> evens = [];
    List<int> odds = [];

    for (int i = 0; i < nums.length; i++) {
      if (i % 2 == 0) {
        evens.add(nums[i]);
      } else {
        odds.add(nums[i]);
      }
    }

    evens.sort(); // non-decreasing
    odds.sort((a, b) => b - a); // non-increasing

    int eIdx = 0, oIdx = 0;
    List<int> result = List.filled(nums.length, 0);

    for (int i = 0; i < nums.length; i++) {
      if (i % 2 == 0) {
        result[i] = evens[eIdx++];
      } else {
        result[i] = odds[oIdx++];
      }
    }

    return result;
  }
}
```

## Golang

```go
package main

import "sort"

func sortEvenOdd(nums []int) []int {
	evenVals := []int{}
	oddVals := []int{}
	for i, v := range nums {
		if i%2 == 0 {
			evenVals = append(evenVals, v)
		} else {
			oddVals = append(oddVals, v)
		}
	}
	sort.Ints(evenVals)
	sort.Sort(sort.Reverse(sort.IntSlice(oddVals)))

	ei, oi := 0, 0
	for i := range nums {
		if i%2 == 0 {
			nums[i] = evenVals[ei]
			ei++
		} else {
			nums[i] = oddVals[oi]
			oi++
		}
	}
	return nums
}
```

## Ruby

```ruby
def sort_even_odd(nums)
  evens = []
  odds = []
  nums.each_with_index do |val, idx|
    if idx.even?
      evens << val
    else
      odds << val
    end
  end
  evens.sort!
  odds.sort!.reverse!
  e_idx = 0
  o_idx = 0
  result = Array.new(nums.size)
  nums.each_index do |i|
    if i.even?
      result[i] = evens[e_idx]
      e_idx += 1
    else
      result[i] = odds[o_idx]
      o_idx += 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def sortEvenOdd(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val evens = (0 until n by 2).map(i => nums(i)).sorted
        val odds = (1 until n by 2).map(i => nums(i)).sorted(Ordering[Int].reverse)
        val result = new Array[Int](n)
        var eIdx = 0
        var oIdx = 0
        for (i <- 0 until n) {
            if ((i & 1) == 0) {
                result(i) = evens(eIdx)
                eIdx += 1
            } else {
                result(i) = odds(oIdx)
                oIdx += 1
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_even_odd(nums: Vec<i32>) -> Vec<i32> {
        let mut evens = Vec::new();
        let mut odds = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if i % 2 == 0 {
                evens.push(v);
            } else {
                odds.push(v);
            }
        }
        evens.sort(); // non-decreasing
        odds.sort_by(|a, b| b.cmp(a)); // non-increasing

        let mut result = vec![0; nums.len()];
        let (mut e_idx, mut o_idx) = (0usize, 0usize);
        for i in 0..nums.len() {
            if i % 2 == 0 {
                result[i] = evens[e_idx];
                e_idx += 1;
            } else {
                result[i] = odds[o_idx];
                o_idx += 1;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (sort-even-odd nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((len (length nums))
         (indexed (map cons (range len) nums))
         (evens (filter (lambda (p) (even? (car p))) indexed))
         (odds (filter (lambda (p) (odd? (car p))) indexed))
         (sorted-evens (sort (map cdr evens) <))
         (sorted-odds (sort (map cdr odds) >)))
    (let loop ((i 0) (e sorted-evens) (o sorted-odds) (acc '()))
      (if (= i len)
          (reverse acc)
          (if (even? i)
              (loop (+ i 1) (cdr e) o (cons (car e) acc))
              (loop (+ i 1) e (cdr o) (cons (car o) acc)))))))
```

## Erlang

```erlang
-spec sort_even_odd(Nums :: [integer()]) -> [integer()].
sort_even_odd(Nums) ->
    Indexed = lists:zip(lists:seq(0, length(Nums) - 1), Nums),
    Evens = [Val || {Idx, Val} <- Indexed, Idx rem 2 == 0],
    Odds = [Val || {Idx, Val} <- Indexed, Idx rem 2 == 1],
    SortedEvens = lists:sort(Evens),
    SortedOddsDesc = lists:reverse(lists:sort(Odds)),
    build(0, length(Nums), SortedEvens, SortedOddsDesc, []).

build(Index, Len, Evens, Odds, Acc) when Index == Len ->
    lists:reverse(Acc);
build(Index, Len, [HE|TE], Odds, Acc) when Index rem 2 == 0 ->
    build(Index + 1, Len, TE, Odds, [HE | Acc]);
build(Index, Len, Evens, [HO|TO], Acc) ->
    build(Index + 1, Len, Evens, TO, [HO | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_even_odd(nums :: [integer]) :: [integer]
  def sort_even_odd(nums) do
    {evens, odds} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({[], []}, fn {val, idx}, {e_acc, o_acc} ->
        if rem(idx, 2) == 0 do
          {[val | e_acc], o_acc}
        else
          {e_acc, [val | o_acc]}
        end
      end)

    evens_sorted = evens |> Enum.sort()
    odds_sorted = odds |> Enum.sort(&>=/2)

    {result_rev, _, _} =
      0..(length(nums) - 1)
      |> Enum.reduce({[], evens_sorted, odds_sorted}, fn i, {acc, e_rest, o_rest} ->
        if rem(i, 2) == 0 do
          [h | t] = e_rest
          {[h | acc], t, o_rest}
        else
          [h | t] = o_rest
          {[h | acc], e_rest, t}
        end
      end)

    Enum.reverse(result_rev)
  end
end
```
