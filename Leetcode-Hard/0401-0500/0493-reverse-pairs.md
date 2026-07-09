# 0493. Reverse Pairs

## Cpp

```cpp
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        vector<long long> a(nums.begin(), nums.end());
        return (int)mergeSort(a, 0, (int)a.size() - 1);
    }
private:
    long long mergeSort(vector<long long>& a, int left, int right) {
        if (left >= right) return 0;
        int mid = left + (right - left) / 2;
        long long cnt = mergeSort(a, left, mid) + mergeSort(a, mid + 1, right);
        
        // count cross pairs
        int j = mid + 1;
        for (int i = left; i <= mid; ++i) {
            while (j <= right && a[i] > 2LL * a[j]) ++j;
            cnt += (j - (mid + 1));
        }
        
        // merge step
        vector<long long> temp(right - left + 1);
        int p = left, q = mid + 1, k = 0;
        while (p <= mid && q <= right) {
            if (a[p] <= a[q]) temp[k++] = a[p++];
            else temp[k++] = a[q++];
        }
        while (p <= mid) temp[k++] = a[p++];
        while (q <= right) temp[k++] = a[q++];
        for (int i = 0; i < (int)temp.size(); ++i) {
            a[left + i] = temp[i];
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int reversePairs(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        long count = mergeSort(nums, 0, nums.length - 1);
        return (int) count;
    }

    private long mergeSort(int[] nums, int left, int right) {
        if (left >= right) return 0;
        int mid = left + (right - left) / 2;
        long count = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right);

        // Count reverse pairs across the two halves
        int j = mid + 1;
        for (int i = left; i <= mid; i++) {
            while (j <= right && (long) nums[i] > 2L * nums[j]) {
                j++;
            }
            count += j - (mid + 1);
        }

        // Merge the two sorted halves
        int[] temp = new int[right - left + 1];
        int i = left, k = mid + 1, t = 0;
        while (i <= mid && k <= right) {
            if (nums[i] <= nums[k]) {
                temp[t++] = nums[i++];
            } else {
                temp[t++] = nums[k++];
            }
        }
        while (i <= mid) temp[t++] = nums[i++];
        while (k <= right) temp[t++] = nums[k++];

        System.arraycopy(temp, 0, nums, left, temp.length);
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge_sort(l, r):
            if r - l <= 1:
                return 0
            m = (l + r) // 2
            cnt = merge_sort(l, m) + merge_sort(m, r)

            # count cross pairs
            j = m
            for i in range(l, m):
                while j < r and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - m

            # merge step
            temp = []
            p, q = l, m
            while p < m and q < r:
                if nums[p] <= nums[q]:
                    temp.append(nums[p])
                    p += 1
                else:
                    temp.append(nums[q])
                    q += 1
            while p < m:
                temp.append(nums[p])
                p += 1
            while q < r:
                temp.append(nums[q])
                q += 1
            nums[l:r] = temp
            return cnt

        return merge_sort(0, len(nums))
```

## Python3

```python
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(lo: int, hi: int) -> int:
            if lo >= hi:
                return 0
            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid + 1, hi)

            # Count cross reverse pairs
            j = mid + 1
            for i in range(lo, mid + 1):
                while j <= hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge step
            temp = []
            left, right = lo, mid + 1
            while left <= mid and right <= hi:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= hi:
                temp.append(nums[right])
                right += 1

            nums[lo:hi + 1] = temp
            return count

        return merge_sort(0, len(nums) - 1)
```

## C

