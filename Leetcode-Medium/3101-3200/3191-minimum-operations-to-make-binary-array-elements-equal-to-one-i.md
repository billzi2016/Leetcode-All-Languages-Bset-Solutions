# 3191. Minimum Operations to Make Binary Array Elements Equal to One I

## Cpp

```cpp
class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = nums.size();
        int ops = 0;
        for (int i = 2; i < n; ++i) {
            if (nums[i - 2] == 0) {
                // flip three consecutive elements
                nums[i - 2] ^= 1;
                nums[i - 1] ^= 1;
                nums[i] ^= 1;
                ++ops;
            }
        }
        for (int v : nums) {
            if (v == 0) return -1;
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        int[] end = new int[n + 3]; // marks when a flip effect ends
        int curFlip = 0; // current parity of flips affecting position i
        int ops = 0;
        for (int i = 0; i < n; i++) {
            curFlip ^= end[i];
            int effective = nums[i] ^ curFlip;
            if (effective == 0) { // need to flip starting at i
                if (i + 2 >= n) return -1;
                ops++;
                curFlip ^= 1;          // start new flip effect
                end[i + 3] ^= 1;       // it will cease after three positions
            }
        }
        return ops;
    }
}
```

## Python

```python
import collections

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        flip_queue = collections.deque()
        ops = 0
        for i in range(n):
            # discard flips that no longer affect position i
            while flip_queue and flip_queue[0] + 2 < i:
                flip_queue.popleft()
            # current value after applied flips
            cur = (nums[i] + len(flip_queue)) % 2
            if cur == 0:  # need to flip starting at i
                if i + 2 >= n:
                    return -1
                ops += 1
                flip_queue.append(i)
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ops += 1
        if any(x == 0 for x in nums[-2:]):
            return -1
        return ops
```

## C

```c
int minOperations(int* nums, int numsSize) {
    int ops = 0;
    for (int i = 0; i + 2 < numsSize; ++i) {
        if (nums[i] == 0) {
            nums[i] ^= 1;
            nums[i + 1] ^= 1;
            nums[i + 2] ^= 1;
            ++ops;
        }
    }
    for (int i = numsSize - 2; i < numsSize; ++i) {
        if (i >= 0 && nums[i] == 0) return -1;
    }
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        int ops = 0;
        for (int i = 0; i <= n - 3; i++) {
            if (nums[i] == 0) {
                nums[i] ^= 1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                ops++;
            }
        }
        return (nums[n - 2] == 1 && nums[n - 1] == 1) ? ops : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0); // marks where a flip effect ends
    let curFlip = 0; // current parity of flips affecting position i
    let ops = 0;
    
    for (let i = 0; i < n; ++i) {
        curFlip ^= diff[i]; // remove flips that expired before i
        
        // effective value after applying current flips
        const val = nums[i] ^ curFlip;
        if (val === 0) { // need to flip this position
            if (i + 3 > n) return -1; // not enough elements for a triplet
            ops++;
            curFlip ^= 1;          // start new flip effect
            diff[i + 3] ^= 1;      // it will end after index i+2
        }
    }
    
    return ops;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    const n = nums.length;
    let ops = 0;
    for (let i = 0; i <= n - 3; ++i) {
        if (nums[i] === 0) {
            nums[i] ^= 1;
            nums[i + 1] ^= 1;
            nums[i + 2] ^= 1;
            ops++;
        }
    }
    for (let i = n - 2; i < n; ++i) {
        if (i >= 0 && nums[i] === 0) return -1;
    }
    return ops;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $n = count($nums);
        // marks where a flip operation starts
        $startFlip = array_fill(0, $n, false);
        $parity = 0; // current parity of flips affecting position i
        $ops = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i >= 3 && $startFlip[$i - 3]) {
                // the flip that started three positions ago no longer affects i
                $parity ^= 1;
            }
            $val = $nums[$i];
            if ($parity) {
                $val ^= 1; // apply current parity
            }
            if ($val == 0) {
                if ($i + 2 >= $n) {
                    return -1;
                }
                $ops++;
                $startFlip[$i] = true; // start a new flip at i
                $parity ^= 1; // this flip now affects current and next two positions
            }
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var startFlip = [Int](repeating: 0, count: n)
        var flipParity = 0
        var ans = 0
        
        for i in 0..<n {
            if i >= 3 {
                flipParity ^= startFlip[i - 3]
            }
            let current = nums[i] ^ flipParity
            if current == 0 {
                if i + 2 >= n { return -1 }
                ans += 1
                flipParity ^= 1
                startFlip[i] = 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        var ops = 0
        val n = nums.size
        for (i in 0 until n - 2) {
            if (nums[i] == 0) {
                // flip three consecutive elements
                nums[i] = 1
                nums[i + 1] = nums[i + 1] xor 1
                nums[i + 2] = nums[i + 2] xor 1
                ops++
            }
        }
        return if (nums[n - 2] == 0 || nums[n - 1] == 0) -1 else ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    int n = nums.length;
    int ops = 0;
    for (int i = 0; i <= n - 3; ++i) {
      if (nums[i] == 0) {
        nums[i] ^= 1;
        nums[i + 1] ^= 1;
        nums[i + 2] ^= 1;
        ops++;
      }
    }
    for (int i = n - 2; i < n; ++i) {
      if (nums[i] == 0) return -1;
    }
    return ops;
  }
}
```

