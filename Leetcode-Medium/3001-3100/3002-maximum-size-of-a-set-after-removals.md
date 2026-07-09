# 3002. Maximum Size of a Set After Removals

## Cpp

```cpp
class Solution {
public:
    int maximumSetSize(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int k = n / 2;
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        int a = set1.size();
        int b = set2.size();
        // compute common distinct count
        int common = 0;
        if (set1.size() < set2.size()) {
            for (int x : set1) if (set2.count(x)) ++common;
        } else {
            for (int x : set2) if (set1.count(x)) ++common;
        }
        int exclusive1 = a - common;
        int exclusive2 = b - common;
        int used1 = min(exclusive1, k);
        int used2 = min(exclusive2, k);
        int remainingSlots = 2 * k - used1 - used2;
        int total = used1 + used2 + min(common, remainingSlots);
        return total;
    }
};
```

## Java

```java
class Solution {
    public int maximumSetSize(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int cap = n / 2;

        java.util.HashSet<Integer> set1 = new java.util.HashSet<>();
        for (int x : nums1) set1.add(x);
        java.util.HashSet<Integer> set2 = new java.util.HashSet<>();
        for (int x : nums2) set2.add(x);

        int common = 0;
        for (int x : set1) {
            if (set2.contains(x)) common++;
        }

        int u1 = set1.size() - common;
        int u2 = set2.size() - common;

        int keepA = Math.min(u1, cap);
        int keepB = Math.min(u2, cap);

        int remainingSlots = (cap - keepA) + (cap - keepB);
        return keepA + keepB + Math.min(common, remainingSlots);
    }
}
```

## Python

```python
class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set1 = set(nums1)
        set2 = set(nums2)
        exclusive1 = len(set1 - set2)
        exclusive2 = len(set2 - set1)
        common = len(set1 & set2)
        k = len(nums1) // 2

        keep_excl1 = min(exclusive1, k)
        keep_excl2 = min(exclusive2, k)

        remaining_slots = max(0, k - exclusive1) + max(0, k - exclusive2)
        keep_common = min(common, remaining_slots)

        return keep_excl1 + keep_excl2 + keep_common
```

## Python3

```python
from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        common = len(s1 & s2)
        excl1 = len(s1) - common
        excl2 = len(s2) - common
        cap = len(nums1) // 2

        keep_excl1 = min(excl1, cap)
        keep_excl2 = min(excl2, cap)

        remaining = 2 * cap - keep_excl1 - keep_excl2
        return keep_excl1 + keep_excl2 + min(common, remaining)
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int maximumSetSize(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size;               // both sizes are equal
    int half = n / 2;

    // copy arrays to sort
    int *a = (int *)malloc(n * sizeof(int));
    int *b = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        a[i] = nums1[i];
        b[i] = nums2[i];
    }

    qsort(a, n, sizeof(int), cmp_int);
    qsort(b, n, sizeof(int), cmp_int);

    // extract unique elements
    int *u1 = (int *)malloc(n * sizeof(int));
    int *u2 = (int *)malloc(n * sizeof(int));
    int sz1 = 0, sz2 = 0;

    for (int i = 0; i < n; ++i) {
        if (i == 0 || a[i] != a[i - 1]) {
            u1[sz1++] = a[i];
        }
    }
    for (int i = 0; i < n; ++i) {
        if (i == 0 || b[i] != b[i - 1]) {
            u2[sz2++] = b[i];
        }
    }

    // count exclusive and common distinct values
    int only1 = 0, only2 = 0, both = 0;
    int i = 0, j = 0;
    while (i < sz1 && j < sz2) {
        if (u1[i] == u2[j]) {
            both++;
            i++; j++;
        } else if (u1[i] < u2[j]) {
            only1++;
            i++;
        } else {
            only2++;
            j++;
        }
    }
    while (i < sz1) { only1++; i++; }
    while (j < sz2) { only2++; j++; }

    // allocate slots
    int keep1 = only1 < half ? only1 : half;
    int keep2 = only2 < half ? only2 : half;

    int remaining = (half - keep1) + (half - keep2);
    int addCommon = both < remaining ? both : remaining;

    int result = keep1 + keep2 + addCommon;

    free(a);
    free(b);
    free(u1);
    free(u2);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumSetSize(int[] nums1, int[] nums2)
    {
        var set1 = new HashSet<int>(nums1);
        var set2 = new HashSet<int>(nums2);

        int cap = nums1.Length / 2;

        int exclusive1 = 0, exclusive2 = 0, common = 0;

        foreach (int x in set1)
        {
            if (set2.Contains(x))
                common++;
            else
                exclusive1++;
        }

        foreach (int x in set2)
        {
            if (!set1.Contains(x))
                exclusive2++;
        }

        int keepExclusive1 = Math.Min(exclusive1, cap);
        int keepExclusive2 = Math.Min(exclusive2, cap);

        int remainingSlots = (cap - keepExclusive1) + (cap - keepExclusive2);
        int addCommon = Math.Min(common, remainingSlots);

        return keepExclusive1 + keepExclusive2 + addCommon;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maximumSetSize = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    
    let both = 0;
    for (const v of set1) {
        if (set2.has(v)) both++;
    }
    
    const only1 = set1.size - both;
    const only2 = set2.size - both;
    const k = nums1.length >> 1; // n / 2
    
    const keepOnly1 = Math.min(only1, k);
    const keepOnly2 = Math.min(only2, k);
    
    const rem1 = k - keepOnly1;
    const rem2 = k - keepOnly2;
    
    const extra = Math.min(both, rem1 + rem2);
    
    return keepOnly1 + keepOnly2 + extra;
};
```

