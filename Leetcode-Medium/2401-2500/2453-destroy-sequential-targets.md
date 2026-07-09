# 2453. Destroy Sequential Targets

## Cpp

```cpp
class Solution {
public:
    int destroyTargets(vector<int>& nums, int space) {
        unordered_map<int, vector<int>> groups;
        groups.reserve(nums.size()*2);
        for (int x : nums) {
            int r = x % space;
            groups[r].push_back(x);
        }
        int bestCnt = -1;
        int ans = INT_MAX;
        for (auto& kv : groups) {
            auto& vec = kv.second;
            sort(vec.begin(), vec.end());
            int sz = vec.size();
            for (int i = 0; i < sz; ++i) {
                int cnt = sz - i;
                int seed = vec[i];
                if (cnt > bestCnt || (cnt == bestCnt && seed < ans)) {
                    bestCnt = cnt;
                    ans = seed;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int destroyTargets(int[] nums, int space) {
        java.util.Map<Integer, int[]> map = new java.util.HashMap<>();
        for (int num : nums) {
            int r = num % space;
            int[] info = map.get(r);
            if (info == null) {
                map.put(r, new int[]{1, num});
            } else {
                info[0]++;
                if (num < info[1]) {
                    info[1] = num;
                }
            }
        }
        int bestCount = -1;
        int answer = Integer.MAX_VALUE;
        for (int[] info : map.values()) {
            int cnt = info[0];
            int minVal = info[1];
            if (cnt > bestCount || (cnt == bestCount && minVal < answer)) {
                bestCount = cnt;
                answer = minVal;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        mod_info = {}
        for num in nums:
            r = num % space
            if r not in mod_info:
                mod_info[r] = [1, num]  # count, minimal value
            else:
                mod_info[r][0] += 1
                if num < mod_info[r][1]:
                    mod_info[r][1] = num

        best_cnt = -1
        answer = None
        for cnt, min_val in mod_info.values():
            if cnt > best_cnt or (cnt == best_cnt and (answer is None or min_val < answer)):
                best_cnt = cnt
                answer = min_val
        return answer
```

## Python3

