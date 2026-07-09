# 0870. Advantage Shuffle

## Cpp

```cpp
class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        multiset<int> ms(nums1.begin(), nums1.end());
        vector<int> ans(n);
        // indices sorted by descending nums2 values
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return nums2[a] > nums2[b];
        });
        for (int i : idx) {
            auto it = ms.upper_bound(nums2[i]);
            if (it != ms.end()) {
                ans[i] = *it;
                ms.erase(it);
            } else {
                ans[i] = *ms.begin();
                ms.erase(ms.begin());
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] sortedA = nums1.clone();
        java.util.Arrays.sort(sortedA);
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        java.util.Arrays.sort(idx, (i, j) -> Integer.compare(nums2[j], nums2[i])); // descending by nums2
        int lo = 0, hi = n - 1;
        int[] ans = new int[n];
        for (int i : idx) {
            if (sortedA[hi] > nums2[i]) {
                ans[i] = sortedA[hi--];
            } else {
                ans[i] = sortedA[lo++];
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        nums1.sort()
        # indices of nums2 sorted by descending values
        idx = sorted(range(n), key=lambda i: -nums2[i])
        res = [0] * n
        left, right = 0, n - 1
        for i in idx:
            if nums1[right] > nums2[i]:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left += 1
        return res
```

## Python3

