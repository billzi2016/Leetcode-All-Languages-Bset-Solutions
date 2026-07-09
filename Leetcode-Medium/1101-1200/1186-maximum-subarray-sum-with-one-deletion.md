# 1186. Maximum Subarray Sum with One Deletion

## Cpp

```cpp
class Solution {
public:
    int maximumSum(vector<int>& arr) {
        int n = arr.size();
        if (n == 1) return arr[0];
        vector<int> forward(n), backward(n);
        forward[0] = arr[0];
        for (int i = 1; i < n; ++i)
            forward[i] = max(arr[i], forward[i - 1] + arr[i]);
        backward[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; --i)
            backward[i] = max(arr[i], backward[i + 1] + arr[i]);
        int ans = *max_element(forward.begin(), forward.end());
        for (int i = 1; i < n - 1; ++i)
            ans = max(ans, forward[i - 1] + backward[i + 1]); // delete arr[i]
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumSum(int[] arr) {
        int n = arr.length;
        if (n == 1) return arr[0];
        
        int[] left = new int[n];   // max subarray sum ending at i
        int[] right = new int[n];  // max subarray sum starting at i
        
        left[0] = arr[0];
        int ans = arr[0];
        for (int i = 1; i < n; i++) {
            left[i] = Math.max(arr[i], left[i - 1] + arr[i]);
            ans = Math.max(ans, left[i]); // no deletion case
        }
        
        right[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            right[i] = Math.max(arr[i], right[i + 1] + arr[i]);
        }
        
        // delete first or last element
        ans = Math.max(ans, right[1]);      // delete arr[0]
        ans = Math.max(ans, left[n - 2]);   // delete arr[n-1]
        
        // delete middle element
        for (int i = 1; i < n - 1; i++) {
            ans = Math.max(ans, left[i - 1] + right[i + 1]);
        }
        
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return arr[0]

        # forward[i]: max subarray sum ending at i (no deletion)
        forward = [0] * n
        cur = arr[0]
        forward[0] = cur
        for i in range(1, n):
            cur = max(arr[i], cur + arr[i])
            forward[i] = cur

        # backward[i]: max subarray sum starting at i (no deletion)
        backward = [0] * n
        cur = arr[-1]
        backward[-1] = cur
        for i in range(n - 2, -1, -1):
            cur = max(arr[i], cur + arr[i])
            backward[i] = cur

        ans = max(forward)  # case without any deletion
        for i in range(1, n - 1):
            ans = max(ans, forward[i - 1] + backward[i + 1])  # delete arr[i]

        return ans
```

## Python3

```python
class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        left = [0] * n
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i - 1] + arr[i], arr[i])
        right = [0] * n
        right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1] + arr[i], arr[i])
        ans = max(arr)
        for i in range(1, n - 1):
            ans = max(ans, left[i - 1] + right[i + 1])
        return ans
```

## C

```c
#include <stdlib.h>

int maximumSum(int* arr, int arrSize) {
    if (arrSize == 0) return 0;
    
    int *forward = (int *)malloc(sizeof(int) * arrSize);
    int *backward = (int *)malloc(sizeof(int) * arrSize);
    
    forward[0] = arr[0];
    int ans = arr[0];
    for (int i = 1; i < arrSize; ++i) {
        int without = forward[i - 1] + arr[i];
        forward[i] = arr[i] > without ? arr[i] : without;
        if (forward[i] > ans) ans = forward[i];
    }
    
    backward[arrSize - 1] = arr[arrSize - 1];
    for (int i = arrSize - 2; i >= 0; --i) {
        int without = backward[i + 1] + arr[i];
        backward[i] = arr[i] > without ? arr[i] : without;
    }
    
    for (int i = 1; i < arrSize - 1; ++i) {
        int combined = forward[i - 1] + backward[i + 1];
        if (combined > ans) ans = combined;
    }
    
    free(forward);
    free(backward);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumSum(int[] arr) {
        int n = arr.Length;
        int[] forward = new int[n];
        forward[0] = arr[0];
        int maxAns = arr[0];
        for (int i = 1; i < n; i++) {
            forward[i] = Math.Max(arr[i], forward[i - 1] + arr[i]);
            if (forward[i] > maxAns) maxAns = forward[i];
        }
        int[] backward = new int[n];
        backward[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            backward[i] = Math.Max(arr[i], backward[i + 1] + arr[i]);
        }
        for (int i = 1; i < n - 1; i++) {
            int combined = forward[i - 1] + backward[i + 1];
            if (combined > maxAns) maxAns = combined;
        }
        return maxAns;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumSum = function(arr) {
    const n = arr.length;
    if (n === 1) return arr[0];
    
    const forward = new Array(n);
    const backward = new Array(n);
    
    forward[0] = arr[0];
    let ans = arr[0];
    for (let i = 1; i < n; i++) {
        forward[i] = Math.max(arr[i], forward[i - 1] + arr[i]);
        if (forward[i] > ans) ans = forward[i];
    }
    
    backward[n - 1] = arr[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        backward[i] = Math.max(arr[i], backward[i + 1] + arr[i]);
    }
    
    for (let i = 1; i < n - 1; i++) {
        const sum = forward[i - 1] + backward[i + 1];
        if (sum > ans) ans = sum;
    }
    
    return ans;
};
```

