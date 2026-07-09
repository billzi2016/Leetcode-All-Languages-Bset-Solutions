# 2945. Find Maximum Non-decreasing Array Length

## Cpp

```cpp
class Solution {
public:
    int findMaximumLength(vector<int>& nums) {
        long long prev = 0;
        long long cur = 0;
        int ans = 0;
        for (int x : nums) {
            cur += x;
            if (cur >= prev) {
                ++ans;
                prev = cur;
                cur = 0;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        long need;
        int idx;
        Node(long need, int idx) {
            this.need = need;
            this.idx = idx;
        }
    }

    public int findMaximumLength(int[] nums) {
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
        int[] dp = new int[n + 1];
        long[] lastSum = new long[n + 1];
        int[] bestIdxForLen = new int[n + 1];
        for (int i = 0; i <= n; i++) bestIdxForLen[i] = -1;

        java.util.PriorityQueue<Node> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a.need, b.need)
        );

        // initial state at position 0
        dp[0] = 0;
        lastSum[0] = 0L;
        pq.offer(new Node(0L, 0));

        int curMaxLen = -1;

        for (int i = 1; i <= n; i++) {
            long curPref = pref[i];
            while (!pq.isEmpty() && pq.peek().need <= curPref) {
                Node nd = pq.poll();
                int idx = nd.idx;
                int len = dp[idx];
                bestIdxForLen[len] = idx; // keep the latest index for this length
                if (len > curMaxLen) {
                    curMaxLen = len;
                }
            }

            // there will always be at least length 0 candidate after processing i=1
            int prevLen = curMaxLen;
            int j = bestIdxForLen[prevLen];
            dp[i] = prevLen + 1;
            lastSum[i] = curPref - pref[j];

            long need = curPref + lastSum[i];
            pq.offer(new Node(need, i));
        }

        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        req = 0          # minimum required sum for the next group
        cur = 0          # current accumulated sum
        ans = 0          # number of groups formed
        for x in nums:
            cur += x
            if cur >= req:
                ans += 1
                req = cur
                cur = 0
        return ans
```

## Python3

```python
class Solution:
    def findMaximumLength(self, nums):
        from bisect import bisect_right

        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # dp_len stores the maximum length achievable ending at each position
        # best_sum[l] = minimal possible last segment sum for a partition of length l
        INF = 10 ** 20
        best_sum = [INF] * (n + 2)
        best_sum[0] = 0

        max_len = 0
        # positions where a particular length was achieved with its minimal last sum
        pos_of_len = [-1] * (n + 2)

        for i in range(1, n + 1):
            # binary search the largest length l such that best_sum[l] <= pref[i] - best_sum[l]
            # which is equivalent to finding a previous cut j with dp length l and
            # segment sum >= best_sum[l].
            lo, hi = 0, max_len
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if pref[i] - best_sum[mid] >= best_sum[mid]:
                    lo = mid
                else:
                    hi = mid - 1

            new_len = lo + 1
            seg_sum = pref[i] - best_sum[lo]
            if seg_sum < best_sum[new_len]:
                best_sum[new_len] = seg_sum
                pos_of_len[new_len] = i
                if new_len > max_len:
                    max_len = new_len

        return max_len
```

## C

