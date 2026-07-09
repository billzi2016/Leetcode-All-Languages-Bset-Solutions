# 2289. Steps to Make Array Non-decreasing

## Cpp

```cpp
class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);
        stack<int> st; // store indices
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int cur = 0;
            while (!st.empty() && nums[st.top()] <= nums[i]) {
                cur = max(cur, dp[st.top()]);
                st.pop();
            }
            if (!st.empty()) {
                dp[i] = cur + 1;
                ans = max(ans, dp[i]);
            } // else dp[i] stays 0
            st.push(i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int totalSteps(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int cur = 0;
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                cur = Math.max(cur, dp[stack.pop()]);
            }
            if (!stack.isEmpty()) {
                dp[i] = cur + 1;
                ans = Math.max(ans, dp[i]);
            } else {
                dp[i] = 0;
            }
            stack.push(i);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []  # each element is (value, steps)
        max_steps = 0
        for num in nums:
            cur_step = 0
            # pop elements that are less than or equal to current
            while stack and num >= stack[-1][0]:
                cur_step = max(cur_step, stack[-1][1])
                stack.pop()
            if not stack:
                cur_step = 0
            else:
                cur_step += 1
            max_steps = max(max_steps, cur_step)
            stack.append((num, cur_step))
        return max_steps
```

## Python3

```python
class Solution:
    def totalSteps(self, nums):
        stack = []  # each element is (value, steps)
        ans = 0
        for x in nums:
            cur = 0
            while stack and x > stack[-1][0]:
                cur = max(cur, stack.pop()[1])
            if not stack:
                cur = 0
            else:
                cur += 1
            ans = max(ans, cur)
            stack.append((x, cur))
        return ans
```

## C

```c
#include <stdlib.h>

int totalSteps(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int *dp = (int*)calloc(numsSize, sizeof(int));
    int *stack = (int*)malloc(numsSize * sizeof(int));
    int top = -1;
    int ans = 0;

    for (int i = 0; i < numsSize; ++i) {
        int curMax = 0;
        while (top >= 0 && nums[stack[top]] <= nums[i]) {
            if (dp[stack[top]] > curMax) curMax = dp[stack[top]];
            --top;
        }
        if (top == -1) {
            dp[i] = 0;
        } else {
            dp[i] = curMax + 1;
            if (dp[i] > ans) ans = dp[i];
        }
        stack[++top] = i;
    }

    free(dp);
    free(stack);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int TotalSteps(int[] nums) {
        var stack = new System.Collections.Generic.Stack<(int val, int step)>();
        int maxSteps = 0;
        foreach (var num in nums) {
            int curStep = 0;
            while (stack.Count > 0 && num >= stack.Peek().val) {
                curStep = Math.Max(curStep, stack.Peek().step);
                stack.Pop();
            }
            if (stack.Count == 0) {
                curStep = 0;
            } else {
                curStep += 1;
            }
            maxSteps = Math.Max(maxSteps, curStep);
            stack.Push((num, curStep));
        }
        return maxSteps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var totalSteps = function(nums) {
    const stack = []; // each element: [value, steps]
    let ans = 0;
    for (const num of nums) {
        let cur = 0;
        while (stack.length && stack[stack.length - 1][0] <= num) {
            cur = Math.max(cur, stack.pop()[1]);
        }
        if (stack.length === 0) {
            cur = 0; // no greater element on the left
        } else {
            cur += 1; // will be removed one step after the max of popped elements
        }
        ans = Math.max(ans, cur);
        stack.push([num, cur]);
    }
    return ans;
};
```

## Typescript

```typescript
function totalSteps(nums: number[]): number {
    const stack: [number, number][] = []; // [value, steps]
    let answer = 0;
    for (const num of nums) {
        let curStep = 0;
        while (stack.length && num > stack[stack.length - 1][0]) {
            curStep = Math.max(curStep, stack.pop()![1]);
        }
        if (stack.length === 0) {
            curStep = 0;
        } else {
            curStep += 1;
        }
        answer = Math.max(answer, curStep);
        stack.push([num, curStep]);
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function totalSteps($nums) {
        $stack = [];
        $maxSteps = 0;
        foreach ($nums as $x) {
            $curStep = 0;
            while (!empty($stack) && $stack[count($stack) - 1]['val'] < $x) {
                $curStep = max($curStep, $stack[count($stack) - 1]['steps']);
                array_pop($stack);
            }
            if (empty($stack)) {
                $curStep = 0;
            } else {
                $curStep += 1;
            }
            $maxSteps = max($maxSteps, $curStep);
            $stack[] = ['val' => $x, 'steps' => $curStep];
        }
        return $maxSteps;
    }
}
```

## Swift

```swift
class Solution {
    func totalSteps(_ nums: [Int]) -> Int {
        var stack: [(value: Int, steps: Int)] = []
        var answer = 0
        for x in nums {
            var cur = 0
            while !stack.isEmpty && x >= stack[stack.count - 1].value {
                cur = max(cur, stack.removeLast().steps)
            }
            if stack.isEmpty {
                cur = 0
            } else {
                cur += 1
            }
            answer = max(answer, cur)
            stack.append((value: x, steps: cur))
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalSteps(nums: IntArray): Int {
        val n = nums.size
        val dp = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        var answer = 0
        for (i in 0 until n) {
            var cur = 0
            while (stack.isNotEmpty() && nums[i] >= nums[stack.peekLast()!!]) {
                cur = kotlin.math.max(cur, dp[stack.pollLast()!!])
            }
            if (stack.isEmpty()) {
                dp[i] = 0
            } else {
                dp[i] = cur + 1
            }
            answer = kotlin.math.max(answer, dp[i])
            stack.addLast(i)
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int totalSteps(List<int> nums) {
    int n = nums.length;
    List<int> dp = List.filled(n, 0);
    List<int> stack = [];
    int ans = 0;

    for (int i = 0; i < n; ++i) {
      int cur = 0;
      while (stack.isNotEmpty && nums[stack.last] <= nums[i]) {
        int idx = stack.removeLast();
        cur = max(cur, dp[idx]);
      }
      if (stack.isEmpty) {
        dp[i] = 0;
      } else {
        dp[i] = cur + 1;
        ans = max(ans, dp[i]);
      }
      stack.add(i);
    }

    return ans;
  }
}
```

