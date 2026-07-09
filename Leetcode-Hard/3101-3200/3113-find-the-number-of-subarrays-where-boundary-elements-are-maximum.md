# 3113. Find the Number of Subarrays Where Boundary Elements Are Maximum

## Cpp

```cpp
class Solution {
public:
    long long numberOfSubarrays(std::vector<int>& nums) {
        int n = nums.size();
        std::stack<int> st; // indices with decreasing values
        std::unordered_map<long long, std::vector<int>> pos;
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] <= nums[i]) st.pop();
            int p = st.empty() ? -1 : st.top(); // previous greater element index
            auto &vec = pos[nums[i]];
            // count previous occurrences of the same value after index p
            int cntPrev = std::lower_bound(vec.begin(), vec.end(), p + 1) - vec.begin();
            long long total = (long long)(vec.size() - cntPrev) + 1; // include current i
            ans += total;
            vec.push_back(i);
            st.push(i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long numberOfSubarrays(int[] nums) {
        int n = nums.length;
        Deque<Integer> stack = new ArrayDeque<>();
        java.util.HashMap<Integer, Deque<Integer>> map = new java.util.HashMap<>();
        long ans = 0L;
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }
            int left = stack.isEmpty() ? -1 : stack.peek();
            Deque<Integer> dq = map.computeIfAbsent(nums[i], k -> new ArrayDeque<>());
            while (!dq.isEmpty() && dq.peekFirst() <= left) {
                dq.pollFirst();
            }
            ans += (long) dq.size() + 1L;
            dq.addLast(i);
            stack.push(i);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        from collections import defaultdict
        import bisect

        occ = defaultdict(list)
        ans = 0
        for i, v in enumerate(nums):
            lst = occ[v]
            idx = bisect.bisect_right(lst, left[i])
            cnt_prev = len(lst) - idx
            ans += cnt_prev + 1  # include subarray [i,i]
            lst.append(i)
        return ans
```

## Python3

```python
from bisect import bisect_left
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        prev_smaller = [-1] * n
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] >= v:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        pos_dict = {}
        ans = 0
        for i, v in enumerate(nums):
            lst = pos_dict.get(v)
            if lst is None:
                cnt_prev = 0
                lst = []
                pos_dict[v] = lst
            else:
                left = bisect_left(lst, prev_smaller[i] + 1)
                cnt_prev = len(lst) - left
            ans += cnt_prev + 1
            lst.append(i)

        return ans
```

## C

