# 2972. Count the Number of Incremovable Subarrays II

## Cpp

```cpp
class Solution {
public:
    long long incremovableSubarrayCount(vector<int>& nums) {
        int n = nums.size();
        vector<char> prefOk(n);
        prefOk[0] = 1;
        for (int i = 1; i < n; ++i)
            prefOk[i] = prefOk[i - 1] && (nums[i - 1] < nums[i]);
        
        vector<char> suffOk(n);
        suffOk[n - 1] = 1;
        for (int i = n - 2; i >= 0; --i)
            suffOk[i] = suffOk[i + 1] && (nums[i] < nums[i + 1]);
        
        int y = 0;
        while (y < n && !suffOk[y]) ++y;          // smallest index where suffix is increasing
        vector<int> suffixVals(nums.begin() + y, nums.end());
        
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (i > 0 && !prefOk[i - 1]) break;   // prefix before i is not strictly increasing
            int minK = max(y, i + 1);               // earliest possible suffix start after removal
            
            if (i == 0) {
                int k = minK;
                ans += (long long)n - k + 1;
            } else {
                int startIdx = minK - y;             // offset in suffixVals
                auto itStart = suffixVals.begin() + startIdx;
                auto it = upper_bound(itStart, suffixVals.end(), nums[i - 1]);
                int k = (it == suffixVals.end()) ? n : y + (int)(it - suffixVals.begin());
                ans += (long long)n - k + 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long incremovableSubarrayCount(int[] nums) {
        int n = nums.length;
        boolean[] prefInc = new boolean[n];
        boolean[] suffInc = new boolean[n];
        // prefix increasing
        prefInc[0] = true;
        for (int i = 1; i < n; i++) {
            prefInc[i] = prefInc[i - 1] && nums[i - 1] < nums[i];
        }
        // suffix increasing
        suffInc[n - 1] = true;
        for (int i = n - 2; i >= 0; i--) {
            suffInc[i] = suffInc[i + 1] && nums[i] < nums[i + 1];
        }
        int x = -1; // last index where prefix is strictly increasing
        for (int i = 0; i < n; i++) {
            if (prefInc[i]) x = i;
        }
        int y = n - 1; // first index where suffix is strictly increasing
        for (int i = 0; i < n; i++) {
            if (suffInc[i]) { y = i; break; }
        }
        long ans = 0L;
        int limit = Math.min(x, n - 2); // i must be <= n-2 to allow non‑empty deletion
        int j = y; // start of suffix kept
        for (int i = -1; i <= limit; i++) {
            if (j < i + 2) j = i + 2; // ensure at least one element removed
            while (j < n && !(i == -1 || nums[i] < nums[j])) {
                ++j;
            }
            ans += (long)(n - j + 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # longest strictly increasing prefix ending at x
        x = 0
        while x + 1 < n and nums[x] < nums[x + 1]:
            x += 1

        # smallest index y such that nums[y:] is strictly increasing
        y = n - 1
        while y - 1 >= 0 and nums[y - 1] < nums[y]:
            y -= 1

        total = 0
        # minimal possible j (end index of subarray) to keep suffix increasing
        j = max(y - 1, 0)

        limit_i = min(x + 2, n)  # i can be at most x+1, but not exceed n-1
        for i in range(limit_i):
            if j < i:
                j = i
            # advance j until left element (if exists) is less than right element (if exists)
            while j < n - 1 and i > 0:
                if nums[i - 1] < nums[j + 1]:
                    break
                j += 1
            total += n - j
        return total
```

## Python3

```python
from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        # longest strictly increasing prefix
        x = 0
        while x + 1 < n and nums[x] < nums[x + 1]:
            x += 1
        # longest strictly increasing suffix
        y = n - 1
        while y - 1 >= 0 and nums[y - 1] < nums[y]:
            y -= 1

        ans = 0
        j = y  # pointer for suffix start satisfying cross condition
        for i in range(-1, x + 1):
            if i == -1:
                start_k = max(y, 1)  # need removed part non‑empty
            else:
                while j < n and nums[i] >= nums[j]:
                    j += 1
                start_k = max(j, i + 2)  # ensure removed subarray non‑empty
            if start_k <= n:
                ans += n - start_k + 1
        return ans
```

