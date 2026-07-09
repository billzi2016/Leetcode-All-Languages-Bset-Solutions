# 3447. Assign Elements to Groups with Constraints

## Cpp

```cpp
class Solution {
public:
    vector<int> assignElements(vector<int>& groups, vector<int>& elements) {
        const int INF = 1e9;
        int maxG = 0;
        for (int g : groups) if (g > maxG) maxG = g;
        vector<int> firstIdx(maxG + 1, INF);
        for (int i = 0; i < (int)elements.size(); ++i) {
            int v = elements[i];
            if (v <= maxG && firstIdx[v] == INF) firstIdx[v] = i;
        }
        vector<int> ans;
        ans.reserve(groups.size());
        for (int g : groups) {
            int best = INF;
            for (int d = 1; (long long)d * d <= g; ++d) {
                if (g % d == 0) {
                    int d2 = g / d;
                    if (firstIdx[d] != INF) best = min(best, firstIdx[d]);
                    if (d2 != d && firstIdx[d2] != INF) best = min(best, firstIdx[d2]);
                }
            }
            ans.push_back(best == INF ? -1 : best);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] assignElements(int[] groups, int[] elements) {
        int maxGroup = 0;
        for (int g : groups) {
            if (g > maxGroup) maxGroup = g;
        }
        final int INF = Integer.MAX_VALUE;
        int limit = Math.max(maxGroup, 100000) + 1; // constraints up to 1e5
        int[] minIdx = new int[limit];
        Arrays.fill(minIdx, INF);
        for (int i = 0; i < elements.length; i++) {
            int val = elements[i];
            if (val < limit && i < minIdx[val]) {
                minIdx[val] = i;
            }
        }

        int[] bestIdx = new int[maxGroup + 1];
        Arrays.fill(bestIdx, INF);
        for (int v = 1; v <= maxGroup; v++) {
            int idx = minIdx[v];
            if (idx == INF) continue;
            for (int mult = v; mult <= maxGroup; mult += v) {
                if (idx < bestIdx[mult]) {
                    bestIdx[mult] = idx;
                }
            }
        }

        int[] res = new int[groups.length];
        for (int i = 0; i < groups.length; i++) {
            int idx = bestIdx[groups[i]];
            res[i] = (idx == INF) ? -1 : idx;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        n = len(groups)
        ans = [-1] * n
        # map group size to list of indices needing assignment
        size_to_idxs = {}
        max_g = 0
        for i, g in enumerate(groups):
            size_to_idxs.setdefault(g, []).append(i)
            if g > max_g:
                max_g = g

        for j, v in enumerate(elements):
            if v == 0 or v > max_g:
                continue
            # iterate over multiples of v up to max_g
            mult = v
            while mult <= max_g:
                if mult in size_to_idxs:
                    for idx in size_to_idxs[mult]:
                        ans[idx] = j
                    del size_to_idxs[mult]
                mult += v

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        if not groups:
            return []
        max_group = max(groups)
        max_elem = max(elements) if elements else 0
        INF = len(elements) + 5

        # smallest index for each element value
        min_idx = [INF] * (max_elem + 1)
        for idx, val in enumerate(elements):
            if idx < min_idx[val]:
                min_idx[val] = idx

        best_idx = [INF] * (max_group + 1)

        # sieve-like propagation of minimal indices to multiples
        for v in range(1, max_elem + 1):
            idx = min_idx[v]
            if idx == INF:
                continue
            step = v
            for mult in range(step, max_group + 1, step):
                if idx < best_idx[mult]:
                    best_idx[mult] = idx

        return [best_idx[g] if best_idx[g] != INF else -1 for g in groups]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int* assignElements(int* groups, int groupsSize, int* elements, int elementsSize, int* returnSize) {
    int maxVal = 0;
    for (int i = 0; i < groupsSize; ++i)
        if (groups[i] > maxVal) maxVal = groups[i];
    for (int i = 0; i < elementsSize; ++i)
        if (elements[i] > maxVal) maxVal = elements[i];

    int *minIdx = (int*)malloc((maxVal + 1) * sizeof(int));
    for (int i = 0; i <= maxVal; ++i) minIdx[i] = INT_MAX;

    for (int i = 0; i < elementsSize; ++i) {
        int v = elements[i];
        if (i < minIdx[v]) minIdx[v] = i;
    }

    int *ans = (int*)malloc(groupsSize * sizeof(int));
    for (int i = 0; i < groupsSize; ++i) {
        int g = groups[i];
        int best = INT_MAX;
        for (int d = 1; d * d <= g; ++d) {
            if (g % d == 0) {
                int v1 = d, v2 = g / d;
                if (minIdx[v1] < best) best = minIdx[v1];
                if (v2 != v1 && minIdx[v2] < best) best = minIdx[v2];
            }
        }
        ans[i] = (best == INT_MAX) ? -1 : best;
    }

    free(minIdx);
    *returnSize = groupsSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] AssignElements(int[] groups, int[] elements)
    {
        int maxVal = 0;
        foreach (int g in groups) if (g > maxVal) maxVal = g;
        foreach (int e in elements) if (e > maxVal) maxVal = e;

        int[] minIdx = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) minIdx[i] = -1;

        for (int i = 0; i < elements.Length; i++)
        {
            int v = elements[i];
            if (minIdx[v] == -1 || i < minIdx[v]) minIdx[v] = i;
        }

        int[] result = new int[groups.Length];

        for (int i = 0; i < groups.Length; i++)
        {
            int g = groups[i];
            int best = -1;
            int limit = (int)Math.Sqrt(g);
            for (int d = 1; d <= limit; d++)
            {
                if (g % d != 0) continue;

                int idx1 = minIdx[d];
                if (idx1 != -1 && (best == -1 || idx1 < best)) best = idx1;

                int other = g / d;
                if (other != d)
                {
                    int idx2 = minIdx[other];
                    if (idx2 != -1 && (best == -1 || idx2 < best)) best = idx2;
                }
            }
            result[i] = best;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} groups
 * @param {number[]} elements
 * @return {number[]}
 */
var assignElements = function(groups, elements) {
    const maxVal = Math.max(
        ...groups,
        ...elements
    );
    const minIdx = new Int32Array(maxVal + 1);
    for (let i = 0; i <= maxVal; ++i) minIdx[i] = -1;
    
    for (let i = 0; i < elements.length; ++i) {
        const v = elements[i];
        if (minIdx[v] === -1 || i < minIdx[v]) {
            minIdx[v] = i;
        }
    }
    
    const res = new Array(groups.length);
    for (let i = 0; i < groups.length; ++i) {
        const g = groups[i];
        let best = Number.MAX_SAFE_INTEGER;
        for (let d = 1; d * d <= g; ++d) {
            if (g % d === 0) {
                const idx1 = minIdx[d];
                if (idx1 !== -1 && idx1 < best) best = idx1;
                const other = g / d;
                if (other !== d) {
                    const idx2 = minIdx[other];
                    if (idx2 !== -1 && idx2 < best) best = idx2;
                }
            }
        }
        res[i] = best === Number.MAX_SAFE_INTEGER ? -1 : best;
    }
    return res;
};
```

