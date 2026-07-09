# 1470. Shuffle the Array

## Cpp

```cpp
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> result;
        result.reserve(2 * n);
        for (int i = 0; i < n; ++i) {
            result.push_back(nums[i]);
            result.push_back(nums[n + i]);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[2 * n];
        for (int i = 0; i < n; i++) {
            result[2 * i] = nums[i];
            result[2 * i + 1] = nums[i + n];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res
```

## Python3

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int *res = (int*)malloc(numsSize * sizeof(int));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    for (int i = 0; i < n; ++i) {
        res[2*i] = nums[i];
        res[2*i + 1] = nums[i + n];
    }
    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        int[] result = new int[2 * n];
        for (int i = 0; i < n; i++) {
            result[2 * i] = nums[i];
            result[2 * i + 1] = nums[n + i];
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    const res = new Array(2 * n);
    for (let i = 0; i < n; ++i) {
        res[2 * i] = nums[i];
        res[2 * i + 1] = nums[i + n];
    }
    return res;
};
```

## Typescript

```typescript
function shuffle(nums: number[], n: number): number[] {
    const result: number[] = new Array(2 * n);
    for (let i = 0; i < n; i++) {
        result[2 * i] = nums[i];
        result[2 * i + 1] = nums[n + i];
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer[]
     */
    function shuffle($nums, $n) {
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            $result[] = $nums[$i];
            $result[] = $nums[$i + $n];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func shuffle(_ nums: [Int], _ n: Int) -> [Int] {
        var result = [Int]()
        result.reserveCapacity(nums.count)
        for i in 0..<n {
            result.append(nums[i])
            result.append(nums[i + n])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shuffle(nums: IntArray, n: Int): IntArray {
        val result = IntArray(2 * n)
        for (i in 0 until n) {
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[n + i]
        }
        return result
    }
}
```

## Golang

```go
func shuffle(nums []int, n int) []int {
    result := make([]int, 0, 2*n)
    for i := 0; i < n; i++ {
        result = append(result, nums[i], nums[i+n])
    }
    return result
}
```

## Ruby

```ruby
def shuffle(nums, n)
  result = []
  i = 0
  while i < n
    result << nums[i]
    result << nums[i + n]
    i += 1
  end
  result
end
```

## Scala

```scala
object Solution {
    def shuffle(nums: Array[Int], n: Int): Array[Int] = {
        val res = new Array[Int](2 * n)
        var i = 0
        while (i < n) {
            res(2 * i) = nums(i)
            res(2 * i + 1) = nums(i + n)
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut result = Vec::with_capacity(2 * n);
        for i in 0..n {
            result.push(nums[i]);
            result.push(nums[n + i]);
        }
        result
    }
}
```
