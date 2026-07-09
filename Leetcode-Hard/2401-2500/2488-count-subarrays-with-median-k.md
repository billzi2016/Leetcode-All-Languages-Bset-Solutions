# 2488. Count Subarrays With Median K

## Cpp

```cpp
class Solution {
public:
    int countSubarrays(std::vector<int>& nums, int k) {
        int n = nums.size();
        int pos = -1;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == k) { pos = i; break; }
        }
        std::unordered_map<int, long long> freq;
        int bal = 0;
        freq[0] = 1; // empty left part
        for (int i = pos - 1; i >= 0; --i) {
            if (nums[i] > k) ++bal;
            else --bal;
            ++freq[bal];
        }
        long long ans = 0;
        int rightBal = 0;
        for (int i = pos; i < n; ++i) {
            if (i != pos) {
                if (nums[i] > k) ++rightBal;
                else --rightBal;
            }
            ans += freq[-rightBal];
            ans += freq[1 - rightBal];
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int countSubarrays(int[] nums, int k) {
        int n = nums.length;
        int pos = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == k) {
                pos = i;
                break;
            }
        }

        java.util.HashMap<Integer, Integer> leftCount = new java.util.HashMap<>();
        leftCount.put(0, 1);
        int balance = 0;
        for (int i = pos - 1; i >= 0; i--) {
            if (nums[i] > k) {
                balance++;
            } else { // nums[i] < k because distinct
                balance--;
            }
            leftCount.merge(balance, 1, Integer::sum);
        }

        long ans = 0;
        int rightBalance = 0;
        for (int i = pos; i < n; i++) {
            if (nums[i] > k) {
                rightBalance++;
            } else if (nums[i] < k) {
                rightBalance--;
            }
            ans += leftCount.getOrDefault(-rightBalance, 0);
            ans += leftCount.getOrDefault(1 - rightBalance, 0);
        }

        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pos = nums.index(k)
        from collections import defaultdict

        left_counts = defaultdict(int)
        balance = 0
        left_counts[0] = 1  # empty prefix on the left

        # Process elements to the left of k
        for i in range(pos - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:  # nums[i] < k (distinct values)
                balance -= 1
            left_counts[balance] += 1

        ans = 0
        balance = 0
        # Process elements from k to the right end
        for i in range(pos, len(nums)):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            # else nums[i] == k contributes 0

            ans += left_counts.get(-balance, 0) + left_counts.get(1 - balance, 0)

        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        idx = nums.index(k)

        left_counts = defaultdict(int)
        balance = 0
        left_counts[0] = 1  # empty prefix to the left of k

        for i in range(idx - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:  # nums[i] < k because distinct
                balance -= 1
            left_counts[balance] += 1

        ans = 0
        balance = 0
        for i in range(idx, n):
            if i == idx:
                pass  # value contributes 0
            else:
                if nums[i] > k:
                    balance += 1
                else:  # nums[i] < k
                    balance -= 1
            ans += left_counts.get(-balance, 0) + left_counts.get(1 - balance, 0)

        return ans
```

## C

```c
int countSubarrays(int* nums, int numsSize, int k) {
    int pos = -1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == k) { pos = i; break; }
    }
    int offset = numsSize;
    int size = 2 * numsSize + 3;
    long long* cnt = (long long*)calloc(size, sizeof(long long));
    long long ans = 0;
    
    int sum = 0;
    cnt[offset] = 1; // empty prefix on the left
    
    for (int i = pos - 1; i >= 0; --i) {
        int val = nums[i] > k ? 1 : -1;
        sum += val;
        cnt[offset + sum]++;
    }
    
    int rsum = 0;
    for (int j = pos; j < numsSize; ++j) {
        if (j != pos) {
            int val = nums[j] > k ? 1 : -1;
            rsum += val;
        }
        int idx0 = offset - rsum;
        if (idx0 >= 0 && idx0 < size) ans += cnt[idx0];
        int idx1 = offset + 1 - rsum;
        if (idx1 >= 0 && idx1 < size) ans += cnt[idx1];
    }
    
    free(cnt);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountSubarrays(int[] nums, int k) {
        int n = nums.Length;
        int pos = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == k) { pos = i; break; }
        }

        var leftCount = new Dictionary<int, long>();
        int balance = 0;
        leftCount[0] = 1; // empty prefix to the left of k

        for (int i = pos - 1; i >= 0; i--) {
            if (nums[i] > k) balance++;
            else balance--;
            if (!leftCount.ContainsKey(balance)) leftCount[balance] = 0;
            leftCount[balance]++;
        }

        long result = 0;
        balance = 0;
        for (int i = pos; i < n; i++) {
            if (i != pos) {
                if (nums[i] > k) balance++;
                else balance--;
            }
            // need total sum 0 or 1
            int needZero = -balance;
            int needOne = 1 - balance;

            long cntZero = 0, cntOne = 0;
            leftCount.TryGetValue(needZero, out cntZero);
            leftCount.TryGetValue(needOne, out cntOne);
            result += cntZero + cntOne;
        }

        return (int)result;
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
var countSubarrays = function(nums, k) {
    const n = nums.length;
    const pos = nums.indexOf(k);
    
    // Count balances on the left side of k (including empty prefix)
    const leftCount = new Map();
    let bal = 0;
    leftCount.set(0, 1); // empty prefix
    
    for (let i = pos - 1; i >= 0; --i) {
        bal += nums[i] > k ? 1 : -1;
        leftCount.set(bal, (leftCount.get(bal) || 0) + 1);
    }
    
    let ans = 0;
    let rightBal = 0;
    
    for (let i = pos; i < n; ++i) {
        if (i > pos) {
            rightBal += nums[i] > k ? 1 : -1;
        }
        // Need left balance such that total is 0 or 1
        ans += (leftCount.get(-rightBal) || 0) + (leftCount.get(1 - rightBal) || 0);
    }
    
    return ans;
};
```