```c
#include <stdlib.h>
#include "uthash.h"

typedef struct {
    int key;                // value of nums[i]
    int *pos;               // dynamic array of positions where this value occurs
    int size;
    int cap;
    UT_hash_handle hh;
} Entry;

static void add_position(Entry **map, int val, int idx) {
    Entry *e = NULL;
    HASH_FIND_INT(*map, &val, e);
    if (!e) {
        e = (Entry *)malloc(sizeof(Entry));
        e->key = val;
        e->size = 0;
        e->cap = 4;
        e->pos = (int *)malloc(e->cap * sizeof(int));
        HASH_ADD_INT(*map, key, e);
    }
    if (e->size == e->cap) {
        e->cap <<= 1;
        e->pos = (int *)realloc(e->pos, e->cap * sizeof(int));
    }
    e->pos[e->size++] = idx;
}

static int lower_bound(int *a, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = (l + r) >> 1;
        if (a[m] >= target) r = m;
        else l = m + 1;
    }
    return l;
}

static int upper_bound(int *a, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = (l + r) >> 1;
        if (a[m] > target) r = m;
        else l = m + 1;
    }
    return l;
}

long long numberOfSubarrays(int* nums, int numsSize) {
    // Build map from value to list of positions
    Entry *map = NULL;
    for (int i = 0; i < numsSize; ++i) {
        add_position(&map, nums[i], i);
    }

    // Compute previous greater element for each index
    int *prevGreater = (int *)malloc(numsSize * sizeof(int));
    int *stack = (int *)malloc(numsSize * sizeof(int));
    int top = -1;
    for (int i = 0; i < numsSize; ++i) {
        while (top >= 0 && nums[stack[top]] <= nums[i]) top--;
        prevGreater[i] = (top == -1) ? -1 : stack[top];
        stack[++top] = i;
    }
    free(stack);

    long long ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        Entry *e = NULL;
        int key = nums[i];
        HASH_FIND_INT(map, &key, e);
        // positions are stored in increasing order
        int leftIdx = lower_bound(e->pos, e->size, prevGreater[i] + 1);
        int rightIdx = upper_bound(e->pos, e->size, i);
        ans += (long long)(rightIdx - leftIdx);
    }

    // Cleanup
    free(prevGreater);
    Entry *cur, *tmp;
    HASH_ITER(hh, map, cur, tmp) {
        HASH_DEL(map, cur);
        free(cur->pos);
        free(cur);
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long NumberOfSubarrays(int[] nums) {
        int n = nums.Length;
        // Map each value to list of its positions
        var posMap = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!posMap.TryGetValue(nums[i], out var lst)) {
                lst = new List<int>();
                posMap[nums[i]] = lst;
            }
            lst.Add(i);
        }

        // Monotonic stack to find previous greater element
        var stack = new Stack<int>();
        long ans = 0;

        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack.Peek()] <= nums[i]) {
                stack.Pop();
            }
            int prevGreater = stack.Count > 0 ? stack.Peek() : -1;

            var list = posMap[nums[i]];
            int leftIdx = UpperBound(list, prevGreater); // first index > prevGreater
            int rightIdx = UpperBound(list, i);          // first index > i
            ans += (rightIdx - leftIdx);

            stack.Push(i);
        }

        return ans;
    }

    // Returns the index of the first element in 'list' that is greater than 'value'
    private int UpperBound(List<int> list, int value) {
        int lo = 0, hi = list.Count;
        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (list[mid] <= value)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfSubarrays = function(nums) {
    const n = nums.length;
    const prevGreater = new Array(n).fill(-1);
    const stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) {
            stack.pop();
        }
        prevGreater[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    const map = new Map(); // value -> {arr: [], ptr: number}
    let ans = 0;

    for (let i = 0; i < n; i++) {
        const v = nums[i];
        let entry = map.get(v);
        if (!entry) {
            entry = { arr: [], ptr: 0 };
            map.set(v, entry);
        }
        // discard indices that are not allowed
        while (entry.ptr < entry.arr.length && entry.arr[entry.ptr] <= prevGreater[i]) {
            entry.ptr++;
        }
        const cntPrevValid = entry.arr.length - entry.ptr; // prior occurrences after prevGreater
        ans += cntPrevValid + 1; // include subarray [i,i]
        entry.arr.push(i);
    }

    return ans;
};
```

## Typescript

