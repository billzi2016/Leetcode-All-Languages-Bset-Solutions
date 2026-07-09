# 3388. Count Beautiful Splits in an Array

## Cpp

```cpp
class Solution {
public:
    int beautifulSplits(vector<int>& nums) {
        const int MAXV = 51;
        int n = nums.size();
        vector<array<int, MAXV>> pref(n + 1);
        for (int v = 0; v < MAXV; ++v) pref[0][v] = 0;
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i];
            ++pref[i + 1][nums[i]];
        }
        array<int, MAXV> total = pref[n];
        int ans = 0;
        for (int i = 1; i < n; ++i) { // split after i-1
            bool ge = true, le = true;
            for (int v = 0; v < MAXV; ++v) {
                int left = pref[i][v];
                int right = total[v] - left;
                if (left < right) ge = false;
                if (left > right) le = false;
                if (!ge && !le) break;
            }
            if (ge || le) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int beautifulSplits(int[] nums) {
        int n = nums.length;
        if (n < 2) return 0;
        int[] suffixMin = new int[n];
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
        }
        int count = 0;
        int prefixMax = nums[0];
        for (int i = 0; i < n - 1; ++i) {
            if (i > 0) prefixMax = Math.max(prefixMax, nums[i]);
            else prefixMax = nums[0];
            if (prefixMax == suffixMin[i + 1]) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def beautifulSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        total = Counter(nums)
        suffix = dict(total)          # remaining counts in the right part
        prefix = {}
        bad = 0                       # number of values present in prefix but absent in suffix
        ans = 0
        n = len(nums)
        for i in range(n - 1):        # split after position i, both parts non‑empty
            v = nums[i]
            # move v from suffix to prefix
            prefix[v] = prefix.get(v, 0) + 1
            suffix[v] -= 1
            if suffix[v] == 0 and prefix[v] > 0:
                bad += 1
            if bad == 0:
                ans += 1
        return ans
```

## Python3

```python
class Solution:
    def beautifulSplits(self, nums):
        n = len(nums)
        ans = 0
        for i in range(1, n):
            left_len = i
            right_len = n - i
            if left_len <= right_len:
                # check if left is a subsequence of right
                j = 0
                for x in nums[i:]:
                    if x == nums[j]:
                        j += 1
                        if j == left_len:
                            break
                if j == left_len:
                    ans += 1
            else:
                # check if right is a subsequence of left
                j = 0
                for x in nums[:i]:
                    if x == nums[i + j]:
                        j += 1
                        if j == right_len:
                            break
                if j == right_len:
                    ans += 1
        return ans
```

## C

```c
int beautifulSplits(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    int *prefMax = (int*)malloc(numsSize * sizeof(int));
    int *sufMin = (int*)malloc(numsSize * sizeof(int));
    prefMax[0] = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        prefMax[i] = prefMax[i-1] > nums[i] ? prefMax[i-1] : nums[i];
    }
    sufMin[numsSize-1] = nums[numsSize-1];
    for (int i = numsSize - 2; i >= 0; --i) {
        sufMin[i] = sufMin[i+1] < nums[i] ? sufMin[i+1] : nums[i];
    }
    int count = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        if (prefMax[i] == sufMin[i+1]) {
            ++count;
        }
    }
    free(prefMax);
    free(sufMin);
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int BeautifulSplits(int[] nums) {
        int n = nums.Length;
        if (n < 2) return 0;

        int[] prefMax = new int[n];
        int[] suffMin = new int[n];

        prefMax[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefMax[i] = Math.Max(prefMax[i - 1], nums[i]);
        }

        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.Min(suffMin[i + 1], nums[i]);
        }

        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            if (prefMax[i] == suffMin[i + 1]) {
                count++;
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var beautifulSplits = function(nums) {
    const n = nums.length;
    if (n < 2) return 0;

    const MAX_VAL = 51; // given constraint 0 <= nums[i] <= 50
    const prefixMax = new Array(n);
    const suffixMax = new Array(n);

    let freq = new Array(MAX_VAL).fill(0);
    let curMax = 0;
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        freq[v]++;
        if (freq[v] > curMax) curMax = freq[v];
        prefixMax[i] = curMax;
    }

    freq.fill(0);
    curMax = 0;
    for (let i = n - 1; i >= 0; --i) {
        const v = nums[i];
        freq[v]++;
        if (freq[v] > curMax) curMax = freq[v];
        suffixMax[i] = curMax;
    }

    let ans = 0;
    for (let i = 0; i < n - 1; ++i) {
        if (prefixMax[i] > suffixMax[i + 1]) ans++;
    }
    return ans;
};
```

