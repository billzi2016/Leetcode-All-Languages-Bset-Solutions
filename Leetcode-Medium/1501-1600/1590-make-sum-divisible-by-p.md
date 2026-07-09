# 1590. Make Sum Divisible by P

## Cpp

```cpp
class Solution {
public:
    int minSubarray(std::vector<int>& nums, int p) {
        long long total = 0;
        for (int x : nums) total += x;
        int target = total % p;
        if (target == 0) return 0;

        std::unordered_map<int,int> idx;
        idx.reserve(nums.size()*2);
        idx[0] = -1; // prefix sum remainder 0 at position -1

        int cur = 0;
        int n = nums.size();
        int best = n; // initialize with impossible large length

        for (int i = 0; i < n; ++i) {
            cur = (cur + nums[i]) % p;
            int need = cur - target;
            if (need < 0) need += p;

            auto it = idx.find(need);
            if (it != idx.end()) {
                int len = i - it->second;
                if (len < best) best = len;
            }
            // store the latest index for this remainder
            idx[cur] = i;
        }

        return (best == n) ? -1 : best;
    }
};
```

## Java

```java
class Solution {
    public int minSubarray(int[] nums, int p) {
        long total = 0;
        for (int num : nums) {
            total += num;
        }
        int target = (int)(total % p);
        if (target == 0) return 0;

        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        map.put(0, -1); // prefix sum remainder 0 at index -1

        int cur = 0;
        int n = nums.length;
        int minLen = n; // initialize with max possible length

        for (int i = 0; i < n; i++) {
            cur = (int)((cur + (long)nums[i]) % p);
            int need = cur - target;
            if (need < 0) need += p;

            Integer prevIdx = map.get(need);
            if (prevIdx != null) {
                int len = i - prevIdx;
                if (len < minLen) {
                    minLen = len;
                }
            }

            // store the latest index for this remainder
            map.put(cur, i);
        }

        return minLen == n ? -1 : minLen;
    }
}
```

## Python

```python
class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total_mod = sum(nums) % p
        if total_mod == 0:
            return 0

        target = total_mod
        prefix_index = {0: -1}
        cur = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            needed = (cur - target) % p
            if needed in prefix_index:
                length = i - prefix_index[needed]
                if length < min_len:
                    min_len = length
            # store the latest index for this remainder to get shortest future subarray
            prefix_index[cur] = i

        return -1 if min_len == len(nums) else min_len
```

## Python3

