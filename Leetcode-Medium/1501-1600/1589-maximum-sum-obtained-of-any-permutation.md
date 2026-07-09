# 1589. Maximum Sum Obtained of Any Permutation

## Cpp

```cpp
class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
        const int MOD = 1'000'000'007;
        int n = nums.size();
        vector<long long> diff(n + 1, 0);
        for (const auto& req : requests) {
            int l = req[0];
            int r = req[1];
            diff[l] += 1;
            if (r + 1 < n) diff[r + 1] -= 1;
        }
        vector<long long> freq(n, 0);
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            freq[i] = cur;
        }
        sort(nums.begin(), nums.end());
        sort(freq.begin(), freq.end());
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (freq[i] == 0) continue;
            ans = (ans + (freq[i] % MOD) * (nums[i] % MOD)) % MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maxSumRangeQuery(int[] nums, int[][] requests) {
        int n = nums.length;
        long[] diff = new long[n + 1];
        for (int[] req : requests) {
            int l = req[0];
            int r = req[1];
            diff[l] += 1;
            if (r + 1 < n) {
                diff[r + 1] -= 1;
            }
        }
        long[] freq = new long[n];
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            freq[i] = cur;
        }
        java.util.Arrays.sort(nums);
        java.util.Arrays.sort(freq);
        final long MOD = 1_000_000_007L;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            if (freq[i] == 0) continue;
            ans = (ans + (nums[i] * (freq[i] % MOD)) ) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in requests:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        freq = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            freq[i] = cur
        nums.sort()
        freq.sort()
        total = 0
        for a, f in zip(nums, freq):
            if f == 0:
                continue
            total = (total + a * f) % MOD
        return total
```

## Python3

```python
class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in requests:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        freq = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            freq[i] = cur
        nums.sort(reverse=True)
        freq.sort(reverse=True)
        ans = 0
        for a, f in zip(nums, freq):
            if f == 0:
                break
            ans = (ans + a * f) % MOD
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

static int cmp_ll(const void *a, const void *b) {
    long long va = *(const long long *)a;
    long long vb = *(const long long *)b;
    if (va == vb) return 0;
    return (va > vb) ? 1 : -1;
}

int maxSumRangeQuery(int* nums, int numsSize, int** requests, int requestsSize, int* requestsColSize) {
    const int MOD = 1000000007;

    int *diff = (int *)calloc(numsSize + 1, sizeof(int));
    for (int i = 0; i < requestsSize; ++i) {
        int l = requests[i][0];
        int r = requests[i][1];
        diff[l] += 1;
        if (r + 1 < numsSize) diff[r + 1] -= 1;
    }

    long long *freq = (long long *)malloc(numsSize * sizeof(long long));
    long long cur = 0;
    for (int i = 0; i < numsSize; ++i) {
        cur += diff[i];
        freq[i] = cur;
    }
    free(diff);

    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    qsort(freq, (size_t)numsSize, sizeof(long long), cmp_ll);

    long long ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        long long add = ((long long)(nums[i] % MOD) * (freq[i] % MOD)) % MOD;
        ans += add;
        if (ans >= MOD) ans -= MOD;
    }

    free(freq);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSumRangeQuery(int[] nums, int[][] requests) {
        int n = nums.Length;
        long[] diff = new long[n + 1];
        foreach (var req in requests) {
            int l = req[0];
            int r = req[1];
            diff[l] += 1;
            if (r + 1 < n) diff[r + 1] -= 1;
        }
        long[] freq = new long[n];
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            freq[i] = cur;
        }
        Array.Sort(nums);
        Array.Sort(freq);
        const int MOD = 1_000_000_007;
        long ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (freq[i] == 0) break;
            ans = (ans + ((long)nums[i] * freq[i]) % MOD) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} requests
 * @return {number}
 */
var maxSumRangeQuery = function(nums, requests) {
    const MOD = 1_000_000_007;
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    
    for (const [l, r] of requests) {
        diff[l] += 1;
        if (r + 1 < n) diff[r + 1] -= 1;
    }
    
    const freq = new Array(n);
    let cur = 0;
    for (let i = 0; i < n; ++i) {
        cur += diff[i];
        freq[i] = cur;
    }
    
    nums.sort((a, b) => b - a);
    freq.sort((a, b) => b - a);
    
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (freq[i] === 0) break;
        ans = (ans + (freq[i] * nums[i]) % MOD) % MOD;
    }
    
    return ans;
};
```

## Typescript

