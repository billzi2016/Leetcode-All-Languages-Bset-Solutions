# 3523. Make Array Non-decreasing

## Cpp

```cpp
class Solution {
public:
    int maximumPossibleSize(vector<int>& nums) {
        long long curMax = LLONG_MIN;
        int ans = 0;
        for (int x : nums) {
            if ((long long)x >= curMax) {
                ++ans;
                curMax = x;
            } else {
                if (x > curMax) curMax = x; // actually not needed since x<curMax here
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumPossibleSize(int[] nums) {
        int n = nums.length;
        int[] stack = new int[n];
        int top = -1; // empty
        
        for (int num : nums) {
            int cur = num;
            while (top >= 0 && stack[top] > cur) {
                cur = Math.max(cur, stack[top]);
                top--;
            }
            stack[++top] = cur;
        }
        return top + 1;
    }
}
```

## Python

```python
class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for x in reversed(nums):
            while stack and x > stack[-1]:
                stack.pop()
            stack.append(x)
        return len(stack)
```

## Python3

```python
class Solution:
    def maximumPossibleSize(self, nums):
        n = len(nums)
        cnt = 1
        cur_max = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > cur_max:
                cur_max = nums[i]  # merge into current block
            else:
                cnt += 1          # start new block
                cur_max = nums[i]
        return cnt
```

## C

```c
int maximumPossibleSize(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int count = 1;
    int thresh = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; --i) {
        if (nums[i] <= thresh) {
            ++count;
            thresh = nums[i];
        } else {
            thresh = nums[i]; // merge with right block, update max
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumPossibleSize(int[] nums) {
        int count = 0;
        int curMax = -1; // smaller than any possible element (nums[i] >= 1)
        foreach (int x in nums) {
            if (x >= curMax) {
                count++;
                curMax = x;
            }
            // else: merge into current block, curMax unchanged
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumPossibleSize = function(nums) {
    const stack = [];
    for (let i = nums.length - 1; i >= 0; --i) {
        let cur = nums[i];
        while (stack.length && cur > stack[stack.length - 1]) {
            cur = Math.max(cur, stack.pop());
        }
        stack.push(cur);
    }
    return stack.length;
};
```

## Typescript

```typescript
function maximumPossibleSize(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;

    const suffixMax: number[] = new Array(n);
    suffixMax[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        suffixMax[i] = Math.max(nums[i], suffixMax[i + 1]);
    }

    let ans = 0;
    let prevMax = Number.NEGATIVE_INFINITY;
    let curMax = Number.NEGATIVE_INFINITY;

    for (let i = 0; i < n - 1; ++i) {
        curMax = Math.max(curMax, nums[i]);

        if (curMax >= prevMax && suffixMax[i + 1] >= curMax) {
            ans++;
            prevMax = curMax;
            curMax = Number.NEGATIVE_INFINITY;
        }
    }

    const finalMax = Math.max(curMax, nums[n - 1]);
    if (finalMax >= prevMax) ans++;

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumPossibleSize($nums) {
        $stack = [];
        // iterate from right to left
        for ($i = count($nums) - 1; $i >= 0; --$i) {
            $cur = $nums[$i];
            while (!empty($stack) && $cur > end($stack)) {
                $top = array_pop($stack);
                if ($top > $cur) {
                    $cur = $top;
                }
            }
            $stack[] = $cur;
        }
        return count($stack);
    }
}
```

## Swift

```swift
class Solution {
    func maximumPossibleSize(_ nums: [Int]) -> Int {
        var stack = [Int]()
        for x in nums {
            stack.append(x)
            while stack.count >= 2 && stack[stack.count - 2] > stack[stack.count - 1] {
                // Merge the last two blocks; keep the larger (the second-last) as the block's max
                stack.removeLast()
            }
        }
        return stack.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumPossibleSize(nums: IntArray): Int {
        val n = nums.size
        val stack = IntArray(n)
        var sz = 0
        for (i in n - 1 downTo 0) {
            var cur = nums[i]
            while (sz > 0 && stack[sz - 1] < cur) {
                // merge with the right block
                cur = maxOf(cur, stack[sz - 1])
                sz--
            }
            stack[sz++] = cur
        }
        return sz
    }
}
```

## Dart

```dart
class Solution {
  int maximumPossibleSize(List<int> nums) {
    List<int> stack = [];
    for (int x in nums) {
      stack.add(x);
      while (stack.length >= 2 && stack[stack.length - 2] > stack.last) {
        stack.removeLast();
      }
    }
    return stack.length;
  }
}
```

## Golang

```go
func maximumPossibleSize(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    ans := 1
    curMax := nums[n-1]
    for i := n - 2; i >= 0; i-- {
        if nums[i] <= curMax {
            ans++
            curMax = nums[i]
        } else {
            curMax = nums[i]
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_possible_size(nums)
  stack = []
  (nums.length - 1).downto(0) do |i|
    cur = nums[i]
    while !stack.empty? && cur > stack[-1]
      stack.pop
    end
    stack << cur
  end
  stack.size
end
```

## Scala

```scala
object Solution {
    def maximumPossibleSize(nums: Array[Int]): Int = {
        val n = nums.length
        if (n == 0) return 0
        var ans = 1
        var cur = nums(n - 1)
        var i = n - 2
        while (i >= 0) {
            val v = nums(i)
            if (v <= cur) {
                ans += 1
                cur = v
            } else {
                cur = v // merge with the right block
            }
            i -= 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_possible_size(nums: Vec<i32>) -> i32 {
        let mut cur = std::i32::MAX;
        let mut ans = 0;
        for &x in nums.iter().rev() {
            if x <= cur {
                ans += 1;
                cur = x;
            } else {
                // merge with the block on the right, its max becomes larger
                cur = x.max(cur);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-possible-size nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (last 0) (cnt 0))
    (if (null? lst)
        cnt
        (let ((x (car lst)))
          (if (>= x last)
              (loop (cdr lst) x (+ cnt 1))
              (loop (cdr lst) last cnt))))))
```

## Erlang

```erlang
-spec maximum_possible_size(Nums :: [integer()]) -> integer().
maximum_possible_size(Nums) ->
    Inf = 1 bsl 30,
    {Ans, _} = lists:foldl(
        fun(V, {Cnt, Cur}) ->
            if V =< Cur -> {Cnt + 1, V};
               true     -> {Cnt, V}
            end
        end,
        {0, Inf},
        lists:reverse(Nums)
    ),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_possible_size(nums :: [integer]) :: integer
  def maximum_possible_size([head | tail]) do
    {ans, _cur} =
      Enum.reduce(tail, {1, head}, fn val, {cnt, cur_max} ->
        if val <= cur_max do
          {cnt + 1, val}
        else
          {cnt, val}
        end
      end)

    ans
  end

  def maximum_possible_size([]), do: 0
end
```