## Typescript

```typescript
function maximumSetSize(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const cap = n / 2;

    const set1 = new Set<number>(nums1);
    const set2 = new Set<number>(nums2);

    let exclusive1 = 0;
    let common = 0;

    for (const v of set1) {
        if (set2.has(v)) {
            common++;
        } else {
            exclusive1++;
        }
    }

    const exclusive2 = set2.size - common; // elements only in nums2

    const take1 = Math.min(exclusive1, cap);
    const take2 = Math.min(exclusive2, cap);

    const remaining = (cap - take1) + (cap - take2);
    const takeCommon = Math.min(common, remaining);

    return take1 + take2 + takeCommon;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maximumSetSize($nums1, $nums2) {
        $map1 = [];
        foreach ($nums1 as $v) {
            $map1[$v] = true;
        }
        $map2 = [];
        foreach ($nums2 as $v) {
            $map2[$v] = true;
        }

        $a = 0; // exclusive to nums1
        $b = 0; // exclusive to nums2
        $c = 0; // common to both

        foreach ($map1 as $val => $_) {
            if (isset($map2[$val])) {
                $c++;
            } else {
                $a++;
            }
        }

        foreach ($map2 as $val => $_) {
            if (!isset($map1[$val])) {
                $b++;
            }
        }

        $n = count($nums1);
        $k = intdiv($n, 2);

        $keepA = min($a, $k);
        $keepB = min($b, $k);
        $leftSlots = ($k - $keepA) + ($k - $keepB);
        $addCommon = min($c, $leftSlots);

        return $keepA + $keepB + $addCommon;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSetSize(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        let keep = n / 2
        
        var set1 = Set<Int>()
        for v in nums1 { set1.insert(v) }
        var set2 = Set<Int>()
        for v in nums2 { set2.insert(v) }
        
        var exclusive1 = 0
        var exclusive2 = 0
        var common = 0
        
        for v in set1 {
            if set2.contains(v) {
                common += 1
            } else {
                exclusive1 += 1
            }
        }
        for v in set2 where !set1.contains(v) {
            exclusive2 += 1
        }
        
        let take1 = min(exclusive1, keep)
        let take2 = min(exclusive2, keep)
        let remaining = (keep - take1) + (keep - take2)
        
        return take1 + take2 + min(common, remaining)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSetSize(nums1: IntArray, nums2: IntArray): Int {
        val set1 = HashSet<Int>()
        val set2 = HashSet<Int>()
        for (v in nums1) set1.add(v)
        for (v in nums2) set2.add(v)

        var exclusiveA = 0
        var common = 0
        for (v in set1) {
            if (set2.contains(v)) {
                common++
            } else {
                exclusiveA++
            }
        }

        var exclusiveB = 0
        for (v in set2) {
            if (!set1.contains(v)) exclusiveB++
        }

        val k = nums1.size / 2
        val takeA = minOf(exclusiveA, k)
        val takeB = minOf(exclusiveB, k)

        val rem1 = k - takeA
        val rem2 = k - takeB

        val additional = minOf(common, rem1 + rem2)

        return takeA + takeB + additional
    }
}
```

