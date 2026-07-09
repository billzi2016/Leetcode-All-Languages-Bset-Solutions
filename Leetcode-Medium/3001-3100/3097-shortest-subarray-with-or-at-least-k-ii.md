# 3097. Shortest Subarray With OR at Least K II

## Cpp

```cpp
class Solution {
public:
    int minimumSubarrayLength(std::vector<int>& nums, int k) {
        const int MAX_BIT = 31; // enough for values up to 1e9
        std::vector<int> cnt(MAX_BIT, 0);
        int curOr = 0;
        int left = 0;
        int n = nums.size();
        int ans = n + 1;

        for (int right = 0; right < n; ++right) {
            int x = nums[right];
            curOr |= x;
            // add bits of x
            int tmp = x;
            while (tmp) {
                int b = __builtin_ctz(tmp);
                cnt[b]++;
                tmp &= (tmp - 1);
            }

            while (left <= right && curOr >= k) {
                ans = std::min(ans, right - left + 1);
                int y = nums[left];
                // remove bits of y
                int t = y;
                while (t) {
                    int b = __builtin_ctz(t);
                    cnt[b]--;
                    if (cnt[b] == 0) {
                        curOr &= ~(1 << b);
                    }
                    t &= (t - 1);
                }
                ++left;
            }
        }

        return ans == n + 1 ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumSubarrayLength(int[] nums, int k) {
        int n = nums.length;
        int[] bitCount = new int[31]; // counts for bits 0..30
        int curOr = 0;
        int left = 0;
        int best = Integer.MAX_VALUE;

        for (int right = 0; right < n; ++right) {
            int val = nums[right];
            curOr |= val;
            int tmp = val;
            while (tmp != 0) {
                int b = Integer.numberOfTrailingZeros(tmp);
                bitCount[b]++;
                tmp &= (tmp - 1);
            }

            while (left <= right && curOr >= k) {
                best = Math.min(best, right - left + 1);

                int rem = nums[left];
                int t = rem;
                while (t != 0) {
                    int b = Integer.numberOfTrailingZeros(t);
                    bitCount[b]--;
                    if (bitCount[b] == 0) {
                        curOr &= ~(1 << b);
                    }
                    t &= (t - 1);
                }
                left++;
            }
        }

        return best == Integer.MAX_VALUE ? -1 : best;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # bit counts for current window
        BIT = 31  # enough for numbers up to 1e9
        cnt = [0] * BIT

        def update(num, delta):
            b = 0
            while num:
                if num & 1:
                    cnt[b] += delta
                num >>= 1
                b += 1

        def current_or():
            res = 0
            for i in range(BIT):
                if cnt[i]:
                    res |= (1 << i)
            return res

        ans = n + 1
        left = 0
        for right, val in enumerate(nums):
            update(val, 1)
            while left <= right:
                cur = current_or()
                if cur >= k:
                    ans = min(ans, right - left + 1)
                    update(nums[left], -1)
                    left += 1
                else:
                    break

        return ans if ans != n + 1 else -1
```

## Python3

```python
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1  # any non‑empty subarray works
        
        n = len(nums)
        cnt = [0] * 31  # enough for numbers up to 10^9
        left = 0
        ans = n + 1

        def add_num(num: int, delta: int) -> None:
            for b in range(31):
                if (num >> b) & 1:
                    cnt[b] += delta

        def current_or() -> int:
            res = 0
            for b in range(31):
                if cnt[b]:
                    res |= (1 << b)
            return res

        for right in range(n):
            add_num(nums[right], 1)

            while left <= right and current_or() >= k:
                ans = min(ans, right - left + 1)
                add_num(nums[left], -1)
                left += 1

        return -1 if ans == n + 1 else ans
```

## C

