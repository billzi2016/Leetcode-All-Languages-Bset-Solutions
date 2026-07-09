# 2845. Count of Interesting Subarrays

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        unordered_map<long long,long long> freq;
        long long ans = 0;
        long long pref = 0; // number of special elements seen so far
        
        for (size_t i = 0; i <= nums.size(); ++i) {
            if (i > 0 && static_cast<long long>(nums[i-1]) % modulo == k)
                ++pref;
            
            long long target = (pref - k) % modulo;
            if (target < 0) target += modulo;
            
            auto it = freq.find(target);
            if (it != freq.end())
                ans += it->second;
            
            long long rem = pref % modulo;
            ++freq[rem];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countInterestingSubarrays(java.util.List<Integer> nums, int modulo, int k) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        int pref = 0;
        int prefMod = 0; // pref % modulo
        freq.put(0, 1);
        long ans = 0L;
        for (int val : nums) {
            if (val % modulo == k) {
                pref++;
            }
            prefMod = pref % modulo;
            int target = (int) ((prefMod - k + (long) modulo) % modulo);
            ans += freq.getOrDefault(target, 0);
            freq.put(prefMod, freq.getOrDefault(prefMod, 0) + 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        freq = {0: 1}  # residue of prefix sum before any element
        pref = 0
        ans = 0
        for num in nums:
            if num % modulo == k:
                pref += 1
            target = (pref - k) % modulo
            ans += freq.get(target, 0)
            resid = pref % modulo
            freq[resid] = freq.get(resid, 0) + 1
        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1  # prefix before any element
        pref = 0
        ans = 0
        for num in nums:
            if num % modulo == k:
                pref += 1
            target = (pref - k) % modulo
            ans += freq.get(target, 0)
            freq[pref % modulo] += 1
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long *keys;
    long long *vals;
    char *used;
    int size;
} HashMap;

static inline long long hashmap_get(HashMap *hm, long long key) {
    int mask = hm->size - 1;
    unsigned int h = (unsigned int)(key ^ (key >> 32));
    h &= mask;
    while (hm->used[h]) {
        if (hm->keys[h] == key) return hm->vals[h];
        h = (h + 1) & mask;
    }
    return 0;
}

static inline void hashmap_add(HashMap *hm, long long key, long long delta) {
    int mask = hm->size - 1;
    unsigned int h = (unsigned int)(key ^ (key >> 32));
    h &= mask;
    while (hm->used[h]) {
        if (hm->keys[h] == key) {
            hm->vals[h] += delta;
            return;
        }
        h = (h + 1) & mask;
    }
    hm->used[h] = 1;
    hm->keys[h] = key;
    hm->vals[h] = delta;
}

long long countInterestingSubarrays(int* nums, int numsSize, int modulo, int k) {
    if (numsSize == 0) return 0;
    int tableSize = 1;
    while (tableSize < numsSize * 4) tableSize <<= 1;   // keep load factor low

    HashMap hm;
    hm.size = tableSize;
    hm.keys = (long long *)calloc(tableSize, sizeof(long long));
    hm.vals = (long long *)calloc(tableSize, sizeof(long long));
    hm.used = (char *)calloc(tableSize, sizeof(char));

    hashmap_add(&hm, 0LL, 1LL);   // prefix count for empty prefix

    long long pref = 0;
    long long ans = 0;
    long long mod = (long long)modulo;

    for (int i = 0; i < numsSize; ++i) {
        if ((long long)nums[i] % mod == k) pref++;

        long long target = ((pref - (long long)k) % mod + mod) % mod;
        ans += hashmap_get(&hm, target);

        hashmap_add(&hm, pref % mod, 1LL);
    }

    free(hm.keys);
    free(hm.vals);
    free(hm.used);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public long CountInterestingSubarrays(IList<int> nums, int modulo, int k) {
        var freq = new Dictionary<long, long>();
        long mod = modulo;
        freq[0] = 1; // prefix sum remainder before any element
        long ans = 0;
        long specialCount = 0;

        foreach (int val in nums) {
            if (val % modulo == k) {
                specialCount++;
            }
            long curRem = specialCount % mod;
            long target = (curRem - k + mod) % mod;

            if (freq.TryGetValue(target, out var cnt)) {
                ans += cnt;
            }

            if (freq.TryGetValue(curRem, out var existing)) {
                freq[curRem] = existing + 1;
            } else {
                freq[curRem] = 1;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} modulo
 * @param {number} k
 * @return {number}
 */
var countInterestingSubarrays = function(nums, modulo, k) {
    const freq = new Map();
    // prefix sum of special elements before any element (empty prefix)
    freq.set(0, 1);
    let pref = 0;
    let ans = 0;
    for (const num of nums) {
        if (num % modulo === k) pref += 1;
        const rem = pref % modulo; // non‑negative since pref >= 0
        const target = ((rem - k) % modulo + modulo) % modulo;
        ans += freq.get(target) || 0;
        freq.set(rem, (freq.get(rem) || 0) + 1);
    }
    return ans;
};
```

## Typescript

```typescript
function countInterestingSubarrays(nums: number[], modulo: number, k: number): number {
    const freq = new Map<number, number>();
    freq.set(0, 1); // prefix sum of zero elements
    let pref = 0;
    let ans = 0;

    for (const v of nums) {
        if (v % modulo === k) pref += 1;

        const curRem = pref % modulo;               // current prefix remainder
        let target = curRem - k;                     // needed previous remainder
        if (target < 0) target += modulo;

        ans += freq.get(target) ?? 0;
        freq.set(curRem, (freq.get(curRem) ?? 0) + 1);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $modulo
     * @param Integer $k
     * @return Integer
     */
    function countInterestingSubarrays($nums, $modulo, $k) {
        $freq = [0 => 1];
        $prefix = 0;
        $ans = 0;

        foreach ($nums as $num) {
            if ($num % $modulo == $k) {
                $prefix++;
            }
            $modVal = $prefix % $modulo;
            $target = $modVal - $k;
            $target %= $modulo;
            if ($target < 0) {
                $target += $modulo;
            }
            if (isset($freq[$target])) {
                $ans += $freq[$target];
            }
            if (!isset($freq[$modVal])) {
                $freq[$modVal] = 1;
            } else {
                $freq[$modVal]++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countInterestingSubarrays(_ nums: [Int], _ modulo: Int, _ k: Int) -> Int {
        var freq = [Int: Int]()
        let mod = modulo
        var prefix = 0               // number of elements satisfying condition so far
        freq[0] = 1                  // empty prefix
        
        var result: Int64 = 0
        
        for num in nums {
            if num % mod == k {
                prefix += 1
            }
            let curRem = prefix % mod
            var need = (curRem - k) % mod
            if need < 0 { need += mod }
            
            if let cnt = freq[need] {
                result += Int64(cnt)
            }
            freq[curRem, default: 0] += 1
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countInterestingSubarrays(nums: List<Int>, modulo: Int, k: Int): Long {
        val freq = HashMap<Int, Long>()
        var pref = 0
        var ans = 0L
        freq[0] = 1L
        for (num in nums) {
            if (num % modulo == k) pref += 1
            val target = ((pref - k) % modulo + modulo) % modulo
            ans += freq.getOrDefault(target, 0L)
            val curMod = pref % modulo
            freq[curMod] = freq.getOrDefault(curMod, 0L) + 1L
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countInterestingSubarrays(List<int> nums, int modulo, int k) {
    Map<int, int> freq = {};
    int pref = 0;
    int ans = 0;

    // initial prefix sum remainder
    int rem0 = ((pref % modulo) + modulo) % modulo;
    freq[rem0] = 1;

    for (int num in nums) {
      if (num % modulo == k) {
        pref += 1;
      }
      int curRem = ((pref % modulo) + modulo) % modulo;
      int target = (curRem - k) % modulo;
      if (target < 0) target += modulo;

      ans += freq[target] ?? 0;
      freq[curRem] = (freq[curRem] ?? 0) + 1;
    }

    return ans;
  }
}
```

## Golang

```go
func countInterestingSubarrays(nums []int, modulo int, k int) int64 {
    freq := make(map[int]int64)
    freq[0] = 1

    var ans int64
    cntSpecial := 0
    prefMod := 0

    for _, v := range nums {
        if v%modulo == k {
            cntSpecial++
        }
        prefMod = cntSpecial % modulo
        target := (prefMod - k) % modulo
        if target < 0 {
            target += modulo
        }
        ans += freq[target]
        freq[prefMod]++
    }

    return ans
}
```

## Ruby

```ruby
def count_interesting_subarrays(nums, modulo, k)
  freq = Hash.new(0)
  freq[0] = 1
  ans = 0
  pref = 0

  nums.each do |num|
    pref += 1 if num % modulo == k
    target = (pref - k) % modulo
    ans += freq[target]
    freq[pref % modulo] += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countInterestingSubarrays(nums: List[Int], modulo: Int, k: Int): Long = {
        val freq = scala.collection.mutable.Map[Int, Long]().withDefaultValue(0L)
        var prefixCount = 0
        var result: Long = 0L

        // prefix before any element (index -1) has count 0
        freq(0) = 1L

        for (num <- nums) {
            if (num % modulo == k) {
                prefixCount += 1
            }
            val curMod = prefixCount % modulo
            val target = ((curMod - k) % modulo + modulo) % modulo
            result += freq(target)
            freq(curMod) = freq(curMod) + 1L
        }

        result
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_interesting_subarrays(nums: Vec<i32>, modulo: i32, k: i32) -> i64 {
        let m = modulo as i64;
        let kk = k as i64;
        let mut pref: i64 = 0;
        let mut ans: i64 = 0;
        let mut cnt: HashMap<i64, i64> = HashMap::new();
        cnt.insert(0, 1); // empty prefix

        for &x in nums.iter() {
            if x % modulo == k {
                pref += 1;
            }
            // target remainder for previous prefix
            let mut target = (pref - kk) % m;
            if target < 0 {
                target += m;
            }
            if let Some(v) = cnt.get(&target) {
                ans += *v;
            }
            let rem = pref % m;
            *cnt.entry(rem).or_insert(0) += 1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-interesting-subarrays nums modulo k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (define (pos-mod x m)
    (let ([r (remainder x m)])
      (if (< r 0) (+ r m) r)))
  (define freq (make-hash))
  (hash-set! freq 0 1)
  (let loop ((lst nums) (p 0) (ans 0))
    (if (null? lst)
        ans
        (let* ([x (car lst)]
               [p2 (if (= (remainder x modulo) k) (+ p 1) p)]
               [target (pos-mod (- p2 k) modulo)]
               [cnt (hash-ref freq target 0)]
               [ans2 (+ ans cnt)]
               [curmod (pos-mod p2 modulo)])
          (hash-set! freq curmod (+ (hash-ref freq curmod 0) 1))
          (loop (cdr lst) p2 ans2)))))
```

## Erlang

```erlang
-spec count_interesting_subarrays(Nums :: [integer()], Modulo :: integer(), K :: integer()) -> integer().
count_interesting_subarrays(Nums, Modulo, K) ->
    InitialMap = #{0 => 1},
    {Ans, _, _} =
        lists:foldl(
            fun(X, {Acc, Pref, Map}) ->
                NewPref =
                    case X rem Modulo of
                        R when R == K -> Pref + 1;
                        _ -> Pref
                    end,
                Needed = ((NewPref - K) rem Modulo + Modulo) rem Modulo,
                Add = maps:get(Needed, Map, 0),
                NewMap =
                    maps:update_with(
                        NewPref rem Modulo,
                        fun(V) -> V + 1 end,
                        1,
                        Map
                    ),
                {Acc + Add, NewPref, NewMap}
            end,
            {0, 0, InitialMap},
            Nums
        ),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_interesting_subarrays(nums :: [integer], modulo :: integer, k :: integer) :: integer
  def count_interesting_subarrays(nums, modulo, k) do
    {_prefix, _freq, ans} =
      Enum.reduce(nums, {0, %{0 => 1}, 0}, fn num, {pref, freq, acc} ->
        pref = if rem(num, modulo) == k, do: pref + 1, else: pref
        cur_mod = rem(pref, modulo)
        target = rem(cur_mod - k + modulo, modulo)
        add = Map.get(freq, target, 0)

        freq =
          Map.update(freq, cur_mod, 1, fn count -> count + 1 end)

        {pref, freq, acc + add}
      end)

    ans
  end
end
```
