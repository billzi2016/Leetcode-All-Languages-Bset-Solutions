# 2588. Count the Number of Beautiful Subarrays

## Cpp

```cpp
class Solution {
public:
    long long beautifulSubarrays(vector<int>& nums) {
        unordered_map<int, long long> freq;
        freq.reserve(nums.size() * 2);
        freq.max_load_factor(0.7);
        freq[0] = 1; // empty prefix
        
        int pref = 0;
        long long ans = 0;
        for (int v : nums) {
            pref ^= v;
            auto it = freq.find(pref);
            if (it != freq.end()) {
                ans += it->second;
                ++(it->second);
            } else {
                freq[pref] = 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long beautifulSubarrays(int[] nums) {
        java.util.HashMap<Integer, Long> freq = new java.util.HashMap<>();
        freq.put(0, 1L);
        int prefixXor = 0;
        long result = 0L;
        for (int num : nums) {
            prefixXor ^= num;
            long count = freq.getOrDefault(prefixXor, 0L);
            result += count;
            freq.put(prefixXor, count + 1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def beautifulSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {0: 1}
        cur = 0
        ans = 0
        for num in nums:
            cur ^= num
            ans += freq.get(cur, 0)
            freq[cur] = freq.get(cur, 0) + 1
        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        pref = 0
        ans = 0
        for x in nums:
            pref ^= x
            ans += cnt[pref]
            cnt[pref] += 1
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

long long beautifulSubarrays(int* nums, int numsSize) {
    const int MAXXOR = 1 << 20; // sufficient for values up to 10^6
    long long *freq = (long long *)calloc(MAXXOR, sizeof(long long));
    long long ans = 0;
    int prefix = 0;
    freq[0] = 1; // empty prefix

    for (int i = 0; i < numsSize; ++i) {
        prefix ^= nums[i];
        ans += freq[prefix];
        freq[prefix]++;
    }

    free(freq);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long BeautifulSubarrays(int[] nums)
    {
        var freq = new System.Collections.Generic.Dictionary<int, long>();
        freq[0] = 1;
        int xor = 0;
        long result = 0;

        foreach (int num in nums)
        {
            xor ^= num;
            if (freq.TryGetValue(xor, out long count))
            {
                result += count;
                freq[xor] = count + 1;
            }
            else
            {
                freq[xor] = 1;
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
 * @return {number}
 */
var beautifulSubarrays = function(nums) {
    const freq = new Map();
    let prefixXor = 0;
    let result = 0;
    freq.set(0, 1);
    
    for (const num of nums) {
        prefixXor ^= num;
        const count = freq.get(prefixXor) || 0;
        result += count;
        freq.set(prefixXor, count + 1);
    }
    
    return result;
};
```

## Typescript

```typescript
function beautifulSubarrays(nums: number[]): number {
    const freq = new Map<number, number>();
    freq.set(0, 1);
    let xor = 0;
    let result = 0;
    for (const num of nums) {
        xor ^= num;
        const count = freq.get(xor) ?? 0;
        result += count;
        freq.set(xor, count + 1);
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
    function beautifulSubarrays($nums) {
        $freq = [0 => 1];
        $xor = 0;
        $ans = 0;
        foreach ($nums as $num) {
            $xor ^= $num;
            if (isset($freq[$xor])) {
                $ans += $freq[$xor];
                $freq[$xor]++;
            } else {
                $freq[$xor] = 1;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulSubarrays(_ nums: [Int]) -> Int {
        var prefixCount = [Int: Int]()
        prefixCount[0] = 1
        var xor = 0
        var result = 0
        
        for num in nums {
            xor ^= num
            if let cnt = prefixCount[xor] {
                result += cnt
            }
            prefixCount[xor, default: 0] += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun beautifulSubarrays(nums: IntArray): Long {
        val freq = HashMap<Int, Long>()
        var xor = 0
        var ans = 0L
        freq[0] = 1L
        for (num in nums) {
            xor = xor xor num
            val cnt = freq.getOrDefault(xor, 0L)
            ans += cnt
            freq[xor] = cnt + 1
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int beautifulSubarrays(List<int> nums) {
    final Map<int, int> freq = {0: 1};
    int xor = 0;
    int ans = 0;
    for (final v in nums) {
      xor ^= v;
      final count = freq[xor] ?? 0;
      ans += count;
      freq[xor] = count + 1;
    }
    return ans;
  }
}
```

## Golang

```go
func beautifulSubarrays(nums []int) int64 {
    cnt := make(map[int]int64)
    cnt[0] = 1
    var pref, ans int64
    // use int for xor computation, but store as int key
    px := 0
    for _, v := range nums {
        px ^= v
        if c, ok := cnt[px]; ok {
            ans += c
        }
        cnt[px]++
    }
    return ans
}
```

## Ruby

```ruby
def beautiful_subarrays(nums)
  freq = Hash.new(0)
  freq[0] = 1
  xor = 0
  result = 0
  nums.each do |num|
    xor ^= num
    result += freq[xor]
    freq[xor] += 1
  end
  result
end
```

## Scala

```scala
object Solution {
    def beautifulSubarrays(nums: Array[Int]): Long = {
        var ans: Long = 0L
        var pref: Int = 0
        val freq = scala.collection.mutable.Map[Int, Long]().withDefaultValue(0L)
        freq(0) = 1L // empty prefix

        for (num <- nums) {
            pref ^= num
            val cnt = freq(pref)
            ans += cnt
            freq.update(pref, cnt + 1L)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn beautiful_subarrays(nums: Vec<i32>) -> i64 {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, i64> = HashMap::new();
        freq.insert(0, 1);
        let mut ans: i64 = 0;
        let mut pref: i32 = 0;
        for &x in nums.iter() {
            pref ^= x;
            if let Some(&cnt) = freq.get(&pref) {
                ans += cnt;
            }
            *freq.entry(pref).or_insert(0) += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (beautiful-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([freq (make-hash)]
         [_ (hash-set! freq 0 1)]
         [xor 0]
         [ans 0])
    (for ([x nums])
      (set! xor (bitwise-xor xor x))
      (define cnt (hash-ref freq xor 0))
      (set! ans (+ ans cnt))
      (hash-set! freq xor (+ cnt 1)))
    ans))
```

## Erlang

```erlang
-spec beautiful_subarrays(Nums :: [integer()]) -> integer().
beautiful_subarrays(Nums) ->
    {Ans, _, _} = lists:foldl(
        fun(N, {Acc, CumXor, Map}) ->
            NewCum = CumXor bxor N,
            Count = maps:get(NewCum, Map, 0),
            {Acc + Count, NewCum, Map#{NewCum => Count + 1}}
        end,
        {0, 0, #{0 => 1}},
        Nums),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_subarrays(nums :: [integer]) :: integer
  def beautiful_subarrays(nums) do
    require Bitwise

    {ans, _, _} =
      Enum.reduce(nums, {0, 0, %{0 => 1}}, fn num, {cnt, cur_xor, freq} ->
        new_xor = Bitwise.bxor(cur_xor, num)
        prev = Map.get(freq, new_xor, 0)
        new_cnt = cnt + prev
        new_freq = Map.put(freq, new_xor, prev + 1)
        {new_cnt, new_xor, new_freq}
      end)

    ans
  end
end
```
