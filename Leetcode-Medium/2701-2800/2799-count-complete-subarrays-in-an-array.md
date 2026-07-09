# 2799. Count Complete Subarrays in an Array

## Cpp

```cpp
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        const int MAXV = 2000;
        vector<bool> seen(MAXV + 1, false);
        int totalDistinct = 0;
        for (int x : nums) {
            if (!seen[x]) {
                seen[x] = true;
                ++totalDistinct;
            }
        }
        vector<int> freq(MAXV + 1, 0);
        int distinct = 0;
        long long ans = 0;
        int n = nums.size();
        int r = 0;
        for (int l = 0; l < n; ++l) {
            while (r < n && distinct < totalDistinct) {
                if (++freq[nums[r]] == 1) ++distinct;
                ++r;
            }
            if (distinct == totalDistinct) {
                ans += n - r + 1;
            } else {
                break; // cannot satisfy further left positions
            }
            if (--freq[nums[l]] == 0) --distinct;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int countCompleteSubarrays(int[] nums) {
        int n = nums.length;
        java.util.HashSet<Integer> totalSet = new java.util.HashSet<>();
        for (int v : nums) totalSet.add(v);
        int need = totalSet.size();
        if (need == 1) return n * (n + 1) / 2;

        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        int distinct = 0;
        long ans = 0;
        int right = 0;

        for (int left = 0; left < n; left++) {
            while (right < n && distinct < need) {
                int val = nums[right];
                int cnt = freq.getOrDefault(val, 0);
                if (cnt == 0) distinct++;
                freq.put(val, cnt + 1);
                right++;
            }
            if (distinct == need) {
                ans += n - right + 1;
            } else {
                break;
            }

            int leftVal = nums[left];
            int cntLeft = freq.get(leftVal);
            if (cntLeft == 1) {
                freq.remove(leftVal);
                distinct--;
            } else {
                freq.put(leftVal, cntLeft - 1);
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_distinct = len(set(nums))
        cnt = {}
        distinct_in_window = 0
        right = 0
        result = 0

        for left in range(n):
            # expand right until we have all distinct elements or reach end
            while right < n and distinct_in_window < total_distinct:
                x = nums[right]
                if cnt.get(x, 0) == 0:
                    distinct_in_window += 1
                cnt[x] = cnt.get(x, 0) + 1
                right += 1

            # if window contains all distinct elements, count subarrays
            if distinct_in_window == total_distinct:
                result += n - right + 1

            # shrink from left for next iteration
            y = nums[left]
            cnt[y] -= 1
            if cnt[y] == 0:
                distinct_in_window -= 1
                del cnt[y]

        return result
```

## Python3

```python
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)
        cnt = {}
        cur_dist = 0
        right = 0
        ans = 0

        for left in range(n):
            while right < n and cur_dist < total_distinct:
                x = nums[right]
                cnt[x] = cnt.get(x, 0) + 1
                if cnt[x] == 1:
                    cur_dist += 1
                right += 1

            if cur_dist == total_distinct:
                ans += n - right + 1
            else:
                break

            y = nums[left]
            cnt[y] -= 1
            if cnt[y] == 0:
                cur_dist -= 1
                del cnt[y]

        return ans
```

## C

