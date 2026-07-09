# 1829. Maximum XOR for Each Query

## Cpp

```cpp
class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int n = nums.size();
        int xorAll = 0;
        for (int num : nums) xorAll ^= num;
        int mask = (1 << maximumBit) - 1;
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            ans[i] = xorAll ^ mask;
            xorAll ^= nums[n - 1 - i];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int n = nums.length;
        int mask = (1 << maximumBit) - 1;
        int xorAll = 0;
        for (int num : nums) {
            xorAll ^= num;
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = xorAll ^ mask;
            xorAll ^= nums[n - 1 - i];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        mask = (1 << maximumBit) - 1
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(xor_sum ^ mask)
            xor_sum ^= nums[n - 1 - i]  # remove the last element for next query
        return ans
```

## Python3

```python
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        cur_xor = 0
        for num in nums:
            cur_xor ^= num
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(cur_xor ^ mask)
            cur_xor ^= nums[i]
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getMaximumXor(int* nums, int numsSize, int maximumBit, int* returnSize) {
    int mask = (1 << maximumBit) - 1;
    int xorAll = 0;
    for (int i = 0; i < numsSize; ++i) {
        xorAll ^= nums[i];
    }
    
    int *ans = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        ans[i] = xorAll ^ mask;
        xorAll ^= nums[numsSize - 1 - i]; // remove last element for next query
    }
    
    *returnSize = numsSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] GetMaximumXor(int[] nums, int maximumBit)
    {
        int n = nums.Length;
        int xor = 0;
        foreach (int num in nums)
            xor ^= num;

        int mask = (1 << maximumBit) - 1;
        int[] ans = new int[n];

        for (int i = 0; i < n; i++)
        {
            ans[i] = xor ^ mask;
            xor ^= nums[n - 1 - i];
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} maximumBit
 * @return {number[]}
 */
var getMaximumXor = function(nums, maximumBit) {
    const n = nums.length;
    let xorAll = 0;
    for (let i = 0; i < n; ++i) {
        xorAll ^= nums[i];
    }
    const mask = (1 << maximumBit) - 1;
    const ans = new Array(n);
    for (let i = 0; i < n; ++i) {
        ans[i] = xorAll ^ mask;
        xorAll ^= nums[n - 1 - i];
    }
    return ans;
};
```

## Typescript

```typescript
function getMaximumXor(nums: number[], maximumBit: number): number[] {
    const n = nums.length;
    let xor = 0;
    for (const v of nums) {
        xor ^= v;
    }
    const mask = (1 << maximumBit) - 1;
    const ans: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        ans[i] = xor ^ mask;
        xor ^= nums[n - 1 - i];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $maximumBit
     * @return Integer[]
     */
    function getMaximumXor($nums, $maximumBit) {
        $xor = 0;
        foreach ($nums as $num) {
            $xor ^= $num;
        }
        $mask = (1 << $maximumBit) - 1;
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $ans[] = $xor ^ $mask;
            // remove the last element of current prefix
            $xor ^= $nums[$n - 1 - $i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func getMaximumXor(_ nums: [Int], _ maximumBit: Int) -> [Int] {
        var totalXor = 0
        for num in nums {
            totalXor ^= num
        }
        let mask = (1 << maximumBit) - 1
        var result = [Int]()
        result.reserveCapacity(nums.count)
        var currentXor = totalXor
        for i in 0..<nums.count {
            result.append(currentXor ^ mask)
            currentXor ^= nums[nums.count - 1 - i]
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMaximumXor(nums: IntArray, maximumBit: Int): IntArray {
        var xorAll = 0
        for (num in nums) {
            xorAll = xorAll xor num
        }
        val mask = (1 shl maximumBit) - 1
        val n = nums.size
        val answer = IntArray(n)
        var idx = 0
        for (i in n - 1 downTo 0) {
            answer[idx++] = xorAll xor mask
            xorAll = xorAll xor nums[i]
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> getMaximumXor(List<int> nums, int maximumBit) {
    int mask = (1 << maximumBit) - 1;
    int xorProduct = 0;
    for (var num in nums) {
      xorProduct ^= num;
    }
    int n = nums.length;
    List<int> ans = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      ans[i] = xorProduct ^ mask;
      xorProduct ^= nums[n - 1 - i];
    }
    return ans;
  }
}
```

