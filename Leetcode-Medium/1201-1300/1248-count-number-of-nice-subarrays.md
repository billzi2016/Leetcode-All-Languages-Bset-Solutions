# 1248. Count Number of Nice Subarrays

## Cpp

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        freq[0] = 1;
        int prefix = 0;
        long long result = 0;
        for (int num : nums) {
            prefix += (num & 1);
            if (freq.find(prefix - k) != freq.end())
                result += freq[prefix - k];
            ++freq[prefix];
        }
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        java.util.Map<Integer, Integer> prefixCount = new java.util.HashMap<>();
        prefixCount.put(0, 1);
        int curSum = 0;
        int result = 0;
        for (int num : nums) {
            curSum += (num & 1); // add 1 if odd, else 0
            result += prefixCount.getOrDefault(curSum - k, 0);
            prefixCount.put(curSum, prefixCount.getOrDefault(curSum, 0) + 1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_counts = {0: 1}
        cur_sum = 0
        result = 0
        for num in nums:
            cur_sum += num & 1  # add 1 if odd, else 0
            result += prefix_counts.get(cur_sum - k, 0)
            prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1
        return result
```

## Python3

```python
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        cur_sum = 0
        result = 0
        for num in nums:
            cur_sum += num & 1  # add 1 if odd, else 0
            result += prefix_counts.get(cur_sum - k, 0)
            prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1
        return result
```

## C

```c
#include <stdlib.h>

int numberOfSubarrays(int* nums, int numsSize, int k) {
    // Prefix sum of odd counts ranges from 0 to numsSize
    long long *freq = (long long *)calloc(numsSize + 1, sizeof(long long));
    if (!freq) return 0;
    
    freq[0] = 1;               // empty prefix
    int cur = 0;
    long long ans = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] & 1) cur++;                // count odd numbers
        if (cur >= k) {
            ans += freq[cur - k];
        }
        freq[cur]++;
    }
    
    free(freq);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfSubarrays(int[] nums, int k) {
        var prefixCount = new Dictionary<int, int>();
        prefixCount[0] = 1;
        int currSum = 0;
        long result = 0;
        foreach (int num in nums) {
            currSum += (num & 1);
            if (prefixCount.TryGetValue(currSum - k, out int cnt)) {
                result += cnt;
            }
            if (prefixCount.ContainsKey(currSum))
                prefixCount[currSum]++;
            else
                prefixCount[currSum] = 1;
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
var numberOfSubarrays = function(nums, k) {
    const prefixCount = new Map();
    prefixCount.set(0, 1);
    let curSum = 0;
    let result = 0;
    
    for (const num of nums) {
        curSum += (num & 1); // add 1 if odd, else 0
        const need = curSum - k;
        if (prefixCount.has(need)) {
            result += prefixCount.get(need);
        }
        prefixCount.set(curSum, (prefixCount.get(curSum) || 0) + 1);
    }
    
    return result;
};
```

## Typescript

```typescript
function numberOfSubarrays(nums: number[], k: number): number {
    const prefixMap = new Map<number, number>();
    prefixMap.set(0, 1);
    let oddSum = 0;
    let result = 0;

    for (const num of nums) {
        oddSum += num & 1; // add 1 if odd, else 0
        const need = oddSum - k;
        if (prefixMap.has(need)) {
            result += prefixMap.get(need)!;
        }
        prefixMap.set(oddSum, (prefixMap.get(oddSum) ?? 0) + 1);
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
    function numberOfSubarrays($nums, $k) {
        $prefix = [0 => 1];
        $curr = 0;
        $ans = 0;
        foreach ($nums as $num) {
            $curr += $num % 2; // add 1 if odd, else 0
            $need = $curr - $k;
            if (isset($prefix[$need])) {
                $ans += $prefix[$need];
            }
            if (isset($prefix[$curr])) {
                $prefix[$curr]++;
            } else {
                $prefix[$curr] = 1;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var prefixCount = [Int: Int]()
        prefixCount[0] = 1
        var currentSum = 0
        var result = 0
        
        for num in nums {
            currentSum += (num & 1)
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
    fun numberOfSubarrays(nums: IntArray, k: Int): Int {
        var prefix = 0
        var result = 0L
        val freq = HashMap<Int, Int>()
        freq[0] = 1
        for (num in nums) {
            if ((num and 1) == 1) prefix++
            val need = prefix - k
            result += freq.getOrDefault(need, 0)
            freq[prefix] = freq.getOrDefault(prefix, 0) + 1
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSubarrays(List<int> nums, int k) {
    final Map<int, int> freq = {0: 1};
    int sum = 0;
    int result = 0;

    for (final num in nums) {
      if ((num & 1) == 1) sum++;
      final need = sum - k;
      if (freq.containsKey(need)) {
        result += freq[need]!;
      }
      freq[sum] = (freq[sum] ?? 0) + 1;
    }

    return result;
  }
}
```

## Golang

```go
func numberOfSubarrays(nums []int, k int) int {
	freq := make(map[int]int)
	freq[0] = 1
	curr := 0
	ans := 0
	for _, v := range nums {
		if v%2 == 1 {
			curr++
		}
		if cnt, ok := freq[curr-k]; ok {
			ans += cnt
		}
		freq[curr]++
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def number_of_subarrays(nums, k)
  prefix_counts = Hash.new(0)
  prefix_counts[0] = 1
  curr_sum = 0
  result = 0

  nums.each do |num|
    curr_sum += num & 1
    result += prefix_counts[curr_sum - k] if prefix_counts.key?(curr_sum - k)
    prefix_counts[curr_sum] += 1
  end

  result
end
```

## Scala

```scala
object Solution {
    def numberOfSubarrays(nums: Array[Int], k: Int): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        freq(0) = 1
        var sum = 0
        var ans: Long = 0L
        for (num <- nums) {
            if ((num & 1) == 1) sum += 1
            val need = sum - k
            ans += freq.getOrElse(need, 0)
            freq(sum) = freq.getOrElse(sum, 0) + 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let mut prefix: HashMap<i32, i64> = HashMap::new();
        prefix.insert(0, 1);
        let mut curr_sum: i32 = 0;
        let mut ans: i64 = 0;

        for num in nums {
            if num % 2 != 0 {
                curr_sum += 1;
            }
            let need = curr_sum - k;
            if let Some(cnt) = prefix.get(&need) {
                ans += *cnt;
            }
            *prefix.entry(curr_sum).or_insert(0) += 1;
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([prefix (make-hash)]
         [_ (hash-set! prefix 0 1)] ; initial prefix sum count
         [curr-sum 0]
         [result 0])
    (for ([x nums])
      (set! curr-sum (+ curr-sum (modulo x 2))) ; add 1 if odd, else 0
      (let* ([need (- curr-sum k)]
             [add (hash-ref prefix need 0)])
        (set! result (+ result add)))
      (hash-set! prefix curr-sum (+ 1 (hash-ref prefix curr-sum 0))))
    result))
```

## Erlang

```erlang
-spec number_of_subarrays(Nums :: [integer()], K :: integer()) -> integer().
number_of_subarrays(Nums, K) ->
    {_, Answer, _} = lists:foldl(
        fun(Num, {CurSum, Acc, Map}) ->
            NewSum = CurSum + (Num band 1),
            Add = maps:get(NewSum - K, Map, 0),
            NewAcc = Acc + Add,
            NewMap = maps:update_with(NewSum,
                                      fun(V) -> V + 1 end,
                                      1,
                                      Map),
            {NewSum, NewAcc, NewMap}
        end,
        {0, 0, #{0 => 1}},
        Nums),
    Answer.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_subarrays(nums :: [integer], k :: integer) :: integer
  def number_of_subarrays(nums, k) do
    {ans, _curr, _freq} =
      Enum.reduce(nums, {0, 0, %{0 => 1}}, fn num, {ans, curr, freq} ->
        curr = if rem(num, 2) == 1, do: curr + 1, else: curr
        ans = ans + Map.get(freq, curr - k, 0)
        freq = Map.update(freq, curr, 1, &(&1 + 1))
        {ans, curr, freq}
      end)

    ans
  end
end
```
