# 1673. Find the Most Competitive Subsequence

## Cpp

```cpp
class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> st;
        st.reserve(k);
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && st.back() > nums[i] && (int)st.size() - 1 + (n - i) >= k) {
                st.pop_back();
            }
            if ((int)st.size() < k) {
                st.push_back(nums[i]);
            }
        }
        return st;
    }
};
```

## Java

```java
class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        int n = nums.length;
        int[] stack = new int[k];
        int top = 0; // current size of the stack
        
        for (int i = 0; i < n; i++) {
            // While we can remove a larger element to make the sequence smaller
            while (top > 0 && stack[top - 1] > nums[i] && (top - 1 + (n - i) >= k)) {
                top--;
            }
            // If we still need more elements, push current number
            if (top < k) {
                stack[top++] = nums[i];
            }
        }
        return stack;
    }
}
```

## Python

```python
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            # while we can remove previous larger element to make room for smaller one
            while stack and num < stack[-1] and len(stack) - 1 + (n - i) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
```

## Python3

```python
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            # while we can pop to make a smaller number and still have enough elements left
            while stack and num < stack[-1] and len(stack) - 1 + (n - i) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* mostCompetitive(int* nums, int numsSize, int k, int* returnSize) {
    int *stack = (int*)malloc(sizeof(int) * numsSize);
    int top = 0;
    for (int i = 0; i < numsSize; ++i) {
        while (top > 0 && stack[top - 1] > nums[i] &&
               (top - 1 + (numsSize - i) >= k)) {
            --top;
        }
        if (top < k) {
            stack[top++] = nums[i];
        }
    }
    *returnSize = k;
    int* result = (int*)malloc(sizeof(int) * k);
    memcpy(result, stack, sizeof(int) * k);
    free(stack);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] MostCompetitive(int[] nums, int k)
    {
        int n = nums.Length;
        int[] stack = new int[n];
        int top = 0;

        for (int i = 0; i < n; i++)
        {
            while (top > 0 && stack[top - 1] > nums[i] && (top - 1 + (n - i) >= k))
            {
                top--;
            }

            if (top < k)
            {
                stack[top++] = nums[i];
            }
        }

        int[] result = new int[k];
        System.Array.Copy(stack, result, k);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var mostCompetitive = function(nums, k) {
    const n = nums.length;
    const stack = [];
    for (let i = 0; i < n; i++) {
        const num = nums[i];
        while (
            stack.length &&
            stack[stack.length - 1] > num &&
            stack.length - 1 + (n - i) >= k
        ) {
            stack.pop();
        }
        if (stack.length < k) {
            stack.push(num);
        }
    }
    return stack;
};
```

## Typescript

```typescript
function mostCompetitive(nums: number[], k: number): number[] {
    const stack: number[] = [];
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        const num = nums[i];
        while (
            stack.length > 0 &&
            stack[stack.length - 1] > num &&
            stack.length - 1 + (n - i) >= k
        ) {
            stack.pop();
        }
        if (stack.length < k) {
            stack.push(num);
        }
    }
    return stack;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function mostCompetitive($nums, $k) {
        $n = count($nums);
        $stack = [];
        foreach ($nums as $i => $num) {
            while (!empty($stack) && end($stack) > $num && (count($stack) - 1 + ($n - $i) >= $k)) {
                array_pop($stack);
            }
            if (count($stack) < $k) {
                $stack[] = $num;
            }
        }
        return $stack;
    }
}
```

## Swift

```swift
class Solution {
    func mostCompetitive(_ nums: [Int], _ k: Int) -> [Int] {
        var stack = [Int]()
        let n = nums.count
        for i in 0..<n {
            let num = nums[i]
            while !stack.isEmpty && stack.last! > num && (stack.count - 1 + (n - i)) >= k {
                stack.removeLast()
            }
            if stack.count < k {
                stack.append(num)
            }
        }
        return stack
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostCompetitive(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        val stack = IntArray(k)
        var top = 0
        for (i in 0 until n) {
            val cur = nums[i]
            while (top > 0 && stack[top - 1] > cur && top - 1 + (n - i) >= k) {
                top--
            }
            if (top < k) {
                stack[top++] = cur
            }
        }
        return stack
    }
}
```

## Dart

```dart
class Solution {
  List<int> mostCompetitive(List<int> nums, int k) {
    int n = nums.length;
    List<int> stack = [];
    for (int i = 0; i < n; i++) {
      int num = nums[i];
      while (stack.isNotEmpty &&
          stack.last > num &&
          stack.length - 1 + (n - i) >= k) {
        stack.removeLast();
      }
      if (stack.length < k) {
        stack.add(num);
      }
    }
    return stack;
  }
}
```

