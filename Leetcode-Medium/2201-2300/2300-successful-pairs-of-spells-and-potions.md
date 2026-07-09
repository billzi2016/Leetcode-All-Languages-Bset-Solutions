# 2300. Successful Pairs of Spells and Potions

## Cpp

```cpp
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        int m = potions.size();
        vector<int> ans;
        ans.reserve(spells.size());
        for (int s : spells) {
            long long need = (success + s - 1) / s; // ceil division
            auto it = lower_bound(potions.begin(), potions.end(), need);
            ans.push_back(m - static_cast<int>(it - potions.begin()));
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        Arrays.sort(potions);
        int m = potions.length;
        int n = spells.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            long spell = spells[i];
            long need = (success + spell - 1) / spell; // ceil division
            int idx = lowerBound(potions, need);
            result[i] = m - idx;
        }
        return result;
    }

    private int lowerBound(int[] arr, long target) {
        int left = 0, right = arr.length;
        while (left < right) {
            int mid = (left + right) >>> 1;
            if ((long) arr[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        import bisect
        potions.sort()
        m = len(potions)
        res = []
        for s in spells:
            # minimum required potion strength
            need = (success + s - 1) // s  # ceil division
            idx = bisect.bisect_left(potions, need)
            res.append(m - idx)
        return res
```

## Python3

```python
class Solution:
    def successfulPairs(self, spells, potions, success):
        from bisect import bisect_left
        potions.sort()
        m = len(potions)
        res = []
        for s in spells:
            # minimum potion strength needed
            need = (success + s - 1) // s  # ceil division
            idx = bisect_left(potions, need)
            res.append(m - idx)
        return res
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* successfulPairs(int* spells, int spellsSize, int* potions, int potionsSize,
                     long long success, int* returnSize) {
    *returnSize = spellsSize;
    int *ans = (int *)malloc(sizeof(int) * spellsSize);
    if (!ans) return NULL;

    qsort(potions, potionsSize, sizeof(int), cmp_int);

    for (int i = 0; i < spellsSize; ++i) {
        long long s = spells[i];
        /* If even the strongest potion cannot reach success, answer is 0 */
        if (s * (long long)potions[potionsSize - 1] < success) {
            ans[i] = 0;
            continue;
        }
        /* Minimum required potion strength (ceil division) */
        long long need = (success + s - 1) / s;

        int lo = 0, hi = potionsSize;   // lower_bound search
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if ((long long)potions[mid] >= need)
                hi = mid;
            else
                lo = mid + 1;
        }
        ans[i] = potionsSize - lo;
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SuccessfulPairs(int[] spells, int[] potions, long success) {
        Array.Sort(potions);
        int m = potions.Length;
        int n = spells.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            long spell = spells[i];
            long need = (success + spell - 1) / spell; // ceil division
            int left = 0, right = m;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if ((long)potions[mid] >= need)
                    right = mid;
                else
                    left = mid + 1;
            }
            result[i] = m - left;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    potions.sort((a, b) => a - b);
    const m = potions.length;
    const result = new Array(spells.length);
    
    for (let i = 0; i < spells.length; i++) {
        const need = Math.ceil(success / spells[i]);
        let left = 0, right = m;
        while (left < right) {
            const mid = (left + right) >>> 1;
            if (potions[mid] < need) left = mid + 1;
            else right = mid;
        }
        result[i] = m - left;
    }
    
    return result;
};
```

## Typescript

```typescript
function successfulPairs(spells: number[], potions: number[], success: number): number[] {
    const sorted = potions.slice().sort((a, b) => a - b);
    const m = sorted.length;
    const result = new Array<number>(spells.length);
    for (let i = 0; i < spells.length; i++) {
        const need = Math.ceil(success / spells[i]);
        let left = 0, right = m;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (sorted[mid] >= need) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        result[i] = m - left;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $spells
     * @param Integer[] $potions
     * @param Integer $success
     * @return Integer[]
     */
    function successfulPairs($spells, $potions, $success) {
        sort($potions);
        $m = count($potions);
        $result = [];

        foreach ($spells as $s) {
            // Minimum potion strength needed: ceil(success / s)
            $need = intdiv($success + $s - 1, $s);

            // Binary search for first index with value >= need
            $l = 0;
            $r = $m; // exclusive upper bound
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($potions[$mid] >= $need) {
                    $r = $mid;
                } else {
                    $l = $mid + 1;
                }
            }

            $result[] = $m - $l; // number of potions from index l to end
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func successfulPairs(_ spells: [Int], _ potions: [Int], _ success: Int) -> [Int] {
        let m = potions.count
        var sortedPotions = potions.map { Int64($0) }.sorted()
        let target = Int64(success)
        var result = [Int]()
        result.reserveCapacity(spells.count)
        
        for spell in spells {
            let s = Int64(spell)
            // Minimum potion strength needed (ceil division)
            let need = (target + s - 1) / s
            
            // Binary search for lower bound
            var left = 0
            var right = m
            while left < right {
                let mid = (left + right) >> 1
                if sortedPotions[mid] >= need {
                    right = mid
                } else {
                    left = mid + 1
                }
            }
            result.append(m - left)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun successfulPairs(spells: IntArray, potions: IntArray, success: Long): IntArray {
        val sortedPotions = potions.sorted()
        val m = sortedPotions.size
        val result = IntArray(spells.size)
        for (i in spells.indices) {
            val spellVal = spells[i].toLong()
            var need = success / spellVal
            if (success % spellVal != 0L) need += 1
            var left = 0
            var right = m
            while (left < right) {
                val mid = (left + right) ushr 1
                if (sortedPotions[mid].toLong() >= need) {
                    right = mid
                } else {
                    left = mid + 1
                }
            }
            result[i] = m - left
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> successfulPairs(List<int> spells, List<int> potions, int success) {
    final sortedPotions = List<int>.from(potions);
    sortedPotions.sort();
    final m = sortedPotions.length;
    final result = List<int>.filled(spells.length, 0);
    for (int i = 0; i < spells.length; ++i) {
      int spell = spells[i];
      int need = (success + spell - 1) ~/ spell; // ceil division
      int idx = _lowerBound(sortedPotions, need);
      result[i] = m - idx;
    }
    return result;
  }

  int _lowerBound(List<int> arr, int target) {
    int left = 0, right = arr.length;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}
```

