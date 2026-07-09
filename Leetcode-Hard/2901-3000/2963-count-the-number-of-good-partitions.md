# 2963. Count the Number of Good Partitions

## Cpp

```cpp
class Solution {
public:
    int numberOfGoodPartitions(vector<int>& nums) {
        const int MOD = 1000000007;
        unordered_map<int,int> first, last;
        first.reserve(nums.size()*2);
        last.reserve(nums.size()*2);
        for (int i = 0; i < (int)nums.size(); ++i) {
            int v = nums[i];
            if (!first.count(v)) first[v] = i;
            last[v] = i;
        }
        long long segments = 0;
        int curRight = -1;
        for (int i = 0; i < (int)nums.size(); ++i) {
            curRight = max(curRight, last[nums[i]]);
            if (i == curRight) ++segments;
        }
        // answer = 2^(segments-1) mod MOD
        long long exp = segments - 1;
        long long base = 2, res = 1;
        while (exp > 0) {
            if (exp & 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return (int)res;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int numberOfGoodPartitions(int[] nums) {
        int n = nums.length;
        java.util.HashMap<Integer, Integer> lastPos = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            lastPos.put(nums[i], i);
        }
        long blocks = 0;
        int curMax = -1;
        for (int i = 0; i < n; i++) {
            curMax = Math.max(curMax, lastPos.get(nums[i]));
            if (i == curMax) {
                blocks++;
            }
        }
        long ans = modPow(2L, blocks - 1);
        return (int) ans;
    }
    
    private long modPow(long base, long exp) {
        long result = 1L;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfGoodPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        last = {}
        for i, v in enumerate(nums):
            last[v] = i

        blocks = 0
        cur_end = -1
        for i, v in enumerate(nums):
            cur_end = max(cur_end, last[v])
            if i == cur_end:
                blocks += 1

        return pow(2, blocks - 1, MOD)
```

## Python3

```python
from typing import List

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        last = {}
        for i, v in enumerate(nums):
            last[v] = i
        blocks = 0
        right = -1
        for i, v in enumerate(nums):
            if last[v] > right:
                right = last[v]
            if i == right:
                blocks += 1
        return pow(2, blocks - 1, MOD)
```

## C

```c
#include <stdlib.h>
#include <stdint.h>

#define MOD 1000000007ULL
/* simple open-addressing hash map */
typedef struct {
    int key;
    int val;
    char used;
} Entry;

static inline void hashmap_put(Entry *table, int mask, int key, int val) {
    uint32_t h = ((uint32_t)key * 2654435761u) & mask;
    while (table[h].used && table[h].key != key) {
        h = (h + 1) & mask;
    }
    table[h].key = key;
    table[h].val = val;
    table[h].used = 1;
}

static inline int hashmap_get(Entry *table, int mask, int key) {
    uint32_t h = ((uint32_t)key * 2654435761u) & mask;
    while (table[h].used) {
        if (table[h].key == key) return table[h].val;
        h = (h + 1) & mask;
    }
    return -1; /* should not happen for existing keys */
}

static unsigned long long modpow(unsigned long long base, unsigned long long exp) {
    unsigned long long res = 1ULL;
    while (exp) {
        if (exp & 1ULL) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1ULL;
    }
    return res;
}

int numberOfGoodPartitions(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    /* hash size: power of two > 2 * numsSize */
    int sz = 1;
    while (sz <= numsSize * 2) sz <<= 1;
    int mask = sz - 1;
    Entry *table = (Entry *)calloc(sz, sizeof(Entry));
    if (!table) return 0; /* allocation failure */

    /* first pass: record last occurrence of each value */
    for (int i = 0; i < numsSize; ++i) {
        hashmap_put(table, mask, nums[i], i);
    }

    int segments = 0;
    int curMax = -1;
    for (int i = 0; i < numsSize; ++i) {
        int lastPos = hashmap_get(table, mask, nums[i]);
        if (lastPos > curMax) curMax = lastPos;
        if (i == curMax) {
            ++segments;
            curMax = -1;
        }
    }

    free(table);
    return (int)modpow(2ULL, (unsigned long long)(segments ? segments - 1 : 0));
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    public int NumberOfGoodPartitions(int[] nums) {
        int n = nums.Length;
        var lastPos = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            lastPos[nums[i]] = i;
        }
        long segments = 0;
        int currentMax = -1;
        for (int i = 0; i < n; i++) {
            int lp = lastPos[nums[i]];
            if (lp > currentMax) currentMax = lp;
            if (i == currentMax) {
                segments++;
            }
        }
        long exp = segments - 1;
        long result = 1;
        long baseVal = 2;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * baseVal) % MOD;
            }
            baseVal = (baseVal * baseVal) % MOD;
            exp >>= 1;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodPartitions = function(nums) {
    const n = nums.length;
    const lastPos = new Map();
    for (let i = 0; i < n; i++) {
        lastPos.set(nums[i], i);
    }
    let segments = 0;
    let curMax = -1;
    for (let i = 0; i < n; i++) {
        const r = lastPos.get(nums[i]);
        if (r > curMax) curMax = r;
        if (i === curMax) segments++;
    }
    const MOD = 1000000007n;
    let exp = BigInt(segments - 1);
    let base = 2n;
    let result = 1n;
    while (exp > 0n) {
        if (exp & 1n) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    return Number(result);
};
```

