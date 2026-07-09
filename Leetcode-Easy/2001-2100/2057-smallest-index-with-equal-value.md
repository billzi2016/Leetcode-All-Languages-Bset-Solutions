# 2057. Smallest Index With Equal Value

## Cpp

```cpp
class Solution {
public:
    int smallestEqual(vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (i % 10 == nums[i]) return i;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int smallestEqual(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (i % 10 == nums[i]) {
                return i;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, v in enumerate(nums):
            if i % 10 == v:
                return i
        return -1
```

## Python3

```python
class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i, v in enumerate(nums):
            if i % 10 == v:
                return i
        return -1
```

## C

```c
int smallestEqual(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        if (i % 10 == nums[i]) {
            return i;
        }
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestEqual(int[] nums) {
        for (int i = 0; i < nums.Length; i++) {
            if (i % 10 == nums[i]) return i;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var smallestEqual = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        if (i % 10 === nums[i]) return i;
    }
    return -1;
};
```

## Typescript

```typescript
function smallestEqual(nums: number[]): number {
    for (let i = 0; i < nums.length; i++) {
        if (i % 10 === nums[i]) {
            return i;
        }
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function smallestEqual($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 10 == $nums[$i]) {
                return $i;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func smallestEqual(_ nums: [Int]) -> Int {
        for (i, v) in nums.enumerated() {
            if i % 10 == v {
                return i
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestEqual(nums: IntArray): Int {
        for (i in nums.indices) {
            if (i % 10 == nums[i]) return i
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int smallestEqual(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      if (i % 10 == nums[i]) return i;
    }
    return -1;
  }
}
```

## Golang

```go
func smallestEqual(nums []int) int {
	for i, v := range nums {
		if i%10 == v {
			return i
		}
	}
	return -1
}
```

## Ruby

```ruby
def smallest_equal(nums)
  nums.each_with_index do |val, i|
    return i if i % 10 == val
  end
  -1
end
```

## Scala

```scala
object Solution {
    def smallestEqual(nums: Array[Int]): Int = {
        var i = 0
        while (i < nums.length) {
            if (i % 10 == nums(i)) return i
            i += 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_equal(nums: Vec<i32>) -> i32 {
        for (i, &v) in nums.iter().enumerate() {
            if (i as i32 % 10) == v {
                return i as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (smallest-equal nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((i 0) (lst nums))
    (cond
      [(null? lst) -1]
      [else (if (= (modulo i 10) (car lst))
                i
                (loop (+ i 1) (cdr lst)))])))
```

## Erlang

```erlang
-spec smallest_equal(Nums :: [integer()]) -> integer().
smallest_equal(Nums) ->
    smallest_equal(Nums, 0).

smallest_equal([], _Idx) ->
    -1;
smallest_equal([H|T], Idx) ->
    case (Idx rem 10) =:= H of
        true -> Idx;
        false -> smallest_equal(T, Idx + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_equal(nums :: [integer]) :: integer
  def smallest_equal(nums) do
    case Enum.find(Enum.with_index(nums), fn {val, i} -> rem(i, 10) == val end) do
      nil -> -1
      {_val, i} -> i
    end
  end
end
```
