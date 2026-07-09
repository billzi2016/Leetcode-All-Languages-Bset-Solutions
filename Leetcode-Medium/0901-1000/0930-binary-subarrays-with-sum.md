# 0930. Binary Subarrays With Sum

## Cpp

```cpp
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int, long long> freq;
        freq[0] = 1;
        int cur = 0;
        long long ans = 0;
        for (int v : nums) {
            cur += v;
            if (freq.find(cur - goal) != freq.end())
                ans += freq[cur - goal];
            ++freq[cur];
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        freq.put(0, 1);
        long count = 0;
        int sum = 0;
        for (int num : nums) {
            sum += num;
            count += freq.getOrDefault(sum - goal, 0);
            freq.put(sum, freq.getOrDefault(sum, 0) + 1);
        }
        return (int) count;
    }
}
```

## Python

```python
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        from collections import defaultdict
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        ans = 0
        for num in nums:
            cur += num
            ans += freq.get(cur - goal, 0)
            freq[cur] += 1
        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        ans = 0
        for v in nums:
            cur += v
            ans += freq[cur - goal]
            freq[cur] += 1
        return ans
```

## C

```c
int numSubarraysWithSum(int* nums, int numsSize, int goal) {
    int *freq = (int *)calloc(numsSize + 1, sizeof(int));
    if (!freq) return 0;
    freq[0] = 1; // empty prefix
    int cur = 0;
    long long ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        cur += nums[i];
        if (cur >= goal) {
            ans += freq[cur - goal];
        }
        freq[cur] ++;
    }
    free(freq);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumSubarraysWithSum(int[] nums, int goal)
    {
        var prefixCount = new Dictionary<int, int>();
        prefixCount[0] = 1;
        long result = 0;
        int sum = 0;

        foreach (int num in nums)
        {
            sum += num;
            if (prefixCount.TryGetValue(sum - goal, out int cnt))
                result += cnt;

            if (prefixCount.ContainsKey(sum))
                prefixCount[sum]++;
            else
                prefixCount[sum] = 1;
        }

        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var numSubarraysWithSum = function(nums, goal) {
    let prefixCount = new Map();
    prefixCount.set(0, 1);
    let sum = 0;
    let result = 0;
    
    for (let i = 0; i < nums.length; ++i) {
        sum += nums[i];
        const need = sum - goal;
        if (prefixCount.has(need)) {
            result += prefixCount.get(need);
        }
        prefixCount.set(sum, (prefixCount.get(sum) || 0) + 1);
    }
    
    return result;
};
```

## Typescript

```typescript
function numSubarraysWithSum(nums: number[], goal: number): number {
    const prefixCount = new Map<number, number>();
    prefixCount.set(0, 1);
    let sum = 0;
    let result = 0;

    for (const num of nums) {
        sum += num;
        const need = sum - goal;
        if (prefixCount.has(need)) {
            result += prefixCount.get(need)!;
        }
        prefixCount.set(sum, (prefixCount.get(sum) ?? 0) + 1);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $goal
     * @return Integer
     */
    function numSubarraysWithSum($nums, $goal) {
        $count = 0;
        $prefix = 0;
        $freq = [0 => 1];
        foreach ($nums as $num) {
            $prefix += $num;
            $need = $prefix - $goal;
            if (isset($freq[$need])) {
                $count += $freq[$need];
            }
            if (!isset($freq[$prefix])) {
                $freq[$prefix] = 0;
            }
            $freq[$prefix]++;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func numSubarraysWithSum(_ nums: [Int], _ goal: Int) -> Int {
        var prefixCount = [Int: Int]()
        prefixCount[0] = 1
        var currentSum = 0
        var result = 0
        
        for num in nums {
            currentSum += num
            if let cnt = prefixCount[currentSum - goal] {
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
    fun numSubarraysWithSum(nums: IntArray, goal: Int): Int {
        val freq = HashMap<Int, Int>()
        freq[0] = 1
        var sum = 0
        var ans = 0L
        for (num in nums) {
            sum += num
            val need = sum - goal
            ans += freq.getOrDefault(need, 0)
            freq[sum] = freq.getOrDefault(sum, 0) + 1
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numSubarraysWithSum(List<int> nums, int goal) {
    final Map<int, int> freq = {0: 1};
    int cur = 0;
    int ans = 0;
    for (final num in nums) {
      cur += num;
      final need = cur - goal;
      if (freq.containsKey(need)) {
        ans += freq[need]!;
      }
      freq[cur] = (freq[cur] ?? 0) + 1;
    }
    return ans;
  }
}
```

