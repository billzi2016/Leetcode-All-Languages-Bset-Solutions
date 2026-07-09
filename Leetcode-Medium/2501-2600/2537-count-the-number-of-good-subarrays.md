# 2537. Count the Number of Good Subarrays

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, long long> cnt;
        long long curPairs = 0;
        long long ans = 0;
        int r = -1;
        for (int l = 0; l < n; ++l) {
            while (r + 1 < n && curPairs < k) {
                ++r;
                int val = nums[r];
                long long prev = cnt[val];
                curPairs += prev;
                cnt[val] = prev + 1;
            }
            if (curPairs >= k) {
                ans += n - r;
            } else {
                break; // cannot reach k for this and further l
            }
            int valL = nums[l];
            long long c = cnt[valL];          // current count including nums[l]
            cnt[valL] = c - 1;                 // decrement count
            curPairs -= (c - 1);               // remove pairs contributed by nums[l]
            if (cnt[valL] == 0) cnt.erase(valL);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countGood(int[] nums, int k) {
        int n = nums.length;
        java.util.HashMap<Integer, Integer> cnt = new java.util.HashMap<>();
        long pairs = 0;
        long ans = 0;
        int r = -1;
        for (int l = 0; l < n; ++l) {
            while (r + 1 < n && pairs < k) {
                ++r;
                int val = nums[r];
                int c = cnt.getOrDefault(val, 0);
                pairs += c;               // new pairs formed with existing occurrences
                cnt.put(val, c + 1);
            }
            if (pairs >= k) {
                ans += n - r;              // all extensions to the right are also good
            } else {
                break;                     // cannot reach k any more
            }
            int valL = nums[l];
            int cL = cnt.get(valL);        // current count of this value
            pairs -= (cL - 1);             // remove pairs contributed by this leftmost element
            if (cL == 1) {
                cnt.remove(valL);
            } else {
                cnt.put(valL, cL - 1);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cnt = {}
        total_pairs = 0
        ans = 0
        r = -1

        for l in range(n):
            while r + 1 < n and total_pairs < k:
                r += 1
                x = nums[r]
                prev = cnt.get(x, 0)
                total_pairs += prev          # each previous occurrence forms a new pair
                cnt[x] = prev + 1

            if total_pairs >= k:
                ans += n - r                 # all subarrays ending at >= r are good
            else:
                break                        # cannot reach k any more

            # remove nums[l] from the window before moving left pointer
            x = nums[l]
            cur = cnt[x]
            total_pairs -= (cur - 1)         # pairs lost when this occurrence is removed
            if cur == 1:
                del cnt[x]
            else:
                cnt[x] = cur - 1

        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        total_pairs = 0
        right = -1
        ans = 0

        for left in range(n):
            while right + 1 < n and total_pairs < k:
                right += 1
                x = nums[right]
                total_pairs += cnt[x]   # new pairs formed with existing occurrences
                cnt[x] += 1

            if total_pairs >= k:
                ans += n - right

            # remove left element from window
            x = nums[left]
            cnt[x] -= 1
            total_pairs -= cnt[x]  # subtract pairs contributed by this occurrence

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int idx;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->val != pb->val) return pa->val < pb->val ? -1 : 1;
    return pa->idx - pb->idx;
}

long long countGood(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    // Coordinate compression
    Pair *arr = (Pair *)malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
    }
    qsort(arr, numsSize, sizeof(Pair), cmpPair);
    
    int *comp = (int *)malloc(numsSize * sizeof(int));
    int curId = -1;
    int prevVal = 0; // dummy init
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || arr[i].val != prevVal) {
            ++curId;
            prevVal = arr[i].val;
        }
        comp[arr[i].idx] = curId;
    }
    int distinct = curId + 1;
    free(arr);
    
    int *cnt = (int *)calloc(distinct, sizeof(int));
    long long pairs = 0;
    long long ans = 0;
    int r = -1;
    
    for (int l = 0; l < numsSize; ++l) {
        while (r + 1 < numsSize && pairs < k) {
            ++r;
            int id = comp[r];
            pairs += cnt[id];
            cnt[id]++;
        }
        if (pairs >= k) {
            ans += (long long)(numsSize - r);
        } else {
            // No further windows can satisfy the condition
            break;
        }
        int idl = comp[l];
        cnt[idl]--;
        pairs -= cnt[idl];  // subtract pairs contributed by removed element
    }
    
    free(cnt);
    free(comp);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public long CountGood(int[] nums, int k) {
        int n = nums.Length;
        var cnt = new Dictionary<int, int>();
        long totalPairs = 0;
        long ans = 0;
        int r = -1;

        for (int l = 0; l < n; ++l) {
            while (r + 1 < n && totalPairs < k) {
                r++;
                int val = nums[r];
                cnt.TryGetValue(val, out int c);
                totalPairs += c;
                cnt[val] = c + 1;
            }

            if (totalPairs >= k) {
                ans += n - r;
            } else {
                break; // cannot reach k for this and any further left
            }

            int leftVal = nums[l];
            cnt.TryGetValue(leftVal, out int cl);
            // cl is current count before removal (>=1)
            cnt[leftVal] = cl - 1;
            totalPairs -= (cl - 1);
            if (cnt[leftVal] == 0) {
                cnt.Remove(leftVal);
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
 * @param {number} k
 * @return {number}
 */
var countGood = function(nums, k) {
    const n = nums.length;
    const freq = new Map();
    let right = 0;
    let pairs = 0;
    let ans = 0;

    for (let left = 0; left < n; left++) {
        while (right < n && pairs < k) {
            const val = nums[right];
            const cnt = freq.get(val) || 0;
            pairs += cnt;
            freq.set(val, cnt + 1);
            right++;
        }
        if (pairs >= k) {
            ans += n - right + 1;
        }

        // remove left element from window
        const valL = nums[left];
        const cntL = freq.get(valL); // must exist
        pairs -= (cntL - 1);
        if (cntL === 1) {
            freq.delete(valL);
        } else {
            freq.set(valL, cntL - 1);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function countGood(nums: number[], k: number): number {
    const n = nums.length;
    const cnt = new Map<number, number>();
    let curPairs = 0;
    let ans = 0;
    let r = -1;

    for (let l = 0; l < n; ++l) {
        while (r + 1 < n && curPairs < k) {
            r++;
            const val = nums[r];
            const prev = cnt.get(val) ?? 0;
            curPairs += prev;
            cnt.set(val, prev + 1);
        }

        if (curPairs >= k) {
            ans += n - r;
        } else {
            break;
        }

        const leftVal = nums[l];
        const leftCount = cnt.get(leftVal)!;
        curPairs -= leftCount - 1;
        if (leftCount === 1) {
            cnt.delete(leftVal);
        } else {
            cnt.set(leftVal, leftCount - 1);
        }
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
    function countGood($nums, $k) {
        $n = count($nums);
        $cnt = [];
        $pairs = 0;
        $right = -1;
        $ans = 0;

        for ($left = 0; $left < $n; $left++) {
            while ($right + 1 < $n && $pairs < $k) {
                $right++;
                $val = $nums[$right];
                $prev = $cnt[$val] ?? 0;
                $pairs += $prev;
                $cnt[$val] = $prev + 1;
            }

            if ($pairs >= $k) {
                $ans += $n - $right;
            } else {
                break;
            }

            $valL = $nums[$left];
            $cntVal = $cnt[$valL];
            $pairs -= ($cntVal - 1);
            $cnt[$valL] = $cntVal - 1;
            if ($cnt[$valL] == 0) {
                unset($cnt[$valL]);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countGood(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var cnt = [Int:Int]()
        var right = -1
        var curPairs: Int64 = 0
        var ans: Int64 = 0
        let target = Int64(k)
        
        for left in 0..<n {
            while right + 1 < n && curPairs < target {
                right += 1
                let v = nums[right]
                let c = cnt[v] ?? 0
                curPairs += Int64(c)
                cnt[v] = c + 1
            }
            
            if curPairs >= target {
                ans += Int64(n - right)
            } else {
                break
            }
            
            // remove left element
            let vLeft = nums[left]
            if let c = cnt[vLeft] {
                curPairs -= Int64(c - 1)
                if c == 1 {
                    cnt.removeValue(forKey: vLeft)
                } else {
                    cnt[vLeft] = c - 1
                }
            }
        }
        
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countGood(nums: IntArray, k: Int): Long {
        val n = nums.size
        var right = -1
        var pairs = 0L
        var ans = 0L
        val cnt = HashMap<Int, Int>()
        for (left in 0 until n) {
            while (right + 1 < n && pairs < k) {
                right++
                val x = nums[right]
                val c = cnt.getOrDefault(x, 0)
                pairs += c.toLong()
                cnt[x] = c + 1
            }
            if (pairs >= k) {
                ans += (n - right).toLong()
            } else {
                break
            }
            val y = nums[left]
            val countY = cnt[y]!!
            pairs -= (countY - 1).toLong()
            if (countY == 1) {
                cnt.remove(y)
            } else {
                cnt[y] = countY - 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countGood(List<int> nums, int k) {
    int n = nums.length;
    Map<int, int> cnt = {};
    int totalPairs = 0;
    int ans = 0;
    int right = -1;

    for (int left = 0; left < n; ++left) {
      while (right + 1 < n && totalPairs < k) {
        right++;
        int x = nums[right];
        int c = cnt[x] ?? 0;
        totalPairs += c;
        cnt[x] = c + 1;
      }
      if (totalPairs >= k) {
        ans += n - right;
      } else {
        break;
      }

      int x = nums[left];
      int c = cnt[x]!;
      totalPairs -= (c - 1);
      if (c == 1) {
        cnt.remove(x);
      } else {
        cnt[x] = c - 1;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countGood(nums []int, k int) int64 {
    n := len(nums)
    cnt := make(map[int]int)
    var curPairs int64
    var ans int64
    right := -1

    for left := 0; left < n; left++ {
        for right+1 < n && curPairs < int64(k) {
            right++
            c := cnt[nums[right]]
            curPairs += int64(c)
            cnt[nums[right]] = c + 1
        }
        if curPairs >= int64(k) {
            ans += int64(n - right)
        } else {
            break
        }

        c := cnt[nums[left]]
        curPairs -= int64(c - 1)
        if c == 1 {
            delete(cnt, nums[left])
        } else {
            cnt[nums[left]] = c - 1
        }
    }
    return ans
}
```

## Ruby

```ruby
def count_good(nums, k)
  n = nums.length
  cnt = Hash.new(0)
  total_pairs = 0
  right = -1
  ans = 0

  (0...n).each do |left|
    while right + 1 < n && total_pairs < k
      right += 1
      x = nums[right]
      total_pairs += cnt[x]
      cnt[x] += 1
    end

    break if total_pairs < k   # cannot reach k anymore

    ans += n - right

    x = nums[left]
    total_pairs -= (cnt[x] - 1)
    cnt[x] -= 1
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countGood(nums: Array[Int], k: Int): Long = {
        val n = nums.length
        val cnt = scala.collection.mutable.HashMap[Int, Int]()
        var totalPairs: Long = 0L
        var ans: Long = 0L
        var r = -1
        var l = 0
        while (l < n) {
            while (r + 1 < n && totalPairs < k) {
                r += 1
                val x = nums(r)
                val prev = cnt.getOrElse(x, 0)
                totalPairs += prev.toLong
                cnt.update(x, prev + 1)
            }
            if (totalPairs < k) return ans
            ans += (n - r).toLong
            val x = nums(l)
            val cur = cnt.getOrElse(x, 0)
            totalPairs -= (cur - 1).toLong
            if (cur == 1) cnt.remove(x) else cnt.update(x, cur - 1)
            l += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_good(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut cnt: HashMap<i32, i64> = HashMap::new();
        let mut right: usize = 0;
        let mut pairs: i64 = 0;
        let mut ans: i64 = 0;
        let k_i64 = k as i64;

        for left in 0..n {
            while right < n && pairs < k_i64 {
                let x = nums[right];
                let entry = cnt.entry(x).or_insert(0);
                pairs += *entry; // new pairs formed with existing occurrences
                *entry += 1;
                right += 1;
            }

            if pairs >= k_i64 {
                ans += (n - right + 1) as i64;
            } else {
                break; // cannot reach k for this and further left positions
            }

            // remove nums[left] from the window
            let y = nums[left];
            {
                let entry = cnt.get_mut(&y).unwrap();
                pairs -= *entry - 1; // subtract pairs contributed by this occurrence
                *entry -= 1;
            }
            if let Some(&0) = cnt.get(&y) {
                cnt.remove(&y);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-good nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (cnt (make-hash))
         (right -1)
         (curPairs 0)
         (ans 0)
         (done #f))
    (for ([left (in-range n)])
      (when (not done)
        ;; expand right until we have at least k pairs or reach the end
        (while (and (< (+ right 1) n) (< curPairs k))
          (set! right (+ right 1))
          (define x (vector-ref v right))
          (define c (hash-ref cnt x 0))
          (set! curPairs (+ curPairs c))
          (hash-set! cnt x (+ c 1)))
        (if (>= curPairs k)
            (set! ans (+ ans (- n right)))   ; all subarrays starting at left with end >= right are good
            (set! done #t))                  ; cannot reach k any more, stop processing further lefts
        ;; slide window: remove element at position left
        (when (not done)
          (define y (vector-ref v left))
          (define c (hash-ref cnt y 0))
          (define newc (- c 1))
          (if (= newc 0)
              (hash-remove! cnt y)
              (hash-set! cnt y newc))
          (set! curPairs (- curPairs newc)))))
    ans))
```

## Erlang

```erlang
count_good(Nums, K) ->
    N = length(Nums),
    Arr = list_to_tuple(Nums),
    loop_left(0, -1, 0, #{}, 0, N, Arr, K).

loop_left(L, _R, _Pairs, _CountMap, Ans, N, _Arr, _K) when L == N ->
    Ans;
loop_left(L, R, Pairs, CountMap, Ans, N, Arr, K) ->
    {NewR, NewPairs, NewCountMap} = expand(R, Pairs, CountMap, Arr, N, K),
    Add = if NewPairs >= K -> N - NewR; true -> 0 end,
    Ans2 = Ans + Add,
    case L =< NewR of
        true ->
            ValL = element(L + 1, Arr),
            C = maps:get(ValL, NewCountMap),
            PairsAfterRemoval = NewPairs - (C - 1),
            CountMapAfterRemoval =
                if C == 1 -> maps:remove(ValL, NewCountMap);
                   true   -> maps:put(ValL, C - 1, NewCountMap)
                end,
            loop_left(L + 1, NewR, PairsAfterRemoval, CountMapAfterRemoval, Ans2, N, Arr, K);
        false ->
            % window already empty
            loop_left(L + 1, NewR, NewPairs, NewCountMap, Ans2, N, Arr, K)
    end.

expand(R, Pairs, CountMap, _Arr, N, _K) when Pairs >= 0, (Pairs >= 0), false -> ok. % placeholder to avoid warning
expand(R, Pairs, CountMap, Arr, N, K) ->
    case (Pairs >= K) orelse (R + 1 >= N) of
        true ->
            {R, Pairs, CountMap};
        false ->
            NextIdx = R + 1,
            Val = element(NextIdx + 1, Arr),
            C = maps:get(Val, CountMap, 0),
            NewPairs = Pairs + C,
            NewCountMap = maps:put(Val, C + 1, CountMap),
            expand(NextIdx, NewPairs, NewCountMap, Arr, N, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_good(nums :: [integer], k :: integer) :: integer
  def count_good(nums, k) do
    arr = List.to_tuple(nums)
    n = tuple_size(arr)

    loop(0, -1, 0, %{}, 0, k, n, arr)
  end

  defp loop(left, _right, _pairs, _counts, ans, _k, n, _arr) when left >= n do
    ans
  end

  defp loop(left, right, pairs, counts, ans, k, n, arr) do
    {right2, pairs2, counts2} = expand(right, pairs, counts, k, n, arr)

    if pairs2 >= k do
      ans2 = ans + (n - right2)

      val_l = elem(arr, left)
      cnt_l = Map.get(counts2, val_l)

      pairs3 = pairs2 - (cnt_l - 1)

      counts3 =
        if cnt_l == 1 do
          Map.delete(counts2, val_l)
        else
          Map.put(counts2, val_l, cnt_l - 1)
        end

      loop(left + 1, right2, pairs3, counts3, ans2, k, n, arr)
    else
      ans
    end
  end

  defp expand(right, pairs, counts, k, n, arr) do
    if right + 1 < n and pairs < k do
      r = right + 1
      val = elem(arr, r)
      cnt = Map.get(counts, val, 0)

      pairs2 = pairs + cnt
      counts2 = Map.put(counts, val, cnt + 1)

      expand(r, pairs2, counts2, k, n, arr)
    else
      {right, pairs, counts}
    end
  end
end
```