## C

```c
long long incremovableSubarrayCount(int* nums, int numsSize) {
    int n = numsSize;
    if (n == 0) return 0;
    // Find longest increasing prefix
    int x = 0;
    while (x + 1 < n && nums[x] < nums[x + 1]) {
        ++x;
    }
    // Find longest increasing suffix
    int y = n - 1;
    while (y > 0 && nums[y - 1] < nums[y]) {
        --y;
    }
    long long ans = 0;
    int j = y; // minimal suffix start candidate
    int limitStart = x + 1;
    if (limitStart > n) limitStart = n; // just in case, though x <= n-1
    for (int i = 0; i < limitStart && i < n; ++i) {
        while (j < n && i > 0 && !(nums[i - 1] < nums[j])) {
            ++j;
        }
        int start = j;
        if (start < i + 1) start = i + 1; // ensure non‑empty removal
        ans += (long long)(n - start + 1);
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long IncremovableSubarrayCount(int[] nums) {
        int n = nums.Length;
        // Check if the whole array is strictly increasing
        bool fullInc = true;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] >= nums[i + 1]) { fullInc = false; break; }
        }
        if (fullInc) return (long)n * (n + 1) / 2;

        // Longest strictly increasing prefix
        int leftIncEnd = 0;
        while (leftIncEnd + 1 < n && nums[leftIncEnd] < nums[leftIncEnd + 1]) leftIncEnd++;

        // Smallest index where suffix is strictly increasing
        int rightIncStart = n - 1;
        while (rightIncStart - 1 >= 0 && nums[rightIncStart - 1] < nums[rightIncStart]) rightIncStart--;

        long ans = 0;
        int j = Math.Max(0, rightIncStart - 1);
        int maxStart = leftIncEnd + 1; // inclusive upper bound for start index

        for (int i = 0; i <= maxStart; i++) {
            int minR = Math.Max(i, rightIncStart - 1);
            if (j < minR) j = minR;
            while (j < n && !(i == 0 || j == n - 1 || nums[i - 1] < nums[j + 1])) {
                j++;
            }
            ans += (long)(n - j);
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
var incremovableSubarrayCount = function(nums) {
    const n = nums.length;
    // longest strictly increasing prefix ending at x
    let x = 0;
    while (x + 1 < n && nums[x] < nums[x + 1]) x++;
    // longest strictly increasing suffix starting at y
    let y = n - 1;
    while (y - 1 >= 0 && nums[y - 1] < nums[y]) y--;
    
    let total = 0;
    let j = y; // first index of the kept suffix
    
    for (let i = -1; i <= x; i++) {
        if (i !== -1) {
            while (j < n && nums[i] >= nums[j]) {
                j++;
            }
        }
        const kStart = Math.max(j, i + 2); // need at least one removed element
        if (kStart <= n) {
            total += (n - kStart + 1);
        }
    }
    
    return total;
};
```

## Typescript