```python
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_mod = sum(nums) % p
        if total_mod == 0:
            return 0

        target = total_mod
        prefix_index = {0: -1}
        cur = 0
        n = len(nums)
        min_len = n  # initialize with max possible length

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            needed = (cur - target) % p
            if needed in prefix_index:
                candidate_len = i - prefix_index[needed]
                if candidate_len < min_len:
                    min_len = candidate_len
            # store latest index for this remainder to get shortest future subarray
            prefix_index[cur] = i

        return -1 if min_len == n else min_len
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int hashmap_get(int *keys, int *vals, int cap, int key) {
    int idx = key & (cap - 1);
    while (keys[idx] != -1) {
        if (keys[idx] == key) return vals[idx];
        idx = (idx + 1) & (cap - 1);
    }
    return INT_MIN; // not found
}

static void hashmap_put(int *keys, int *vals, int cap, int key, int val) {
    int idx = key & (cap - 1);
    while (keys[idx] != -1 && keys[idx] != key) {
        idx = (idx + 1) & (cap - 1);
    }
    keys[idx] = key;
    vals[idx] = val;
}

int minSubarray(int* nums, int numsSize, int p) {
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    int target = (int)(total % p);
    if (target == 0) return 0;

    // hashmap capacity: power of two >= 2 * numsSize
    int cap = 1;
    while (cap < numsSize * 2) cap <<= 1;
    int *keys = (int *)malloc(sizeof(int) * cap);
    int *vals = (int *)malloc(sizeof(int) * cap);
    if (!keys || !vals) return -1; // allocation failure fallback
    memset(keys, -1, sizeof(int) * cap);

    hashmap_put(keys, vals, cap, 0, -1); // prefix sum 0 at index -1

    int cur = 0;
    int minLen = numsSize + 1;

    for (int i = 0; i < numsSize; ++i) {
        cur = (cur + nums[i]) % p;
        int needed = cur - target;
        if (needed < 0) needed += p;
        int idx = hashmap_get(keys, vals, cap, needed);
        if (idx != INT_MIN) {
            int len = i - idx;
            if (len < minLen) minLen = len;
        }
        hashmap_put(keys, vals, cap, cur, i); // store latest index
    }

    free(keys);
    free(vals);

    if (minLen == numsSize + 1 || minLen == numsSize) return -1;
    return minLen;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSubarray(int[] nums, int p) {
        long total = 0;
        foreach (int num in nums) total += num;
        int target = (int)(total % p);
        if (target == 0) return 0;

        var map = new Dictionary<int, int>();
        map[0] = -1; // prefix remainder 0 at index -1

        long cur = 0;
        int minLen = nums.Length;

        for (int i = 0; i < nums.Length; i++) {
            cur = (cur + nums[i]) % p;
            int curMod = (int)cur;

            int need = curMod - target;
            if (need < 0) need += p;

            if (map.TryGetValue(need, out int prevIdx)) {
                int len = i - prevIdx;
                if (len < minLen) minLen = len;
            }

            // store the latest index for this remainder
            map[curMod] = i;
        }

        return minLen == nums.Length ? -1 : minLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minSubarray = function(nums, p) {
    const n = nums.length;
    let totalMod = 0;
    for (let num of nums) {
        totalMod = (totalMod + num) % p;
    }
    if (totalMod === 0) return 0; // already divisible

    const target = totalMod; // remainder to eliminate
    const modMap = new Map();
    modMap.set(0, -1); // prefix sum of 0 at index -1

    let cur = 0;
    let minLen = n; // initialize with max possible length

    for (let i = 0; i < n; ++i) {
        cur = (cur + nums[i]) % p;
        const needed = (cur - target + p) % p;

        if (modMap.has(needed)) {
            const prevIdx = modMap.get(needed);
            const len = i - prevIdx;
            if (len < minLen) minLen = len;
        }
        // store latest index for this remainder to potentially get shorter subarrays later
        modMap.set(cur, i);
    }

    return minLen === n ? -1 : minLen;
};
```

## Typescript

```typescript
function minSubarray(nums: number[], p: number): number {
    let total = 0;
    for (const x of nums) {
        total = (total + x) % p;
    }
    const target = total % p;
    if (target === 0) return 0;

    const modMap = new Map<number, number>();
    modMap.set(0, -1);
    let cur = 0;
    let minLen = nums.length;

    for (let i = 0; i < nums.length; ++i) {
        cur = (cur + nums[i]) % p;
        const need = (cur - target + p) % p;
        if (modMap.has(need)) {
            const prevIdx = modMap.get(need)!;
            const len = i - prevIdx;
            if (len < minLen) minLen = len;
        }
        // store the latest index for this remainder
        modMap.set(cur, i);
    }

    return minLen === nums.length ? -1 : minLen;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $p
     * @return Integer
     */
    function minSubarray($nums, $p) {
        $n = count($nums);
        $totalMod = 0;
        foreach ($nums as $val) {
            $totalMod = ($totalMod + $val) % $p;
        }
        if ($totalMod == 0) return 0;

        $target = $totalMod; // remainder to eliminate
        $modMap = [0 => -1]; // remainder => latest index
        $curr = 0;
        $minLen = $n + 1; // larger than any possible answer

        for ($i = 0; $i < $n; ++$i) {
            $curr = ($curr + $nums[$i]) % $p;
            $need = ($curr - $target);
            if ($need < 0) $need += $p;
            // ensure positive modulo
            $need %= $p;

            if (isset($modMap[$need])) {
                $len = $i - $modMap[$need];
                if ($len < $minLen) {
                    $minLen = $len;
                }
            }
            // store latest index for current remainder
            $modMap[$curr] = $i;
        }

        return ($minLen == $n + 1 || $minLen == $n) ? -1 : $minLen;
    }
}
```

