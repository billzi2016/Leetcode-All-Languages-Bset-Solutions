# 3041. Maximize Consecutive Elements in an Array After Modification

## Cpp

```cpp
class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(), nums.end());
        int mx = *max_element(nums.begin(), nums.end()) + 2; // extra for val+1
        vector<int> dp(mx + 3, 0);
        int ans = 0;
        for (int v : nums) {
            int prevMinus = (v - 1 >= 0) ? dp[v - 1] : 0;
            int prevSame = dp[v];
            int candOrig = prevMinus + 1;
            if (candOrig > dp[v]) dp[v] = candOrig;
            int candInc = prevSame + 1;
            if (candInc > dp[v + 1]) dp[v + 1] = candInc;
            ans = max({ans, dp[v], dp[v + 1]});
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxSelectedElements(int[] nums) {
        int n = nums.length;
        int minVal = Integer.MAX_VALUE;
        int maxVal = 0;
        for (int v : nums) {
            if (v < minVal) minVal = v;
            if (v > maxVal) maxVal = v;
        }
        // frequency array up to maxVal + 1 (extra slot for possible increase)
        int[] freq = new int[maxVal + 2];
        for (int v : nums) {
            freq[v]++;
        }

        int best = 0;
        int curLen = 0;
        boolean carry = false; // true if we have an unused element from previous value to use now

        for (int k = minVal; k <= maxVal + 1; k++) {
            int c = freq[k];
            if (carry) {
                // use the carried element for position k
                // decide whether we can keep a new carry from current bucket
                carry = c >= 1;
                curLen++;
            } else {
                if (c == 0) {
                    // cannot fill this position, reset run
                    curLen = 0;
                    carry = false;
                } else {
                    // use one element from current bucket
                    carry = c - 1 >= 1;
                    curLen++;
                }
            }
            if (curLen > best) best = curLen;
        }

        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        max_val = max(nums) + 2  # accommodate v+1
        dp = [0] * (max_val + 3)
        ans = 0
        for v in nums:
            prev_vm1 = dp[v - 1]
            prev_v = dp[v]
            cand_to_v = prev_vm1 + 1
            if cand_to_v > dp[v]:
                dp[v] = cand_to_v
                if cand_to_v > ans:
                    ans = cand_to_v
            cand_to_vplus = prev_v + 1
            if cand_to_vplus > dp[v + 1]:
                dp[v + 1] = cand_to_vplus
                if cand_to_vplus > ans:
                    ans = cand_to_vplus
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        cur_len = 0
        last_val = -10**9  # sentinel value
        
        for x in nums:
            if cur_len == 0:
                cur_len = 1
                last_val = x
            else:
                if x > last_val + 1:
                    cur_len = 1
                    last_val = x
                elif x == last_val + 1:
                    cur_len += 1
                    last_val = x
                elif x == last_val:
                    cur_len += 1
                    last_val += 1
                else:  # x < last_val, cannot use this element
                    pass
            if cur_len > ans:
                ans = cur_len
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int maxSelectedElements(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int *arr = (int *)malloc(numsSize * sizeof(int));
    memcpy(arr, nums, numsSize * sizeof(int));
    qsort(arr, numsSize, sizeof(int), cmp_int);

    int maxVal = arr[numsSize - 1] + 1;               // possible value after increment
    int dpSize = maxVal + 2;                         // extra space for safety
    int *dp = (int *)calloc(dpSize, sizeof(int));

    int answer = 0;
    for (int i = 0; i < numsSize; ++i) {
        int a = arr[i];
        int v1 = a;
        int v2 = a + 1;

        int prev1 = (v1 > 0) ? dp[v1 - 1] : 0;
        int cand1 = prev1 + 1;

        int prev2 = (v2 > 0) ? dp[v2 - 1] : 0;
        int cand2 = prev2 + 1;

        if (cand1 > dp[v1]) dp[v1] = cand1;
        if (cand2 > dp[v2]) dp[v2] = cand2;

        if (dp[v1] > answer) answer = dp[v1];
        if (dp[v2] > answer) answer = dp[v2];
    }

    free(arr);
    free(dp);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSelectedElements(int[] nums) {
        int maxVal = 0;
        foreach (int x in nums) if (x > maxVal) maxVal = x;
        int size = maxVal + 2; // include max+1
        int[] freq = new int[size];
        foreach (int x in nums) freq[x]++;

        long carry = 0; // leftovers from previous value that can be used now
        int curLen = 0, ans = 0;

        for (int v = 0; v <= maxVal + 1; v++) {
            int cnt = freq[v];
            long total = cnt + carry;
            if (total > 0) {
                curLen++;
                if (carry > 0) {
                    // use one from previous leftovers, remaining are original v elements
                    carry = cnt;
                } else {
                    // use one from current count, rest become leftovers for next value
                    carry = cnt - 1;
                }
            } else {
                curLen = 0;
                carry = 0;
            }
            if (curLen > ans) ans = curLen;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSelectedElements = function(nums) {
    if (nums.length === 0) return 0;
    nums.sort((a, b) => a - b);
    const maxVal = Math.max(...nums) + 1; // need space for v+1
    const dp = new Uint32Array(maxVal + 2); // initialized to 0
    let answer = 0;
    for (let i = 0; i < nums.length; ++i) {
        const v = nums[i];
        const prevForV = dp[v - 1];          // length ending at v-1 before using this element
        const curForV = dp[v];               // length ending at v before using this element

        // assign this element to value v
        if (prevForV + 1 > dp[v]) {
            dp[v] = prevForV + 1;
        }

        // assign this element to value v+1
        if (curForV + 1 > dp[v + 1]) {
            dp[v + 1] = curForV + 1;
        }

        // update answer with possible new lengths
        if (dp[v] > answer) answer = dp[v];
        if (dp[v + 1] > answer) answer = dp[v + 1];
    }
    return answer;
};
```