```c
#include <stdlib.h>

static long long merge_sort(int *nums, int left, int right, int *temp) {
    if (left >= right) return 0;
    int mid = left + ((right - left) >> 1);
    long long cnt = merge_sort(nums, left, mid, temp) +
                    merge_sort(nums, mid + 1, right, temp);

    // count reverse pairs
    int j = mid + 1;
    for (int i = left; i <= mid; ++i) {
        while (j <= right && (long long)nums[i] > 2LL * nums[j]) {
            ++j;
        }
        cnt += (long long)(j - (mid + 1));
    }

    // merge two sorted halves
    int i = left, k = mid + 1, t = left;
    while (i <= mid && k <= right) {
        if (nums[i] <= nums[k]) {
            temp[t++] = nums[i++];
        } else {
            temp[t++] = nums[k++];
        }
    }
    while (i <= mid) temp[t++] = nums[i++];
    while (k <= right) temp[t++] = nums[k++];

    for (int p = left; p <= right; ++p) {
        nums[p] = temp[p];
    }

    return cnt;
}

int reversePairs(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    int *temp = (int *)malloc(sizeof(int) * numsSize);
    long long result = merge_sort(nums, 0, numsSize - 1, temp);
    free(temp);
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int ReversePairs(int[] nums) {
        if (nums == null || nums.Length == 0) return 0;
        int n = nums.Length;
        int[] temp = new int[n];
        long count = MergeSort(nums, temp, 0, n - 1);
        return (int)count;
    }

    private long MergeSort(int[] nums, int[] temp, int left, int right) {
        if (left >= right) return 0;
        int mid = left + (right - left) / 2;
        long count = MergeSort(nums, temp, left, mid) + MergeSort(nums, temp, mid + 1, right);

        // Count reverse pairs across the two halves
        int j = mid + 1;
        for (int i = left; i <= mid; i++) {
            while (j <= right && (long)nums[i] > 2L * nums[j]) {
                j++;
            }
            count += j - (mid + 1);
        }

        // Merge the two sorted halves
        int iPtr = left, rPtr = mid + 1, k = left;
        while (iPtr <= mid && rPtr <= right) {
            if (nums[iPtr] <= nums[rPtr]) {
                temp[k++] = nums[iPtr++];
            } else {
                temp[k++] = nums[rPtr++];
            }
        }
        while (iPtr <= mid) temp[k++] = nums[iPtr++];
        while (rPtr <= right) temp[k++] = nums[rPtr++];

        for (int i = left; i <= right; i++) {
            nums[i] = temp[i];
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
var reversePairs = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    const temp = new Array(n);
    
    function mergeSort(l, r) {
        if (l >= r) return 0;
        const mid = Math.floor((l + r) / 2);
        let count = mergeSort(l, mid) + mergeSort(mid + 1, r);
        
        // Count cross reverse pairs
        let j = mid + 1;
        for (let i = l; i <= mid; i++) {
            while (j <= r && nums[i] > 2 * nums[j]) {
                j++;
            }
            count += j - (mid + 1);
        }
        
        // Merge step
        let i = l, k = mid + 1, t = l;
        while (i <= mid && k <= r) {
            if (nums[i] <= nums[k]) {
                temp[t++] = nums[i++];
            } else {
                temp[t++] = nums[k++];
            }
        }
        while (i <= mid) temp[t++] = nums[i++];
        while (k <= r) temp[t++] = nums[k++];
        for (let idx = l; idx <= r; idx++) {
            nums[idx] = temp[idx];
        }
        return count;
    }
    
    return mergeSort(0, n - 1);
};
```

## Typescript

