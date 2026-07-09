# 1696. Jump Game VI

## Cpp

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> dp(n);
        dp[0] = nums[0];
        deque<int> dq;
        dq.push_back(0);
        for (int i = 1; i < n; ++i) {
            while (!dq.empty() && dq.front() < i - k) dq.pop_front();
            dp[i] = nums[i] + dp[dq.front()];
            while (!dq.empty() && dp[dq.back()] <= dp[i]) dq.pop_back();
            dq.push_back(i);
        }
        return (int)dp[n - 1];
    }
};
```

## Java

```java
class Solution {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        long[] dp = new long[n];
        dp[0] = nums[0];
        java.util.Deque<Integer> deque = new java.util.ArrayDeque<>();
        deque.addLast(0);
        for (int i = 1; i < n; i++) {
            while (!deque.isEmpty() && deque.peekFirst() < i - k) {
                deque.pollFirst();
            }
            dp[i] = nums[i] + dp[deque.peekFirst()];
            while (!deque.isEmpty() && dp[deque.peekLast()] <= dp[i]) {
                deque.pollLast();
            }
            deque.addLast(i);
        }
        return (int) dp[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        from collections import deque
        dq = deque([0])  # store indices with decreasing dp values

        for i in range(1, n):
            # remove out-of-window indices
            while dq and dq[0] < i - k:
                dq.popleft()
            # best previous dp
            best = dp[dq[0]]
            dp[i] = nums[i] + best
            # maintain decreasing order in deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return dp[-1]
```

## Python3

```python
class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        from collections import deque
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque([0])  # stores indices with decreasing dp values
        for i in range(1, n):
            # remove out-of-window indices
            while dq and dq[0] < i - k:
                dq.popleft()
            # best previous score
            dp[i] = nums[i] + dp[dq[0]]
            # maintain monotonic decreasing order
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
        return dp[-1]
```

## C

```c
int maxResult(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    long *dp = (long *)malloc(numsSize * sizeof(long));
    int *deq = (int *)malloc(numsSize * sizeof(int));
    int head = 0, tail = 0; // deq[head..tail-1] holds indices
    
    dp[0] = nums[0];
    deq[tail++] = 0;
    
    for (int i = 1; i < numsSize; ++i) {
        while (head < tail && deq[head] < i - k) {
            ++head;
        }
        long bestPrev = dp[deq[head]];
        dp[i] = nums[i] + bestPrev;
        
        while (head < tail && dp[deq[tail - 1]] <= dp[i]) {
            --tail;
        }
        deq[tail++] = i;
    }
    
    int ans = (int)dp[numsSize - 1];
    free(dp);
    free(deq);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxResult(int[] nums, int k) {
        int n = nums.Length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        var deque = new LinkedList<int>();
        deque.AddLast(0);
        for (int i = 1; i < n; i++) {
            // Remove indices out of the window
            while (deque.First != null && deque.First.Value < i - k) {
                deque.RemoveFirst();
            }
            dp[i] = nums[i] + dp[deque.First.Value];
            // Maintain decreasing order of dp values in deque
            while (deque.Last != null && dp[deque.Last.Value] <= dp[i]) {
                deque.RemoveLast();
            }
            deque.AddLast(i);
        }
        return dp[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxResult = function(nums, k) {
    const n = nums.length;
    if (n === 0) return 0;
    const dp = new Array(n);
    dp[0] = nums[0];

    // deque implemented with a circular buffer using indices
    const deq = new Array(n);
    let front = 0, back = -1; // empty when front > back

    // initialize deque with index 0
    deq[++back] = 0;

    for (let i = 1; i < n; ++i) {
        // remove indices out of the window [i-k, i-1]
        while (front <= back && deq[front] < i - k) {
            front++;
        }

        // the max dp within window is at deq[front]
        dp[i] = nums[i] + dp[deq[front]];

        // maintain decreasing order of dp values in deque
        while (front <= back && dp[deq[back]] <= dp[i]) {
            back--;
        }
        deq[++back] = i;
    }

    return dp[n - 1];
};
```

## Typescript

```typescript
function maxResult(nums: number[], k: number): number {
    const n = nums.length;
    const dp = new Array<number>(n);
    dp[0] = nums[0];
    const deque: number[] = [0]; // store indices with decreasing dp values
    let front = 0;

    for (let i = 1; i < n; ++i) {
        while (front < deque.length && deque[front] < i - k) {
            front++;
        }
        const bestIdx = deque[front];
        dp[i] = nums[i] + dp[bestIdx];

        while (deque.length > front && dp[deque[deque.length - 1]] <= dp[i]) {
            deque.pop();
        }
        deque.push(i);
    }

    return dp[n - 1];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxResult($nums, $k) {
        $n = count($nums);
        $dp = array_fill(0, $n, 0);
        $dp[0] = $nums[0];
        $deque = new SplDoublyLinkedList();
        $deque->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
        $deque->push(0);
        for ($i = 1; $i < $n; ++$i) {
            while (!$deque->isEmpty() && $deque->bottom() < $i - $k) {
                $deque->shift();
            }
            $bestIdx = $deque->bottom();
            $dp[$i] = $nums[$i] + $dp[$bestIdx];
            while (!$deque->isEmpty() && $dp[$i] >= $dp[$deque->top()]) {
                $deque->pop();
            }
            $deque->push($i);
        }
        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maxResult(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var dp = Array(repeating: 0, count: n)
        dp[0] = nums[0]
        var deque = [Int]()
        var head = 0
        deque.append(0)

        for i in 1..<n {
            while head < deque.count && i - deque[head] > k {
                head += 1
            }
            let bestIdx = deque[head]
            dp[i] = nums[i] + dp[bestIdx]

            while deque.count > head && dp[i] >= dp[deque.last!] {
                deque.removeLast()
            }
            deque.append(i)
        }

        return dp[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxResult(nums: IntArray, k: Int): Int {
        val n = nums.size
        val dp = IntArray(n)
        dp[0] = nums[0]
        val deque = java.util.ArrayDeque<Int>()
        deque.addLast(0)

        for (i in 1 until n) {
            while (!deque.isEmpty() && deque.peekFirst() < i - k) {
                deque.pollFirst()
            }
            dp[i] = nums[i] + dp[deque.peekFirst()]
            while (!deque.isEmpty() && dp[deque.peekLast()] <= dp[i]) {
                deque.pollLast()
            }
            deque.addLast(i)
        }

        return dp[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int maxResult(List<int> nums, int k) {
    int n = nums.length;
    if (n == 0) return 0;
    List<int> dp = List.filled(n, 0);
    dp[0] = nums[0];
    final heap = _MaxHeap();
    heap.push(_Item(dp[0], 0));

    for (int i = 1; i < n; ++i) {
      while (!heap.isEmpty && heap.top.idx < i - k) {
        heap.pop();
      }
      int best = heap.top.val;
      dp[i] = nums[i] + best;
      heap.push(_Item(dp[i], i));
    }
    return dp[n - 1];
  }
}

class _Item {
  final int val;
  final int idx;
  _Item(this.val, this.idx);
}

class _MaxHeap {
  final List<_Item> _data = [];

  bool get isEmpty => _data.isEmpty;

  _Item get top => _data[0];

  void push(_Item item) {
    _data.add(item);
    _siftUp(_data.length - 1);
  }

  void pop() {
    int last = _data.length - 1;
    if (last == 0) {
      _data.removeLast();
      return;
    }
    _swap(0, last);
    _data.removeLast();
    _siftDown(0);
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_data[parent].val >= _data[idx].val) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int largest = idx;

      if (left < n && _data[left].val > _data[largest].val) {
        largest = left;
      }
      if (right < n && _data[right].val > _data[largest].val) {
        largest = right;
      }
      if (largest == idx) break;
      _swap(idx, largest);
      idx = largest;
    }
  }

  void _swap(int i, int j) {
    final temp = _data[i];
    _data[i] = _data[j];
    _data[j] = temp;
  }
}
```

## Golang

```go
func maxResult(nums []int, k int) int {
    n := len(nums)
    dp := make([]int, n)
    dp[0] = nums[0]

    // deque will store indices of dp in decreasing order of dp value
    deque := make([]int, 0, n)
    deque = append(deque, 0)

    for i := 1; i < n; i++ {
        // Remove indices that are out of the window [i-k, i-1]
        for len(deque) > 0 && deque[0] < i-k {
            deque = deque[1:]
        }

        // The front of deque has the max dp value within the window
        dp[i] = nums[i] + dp[deque[0]]

        // Maintain decreasing order: remove from back while current dp is >= dp at back
        for len(deque) > 0 && dp[i] >= dp[deque[len(deque)-1]] {
            deque = deque[:len(deque)-1]
        }
        deque = append(deque, i)
    }

    return dp[n-1]
}
```

## Ruby

```ruby
def max_result(nums, k)
  n = nums.length
  dp = Array.new(n, 0)
  dp[0] = nums[0]

  deque = [0]   # store indices with decreasing dp values
  head = 0

  (1...n).each do |i|
    # Remove indices out of the window [i-k, i-1]
    while head < deque.length && deque[head] < i - k
      head += 1
    end

    best_idx = deque[head]
    dp[i] = nums[i] + dp[best_idx]

    # Maintain decreasing order of dp values in the deque
    while head < deque.length && dp[i] >= dp[deque[-1]]
      deque.pop
    end
    deque << i
  end

  dp[-1]
end
```

## Scala

```scala
object Solution {
  def maxResult(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val dp = new Array[Int](n)
    dp(0) = nums(0)

    import scala.collection.mutable.PriorityQueue
    implicit val ord: Ordering[(Int, Int)] = Ordering.by[(Int, Int), Int](_._1)
    val pq = PriorityQueue.empty[(Int, Int)]
    pq.enqueue((dp(0), 0))

    var i = 1
    while (i < n) {
      while (pq.nonEmpty && pq.head._2 < i - k) {
        pq.dequeue()
      }
      val best = pq.head._1
      dp(i) = nums(i) + best
      pq.enqueue((dp(i), i))
      i += 1
    }

    dp(n - 1)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_result(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::VecDeque;
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut dp = vec![0i64; n];
        dp[0] = nums[0] as i64;
        let mut deque: VecDeque<usize> = VecDeque::new();
        deque.push_back(0);
        let k_usize = k as usize;

        for i in 1..n {
            // Remove indices that are out of the window [i - k, i-1]
            while let Some(&front) = deque.front() {
                if front + k_usize < i {
                    deque.pop_front();
                } else {
                    break;
                }
            }

            // The best previous dp is at the front
            let best = dp[*deque.front().unwrap()];
            dp[i] = nums[i] as i64 + best;

            // Maintain decreasing order of dp values in the deque
            while let Some(&back) = deque.back() {
                if dp[back] <= dp[i] {
                    deque.pop_back();
                } else {
                    break;
                }
            }
            deque.push_back(i);
        }

        dp[n - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (max-result nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (dp (make-vector n 0))
         (deque (make-vector n 0)))
    (define head 0)
    (define tail 0)
    ;; initialize dp[0] and deque with index 0
    (vector-set! dp 0 (vector-ref arr 0))
    (vector-set! deque tail 0)
    (set! tail (+ tail 1))
    (for ([i (in-range 1 n)])
      ;; discard indices that are out of the window [i-k, i-1]
      (let loop-out ()
        (when (and (< head tail)
                   (< (vector-ref deque head) (- i k)))
          (set! head (+ head 1))
          (loop-out)))
      ;; best previous index is at the front of deque
      (let ((best (vector-ref deque head)))
        (vector-set! dp i (+ (vector-ref arr i) (vector-ref dp best))))
      ;; maintain deque in decreasing order of dp values
      (let loop-in ()
        (when (and (> tail head)
                   (>= (vector-ref dp i)
                       (vector-ref dp (vector-ref deque (- tail 1)))))
          (set! tail (- tail 1))
          (loop-in)))
      (vector-set! deque tail i)
      (set! tail (+ tail 1)))
    (vector-ref dp (- n 1))))
```

## Erlang

```erlang
-spec max_result(Nums :: [integer()], K :: integer()) -> integer().
max_result(Nums, K) ->
    case Nums of
        [] -> 0;
        [First | Rest] ->
            DP0 = First,
            Deq0 = :queue.in({0, DP0}, :queue.new()),
            loop(Rest, 1, K, DP0, Deq0)
    end.

loop([], _Idx, _K, DPPrev, _Deq) ->
    DPPrev;
loop([Num | Rest], Idx, K, _, DeqPrev) ->
    Deq1 = remove_out_of_window(DeqPrev, Idx, K),
    {_, MaxDP} = get_front(Deq1),
    DP = Num + MaxDP,
    Deq2 = insert_monotonic(Deq1, {Idx, DP}),
    loop(Rest, Idx + 1, K, DP, Deq2).

remove_out_of_window(Q, Idx, K) ->
    case :queue.peek(Q) of
        empty -> Q;
        {FrontIdx, _} when FrontIdx < Idx - K ->
            {_Removed, Q1} = :queue.out(Q),
            remove_out_of_window(Q1, Idx, K);
        _ -> Q
    end.

get_front(Q) ->
    case :queue.peek(Q) of
        empty -> {0, 0};
        Value -> Value
    end.

insert_monotonic(Q, Elem = {_Idx, DP}) ->
    case :queue.peek_r(Q) of
        empty -> :queue.in(Elem, Q);
        {_LastIdx, LastDP} when LastDP =< DP ->
            {_Removed, Q1} = :queue.out_r(Q),
            insert_monotonic(Q1, Elem);
        _ -> :queue.in_r(Elem, Q)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_result(nums :: [integer], k :: integer) :: integer
  def max_result(nums, k) do
    n = length(nums)
    nums_t = List.to_tuple(nums)

    dp0 = elem(nums_t, 0)
    dq0 = Deque.new() |> Deque.push_back({0, dp0})

    {final_dp, _} =
      Enum.reduce(1..(n - 1), {dp0, dq0}, fn i, {_prev_dp, dq} ->
        dq1 = clean_front(dq, i, k)

        max_prev =
          case Deque.peek_front(dq1) do
            nil -> 0
            {_idx, val} -> val
          end

        dpi = elem(nums_t, i) + max_prev
        dq2 = clean_back(dq1, dpi)
        dq3 = Deque.push_back(dq2, {i, dpi})
        {dpi, dq3}
      end)

    final_dp
  end

  defp clean_front(dq, i, k) do
    case Deque.peek_front(dq) do
      nil ->
        dq

      {idx, _val} = pair when idx < i - k ->
        {_removed, new_dq} = Deque.pop_front(dq)
        clean_front(new_dq, i, k)

      _ ->
        dq
    end
  end

  defp clean_back(dq, dpi) do
    case Deque.peek_back(dq) do
      nil ->
        dq

      {_idx, val} = pair when val <= dpi ->
        new_dq = Deque.pop_back(dq)
        clean_back(new_dq, dpi)

      _ ->
        dq
    end
  end

  defmodule Deque do
    defstruct front: [], back: []

    @spec new() :: %Deque{}
    def new(), do: %Deque{}

    @spec push_back(%Deque{}, any) :: %Deque{}
    def push_back(%Deque{front: f, back: b} = dq, elem), do: %{dq | back: [elem | b]}

    @spec peek_front(%Deque{}) :: any | nil
    def peek_front(%Deque{front: [h | _], back: _}), do: h

    def peek_front(%Deque{front: [], back: []}), do: nil

    def peek_front(%Deque{front: [], back: b}) do
      case Enum.reverse(b) do
        [h | _] -> h
        [] -> nil
      end
    end

    @spec pop_front(%Deque{}) :: {any, %Deque{}}
    def pop_front(%Deque{front: [h | t], back: b} = dq), do: {h, %{dq | front: t, back: b}}

    def pop_front(%Deque{front: [], back: b}) when b != [] do
      rev = Enum.reverse(b)

      case rev do
        [h | t] -> {h, %Deque{front: t, back: []}}
        [] -> {nil, %Deque{}}
      end
    end

    @spec peek_back(%Deque{}) :: any | nil
    def peek_back(%Deque{back: [h | _]}), do: h
    def peek_back(%Deque{front: [], back: []}), do: nil

    def peek_back(%Deque{back: [], front: f}) do
      case Enum.reverse(f) do
        [h | _] -> h
        [] -> nil
      end
    end

    @spec pop_back(%Deque{}) :: %Deque{}
    def pop_back(%Deque{back: [_h | t]} = dq), do: %{dq | back: t}

    def pop_back(%Deque{back: [], front: f}) when f != [] do
      rev = Enum.reverse(f)

      case rev do
        [_h | t] -> %Deque{front: [], back: Enum.reverse(t)}
        [] -> %Deque{}
      end
    end

    @spec empty?(%Deque{}) :: boolean
    def empty?(%Deque{front: [], back: []}), do: true
    def empty?(_), do: false
  end
end
```
