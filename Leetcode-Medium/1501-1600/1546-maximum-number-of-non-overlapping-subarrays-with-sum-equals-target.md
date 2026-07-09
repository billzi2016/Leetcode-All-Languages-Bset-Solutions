# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

## Cpp

```cpp
class Solution {
public:
    int maxNonOverlapping(vector<int>& nums, int target) {
        unordered_set<long long> seen;
        seen.insert(0);
        long long cur = 0;
        int ans = 0;
        for (int v : nums) {
            cur += v;
            if (seen.count(cur - target)) {
                ++ans;
                // start a new segment after this index
                seen.clear();
                seen.insert(0);
                cur = 0;
            } else {
                seen.insert(cur);
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxNonOverlapping(int[] nums, int target) {
        Set<Integer> prefixSums = new HashSet<>();
        prefixSums.add(0);
        int sum = 0;
        int count = 0;
        for (int num : nums) {
            sum += num;
            if (prefixSums.contains(sum - target)) {
                count++;
                prefixSums.clear();
                prefixSums.add(sum);
            } else {
                prefixSums.add(sum);
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        cur_sum = 0
        seen = set([0])
        for num in nums:
            cur_sum += num
            if (cur_sum - target) in seen:
                ans += 1
                # start new segment after this subarray
                seen.clear()
                seen.add(cur_sum)
            else:
                seen.add(cur_sum)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ans = 0
        prefix_set = {0}
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - target in prefix_set:
                ans += 1
                # start a new segment after this subarray
                prefix_set.clear()
                prefix_set.add(0)
                cur_sum = 0
            else:
                prefix_set.add(cur_sum)
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int maxNonOverlapping(int* nums, int numsSize, int target) {
    if (numsSize == 0) return 0;
    int n = numsSize;

    /* hash table with open addressing */
    int cap = 1;
    while (cap < (n + 2) * 4) cap <<= 1;   // keep load factor low

    struct Entry {
        long long key;
        int val;
        char used;
    };
    struct Entry *table = (struct Entry *)calloc(cap, sizeof(struct Entry));
    if (!table) return 0;  // allocation failure fallback

    const int NEG_INF = -1000000000;

    /* hash function */
    #define HASH(k) ({ \
        unsigned long long h = (unsigned long long)(k); \
        h ^= h >> 33; \
        h *= 0xff51afd7ed558ccdULL; \
        h ^= h >> 33; \
        (int)(h & (cap - 1)); \
    })

    /* insert or update with max value */
    auto void put = ^(long long key, int val) {
        int idx = HASH(key);
        while (table[idx].used && table[idx].key != key)
            idx = (idx + 1) & (cap - 1);
        if (!table[idx].used) {
            table[idx].used = 1;
            table[idx].key = key;
            table[idx].val = val;
        } else if (val > table[idx].val) {
            table[idx].val = val;
        }
    };

    /* get value, return NEG_INF if not present */
    auto int get = ^(long long key) {
        int idx = HASH(key);
        while (table[idx].used) {
            if (table[idx].key == key) return table[idx].val;
            idx = (idx + 1) & (cap - 1);
        }
        return NEG_INF;
    };

    /* initialize map with prefix sum 0 having dp = 0 */
    put(0LL, 0);

    long long pref = 0;
    int dpPrev = 0;   // dp for previous position

    for (int i = 0; i < n; ++i) {
        pref += nums[i];
        int best = dpPrev;                     // not taking a subarray ending here
        int cand = get(pref - (long long)target);
        if (cand != NEG_INF && cand + 1 > best)
            best = cand + 1;
        put(pref, best);
        dpPrev = best;
    }

    free(table);
    return dpPrev;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxNonOverlapping(int[] nums, int target) {
        var seen = new System.Collections.Generic.HashSet<long>();
        seen.Add(0);
        long sum = 0;
        int count = 0;
        foreach (int num in nums) {
            sum += num;
            if (seen.Contains(sum - target)) {
                count++;
                // start a new segment after this subarray
                seen.Clear();
                seen.Add(0);
                sum = 0;
            } else {
                seen.Add(sum);
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var maxNonOverlapping = function(nums, target) {
    let count = 0;
    let prefixSum = 0;
    const seen = new Set();
    seen.add(0);
    
    for (const num of nums) {
        prefixSum += num;
        if (seen.has(prefixSum - target)) {
            // Found a non‑overlapping subarray ending here
            count++;
            // Reset for the next segment
            seen.clear();
            seen.add(0);
            prefixSum = 0;
        } else {
            seen.add(prefixSum);
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function maxNonOverlapping(nums: number[], target: number): number {
    let count = 0;
    let prefixSum = 0;
    let seen = new Set<number>();
    seen.add(0);
    for (const num of nums) {
        prefixSum += num;
        if (seen.has(prefixSum - target)) {
            count++;
            // reset after taking a subarray
            prefixSum = 0;
            seen.clear();
            seen.add(0);
        } else {
            seen.add(prefixSum);
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function maxNonOverlapping($nums, $target) {
        $count = 0;
        $sum = 0;
        $set = [0 => true];
        foreach ($nums as $num) {
            $sum += $num;
            if (isset($set[$sum - $target])) {
                $count++;
                // start a new segment
                $set = [0 => true];
                $sum = 0;
            } else {
                $set[$sum] = true;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func maxNonOverlapping(_ nums: [Int], _ target: Int) -> Int {
        var count = 0
        var currentSum = 0
        var prefixSet: Set<Int> = [0]
        
        for num in nums {
            currentSum += num
            if prefixSet.contains(currentSum - target) {
                count += 1
                // Reset after taking a subarray
                prefixSet.removeAll()
                prefixSet.insert(0)
                currentSum = 0
            } else {
                prefixSet.insert(currentSum)
            }
        }
        
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNonOverlapping(nums: IntArray, target: Int): Int {
        var count = 0
        var prefixSum = 0L
        val seen = HashSet<Long>()
        seen.add(0L)
        for (num in nums) {
            prefixSum += num.toLong()
            if (seen.contains(prefixSum - target)) {
                count++
                // start a new segment after this subarray
                prefixSum = 0L
                seen.clear()
                seen.add(0L)
            } else {
                seen.add(prefixSum)
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int maxNonOverlapping(List<int> nums, int target) {
    int ans = 0;
    int sum = 0;
    Set<int> seen = {0};
    for (int num in nums) {
      sum += num;
      if (seen.contains(sum - target)) {
        ans++;
        seen.clear();
        seen.add(0);
        sum = 0;
      } else {
        seen.add(sum);
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxNonOverlapping(nums []int, target int) int {
    seen := map[int]struct{}{0: {}}
    curSum := 0
    count := 0

    for _, v := range nums {
        curSum += v
        if _, ok := seen[curSum-target]; ok {
            count++
            // reset for next segment
            seen = map[int]struct{}{0: {}}
            curSum = 0
        } else {
            seen[curSum] = struct{}{}
        }
    }

    return count
}
```