## Golang

```go
package main

import "sort"

func successfulPairs(spells []int, potions []int, success int64) []int {
	sort.Ints(potions)
	m := len(potions)
	ans := make([]int, len(spells))
	for i, s := range spells {
		need := (success + int64(s) - 1) / int64(s) // ceil division
		idx := sort.Search(m, func(j int) bool { return int64(potions[j]) >= need })
		ans[i] = m - idx
	}
	return ans
}
```

## Ruby

```ruby
def successful_pairs(spells, potions, success)
  potions.sort!
  m = potions.length
  spells.map do |s|
    need = (success + s - 1) / s
    idx = potions.bsearch_index { |x| x >= need } || m
    m - idx
  end
end
```

## Scala

```scala
object Solution {
    def successfulPairs(spells: Array[Int], potions: Array[Int], success: Long): Array[Int] = {
        val sortedPotions = potions.sorted
        val m = sortedPotions.length
        val result = new Array[Int](spells.length)
        for (i <- spells.indices) {
            val spellVal = spells(i).toLong
            val need = (success + spellVal - 1) / spellVal // ceil division
            var left = 0
            var right = m
            while (left < right) {
                val mid = (left + right) >>> 1
                if (sortedPotions(mid).toLong >= need) right = mid else left = mid + 1
            }
            result(i) = m - left
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let mut pots: Vec<i64> = potions.iter().map(|&x| x as i64).collect();
        pots.sort_unstable();
        let m = pots.len() as i64;
        let mut ans = Vec::with_capacity(spells.len());
        for &spell in spells.iter() {
            let s = spell as i64;
            // minimum potion strength needed so that spell * potion >= success
            let need = (success + s - 1) / s; // ceil division
            // lower bound binary search
            let mut l = 0usize;
            let mut r = pots.len();
            while l < r {
                let mid = (l + r) / 2;
                if pots[mid] < need {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            let count = m - l as i64;
            ans.push(count as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (successful-pairs spells potions success)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([sorted-potions (list->vector (sort potions <))]
         [m (vector-length sorted-potions)])
    (map
     (lambda (s)
       (define need
         (let ([q (quotient success s)]
               [r (remainder success s)])
           (if (= r 0) q (+ q 1))))
       (let loop ([lo 0] [hi m])
         (if (< lo hi)
             (let* ([mid (quotient (+ lo hi) 2)]
                    [val (vector-ref sorted-potions mid)])
               (if (>= val need)
                   (loop lo mid)
                   (loop (+ mid 1) hi)))
             (- m lo))))
     spells)))
```

## Erlang

```erlang
-module(solution).
-export([successful_pairs/3]).

-spec successful_pairs(Spells :: [integer()], Potions :: [integer()], Success :: integer()) -> [integer()].
successful_pairs(Spells, Potions, Success) ->
    Sorted = lists:sort(Potions),
    Tuple = list_to_tuple(Sorted),
    Len = tuple_size(Tuple),
    lists:map(fun(Spell) ->
        Needed = (Success + Spell - 1) div Spell,
        Pos = lower_bound(Tuple, 1, Len, Needed),
        if Pos =< Len -> Len - Pos + 1;
           true -> 0
        end
    end, Spells).

lower_bound(_Tuple, Low, High, _Target) when Low > High ->
    Low;
lower_bound(Tuple, Low, High, Target) ->
    Mid = (Low + High) div 2,
    case element(Mid, Tuple) >= Target of
        true -> lower_bound(Tuple, Low, Mid - 1, Target);
        false -> lower_bound(Tuple, Mid + 1, High, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec successful_pairs(spells :: [integer], potions :: [integer], success :: integer) :: [integer]
  def successful_pairs(spells, potions, success) do
    sorted = Enum.sort(potions) |> List.to_tuple()
    m = tuple_size(sorted)

    Enum.map(spells, fn spell ->
      needed = div(success + spell - 1, spell)
      idx = lower_bound(sorted, needed, 0, m)

      if idx == m, do: 0, else: m - idx
    end)
  end

  defp lower_bound(_arr, _target, low, high) when low >= high, do: low

  defp lower_bound(arr, target, low, high) do
    mid = div(low + high, 2)
    val = elem(arr, mid)

    if val < target do
      lower_bound(arr, target, mid + 1, high)
    else
      lower_bound(arr, target, low, mid)
    end
  end
end
```
