# 0888. Fair Candy Swap

## Cpp

```cpp
class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        long long sumA = 0, sumB = 0;
        for (int x : aliceSizes) sumA += x;
        for (int y : bobSizes) sumB += y;
        long long delta = (sumA - sumB) / 2; // guaranteed integer
        
        unordered_set<int> bobSet(bobSizes.begin(), bobSizes.end());
        for (int x : aliceSizes) {
            int y = static_cast<int>(x - delta);
            if (bobSet.count(y)) {
                return {x, y};
            }
        }
        return {}; // should never reach here as per problem guarantee
    }
};
```

## Java

```java
class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        long sumA = 0, sumB = 0;
        for (int a : aliceSizes) sumA += a;
        for (int b : bobSizes) sumB += b;
        int delta = (int)((sumA - sumB) / 2);
        java.util.HashSet<Integer> bobSet = new java.util.HashSet<>();
        for (int b : bobSizes) bobSet.add(b);
        for (int a : aliceSizes) {
            int target = a - delta;
            if (bobSet.contains(target)) {
                return new int[]{a, target};
            }
        }
        return new int[0]; // guaranteed to find a solution
    }
}
```

## Python

```python
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        # Alice needs to give away (sum_a - sum_b) / 2 more candies than she receives
        diff = (sum_a - sum_b) // 2
        bob_set = set(bobSizes)
        for a in aliceSizes:
            b = a - diff
            if b in bob_set:
                return [a, b]
```

## Python3

```python
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumA - sumB) // 2
        bob_set = set(bobSizes)
        for a in aliceSizes:
            b = a - diff
            if b in bob_set:
                return [a, b]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

static int binary_search(int *arr, int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (arr[mid] == target) return 1;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fairCandySwap(int* aliceSizes, int aliceSizesSize, int* bobSizes, int bobSizesSize, int* returnSize) {
    long sumA = 0, sumB = 0;
    for (int i = 0; i < aliceSizesSize; ++i) sumA += aliceSizes[i];
    for (int i = 0; i < bobSizesSize; ++i) sumB += bobSizes[i];

    int diff = (int)((sumA - sumB) / 2);   // x - y must equal diff

    qsort(bobSizes, bobSizesSize, sizeof(int), cmp_int);

    for (int i = 0; i < aliceSizesSize; ++i) {
        int x = aliceSizes[i];
        int y = x - diff;
        if (binary_search(bobSizes, bobSizesSize, y)) {
            int *res = (int *)malloc(2 * sizeof(int));
            res[0] = x;
            res[1] = y;
            *returnSize = 2;
            return res;
        }
    }

    // According to problem guarantees, this point is never reached.
    *returnSize = 0;
    return NULL;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] FairCandySwap(int[] aliceSizes, int[] bobSizes) {
        long sumA = 0, sumB = 0;
        foreach (int a in aliceSizes) sumA += a;
        foreach (int b in bobSizes) sumB += b;
        long diff = (sumA - sumB) / 2; // x - y should equal diff

        var bobSet = new HashSet<int>(bobSizes);
        foreach (int x in aliceSizes) {
            int y = (int)(x - diff);
            if (bobSet.Contains(y)) {
                return new int[] { x, y };
            }
        }
        // Problem guarantees a solution exists
        return new int[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} aliceSizes
 * @param {number[]} bobSizes
 * @return {number[]}
 */
var fairCandySwap = function(aliceSizes, bobSizes) {
    let sumA = 0, sumB = 0;
    for (let v of aliceSizes) sumA += v;
    for (let v of bobSizes) sumB += v;
    
    const delta = (sumA - sumB) / 2; // x - y = delta
    
    const bobSet = new Set(bobSizes);
    for (let x of aliceSizes) {
        const y = x - delta;
        if (bobSet.has(y)) {
            return [x, y];
        }
    }
    // According to problem constraints, this line is never reached.
    return [];
};
```

## Typescript

```typescript
function fairCandySwap(aliceSizes: number[], bobSizes: number[]): number[] {
    const sumA = aliceSizes.reduce((acc, val) => acc + val, 0);
    const sumB = bobSizes.reduce((acc, val) => acc + val, 0);
    const diff = (sumA - sumB) / 2;
    const bobSet = new Set<number>(bobSizes);
    for (const a of aliceSizes) {
        const b = a - diff;
        if (bobSet.has(b)) {
            return [a, b];
        }
    }
    return [];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $aliceSizes
     * @param Integer[] $bobSizes
     * @return Integer[]
     */
    function fairCandySwap($aliceSizes, $bobSizes) {
        $sumA = array_sum($aliceSizes);
        $sumB = array_sum($bobSizes);
        $diff = intdiv($sumA - $sumB, 2); // x - y should equal diff

        $bobSet = [];
        foreach ($bobSizes as $b) {
            $bobSet[$b] = true;
        }

        foreach ($aliceSizes as $a) {
            $target = $a - $diff; // y needed from Bob
            if (isset($bobSet[$target])) {
                return [$a, $target];
            }
        }

        return []; // guaranteed to find a solution before reaching here
    }
}
```

## Swift

