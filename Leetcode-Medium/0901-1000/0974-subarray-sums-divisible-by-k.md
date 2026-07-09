# 0974. Subarray Sums Divisible by K

## Cpp

```cpp
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int> count(k, 0);
        count[0] = 1;
        int prefixMod = 0;
        long long result = 0;
        for (int num : nums) {
            int mod = ((num % k) + k) % k;          // ensure non‑negative contribution
            prefixMod = (prefixMod + mod) % k;      // cumulative remainder
            result += count[prefixMod];
            ++count[prefixMod];
        }
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] count = new int[k];
        count[0] = 1;
        int prefixMod = 0;
        long result = 0;
        for (int num : nums) {
            int modNum = ((num % k) + k) % k; // ensure non‑negative
            prefixMod = (prefixMod + modNum) % k;
            result += count[prefixMod];
            count[prefixMod]++;
        }
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = [0] * k
        count[0] = 1
        prefix_mod = 0
        result = 0
        for num in nums:
            prefix_mod = (prefix_mod + num % k + k) % k
            result += count[prefix_mod]
            count[prefix_mod] += 1
        return result
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        prefix = 0
        res = 0
        for num in nums:
            prefix = (prefix + num) % k
            res += cnt[prefix]
            cnt[prefix] += 1
        return res
```

## C

```c
#include <stdlib.h>

int subarraysDivByK(int* nums, int numsSize, int k) {
    long long *cnt = (long long *)calloc(k, sizeof(long long));
    if (!cnt) return 0;
    cnt[0] = 1;
    long long sum = 0;
    long long res = 0;
    for (int i = 0; i < numsSize; ++i) {
        sum = (sum + nums[i]) % k;
        if (sum < 0) sum += k;
        res += cnt[sum];
        cnt[sum]++;
    }
    free(cnt);
    return (int)res;
}
```

## Csharp

```csharp
public class Solution
{
    public int SubarraysDivByK(int[] nums, int k)
    {
        int[] modCount = new int[k];
        modCount[0] = 1;
        int prefixMod = 0;
        long result = 0;

        foreach (int num in nums)
        {
            int cur = ((num % k) + k) % k; // ensure non‑negative
            prefixMod = (prefixMod + cur) % k;
            result += modCount[prefixMod];
            modCount[prefixMod]++;
        }

        return (int)result;
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
var subarraysDivByK = function(nums, k) {
    const modCount = new Array(k).fill(0);
    modCount[0] = 1; // empty prefix has remainder 0
    let prefixMod = 0;
    let result = 0;
    
    for (const num of nums) {
        // keep remainder non‑negative
        prefixMod = ((prefixMod + (num % k) + k) % k);
        result += modCount[prefixMod];
        modCount[prefixMod] += 1;
    }
    
    return result;
};
```

## Typescript

```typescript
function subarraysDivByK(nums: number[], k: number): number {
    const modCount = new Array(k).fill(0);
    modCount[0] = 1;
    let prefixMod = 0;
    let result = 0;
    for (const num of nums) {
        prefixMod = (prefixMod + ((num % k) + k)) % k;
        result += modCount[prefixMod];
        modCount[prefixMod]++;
    }
    return result;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarraysDivByK($nums, $k) {
        $modGroups = array_fill(0, $k, 0);
        $modGroups[0] = 1;
        $prefixMod = 0;
        $result = 0;
        foreach ($nums as $num) {
            $prefixMod = ($prefixMod + ($num % $k) + $k) % $k;
            $result += $modGroups[$prefixMod];
            $modGroups[$prefixMod]++;
        }
        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    func subarraysDivByK(_ nums: [Int], _ k: Int) -> Int {
        var modCount = Array(repeating: 0, count: k)
        modCount[0] = 1
        var prefixMod = 0
        var result = 0
        
        for num in nums {
            let adjustedNum = ((num % k) + k) % k
            prefixMod = (prefixMod + adjustedNum) % k
            result += modCount[prefixMod]
            modCount[prefixMod] += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subarraysDivByK(nums: IntArray, k: Int): Int {
        val modCount = IntArray(k)
        modCount[0] = 1
        var prefixMod = 0
        var result = 0L
        for (num in nums) {
            val cur = ((num % k) + k) % k
            prefixMod = (prefixMod + cur) % k
            result += modCount[prefixMod]
            modCount[prefixMod]++
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int subarraysDivByK(List<int> nums, int k) {
    List<int> count = List.filled(k, 0);
    count[0] = 1;
    int prefixMod = 0;
    int result = 0;
    for (int num in nums) {
      int mod = ((num % k) + k) % k;
      prefixMod = (prefixMod + mod) % k;
      result += count[prefixMod];
      count[prefixMod] += 1;
    }
    return result;
  }
}
```