```c
int countCompleteSubarrays(int* nums, int numsSize){
    int freq[2001] = {0};
    int seen[2001] = {0};
    int totalDistinct = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (!seen[nums[i]]) {
            seen[nums[i]] = 1;
            ++totalDistinct;
        }
    }
    long long ans = 0;
    int distinctInWindow = 0;
    int right = 0;
    for (int left = 0; left < numsSize; ++left) {
        while (right < numsSize && distinctInWindow < totalDistinct) {
            int v = nums[right];
            if (freq[v] == 0) ++distinctInWindow;
            ++freq[v];
            ++right;
        }
        if (distinctInWindow == totalDistinct) {
            ans += (long long)(numsSize - right + 1);
        }
        int vL = nums[left];
        --freq[vL];
        if (freq[vL] == 0) --distinctInWindow;
    }
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int CountCompleteSubarrays(int[] nums) {
        int n = nums.Length;
        var uniqueSet = new HashSet<int>(nums);
        int totalDistinct = uniqueSet.Count;

        var cnt = new Dictionary<int, int>();
        int distinctInWindow = 0;
        long ans = 0;
        int right = 0;

        for (int left = 0; left < n; ++left) {
            while (right < n && distinctInWindow < totalDistinct) {
                int val = nums[right];
                if (!cnt.ContainsKey(val) || cnt[val] == 0) {
                    distinctInWindow++;
                    cnt[val] = 1;
                } else {
                    cnt[val]++;
                }
                right++;
            }

            if (distinctInWindow == totalDistinct) {
                ans += n - right + 1;
            }

            int leftVal = nums[left];
            cnt[leftVal]--;
            if (cnt[leftVal] == 0) {
                distinctInWindow--;
                cnt.Remove(leftVal);
            }
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function(nums) {
    const n = nums.length;
    // total distinct elements in the whole array
    const totalDistinct = new Set(nums).size;

    const cnt = new Map();
    let distinctInWindow = 0;
    let right = 0;
    let result = 0;

    for (let left = 0; left < n; ++left) {
        // expand right until window contains all distinct elements
        while (right < n && distinctInWindow < totalDistinct) {
            const val = nums[right];
            const cur = cnt.get(val) || 0;
            if (cur === 0) distinctInWindow++;
            cnt.set(val, cur + 1);
            right++;
        }

        // if we have a complete subarray starting at left,
        // all extensions to the end are also complete
        if (distinctInWindow === totalDistinct) {
            result += n - right + 1;
        }

        // shrink window from the left for next iteration
        const valL = nums[left];
        const curL = cnt.get(valL);
        if (curL === 1) {
            cnt.delete(valL);
            distinctInWindow--;
        } else {
            cnt.set(valL, curL - 1);
        }
    }

    return result;
};
```

## Typescript