```typescript
function reversePairs(nums: number[]): number {
    const n = nums.length;
    if (n < 2) return 0;
    const temp = new Array<number>(n);
    function mergeSort(l: number, r: number): number {
        if (l >= r) return 0;
        const mid = Math.floor((l + r) / 2);
        let count = mergeSort(l, mid) + mergeSort(mid + 1, r);
        // Count cross pairs
        let j = mid + 1;
        for (let i = l; i <= mid; i++) {
            while (j <= r && nums[i] > 2 * nums[j]) {
                j++;
            }
            count += j - (mid + 1);
        }
        // Merge step
        let p = l, q = mid + 1, k = l;
        while (p <= mid && q <= r) {
            if (nums[p] <= nums[q]) {
                temp[k++] = nums[p++];
            } else {
                temp[k++] = nums[q++];
            }
        }
        while (p <= mid) temp[k++] = nums[p++];
        while (q <= r) temp[k++] = nums[q++];
        for (let i = l; i <= r; i++) {
            nums[i] = temp[i];
        }
        return count;
    }
    return mergeSort(0, n - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function reversePairs($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        $temp = array_fill(0, $n, 0);
        return $this->mergeSortCount($nums, $temp, 0, $n - 1);
    }

    private function mergeSortCount(&$arr, &$temp, $left, $right) {
        if ($left >= $right) {
            return 0;
        }
        $mid = intdiv($left + $right, 2);
        $count = $this->mergeSortCount($arr, $temp, $left, $mid);
        $count += $this->mergeSortCount($arr, $temp, $mid + 1, $right);

        // Count reverse pairs across the two halves
        $j = $mid + 1;
        for ($i = $left; $i <= $mid; $i++) {
            while ($j <= $right && $arr[$i] > 2 * $arr[$j]) {
                $j++;
            }
            $count += $j - ($mid + 1);
        }

        // Merge step
        $i = $left;
        $j = $mid + 1;
        $k = $left;

        while ($i <= $mid && $j <= $right) {
            if ($arr[$i] <= $arr[$j]) {
                $temp[$k++] = $arr[$i++];
            } else {
                $temp[$k++] = $arr[$j++];
            }
        }

        while ($i <= $mid) {
            $temp[$k++] = $arr[$i++];
        }

        while ($j <= $right) {
            $temp[$k++] = $arr[$j++];
        }

        for ($i = $left; $i <= $right; $i++) {
            $arr[$i] = $temp[$i];
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func reversePairs(_ nums: [Int]) -> Int {
        var arr = nums
        guard !arr.isEmpty else { return 0 }
        return mergeSort(&arr, 0, arr.count - 1)
    }
    
    private func mergeSort(_ nums: inout [Int], _ left: Int, _ right: Int) -> Int {
        if left >= right { return 0 }
        let mid = (left + right) >> 1
        var count = mergeSort(&nums, left, mid)
        count += mergeSort(&nums, mid + 1, right)
        
        // Count reverse pairs across the two halves
        var j = mid + 1
        for i in left...mid {
            while j <= right && Int64(nums[i]) > 2 * Int64(nums[j]) {
                j += 1
            }
            count += j - (mid + 1)
        }
        
        // Merge step
        var temp = [Int]()
        var p = left, q = mid + 1
        while p <= mid && q <= right {
            if nums[p] <= nums[q] {
                temp.append(nums[p])
                p += 1
            } else {
                temp.append(nums[q])
                q += 1
            }
        }
        while p <= mid {
            temp.append(nums[p])
            p += 1
        }
        while q <= right {
            temp.append(nums[q])
            q += 1
        }
        for i in 0..<temp.count {
            nums[left + i] = temp[i]
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reversePairs(nums: IntArray): Int {
        val n = nums.size
        if (n < 2) return 0
        val temp = IntArray(n)
        var count = 0L

        fun mergeSort(l: Int, r: Int) {
            if (l >= r) return
            val m = (l + r) ushr 1
            mergeSort(l, m)
            mergeSort(m + 1, r)

            // Count reverse pairs across the two halves
            var j = m + 1
            for (i in l..m) {
                while (j <= r && nums[i].toLong() > 2L * nums[j]) {
                    j++
                }
                count += (j - (m + 1)).toLong()
            }

            // Merge step
            var i = l
            var k = m + 1
            var p = l
            while (i <= m && k <= r) {
                if (nums[i] <= nums[k]) {
                    temp[p++] = nums[i++]
                } else {
                    temp[p++] = nums[k++]
                }
            }
            while (i <= m) temp[p++] = nums[i++]
            while (k <= r) temp[p++] = nums[k++]

            for (idx in l..r) {
                nums[idx] = temp[idx]
            }
        }

        mergeSort(0, n - 1)
        return count.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int reversePairs(List<int> nums) {
    if (nums.isEmpty) return 0;
    return _mergeSort(nums, 0, nums.length - 1);
  }

  int _mergeSort(List<int> nums, int left, int right) {
    if (left >= right) return 0;
    int mid = left + ((right - left) >> 1);
    int count = _mergeSort(nums, left, mid) + _mergeSort(nums, mid + 1, right);

    // Count cross reverse pairs
    int j = mid + 1;
    for (int i = left; i <= mid; i++) {
      while (j <= right && nums[i] > 2 * nums[j]) {
        j++;
      }
      count += j - (mid + 1);
    }

    // Merge step
    List<int> temp = [];
    int p = left, q = mid + 1;
    while (p <= mid && q <= right) {
      if (nums[p] <= nums[q]) {
        temp.add(nums[p++]);
      } else {
        temp.add(nums[q++]);
      }
    }
    while (p <= mid) temp.add(nums[p++]);
    while (q <= right) temp.add(nums[q++]);

    for (int i = 0; i < temp.length; i++) {
      nums[left + i] = temp[i];
    }

    return count;
  }
}
```

## Golang

```go
func reversePairs(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    temp := make([]int, n)

    var mergeSort func(l, r int) int64
    mergeSort = func(l, r int) int64 {
        if l >= r {
            return 0
        }
        m := (l + r) / 2
        cnt := mergeSort(l, m) + mergeSort(m+1, r)

        // count cross pairs
        j := m + 1
        for i := l; i <= m; i++ {
            for j <= r && int64(nums[i]) > 2*int64(nums[j]) {
                j++
            }
            cnt += int64(j - (m + 1))
        }

        // merge two sorted halves
        i, k := l, m+1
        idx := l
        for i <= m && k <= r {
            if nums[i] <= nums[k] {
                temp[idx] = nums[i]
                i++
            } else {
                temp[idx] = nums[k]
                k++
            }
            idx++
        }
        for i <= m {
            temp[idx] = nums[i]
            i++
            idx++
        }
        for k <= r {
            temp[idx] = nums[k]
            k++
            idx++
        }
        copy(nums[l:r+1], temp[l:r+1])
        return cnt
    }

    return int(mergeSort(0, n-1))
}
```