## Typescript

```typescript
function maximumSum(arr: number[]): number {
    const n = arr.length;
    if (n === 1) return arr[0];

    const fwd = new Array<number>(n);
    fwd[0] = arr[0];
    let bestNoDel = arr[0];
    for (let i = 1; i < n; i++) {
        fwd[i] = Math.max(arr[i], fwd[i - 1] + arr[i]);
        if (fwd[i] > bestNoDel) bestNoDel = fwd[i];
    }

    const bwd = new Array<number>(n);
    bwd[n - 1] = arr[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        bwd[i] = Math.max(arr[i], bwd[i + 1] + arr[i]);
    }

    let ans = bestNoDel;
    for (let i = 1; i < n - 1; i++) {
        const sumWithDeletion = fwd[i - 1] + bwd[i + 1];
        if (sumWithDeletion > ans) ans = sumWithDeletion;
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maximumSum($arr) {
        $n = count($arr);
        if ($n == 0) return 0;
        $forward = [];
        $backward = [];

        $forward[0] = $arr[0];
        for ($i = 1; $i < $n; $i++) {
            $forward[$i] = max($arr[$i], $forward[$i - 1] + $arr[$i]);
        }

        $backward[$n - 1] = $arr[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            $backward[$i] = max($arr[$i], $backward[$i + 1] + $arr[$i]);
        }

        $ans = $arr[0];
        for ($i = 0; $i < $n; $i++) {
            if ($forward[$i] > $ans) $ans = $forward[$i];
        }

        for ($i = 1; $i < $n - 1; $i++) {
            $candidate = $forward[$i - 1] + $backward[$i + 1];
            if ($candidate > $ans) $ans = $candidate;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSum(_ arr: [Int]) -> Int {
        let n = arr.count
        var left = Array(repeating: 0, count: n)
        var right = Array(repeating: 0, count: n)

        left[0] = arr[0]
        var ans = arr[0]

        if n > 1 {
            for i in 1..<n {
                left[i] = max(arr[i], left[i - 1] + arr[i])
                ans = max(ans, left[i])   // no deletion
            }

            right[n - 1] = arr[n - 1]
            for i in stride(from: n - 2, through: 0, by: -1) {
                right[i] = max(arr[i], right[i + 1] + arr[i])
            }

            if n >= 3 {
                for i in 1..<(n - 1) {
                    ans = max(ans, left[i - 1] + right[i + 1]) // delete arr[i]
                }
            }
        }

        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSum(arr: IntArray): Int {
        val n = arr.size
        if (n == 1) return arr[0]

        val forward = IntArray(n)
        forward[0] = arr[0]
        for (i in 1 until n) {
            forward[i] = maxOf(arr[i], forward[i - 1] + arr[i])
        }

        val backward = IntArray(n)
        backward[n - 1] = arr[n - 1]
        for (i in n - 2 downTo 0) {
            backward[i] = maxOf(arr[i], backward[i + 1] + arr[i])
        }

        var ans = forward[0]
        for (v in forward) if (v > ans) ans = v

        for (i in 1 until n - 1) {
            val candidate = forward[i - 1] + backward[i + 1]
            if (candidate > ans) ans = candidate
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumSum(List<int> arr) {
    int n = arr.length;
    if (n == 0) return 0;
    List<int> left = List.filled(n, 0);
    List<int> right = List.filled(n, 0);

    left[0] = arr[0];
    for (int i = 1; i < n; i++) {
      int extend = left[i - 1] + arr[i];
      left[i] = extend > arr[i] ? extend : arr[i];
    }

    right[n - 1] = arr[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      int extend = right[i + 1] + arr[i];
      right[i] = extend > arr[i] ? extend : arr[i];
    }

    int ans = arr[0];
    for (int i = 0; i < n; i++) {
      if (left[i] > ans) ans = left[i];
    }

    for (int i = 1; i < n - 1; i++) {
      int combined = left[i - 1] + right[i + 1];
      if (combined > ans) ans = combined;
    }

    return ans;
  }
}
```

