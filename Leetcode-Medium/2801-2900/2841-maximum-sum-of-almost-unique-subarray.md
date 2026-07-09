# 2841. Maximum Sum of Almost Unique Subarray

## Cpp

```cpp
class Solution {
public:
    long long maxSum(vector<int>& nums, int m, int k) {
        int n = nums.size();
        unordered_map<int,int> cnt;
        long long sum = 0;
        int distinct = 0;
        long long ans = 0;
        
        // initial window
        for (int i = 0; i < k; ++i) {
            sum += nums[i];
            if (++cnt[nums[i]] == 1) distinct++;
        }
        if (distinct >= m) ans = max(ans, sum);
        
        // slide the window
        for (int i = k; i < n; ++i) {
            int outVal = nums[i - k];
            // remove outgoing element
            sum -= outVal;
            if (--cnt[outVal] == 0) {
                cnt.erase(outVal);
                distinct--;
            }
            // add incoming element
            int inVal = nums[i];
            sum += inVal;
            if (++cnt[inVal] == 1) distinct++;
            
            if (distinct >= m) ans = max(ans, sum);
        }
        
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxSum(List<Integer> nums, int m, int k) {
        int n = nums.size();
        if (k > n) return 0;
        Map<Integer, Integer> freq = new HashMap<>();
        long sum = 0;
        for (int i = 0; i < k; i++) {
            int val = nums.get(i);
            sum += val;
            freq.put(val, freq.getOrDefault(val, 0) + 1);
        }
        long ans = 0;
        if (freq.size() >= m) ans = sum;
        for (int i = k; i < n; i++) {
            int outVal = nums.get(i - k);
            int cntOut = freq.get(outVal);
            if (cntOut == 1) {
                freq.remove(outVal);
            } else {
                freq.put(outVal, cntOut - 1);
            }
            sum -= outVal;
            
            int inVal = nums.get(i);
            sum += inVal;
            freq.put(inVal, freq.getOrDefault(inVal, 0) + 1);
            
            if (freq.size() >= m) {
                ans = Math.max(ans, sum);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        freq = {}
        distinct = 0
        cur_sum = 0
        best = 0

        for i, val in enumerate(nums):
            # add new element
            cur_sum += val
            if freq.get(val, 0) == 0:
                distinct += 1
            freq[val] = freq.get(val, 0) + 1

            # remove element leaving the window
            if i >= k:
                out_val = nums[i - k]
                cur_sum -= out_val
                if freq[out_val] == 1:
                    distinct -= 1
                    del freq[out_val]
                else:
                    freq[out_val] -= 1

            # evaluate full window
            if i >= k - 1 and distinct >= m:
                if cur_sum > best:
                    best = cur_sum

        return best
```

## Python3