## Ruby

```ruby
def reverse_pairs(nums)
  _, cnt = sort_and_count(nums)
  cnt
end

def sort_and_count(arr)
  return [arr, 0] if arr.length <= 1

  mid = arr.length / 2
  left, left_cnt = sort_and_count(arr[0...mid])
  right, right_cnt = sort_and_count(arr[mid..-1])

  cnt = left_cnt + right_cnt

  j = 0
  left.each do |l|
    while j < right.length && l > (right[j] * 2)
      j += 1
    end
    cnt += j
  end

  merged = []
  i = 0
  k = 0
  while i < left.length && k < right.length
    if left[i] <= right[k]
      merged << left[i]
      i += 1
    else
      merged << right[k]
      k += 1
    end
  end
  merged.concat(left[i..-1]) if i < left.length
  merged.concat(right[k..-1]) if k < right.length

  [merged, cnt]
end
```

## Scala

```scala
object Solution {
    def reversePairs(nums: Array[Int]): Int = {
        val n = nums.length
        if (n < 2) return 0
        val temp = new Array[Int](n)

        def mergeSort(l: Int, r: Int): Long = {
            if (l >= r) return 0L
            val mid = l + (r - l) / 2
            var count = mergeSort(l, mid) + mergeSort(mid + 1, r)

            // Count cross reverse pairs
            var j = mid + 1
            for (i <- l to mid) {
                while (j <= r && nums(i).toLong > 2L * nums(j).toLong) {
                    j += 1
                }
                count += (j - (mid + 1))
            }

            // Merge step
            var i = l
            var k = mid + 1
            var t = l
            while (i <= mid && k <= r) {
                if (nums(i) <= nums(k)) {
                    temp(t) = nums(i)
                    i += 1
                } else {
                    temp(t) = nums(k)
                    k += 1
                }
                t += 1
            }
            while (i <= mid) {
                temp(t) = nums(i)
                i += 1
                t += 1
            }
            while (k <= r) {
                temp(t) = nums(k)
                k += 1
                t += 1
            }
            // Copy back to original array
            for (p <- l to r) {
                nums(p) = temp(p)
            }

            count
        }

        mergeSort(0, n - 1).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_pairs(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut arr = nums.clone();
        let mut tmp = vec![0i32; n];
        let cnt = Self::merge_sort(&mut arr, &mut tmp);
        cnt as i32
    }

    fn merge_sort(arr: &mut [i32], tmp: &mut [i32]) -> i64 {
        let len = arr.len();
        if len <= 1 {
            return 0;
        }
        let mid = len / 2;
        let (left, right) = arr.split_at_mut(mid);
        let (tmp_left, tmp_right) = tmp.split_at_mut(mid);

        let mut count = Self::merge_sort(left, tmp_left) + Self::merge_sort(right, tmp_right);

        // Count cross reverse pairs
        let mut j = 0usize;
        for i in 0..left.len() {
            while j < right.len()
                && (left[i] as i64) > 2 * (right[j] as i64)
            {
                j += 1;
            }
            count += j as i64;
        }

        // Merge left and right into tmp
        let mut i = 0usize;
        let mut k = 0usize;
        let mut l = 0usize;
        while i < left.len() && l < right.len() {
            if left[i] <= right[l] {
                tmp[k] = left[i];
                i += 1;
            } else {
                tmp[k] = right[l];
                l += 1;
            }
            k += 1;
        }
        while i < left.len() {
            tmp[k] = left[i];
            i += 1;
            k += 1;
        }
        while l < right.len() {
            tmp[k] = right[l];
            l += 1;
            k += 1;
        }

        // Copy back to original slice
        arr.copy_from_slice(&tmp[0..len]);

        count
    }
}
```

## Racket

