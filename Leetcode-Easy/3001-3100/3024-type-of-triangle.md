# 3024. Type of Triangle

## Cpp

```cpp
class Solution {
public:
    string triangleType(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if (nums[0] + nums[1] <= nums[2]) return "none";
        if (nums[0] == nums[2]) return "equilateral";
        if (nums[0] == nums[1] || nums[1] == nums[2]) return "isosceles";
        return "scalene";
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public String triangleType(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        if (a[0] + a[1] <= a[2]) {
            return "none";
        }
        if (a[0] == a[2]) {
            return "equilateral";
        }
        if (a[0] == a[1] || a[1] == a[2]) {
            return "isosceles";
        }
        return "scalene";
    }
}
```

## Python

```python
class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        if a == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"
```

## Python3

```python
from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        if a == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"
```

## C

```c
char* triangleType(int* nums, int numsSize) {
    int a = nums[0], b = nums[1], c = nums[2];
    // sort a <= b <= c
    if (a > b) { int t = a; a = b; b = t; }
    if (b > c) { int t = b; b = c; c = t; }
    if (a > b) { int t = a; a = b; b = t; }
    
    if (a + b <= c) return "none";
    if (a == c) return "equilateral";
    if (a == b || b == c) return "isosceles";
    return "scalene";
}
```

## Csharp

```csharp
public class Solution {
    public string TriangleType(int[] nums) {
        // Sort the three sides
        System.Array.Sort(nums);
        
        // Check triangle inequality
        if (nums[0] + nums[1] <= nums[2]) {
            return "none";
        }
        
        // All sides equal -> equilateral
        if (nums[0] == nums[2]) {
            return "equilateral";
        }
        
        // Two sides equal -> isosceles
        if (nums[0] == nums[1] || nums[1] == nums[2]) {
            return "isosceles";
        }
        
        // All sides different -> scalene
        return "scalene";
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {string}
 */
var triangleType = function(nums) {
    // Sort the sides in non-decreasing order
    nums.sort((a, b) => a - b);
    const [a, b, c] = nums;
    
    // Check triangle inequality
    if (a + b <= c) return "none";
    
    // Determine type based on side equality
    if (a === c) return "equilateral";
    if (a === b || b === c) return "isosceles";
    return "scalene";
};
```

## Typescript

```typescript
function triangleType(nums: number[]): string {
    const sides = [...nums].sort((a, b) => a - b);
    if (sides[0] + sides[1] <= sides[2]) return "none";
    if (sides[0] === sides[2]) return "equilateral";
    if (sides[0] === sides[1] || sides[1] === sides[2]) return "isosceles";
    return "scalene";
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return String
     */
    function triangleType($nums) {
        sort($nums);
        if ($nums[0] + $nums[1] <= $nums[2]) {
            return "none";
        }
        if ($nums[0] == $nums[2]) {
            return "equilateral";
        }
        if ($nums[0] == $nums[1] || $nums[1] == $nums[2]) {
            return "isosceles";
        }
        return "scalene";
    }
}
```

## Swift

```swift
class Solution {
    func triangleType(_ nums: [Int]) -> String {
        let sides = nums.sorted()
        if sides[0] + sides[1] <= sides[2] {
            return "none"
        }
        if sides[0] == sides[2] {
            return "equilateral"
        }
        if sides[0] == sides[1] || sides[1] == sides[2] {
            return "isosceles"
        }
        return "scalene"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun triangleType(nums: IntArray): String {
        val sides = nums.clone()
        sides.sort()
        if (sides[0] + sides[1] <= sides[2]) return "none"
        return when {
            sides[0] == sides[2] -> "equilateral"
            sides[0] == sides[1] || sides[1] == sides[2] -> "isosceles"
            else -> "scalene"
        }
    }
}
```

## Dart

```dart
class Solution {
  String triangleType(List<int> nums) {
    List<int> sides = List.from(nums);
    sides.sort();
    if (sides[0] + sides[1] <= sides[2]) {
      return "none";
    }
    if (sides[0] == sides[2]) {
      return "equilateral";
    }
    if (sides[0] == sides[1] || sides[1] == sides[2]) {
      return "isosceles";
    }
    return "scalene";
  }
}
```

## Golang

```go
import "sort"

func triangleType(nums []int) string {
	sort.Ints(nums)
	if nums[0]+nums[1] <= nums[2] {
		return "none"
	}
	if nums[0] == nums[2] {
		return "equilateral"
	}
	if nums[0] == nums[1] || nums[1] == nums[2] {
		return "isosceles"
	}
	return "scalene"
}
```

## Ruby

```ruby
def triangle_type(nums)
  a, b, c = nums.sort
  return "none" if a + b <= c
  return "equilateral" if a == c
  return "isosceles" if a == b || b == c
  "scalene"
end
```

## Scala

```scala
object Solution {
    def triangleType(nums: Array[Int]): String = {
        val a = nums.sorted
        if (a(0) + a(1) <= a(2)) "none"
        else if (a(0) == a(2)) "equilateral"
        else if (a(0) == a(1) || a(1) == a(2)) "isosceles"
        else "scalene"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn triangle_type(nums: Vec<i32>) -> String {
        let mut v = nums;
        v.sort();
        if v[0] + v[1] <= v[2] {
            "none".to_string()
        } else if v[0] == v[2] {
            "equilateral".to_string()
        } else if v[0] == v[1] || v[1] == v[2] {
            "isosceles".to_string()
        } else {
            "scalene".to_string()
        }
    }
}
```

## Racket

```racket
(define/contract (triangle-type nums)
  (-> (listof exact-integer?) string?)
  (let* ([sorted (sort nums <)]
         [a (first sorted)]
         [b (second sorted)]
         [c (third sorted)])
    (cond
      [(<= (+ a b) c) "none"]
      [(= a c) "equilateral"]
      [(or (= a b) (= b c)) "isosceles"]
      [else "scalene"])))
```

## Erlang

```erlang
-module(solution).
-export([triangle_type/1]).

-spec triangle_type(Nums :: [integer()]) -> unicode:unicode_binary().
triangle_type(Nums) ->
    Sorted = lists:sort(Nums),
    [A, B, C] = Sorted,
    case A + B =< C of
        true -> <<"none">>;
        false ->
            if
                A == C -> <<"equilateral">>;
                A == B -> <<"isosceles">>;
                B == C -> <<"isosceles">>;
                true   -> <<"scalene">>
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec triangle_type(nums :: [integer]) :: String.t()
  def triangle_type(nums) do
    [a, b, c] = Enum.sort(nums)

    cond do
      a + b <= c ->
        "none"

      a == c ->
        "equilateral"

      a == b or b == c ->
        "isosceles"

      true ->
        "scalene"
    end
  end
end
```