## Typescript

```typescript
function beautifulSplits(nums: number[]): number {
    const MAX_VAL = 51;
    const total = new Array(MAX_VAL).fill(0);
    for (const x of nums) total[x]++;

    const prefix = new Array(MAX_VAL).fill(0);
    let ans = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        const v = nums[i];
        prefix[v]++;

        let hasPos = false;
        let hasNeg = false;
        for (let val = 0; val < MAX_VAL; val++) {
            const diff = prefix[val] - (total[val] - prefix[val]); // left - right
            if (diff > 0) hasPos = true;
            else if (diff < 0) hasNeg = true;
            if (hasPos && hasNeg) break;
        }
        if (!(hasPos && hasNeg)) ans++;
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
    function beautifulSplits($nums) {
        $n = count($nums);
        if ($n < 2) return 0;

        // Prefix maximum frequencies
        $prefMax = array_fill(0, $n, 0);
        $cnt = array_fill(0, 51, 0);   // nums[i] <= 50
        $curMax = 0;
        for ($i = 0; $i < $n; $i++) {
            $v = $nums[$i];
            $cnt[$v]++;
            if ($cnt[$v] > $curMax) {
                $curMax = $cnt[$v];
            }
            $prefMax[$i] = $curMax;
        }

        // Suffix maximum frequencies
        $suffMax = array_fill(0, $n, 0);
        $cnt = array_fill(0, 51, 0);
        $curMax = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $v = $nums[$i];
            $cnt[$v]++;
            if ($cnt[$v] > $curMax) {
                $curMax = $cnt[$v];
            }
            $suffMax[$i] = $curMax;
        }

        // Count beautiful splits
        $ans = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($prefMax[$i] > $suffMax[$i + 1]) {
                $ans++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulSplits(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 2 { return 0 }
        // prefix distinct count
        var prefDistinct = Array(repeating: 0, count: n)
        var seenPref = Set<Int>()
        for i in 0..<n {
            seenPref.insert(nums[i])
            prefDistinct[i] = seenPref.count
        }
        // suffix distinct count
        var suffDistinct = Array(repeating: 0, count: n)
        var seenSuff = Set<Int>()
        for i in stride(from: n-1, through: 0, by: -1) {
            seenSuff.insert(nums[i])
            suffDistinct[i] = seenSuff.count
        }
        // prefix frequency counts (value up to 50)
        let maxVal = 51
        var prefFreq = Array(repeating: Array(repeating: 0, count: maxVal), count: n+1)
        for i in 0..<n {
            prefFreq[i+1] = prefFreq[i]
            prefFreq[i+1][nums[i]] += 1
        }
        // suffix frequency counts
        var suffFreq = Array(repeating: Array(repeating: 0, count: maxVal), count: n+1)
        for i in stride(from: n-1, through: 0, by: -1) {
            suffFreq[i] = suffFreq[i+1]
            suffFreq[i][nums[i]] += 1
        }
        var result = 0
        // A split is beautiful if there exists a value x such that:
        // count of x in left part == number of distinct elements in right part.
        for split in 1..<n {
            let distinctRight = suffDistinct[split]
            var ok = false
            for v in 0..<maxVal where prefFreq[split][v] > 0 {
                if prefFreq[split][v] == distinctRight {
                    ok = true
                    break
                }
            }
            if ok { result += 1 }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun beautifulSplits(nums: IntArray): Int {
        val n = nums.size
        if (n < 2) return 0
        val prefMax = IntArray(n)
        var curMax = nums[0]
        for (i in 0 until n) {
            if (nums[i] > curMax) curMax = nums[i]
            prefMax[i] = curMax
        }
        val suffMin = IntArray(n)
        var curMin = nums[n - 1]
        for (i in n - 1 downTo 0) {
            if (nums[i] < curMin) curMin = nums[i]
            suffMin[i] = curMin
        }
        var ans = 0
        for (i in 0 until n - 1) {
            if (prefMax[i] == suffMin[i + 1]) ans++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int beautifulSplits(List<int> nums) {
    int n = nums.length;
    if (n <= 1) return 0;

    List<int> prefixMax = List.filled(n, 0);
    List<int> suffixMax = List.filled(n, 0);

    // Prefix maximum frequencies
    List<int> freq = List.filled(51, 0);
    int curMax = 0;
    for (int i = 0; i < n; i++) {
      int v = nums[i];
      freq[v]++;
      if (freq[v] > curMax) curMax = freq[v];
      prefixMax[i] = curMax;
    }

    // Suffix maximum frequencies
    freq = List.filled(51, 0);
    curMax = 0;
    for (int i = n - 1; i >= 0; i--) {
      int v = nums[i];
      freq[v]++;
      if (freq[v] > curMax) curMax = freq[v];
      suffixMax[i] = curMax;
    }

    int ans = 0;
    for (int i = 0; i < n - 1; i++) {
      if (prefixMax[i] > suffixMax[i + 1]) ans++;
    }
    return ans;
  }
}
```