## Typescript

```typescript
function maxSelectedElements(nums: number[]): number {
    if (nums.length === 0) return 0;
    let maxNum = 0;
    for (const v of nums) if (v > maxNum) maxNum = v;
    const dp = new Uint32Array(maxNum + 3); // indices up to maxNum+1
    let ans = 0;
    for (const x of nums) {
        const lenX = (x > 0 ? dp[x - 1] : 0) + 1;   // assign as x
        const lenX1 = dp[x] + 1;                    // assign as x+1
        if (lenX > dp[x]) dp[x] = lenX;
        if (lenX1 > dp[x + 1]) dp[x + 1] = lenX1;
        if (dp[x] > ans) ans = dp[x];
        if (dp[x + 1] > ans) ans = dp[x + 1];
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
    function maxSelectedElements($nums) {
        sort($nums);
        $dp = [];
        $ans = 0;
        foreach ($nums as $x) {
            // length if we keep the element as x
            $lenX = (isset($dp[$x - 1]) ? $dp[$x - 1] + 1 : 1);
            // previous best ending at x before using this element (for increment case)
            $prevAtX = $dp[$x] ?? 0;
            // length if we increase the element to x+1
            $lenXp1 = $prevAtX + 1;

            // update dp for value x
            if (!isset($dp[$x]) || $lenX > $dp[$x]) {
                $dp[$x] = $lenX;
            }
            // update dp for value x+1
            $xp1 = $x + 1;
            if (!isset($dp[$xp1]) || $lenXp1 > $dp[$xp1]) {
                $dp[$xp1] = $lenXp1;
            }

            if ($dp[$x] > $ans) $ans = $dp[$x];
            if ($dp[$xp1] > $ans) $ans = $dp[$xp1];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxSelectedElements(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var dp = [Int: Int]()
        var answer = 0
        for a in sorted {
            let prevLen = dp[a - 1] ?? 0          // length ending at a-1 before using current element
            let oldLenA = dp[a] ?? 0              // existing length ending at a before update
            
            // Use current element as value a (no increment)
            let candA = max(oldLenA, prevLen + 1)
            
            // Use current element as value a+1 (increment by 1)
            let oldLenAp1 = dp[a + 1] ?? 0
            let candAp1 = max(oldLenAp1, oldLenA + 1)   // predecessor is old length at a
            
            if candA > oldLenA {
                dp[a] = candA
            }
            if candAp1 > oldLenAp1 {
                dp[a + 1] = candAp1
            }
            answer = max(answer, candA, candAp1)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSelectedElements(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v
        val freq = IntArray(maxVal + 2)
        for (v in nums) freq[v]++
        var prevUnused = 0
        var curLen = 0
        var ans = 0
        for (x in 0..maxVal + 1) {
            if (prevUnused > 0) {
                // use an element that can only cover this position
                prevUnused--
                curLen++
                ans = maxOf(ans, curLen)
                // elements equal to x become available for the next position
                prevUnused = freq[x]
            } else if (freq[x] > 0) {
                // use one of the current value elements
                curLen++
                ans = maxOf(ans, curLen)
                // remaining ones can be used for the next position
                prevUnused = freq[x] - 1
            } else {
                // cannot cover this integer, reset streak
                curLen = 0
                prevUnused = 0
            }
        }
        return ans
    }
}
```