```c
int minimumSubarrayLength(int* nums, int numsSize, int k) {
    const int BITS = 31;                 // enough for values up to 1e9
    int cnt[BITS];
    for (int i = 0; i < BITS; ++i) cnt[i] = 0;

    int cur_or = 0;
    int left = 0;
    int ans = numsSize + 1;               // sentinel value

    for (int right = 0; right < numsSize; ++right) {
        int x = nums[right];
        for (int b = 0; b < BITS; ++b) {
            if ((x >> b) & 1) cnt[b]++;   // add bits of new element
        }
        cur_or |= x;                      // update current OR

        while (left <= right && cur_or >= k) {
            int len = right - left + 1;
            if (len < ans) ans = len;

            int y = nums[left];
            for (int b = 0; b < BITS; ++b) {
                if ((y >> b) & 1) {
                    cnt[b]--;
                    if (cnt[b] == 0) {
                        cur_or &= ~(1 << b);   // clear bit if no longer present
                    }
                }
            }
            ++left;                       // shrink window from the left
        }
    }

    return (ans == numsSize + 1) ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSubarrayLength(int[] nums, int k) {
        int n = nums.Length;
        const int BITS = 31; // sufficient for values up to 1e9
        int[] bitCounts = new int[BITS];
        int currentOr = 0;
        int left = 0;
        int minLen = int.MaxValue;

        void Add(int x) {
            for (int i = 0; i < BITS; ++i) {
                if (((x >> i) & 1) == 1) {
                    bitCounts[i]++;
                    if (bitCounts[i] == 1) {
                        currentOr |= (1 << i);
                    }
                }
            }
        }

        void Remove(int x) {
            for (int i = 0; i < BITS; ++i) {
                if (((x >> i) & 1) == 1) {
                    bitCounts[i]--;
                    if (bitCounts[i] == 0) {
                        currentOr &= ~(1 << i);
                    }
                }
            }
        }

        for (int right = 0; right < n; ++right) {
            Add(nums[right]);
            while (left <= right && currentOr >= k) {
                minLen = Math.Min(minLen, right - left + 1);
                Remove(nums[left]);
                left++;
            }
        }

        return minLen == int.MaxValue ? -1 : minLen;
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
var minimumSubarrayLength = function(nums, k) {
    if (k === 0) return 1; // any non‑empty subarray works
    
    const n = nums.length;
    const bitCounts = new Array(32).fill(0);
    
    const addNum = (num) => {
        for (let b = 0; b < 32; ++b) {
            if ((num >> b) & 1) bitCounts[b]++;
        }
    };
    
    const removeNum = (num) => {
        for (let b = 0; b < 32; ++b) {
            if ((num >> b) & 1) bitCounts[b]--;
        }
    };
    
    const currentOr = () => {
        let res = 0;
        for (let b = 0; b < 32; ++b) {
            if (bitCounts[b] > 0) res |= (1 << b);
        }
        return res;
    };
    
    let left = 0;
    let best = Infinity;
    
    for (let right = 0; right < n; ++right) {
        addNum(nums[right]);
        while (left <= right && currentOr() >= k) {
            best = Math.min(best, right - left + 1);
            removeNum(nums[left]);
            left++;
        }
    }
    
    return best === Infinity ? -1 : best;
};
```

## Typescript