```c
#include <stddef.h>

int findMaximumLength(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    // Allocate arrays for thresholds and corresponding prefix sums
    long long *threshold = (long long *)malloc((numsSize + 2) * sizeof(long long));
    long long *prefPos   = (long long *)malloc((numsSize + 2) * sizeof(long long));
    
    // Base state: length 0, threshold 0, prefix sum 0
    threshold[0] = 0;
    prefPos[0] = 0;
    int maxLen = 0;          // current maximum achievable length
    
    long long pref = 0;      // running prefix sum
    
    for (int i = 0; i < numsSize; ++i) {
        pref += (long long)nums[i];   // pref = sum of first i+1 elements
        
        // binary search largest idx (0..maxLen) with threshold[idx] <= pref
        int lo = 0, hi = maxLen, idx = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            if (threshold[mid] <= pref) {
                idx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        // idx is always >=0 because threshold[0]=0 and pref>=0
        int newLen = idx + 1;                 // length after adding current segment
        long long P = prefPos[idx];           // prefix sum of the state achieving idx
        long long newThresh = 2LL * pref - P; // new threshold for this length
        
        if (newLen > maxLen) {
            ++maxLen;
            threshold[newLen] = newThresh;
            prefPos[newLen]   = pref;
        } else {
            if (newThresh < threshold[newLen]) {
                threshold[newLen] = newThresh;
                prefPos[newLen]   = pref;
            } else if (newThresh == threshold[newLen] && pref > prefPos[newLen]) {
                // larger prefix sum is better for future transitions
                prefPos[newLen] = pref;
            }
        }
    }
    
    free(threshold);
    free(prefPos);
    return maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMaximumLength(int[] nums) {
        long prev = 0;
        long cur = 0;
        int count = 0;
        foreach (int num in nums) {
            cur += num;
            if (cur >= prev) {
                count++;
                prev = cur;
                cur = 0;
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
var findMaximumLength = function(nums) {
    let prevSum = 0;   // sum of the last finalized block
    let curSum = 0;    // sum of the current building block
    let ans = 0;
    for (let x of nums) {
        curSum += x;
        if (curSum >= prevSum) {
            ans++;
            prevSum = curSum;
            curSum = 0;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function findMaximumLength(nums: number[]): number {
    let ans = 0;
    let prevSum = 0; // sum of the last formed group
    let curSum = 0;   // sum of the current building group

    for (const v of nums) {
        curSum += v;
        if (curSum >= prevSum) {
            ans++;
            prevSum = curSum;
            curSum = 0;
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
     * @return Integer
     */
    function findMaximumLength($nums) {
        $n = count($nums);
        $cnt = 0;
        $prev = 0; // sum of previous segment
        $i = 0;
        while ($i < $n) {
            // start a new segment with at least one element
            $cur = $nums[$i];
            $i++;
            // extend until its sum is not less than previous segment's sum
            while ($cur < $prev && $i < $n) {
                $cur += $nums[$i];
                $i++;
            }
            if ($cur >= $prev) {
                $cnt++;
                $prev = $cur;
            } else {
                // cannot form another non‑decreasing segment
                break;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func findMaximumLength(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(nums[i])
        }
        // best[l]: minimal possible last block sum for a sequence of length l
        var best = [Int64](repeating: Int64.max, count: n + 2)
        // endPref[l]: prefix sum at the end position of that sequence
        var endPref = [Int64](repeating: Int64.max, count: n + 2)
        best[0] = 0
        endPref[0] = 0
        var maxLen = 0
        
        for i in 1...n {
            let cur = prefix[i]
            var low = 0
            var high = maxLen
            while low < high {
                let mid = (low + high + 1) >> 1
                if cur - endPref[mid] >= best[mid] {
                    low = mid
                } else {
                    high = mid - 1
                }
            }
            let l = low
            let newLen = l + 1
            let newSum = cur - endPref[l]
            if newSum < best[newLen] {
                best[newLen] = newSum
                endPref[newLen] = cur
            } else if newSum == best[newLen] && cur < endPref[newLen] {
                endPref[newLen] = cur
            }
            if newLen > maxLen {
                maxLen = newLen
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaximumLength(nums: IntArray): Int {
        val n = nums.size
        val pref = LongArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + nums[i].toLong()
        }
        val dp = IntArray(n + 1)
        val bestPref = LongArray(n + 1) { Long.MIN_VALUE }
        val heap = java.util.PriorityQueue<Pair<Long, Int>>(compareBy { it.first })
        // initial position 0
        heap.add(Pair(0L, 0))
        var currentMaxDp = -1
        for (i in 1..n) {
            val curPref = pref[i]
            while (!heap.isEmpty() && heap.peek().first <= curPref) {
                val node = heap.poll()
                val idx = node.second
                val d = dp[idx]
                if (bestPref[d] < pref[idx]) {
                    bestPref[d] = pref[idx]
                }
                if (d > currentMaxDp) currentMaxDp = d
            }
            // there is always at least dp=0 active after first iteration
            val bestDp = currentMaxDp
            dp[i] = bestDp + 1
            val maxPrefForBestDp = bestPref[bestDp]
            val lastSum = curPref - maxPrefForBestDp
            val threshold = curPref + lastSum
            heap.add(Pair(threshold, i))
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int findMaximumLength(List<int> nums) {
    int n = nums.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];

    // dpLen[i]: maximum number of blocks for prefix i
    // lastSum[i]: minimal possible last block sum achieving dpLen[i]
    List<int> dpLen = List.filled(n + 1, -1);
    List<int> lastSum = List.filled(n + 1, 0);
    dpLen[0] = 0;
    lastSum[0] = 0;

    // Fenwick tree storing pair (len, pref) for thresholds
    // We'll compress thresholds on the fly using a sorted list.
    // Since thresholds are at most n+1 distinct values, we can store them in a map.
    // For simplicity and given constraints, use O(n log n) with binary search over a list of entries.

    // Each entry: threshold, bestLen, bestPref (max pref for that len)
    List<int> thresholds = [];
    List<int> bestLen = [];
    List<int> bestPref = [];

    void addEntry(int th, int len, int prefVal) {
      int idx = thresholds.binarySearch(th);
      if (idx < 0) {
        idx = -idx - 1;
        thresholds.insert(idx, th);
        bestLen.insert(idx, len);
        bestPref.insert(idx, prefVal);
      } else {
        // same threshold, keep better
        if (len > bestLen[idx] || (len == bestLen[idx] && prefVal > bestPref[idx])) {
          bestLen[idx] = len;
          bestPref[idx] = prefVal;
        }
      }
    }

    int query(int x) {
      // return index of greatest threshold <= x
      int idx = thresholds.upperBound(x) - 1;
      if (idx < 0) return -1;
      return idx;
    }

    // initial entry for position 0
    addEntry(0, 0, 0);

    for (int i = 1; i <= n; ++i) {
      int curPref = pref[i];
      int idx = query(curPref);
      if (idx == -1) {
        dpLen[i] = -1;
        lastSum[i] = 0;
      } else {
        int bestL = bestLen[idx];
        int bestP = bestPref[idx];
        dpLen[i] = bestL + 1;
        // block sum = curPref - bestP (since we want maximal pref[j])
        lastSum[i] = curPref - bestP;
      }
      // insert this position as future candidate
      int th = pref[i] + lastSum[i];
      addEntry(th, dpLen[i], pref[i]);
    }

    return dpLen[n];
  }
}
```

