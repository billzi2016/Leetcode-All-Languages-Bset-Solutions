# 3065. Minimum Operations to Exceed Threshold Value I

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int cnt = 0;
        for (int x : nums) {
            if (x < k) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums, int k) {
        int ops = 0;
        for (int num : nums) {
            if (num < k) {
                ops++;
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for num in nums:
            if num < k:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 for x in nums if x < k)
```

## C

```c
int minOperations(int* nums, int numsSize, int k) {
    int ops = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] < k) {
            ++ops;
        }
    }
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums, int k) {
        int ops = 0;
        foreach (int num in nums) {
            if (num < k) ops++;
        }
        return ops;
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
var minOperations = function(nums, k) {
    let ops = 0;
    for (const num of nums) {
        if (num < k) ops++;
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(nums: number[], k: number): number {
    let ops = 0;
    for (const num of nums) {
        if (num < k) ops++;
    }
    return ops;
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
    function minOperations($nums, $k) {
        $cnt = 0;
        foreach ($nums as $v) {
            if ($v < $k) {
                $cnt++;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var count = 0
        for num in nums {
            if num < k {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        var count = 0
        for (num in nums) {
            if (num < k) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, int k) {
    int count = 0;
    for (int num in nums) {
      if (num < k) count++;
    }
    return count;
  }
}
```

## Golang

```go
func minOperations(nums []int, k int) int {
    cnt := 0
    for _, v := range nums {
        if v < k {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
def min_operations(nums, k)
  nums.count { |num| num < k }
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        var cnt = 0
        for (v <- nums) {
            if (v < k) cnt += 1
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        nums.iter().filter(|&&x| x < k).count() as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (length (filter (lambda (x) (< x k)) nums)))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/2]).

-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
    count_less_than(Nums, K, 0).

count_less_than([], _K, Acc) ->
    Acc;
count_less_than([H|T], K, Acc) when H < K ->
    count_less_than(T, K, Acc + 1);
count_less_than([_|T], K, Acc) ->
    count_less_than(T, K, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    Enum.count(nums, fn x -> x < k end)
  end
end
```
