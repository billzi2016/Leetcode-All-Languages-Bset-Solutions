# 0260. Single Number III

## Cpp

```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xorAll = 0;
        for (int num : nums) {
            xorAll ^= num;
        }
        int diffBit = xorAll & -xorAll; // isolate rightmost set bit
        int a = 0, b = 0;
        for (int num : nums) {
            if (num & diffBit)
                a ^= num;
            else
                b ^= num;
        }
        return {a, b};
    }
};
```

## Java

```java
class Solution {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }
        int diffBit = xor & -xor;
        int a = 0, b = 0;
        for (int num : nums) {
            if ((num & diffBit) == 0) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        return new int[]{a, b};
    }
}
```

## Python

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # XOR of all numbers gives a ^ b where a and b are the unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Get rightmost set bit (differs between a and b)
        diff_bit = xor_all & -xor_all

        # Separate numbers into two groups based on diff_bit and XOR each group
        a = 0
        b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
```

## Python3

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        diff = xor & -xor
        a = 0
        b = 0
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n
        return [a, b]
```

## C

```c
#include <stdlib.h>

int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int xorAll = 0;
    for (int i = 0; i < numsSize; ++i)
        xorAll ^= nums[i];
    
    int diff = xorAll & (-xorAll);
    int a = 0, b = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] & diff)
            a ^= nums[i];
        else
            b ^= nums[i];
    }
    
    int* res = (int*)malloc(2 * sizeof(int));
    res[0] = a;
    res[1] = b;
    *returnSize = 2;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SingleNumber(int[] nums) {
        int xor = 0;
        foreach (int num in nums) {
            xor ^= num;
        }
        // Get rightmost set bit
        int diffBit = xor & -xor;
        int a = 0, b = 0;
        foreach (int num in nums) {
            if ((num & diffBit) == 0)
                a ^= num;
            else
                b ^= num;
        }
        return new int[] { a, b };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    let xor = 0;
    for (const n of nums) xor ^= n;
    
    // isolate rightmost set bit where the two unique numbers differ
    const diffBit = xor & -xor;
    
    let a = 0, b = 0;
    for (const n of nums) {
        if ((n & diffBit) !== 0) {
            a ^= n;
        } else {
            b ^= n;
        }
    }
    return [a, b];
};
```

## Typescript

```typescript
function singleNumber(nums: number[]): number[] {
    let xor = 0;
    for (const n of nums) {
        xor ^= n;
    }
    const diffBit = xor & -xor;
    let a = 0, b = 0;
    for (const n of nums) {
        if ((n & diffBit) !== 0) {
            a ^= n;
        } else {
            b ^= n;
        }
    }
    return [a, b];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function singleNumber($nums) {
        $xor = 0;
        foreach ($nums as $n) {
            $xor ^= $n;
        }
        // isolate rightmost set bit
        $diff = $xor & (-$xor);
        $a = 0;
        $b = 0;
        foreach ($nums as $n) {
            if (($n & $diff) != 0) {
                $a ^= $n;
            } else {
                $b ^= $n;
            }
        }
        return [$a, $b];
    }
}
```

## Swift

```swift
class Solution {
    func singleNumber(_ nums: [Int]) -> [Int] {
        var xorAll = 0
        for num in nums {
            xorAll ^= num
        }
        let diffBit = xorAll & -xorAll
        var a = 0, b = 0
        for num in nums {
            if (num & diffBit) != 0 {
                a ^= num
            } else {
                b ^= num
            }
        }
        return [a, b]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun singleNumber(nums: IntArray): IntArray {
        var xorAll = 0
        for (num in nums) {
            xorAll = xorAll xor num
        }
        val diffBit = xorAll and -xorAll
        var a = 0
        var b = 0
        for (num in nums) {
            if ((num and diffBit) != 0) {
                a = a xor num
            } else {
                b = b xor num
            }
        }
        return intArrayOf(a, b)
    }
}
```

## Dart

```dart
class Solution {
  List<int> singleNumber(List<int> nums) {
    int xor = 0;
    for (int num in nums) {
      xor ^= num;
    }
    int diff = xor & -xor; // rightmost set bit
    int a = 0, b = 0;
    for (int num in nums) {
      if ((num & diff) != 0) {
        a ^= num;
      } else {
        b ^= num;
      }
    }
    return [a, b];
  }
}
```

## Golang

```go
func singleNumber(nums []int) []int {
	xorAll := 0
	for _, v := range nums {
		xorAll ^= v
	}
	diffBit := xorAll & -xorAll
	a, b := 0, 0
	for _, v := range nums {
		if v&diffBit == 0 {
			a ^= v
		} else {
			b ^= v
		}
	}
	return []int{a, b}
}
```

## Ruby

```ruby
def single_number(nums)
  xor = 0
  nums.each { |num| xor ^= num }
  diff = xor & -xor
  a = 0
  b = 0
  nums.each do |num|
    if (num & diff).zero?
      a ^= num
    else
      b ^= num
    end
  end
  [a, b]
end
```

## Scala

```scala
object Solution {
    def singleNumber(nums: Array[Int]): Array[Int] = {
        var xorAll = 0
        for (num <- nums) xorAll ^= num

        // Get rightmost set bit
        val diffBit = xorAll & -xorAll

        var a = 0
        var b = 0
        for (num <- nums) {
            if ((num & diffBit) != 0) a ^= num else b ^= num
        }
        Array(a, b)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let mut xor_all = 0;
        for &num in nums.iter() {
            xor_all ^= num;
        }
        // Isolate rightmost set bit where the two unique numbers differ
        let diff_bit = xor_all & -xor_all;
        let (mut a, mut b) = (0, 0);
        for &num in nums.iter() {
            if num & diff_bit != 0 {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        vec![a, b]
    }
}
```

## Racket

```racket
(define/contract (single-number nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((xor-all (foldl bitwise-xor 0 nums))
         (diff-bit (bitwise-and xor-all (negative xor-all))))
    (let loop ((lst nums) (x 0) (y 0))
      (if (null? lst)
          (list x y)
          (let* ((num (car lst))
                 (has-bit (bitwise-and num diff-bit)))
            (if (= has-bit 0)
                (loop (cdr lst) (bitwise-xor x num) y)
                (loop (cdr lst) x (bitwise-xor y num))))))))
```

## Erlang

```erlang
-module(solution).
-export([single_number/1]).

-spec single_number(Nums :: [integer()]) -> [integer()].
single_number(Nums) ->
    XorAll = lists:foldl(fun(N, Acc) -> N bxor Acc end, 0, Nums),
    DiffBit = XorAll band (-XorAll),
    A = lists:foldl(
            fun(N, Acc) ->
                case (N band DiffBit) of
                    0 -> Acc;
                    _ -> N bxor Acc
                end
            end,
            0,
            Nums),
    B = XorAll bxor A,
    [A, B].
```

## Elixir

```elixir
defmodule Solution do
  @spec single_number(nums :: [integer]) :: [integer]
  def single_number(nums) do
    import Bitwise

    xor_all = Enum.reduce(nums, 0, fn x, acc -> bxor(acc, x) end)
    diff_bit = xor_all &&& (-xor_all)

    {a, b} =
      Enum.reduce(nums, {0, 0}, fn x, {a_acc, b_acc} ->
        if (x &&& diff_bit) != 0 do
          {bxor(a_acc, x), b_acc}
        else
          {a_acc, bxor(b_acc, x)}
        end
      end)

    [a, b]
  end
end
```