## Dart

```dart
class MinHeap {
  final List<int> _heap = [];

  bool get isEmpty => _heap.isEmpty;
  int get min => _heap[0];

  void add(int value) {
    _heap.add(value);
    _siftUp(_heap.length - 1);
  }

  int pop() {
    final int result = _heap[0];
    final int last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return result;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final int parent = (idx - 1) >> 1;
      if (_heap[parent] <= _heap[idx]) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final int n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _heap[left] < _heap[smallest]) smallest = left;
      if (right < n && _heap[right] < _heap[smallest]) smallest = right;

      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    final int tmp = _heap[i];
    _heap[i] = _heap[j];
    _heap[j] = tmp;
  }
}

class Solution {
  int maxSelectedElements(List<int> nums) {
    nums.sort();
    final int n = nums.length;
    int i = 0;
    int cur = nums[0];
    int best = 0;
    int streak = 0;
    final MinHeap heap = MinHeap();

    while (true) {
      // add intervals whose start <= cur
      while (i < n && nums[i] <= cur) {
        heap.add(nums[i] + 1); // interval end
        i++;
      }

      // discard intervals that cannot cover cur
      while (!heap.isEmpty && heap.min < cur) {
        heap.pop();
      }

      if (heap.isEmpty) {
        best = best > streak ? best : streak;
        if (i >= n) break; // no more elements to start a new sequence
        cur = nums[i];
        streak = 0;
        continue;
      } else {
        // assign current number using the interval with smallest end
        heap.pop();
        streak++;
        best = best > streak ? best : streak;
        cur++; // move to next target value
      }
    }

    return best;
  }
}
```

## Golang

```go
func maxSelectedElements(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	minVal := nums[0]
	maxVal := nums[0]
	for _, v := range nums {
		if v < minVal {
			minVal = v
		}
		if v > maxVal {
			maxVal = v
		}
	}
	freq := make([]int, maxVal+2) // extra slot for maxVal+1
	for _, v := range nums {
		freq[v]++
	}

	curLen, maxLen := 0, 0
	prevUnused := 0

	for x := minVal; x <= maxVal+1; x++ {
		if prevUnused > 0 {
			// use one element of value x-1 increased to x
			curLen++
			// leftover from previous cannot be used further
			prevUnused = freq[x] // remaining elements of value x can be used for next position
		} else {
			if freq[x] > 0 {
				// use an element of exact value x
				freq[x]--
				curLen++
				prevUnused = freq[x] // remaining of this value become unused for next step
			} else {
				// cannot cover this position, end current segment
				if curLen > maxLen {
					maxLen = curLen
				}
				curLen = 0
				prevUnused = 0
			}
		}
	}
	if curLen > maxLen {
		maxLen = curLen
	}
	return maxLen
}
```

## Ruby

