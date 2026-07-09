# 2364. Count Number of Bad Pairs

## Cpp

```cpp
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n = nums.size();
        unordered_map<long long, long long> cnt;
        cnt.reserve(n * 2);
        for (int i = 0; i < n; ++i) {
            long long key = (long long)nums[i] - i;
            ++cnt[key];
        }
        long long totalPairs = (long long)n * (n - 1) / 2;
        long long goodPairs = 0;
        for (auto& p : cnt) {
            long long f = p.second;
            goodPairs += f * (f - 1) / 2;
        }
        return totalPairs - goodPairs;
    }
};
```

## Java

```java
class Solution {
    public long countBadPairs(int[] nums) {
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        long badPairs = 0;
        for (int i = 0; i < nums.length; i++) {
            int key = nums[i] - i;
            int good = map.getOrDefault(key, 0);
            badPairs += i - good;
            map.put(key, good + 1);
        }
        return badPairs;
    }
}
```

## Python

```python
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        freq = {}
        good_pairs = 0
        for i, v in enumerate(nums):
            key = v - i
            cnt = freq.get(key, 0)
            good_pairs += cnt
            freq[key] = cnt + 1
        return total_pairs - good_pairs
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff_counts = Counter()
        for i, v in enumerate(nums):
            diff_counts[v - i] += 1
        good_pairs = sum(c * (c - 1) // 2 for c in diff_counts.values())
        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs
```

## C

```c
#include <stdlib.h>

static int cmp_ll(const void *a, const void *b) {
    long long va = *(const long long *)a;
    long long vb = *(const long long *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

long long countBadPairs(int* nums, int numsSize) {
    if (numsSize <= 1) return 0LL;
    
    long long *diffs = (long long *)malloc(sizeof(long long) * numsSize);
    for (int i = 0; i < numsSize; ++i) {
        diffs[i] = (long long)nums[i] - i;
    }
    
    qsort(diffs, numsSize, sizeof(long long), cmp_ll);
    
    long long goodPairs = 0;
    long long run = 1;
    for (int i = 1; i < numsSize; ++i) {
        if (diffs[i] == diffs[i - 1]) {
            ++run;
        } else {
            goodPairs += run * (run - 1) / 2;
            run = 1;
        }
    }
    goodPairs += run * (run - 1) / 2; // last run
    
    free(diffs);
    
    long long totalPairs = (long long)numsSize * (numsSize - 1) / 2;
    return totalPairs - goodPairs;
}
```

## Csharp

```csharp
public class Solution
{
    public long CountBadPairs(int[] nums)
    {
        int n = nums.Length;
        long totalPairs = ((long)n * (n - 1)) / 2;
        long goodPairs = 0;

        var diffCount = new Dictionary<long, int>();

        for (int i = 0; i < n; i++)
        {
            long key = i - (long)nums[i];
            if (diffCount.TryGetValue(key, out int cnt))
            {
                goodPairs += cnt;
                diffCount[key] = cnt + 1;
            }
            else
            {
                diffCount[key] = 1;
            }
        }

        return totalPairs - goodPairs;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countBadPairs = function(nums) {
    const diffCount = new Map();
    for (let i = 0; i < nums.length; i++) {
        const key = i - nums[i];
        diffCount.set(key, (diffCount.get(key) || 0) + 1);
    }
    const n = nums.length;
    let totalPairs = n * (n - 1) / 2;
    let goodPairs = 0;
    for (const cnt of diffCount.values()) {
        goodPairs += cnt * (cnt - 1) / 2;
    }
    return totalPairs - goodPairs;
};
```

## Typescript

```typescript
function countBadPairs(nums: number[]): number {
    const freq = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        const key = nums[i] - i;
        freq.set(key, (freq.get(key) ?? 0) + 1);
    }
    let goodPairs = 0;
    for (const cnt of freq.values()) {
        goodPairs += cnt * (cnt - 1) / 2;
    }
    const n = nums.length;
    const totalPairs = n * (n - 1) / 2;
    return totalPairs - goodPairs;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countBadPairs($nums) {
        $diffCount = [];
        $badPairs = 0;
        foreach ($nums as $i => $val) {
            $diff = $i - $val;
            $good = $diffCount[$diff] ?? 0;
            $badPairs += $i - $good;
            $diffCount[$diff] = $good + 1;
        }
        return $badPairs;
    }
}
```

## Swift

