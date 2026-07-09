# 2007. Find Original Array From Doubled Array

## Cpp

```cpp
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        if (changed.size() % 2 != 0) return {};
        sort(changed.begin(), changed.end());
        unordered_map<long long, int> cnt;
        cnt.reserve(changed.size()*2);
        for (int x : changed) ++cnt[x];
        vector<int> original;
        for (int x : changed) {
            if (cnt[x] == 0) continue;
            --cnt[x];
            long long dbl = 2LL * x;
            if (cnt[dbl] == 0) return {};
            --cnt[dbl];
            original.push_back(x);
        }
        return original;
    }
};
```

## Java

```java
class Solution {
    public int[] findOriginalArray(int[] changed) {
        int n = changed.length;
        if (n % 2 != 0) return new int[0];
        java.util.Arrays.sort(changed);
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int v : changed) {
            freq.put(v, freq.getOrDefault(v, 0) + 1);
        }
        java.util.ArrayList<Integer> original = new java.util.ArrayList<>(n / 2);
        for (int x : changed) {
            int cnt = freq.getOrDefault(x, 0);
            if (cnt == 0) continue;
            int doubleVal = x * 2;
            int cntDouble = freq.getOrDefault(doubleVal, 0);
            if (cntDouble == 0) return new int[0];
            // decrement counts
            freq.put(x, cnt - 1);
            freq.put(doubleVal, cntDouble - 1);
            original.add(x);
        }
        int[] res = new int[original.size()];
        for (int i = 0; i < original.size(); i++) {
            res[i] = original.get(i);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2:
            return []
        from collections import Counter
        cnt = Counter(changed)
        original = []
        for x in sorted(cnt.keys()):
            if cnt[x] == 0:
                continue
            if x == 0:
                # need pairs of zeros
                if cnt[0] % 2:
                    return []
                original.extend([0] * (cnt[0] // 2))
                cnt[0] = 0
                continue
            double = x * 2
            if cnt[double] < cnt[x]:
                return []
            cnt[double] -= cnt[x]
            original.extend([x] * cnt[x])
            cnt[x] = 0
        return original
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        cnt = Counter(changed)
        result = []
        for x in sorted(cnt):
            if cnt[x] == 0:
                continue
            if x * 2 not in cnt or cnt[2 * x] < cnt[x]:
                return []
            if x == 0:
                # need even number of zeros
                if cnt[x] % 2 != 0:
                    return []
                result.extend([0] * (cnt[x] // 2))
                cnt[x] = 0
                continue
            freq = cnt[x]
            result.extend([x] * freq)
            cnt[2 * x] -= freq
            cnt[x] = 0
        return result
```

## C

```c
#include <stdlib.h>

int compare_int(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findOriginalArray(int* changed, int changedSize, int* returnSize) {
    if (changedSize % 2 != 0) {
        *returnSize = 0;
        return NULL;
    }

    int maxVal = 0;
    for (int i = 0; i < changedSize; ++i)
        if (changed[i] > maxVal) maxVal = changed[i];

    int *cnt = (int *)calloc(maxVal + 1, sizeof(int));
    if (!cnt) {
        *returnSize = 0;
        return NULL;
    }

    for (int i = 0; i < changedSize; ++i)
        cnt[changed[i]]++;

    int half = changedSize / 2;
    int *original = (int *)malloc(half * sizeof(int));
    if (!original) {
        free(cnt);
        *returnSize = 0;
        return NULL;
    }
    int idx = 0;

    /* handle zeros */
    if (cnt[0] % 2 != 0) {
        free(cnt);
        free(original);
        *returnSize = 0;
        return NULL;
    }
    while (cnt[0] > 0) {
        cnt[0] -= 2;
        original[idx++] = 0;
    }

    for (int i = 1; i <= maxVal && idx < half; ++i) {
        while (cnt[i] > 0) {
            int d = i * 2;
            if (d > maxVal || cnt[d] == 0) {
                free(cnt);
                free(original);
                *returnSize = 0;
                return NULL;
            }
            cnt[i]--;
            cnt[d]--;
            original[idx++] = i;
        }
    }

    free(cnt);
    *returnSize = idx;
    return original;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindOriginalArray(int[] changed) {
        if (changed.Length % 2 == 1) return new int[0];
        Array.Sort(changed);
        var cnt = new Dictionary<int, int>();
        foreach (var v in changed) {
            if (cnt.ContainsKey(v)) cnt[v]++; else cnt[v] = 1;
        }
        var original = new List<int>();
        foreach (var v in changed) {
            if (!cnt.TryGetValue(v, out int c) || c == 0) continue;
            if (v == 0) {
                if (c < 2) return new int[0];
                cnt[v] -= 2;
                original.Add(0);
            } else {
                int doubleVal = v * 2;
                if (!cnt.TryGetValue(doubleVal, out int cd) || cd == 0) return new int[0];
                cnt[v]--;
                cnt[doubleVal]--;
                original.Add(v);
            }
        }
        foreach (var kv in cnt) {
            if (kv.Value != 0) return new int[0];
        }
        return original.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} changed
 * @return {number[]}
 */
var findOriginalArray = function(changed) {
    const n = changed.length;
    if (n % 2 !== 0) return [];
    
    changed.sort((a, b) => a - b);
    const freq = new Map();
    for (const v of changed) {
        freq.set(v, (freq.get(v) || 0) + 1);
    }
    
    const original = [];
    for (const v of changed) {
        const cnt = freq.get(v);
        if (!cnt) continue; // already used
        
        const doubleVal = v * 2;
        const doubleCnt = freq.get(doubleVal) || 0;
        if (doubleCnt === 0) return []; // cannot find a pair
        
        // use one occurrence of v and its double
        freq.set(v, cnt - 1);
        freq.set(doubleVal, doubleCnt - 1);
        original.push(v);
    }
    
    return original;
};
```