```python
from typing import List

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        freq = {}
        for num in nums:
            r = num % space
            if r not in freq:
                freq[r] = [1, num]  # count, min value
            else:
                freq[r][0] += 1
                if num < freq[r][1]:
                    freq[r][1] = num

        max_cnt = -1
        answer = None
        for cnt, mn in freq.values():
            if cnt > max_cnt or (cnt == max_cnt and mn < answer):
                max_cnt = cnt
                answer = mn
        return answer
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int rem;
    int val;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *p = (const Pair *)a;
    const Pair *q = (const Pair *)b;
    if (p->rem != q->rem) return p->rem < q->rem ? -1 : 1;
    if (p->val != q->val) return p->val < q->val ? -1 : 1;
    return 0;
}

int destroyTargets(int* nums, int numsSize, int space) {
    Pair *arr = (Pair *)malloc(sizeof(Pair) * numsSize);
    for (int i = 0; i < numsSize; ++i) {
        arr[i].rem = nums[i] % space;
        arr[i].val = nums[i];
    }
    qsort(arr, numsSize, sizeof(Pair), cmpPair);

    int bestCount = 0;
    int bestVal = INT_MAX;
    int i = 0;
    while (i < numsSize) {
        int curRem = arr[i].rem;
        int cnt = 0;
        int minVal = arr[i].val;   // first element in this remainder group
        while (i < numsSize && arr[i].rem == curRem) {
            ++cnt;
            ++i;
        }
        if (cnt > bestCount || (cnt == bestCount && minVal < bestVal)) {
            bestCount = cnt;
            bestVal = minVal;
        }
    }

    free(arr);
    return bestVal;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int DestroyTargets(int[] nums, int space) {
        var dict = new Dictionary<int, (int cnt, int min)>();
        foreach (int v in nums) {
            int r = v % space;
            if (dict.TryGetValue(r, out var entry)) {
                int newCnt = entry.cnt + 1;
                int newMin = Math.Min(entry.min, v);
                dict[r] = (newCnt, newMin);
            } else {
                dict[r] = (1, v);
            }
        }

        int bestCount = -1;
        int answer = int.MaxValue;

        foreach (var kvp in dict) {
            int cnt = kvp.Value.cnt;
            int minVal = kvp.Value.min;
            if (cnt > bestCount || (cnt == bestCount && minVal < answer)) {
                bestCount = cnt;
                answer = minVal;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} space
 * @return {number}
 */
var destroyTargets = function(nums, space) {
    const map = new Map(); // remainder -> {cnt, min}
    for (const num of nums) {
        const r = num % space;
        if (!map.has(r)) {
            map.set(r, { cnt: 1, min: num });
        } else {
            const obj = map.get(r);
            obj.cnt += 1;
            if (num < obj.min) obj.min = num;
        }
    }
    let bestCnt = -1;
    let answer = Infinity;
    for (const {cnt, min} of map.values()) {
        if (cnt > bestCnt || (cnt === bestCnt && min < answer)) {
            bestCnt = cnt;
            answer = min;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function destroyTargets(nums: number[], space: number): number {
    const count = new Map<number, number>();
    const minVal = new Map<number, number>();
    for (const num of nums) {
        const r = num % space;
        count.set(r, (count.get(r) ?? 0) + 1);
        const curMin = minVal.get(r);
        if (curMin === undefined || num < curMin) {
            minVal.set(r, num);
        }
    }
    let bestCount = -1;
    let answer = Infinity;
    for (const [r, c] of count.entries()) {
        const candidate = minVal.get(r)!;
        if (c > bestCount) {
            bestCount = c;
            answer = candidate;
        } else if (c === bestCount && candidate < answer) {
            answer = candidate;
        }
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $space
     * @return Integer
     */
    function destroyTargets($nums, $space) {
        $cnt = [];
        $minVal = [];

        foreach ($nums as $num) {
            $r = $num % $space;
            if (!isset($cnt[$r])) {
                $cnt[$r] = 0;
                $minVal[$r] = $num;
            }
            $cnt[$r]++;
            if ($num < $minVal[$r]) {
                $minVal[$r] = $num;
            }
        }

        $maxCount = -1;
        $answer = PHP_INT_MAX;

        foreach ($cnt as $r => $c) {
            if ($c > $maxCount) {
                $maxCount = $c;
                $answer = $minVal[$r];
            } elseif ($c == $maxCount && $minVal[$r] < $answer) {
                $answer = $minVal[$r];
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func destroyTargets(_ nums: [Int], _ space: Int) -> Int {
        var freq = [Int: Int]()
        for num in nums {
            let r = num % space
            freq[r, default: 0] += 1
        }
        var maxCount = 0
        for count in freq.values {
            if count > maxCount { maxCount = count }
        }
        var answer = Int.max
        for num in nums {
            let r = num % space
            if freq[r] == maxCount && num < answer {
                answer = num
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun destroyTargets(nums: IntArray, space: Int): Int {
        val map = HashMap<Int, IntArray>()
        for (num in nums) {
            val rem = num % space
            val arr = map.getOrPut(rem) { intArrayOf(0, num) }
            arr[0]++
            if (num < arr[1]) {
                arr[1] = num
            }
        }
        var bestCount = -1
        var answer = Int.MAX_VALUE
        for (arr in map.values) {
            val cnt = arr[0]
            val minVal = arr[1]
            if (cnt > bestCount || (cnt == bestCount && minVal < answer)) {
                bestCount = cnt
                answer = minVal
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int destroyTargets(List<int> nums, int space) {
    final Map<int, List<int>> groups = {};
    for (var num in nums) {
      int r = num % space;
      if (!groups.containsKey(r)) {
        groups[r] = [1, num];
      } else {
        var entry = groups[r]!;
        entry[0] += 1;
        if (num < entry[1]) entry[1] = num;
      }
    }

    int maxCount = -1;
    int answer = 0;
    bool first = true;

    for (var entry in groups.values) {
      int cnt = entry[0];
      int minVal = entry[1];
      if (cnt > maxCount) {
        maxCount = cnt;
        answer = minVal;
        first = false;
      } else if (cnt == maxCount && (!first && minVal < answer)) {
        answer = minVal;
      }
    }

    return answer;
  }
}
```

## Golang

```go
func destroyTargets(nums []int, space int) int {
	type info struct {
		cnt int
		min int
	}
	m := make(map[int]info)
	for _, v := range nums {
		r := v % space
		if inf, ok := m[r]; ok {
			inf.cnt++
			if v < inf.min {
				inf.min = v
			}
			m[r] = inf
		} else {
			m[r] = info{cnt: 1, min: v}
		}
	}
	maxCnt := 0
	ans := int(^uint(0) >> 1) // MaxInt
	for _, inf := range m {
		if inf.cnt > maxCnt {
			maxCnt = inf.cnt
			ans = inf.min
		} else if inf.cnt == maxCnt && inf.min < ans {
			ans = inf.min
		}
	}
	return ans
}
```

## Ruby

```ruby
def destroy_targets(nums, space)
  counts = Hash.new(0)
  mins = {}
  nums.each do |num|
    r = num % space
    counts[r] += 1
    mins[r] = num if !mins.key?(r) || num < mins[r]
  end
  max_cnt = counts.values.max
  answer = nil
  counts.each do |r, cnt|
    next unless cnt == max_cnt
    val = mins[r]
    answer = val if answer.nil? || val < answer
  end
  answer
end
```