## Golang

```go
func getMaximumXor(nums []int, maximumBit int) []int {
	xor := 0
	for _, v := range nums {
		xor ^= v
	}
	mask := (1 << maximumBit) - 1
	n := len(nums)
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = xor ^ mask
		xor ^= nums[n-1-i]
	}
	return ans
}
```

## Ruby

```ruby
def get_maximum_xor(nums, maximum_bit)
  mask = (1 << maximum_bit) - 1
  xor = 0
  nums.each { |num| xor ^= num }
  ans = []
  (nums.length - 1).downto(0) do |i|
    ans << (xor ^ mask)
    xor ^= nums[i]
  end
  ans
end
```

## Scala

```scala
object Solution {
  def getMaximumXor(nums: Array[Int], maximumBit: Int): Array[Int] = {
    val n = nums.length
    var xorAll = 0
    var i = 0
    while (i < n) {
      xorAll ^= nums(i)
      i += 1
    }
    val mask = (1 << maximumBit) - 1
    val ans = new Array[Int](n)
    var idx = 0
    while (idx < n) {
      ans(idx) = xorAll ^ mask
      xorAll ^= nums(n - 1 - idx)
      idx += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_maximum_xor(nums: Vec<i32>, maximum_bit: i32) -> Vec<i32> {
        let n = nums.len();
        let mut xor_val: i32 = 0;
        for &num in &nums {
            xor_val ^= num;
        }
        let mask: i32 = (1i32 << maximum_bit) - 1;
        let mut ans = Vec::with_capacity(n);
        for i in 0..n {
            ans.push(xor_val ^ mask);
            let idx = n - 1 - i;
            xor_val ^= nums[idx];
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (get-maximum-xor nums maximumBit)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((mask (sub1 (arithmetic-shift 1 maximumBit)))
         (total-xor (foldl bitwise-xor 0 nums))
         (rev-nums (reverse nums)))
    (let loop ((remaining rev-nums) (cur total-xor) (acc '()))
      (if (null? remaining)
          (reverse acc)
          (let* ((ans (bitwise-xor cur mask))
                 (next-cur (bitwise-xor cur (car remaining))))
            (loop (cdr remaining) next-cur (cons ans acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([get_maximum_xor/2]).

-spec get_maximum_xor(Nums :: [integer()], MaximumBit :: integer()) -> [integer()].
get_maximum_xor(Nums, MaximumBit) ->
    Mask = (1 bsl MaximumBit) - 1,
    TotalXor = lists:foldl(fun(X, Acc) -> X bxor Acc end, 0, Nums),
    process_reverse(lists:reverse(Nums), TotalXor, Mask, []).

process_reverse([], _Xor, _Mask, Acc) ->
    lists:reverse(Acc);
process_reverse([Num|Rest], Xor, Mask, Acc) ->
    Answer = Xor bxor Mask,
    NewXor = Xor bxor Num,
    process_reverse(Rest, NewXor, Mask, [Answer|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_maximum_xor(nums :: [integer], maximum_bit :: integer) :: [integer]
  def get_maximum_xor(nums, maximum_bit) do
    mask = (1 <<< maximum_bit) - 1

    total =
      Enum.reduce(nums, 0, fn x, acc ->
        Bitwise.bxor(acc, x)
      end)

    {answers_rev, _} =
      Enum.reduce(Enum.reverse(nums), {[], total}, fn num, {list, cur_xor} ->
        ans = Bitwise.bxor(cur_xor, mask)
        {[ans | list], Bitwise.bxor(cur_xor, num)}
      end)

    Enum.reverse(answers_rev)
  end
end
```