## Golang

```go
func totalSteps(nums []int) int {
	n := len(nums)
	dp := make([]int, n)
	stack := make([]int, 0, n)
	ans := 0

	for i := 0; i < n; i++ {
		cur := 0
		for len(stack) > 0 && nums[stack[len(stack)-1]] <= nums[i] {
			idx := stack[len(stack)-1]
			if dp[idx] > cur {
				cur = dp[idx]
			}
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			dp[i] = 0
		} else {
			dp[i] = cur + 1
			if dp[i] > ans {
				ans = dp[i]
			}
		}
		stack = append(stack, i)
	}
	return ans
}
```

## Ruby

```ruby
def total_steps(nums)
  stack = []
  max_steps = 0
  nums.each do |x|
    cur = 0
    while !stack.empty? && stack[-1][0] <= x
      cur = [cur, stack.pop[1]].max
    end
    if stack.empty?
      cur = 0
    else
      cur += 1
    end
    max_steps = [max_steps, cur].max
    stack << [x, cur]
  end
  max_steps
end
```

## Scala

```scala
object Solution {
    def totalSteps(nums: Array[Int]): Int = {
        val n = nums.length
        val dp = new Array[Int](n)
        import scala.collection.mutable.ArrayDeque
        val stack = new ArrayDeque[Int]() // store indices, monotonic decreasing by value
        var ans = 0

        for (i <- 0 until n) {
            var cur = 0
            while (stack.nonEmpty && nums(stack.last) <= nums(i)) {
                cur = math.max(cur, dp(stack.removeLast()))
            }
            if (stack.nonEmpty) {
                dp(i) = cur + 1
                ans = math.max(ans, dp(i))
            } else {
                dp(i) = 0
            }
            stack.append(i)
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn total_steps(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![0i32; n];
        let mut stack: Vec<usize> = Vec::new();
        let mut ans = 0i32;
        for i in 0..n {
            let mut cur_step = 0i32;
            while let Some(&last) = stack.last() {
                if nums[last] < nums[i] {
                    cur_step = cur_step.max(dp[last]);
                    stack.pop();
                } else {
                    break;
                }
            }
            if let Some(&last) = stack.last() {
                if nums[last] == nums[i] {
                    dp[i] = 0;
                } else {
                    dp[i] = cur_step + 1;
                    ans = ans.max(dp[i]);
                }
            } // else dp[i] stays 0
            stack.push(i);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (total-steps nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (dp (make-vector n 0))
         (stack '())
         (max-step 0))
    (for ([i (in-range n)])
      (define steps 0)
      ;; pop all indices with value <= current
      (let loop ()
        (when (and (pair? stack)
                   (<= (vector-ref arr (car stack)) (vector-ref arr i)))
          (set! steps (max steps (vector-ref dp (car stack))))
          (set! stack (cdr stack))
          (loop)))
      (if (null? stack)
          (vector-set! dp i 0)
          (begin
            (vector-set! dp i (+ steps 1))
            (when (> (vector-ref dp i) max-step)
              (set! max-step (vector-ref dp i)))))
      (set! stack (cons i stack)))
    max-step))
```

## Erlang

```erlang
-spec total_steps(Nums :: [integer()]) -> integer().
total_steps(Nums) ->
    total_steps_loop(Nums, [], 0).

total_steps_loop([], _Stack, Max) ->
    Max;
total_steps_loop([Num | Rest], Stack, Max) ->
    {NewStack, Steps} = process_num(Num, Stack),
    NewMax = erlang:max(Max, Steps),
    total_steps_loop(Rest, NewStack, NewMax).

process_num(Num, Stack) ->
    {TmpStack, Cur} = pop_smaller(Num, Stack, 0),
    Steps = case TmpStack of
                [] -> 0;
                _ -> Cur + 1
            end,
    {[{Num, Steps} | TmpStack], Steps}.

pop_smaller(_Num, [], Acc) ->
    {[], Acc};
pop_smaller(Num, [{Val, Step} = Top | Tail], Acc) when Num >= Val ->
    NewAcc = erlang:max(Acc, Step),
    pop_smaller(Num, Tail, NewAcc);
pop_smaller(_Num, Stack, Acc) ->
    {Stack, Acc}.
```

## Elixir

```elixir
defmodule Solution do
  @spec total_steps(nums :: [integer]) :: integer
  def total_steps(nums) do
    {ans, _stack} =
      Enum.reduce(nums, {0, []}, fn x, {max_ans, stack} ->
        {new_stack, max_popped_step} = pop_smaller(stack, x, 0)

        cur_step =
          if new_stack == [] do
            0
          else
            max_popped_step + 1
          end

        new_max = if cur_step > max_ans, do: cur_step, else: max_ans
        {new_max, [{x, cur_step} | new_stack]}
      end)

    ans
  end

  defp pop_smaller([], _x, acc), do: {[], acc}

  defp pop_smaller([{val, step} = _head | tail], x, acc) when val < x do
    new_acc = if step > acc, do: step, else: acc
    pop_smaller(tail, x, new_acc)
  end

  defp pop_smaller(stack, _x, acc), do: {stack, acc}
end
```