## Golang

```go
func subarraysDivByK(nums []int, k int) int {
    cnt := make([]int, k)
    cnt[0] = 1
    prefixMod, res := 0, 0
    for _, v := range nums {
        prefixMod = (prefixMod + v) % k
        if prefixMod < 0 {
            prefixMod += k
        }
        res += cnt[prefixMod]
        cnt[prefixMod]++
    }
    return res
}
```

## Ruby

```ruby
def subarrays_div_by_k(nums, k)
  mod_counts = Array.new(k, 0)
  mod_counts[0] = 1
  prefix_mod = 0
  result = 0

  nums.each do |num|
    prefix_mod = (prefix_mod + num % k) % k
    result += mod_counts[prefix_mod]
    mod_counts[prefix_mod] += 1
  end

  result
end
```

## Scala

```scala
object Solution {
    def subarraysDivByK(nums: Array[Int], k: Int): Int = {
        val modCounts = new Array[Long](k)
        modCounts(0) = 1L
        var prefix = 0
        var result: Long = 0L

        for (num <- nums) {
            prefix = (prefix + num) % k
            if (prefix < 0) prefix += k
            result += modCounts(prefix)
            modCounts(prefix) += 1
        }

        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let k_usize = k as usize;
        let mut count = vec![0i64; k_usize];
        count[0] = 1;
        let mut prefix = 0i32;
        let mut result: i64 = 0;
        for &num in nums.iter() {
            // ensure positive remainder for current number
            let cur_mod = ((num % k) + k) % k;
            prefix = (prefix + cur_mod) % k;
            let idx = prefix as usize;
            result += count[idx];
            count[idx] += 1;
        }
        result as i32
    }
}
```

## Racket

```racket
(define/contract (subarrays-div-by-k nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([counts (make-vector k 0)]
         [_ (vector-set! counts 0 1)])
    (let loop ((lst nums) (prefix 0) (result 0))
      (if (null? lst)
          result
          (let* ([num (car lst)]
                 [new-prefix (modulo (+ prefix (modulo num k)) k)]
                 [cnt (vector-ref counts new-prefix)])
            (vector-set! counts new-prefix (+ cnt 1))
            (loop (cdr lst) new-prefix (+ result cnt)))))))
```

## Erlang

```erlang
-module(solution).
-export([subarrays_div_by_k/2]).

-spec subarrays_div_by_k(Nums :: [integer()], K :: integer()) -> integer().
subarrays_div_by_k(Nums, K) ->
    subarrays_div_by_k(Nums, K, 0, #{0 => 1}, 0).

subarrays_div_by_k([], _K, _PrefixMod, _MapCounts, Result) ->
    Result;
subarrays_div_by_k([H|T], K, PrefixMod, MapCounts, Result) ->
    NewPrefix = (PrefixMod + H) rem K,
    AdjPrefix = if NewPrefix < 0 -> NewPrefix + K; true -> NewPrefix end,
    Count = maps:get(AdjPrefix, MapCounts, 0),
    NewResult = Result + Count,
    UpdatedMap = maps:put(AdjPrefix, Count + 1, MapCounts),
    subarrays_div_by_k(T, K, AdjPrefix, UpdatedMap, NewResult).
```

## Elixir

```elixir
defmodule Solution do
  @spec subarrays_div_by_k(nums :: [integer], k :: integer) :: integer
  def subarrays_div_by_k(nums, k) do
    {_pref, result, _counts} =
      Enum.reduce(nums, {0, 0, %{0 => 1}}, fn num, {pref, res, counts} ->
        pref = Integer.mod(pref + num, k)
        cnt = Map.get(counts, pref, 0)
        new_res = res + cnt
        new_counts = Map.update(counts, pref, 1, &(&1 + 1))
        {pref, new_res, new_counts}
      end)

    result
  end
end
```