## Typescript

```typescript
function findOriginalArray(changed: number[]): number[] {
    if (changed.length % 2 !== 0) return [];
    changed.sort((a, b) => a - b);
    const freq = new Map<number, number>();
    for (const v of changed) {
        freq.set(v, (freq.get(v) ?? 0) + 1);
    }
    const original: number[] = [];
    for (const num of changed) {
        const cnt = freq.get(num)!;
        if (cnt === 0) continue;
        if (num === 0) {
            if (cnt % 2 !== 0) return [];
            const times = cnt / 2;
            for (let i = 0; i < times; ++i) original.push(0);
            freq.set(0, 0);
        } else {
            const double = num * 2;
            const cntDouble = freq.get(double) ?? 0;
            if (cntDouble < cnt) return [];
            for (let i = 0; i < cnt; ++i) original.push(num);
            freq.set(double, cntDouble - cnt);
            freq.set(num, 0);
        }
    }
    return original;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $changed
     * @return Integer[]
     */
    function findOriginalArray($changed) {
        $n = count($changed);
        if ($n % 2 == 1) {
            return [];
        }
        sort($changed, SORT_NUMERIC);
        $freq = [];
        foreach ($changed as $v) {
            $freq[$v] = ($freq[$v] ?? 0) + 1;
        }

        $original = [];

        // handle zeros separately
        if (isset($freq[0])) {
            if ($freq[0] % 2 != 0) {
                return [];
            }
            $pairs = intdiv($freq[0], 2);
            for ($i = 0; $i < $pairs; $i++) {
                $original[] = 0;
            }
            $freq[0] = 0;
        }

        ksort($freq, SORT_NUMERIC);

        foreach ($freq as $x => $cnt) {
            if ($cnt == 0) continue;
            $double = $x * 2;
            if (!isset($freq[$double]) || $freq[$double] < $cnt) {
                return [];
            }
            for ($i = 0; $i < $cnt; $i++) {
                $original[] = $x;
            }
            $freq[$double] -= $cnt;
        }

        return $original;
    }
}
```

## Swift