## Golang

```go
func beautifulSplits(nums []int) int {
    n := len(nums)
    if n < 2 {
        return 0
    }
    prefixOdd := make([]int, n)
    var freq [51]int
    odd := 0
    for i, v := range nums {
        freq[v]++
        if freq[v]%2 == 1 {
            odd++
        } else {
            odd--
        }
        prefixOdd[i] = odd
    }

    suffixOdd := make([]int, n)
    var freqR [51]int
    odd = 0
    for i := n - 1; i >= 0; i-- {
        v := nums[i]
        freqR[v]++
        if freqR[v]%2 == 1 {
            odd++
        } else {
            odd--
        }
        suffixOdd[i] = odd
    }

    count := 0
    for i := 0; i < n-1; i++ {
        if prefixOdd[i] <= 1 && suffixOdd[i+1] <= 1 {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def beautiful_splits(nums)
  n = nums.length
  ans = 0
  (1...n).each do |k|
    match = true
    i = 0
    while i < k
      if nums[i] != nums[n - k + i]
        match = false
        break
      end
      i += 1
    end
    next unless match
    ans += (k * 2 == n) ? 1 : 2
  end
  ans
end
```

## Scala

```scala
object Solution {
    def beautifulSplits(nums: Array[Int]): Int = {
        val n = nums.length
        if (n < 2) return 0
        val prefixMax = new Array[Int](n)
        var curMax = Int.MinValue
        for (i <- 0 until n) {
            curMax = math.max(curMax, nums(i))
            prefixMax(i) = curMax
        }
        val suffixMin = new Array[Int](n)
        var curMin = Int.MaxValue
        for (i <- (n - 1) to 0 by -1) {
            curMin = math.min(curMin, nums(i))
            suffixMin(i) = curMin
        }
        var count = 0
        for (i <- 1 until n) {
            if (prefixMax(i - 1) == suffixMin(i)) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn beautiful_splits(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 2 {
            return 0;
        }
        const MAX_VAL: usize = 50;
        let mut total = vec![0usize; MAX_VAL + 1];
        for &x in &nums {
            total[x as usize] += 1;
        }
        let mut pref = vec![0usize; MAX_VAL + 1];
        let mut ans: i32 = 0;
        for i in 0..n - 1 {
            let v = nums[i] as usize;
            pref[v] += 1;
            let mut left_le_right = true;
            let mut right_le_left = true;
            for val in 0..=MAX_VAL {
                let left = pref[val];
                let right = total[val] - left;
                if left > right {
                    left_le_right = false;
                }
                if right > left {
                    right_le_left = false;
                }
                if !left_le_right && !right_le_left {
                    break;
                }
            }
            if left_le_right || right_le_left {
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (beautiful-splits nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums)))
    (if (< n 2)
        0
        (let* ((vec (list->vector nums))
               (pref (make-vector n))
               (suff (make-vector n)))
          ;; prefix maximums
          (for ([i (in-range n)])
            (if (= i 0)
                (vector-set! pref i (vector-ref vec i))
                (let ((prev (vector-ref pref (- i 1)))
                      (cur (vector-ref vec i)))
                  (vector-set! pref i (max prev cur)))))
          ;; suffix minimums
          (for ([i (in-range (sub1 n) -1 -1)])
            (if (= i (sub1 n))
                (vector-set! suff i (vector-ref vec i))
                (let ((next (vector-ref suff (+ i 1)))
                      (cur (vector-ref vec i)))
                  (vector-set! suff i (min next cur)))))
          ;; count beautiful splits
          (let loop ((i 0) (cnt 0))
            (if (= i (- n 1))
                cnt
                (loop (+ i 1)
                      (if (= (vector-ref pref i)
                             (vector-ref suff (+ i 1)))
                          (+ cnt 1)
                          cnt)))))))))
```

