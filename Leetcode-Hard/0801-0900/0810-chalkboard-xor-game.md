# 0810. Chalkboard XOR Game

## Cpp

```cpp
class Solution {
public:
    bool xorGame(vector<int>& nums) {
        int x = 0;
        for (int v : nums) x ^= v;
        return x == 0 || nums.size() % 2 == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean xorGame(int[] nums) {
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }
        return xor == 0 || nums.length % 2 == 0;
    }
}
```

## Python

```python
class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = 0
        for num in nums:
            total ^= num
        return total == 0 or len(nums) % 2 == 0
```

## Python3

```python
class Solution:
    def xorGame(self, nums):
        total = 0
        for x in nums:
            total ^= x
        return total == 0 or len(nums) % 2 == 0
```

## C

```c
#include <stdbool.h>

bool xorGame(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total ^= nums[i];
    }
    return (total == 0) || (numsSize % 2 == 0);
}
```

## Csharp

```csharp
public class Solution
{
    public bool XorGame(int[] nums)
    {
        int xor = 0;
        foreach (int num in nums)
            xor ^= num;
        return xor == 0 || nums.Length % 2 == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var xorGame = function(nums) {
    let totalXor = 0;
    for (const num of nums) {
        totalXor ^= num;
    }
    return totalXor === 0 || nums.length % 2 === 0;
};
```

## Typescript

```typescript
function xorGame(nums: number[]): boolean {
    let xor = 0;
    for (const num of nums) {
        xor ^= num;
    }
    return xor === 0 || nums.length % 2 === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function xorGame($nums) {
        $xor = 0;
        foreach ($nums as $num) {
            $xor ^= $num;
        }
        return $xor === 0 || (count($nums) % 2 === 0);
    }
}
```

## Swift

```swift
class Solution {
    func xorGame(_ nums: [Int]) -> Bool {
        var totalXor = 0
        for num in nums {
            totalXor ^= num
        }
        return totalXor == 0 || nums.count % 2 == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun xorGame(nums: IntArray): Boolean {
        var totalXor = 0
        for (num in nums) {
            totalXor = totalXor xor num
        }
        return totalXor == 0 || nums.size % 2 == 0
    }
}
```

## Dart

```dart
class Solution {
  bool xorGame(List<int> nums) {
    int xor = 0;
    for (int num in nums) {
      xor ^= num;
    }
    if (xor == 0) return true;
    return nums.length % 2 == 0;
  }
}
```

## Golang

```go
func xorGame(nums []int) bool {
	xor := 0
	for _, v := range nums {
		xor ^= v
	}
	return xor == 0 || len(nums)%2 == 0
}
```

## Ruby

```ruby
def xor_game(nums)
  total = 0
  nums.each { |v| total ^= v }
  total == 0 || (nums.length & 1) == 0
end
```

## Scala

```scala
object Solution {
    def xorGame(nums: Array[Int]): Boolean = {
        val totalXor = nums.foldLeft(0)(_ ^ _)
        totalXor == 0 || (nums.length % 2 == 0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn xor_game(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut x = 0;
        for v in nums {
            x ^= v;
        }
        x == 0 || n % 2 == 0
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (xor-game nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([total (foldl bitwise-xor 0 nums)]
         [n (length nums)])
    (or (= total 0) (even? n))))
```

## Erlang

```erlang
-spec xor_game([integer()]) -> boolean().
xor_game(Nums) ->
    TotalXor = lists:foldl(fun(N, Acc) -> N bxor Acc end, 0, Nums),
    case {TotalXor, length(Nums)} of
        {0, _} -> true;
        {_, Len} when Len rem 2 == 0 -> true;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec xor_game(nums :: [integer]) :: boolean
  def xor_game(nums) do
    total_xor = Enum.reduce(nums, 0, &Bitwise.bxor/2)
    total_xor == 0 or rem(length(nums), 2) == 0
  end
end
```
