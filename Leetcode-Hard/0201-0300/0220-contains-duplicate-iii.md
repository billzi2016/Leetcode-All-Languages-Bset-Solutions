# 0220. Contains Duplicate III

## Cpp

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) return false;
        std::set<long long> window;
        for (int i = 0; i < (int)nums.size(); ++i) {
            long long val = nums[i];
            auto it = window.lower_bound(val - (long long)valueDiff);
            if (it != window.end() && *it <= val + (long long)valueDiff)
                return true;
            window.insert(val);
            if ((int)window.size() > indexDiff) {
                window.erase((long long)nums[i - indexDiff]);
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        if (valueDiff < 0 || nums == null || nums.length == 0) return false;
        java.util.TreeSet<Long> set = new java.util.TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            long cur = (long) nums[i];
            Long lower = set.ceiling(cur - (long) valueDiff);
            if (lower != null && lower <= cur + (long) valueDiff) {
                return true;
            }
            set.add(cur);
            if (i >= indexDiff) {
                set.remove((long) nums[i - indexDiff]);
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0 or indexDiff <= 0:
            return False

        width = valueDiff + 1  # bucket size, avoid zero division
        bucket = {}

        for i, num in enumerate(nums):
            b_id = num // width

            if b_id in bucket:
                return True

            left = b_id - 1
            right = b_id + 1

            if left in bucket and abs(num - bucket[left]) < width:
                return True
            if right in bucket and abs(bucket[right] - num) < width:
                return True

            bucket[b_id] = num

            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                del bucket[old_num // width]

        return False
```

## Python3

```python
from bisect import bisect_left, insort
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0 or not nums:
            return False
        window: List[int] = []
        for i, num in enumerate(nums):
            pos = bisect_left(window, num)
            if pos > 0 and abs(num - window[pos - 1]) <= valueDiff:
                return True
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True
            insort(window, num)
            if i >= indexDiff:
                old = nums[i - indexDiff]
                del_pos = bisect_left(window, old)
                # remove the exact element (there is guaranteed to be one)
                window.pop(del_pos)
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct Node {
    long long key;
    long long val;
    struct Node* next;
} Node;

static inline long long getBucket(long long x, long long w) {
    long long id = x / w;
    if (x < 0 && x % w != 0) id--;
    return id;
}

bool containsNearbyAlmostDuplicate(int* nums, int numsSize, int indexDiff, int valueDiff) {
    if (valueDiff < 0 || indexDiff <= 0) return false;

    long long w = (long long)valueDiff + 1;          // bucket size
    const int HASH_SIZE = 200003;                    // a prime number > 2*10^5
    Node** table = (Node**)calloc(HASH_SIZE, sizeof(Node*));
    if (!table) return false;

    for (int i = 0; i < numsSize; ++i) {
        long long num = (long long)nums[i];
        long long bucketId = getBucket(num, w);
        size_t idx = ((unsigned long long)bucketId) % HASH_SIZE;

        // same bucket
        for (Node* cur = table[idx]; cur; cur = cur->next) {
            if (cur->key == bucketId) {
                free(table);
                return true;
            }
        }

        // neighbor buckets
        size_t idxPrev = ((unsigned long long)(bucketId - 1)) % HASH_SIZE;
        for (Node* cur = table[idxPrev]; cur; cur = cur->next) {
            if (cur->key == bucketId - 1 && llabs(cur->val - num) <= valueDiff) {
                free(table);
                return true;
            }
        }

        size_t idxNext = ((unsigned long long)(bucketId + 1)) % HASH_SIZE;
        for (Node* cur = table[idxNext]; cur; cur = cur->next) {
            if (cur->key == bucketId + 1 && llabs(cur->val - num) <= valueDiff) {
                free(table);
                return true;
            }
        }

        // insert current
        Node* node = (Node*)malloc(sizeof(Node));
        node->key = bucketId;
        node->val = num;
        node->next = table[idx];
        table[idx] = node;

        // maintain window size
        if (i > indexDiff) {
            int oldIdx = i - indexDiff - 1;
            long long oldNum = (long long)nums[oldIdx];
            long long oldBucket = getBucket(oldNum, w);
            size_t delIdx = ((unsigned long long)oldBucket) % HASH_SIZE;
            Node** pp = &table[delIdx];
            while (*pp) {
                if ((*pp)->key == oldBucket) {
                    Node* tmp = *pp;
                    *pp = (*pp)->next;
                    free(tmp);
                    break;
                }
                pp = &((*pp)->next);
            }
        }
    }

    // clean up (optional for LeetCode)
    for (int i = 0; i < HASH_SIZE; ++i) {
        Node* cur = table[i];
        while (cur) {
            Node* nxt = cur->next;
            free(cur);
            cur = nxt;
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
    public bool ContainsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff)
    {
        if (indexDiff <= 0 || valueDiff < 0) return false;

        var comparer = Comparer<(long val, int idx)>.Create((a, b) =>
        {
            int cmp = a.val.CompareTo(b.val);
            return cmp != 0 ? cmp : a.idx.CompareTo(b.idx);
        });

        SortedSet<(long val, int idx)> set = new SortedSet<(long, int)>(comparer);
        long t = valueDiff;

        for (int i = 0; i < nums.Length; i++)
        {
            long cur = nums[i];
            var lower = (cur - t, int.MinValue);
            var upper = (cur + t, int.MaxValue);

            foreach (var _ in set.GetViewBetween(lower, upper))
                return true;

            set.Add((cur, i));

            if (i >= indexDiff)
                set.Remove(((long)nums[i - indexDiff], i - indexDiff));
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} indexDiff
 * @param {number} valueDiff
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff) {
    if (valueDiff < 0) return false;
    const bucketSize = valueDiff + 1; // width of each bucket
    const buckets = new Map(); // bucketId -> number

    for (let i = 0; i < nums.length; ++i) {
        const num = nums[i];
        const bucketId = Math.floor(num / bucketSize);

        if (buckets.has(bucketId)) return true;

        const left = buckets.get(bucketId - 1);
        if (left !== undefined && Math.abs(num - left) <= valueDiff) return true;

        const right = buckets.get(bucketId + 1);
        if (right !== undefined && Math.abs(num - right) <= valueDiff) return true;

        buckets.set(bucketId, num);

        if (i >= indexDiff) {
            const oldNum = nums[i - indexDiff];
            const oldBucketId = Math.floor(oldNum / bucketSize);
            buckets.delete(oldBucketId);
        }
    }

    return false;
};
```

## Typescript

```typescript
function containsNearbyAlmostDuplicate(nums: number[], indexDiff: number, valueDiff: number): boolean {
    if (valueDiff < 0) return false;
    const window: number[] = [];

    const lowerBound = (arr: number[], target: number): number => {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (arr[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    };

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        // Find the smallest element >= num - valueDiff
        const pos = lowerBound(window, num - valueDiff);
        if (pos < window.length && Math.abs(window[pos] - num) <= valueDiff) {
            return true;
        }

        // Insert current number into sorted window
        const insertPos = lowerBound(window, num);
        window.splice(insertPos, 0, num);

        // Remove element that is now out of the allowed index range
        if (i >= indexDiff) {
            const outNum = nums[i - indexDiff];
            const removePos = lowerBound(window, outNum);
            if (removePos < window.length && window[removePos] === outNum) {
                window.splice(removePos, 1);
            }
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
     * @param Integer $indexDiff
     * @param Integer $valueDiff
     * @return Boolean
     */
    function containsNearbyAlmostDuplicate($nums, $indexDiff, $valueDiff) {
        $n = count($nums);
        if ($valueDiff < 0 || $indexDiff <= 0) return false;
        $width = $valueDiff + 1; // bucket size

        $bucket = [];

        // helper to compute bucket id using floor division
        $getBucketId = function($num) use ($width) {
            if ($num >= 0) {
                return intdiv($num, $width);
            } else {
                // floor division for negatives
                return intdiv($num - $width + 1, $width);
            }
        };

        for ($i = 0; $i < $n; ++$i) {
            $num = $nums[$i];
            $id = $getBucketId($num);

            // same bucket -> difference <= valueDiff
            if (isset($bucket[$id])) {
                return true;
            }

            // check neighboring buckets
            if (isset($bucket[$id - 1]) && abs($num - $bucket[$id - 1]) <= $valueDiff) {
                return true;
            }
            if (isset($bucket[$id + 1]) && abs($num - $bucket[$id + 1]) <= $valueDiff) {
                return true;
            }

            // insert current number into its bucket
            $bucket[$id] = $num;

            // maintain sliding window of size indexDiff
            if ($i >= $indexDiff) {
                $oldNum = $nums[$i - $indexDiff];
                $oldId = $getBucketId($oldNum);
                unset($bucket[$oldId]);
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func containsNearbyAlmostDuplicate(_ nums: [Int], _ indexDiff: Int, _ valueDiff: Int) -> Bool {
        if valueDiff < 0 { return false }
        let w = Int64(valueDiff) + 1
        var buckets = [Int64: Int64]()
        
        for i in 0..<nums.count {
            let x = Int64(nums[i])
            let bucketId: Int64
            if x >= 0 {
                bucketId = x / w
            } else {
                bucketId = ((x + 1) / w) - 1
            }
            
            // Same bucket -> difference <= valueDiff
            if buckets[bucketId] != nil { return true }
            
            // Check neighboring buckets
            if let left = buckets[bucketId - 1], abs(x - left) <= Int64(valueDiff) {
                return true
            }
            if let right = buckets[bucketId + 1], abs(x - right) <= Int64(valueDiff) {
                return true
            }
            
            // Insert current element into its bucket
            buckets[bucketId] = x
            
            // Maintain sliding window of size indexDiff
            if i >= indexDiff {
                let oldX = Int64(nums[i - indexDiff])
                let oldBucket: Int64
                if oldX >= 0 {
                    oldBucket = oldX / w
                } else {
                    oldBucket = ((oldX + 1) / w) - 1
                }
                buckets.removeValue(forKey: oldBucket)
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun containsNearbyAlmostDuplicate(nums: IntArray, indexDiff: Int, valueDiff: Int): Boolean {
        if (valueDiff < 0) return false
        val set = java.util.TreeSet<Long>()
        for (i in nums.indices) {
            val num = nums[i].toLong()
            val lower = set.ceiling(num - valueDiff)
            if (lower != null && lower <= num + valueDiff) return true
            set.add(num)
            if (set.size > indexDiff) {
                set.remove(nums[i - indexDiff].toLong())
            }
        }
        return false
    }
}
```

## Dart

```dart
import 'dart:core';

class Solution {
  bool containsNearbyAlmostDuplicate(List<int> nums, int indexDiff, int valueDiff) {
    if (valueDiff < 0) return false;
    int w = valueDiff + 1; // bucket size
    Map<int, int> buckets = {};

    int getBucket(int x) {
      int id = x ~/ w;
      if (x < 0 && x % w != 0) id -= 1;
      return id;
    }

    for (int i = 0; i < nums.length; i++) {
      int bucketId = getBucket(nums[i]);

      // Same bucket
      if (buckets.containsKey(bucketId)) {
        return true;
      }
      // Adjacent buckets
      int leftId = bucketId - 1;
      if (buckets.containsKey(leftId) &&
          (nums[i] - buckets[leftId]!).abs() <= valueDiff) {
        return true;
      }
      int rightId = bucketId + 1;
      if (buckets.containsKey(rightId) &&
          (buckets[rightId]! - nums[i]).abs() <= valueDiff) {
        return true;
      }

      // Insert current element
      buckets[bucketId] = nums[i];

      // Remove the element that's now out of the sliding window
      if (i >= indexDiff) {
        int oldBucketId = getBucket(nums[i - indexDiff]);
        buckets.remove(oldBucketId);
      }
    }
    return false;
  }
}
```

## Golang

```go
func containsNearbyAlmostDuplicate(nums []int, indexDiff int, valueDiff int) bool {
	if valueDiff < 0 || indexDiff <= 0 {
		return false
	}
	w := int64(valueDiff) + 1 // bucket size, at least 1
	buckets := make(map[int64]int64)

	getBucketID := func(x, width int64) int64 {
		id := x / width
		if x < 0 && x%width != 0 {
			id--
		}
		return id
	}

	absInt64 := func(a int64) int64 {
		if a < 0 {
			return -a
		}
		return a
	}

	for i, v := range nums {
		x := int64(v)
		bid := getBucketID(x, w)

		if _, ok := buckets[bid]; ok {
			return true
		}
		if val, ok := buckets[bid-1]; ok && absInt64(x-val) <= int64(valueDiff) {
			return true
		}
		if val, ok := buckets[bid+1]; ok && absInt64(x-val) <= int64(valueDiff) {
			return true
		}

		buckets[bid] = x

		if i >= indexDiff {
			oldX := int64(nums[i-indexDiff])
			oldBid := getBucketID(oldX, w)
			delete(buckets, oldBid)
		}
	}
	return false
}
```

## Ruby

```ruby
def contains_nearby_almost_duplicate(nums, index_diff, value_diff)
  w = value_diff + 1
  buckets = {}
  nums.each_with_index do |num, i|
    id = num.div(w)
    return true if buckets.key?(id)
    if buckets.key?(id - 1) && (num - buckets[id - 1]).abs <= value_diff
      return true
    end
    if buckets.key?(id + 1) && (buckets[id + 1] - num).abs <= value_diff
      return true
    end
    buckets[id] = num
    if i >= index_diff
      old_id = nums[i - index_diff].div(w)
      buckets.delete(old_id)
    end
  end
  false
end
```

## Scala

```scala
object Solution {
  import java.util.TreeSet

  def containsNearbyAlmostDuplicate(nums: Array[Int], indexDiff: Int, valueDiff: Int): Boolean = {
    if (valueDiff < 0) return false
    val set = new TreeSet[Long]()
    val t = valueDiff.toLong
    var i = 0
    while (i < nums.length) {
      val cur = nums(i).toLong
      val candidate = set.ceiling(cur - t)
      if (candidate != null && candidate <= cur + t) return true
      set.add(cur)
      if (i >= indexDiff) {
        set.remove(nums(i - indexDiff).toLong)
      }
      i += 1
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn contains_nearby_almost_duplicate(nums: Vec<i32>, index_diff: i32, value_diff: i32) -> bool {
        let k = index_diff as usize;
        let t = value_diff as i64;
        use std::collections::BTreeSet;
        let mut set = BTreeSet::new();

        for (i, &num) in nums.iter().enumerate() {
            let cur = num as i64;

            if let Some(&candidate) = set.range(cur - t..).next() {
                if candidate <= cur + t {
                    return true;
                }
            }

            set.insert(cur);

            if i >= k {
                let old = nums[i - k] as i64;
                set.remove(&old);
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (contains-nearby-almost-duplicate nums indexDiff valueDiff)
  (-> (listof exact-integer?) exact-integer? exact-integer? boolean?)
  (let* ((n (length nums))
         (size (+ valueDiff 1))) ; bucket size, at least 1
    (let loop ((i 0) (hash (make-hash)))
      (if (= i n)
          #f
          (let* ((num (list-ref nums i))
                 (bucket-id
                  (let* ((b (quotient num size))
                         (adjusted (if (< num 0) (sub1 b) b)))
                    adjusted)))
            (cond
              [(hash-has-key? hash bucket-id) #t]
              [(and (hash-has-key? hash (- bucket-id 1))
                    (<= (abs (- num (hash-ref hash (- bucket-id 1)))) valueDiff)) #t]
              [(and (hash-has-key? hash (+ bucket-id 1))
                    (<= (abs (- num (hash-ref hash (+ bucket-id 1)))) valueDiff)) #t]
              [else
               (hash-set! hash bucket-id num)
               (when (>= i indexDiff)
                 (let* ((old-num (list-ref nums (- i indexDiff)))
                        (old-bucket
                         (let* ((b (quotient old-num size))
                                (adjusted (if (< old-num 0) (sub1 b) b)))
                           adjusted)))
                   (hash-remove! hash old-bucket)))
               (loop (add1 i) hash)]))))))
```

## Erlang

```erlang
-spec contains_nearby_almost_duplicate(Nums :: [integer()], IndexDiff :: integer(), ValueDiff :: integer()) -> boolean().
contains_nearby_almost_duplicate(Nums, IndexDiff, ValueDiff) ->
    case ValueDiff < 0 of
        true -> false;
        false ->
            BucketSize = ValueDiff + 1,
            loop(Nums, IndexDiff, ValueDiff, BucketSize, #{}, queue:new(), 0)
    end.

loop([], _IndexDiff, _ValueDiff, _BucketSize, _Map, _Queue, _Idx) ->
    false;
loop([Num|Rest], IndexDiff, ValueDiff, BucketSize, Map, Queue, Idx) ->
    BucketId = bucket_id(Num, BucketSize),
    case maps:is_key(BucketId, Map) of
        true -> true;
        false ->
            case check_neighbors(BucketId, Num, ValueDiff, Map) of
                true -> true;
                false ->
                    NewMap = maps:put(BucketId, Num, Map),
                    NewQueue = queue:in({BucketId, Num}, Queue),
                    {FinalMap, FinalQueue} =
                        if Idx >= IndexDiff ->
                                {{value, {OldBucket,_}}, Q1} = queue:out(NewQueue),
                                {maps:remove(OldBucket, NewMap), Q1};
                           true -> {NewMap, NewQueue}
                        end,
                    loop(Rest, IndexDiff, ValueDiff, BucketSize, FinalMap, FinalQueue, Idx + 1)
            end
    end.

bucket_id(Num, Size) ->
    case Num >= 0 of
        true -> Num div Size;
        false -> (Num + 1) div Size - 1
    end.

check_neighbors(BucketId, Num, ValueDiff, Map) ->
    NeighborIds = [BucketId - 1, BucketId + 1],
    lists:any(fun(NId) ->
                      case maps:find(NId, Map) of
                          {ok, Other} -> abs(Num - Other) =< ValueDiff;
                          error -> false
                      end
              end, NeighborIds).
```

## Elixir

```elixir
defmodule Solution do
  @spec contains_nearby_almost_duplicate(nums :: [integer], index_diff :: integer, value_diff :: integer) :: boolean
  def contains_nearby_almost_duplicate(nums, index_diff, value_diff) do
    bucket_size = value_diff + 1
    nums_tuple = List.to_tuple(nums)
    n = tuple_size(nums_tuple)

    result =
      Enum.reduce_while(0..(n - 1), %{}, fn i, buckets ->
        num = elem(nums_tuple, i)
        bucket_id = get_bucket(num, bucket_size)

        cond do
          Map.has_key?(buckets, bucket_id) ->
            {:halt, true}

          (v = Map.get(buckets, bucket_id - 1)) && abs(num - v) <= value_diff ->
            {:halt, true}

          (v = Map.get(buckets, bucket_id + 1)) && abs(num - v) <= value_diff ->
            {:halt, true}

          true ->
            buckets = Map.put(buckets, bucket_id, num)

            if i >= index_diff do
              old_num = elem(nums_tuple, i - index_diff)
              old_bucket = get_bucket(old_num, bucket_size)
              buckets = Map.delete(buckets, old_bucket)
            end

            {:cont, buckets}
        end
      end)

    case result do
      true -> true
      _ -> false
    end
  end

  defp get_bucket(num, size) do
    div_res = div(num, size)

    if num < 0 and rem(num, size) != 0 do
      div_res - 1
    else
      div_res
    end
  end
end
```