```ruby
def max_selected_elements(nums)
  nums.sort!
  dp = Hash.new(0)
  ans = 0
  nums.each do |v|
    len_a = dp[v - 1] + 1          # use v as is (need previous value v-1)
    len_b = dp[v] + 1              # increase v to v+1 (need previous value v)
    dp[v] = len_a if len_a > dp[v]
    dp[v + 1] = len_b if len_b > dp[v + 1]
    ans = [ans, dp[v], dp[v + 1]].max
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxSelectedElements(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        java.util.Arrays.sort(nums)
        val maxVal = nums.max + 1
        val dp = new Array[Int](maxVal + 2) // extra space for v+1
        var i = 0
        while (i < nums.length) {
            val x = nums(i)
            val without = dp(x - 1) + 1          // use as x
            val withInc = dp(x) + 1              // increase to x+1
            if (without > dp(x)) dp(x) = without
            if (withInc > dp(x + 1)) dp(x + 1) = withInc
            i += 1
        }
        var ans = 0
        var idx = 0
        while (idx < dp.length) {
            if (dp(idx) > ans) ans = dp(idx)
            idx += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_selected_elements(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // sort the array
        let mut a = nums.clone();
        a.sort_unstable();

        // compute c[i] = a[i] - i
        let mut c: Vec<i64> = Vec::with_capacity(n);
        for (i, &val) in a.iter().enumerate() {
            c.push(val as i64 - i as i64);
        }

        use std::collections::VecDeque;
        let mut max_deq: VecDeque<usize> = VecDeque::new(); // decreasing values
        let mut min_deq: VecDeque<usize> = VecDeque::new(); // increasing values

        let mut left: usize = 0;
        let mut ans: usize = 0;

        for right in 0..n {
            let cur = c[right];
            while let Some(&idx) = max_deq.back() {
                if c[idx] <= cur { break; }
                max_deq.pop_back();
            }
            max_deq.push_back(right);
            while let Some(&idx) = min_deq.back() {
                if c[idx] >= cur { break; }
                min_deq.pop_back();
            }
            min_deq.push_back(right);

            // shrink window until condition satisfied: max - min <= 1
            loop {
                let max_val = c[*max_deq.front().unwrap()];
                let min_val = c[*min_deq.front().unwrap()];
                if max_val - min_val <= 1 { break; }
                if *max_deq.front().unwrap() == left { max_deq.pop_front(); }
                if *min_deq.front().unwrap() == left { min_deq.pop_front(); }
                left += 1;
            }

            ans = ans.max(right - left + 1);
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-selected-elements nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort nums <)]
         [best (make-hash)])
    (let loop ((lst sorted) (ans 0))
      (if (null? lst)
          ans
          (let* ([v (car lst)]
                 [prev (- v 1)]
                 [old-prev (hash-ref best prev 0)]
                 [old-v   (hash-ref best v 0)]
                 [len1 (+ old-prev 1)]        ; assign v as final value
                 [len2 (+ old-v    1)])       ; assign v+1 as final value
            ;; update best for v
            (when (> len1 (hash-ref best v 0))
              (hash-set! best v len1))
            ;; update best for v+1
            (let ([vplus (+ v 1)])
              (when (> len2 (hash-ref best vplus 0))
                (hash-set! best vplus len2)))
            (define new-ans (max ans len1 len2))
            (loop (cdr lst) new-ans))))))
```

## Erlang