```python
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        from collections import defaultdict

        cnt = defaultdict(int)
        distinct = 0
        cur_sum = 0
        n = len(nums)

        # initialize first window
        for i in range(k):
            val = nums[i]
            if cnt[val] == 0:
                distinct += 1
            cnt[val] += 1
            cur_sum += val

        ans = cur_sum if distinct >= m else 0

        # slide the window
        for i in range(k, n):
            # add new element
            add_val = nums[i]
            if cnt[add_val] == 0:
                distinct += 1
            cnt[add_val] += 1
            cur_sum += add_val

            # remove old element
            rem_val = nums[i - k]
            cnt[rem_val] -= 1
            cur_sum -= rem_val
            if cnt[rem_val] == 0:
                distinct -= 1
                del cnt[rem_val]

            if distinct >= m and cur_sum > ans:
                ans = cur_sum

        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

#define HASH_SIZE 32768               // power of two, > 2 * max numsSize
#define HASH_MASK (HASH_SIZE - 1)

static unsigned int hash_key(int key) {
    return ((unsigned int)key * 2654435761u) & HASH_MASK;
}

/* Hash map with open addressing and linear probing */
typedef struct {
    int   keys[HASH_SIZE];
    int   cnts[HASH_SIZE];
    char state[HASH_SIZE]; // 0 = empty, 1 = occupied, 2 = deleted
} IntHashMap;

static void hashmap_init(IntHashMap *hm) {
    for (int i = 0; i < HASH_SIZE; ++i) hm->state[i] = 0;
}

/* Insert one occurrence of key.
   Returns +1 if a new distinct element is added, otherwise 0. */
static int hashmap_add(IntHashMap *hm, int key) {
    unsigned int idx = hash_key(key);
    while (hm->state[idx] == 1 && hm->keys[idx] != key) {
        idx = (idx + 1) & HASH_MASK;
    }
    if (hm->state[idx] == 1) {               // already present
        hm->cnts[idx]++;
        return 0;
    } else {                                 // empty or deleted slot -> new distinct
        hm->state[idx] = 1;
        hm->keys[idx] = key;
        hm->cnts[idx] = 1;
        return 1;
    }
}

/* Remove one occurrence of key.
   Returns -1 if the element becomes absent (distinct count decreases), otherwise 0. */
static int hashmap_remove(IntHashMap *hm, int key) {
    unsigned int idx = hash_key(key);
    while (hm->state[idx] != 0 && (hm->state[idx] == 2 || hm->keys[idx] != key)) {
        idx = (idx + 1) & HASH_MASK;
    }
    // key must exist
    if (hm->state[idx] != 1) return 0; // safety, should not happen
    hm->cnts[idx]--;
    if (hm->cnts[idx] == 0) {
        hm->state[idx] = 2;   // mark as deleted
        return -1;
    }
    return 0;
}

long long maxSum(int* nums, int numsSize, int m, int k) {
    if (k > numsSize) return 0;
    IntHashMap hm;
    hashmap_init(&hm);
    long long curSum = 0;
    int distinct = 0;

    for (int i = 0; i < k; ++i) {
        curSum += nums[i];
        distinct += hashmap_add(&hm, nums[i]);
    }

    long long best = (distinct >= m) ? curSum : 0LL;

    for (int i = k; i < numsSize; ++i) {
        int outVal = nums[i - k];
        int inVal  = nums[i];

        curSum -= outVal;
        distinct += hashmap_remove(&hm, outVal);

        curSum += inVal;
        distinct += hashmap_add(&hm, inVal);

        if (distinct >= m && curSum > best) {
            best = curSum;
        }
    }

    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaxSum(IList<int> nums, int m, int k)
    {
        int n = nums.Count;
        var freq = new Dictionary<int, int>();
        long curSum = 0;
        int distinct = 0;

        // Initialize first window
        for (int i = 0; i < k; i++)
        {
            int val = nums[i];
            curSum += val;
            if (freq.TryGetValue(val, out int cnt))
            {
                freq[val] = cnt + 1;
            }
            else
            {
                freq[val] = 1;
                distinct++;
            }
        }

        long maxSum = distinct >= m ? curSum : 0;

        // Slide the window
        for (int i = k; i < n; i++)
        {
            int outVal = nums[i - k];
            int inVal = nums[i];

            // Remove outgoing element
            curSum -= outVal;
            int outCnt = freq[outVal];
            if (outCnt == 1)
            {
                freq.Remove(outVal);
                distinct--;
            }
            else
            {
                freq[outVal] = outCnt - 1;
            }

            // Add incoming element
            curSum += inVal;
            if (freq.TryGetValue(inVal, out int inCnt))
            {
                freq[inVal] = inCnt + 1;
            }
            else
            {
                freq[inVal] = 1;
                distinct++;
            }

            if (distinct >= m && curSum > maxSum)
            {
                maxSum = curSum;
            }
        }

        return maxSum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var maxSum = function(nums, m, k) {
    const n = nums.length;
    const freq = new Map();
    let distinct = 0;
    let curSum = 0;
    let ans = 0;

    for (let i = 0; i < n; ++i) {
        // add current element
        const valAdd = nums[i];
        curSum += valAdd;
        freq.set(valAdd, (freq.get(valAdd) || 0) + 1);
        if (freq.get(valAdd) === 1) distinct++;

        // remove element that slides out of the window
        if (i >= k) {
            const valRemove = nums[i - k];
            curSum -= valRemove;
            const cnt = freq.get(valRemove);
            if (cnt === 1) {
                freq.delete(valRemove);
                distinct--;
            } else {
                freq.set(valRemove, cnt - 1);
            }
        }

        // evaluate when window size is exactly k
        if (i >= k - 1) {
            if (distinct >= m && curSum > ans) {
                ans = curSum;
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxSum(nums: number[], m: number, k: number): number {
    const n = nums.length;
    if (k > n) return 0;

    const freq = new Map<number, number>();
    let distinct = 0;
    let sum = 0;
    let ans = 0;

    // Initialize first window
    for (let i = 0; i < k; i++) {
        const val = nums[i];
        sum += val;
        const cnt = freq.get(val) ?? 0;
        if (cnt === 0) distinct++;
        freq.set(val, cnt + 1);
    }
    if (distinct >= m) ans = Math.max(ans, sum);

    // Slide the window
    for (let i = k; i < n; i++) {
        const outVal = nums[i - k];
        const outCnt = freq.get(outVal)!;
        if (outCnt === 1) {
            freq.delete(outVal);
            distinct--;
        } else {
            freq.set(outVal, outCnt - 1);
        }
        sum -= outVal;

        const inVal = nums[i];
        const inCnt = freq.get(inVal) ?? 0;
        if (inCnt === 0) distinct++;
        freq.set(inVal, inCnt + 1);
        sum += inVal;

        if (distinct >= m && sum > ans) {
            ans = sum;
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
     * @param Integer $m
     * @param Integer $k
     * @return Integer
     */
    function maxSum($nums, $m, $k) {
        $n = count($nums);
        if ($k > $n) return 0;

        $freq = [];
        $distinct = 0;
        $sum = 0;
        $max = 0;

        // Initialize first window
        for ($i = 0; $i < $k; $i++) {
            $val = $nums[$i];
            $sum += $val;
            if (!isset($freq[$val])) {
                $freq[$val] = 1;
                $distinct++;
            } else {
                $freq[$val]++;
            }
        }

        if ($distinct >= $m) {
            $max = $sum;
        }

        // Slide the window
        for ($i = $k; $i < $n; $i++) {
            // Remove leftmost element
            $left = $nums[$i - $k];
            $sum -= $left;
            $freq[$left]--;
            if ($freq[$left] == 0) {
                unset($freq[$left]);
                $distinct--;
            }

            // Add new rightmost element
            $right = $nums[$i];
            $sum += $right;
            if (!isset($freq[$right])) {
                $freq[$right] = 1;
                $distinct++;
            } else {
                $freq[$right]++;
            }

            if ($distinct >= $m && $sum > $max) {
                $max = $sum;
            }
        }

        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ nums: [Int], _ m: Int, _ k: Int) -> Int {
        var freq = [Int: Int]()
        var distinctCount = 0
        var windowSum = 0
        var best = 0
        
        for i in 0..<nums.count {
            let val = nums[i]
            windowSum += val
            if let cnt = freq[val] {
                freq[val] = cnt + 1
            } else {
                freq[val] = 1
                distinctCount += 1
            }
            
            if i >= k {
                let leftVal = nums[i - k]
                windowSum -= leftVal
                if let cnt = freq[leftVal] {
                    if cnt == 1 {
                        freq.removeValue(forKey: leftVal)
                        distinctCount -= 1
                    } else {
                        freq[leftVal] = cnt - 1
                    }
                }
            }
            
            if i >= k - 1 && distinctCount >= m {
                if windowSum > best {
                    best = windowSum
                }
            }
        }
        
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSum(nums: List<Int>, m: Int, k: Int): Long {
        val n = nums.size
        if (k > n) return 0L
        val freq = HashMap<Int, Int>()
        var sum = 0L
        var distinct = 0
        var best = 0L

        for (i in 0 until n) {
            val add = nums[i]
            sum += add.toLong()
            val newCount = (freq[add] ?: 0) + 1
            freq[add] = newCount
            if (newCount == 1) distinct++

            if (i >= k) {
                val remove = nums[i - k]
                sum -= remove.toLong()
                val cnt = freq[remove]!! - 1
                if (cnt == 0) {
                    freq.remove(remove)
                    distinct--
                } else {
                    freq[remove] = cnt
                }
            }

            if (i >= k - 1 && distinct >= m) {
                if (sum > best) best = sum
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxSum(List<int> nums, int m, int k) {
    int n = nums.length;
    Map<int, int> freq = {};
    int distinct = 0;
    int sum = 0;
    int best = 0;

    for (int i = 0; i < n; i++) {
      int val = nums[i];
      sum += val;
      freq[val] = (freq[val] ?? 0) + 1;
      if (freq[val] == 1) distinct++;

      if (i >= k) {
        int leftVal = nums[i - k];
        sum -= leftVal;
        int cnt = freq[leftVal]!;
        if (cnt == 1) {
          freq.remove(leftVal);
          distinct--;
        } else {
          freq[leftVal] = cnt - 1;
        }
      }

      if (i >= k - 1 && distinct >= m) {
        if (sum > best) best = sum;
      }
    }

    return best;
  }
}
```

