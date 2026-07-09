# 2221. Find Triangular Sum of an Array

## Cpp

```cpp
class Solution {
public:
    int triangularSum(vector<int>& nums) {
        int n = nums.size();
        while (n > 1) {
            for (int i = 0; i < n - 1; ++i) {
                nums[i] = (nums[i] + nums[i + 1]) % 10;
            }
            --n;
        }
        return nums[0];
    }
};
```

## Java

```java
class Solution {
    public int triangularSum(int[] nums) {
        int n = nums.length;
        while (n > 1) {
            for (int i = 0; i < n - 1; i++) {
                nums[i] = (nums[i] + nums[i + 1]) % 10;
            }
            n--;
        }
        return nums[0];
    }
}
```

## Python

```python
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        while n > 1:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1
        return nums[0]
```

## Python3

```python
from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        return nums[0]
```

## C

```c
int triangularSum(int* nums, int numsSize) {
    int coeff[1001] = {0};
    coeff[0] = 1;
    for (int i = 1; i < numsSize; ++i) {
        for (int j = i; j >= 1; --j) {
            coeff[j] = (coeff[j] + coeff[j - 1]) % 10;
        }
    }
    int res = 0;
    for (int i = 0; i < numsSize; ++i) {
        res = (res + coeff[i] * nums[i]) % 10;
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int TriangularSum(int[] nums) {
        int n = nums.Length;
        int[] coeff = new int[n];
        coeff[0] = 1; // C(0,0)
        for (int i = 1; i < n; i++) {
            for (int j = i; j > 0; j--) {
                coeff[j] = (coeff[j] + coeff[j - 1]) % 10;
            }
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            result = (result + coeff[i] * nums[i]) % 10;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var triangularSum = function(nums) {
    while (nums.length > 1) {
        for (let i = 0; i < nums.length - 1; i++) {
            nums[i] = (nums[i] + nums[i + 1]) % 10;
        }
        nums.pop();
    }
    return nums[0];
};
```

## Typescript

```typescript
function triangularSum(nums: number[]): number {
    while (nums.length > 1) {
        const next = new Array(nums.length - 1);
        for (let i = 0; i < next.length; ++i) {
            next[i] = (nums[i] + nums[i + 1]) % 10;
        }
        nums = next;
    }
    return nums[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function triangularSum($nums) {
        $n = count($nums);
        while ($n > 1) {
            for ($i = 0; $i < $n - 1; $i++) {
                $nums[$i] = ($nums[$i] + $nums[$i + 1]) % 10;
            }
            $n--;
        }
        return $nums[0];
    }
}
```

## Swift

```swift
class Solution {
    func triangularSum(_ nums: [Int]) -> Int {
        var arr = nums
        var n = arr.count
        while n > 1 {
            for i in 0..<(n - 1) {
                arr[i] = (arr[i] + arr[i + 1]) % 10
            }
            n -= 1
        }
        return arr[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun triangularSum(nums: IntArray): Int {
        val arr = nums.clone()
        var size = arr.size
        while (size > 1) {
            for (i in 0 until size - 1) {
                arr[i] = (arr[i] + arr[i + 1]) % 10
            }
            size--
        }
        return arr[0]
    }
}
```

## Dart

```dart
class Solution {
  int triangularSum(List<int> nums) {
    List<int> cur = List.from(nums);
    while (cur.length > 1) {
      for (int i = 0; i < cur.length - 1; i++) {
        cur[i] = (cur[i] + cur[i + 1]) % 10;
      }
      cur.removeLast();
    }
    return cur[0];
  }
}
```

## Golang

```go
func triangularSum(nums []int) int {
    n := len(nums)
    for n > 1 {
        for i := 0; i < n-1; i++ {
            nums[i] = (nums[i] + nums[i+1]) % 10
        }
        n--
    }
    return nums[0]
}
```

## Ruby

```ruby
def triangular_sum(nums)
  while nums.length > 1
    (0...nums.length - 1).each do |i|
      nums[i] = (nums[i] + nums[i + 1]) % 10
    end
    nums.pop
  end
  nums[0]
end
```

## Scala

```scala
object Solution {
    def triangularSum(nums: Array[Int]): Int = {
        var arr = nums
        var n = arr.length
        while (n > 1) {
            val next = new Array[Int](n - 1)
            var i = 0
            while (i < n - 1) {
                next(i) = (arr(i) + arr(i + 1)) % 10
                i += 1
            }
            arr = next
            n -= 1
        }
        arr(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn triangular_sum(nums: Vec<i32>) -> i32 {
        let mut cur = nums;
        while cur.len() > 1 {
            let mut next = Vec::with_capacity(cur.len() - 1);
            for i in 0..cur.len() - 1 {
                next.push((cur[i] + cur[i + 1]) % 10);
            }
            cur = next;
        }
        cur[0]
    }
}
```

## Racket

```racket
(define/contract (triangular-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (letrec ((next-list
            (lambda (lst)
              (if (null? (cdr lst))
                  '()
                  (cons (modulo (+ (car lst) (cadr lst)) 10)
                        (next-list (cdr lst))))))
           (loop
            (lambda (arr)
              (if (= (length arr) 1)
                  (car arr)
                  (loop (next-list arr))))))
    (loop nums)))
```

## Erlang

```erlang
-spec triangular_sum(Nums :: [integer()]) -> integer().
triangular_sum(Nums) ->
    case Nums of
        [_] -> hd(Nums);
        _ -> triangular_sum(step(Nums))
    end.

step([]) -> [];
step([_]) -> [];
step([A, B | Rest]) ->
    [(A + B) rem 10 | step([B | Rest])].
```

## Elixir

```elixir
defmodule Solution do
  @spec triangular_sum(nums :: [integer]) :: integer
  def triangular_sum(nums) do
    n = length(nums)

    coeffs =
      Enum.reduce(1..(n - 1), [1], fn _, row ->
        middle =
          Enum.zip(row, tl(row))
          |> Enum.map(fn {a, b} -> rem(a + b, 10) end)

        [1] ++ middle ++ [1]
      end)

    Enum.zip(coeffs, nums)
    |> Enum.reduce(0, fn {c, v}, acc -> rem(acc + c * v, 10) end)
  end
end
```