## Swift

```swift
class Solution {
    func minSubarray(_ nums: [Int], _ p: Int) -> Int {
        var total = 0
        for num in nums {
            total = (total + num % p) % p
        }
        if total == 0 { return 0 }
        let target = total
        var dict = [Int:Int]()
        dict[0] = -1
        var prefix = 0
        var minLen = nums.count + 1
        for (i, num) in nums.enumerated() {
            prefix = (prefix + num % p) % p
            let need = (prefix - target + p) % p
            if let prev = dict[need] {
                let len = i - prev
                if len < minLen { minLen = len }
            }
            dict[prefix] = i
        }
        return minLen == nums.count + 1 ? -1 : minLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSubarray(nums: IntArray, p: Int): Int {
        var total = 0L
        for (num in nums) {
            total += num.toLong()
        }
        val target = ((total % p).toInt())
        if (target == 0) return 0

        val map = HashMap<Int, Int>()
        map[0] = -1
        var cur = 0
        var minLen = nums.size

        for (i in nums.indices) {
            cur = (cur + nums[i]) % p
            val need = (cur - target + p) % p
            map[need]?.let { prevIdx ->
                val len = i - prevIdx
                if (len < minLen) minLen = len
            }
            map[cur] = i
        }

        return if (minLen == nums.size) -1 else minLen
    }
}
```

## Dart

```dart
class Solution {
  int minSubarray(List<int> nums, int p) {
    int n = nums.length;
    int totalMod = 0;
    for (int num in nums) {
      totalMod = (totalMod + num) % p;
    }
    if (totalMod == 0) return 0;

    int target = totalMod;
    Map<int, int> modIndex = {0: -1};
    int cur = 0;
    int minLen = n + 1;

    for (int i = 0; i < n; ++i) {
      cur = (cur + nums[i]) % p;
      int need = (cur - target) % p;
      if (need < 0) need += p;
      if (modIndex.containsKey(need)) {
        int len = i - modIndex[need]!;
        if (len < minLen) minLen = len;
      }
      modIndex[cur] = i; // store latest index for this remainder
    }

    if (minLen == n + 1 || minLen == n) return -1;
    return minLen;
  }
}
```

## Golang

```go
func minSubarray(nums []int, p int) int {
    sumMod := 0
    for _, v := range nums {
        sumMod = (sumMod + v%p) % p
    }
    if sumMod == 0 {
        return 0
    }
    target := sumMod

    modMap := make(map[int]int)
    modMap[0] = -1

    cur := 0
    n := len(nums)
    minLen := n + 1

    for i, v := range nums {
        cur = (cur + v%p) % p
        need := cur - target
        if need < 0 {
            need += p
        }
        if idx, ok := modMap[need]; ok {
            length := i - idx
            if length < minLen {
                minLen = length
            }
        }
        modMap[cur] = i
    }

    if minLen == n+1 || minLen == n {
        return -1
    }
    return minLen
}
```

## Ruby

```ruby
def min_subarray(nums, p)
  target = nums.sum % p
  return 0 if target == 0

  prefix_index = {0 => -1}
  cur = 0
  min_len = nums.length

  nums.each_with_index do |num, i|
    cur = (cur + num) % p
    needed = (cur - target) % p
    if prefix_index.key?(needed)
      len = i - prefix_index[needed]
      min_len = len if len < min_len
    end
    prefix_index[cur] = i
  end

  min_len == nums.length ? -1 : min_len
end
```

## Scala