```typescript
function countCompleteSubarrays(nums: number[]): number {
    const n = nums.length;
    // total distinct elements in the whole array
    const totalSet = new Set<number>(nums);
    const totalDistinct = totalSet.size;

    const freq = new Map<number, number>();
    let distinctCount = 0;
    let right = -1;
    let result = 0;

    for (let left = 0; left < n; left++) {
        // expand right until we have all distinct elements or reach end
        while (right + 1 < n && distinctCount < totalDistinct) {
            right++;
            const val = nums[right];
            const cnt = (freq.get(val) ?? 0) + 1;
            freq.set(val, cnt);
            if (cnt === 1) distinctCount++;
        }

        // if current window contains all distinct elements
        if (distinctCount === totalDistinct) {
            result += n - right;
        } else {
            // cannot find further windows for larger left either
            break;
        }

        // shrink from the left before moving to next left
        const leftVal = nums[left];
        const leftCnt = freq.get(leftVal)! - 1;
        if (leftCnt === 0) {
            freq.delete(leftVal);
            distinctCount--;
        } else {
            freq.set(leftVal, leftCnt);
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countCompleteSubarrays($nums) {
        $n = count($nums);
        // total distinct elements in the whole array
        $distinctTotal = count(array_unique($nums));
        if ($distinctTotal == 0) return 0;

        $cnt = [];
        $right = 0;
        $curDistinct = 0;
        $result = 0;

        for ($left = 0; $left < $n; $left++) {
            // expand right until we have all distinct elements
            while ($right < $n && $curDistinct < $distinctTotal) {
                $val = $nums[$right];
                if (!isset($cnt[$val]) || $cnt[$val] == 0) {
                    $curDistinct++;
                }
                $cnt[$val] = ($cnt[$val] ?? 0) + 1;
                $right++;
            }

            // if window contains all distinct elements, count subarrays
            if ($curDistinct == $distinctTotal) {
                $result += $n - $right + 1;
            }

            // shrink from left
            $leftVal = $nums[$left];
            $cnt[$leftVal]--;
            if ($cnt[$leftVal] == 0) {
                $curDistinct--;
                unset($cnt[$leftVal]);
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countCompleteSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        let totalDistinct = Set(nums).count
        var cnt = [Int:Int]()
        var distinctInWindow = 0
        var right = 0
        var ans = 0
        
        for left in 0..<n {
            while right < n && distinctInWindow < totalDistinct {
                let val = nums[right]
                let newCount = (cnt[val] ?? 0) + 1
                cnt[val] = newCount
                if newCount == 1 { distinctInWindow += 1 }
                right += 1
            }
            
            if distinctInWindow == totalDistinct {
                ans += n - right + 1
            } else {
                // cannot find a complete subarray starting from this left or any further left
                break
            }
            
            let removeVal = nums[left]
            if let curCount = cnt[removeVal] {
                if curCount == 1 {
                    cnt.removeValue(forKey: removeVal)
                    distinctInWindow -= 1
                } else {
                    cnt[removeVal] = curCount - 1
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
    fun countCompleteSubarrays(nums: IntArray): Int {
        val n = nums.size
        val totalDistinct = nums.toSet().size
        var ans = 0
        val cnt = HashMap<Int, Int>()
        var distinctInWindow = 0
        var right = 0

        for (left in 0 until n) {
            while (right < n && distinctInWindow < totalDistinct) {
                val v = nums[right]
                val c = cnt.getOrDefault(v, 0)
                if (c == 0) distinctInWindow++
                cnt[v] = c + 1
                right++
            }
            if (distinctInWindow == totalDistinct) {
                ans += n - right + 1
            }
            // move left pointer forward
            val vLeft = nums[left]
            val cLeft = cnt[vLeft]!!
            if (cLeft == 1) {
                cnt.remove(vLeft)
                distinctInWindow--
            } else {
                cnt[vLeft] = cLeft - 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countCompleteSubarrays(List<int> nums) {
    int n = nums.length;
    // Total distinct elements in the whole array
    Set<int> distinctSet = {};
    for (int v in nums) distinctSet.add(v);
    int totalDistinct = distinctSet.length;

    Map<int, int> freq = {};
    int distinctCount = 0;
    int ans = 0;
    int right = 0;

    for (int left = 0; left < n; ++left) {
      while (right < n && distinctCount < totalDistinct) {
        int val = nums[right];
        int cnt = freq[val] ?? 0;
        if (cnt == 0) distinctCount++;
        freq[val] = cnt + 1;
        right++;
      }

      if (distinctCount == totalDistinct) {
        ans += n - right + 1;
      } else {
        // No further complete subarrays can be formed
        break;
      }

      int leftVal = nums[left];
      int cntLeft = freq[leftVal]!;
      if (cntLeft == 1) {
        distinctCount--;
        freq.remove(leftVal);
      } else {
        freq[leftVal] = cntLeft - 1;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countCompleteSubarrays(nums []int) int {
    n := len(nums)
    // total distinct elements in the whole array
    uniq := make(map[int]struct{})
    for _, v := range nums {
        uniq[v] = struct{}{}
    }
    need := len(uniq)

    freq := make(map[int]int)
    curDistinct := 0
    ans := 0
    right := 0

    for left := 0; left < n; left++ {
        // expand window to include all distinct elements
        for right < n && curDistinct < need {
            v := nums[right]
            if freq[v] == 0 {
                curDistinct++
            }
            freq[v]++
            right++
        }

        if curDistinct == need {
            ans += n - right + 1
        }

        // shrink window from the left
        v := nums[left]
        freq[v]--
        if freq[v] == 0 {
            delete(freq, v)
            curDistinct--
        }
    }

    return ans
}
```