## Golang

```go
func maximumSum(arr []int) int {
    n := len(arr)
    if n == 0 {
        return 0
    }
    // forward[i]: max subarray sum ending at i without deletion
    fwd := make([]int, n)
    cur := arr[0]
    fwd[0] = cur
    ans := cur
    for i := 1; i < n; i++ {
        if cur > 0 {
            cur += arr[i]
        } else {
            cur = arr[i]
        }
        fwd[i] = cur
        if cur > ans {
            ans = cur
        }
    }

    // backward[i]: max subarray sum starting at i without deletion
    bwd := make([]int, n)
    cur = arr[n-1]
    bwd[n-1] = cur
    for i := n - 2; i >= 0; i-- {
        if cur > 0 {
            cur += arr[i]
        } else {
            cur = arr[i]
        }
        bwd[i] = cur
    }

    // consider deleting each element (except first and last)
    for i := 1; i < n-1; i++ {
        sum := fwd[i-1] + bwd[i+1]
        if sum > ans {
            ans = sum
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_sum(arr)
  n = arr.length
  return arr[0] if n == 1

  fwd = Array.new(n)
  bwd = Array.new(n)

  cur = arr[0]
  fwd[0] = cur
  (1...n).each do |i|
    cur = [arr[i], cur + arr[i]].max
    fwd[i] = cur
  end

  cur = arr[-1]
  bwd[n - 1] = cur
  (n - 2).downto(0) do |i|
    cur = [arr[i], cur + arr[i]].max
    bwd[i] = cur
  end

  ans = arr.max
  fwd.each { |v| ans = v if v > ans }

  (1...n - 1).each do |i|
    combined = fwd[i - 1] + bwd[i + 1]
    ans = combined if combined > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumSum(arr: Array[Int]): Int = {
        val n = arr.length
        if (n == 1) return arr(0)

        val forward = new Array[Int](n)
        val backward = new Array[Int](n)

        forward(0) = arr(0)
        for (i <- 1 until n) {
            forward(i) = math.max(arr(i), forward(i - 1) + arr(i))
        }

        backward(n - 1) = arr(n - 1)
        var i = n - 2
        while (i >= 0) {
            backward(i) = math.max(arr(i), backward(i + 1) + arr(i))
            i -= 1
        }

        var ans = forward.max // no deletion case

        for (j <- 1 until n - 1) {
            val candidate = forward(j - 1) + backward(j + 1)
            if (candidate > ans) ans = candidate
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_sum(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n == 0 {
            return 0;
        }
        if n == 1 {
            return arr[0];
        }

        // fwd[i]: max subarray sum ending at i (no deletion)
        let mut fwd = vec![0i32; n];
        fwd[0] = arr[0];
        for i in 1..n {
            fwd[i] = std::cmp::max(arr[i], fwd[i - 1] + arr[i]);
        }

        // bwd[i]: max subarray sum starting at i (no deletion)
        let mut bwd = vec![0i32; n];
        bwd[n - 1] = arr[n - 1];
        for i in (0..n - 1).rev() {
            bwd[i] = std::cmp::max(arr[i], bwd[i + 1] + arr[i]);
        }

        // answer without any deletion
        let mut ans = *fwd.iter().max().unwrap();

        // consider deleting one element at position i (1..n-2)
        for i in 1..n - 1 {
            let cand = fwd[i - 1] + bwd[i + 1];
            if cand > ans {
                ans = cand;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-sum arr)
  (-> (listof exact-integer?) exact-integer?)
  (let ((n (length arr)))
    (cond
      [(= n 0) 0]                         ; not expected per constraints
      [(= n 1) (car arr)]
      [else
       (let* ((v   (list->vector arr))
              (fwd (make-vector n))
              (bwd (make-vector n)))
         ;; forward DP: max subarray sum ending at each position
         (vector-set! fwd 0 (vector-ref v 0))
         (let ((max-no-del (vector-ref v 0)))
           (for ([i (in-range 1 n)])
             (let* ((cur  (vector-ref v i))
                    (prev (vector-ref fwd (- i 1)))
                    (best (max cur (+ prev cur))))
               (vector-set! fwd i best)
               (when (> best max-no-del) (set! max-no-del best))))
           ;; backward DP: max subarray sum starting at each position
           (vector-set! bwd (- n 1) (vector-ref v (- n 1)))
           (for ([i (in-range (- n 2) -1 -1)])
             (let* ((cur  (vector-ref v i))
                    (next (vector-ref bwd (+ i 1)))
                    (best (max cur (+ next cur))))
               (vector-set! bwd i best)))
           ;; evaluate deletions
           (let ((ans max-no-del))
             (for ([i (in-range n)])
               (cond
                 [(= i 0)
                  (let ((cand (vector-ref bwd 1)))
                    (when (> cand ans) (set! ans cand)))]
                 [(= i (- n 1))
                  (let ((cand (vector-ref fwd (- n 2))))
                    (when (> cand ans) (set! ans cand)))]
                 [else
                  (let ((cand (+ (vector-ref fwd (- i 1))
                                 (vector-ref bwd (+ i 1)))))
                    (when (> cand ans) (set! ans cand)))]))
             ans))))])))
```