## Dart

```dart
class Solution {
  int maximumSetSize(List<int> nums1, List<int> nums2) {
    final set1 = <int>{...nums1};
    final set2 = <int>{...nums2};

    final common = set1.intersection(set2);
    final onlyInFirst = set1.difference(set2);
    final onlyInSecond = set2.difference(set1);

    int n = nums1.length;
    int half = n ~/ 2;

    int keepA = onlyInFirst.length < half ? onlyInFirst.length : half;
    int keepB = onlyInSecond.length < half ? onlyInSecond.length : half;

    int remaining = (half - keepA) + (half - keepB);
    int keepCommon = common.length < remaining ? common.length : remaining;

    return keepA + keepB + keepCommon;
  }
}
```

## Golang

```go
func maximumSetSize(nums1 []int, nums2 []int) int {
	set1 := make(map[int]struct{}, len(nums1))
	for _, v := range nums1 {
		set1[v] = struct{}{}
	}
	set2 := make(map[int]struct{}, len(nums2))
	for _, v := range nums2 {
		set2[v] = struct{}{}
	}

	only1, only2, common := 0, 0, 0
	for k := range set1 {
		if _, ok := set2[k]; ok {
			common++
		} else {
			only1++
		}
	}
	for k := range set2 {
		if _, ok := set1[k]; !ok {
			only2++
		}
	}

	n := len(nums1)
	half := n / 2

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	keptExclusive := min(only1, half) + min(only2, half)
	ans := keptExclusive + common
	if ans > n {
		ans = n
	}
	return ans
}
```

## Ruby

```ruby
def maximum_set_size(nums1, nums2)
  set1 = {}
  nums1.each { |v| set1[v] = true }
  set2 = {}
  nums2.each { |v| set2[v] = true }

  common = 0
  set1.each_key { |k| common += 1 if set2.key?(k) }

  exclusive1 = set1.size - common
  exclusive2 = set2.size - common

  cap = nums1.length / 2
  use1 = [exclusive1, cap].min
  use2 = [exclusive2, cap].min
  remaining = (cap - use1) + (cap - use2)

  use1 + use2 + [[common, remaining].min]
end
```

## Scala

