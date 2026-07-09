# 1508. Range Sum of Sorted Subarray Sums

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    
    long long sumFirstK(const vector<int>& nums, int n, long long k) {
        if (k == 0) return 0;
        // prefix sums of nums
        vector<long long> pref(n + 1, 0), prefAcc(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + nums[i];
        }
        prefAcc[0] = pref[0];
        for (int i = 1; i <= n; ++i) {
            prefAcc[i] = prefAcc[i - 1] + pref[i];
        }
        
        auto countAndSum = [&](long long limit) -> pair<long long, long long> {
            long long cnt = 0;
            long long total = 0;
            int left = 0;
            for (int r = 0; r < n; ++r) {
                while (left <= r && pref[r + 1] - pref[left] > limit) ++left;
                int curCnt = r - left + 1;
                if (curCnt > 0) {
                    cnt += curCnt;
                    long long sumPrefL = prefAcc[r] - (left > 0 ? prefAcc[left - 1] : 0);
                    total += (long long)curCnt * pref[r + 1] - sumPrefL;
                }
            }
            return {cnt, total};
        };
        
        int low = *min_element(nums.begin(), nums.end());
        int high = (int)pref[n];
        while (low < high) {
            int mid = low + (high - low) / 2;
            auto [c, t] = countAndSum(mid);
            if (c >= k) high = mid;
            else low = mid + 1;
        }
        auto [cnt, tot] = countAndSum(low);
        long long sumK = tot - (cnt - k) * (long long)low;
        return sumK % MOD;
    }
    
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        long long ans = sumFirstK(nums, n, right) - sumFirstK(nums, n, left - 1);
        ans %= MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int rangeSum(int[] nums, int n, int left, int right) {
        int total = n * (n + 1) / 2;
        long[] sums = new long[total];
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        int idx = 0;
        for (int start = 0; start < n; start++) {
            for (int end = start + 1; end <= n; end++) {
                sums[idx++] = prefix[end] - prefix[start];
            }
        }
        java.util.Arrays.sort(sums);
        long ans = 0;
        for (int i = left - 1; i < right; i++) {
            ans += sums[i];
            if (ans >= MOD) ans %= MOD;
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        mod = 10**9 + 7
        # Prefix sums for O(1) subarray sum queries
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        subs = []
        for i in range(n):
            pi = pref[i]
            for j in range(i + 1, n + 1):
                subs.append(pref[j] - pi)

        subs.sort()
        return sum(subs[left - 1:right]) % mod
```

## Python3

```python
from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        # prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        sub_sums = []
        for i in range(n):
            pi = pref[i]
            for j in range(i + 1, n + 1):
                sub_sums.append(pref[j] - pi)

        sub_sums.sort()
        total = sum(sub_sums[left - 1:right]) % MOD
        return total
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007

static int cmpLong(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

int rangeSum(int* nums, int numsSize, int n, int left, int right) {
    if (n <= 0) return 0;
    long long total = (long long)n * (n + 1) / 2;
    long long *sums = (long long *)malloc(sizeof(long long) * total);
    if (!sums) return 0;

    long long idx = 0;
    for (int i = 0; i < n; ++i) {
        long long cur = 0;
        for (int j = i; j < n; ++j) {
            cur += nums[j];
            sums[idx++] = cur;
        }
    }

    qsort(sums, total, sizeof(long long), cmpLong);

    long long ans = 0;
    for (long long i = left - 1; i <= right - 1; ++i) {
        ans += sums[i];
        if (ans >= MOD) ans %= MOD;
    }

    free(sums);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int RangeSum(int[] nums, int n, int left, int right) {
        const int MOD = 1000000007;
        int totalSubarrays = n * (n + 1) / 2;
        var sums = new List<int>(totalSubarrays);
        for (int i = 0; i < n; i++) {
            long cur = 0;
            for (int j = i; j < n; j++) {
                cur += nums[j];
                sums.Add((int)cur);
            }
        }
        sums.Sort();
        long ans = 0;
        for (int i = left - 1; i <= right - 1; i++) {
            ans += sums[i];
            if (ans >= MOD) ans %= MOD;
        }
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} n
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeSum = function(nums, n, left, right) {
    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const sums = [];
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j <= n; ++j) {
            sums.push(prefix[j] - prefix[i]);
        }
    }
    sums.sort((a, b) => a - b);
    const MOD = 1000000007;
    let ans = 0;
    for (let i = left - 1; i < right; ++i) {
        ans = (ans + sums[i]) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function rangeSum(nums: number[], n: number, left: number, right: number): number {
    const sums: number[] = [];
    for (let i = 0; i < n; i++) {
        let cur = 0;
        for (let j = i; j < n; j++) {
            cur += nums[j];
            sums.push(cur);
        }
    }
    sums.sort((a, b) => a - b);
    const MOD = 1_000_000_007;
    let ans = 0;
    for (let i = left - 1; i <= right - 1; i++) {
        ans = (ans + sums[i]) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function rangeSum($nums, $n, $left, $right) {
        $mod = 1000000007;

        // Prefix sums
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] + $nums[$i];
        }

        // Collect all subarray sums
        $sums = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j <= $n; $j++) {
                $sums[] = $pref[$j] - $pref[$i];
            }
        }

        // Sort them
        sort($sums, SORT_NUMERIC);

        // Sum the required range (1-indexed)
        $ans = 0;
        for ($k = $left - 1; $k <= $right - 1; $k++) {
            $ans = ($ans + $sums[$k]) % $mod;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func rangeSum(_ nums: [Int], _ n: Int, _ left: Int, _ right: Int) -> Int {
        let MOD = 1_000_000_007
        var heap = MinHeap()
        for i in 0..<n {
            heap.push(Node(sum: nums[i], start: i, end: i))
        }
        var ans = 0
        var count = 0
        while !heap.isEmpty && count < right {
            guard let node = heap.pop() else { break }
            count += 1
            if count >= left {
                ans = (ans + node.sum) % MOD
            }
            if node.end + 1 < n {
                let newSum = node.sum + nums[node.end + 1]
                heap.push(Node(sum: newSum, start: node.start, end: node.end + 1))
            }
        }
        return ans
    }
}

private struct Node {
    var sum: Int
    var start: Int
    var end: Int
}

private class MinHeap {
    private var data: [Node] = []
    
    var isEmpty: Bool { data.isEmpty }
    
    func push(_ node: Node) {
        data.append(node)
        siftUp(data.count - 1)
    }
    
    func pop() -> Node? {
        guard !data.isEmpty else { return nil }
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return result
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child].sum < data[parent].sum {
                data.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left].sum < data[smallest].sum {
                smallest = left
            }
            if right < data.count && data[right].sum < data[smallest].sum {
                smallest = right
            }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rangeSum(nums: IntArray, n: Int, left: Int, right: Int): Int {
        val total = n * (n + 1) / 2
        val sums = IntArray(total)
        var idx = 0
        val pref = LongArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + nums[i]
        }
        for (i in 0 until n) {
            for (j in i until n) {
                sums[idx++] = (pref[j + 1] - pref[i]).toInt()
            }
        }
        java.util.Arrays.sort(sums)
        val MOD = 1_000_000_007L
        var ans = 0L
        for (k in left - 1..right - 1) {
            ans += sums[k]
            if (ans >= MOD) ans %= MOD
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int rangeSum(List<int> nums, int n, int left, int right) {
    const int MOD = 1000000007;
    // Prefix sums for O(1) subarray sum queries
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + nums[i];
    }

    int totalSub = n * (n + 1) ~/ 2;
    List<int> sums = List.filled(totalSub, 0);
    int idx = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i; j < n; ++j) {
        sums[idx++] = prefix[j + 1] - prefix[i];
      }
    }

    sums.sort();

    int ans = 0;
    for (int i = left - 1; i < right; ++i) {
      ans += sums[i];
      if (ans >= MOD) ans %= MOD;
    }
    return ans % MOD;
  }
}
```

## Golang

```go
package main

import "sort"

func rangeSum(nums []int, n int, left int, right int) int {
	const MOD int64 = 1000000007
	sums := make([]int, 0, n*(n+1)/2)
	for i := 0; i < n; i++ {
		cur := 0
		for j := i; j < n; j++ {
			cur += nums[j]
			sums = append(sums, cur)
		}
	}
	sort.Ints(sums)
	var ans int64
	for i := left - 1; i <= right-1; i++ {
		ans = (ans + int64(sums[i])) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def range_sum(nums, n, left, right)
  mod = 1_000_000_007
  total_subarrays = n * (n + 1) / 2
  sums = Array.new(total_subarrays)
  idx = 0
  i = 0
  while i < n
    cur = 0
    j = i
    while j < n
      cur += nums[j]
      sums[idx] = cur
      idx += 1
      j += 1
    end
    i += 1
  end

  sums.sort!
  ans = 0
  l = left - 1
  r = right - 1
  while l <= r
    ans += sums[l]
    ans -= mod if ans >= mod
    l += 1
  end
  ans % mod
end
```

## Scala

```scala
object Solution {
    def rangeSum(nums: Array[Int], n: Int, left: Int, right: Int): Int = {
        val MOD = 1000000007L
        // Prefix sums
        val pref = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            pref(i + 1) = pref(i) + nums(i).toLong
            i += 1
        }
        // All subarray sums
        val total = n * (n + 1) / 2
        val sums = new Array[Long](total)
        var idx = 0
        var start = 0
        while (start < n) {
            var end = start + 1
            while (end <= n) {
                sums(idx) = pref(end) - pref(start)
                idx += 1
                end += 1
            }
            start += 1
        }
        java.util.Arrays.sort(sums)
        // Sum required range
        var ans = 0L
        var k = left - 1
        while (k < right) {
            ans += sums(k)
            if (ans >= MOD) ans %= MOD
            k += 1
        }
        (ans % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn range_sum(nums: Vec<i32>, n: i32, left: i32, right: i32) -> i32 {
        let len = nums.len();
        let total_subarrays = len * (len + 1) / 2;
        let mut sums = Vec::with_capacity(total_subarrays);
        for i in 0..len {
            let mut cur: i64 = 0;
            for j in i..len {
                cur += nums[j] as i64;
                sums.push(cur);
            }
        }
        sums.sort_unstable();
        const MOD: i64 = 1_000_000_007;
        let l = (left - 1) as usize;
        let r = (right - 1) as usize;
        let mut ans: i64 = 0;
        for idx in l..=r {
            ans += sums[idx];
            if ans >= MOD {
                ans %= MOD;
            }
        }
        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (range-sum nums n left right)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((len n)
         (total (/ (* len (+ len 1)) 2))
         (vec (make-vector total))
         ;; prefix sums
         (pref (make-vector (+ len 1) 0)))
    ;; build prefix sum array
    (for ([i (in-range len)])
      (vector-set! pref (add1 i)
                   (+ (vector-ref pref i) (list-ref nums i))))
    ;; collect all subarray sums
    (let ((idx (box 0)))
      (for ([i (in-range len)])
        (for ([j (in-range (add1 i) (add1 len))])
          (let* ((s (- (vector-ref pref j) (vector-ref pref i)))
                 (pos (unbox idx)))
            (vector-set! vec pos s)
            (set-box! idx (add1 pos))))))
    ;; sort the sums
    (define sorted-vec
      (list->vector (sort (vector->list vec) <)))
    ;; sum required range [left, right] (1‑based)
    (let ((ans 0))
      (for ([k (in-range (sub1 left) right)])
        (set! ans (modulo (+ ans (vector-ref sorted-vec k)) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([range_sum/4]).
-define(MOD, 1000000007).

-spec range_sum(Nums :: [integer()], N :: integer(), Left :: integer(), Right :: integer()) -> integer().
range_sum(Nums, _N, Left, Right) ->
    All = all_sums(Nums, []),
    Sorted = lists:sort(All),
    Sub = lists:sublist(Sorted, Left, Right - Left + 1),
    sum_mod(Sub, 0).

all_sums([], Acc) -> Acc;
all_sums([_|Tail]=Rest, Acc) ->
    Sums = collect_extend(Rest, 0, []),
    NewAcc = Sums ++ Acc,
    all_sums(Tail, NewAcc).

collect_extend([], _Curr, Acc) -> Acc;
collect_extend([X|Xs], Curr, Acc) ->
    NewSum = Curr + X,
    collect_extend(Xs, NewSum, [NewSum | Acc]).

sum_mod([], Res) -> Res rem ?MOD;
sum_mod([H|T], Acc) ->
    sum_mod(T, (Acc + H) rem ?MOD).
```

## Elixir

```elixir
defmodule Solution do
  @spec range_sum(nums :: [integer], n :: integer, left :: integer, right :: integer) :: integer
  def range_sum(nums, _n, left, right) do
    mod = 1_000_000_007
    len = length(nums)

    # prefix sums as a tuple for O(1) access
    pref_tuple =
      List.to_tuple([0] ++ Enum.scan(nums, fn x, acc -> acc + x end))

    # all subarray sums
    sums =
      for i <- 0..(len - 1),
          j <- (i + 1)..len,
          do: elem(pref_tuple, j) - elem(pref_tuple, i)

    sorted = Enum.sort(sums)
    slice_len = right - left + 1

    sorted
    |> Enum.slice(left - 1, slice_len)
    |> Enum.reduce(0, fn v, acc -> rem(acc + v, mod) end)
  end
end
```
