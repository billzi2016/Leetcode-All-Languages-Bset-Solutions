# 3379. Transformed Array

## Cpp

```cpp
class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        for (int i = 0; i < n; ++i) {
            long long idx = (long long)i + nums[i];
            idx %= n;
            if (idx < 0) idx += n;
            result[i] = nums[(int)idx];
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int idx = (i + nums[i]) % n;
            if (idx < 0) idx += n;
            result[i] = nums[idx];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        for i, v in enumerate(nums):
            target = (i + v) % n
            result[i] = nums[target]
        return result
```

## Python3

```python
from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]
```

## C

```c
/**
 * Note: The the returned array must be malloced, assume caller calls free().
 */
int* constructTransformedArray(int* nums, int numsSize, int* returnSize){
    // Frequency array for values in range [-100, 100]
    int freq[201] = {0};
    int maxVal = nums[0];
    for (int i = 0; i < numsSize; ++i) {
        int idx = nums[i] + 100;
        freq[idx]++;
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    
    // Find mode (most frequent value, tie -> smaller value)
    int mode = nums[0];
    int bestCnt = freq[mode + 100];
    for (int v = -100; v <= 100; ++v) {
        int cnt = freq[v + 100];
        if (cnt > bestCnt || (cnt == bestCnt && v < mode)) {
            bestCnt = cnt;
            mode = v;
        }
    }
    
    // Build result
    int* res = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        res[i] = mode;
    }
    if (numsSize > 0) {
        res[numsSize - 1] = maxVal;
    }
    
    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ConstructTransformedArray(int[] nums) {
        int n = nums.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            long idx = (long)i + nums[i];
            int target = (int)((idx % n + n) % n);
            result[i] = nums[target];
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
var constructTransformedArray = function(nums) {
    const n = nums.length;
    if (n === 0) return [];
    if (n === 1) return [nums[0]];
    
    let max = -Infinity, second = -Infinity;
    for (const v of nums) {
        if (v > max) {
            second = max;
            max = v;
        } else if (v > second) {
            second = v;
        }
    }
    // In case all elements are the same and n>1, second will be -Infinity.
    // Set it to max in that scenario.
    if (second === -Infinity) second = max;
    
    const result = new Array(n);
    for (let i = 0; i < n - 1; ++i) {
        result[i] = second;
    }
    result[n - 1] = max;
    return result;
};
```

## Typescript

```typescript
function constructTransformedArray(nums: number[]): number[] {
    const n = nums.length;
    const res: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        let idx = (i + nums[i]) % n;
        if (idx < 0) idx += n;
        res[i] = nums[idx];
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function constructTransformedArray($nums) {
        $n = count($nums);
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            $idx = ($i + $nums[$i]) % $n;
            if ($idx < 0) {
                $idx += $n;
            }
            $result[] = $nums[$idx];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func constructTransformedArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        guard n > 0 else { return [] }
        
        var maxVal = nums[0]
        for v in nums {
            if v > maxVal { maxVal = v }
        }
        
        var secondMax = Int.min
        var hasSecond = false
        for v in nums {
            if v != maxVal {
                if !hasSecond || v > secondMax {
                    secondMax = v
                    hasSecond = true
                }
            }
        }
        if !hasSecond { // all elements are equal
            secondMax = maxVal
        }
        
        var result = Array(repeating: secondMax, count: n)
        result[n - 1] = maxVal
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun constructTransformedArray(nums: IntArray): IntArray {
        val n = nums.size
        val result = IntArray(n)
        for (i in 0 until n) {
            var idx = i + nums[i]
            idx %= n
            if (idx < 0) idx += n
            result[i] = nums[idx]
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> constructTransformedArray(List<int> nums) {
    int n = nums.length;
    List<int> result = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int idx = (i + nums[i]) % n;
      if (idx < 0) idx += n;
      result[i] = nums[idx];
    }
    return result;
  }
}
```

## Golang

```go
func constructTransformedArray(nums []int) []int {
    n := len(nums)
    result := make([]int, n)
    for i, v := range nums {
        idx := (i + v) % n
        if idx < 0 {
            idx += n
        }
        result[i] = nums[idx]
    }
    return result
}
```

## Ruby

```ruby
def construct_transformed_array(nums)
  n = nums.length
  result = Array.new(n)
  n.times do |i|
    target = (i + nums[i]) % n
    result[i] = nums[target]
  end
  result
end
```

## Scala

```scala
object Solution {
    def constructTransformedArray(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val res = new Array[Int](n)
        for (i <- 0 until n) {
            var idx = i + nums(i)
            idx %= n
            if (idx < 0) idx += n
            res(i) = nums(idx)
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn construct_transformed_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut result = Vec::with_capacity(nums.len());
        for (i, &v) in nums.iter().enumerate() {
            let mut idx = (i as i32 + v) % n;
            if idx < 0 {
                idx += n;
            }
            result.push(nums[idx as usize]);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (construct-transformed-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (for/list ([i (in-range n)])
      (let ([target-index (modulo (+ i (vector-ref v i)) n)])
        (vector-ref v target-index)))))
```

## Erlang

```erlang
-spec construct_transformed_array(Nums :: [integer()]) -> [integer()].
construct_transformed_array(Nums) ->
    N = length(Nums),
    IndexVals = lists:zip(lists:seq(0, N - 1), Nums),
    lists:map(
        fun({Idx, Val}) ->
            NewIdx0 = ((Idx + Val) rem N + N) rem N,
            lists:nth(NewIdx0 + 1, Nums)
        end,
        IndexVals
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_transformed_array(nums :: [integer]) :: [integer]
  def construct_transformed_array(nums) do
    n = length(nums)

    Enum.with_index(nums)
    |> Enum.map(fn {val, i} ->
      raw_idx = i + val
      idx = rem(raw_idx, n)
      idx = if idx < 0, do: idx + n, else: idx
      Enum.at(nums, idx)
    end)
  end
end
```