## Typescript

```typescript
function assignElements(groups: number[], elements: number[]): number[] {
    const maxGroup = Math.max(...groups);
    const maxElement = Math.max(...elements);
    const size = Math.max(maxGroup, maxElement) + 1;
    const firstIdx = new Int32Array(size);
    for (let i = 0; i < size; i++) firstIdx[i] = -1;
    for (let i = 0; i < elements.length; i++) {
        const v = elements[i];
        if (firstIdx[v] === -1) firstIdx[v] = i;
    }
    const res: number[] = new Array(groups.length);
    for (let i = 0; i < groups.length; i++) {
        const g = groups[i];
        let best = Number.MAX_SAFE_INTEGER;
        const limit = Math.floor(Math.sqrt(g));
        for (let d = 1; d <= limit; d++) {
            if (g % d === 0) {
                const idx1 = firstIdx[d];
                if (idx1 !== -1 && idx1 < best) best = idx1;
                const other = g / d;
                if (other !== d) {
                    const idx2 = firstIdx[other];
                    if (idx2 !== -1 && idx2 < best) best = idx2;
                }
            }
        }
        res[i] = best === Number.MAX_SAFE_INTEGER ? -1 : best;
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $groups
     * @param Integer[] $elements
     * @return Integer[]
     */
    function assignElements($groups, $elements) {
        $n = count($groups);
        $ans = array_fill(0, $n, -1);

        // Map group size to list of indices having that size
        $sizeMap = [];
        $maxGroup = 0;
        foreach ($groups as $idx => $g) {
            if (!isset($sizeMap[$g])) {
                $sizeMap[$g] = [];
            }
            $sizeMap[$g][] = $idx;
            if ($g > $maxGroup) $maxGroup = $g;
        }

        $mElements = count($elements);
        for ($j = 0; $j < $mElements; ++$j) {
            $val = $elements[$j];
            // iterate over multiples of val up to maxGroup
            for ($multiple = $val; $multiple <= $maxGroup; $multiple += $val) {
                if (isset($sizeMap[$multiple])) {
                    foreach ($sizeMap[$multiple] as $pos) {
                        if ($ans[$pos] === -1) {
                            $ans[$pos] = $j;
                        }
                    }
                    // All groups of this size are now assigned, remove to avoid future work
                    unset($sizeMap[$multiple]);
                }
            }
            // early exit if all groups have been assigned
            if (empty($sizeMap)) {
                break;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func assignElements(_ groups: [Int], _ elements: [Int]) -> [Int] {
        let maxGroup = groups.max() ?? 0
        let maxElem = elements.max() ?? 0
        let limit = max(maxGroup, maxElem)
        var minIdx = Array(repeating: -1, count: limit + 1)
        for (i, v) in elements.enumerated() {
            if minIdx[v] == -1 || i < minIdx[v] {
                minIdx[v] = i
            }
        }
        var result = [Int]()
        result.reserveCapacity(groups.count)
        for g in groups {
            var best = Int.max
            var d = 1
            while d * d <= g {
                if g % d == 0 {
                    let d1 = d
                    let d2 = g / d
                    let idx1 = minIdx[d1]
                    if idx1 != -1 && idx1 < best { best = idx1 }
                    if d2 != d1 {
                        let idx2 = minIdx[d2]
                        if idx2 != -1 && idx2 < best { best = idx2 }
                    }
                }
                d += 1
            }
            result.append(best == Int.max ? -1 : best)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun assignElements(groups: IntArray, elements: IntArray): IntArray {
        var maxV = 0
        for (v in groups) if (v > maxV) maxV = v
        for (v in elements) if (v > maxV) maxV = v

        val INF = Int.MAX_VALUE
        val minIdx = IntArray(maxV + 1) { INF }
        for (i in elements.indices) {
            val v = elements[i]
            if (minIdx[v] > i) minIdx[v] = i
        }

        val res = IntArray(groups.size)
        for (gi in groups.indices) {
            val g = groups[gi]
            var best = INF
            var d = 1
            while (d * d <= g) {
                if (g % d == 0) {
                    val other = g / d
                    val idx1 = minIdx[d]
                    if (idx1 < best) best = idx1
                    if (other != d) {
                        val idx2 = minIdx[other]
                        if (idx2 < best) best = idx2
                    }
                }
                d++
            }
            res[gi] = if (best == INF) -1 else best
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> assignElements(List<int> groups, List<int> elements) {
    const int INF = 1 << 30;
    int maxGroup = 0;
    for (int g in groups) if (g > maxGroup) maxGroup = g;
    int maxElem = 0;
    for (int e in elements) if (e > maxElem) maxElem = e;

    int limit = maxGroup > maxElem ? maxGroup : maxElem;
    List<int> minIdx = List.filled(limit + 1, INF);
    for (int i = 0; i < elements.length; ++i) {
      int val = elements[i];
      if (i < minIdx[val]) minIdx[val] = i;
    }

    List<int> bestIdx = List.filled(limit + 1, INF);
    for (int v = 1; v <= maxElem; ++v) {
      int idx = minIdx[v];
      if (idx == INF) continue;
      for (int m = v; m <= maxGroup; m += v) {
        if (idx < bestIdx[m]) bestIdx[m] = idx;
      }
    }

    List<int> result = List.filled(groups.length, -1);
    for (int i = 0; i < groups.length; ++i) {
      int g = groups[i];
      int ans = bestIdx[g];
      if (ans != INF) result[i] = ans;
    }
    return result;
  }
}
```