```typescript
function numberOfSubarrays(nums: number[]): number {
    const n = nums.length;
    const prevGreater = new Array<number>(n);
    const stack: number[] = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) {
            stack.pop();
        }
        prevGreater[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    const posMap = new Map<number, number[]>();
    let ans = 0;

    for (let i = 0; i < n; i++) {
        const val = nums[i];
        const leftBound = prevGreater[i];
        const arr = posMap.get(val) || [];

        // find first index > leftBound using binary search
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] <= leftBound) l = m + 1;
            else r = m;
        }
        const cntPrev = arr.length - l; // previous same values after leftBound
        ans += 1 + cntPrev; // include subarray [i,i]

        // store current index
        if (!posMap.has(val)) posMap.set(val, [i]);
        else posMap.get(val)!.push(i);
    }

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
    function numberOfSubarrays($nums) {
        $n = count($nums);
        // previous greater element index for each position
        $prevGreater = array_fill(0, $n, -1);
        $stack = [];
        for ($i = 0; $i < $n; ++$i) {
            while (!empty($stack) && $nums[end($stack)] <= $nums[$i]) {
                array_pop($stack);
            }
            $prevGreater[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }

        // map value => list of indices where it occurs
        $pos = [];
        foreach ($nums as $idx => $val) {
            if (!isset($pos[$val])) {
                $pos[$val] = [];
            }
            $pos[$val][] = $idx;
        }

        $ptrMap = []; // value => number of occurrences processed so far
        $ans = 0;

        for ($i = 0; $i < $n; ++$i) {
            $v = $nums[$i];
            $L = $prevGreater[$i];

            $list = $pos[$v];
            // lower bound: first index in $list with value > $L
            $low = 0;
            $high = count($list);
            while ($low < $high) {
                $mid = ($low + $high) >> 1;
                if ($list[$mid] <= $L) {
                    $low = $mid + 1;
                } else {
                    $high = $mid;
                }
            }
            $lowerIdx = $low;

            $idxInList = $ptrMap[$v] ?? 0; // current occurrence index (0‑based)
            $ans += ($idxInList - $lowerIdx + 1);

            $ptrMap[$v] = $idxInList + 1;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSubarrays(_ nums: [Int]) -> Int {
        var stack = [Int]()
        var counts = [Int:Int]()
        var ans: Int64 = 0
        for x in nums {
            while let last = stack.last, last < x {
                stack.removeLast()
                counts[last] = 0
            }
            if stack.isEmpty || stack.last! > x {
                stack.append(x)
            }
            let prev = counts[x] ?? 0
            ans += Int64(prev + 1)
            counts[x] = prev + 1
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSubarrays(nums: IntArray): Long {
        val n = nums.size
        val prevSmaller = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[stack.peekLast()] >= nums[i]) {
                stack.pollLast()
            }
            prevSmaller[i] = if (stack.isEmpty()) -1 else stack.peekLast()
            stack.addLast(i)
        }

        val map = HashMap<Int, java.util.ArrayList<Int>>()
        var ans = 0L
        for (i in 0 until n) {
            val left = prevSmaller[i] + 1
            val list = map.getOrPut(nums[i]) { java.util.ArrayList() }
            // lower bound to find first index >= left
            var l = 0
            var r = list.size
            while (l < r) {
                val mid = (l + r) ushr 1
                if (list[mid] >= left) {
                    r = mid
                } else {
                    l = mid + 1
                }
            }
            val cntPrev = list.size - l
            ans += cntPrev.toLong() + 1L
            list.add(i)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSubarrays(List<int> nums) {
    int n = nums.length;
    List<int> prevGreater = List.filled(n, -1);
    List<int> stack = [];

    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && nums[stack.last] <= nums[i]) {
        stack.removeLast();
      }
      prevGreater[i] = stack.isEmpty ? -1 : stack.last;
      stack.add(i);
    }

    Map<int, List<int>> posMap = {};
    for (int i = 0; i < n; i++) {
      posMap.putIfAbsent(nums[i], () => []).add(i);
    }

    int lowerBound(List<int> arr, int target) {
      int l = 0, r = arr.length;
      while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] >= target) {
          r = m;
        } else {
          l = m + 1;
        }
      }
      return l;
    }

    int upperBound(List<int> arr, int target) {
      int l = 0, r = arr.length;
      while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] > target) {
          r = m;
        } else {
          l = m + 1;
        }
      }
      return l;
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      List<int> list = posMap[nums[i]]!;
      int left = prevGreater[i] + 1;
      int lIdx = lowerBound(list, left);
      int rIdx = upperBound(list, i);
      ans += (rIdx - lIdx);
    }
    return ans;
  }
}
```

## Golang

```go
func numberOfSubarrays(nums []int) int64 {
	n := len(nums)
	stack := make([]int, 0, n)
	posMap := make(map[int][]int)
	var ans int64

	for i, v := range nums {
		// find nearest greater element to the left
		for len(stack) > 0 && nums[stack[len(stack)-1]] <= v {
			stack = stack[:len(stack)-1]
		}
		prev := -1
		if len(stack) > 0 {
			prev = stack[len(stack)-1]
		}

		// count previous occurrences of v after prev
		positions := posMap[v]
		target := prev + 1
		lo, hi := 0, len(positions)
		for lo < hi {
			mid := (lo + hi) >> 1
			if positions[mid] >= target {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		cntPrev := len(positions) - lo // number of earlier v's in range
		ans += int64(cntPrev + 1)       // include subarray [i,i]

		// update structures
		stack = append(stack, i)
		posMap[v] = append(posMap[v], i)
	}
	return ans
}
```

## Ruby

