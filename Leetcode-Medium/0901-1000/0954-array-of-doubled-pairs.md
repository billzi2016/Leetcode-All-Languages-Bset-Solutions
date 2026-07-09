# 0954. Array of Doubled Pairs

## Cpp

```cpp
class Solution {
public:
    bool canReorderDoubled(std::vector<int>& arr) {
        std::unordered_map<long long, int> freq;
        for (int v : arr) ++freq[v];
        std::sort(arr.begin(), arr.end(),
                  [](int a, int b){ return std::abs(a) < std::abs(b); });
        for (int v : arr) {
            long long x = v;
            if (freq[x] == 0) continue;
            long long y = x * 2;
            if (freq.find(y) == freq.end() || freq[y] < freq[x]) return false;
            freq[y] -= freq[x];
            freq[x] = 0;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canReorderDoubled(int[] arr) {
        java.util.Map<Integer, Integer> count = new java.util.HashMap<>();
        for (int x : arr) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }
        Integer[] sorted = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) {
            sorted[i] = arr[i];
        }
        java.util.Arrays.sort(sorted, java.util.Comparator.comparingInt(Math::abs));
        for (int x : sorted) {
            int c = count.getOrDefault(x, 0);
            if (c == 0) continue;
            int target = x * 2;
            int targetCount = count.getOrDefault(target, 0);
            if (targetCount < c) return false;
            count.put(target, targetCount - c);
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        count = Counter(arr)
        for x in sorted(count.keys(), key=abs):
            if count[x] == 0:
                continue
            need = x * 2
            if count[need] < count[x]:
                return False
            count[need] -= count[x]
        return True
```

## Python3

```python
class Solution:
    def canReorderDoubled(self, arr):
        from collections import Counter
        cnt = Counter(arr)
        for x in sorted(cnt.keys(), key=abs):
            if cnt[x] == 0:
                continue
            need = x * 2
            if cnt[need] < cnt[x]:
                return False
            cnt[need] -= cnt[x]
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmpAbs(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    int aa = abs(av);
    int bb = abs(bv);
    if (aa != bb) return aa - bb;
    return av - bv;
}

bool canReorderDoubled(int* arr, int arrSize) {
    const int OFFSET = 200000;
    const int SIZE = 400001; // covers range [-200000, 200000]
    static int freq[SIZE];
    memset(freq, 0, sizeof(freq));

    for (int i = 0; i < arrSize; ++i) {
        freq[arr[i] + OFFSET]++;
    }

    int *sorted = (int *)malloc(arrSize * sizeof(int));
    if (!sorted) return false;
    memcpy(sorted, arr, arrSize * sizeof(int));
    qsort(sorted, arrSize, sizeof(int), cmpAbs);

    for (int i = 0; i < arrSize; ++i) {
        int x = sorted[i];
        int idx = x + OFFSET;
        if (freq[idx] == 0) continue;
        freq[idx]--;
        long long y = 2LL * x;
        int yIdx = (int)(y + OFFSET);
        if (yIdx < 0 || yIdx >= SIZE || freq[yIdx] == 0) {
            free(sorted);
            return false;
        }
        freq[yIdx]--;
    }

    free(sorted);
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanReorderDoubled(int[] arr) {
        Array.Sort(arr, (a, b) => Math.Abs(a).CompareTo(Math.Abs(b)));
        var count = new Dictionary<int, int>();
        foreach (int v in arr) {
            if (count.ContainsKey(v)) count[v]++; else count[v] = 1;
        }
        foreach (int x in arr) {
            if (count[x] == 0) continue;
            count[x]--;
            int target = x * 2;
            if (!count.ContainsKey(target) || count[target] == 0) return false;
            count[target]--;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canReorderDoubled = function(arr) {
    const count = new Map();
    for (const num of arr) {
        count.set(num, (count.get(num) || 0) + 1);
    }
    arr.sort((a, b) => Math.abs(a) - Math.abs(b));
    for (const x of arr) {
        const cur = count.get(x);
        if (!cur) continue; // already paired
        const target = x * 2;
        const tgtCnt = count.get(target) || 0;
        if (tgtCnt === 0) return false;
        count.set(x, cur - 1);
        count.set(target, tgtCnt - 1);
    }
    return true;
};
```