```scala
object Solution {
    def maximumSetSize(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        val k = n / 2

        import scala.collection.mutable.HashSet

        val set1 = new HashSet[Int]()
        val set2 = new HashSet[Int]()

        for (v <- nums1) set1.add(v)
        for (v <- nums2) set2.add(v)

        var uniq1 = 0
        var uniq2 = 0
        var common = 0

        for (v <- set1) {
            if (set2.contains(v)) common += 1 else uniq1 += 1
        }
        for (v <- set2) {
            if (!set1.contains(v)) uniq2 += 1
        }

        val keepFrom1 = math.min(k, uniq1)
        val keepFrom2 = math.min(k, uniq2)

        val remainingSlots = (k - keepFrom1) + (k - keepFrom2)

        val addCommon = math.min(common, remainingSlots)

        keepFrom1 + keepFrom2 + addCommon
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_set_size(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let mut set1 = HashSet::new();
        for &x in &nums1 {
            set1.insert(x);
        }
        let mut set2 = HashSet::new();
        for &x in &nums2 {
            set2.insert(x);
        }

        let mut cnt1_excl = 0usize;
        let mut common = 0usize;
        for &v in set1.iter() {
            if set2.contains(&v) {
                common += 1;
            } else {
                cnt1_excl += 1;
            }
        }

        let mut cnt2_excl = 0usize;
        for &v in set2.iter() {
            if !set1.contains(&v) {
                cnt2_excl += 1;
            }
        }

        let k = nums1.len() / 2;

        let take1 = std::cmp::min(cnt1_excl, k);
        let take2 = std::cmp::min(cnt2_excl, k);
        let remaining = (k - take1) + (k - take2);
        let add_common = std::cmp::min(common, remaining);

        (take1 + take2 + add_common) as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-set-size nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((set1 (make-hash))
         (set2 (make-hash)))
    (for ([x nums1]) (hash-set! set1 x #t))
    (for ([x nums2]) (hash-set! set2 x #t))
    (define only1 0)
    (define only2 0)
    (define common 0)
    (for ([k (in-hash-keys set1)])
      (if (hash-has-key? set2 k)
          (set! common (+ common 1))
          (set! only1 (+ only1 1))))
    (for ([k (in-hash-keys set2)])
      (unless (hash-has-key? set1 k)
        (set! only2 (+ only2 1))))
    (define nHalf (quotient (length nums1) 2))
    (define keepOnly1 (min only1 nHalf))
    (define keepOnly2 (min only2 nHalf))
    (define rem (+ (- nHalf keepOnly1) (- nHalf keepOnly2)))
    (+ keepOnly1 keepOnly2 (min common rem))))
```

## Erlang

```erlang
-spec maximum_set_size(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
maximum_set_size(Nums1, Nums2) ->
    N = length(Nums1),
    Half = N div 2,
    Map1 = build_map(Nums1),
    Map2 = build_map(Nums2),
    {A, B, C} = count_distinct(Map1, Map2),
    KeepA = erlang:min(A, Half),
    KeepB = erlang:min(B, Half),
    Remaining = N - KeepA - KeepB,
    KeepA + KeepB + erlang:min(C, Remaining).

build_map(List) ->
    lists:foldl(fun(X, Acc) -> maps:put(X, true, Acc) end, #{}, List).

count_distinct(Map1, Map2) ->
    Keys1 = maps:keys(Map1),
    {A, C} = count_a_c(Keys1, Map2, 0, 0),
    Keys2 = maps:keys(Map2),
    B = count_b(Keys2, Map1, 0),
    {A, B, C}.

count_a_c([], _Map2, A, C) ->
    {A, C};
count_a_c([K | Rest], Map2, A, C) ->
    case maps:is_key(K, Map2) of
        true -> count_a_c(Rest, Map2, A, C + 1);
        false -> count_a_c(Rest, Map2, A + 1, C)
    end.

count_b([], _Map1, B) ->
    B;
count_b([K | Rest], Map1, B) ->
    case maps:is_key(K, Map1) of
        true -> count_b(Rest, Map1, B);
        false -> count_b(Rest, Map1, B + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_set_size(nums1 :: [integer], nums2 :: [integer]) :: integer
  def maximum_set_size(nums1, nums2) do
    n = length(nums1)
    k = div(n, 2)

    set1 = MapSet.new(nums1)
    set2 = MapSet.new(nums2)

    only1 = MapSet.difference(set1, set2) |> MapSet.size()
    only2 = MapSet.difference(set2, set1) |> MapSet.size()
    common = MapSet.intersection(set1, set2) |> MapSet.size()

    take_a = min(only1, k)
    take_b = min(only2, k)

    remaining = 2 * k - take_a - take_b
    take_a + take_b + min(common, remaining)
  end
end
```
