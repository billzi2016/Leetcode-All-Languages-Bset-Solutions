# 0560. Subarray Sum Equals K

## Cpp

```cpp
class Solution {
public:
    int subarraySum(std::vector<int>& nums, int k) {
        std::unordered_map<long long, int> cnt;
        cnt[0] = 1;
        long long sum = 0;
        int ans = 0;
        for (int num : nums) {
            sum += num;
            auto it = cnt.find(sum - k);
            if (it != cnt.end()) ans += it->second;
            ++cnt[sum];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        java.util.Map<Integer, Integer> prefixCount = new java.util.HashMap<>();
        prefixCount.put(0, 1);
        int sum = 0;
        int result = 0;
        for (int num : nums) {
            sum += num;
            result += prefixCount.getOrDefault(sum - k, 0);
            prefixCount.put(sum, prefixCount.getOrDefault(sum, 0) + 1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        cum_sum = 0
        prefix_counts = {0: 1}
        for num in nums:
            cum_sum += num
            if cum_sum - k in prefix_counts:
                count += prefix_counts[cum_sum - k]
            prefix_counts[cum_sum] = prefix_counts.get(cum_sum, 0) + 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        prefix_counts = {0: 1}
        for num in nums:
            cum_sum += num
            count += prefix_counts.get(cum_sum - k, 0)
            prefix_counts[cum_sum] = prefix_counts.get(cum_sum, 0) + 1
        return count
```

## C

```c
#include <stdlib.h>

int subarraySum(int* nums, int numsSize, int k) {
    const int MOD = 20011; // a prime number for hashing
    struct Entry {
        long long key;
        int val;
        struct Entry *next;
    };
    
    struct Entry **table = (struct Entry **)calloc(MOD, sizeof(struct Entry *));
    
    /* insert prefix sum 0 with count 1 */
    long long initKey = 0;
    int idx = ((initKey % MOD) + MOD) % MOD;
    struct Entry *e = (struct Entry *)malloc(sizeof(struct Entry));
    e->key = initKey;
    e->val = 1;
    e->next = NULL;
    table[idx] = e;
    
    long long sum = 0;
    int count = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
        
        /* look for (sum - k) */
        long long target = sum - k;
        idx = ((target % MOD) + MOD) % MOD;
        struct Entry *cur = table[idx];
        while (cur) {
            if (cur->key == target) {
                count += cur->val;
                break;
            }
            cur = cur->next;
        }
        
        /* add current prefix sum */
        idx = ((sum % MOD) + MOD) % MOD;
        cur = table[idx];
        while (cur) {
            if (cur->key == sum) {
                cur->val++;
                break;
            }
            cur = cur->next;
        }
        if (!cur) {
            struct Entry *ne = (struct Entry *)malloc(sizeof(struct Entry));
            ne->key = sum;
            ne->val = 1;
            ne->next = table[idx];
            table[idx] = ne;
        }
    }
    
    /* clean up */
    for (int i = 0; i < MOD; ++i) {
        struct Entry *cur = table[i];
        while (cur) {
            struct Entry *nxt = cur->next;
            free(cur);
            cur = nxt;
        }
    }
    free(table);
    
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int SubarraySum(int[] nums, int k) {
        var prefixCounts = new Dictionary<long, int>();
        prefixCounts[0] = 1;
        long sum = 0;
        int result = 0;

        foreach (int num in nums) {
            sum += num;
            long needed = sum - k;
            if (prefixCounts.TryGetValue(needed, out int cnt)) {
                result += cnt;
            }

            if (prefixCounts.ContainsKey(sum)) {
                prefixCounts[sum] = prefixCounts[sum] + 1;
            } else {
                prefixCounts[sum] = 1;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let count = 0;
    let prefix = 0;
    const freq = new Map();
    freq.set(0, 1);
    
    for (const num of nums) {
        prefix += num;
        if (freq.has(prefix - k)) {
            count += freq.get(prefix - k);
        }
        freq.set(prefix, (freq.get(prefix) || 0) + 1);
    }
    
    return count;
};
```

## Typescript