```scala
object Solution {
    def minSubarray(nums: Array[Int], p: Int): Int = {
        val n = nums.length
        var total: Long = 0L
        val pp = p.toLong
        for (x <- nums) {
            total = (total + x) % pp
        }
        if (total == 0) return 0
        val target = total.toInt

        import scala.collection.mutable.HashMap
        val map = new HashMap[Int, Int]()
        map.put(0, -1)

        var cur: Long = 0L
        var minLen = n

        for (i <- 0 until n) {
            cur = (cur + nums(i)) % pp
            val curMod = cur.toInt
            var needed = (curMod - target) % p
            if (needed < 0) needed += p
            map.get(needed).foreach { idx =>
                val len = i - idx
                if (len < minLen) minLen = len
            }
            map.put(curMod, i)
        }

        if (minLen == n) -1 else minLen
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let n = nums.len();
        let mut total: i64 = 0;
        for &x in &nums {
            total += x as i64;
        }
        let p_i64 = p as i64;
        let target = total % p_i64;
        if target == 0 {
            return 0;
        }

        let mut map: HashMap<i64, i32> = HashMap::new();
        map.insert(0, -1);
        let mut cur: i64 = 0;
        let mut ans = n as i32;

        for (i, &x) in nums.iter().enumerate() {
            cur = (cur + x as i64) % p_i64;
            let need = (cur - target + p_i64) % p_i64;
            if let Some(&prev_idx) = map.get(&need) {
                let len = i as i32 - prev_idx;
                if len < ans {
                    ans = len;
                }
            }
            // store the latest index for this remainder
            map.insert(cur, i as i32);
        }

        if ans == n as i32 { -1 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (min-subarray nums p)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [total (apply + nums)]
         [target (modulo total p)])
    (if (= target 0)
        0
        (let ([hash (make-hash)])
          (hash-set! hash 0 -1) ; prefix remainder 0 at index -1
          (let loop ((i 0) (curr 0) (best n))
            (if (= i n)
                (if (= best n) -1 best)
                (let* ([val (list-ref nums i)]
                       [newcurr (modulo (+ curr val) p)]
                       [need (modulo (- newcurr target) p)])
                  (define next-best
                    (if (hash-has-key? hash need)
                        (let ([prev (hash-ref hash need)])
                          (min best (- i prev)))
                        best))
                  (hash-set! hash newcurr i)
                  (loop (+ i 1) newcurr next-best)))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_subarray/2]).

-spec min_subarray(Nums :: [integer()], P :: integer()) -> integer().
min_subarray(Nums, P) ->
    Total = lists:foldl(fun(X, Acc) -> (Acc + X) rem P end, 0, Nums),
    Target = Total,
    case Target of
        0 -> 0;
        _ ->
            N = length(Nums),
            FoldFun = fun(Elem, {MapAcc, CurAcc, MinAcc, Idx}) ->
                NewCur = (CurAcc + Elem) rem P,
                Needed = (NewCur - Target + P) rem P,
                PrevIdx = maps:get(Needed, MapAcc, undefined),
                NewMin = case PrevIdx of
                    undefined -> MinAcc;
                    _ ->
                        Len = Idx - PrevIdx,
                        if Len < MinAcc -> Len; true -> MinAcc end
                end,
                NewMap = maps:put(NewCur, Idx, MapAcc),
                {NewMap, NewCur, NewMin, Idx + 1}
            end,
            {_FinalMap, _FinalCur, MinLen, _} = lists:foldl(FoldFun, {#{0 => -1}, 0, N, 0}, Nums),
            if MinLen == N -> -1; true -> MinLen end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_subarray(nums :: [integer], p :: integer) :: integer
  def min_subarray(nums, p) do
    total = Enum.reduce(nums, 0, fn x, acc -> rem(acc + x, p) end)
    target = total

    if target == 0 do
      0
    else
      n = length(nums)

      {best_len, _cur, _map} =
        Enum.with_index(nums)
        |> Enum.reduce({n + 1, 0, %{0 => -1}}, fn {num, idx}, {best, cur, map} ->
          new_cur = rem(cur + num, p)

          needed = new_cur - target
          needed = rem(needed, p)
          needed = if needed < 0, do: needed + p, else: needed

          best =
            case Map.fetch(map, needed) do
              {:ok, prev_idx} ->
                len = idx - prev_idx
                if len < best, do: len, else: best

              :error ->
                best
            end

          new_map = Map.put(map, new_cur, idx)
          {best, new_cur, new_map}
        end)

      cond do
        best_len > n - 1 -> -1
        true -> best_len
      end
    end
  end
end
```