```swift
class Solution {
    func countBadPairs(_ nums: [Int]) -> Int {
        var diffCount = [Int: Int]()
        var badPairs: Int64 = 0
        for i in 0..<nums.count {
            let key = nums[i] - i
            let good = diffCount[key] ?? 0
            badPairs += Int64(i - good)
            diffCount[key] = good + 1
        }
        return Int(badPairs)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countBadPairs(nums: IntArray): Long {
        val freq = HashMap<Long, Long>()
        var goodPairs = 0L
        for (i in nums.indices) {
            val key = i.toLong() - nums[i].toLong()
            val cnt = freq.getOrDefault(key, 0L)
            goodPairs += cnt
            freq[key] = cnt + 1
        }
        val n = nums.size.toLong()
        val totalPairs = n * (n - 1) / 2
        return totalPairs - goodPairs
    }
}
```

## Dart

```dart
class Solution {
  int countBadPairs(List<int> nums) {
    int n = nums.length;
    int totalPairs = n * (n - 1) ~/ 2;
    Map<int, int> freq = {};
    int goodPairs = 0;
    for (int i = 0; i < n; ++i) {
      int key = nums[i] - i;
      int count = freq[key] ?? 0;
      goodPairs += count;
      freq[key] = count + 1;
    }
    return totalPairs - goodPairs;
  }
}
```

## Golang

```go
func countBadPairs(nums []int) int64 {
	n := int64(len(nums))
	total := n * (n - 1) / 2

	var good int64
	diffCount := make(map[int]int64)

	for i, v := range nums {
		key := v - i
		if cnt, ok := diffCount[key]; ok {
			good += cnt
		}
		diffCount[key]++
	}

	return total - good
}
```

## Ruby

```ruby
def count_bad_pairs(nums)
  n = nums.length
  total = n * (n - 1) / 2
  freq = Hash.new(0)
  nums.each_with_index do |val, i|
    key = i - val
    freq[key] += 1
  end
  good = 0
  freq.each_value { |c| good += c * (c - 1) / 2 }
  total - good
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def countBadPairs(nums: Array[Int]): Long = {
    val freq = mutable.HashMap[Long, Long]()
    var bad: Long = 0L
    for (i <- nums.indices) {
      val diff = nums(i).toLong - i.toLong
      val goodPrev = freq.getOrElse(diff, 0L)
      bad += i.toLong - goodPrev
      freq.update(diff, goodPrev + 1L)
    }
    bad
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_bad_pairs(nums: Vec<i32>) -> i64 {
        let mut freq: HashMap<i64, i64> = HashMap::new();
        let mut bad: i64 = 0;
        for (i, &val) in nums.iter().enumerate() {
            let key = val as i64 - i as i64;
            let same = *freq.get(&key).unwrap_or(&0);
            bad += i as i64 - same;
            freq.entry(key).and_modify(|e| *e += 1).or_insert(1);
        }
        bad
    }
}
```

## Racket

```racket
(define/contract (count-bad-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)]
         [total (/ (* n (- n 1)) 2)])
    (let ([freq (make-hash)]
          [good 0])
      (for ([i (in-range n)])
        (define diff (- (vector-ref v i) i))
        (define cnt (hash-ref freq diff 0))
        (set! good (+ good cnt))
        (hash-set! freq diff (+ cnt 1)))
      (- total good))))
```

## Erlang

```erlang
-spec count_bad_pairs(Nums :: [integer()]) -> integer().
count_bad_pairs(Nums) ->
    {FreqMap, _} = lists:foldl(
        fun (Num, {AccMap, Idx}) ->
            Key = Num - Idx,
            NewCnt = maps:get(Key, AccMap, 0) + 1,
            {maps:put(Key, NewCnt, AccMap), Idx + 1}
        end,
        {#{}, 0},
        Nums
    ),
    GoodPairs = maps:fold(
        fun (_Key, Cnt, Sum) ->
            Sum + (Cnt * (Cnt - 1)) div 2
        end,
        0,
        FreqMap
    ),
    N = length(Nums),
    TotalPairs = N * (N - 1) div 2,
    TotalPairs - GoodPairs.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_bad_pairs(nums :: [integer]) :: integer
  def count_bad_pairs(nums) do
    freq_map =
      Enum.reduce(Enum.with_index(nums), %{}, fn {num, idx}, acc ->
        key = num - idx
        Map.update(acc, key, 1, &(&1 + 1))
      end)

    n = length(nums)
    total_pairs = div(n * (n - 1), 2)

    good_pairs =
      Enum.reduce(freq_map, 0, fn {_key, cnt}, acc ->
        acc + div(cnt * (cnt - 1), 2)
      end)

    total_pairs - good_pairs
  end
end
```
