# 1313. Decompress Run-Length Encoded List

## Cpp

```cpp
class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        int n = nums.size();
        int total = 0;
        for (int i = 0; i < n; i += 2) {
            total += nums[i];
        }
        vector<int> result;
        result.reserve(total);
        for (int i = 0; i < n; i += 2) {
            int freq = nums[i];
            int val = nums[i + 1];
            for (int j = 0; j < freq; ++j) {
                result.push_back(val);
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] decompressRLElist(int[] nums) {
        int total = 0;
        for (int i = 0; i < nums.length; i += 2) {
            total += nums[i];
        }
        int[] result = new int[total];
        int idx = 0;
        for (int i = 0; i < nums.length; i += 2) {
            int freq = nums[i];
            int val = nums[i + 1];
            for (int j = 0; j < freq; ++j) {
                result[idx++] = val;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            res.extend([val] * freq)
        return res
```

## Python3

```python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            result.extend([val] * freq)
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decompressRLElist(int* nums, int numsSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i += 2) {
        total += nums[i];
    }
    *returnSize = total;
    int* result = (int*)malloc(total * sizeof(int));
    int idx = 0;
    for (int i = 0; i < numsSize; i += 2) {
        int freq = nums[i];
        int val = nums[i + 1];
        for (int j = 0; j < freq; ++j) {
            result[idx++] = val;
        }
    }
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] DecompressRLElist(int[] nums) {
        var result = new List<int>();
        for (int i = 0; i < nums.Length; i += 2) {
            int freq = nums[i];
            int val = nums[i + 1];
            for (int j = 0; j < freq; j++) {
                result.Add(val);
            }
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function(nums) {
    const res = [];
    for (let i = 0; i < nums.length; i += 2) {
        const freq = nums[i];
        const val = nums[i + 1];
        for (let j = 0; j < freq; ++j) {
            res.push(val);
        }
    }
    return res;
};
```

## Typescript

```typescript
function decompressRLElist(nums: number[]): number[] {
    const result: number[] = [];
    for (let i = 0; i < nums.length; i += 2) {
        const freq = nums[i];
        const val = nums[i + 1];
        for (let j = 0; j < freq; ++j) {
            result.push(val);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function decompressRLElist($nums) {
        $result = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i += 2) {
            $freq = $nums[$i];
            $val = $nums[$i + 1];
            for ($j = 0; $j < $freq; $j++) {
                $result[] = $val;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func decompressRLElist(_ nums: [Int]) -> [Int] {
        var result = [Int]()
        var i = 0
        while i < nums.count {
            let freq = nums[i]
            let val = nums[i + 1]
            if freq > 0 {
                result.append(contentsOf: Array(repeating: val, count: freq))
            }
            i += 2
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decompressRLElist(nums: IntArray): IntArray {
        var total = 0
        var i = 0
        while (i < nums.size) {
            total += nums[i]
            i += 2
        }
        val result = IntArray(total)
        var idx = 0
        i = 0
        while (i < nums.size) {
            val freq = nums[i]
            val value = nums[i + 1]
            repeat(freq) {
                result[idx++] = value
            }
            i += 2
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> decompressRLElist(List<int> nums) {
    List<int> result = [];
    for (int i = 0; i < nums.length; i += 2) {
      int freq = nums[i];
      int val = nums[i + 1];
      for (int j = 0; j < freq; ++j) {
        result.add(val);
      }
    }
    return result;
  }
}
```

## Golang

```go
func decompressRLElist(nums []int) []int {
    total := 0
    for i := 0; i < len(nums); i += 2 {
        total += nums[i]
    }
    result := make([]int, total)
    idx := 0
    for i := 0; i < len(nums); i += 2 {
        freq, val := nums[i], nums[i+1]
        for j := 0; j < freq; j++ {
            result[idx] = val
            idx++
        }
    }
    return result
}
```

## Ruby

```ruby
def decompress_rl_elist(nums)
  result = []
  i = 0
  while i < nums.length
    freq = nums[i]
    val = nums[i + 1]
    result.concat([val] * freq)
    i += 2
  end
  result
end
```

## Scala

```scala
object Solution {
    def decompressRLElist(nums: Array[Int]): Array[Int] = {
        val result = scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < nums.length) {
            val freq = nums(i)
            val value = nums(i + 1)
            var count = 0
            while (count < freq) {
                result += value
                count += 1
            }
            i += 2
        }
        result.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        // Calculate total size to reserve capacity
        let mut total = 0usize;
        for i in (0..nums.len()).step_by(2) {
            total += nums[i] as usize;
        }
        let mut result = Vec::with_capacity(total);
        let n = nums.len();
        let mut i = 0;
        while i < n {
            let freq = nums[i] as usize;
            let val = nums[i + 1];
            for _ in 0..freq {
                result.push(val);
            }
            i += 2;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (decompress-rl-elist nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let recur ((lst nums) (acc '()))
    (if (null? lst)
        (reverse acc)
        (let* ((freq (car lst))
               (val (cadr lst))
               (rest (cddr lst)))
          (define (add-times n v a)
            (if (= n 0) a
                (add-times (- n 1) v (cons v a))))
          (recur rest (add-times freq val acc))))))
```

## Erlang

```erlang
-spec decompress_rl_elist(Nums :: [integer()]) -> [integer()].
decompress_rl_elist([]) -> 
    [];
decompress_rl_elist([Freq, Val | Rest]) ->
    lists:duplicate(Freq, Val) ++ decompress_rl_elist(Rest).
```

## Elixir

```elixir
defmodule Solution do
  @spec decompress_rl_elist(nums :: [integer]) :: [integer]
  def decompress_rl_elist(nums) do
    nums
    |> Enum.chunk_every(2)
    |> Enum.flat_map(fn [freq, val] -> List.duplicate(val, freq) end)
  end
end
```
