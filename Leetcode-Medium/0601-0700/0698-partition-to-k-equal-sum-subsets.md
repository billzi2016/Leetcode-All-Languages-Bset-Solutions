# 0698. Partition to K Equal Sum Subsets

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int n = nums.size();
        int total = accumulate(nums.begin(), nums.end(), 0);
        if (total % k != 0) return false;
        int target = total / k;
        sort(nums.rbegin(), nums.rend());
        if (nums[0] > target) return false;

        unordered_map<int, bool> memo;
        function<bool(int,int,int,int)> dfs = [&](int usedMask, int curSum, int startIdx, int bucketsLeft) -> bool {
            if (bucketsLeft == 1) return true; // last bucket will naturally have required sum
            if (curSum == target) {
                bool res = dfs(usedMask, 0, 0, bucketsLeft - 1);
                memo[usedMask] = res;
                return res;
            }
            if (memo.count(usedMask)) return memo[usedMask];
            for (int i = startIdx; i < n; ++i) {
                if (usedMask & (1 << i)) continue;
                int nextSum = curSum + nums[i];
                if (nextSum > target) continue;
                int newMask = usedMask | (1 << i);
                if (dfs(newMask, nextSum, i + 1, bucketsLeft)) {
                    memo[usedMask] = true;
                    return true;
                }
                // pruning: if we placed a number at the start of an empty bucket and it didn't lead to solution,
                // no need to try other numbers in this position (avoid symmetric states)
                if (curSum == 0) break;
                // also, if filling exactly reaches target but leads to dead end, no need to try further same-sized numbers
                if (nextSum == target) break;
            }
            memo[usedMask] = false;
            return false;
        };

        return dfs(0, 0, 0, k);
    }
};
```

## Java

```java
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int v : nums) total += v;
        if (total % k != 0) return false;
        int target = total / k;
        Arrays.sort(nums);
        int n = nums.length;
        if (nums[n - 1] > target) return false; // largest element too big
        boolean[] used = new boolean[n];
        return dfs(k, 0, 0, target, nums, used);
    }

    private boolean dfs(int bucketsLeft, int startIdx, int curSum, int target,
                        int[] nums, boolean[] used) {
        if (bucketsLeft == 1) return true; // last bucket will automatically be correct
        if (curSum == target) {
            // current bucket filled, move to next bucket
            return dfs(bucketsLeft - 1, nums.length - 1, 0, target, nums, used);
        }
        for (int i = startIdx; i >= 0; --i) {
            if (used[i] || curSum + nums[i] > target) continue;
            used[i] = true;
            if (dfs(bucketsLeft, i - 1, curSum + nums[i], target, nums, used))
                return true;
            used[i] = false;

            // pruning: if we placed the first element in an empty bucket and it didn't work,
            // no need to try other elements at this level (avoid symmetric states)
            if (curSum == 0) break;
            // also prune when exactly filling the bucket fails
            if (curSum + nums[i] == target) break;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        n = len(nums)
        if nums[0] > target:
            return False

        used = [False] * n

        # helper recursive function
        def dfs(k_remain, start_idx, cur_sum):
            if k_remain == 1:  # last bucket will automatically have required sum
                return True
            if cur_sum == target:
                # current bucket filled, move to next bucket
                return dfs(k_remain - 1, 0, 0)
            prev = -1
            for i in range(start_idx, n):
                if not used[i] and cur_sum + nums[i] <= target and nums[i] != prev:
                    used[i] = True
                    if dfs(k_remain, i + 1, cur_sum + nums[i]):
                        return True
                    used[i] = False
                    # pruning: if we placed the first element in an empty bucket and it fails,
                    # no need to try other elements of same value at this position.
                    if cur_sum == 0:
                        return False
                    # pruning: if filling exactly reaches target but leads to dead end, break
                    if cur_sum + nums[i] == target:
                        return False
                    prev = nums[i]
            return False

        return dfs(k, 0, 0)
```

## Python3

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        n = len(nums)
        if nums[0] > target:
            return False

        all_used = (1 << n) - 1
        memo = set()

        def dfs(used: int, cur_sum: int) -> bool:
            if used == all_used:
                return True
            if cur_sum == target:
                # start filling next bucket
                res = dfs(used, 0)
                if not res:
                    memo.add(used)
                return res
            if used in memo:
                return False
            for i in range(n):
                if not (used >> i) & 1 and cur_sum + nums[i] <= target:
                    if dfs(used | (1 << i), cur_sum + nums[i]):
                        return True
            memo.add(used)
            return False

        return dfs(0, 0)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int *g_nums;
static int g_n;
static int g_target;
static bool g_used[16];
static int g_k;

static bool dfs(int start, int kRemaining, int curSum) {
    if (kRemaining == 1) return true;               // last bucket will automatically have correct sum
    if (curSum == g_target)                         // current bucket filled, move to next bucket
        return dfs(0, kRemaining - 1, 0);
    for (int i = start; i < g_n; ++i) {
        if (g_used[i]) continue;
        int val = g_nums[i];
        if (curSum + val > g_target) continue;
        g_used[i] = true;
        if (dfs(i + 1, kRemaining, curSum + val)) return true;
        g_used[i] = false;
        // pruning: if we placed the first element of this bucket and it didn't lead to solution,
        // no need to try other elements at same level
        if (curSum == 0) break;
        // also prune duplicate values leading to same dead end
        while (i + 1 < g_n && g_nums[i] == g_nums[i + 1]) ++i;
    }
    return false;
}

static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return vb - va; // descending
}

bool canPartitionKSubsets(int* nums, int numsSize, int k) {
    if (k == 1) return true;
    long total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];
    if (total % k != 0) return false;
    g_target = (int)(total / k);
    // any element larger than target makes it impossible
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > g_target) return false;

    qsort(nums, numsSize, sizeof(int), cmp_desc);

    g_nums = nums;
    g_n = numsSize;
    g_k = k;
    for (int i = 0; i < numsSize; ++i) g_used[i] = false;

    return dfs(0, k, 0);
}
```

## Csharp

```csharp
using System;
using System.Linq;

public class Solution {
    public bool CanPartitionKSubsets(int[] nums, int k) {
        int total = nums.Sum();
        if (total % k != 0) return false;
        int target = total / k;
        Array.Sort(nums);
        Array.Reverse(nums); // descending order for better pruning
        if (nums[0] > target) return false;
        bool[] used = new bool[nums.Length];
        return Dfs(0, 0, k, target, nums, used);
    }

    private bool Dfs(int startIndex, int curSum, int bucketsLeft, int target, int[] nums, bool[] used) {
        if (bucketsLeft == 1) return true; // last bucket will automatically have required sum
        if (curSum == target) {
            // current bucket filled, move to next bucket
            return Dfs(0, 0, bucketsLeft - 1, target, nums, used);
        }

        for (int i = startIndex; i < nums.Length; i++) {
            if (used[i] || curSum + nums[i] > target) continue;

            used[i] = true;
            if (Dfs(i + 1, curSum + nums[i], bucketsLeft, target, nums, used))
                return true;
            used[i] = false;

            // pruning: if placing this number at the start of a bucket doesn't work,
            // no need to try other numbers of same value or further because they are
            // sorted descending.
            if (curSum == 0) break;               // first element failed, bucket can't be formed
            if (curSum + nums[i] == target) break; // exact fill leads to dead end
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canPartitionKSubsets = function(nums, k) {
    const total = nums.reduce((a, b) => a + b, 0);
    if (total % k !== 0) return false;
    const target = total / k;
    nums.sort((a, b) => b - a);
    if (nums[0] > target) return false;

    const groups = new Array(k).fill(0);

    function dfs(index) {
        if (index === nums.length) {
            // all numbers placed, each group must equal target
            return true;
        }
        const v = nums[index];
        for (let i = 0; i < k; i++) {
            if (groups[i] + v <= target) {
                groups[i] += v;
                if (dfs(index + 1)) return true;
                groups[i] -= v;
            }
            // If this group is empty, no need to try other empty groups
            if (groups[i] === 0) break;
        }
        return false;
    }

    return dfs(0);
};
```

## Typescript

```typescript
function canPartitionKSubsets(nums: number[], k: number): boolean {
    const total = nums.reduce((a, b) => a + b, 0);
    if (total % k !== 0) return false;
    const target = total / k;

    nums.sort((a, b) => b - a);
    if (nums[0] > target) return false;

    const n = nums.length;
    const used = new Array(n).fill(false);

    function dfs(remainingGroups: number, startIdx: number, curSum: number): boolean {
        if (remainingGroups === 1) return true; // last group will automatically have correct sum
        if (curSum === target) {
            // current group completed, move to next group
            return dfs(remainingGroups - 1, 0, 0);
        }

        for (let i = startIdx; i < n; i++) {
            if (used[i]) continue;
            const val = nums[i];
            if (curSum + val > target) continue;

            used[i] = true;
            if (dfs(remainingGroups, i + 1, curSum + val)) return true;
            used[i] = false;

            // pruning
            if (curSum === 0) break;          // if first element can't lead to solution, no need to try others as start
            if (curSum + val === target) break; // if filling exactly but fails later, stop trying other equal options
        }
        return false;
    }

    return dfs(k, 0, 0);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function canPartitionKSubsets($nums, $k) {
        $total = array_sum($nums);
        if ($total % $k !== 0) {
            return false;
        }
        $target = intdiv($total, $k);
        rsort($nums); // descending order for better pruning
        if ($nums[0] > $target) {
            return false;
        }

        $n = count($nums);
        $memo = [];

        $dfs = function($usedMask, $curSum, $startIdx, $bucket) use (&$dfs, &$nums, $n, $target, $k, &$memo) {
            if ($bucket == $k - 1) {
                // Last bucket will automatically have the required sum
                return true;
            }
            if ($curSum == $target) {
                // Current bucket completed, move to next bucket
                if ($dfs($usedMask, 0, 0, $bucket + 1)) {
                    return true;
                }
            }

            if (isset($memo[$usedMask])) {
                return false;
            }

            for ($i = $startIdx; $i < $n; $i++) {
                if ((($usedMask >> $i) & 1) == 0 && $curSum + $nums[$i] <= $target) {
                    $newMask = $usedMask | (1 << $i);
                    if ($dfs($newMask, $curSum + $nums[$i], $i + 1, $bucket)) {
                        return true;
                    }
                }
            }

            $memo[$usedMask] = false;
            return false;
        };

        return $dfs(0, 0, 0, 0);
    }
}
```

## Swift

```swift
class Solution {
    func canPartitionKSubsets(_ nums: [Int], _ k: Int) -> Bool {
        let total = nums.reduce(0, +)
        if total % k != 0 { return false }
        let target = total / k
        var sortedNums = nums.sorted(by: >)
        if sortedNums.first! > target { return false }
        let n = sortedNums.count
        var used = [Bool](repeating: false, count: n)

        func backtrack(_ bucket: Int, _ startIdx: Int, _ curSum: Int) -> Bool {
            if bucket == k { return true }
            if curSum == target {
                return backtrack(bucket + 1, 0, 0)
            }

            var i = startIdx
            while i < n {
                if !used[i] && curSum + sortedNums[i] <= target {
                    used[i] = true
                    if backtrack(bucket, i + 1, curSum + sortedNums[i]) {
                        return true
                    }
                    used[i] = false

                    if curSum == 0 { return false }

                    var j = i + 1
                    while j < n && sortedNums[j] == sortedNums[i] {
                        j += 1
                    }
                    i = j - 1
                }
                i += 1
            }
            return false
        }

        return backtrack(0, 0, 0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canPartitionKSubsets(nums: IntArray, k: Int): Boolean {
        val total = nums.sum()
        if (total % k != 0) return false
        val target = total / k
        java.util.Arrays.sort(nums)
        if (nums[nums.size - 1] > target) return false

        val n = nums.size
        val memo = IntArray(1 shl n) { -1 }

        fun dfs(mask: Int, curSum: Int, groupsFormed: Int): Boolean {
            if (groupsFormed == k - 1) return true
            if (curSum == target) {
                val res = dfs(mask, 0, groupsFormed + 1)
                memo[mask] = if (res) 1 else 0
                return res
            }
            if (memo[mask] != -1) return memo[mask] == 1

            var i = n - 1
            while (i >= 0) {
                val bit = 1 shl i
                if ((mask and bit) == 0 && curSum + nums[i] <= target) {
                    if (dfs(mask or bit, curSum + nums[i], groupsFormed)) {
                        memo[mask] = 1
                        return true
                    }
                }
                i--
            }
            memo[mask] = 0
            return false
        }

        return dfs(0, 0, 0)
    }
}
```

## Dart

```dart
class Solution {
  bool canPartitionKSubsets(List<int> nums, int k) {
    int n = nums.length;
    int total = nums.fold(0, (a, b) => a + b);
    if (total % k != 0) return false;
    int target = total ~/ k;

    List<int> arr = List.from(nums);
    arr.sort((a, b) => b.compareTo(a));
    if (arr[0] > target) return false;

    int allMask = (1 << n) - 1;
    Map<int, bool> memo = {};

    bool dfs(int usedMask, int curSum, int startIdx, int groupsRemaining) {
      if (groupsRemaining == 0) return true; // all groups formed
      if (curSum == target) {
        bool res = dfs(usedMask, 0, 0, groupsRemaining - 1);
        memo[usedMask] = res;
        return res;
      }
      if (memo.containsKey(usedMask)) return false;

      for (int i = startIdx; i < n; ++i) {
        int bit = 1 << i;
        if ((usedMask & bit) != 0) continue;
        int newSum = curSum + arr[i];
        if (newSum > target) continue;
        if (dfs(usedMask | bit, newSum, i + 1, groupsRemaining)) return true;

        // pruning
        if (curSum == 0) break;          // first element didn't fit, no need to try others at this level
        if (newSum == target) break;     // exact fill failed, stop further tries
      }

      memo[usedMask] = false;
      return false;
    }

    return dfs(0, 0, 0, k);
  }
}
```

## Golang

```go
import "sort"

func canPartitionKSubsets(nums []int, k int) bool {
	n := len(nums)
	if k == 0 || k > n {
		return false
	}
	total := 0
	for _, v := range nums {
		total += v
	}
	if total%k != 0 {
		return false
	}
	target := total / k

	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	if nums[0] > target {
		return false
	}

	used := make([]bool, n)

	var dfs func(remainingBuckets int, startIdx int, curSum int) bool
	dfs = func(remainingBuckets int, startIdx int, curSum int) bool {
		if remainingBuckets == 1 {
			return true // last bucket will automatically have the required sum
		}
		if curSum == target {
			return dfs(remainingBuckets-1, 0, 0)
		}

		prev := -1
		for i := startIdx; i < n; i++ {
			if used[i] || curSum+nums[i] > target {
				continue
			}
			if prev != -1 && nums[i] == prev {
				continue // skip duplicates to reduce symmetric states
			}
			used[i] = true
			if dfs(remainingBuckets, i+1, curSum+nums[i]) {
				return true
			}
			used[i] = false
			prev = nums[i]

			if curSum == 0 || curSum+nums[i] == target {
				break // pruning: if first element fails or completing bucket fails, no need to try further
			}
		}
		return false
	}

	return dfs(k, 0, 0)
}
```

## Ruby

```ruby
def can_partition_k_subsets(nums, k)
  total = nums.sum
  return false if total % k != 0
  target = total / k

  nums.sort!.reverse!
  return false if nums[0] > target

  n = nums.length
  buckets = Array.new(k, 0)

  dfs = nil
  dfs = ->(idx) {
    return true if idx == n
    val = nums[idx]
    k.times do |i|
      if buckets[i] + val <= target
        buckets[i] += val
        return true if dfs.call(idx + 1)
        buckets[i] -= val
      end
      break if buckets[i] == 0
    end
    false
  }

  dfs.call(0)
end
```

## Scala

```scala
object Solution {
  def canPartitionKSubsets(nums: Array[Int], k: Int): Boolean = {
    val total = nums.sum
    if (total % k != 0) return false
    val target = total / k
    val sorted = nums.sorted(Ordering[Int].reverse)
    if (sorted.head > target) return false

    val n = sorted.length
    val used = Array.fill[Boolean](n)(false)

    def dfs(kRemaining: Int, startIdx: Int, curSum: Int): Boolean = {
      if (kRemaining == 1) true
      else if (curSum == target) {
        dfs(kRemaining - 1, 0, 0)
      } else {
        var i = startIdx
        while (i < n) {
          if (!used(i) && curSum + sorted(i) <= target) {
            used(i) = true
            if (dfs(kRemaining, i + 1, curSum + sorted(i))) return true
            used(i) = false
            if (curSum == 0) return false
            if (curSum + sorted(i) == target) return false
          }
          i += 1
        }
        false
      }
    }

    dfs(k, 0, 0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn can_partition_k_subsets(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        if k as usize > n {
            return false;
        }
        let total: i32 = nums.iter().sum();
        if total % k != 0 {
            return false;
        }
        let target = total / k;
        for &v in &nums {
            if v > target {
                return false;
            }
        }

        let full_mask = (1usize << n) - 1;
        let mut dp = vec![-1i32; 1usize << n];
        dp[0] = 0;

        for mask in 0..=full_mask {
            if dp[mask] == -1 {
                continue;
            }
            let cur_sum = dp[mask];
            for i in 0..n {
                if (mask >> i) & 1 == 0 {
                    let next_sum = cur_sum + nums[i];
                    if next_sum <= target {
                        let new_mask = mask | (1usize << i);
                        let rem = next_sum % target;
                        if dp[new_mask] == -1 {
                            dp[new_mask] = rem;
                        }
                    }
                }
            }
        }

        dp[full_mask] == 0
    }
}
```

## Racket

```racket
(define/contract (can-partition-k-subsets nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ((n (length nums))
         (total (apply + nums)))
    (if (or (= k 0) (> k n) (not (= (remainder total k) 0)))
        #false
        (let* ((target (/ total k))
               (sorted (sort nums >))                     ; descending for pruning
               (numsV (list->vector sorted))
               (fullMask (sub1 (arithmetic-shift 1 n)))   ; 2^n - 1
               (memo (make-hash)))
          (define (search used cur-sum start)
            (cond
              [(= used fullMask) #true]
              [(= cur-sum target) (search used 0 0)]
              [else
               (if (hash-has-key? memo used)
                   #false
                   (let loop ((i start))
                     (cond
                       [(>= i n)
                        (begin (hash-set! memo used #t) #false)]
                       [else
                        (define bit (arithmetic-shift 1 i))
                        (if (zero? (bitwise-and used bit))
                            (let ((v (vector-ref numsV i)))
                              (if (<= (+ cur-sum v) target)
                                  (if (search (bitwise-ior used bit) (+ cur-sum v) (add1 i))
                                      #t
                                      (begin
                                        ;; prune: if we failed to place the first element of a new bucket,
                                        ;; no need to try other elements at this level.
                                        (when (= cur-sum 0)
                                          (hash-set! memo used #t))
                                        (loop (add1 i))))
                                  (loop (add1 i))))
                            (loop (add1 i))))))]))])
          (if (> (vector-ref numsV 0) target)
              #false
              (search 0 0 0))))))
```

## Erlang

```erlang
-module(solution).
-export([can_partition_k_subsets/2]).

-spec can_partition_k_subsets(Nums :: [integer()], K :: integer()) -> boolean().
can_partition_k_subsets(Nums, K) ->
    Sum = lists:sum(Nums),
    case Sum rem K of
        0 ->
            Target = Sum div K,
            Sorted = lists:sort(fun(A, B) -> A > B end, Nums),
            case lists:any(fun(X) -> X > Target end, Sorted) of
                true -> false;
                false ->
                    N = length(Sorted),
                    FullMask = (1 bsl N) - 1,
                    NumsTuple = list_to_tuple(Sorted),
                    {Res, _} = search(NumsTuple, N, Target, FullMask, 0, 0, #{}),
                    Res
            end;
        _ -> false
    end.

search(_NumsTuple, _N, _Target, FullMask, UsedMask, _CurrSum, Memo) when UsedMask == FullMask ->
    {true, Memo};
search(NumsTuple, N, Target, FullMask, UsedMask, CurrSum, Memo) when CurrSum == Target ->
    {Res, NewMemo} = search(NumsTuple, N, Target, FullMask, UsedMask, 0, Memo),
    case Res of
        true -> {true, NewMemo};
        false -> {false, maps:put(UsedMask, false, NewMemo)}
    end;
search(NumsTuple, N, Target, FullMask, UsedMask, CurrSum, Memo) ->
    case maps:is_key(UsedMask, Memo) of
        true -> {false, Memo};
        false -> try_indices(0, NumsTuple, N, Target, FullMask, UsedMask, CurrSum, Memo)
    end.

try_indices(I, _NumsTuple, N, _Target, _FullMask, _UsedMask, _CurrSum, Memo) when I >= N ->
    {false, maps:put(_UsedMask, false, Memo)};
try_indices(I, NumsTuple, N, Target, FullMask, UsedMask, CurrSum, Memo) ->
    Bit = 1 bsl I,
    case (UsedMask band Bit) of
        0 ->
            Num = element(I + 1, NumsTuple),
            if Num + CurrSum =< Target ->
                    NewMask = UsedMask bor Bit,
                    {Res, NewMemo} = search(NumsTuple, N, Target, FullMask, NewMask, CurrSum + Num, Memo),
                    case Res of
                        true -> {true, NewMemo};
                        false -> try_indices(I + 1, NumsTuple, N, Target, FullMask, UsedMask, CurrSum, NewMemo)
                    end;
               true ->
                    try_indices(I + 1, NumsTuple, N, Target, FullMask, UsedMask, CurrSum, Memo)
            end;
        _ ->
            try_indices(I + 1, NumsTuple, N, Target, FullMask, UsedMask, CurrSum, Memo)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_partition_k_subsets(nums :: [integer], k :: integer) :: boolean
  def can_partition_k_subsets(nums, k) do
    total = Enum.sum(nums)

    if rem(total, k) != 0 do
      false
    else
      target = div(total, k)
      sorted = Enum.sort(nums, &>=/2)
      n = length(sorted)

      if Enum.any?(sorted, fn x -> x > target end) do
        false
      else
        {result, _} = dfs(sorted, target, k, n, 0, 0, 0, 0, %{})
        result
      end
    end
  end

  import Bitwise

  defp dfs(_nums, _target, k, _n, _used, _cur_sum, _start_idx, groups_done, memo) when groups_done == k - 1 do
    {true, memo}
  end

  defp dfs(nums, target, k, n, used, cur_sum, start_idx, groups_done, memo) do
    cond do
      cur_sum == target ->
        dfs(nums, target, k, n, used, 0, 0, groups_done + 1, memo)

      Map.has_key?(memo, used) ->
        {false, memo}

      true ->
        range = start_idx..(n - 1)

        {found, new_memo} =
          Enum.reduce_while(range, {false, memo}, fn i, {_found, mem} ->
            if (used &&& (1 <<< i)) == 0 and cur_sum + Enum.at(nums, i) <= target do
              new_used = used ||| (1 <<< i)

              {res, res_memo} =
                dfs(nums, target, k, n, new_used, cur_sum + Enum.at(nums, i), i + 1, groups_done, mem)

              if res do
                {:halt, {true, res_memo}}
              else
                {:cont, {false, res_memo}}
              end
            else
              {:cont, {false, mem}}
            end
          end)

        if found do
          {true, new_memo}
        else
          {false, Map.put(new_memo, used, true)}
        end
    end
  end
end
```