```swift
class Solution {
    func findOriginalArray(_ changed: [Int]) -> [Int] {
        if changed.count % 2 != 0 { return [] }
        let sorted = changed.sorted()
        var freq = [Int:Int]()
        for num in sorted {
            freq[num, default: 0] += 1
        }
        var original = [Int]()
        for num in sorted {
            guard let cnt = freq[num], cnt > 0 else { continue }
            freq[num]! = cnt - 1
            let doubleVal = num * 2
            if let dcnt = freq[doubleVal], dcnt > 0 {
                freq[doubleVal] = dcnt - 1
                original.append(num)
            } else {
                return []
            }
        }
        return original
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findOriginalArray(changed: IntArray): IntArray {
        if (changed.size % 2 != 0) return intArrayOf()
        changed.sort()
        val freq = HashMap<Int, Int>()
        for (v in changed) {
            freq[v] = freq.getOrDefault(v, 0) + 1
        }
        val original = ArrayList<Int>()
        for (num in changed) {
            val cnt = freq.getOrDefault(num, 0)
            if (cnt == 0) continue
            if (num == 0) {
                if (cnt % 2 != 0) return intArrayOf()
                repeat(cnt / 2) { original.add(0) }
                freq[num] = 0
            } else {
                val doubleVal = num * 2
                val doubleCnt = freq.getOrDefault(doubleVal, 0)
                if (doubleCnt < cnt) return intArrayOf()
                repeat(cnt) { original.add(num) }
                freq[num] = 0
                freq[doubleVal] = doubleCnt - cnt
            }
        }
        return original.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> findOriginalArray(List<int> changed) {
    int n = changed.length;
    if (n % 2 == 1) return [];
    changed.sort();
    Map<int, int> freq = {};
    for (var v in changed) {
      freq[v] = (freq[v] ?? 0) + 1;
    }
    List<int> original = [];
    for (int x in changed) {
      if ((freq[x] ?? 0) == 0) continue;
      // use one occurrence of x
      freq[x] = freq[x]! - 1;
      int target = x * 2;
      if (!freq.containsKey(target) || freq[target] == 0) {
        return [];
      }
      freq[target] = freq[target]! - 1;
      original.add(x);
    }
    return original;
  }
}
```

## Golang

```go
package main

import "sort"

func findOriginalArray(changed []int) []int {
	if len(changed)%2 == 1 {
		return []int{}
	}
	sort.Ints(changed)
	freq := make(map[int]int, len(changed))
	for _, v := range changed {
		freq[v]++
	}
	original := make([]int, 0, len(changed)/2)
	for _, v := range changed {
		if freq[v] == 0 {
			continue
		}
		if v == 0 {
			if freq[0] < 2 {
				return []int{}
			}
			freq[0] -= 2
			original = append(original, 0)
			continue
		}
		double := v * 2
		if cnt, ok := freq[double]; !ok || cnt == 0 {
			return []int{}
		}
		freq[v]--
		freq[double]--
		original = append(original, v)
	}
	if len(original) != len(changed)/2 {
		return []int{}
	}
	return original
}
```

## Ruby

```ruby
def find_original_array(changed)
  return [] if changed.length.odd?
  changed.sort!
  freq = Hash.new(0)
  changed.each { |v| freq[v] += 1 }
  original = []
  changed.each do |x|
    next if freq[x] == 0
    if x == 0
      cnt = freq[0]
      return [] if cnt.odd?
      (cnt / 2).times { original << 0 }
      freq[0] = 0
    else
      double = x * 2
      return [] if freq[double] < freq[x]
      count = freq[x]
      original.concat([x] * count)
      freq[double] -= count
      freq[x] = 0
    end
  end
  original
end
```

## Scala

```scala
object Solution {
    def findOriginalArray(changed: Array[Int]): Array[Int] = {
        if (changed.length % 2 == 1) return Array.empty[Int]
        val sorted = changed.sorted
        import scala.collection.mutable

        val count = mutable.HashMap[Int, Int]()
        for (v <- sorted) {
            count(v) = count.getOrElse(v, 0) + 1
        }

        val original = mutable.ArrayBuffer[Int]()

        for (v <- sorted) {
            val cnt = count.getOrElse(v, 0)
            if (cnt == 0) {
                // already paired
            } else {
                if (v == 0) {
                    if (cnt < 2) return Array.empty[Int]
                    count(v) = cnt - 2
                    original += v
                } else {
                    val doubleVal = v * 2
                    val cntDouble = count.getOrElse(doubleVal, 0)
                    if (cntDouble == 0) return Array.empty[Int]
                    count(v) = cnt - 1
                    count(doubleVal) = cntDouble - 1
                    original += v
                }
            }
        }

        original.toArray
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn find_original_array(mut changed: Vec<i32>) -> Vec<i32> {
        let n = changed.len();
        if n % 2 == 1 {
            return Vec::new();
        }
        changed.sort_unstable();

        let mut cnt: HashMap<i32, i32> = HashMap::with_capacity(n);
        for &v in &changed {
            *cnt.entry(v).or_insert(0) += 1;
        }

        let mut original = Vec::with_capacity(n / 2);

        for &x in &changed {
            let cur = match cnt.get(&x) {
                Some(&c) => c,
                None => 0,
            };
            if cur == 0 {
                continue;
            }
            let double = x * 2;
            let double_cnt = match cnt.get(&double) {
                Some(&c) => c,
                None => 0,
            };
            if double_cnt == 0 {
                return Vec::new();
            }

            // decrement counts
            *cnt.get_mut(&x).unwrap() -= 1;
            *cnt.get_mut(&double).unwrap() -= 1;

            original.push(x);
        }

        original
    }
}
```