## Golang

```go
func assignElements(groups []int, elements []int) []int {
	const INF = int(1 << 30)
	maxVal := 0
	for _, v := range elements {
		if v > maxVal {
			maxVal = v
		}
	}
	minIdx := make([]int, maxVal+1)
	for i := range minIdx {
		minIdx[i] = INF
	}
	for i, v := range elements {
		if i < minIdx[v] {
			minIdx[v] = i
		}
	}

	ans := make([]int, len(groups))
	for i, g := range groups {
		best := INF
		for d := 1; d*d <= g; d++ {
			if g%d == 0 {
				if d <= maxVal && minIdx[d] < best {
					best = minIdx[d]
				}
				other := g / d
				if other != d && other <= maxVal && minIdx[other] < best {
					best = minIdx[other]
				}
			}
		}
		if best == INF {
			ans[i] = -1
		} else {
			ans[i] = best
		}
	}
	return ans
}
```

## Ruby

```ruby
def assign_elements(groups, elements)
  min_idx = {}
  elements.each_with_index do |v, i|
    if !min_idx.key?(v) || i < min_idx[v]
      min_idx[v] = i
    end
  end

  result = Array.new(groups.length, -1)

  groups.each_with_index do |g, gi|
    best = nil
    limit = Math.sqrt(g).to_i
    d = 1
    while d <= limit
      if g % d == 0
        idx = min_idx[d]
        if idx && (best.nil? || idx < best)
          best = idx
        end
        other = g / d
        if other != d
          idx2 = min_idx[other]
          if idx2 && (best.nil? || idx2 < best)
            best = idx2
          end
        end
      end
      d += 1
    end
    result[gi] = best.nil? ? -1 : best
  end

  result
end
```