## Typescript

```typescript
function numberOfGoodPartitions(nums: number[]): number {
    const MOD = 1000000007;
    const posMap = new Map<number, { first: number; last: number }>();
    for (let i = 0; i < nums.length; i++) {
        const v = nums[i];
        if (!posMap.has(v)) {
            posMap.set(v, { first: i, last: i });
        } else {
            posMap.get(v)!.last = i;
        }
    }

    let right = -1;
    let blocks = 0;
    for (let i = 0; i < nums.length; i++) {
        const v = nums[i];
        const lastPos = posMap.get(v)!.last;
        if (lastPos > right) right = lastPos;
        if (i === right) blocks++;
    }

    let exp = blocks - 1;
    let result = 1;
    let base = 2;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
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
    function numberOfGoodPartitions($nums) {
        $mod = 1000000007;
        $n = count($nums);
        // record last occurrence of each value
        $last = [];
        for ($i = 0; $i < $n; $i++) {
            $last[$nums[$i]] = $i;
        }

        $segments = 0;
        $curEnd = -1;
        for ($i = 0; $i < $n; $i++) {
            $val = $nums[$i];
            if ($last[$val] > $curEnd) {
                $curEnd = $last[$val];
            }
            if ($i == $curEnd) {
                $segments++;
            }
        }

        // compute 2^(segments-1) mod MOD
        $exp = $segments - 1;
        $result = 1;
        $base = 2 % $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfGoodPartitions(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        var lastPos = [Int: Int]()
        for (i, v) in nums.enumerated() {
            lastPos[v] = i
        }
        var segmentCount = 0
        var right = -1
        for (i, v) in nums.enumerated() {
            if let r = lastPos[v], r > right {
                right = r
            }
            if i == right {
                segmentCount += 1
            }
        }
        // number of ways = 2^(segmentCount-1)
        var exp = segmentCount - 1
        var result: Int64 = 1
        var base: Int64 = 2
        while exp > 0 {
            if exp & 1 == 1 {
                result = (result * base) % Int64(MOD)
            }
            base = (base * base) % Int64(MOD)
            exp >>= 1
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfGoodPartitions(nums: IntArray): Int {
        val first = HashMap<Int, Int>()
        val last = HashMap<Int, Int>()
        for (i in nums.indices) {
            val v = nums[i]
            if (!first.containsKey(v)) first[v] = i
            last[v] = i
        }
        var segments = 0
        var i = 0
        val n = nums.size
        while (i < n) {
            var end = last[nums[i]]!!
            var j = i
            while (j <= end) {
                val v = nums[j]
                val l = last[v]!!
                if (l > end) end = l
                j++
            }
            segments++
            i = j
        }
        val MOD = 1_000_000_007L
        var result = 1L
        var base = 2L
        var exp = segments - 1
        while (exp > 0) {
            if ((exp and 1) == 1) {
                result = (result * base) % MOD
            }
            base = (base * base) % MOD
            exp = exp shr 1
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numberOfGoodPartitions(List<int> nums) {
    final n = nums.length;
    final Map<int, int> lastPos = {};
    for (int i = 0; i < n; i++) {
      lastPos[nums[i]] = i;
    }

    int segments = 0;
    int curMax = -1;
    for (int i = 0; i < n; i++) {
      final lp = lastPos[nums[i]]!;
      if (lp > curMax) curMax = lp;
      if (i == curMax) segments++;
    }

    // Number of good partitions = 2^(segments-1)
    int exp = segments - 1;
    int result = 1;
    int base = 2;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * base) % _mod;
      }
      base = (base * base) % _mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
func numberOfGoodPartitions(nums []int) int {
	const MOD int64 = 1000000007
	n := len(nums)
	last := make(map[int]int, n)
	for i, v := range nums {
		last[v] = i
	}
	cnt := 0
	right := -1
	for i, v := range nums {
		if last[v] > right {
			right = last[v]
		}
		if i == right {
			cnt++
		}
	}
	exp := cnt - 1
	var res int64 = 1
	base := int64(2)
	for exp > 0 {
		if exp&1 == 1 {
			res = (res * base) % MOD
		}
		base = (base * base) % MOD
		exp >>= 1
	}
	return int(res)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = (result * b) % mod if (e & 1) == 1
    b = (b * b) % mod
    e >>= 1
  end
  result
end

# @param {Integer[]} nums
# @return {Integer}
def number_of_good_partitions(nums)
  last = {}
  nums.each_with_index { |v, i| last[v] = i }

  segments = 0
  cur_end = -1
  nums.each_with_index do |v, i|
    cur_end = [cur_end, last[v]].max
    if i == cur_end
      segments += 1
    end
  end

  mod_pow(2, segments - 1, MOD)
end
```

## Scala