```typescript
function minimumSubarrayLength(nums: number[], k: number): number {
    const n = nums.length;
    if (k === 0) return 1; // any non‑empty subarray works

    const bitCounts = new Array(32).fill(0);
    let left = 0;
    let best = Number.MAX_SAFE_INTEGER;

    const currentOR = (): number => {
        let or = 0;
        for (let i = 0; i < 32; i++) {
            if (bitCounts[i] > 0) or |= (1 << i);
        }
        return or;
    };

    for (let right = 0; right < n; right++) {
        const val = nums[right];
        for (let b = 0; b < 32; b++) {
            if ((val >> b) & 1) bitCounts[b]++;
        }

        while (left <= right) {
            const orVal = currentOR();
            if (orVal >= k) {
                const len = right - left + 1;
                if (len < best) best = len;

                const rem = nums[left];
                for (let b = 0; b < 32; b++) {
                    if ((rem >> b) & 1) bitCounts[b]--;
                }
                left++;
            } else {
                break;
            }
        }
    }

    return best === Number.MAX_SAFE_INTEGER ? -1 : best;
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
    function minimumSubarrayLength($nums, $k) {
        $n = count($nums);
        if ($n == 0) return -1;

        // bit counts for current window
        $cnt = array_fill(0, 32, 0);
        $left = 0;
        $best = $n + 1; // sentinel larger than any possible length

        for ($right = 0; $right < $n; $right++) {
            $val = $nums[$right];
            for ($b = 0; $b < 32; $b++) {
                if ((($val >> $b) & 1) === 1) {
                    $cnt[$b]++;
                }
            }

            // compute current OR from bit counts
            $curOr = 0;
            for ($b = 0; $b < 32; $b++) {
                if ($cnt[$b] > 0) {
                    $curOr |= (1 << $b);
                }
            }

            // try to shrink window while it satisfies the condition
            while ($left <= $right && $curOr >= $k) {
                $len = $right - $left + 1;
                if ($len < $best) {
                    $best = $len;
                }

                // remove leftmost element from window
                $valLeft = $nums[$left];
                for ($b = 0; $b < 32; $b++) {
                    if ((($valLeft >> $b) & 1) === 1) {
                        $cnt[$b]--;
                    }
                }
                $left++;

                // recompute OR after removal
                $curOr = 0;
                for ($b = 0; $b < 32; $b++) {
                    if ($cnt[$b] > 0) {
                        $curOr |= (1 << $b);
                    }
                }
            }
        }

        return $best == $n + 1 ? -1 : $best;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var bitCounts = [Int](repeating: 0, count: 32)
        
        @inline(__always) func add(_ x: Int) {
            var v = x
            for b in 0..<32 {
                if (v & 1) == 1 { bitCounts[b] += 1 }
                v >>= 1
            }
        }
        
        @inline(__always) func remove(_ x: Int) {
            var v = x
            for b in 0..<32 {
                if (v & 1) == 1 { bitCounts[b] -= 1 }
                v >>= 1
            }
        }
        
        @inline(__always) func currentOR() -> Int {
            var res = 0
            for b in 0..<32 where bitCounts[b] > 0 {
                res |= (1 << b)
            }
            return res
        }
        
        var left = 0
        var minLen = Int.max
        
        for right in 0..<n {
            add(nums[right])
            while left <= right && currentOR() >= k {
                let len = right - left + 1
                if len < minLen { minLen = len }
                remove(nums[left])
                left += 1
            }
        }
        
        return minLen == Int.max ? -1 : minLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSubarrayLength(nums: IntArray, k: Int): Int {
        val n = nums.size
        var minLen = Int.MAX_VALUE
        val cnt = IntArray(31)
        var left = 0
        for (right in 0 until n) {
            updateBits(nums[right], cnt, 1)
            while (left <= right && currentOr(cnt) >= k) {
                minLen = kotlin.math.min(minLen, right - left + 1)
                updateBits(nums[left], cnt, -1)
                left++
            }
        }
        return if (minLen == Int.MAX_VALUE) -1 else minLen
    }

    private fun updateBits(num: Int, cnt: IntArray, delta: Int) {
        var x = num
        var bit = 0
        while (x != 0) {
            if ((x and 1) != 0) {
                cnt[bit] += delta
            }
            x = x ushr 1
            bit++
        }
    }

    private fun currentOr(cnt: IntArray): Int {
        var res = 0
        for (i in cnt.indices) {
            if (cnt[i] > 0) {
                res = res or (1 shl i)
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  int minimumSubarrayLength(List<int> nums, int k) {
    int n = nums.length;
    const int BITS = 32; // cover all possible bits
    List<int> cnt = List.filled(BITS, 0);
    int curOr = 0;
    int left = 0;
    int ans = n + 1;

    void add(int num) {
      for (int i = 0; i < BITS; ++i) {
        if (((num >> i) & 1) == 1) {
          if (cnt[i] == 0) curOr |= (1 << i);
          cnt[i]++;
        }
      }
    }

    void remove(int num) {
      for (int i = 0; i < BITS; ++i) {
        if (((num >> i) & 1) == 1) {
          cnt[i]--;
          if (cnt[i] == 0) curOr &= ~(1 << i);
        }
      }
    }

    for (int right = 0; right < n; ++right) {
      add(nums[right]);
      while (left <= right && curOr >= k) {
        int len = right - left + 1;
        if (len < ans) ans = len;
        remove(nums[left]);
        left++;
      }
    }

    return ans == n + 1 ? -1 : ans;
  }
}
```

## Golang

```go
func minimumSubarrayLength(nums []int, k int) int {
	const B = 31 // enough for values up to 1e9
	bitCounts := make([]int, B)
	n := len(nums)
	minLen := n + 1
	left := 0

	// helper to compute current OR from bit counts
	computeOR := func() int {
		res := 0
		for b := 0; b < B; b++ {
			if bitCounts[b] > 0 {
				res |= 1 << b
			}
		}
		return res
	}

	for right, val := range nums {
		// add bits of nums[right]
		for b := 0; b < B; b++ {
			if (val>>b)&1 == 1 {
				bitCounts[b]++
			}
		}
		// try to shrink from the left while window is valid
		for {
			curOr := computeOR()
			if curOr >= k && left <= right {
				length := right - left + 1
				if length < minLen {
					minLen = length
				}
				// remove bits of nums[left]
				lv := nums[left]
				for b := 0; b < B; b++ {
					if (lv>>b)&1 == 1 {
						bitCounts[b]--
					}
				}
				left++
			} else {
				break
			}
		}
	}

	if minLen == n+1 {
		return -1
	}
	return minLen
}
```

## Ruby

