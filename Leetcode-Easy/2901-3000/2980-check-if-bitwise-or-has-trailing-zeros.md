# 2980. Check if Bitwise OR Has Trailing Zeros

## Cpp

```cpp
class Solution {
public:
    bool hasTrailingZeros(vector<int>& nums) {
        int evenCount = 0;
        for (int x : nums) {
            if ((x & 1) == 0) {
                ++evenCount;
                if (evenCount >= 2) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean hasTrailingZeros(int[] nums) {
        int evenCount = 0;
        for (int num : nums) {
            if ((num & 1) == 0) {
                evenCount++;
                if (evenCount >= 2) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        even_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
                if even_count >= 2:
                    return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
                if even_count >= 2:
                    return True
        return False
```

## C

```c
#include <stdbool.h>

bool hasTrailingZeros(int* nums, int numsSize) {
    int evenCount = 0;
    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & 1) == 0) {
            ++evenCount;
            if (evenCount >= 2) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool HasTrailingZeros(int[] nums) {
        int evenCount = 0;
        foreach (int num in nums) {
            if ((num & 1) == 0) {
                evenCount++;
                if (evenCount >= 2) return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var hasTrailingZeros = function(nums) {
    let evenCount = 0;
    for (const num of nums) {
        if ((num & 1) === 0) {
            evenCount++;
            if (evenCount >= 2) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function hasTrailingZeros(nums: number[]): boolean {
    let evenCount = 0;
    for (const num of nums) {
        if ((num & 1) === 0) {
            evenCount++;
            if (evenCount >= 2) return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function hasTrailingZeros($nums) {
        $evenCount = 0;
        foreach ($nums as $num) {
            if (($num & 1) === 0) {
                $evenCount++;
                if ($evenCount >= 2) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func hasTrailingZeros(_ nums: [Int]) -> Bool {
        var evenCount = 0
        for num in nums {
            if (num & 1) == 0 {
                evenCount += 1
                if evenCount >= 2 {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasTrailingZeros(nums: IntArray): Boolean {
        var evenCount = 0
        for (num in nums) {
            if ((num and 1) == 0) {
                evenCount++
                if (evenCount >= 2) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool hasTrailingZeros(List<int> nums) {
    int evenCount = 0;
    for (int num in nums) {
      if ((num & 1) == 0) {
        evenCount++;
        if (evenCount >= 2) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func hasTrailingZeros(nums []int) bool {
    evenCount := 0
    for _, v := range nums {
        if v%2 == 0 {
            evenCount++
            if evenCount >= 2 {
                return true
            }
        }
    }
    return false
}
```

## Ruby

```ruby
def has_trailing_zeros(nums)
  nums.count(&:even?) >= 2
end
```

## Scala

```scala
object Solution {
    def hasTrailingZeros(nums: Array[Int]): Boolean = {
        var evenCount = 0
        for (num <- nums) {
            if ((num & 1) == 0) {
                evenCount += 1
                if (evenCount >= 2) return true
            }
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_trailing_zeros(nums: Vec<i32>) -> bool {
        let mut even_cnt = 0;
        for &num in nums.iter() {
            if num % 2 == 0 {
                even_cnt += 1;
                if even_cnt >= 2 {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (has-trailing-zeros nums)
  (-> (listof exact-integer?) boolean?)
  (>= (length (filter even? nums)) 2))
```

## Erlang

```erlang
-spec has_trailing_zeros(Nums :: [integer()]) -> boolean().
has_trailing_zeros(Nums) ->
    EvenCount = lists:foldl(
        fun(N, Acc) ->
            case N band 1 of
                0 -> Acc + 1;
                _ -> Acc
            end
        end,
        0,
        Nums),
    EvenCount >= 2.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_trailing_zeros(nums :: [integer]) :: boolean
  def has_trailing_zeros(nums) do
    Enum.count(nums, fn x -> rem(x, 2) == 0 end) >= 2
  end
end
```