```python
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        sorted_a = sorted(nums1)
        # indices of nums2 sorted by value
        order = sorted(range(n), key=lambda i: nums2[i])
        res = [0] * n
        left, right = 0, n - 1
        for i in reversed(order):
            if sorted_a[right] > nums2[i]:
                res[i] = sorted_a[right]
                right -= 1
            else:
                res[i] = sorted_a[left]
                left += 1
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int val;
    int idx;
} Pair;

/* comparator for integers (ascending) */
static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/* comparator for Pair by val descending */
static int cmp_pair_desc(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->val != pb->val)
        return (pb->val > pa->val) - (pb->val < pa->val);
    return (pa->idx > pb->idx) - (pa->idx < pb->idx);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* advantageCount(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int n = nums1Size;
    *returnSize = n;

    /* copy and sort nums1 */
    int *sortedA = (int *)malloc(n * sizeof(int));
    memcpy(sortedA, nums1, n * sizeof(int));
    qsort(sortedA, n, sizeof(int), cmp_int);

    /* create pairs for nums2 and sort descending by value */
    Pair *pairs = (Pair *)malloc(n * sizeof(Pair));
    for (int i = 0; i < n; ++i) {
        pairs[i].val = nums2[i];
        pairs[i].idx = i;
    }
    qsort(pairs, n, sizeof(Pair), cmp_pair_desc);

    int *result = (int *)malloc(n * sizeof(int));
    int low = 0, high = n - 1;

    for (int i = 0; i < n; ++i) {
        if (sortedA[high] > pairs[i].val) {
            result[pairs[i].idx] = sortedA[high];
            --high;
        } else {
            result[pairs[i].idx] = sortedA[low];
            ++low;
        }
    }

    free(sortedA);
    free(pairs);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Linq;

public class Solution {
    public int[] AdvantageCount(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        Array.Sort(nums1);
        int[] order = Enumerable.Range(0, n).ToArray();
        Array.Sort(order, (i, j) => nums2[j].CompareTo(nums2[i])); // descending by nums2 value

        int[] result = new int[n];
        int left = 0, right = n - 1;

        foreach (int idx in order) {
            if (nums1[right] > nums2[idx]) {
                result[idx] = nums1[right];
                right--;
            } else {
                result[idx] = nums1[left];
                left++;
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
 * @return {number[]}
 */
var advantageCount = function(nums1, nums2) {
    const n = nums1.length;
    // sort nums1 ascending
    const sortedA = nums1.slice().sort((a, b) => a - b);
    // pair each element in nums2 with its original index and sort descending by value
    const pairedB = nums2.map((val, idx) => ({ val, idx }));
    pairedB.sort((a, b) => b.val - a.val);
    
    const result = new Array(n);
    let left = 0;
    let right = n - 1;
    
    for (const { val, idx } of pairedB) {
        if (sortedA[right] > val) {
            result[idx] = sortedA[right];
            right--;
        } else {
            result[idx] = sortedA[left];
            left++;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function advantageCount(nums1: number[], nums2: number[]): number[] {
    const n = nums1.length;
    const sortedA = [...nums1].sort((a, b) => a - b);
    const bPairs = nums2.map((v, i) => ({ value: v, idx: i }));
    bPairs.sort((a, b) => b.value - a.value); // descending by value

    let left = 0;
    let right = n - 1;
    const result = new Array<number>(n);

    for (const { value, idx } of bPairs) {
        if (sortedA[right] > value) {
            result[idx] = sortedA[right];
            right--;
        } else {
            result[idx] = sortedA[left];
            left++;
        }
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
     * @return Integer[]
     */
    function advantageCount($nums1, $nums2) {
        $n = count($nums1);
        sort($nums1); // ascending

        // indices of nums2 sorted by value descending
        $order = range(0, $n - 1);
        usort($order, function ($i, $j) use ($nums2) {
            return $nums2[$j] <=> $nums2[$i];
        });

        $result = array_fill(0, $n, 0);
        $lo = 0;
        $hi = $n - 1;

        foreach ($order as $idx) {
            if ($nums1[$hi] > $nums2[$idx]) {
                $result[$idx] = $nums1[$hi];
                $hi--;
            } else {
                $result[$idx] = $nums1[$lo];
                $lo++;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func advantageCount(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let n = nums1.count
        var sortedA = nums1.sorted()
        var indexedB: [(value: Int, index: Int)] = []
        for (i, v) in nums2.enumerated() {
            indexedB.append((v, i))
        }
        indexedB.sort { $0.value > $1.value }  // descending by value
        
        var result = Array(repeating: 0, count: n)
        var left = 0
        var right = n - 1
        
        for pair in indexedB {
            if sortedA[right] > pair.value {
                result[pair.index] = sortedA[right]
                right -= 1
            } else {
                result[pair.index] = sortedA[left]
                left += 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun advantageCount(nums1: IntArray, nums2: IntArray): IntArray {
        val n = nums1.size
        val sortedA = nums1.clone()
        java.util.Arrays.sort(sortedA)
        // indices of nums2 sorted by descending values
        val idx = (0 until n).sortedWith { i, j ->
            when {
                nums2[i] > nums2[j] -> -1
                nums2[i] < nums2[j] -> 1
                else -> 0
            }
        }
        var left = 0
        var right = n - 1
        val result = IntArray(n)
        for (i in idx) {
            if (sortedA[right] > nums2[i]) {
                result[i] = sortedA[right]
                right--
            } else {
                result[i] = sortedA[left]
                left++
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> advantageCount(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    List<int> sortedA = List.from(nums1);
    sortedA.sort(); // ascending

    // Pair each value in nums2 with its original index
    List<_Pair> bPairs = List.generate(
        n, (i) => _Pair(value: nums2[i], index: i));
    // Sort pairs by value descending
    bPairs.sort((a, b) => b.value.compareTo(a.value));

    List<int> result = List.filled(n, 0);
    int left = 0;
    int right = n - 1;

    for (var p in bPairs) {
      if (sortedA[right] > p.value) {
        result[p.index] = sortedA[right];
        right--;
      } else {
        result[p.index] = sortedA[left];
        left++;
      }
    }

    return result;
  }
}

class _Pair {
  final int value;
  final int index;
  _Pair({required this.value, required this.index});
}
```

## Golang

```go
import "sort"

func advantageCount(nums1 []int, nums2 []int) []int {
	n := len(nums1)
	a := make([]int, n)
	copy(a, nums1)
	sort.Ints(a)

	idx := make([]int, n)
	for i := 0; i < n; i++ {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool {
		return nums2[idx[i]] > nums2[idx[j]]
	})

	res := make([]int, n)
	left, right := 0, n-1
	for _, i := range idx {
		if a[right] > nums2[i] {
			res[i] = a[right]
			right--
		} else {
			res[i] = a[left]
			left++
		}
	}
	return res
}
```

## Ruby