```ruby
def minimum_subarray_length(nums, k)
  n = nums.length
  cnt = Array.new(32, 0)
  cur_or = 0
  left = 0
  ans = n + 1

  nums.each_with_index do |x, right|
    # add x to window
    temp = x
    bit = 0
    while temp > 0
      if (temp & 1) == 1
        cnt[bit] += 1
        cur_or |= (1 << bit)
      end
      temp >>= 1
      bit += 1
    end

    # try to shrink window while condition holds
    while left <= right && cur_or >= k
      length = right - left + 1
      ans = length if length < ans

      y = nums[left]
      temp2 = y
      bit2 = 0
      while temp2 > 0
        if (temp2 & 1) == 1
          cnt[bit2] -= 1
          cur_or &= ~(1 << bit2) if cnt[bit2] == 0
        end
        temp2 >>= 1
        bit2 += 1
      end
      left += 1
    end
  end

  ans <= n ? ans : -1
end
```

## Scala

```scala
object Solution {
    def minimumSubarrayLength(nums: Array[Int], k: Int): Int = {
        if (k == 0) return 1
        val cnt = new Array[Int](32)
        var left = 0
        var minLen = Int.MaxValue

        def add(num: Int): Unit = {
            var i = 0
            while (i < 32) {
                if (((num >> i) & 1) != 0) cnt(i) += 1
                i += 1
            }
        }

        def remove(num: Int): Unit = {
            var i = 0
            while (i < 32) {
                if (((num >> i) & 1) != 0) cnt(i) -= 1
                i += 1
            }
        }

        def currentOr(): Int = {
            var res = 0
            var i = 0
            while (i < 32) {
                if (cnt(i) > 0) res |= (1 << i)
                i += 1
            }
            res
        }

        for (right <- nums.indices) {
            add(nums(right))
            var curOr = currentOr()
            while (left <= right && curOr >= k) {
                val len = right - left + 1
                if (len < minLen) minLen = len
                remove(nums(left))
                left += 1
                curOr = currentOr()
            }
        }

        if (minLen == Int.MaxValue) -1 else minLen
    }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn minimum_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        if k == 0 {
            return 1;
        }
        const BITS: usize = 31; // sufficient for values up to 1e9
        let n = nums.len();
        let mut cnt = [0i32; BITS];
        let mut cur_or: i32 = 0;
        let mut left: usize = 0;
        let mut ans: usize = usize::MAX;

        for right in 0..n {
            let val = nums[right] as u32;
            for b in 0..BITS {
                if (val >> b) & 1 == 1 {
                    cnt[b] += 1;
                    cur_or |= 1 << b;
                }
            }

            while left <= right && cur_or >= k {
                ans = min(ans, right - left + 1);
                let v = nums[left] as u32;
                for b in 0..BITS {
                    if (v >> b) & 1 == 1 {
                        cnt[b] -= 1;
                        if cnt[b] == 0 {
                            cur_or &= !(1 << b);
                        }
                    }
                }
                left += 1;
            }
        }

        if ans == usize::MAX { -1 } else { ans as i32 }
    }
}
```

## Racket

