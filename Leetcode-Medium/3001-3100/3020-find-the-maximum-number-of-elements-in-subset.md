# 3020. Find the Maximum Number of Elements in Subset

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumLength(vector<int>& nums) {
        unordered_map<long long,int> cnt;
        for (int v: nums) ++cnt[v];
        int ans = 1; // at least one element can be taken
        if (cnt.count(1)) {
            int c = cnt[1];
            int odd = (c % 2 ? c : max(c - 1, 0));
            ans = max(ans, odd);
        }
        for (auto &p: cnt) {
            long long x = p.first;
            if (x <= 1) continue;
            if (p.second >= 2 && cnt.count(x * x) && cnt[x * x] > 0) {
                ans = max(ans, 3);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumLength(int[] nums) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int v : nums) {
            freq.put(v, freq.getOrDefault(v, 0) + 1);
        }
        int best = 0;
        // handle value 1 separately
        int cntOne = freq.getOrDefault(1, 0);
        if (cntOne > 0) {
            int adj = (cntOne % 2 == 1) ? cntOne : cntOne - 1;
            best = Math.max(best, adj);
        }
        java.util.HashSet<Integer> visited = new java.util.HashSet<>();
        for (int val : freq.keySet()) {
            if (val == 1) continue;
            // skip if already processed in a chain
            if (visited.contains(val)) continue;
            // check if it has an integer square root present; if so, it's not the smallest of its chain
            int sqrt = (int) Math.sqrt(val);
            if ((long) sqrt * sqrt == val && freq.containsKey(sqrt)) {
                continue;
            }
            // build the chain starting from val
            java.util.ArrayList<Integer> counts = new java.util.ArrayList<>();
            long cur = val;
            while (cur <= 1_000_000_000L && freq.containsKey((int) cur)) {
                int c = freq.get((int) cur);
                counts.add(c);
                visited.add((int) cur);
                // next power by squaring
                if (cur > Math.sqrt(Long.MAX_VALUE)) break; // avoid overflow
                cur = cur * cur;
            }
            int k = counts.size();
            if (k == 0) continue;
            int length;
            if (k == 1) {
                // only one distinct value (>1), can take at most one element
                length = Math.min(counts.get(0), 1);
            } else {
                int[] cArr = new int[k];
                for (int i = 0; i < k; i++) cArr[i] = counts.get(i);
                boolean changed = true;
                while (changed) {
                    changed = false;
                    for (int i = 0; i < k; i++) {
                        int limit;
                        if (i == 0) {
                            limit = cArr[1] + 1;
                        } else if (i == k - 1) {
                            limit = cArr[k - 2] + 1;
                        } else {
                            limit = cArr[i - 1] + cArr[i + 1];
                        }
                        if (cArr[i] > limit) {
                            cArr[i] = limit;
                            changed = true;
                        }
                    }
                }
                int sum = 0;
                for (int v : cArr) sum += v;
                length = sum;
            }
            // adjust to odd size
            if (length % 2 == 0) length--;
            if (length > best) best = length;
        }
        // ensure at least one element can be chosen
        return Math.max(best, 1);
    }
}
```

## Python

```python
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(nums)
        num_set = set(cnt.keys())
        ans = 0

        # handle ones separately
        if 1 in cnt:
            c1 = cnt[1]
            ans = max(ans, c1 if c1 % 2 == 1 else c1 - 1)

        for x in cnt:
            if x <= 1:
                continue
            cur = x
            length = 0
            while cur in num_set:
                length += 1
                # prevent overflow and stop when next square exceeds limit
                if cur > 10**9 // cur:
                    break
                cur = cur * cur

            cand = length
            if length >= 2 and cnt[x] >= 2:
                cand += 1
            ans = max(ans, cand)

        return ans
```

## Python3

```python
class Solution:
    def maximumLength(self, nums):
        from collections import Counter
        cnt = Counter(nums)
        ans = 0

        # handle value 1 (must take an odd count)
        if 1 in cnt:
            ones = cnt[1]
            ans = ones if ones % 2 == 1 else ones - 1

        # precompute set for fast lookup
        present = set(cnt.keys())

        import math
        LIMIT = 10 ** 9

        for x in list(present):
            if x == 1:
                continue
            # consider only the smallest element of each component
            r = int(math.isqrt(x))
            if r * r == x and r in present:
                continue

            total = 0
            cur = x
            while True:
                total += cnt[cur]
                nxt = cur * cur
                if nxt > LIMIT or nxt not in present:
                    break
                cur = nxt

            # subset size must be odd
            if total % 2 == 0:
                total -= 1
            if total > ans:
                ans = total

        return ans