```swift
class Solution {
    func fairCandySwap(_ aliceSizes: [Int], _ bobSizes: [Int]) -> [Int] {
        var sumA = 0
        for v in aliceSizes { sumA += v }
        var sumB = 0
        for v in bobSizes { sumB += v }
        let diff = (sumA - sumB) / 2
        let bobSet = Set(bobSizes)
        for x in aliceSizes {
            let y = x - diff
            if bobSet.contains(y) {
                return [x, y]
            }
        }
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fairCandySwap(aliceSizes: IntArray, bobSizes: IntArray): IntArray {
        var sumA = 0L
        for (v in aliceSizes) sumA += v
        var sumB = 0L
        for (v in bobSizes) sumB += v
        val diff = ((sumA - sumB) / 2).toInt()
        val bobSet = HashSet<Int>()
        for (v in bobSizes) bobSet.add(v)
        for (x in aliceSizes) {
            val y = x - diff
            if (bobSet.contains(y)) {
                return intArrayOf(x, y)
            }
        }
        return intArrayOf()
    }
}
```

## Dart

```dart
class Solution {
  List<int> fairCandySwap(List<int> aliceSizes, List<int> bobSizes) {
    int sumA = 0;
    for (var v in aliceSizes) sumA += v;
    int sumB = 0;
    for (var v in bobSizes) sumB += v;

    int diff = (sumA - sumB) ~/ 2; // x - y should equal diff

    final Set<int> bobSet = bobSizes.toSet();
    for (int x in aliceSizes) {
      int y = x - diff;
      if (bobSet.contains(y)) {
        return [x, y];
      }
    }
    return []; // guaranteed to find a solution
  }
}
```

## Golang

```go
func fairCandySwap(aliceSizes []int, bobSizes []int) []int {
    sumA, sumB := 0, 0
    for _, v := range aliceSizes {
        sumA += v
    }
    for _, v := range bobSizes {
        sumB += v
    }
    diff := (sumA - sumB) / 2

    bobSet := make(map[int]struct{}, len(bobSizes))
    for _, v := range bobSizes {
        bobSet[v] = struct{}{}
    }

    for _, x := range aliceSizes {
        y := x - diff
        if _, ok := bobSet[y]; ok {
            return []int{x, y}
        }
    }
    // According to problem statement, a solution always exists.
    return nil
}
```

## Ruby

```ruby
def fair_candy_swap(alice_sizes, bob_sizes)
  sum_a = alice_sizes.sum
  sum_b = bob_sizes.sum
  diff = (sum_a - sum_b) / 2
  bob_set = {}
  bob_sizes.each { |v| bob_set[v] = true }
  alice_sizes.each do |a|
    b = a - diff
    return [a, b] if bob_set.key?(b)
  end
end
```

## Scala

```scala
object Solution {
    def fairCandySwap(aliceSizes: Array[Int], bobSizes: Array[Int]): Array[Int] = {
        val sumA = aliceSizes.foldLeft(0L)(_ + _)
        val sumB = bobSizes.foldLeft(0L)(_ + _)
        val diff = ((sumA - sumB) / 2).toInt
        val bobSet = bobSizes.toSet
        for (a <- aliceSizes) {
            val b = a - diff
            if (bobSet.contains(b)) return Array(a, b)
        }
        Array.empty[Int] // guaranteed to find a solution before this point
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn fair_candy_swap(alice_sizes: Vec<i32>, bob_sizes: Vec<i32>) -> Vec<i32> {
        let sum_a: i64 = alice_sizes.iter().map(|&v| v as i64).sum();
        let sum_b: i64 = bob_sizes.iter().map(|&v| v as i64).sum();
        let diff = (sum_a - sum_b) / 2; // x - y = diff

        let bob_set: HashSet<i32> = bob_sizes.into_iter().collect();

        for &x in alice_sizes.iter() {
            let y_i64 = x as i64 - diff;
            if y_i64 >= i32::MIN as i64 && y_i64 <= i32::MAX as i64 {
                let y = y_i64 as i32;
                if bob_set.contains(&y) {
                    return vec![x, y];
                }
            }
        }
        Vec::new()
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (fair-candy-swap aliceSizes bobSizes)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((sumA (apply + aliceSizes))
         (sumB (apply + bobSizes))
         (diff (quotient (- sumA sumB) 2))
         (bobSet (list->set bobSizes)))
    (for/first ([a aliceSizes]
                #:when (set-member? bobSet (- a diff)))
      (list a (- a diff)))))
```

## Erlang

```erlang
-module(solution).
-export([fair_candy_swap/2]).

-spec fair_candy_swap(AliceSizes :: [integer()], BobSizes :: [integer()]) -> [integer()].
fair_candy_swap(AliceSizes, BobSizes) ->
    SumA = lists:sum(AliceSizes),
    SumB = lists:sum(BobSizes),
    DiffHalf = (SumA - SumB) div 2,
    BobSet = sets:from_list(BobSizes),
    find_pair(AliceSizes, DiffHalf, BobSet).

find_pair([], _, _) -> [];
find_pair([X|Rest], DiffHalf, BobSet) ->
    Y = X - DiffHalf,
    case sets:is_element(Y, BobSet) of
        true -> [X, Y];
        false -> find_pair(Rest, DiffHalf, BobSet)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec fair_candy_swap(alice_sizes :: [integer], bob_sizes :: [integer]) :: [integer]
  def fair_candy_swap(alice_sizes, bob_sizes) do
    sum_a = Enum.sum(alice_sizes)
    sum_b = Enum.sum(bob_sizes)
    delta = div(sum_a - sum_b, 2)

    bob_set = MapSet.new(bob_sizes)

    Enum.find_value(alice_sizes, fn x ->
      y = x - delta
      if MapSet.member?(bob_set, y), do: [x, y], else: nil
    end)
  end
end
```