```racket
(define/contract (minimum-subarray-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (counts (make-vector 32 0))
         (left 0)
         (min-len (+ n 1)))
    (define (add num delta)
      (for ([i (in-range 32)])
        (when (= (bitwise-and (arithmetic-shift num i) 1) 1)
          (vector-set! counts i (+ (vector-ref counts i) delta)))))
    (define (current-or)
      (let loop ((i 0) (res 0))
        (if (= i 32)
            res
            (let ((cnt (vector-ref counts i)))
              (loop (+ i 1)
                    (if (> cnt 0)
                        (bitwise-ior res (arithmetic-shift 1 i))
                        res))))))
    (for ([right (in-range n)])
      (add (list-ref nums right) 1)
      (let loop-inner ()
        (define cur-or (current-or))
        (when (and (>= cur-or k) (<= left right))
          (set! min-len (min min-len (+ (- right left) 1)))
          (add (list-ref nums left) -1)
          (set! left (+ left 1))
          (loop-inner))))
    (if (> min-len n) -1 min-len)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_subarray_length/2]).

-spec minimum_subarray_length(Nums :: [integer()], K :: integer()) -> integer().
minimum_subarray_length(Nums, K) ->
    NumsTuple = list_to_tuple(Nums),
    N = tuple_size(NumsTuple),
    Counts0 = lists:duplicate(32, 0),
    MinLenInit = N + 1,
    {FinalMin, _Left, _Counts} = loop(0, 0, Counts0, MinLenInit, NumsTuple, K, N),
    if FinalMin =< N -> FinalMin; true -> -1 end.

%% main sliding window loop
loop(Right, Left, Counts, MinLen, _NumsTuple, _K, N) when Right == N ->
    {MinLen, Left, Counts};
loop(Right, Left, Counts, MinLen, NumsTuple, K, N) ->
    NumR = element(Right + 1, NumsTuple),
    NewCounts = add_bits(NumR, Counts, 1),
    {NewMin, NewLeft, UpdatedCounts} = shrink_window(NewCounts, Left, Right, MinLen, NumsTuple, K),
    loop(Right + 1, NewLeft, UpdatedCounts, NewMin, NumsTuple, K, N).

%% shrink window while OR >= K and non‑empty
shrink_window(Counts, Left, Right, MinLen, NumsTuple, K) ->
    CurrentOR = or_from_counts(Counts),
    case (CurrentOR >= K) andalso (Left =< Right) of
        true ->
            Len = Right - Left + 1,
            NewMin = if Len < MinLen -> Len; true -> MinLen end,
            NumL = element(Left + 1, NumsTuple),
            UpdatedCounts = add_bits(NumL, Counts, -1),
            shrink_window(UpdatedCounts, Left + 1, Right, NewMin, NumsTuple, K);
        false ->
            {MinLen, Left, Counts}
    end.

%% update bit counts by Delta (+1 to add, -1 to remove)
add_bits(Number, Counts, Delta) ->
    add_bits(0, Number, Counts, Delta).

add_bits(_BitPos, _Number, [], _Delta) ->
    [];
add_bits(BitPos, Number, [C|Rest], Delta) ->
    BitSet = (Number bsr BitPos) band 1,
    NewC = C + Delta * BitSet,
    [NewC | add_bits(BitPos + 1, Number, Rest, Delta)].

%% compute OR from counts
or_from_counts(Counts) ->
    or_from_counts(0, Counts, 0).

or_from_counts(_BitPos, [], Acc) ->
    Acc;
or_from_counts(BitPos, [C|Rest], Acc) ->
    NewAcc = if C > 0 -> Acc bor (1 bsl BitPos); true -> Acc end,
    or_from_counts(BitPos + 1, Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec minimum_subarray_length(nums :: [integer], k :: integer) :: integer
  def minimum_subarray_length(nums, k) do
    if k == 0 do
      1
    else
      n = length(nums)
      nums_tuple = List.to_tuple(nums)
      cnt = :array.new(32, default: 0)
      process(0, n, nums_tuple, 0, cnt, 0, n + 1, k)
    end
  end

  defp process(right, len, nums_tuple, left, cnt, cur_or, min_len, k) do
    if right == len do
      if min_len == len + 1, do: -1, else: min_len
    else
      num = elem(nums_tuple, right)
      {cnt1, or1} = add_num(num, cnt, cur_or)

      {new_left, new_cnt, new_or, new_min} =
        shrink_window(left, cnt1, or1, min_len, right, nums_tuple, k)

      process(right + 1, len, nums_tuple, new_left, new_cnt, new_or, new_min, k)
    end
  end

  defp shrink_window(left, cnt, cur_or, min_len, right, nums_tuple, k) do
    if cur_or >= k do
      new_min = if (right - left + 1) < min_len, do: (right - left + 1), else: min_len
      left_num = elem(nums_tuple, left)
      {cnt2, or2} = remove_num(left_num, cnt, cur_or)
      shrink_window(left + 1, cnt2, or2, new_min, right, nums_tuple, k)
    else
      {left, cnt, cur_or, min_len}
    end
  end

  defp add_num(num, cnt, cur_or) do
    {new_cnt, new_or} =
      0..31
      |> Enum.reduce({cnt, cur_or}, fn b, {c, o} ->
        if ((num >>> b) &&& 1) == 1 do
          old = :array.get(b, c)
          c2 = :array.set(b, old + 1, c)
          o2 = if old == 0, do: o ||| (1 <<< b), else: o
          {c2, o2}
        else
          {c, o}
        end
      end)

    {new_cnt, new_or}
  end

  defp remove_num(num, cnt, cur_or) do
    {new_cnt, new_or} =
      0..31
      |> Enum.reduce({cnt, cur_or}, fn b, {c, o} ->
        if ((num >>> b) &&& 1) == 1 do
          old = :array.get(b, c)
          new_val = old - 1
          c2 = :array.set(b, new_val, c)

          o2 =
            if new_val == 0,
              do: o &&& Bitwise.bnot(1 <<< b),
              else: o

          {c2, o2}
        else
          {c, o}
        end
      end)

    {new_cnt, new_or}
  end
end
```
