# 2149. Rearrange Array Elements by Sign

## Cpp

```cpp
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        int posIdx = 0, negIdx = 1;
        for (int x : nums) {
            if (x > 0) {
                ans[posIdx] = x;
                posIdx += 2;
            } else {
                ans[negIdx] = x;
                negIdx += 2;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        int posIdx = 0, negIdx = 1;
        for (int num : nums) {
            if (num > 0) {
                ans[posIdx] = num;
                posIdx += 2;
            } else {
                ans[negIdx] = num;
                negIdx += 2;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        pos_idx, neg_idx = 0, 1
        for num in nums:
            if num > 0:
                ans[pos_idx] = num
                pos_idx += 2
            else:
                ans[neg_idx] = num
                neg_idx += 2
        return ans
```

## Python3

```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pos_idx, neg_idx = 0, 1
        for x in nums:
            if x > 0:
                ans[pos_idx] = x
                pos_idx += 2
            else:
                ans[neg_idx] = x
                neg_idx += 2
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize * sizeof(int));
    int posIdx = 0;
    int negIdx = 1;
    
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > 0) {
            ans[posIdx] = nums[i];
            posIdx += 2;
        } else {
            ans[negIdx] = nums[i];
            negIdx += 2;
        }
    }
    
    *returnSize = numsSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] RearrangeArray(int[] nums)
    {
        int n = nums.Length;
        int[] ans = new int[n];
        int posIdx = 0, negIdx = 1;

        foreach (int num in nums)
        {
            if (num > 0)
            {
                ans[posIdx] = num;
                posIdx += 2;
            }
            else
            {
                ans[negIdx] = num;
                negIdx += 2;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    const n = nums.length;
    const ans = new Array(n);
    let posIdx = 0; // even indices for positives
    let negIdx = 1; // odd indices for negatives
    
    for (let i = 0; i < n; i++) {
        const val = nums[i];
        if (val > 0) {
            ans[posIdx] = val;
            posIdx += 2;
        } else {
            ans[negIdx] = val;
            negIdx += 2;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function rearrangeArray(nums: number[]): number[] {
    const n = nums.length;
    const ans = new Array<number>(n);
    let posIdx = 0;
    let negIdx = 1;
    for (const x of nums) {
        if (x > 0) {
            ans[posIdx] = x;
            posIdx += 2;
        } else {
            ans[negIdx] = x;
            negIdx += 2;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function rearrangeArray($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $posIdx = 0;
        $negIdx = 1;
        foreach ($nums as $num) {
            if ($num > 0) {
                $ans[$posIdx] = $num;
                $posIdx += 2;
            } else {
                $ans[$negIdx] = $num;
                $negIdx += 2;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func rearrangeArray(_ nums: [Int]) -> [Int] {
        var result = Array(repeating: 0, count: nums.count)
        var posIndex = 0
        var negIndex = 1
        
        for num in nums {
            if num > 0 {
                result[posIndex] = num
                posIndex += 2
            } else {
                result[negIndex] = num
                negIndex += 2
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rearrangeArray(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(n)
        var posIdx = 0
        var negIdx = 1
        for (num in nums) {
            if (num > 0) {
                ans[posIdx] = num
                posIdx += 2
            } else {
                ans[negIdx] = num
                negIdx += 2
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> rearrangeArray(List<int> nums) {
    int n = nums.length;
    List<int> ans = List.filled(n, 0);
    int posIdx = 0, negIdx = 1;
    for (int num in nums) {
      if (num > 0) {
        ans[posIdx] = num;
        posIdx += 2;
      } else {
        ans[negIdx] = num;
        negIdx += 2;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func rearrangeArray(nums []int) []int {
    n := len(nums)
    ans := make([]int, n)
    posIdx, negIdx := 0, 1
    for _, v := range nums {
        if v > 0 {
            ans[posIdx] = v
            posIdx += 2
        } else {
            ans[negIdx] = v
            negIdx += 2
        }
    }
    return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def rearrange_array(nums)
  n = nums.length
  ans = Array.new(n)
  pos_idx = 0
  neg_idx = 1

  nums.each do |num|
    if num > 0
      ans[pos_idx] = num
      pos_idx += 2
    else
      ans[neg_idx] = num
      neg_idx += 2
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def rearrangeArray(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val ans = new Array[Int](n)
        var posIdx = 0
        var negIdx = 1
        for (x <- nums) {
            if (x > 0) {
                ans(posIdx) = x
                posIdx += 2
            } else {
                ans(negIdx) = x
                negIdx += 2
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0; n];
        let (mut pos_idx, mut neg_idx) = (0usize, 1usize);
        for &num in nums.iter() {
            if num > 0 {
                ans[pos_idx] = num;
                pos_idx += 2;
            } else {
                ans[neg_idx] = num;
                neg_idx += 2;
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (rearrange-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (ans (make-vector n))
         (pos-index 0)
         (neg-index 1))
    (for ([x nums])
      (if (> x 0)
          (begin
            (vector-set! ans pos-index x)
            (set! pos-index (+ pos-index 2)))
          (begin
            (vector-set! ans neg-index x)
            (set! neg-index (+ neg-index 2)))))
    (vector->list ans)))
```

## Erlang

```erlang
-module(solution).
-export([rearrange_array/1]).

-spec rearrange_array(Nums :: [integer()]) -> [integer()].
rearrange_array(Nums) ->
    {PosRev, NegRev} = split(Nums, [], []),
    Pos = lists:reverse(PosRev),
    Neg = lists:reverse(NegRev),
    merge(Pos, Neg).

split([], PosAcc, NegAcc) ->
    {PosAcc, NegAcc};
split([H|T], PosAcc, NegAcc) when H > 0 ->
    split(T, [H|PosAcc], NegAcc);
split([H|T], PosAcc, NegAcc) ->
    split(T, PosAcc, [H|NegAcc]).

merge([], []) -> [];
merge([P|Ps], [N|Ns]) -> [P,N | merge(Ps, Ns)].
```

## Elixir

```elixir
defmodule Solution do
  @spec rearrange_array(nums :: [integer]) :: [integer]
  def rearrange_array(nums) do
    {pos_rev, neg_rev} =
      Enum.reduce(nums, {[], []}, fn x, {pos_acc, neg_acc} ->
        if x > 0, do: {[x | pos_acc], neg_acc}, else: {pos_acc, [x | neg_acc]}
      end)

    pos = Enum.reverse(pos_rev)
    neg = Enum.reverse(neg_rev)

    Enum.flat_map(Enum.zip(pos, neg), fn {p, n} -> [p, n] end)
  end
end
```