```typescript
function incremovableSubarrayCount(nums: number[]): number {
    const n = nums.length;
    const pref = new Array<boolean>(n);
    pref[0] = true;
    for (let i = 1; i < n; i++) {
        pref[i] = pref[i - 1] && nums[i - 1] < nums[i];
    }
    let x = n - 1;
    while (x >= 0 && !pref[x]) x--;

    const suff = new Array<boolean>(n);
    suff[n - 1] = true;
    for (let i = n - 2; i >= 0; i--) {
        suff[i] = suff[i + 1] && nums[i] < nums[i + 1];
    }

    let maxI = Math.min(n - 1, x + 1);
    let ans = 0;
    let j = -1;

    const isValid = (i: number, end: number): boolean => {
        if (end < n - 1 && !suff[end + 1]) return false;
        if (i > 0 && end < n - 1 && nums[i - 1] >= nums[end + 1]) return false;
        return true;
    };

    for (let i = 0; i <= maxI; i++) {
        if (j < i) j = i;
        while (j + 1 < n && !isValid(i, j + 1)) {
            j++;
        }
        if (!isValid(i, j)) continue;
        ans += n - j;
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
    function incremovableSubarrayCount($nums) {
        $n = count($nums);
        if ($n == 0) return 0;

        // Find the longest strictly increasing prefix
        $x = 0;
        while ($x + 1 < $n && $nums[$x] < $nums[$x + 1]) {
            $x++;
        }

        // Find the earliest index where suffix is strictly increasing
        $y = $n - 1;
        while ($y - 1 >= 0 && $nums[$y - 1] < $nums[$y]) {
            $y--;
        }

        $j = $y;          // start of suffix after removal
        $ans = 0;

        $maxL = min($x + 1, $n - 1);
        for ($i = 0; $i <= $maxL; $i++) {
            while ($j < $n && $i > 0 && $nums[$i - 1] >= $nums[$j]) {
                $j++;
            }
            $minK = max($j, $i + 1); // k is the index where suffix starts (could be n)
            if ($minK <= $n) {
                $ans += $n - $minK + 1;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func incremovableSubarrayCount(_ nums: [Int]) -> Int {
        let n = nums.count
        // Find longest increasing prefix
        var x = -1
        for i in 0..<n {
            if i == 0 || nums[i] > nums[i - 1] {
                x = i
            } else {
                break
            }
        }
        // Find earliest index where suffix is strictly increasing
        var y = n
        for i in stride(from: n - 1, through: 0, by: -1) {
            if i == n - 1 || nums[i] < nums[i + 1] {
                y = i
            } else {
                break
            }
        }
        var ans: Int64 = 0
        var j = y
        var i = -1
        while i <= x {
            if j < i + 2 {
                j = i + 2
            }
            while j < n && i >= 0 && nums[i] >= nums[j] {
                j += 1
            }
            // number of valid suffix starts from j to n (including n for empty suffix)
            ans += Int64(n - j + 1)
            i += 1
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun incremovableSubarrayCount(nums: IntArray): Long {
        val n = nums.size
        // longest strictly increasing prefix ending at x
        var x = 0
        while (x + 1 < n && nums[x] < nums[x + 1]) {
            x++
        }
        // smallest index y such that nums[y..n-1] is strictly increasing
        var y = n - 1
        while (y > 0 && nums[y - 1] < nums[y]) {
            y--
        }
        val maxStart = if (x == n - 1) n - 1 else x + 1
        var ans = 0L
        var p = y // pointer to candidate right side start index (t)
        for (i in 0..maxStart) {
            if (i == 0) {
                val minR = kotlin.math.max(i, y - 1)
                ans += (n - minR).toLong()
            } else {
                // ensure p is at least max(y, i+1)
                if (p < i + 1) p = i + 1
                if (p < y) p = y
                while (p < n && nums[p] <= nums[i - 1]) {
                    p++
                }
                val minR = if (p == n) n - 1 else p - 1
                ans += (n - minR).toLong()
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int incremovableSubarrayCount(List<int> nums) {
    int n = nums.length;
    // Prefix strictly increasing flags
    List<bool> pref = List.filled(n, false);
    pref[0] = true;
    for (int i = 1; i < n; ++i) {
      pref[i] = pref[i - 1] && nums[i - 1] < nums[i];
    }
    int x = n - 1;
    while (x >= 0 && !pref[x]) {
      --x;
    }

    // Suffix strictly increasing flags
    List<bool> suff = List.filled(n, false);
    suff[n - 1] = true;
    for (int i = n - 2; i >= 0; --i) {
      suff[i] = suff[i + 1] && nums[i] < nums[i + 1];
    }
    int y = 0;
    while (y < n && !suff[y]) {
      ++y;
    }

    int j = y;
    int limit = x + 1;
    if (limit > n - 1) limit = n - 1;
    int ans = 0;

    for (int i = 0; i <= limit; ++i) {
      while (j < n && i > 0 && nums[i - 1] >= nums[j]) {
        ++j;
      }
      int start = j;
      if (start < i + 1) start = i + 1;
      ans += (n - start + 1);
    }

    return ans;
  }
}
```

## Golang

```go
func incremovableSubarrayCount(nums []int) int64 {
    n := len(nums)
    if n == 0 {
        return 0
    }
    // longest strictly increasing prefix ending index
    left := 0
    for left+1 < n && nums[left] < nums[left+1] {
        left++
    }
    // earliest index where suffix is strictly increasing
    right := n - 1
    for right-1 >= 0 && nums[right-1] < nums[right] {
        right--
    }

    var ans int64
    j := right
    for i := -1; i <= left; i++ {
        if j < i+2 {
            j = i + 2
        }
        // ensure cross condition when both sides exist
        for j < n && i >= 0 && !(nums[i] < nums[j]) {
            j++
        }
        if j > n {
            break
        }
        ans += int64(n - j + 1)
    }
    return ans
}
```

