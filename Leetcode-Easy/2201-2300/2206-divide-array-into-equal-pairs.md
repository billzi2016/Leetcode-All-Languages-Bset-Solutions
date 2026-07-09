# 2206. Divide Array Into Equal Pairs

## Cpp

```cpp
class Solution {
public:
    bool divideArray(std::vector<int>& nums) {
        int cnt[501] = {0};
        for (int x : nums) {
            ++cnt[x];
        }
        for (int i = 1; i <= 500; ++i) {
            if (cnt[i] & 1) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean divideArray(int[] nums) {
        int[] count = new int[501];
        for (int num : nums) {
            count[num]++;
        }
        for (int c : count) {
            if ((c & 1) == 1) {
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
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for count in freq.values():
            if count % 2 != 0:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = [0] * 501
        for num in nums:
            freq[num] += 1
            if freq[num] % 2:  # odd count so far, continue
                continue
        # After counting, ensure all counts are even
        for count in freq:
            if count & 1:
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool divideArray(int* nums, int numsSize) {
    int freq[501] = {0};
    for (int i = 0; i < numsSize; ++i) {
        ++freq[nums[i]];
    }
    for (int v = 1; v <= 500; ++v) {
        if (freq[v] & 1) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool DivideArray(int[] nums) {
        int[] count = new int[501];
        foreach (int num in nums) {
            count[num]++;
        }
        foreach (int c in count) {
            if ((c & 1) == 1) return false;
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
var divideArray = function(nums) {
    const freq = new Array(501).fill(0);
    for (const num of nums) {
        freq[num]++;
    }
    for (let i = 1; i <= 500; i++) {
        if (freq[i] % 2 !== 0) return false;
    }
    return true;
};
```

## Typescript

```typescript
function divideArray(nums: number[]): boolean {
    const freq = new Array(501).fill(0);
    for (const num of nums) {
        freq[num]++;
    }
    for (let i = 1; i <= 500; i++) {
        if (freq[i] % 2 !== 0) return false;
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
    function divideArray($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (isset($freq[$num])) {
                $freq[$num]++;
            } else {
                $freq[$num] = 1;
            }
        }
        foreach ($freq as $count) {
            if ($count % 2 !== 0) {
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
    func divideArray(_ nums: [Int]) -> Bool {
        var unpaired = Set<Int>()
        for num in nums {
            if unpaired.contains(num) {
                unpaired.remove(num)
            } else {
                unpaired.insert(num)
            }
        }
        return unpaired.isEmpty
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun divideArray(nums: IntArray): Boolean {
        val freq = IntArray(501)
        for (num in nums) {
            freq[num]++
        }
        for (count in freq) {
            if (count % 2 != 0) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool divideArray(List<int> nums) {
    var freq = List.filled(501, 0);
    for (var v in nums) {
      freq[v]++;
    }
    for (var count in freq) {
      if (count % 2 != 0) return false;
    }
    return true;
  }
}
```

## Golang

```go
func divideArray(nums []int) bool {
    const maxVal = 500
    counts := make([]int, maxVal+1)
    for _, v := range nums {
        counts[v]++
    }
    for i := 0; i <= maxVal; i++ {
        if counts[i]%2 == 1 {
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
def divide_array(nums)
  counts = Array.new(501, 0)
  nums.each { |num| counts[num] += 1 }
  counts.all? { |c| c.even? }
end
```

## Scala

```scala
object Solution {
    def divideArray(nums: Array[Int]): Boolean = {
        val parity = new Array[Boolean](501)
        for (num <- nums) {
            parity(num) = !parity(num)
        }
        for (p <- parity) {
            if (p) return false
        }
        true
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut freq = [0usize; 501];
        for num in nums {
            freq[num as usize] += 1;
        }
        freq.iter().all(|&c| c % 2 == 0)
    }
}
```

## Racket

```racket
(define/contract (divide-array nums)
  (-> (listof exact-integer?) boolean?)
  (let ([freq (make-hash)])
    ;; count frequencies
    (for ([x nums])
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    ;; ensure each count is even
    (for/and ([cnt (in-hash-values freq)])
      (= (modulo cnt 2) 0))))
```

## Erlang

```erlang
-spec divide_array(Nums :: [integer()]) -> boolean().
divide_array(Nums) ->
    Unpaired = lists:foldl(
        fun(Num, Map) ->
            case maps:is_key(Num, Map) of
                true -> maps:remove(Num, Map);
                false -> maps:put(Num, true, Map)
            end
        end,
        #{},
        Nums),
    maps:size(Unpaired) =:= 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec divide_array(nums :: [integer]) :: boolean
  def divide_array(nums) do
    freq = Enum.reduce(nums, %{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)

    Enum.all?(freq, fn {_k, v} -> rem(v, 2) == 0 end)
  end
end
```
