# 1296. Divide Array in Sets of K Consecutive Numbers

## Cpp

```cpp
class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        if (nums.size() % k != 0) return false;
        map<long long,int> freq;
        for (int x : nums) ++freq[x];
        for (auto it = freq.begin(); it != freq.end(); ++it) {
            long long start = it->first;
            int cnt = it->second;
            if (cnt == 0) continue;
            // need to create 'cnt' sequences starting at 'start'
            for (int i = 0; i < k; ++i) {
                long long val = start + i;
                auto itr = freq.find(val);
                if (itr == freq.end() || itr->second < cnt) return false;
                itr->second -= cnt;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        if (nums.length % k != 0) return false;
        java.util.TreeMap<Integer, Integer> freq = new java.util.TreeMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        while (!freq.isEmpty()) {
            int start = freq.firstKey();
            int count = freq.get(start);
            for (int i = start; i < start + k; i++) {
                Integer cur = freq.get(i);
                if (cur == null || cur < count) return false;
                if (cur == count) {
                    freq.remove(i);
                } else {
                    freq.put(i, cur - count);
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n % k != 0:
            return False

        from collections import Counter
        count = Counter(nums)

        for x in sorted(count):
            occ = count[x]
            if occ > 0:
                for i in range(x, x + k):
                    if count[i] < occ:
                        return False
                    count[i] -= occ
        return True
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        cnt = Counter(nums)
        for v in sorted(cnt):
            c = cnt[v]
            if c > 0:
                for i in range(v, v + k):
                    if cnt[i] < c:
                        return False
                    cnt[i] -= c
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

static int findIdx(int *arr, int size, long long target) {
    int l = 0, r = size - 1;
    while (l <= r) {
        int mid = (l + r) >> 1;
        if ((long long)arr[mid] == target)
            return mid;
        else if ((long long)arr[mid] < target)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return -1;
}

bool isPossibleDivide(int* nums, int numsSize, int k) {
    if (k <= 0 || numsSize % k != 0)
        return false;

    qsort(nums, numsSize, sizeof(int), cmp_int);

    int *vals = (int *)malloc(sizeof(int) * numsSize);
    int *cnts = (int *)malloc(sizeof(int) * numsSize);
    if (!vals || !cnts) {
        free(vals);
        free(cnts);
        return false;
    }

    int m = 0;
    for (int i = 0; i < numsSize;) {
        int v = nums[i];
        int j = i;
        while (j < numsSize && nums[j] == v) ++j;
        vals[m] = v;
        cnts[m] = j - i;
        ++m;
        i = j;
    }

    for (int i = 0; i < m; ++i) {
        while (cnts[i] > 0) {
            int need = cnts[i];
            for (int offset = 0; offset < k; ++offset) {
                long long target = (long long)vals[i] + offset;
                int idx = findIdx(vals, m, target);
                if (idx == -1 || cnts[idx] < need) {
                    free(vals);
                    free(cnts);
                    return false;
                }
                cnts[idx] -= need;
            }
        }
    }

    free(vals);
    free(cnts);
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPossibleDivide(int[] nums, int k) {
        if (k == 1) return true;
        if (nums.Length % k != 0) return false;

        var freq = new SortedDictionary<int, int>();
        foreach (var num in nums) {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        while (freq.Count > 0) {
            int start = freq.First().Key;
            int count = freq[start];

            for (int i = 0; i < k; i++) {
                int cur = start + i;
                if (!freq.ContainsKey(cur))
                    return false;

                if (freq[cur] < count)
                    return false;

                freq[cur] -= count;
                if (freq[cur] == 0)
                    freq.Remove(cur);
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var isPossibleDivide = function(nums, k) {
    if (nums.length % k !== 0) return false;
    
    nums.sort((a, b) => a - b);
    const freq = new Map();
    for (const n of nums) {
        freq.set(n, (freq.get(n) || 0) + 1);
    }
    
    for (const num of nums) {
        const cnt = freq.get(num);
        if (!cnt) continue; // already used up
        
        for (let offset = 0; offset < k; ++offset) {
            const cur = num + offset;
            const curCnt = freq.get(cur) || 0;
            if (curCnt < cnt) return false;
            freq.set(cur, curCnt - cnt);
        }
    }
    
    return true;
};
```

## Typescript

