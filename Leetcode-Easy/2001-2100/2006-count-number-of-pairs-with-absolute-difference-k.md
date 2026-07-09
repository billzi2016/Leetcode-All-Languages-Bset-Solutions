# 2006. Count Number of Pairs With Absolute Difference K

## Cpp

```cpp
class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int x : nums) ++freq[x];
        long long ans = 0;
        for (const auto& p : freq) {
            int val = p.first;
            auto it = freq.find(val + k);
            if (it != freq.end()) {
                ans += 1LL * p.second * it->second;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int countKDifference(int[] nums, int k) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        int count = 0;
        for (int num : nums) {
            count += freq.getOrDefault(num - k, 0);
            count += freq.getOrDefault(num + k, 0);
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        freq = Counter(nums)
        ans = 0
        for num in freq:
            target = num + k
            if target in freq:
                ans += freq[num] * freq[target]
        return ans
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0
        for num in freq:
            target = num + k
            if target in freq:
                ans += freq[num] * freq[target]
        return ans
```

## C

```c
int countKDifference(int* nums, int numsSize, int k) {
    int freq[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] >= 1 && nums[i] <= 100)
            freq[nums[i]]++;
    }
    long long ans = 0;
    if (k == 0) {
        for (int v = 1; v <= 100; ++v) {
            if (freq[v] > 1)
                ans += (long long)freq[v] * (freq[v] - 1) / 2;
        }
    } else {
        for (int v = 1; v + k <= 100; ++v) {
            ans += (long long)freq[v] * freq[v + k];
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountKDifference(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        int count = 0;
        foreach (int x in nums) {
            if (freq.TryGetValue(x - k, out int c1)) count += c1;
            if (k != 0 && freq.TryGetValue(x + k, out int c2)) count += c2;
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        return count;
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
var countKDifference = function(nums, k) {
    const freq = new Map();
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }
    let ans = 0;
    for (const [num, cnt] of freq.entries()) {
        const target = num + k;
        if (freq.has(target)) {
            ans += cnt * freq.get(target);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countKDifference(nums: number[], k: number): number {
    const freq = new Map<number, number>();
    let result = 0;
    for (const num of nums) {
        const lower = num - k;
        const higher = num + k;
        if (freq.has(lower)) result += freq.get(lower)!;
        if (freq.has(higher)) result += freq.get(higher)!;
        freq.set(num, (freq.get(num) ?? 0) + 1);
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
    function countKDifference($nums, $k) {
        $freq = [];
        foreach ($nums as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }

        $count = 0;
        foreach ($freq as $value => $cnt) {
            $target = $value + $k;
            if (isset($freq[$target])) {
                $count += $cnt * $freq[$target];
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countKDifference(_ nums: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        var result = 0
        for num in nums {
            if let cnt = freq[num - k] {
                result += cnt
            }
            if let cnt = freq[num + k] {
                result += cnt
            }
            freq[num, default: 0] += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countKDifference(nums: IntArray, k: Int): Int {
        val freq = IntArray(101)
        var ans = 0
        for (num in nums) {
            if (num - k >= 0) ans += freq[num - k]
            if (num + k <= 100) ans += freq[num + k]
            freq[num]++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countKDifference(List<int> nums, int k) {
    final Map<int, int> freq = {};
    for (var num in nums) {
      freq.update(num, (v) => v + 1, ifAbsent: () => 1);
    }
    int ans = 0;
    for (var entry in freq.entries) {
      int target = entry.key + k;
      if (freq.containsKey(target)) {
        ans += entry.value * freq[target]!;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countKDifference(nums []int, k int) int {
	freq := make(map[int]int)
	for _, v := range nums {
		freq[v]++
	}
	ans := 0
	for val, cnt := range freq {
		if c2, ok := freq[val+k]; ok {
			ans += cnt * c2
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_k_difference(nums, k)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  ans = 0
  freq.each do |v, cnt|
    if (c2 = freq[v + k])
      ans += cnt * c2
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countKDifference(nums: Array[Int], k: Int): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        var ans = 0
        for (num <- nums) {
            ans += freq.getOrElse(num - k, 0)
            ans += freq.getOrElse(num + k, 0)
            freq(num) = freq(num) + 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_k_difference(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::HashMap;
        let mut freq = HashMap::new();
        for &num in &nums {
            *freq.entry(num).or_insert(0i32) += 1;
        }
        let mut ans: i64 = 0;
        if k == 0 {
            for &cnt in freq.values() {
                ans += (cnt as i64) * ((cnt - 1) as i64) / 2;
            }
        } else {
            for (&num, &cnt) in freq.iter() {
                if let Some(&cnt2) = freq.get(&(num + k)) {
                    ans += (cnt as i64) * (cnt2 as i64);
                }
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-k-difference nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ((freq (make-hash)))
    ;; build frequency map
    (for ([x nums])
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    (if (= k 0)
        ;; pairs of equal numbers: nC2 for each value
        (foldl (lambda (key acc)
                 (let ((c (hash-ref freq key)))
                   (+ acc (/ (* c (- c 1)) 2))))
               0
               (hash-keys freq))
        ;; k > 0 : count pairs (v, v+k)
        (foldl (lambda (key acc)
                 (let* ((c (hash-ref freq key))
                        (target (+ key k))
                        (c2 (hash-ref freq target #f)))
                   (if c2
                       (+ acc (* c c2))
                       acc)))
               0
               (hash-keys freq)))))
```

## Erlang

```erlang
-spec count_k_difference(Nums :: [integer()], K :: integer()) -> integer().
count_k_difference(Nums, K) ->
    Freq = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Nums
    ),
    maps:fold(
        fun(Key, Val, Sum) ->
            case maps:get(Key + K, Freq, undefined) of
                undefined -> Sum;
                OtherVal -> Sum + Val * OtherVal
            end
        end,
        0,
        Freq
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_k_difference(nums :: [integer], k :: integer) :: integer
  def count_k_difference(nums, k) do
    freq = Enum.reduce(nums, %{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)

    if k == 0 do
      Enum.reduce(freq, 0, fn {_val, cnt}, sum ->
        sum + div(cnt * (cnt - 1), 2)
      end)
    else
      Enum.reduce(freq, 0, fn {val, cnt}, sum ->
        case Map.get(freq, val + k) do
          nil -> sum
          cnt2 -> sum + cnt * cnt2
        end
      end)
    end
  end
end
```