```scala
object Solution {
    def numberOfGoodPartitions(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        val n = nums.length
        val last = scala.collection.mutable.HashMap[Int, Int]()
        for (i <- 0 until n) {
            last(nums(i)) = i
        }
        var maxLast = -1
        var segments = 0
        for (i <- 0 until n) {
            val l = last(nums(i))
            if (l > maxLast) maxLast = l
            if (i == maxLast) segments += 1
        }
        var exp = segments - 1
        var result: Long = 1L
        var base: Long = 2L % MOD
        while (exp > 0) {
            if ((exp & 1) == 1) result = (result * base) % MOD
            base = (base * base) % MOD
            exp >>= 1
        }
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_good_partitions(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        const MOD: i64 = 1_000_000_007;

        // Record the last occurrence of each value.
        let mut last: HashMap<i32, usize> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            last.insert(v, i);
        }

        // Determine minimal blocks.
        let mut blocks: usize = 0;
        let mut cur_end: usize = 0;
        for (i, &v) in nums.iter().enumerate() {
            if let Some(&end) = last.get(&v) {
                if end > cur_end {
                    cur_end = end;
                }
            }
            if i == cur_end {
                blocks += 1;
            }
        }

        // Number of good partitions = 2^(blocks-1) mod MOD.
        let mut exp: i64 = blocks as i64 - 1;
        let mut base: i64 = 2;
        let mut result: i64 = 1;
        while exp > 0 {
            if (exp & 1) == 1 {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        result as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (pow-mod base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) MOD)
              (quotient e 2)
              (if (odd? e) (modulo (* res b) MOD) res)))))

(define/contract (number-of-good-partitions nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector nums))
         (n (vector-length vec))
         (last-pos (make-hash)))
    ;; record last occurrence of each value
    (for ([i (in-range n)])
      (hash-set! last-pos (vector-ref vec i) i))
    (let loop ((i 0) (cur-end -1) (segments 0))
      (if (= i n)
          (pow-mod 2 (max 0 (- segments 1)))
          (let* ((v (vector-ref vec i))
                 (new-end (max cur-end (hash-ref last-pos v))))
            (if (= i new-end)
                (loop (+ i 1) -1 (+ segments 1))
                (loop (+ i 1) new-end segments)))))))
```

## Erlang

```erlang
-spec number_of_good_partitions([integer()]) -> integer().
number_of_good_partitions(Nums) ->
    Mod = 1000000007,
    LastMap = build_last(Nums, 0, #{}),
    K = count_segments(Nums, 0, -1, 0, LastMap),
    Exp = K - 1,
    pow_mod(2, Exp, Mod).

build_last([], _Idx, Map) -> Map;
build_last([H|T], Idx, Map) ->
    NewMap = maps:put(H, Idx, Map),
    build_last(T, Idx + 1, NewMap).

count_segments([], _Idx, _CurMax, Count, _LastMap) -> Count;
count_segments([H|T], Idx, CurMax, Count, LastMap) ->
    LastIdx = maps:get(H, LastMap),
    NewCurMax = if LastIdx > CurMax -> LastIdx; true -> CurMax end,
    case Idx of
        NewCurMax ->
            count_segments(T, Idx + 1, -1, Count + 1, LastMap);
        _ ->
            count_segments(T, Idx + 1, NewCurMax, Count, LastMap)
    end.

pow_mod(_Base, Exp, _Mod) when Exp =< 0 -> 1;
pow_mod(Base, Exp, Mod) ->
    pow_mod_iter(Base rem Mod, Exp, Mod, 1).

pow_mod_iter(_, 0, _, Acc) -> Acc;
pow_mod_iter(B, E, M, Acc) when (E band 1) =:= 1 ->
    NewAcc = (Acc * B) rem M,
    pow_mod_iter((B * B) rem M, E bsr 1, M, NewAcc);
pow_mod_iter(B, E, M, Acc) ->
    pow_mod_iter((B * B) rem M, E bsr 1, M, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_good_partitions(nums :: [integer]) :: integer
  def number_of_good_partitions(nums) do
    mod = 1_000_000_007

    last_map =
      Enum.reduce(Enum.with_index(nums), %{}, fn {v, idx}, acc ->
        Map.put(acc, v, idx)
      end)

    {components, _} =
      Enum.reduce(Enum.with_index(nums), {0, -1}, fn {v, idx}, {cnt, cur_end} ->
        new_end = max(cur_end, Map.get(last_map, v))

        if idx == new_end do
          {cnt + 1, -1}
        else
          {cnt, new_end}
        end
      end)

    exp = components - 1
    pow_mod(2, exp, mod)
  end

  defp pow_mod(_base, 0, _mod), do: 1

  defp pow_mod(base, exp, mod) when exp > 0 do
    require Bitwise
    do_pow(rem(base, mod), exp, 1, mod)
  end

  defp do_pow(_base, 0, acc, _mod), do: acc

  defp do_pow(base, exp, acc, mod) do
    require Bitwise
    acc = if (exp &&& 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    do_pow(base, exp >>> 1, acc, mod)
  end
end
```