## Golang

```go
func minOperations(nums []int) int {
    n := len(nums)
    ops := 0
    for i := 0; i+2 < n; i++ {
        if nums[i] == 0 {
            nums[i] ^= 1
            nums[i+1] ^= 1
            nums[i+2] ^= 1
            ops++
        }
    }
    for _, v := range nums {
        if v == 0 {
            return -1
        }
    }
    return ops
}
```

## Ruby

```ruby
def min_operations(nums)
  n = nums.length
  count = 0
  (0..n - 3).each do |i|
    if nums[i] == 0
      nums[i] ^= 1
      nums[i + 1] ^= 1
      nums[i + 2] ^= 1
      count += 1
    end
  end
  (nums[n - 2] == 1 && nums[n - 1] == 1) ? count : -1
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        var count = 0
        val n = nums.length
        var i = 0
        while (i <= n - 3) {
            if (nums(i) == 0) {
                nums(i) ^= 1
                nums(i + 1) ^= 1
                nums(i + 2) ^= 1
                count += 1
            }
            i += 1
        }
        if (nums(n - 2) == 0 || nums(n - 1) == 0) -1 else count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return -1;
        }
        let mut arr = nums;
        let mut ops = 0i32;
        for i in 2..n {
            if arr[i - 2] == 0 {
                // flip three consecutive elements
                arr[i - 2] ^= 1;
                arr[i - 1] ^= 1;
                arr[i] ^= 1;
                ops += 1;
            }
        }
        if arr.iter().all(|&x| x == 1) { ops } else { -1 }
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums)))
    (define (toggle idx)
      (vector-set! v idx (if (= (vector-ref v idx) 0) 1 0)))
    (let loop ((i 0) (cnt 0))
      (if (> i (- n 3))
          (if (or (= (vector-ref v (- n 2)) 0)
                  (= (vector-ref v (- n 1)) 0))
              -1
              cnt)
          (if (= (vector-ref v i) 0)
              (begin
                (toggle i)
                (toggle (+ i 1))
                (toggle (+ i 2))
                (loop (+ i 1) (+ cnt 1)))
              (loop (+ i 1) cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    N = length(Nums),
    case go(0, Nums, [], 0, 0, N) of
        {ok, Count} -> Count;
        error -> -1
    end.

go(Index, Rest, Queue, Parity, Count, N) when Index < N ->
    {NewQueue, NewParity} = expire(Index, Queue, Parity),
    [Cur | Tail] = Rest,
    Effective = Cur bxor NewParity,
    case Effective of
        0 ->
            if Index + 2 >= N -> error;
               true ->
                    ExpireIdx = Index + 3,
                    go(Index + 1, Tail, [ExpireIdx | NewQueue],
                       NewParity bxor 1, Count + 1, N)
            end;
        _ ->
            go(Index + 1, Tail, NewQueue, NewParity, Count, N)
    end;
go(_, [], _, _, Count, _) -> {ok, Count}.

expire(Index, Queue, Parity) ->
    case Queue of
        [H | T] when H =< Index ->
            expire(Index, T, Parity bxor 1);
        _ -> {Queue, Parity}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    n = length(nums)
    arr = :array.from_list(nums)

    init_state = %{cur: 0, ans: 0, q: :queue.new()}

    result =
      Enum.reduce_while(0..(n - 1), init_state, fn i, state ->
        cur = state.cur
        q = state.q

        # Remove flips that expire at current index
        {cur, q} =
          case :queue.peek(q) do
            {:value, v} when v == i ->
              {_val, q2} = :queue.out(q)
              {1 - cur, q2}
            _ ->
              {cur, q}
          end

        val = :array.get(i, arr)
        effective = rem(val + cur, 2)

        if effective == 0 do
          if i + 2 >= n do
            {:halt, -1}
          else
            new_cur = 1 - cur
            new_q = :queue.in(i + 3, q)
            {:cont,
             %{state |
               cur: new_cur,
               ans: state.ans + 1,
               q: new_q}}
          end
        else
          {:cont, %{state | cur: cur, q: q}}
        end
      end)

    case result do
      -1 -> -1
      final_state -> final_state.ans
    end
  end
end
```