```

## C

```c
#include <stddef.h>
#include <stdlib.h>

int maximumLength(int* nums, int numsSize) {
    // Build frequency map
    struct Node { int key; int val; struct Node *next; };
    #define MOD 1000033
    static struct Node *table[MOD];
    for (int i = 0; i < numsSize; ++i) {
        int k = ((unsigned)nums[i]) % MOD;
        struct Node *p = table[k];
        while (p && p->key != nums[i]) p = p->next;
        if (p) p->val++;
        else {
            struct Node *n = (struct Node*)malloc(sizeof(struct Node));
            n->key = nums[i];
            n->val = 1;
            n->next = table[k];
            table[k] = n;
        }
    }

    // helper to get count
    auto getCount = [&](int x) -> int {
        int k = ((unsigned)x) % MOD;
        struct Node *p = table[k];
        while (p && p->key != x) p = p->next;
        return p ? p->val : 0;
    };

    int ans = 0;

    // handle ones: can take the largest odd count of 1s
    int cntOnes = getCount(1);
    if (cntOnes > 0) {
        int use = (cntOnes % 2 == 1) ? cntOnes : cntOnes - 1;
        if (use > ans) ans = use;
    }

    // iterate over distinct keys
    for (int i = 0; i < MOD; ++i) {
        struct Node *p = table[i];
        while (p) {
            int v = p->key;
            if (v != 1) {
                long long cur = v;
                int len = 0;
                while (cur <= 1000000000LL && getCount((int)cur) > 0) {
                    ++len;
                    if (cur > 1000000000LL / cur) break; // prevent overflow
                    cur = cur * cur;
                }
                int extra = 0;
                long long sq = (long long)v * v;
                if (p->val >= 2 && sq <= 1000000000LL && getCount((int)sq) > 0)
                    extra = 1;
                int total = len + extra;
                if (total > ans) ans = total;
            }
            p = p->next;
        }
    }

    // free hash table
    for (int i = 0; i < MOD; ++i) {
        struct Node *p = table[i];
        while (p) {
            struct Node *tmp = p;
            p = p->next;
            free(tmp);
        }
        table[i] = NULL;
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumLength(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var v in nums) {
            if (freq.ContainsKey(v)) freq[v]++; else freq[v] = 1;
        }

        int ans = 0;
        // handle ones: we can take an odd number of them
        if (freq.TryGetValue(1, out int cntOnes)) {
            ans = cntOnes % 2 == 1 ? cntOnes : cntOnes - 1;
        }

        var values = new List<int>(freq.Keys);
        foreach (int x in values) {
            if (x == 1) continue;
            long cur = x;
            int length = freq[x];
            while (true) {
                long nxt = cur * cur;
                if (nxt > 1000000000L) break;
                if (!freq.TryGetValue((int)nxt, out int cnt)) break;
                length += cnt;
                cur = nxt;
            }
            if (length > ans) ans = length;
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
var maximumLength = function(nums) {
    const freq = new Map();
    for (const v of nums) {
        freq.set(v, (freq.get(v) || 0) + 1);
    }
    const present = new Set(freq.keys());
    let ans = 0;
    
    // handle value 1: can take any odd count
    const ones = freq.get(1) || 0;
    if (ones > 0) {
        ans = ones % 2 === 1 ? ones : ones - 1;
    }
    
    for (const [x, cnt] of freq.entries()) {
        if (x === 1) continue;          // already processed
        if (cnt < 2) continue;           // need at least two copies of the smallest value
        
        let cur = x;
        let distinct = 0;
        while (present.has(cur)) {
            distinct++;
            // avoid overflow: stop if next square exceeds limit
            if (cur > 1e9 / cur) break;
            const nxt = cur * cur;
            if (!present.has(nxt)) break;
            cur = nxt;
        }
        if (distinct > 0) {
            const candidate = 2 * distinct - 1; // symmetric sequence length
            if (candidate > ans) ans = candidate;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function maximumLength(nums: number[]): number {
    const cnt = new Map<number, number>();
    for (const v of nums) {
        cnt.set(v, (cnt.get(v) ?? 0) + 1);
    }

    let ans = 1;

    // handle value 1 separately (need odd count)
    if (cnt.has(1)) {
        const c1 = cnt.get(1)!;
        const oddC1 = c1 % 2 === 1 ? c1 : c1 - 1;
        ans = Math.max(ans, oddC1);
    }

    // maximum value in nums is 1e9, sqrt(1e9) ≈ 31623
    const LIMIT = 31623;

    for (const [x, cx] of cnt.entries()) {
        if (x === 1 || x > LIMIT) continue;
        const y = x * x; // y <= 1e9 because x <= LIMIT
        const cy = cnt.get(y);
        if (!cy) continue;

        const minCnt = Math.min(cx, cy);
        let cand: number;
        if (cx === cy) {
            // need odd length, drop one element
            cand = 2 * minCnt - 1;
        } else {
            // extra of the more frequent value gives odd length
            cand = 2 * minCnt + 1;
        }
        ans = Math.max(ans, cand);
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
    function maximumLength($nums) {
        $freq = [];
        foreach ($nums as $v) {
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
        }

        $ans = 0;

        // handle value 1 (any odd count)
        if (isset($freq[1])) {
            $cnt1 = $freq[1];
            if ($cnt1 % 2 == 0) $cnt1--;   // make it odd
            $ans = max($ans, $cnt1);
        }

        // prepare a set for fast existence check
        $present = [];
        foreach ($freq as $k => $_) {
            $present[$k] = true;
        }

        foreach ($freq as $x => $_) {
            if ($x == 1) continue;

            // consider only the smallest element of each chain
            $root = (int)sqrt($x);
            if ($root * $root == $x && isset($present[$root])) {
                continue;
            }

            // build the power chain x, x^2, x^4, ...
            $powers = [];
            $cur = $x;
            while (isset($present[$cur])) {
                $powers[] = $cur;
                if ($cur > 1000000000 / $cur) break;   // avoid overflow
                $next = $cur * $cur;
                if ($next > 1000000000) break;
                $cur = $next;
            }

            // longest odd-length palindrome we can form from this chain
            $maxLen = 1; // at least the middle element alone
            for ($t = 1; $t < count($powers); $t++) {
                // need two copies of the previous (outer) value to place on both sides
                if ($freq[$powers[$t - 1]] >= 2) {
                    $candidate = 2 * $t + 1;
                    if ($candidate > $maxLen) $maxLen = $candidate;
                } else {
                    break; // cannot extend further
                }
            }

            if ($maxLen > $ans) $ans = $maxLen;
        }

        // fallback: at least one element can always be taken
        if ($ans == 0 && count($nums) > 0) $ans = 1;

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int]) -> Int {
        var freq = [Int:Int]()
        for v in nums {
            freq[v, default: 0] += 1
        }
        var ans = 0
        
        if let cnt1 = freq[1] {
            let use = (cnt1 % 2 == 1) ? cnt1 : cnt1 - 1
            ans = max(ans, use)
        }
        
        for (x, _) in freq {
            if x == 1 { continue }
            // check if x is a perfect square of another number present
            let r = Int(Double(x).squareRoot())
            if r * r == x && freq[r] != nil {
                continue   // not the smallest element of its chain
            }
            
            var counts = [Int]()
            var val = x
            while true {
                guard let c = freq[val] else { break }
                counts.append(c)
                // prevent overflow when squaring
                if val > 1_000_000_000 / val { break }
                let next = val * val
                if next == val { break }
                val = next
            }
            
            if counts.isEmpty { continue }
            if counts.count == 1 {
                ans = max(ans, 1)
            } else {
                let leftDef = max(0, counts[0] - (counts[1] + 1))
                let rightDef = max(0, counts[counts.count - 1] - (counts[counts.count - 2] + 1))
                let total = counts.reduce(0, +) - leftDef - rightDef
                ans = max(ans, total)
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (v in nums) {
            freq[v] = (freq[v] ?: 0) + 1
        }
        var ans = 0
        // handle value 1 (odd count can be taken)
        val cntOne = freq[1] ?: 0
        if (cntOne > 0) {
            ans = if (cntOne % 2 == 1) cntOne else cntOne - 1
        }
        for ((x, cx) in freq) {
            if (x == 1) continue
            val sqLong = x.toLong() * x
            if (sqLong <= Int.MAX_VALUE) {
                val csq = freq[sqLong.toInt()] ?: 0
                ans = maxOf(ans, cx + csq)
            }
        }
        // at least one element can always be chosen
        if (ans == 0 && nums.isNotEmpty()) ans = 1
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumLength(List<int> nums) {
    Map<int, int> freq = {};
    for (var v in nums) {
      freq[v] = (freq[v] ?? 0) + 1;
    }

    int ans = 0;

    // handle ones: we can take the largest odd count of 1's
    int cntOne = freq[1] ?? 0;
    if (cntOne > 0) {
      int cand = (cntOne % 2 == 1) ? cntOne : cntOne - 1;
      ans = cand;
    }

    // handle other numbers where we have at least two copies of the smallest value
    const int LIMIT = 1000000000;
    for (var entry in freq.entries) {
      int x = entry.key;
      int countX = entry.value;
      if (x == 1 || countX < 2) continue;

      int len = countX; // we can use all copies of the smallest value
      int cur = x;
      while (true) {
        if (cur > LIMIT ~/ cur) break; // avoid overflow
        int nxt = cur * cur;
        if (!freq.containsKey(nxt)) break;
        len += 1; // only one copy of each higher power is usable
        cur = nxt;
      }
      if (len > ans) ans = len;
    }

    // If we couldn't form any subset larger than 0, pick a single element
    if (ans == 0) ans = 1;

    return ans;
  }
}
```

## Golang

```go
func maximumLength(nums []int) int {
    freq := make(map[int]int)
    for _, v := range nums {
        freq[v]++
    }

    ans := 0
    // handle value 1: we can only take an odd count of them
    if c, ok := freq[1]; ok {
        if c%2 == 1 {
            ans = c
        } else if c > 0 {
            ans = c - 1
        }
    }

    const limit int64 = 1_000_000_000

    for x := range freq {
        if x == 1 {
            continue
        }
        total := 0
        cur := int64(x)
        for {
            cnt, ok := freq[int(cur)]
            if !ok {
                break
            }
            total += cnt
            // compute next square, stop if overflow or exceeds limit
            if cur > limit/cur { // would exceed limit
                break
            }
            nxt := cur * cur
            if nxt == cur { // should not happen for x>1, but guard
                break
            }
            cur = nxt
        }
        if total%2 == 0 && total > 0 {
            total--
        }
        if total > ans {
            ans = total
        }
    }

    return ans
}
```

## Ruby

```ruby
def maximum_length(nums)
  freq = Hash.new(0)
  nums.each { |v| freq[v] += 1 }

  ans = 1

  if freq.key?(1)
    ones = freq[1]
    ans = [ans, (ones.odd? ? ones : ones - 1)].max
  end

  freq.each_key do |x|
    next if x == 1
    y = x * x
    next unless freq.key?(y)

    a = freq[x]
    b = freq[y]
    cur = [a, b].min * 2 + (a > b ? 1 : 0)
    ans = cur if cur > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int]): Int = {
        import scala.collection.mutable

        val freq = mutable.Map[Int, Int]()
        for (v <- nums) {
            freq(v) = freq.getOrElse(v, 0) + 1
        }

        var ans = 0

        // handle value 1
        freq.get(1).foreach { c =>
            val cand = if ((c & 1) == 1) c else c - 1
            ans = math.max(ans, cand)
        }

        // handle pairs x and x^2
        for ((x, cntX) <- freq if x > 1) {
            val yLong = x.toLong * x
            if (yLong <= 1000000000L) {
                val y = yLong.toInt
                freq.get(y).foreach { cntY =>
                    var len = 2 * math.min(cntX, cntY)
                    if (cntX > cntY) len += 1
                    ans = math.max(ans, len)
                }
            }
        }

        // at least one element can always be taken
        if (ans == 0 && nums.nonEmpty) ans = 1
        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut cnt: HashMap<i64, i32> = HashMap::new();
        for &num in &nums {
            *cnt.entry(num as i64).or_insert(0) += 1;
        }

        // handle value 1 (must take an odd number of them)
        let mut ans = 0;
        if let Some(&c1) = cnt.get(&1) {
            let mut use_one = c1;
            if use_one % 2 == 0 && use_one > 0 {
                use_one -= 1;
            }
            ans = ans.max(use_one);
        }

        // consider pairs (x, x^2) for x > 1
        for (&x, &cx) in cnt.iter() {
            if x <= 1 { continue; }
            let sq = x * x;
            if let Some(&csq) = cnt.get(&sq) {
                let mut cand = cx + csq;
                if cand % 2 == 0 && cand > 0 {
                    cand -= 1;
                }
                ans = ans.max(cand);
            }
        }

        // at least one element can always be taken
        if ans == 0 { ans = 1; }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((freq (make-hash))
         (add-count (lambda (x) (hash-update! freq x add1 0))))
    (for-each add-count nums)
    (define cnt1 (hash-ref freq 1 0))
    (define ans
      (if (> cnt1 0)
          (if (odd? cnt1) cnt1 (- cnt1 1))
          0))
    (hash-for-each
     freq
     (lambda (k v)
       (when (> k 1)
         (let* ((sq (* k k))
                (cnt-sq (hash-ref freq sq 0)))
           (when (> cnt-sq 0)
             (define common (min v cnt-sq))
             (define extra (if (> v cnt-sq) 1 0))
             (define len (+ (* 2 common) extra))
             (set! ans (max ans len)))))))
    (max ans 1)))
```

## Erlang

```erlang
-spec maximum_length(Nums :: [integer()]) -> integer().
maximum_length(Nums) ->
    % Count occurrences of each number
    Counts = maps:from_list(
        lists:foldl(fun(N, Acc) ->
            case maps:is_key(N, Acc) of
                true -> maps:update(N, fun(C) -> C + 1 end, Acc);
                false -> maps:put(N, 1, Acc)
            end
        end, #{}, Nums)),
    % Number of ones
    OneCnt = maps:get(1, Counts, 0),
    % Start with the best answer using only ones (must be odd)
    BestOneAns = case OneCnt rem 2 of
        0 -> max(OneCnt - 1, 0);
        _ -> OneCnt
    end,
    % Evaluate chains starting from each x > 1
    Keys = maps:keys(Counts),
    ChainBest = lists:foldl(fun(X, Best) when X =< 1 -> Best;
                              (X, Best) ->
        case maps:get(X, Counts) of
            Cx when Cx >= 2 ->
                % we have at least two copies of the smallest element,
                % try to extend the chain by squaring repeatedly
                Len = explore_chain(X, Counts, 0),
                max(Best, Len);
            _ -> Best
        end
    end, 0, Keys),
    MaxAns = max(BestOneAns, ChainBest),
    case MaxAns of
        0 -> 1; % at least one element can always be chosen
        _ -> MaxAns
    end.

explore_chain(X, Counts, Acc) ->
    case maps:get(X, Counts, 0) of
        Cx when Cx >= 2 ->
            Next = X * X,
            explore_chain(Next, Counts, Acc + Cx);
        _ -> Acc
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer]) :: integer
  def maximum_length(nums) do
    cnt = Enum.reduce(nums, %{}, fn v, acc -> Map.update(acc, v, 1, &(&1 + 1)) end)
    set = MapSet.new(Map.keys(cnt))

    # candidate using only 1's (must be odd count if any)
    ans =
      case Map.get(cnt, 1, 0) do
        c when c > 0 ->
          if rem(c, 2) == 0, do: c - 1, else: c

        _ -> 0
      end

    # evaluate chains starting from each x > 1
    ans =
      Enum.reduce(Map.keys(cnt), ans, fn x, cur_max ->
        if x > 1 do
          length = chain_length(x, set)
          max(cur_max, length)
        else
          cur_max
        end
      end)

    ans
  end

  defp chain_length(start, set) do
    Stream.unfold({start, 0}, fn {v, _} ->
      if MapSet.member?(set, v) do
        nxt = v * v
        {{v, nxt}, {nxt, 0}}
      else
        nil
      end
    end)
    |> Enum.count()
  end
end
```