## Ruby

```ruby
def count_complete_subarrays(nums)
  n = nums.length
  total_distinct = nums.uniq.size
  freq = Hash.new(0)
  distinct_in_window = 0
  right = 0
  ans = 0

  (0...n).each do |left|
    while right < n && distinct_in_window < total_distinct
      val = nums[right]
      freq[val] += 1
      distinct_in_window += 1 if freq[val] == 1
      right += 1
    end
    break if distinct_in_window < total_distinct

    ans += n - (right - 1)

    val = nums[left]
    freq[val] -= 1
    if freq[val] == 0
      distinct_in_window -= 1
      freq.delete(val)
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countCompleteSubarrays(nums: Array[Int]): Int = {
        val n = nums.length
        val totalDistinct = nums.toSet.size
        import scala.collection.mutable.{Map => MutableMap}
        val cnt = MutableMap[Int, Int]()
        var distinctInWindow = 0
        var right = 0
        var result: Long = 0L

        var left = 0
        while (left < n) {
            while (right < n && distinctInWindow < totalDistinct) {
                val v = nums(right)
                cnt.put(v, cnt.getOrElse(v, 0) + 1)
                if (cnt(v) == 1) distinctInWindow += 1
                right += 1
            }
            if (distinctInWindow == totalDistinct) {
                result += (n - right + 1).toLong
            } else {
                // No further complete subarrays possible
                return result.toInt
            }

            val vLeft = nums(left)
            cnt.put(vLeft, cnt(vLeft) - 1)
            if (cnt(vLeft) == 0) {
                cnt.remove(vLeft)
                distinctInWindow -= 1
            }
            left += 1
        }
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_complete_subarrays(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        const MAXV: usize = 2001; // since nums[i] <= 2000
        let mut seen = vec![false; MAXV];
        let mut total_distinct = 0usize;
        for &v in &nums {
            let idx = v as usize;
            if !seen[idx] {
                seen[idx] = true;
                total_distinct += 1;
            }
        }

        let mut cnt = vec![0usize; MAXV];
        let mut cur_distinct = 0usize;
        let mut right = 0usize;
        let mut ans: i64 = 0;

        for left in 0..n {
            while right < n && cur_distinct < total_distinct {
                let idx = nums[right] as usize;
                if cnt[idx] == 0 {
                    cur_distinct += 1;
                }
                cnt[idx] += 1;
                right += 1;
            }

            if cur_distinct == total_distinct {
                ans += (n - right + 1) as i64;
            } else {
                break; // cannot find further complete subarrays
            }

            let idx_left = nums[left] as usize;
            cnt[idx_left] -= 1;
            if cnt[idx_left] == 0 {
                cur_distinct -= 1;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-complete-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    ;; total distinct elements in the whole array
    (let ((total-distinct
           (let ((h (make-hash)))
             (for ([i n])
               (hash-set! h (vector-ref v i) #t))
             (hash-count h))))
      (let ((cnt (make-hash))
            (right 0)
            (distinct-in-window 0)
            (ans 0))
        (define (add x)
          (let* ((prev (hash-ref cnt x 0))
                 (new (+ prev 1)))
            (hash-set! cnt x new)
            (when (= prev 0)
              (set! distinct-in-window (+ distinct-in-window 1)))))
        (define (remove x)
          (let ((prev (hash-ref cnt x)))
            (if (= prev 1)
                (begin
                  (hash-remove! cnt x)
                  (set! distinct-in-window (- distinct-in-window 1)))
                (hash-set! cnt x (- prev 1)))))
        (let loop-left ((left 0))
          (if (>= left n)
              ans
              (begin
                ;; expand right until window has all distinct elements or reaches end
                (let expand ()
                  (when (and (< right n) (< distinct-in-window total-distinct))
                    (add (vector-ref v right))
                    (set! right (+ right 1))
                    (expand)))
                (if (= distinct-in-window total-distinct)
                    (begin
                      (set! ans (+ ans (+ (- n right) 1))) ; add n - right + 1
                      (remove (vector-ref v left))
                      (loop-left (+ left 1)))
                    ans)))))))))
```