```ruby
def number_of_subarrays(nums)
  n = nums.length
  prev_greater = Array.new(n, -1)
  stack = []

  (0...n).each do |i|
    while !stack.empty? && nums[stack[-1]] <= nums[i]
      stack.pop
    end
    prev_greater[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end

  positions = Hash.new { |h, k| h[k] = [] }
  ans = 0

  n.times do |i|
    val = nums[i]
    arr = positions[val]

    # binary search first index > prev_greater[i]
    l = 0
    r = arr.length
    target = prev_greater[i]
    while l < r
      m = (l + r) / 2
      if arr[m] <= target
        l = m + 1
      else
        r = m
      end
    end

    prior = arr.length - l   # occurrences of val after prev_greater[i]
    ans += prior + 1          # include subarray starting at i itself
    arr << i
  end

  ans
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{ArrayBuffer, HashMap}
    def numberOfSubarrays(nums: Array[Int]): Long = {
        val n = nums.length
        val prev = new Array[Int](n)
        val stack = new java.util.ArrayDeque[Int]()
        var i = 0
        while (i < n) {
            while (!stack.isEmpty && nums(stack.peek()) <= nums(i)) {
                stack.pop()
            }
            prev(i) = if (stack.isEmpty) -1 else stack.peek()
            stack.push(i)
            i += 1
        }

        val posMap = new HashMap[Int, ArrayBuffer[Int]]()
        var ans: Long = 0L
        i = 0
        while (i < n) {
            val v = nums(i)
            val buf = posMap.getOrElseUpdate(v, new ArrayBuffer[Int]())
            // binary search for first index >= prev(i)+1
            var left = 0
            var right = buf.length
            val target = prev(i) + 1
            while (left < right) {
                val mid = (left + right) >>> 1
                if (buf(mid) >= target) right = mid else left = mid + 1
            }
            val cntPrev = buf.length - left // previous positions satisfying condition
            ans += (cntPrev + 1).toLong   // include subarray consisting of only nums[i]
            buf.append(i)
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        // prev_greater[i] = index of nearest element to the left that is > nums[i], or -1
        let mut prev_greater = vec![-1i32; n];
        let mut stack: Vec<usize> = Vec::new(); // monotonic decreasing stack (values strictly decreasing)
        for i in 0..n {
            while let Some(&top) = stack.last() {
                if nums[top] <= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            prev_greater[i] = if let Some(&top) = stack.last() { top as i32 } else { -1 };
            stack.push(i);
        }

        // positions of each value
        use std::collections::HashMap;
        let mut pos_map: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            pos_map.entry(v).or_default().push(i);
        }

        // count subarrays
        let mut ans: i64 = 0;
        for i in 0..n {
            let v = nums[i];
            let pg = prev_greater[i];
            let left_bound = if pg == -1 { 0 } else { (pg as usize) + 1 };
            let positions = pos_map.get(&v).unwrap();
            // number of positions of value v in [left_bound, i]
            let l_idx = positions.partition_point(|&x| x < left_bound);
            let r_idx = positions.partition_point(|&x| x <= i);
            ans += (r_idx - l_idx) as i64;
        }
        ans
    }
}
```

## Racket

```racket
(struct pos-vec (vec len) #:mutable)

(define (pos-vec-add! pv i)
  (let* ([vec (pos-vec-vec pv)]
         [len (pos-vec-len pv)])
    (when (= len (vector-length vec))
      (let* ([new-cap (max 1 (* 2 (vector-length vec)))]
             [new-vec (make-vector new-cap)])
        (for ([j (in-range len)])
          (vector-set! new-vec j (vector-ref vec j)))
        (set-pos-vec-vec! pv new-vec)
        (set! vec new-vec)))
    (vector-set! (pos-vec-vec pv) len i)
    (set-pos-vec-len! pv (+ len 1))))

(define (pos-vec-count-from pv L)
  (let* ([vec (pos-vec-vec pv)]
         [len (pos-vec-len pv)])
    (let loop ([lo 0] [hi len])
      (if (= lo hi)
          (- len lo)
          (let* ([mid (quotient (+ lo hi) 2)]
                 [val (vector-ref vec mid)])
            (if (< val L)
                (loop (+ mid 1) hi)
                (loop lo mid)))))))

(define/contract (number-of-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [stk '()]                                   ; monotonic decreasing stack of indices
         [hash (make-hash)]                         ; value -> pos-vec of positions
         [ans 0])
    (for ([i (in-range n)])
      (define val (vector-ref arr i))
      ;; maintain strictly greater elements in stack
      (let loop ()
        (when (and (pair? stk)
                   (<= (vector-ref arr (car stk)) val))
          (set! stk (cdr stk))
          (loop)))
      (define prevGreater (if (null? stk) -1 (car stk)))
      ;; retrieve or create position vector for this value
      (define pv
        (hash-ref hash val
                  (lambda ()
                    (let ([new (pos-vec (make-vector 4) 0)])
                      (hash-set! hash val new)
                      new))))
      ;; count previous occurrences within allowed window
      (define cnt-prev (pos-vec-count-from pv (+ prevGreater 1)))
      (set! ans (+ ans (+ cnt-prev 1)))   ; include subarray consisting of only current element
      ;; record current position
      (pos-vec-add! pv i)
      ;; push current index onto stack
      (set! stk (cons i stk)))
    ans))
```