```erlang
-spec max_selected_elements(Nums :: [integer()]) -> integer().
max_selected_elements(Nums) ->
    % Build frequency array
    MaxVal = lists:max(Nums),
    Limit = MaxVal + 1,                     % possible target values up to MaxVal+1
    Size = Limit + 1,                       % include value Limit itself (freq may be zero)
    Freq0 = lists:duplicate(Size, 0),
    Freq = add_freqs(Nums, Freq0, 0),

    % Prefix sums and auxiliary arrays A (=pref - index) and B (=A - freq)
    {Pref, A, B} = build_arrays(Freq, Size),

    Base0 = 1,                               % A[-1] = pref[-1] - (-1) = 1

    % Binary search on answer length
    MaxLen = binary_search(0, Limit + 1, fun(Len) ->
        feasible(Len, A, B, Base0, Size)
    end),
    MaxLen.

add_freqs([], Freq, _Idx) -> Freq;
add_freqs([H|T], Freq, Idx) ->
    NewFreq = lists:foldl(fun(I, Acc) ->
                case I of
                    {Pos, Val} when Pos == H -> [{Pos, Val+1}|Acc];
                    _ -> [I|Acc]
                end
            end, [], [{Idx,0} || Idx <- lists:seq(0, length(Freq)-1)]),
    add_freqs(T, NewFreq, Idx).

build_arrays(Freq, Size) ->
    build_arrays(Freq, 0, 0, [], [], []).

build_arrays([], _PrefAcc, _Idx, PrefRev, ARev, BRev) ->
    {lists:reverse(PrefRev), lists:reverse(ARev), lists:reverse(BRev)};
build_arrays([F|Rest], PrefAcc, Idx, PrefRev, ARev, BRev) ->
    NewPref = PrefAcc + F,
    AVal = NewPref - Idx,
    BVal = AVal - F,
    build_arrays(Rest, NewPref, Idx+1,
                 [NewPref|PrefRev],
                 [AVal|ARev],
                 [BVal|BRev]).

binary_search(Low, High, _Check) when Low >= High -> Low;
binary_search(Low, High, Check) ->
    Mid = (Low + High) div 2,
    case Check(Mid) of
        true -> binary_search(Mid+1, High, Check);
        false -> binary_search(Low, Mid-1, Check)
    end.

feasible(0, _A, _B, _Base0, _Size) -> true;
feasible(Len, A, B, Base0, Size) ->
    % Use monotonic deques implemented with queue module
    MinDeque = queue:new(),
    MaxDeque = queue:new(),
    feasible_loop(0, Len-1, Len, A, B, Base0, MinDeque, MaxDeque, Size).

feasible_loop(R, _LIdx, Len, _A, _B, _Base0, _MinQ, _MaxQ, Size) when R >= Size -> false;
feasible_loop(R, LIdx, Len, A, B, Base0, MinQ, MaxQ, Size) ->
    % Insert index R into deques
    ValA = lists:nth(R+1, A),
    ValB = lists:nth(R+1, B),

    NewMinQ = push_min(R, ValA, MinQ),
    NewMaxQ = push_max(R, ValB, MaxQ),

    case R >= Len-1 of
        true ->
            % Window ready, check feasibility
            CurL = R - Len + 1,
            % Remove out-of-window elements from fronts
            CleanMinQ = clean_front(CurL, MinQ),
            CleanMaxQ = clean_front(CurL, MaxQ),

            Baseline = case CurL of
                0 -> Base0;
                _ -> lists:nth(CurL, A)   % A[CurL-1] because A is 0‑based list
            end,

            MinA = element(2, queue:peek(CleanMinQ)),
            MaxB = element(2, queue:peek(CleanMaxQ)),

            if MaxB =< Baseline, Baseline =< MinA ->
                    true;
               true ->
                    feasible_loop(R+1, CurL+1, Len, A, B, Base0,
                                  CleanMinQ, CleanMaxQ, Size)
            end;
        false ->
            feasible_loop(R+1, LIdx, Len, A, B, Base0, NewMinQ, NewMaxQ, Size)
    end.

push_min(Idx, Val, Q) ->
    case queue:out_r(Q) of
        {empty, _} -> queue:in({Idx, Val}, Q);
        {{PrevIdx, PrevVal}, Rest} when PrevVal >= Val ->
            push_min(Idx, Val, Rest);
        {{PrevIdx, PrevVal}, _}=Res ->
            % put back the popped element and insert new one
            Q1 = queue:in_r({PrevIdx, PrevVal}, Rest),
            queue:in({Idx, Val}, Q1)
    end.

push_max(Idx, Val, Q) ->
    case queue:out_r(Q) of
        {empty, _} -> queue:in({Idx, Val}, Q);
        {{PrevIdx, PrevVal}, Rest} when PrevVal =< Val ->
            push_max(Idx, Val, Rest);
        {{PrevIdx, PrevVal}, _}=Res ->
            Q1 = queue:in_r({PrevIdx, PrevVal}, Rest),
            queue:in({Idx, Val}, Q1)
    end.

clean_front(LimitIdx, Q) ->
    case queue:peek(Q) of
        empty -> Q;
        {{Idx,_},_} when Idx < LimitIdx ->
            {_, NewQ} = queue:out(Q),
            clean_front(LimitIdx, NewQ);
        _ -> Q
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_selected_elements(nums :: [integer]) :: integer
  def max_selected_elements(nums) do
    sorted = Enum.sort(nums)

    {ans, _l, _counts, _queue} =
      Enum.reduce(Enum.with_index(sorted), {0, 0, %{}, :queue.new()}, fn {v, r},
                                                                          {ans, l, counts, q} ->
        val = v - r
        q = :queue.in(val, q)
        counts = Map.update(counts, val, 1, &(&1 + 1))

        {l, counts, q} = shrink_until_valid(l, counts, q)

        ans = if r - l + 1 > ans, do: r - l + 1, else: ans
        {ans, l, counts, q}
      end)

    ans
  end

  defp shrink_until_valid(l, counts, q) do
    if valid?(counts) do
      {l, counts, q}
    else
      {{:value, out_val}, q2} = :queue.out(q)
      cnt = Map.get(counts, out_val)

      counts =
        if cnt == 1 do
          Map.delete(counts, out_val)
        else
          Map.put(counts, out_val, cnt - 1)
        end

      shrink_until_valid(l + 1, counts, q2)
    end
  end

  defp valid?(counts) do
    case map_size(counts) do
      0 -> true
      1 -> true
      2 ->
        [k1, k2] = Map.keys(counts)
        abs(k1 - k2) <= 1
      _ -> false
    end
  end
end
```
