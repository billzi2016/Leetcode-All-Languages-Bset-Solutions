# 2763. Sum of Imbalance Numbers of All Subarrays

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sumImbalanceNumbers(vector<int>& nums) {
        int n = nums.size();
        long long total = 0;
        for (int left = 0; left < n; ++left) {
            set<int> s;
            int cur = 0; // current imbalance for subarray [left, right]
            for (int right = left; right < n; ++right) {
                int x = nums[right];
                if (s.find(x) == s.end()) {
                    auto it = s.lower_bound(x);
                    int succ = -1, pred = -1;
                    if (it != s.end()) succ = *it;
                    if (it != s.begin()) {
                        --it;
                        pred = *it;
                    }
                    if (pred != -1 && succ != -1) {
                        if (succ - pred > 1) cur--;               // remove old gap
                        if (x - pred > 1) cur++;                  // new left gap
                        if (succ - x > 1) cur++;                  // new right gap
                    } else if (pred != -1) {
                        if (x - pred > 1) cur++;
                    } else if (succ != -1) {
                        if (succ - x > 1) cur++;
                    }
                    s.insert(x);
                }
                total += cur;
            }
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int sumImbalanceNumbers(int[] nums) {
        int n = nums.length;
        int maxVal = n; // given constraint nums[i] <= n
        int answer = 0;
        int[] cnt = new int[maxVal + 3];
        for (int left = 0; left < n; left++) {
            java.util.Arrays.fill(cnt, 0);
            int cur = 0;
            for (int right = left; right < n; right++) {
                int v = nums[right];
                if (++cnt[v] == 1) { // first occurrence of this value
                    boolean hasLeft = v > 1 && cnt[v - 1] > 0;
                    boolean hasRight = v < maxVal && cnt[v + 1] > 0;
                    if (!hasLeft && !hasRight) {
                        cur += 1;
                    } else if (hasLeft && hasRight) {
                        cur -= 1;
                    }
                }
                answer += cur;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def sumImbalanceNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for left in range(n):
            seen = set()
            cur = 0
            for right in range(left, n):
                v = nums[right]
                if v not in seen:
                    left_adj = (v - 1) in seen
                    right_adj = (v + 1) in seen
                    if not left_adj and not right_adj:
                        cur += 1
                    elif left_adj and right_adj:
                        cur -= 1
                    seen.add(v)
                total += cur
        return total
```

## Python3

```python
class Solution:
    def sumImbalanceNumbers(self, nums):
        from typing import List

        n = len(nums)

        class BIT:
            __slots__ = ("n", "bit")
            def __init__(self, n: int):
                self.n = n
                self.bit = [0] * (n + 2)
            def add(self, i: int, delta: int) -> None:
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def sum(self, i: int) -> int:
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s
            # find smallest idx such that prefix sum >= k (k>=1)
            def kth(self, k: int) -> int:
                idx = 0
                bitmask = 1 << (self.n.bit_length())
                while bitmask:
                    nxt = idx + bitmask
                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]
                    bitmask >>= 1
                return idx + 1

        ans = 0
        max_val = n  # nums[i] <= n
        for left in range(n):
            present = [False] * (max_val + 2)
            bit = BIT(max_val)
            imbalance = 0
            for right in range(left, n):
                x = nums[right]
                if not present[x]:
                    total_left = bit.sum(x - 1)
                    pre = None
                    if total_left:
                        pre = bit.kth(total_left)          # predecessor
                    total_all = bit.sum(max_val)
                    total_up_to_x = bit.sum(x)
                    succ = None
                    if total_all - total_up_to_x:
                        succ = bit.kth(total_up_to_x + 1)   # successor

                    if pre is not None and succ is not None:
                        imbalance -= 1
                    elif pre is not None:
                        imbalance += x - pre - 1
                    elif succ is not None:
                        imbalance += succ - x - 1
                    # else: first element, no change

                    present[x] = True
                    bit.add(x, 1)
                ans += imbalance
        return ans
```

## C

```c
int sumImbalanceNumbers(int* nums, int numsSize) {
    long long total = 0;
    int maxVal = numsSize;                     // values are in [1, numsSize]
    int *cnt = (int*)calloc(maxVal + 3, sizeof(int));
    
    for (int i = 0; i < numsSize; ++i) {
        memset(cnt, 0, (maxVal + 3) * sizeof(int));
        int components = 0;
        for (int j = i; j < numsSize; ++j) {
            int x = nums[j];
            if (++cnt[x] == 1) {               // first occurrence of this value
                int left  = cnt[x - 1] > 0;
                int right = cnt[x + 1] > 0;
                if (!left && !right) {
                    ++components;              // new isolated component
                } else if (left && right) {
                    --components;              // merge two components
                }
                // exactly one neighbor: component count unchanged
            }
            total += (components > 0 ? components - 1 : 0);
        }
    }
    
    free(cnt);
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int SumImbalanceNumbers(int[] nums) {
        int n = nums.Length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            var seen = new HashSet<int>();
            int cur = -1; // start before first element
            for (int j = i; j < n; j++) {
                int x = nums[j];
                if (!seen.Contains(x)) {
                    bool left = seen.Contains(x - 1);
                    bool right = seen.Contains(x + 1);
                    if (!left && !right) {
                        cur++;
                    } else if (left && right) {
                        cur--;
                    }
                    // otherwise unchanged
                    seen.Add(x);
                }
                ans += cur;
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
 * @return {number}
 */
var sumImbalanceNumbers = function(nums) {
    const n = nums.length;
    let answer = 0;

    class BIT {
        constructor(size) {
            this.n = size;
            this.tree = new Array(size + 2).fill(0);
        }
        add(idx, delta) {
            for (let i = idx; i <= this.n; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx) {
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
        // smallest index such that prefix sum >= k (k >=1)
        kth(k) {
            let idx = 0;
            let bitMask = 1 << Math.floor(Math.log2(this.n + 1));
            while (bitMask !== 0) {
                const next = idx + bitMask;
                if (next <= this.n && this.tree[next] < k) {
                    idx = next;
                    k -= this.tree[next];
                }
                bitMask >>= 1;
            }
            return idx + 1;
        }
    }

    for (let left = 0; left < n; ++left) {
        const bit = new BIT(n);
        const present = new Array(n + 2).fill(false);
        let curImbalance = 0;

        for (let right = left; right < n; ++right) {
            const x = nums[right];
            if (!present[x]) {
                // find predecessor
                let L = null;
                const leftCnt = bit.sum(x - 1);
                if (leftCnt > 0) {
                    L = bit.kth(leftCnt);
                }
                // find successor
                let R = null;
                const total = bit.sum(n);
                const cntLeX = bit.sum(x);
                if (cntLeX < total) {
                    R = bit.kth(cntLeX + 1);
                }

                let delta = 0;
                if (L !== null) delta += (x - L > 1 ? 1 : 0);
                if (R !== null) delta += (R - x > 1 ? 1 : 0);
                if (L !== null && R !== null) delta -= (R - L > 1 ? 1 : 0);

                curImbalance += delta;
                bit.add(x, 1);
                present[x] = true;
            }
            answer += curImbalance;
        }
    }

    return answer;
};
```

## Typescript

```typescript
function sumImbalanceNumbers(nums: number[]): number {
    const n = nums.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        const seen = new Array(n + 2).fill(false);
        let blocks = 0;
        for (let j = i; j < n; ++j) {
            const x = nums[j];
            if (!seen[x]) {
                const left = seen[x - 1];
                const right = seen[x + 1];
                if (!left && !right) {
                    blocks += 1;
                } else if (left && right) {
                    blocks -= 1;
                }
                seen[x] = true;
            }
            if (blocks > 0) total += blocks - 1;
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumImbalanceNumbers($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        $maxVal = max($nums);
        $ans = 0;

        for ($i = 0; $i < $n; ++$i) {
            // presence array for values 0..$maxVal+1
            $present = array_fill(0, $maxVal + 2, false);
            $imbalance = 0;
            for ($j = $i; $j < $n; ++$j) {
                $x = $nums[$j];
                if (!$present[$x]) {
                    $left  = $present[$x - 1] ?? false;
                    $right = $present[$x + 1] ?? false;

                    if (!$left && !$right) {
                        $imbalance += 1;
                    } elseif ($left && $right) {
                        $imbalance -= 1;
                    }
                    $present[$x] = true;
                }
                $ans += $imbalance;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func sumImbalanceNumbers(_ nums: [Int]) -> Int {
        let n = nums.count
        var total = 0
        for i in 0..<n {
            var present = Array(repeating: false, count: n + 3) // indices up to n+2 safe
            var components = 0
            for j in i..<n {
                let x = nums[j]
                if !present[x] {
                    let leftAdj = present[x - 1]
                    let rightAdj = present[x + 1]
                    if !leftAdj && !rightAdj {
                        components += 1
                    } else if leftAdj && rightAdj {
                        components -= 1
                    }
                    present[x] = true
                }
                if components > 0 {
                    total += components - 1
                }
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumImbalanceNumbers(nums: IntArray): Int {
        val n = nums.size
        var total = 0L
        for (i in 0 until n) {
            val present = BooleanArray(n + 2)
            var cur = 0
            for (j in i until n) {
                val x = nums[j]
                if (!present[x]) {
                    val left = present[x - 1]
                    val right = present[x + 1]
                    when {
                        left && right -> cur--
                        !left && !right -> cur++
                    }
                    present[x] = true
                }
                total += cur
            }
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int sumImbalanceNumbers(List<int> nums) {
    int n = nums.length;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      List<bool> present = List.filled(n + 2, false);
      int cur = -1;
      for (int j = i; j < n; ++j) {
        int v = nums[j];
        if (!present[v]) {
          bool leftAdj = v > 1 && present[v - 1];
          bool rightAdj = v < n && present[v + 1];
          if (!leftAdj && !rightAdj) {
            cur += 1;
          } else if (leftAdj && rightAdj) {
            cur -= 1;
          }
          present[v] = true;
        }
        ans += cur;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func sumImbalanceNumbers(nums []int) int {
    n := len(nums)
    maxVal := n + 2
    ans := 0

    for l := 0; l < n; l++ {
        bit := make([]int, maxVal+1)
        present := make([]bool, maxVal+1)
        imbalance := 0
        for r := l; r < n; r++ {
            v := nums[r]
            if !present[v] {
                // predecessor
                pre := -1
                cntBefore := sum(bit, v-1)
                if cntBefore > 0 {
                    pre = lowerBound(bit, cntBefore)
                }
                // successor
                suc := -1
                total := sum(bit, maxVal)
                cntUpToV := sum(bit, v)
                if total-cntUpToV > 0 {
                    suc = lowerBound(bit, cntUpToV+1)
                }

                oldGap, newGap := 0, 0
                if pre != -1 && suc != -1 {
                    if suc-pre > 1 {
                        oldGap = 1
                    }
                    if v-pre > 1 {
                        newGap++
                    }
                    if suc-v > 1 {
                        newGap++
                    }
                } else if pre != -1 {
                    if v-pre > 1 {
                        newGap = 1
                    }
                } else if suc != -1 {
                    if suc-v > 1 {
                        newGap = 1
                    }
                }

                imbalance += newGap - oldGap

                present[v] = true
                add(bit, v, 1)
            }
            ans += imbalance
        }
    }
    return ans
}

func add(bit []int, idx, delta int) {
    for i := idx; i < len(bit); i += i & -i {
        bit[i] += delta
    }
}

func sum(bit []int, idx int) int {
    res := 0
    for i := idx; i > 0; i -= i & -i {
        res += bit[i]
    }
    return res
}

// returns smallest index such that prefix sum >= k (k >= 1)
func lowerBound(bit []int, k int) int {
    idx := 0
    n := len(bit) - 1
    mask := 1
    for mask<<1 <= n {
        mask <<= 1
    }
    for mask != 0 {
        next := idx + mask
        if next <= n && bit[next] < k {
            k -= bit[next]
            idx = next
        }
        mask >>= 1
    }
    return idx + 1
}
```

## Ruby

```ruby
class BIT
  def initialize(size)
    @size = size
    @tree = Array.new(size + 2, 0)
  end

  def add(idx, delta)
    i = idx
    while i <= @size
      @tree[i] += delta
      i += i & -i
    end
  end

  def sum(idx)
    res = 0
    i = idx
    while i > 0
      res += @tree[i]
      i -= i & -i
    end
    res
  end

  # smallest index such that prefix sum >= k (k >= 1)
  def kth(k)
    idx = 0
    bitmask = 1
    while bitmask <= @size
      bitmask <<= 1
    end
    while bitmask > 0
      t = idx + bitmask
      if t <= @size && @tree[t] < k
        idx = t
        k -= @tree[t]
      end
      bitmask >>= 1
    end
    idx + 1
  end
end

# @param {Integer[]} nums
# @return {Integer}
def sum_imbalance_numbers(nums)
  n = nums.length
  max_val = n + 2
  total = 0

  (0...n).each do |left|
    bit = BIT.new(max_val)
    cur = 0
    (left...n).each do |right|
      v = nums[right]

      pred = nil
      succ = nil

      cnt_left = bit.sum(v - 1)
      pred = bit.kth(cnt_left) if cnt_left > 0

      total_present = bit.sum(max_val)
      cnt_up_to_v = bit.sum(v)
      if total_present - cnt_up_to_v > 0
        succ = bit.kth(cnt_up_to_v + 1)
      end

      if pred && succ
        cur -= (succ - pred > 1 ? 1 : 0)
        cur += (v - pred > 1 ? 1 : 0)
        cur += (succ - v > 1 ? 1 : 0)
      elsif pred
        cur += (v - pred > 1 ? 1 : 0)
      elsif succ
        cur += (succ - v > 1 ? 1 : 0)
      end

      bit.add(v, 1)
      total += cur
    end
  end

  total
end
```

## Scala

```scala
import java.util.TreeSet

object Solution {
  def sumImbalanceNumbers(nums: Array[Int]): Int = {
    val n = nums.length
    var total: Long = 0L
    for (i <- 0 until n) {
      val set = new TreeSet[Int]()
      var imb = 0
      for (j <- i until n) {
        val x = nums(j)
        if (!set.contains(x)) {
          val lower = set.lower(x)   // may be null
          val higher = set.higher(x) // may be null
          var delta = 0
          if (lower != null && higher != null) {
            if (higher - lower > 1) delta -= 1
            if (x - lower > 1) delta += 1
            if (higher - x > 1) delta += 1
          } else if (lower != null) {
            if (x - lower > 1) delta += 1
          } else if (higher != null) {
            if (higher - x > 1) delta += 1
          }
          imb += delta
          set.add(x)
        }
        total += imb
      }
    }
    total.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_imbalance_numbers(nums: Vec<i32>) -> i32 {
        use std::collections::BTreeSet;
        let n = nums.len();
        let mut total: i64 = 0;
        for left in 0..n {
            let mut set: BTreeSet<i32> = BTreeSet::new();
            let mut cur: i32 = 0;
            for right in left..n {
                let x = nums[right];
                if !set.contains(&x) {
                    // find predecessor and successor
                    let pred_opt = set.range(..x).next_back().cloned();
                    let succ_opt = set.range((x + 1)..).next().cloned();

                    // remove old contribution between pred and succ
                    if let (Some(pred), Some(succ)) = (pred_opt, succ_opt) {
                        if succ - pred > 1 {
                            cur -= 1;
                        }
                    }

                    // add new contributions
                    if let Some(pred) = pred_opt {
                        if x - pred > 1 {
                            cur += 1;
                        }
                    }
                    if let Some(succ) = succ_opt {
                        if succ - x > 1 {
                            cur += 1;
                        }
                    }

                    set.insert(x);
                }
                total += cur as i64;
            }
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (sum-imbalance-numbers nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (max-val (if (null? nums) 0 (apply max nums))))
    (define (make-bit size)
      (make-vector (+ size 2) 0))
    (define (bit-add! bit idx delta)
      (let loop ((i idx))
        (when (<= i (- (vector-length bit) 2))
          (vector-set! bit i (+ (vector-ref bit i) delta))
          (loop (+ i (bitwise-and i (- i)))))))
    (define (bit-sum bit idx)
      (let loop ((i idx) (acc 0))
        (if (= i 0)
            acc
            (loop (bitwise-and i (- i)) (+ acc (vector-ref bit i))))))
    ;; find smallest index such that prefix sum >= k (k is 1‑based)
    (define (bit-find-by-order bit k)
      (let ((lo 1) (hi (- (vector-length bit) 2)))
        (let loop ()
          (if (= lo hi)
              lo
              (let* ((mid (quotient (+ lo hi) 2))
                     (s (bit-sum bit mid)))
                (if (< s k)
                    (begin (set! lo (+ mid 1)) (loop))
                    (begin (set! hi mid) (loop))))))))
    (define total 0)
    (for ([l (in-range n)])
      (let ((size max-val)
            (bit (make-bit max-val))
            (imbalance 0))
        (for ([r (in-range l n)])
          (let* ((v (list-ref nums r))
                 ;; predecessor
                 (cnt-left (if (> v 1) (bit-sum bit (- v 1)) 0))
                 (pred (and (> cnt-left 0) (bit-find-by-order bit cnt-left)))
                 ;; successor
                 (cnt-up-to-v (bit-sum bit v))
                 (total-present (bit-sum bit max-val))
                 (succ (and (< cnt-up-to-v total-present)
                            (bit-find-by-order bit (+ cnt-up-to-v 1)))))
            (when pred
              (when (> (- v pred) 1) (set! imbalance (+ imbalance 1))))
            (when succ
              (when (> (- succ v) 1) (set! imbalance (+ imbalance 1))))
            (when (and pred succ)
              (when (> (- succ pred) 1) (set! imbalance (- imbalance 1))))
            (bit-add! bit v 1)
            (set! total (+ total imbalance)))))
    total)))
```

## Erlang

```erlang
-spec sum_imbalance_numbers(Nums :: [integer()]) -> integer().
sum_imbalance_numbers(Nums) ->
    Arr = list_to_tuple(Nums),
    N = tuple_size(Arr),
    sum_left(0, N, Arr, 0).

%% iterate over left index
sum_left(L, N, _Arr, Acc) when L >= N ->
    Acc;
sum_left(L, N, Arr, Acc) ->
    SumForL = sum_right(L, L, N, Arr, gb_sets:new(), 0, 0),
    sum_left(L + 1, N, Arr, Acc + SumForL).

%% iterate over right index for a fixed left
sum_right(_L, R, N, _Arr, _Set, _Cur, Sum) when R >= N ->
    Sum;
sum_right(L, R, N, Arr, Set, Cur, Sum) ->
    X = element(R + 1, Arr),
    case gb_sets:is_element(X, Set) of
        true ->
            NewSet = Set,
            NewCur = Cur;
        false ->
            LeftAdj = gb_sets:is_element(X - 1, Set),
            RightAdj = gb_sets:is_element(X + 1, Set),
            Delta = case {LeftAdj, RightAdj} of
                        {false, false} -> 1;
                        {true, true}   -> -1;
                        _              -> 0
                    end,
            NewCur = Cur + Delta,
            NewSet = gb_sets:add(X, Set)
    end,
    NewSum = Sum + NewCur,
    sum_right(L, R + 1, N, Arr, NewSet, NewCur, NewSum).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_imbalance_numbers(nums :: [integer]) :: integer
  def sum_imbalance_numbers(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)

    Enum.reduce(0..(n - 1), 0, fn left, total ->
      {_, _, cur, sub_sum} =
        Enum.reduce(left..(n - 1), {:gb_sets.empty(), %{}, 0, 0}, fn right,
                                                                   {set, freq, cur, sum} ->
          x = elem(arr, right)
          cnt = Map.get(freq, x, 0)

          {new_set, new_cur} =
            if cnt == 0 do
              # find predecessor and successor in the ordered set
              p_raw = :gb_sets.prev(set, x)
              s_raw = :gb_sets.next(set, x)

              p = if p_raw == :none, do: nil, else: p_raw end
              s = if s_raw == :none, do: nil, else: s_raw end

              old_gap =
                case {p, s} do
                  {nil, _} -> 0
                  {_, nil} -> 0
                  {pp, ss} -> if ss - pp > 1, do: 1, else: 0
                end

              new_gap =
                (if p != nil and x - p > 1, do: 1, else: 0) +
                  (if s != nil and s - x > 1, do: 1, else: 0)

              {:gb_sets.add(x, set), cur + new_gap - old_gap}
            else
              {set, cur}
            end

          new_freq = Map.put(freq, x, cnt + 1)
          {new_set, new_freq, new_cur, sum + new_cur}
        end)

      total + sub_sum
    end)
  end
end
```