## Scala

```scala
object Solution {
    def destroyTargets(nums: Array[Int], space: Int): Int = {
        import scala.collection.mutable
        val map = mutable.HashMap[Int, (Int, Int)]() // remainder -> (count, minValue)
        for (v <- nums) {
            val r = v % space
            map.get(r) match {
                case Some((cnt, mn)) =>
                    val newCnt = cnt + 1
                    val newMn = if (v < mn) v else mn
                    map.update(r, (newCnt, newMn))
                case None =>
                    map.put(r, (1, v))
            }
        }
        var bestCount = -1
        var answer = Int.MaxValue
        for ((_, (cnt, mn)) <- map) {
            if (cnt > bestCount || (cnt == bestCount && mn < answer)) {
                bestCount = cnt
                answer = mn
            }
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn destroy_targets(nums: Vec<i32>, space: i32) -> i32 {
        use std::collections::HashMap;
        let mut map: HashMap<i32, (i32, i32)> = HashMap::new(); // remainder -> (count, min_value)
        for &num in nums.iter() {
            let r = num % space;
            let entry = map.entry(r).or_insert((0, num));
            entry.0 += 1;
            if num < entry.1 {
                entry.1 = num;
            }
        }
        let mut best_cnt = -1i32;
        let mut answer = i32::MAX;
        for (_, (cnt, min_val)) in map.iter() {
            if *cnt > best_cnt {
                best_cnt = *cnt;
                answer = *min_val;
            } else if *cnt == best_cnt && *min_val < answer {
                answer = *min_val;
            }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (destroy-targets nums space)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([ht (make-hash)])
    ;; group numbers by remainder
    (for ([x nums])
      (define r (modulo x space))
      (hash-set! ht r (cons x (hash-ref ht r '()))))
    (define best-count -1)
    (define best-seed #f)
    ;; evaluate each group
    (for ([kv (in-hash ht)])
      (define group (sort (hash-ref ht (car kv)) <))
      (define len (length group))
      (define vec (list->vector group))
      (for ([i (in-range len)])
        (define seed (vector-ref vec i))
        (define cnt (- len i))
        (cond
          [(> cnt best-count)
           (set! best-count cnt)
           (set! best-seed seed)]
          [(and (= cnt best-count) (< seed best-seed))
           (set! best-seed seed)])))
    best-seed))
```

## Erlang

```erlang
-module(solution).
-export([destroy_targets/2]).

-spec destroy_targets(Nums :: [integer()], Space :: integer()) -> integer().
destroy_targets(Nums, Space) ->
    Map = lists:foldl(
        fun(Num, Acc) ->
            Rem = Num rem Space,
            case maps:get(Rem, Acc, undefined) of
                undefined ->
                    maps:put(Rem, {1, Num}, Acc);
                {Cnt, Min} ->
                    NewCnt = Cnt + 1,
                    NewMin = if Num < Min -> Num; true -> Min end,
                    maps:put(Rem, {NewCnt, NewMin}, Acc)
            end
        end,
        #{},
        Nums),
    {BestSeed, _} = maps:fold(
        fun(_Rem, {Cnt, MinVal}, {CurSeed, CurCnt}) ->
            case CurSeed of
                undefined ->
                    {MinVal, Cnt};
                _ ->
                    if
                        Cnt > CurCnt -> {MinVal, Cnt};
                        Cnt == CurCnt andalso MinVal < CurSeed -> {MinVal, Cnt};
                        true -> {CurSeed, CurCnt}
                    end
            end
        end,
        {undefined, 0},
        Map),
    BestSeed.
```

## Elixir

```elixir
defmodule Solution do
  @spec destroy_targets(nums :: [integer], space :: integer) :: integer
  def destroy_targets(nums, space) do
    groups =
      Enum.reduce(nums, %{}, fn num, acc ->
        r = rem(num, space)

        case Map.get(acc, r) do
          nil -> Map.put(acc, r, {1, num})
          {cnt, minv} ->
            new_cnt = cnt + 1
            new_min = if num < minv, do: num, else: minv
            Map.put(acc, r, {new_cnt, new_min})
        end
      end)

    {_best_cnt, best_val} =
      Enum.reduce(groups, {-1, nil}, fn {_r, {cnt, minv}}, {best_cnt, best_val} ->
        cond do
          cnt > best_cnt -> {cnt, minv}
          cnt == best_cnt and (best_val == nil or minv < best_val) -> {cnt, minv}
          true -> {best_cnt, best_val}
        end
      end)

    best_val
  end
end
```