```typescript
function subarraySum(nums: number[], k: number): number {
    const prefixCount = new Map<number, number>();
    prefixCount.set(0, 1);
    let sum = 0;
    let result = 0;
    for (const num of nums) {
        sum += num;
        const need = sum - k;
        if (prefixCount.has(need)) {
            result += prefixCount.get(need)!;
        }
        prefixCount.set(sum, (prefixCount.get(sum) ?? 0) + 1);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarraySum($nums, $k) {
        $count = 0;
        $sum = 0;
        $map = [0 => 1]; // prefix sum 0 occurs once

        foreach ($nums as $num) {
            $sum += $num;
            $need = $sum - $k;
            if (isset($map[$need])) {
                $count += $map[$need];
            }
            if (isset($map[$sum])) {
                $map[$sum] += 1;
            } else {
                $map[$sum] = 1;
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var prefixCount = [Int: Int]()
        prefixCount[0] = 1
        var currentSum = 0
        var result = 0
        
        for num in nums {
            currentSum += num
            if let cnt = prefixCount[currentSum - k] {
                result += cnt
            }
            prefixCount[currentSum, default: 0] += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {
        val freq = HashMap<Long, Int>()
        var sum = 0L
        var result = 0L
        freq[0L] = 1
        for (num in nums) {
            sum += num.toLong()
            val need = sum - k
            result += freq.getOrDefault(need, 0)
            freq[sum] = freq.getOrDefault(sum, 0) + 1
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int subarraySum(List<int> nums, int k) {
    final Map<int, int> prefixCounts = {0: 1};
    int sum = 0;
    int result = 0;
    for (final num in nums) {
      sum += num;
      if (prefixCounts.containsKey(sum - k)) {
        result += prefixCounts[sum - k]!;
      }
      prefixCounts.update(sum, (v) => v + 1, ifAbsent: () => 1);
    }
    return result;
  }
}
```

## Golang

```go
func subarraySum(nums []int, k int) int {
	count, sum := 0, 0
	prefix := map[int]int{0: 1}
	for _, v := range nums {
		sum += v
		if c, ok := prefix[sum-k]; ok {
			count += c
		}
		prefix[sum]++
	}
	return count
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)
  prefix_counts = Hash.new(0)
  prefix_counts[0] = 1
  current_sum = 0
  result = 0

  nums.each do |num|
    current_sum += num
    result += prefix_counts[current_sum - k]
    prefix_counts[current_sum] += 1
  end

  result
end
```

## Scala

```scala
object Solution {
    def subarraySum(nums: Array[Int], k: Int): Int = {
        import scala.collection.mutable

        val freq = mutable.Map[Int, Int]().withDefaultValue(0)
        freq(0) = 1

        var sum = 0
        var count = 0

        for (num <- nums) {
            sum += num
            val need = sum - k
            count += freq.getOrElse(need, 0)
            freq(sum) = freq(sum) + 1
        }

        count
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut prefix_counts: HashMap<i64, i32> = HashMap::new();
        prefix_counts.insert(0, 1);
        let mut cum_sum: i64 = 0;
        let mut result: i64 = 0;
        let target = k as i64;

        for num in nums {
            cum_sum += num as i64;
            if let Some(&cnt) = prefix_counts.get(&(cum_sum - target)) {
                result += cnt as i64;
            }
            *prefix_counts.entry(cum_sum).or_insert(0) += 1;
        }

        result as i32
    }
}
```

## Racket

```racket
(define/contract (subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((freq (make-hash))
         (_    (hash-set! freq 0 1))   ; prefix sum 0 occurs once
         (cum 0)
         (cnt 0))
    (for ([x nums])
      (set! cum (+ cum x))
      (define need (- cum k))
      (when (hash-has-key? freq need)
        (set! cnt (+ cnt (hash-ref freq need))))
      (hash-set! freq cum
                 (+ 1 (if (hash-has-key? freq cum) (hash-ref freq cum) 0))))
    cnt))
```

## Erlang

```erlang
-spec subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
subarray_sum(Nums, K) ->
    subarray_sum(Nums, K, 0, #{0 => 1}, 0).

subarray_sum([], _K, _Sum, _Map, Count) ->
    Count;
subarray_sum([H|T], K, Sum, Map, Count) ->
    NewSum = Sum + H,
    Add = maps:get(NewSum - K, Map, 0),
    NewCount = Count + Add,
    Freq = maps:get(NewSum, Map, 0) + 1,
    NewMap = Map#{NewSum => Freq},
    subarray_sum(T, K, NewSum, NewMap, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec subarray_sum(nums :: [integer], k :: integer) :: integer
  def subarray_sum(nums, k) do
    {_sum, count, _map} =
      Enum.reduce(nums, {0, 0, %{0 => 1}}, fn num, {curr_sum, cnt, m} ->
        new_sum = curr_sum + num
        add = Map.get(m, new_sum - k, 0)
        new_cnt = cnt + add
        new_m = Map.update(m, new_sum, 1, &(&1 + 1))
        {new_sum, new_cnt, new_m}
      end)

    count
  end
end
```