## Golang

```go
func maxSum(nums []int, m int, k int) int64 {
    freq := make(map[int]int)
    var curSum int64
    distinct := 0
    var ans int64

    for i, v := range nums {
        curSum += int64(v)
        if cnt := freq[v]; cnt == 0 {
            distinct++
        }
        freq[v]++

        if i >= k {
            out := nums[i-k]
            curSum -= int64(out)
            freq[out]--
            if freq[out] == 0 {
                distinct--
                delete(freq, out)
            }
        }

        if i >= k-1 && distinct >= m {
            if curSum > ans {
                ans = curSum
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_sum(nums, m, k)
  n = nums.length
  freq = Hash.new(0)
  sum = 0
  distinct = 0
  max_sum = 0

  (0...k).each do |i|
    val = nums[i]
    sum += val
    distinct += 1 if freq[val] == 0
    freq[val] += 1
  end

  max_sum = sum if distinct >= m

  (k...n).each do |i|
    left_val = nums[i - k]
    sum -= left_val
    freq[left_val] -= 1
    distinct -= 1 if freq[left_val] == 0

    val = nums[i]
    sum += val
    distinct += 1 if freq[val] == 0
    freq[val] += 1

    max_sum = [max_sum, sum].max if distinct >= m
  end

  max_sum
end
```

