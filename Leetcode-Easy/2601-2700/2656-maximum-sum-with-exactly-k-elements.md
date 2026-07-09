# 2656. Maximum Sum With Exactly K Elements

## Cpp

```cpp
class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        int mx = *max_element(nums.begin(), nums.end());
        long long ans = 1LL * k * mx + 1LL * k * (k - 1) / 2;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maximizeSum(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num > max) {
                max = num;
            }
        }
        return max * k + k * (k - 1) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        return mx * k + k * (k - 1) // 2
```

## Python3

```python
from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        return k * max_val + k * (k - 1) // 2
```

## C

```c
int maximizeSum(int* nums, int numsSize, int k) {
    int maxVal = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    return k * maxVal + k * (k - 1) / 2;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximizeSum(int[] nums, int k) {
        var pq = new PriorityQueue<int, int>();
        foreach (var v in nums) {
            pq.Enqueue(v, -v);
        }
        long sum = 0;
        for (int i = 0; i < k; i++) {
            int cur = pq.Dequeue();
            sum += cur;
            pq.Enqueue(cur + 1, -(cur + 1));
        }
        return (int)sum;
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
var maximizeSum = function(nums, k) {
    let maxVal = Math.max(...nums);
    return k * maxVal + (k * (k - 1)) / 2;
};
```

## Typescript

```typescript
function maximizeSum(nums: number[], k: number): number {
    let total = 0;
    const n = nums.length;
    for (let i = 0; i < k; i++) {
        let maxIdx = 0;
        for (let j = 1; j < n; j++) {
            if (nums[j] > nums[maxIdx]) {
                maxIdx = j;
            }
        }
        total += nums[maxIdx];
        nums[maxIdx]++;
    }
    return total;
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
    function maximizeSum($nums, $k) {
        $max = max($nums);
        return $k * $max + intdiv($k * ($k - 1), 2);
    }
}
```

## Swift

```swift
class Solution {
    func maximizeSum(_ nums: [Int], _ k: Int) -> Int {
        guard let maxVal = nums.max() else { return 0 }
        return k * maxVal + (k * (k - 1)) / 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeSum(nums: IntArray, k: Int): Int {
        val maxHeap = java.util.PriorityQueue<Int>(compareByDescending { it })
        for (num in nums) {
            maxHeap.add(num)
        }
        var sum = 0
        repeat(k) {
            val cur = maxHeap.poll()
            sum += cur
            maxHeap.offer(cur + 1)
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int maximizeSum(List<int> nums, int k) {
    int total = 0;
    for (int i = 0; i < k; i++) {
      int maxIdx = 0;
      for (int j = 1; j < nums.length; j++) {
        if (nums[j] > nums[maxIdx]) {
          maxIdx = j;
        }
      }
      total += nums[maxIdx];
      nums[maxIdx] += 1;
    }
    return total;
  }
}
```

## Golang

```go
func maximizeSum(nums []int, k int) int {
    total := 0
    n := len(nums)
    for i := 0; i < k; i++ {
        maxIdx := 0
        for j := 1; j < n; j++ {
            if nums[j] > nums[maxIdx] {
                maxIdx = j
            }
        }
        total += nums[maxIdx]
        nums[maxIdx]++
    }
    return total
}
```

## Ruby

```ruby
def maximize_sum(nums, k)
  total = 0
  k.times do
    max_idx = 0
    max_val = nums[0]
    nums.each_with_index do |v, i|
      if v > max_val
        max_val = v
        max_idx = i
      end
    end
    total += max_val
    nums[max_idx] = max_val + 1
  end
  total
end
```

## Scala

```scala
import scala.collection.mutable.PriorityQueue

object Solution {
  def maximizeSum(nums: Array[Int], k: Int): Int = {
    val pq = PriorityQueue.empty[Int](Ordering[Int].reverse)
    nums.foreach(pq.enqueue(_))
    var sum: Long = 0
    for (_ <- 0 until k) {
      val cur = pq.dequeue()
      sum += cur
      pq.enqueue(cur + 1)
    }
    sum.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_sum(nums: Vec<i32>, k: i32) -> i32 {
        let max_val = *nums.iter().max().unwrap();
        let k_i64 = k as i64;
        let max_i64 = max_val as i64;
        (max_i64 * k_i64 + k_i64 * (k_i64 - 1) / 2) as i32
    }
}
```

## Racket

```racket
(define/contract (maximize-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([vec (list->vector nums)]
         [n (vector-length vec)])
    (let loop ((remaining k) (total 0))
      (if (= remaining 0)
          total
          (let find-max ((idx 0) (best-idx 0) (best-val (vector-ref vec 0)))
            (if (= idx n)
                (let ([max-val best-val])
                  (vector-set! vec best-idx (+ max-val 1))
                  (loop (- remaining 1) (+ total max-val)))
                (let ([val (vector-ref vec idx)])
                  (if (> val best-val)
                      (find-max (+ idx 1) idx val)
                      (find-max (+ idx 1) best-idx best-val)))))))))
```

## Erlang

```erlang
-spec maximize_sum(Nums :: [integer()], K :: integer()) -> integer().
maximize_sum(Nums, K) ->
    maximize_sum(Nums, K, 0).

%% Recursive helper with accumulator
-spec maximize_sum([integer()], non_neg_integer(), integer()) -> integer().
maximize_sum(_, 0, Acc) ->
    Acc;
maximize_sum(Nums, K, Acc) when K > 0 ->
    Max = lists:max(Nums),
    NewAcc = Acc + Max,
    NewNums = replace_first(Max, Max + 1, Nums),
    maximize_sum(NewNums, K - 1, NewAcc).

%% Replace the first occurrence of Old with New in the list
-spec replace_first(integer(), integer(), [integer()]) -> [integer()].
replace_first(_, _, []) ->
    [];
replace_first(Old, New, [Old | Tail]) ->
    [New | Tail];
replace_first(Old, New, [H | Tail]) ->
    [H | replace_first(Old, New, Tail)].
```

## Elixir

```elixir
defmodule Solution do
  @spec maximize_sum(nums :: [integer], k :: integer) :: integer
  def maximize_sum(nums, k) do
    do_maximize(nums, k, 0)
  end

  defp do_maximize(_nums, 0, acc), do: acc

  defp do_maximize(nums, k, acc) do
    max_val = Enum.max(nums)
    new_nums = replace_one(nums, max_val)
    do_maximize(new_nums, k - 1, acc + max_val)
  end

  defp replace_one([], _max), do: []

  defp replace_one([head | tail], max) when head == max do
    [head + 1 | tail]
  end

  defp replace_one([head | tail], max) do
    [head | replace_one(tail, max)]
  end
end
```