```typescript
function maxSumRangeQuery(nums: number[], requests: number[][]): number {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    for (const [l, r] of requests) {
        diff[l] += 1;
        if (r + 1 < n) diff[r + 1] -= 1;
    }
    const freq: number[] = new Array(n);
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        freq[i] = cur;
    }
    nums.sort((a, b) => b - a);
    freq.sort((a, b) => b - a);
    const MOD = 1_000_000_007;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (freq[i] === 0) break;
        ans = (ans + (nums[i] * freq[i]) % MOD) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $requests
     * @return Integer
     */
    function maxSumRangeQuery($nums, $requests) {
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        foreach ($requests as $req) {
            $l = $req[0];
            $r = $req[1];
            $diff[$l] += 1;
            if ($r + 1 < $n) {
                $diff[$r + 1] -= 1;
            }
        }

        $freq = array_fill(0, $n, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $freq[$i] = $cur;
        }

        rsort($nums);   // descending
        rsort($freq);   // descending

        $mod = 1000000007;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($freq[$i] == 0) break;
            $ans = ($ans + ($nums[$i] % $mod) * ($freq[$i] % $mod)) % $mod;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxSumRangeQuery(_ nums: [Int], _ requests: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        var diff = [Int](repeating: 0, count: n + 1)
        for req in requests {
            let l = req[0]
            let r = req[1]
            diff[l] += 1
            if r + 1 < n {
                diff[r + 1] -= 1
            }
        }
        var freq = [Int](repeating: 0, count: n)
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            freq[i] = cur
        }
        let sortedNums = nums.sorted(by: >)
        let sortedFreq = freq.sorted(by: >)
        var ans: Int64 = 0
        for i in 0..<n {
            if sortedFreq[i] == 0 { break }
            ans = (ans + Int64(sortedNums[i]) * Int64(sortedFreq[i])) % Int64(MOD)
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumRangeQuery(nums: IntArray, requests: Array<IntArray>): Int {
        val n = nums.size
        val diff = IntArray(n + 1)
        for (req in requests) {
            val l = req[0]
            val r = req[1]
            diff[l]++
            if (r + 1 < n) diff[r + 1]--
        }
        val freq = LongArray(n)
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            freq[i] = cur.toLong()
        }
        val sortedNums = nums.clone()
        java.util.Arrays.sort(sortedNums) // ascending
        java.util.Arrays.sort(freq) // ascending
        val MOD = 1_000_000_007L
        var ans = 0L
        for (i in n - 1 downTo 0) {
            ans = (ans + sortedNums[i].toLong() * freq[i]) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxSumRangeQuery(List<int> nums, List<List<int>> requests) {
    const int MOD = 1000000007;
    int n = nums.length;
    List<int> diff = List.filled(n + 1, 0);
    for (var req in requests) {
      int l = req[0];
      int r = req[1];
      diff[l] += 1;
      if (r + 1 < n) diff[r + 1] -= 1;
    }
    List<int> freq = List.filled(n, 0);
    int cur = 0;
    for (int i = 0; i < n; i++) {
      cur += diff[i];
      freq[i] = cur;
    }
    nums.sort((a, b) => b - a);
    freq.sort((a, b) => b - a);
    int ans = 0;
    for (int i = 0; i < n; i++) {
      if (freq[i] == 0) break;
      ans = (ans + (nums[i] % MOD) * (freq[i] % MOD)) % MOD;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func maxSumRangeQuery(nums []int, requests [][]int) int {
	n := len(nums)
	diff := make([]int64, n+1)

	for _, r := range requests {
		l, rr := r[0], r[1]
		diff[l]++
		if rr+1 < n {
			diff[rr+1]--
		}
	}

	freq := make([]int64, n)
	var cur int64
	for i := 0; i < n; i++ {
		cur += diff[i]
		freq[i] = cur
	}

	sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
	sort.Slice(freq, func(i, j int) bool { return freq[i] > freq[j] })

	const MOD int64 = 1e9 + 7
	var ans int64
	for i := 0; i < n && freq[i] > 0; i++ {
		ans = (ans + (int64(nums[i])%MOD)*(freq[i]%MOD)) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def max_sum_range_query(nums, requests)
  n = nums.length
  freq = Array.new(n, 0)

  requests.each do |l, r|
    freq[l] += 1
    freq[r + 1] -= 1 if r + 1 < n
  end

  (1...n).each { |i| freq[i] += freq[i - 1] }

  nums.sort!.reverse!
  freq.sort!.reverse!

  mod = 1_000_000_007
  ans = 0
  n.times do |i|
    break if freq[i] == 0
    ans = (ans + nums[i] * freq[i]) % mod
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxSumRangeQuery(nums: Array[Int], requests: Array[Array[Int]]): Int = {
        val MOD = 1000000007L
        val n = nums.length
        val diff = new Array[Long](n + 1)
        for (req <- requests) {
            val l = req(0)
            val r = req(1)
            diff(l) += 1
            if (r + 1 < n) diff(r + 1) -= 1
        }
        val freq = new Array[Long](n)
        var cur = 0L
        for (i <- 0 until n) {
            cur += diff(i)
            freq(i) = cur
        }
        java.util.Arrays.sort(nums)   // ascending
        java.util.Arrays.sort(freq)   // ascending
        var ans = 0L
        var i = n - 1
        while (i >= 0) {
            if (freq(i) > 0) {
                ans = (ans + (nums(i).toLong % MOD) * (freq(i) % MOD)) % MOD
            }
            i -= 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_range_query(nums: Vec<i32>, requests: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        // difference array to count frequency of each index
        let mut diff = vec![0i64; n + 1];
        for req in requests.iter() {
            let l = req[0] as usize;
            let r = req[1] as usize;
            diff[l] += 1;
            if r + 1 < n {
                diff[r + 1] -= 1;
            }
        }
        // prefix sum to get counts
        let mut cnt = vec![0i64; n];
        let mut cur = 0i64;
        for i in 0..n {
            cur += diff[i];
            cnt[i] = cur;
        }
        // sort nums and counts descending
        let mut nums_sorted: Vec<i64> = nums.into_iter().map(|x| x as i64).collect();
        nums_sorted.sort_by(|a, b| b.cmp(a));
        cnt.sort_by(|a, b| b.cmp(a));
        // compute answer
        let mut ans: i64 = 0;
        for i in 0..n {
            ans = (ans + nums_sorted[i] * cnt[i]) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (max-sum-range-query nums requests)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length nums))
         (diff (make-vector (+ n 1) 0)))
    ;; apply difference array updates
    (for-each (lambda (req)
                (define l (first req))
                (define r (second req))
                (vector-set! diff l (+ 1 (vector-ref diff l)))
                (vector-set! diff (+ r 1) (- (vector-ref diff (+ r 1)) 1)))
              requests)
    ;; compute frequencies per index
    (define freq (make-vector n 0))
    (let loop ((i 0) (cur 0))
      (when (< i n)
        (set! cur (+ cur (vector-ref diff i)))
        (vector-set! freq i cur)
        (loop (+ i 1) cur)))
    ;; sort nums and frequencies descending
    (define sorted-nums (list->vector (sort nums >)))
    (define sorted-freq (list->vector (sort (vector->list freq) >)))
    ;; accumulate answer modulo MOD
    (let loop2 ((i 0) (ans 0))
      (if (= i n)
          ans
          (let* ((prod (* (vector-ref sorted-nums i)
                         (vector-ref sorted-freq i)))
                 (new-ans (modulo (+ ans prod) MOD)))
            (loop2 (+ i 1) new-ans))))))
```

