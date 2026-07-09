# 3151. Special Array I

## Cpp

```cpp
class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        for (size_t i = 1; i < nums.size(); ++i) {
            if ((nums[i] & 1) == (nums[i - 1] & 1))
                return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isArraySpecial(int[] nums) {
        for (int i = 0; i + 1 < nums.length; i++) {
            if ((nums[i] & 1) == (nums[i + 1] & 1)) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            if (nums[i] & 1) == (nums[i + 1] & 1):
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] & 1) == (nums[i + 1] & 1):
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool isArraySpecial(int* nums, int numsSize) {
    for (int i = 0; i + 1 < numsSize; ++i) {
        if ((nums[i] & 1) == (nums[i + 1] & 1))
            return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsArraySpecial(int[] nums)
    {
        for (int i = 0; i + 1 < nums.Length; i++)
        {
            if ((nums[i] & 1) == (nums[i + 1] & 1))
                return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isArraySpecial = function(nums) {
    for (let i = 0; i < nums.length - 1; ++i) {
        if ((nums[i] & 1) === (nums[i + 1] & 1)) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isArraySpecial(nums: number[]): boolean {
    for (let i = 1; i < nums.length; i++) {
        if ((nums[i] & 1) === (nums[i - 1] & 1)) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isArraySpecial($nums) {
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ( ($nums[$i] & 1) === ($nums[$i - 1] & 1) ) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isArraySpecial(_ nums: [Int]) -> Bool {
        guard nums.count > 1 else { return true }
        for i in 1..<nums.count {
            if (nums[i] & 1) == (nums[i - 1] & 1) {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isArraySpecial(nums: IntArray): Boolean {
        for (i in 0 until nums.size - 1) {
            if ((nums[i] and 1) == (nums[i + 1] and 1)) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isArraySpecial(List<int> nums) {
    for (int i = 1; i < nums.length; i++) {
      if ((nums[i] & 1) == (nums[i - 1] & 1)) {
        return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func isArraySpecial(nums []int) bool {
    for i := 1; i < len(nums); i++ {
        if (nums[i]&1) == (nums[i-1]&1) {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def is_array_special(nums)
  (0...nums.length - 1).each do |i|
    return false if nums[i] % 2 == nums[i + 1] % 2
  end
  true
end
```

## Scala

```scala
object Solution {
    def isArraySpecial(nums: Array[Int]): Boolean = {
        for (i <- 0 until nums.length - 1) {
            if ((nums(i) & 1) == (nums(i + 1) & 1)) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_array_special(nums: Vec<i32>) -> bool {
        for i in 0..nums.len().saturating_sub(1) {
            if (nums[i] & 1) == (nums[i + 1] & 1) {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-array-special nums)
  (-> (listof exact-integer?) boolean?)
  (let loop ((prev #f) (lst nums))
    (cond
      [(null? lst) #t]
      [else
       (if prev
           (if (= (modulo (car lst) 2) (modulo prev 2))
               #f
               (loop (car lst) (cdr lst)))
           (loop (car lst) (cdr lst)))])))
```

## Erlang

```erlang
-spec is_array_special(Nums :: [integer()]) -> boolean().
is_array_special([]) -> true;
is_array_special([_]) -> true;
is_array_special([A,B|Rest]) ->
    (A rem 2 =/= B rem 2) andalso is_array_special([B|Rest]).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_array_special(nums :: [integer]) :: boolean
  def is_array_special([]), do: true
  def is_array_special([_]), do: true

  def is_array_special([a, b | rest]) do
    if rem(a, 2) != rem(b, 2) do
      is_array_special([b | rest])
    else
      false
    end
  end
end
```
