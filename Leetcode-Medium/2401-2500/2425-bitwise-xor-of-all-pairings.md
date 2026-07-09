# 2425. Bitwise XOR of All Pairings

## Cpp

```cpp
class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        int ans = 0;
        if (m % 2 == 1) {
            for (int x : nums1) ans ^= x;
        }
        if (n % 2 == 1) {
            for (int y : nums2) ans ^= y;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        int result = 0;
        if ((len2 & 1) == 1) { // len2 is odd
            for (int num : nums1) {
                result ^= num;
            }
        }
        if ((len1 & 1) == 1) { // len1 is odd
            int xor2 = 0;
            for (int num : nums2) {
                xor2 ^= num;
            }
            result ^= xor2;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor1 = 0
        for x in nums1:
            xor1 ^= x
        xor2 = 0
        for y in nums2:
            xor2 ^= y

        ans = 0
        if len(nums2) % 2 == 1:
            ans ^= xor1
        if len(nums1) % 2 == 1:
            ans ^= xor2
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        res = 0
        if len2 % 2 == 1:
            for x in nums1:
                res ^= x
        if len1 % 2 == 1:
            for y in nums2:
                res ^= y
        return res
```

## C

```c
int xorAllNums(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int result = 0;
    if (nums2Size % 2 == 1) {
        for (int i = 0; i < nums1Size; ++i) {
            result ^= nums1[i];
        }
    }
    if (nums1Size % 2 == 1) {
        for (int i = 0; i < nums2Size; ++i) {
            result ^= nums2[i];
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int XorAllNums(int[] nums1, int[] nums2) {
        int len1 = nums1.Length;
        int len2 = nums2.Length;
        int result = 0;

        if ((len2 & 1) == 1) {
            foreach (int a in nums1) {
                result ^= a;
            }
        }

        if ((len1 & 1) == 1) {
            foreach (int b in nums2) {
                result ^= b;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var xorAllNums = function(nums1, nums2) {
    const n1 = nums1.length;
    const n2 = nums2.length;
    let result = 0;
    if (n2 % 2 === 1) {
        for (const v of nums1) {
            result ^= v;
        }
    }
    if (n1 % 2 === 1) {
        for (const v of nums2) {
            result ^= v;
        }
    }
    return result;
};
```

## Typescript

```typescript
function xorAllNums(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const m = nums2.length;
    let ans = 0;
    if (m % 2 === 1) {
        for (const v of nums1) {
            ans ^= v;
        }
    }
    if (n % 2 === 1) {
        for (const v of nums2) {
            ans ^= v;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function xorAllNums($nums1, $nums2) {
        $len1 = count($nums1);
        $len2 = count($nums2);
        $result = 0;
        if ($len2 % 2 === 1) {
            foreach ($nums1 as $v) {
                $result ^= $v;
            }
        }
        if ($len1 % 2 === 1) {
            foreach ($nums2 as $v) {
                $result ^= $v;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func xorAllNums(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var answer = 0
        let n1 = nums1.count
        let n2 = nums2.count
        
        if n2 % 2 == 1 {
            var xor1 = 0
            for v in nums1 {
                xor1 ^= v
            }
            answer ^= xor1
        }
        
        if n1 % 2 == 1 {
            var xor2 = 0
            for v in nums2 {
                xor2 ^= v
            }
            answer ^= xor2
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun xorAllNums(nums1: IntArray, nums2: IntArray): Int {
        var result = 0
        if (nums2.size % 2 == 1) {
            for (v in nums1) {
                result = result xor v
            }
        }
        if (nums1.size % 2 == 1) {
            for (v in nums2) {
                result = result xor v
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int xorAllNums(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    int m = nums2.length;
    int result = 0;
    if (m % 2 == 1) {
      for (int v in nums1) {
        result ^= v;
      }
    }
    if (n % 2 == 1) {
      for (int v in nums2) {
        result ^= v;
      }
    }
    return result;
  }
}
```

## Golang

```go
func xorAllNums(nums1 []int, nums2 []int) int {
    n1 := len(nums1)
    n2 := len(nums2)
    var ans int
    if n2%2 == 1 {
        for _, v := range nums1 {
            ans ^= v
        }
    }
    if n1%2 == 1 {
        for _, v := range nums2 {
            ans ^= v
        }
    }
    return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def xor_all_nums(nums1, nums2)
  result = 0
  if nums2.length.odd?
    nums1.each { |v| result ^= v }
  end
  if nums1.length.odd?
    nums2.each { |v| result ^= v }
  end
  result
end
```

## Scala

```scala
object Solution {
    def xorAllNums(nums1: Array[Int], nums2: Array[Int]): Int = {
        var result = 0

        if ((nums2.length & 1) == 1) {
            var xor1 = 0
            var i = 0
            while (i < nums1.length) {
                xor1 ^= nums1(i)
                i += 1
            }
            result ^= xor1
        }

        if ((nums1.length & 1) == 1) {
            var xor2 = 0
            var i = 0
            while (i < nums2.length) {
                xor2 ^= nums2(i)
                i += 1
            }
            result ^= xor2
        }

        result
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn xor_all_nums(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut ans = 0;
        if nums2.len() % 2 == 1 {
            for &v in &nums1 {
                ans ^= v;
            }
        }
        if nums1.len() % 2 == 1 {
            for &v in &nums2 {
                ans ^= v;
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket

(require racket/base)

(define/contract (xor-all-nums nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((len1 (length nums1))
         (len2 (length nums2))
         (xor1 (if (odd? len2) (foldl bitwise-xor 0 nums1) 0))
         (xor2 (if (odd? len1) (foldl bitwise-xor 0 nums2) 0)))
    (bitwise-xor xor1 xor2)))
```

## Erlang

```erlang
-module(solution).
-export([xor_all_nums/2]).

-spec xor_all_nums(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
xor_all_nums(Nums1, Nums2) ->
    Len1 = length(Nums1),
    Len2 = length(Nums2),

    Xor1 = case Len2 rem 2 of
        1 -> lists:foldl(fun (X, Acc) -> X bxor Acc end, 0, Nums1);
        _ -> 0
    end,

    Xor2 = case Len1 rem 2 of
        1 -> lists:foldl(fun (Y, Acc) -> Y bxor Acc end, 0, Nums2);
        _ -> 0
    end,

    Xor1 bxor Xor2.
```

## Elixir

```elixir
defmodule Solution do
  @spec xor_all_nums(nums1 :: [integer], nums2 :: [integer]) :: integer
  def xor_all_nums(nums1, nums2) do
    len1 = length(nums1)
    len2 = length(nums2)

    xor1 =
      if rem(len2, 2) == 1 do
        Enum.reduce(nums1, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
      else
        0
      end

    xor2 =
      if rem(len1, 2) == 1 do
        Enum.reduce(nums2, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
      else
        0
      end

    Bitwise.bxor(xor1, xor2)
  end
end
```