## Typescript

```typescript
function canReorderDoubled(arr: number[]): boolean {
    const cnt = new Map<number, number>();
    for (const v of arr) {
        cnt.set(v, (cnt.get(v) ?? 0) + 1);
    }
    const keys = Array.from(cnt.keys()).sort((a, b) => Math.abs(a) - Math.abs(b));
    for (const x of keys) {
        const c = cnt.get(x)!;
        if (c === 0) continue;
        const target = x * 2;
        const targetCount = cnt.get(target) ?? 0;
        if (targetCount < c) return false;
        cnt.set(target, targetCount - c);
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canReorderDoubled($arr) {
        // Sort by absolute value to ensure smallest magnitude processed first
        usort($arr, function($a, $b) {
            return abs($a) <=> abs($b);
        });

        // Frequency map
        $cnt = [];
        foreach ($arr as $x) {
            if (!isset($cnt[$x])) {
                $cnt[$x] = 0;
            }
            $cnt[$x]++;
        }

        // Try to pair each element with its double
        foreach ($arr as $x) {
            if ($cnt[$x] == 0) {
                continue; // already used in a previous pairing
            }
            $double = $x * 2;
            if (!isset($cnt[$double]) || $cnt[$double] == 0) {
                return false;
            }
            $cnt[$x]--;
            $cnt[$double]--;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canReorderDoubled(_ arr: [Int]) -> Bool {
        var freq = [Int:Int]()
        for v in arr {
            freq[v, default: 0] += 1
        }
        let sorted = arr.sorted { abs($0) < abs($1) }
        for x in sorted {
            guard let countX = freq[x], countX > 0 else { continue }
            let doubleVal = x * 2
            guard let countDouble = freq[doubleVal], countDouble > 0 else {
                return false
            }
            freq[x] = countX - 1
            freq[doubleVal] = countDouble - 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canReorderDoubled(arr: IntArray): Boolean {
        val count = HashMap<Int, Int>()
        for (x in arr) {
            count[x] = count.getOrDefault(x, 0) + 1
        }
        val sorted = arr.sortedBy { kotlin.math.abs(it) }
        for (x in sorted) {
            val cur = count.getOrDefault(x, 0)
            if (cur == 0) continue
            val doubleVal = x * 2
            val doubleCount = count.getOrDefault(doubleVal, 0)
            if (doubleCount < cur) return false
            count[x] = cur - 1
            count[doubleVal] = doubleCount - 1
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canReorderDoubled(List<int> arr) {
    // Frequency map
    final Map<int, int> freq = {};
    for (var v in arr) {
      freq[v] = (freq[v] ?? 0) + 1;
    }

    // Sort by absolute value
    final List<int> sorted = List.from(arr);
    sorted.sort((a, b) => a.abs().compareTo(b.abs()));

    for (var x in sorted) {
      int countX = freq[x] ?? 0;
      if (countX == 0) continue; // already paired

      int doubleX = x * 2;
      int countDouble = freq[doubleX] ?? 0;
      if (countDouble == 0) return false;

      // Pair one occurrence of x with one of doubleX
      freq[x] = countX - 1;
      freq[doubleX] = countDouble - 1;
    }

    return true;
  }
}
```

## Golang

```go
import "sort"

func canReorderDoubled(arr []int) bool {
	freq := make(map[int]int, len(arr))
	for _, v := range arr {
		freq[v]++
	}
	sort.Slice(arr, func(i, j int) bool {
		ai, aj := arr[i], arr[j]
		if abs(ai) == abs(aj) {
			return ai < aj
		}
		return abs(ai) < abs(aj)
	})
	for _, v := range arr {
		if freq[v] == 0 {
			continue
		}
		if freq[2*v] == 0 {
			return false
		}
		freq[v]--
		freq[2*v]--
	}
	return true
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def can_reorder_doubled(arr)
  count = Hash.new(0)
  arr.each { |v| count[v] += 1 }
  return false if count[0].odd?
  arr.sort_by(&:abs).each do |x|
    next if count[x] == 0
    target = x * 2
    return false if count[target] < count[x]
    count[target] -= count[x]
    count[x] = 0
  end
  true
end
```

## Scala