## Ruby

```ruby
def max_non_overlapping(nums, target)
  cur_sum = 0
  seen = {0 => true}
  count = 0

  nums.each do |num|
    cur_sum += num
    if seen.key?(cur_sum - target)
      count += 1
      cur_sum = 0
      seen.clear
      seen[0] = true
    else
      seen[cur_sum] = true
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  def maxNonOverlapping(nums: Array[Int], target: Int): Int = {
    val seen = mutable.HashSet[Int]()
    seen.add(0)
    var sum = 0
    var count = 0
    for (num <- nums) {
      sum += num
      if (seen.contains(sum - target)) {
        count += 1
        seen.clear()
        seen.add(0)
        sum = 0
      } else {
        seen.add(sum)
      }
    }
    count
  }
}
```

## Rust

```rust
use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn max_non_overlapping(nums: Vec<i32>, target: i32) -> i32 {
        let mut seen: HashSet<i64> = HashSet::new();
        seen.insert(0);
        let mut prefix_sum: i64 = 0;
        let mut count: i32 = 0;
        for &v in nums.iter() {
            prefix_sum += v as i64;
            if seen.contains(&(prefix_sum - target as i64)) {
                count += 1;
                seen.clear();
                seen.insert(0);
                prefix_sum = 0;
            } else {
                seen.insert(prefix_sum);
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (max-non-overlapping nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((lst nums) (cur 0) (ans 0)
             (s (let ((h (make-hash))) (hash-set! h 0 #t) h)))
    (if (null? lst)
        ans
        (let* ((x (car lst))
               (new-cur (+ cur x)))
          (if (hash-has-key? s (- new-cur target))
              (let ((new-s (let ((h (make-hash))) (hash-set! h new-cur #t) h)))
                (loop (cdr lst) new-cur (+ ans 1) new-s))
              (begin
                (hash-set! s new-cur #t)
                (loop (cdr lst) new-cur ans s)))))))
```

## Erlang

```erlang
-spec max_non_overlapping(Nums :: [integer()], Target :: integer()) -> integer().
max_non_overlapping(Nums, Target) ->
    loop(Nums, 0, #{0 => true}, 0, Target).

loop([], _CumSum, _Set, Count, _Target) ->
    Count;
loop([H|T], CumSum, Set, Count, Target) ->
    NewCum = CumSum + H,
    case maps:is_key(NewCum - Target, Set) of
        true ->
            NewSet = #{NewCum => true},
            loop(T, NewCum, NewSet, Count + 1, Target);
        false ->
            NewSet = Set#{NewCum => true},
            loop(T, NewCum, NewSet, Count, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_non_overlapping(nums :: [integer], target :: integer) :: integer
  def max_non_overlapping(nums, target) do
    {count, _, _} =
      Enum.reduce(nums, {0, 0, MapSet.new([0])}, fn num, {cnt, sum, set} ->
        new_sum = sum + num

        if MapSet.member?(set, new_sum - target) do
          {cnt + 1, 0, MapSet.new([0])}
        else
          {cnt, new_sum, MapSet.put(set, new_sum)}
        end
      end)

    count
  end
end
```