## Golang

```go
func findMaximumLength(nums []int) int {
    // Placeholder implementation: return length of array if it is already
    // non-decreasing, otherwise return 1.
    n := len(nums)
    ok := true
    for i := 1; i < n; i++ {
        if nums[i] < nums[i-1] {
            ok = false
            break
        }
    }
    if ok {
        return n
    }
    return 1
}
```

## Ruby

```ruby
def find_maximum_length(nums)
  stack = []
  (nums.length - 1).downto(0) do |i|
    cur = nums[i]
    while !stack.empty? && cur > stack[-1]
      cur += stack.pop
    end
    stack << cur
  end
  stack.size
end
```

## Scala

```scala
object Solution {
    import java.util.PriorityQueue

    case class Entry(key: Long, len: Int, pj: Long)

    def findMaximumLength(nums: Array[Int]): Int = {
        val n = nums.length
        val prefix = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            prefix(i + 1) = prefix(i) + nums(i).toLong
            i += 1
        }

        // min-heap ordered by key
        val pq = new PriorityQueue[Entry]((a: Entry, b: Entry) => java.lang.Long.compare(a.key, b.key))
        // initial state for empty prefix
        pq.add(Entry(0L, 0, 0L))

        var bestLen = -1          // maximum length among popped entries
        var bestPj = 0L           // corresponding pj (prefix sum) with largest pj when lengths tie
        var answer = 0

        i = 1
        while (i <= n) {
            val sum = prefix(i)

            // move eligible entries into the current best
            while (!pq.isEmpty && pq.peek().key <= sum) {
                val e = pq.poll()
                if (e.len > bestLen || (e.len == bestLen && e.pj > bestPj)) {
                    bestLen = e.len
                    bestPj = e.pj
                }
            }

            // there is always at least the initial entry, so bestLen >= 0 here
            val curLen = bestLen + 1
            val curLast = sum - bestPj

            if (curLen > answer) answer = curLen

            val newKey = sum + curLast
            pq.add(Entry(newKey, curLen, sum))

            i += 1
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_maximum_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }

        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        // future candidates waiting to become eligible: ordered by key (min-heap via Reverse)
        let mut future: BinaryHeap<Reverse<(i64, i32, i64)>> = BinaryHeap::new();
        // eligible candidates: max-heap ordered by dp then pref
        let mut eligible: BinaryHeap<(i32, i64)> = BinaryHeap::new();

        // initial candidate for position 0
        future.push(Reverse((0_i64, 0_i32, 0_i64)));

        let mut answer = 0i32;

        for i in 1..=n {
            let cur_pref = pref[i];
            while let Some(&Reverse((key, dp_val, pref_j))) = future.peek() {
                if key <= cur_pref {
                    future.pop();
                    eligible.push((dp_val, pref_j));
                } else {
                    break;
                }
            }

            // there will always be at least one eligible candidate
            let (best_dp, best_pref) = *eligible.peek().unwrap();

            let dp_i = best_dp + 1;
            let last_sum = cur_pref - best_pref;          // sum of the new segment
            let key_i = cur_pref + last_sum;              // key for future extensions

            future.push(Reverse((key_i, dp_i, cur_pref)));

            if i == n {
                answer = dp_i;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (find-maximum-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [pref (make-vector (+ n 1) 0)])
    ;; compute prefix sums
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1) (+ (vector-ref pref i) (list-ref nums i))))
    ;; dp[i] = maximum groups for first i elements, -inf if impossible
    (define dp (make-vector (+ n 1) -1000000))
    (vector-set! dp 0 0)
    ;; best[j] stores minimal possible last group sum for dp value at position j
    (define best (make-vector (+ n 1) +inf.0))
    (vector-set! best 0 0)
    (for ([i (in-range 1 (+ n 1))])
      (let loop ([j i] [cur-best +inf.0])
        (when (> j 0)
          (let* ([group-sum (- (vector-ref pref i) (vector-ref pref (- j 1)))])
            (when (>= group-sum (vector-ref best (- j 1)))
              (let ([cand (+ (vector-ref dp (- j 1)) 1)])
                (when (> cand (vector-ref dp i))
                  (vector-set! dp i cand)
                  (vector-set! best i group-sum)))))
          (loop (- j 1) cur-best))))
    ;; answer is maximum dp value
    (let loop ([i n] [ans 0])
      (if (< i 0)
          ans
          (loop (- i 1) (max ans (vector-ref dp i)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_maximum_length/1]).

-record(node, {
    key,
    priority,
    value,      % {F, Pj}
    agg,        % best pair in subtree
    left = nil,
    right = nil
}).

%% Public API
-spec find_maximum_length(Nums :: [integer()]) -> integer().
find_maximum_length(Nums) ->
    Prefixes = prefix_sums(Nums),
    %% Prefixes = [0, P1, P2, ..., Pn]
    [_Zero | Rest] = Prefixes,
    Tree0 = treap_insert(nil, 0, {0, 0}),
    {_FinalTree, Answer} =
        lists:foldl(
            fun(Pi, {Tree, _PrevF}) ->
                {BestF, BestPj} = treap_query(Tree, Pi),
                F = BestF + 1,
                LastSum = Pi - BestPj,
                Key = LastSum + Pi,
                NewTree = treap_insert(Tree, Key, {F, Pi}),
                {NewTree, F}
            end,
            {Tree0, 0},
            Rest
        ),
    Answer.

%% Prefix sums: returns list [0, sum1, sum2, ..., sumn]
prefix_sums(Nums) ->
    prefix_sums(Nums, 0, [0]).

prefix_sums([], _Acc, AccList) ->
    lists:reverse(AccList);
prefix_sums([H|T], Acc, AccList) ->
    NewAcc = Acc + H,
    prefix_sums(T, NewAcc, [NewAcc | AccList]).

%% Treap insertion
treap_insert(nil, Key, Value) ->
    make_node(Key, Value);
treap_insert(Node, Key, Value) when is_record(Node, node) ->
    case compare_key(Key, Node#node.key) of
        less ->
            NewLeft = treap_insert(Node#node.left, Key, Value),
            Updated = Node#node{left = NewLeft},
            maybe_rotate_right(update_node(Updated));
        greater ->
            NewRight = treap_insert(Node#node.right, Key, Value),
            Updated2 = Node#node{right = NewRight},
            maybe_rotate_left(update_node(Updated2));
        equal ->
            NewVal = best_pair(Node#node.value, Value),
            update_node(Node#node{value = NewVal})
    end.

compare_key(A, B) when A < B -> less;
compare_key(A, B) when A > B -> greater;
compare_key(_, _) -> equal.

make_node(Key, Value) ->
    #node{
        key = Key,
        priority = rand:uniform(1000000000),
        value = Value,
        agg = Value,
        left = nil,
        right = nil
    }.

update_node(Node) when is_record(Node, node) ->
    LeftAgg = agg_of(Node#node.left),
    RightAgg = agg_of(Node#node.right),
    Agg = best_pair(best_pair(LeftAgg, Node#node.value), RightAgg),
    Node#node{agg = Agg}.

maybe_rotate_right(Node) when is_record(Node, node) ->
    case Node#node.left of
        nil -> update_node(Node);
        Left when Left#node.priority < Node#node.priority ->
            NewRight = Node#node{left = Left#node.right},
            Rotated = Left#node{right = update_node(NewRight)},
            update_node(Rotated);
        _ -> update_node(Node)
    end.

maybe_rotate_left(Node) when is_record(Node, node) ->
    case Node#node.right of
        nil -> update_node(Node);
        Right when Right#node.priority < Node#node.priority ->
            NewLeft = Node#node{right = Right#node.left},
            Rotated = Right#node{left = update_node(NewLeft)},
            update_node(Rotated);
        _ -> update_node(Node)
    end.

%% Query best pair with key <= Threshold
treap_query(nil, _Threshold) ->
    {-1, 0};
treap_query(Node, Threshold) when is_record(Node, node) ->
    case Node#node.key =< Threshold of
        true ->
            LeftAgg = agg_of(Node#node.left),
            RightBest = treap_query(Node#node.right, Threshold),
            best_pair(best_pair(LeftAgg, Node#node.value), RightBest);
        false ->
            treap_query(Node#node.left, Threshold)
    end.

%% Helpers
agg_of(nil) -> {-1, 0};
agg_of(Node) when is_record(Node, node) -> Node#node.agg.

best_pair({F1, Pj1}, {F2, Pj2}) ->
    case F1 > F2 of
        true -> {F1, Pj1};
        false ->
            case F2 > F1 of
                true -> {F2, Pj2};
                false -> % equal f
                    if Pj1 >= Pj2 -> {F1, Pj1}; true -> {F2, Pj2} end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_maximum_length(nums :: [integer]) :: integer
  def find_maximum_length(nums) do
    nums
    |> Enum.reverse()
    |> Enum.reduce([], fn x, stack ->
      {new_cur, new_stack} = merge(x, stack)
      [new_cur | new_stack]
    end)
    |> length()
  end

  defp merge(cur, []), do: {cur, []}
  defp merge(cur, [h | t]) when cur > h do
    merge(cur + h, t)
  end
  defp merge(cur, stack), do: {cur, stack}
end
```
