# 0523. Continuous Subarray Sum

## Cpp

```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if (k == 0) {
            for (size_t i = 1; i < nums.size(); ++i)
                if (nums[i] == 0 && nums[i - 1] == 0)
                    return true;
            return false;
        }
        unordered_map<int, int> modIndex;
        modIndex[0] = -1;
        long long prefixMod = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            prefixMod = (prefixMod + nums[i]) % k;
            int curMod = (int)prefixMod;
            auto it = modIndex.find(curMod);
            if (it != modIndex.end()) {
                if (i - it->second >= 2)
                    return true;
            } else {
                modIndex[curMod] = i;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        java.util.Map<Integer, Integer> modIndex = new java.util.HashMap<>();
        modIndex.put(0, -1);
        int prefixMod = 0;
        for (int i = 0; i < nums.length; i++) {
            prefixMod += nums[i];
            if (k != 0) {
                prefixMod %= k;
            }
            Integer prev = modIndex.get(prefixMod);
            if (prev != null) {
                if (i - prev >= 2) {
                    return true;
                }
            } else {
                modIndex.put(prefixMod, i);
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_index = {0: -1}
        prefix_mod = 0
        for i, num in enumerate(nums):
            if k != 0:
                prefix_mod = (prefix_mod + num) % k
            else:
                prefix_mod += num
            if prefix_mod in mod_index:
                if i - mod_index[prefix_mod] > 1:
                    return True
            else:
                mod_index[prefix_mod] = i
        return False
```

## Python3

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_index = {0: -1}
        prefix_mod = 0
        for i, num in enumerate(nums):
            if k != 0:
                prefix_mod = (prefix_mod + num) % k
            else:
                prefix_mod += num
            if prefix_mod in mod_index:
                if i - mod_index[prefix_mod] > 1:
                    return True
            else:
                mod_index[prefix_mod] = i
        return False
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

struct Entry {
    int key;
    int val;
    bool used;
};

static int next_power_of_two(int n) {
    int p = 1;
    while (p < n) p <<= 1;
    return p;
}

static int hashmap_get(struct Entry *table, int cap, int key, bool *found) {
    uint32_t h = ((uint32_t)key * 2654435761u) & (cap - 1);
    while (true) {
        if (!table[h].used) {
            *found = false;
            return -1;
        }
        if (table[h].key == key) {
            *found = true;
            return table[h].val;
        }
        h = (h + 1) & (cap - 1);
    }
}

static void hashmap_put_if_absent(struct Entry *table, int cap, int key, int val) {
    uint32_t h = ((uint32_t)key * 2654435761u) & (cap - 1);
    while (true) {
        if (!table[h].used) {
            table[h].used = true;
            table[h].key = key;
            table[h].val = val;
            return;
        }
        if (table[h].key == key) {
            // already present, keep earliest index
            return;
        }
        h = (h + 1) & (cap - 1);
    }
}

