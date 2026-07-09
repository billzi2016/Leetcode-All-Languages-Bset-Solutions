# 0446. Arithmetic Slices II - Subsequence

## Cpp

```cpp
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        vector<unordered_map<long long, long long>> dp(n);
        for (int i = 0; i < n; ++i) {
            dp[i].reserve(i);
            for (int j = 0; j < i; ++j) {
                long long diff = (long long)nums[i] - (long long)nums[j];
                long long cnt = 0;
                auto it = dp[j].find(diff);
                if (it != dp[j].end()) cnt = it->second;
                ans += cnt;
                dp[i][diff] += cnt + 1;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length;
        @SuppressWarnings("unchecked")
        java.util.HashMap<Long, Long>[] dp = new java.util.HashMap[n];
        for (int i = 0; i < n; i++) {
            dp[i] = new java.util.HashMap<>();
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                long diff = (long) nums[i] - (long) nums[j];
                long cnt = dp[j].getOrDefault(diff, 0L);
                ans += cnt;
                long newCnt = cnt + 1;
                dp[i].put(diff, dp[i].getOrDefault(diff, 0L) + newCnt);
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
import collections

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(n)]
        total = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt_j = dp[j][diff]
                total += cnt_j
                dp[i][diff] += cnt_j + 1
        return total
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]
                ans += cnt
                dp[i][diff] += cnt + 1
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct Entry {
    long long diff;
    int count;
    struct Entry *next;
} Entry;

static unsigned int hash_diff(long long diff, int size) {
    unsigned long long x = (unsigned long long)diff;
    x ^= x >> 33;
    return (unsigned int)(x % (unsigned long long)size);
}

static Entry* find_entry(Entry **table, int size, long long diff) {
    unsigned int h = hash_diff(diff, size);
    Entry *cur = table[h];
    while (cur) {
        if (cur->diff == diff) return cur;
        cur = cur->next;
    }
    return NULL;
}

static Entry* get_or_create(Entry **table, int size, long long diff) {
    unsigned int h = hash_diff(diff, size);
    Entry *cur = table[h];
    while (cur) {
        if (cur->diff == diff) return cur;
        cur = cur->next;
    }
    Entry *node = (Entry *)malloc(sizeof(Entry));
    node->diff = diff;
    node->count = 0;
    node->next = table[h];
    table[h] = node;
    return node;
}

int numberOfArithmeticSlices(int* nums, int numsSize) {
    if (numsSize < 3) return 0;
    const int HASH_SIZE = 2003;               // prime > max possible entries per index
    Entry ***dp = (Entry ***)malloc(sizeof(Entry **) * numsSize);
    for (int i = 0; i < numsSize; ++i) {
        dp[i] = (Entry **)calloc(HASH_SIZE, sizeof(Entry *));
    }

    long long ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = 0; j < i; ++j) {
            long long diff = (long long)nums[i] - (long long)nums[j];
            Entry *e_j = find_entry(dp[j], HASH_SIZE, diff);
            int cnt_j = e_j ? e_j->count : 0;
            ans += cnt_j;                         // extend existing sequences to length >=3
            Entry *e_i = get_or_create(dp[i], HASH_SIZE, diff);
            e_i->count += cnt_j + 1;               // add new pair (j,i) and extended ones
        }
    }

    for (int i = 0; i < numsSize; ++i) {
        for (int b = 0; b < HASH_SIZE; ++b) {
            Entry *cur = dp[i][b];
            while (cur) {
                Entry *tmp = cur;
                cur = cur->next;
                free(tmp);
            }
        }
        free(dp[i]);
    }
    free(dp);

    return (int)ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int NumberOfArithmeticSlices(int[] nums) {
        int n = nums.Length;
        var dp = new Dictionary<long, long>[n];
        for (int i = 0; i < n; i++) dp[i] = new Dictionary<long, long>();
        long total = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                long diff = (long)nums[i] - (long)nums[j];
                long cnt = 0;
                dp[j].TryGetValue(diff, out cnt);
                total += cnt;
                long prev = 0;
                dp[i].TryGetValue(diff, out prev);
                dp[i][diff] = prev + cnt + 1;
            }
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
    const n = nums.length;
    if (n < 3) return 0;
    const dp = new Array(n);
    for (let i = 0; i < n; i++) dp[i] = new Map();
    let total = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            const diff = nums[i] - nums[j];
            const cntJ = dp[j].get(diff) || 0;
            total += cntJ;
            const prev = dp[i].get(diff) || 0;
            dp[i].set(diff, prev + cntJ + 1);
        }
    }
    return total;
};
```