## Scala

```scala
object Solution {
  def assignElements(groups: Array[Int], elements: Array[Int]): Array[Int] = {
    val n = groups.length
    val maxGroup = if (groups.isEmpty) 0 else groups.max
    val maxElem = if (elements.isEmpty) 0 else elements.max
    val maxVal = math.max(maxGroup, maxElem)

    // smallest index for each element value
    val minIdx = Array.fill(maxVal + 1)(Int.MaxValue)
    var i = 0
    while (i < elements.length) {
      val v = elements(i)
      if (i < minIdx(v)) minIdx(v) = i
      i += 1
    }

    // group indices by their size
    import scala.collection.mutable.ArrayBuffer
    val groupsBySize = Array.fill(maxVal + 1)(new ArrayBuffer[Int]())
    var gi = 0
    while (gi < n) {
      val sz = groups(gi)
      groupsBySize(sz) += gi
      gi += 1
    }

    // answer array initialized to INF
    val ans = Array.fill(n)(Int.MaxValue)

    var d = 1
    while (d <= maxVal) {
      val idx = minIdx(d)
      if (idx != Int.MaxValue) {
        var mult = d
        while (mult <= maxVal) {
          val buf = groupsBySize(mult)
          var j = 0
          while (j < buf.length) {
            val gIdx = buf(j)
            if (ans(gIdx) > idx) ans(gIdx) = idx
            j += 1
          }
          mult += d
        }
      }
      d += 1
    }

    // replace INF with -1
    var k = 0
    while (k < n) {
      if (ans(k) == Int.MaxValue) ans(k) = -1
      k += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn assign_elements(groups: Vec<i32>, elements: Vec<i32>) -> Vec<i32> {
        // Find maximum group value to size the lookup array
        let max_group = *groups.iter().max().unwrap() as usize;
        // For each possible element value store the smallest index where it appears
        let mut min_idx = vec![-1i32; max_group + 1];
        for (i, &val) in elements.iter().enumerate() {
            let v = val as usize;
            if v <= max_group {
                if min_idx[v] == -1 || i as i32 < min_idx[v] {
                    min_idx[v] = i as i32;
                }
            }
        }

        // For each group, find the smallest index of an element that divides it
        let mut result = Vec::with_capacity(groups.len());
        for &g in groups.iter() {
            let g_usize = g as usize;
            let mut best: i32 = -1;
            let limit = (g_usize as f64).sqrt() as usize;
            for d in 1..=limit {
                if g_usize % d == 0 {
                    // divisor d
                    let idx1 = min_idx[d];
                    if idx1 != -1 && (best == -1 || idx1 < best) {
                        best = idx1;
                    }
                    // paired divisor g/d
                    let other = g_usize / d;
                    if other != d {
                        let idx2 = min_idx[other];
                        if idx2 != -1 && (best == -1 || idx2 < best) {
                            best = idx2;
                        }
                    }
                }
            }
            result.push(best);
        }

        result
    }
}
```

## Racket

