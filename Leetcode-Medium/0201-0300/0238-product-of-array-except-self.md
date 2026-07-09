# 0238. Product of Array Except Self

## Cpp

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n);
        int left = 1;
        for (int i = 0; i < n; ++i) {
            answer[i] = left;
            left *= nums[i];
        }
        int right = 1;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] *= right;
            right *= nums[i];
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        int leftProduct = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = leftProduct;
            leftProduct *= nums[i];
        }
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= rightProduct;
            rightProduct *= nums[i];
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer
```

## Python3

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* answer = (int*)malloc(numsSize * sizeof(int));
    if (!answer) return NULL;

    int left = 1;
    for (int i = 0; i < numsSize; ++i) {
        answer[i] = left;
        left *= nums[i];
    }

    int right = 1;
    for (int i = numsSize - 1; i >= 0; --i) {
        answer[i] *= right;
        right *= nums[i];
    }

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] answer = new int[n];
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= rightProduct;
            rightProduct *= nums[i];
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
    const answer = new Array(n);
    let left = 1;
    for (let i = 0; i < n; i++) {
        answer[i] = left;
        left *= nums[i];
    }
    let right = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= right;
        right *= nums[i];
    }
    return answer;
};
```

## Typescript

```typescript
function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const answer = new Array<number>(n);
    let left = 1;
    for (let i = 0; i < n; i++) {
        answer[i] = left;
        left *= nums[i];
    }
    let right = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= right;
        right *= nums[i];
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function productExceptSelf($nums) {
        $n = count($nums);
        $answer = array_fill(0, $n, 1);

        // Compute prefix products
        $left = 1;
        for ($i = 0; $i < $n; $i++) {
            $answer[$i] = $left;
            $left *= $nums[$i];
        }

        // Compute suffix products and combine
        $right = 1;
        for ($i = $n - 1; $i >= 0; $i--) {
            $answer[$i] *= $right;
            $right *= $nums[$i];
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var answer = Array(repeating: 1, count: n)
        var left = 1
        for i in 0..<n {
            answer[i] = left
            left *= nums[i]
        }
        var right = 1
        for i in stride(from: n - 1, through: 0, by: -1) {
            answer[i] *= right
            right *= nums[i]
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val n = nums.size
        val answer = IntArray(n)
        var left = 1
        for (i in 0 until n) {
            answer[i] = left
            left *= nums[i]
        }
        var right = 1
        for (i in n - 1 downTo 0) {
            answer[i] = answer[i] * right
            right *= nums[i]
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> productExceptSelf(List<int> nums) {
    int n = nums.length;
    List<int> answer = List.filled(n, 1);
    int left = 1;
    for (int i = 0; i < n; i++) {
      answer[i] = left;
      left *= nums[i];
    }
    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
      answer[i] *= right;
      right *= nums[i];
    }
    return answer;
  }
}
```

## Golang

```go
func productExceptSelf(nums []int) []int {
	n := len(nums)
	res := make([]int, n)

	// Compute prefix products.
	prefix := 1
	for i := 0; i < n; i++ {
		res[i] = prefix
		prefix *= nums[i]
	}

	// Compute suffix products and combine.
	suffix := 1
	for i := n - 1; i >= 0; i-- {
		res[i] *= suffix
		suffix *= nums[i]
	}
	return res
}
```

## Ruby

```ruby
def product_except_self(nums)
  n = nums.length
  answer = Array.new(n, 1)

  left = 1
  i = 0
  while i < n
    answer[i] = left
    left *= nums[i]
    i += 1
  end

  right = 1
  i = n - 1
  while i >= 0
    answer[i] *= right
    right *= nums[i]
    i -= 1
  end

  answer
end
```

## Scala

```scala
object Solution {
    def productExceptSelf(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val answer = new Array[Int](n)
        var left = 1
        var i = 0
        while (i < n) {
            answer(i) = left
            left *= nums(i)
            i += 1
        }
        var right = 1
        i = n - 1
        while (i >= 0) {
            answer(i) *= right
            right *= nums(i)
            i -= 1
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut answer = vec![1i32; n];
        let mut left: i64 = 1;
        for i in 0..n {
            answer[i] = left as i32;
            left *= nums[i] as i64;
        }
        let mut right: i64 = 1;
        for i in (0..n).rev() {
            answer[i] = ((answer[i] as i64) * right) as i32;
            right *= nums[i] as i64;
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (product-except-self nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (res (make-vector n)))
    ;; first pass: store prefix products
    (let loop ((i 0) (prefix 1))
      (when (< i n)
        (vector-set! res i prefix)
        (loop (+ i 1) (* prefix (vector-ref v i)))))
    ;; second pass: multiply by suffix products
    (let loop ((i (- n 1)) (suffix 1))
      (when (>= i 0)
        (let ((val (vector-ref res i)))
          (vector-set! res i (* val suffix)))
        (loop (- i 1) (* suffix (vector-ref v i)))))
    (vector->list res)))
```

## Erlang

```erlang
-spec product_except_self(Nums :: [integer()]) -> [integer()].
product_except_self(Nums) ->
    Prefix = prefix_products(Nums, 1, []),
    RevNums = lists:reverse(Nums),
    RevPrefix = lists:reverse(Prefix),
    {ResultRev, _} = suffix_pass(RevNums, RevPrefix, 1, []),
    lists:reverse(ResultRev).

prefix_products([], _Acc, Res) ->
    lists:reverse(Res);
prefix_products([H|T], Acc, Res) ->
    prefix_products(T, Acc * H, [Acc | Res]).

suffix_pass([], [], _SuffixAcc, Res) ->
    {Res, ok};
suffix_pass([H|T], [P|PT], SuffixAcc, Res) ->
    ResultVal = P * SuffixAcc,
    NewSuffixAcc = SuffixAcc * H,
    suffix_pass(T, PT, NewSuffixAcc, [ResultVal | Res]).
```

## Elixir

```elixir
defmodule Solution do
  @spec product_except_self(nums :: [integer]) :: [integer]
  def product_except_self(nums) do
    {prefix_rev, _} = Enum.reduce(nums, {[], 1}, fn x, {acc, prod} ->
      {[prod | acc], prod * x}
    end)

    rev_nums = Enum.reverse(nums)

    {result, _} =
      Enum.reduce(Enum.zip(rev_nums, prefix_rev), {[], 1}, fn {x, pref}, {acc, suffix} ->
        val = pref * suffix
        {[val | acc], suffix * x}
      end)

    result
  end
end
```