## Erlang

```erlang
-module(solution).
-export([max_sum_range_query/2]).

-define(MOD, 1000000007).

max_sum_range_query(Nums, Requests) ->
    N = length(Nums),
    DiffMap = build_diff_map(Requests, N, #{}),
    FreqList = freq_list(N, DiffMap),
    SortedNums = lists:reverse(lists:sort(Nums)),
    SortedFreq = lists:reverse(lists:sort(FreqList)),
    compute_sum(SortedNums, SortedFreq, 0).

%% Build difference map from requests
build_diff_map([], _N, Map) -> Map;
build_diff_map([[L,R]|Rest], N, Map) ->
    Map1 = add_diff(Map, L, 1),
    Map2 = if R + 1 < N -> add_diff(Map1, R + 1, -1);
              true       -> Map1
           end,
    build_diff_map(Rest, N, Map2).

add_diff(Map, Index, Delta) ->
    case maps:is_key(Index, Map) of
        true ->
            Old = maps:get(Index, Map),
            maps:put(Index, Old + Delta, Map);
        false ->
            maps:put(Index, Delta, Map)
    end.

%% Generate frequency list using prefix sum over diff map
freq_list(N, DiffMap) -> freq_list(0, 0, N, DiffMap, []).

freq_list(Index, Cur, N, _DiffMap, Acc) when Index == N ->
    lists:reverse(Acc);
freq_list(Index, Cur, N, DiffMap, Acc) ->
    Delta = maps:get(Index, DiffMap, 0),
    NewCur = Cur + Delta,
    freq_list(Index + 1, NewCur, N, DiffMap, [NewCur | Acc]).

%% Compute the total sum modulo MOD
compute_sum([], [], Sum) -> Sum rem ?MOD;
compute_sum([Num|NumsTail], [Freq|FreqTail], Acc) ->
    NewAcc = (Acc + (Num * Freq) rem ?MOD) rem ?MOD,
    compute_sum(NumsTail, FreqTail, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_range_query(nums :: [integer], requests :: [[integer]]) :: integer
  def max_sum_range_query(nums, requests) do
    n = length(nums)

    diff =
      :array.new(n + 1, default: 0)
      |> Enum.reduce(requests, fn [l, r], acc ->
        cur_l = :array.get(l, acc)
        acc = :array.set(l, cur_l + 1, acc)

        if r + 1 < n do
          cur_r = :array.get(r + 1, acc)
          :array.set(r + 1, cur_r - 1, acc)
        else
          acc
        end
      end)

    diff_list = :array.to_list(diff)

    {freq_rev, _} =
      Enum.reduce(Enum.with_index(diff_list), {[], 0}, fn {val, idx}, {acc, cur} ->
        if idx == n do
          {acc, cur}
        else
          new_cur = cur + val
          {[new_cur | acc], new_cur}
        end
      end)

    freq = Enum.reverse(freq_rev)

    sorted_nums = Enum.sort(nums, &>=/2)
    sorted_freq = Enum.sort(freq, &>=/2)

    mod = 1_000_000_007

    Enum.zip(sorted_nums, sorted_freq)
    |> Enum.reduce(0, fn {a, b}, sum -> (sum + a * b) rem mod end)
  end
end
```