## Ruby

```ruby
def incremovable_subarray_count(nums)
  n = nums.length
  pref = Array.new(n, false)
  suff = Array.new(n, false)

  pref[0] = true
  (1...n).each do |i|
    pref[i] = pref[i - 1] && nums[i - 1] < nums[i]
  end

  suff[n - 1] = true
  (n - 2).downto(0) do |i|
    suff[i] = suff[i + 1] && nums[i] < nums[i + 1]
  end

  suffix_good = []
  (0...n).each { |j| suffix_good << j if suff[j] }
  suffix_good << n # virtual suffix representing empty tail

  len = suffix_good.length
  pj = 0
  ans = 0

  (-1...n).each do |i|
    next unless i == -1 || pref[i]

    while pj < len
      j = suffix_good[pj]
      if j < i + 2
        pj += 1
        next
      end
      if i != -1 && j != n && nums[i] >= nums[j]
        pj += 1
        next
      end
      break
    end

    ans += len - pj
  end

  ans
end
```

## Scala

```scala
object Solution {
    def incremovableSubarrayCount(nums: Array[Int]): Long = {
        val n = nums.length
        // longest strictly increasing prefix ending at x
        var x = 0
        while (x + 1 < n && nums(x) < nums(x + 1)) {
            x += 1
        }
        // longest strictly increasing suffix starting at y
        var y = n - 1
        while (y - 1 >= 0 && nums(y - 1) < nums(y)) {
            y -= 1
        }

        var ans: Long = 0L
        var j = y
        var i = -1
        while (i <= x && i + 2 <= n) {
            if (j < i + 2) j = i + 2
            while (j < n && i >= 0 && !(nums(i) < nums(j))) {
                j += 1
            }
            ans += (n - j + 1).toLong
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        // longest strictly increasing prefix ending at L
        let mut l = 0usize;
        while l + 1 < n && nums[l] < nums[l + 1] {
            l += 1;
        }
        // longest strictly increasing suffix starting at r
        let mut r = n - 1;
        while r > 0 && nums[r - 1] < nums[r] {
            r -= 1;
        }

        let mut ans: i64 = 0;
        let mut j = r; // pointer to start of kept suffix

        for i in 0..=l + 1 {
            if i >= n {
                break;
            }
            // removal must be non‑empty, so suffix start > i
            if j < i + 1 {
                j = i + 1;
            }
            while j < n && i > 0 && nums[i - 1] >= nums[j] {
                j += 1;
            }
            ans += (n - j + 1) as i64; // include the case of removing to the end
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (incremovable-subarray-count nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (pref (make-vector n #t))
         (suff (make-vector n #t)))
    ;; prefix strictly increasing
    (for ([i (in-range 1 n)])
      (vector-set! pref i
        (and (vector-ref pref (sub1 i))
             (< (vector-ref vec (sub1 i)) (vector-ref vec i)))))
    ;; suffix strictly increasing
    (for ([i (in-range (- n 2) -1 -1)])
      (vector-set! suff i
        (and (vector-ref suff (+ i 1))
             (< (vector-ref vec i) (vector-ref vec (+ i 1))))))
    ;; main two‑pointer counting
    (let loop ((i 0) (j 0) (ans 0))
      (if (or (= i n)
              (and (> i 0) (not (vector-ref pref (sub1 i)))))
          ans
          (let* ((j-start (max j (+ i 1))) ; need to remove at least one element
                 (j-min
                  (let find ((jj j-start))
                    (cond
                      [(> jj n) (+ n 1)] ; no valid suffix
                      [else
                       (define cond1 (or (= jj n) (vector-ref suff jj)))
                       (define cond2
                         (if (= i 0)
                             #t
                             (if (= jj n)
                                 #t
                                 (< (vector-ref vec (sub1 i))
                                    (vector-ref vec jj)))))
                       (if (and cond1 cond2)
                           jj
                           (find (+ jj 1)))]))))
            (if (> j-min n)
                ans
                (let ((new-ans (+ ans (- n j-min) 1)))
                  (loop (+ i 1) j-min new-ans))))))))
```