## Erlang

```erlang
-module(solution).
-export([maximum_sum/1]).

-define(NEG_INF, -1000000000).

maximum_sum(Arr) ->
    N = length(Arr),
    case N of
        0 -> 0;
        1 -> hd(Arr);
        _ ->
            F = forward(Arr),
            B = backward(Arr),

            MaxNoDel = lists:max(F),

            EdgeFirst = case B of
                [_|[Second|_]] -> Second;
                _ -> ?NEG_INF
            end,
            EdgeLast = case lists:nthtail(N-1, F) of
                [LastPrev|_] -> LastPrev;
                [] -> ?NEG_INF
            end,

            MiddleMax = if N > 2 ->
                    PrefixF = lists:sublist(F, N - 2),
                    SuffixB = lists:nthtail(2, B),
                    zip_max_sum(PrefixF, SuffixB, ?NEG_INF);
                true -> ?NEG_INF
            end,

            MaxDel = max(EdgeFirst, max(EdgeLast, MiddleMax)),
            max(MaxNoDel, MaxDel)
    end.

forward(List) ->
    forward(List, undefined, []).

forward([], _Prev, Acc) ->
    lists:reverse(Acc);
forward([X|Xs], undefined, Acc) ->
    forward(Xs, X, [X|Acc]);
forward([X|Xs], Prev, Acc) ->
    Curr = max(X, Prev + X),
    forward(Xs, Curr, [Curr|Acc]).

backward(List) ->
    Rev = lists:reverse(List),
    RevF = forward(Rev),
    lists:reverse(RevF).

zip_max_sum([], [], Max) -> Max;
zip_max_sum([A|As], [B|Bs], Max) ->
    NewMax = max(Max, A + B),
    zip_max_sum(As, Bs, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_sum(arr :: [integer]) :: integer
  def maximum_sum(arr) do
    n = length(arr)

    case n do
      0 -> 0
      1 -> hd(arr)
      _ ->
        arr_t = List.to_tuple(arr)

        # max subarray sum ending at each position (no deletion)
        left_rev =
          Enum.reduce(0..(n - 1), [], fn i, acc ->
            val = elem(arr_t, i)

            if i == 0 do
              [val | acc]
            else
              prev = hd(acc)               # dp for i‑1 (list is reversed)
              cur = max(val, prev + val)
              [cur | acc]
            end
          end)

        left_dp = List.to_tuple(Enum.reverse(left_rev))

        # max subarray sum starting at each position (no deletion)
        right_rev =
          Enum.reduce(0..(n - 1), [], fn i, acc ->
            idx = n - 1 - i
            val = elem(arr_t, idx)

            if i == 0 do
              [val | acc]
            else
              prev = hd(acc)               # dp for idx+1
              cur = max(val, prev + val)
              [cur | acc]
            end
          end)

        right_dp = List.to_tuple(Enum.reverse(right_rev))

        max_no_del = Enum.max(Tuple.to_list(left_dp))

        ans =
          if n > 2 do
            Enum.reduce(1..(n - 2), max_no_del, fn i, acc ->
              cand = elem(left_dp, i - 1) + elem(right_dp, i + 1)
              if cand > acc, do: cand, else: acc
            end)
          else
            max_no_del
          end

        ans
    end
  end
end
```