## Golang

```go
func mostCompetitive(nums []int, k int) []int {
	n := len(nums)
	stack := make([]int, 0, k)

	for i, num := range nums {
		// While we can remove the last element to get a smaller lexicographic order
		for len(stack) > 0 && stack[len(stack)-1] > num && len(stack)-1+(n-i) >= k {
			stack = stack[:len(stack)-1]
		}
		if len(stack) < k {
			stack = append(stack, num)
		}
	}
	return stack
}
```

## Ruby

```ruby
def most_competitive(nums, k)
  n = nums.length
  stack = []
  nums.each_with_index do |num, i|
    while !stack.empty? && stack[-1] > num && (stack.size - 1 + (n - i) >= k)
      stack.pop
    end
    stack << num if stack.size < k
  end
  stack
end
```

## Scala

```scala
object Solution {
    def mostCompetitive(nums: Array[Int], k: Int): Array[Int] = {
        val n = nums.length
        val stack = new scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- 0 until n) {
            while (stack.nonEmpty && stack.last > nums(i) && (stack.size - 1 + (n - i) >= k)) {
                stack.remove(stack.size - 1)
            }
            if (stack.size < k) {
                stack.append(nums(i))
            }
        }
        stack.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn most_competitive(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k_usize = k as usize;
        let mut stack: Vec<i32> = Vec::with_capacity(k_usize);
        for (i, &num) in nums.iter().enumerate() {
            while let Some(&last) = stack.last() {
                if last > num && stack.len() + (n - i) > k_usize {
                    stack.pop();
                } else {
                    break;
                }
            }
            if stack.len() < k_usize {
                stack.push(num);
            }
        }
        stack
    }
}
```

## Racket

```racket
(define/contract (most-competitive nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((n (length nums))
         (vec (list->vector nums))
         (stack (make-vector k))
         (top 0))
    (for ([i (in-range n)])
      (define x (vector-ref vec i))
      ;; pop while we can get a smaller element and still have enough remaining
      (let loop ()
        (when (and (> top 0)
                   (> (vector-ref stack (- top 1)) x)
                   (>= (+ (- top 1) (- n i)) k))
          (set! top (- top 1))
          (loop)))
      ;; push current element if we still need more
      (when (< top k)
        (vector-set! stack top x)
        (set! top (+ top 1))))
    ;; collect result in order
    (let loop ((i 0) (res '()))
      (if (= i top)
          (reverse res)
          (loop (+ i 1) (cons (vector-ref stack i) res))))))
```

## Erlang

```erlang
-module(solution).
-export([most_competitive/2]).

-spec most_competitive(Nums :: [integer()], K :: integer()) -> [integer()].
most_competitive(Nums, K) ->
    Len = length(Nums),
    {Stack,_} = process(Nums, Len-1, K, [], 0),
    lists:reverse(Stack).

process([], _Rem, _K, Stack, Size) ->
    {Stack, Size};
process([X|Rest], Rem, K, Stack, Size) ->
    {NewStack, NewSize} = maybe_pop(Stack, Size, X, Rem, K),
    case NewSize < K of
        true -> process(Rest, Rem-1, K, [X|NewStack], NewSize+1);
        false -> process(Rest, Rem-1, K, NewStack, NewSize)
    end.

maybe_pop([], Size, _X, _Rem, _K) ->
    {[], Size};
maybe_pop([Top|Rest]=Stack, Size, X, Rem, K) when Top > X, Size + Rem >= K ->
    maybe_pop(Rest, Size-1, X, Rem, K);
maybe_pop(Stack, Size, _X, _Rem, _K) ->
    {Stack, Size}.
```

## Elixir

```elixir
defmodule Solution do
  @spec most_competitive(nums :: [integer], k :: integer) :: [integer]
  def most_competitive(nums, k) do
    n = length(nums)

    {stack_rev, _size} =
      Enum.reduce(Enum.with_index(nums), {[], 0}, fn {num, i}, {stack, size} ->
        {stack_after_pop, size_after_pop} = pop_while(stack, size, num, i, n, k)
        {[num | stack_after_pop], size_after_pop + 1}
      end)

    stack_rev
    |> Enum.reverse()
    |> Enum.take(k)
  end

  defp pop_while([top | rest] = stack, size, num, i, n, k)
       when num < top and size - 1 + (n - i) >= k do
    pop_while(rest, size - 1, num, i, n, k)
  end

  defp pop_while(stack, size, _num, _i, _n, _k), do: {stack, size}
end
```