## Typescript

```typescript
function numberOfArithmeticSlices(nums: number[]): number {
    const n = nums.length;
    const dp: Array<Map<number, number>> = new Array(n);
    for (let i = 0; i < n; i++) dp[i] = new Map();
    let result = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            const diff = nums[i] - nums[j];
            const cntJ = dp[j].get(diff) ?? 0;
            result += cntJ;
            const prev = dp[i].get(diff) ?? 0;
            dp[i].set(diff, prev + cntJ + 1);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfArithmeticSlices($nums) {
        $n = count($nums);
        if ($n < 3) return 0;
        $dp = array_fill(0, $n, []);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                $diff = $nums[$i] - $nums[$j];
                $key = (string)$diff;
                $cnt = $dp[$j][$key] ?? 0;
                $ans += $cnt;
                $dp[$i][$key] = ($dp[$i][$key] ?? 0) + $cnt + 1;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfArithmeticSlices(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 3 { return 0 }
        var dp = Array(repeating: [Int64:Int](), count: n)
        var result = 0
        for i in 0..<n {
            for j in 0..<i {
                let diff = Int64(nums[i]) - Int64(nums[j])
                let cnt = dp[j][diff] ?? 0
                result += cnt
                dp[i][diff] = (dp[i][diff] ?? 0) + cnt + 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfArithmeticSlices(nums: IntArray): Int {
        val n = nums.size
        val dp = Array(n) { HashMap<Long, Long>() }
        var total = 0L
        for (i in 0 until n) {
            for (j in 0 until i) {
                val diff = nums[i].toLong() - nums[j].toLong()
                val cntJ = dp[j][diff] ?: 0L
                total += cntJ
                dp[i][diff] = (dp[i][diff] ?: 0L) + cntJ + 1L
            }
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfArithmeticSlices(List<int> nums) {
    int n = nums.length;
    if (n < 3) return 0;
    List<Map<int, int>> dp = List.generate(n, (_) => {});
    int total = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < i; ++j) {
        int diff = nums[i] - nums[j];
        int cntAtJ = dp[j][diff] ?? 0;
        total += cntAtJ;
        dp[i][diff] = (dp[i][diff] ?? 0) + cntAtJ + 1;
      }
    }
    return total;
  }
}
```

## Golang