```racket
(define/contract (assign-elements groups elements)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((max-val (apply max (append groups elements)))
         (size (+ max-val 1))
         (inf (expt 2 30)) ; sufficiently large sentinel
         (min-idx (make-vector size inf)))
    ;; record smallest index for each element value
    (for ([elem elements] [i (in-naturals)])
      (let ((cur (vector-ref min-idx elem)))
        (when (< i cur)
          (vector-set! min-idx elem i))))
    ;; answer for every possible group value
    (define ans (make-vector size inf))
    (for ([v (in-range 1 size)])
      (let ((idx (vector-ref min-idx v)))
        (when (< idx inf)
          (for ([m (in-range v size v)])
            (let ((cur (vector-ref ans m)))
              (when (< idx cur)
                (vector-set! ans m idx)))))))
    ;; build result list
    (map (lambda (g)
           (let ((a (vector-ref ans g)))
             (if (< a inf) a -1)))
         groups)))
```

## Erlang

```erlang
-export([assign_elements/2]).
-spec assign_elements(Groups :: [integer()], Elements :: [integer()]) -> [integer()].
assign_elements(Groups, Elements) ->
    N = length(Groups),
    MaxG = case Groups of [] -> 0; _ -> lists:max(Groups) end,
    GroupsMap = build_groups_map(Groups, 0, #{}),
    MinIdxMap = build_min_idx_map(Elements, 0, #{}),
    AnsTuple = erlang:make_tuple(N, -1),
    FinalAnsTuple = maps:fold(
        fun(Value, Idx, Acc) ->
            process_multiples(Value, Idx, Value, MaxG, GroupsMap, Acc)
        end,
        AnsTuple,
        MinIdxMap
    ),
    tuple_to_list(FinalAnsTuple).

build_groups_map([], _Idx, Map) -> Map;
build_groups_map([H|T], Idx, Map) ->
    Updated = maps:update_with(
        H,
        fun(L) -> [Idx|L] end,
        [Idx],
        Map
    ),
    build_groups_map(T, Idx + 1, Updated).

build_min_idx_map([], _Idx, Map) -> Map;
build_min_idx_map([H|T], Idx, Map) ->
    case maps:find(H, Map) of
        {ok, Existing} when Existing =< Idx ->
            build_min_idx_map(T, Idx + 1, Map);
        _ ->
            NewMap = maps:put(H, Idx, Map),
            build_min_idx_map(T, Idx + 1, NewMap)
    end.

process_multiples(_Value, _Idx, Multiple, MaxG, _GroupsMap, Ans) when Multiple > MaxG -> Ans;
process_multiples(Value, Idx, Multiple, MaxG, GroupsMap, Ans) ->
    case maps:find(Multiple, GroupsMap) of
        {ok, Indices} ->
            NewAns = update_indices(Indices, Idx, Ans),
            process_multiples(Value, Idx, Multiple + Value, MaxG, GroupsMap, NewAns);
        error ->
            process_multiples(Value, Idx, Multiple + Value, MaxG, GroupsMap, Ans)
    end.

update_indices([], _Idx, Ans) -> Ans;
update_indices([Pos|Rest], Idx, Ans) ->
    Current = element(Pos + 1, Ans),
    NewAns = if
        Current == -1 orelse Idx < Current -> setelement(Pos + 1, Ans, Idx);
        true -> Ans
    end,
    update_indices(Rest, Idx, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec assign_elements(groups :: [integer], elements :: [integer]) :: [integer]
  def assign_elements(groups, elements) do
    max_group = Enum.max(groups)
    max_elem = Enum.max(elements)
    max_val = max(max_group, max_elem)
    inf = 1_000_000_0

    # minimal index for each element value
    min_idx_arr =
      :array.new(max_val + 1, default: inf)
      |> Enum.reduce(Enum.with_index(elements), fn {val, idx}, arr ->
        cur = :array.get(val, arr)

        if idx < cur do
          :array.set(val, idx, arr)
        else
          arr
        end
      end)

    # answer for each possible group size
    ans_arr =
      :array.new(max_group + 1, default: inf)
      |> Enum.reduce(1..max_val, fn v, acc ->
        cur = :array.get(v, min_idx_arr)

        if cur != inf do
          Enum.reduce(v..max_group//v, acc, fn m, a2 ->
            existing = :array.get(m, a2)
            new = if cur < existing, do: cur, else: existing
            :array.set(m, new, a2)
          end)
        else
          acc
        end
      end)

    Enum.map(groups, fn g ->
      idx = :array.get(g, ans_arr)

      if idx == inf, do: -1, else: idx
    end)
  end
end
```
