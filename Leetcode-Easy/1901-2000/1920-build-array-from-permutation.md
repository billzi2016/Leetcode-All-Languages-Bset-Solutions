# 1920. Build Array from Permutation

## Cpp

```cpp
class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            ans[i] = nums[nums[i]];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] buildArray(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[nums[i]];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[nums[i]] for i in range(len(nums))]
```

## Python3

```python
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[nums[i]] for i in range(n)]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* ans = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        ans[i] = nums[nums[i]];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] BuildArray(int[] nums) {
        int n = nums.Length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[nums[i]];
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const newVal = nums[nums[i]] % n;
        nums[i] += newVal * n;
    }
    for (let i = 0; i < n; i++) {
        nums[i] = Math.floor(nums[i] / n);
    }
    return nums;
};
```

## Typescript

```typescript
function buildArray(nums: number[]): number[] {
    const n = nums.length;
    const ans = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        ans[i] = nums[nums[i]];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function buildArray($nums) {
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $ans[$i] = $nums[$nums[$i]];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func buildArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = [Int](repeating: 0, count: n)
        for i in 0..<n {
            ans[i] = nums[nums[i]]
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun buildArray(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(n)
        for (i in 0 until n) {
            ans[i] = nums[nums[i]]
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> buildArray(List<int> nums) {
    int n = nums.length;
    List<int> ans = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      ans[i] = nums[nums[i]];
    }
    return ans;
  }
}
```

## Golang

```go
func buildArray(nums []int) []int {
    n := len(nums)
    ans := make([]int, n)
    for i := 0; i < n; i++ {
        ans[i] = nums[nums[i]]
    }
    return ans
}
```

## Ruby

```ruby
def build_array(nums)
  n = nums.length
  ans = Array.new(n)
  i = 0
  while i < n
    ans[i] = nums[nums[i]]
    i += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def buildArray(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val ans = new Array[Int](n)
        var i = 0
        while (i < n) {
            ans(i) = nums(nums(i))
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = Vec::with_capacity(n);
        for &i in &nums {
            ans.push(nums[i as usize]);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (build-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (loop (add1 i)
                (cons (vector-ref v (vector-ref v i)) acc))))))
```

## Erlang

```erlang
-spec build_array(Nums :: [integer()]) -> [integer()].
build_array(Nums) ->
    Len = length(Nums),
    [lists:nth(lists:nth(I+1, Nums)+1, Nums) || I <- lists:seq(0, Len-1)].
```

## Elixir

```elixir
defmodule Solution do
  @spec build_array(nums :: [integer]) :: [integer]
  def build_array(nums) do
    len = length(nums)

    Enum.map(0..len - 1, fn i ->
      idx = Enum.at(nums, i)
      Enum.at(nums, idx)
    end)
  end
end
```