```ruby
def advantage_count(nums1, nums2)
  n = nums1.length
  sorted_nums1 = nums1.sort
  # indices of nums2 sorted by descending value
  idxs = (0...n).to_a.sort_by { |i| -nums2[i] }

  result = Array.new(n)
  low = 0
  high = n - 1

  idxs.each do |i|
    if sorted_nums1[high] > nums2[i]
      result[i] = sorted_nums1[high]
      high -= 1
    else
      result[i] = sorted_nums1[low]
      low += 1
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    import java.util.TreeMap

    def advantageCount(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        val multiset = new TreeMap[Int, Int]()
        for (v <- nums1) {
            multiset.put(v, multiset.getOrDefault(v, 0) + 1)
        }

        val res = new Array[Int](nums2.length)

        def use(key: Int): Unit = {
            val cnt = multiset.get(key)
            if (cnt == 1) multiset.remove(key)
            else multiset.put(key, cnt - 1)
        }

        for (i <- nums2.indices) {
            val target = nums2(i)
            var chosen = multiset.higherKey(target)
            if (chosen == null) {
                chosen = multiset.firstKey()
            }
            res(i) = chosen
            use(chosen)
        }

        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn advantage_count(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let n = nums1.len();
        let mut a = nums1.clone();
        a.sort(); // ascending order

        // Pair each value in nums2 with its original index
        let mut b: Vec<(i32, usize)> = nums2.iter().cloned().enumerate().collect();
        // Sort descending by value to handle largest opponents first
        b.sort_by(|&(v1, _), &(v2, _)| v2.cmp(&v1));

        let mut result = vec![0; n];
        let (mut left, mut right) = (0usize, n - 1);

        for &(val, idx) in &b {
            if a[right] > val {
                result[idx] = a[right];
                // move to next smallest winning card
                right = right.saturating_sub(1);
            } else {
                // sacrifice the smallest remaining card
                result[idx] = a[left];
                left += 1;
            }
        }

        result
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (advantage-count nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums1))
         (sorted-a (list->vector (sort nums1 <))) ; ascending order
         (pairs (map-indexed (lambda (i v) (cons v i)) nums2)) ; (value . index)
         (sorted-pairs (sort pairs (lambda (p q) (> (car p) (car q))))) ; descending by value
         (result (make-vector n))
         (low 0)
         (high (- n 1)))
    (for ([pair sorted-pairs])
      (define b (car pair))
      (define idx (cdr pair))
      (if (> (vector-ref sorted-a high) b)
          (begin
            (vector-set! result idx (vector-ref sorted-a high))
            (set! high (- high 1)))
          (begin
            (vector-set! result idx (vector-ref sorted-a low))
            (set! low (+ low 1)))))
    (vector->list result)))
```

## Erlang

```erlang
-module(solution).
-export([advantage_count/2]).

-spec advantage_count(Nums1 :: [integer()], Nums2 :: [integer()]) -> [integer()].
advantage_count(Nums1, Nums2) ->
    N = length(Nums1),
    SortedA = lists:sort(Nums1),
    TupleA = list_to_tuple(SortedA),
    IndexedB = lists:zip(Nums2, lists:seq(0, N - 1)),
    BWithIdx = [{V, I} || {V, I} <- IndexedB],
    SortedBDesc = lists:sort(fun({V1, _}, {V2, _}) -> V1 > V2 end, BWithIdx),
    Assigned = assign(SortedBDesc, TupleA, 0, N - 1, []),
    SortedAssigned = lists:keysort(1, Assigned),
    [Val || {_Idx, Val} <- SortedAssigned].

assign([], _Tuple, _L, _R, Acc) ->
    Acc;
assign([{B, Idx} | Rest], Tuple, L, R, Acc) ->
    MaxVal = element(R + 1, Tuple),
    if
        MaxVal > B ->
            assign(Rest, Tuple, L, R - 1, [{Idx, MaxVal} | Acc]);
        true ->
            MinVal = element(L + 1, Tuple),
            assign(Rest, Tuple, L + 1, R, [{Idx, MinVal} | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec advantage_count(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def advantage_count(nums1, nums2) do
    n = length(nums1)
    a_tuple = List.to_tuple(Enum.sort(nums1))

    indexed_b =
      Enum.with_index(nums2)
      |> Enum.map(fn {v, i} -> {v, i} end)

    b_desc = Enum.sort_by(indexed_b, fn {v, _} -> -v end)

    {assign_map, _, _} =
      Enum.reduce(b_desc, {%{}, 0, n - 1}, fn {b_val, idx}, {res, left, right} ->
        if elem(a_tuple, right) > b_val do
          {Map.put(res, idx, elem(a_tuple, right)), left, right - 1}
        else
          {Map.put(res, idx, elem(a_tuple, left)), left + 1, right}
        end
      end)

    Enum.map(0..(n - 1), fn i -> Map.fetch!(assign_map, i) end)
  end
end
```