bool checkSubarraySum(int* nums, int numsSize, int k) {
    if (numsSize < 2) return false;

    int cap = next_power_of_two(numsSize * 2);
    struct Entry *table = calloc((size_t)cap, sizeof(struct Entry));
    if (!table) return false; // allocation failure fallback

    hashmap_put_if_absent(table, cap, 0, -1); // prefix mod 0 at index -1

    long long prefix = 0;
    for (int i = 0; i < numsSize; ++i) {
        prefix += nums[i];
        int mod = (int)(prefix % k);
        bool found;
        int prevIdx = hashmap_get(table, cap, mod, &found);
        if (found) {
            if (i - prevIdx >= 2) {
                free(table);
                return true;
            }
        } else {
            hashmap_put_if_absent(table, cap, mod, i);
        }
    }

    free(table);
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckSubarraySum(int[] nums, int k)
    {
        if (k == 0)
        {
            // Need at least two consecutive zeros
            for (int i = 1; i < nums.Length; i++)
                if (nums[i] == 0 && nums[i - 1] == 0)
                    return true;
            return false;
        }

        var modIndex = new Dictionary<int, int>();
        modIndex[0] = -1; // prefix sum modulo k before any element
        int prefixMod = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            prefixMod = (prefixMod + nums[i]) % k;
            if (modIndex.TryGetValue(prefixMod, out int prevIdx))
            {
                if (i - prevIdx > 1)
                    return true;
            }
            else
            {
                modIndex[prefixMod] = i;
            }
        }

        return false;
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
var checkSubarraySum = function(nums, k) {
    // Special case when k is 0: need a subarray of at least length 2 summing to 0,
    // which can only happen with two consecutive zeros.
    if (k === 0) {
        for (let i = 1; i < nums.length; i++) {
            if (nums[i] === 0 && nums[i - 1] === 0) return true;
        }
        return false;
    }

    const modIndexMap = new Map();
    // prefix sum modulo k == 0 at index -1 (empty prefix)
    modIndexMap.set(0, -1);
    let prefixMod = 0;

    for (let i = 0; i < nums.length; i++) {
        prefixMod = (prefixMod + nums[i]) % k;
        // Ensure non‑negative modulo (JS can produce negative when k is negative,
        // but per constraints k > 0, so this is just a safeguard)
        if (prefixMod < 0) prefixMod += k;

        if (modIndexMap.has(prefixMod)) {
            const prevIdx = modIndexMap.get(prefixMod);
            if (i - prevIdx > 1) return true; // subarray length at least 2
        } else {
            modIndexMap.set(prefixMod, i);
        }
    }

    return false;
};
```

## Typescript

```typescript
function checkSubarraySum(nums: number[], k: number): boolean {
    if (k === 0) {
        for (let i = 1; i < nums.length; i++) {
            if (nums[i] === 0 && nums[i - 1] === 0) return true;
        }
        return false;
    }

    const modMap = new Map<number, number>();
    modMap.set(0, -1);
    let prefix = 0;

    for (let i = 0; i < nums.length; i++) {
        prefix += nums[i];
        prefix %= k;
        if (prefix < 0) prefix += k; // ensure non‑negative

        const prevIdx = modMap.get(prefix);
        if (prevIdx !== undefined) {
            if (i - prevIdx >= 2) return true;
        } else {
            modMap.set(prefix, i);
        }
    }

    return false;
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
    function checkSubarraySum($nums, $k) {
        $n = count($nums);
        if ($k == 0) {
            for ($i = 0; $i < $n - 1; $i++) {
                if ($nums[$i] == 0 && $nums[$i + 1] == 0) {
                    return true;
                }
            }
            return false;
        }

        $modSeen = [0 => -1];
        $prefixMod = 0;

        for ($i = 0; $i < $n; $i++) {
            $prefixMod = ($prefixMod + $nums[$i]) % $k;
            if (array_key_exists($prefixMod, $modSeen)) {
                if ($i - $modSeen[$prefixMod] > 1) {
                    return true;
                }
            } else {
                $modSeen[$prefixMod] = $i;
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func checkSubarraySum(_ nums: [Int], _ k: Int) -> Bool {
        if k == 0 {
            var consecutiveZeros = 0
            for num in nums {
                if num == 0 {
                    consecutiveZeros += 1
                    if consecutiveZeros >= 2 { return true }
                } else {
                    consecutiveZeros = 0
                }
            }
            return false
        }
        
        var modIndex = [Int: Int]()
        modIndex[0] = -1
        var prefixSum = 0
        
        for i in 0..<nums.count {
            prefixSum += nums[i]
            let mod = ((prefixSum % k) + k) % k   // ensure non‑negative
            
            if let prev = modIndex[mod] {
                if i - prev >= 2 { return true }
            } else {
                modIndex[mod] = i
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
        if (k == 0) {
            for (i in 0 until nums.size - 1) {
                if (nums[i] == 0 && nums[i + 1] == 0) return true
            }
            return false
        }
        val modIndex = HashMap<Int, Int>()
        modIndex[0] = -1
        var prefixSum = 0L
        for (i in nums.indices) {
            prefixSum += nums[i].toLong()
            val mod = (prefixSum % k).toInt()
            val prevIdx = modIndex[mod]
            if (prevIdx != null) {
                if (i - prevIdx > 1) return true
            } else {
                modIndex[mod] = i
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool checkSubarraySum(List<int> nums, int k) {
    int prefixMod = 0;
    final Map<int, int> modSeen = {0: -1};

    for (int i = 0; i < nums.length; i++) {
      prefixMod = (prefixMod + nums[i]) % k;

      if (modSeen.containsKey(prefixMod)) {
        if (i - modSeen[prefixMod]! > 1) {
          return true;
        }
      } else {
        modSeen[prefixMod] = i;
      }
    }

    return false;
  }
}
```

## Golang

```go
func checkSubarraySum(nums []int, k int) bool {
	if k == 0 {
		for i := 1; i < len(nums); i++ {
			if nums[i] == 0 && nums[i-1] == 0 {
				return true
			}
		}
		return false
	}
	modSeen := map[int]int{0: -1}
	prefixMod := 0
	for i, num := range nums {
		prefixMod = int((int64(prefixMod) + int64(num)) % int64(k))
		if prevIdx, ok := modSeen[prefixMod]; ok {
			if i-prevIdx >= 2 {
				return true
			}
		} else {
			modSeen[prefixMod] = i
		}
	}
	return false
}
```

## Ruby

```ruby
def check_subarray_sum(nums, k)
  mod_index = {0 => -1}
  sum_mod = 0
  nums.each_with_index do |num, i|
    if k != 0
      sum_mod = (sum_mod + num) % k
    else
      sum_mod += num
    end
    if mod_index.key?(sum_mod)
      return true if i - mod_index[sum_mod] > 1
    else
      mod_index[sum_mod] = i
    end
  end
  false
end
```

## Scala

```scala
object Solution {
  def checkSubarraySum(nums: Array[Int], k: Int): Boolean = {
    if (k == 0) {
      for (i <- 1 until nums.length) {
        if (nums(i) == 0 && nums(i - 1) == 0) return true
      }
      false
    } else {
      val modSeen = scala.collection.mutable.Map[Int, Int]()
      modSeen(0) = -1
      var prefixMod = 0
      for (i <- nums.indices) {
        prefixMod = ((prefixMod + nums(i)) % k + k) % k
        if (modSeen.contains(prefixMod)) {
          if (i - modSeen(prefixMod) > 1) return true
        } else {
          modSeen(prefixMod) = i
        }
      }
      false
    }
  }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {
        if k == 0 {
            for i in 1..nums.len() {
                if nums[i] == 0 && nums[i - 1] == 0 {
                    return true;
                }
            }
            return false;
        }

        let mut map: HashMap<i64, i32> = HashMap::new();
        map.insert(0, -1);
        let mut prefix: i64 = 0;
        let k_i64 = k as i64;

        for (i, &num) in nums.iter().enumerate() {
            prefix = (prefix + num as i64).rem_euclid(k_i64);
            if let Some(&prev_idx) = map.get(&prefix) {
                if (i as i32) - prev_idx >= 2 {
                    return true;
                }
            } else {
                map.insert(prefix, i as i32);
            }
        }

        false
    }
}
```

## Racket

```racket
(define/contract (check-subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let ((mod-index (make-hash)))
    (hash-set! mod-index 0 -1) ; prefix sum 0 at index -1
    (let loop ((i 0) (prefix 0) (rest nums))
      (if (null? rest)
          #f
          (let* ((num (car rest))
                 (new-prefix (if (= k 0)
                                 (+ prefix num)
                                 (mod (+ prefix num) k)))
                 (rem new-prefix))
            (cond
              [(hash-has-key? mod-index rem)
               (let ((prev (hash-ref mod-index rem)))
                 (if (>= (- i prev) 2)
                     #t
                     (loop (+ i 1) new-prefix (cdr rest))))]
              [else
               (hash-set! mod-index rem i)
               (loop (+ i 1) new-prefix (cdr rest))]))))))
```

## Erlang

```erlang
-spec check_subarray_sum(Nums :: [integer()], K :: integer()) -> boolean().
check_subarray_sum(Nums, K) when K =/= 0 ->
    check_subarray_sum(Nums, K, 0, #{0 => -1}, 0).

check_subarray_sum([], _K, _Idx, _Map, _Pref) ->
    false;
check_subarray_sum([H|T], K, Idx, Map, Pref) ->
    NewPref = (Pref + H) rem K,
    case maps:find(NewPref, Map) of
        {ok, FirstIdx} ->
            if Idx - FirstIdx >= 2 ->
                    true;
               true ->
                    check_subarray_sum(T, K, Idx+1, Map, NewPref)
            end;
        error ->
            NewMap = maps:put(NewPref, Idx, Map),
            check_subarray_sum(T, K, Idx+1, NewMap, NewPref)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_subarray_sum(nums :: [integer], k :: integer) :: boolean
  def check_subarray_sum(nums, k) do
    cond do
      k == 0 ->
        has_consecutive_zeros?(nums)

      true ->
        has_subarray_multiple?(nums, k)
    end
  end

  defp has_consecutive_zeros?(nums) do
    Enum.reduce_while(1..length(nums) - 1, false, fn i, _acc ->
      if Enum.at(nums, i) == 0 and Enum.at(nums, i - 1) == 0 do
        {:halt, true}
      else
        {:cont, false}
      end
    end)
  end

  defp has_subarray_multiple?(nums, k) do
    {_, found} =
      Enum.reduce_while(Enum.with_index(nums), {%{0 => -1}, 0}, fn {val, idx},
                                                                   {mod_map, prefix_mod} ->
        new_mod = rem(prefix_mod + val, k)

        case Map.get(mod_map, new_mod) do
          nil ->
            {:cont, {Map.put_new(mod_map, new_mod, idx), new_mod}}

          prev_idx when idx - prev_idx >= 2 ->
            {:halt, {mod_map, true}}

          _prev_idx ->
            {:cont, {mod_map, new_mod}}
        end
      end)

    found == true
  end
end
```
