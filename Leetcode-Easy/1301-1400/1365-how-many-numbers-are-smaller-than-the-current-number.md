# 1365. How Many Numbers Are Smaller Than the Current Number

## Cpp

```cpp
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        const int MAX_VAL = 100;
        vector<int> freq(MAX_VAL + 1, 0);
        for (int v : nums) ++freq[v];
        
        vector<int> lessThan(MAX_VAL + 1, 0);
        int cum = 0;
        for (int i = 0; i <= MAX_VAL; ++i) {
            lessThan[i] = cum;
            cum += freq[i];
        }
        
        vector<int> ans;
        ans.reserve(nums.size());
        for (int v : nums) ans.push_back(lessThan[v]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] freq = new int[101];
        for (int n : nums) {
            freq[n]++;
        }
        int[] prefix = new int[101];
        int cum = 0;
        for (int i = 0; i <= 100; i++) {
            prefix[i] = cum;
            cum += freq[i];
        }
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            ans[i] = prefix[nums[i]];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = [0] * 101
        for v in nums:
            freq[v] += 1

        less = [0] * 101
        total = 0
        for i in range(101):
            less[i] = total
            total += freq[i]

        return [less[v] for v in nums]
```

## Python3

```python
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        for v in nums:
            freq[v] += 1
        prefix = [0] * 101
        total = 0
        for i in range(101):
            prefix[i] = total
            total += freq[i]
        return [prefix[v] for v in nums]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* result = (int*)malloc(numsSize * sizeof(int));
    if (!result) return NULL;

    int count[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        count[nums[i]]++;
    }

    int cum = 0;
    for (int i = 0; i <= 100; ++i) {
        int temp = count[i];
        count[i] = cum;   // numbers smaller than i
        cum += temp;
    }

    for (int i = 0; i < numsSize; ++i) {
        result[i] = count[nums[i]];
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] SmallerNumbersThanCurrent(int[] nums)
    {
        int[] freq = new int[101];
        foreach (int v in nums) freq[v]++;

        int[] smaller = new int[101];
        int cum = 0;
        for (int i = 0; i <= 100; i++)
        {
            smaller[i] = cum;
            cum += freq[i];
        }

        int n = nums.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++)
        {
            result[i] = smaller[nums[i]];
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    const freq = new Array(101).fill(0);
    for (const v of nums) {
        freq[v]++;
    }
    const less = new Array(101).fill(0);
    let cum = 0;
    for (let i = 0; i <= 100; i++) {
        less[i] = cum;
        cum += freq[i];
    }
    return nums.map(v => less[v]);
};
```

## Typescript

```typescript
function smallerNumbersThanCurrent(nums: number[]): number[] {
    const freq = new Array(101).fill(0);
    for (const n of nums) {
        freq[n]++;
    }
    const less = new Array(101).fill(0);
    let cumulative = 0;
    for (let i = 0; i <= 100; i++) {
        less[i] = cumulative;
        cumulative += freq[i];
    }
    return nums.map(n => less[n]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallerNumbersThanCurrent($nums) {
        $freq = array_fill(0, 101, 0);
        foreach ($nums as $v) {
            $freq[$v]++;
        }
        $prefix = array_fill(0, 101, 0);
        $sum = 0;
        for ($i = 0; $i <= 100; $i++) {
            $prefix[$i] = $sum;
            $sum += $freq[$i];
        }
        $result = [];
        foreach ($nums as $v) {
            $result[] = $prefix[$v];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
        var freq = Array(repeating: 0, count: 101)
        for v in nums {
            freq[v] += 1
        }
        var less = Array(repeating: 0, count: 101)
        var cumulative = 0
        for i in 0...100 {
            less[i] = cumulative
            cumulative += freq[i]
        }
        var result = [Int]()
        result.reserveCapacity(nums.count)
        for v in nums {
            result.append(less[v])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallerNumbersThanCurrent(nums: IntArray): IntArray {
        val count = IntArray(101)
        for (n in nums) {
            count[n]++
        }
        val less = IntArray(101)
        var sum = 0
        for (i in 0..100) {
            less[i] = sum
            sum += count[i]
        }
        val res = IntArray(nums.size)
        for (i in nums.indices) {
            res[i] = less[nums[i]]
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> smallerNumbersThanCurrent(List<int> nums) {
    const int maxVal = 100;
    List<int> freq = List.filled(maxVal + 1, 0);
    for (var v in nums) {
      freq[v]++;
    }
    List<int> prefix = List.filled(maxVal + 1, 0);
    int sum = 0;
    for (int i = 0; i <= maxVal; i++) {
      prefix[i] = sum;
      sum += freq[i];
    }
    List<int> res = List.filled(nums.length, 0);
    for (int i = 0; i < nums.length; i++) {
      res[i] = prefix[nums[i]];
    }
    return res;
  }
}
```