## Erlang

```erlang
-spec incremovable_subarray_count(Nums :: [integer()]) -> integer().
incremovable_subarray_count(Nums) ->
    N = length(Nums),
    Tuple = list_to_tuple(Nums),

    %% longest strictly increasing prefix length (number of elements)
    PrefLen = pref_len(N, Tuple, 1),

    %% smallest index (0‑based) where suffix is strictly increasing
    YPos   = suffix_start(N, Tuple, N),          % 1‑based position
    Y0     = YPos - 1,                           % convert to 0‑based

    count_loop(0, PrefLen, N, Tuple, Y0, 0).

%% find length of longest increasing prefix (1‑based length)
pref_len(N, Tuple, I) when I < N ->
    case element(Tuple, I) < element(Tuple, I + 1) of
        true -> pref_len(N, Tuple, I + 1);
        false -> I
    end;
pref_len(_, _, I) -> I.

%% find smallest position (1‑based) where suffix [Pos..N] is increasing
suffix_start(_N, _Tuple, I) when I =< 1 ->
    I;
suffix_start(N, Tuple, I) ->
    case element(Tuple, I - 1) < element(Tuple, I) of
        true -> suffix_start(N, Tuple, I - 1);
        false -> I
    end.

%% main counting loop over possible prefix lengths L (0‑based count)
count_loop(L, PrefLen, N, _Tuple, _J, Acc) when L > PrefLen ->
    Acc;
count_loop(L, PrefLen, N, Tuple, J, Acc) ->
    case L of
        0 ->
            S0 = erlang:max(J, L + 1),
            Add = if S0 =< N -> N - S0 + 1; true -> 0 end,
            count_loop(L + 1, PrefLen, N, Tuple, J, Acc + Add);
        _ ->
            LeftVal = element(Tuple, L),          % element at index L‑1 (0‑based)
            NewJ = advance_j(J, N, Tuple, LeftVal),
            S0 = erlang:max(NewJ, L + 1),
            Add = if S0 =< N -> N - S0 + 1; true -> 0 end,
            count_loop(L + 1, PrefLen, N, Tuple, NewJ, Acc + Add)
    end.

%% move J forward while left value is not smaller than nums[J]
advance_j(J, N, _Tuple, _LeftVal) when J >= N ->
    J;
advance_j(J, N, Tuple, LeftVal) ->
    Elem = element(Tuple, J + 1),   % convert 0‑based J to 1‑based tuple index
    case LeftVal >= Elem of
        true -> advance_j(J + 1, N, Tuple, LeftVal);
        false -> J
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec incremovable_subarray_count(nums :: [integer]) :: integer
  def incremovable_subarray_count(nums) do
    n = length(nums)
    t = List.to_tuple(nums)

    # Find the maximum allowed start index (left_limit)
    left_limit =
      Enum.find_index(1..(n - 1), fn i -> elem(t, i - 1) >= elem(t, i) end)
      |> case do
        nil -> n - 1
        idx -> idx
      end

    # Find the start index of the longest increasing suffix (suffix_start)
    suffix_start =
      Enum.find_index(Enum.reverse(0..(n - 2)), fn i -> elem(t, i) >= elem(t, i + 1) end)
      |> case do
        nil -> 0
        idx -> idx + 1
      end

    min_end = suffix_start - 1
    # advance pointer to satisfy left < right condition
    advance = fn
      r, i, n, t when r + 1 < n and i > 0 and elem(t, i - 1) >= elem(t, r + 1) ->
        advance.(r + 1, i, n, t)
      r, _i, _n, _t -> r
    end

    {_, ans} =
      Enum.reduce(0..left_limit, {min_end, 0}, fn i, {cur_r, acc} ->
        cur_r = if cur_r < i - 1, do: i - 1, else: cur_r
        cur_r = advance.(cur_r, i, n, t)

        cnt =
          if cur_r < i do
            n - i
          else
            n - cur_r
          end

        {cur_r, acc + cnt}
      end)

    ans
  end
end
```