```racket
(define/contract (reverse-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums))
         (temp (make-vector n)))
    (define (merge-sort-count! l r)
      (if (<= (- r l) 1)
          0
          (let* ((mid (+ l (quotient (- r l) 2)))
                 (cnt-left (merge-sort-count! l mid))
                 (cnt-right (merge-sort-count! mid r))
                 (cnt-cross
                  (let loop ((i l) (j mid) (c 0))
                    (if (= i mid)
                        c
                        (let ((new-j (let inner ((jj j))
                                       (if (and (< jj r)
                                                (> (vector-ref v i)
                                                   (* 2 (vector-ref v jj))))
                                           (inner (+ jj 1))
                                           jj))))
                          (loop (+ i 1) new-j (+ c (- new-j mid)))))))
            ;; merge step
            (let loop-merge ((i l) (j mid) (k l))
              (cond
                [(= i mid)
                 (let rec-right ((jj j) (kk k))
                   (when (< jj r)
                     (vector-set! temp kk (vector-ref v jj))
                     (rec-right (+ jj 1) (+ kk 1))))]
                [else
                 (if (and (< j r)
                          (<= (vector-ref v j) (vector-ref v i)))
                     (begin
                       (vector-set! temp k (vector-ref v j))
                       (loop-merge i (+ j 1) (+ k 1)))
                     (begin
                       (vector-set! temp k (vector-ref v i))
                       (loop-merge (+ i 1) j (+ k 1))))]))
            ;; copy back to original vector
            (let rec-copy ((p l))
              (when (< p r)
                (vector-set! v p (vector-ref temp p))
                (rec-copy (+ p 1))))
            (+ cnt-left cnt-right cnt-cross))))
    (merge-sort-count! 0 n)))
```

## Erlang

```erlang
-module(solution).
-export([reverse_pairs/1]).

-spec reverse_pairs(Nums :: [integer()]) -> integer().
reverse_pairs(Nums) ->
    {_, Count} = sort_count(Nums),
    Count.

%%--------------------------------------------------------------------
%% Sort the list and count reverse pairs using divide and conquer.
%%--------------------------------------------------------------------
sort_count([]) -> {[], 0};
sort_count([X]) -> {[X], 0};
sort_count(List) ->
    Len = length(List),
    Half = Len div 2,
    {Left, Right} = lists:split(Half, List),
    {SortedL, CountL} = sort_count(Left),
    {SortedR, CountR} = sort_count(Right),
    Cross = count_cross(SortedL, SortedR),
    Merged = merge(SortedL, SortedR),
    {Merged, CountL + CountR + Cross}.

%%--------------------------------------------------------------------
%% Count cross reverse pairs where left element > 2 * right element.
%% Both lists are sorted in ascending order.
%%--------------------------------------------------------------------
count_cross(Left, Right) ->
    count_cross(Left, Right, 0, 0).

% Left list, pointer into Right (remaining elements), Passed = number of
% right elements already satisfied for previous left elements,
% Acc = accumulated cross pairs.
count_cross([], _RPtr, _Passed, Acc) -> Acc;
count_cross([L|Ls], RPtr, Passed, Acc) ->
    {NewRPtr, NewPassed} = advance(RPtr, L, Passed),
    count_cross(Ls, NewRPtr, NewPassed, Acc + NewPassed).

% Advance the right pointer while condition holds.
advance([], _L, Passed) -> {[], Passed};
advance([H|T] = RPtr, L, Passed) when L > 2 * H ->
    advance(T, L, Passed + 1);
advance(RPtr, _L, Passed) -> {RPtr, Passed}.

%%--------------------------------------------------------------------
%% Standard merge of two sorted lists.
%%--------------------------------------------------------------------
merge([], R) -> R;
merge(L, []) -> L;
merge([Lh|Lt] = Llist, [Rh|Rt] = Rlist) ->
    if
        Lh =< Rh ->
            [Lh | merge(Lt, Rlist)];
        true ->
            [Rh | merge(Llist, Rt)]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_pairs(nums :: [integer]) :: integer
  def reverse_pairs(nums) do
    {_sorted, cnt} = sort_count(nums)
    cnt
  end

  defp sort_count(nums) do
    len = length(nums)

    if len <= 1 do
      {nums, 0}
    else
      mid = div(len, 2)
      {left, right} = Enum.split(nums, mid)

      {sorted_left, cnt_left} = sort_count(left)
      {sorted_right, cnt_right} = sort_count(right)

      cnt_cross = count_cross(sorted_left, sorted_right)
      merged = :lists.merge(sorted_left, sorted_right)

      {merged, cnt_left + cnt_right + cnt_cross}
    end
  end

  defp count_cross(left, right) do
    {_remaining, cnt} =
      Enum.reduce(left, {right, 0}, fn l, {rlist, acc} ->
        {new_rlist, moved} = advance(rlist, l, 0)
        {new_rlist, acc + moved}
      end)

    cnt
  end

  defp advance([], _l, cnt), do: {[], cnt}

  defp advance([h | t] = rlist, l, cnt) when l > 2 * h do
    advance(t, l, cnt + 1)
  end

  defp advance(rlist, _l, cnt), do: {rlist, cnt}
end
```