## Erlang

```erlang
-spec count_complete_subarrays(Nums :: [integer()]) -> integer().
count_complete_subarrays(Nums) ->
    N = length(Nums),
    Arr = list_to_tuple(Nums),
    DistMap = lists:foldl(
        fun(X, M) ->
            maps:update_with(X, fun(C) -> C + 1 end, 1, M)
        end,
        #{},
        Nums
    ),
    TotalDist = maps:size(DistMap),
    loop(1, 1, N, Arr, TotalDist, #{}, 0, 0).

loop(Left, _Right, N, _Arr, _Tot, _Cnt, _Cur, Ans) when Left > N ->
    Ans;
loop(Left, Right, N, Arr, Tot, Cnt, Cur, Ans) ->
    {NewRight, NewCnt, NewCur} = expand(Right, N, Arr, Tot, Cnt, Cur),
    case NewCur == Tot of
        true ->
            NewAns = Ans + (N - NewRight + 2),
            Xl = element(Left, Arr),
            CountL = maps:get(Xl, NewCnt),
            {UpdCnt, UpdCur} =
                if CountL == 1 ->
                        {maps:remove(Xl, NewCnt), NewCur - 1};
                   true ->
                        {maps:put(Xl, CountL - 1, NewCnt), NewCur}
                end,
            loop(Left + 1, NewRight, N, Arr, Tot, UpdCnt, UpdCur, NewAns);
        false ->
            Ans
    end.

expand(Right, N, _Arr, Tot, Cnt, Cur) when Right > N; Cur >= Tot ->
    {Right, Cnt, Cur};
expand(Right, N, Arr, Tot, Cnt, Cur) ->
    X = element(Right, Arr),
    Prev = maps:get(X, Cnt, 0),
    NewCnt = maps:put(X, Prev + 1, Cnt),
    NewCur = if Prev == 0 -> Cur + 1; true -> Cur end,
    expand(Right + 1, N, Arr, Tot, NewCnt, NewCur).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_complete_subarrays(nums :: [integer]) :: integer
  def count_complete_subarrays(nums) do
    n = length(nums)
    total_distinct = MapSet.new(nums) |> MapSet.size()
    arr = List.to_tuple(nums)

    do_count(0, 0, %{}, 0, 0, n, total_distinct, arr)
  end

  defp do_count(left, right, cnt, distinct, ans, n, k, arr) when left < n do
    {new_right, new_cnt, new_distinct} = expand(right, cnt, distinct, k, n, arr)

    if new_distinct == k do
      ans2 = ans + (n - new_right + 1)
      val_left = elem(arr, left)
      {cnt3, dist3} = dec(new_cnt, val_left, new_distinct)
      do_count(left + 1, new_right, cnt3, dist3, ans2, n, k, arr)
    else
      ans
    end
  end

  defp do_count(_, _, _, _, ans, _, _, _), do: ans

  defp expand(right, cnt, distinct, k, n, arr) when right < n and distinct < k do
    val = elem(arr, right)
    prev = Map.get(cnt, val)

    cnt_new =
      Map.update(cnt, val, 1, fn c -> c + 1 end)

    distinct_new = if prev == nil, do: distinct + 1, else: distinct

    expand(right + 1, cnt_new, distinct_new, k, n, arr)
  end

  defp expand(right, cnt, distinct, _k, _n, _arr), do: {right, cnt, distinct}

  defp dec(cnt, val, distinct) do
    c = Map.get(cnt, val)

    if c == 1 do
      {Map.delete(cnt, val), distinct - 1}
    else
      {Map.put(cnt, val, c - 1), distinct}
    end
  end
end
```
