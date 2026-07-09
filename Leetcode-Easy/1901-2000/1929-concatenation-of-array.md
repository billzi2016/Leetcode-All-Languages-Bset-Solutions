# 1929. Concatenation of Array

## Cpp

```cpp
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(2 * n);
        for (int i = 0; i < n; ++i) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums
```

## Python3

```python
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    *returnSize = 2 * numsSize;
    int* ans = (int*)malloc(sizeof(int) * (*returnSize));
    for (int i = 0; i < numsSize; ++i) {
        ans[i] = nums[i];
        ans[i + numsSize] = nums[i];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int n = nums.Length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
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
var getConcatenation = function(nums) {
    const n = nums.length;
    const ans = new Array(2 * n);
    for (let i = 0; i < n; i++) {
        ans[i] = nums[i];
        ans[i + n] = nums[i];
    }
    return ans;
};
```

## Typescript

```typescript
function getConcatenation(nums: number[]): number[] {
    const n = nums.length;
    const ans = new Array<number>(2 * n);
    for (let i = 0; i < n; ++i) {
        ans[i] = nums[i];
        ans[i + n] = nums[i];
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
    function getConcatenation($nums) {
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $ans[] = $nums[$i];
        }
        for ($i = 0; $i < $n; $i++) {
            $ans[] = $nums[$i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func getConcatenation(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = [Int]()
        ans.reserveCapacity(2 * n)
        ans.append(contentsOf: nums)
        ans.append(contentsOf: nums)
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getConcatenation(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(n * 2)
        for (i in 0 until n) {
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> getConcatenation(List<int> nums) {
    int n = nums.length;
    List<int> ans = List.filled(n * 2, 0);
    for (int i = 0; i < n; ++i) {
      ans[i] = nums[i];
      ans[i + n] = nums[i];
    }
    return ans;
  }
}
```

## Golang

```go
func getConcatenation(nums []int) []int {
    n := len(nums)
    ans := make([]int, 2*n)
    copy(ans[:n], nums)
    copy(ans[n:], nums)
    return ans
}
```

## Ruby

```ruby
def get_concatenation(nums)
  n = nums.length
  ans = Array.new(2 * n)
  i = 0
  while i < n
    val = nums[i]
    ans[i] = val
    ans[i + n] = val
    i += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def getConcatenation(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val ans = new Array[Int](2 * n)
        System.arraycopy(nums, 0, ans, 0, n)
        System.arraycopy(nums, 0, ans, n, n)
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = Vec::with_capacity(2 * n);
        ans.extend_from_slice(&nums);
        ans.extend_from_slice(&nums);
        ans
    }
}
```

## Racket

```racket
(define/contract (get-concatenation nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (append nums nums))
```

## Erlang

```erlang
-module(solution).
-export([get_concatenation/1]).

-spec get_concatenation(Nums :: [integer()]) -> [integer()].
get_concatenation(Nums) ->
    Nums ++ Nums.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_concatenation(nums :: [integer]) :: [integer]
  def get_concatenation(nums) do
    nums ++ nums
  end
end
```