## Scala

```scala
object Solution {
    def maxSum(nums: List[Int], m: Int, k: Int): Long = {
        val n = nums.length
        if (k > n) return 0L
        val arr = nums.toArray
        import scala.collection.mutable

        val cnt = mutable.HashMap[Int, Int]()
        var sum: Long = 0L
        var maxSumRes: Long = 0L
        var left = 0

        for (right <- 0 until n) {
            val v = arr(right)
            sum += v.toLong
            cnt.put(v, cnt.getOrElse(v, 0) + 1)

            if (right - left + 1 > k) {
                val lv = arr(left)
                sum -= lv.toLong
                val c = cnt(lv) - 1
                if (c == 0) cnt.remove(lv) else cnt.update(lv, c)
                left += 1
            }

            if (right - left + 1 == k && cnt.size >= m) {
                if (sum > maxSumRes) maxSumRes = sum
            }
        }
        maxSumRes
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>, m: i32, k: i32) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let k_usize = k as usize;
        let m_usize = m as usize;
        use std::collections::HashMap;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut sum: i64 = 0;
        let mut distinct: usize = 0;
        let mut max_sum: i64 = 0;

        for i in 0..n {
            let val = nums[i];
            sum += val as i64;
            let entry = cnt.entry(val).or_insert(0);
            if *entry == 0 {
                distinct += 1;
            }
            *entry += 1;

            if i >= k_usize {
                let left_val = nums[i - k_usize];
                sum -= left_val as i64;
                if let Some(c) = cnt.get_mut(&left_val) {
                    *c -= 1;
                    if *c == 0 {
                        distinct -= 1;
                        cnt.remove(&left_val);
                    }
                }
            }

            if i + 1 >= k_usize && distinct >= m_usize {
                if sum > max_sum {
                    max_sum = sum;
                }
            }
        }

        max_sum
    }
}
```