## Racket

```racket
(require racket/hash)

(define/contract (find-original-array changed)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([n (length changed)]
         [sorted (sort changed <)])
    (if (odd? n)
        '()
        (let ([cnt (make-hash)])
          ;; count occurrences
          (for ([x sorted])
            (hash-update! cnt x add1 0))
          (define result '())
          (define success #t)
          (for ([x sorted] #:break (not success))
            (let ([c (hash-ref cnt x 0)])
              (when (> c 0)
                (if (= x 0)
                    (if (< c 2)
                        (set! success #f)
                        (begin
                          (hash-set! cnt x (- c 2))
                          (set! result (cons 0 result))))
                    (let* ([double (* 2 x)]
                           [c2 (hash-ref cnt double 0)])
                      (if (< c2 1)
                          (set! success #f)
                          (begin
                            (hash-set! cnt x (- c 1))
                            (hash-set! cnt double (- c2 1))
                            (set! result (cons x result))))))))))
          (if success (reverse result) '())))))
```

## Erlang

```erlang
-module(solution).
-export([find_original_array/1]).

-spec find_original_array(Changed :: [integer()]) -> [integer()].
find_original_array(Changed) ->
    Sorted = lists:sort(Changed),
    Counts0 = build_counts(Sorted, #{}),
    case process(Sorted, Counts0, []) of
        {ok, OrigRev} -> lists:reverse(OrigRev);
        error -> []
    end.

build_counts([], Acc) -> Acc;
build_counts([H|T], Acc) ->
    NewAcc = maps:update_with(H, fun(C) -> C + 1 end, 1, Acc),
    build_counts(T, NewAcc).

process([], _Counts, Orig) ->
    {ok, Orig};
process([X|Rest], Counts, Orig) ->
    Cx = maps:get(X, Counts, 0),
    if
        Cx == 0 ->
            process(Rest, Counts, Orig);
        true ->
            case X of
                0 ->
                    if
                        Cx < 2 -> error;
                        true ->
                            NewCounts = maps:put(0, Cx - 2, Counts),
                            process(Rest, NewCounts, [0 | Orig])
                    end;
                _ ->
                    Double = X * 2,
                    Cy = maps:get(Double, Counts, 0),
                    if
                        Cy == 0 -> error;
                        true ->
                            NewCounts1 = maps:put(X, Cx - 1, Counts),
                            NewCounts2 = maps:put(Double, Cy - 1, NewCounts1),
                            process(Rest, NewCounts2, [X | Orig])
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_original_array(changed :: [integer]) :: [integer]
  def find_original_array(changed) do
    if rem(length(changed), 2) == 1 do
      []
    else
      sorted = Enum.sort(changed)

      freq =
        Enum.reduce(sorted, %{}, fn v, acc ->
          Map.update(acc, v, 1, &(&1 + 1))
        end)

      {orig_rev, status} =
        Enum.reduce_while(sorted, {[], freq}, fn x, {orig, cnts} ->
          cur = Map.get(cnts, x, 0)

          if cur == 0 do
            {:cont, {orig, cnts}}
          else
            double = x * 2
            double_cnt = Map.get(cnts, double, 0)

            if double_cnt == 0 do
              {:halt, :error}
            else
              cnts1 = Map.update!(cnts, x, &(&1 - 1))
              cnts2 = Map.update!(cnts1, double, &(&1 - 1))
              {:cont, {[x | orig], cnts2}}
            end
          end
        end)

      case status do
        :error -> []
        _ -> Enum.reverse(orig_rev)
      end
    end
  end
end
```