## Typescript

```typescript
function countSubarrays(nums: number[], k: number): number {
    const n = nums.length;
    let pos = -1;
    for (let i = 0; i < n; i++) {
        if (nums[i] === k) {
            pos = i;
            break;
        }
    }

    const transformed = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        if (nums[i] > k) transformed[i] = 1;
        else if (nums[i] < k) transformed[i] = -1;
        else transformed[i] = 0;
    }

    const leftMap = new Map<number, number>();
    let sum = 0;
    leftMap.set(0, 1);
    for (let i = pos - 1; i >= 0; i--) {
        sum += transformed[i];
        leftMap.set(sum, (leftMap.get(sum) ?? 0) + 1);
    }

    let ans = 0;
    let rightSum = 0;
    for (let j = pos; j < n; j++) {
        if (j > pos) rightSum += transformed[j];
        const cntZero = leftMap.get(-rightSum) ?? 0;
        const cntOne = leftMap.get(1 - rightSum) ?? 0;
        ans += cntZero + cntOne;
    }

    return ans;
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
    function countSubarrays($nums, $k) {
        $n = count($nums);
        $pos = array_search($k, $nums); // index of k

        // Count prefix sums to the left of k
        $cnt = [];
        $sum = 0;
        $cnt[0] = 1; // empty prefix

        for ($i = $pos - 1; $i >= 0; --$i) {
            if ($nums[$i] > $k) {
                $sum += 1;
            } else { // nums[i] < k (distinct)
                $sum -= 1;
            }
            if (!isset($cnt[$sum])) {
                $cnt[$sum] = 0;
            }
            $cnt[$sum]++;
        }

        $ans = 0;
        $rightSum = 0;

        for ($i = $pos; $i < $n; ++$i) {
            if ($i != $pos) {
                if ($nums[$i] > $k) {
                    $rightSum += 1;
                } else { // nums[i] < k
                    $rightSum -= 1;
                }
            }

            $need1 = -$rightSum;       // total sum == 0
            $need2 = 1 - $rightSum;    // total sum == 1

            if (isset($cnt[$need1])) {
                $ans += $cnt[$need1];
            }
            if (isset($cnt[$need2])) {
                $ans += $cnt[$need2];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pos = -1
        for i in 0..<n {
            if nums[i] == k {
                pos = i
                break
            }
        }
        var freq = [Int:Int]()
        var sum = 0
        freq[0] = 1   // empty left part
        
        // Process elements to the left of k
        if pos > 0 {
            for i in stride(from: pos - 1, through: 0, by: -1) {
                sum += nums[i] > k ? 1 : -1
                freq[sum, default: 0] += 1
            }
        }
        
        var result = 0
        var rightSum = 0
        
        // Process elements from k to the end
        for i in pos..<n {
            if i != pos {
                rightSum += nums[i] > k ? 1 : -1
            }
            let need1 = -rightSum
            let need2 = 1 - rightSum
            if let cnt = freq[need1] {
                result += cnt
            }
            if let cnt = freq[need2] {
                result += cnt
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray, k: Int): Int {
        val n = nums.size
        var pos = -1
        for (i in 0 until n) {
            if (nums[i] == k) {
                pos = i
                break
            }
        }

        // Count prefix sums to the left of position k
        val freq = HashMap<Int, Int>()
        var sum = 0
        freq[0] = 1
        for (i in pos - 1 downTo 0) {
            sum += if (nums[i] > k) 1 else -1
            freq[sum] = (freq[sum] ?: 0) + 1
        }

        var ans = 0L
        var rightSum = 0
        for (i in pos until n) {
            if (i != pos) {
                rightSum += if (nums[i] > k) 1 else -1
            }
            ans += (freq[-rightSum] ?: 0).toLong()
            ans += (freq[1 - rightSum] ?: 0).toLong()
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countSubarrays(List<int> nums, int k) {
    int n = nums.length;
    int idx = nums.indexOf(k);
    Map<int, int> cnt = {0: 1};
    int sum = 0;
    for (int i = idx - 1; i >= 0; --i) {
      int v = nums[i] > k ? 1 : -1;
      sum += v;
      cnt[sum] = (cnt[sum] ?? 0) + 1;
    }
    int ans = 0;
    int rightSum = 0;
    for (int i = idx; i < n; ++i) {
      int v = (i == idx) ? 0 : (nums[i] > k ? 1 : -1);
      rightSum += v;
      ans += cnt[-rightSum] ?? 0;
      ans += cnt[1 - rightSum] ?? 0;
    }
    return ans;
  }
}
```