## Erlang

```erlang
-spec beautiful_splits(Nums :: [integer()]) -> integer().
beautiful_splits(Nums) ->
    Right0 = build_freq(Nums),
    N = length(Nums),
    beautiful_splits_loop(Nums, Right0, #{}, 0, 1, N).

build_freq(List) ->
    lists:foldl(fun(X, Acc) ->
        maps:update_with(X, fun(C) -> C + 1 end, 1, Acc)
    end, #{}, List).

beautiful_splits_loop([], _Right, _Left, Acc, _Pos, _N) ->
    Acc;
beautiful_splits_loop([X | Rest], Right, Left, Acc, Pos, N) ->
    Left1 = maps:update_with(X, fun(C) -> C + 1 end, 1, Left),
    Right1 = case maps:get(X, Right, 0) of
                 0 -> Right;
                 1 -> maps:remove(X, Right);
                 C when C > 1 -> maps:put(X, C - 1, Right)
             end,
    Acc1 = if Pos < N ->
               if subset(Left1, Right1) orelse subset(Right1, Left1) ->
                      Acc + 1;
                  true ->
                      Acc
               end;
           true ->
               Acc
           end,
    beautiful_splits_loop(Rest, Right1, Left1, Acc1, Pos + 1, N).

subset(L, R) ->
    lists:all(fun(V) ->
        maps:get(V, L, 0) =< maps:get(V, R, 0)
    end, lists:seq(0, 50)).
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_splits(nums :: [integer]) :: integer
  def beautiful_splits(nums) do
    n = length(nums)

    # Prefix odd counts
    {prefix_rev, _freq, _odd} =
      Enum.reduce(nums, {[], %{}, 0}, fn val, {acc, freq, odd} ->
        cnt = Map.get(freq, val, 0)
        new_cnt = cnt + 1
        freq = Map.put(freq, val, new_cnt)

        odd = if rem(new_cnt, 2) == 1, do: odd + 1, else: odd - 1
        {[odd | acc], freq, odd}
      end)

    prefix_odds = [0 | Enum.reverse(prefix_rev)]

    # Suffix odd counts
    {suffix_rev, _freq2, _odd2} =
      Enum.reduce(Enum.reverse(nums), {[], %{}, 0}, fn val, {acc, freq, odd} ->
        cnt = Map.get(freq, val, 0)
        new_cnt = cnt + 1
        freq = Map.put(freq, val, new_cnt)

        odd = if rem(new_cnt, 2) == 1, do: odd + 1, else: odd - 1
        {[odd | acc], freq, odd}
      end)

    suffix_odds = [0 | Enum.reverse(suffix_rev)]

    # Count beautiful splits
    1..(n - 1)
    |> Enum.reduce(0, fn i, cnt ->
      if Enum.at(prefix_odds, i) <= 1 and Enum.at(suffix_odds, i) <= 1 do
        cnt + 1
      else
        cnt
      end
    end)
  end
end
```
