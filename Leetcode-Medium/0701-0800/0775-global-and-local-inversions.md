# 0775. Global and Local Inversions

## Cpp

```cpp
class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (abs(nums[i] - i) > 1) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isIdealPermutation(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (Math.abs(nums[i] - i) > 1) {
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
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_val = -1
        for i, x in enumerate(nums):
            if i >= 2:
                # update max of elements up to index i-2
                max_val = max(max_val, nums[i-2])
                if x < max_val:
                    return False
        return True
```

## Python3

```python
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i, v in enumerate(nums):
            if abs(v - i) > 1:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool isIdealPermutation(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        if (abs(nums[i] - i) > 1) {
            return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsIdealPermutation(int[] nums)
    {
        for (int i = 0; i < nums.Length; i++)
        {
            if (Math.Abs(nums[i] - i) > 1)
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
var isIdealPermutation = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        if (Math.abs(nums[i] - i) > 1) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isIdealPermutation(nums: number[]): boolean {
    for (let i = 0; i < nums.length; i++) {
        if (Math.abs(nums[i] - i) > 1) return false;
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
    function isIdealPermutation($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (abs($nums[$i] - $i) > 1) {
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
    func isIdealPermutation(_ nums: [Int]) -> Bool {
        for (i, v) in nums.enumerated() {
            if abs(v - i) > 1 {
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
    fun isIdealPermutation(nums: IntArray): Boolean {
        for (i in nums.indices) {
            if (kotlin.math.abs(nums[i] - i) > 1) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isIdealPermutation(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      if ((nums[i] - i).abs() > 1) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isIdealPermutation(nums []int) bool {
	for i, v := range nums {
		if abs(v-i) > 1 {
			return false
		}
	}
	return true
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def is_ideal_permutation(nums)
  nums.each_with_index do |v, i|
    return false if (v - i).abs > 1
  end
  true
end
```

## Scala

```scala
object Solution {
    def isIdealPermutation(nums: Array[Int]): Boolean = {
        var i = 0
        val n = nums.length
        while (i < n) {
            if (math.abs(nums(i) - i) > 1) return false
            i += 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_ideal_permutation(nums: Vec<i32>) -> bool {
        for (i, &v) in nums.iter().enumerate() {
            if (v - i as i32).abs() > 1 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-ideal-permutation nums)
  (-> (listof exact-integer?) boolean?)
  (let loop ((lst nums) (idx 0))
    (cond
      [(null? lst) #t]
      [else (if (> (abs (- (car lst) idx)) 1)
                #f
                (loop (cdr lst) (+ idx 1))))]))
```

## Erlang

```erlang
-module(solution).
-export([is_ideal_permutation/1]).

-spec is_ideal_permutation(Nums :: [integer()]) -> boolean().
is_ideal_permutation([]) -> true;
is_ideal_permutation([_]) -> true;
is_ideal_permutation([_, _]) -> true;
is_ideal_permutation([A0, A1 | Rest]) ->
    check(Rest, A0, A0, A1).

check([], _MaxPrev, _Prev2, _Prev1) -> true;
check([Curr|Tail], MaxPrev, _Prev2, Prev1) ->
    case MaxPrev > Curr of
        true -> false;
        false ->
            NewMaxPrev = erlang:max(MaxPrev, Prev1),
            check(Tail, NewMaxPrev, Prev1, Curr)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_ideal_permutation(nums :: [integer]) :: boolean
  def is_ideal_permutation(nums) do
    nums
    |> Enum.with_index()
    |> Enum.all?(fn {val, idx} -> abs(val - idx) <= 1 end)
  end
end
```