## Erlang

```erlang
-spec number_of_subarrays(Nums :: [integer()]) -> integer().
number_of_subarrays(Nums) ->
    process(0, Nums, [], #{}, 0).

process(_Idx, [], _Stack, _Map, Ans) ->
    Ans;
process(Idx, [Val | Rest], Stack, Map, Ans) ->
    {NewStack, Left} = pop_stack(Stack, Val),
    Deq0 = maps:get(Val, Map, {[], [], 0}),
    Deq1 = clean_deque(Deq0, Left),
    CountPrev = element(3, Deq1),          % number of previous same-value indices > Left
    NewAns = Ans + CountPrev,
    Deq2 = add_back(Idx, Deq1),
    NewMap = maps:put(Val, Deq2, Map),
    UpdatedStack = [{Idx, Val} | NewStack],
    process(Idx + 1, Rest, UpdatedStack, NewMap, NewAns).

pop_stack([], _Val) ->
    {[], -1};
pop_stack([{I, V} | Rest], Val) when V >= Val ->
    pop_stack(Rest, Val);
pop_stack(Stack = [{I, _V} | _Rest], _Val) ->
    {Stack, I}.

clean_deque({Front, BackRev, Cnt}, Left) ->
    case Front of
        [] ->
            case BackRev of
                [] -> {[], [], 0};
                _ ->
                    NewFront = lists:reverse(BackRev),
                    clean_deque({NewFront, [], Cnt}, Left)
            end;
        [H | T] when H =< Left ->
            clean_deque({T, BackRev, Cnt - 1}, Left);
        _ ->
            {Front, BackRev, Cnt}
    end.

add_back(Index, {Front, BackRev, Cnt}) ->
    {Front, [Index | BackRev], Cnt + 1}.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_subarrays(nums :: [integer]) :: integer
  def number_of_subarrays(nums) do
    n = length(nums)

    # Compute next greater index for each position
    next_greater_list = compute_next_greater(nums, n)
    next_arr = :array.from_list(next_greater_list)

    # Build map from value to list of positions (ascending)
    pos_map =
      Enum.reduce(Enum.with_index(nums), %{}, fn {v, i}, acc ->
        Map.update(acc, v, [i], fn lst -> [i | lst] end)
      end)
      |> Map.new(fn {k, v} -> {k, Enum.reverse(v)} end)

    # Sum contributions for each value
    Enum.reduce(pos_map, 0, fn {_val, pos_list}, total ->
      total + sum_for_positions(pos_list, next_arr)
    end)
  end

  defp compute_next_greater(nums, n) do
    nums_arr = :array.from_list(nums)

    {next_rev, _stack} =
      Enum.reduce(0..(n - 1), {[], []}, fn offset, {next_acc, stack} ->
        i = n - 1 - offset
        val = :array.get(i, nums_arr)
        new_stack = pop_until_greater(stack, val)

        ng =
          case new_stack do
            [] -> n
            [{idx, _} | _] -> idx
          end

        {[ng | next_acc], [{i, val} | new_stack]}
      end)

    Enum.reverse(next_rev)
  end

  defp pop_until_greater([], _val), do: []

  defp pop_until_greater([{_idx, v} = top | rest], val) when v <= val do
    pop_until_greater(rest, val)
  end

  defp pop_until_greater(stack, _val), do: stack

  defp sum_for_positions(pos_list, next_arr) do
    len = length(pos_list)
    pos_arr = :array.from_list(pos_list)
    do_sum(0, 0, len, pos_arr, next_arr, 0)
  end

  defp do_sum(l, r, len, _pos_arr, _next_arr, acc) when l == len, do: acc

  defp do_sum(l, r, len, pos_arr, next_arr, acc) do
    r = if r < l, do: l, else: r
    i = :array.get(l, pos_arr)
    limit = :array.get(i, next_arr)
    r2 = advance_r(r, limit, len, pos_arr)
    contrib = r2 - l
    do_sum(l + 1, r2, len, pos_arr, next_arr, acc + contrib)
  end

  defp advance_r(r, limit, len, pos_arr) when r < len do
    val = :array.get(r, pos_arr)

    if val < limit do
      advance_r(r + 1, limit, len, pos_arr)
    else
      r
    end
  end

  defp advance_r(r, _limit, _len, _pos_arr), do: r
end
```