## Racket

```racket
(define/contract (max-sum nums m k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((vec (list->vector nums))
         (n (vector-length vec))
         (counts (make-hash))
         (sum 0)
         (distinct 0)
         (ans 0))
    (for ([i (in-range n)])
      (define val (vector-ref vec i))
      ;; add new element
      (set! sum (+ sum val))
      (define prev (hash-ref counts val 0))
      (when (= prev 0) (set! distinct (+ distinct 1)))
      (hash-set! counts val (+ prev 1))
      ;; remove element if window exceeds size k
      (when (>= i k)
        (define out-val (vector-ref vec (- i k)))
        (define cnt (hash-ref counts out-val))
        (set! sum (- sum out-val))
        (if (= cnt 1)
            (begin
              (hash-remove! counts out-val)
              (set! distinct (- distinct 1)))
            (hash-set! counts out-val (- cnt 1))))
      ;; evaluate window of exact size k
      (when (>= i (- k 1))
        (when (>= distinct m)
          (set! ans (max ans sum)))))
    ans))
```

## Erlang

```erlang
-spec max_sum([integer()], integer(), integer()) -> integer().
max_sum(Nums, M, K) ->
    N = length(Nums),
    if
        N < K ->
            0;
        true ->
            T = list_to_tuple(Nums),
            {Sum0, Map0} = init_window(T, 1, K, 0, #{}),
            Max0 = case maps:size(Map0) >= M of
                       true -> Sum0;
                       false -> 0
                   end,
            slide(T, N, K, M, K + 1, Sum0, Map0, Max0)
    end.

init_window(_T, I, End, Sum, Map) when I > End ->
    {Sum, Map};
init_window(T, I, End, Sum, Map) ->
    Val = element(I, T),
    NewSum = Sum + Val,
    Count = maps:get(Val, Map, 0),
    NewMap = Map#{Val => Count + 1},
    init_window(T, I + 1, End, NewSum, NewMap).

slide(_T, _N, _K, _M, Index, _Sum, _Map, Max) when Index > _N ->
    Max;
slide(T, N, K, M, Index, Sum, Map, Max) ->
    AddVal = element(Index, T),
    RemoveIdx = Index - K,
    RemVal = element(RemoveIdx, T),

    NewSum = Sum - RemVal + AddVal,

    CountRem = maps:get(RemVal, Map),
    MapAfterRem = if
        CountRem == 1 -> maps:remove(RemVal, Map);
        true -> Map#{RemVal => CountRem - 1}
    end,
    CountAdd = maps:get(AddVal, MapAfterRem, 0),
    NewMap = MapAfterRem#{AddVal => CountAdd + 1},

    NewMax = case maps:size(NewMap) >= M of
        true -> erlang:max(NewSum, Max);
        false -> Max
    end,
    slide(T, N, K, M, Index + 1, NewSum, NewMap, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum(nums :: [integer], m :: integer, k :: integer) :: integer
  def max_sum(nums, m, k) do
    {_, _, best, _, _} =
      Enum.reduce(nums, {%{}, 0, 0, :queue.new(), 0}, fn val,
          {freq, sum, best, q, size} ->
        freq = Map.update(freq, val, 1, &(&1 + 1))
        sum = sum + val
        q = :queue.in(val, q)
        size = size + 1

        if size == k do
          distinct = map_size(freq)
          best = if distinct >= m and sum > best, do: sum, else: best

          {{:value, left}, q} = :queue.out(q)

          freq =
            case Map.get(freq, left) do
              1 -> Map.delete(freq, left)
              cnt -> Map.put(freq, left, cnt - 1)
            end

          sum = sum - left
          size = size - 1

          {freq, sum, best, q, size}
        else
          {freq, sum, best, q, size}
        end
      end)

    best
  end
end
```