## Golang

```go
func countSubarrays(nums []int, k int) int {
    n := len(nums)
    pos := -1
    for i, v := range nums {
        if v == k {
            pos = i
            break
        }
    }

    cnt := make(map[int]int)
    bal := 0
    cnt[0] = 1 // empty left side

    // Process elements to the left of k
    for i := pos - 1; i >= 0; i-- {
        if nums[i] > k {
            bal++
        } else { // nums[i] < k (distinct)
            bal--
        }
        cnt[bal]++
    }

    ans := 0
    rightBal := 0

    // Process elements from k to the end
    for j := pos; j < n; j++ {
        if j > pos {
            if nums[j] > k {
                rightBal++
            } else {
                rightBal--
            }
        }
        ans += cnt[-rightBal]
        ans += cnt[1-rightBal]
    }

    return ans
}
```

## Ruby

```ruby
def count_subarrays(nums, k)
  pos = nums.index(k)

  left_counts = Hash.new(0)
  sum = 0
  left_counts[0] = 1

  i = pos - 1
  while i >= 0
    sum += nums[i] > k ? 1 : -1
    left_counts[sum] += 1
    i -= 1
  end

  ans = 0
  right_sum = 0
  i = pos
  while i < nums.length
    if i > pos
      right_sum += nums[i] > k ? 1 : -1
    end
    ans += left_counts[-right_sum]
    ans += left_counts[1 - right_sum]
    i += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        var pos = -1
        for (i <- 0 until n) if (nums(i) == k) { pos = i }
        import scala.collection.mutable
        val cnt = mutable.Map[Int, Int]().withDefaultValue(0)
        var sumLeft = 0
        cnt(0) = 1
        for (i <- (pos - 1) to 0 by -1) {
            if (nums(i) > k) sumLeft += 1 else sumLeft -= 1
            cnt(sumLeft) = cnt(sumLeft) + 1
        }
        var ans: Long = 0L
        var sumRight = 0
        for (i <- pos until n) {
            ans += cnt.getOrElse(-sumRight, 0)
            ans += cnt.getOrElse(1 - sumRight, 0)
            if (i + 1 < n) {
                if (nums(i + 1) > k) sumRight += 1 else sumRight -= 1
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        // locate position of k
        let mut pos = 0usize;
        for (i, &v) in nums.iter().enumerate() {
            if v == k {
                pos = i;
                break;
            }
        }

        use std::collections::HashMap;
        let mut left_cnt: HashMap<i32, i64> = HashMap::new();

        // balance for the empty prefix on the left side
        *left_cnt.entry(0).or_insert(0) += 1;
        let mut bal = 0i32;
        // compute balances to the left of k
        for i in (0..pos).rev() {
            if nums[i] > k {
                bal += 1;
            } else {
                bal -= 1; // nums[i] < k because all distinct and only one equals k
            }
            *left_cnt.entry(bal).or_insert(0) += 1;
        }

        let mut ans: i64 = 0;
        let mut right_bal = 0i32;
        // iterate over subarrays that end at or after k
        for j in pos..n {
            if j > pos {
                if nums[j] > k {
                    right_bal += 1;
                } else {
                    right_bal -= 1; // nums[j] < k
                }
            }
            // need left balance such that total sum is 0 or 1
            let need_zero = -right_bal;
            let need_one = 1 - right_bal;

            if let Some(&cnt) = left_cnt.get(&need_zero) {
                ans += cnt;
            }
            if let Some(&cnt) = left_cnt.get(&need_one) {
                ans += cnt;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((vec (list->vector nums))
         (n (vector-length vec))
         (pos
          (let loop ((i 0))
            (if (= (vector-ref vec i) k)
                i
                (loop (+ i 1)))))
         (cnt (make-hash)))
    ;; count prefix balances to the left of k (including empty prefix)
    (hash-set! cnt 0 1)
    (let ((balance 0))
      (for ([i (in-range (- pos 1) -1 -1)])
        (let ((val (vector-ref vec i)))
          (cond [(> val k) (set! balance (+ balance 1))]
                [(< val k) (set! balance (- balance 1))]))
        (hash-set! cnt balance (+ (hash-ref cnt balance 0) 1))))
    ;; traverse to the right, combining with left counts
    (let ((ans 0)
          (balance 0))
      (for ([j (in-range pos n)])
        (when (> j pos)
          (let ((val (vector-ref vec j)))
            (cond [(> val k) (set! balance (+ balance 1))]
                  [(< val k) (set! balance (- balance 1))])))
        (define left0 (hash-ref cnt (- balance) 0))
        (define left1 (hash-ref cnt (- 1 balance) 0))
        (set! ans (+ ans left0 left1)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_subarrays/2]).

-spec count_subarrays(Nums :: [integer()], K :: integer()) -> integer().
count_subarrays(Nums, K) ->
    N = length(Nums),
    T = list_to_tuple(Nums),
    Pos = find_pos(T, K, 0, N),
    LeftFreq = build_left_freq(T, K, Pos - 1, #{0 => 1}, 0),
    count_right(T, K, Pos, N - 1, LeftFreq).

find_pos(_T, _K, I, N) when I >= N -> -1;
find_pos(T, K, I, N) ->
    case element(I + 1, T) of
        K -> I;
        _ -> find_pos(T, K, I + 1, N)
    end.

build_left_freq(_T, _K, I, Map, _Bal) when I < 0 -> Map;
build_left_freq(T, K, I, Map, Bal) ->
    Val = element(I + 1, T),
    Delta = if Val > K -> 1; true -> -1 end,
    NewBal = Bal + Delta,
    Count = maps:get(NewBal, Map, 0),
    NewMap = maps:put(NewBal, Count + 1, Map),
    build_left_freq(T, K, I - 1, NewMap, NewBal).

count_right(T, K, Pos, EndIdx, LeftFreq) ->
    count_right(T, K, Pos, EndIdx, LeftFreq, 0, 0).

count_right(_T, _K, I, EndIdx, _LeftFreq, _BalR, Ans) when I > EndIdx -> Ans;
count_right(T, K, I, EndIdx, LeftFreq, BalR, Ans) ->
    Contribution = maps:get(-BalR, LeftFreq, 0) + maps:get(1 - BalR, LeftFreq, 0),
    NewAns = Ans + Contribution,
    if I == EndIdx ->
            NewAns;
       true ->
            NextVal = element(I + 2, T),
            Delta = if NextVal > K -> 1; true -> -1 end,
            NewBalR = BalR + Delta,
            count_right(T, K, I + 1, EndIdx, LeftFreq, NewBalR, NewAns)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer], k :: integer) :: integer
  def count_subarrays(nums, k) do
    pos = Enum.find_index(nums, fn x -> x == k end)

    {bal_left, map_left} =
      Enum.reduce(Enum.take(nums, pos), {0, %{0 => 1}}, fn num, {bal, mp} ->
        bal =
          cond do
            num > k -> bal + 1
            num < k -> bal - 1
            true -> bal
          end

        cnt = Map.get(mp, bal, 0)
        {bal, Map.put(mp, bal, cnt + 1)}
      end)

    ans_initial =
      Map.get(map_left, bal_left, 0) + Map.get(map_left, bal_left - 1, 0)

    cnt_k = Map.get(map_left, bal_left, 0)
    map_with_k = Map.put(map_left, bal_left, cnt_k + 1)

    {_, ans_final, _} =
      Enum.reduce(Enum.drop(nums, pos + 1), {bal_left, ans_initial, map_with_k}, fn num,
                                                                                 {bal, acc, mp} ->
        bal =
          cond do
            num > k -> bal + 1
            num < k -> bal - 1
            true -> bal
          end

        add = Map.get(mp, bal, 0) + Map.get(mp, bal - 1, 0)
        {bal, acc + add, mp}
      end)

    ans_final
  end
end
```