```scala
object Solution {
  def canReorderDoubled(arr: Array[Int]): Boolean = {
    import scala.collection.mutable
    val cnt = mutable.Map.empty[Int, Int].withDefaultValue(0)
    for (x <- arr) cnt(x) += 1

    val sorted = arr.sortBy(math.abs)

    for (x <- sorted) {
      if (cnt(x) > 0) {
        cnt(x) -= 1
        val double = x * 2
        if (cnt(double) == 0) return false
        cnt(double) -= 1
      }
    }
    true
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn can_reorder_doubled(arr: Vec<i32>) -> bool {
        let mut count: HashMap<i32, i32> = HashMap::new();
        for &x in &arr {
            *count.entry(x).or_insert(0) += 1;
        }

        let mut sorted = arr.clone();
        sorted.sort_by_key(|&x| x.abs());

        for &x in &sorted {
            let cur_cnt = match count.get(&x) {
                Some(&v) => v,
                None => 0,
            };
            if cur_cnt == 0 {
                continue;
            }

            let double = x * 2;
            let entry = count.entry(double).or_insert(0);
            if *entry < cur_cnt {
                return false;
            }
            *entry -= cur_cnt;
            count.insert(x, 0);
        }
        true
    }
}
```

## Racket

```racket
(define/contract (can-reorder-doubled arr)
  (-> (listof exact-integer?) boolean?)
  (let* ((ht (make-hash))
         (inc (lambda (x)
                (hash-set! ht x (+ (hash-ref ht x 0) 1)))))
    (for-each inc arr)
    (define sorted-keys
      (sort (hash-keys ht)
            (lambda (a b) (< (abs a) (abs b)))))
    (let loop ((ks sorted-keys))
      (cond
        [(null? ks) #t]
        [else
         (define x (car ks))
         (define cnt (hash-ref ht x 0))
         (if (= cnt 0)
             (loop (cdr ks))
             (let* ((target (* 2 x))
                    (cnt-target (hash-ref ht target 0)))
               (if (< cnt-target cnt)
                   #f
                   (begin
                     (hash-set! ht target (- cnt-target cnt))
                     (hash-set! ht x 0)
                     (loop (cdr ks))))))]))))
```

## Erlang

```erlang
-module(solution).
-export([can_reorder_doubled/1]).

-spec can_reorder_doubled([integer()]) -> boolean().
can_reorder_doubled(Arr) ->
    CountMap = lists:foldl(
        fun(X, Acc) ->
            maps:update_with(
                X,
                fun(C) -> C + 1 end,
                1,
                Acc)
        end,
        #{},
        Arr),
    Sorted = lists:sort(fun(A, B) -> abs(A) < abs(B) end, maps:keys(CountMap)),
    process(Sorted, CountMap).

process([], _) ->
    true;
process([X | Rest], Map) ->
    Cx = maps:get(X, Map, 0),
    if
        Cx == 0 ->
            process(Rest, Map);
        true ->
            Need = X * 2,
            Cy = maps:get(Need, Map, 0),
            if
                Cy < Cx ->
                    false;
                true ->
                    NewMap1 = maps:put(X, 0, Map),
                    NewMap2 = maps:put(Need, Cy - Cx, NewMap1),
                    process(Rest, NewMap2)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_reorder_doubled(arr :: [integer]) :: boolean
  def can_reorder_doubled(arr) do
    freq =
      Enum.reduce(arr, %{}, fn v, acc ->
        Map.update(acc, v, 1, &(&1 + 1))
      end)

    sorted = Enum.sort_by(arr, &abs/1)

    {ok, _} =
      Enum.reduce_while(sorted, {true, freq}, fn x, {_ok, map} ->
        cnt = Map.get(map, x, 0)

        if cnt == 0 do
          {:cont, {true, map}}
        else
          need = Map.get(map, x * 2, 0)

          if need < cnt do
            {:halt, {false, map}}
          else
            new_map =
              map
              |> Map.put(x, 0)
              |> decrement(x * 2, cnt)

            {:cont, {true, new_map}}
          end
        end
      end)

    ok
  end

  defp decrement(map, key, dec) do
    cur = Map.get(map, key, 0)
    new = cur - dec

    if new == 0 do
      Map.delete(map, key)
    else
      Map.put(map, key, new)
    end
  end
end
```