```typescript
function isPossibleDivide(nums: number[], k: number): boolean {
    if (nums.length % k !== 0) return false;
    const freq = new Map<number, number>();
    for (const n of nums) {
        freq.set(n, (freq.get(n) ?? 0) + 1);
    }
    const keys = Array.from(freq.keys()).sort((a, b) => a - b);
    for (const start of keys) {
        const cnt = freq.get(start)!;
        if (cnt > 0) {
            for (let i = 1; i < k; i++) {
                const val = start + i;
                const cur = freq.get(val) ?? 0;
                if (cur < cnt) return false;
                freq.set(val, cur - cnt);
            }
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function isPossibleDivide($nums, $k) {
        $n = count($nums);
        if ($k == 0 || $n % $k != 0) {
            return false;
        }
        sort($nums, SORT_NUMERIC);
        $cnt = [];
        foreach ($nums as $num) {
            if (!isset($cnt[$num])) {
                $cnt[$num] = 0;
            }
            $cnt[$num]++;
        }
        $keys = array_keys($cnt);
        sort($keys, SORT_NUMERIC);
        foreach ($keys as $key) {
            $need = $cnt[$key];
            if ($need > 0) {
                for ($i = 0; $i < $k; $i++) {
                    $next = $key + $i;
                    if (!isset($cnt[$next]) || $cnt[$next] < $need) {
                        return false;
                    }
                    $cnt[$next] -= $need;
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isPossibleDivide(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        if n % k != 0 { return false }
        
        var freq = [Int:Int]()
        for num in nums.sorted() {
            freq[num, default: 0] += 1
        }
        
        let sortedKeys = freq.keys.sorted()
        for key in sortedKeys {
            guard let count = freq[key], count > 0 else { continue }
            for i in 0..<k {
                let cur = key + i
                if let curCount = freq[cur], curCount >= count {
                    freq[cur] = curCount - count
                } else {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPossibleDivide(nums: IntArray, k: Int): Boolean {
        if (nums.size % k != 0) return false
        val map = java.util.TreeMap<Int, Int>()
        for (num in nums) {
            map[num] = (map[num] ?: 0) + 1
        }
        while (map.isNotEmpty()) {
            val start = map.firstKey()
            val need = map[start]!!
            for (i in 0 until k) {
                val key = start + i
                val cnt = map[key] ?: return false
                if (cnt < need) return false
                if (cnt == need) {
                    map.remove(key)
                } else {
                    map[key] = cnt - need
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isPossibleDivide(List<int> nums, int k) {
    if (nums.length % k != 0) return false;
    nums.sort();
    final Map<int, int> freq = {};
    for (var num in nums) {
      freq[num] = (freq[num] ?? 0) + 1;
    }
    for (var key in freq.keys.toList()) {
      int cnt = freq[key]!;
      if (cnt > 0) {
        for (int i = 0; i < k; ++i) {
          int need = key + i;
          int cur = freq[need] ?? 0;
          if (cur < cnt) return false;
          freq[need] = cur - cnt;
        }
      }
    }
    return true;
  }
}
```

## Golang

```go
package main

import "sort"

func isPossibleDivide(nums []int, k int) bool {
	if len(nums)%k != 0 {
		return false
	}
	sort.Ints(nums)
	freq := make(map[int]int, len(nums))
	for _, v := range nums {
		freq[v]++
	}
	for _, v := range nums {
		cnt := freq[v]
		if cnt == 0 {
			continue
		}
		for i := 0; i < k; i++ {
			cur := v + i
			c, ok := freq[cur]
			if !ok || c < cnt {
				return false
			}
			freq[cur] = c - cnt
		}
	}
	return true
}
```

## Ruby