## Golang

```go
func numSubarraysWithSum(nums []int, goal int) int {
    freq := make(map[int]int)
    freq[0] = 1
    sum, ans := 0, 0
    for _, v := range nums {
        sum += v
        if cnt, ok := freq[sum-goal]; ok {
            ans += cnt
        }
        freq[sum]++
    }
    return ans
}
```

## Ruby

```ruby
def num_subarrays_with_sum(nums, goal)
  freq = Hash.new(0)
  freq[0] = 1
  cur = 0
  ans = 0
  nums.each do |x|
    cur += x
    ans += freq[cur - goal]
    freq[cur] += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numSubarraysWithSum(nums: Array[Int], goal: Int): Int = {
        def atMost(k: Int): Long = {
            var left = 0
            var sum = 0
            var cnt: Long = 0L
            for (right <- nums.indices) {
                sum += nums(right)
                while (left <= right && sum > k) {
                    sum -= nums(left)
                    left += 1
                }
                cnt += (right - left + 1).toLong
            }
            cnt
        }
        val result = atMost(goal) - atMost(goal - 1)
        result.toInt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        fn at_most(arr: &[i32], k: i32) -> i64 {
            if k < 0 {
                return 0;
            }
            let mut left = 0usize;
            let mut sum = 0i32;
            let mut cnt = 0i64;
            for right in 0..arr.len() {
                sum += arr[right];
                while sum > k {
                    sum -= arr[left];
                    left += 1;
                }
                cnt += (right - left + 1) as i64;
            }
            cnt
        }

        let result = at_most(&nums, goal) - at_most(&nums, goal - 1);
        result as i32
    }
}
```

## Racket

```racket
(define/contract (num-subarrays-with-sum nums goal)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ((freq (make-hash))
        (ans 0)
        (cur 0))
    (hash-set! freq 0 1)
    (for ([x nums])
      (set! cur (+ cur x))
      (define need (- cur goal))
      (when (hash-has-key? freq need)
        (set! ans (+ ans (hash-ref freq need))))
      (hash-set! freq cur (+ 1 (hash-ref freq cur 0))))
    ans))
```

## Erlang

```erlang
-spec num_subarrays_with_sum(Nums :: [integer()], Goal :: integer()) -> integer().
num_subarrays_with_sum(Nums, Goal) ->
    num_subarrays_with_sum(Nums, Goal, 0, #{0 => 1}, 0).

num_subarrays_with_sum([], _Goal, _Sum, _Map, Count) ->
    Count;
num_subarrays_with_sum([H|T], Goal, Sum, Map, Count) ->
    NewSum = Sum + H,
    Add = maps:get(NewSum - Goal, Map, 0),
    NewCount = Count + Add,
    NewMap = maps:put(NewSum, maps:get(NewSum, Map, 0) + 1, Map),
    num_subarrays_with_sum(T, Goal, NewSum, NewMap, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_subarrays_with_sum(nums :: [integer], goal :: integer) :: integer
  def num_subarrays_with_sum(nums, goal) do
    {count, _, _} =
      Enum.reduce(nums, {0, 0, %{0 => 1}}, fn x, {cnt, sum, freq} ->
        new_sum = sum + x
        add = Map.get(freq, new_sum - goal, 0)
        new_cnt = cnt + add
        new_freq = Map.update(freq, new_sum, 1, &(&1 + 1))
        {new_cnt, new_sum, new_freq}
      end)

    count
  end
end
```