```go
func numberOfArithmeticSlices(nums []int) int {
	n := len(nums)
	dp := make([]map[int64]int, n)
	var ans int64
	for i := 0; i < n; i++ {
		dp[i] = make(map[int64]int)
		for j := 0; j < i; j++ {
			diff := int64(nums[i]) - int64(nums[j])
			cnt := dp[j][diff]
			ans += int64(cnt)
			dp[i][diff] = dp[i][diff] + cnt + 1
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
def number_of_arithmetic_slices(nums)
  n = nums.length
  dp = Array.new(n) { Hash.new(0) }
  ans = 0
  (0...n).each do |i|
    (0...i).each do |j|
      diff = nums[i] - nums[j]
      cnt = dp[j][diff]
      ans += cnt
      dp[i][diff] += cnt + 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numberOfArithmeticSlices(nums: Array[Int]): Int = {
        val n = nums.length
        val dp = Array.fill[scala.collection.mutable.Map[Long, Long]](n)(scala.collection.mutable.Map.empty)
        var total: Long = 0L

        for (i <- 0 until n) {
            for (j <- 0 until i) {
                val diff = nums(i).toLong - nums(j).toLong
                val cntJ = dp(j).getOrElse(diff, 0L)
                total += cntJ
                val newCnt = cntJ + 1L
                dp(i)(diff) = dp(i).getOrElse(diff, 0L) + newCnt
            }
        }

        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_arithmetic_slices(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        let mut dp: Vec<std::collections::HashMap<i64, i64>> = vec![std::collections::HashMap::new(); n];
        let mut ans: i64 = 0;
        for i in 0..n {
            for j in 0..i {
                let diff = nums[i] as i64 - nums[j] as i64;
                let cnt_j = *dp[j].get(&diff).unwrap_or(&0);
                ans += cnt_j;
                let entry = dp[i].entry(diff).or_insert(0);
                *entry += cnt_j + 1;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-arithmetic-slices nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (dp (make-vector n)))
    ;; initialize a hash table for each index
    (for ([i (in-range n)])
      (vector-set! dp i (make-hash)))
    (let ((ans 0))
      (for ([i (in-range n)])
        (for ([j (in-range i)])
          (let* ((diff (- (vector-ref v i) (vector-ref v j)))
                 (h_j (vector-ref dp j))
                 (cnt_j (hash-ref h_j diff 0))
                 (h_i (vector-ref dp i))
                 (existing (hash-ref h_i diff 0)))
            (set! ans (+ ans cnt_j))
            (hash-set! h_i diff (+ existing cnt_j 1)))))
      ans)))
```

## Erlang

```erlang
-spec number_of_arithmetic_slices(Nums :: [integer()]) -> integer().
number_of_arithmetic_slices(Nums) ->
    Vals = list_to_tuple(Nums),
    N = tuple_size(Vals),
    {Ans, _} =
        lists:foldl(
            fun(I, {Acc, DPMaps}) ->
                Vi = element(I + 1, Vals),
                {MapI, Acc2} =
                    case I of
                        0 ->
                            {#{}, Acc};
                        _ ->
                            PrevPairs = lists:zip(lists:seq(0, I - 1), DPMaps),
                            lists:foldl(
                                fun({J, MapJ}, {MAcc, AAcc}) ->
                                    Vj = element(J + 1, Vals),
                                    Diff = Vi - Vj,
                                    Cj = maps:get(Diff, MapJ, 0),
                                    ANew = AAcc + Cj,
                                    PrevCnt = maps:get(Diff, MAcc, 0),
                                    MNew = maps:put(Diff, PrevCnt + Cj + 1, MAcc),
                                    {MNew, ANew}
                                end,
                                {#{}, Acc},
                                PrevPairs
                            )
                    end,
                {Acc2, DPMaps ++ [MapI]}
            end,
            {0, []},
            lists:seq(0, N - 1)
        ),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_arithmetic_slices(nums :: [integer]) :: integer
  def number_of_arithmetic_slices(nums) do
    n = length(nums)
    if n < 3, do: 0, else: compute(nums, n)
  end

  defp compute(nums, n) do
    nums_t = List.to_tuple(nums)
    arr = :array.new(n, default: %{})

    {total, _} =
      Enum.reduce(0..(n - 1), {0, arr}, fn i, {tot, a} ->
        cur_num = elem(nums_t, i)

        {new_tot, cur_map} =
          Enum.reduce(0..(i - 1), {tot, %{}}, fn j, {t_acc, map_acc} ->
            diff = cur_num - elem(nums_t, j)
            cnt_j = a |> :array.get(j) |> Map.get(diff, 0)
            t_new = t_acc + cnt_j
            map_new = Map.update(map_acc, diff, cnt_j + 1, &(&1 + cnt_j + 1))
            {t_new, map_new}
          end)

        a = :array.set(i, cur_map, a)
        {new_tot, a}
      end)

    total
  end
end
```