```ruby
def is_possible_divide(nums, k)
  return false unless nums.length % k == 0
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  freq.keys.sort.each do |v|
    c = freq[v]
    next if c == 0
    (0...k).each do |i|
      nxt = v + i
      return false if freq[nxt] < c
      freq[nxt] -= c
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    import java.util.{TreeMap => JTreeMap}
    def isPossibleDivide(nums: Array[Int], k: Int): Boolean = {
        if (nums.length % k != 0) return false
        val map = new JTreeMap[Int, Int]()
        for (num <- nums) {
            map.put(num, map.getOrDefault(num, 0) + 1)
        }
        while (!map.isEmpty) {
            val firstKey = map.firstKey()
            val count = map.get(firstKey)
            var i = 0
            while (i < k) {
                val key = firstKey + i
                val cur = map.getOrDefault(key, 0)
                if (cur < count) return false
                if (cur == count) {
                    map.remove(key)
                } else {
                    map.put(key, cur - count)
                }
                i += 1
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_possible_divide(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        if n % k as usize != 0 {
            return false;
        }
        use std::collections::HashMap;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for &v in &nums {
            *cnt.entry(v).or_insert(0) += 1;
        }
        let mut keys: Vec<i32> = cnt.keys().cloned().collect();
        keys.sort_unstable();

        for &start in &keys {
            while let Some(&c) = cnt.get(&start) {
                if c == 0 {
                    break;
                }
                // need a consecutive block of length k starting at `start`
                for offset in 0..k {
                    let val = start + offset;
                    match cnt.get_mut(&val) {
                        Some(v) => {
                            if *v == 0 {
                                return false;
                            }
                            *v -= 1;
                        }
                        None => return false,
                    }
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-possible-divide nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (if (not (= (remainder (length nums) k) 0))
      #false
      (let* ([sorted (sort nums <)]
             [freq   (make-hash)])
        ;; build frequency map
        (for ([x sorted])
          (hash-set! freq x (+ 1 (hash-ref freq x 0))))
        (define keys (sort (hash-keys freq) <))
        (define impossible #f)
        (let loop ((ks keys))
          (when (and (not impossible) (pair? ks))
            (define v   (car ks))
            (define cnt (hash-ref freq v 0))
            (if (= cnt 0)
                (loop (cdr ks))
                (begin
                  ;; verify we have enough of each needed number
                  (for ([i (in-range v (+ v k))])
                    (when (< (hash-ref freq i 0) cnt)
                      (set! impossible #t)))
                  (unless impossible
                    (for ([i (in-range v (+ v k))])
                      (hash-set! freq i (- (hash-ref freq i) cnt))))
                  (loop (cdr ks))))))
        (not impossible))))
```

## Erlang

```erlang
-spec is_possible_divide([integer()], integer()) -> boolean().
is_possible_divide(Nums, K) ->
    case length(Nums) rem K of
        0 ->
            Sorted = lists:sort(Nums),
            Freq = lists:foldl(
                fun(X, Acc) ->
                    maps:update_with(X, fun(C) -> C + 1 end, 1, Acc)
                end,
                #{},
                Sorted
            ),
            Keys = lists:usort(Sorted),
            process(Keys, Freq, K);
        _ -> false
    end.

process([], _, _) -> true;
process([V | Rest], Map, K) ->
    case maps:get(V, Map, 0) of
        0 -> 
            process(Rest, Map, K);
        Count ->
            case remove_group(V, K, Count, Map) of
                {ok, NewMap} -> process(Rest, NewMap, K);
                error -> false
            end
    end.

remove_group(Start, K, Times, Map) ->
    remove_group(0, Start, K, Times, Map).

remove_group(Offset, _Start, K, _Times, Map) when Offset == K ->
    {ok, Map};
remove_group(Offset, Start, K, Times, Map) ->
    Num = Start + Offset,
    case maps:get(Num, Map, 0) of
        C when C >= Times ->
            NewMap = if C == Times -> maps:remove(Num, Map);
                        true       -> maps:put(Num, C - Times, Map)
                     end,
            remove_group(Offset + 1, Start, K, Times, NewMap);
        _ -> error
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_possible_divide(nums :: [integer], k :: integer) :: boolean
  def is_possible_divide(nums, k) do
    n = length(nums)

    if rem(n, k) != 0 do
      false
    else
      freq =
        Enum.reduce(nums, %{}, fn x, acc ->
          Map.update(acc, x, 1, &(&1 + 1))
        end)

      sorted_keys = Enum.sort(Map.keys(freq))

      {_, possible} =
        Enum.reduce_while(sorted_keys, {freq, true}, fn v, {fmap, _} ->
          cnt = Map.get(fmap, v, 0)

          if cnt == 0 do
            {:cont, {fmap, true}}
          else
            result =
              Enum.reduce_while(0..(k - 1), fmap, fn offset, acc_map ->
                cur = v + offset
                cur_cnt = Map.get(acc_map, cur, 0)

                if cur_cnt < cnt do
                  {:halt, :error}
                else
                  {:cont, Map.put(acc_map, cur, cur_cnt - cnt)}
                end
              end)

            case result do
              :error -> {:halt, {fmap, false}}
              updated_map -> {:cont, {updated_map, true}}
            end
          end
        end)

      possible
    end
  end
end
```