## Golang

```go
func smallerNumbersThanCurrent(nums []int) []int {
	freq := make([]int, 101)
	for _, v := range nums {
		freq[v]++
	}
	for i := 1; i <= 100; i++ {
		freq[i] += freq[i-1]
	}
	res := make([]int, len(nums))
	for i, v := range nums {
		if v == 0 {
			res[i] = 0
		} else {
			res[i] = freq[v-1]
		}
	}
	return res
}
```

## Ruby

```ruby
def smaller_numbers_than_current(nums)
  cnt = Array.new(101, 0)
  nums.each { |num| cnt[num] += 1 }

  less = Array.new(101, 0)
  sum = 0
  (0..100).each do |i|
    less[i] = sum
    sum += cnt[i]
  end

  nums.map { |num| less[num] }
end
```

## Scala

```scala
object Solution {
    def smallerNumbersThanCurrent(nums: Array[Int]): Array[Int] = {
        val maxVal = 100
        val freq = new Array[Int](maxVal + 1)
        for (n <- nums) {
            freq(n) += 1
        }
        val less = new Array[Int](maxVal + 1)
        var cumulative = 0
        for (i <- 0 to maxVal) {
            less(i) = cumulative
            cumulative += freq(i)
        }
        nums.map(less(_))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let mut freq = [0usize; 101];
        for &v in &nums {
            freq[v as usize] += 1;
        }
        let mut less = [0i32; 101];
        let mut cum = 0usize;
        for i in 0..=100 {
            less[i] = cum as i32;
            cum += freq[i];
        }
        nums.iter().map(|&v| less[v as usize]).collect()
    }
}
```

## Racket

```racket
(define/contract (smaller-numbers-than-current nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([max-val 100]
         [freq (make-vector (+ max-val 1) 0)])
    ;; count frequencies
    (for-each (lambda (x)
                (vector-set! freq x (+ 1 (vector-ref freq x))))
              nums)
    ;; compute cumulative counts: cum[v] = number of elements < v
    (let ([cum (make-vector (+ max-val 1) 0)])
      (let loop ((i 1))
        (when (<= i max-val)
          (vector-set! cum i (+ (vector-ref cum (- i 1)) (vector-ref freq (- i 1))))
          (loop (+ i 1))))
      ;; build result list
      (map (lambda (x) (vector-ref cum x)) nums))))
```

## Erlang

```erlang
-spec smaller_numbers_than_current([integer()]) -> [integer()].
smaller_numbers_than_current(Nums) ->
    Freq = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N, fun(V) -> V + 1 end, 1, Acc)
        end,
        #{},
        Nums
    ),
    {_, Prefix} = lists:foldl(
        fun(V, {AccSum, Map}) ->
            Count = maps:get(V, Freq, 0),
            NewMap = maps:put(V, AccSum, Map),
            {AccSum + Count, NewMap}
        end,
        {0, #{}},
        lists:seq(0, 100)
    ),
    [maps:get(N, Prefix) || N <- Nums].
```

## Elixir

```elixir
defmodule Solution do
  @spec smaller_numbers_than_current(nums :: [integer]) :: [integer]
  def smaller_numbers_than_current(nums) do
    freq = Enum.reduce(nums, %{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)

    {less_map, _} =
      0..100
      |> Enum.reduce({%{}, 0}, fn i, {map, sum} ->
        count = Map.get(freq, i, 0)
        {Map.put(map, i, sum), sum + count}
      end)

    Enum.map(nums, fn x -> Map.get(less_map, x) end)
  end
end
```
