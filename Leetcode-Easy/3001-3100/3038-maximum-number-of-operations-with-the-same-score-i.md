# 3038. Maximum Number of Operations With the Same Score I

## Cpp

```cpp
class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int best = 0;
        for (int target = 2; target <= 2000; ++target) {
            vector<int> stk;
            int ops = 0;
            for (int x : nums) {
                if (!stk.empty() && stk.back() + x == target) {
                    stk.pop_back();
                    ++ops;
                } else {
                    stk.push_back(x);
                }
            }
            best = max(best, ops);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxOperations(int[] nums) {
        int[] freq = new int[1001];
        for (int num : nums) {
            freq[num]++;
        }
        int maxOps = 0;
        for (int sum = 2; sum <= 2000; sum++) {
            int ops = 0;
            for (int v = 1; v <= 1000; v++) {
                int w = sum - v;
                if (w < 1 || w > 1000) continue;
                if (v == w) {
                    ops += freq[v] / 2;
                } else if (v < w) {
                    ops += Math.min(freq[v], freq[w]);
                }
            }
            maxOps = Math.max(maxOps, ops);
        }
        return maxOps;
    }
}
```

## Python

```python
class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(nums)
        max_ops = 0
        # possible sums range from min+min to max+max
        min_val, max_val = min(nums), max(nums)
        for s in range(min_val * 2, max_val * 2 + 1):
            ops = 0
            visited = set()
            for v in cnt:
                if v in visited:
                    continue
                u = s - v
                if u not in cnt:
                    continue
                if v == u:
                    ops += cnt[v] // 2
                    visited.add(v)
                else:
                    ops += min(cnt[v], cnt[u])
                    visited.add(v)
                    visited.add(u)
            max_ops = max(max_ops, ops)
        return max_ops
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_ops = 0
        # possible sums range from 2 to 2000 (since nums[i] <= 1000)
        for s in range(2, 2001):
            ops = 0
            for v in freq:
                u = s - v
                if u not in freq:
                    continue
                if v < u:
                    ops += min(freq[v], freq[u])
                elif v == u:
                    ops += freq[v] // 2
            max_ops = max(max_ops, ops)
        return max_ops
```

## C

```c
int maxOperations(int* nums, int numsSize) {
    int freq[1001] = {0};
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] >= 1 && nums[i] <= 1000)
            freq[nums[i]]++;
    }
    int best = 0;
    for (int sum = 2; sum <= 2000; ++sum) {
        int ops = 0;
        for (int v = 1; v <= 1000; ++v) {
            int u = sum - v;
            if (u < 1 || u > 1000) continue;
            if (v < u) {
                ops += freq[v] < freq[u] ? freq[v] : freq[u];
            } else if (v == u) {
                ops += freq[v] / 2;
            }
        }
        if (ops > best) best = ops;
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxOperations(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var x in nums) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }

        var possibleSums = new HashSet<int>();
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                possibleSums.Add(nums[i] + nums[j]);
            }
        }

        var keys = new List<int>(freq.Keys);
        int maxOps = 0;

        foreach (var sum in possibleSums) {
            int ops = 0;
            foreach (var v in keys) {
                int u = sum - v;
                if (!freq.ContainsKey(u)) continue;
                if (v < u) {
                    ops += Math.Min(freq[v], freq[u]);
                } else if (v == u) {
                    ops += freq[v] / 2;
                }
            }
            if (ops > maxOps) maxOps = ops;
        }

        return maxOps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxOperations = function(nums) {
    const MAX_VAL = 1000;
    const freq = new Array(MAX_VAL + 1).fill(0);
    for (const v of nums) freq[v]++;

    let best = 0;
    // possible sums range from 2 to 2000
    for (let s = 2; s <= 2 * MAX_VAL; ++s) {
        let ops = 0;
        let left = 1, right = MAX_VAL;
        while (left <= right) {
            const complement = s - left;
            if (complement < left) break; // ensure left <= complement
            if (complement > MAX_VAL) { left++; continue; }
            if (left === complement) {
                ops += Math.floor(freq[left] / 2);
            } else {
                ops += Math.min(freq[left], freq[complement]);
            }
            left++;
        }
        best = Math.max(best, ops);
    }
    return best;
};
```

## Typescript

```typescript
function maxOperations(nums: number[]): number {
    let maxOps = 0;
    const minSum = 2;
    const maxSum = 2000; // since nums[i] <= 1000
    for (let target = minSum; target <= maxSum; ++target) {
        let ops = 0;
        const stack: number[] = [];
        for (const x of nums) {
            if (stack.length && stack[stack.length - 1] + x === target) {
                stack.pop();
                ++ops;
            } else {
                stack.push(x);
            }
        }
        if (ops > maxOps) maxOps = ops;
    }
    return maxOps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxOperations($nums) {
        // frequency of each value (values are between 1 and 1000)
        $freq = array_fill(0, 1001, 0);
        foreach ($nums as $num) {
            $freq[$num]++;
        }

        $maxOps = 0;
        // possible sums range from 2 to 2000
        for ($s = 2; $s <= 2000; $s++) {
            $ops = 0;
            for ($v = 1; $v <= 1000; $v++) {
                $c = $s - $v;
                if ($c < 1 || $c > 1000) {
                    continue;
                }
                if ($v > $c) { // already counted this pair
                    continue;
                }
                if ($v == $c) {
                    $ops += intdiv($freq[$v], 2);
                } else {
                    $ops += min($freq[$v], $freq[$c]);
                }
            }
            if ($ops > $maxOps) {
                $maxOps = $ops;
            }
        }

        return $maxOps;
    }
}
```

## Swift

```swift
class Solution {
    func maxOperations(_ nums: [Int]) -> Int {
        var freq = Array(repeating: 0, count: 1001)
        for num in nums {
            if num >= 1 && num <= 1000 {
                freq[num] += 1
            }
        }
        var best = 0
        for sum in 2...2000 {
            var pairs = 0
            var v = 1
            while v < sum - v && v <= 1000 {
                let u = sum - v
                if u >= 1 && u <= 1000 {
                    pairs += min(freq[v], freq[u])
                }
                v += 1
            }
            if sum % 2 == 0 {
                let mid = sum / 2
                if mid >= 1 && mid <= 1000 {
                    pairs += freq[mid] / 2
                }
            }
            best = max(best, pairs)
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxOperations(nums: IntArray): Int {
        val freq = IntArray(1001)
        for (num in nums) {
            freq[num]++
        }
        var best = 0
        for (s in 2..2000) {
            var ops = 0
            for (v in 1..1000) {
                val w = s - v
                if (w < 1 || w > 1000) continue
                if (v > w) continue
                if (v == w) {
                    ops += freq[v] / 2
                } else {
                    ops += kotlin.math.min(freq[v], freq[w])
                }
            }
            best = kotlin.math.max(best, ops)
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxOperations(List<int> nums) {
    const int MAX_VAL = 1000;
    List<int> cnt = List.filled(MAX_VAL + 1, 0);
    for (var x in nums) cnt[x]++;

    int best = 0;
    for (int s = 2; s <= 2 * MAX_VAL; ++s) {
      int cur = 0;
      for (int v = 1; v <= MAX_VAL; ++v) {
        int u = s - v;
        if (u < 1 || u > MAX_VAL) continue;
        if (v < u) {
          cur += cnt[v] < cnt[u] ? cnt[v] : cnt[u];
        } else if (v == u) {
          cur += cnt[v] ~/ 2;
        }
      }
      if (cur > best) best = cur;
    }
    return best;
  }
}
```

## Golang

```go
func maxOperations(nums []int) int {
    freq := make(map[int]int)
    for _, v := range nums {
        freq[v]++
    }
    maxOps := 0
    // possible sums from 2 to 2000 (since nums[i] <= 1000)
    for s := 2; s <= 2000; s++ {
        ops := 0
        for v, cntV := range freq {
            w := s - v
            if w < v { // ensure each unordered pair counted once
                continue
            }
            cntW, ok := freq[w]
            if !ok {
                continue
            }
            if v == w {
                ops += cntV / 2
            } else {
                if cntV < cntW {
                    ops += cntV
                } else {
                    ops += cntW
                }
            }
        }
        if ops > maxOps {
            maxOps = ops
        }
    }
    return maxOps
}
```

## Ruby

```ruby
def max_operations(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }

  min_val = nums.min
  max_val = nums.max
  max_ops = 0

  (min_val + min_val).upto(max_val + max_val) do |s|
    ops = 0
    freq.each do |v, cnt|
      c = s - v
      next unless freq.key?(c)
      if v == c
        ops += cnt / 2
      elsif v < c
        ops += [cnt, freq[c]].min
      end
    end
    max_ops = ops if ops > max_ops
  end

  max_ops
end
```

## Scala

```scala
object Solution {
    def maxOperations(nums: Array[Int]): Int = {
        val maxVal = 1000
        val freq = new Array[Int](maxVal + 1)
        for (v <- nums) {
            freq(v) += 1
        }
        var best = 0
        for (s <- 2 to 2 * maxVal) {
            var pairs = 0
            var v = 1
            while (v <= s / 2 && v <= maxVal) {
                val u = s - v
                if (u >= 1 && u <= maxVal) {
                    if (v == u) {
                        pairs += freq(v) / 2
                    } else {
                        pairs += Math.min(freq(v), freq(u))
                    }
                }
                v += 1
            }
            if (pairs > best) best = pairs
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_operations(nums: Vec<i32>) -> i32 {
        let mut freq = vec![0i32; 1001];
        for &v in &nums {
            freq[v as usize] += 1;
        }
        let mut best = 0i32;
        for sum in 2..=2000 {
            let mut pairs = 0i32;
            let mut a = 1usize;
            while a <= 1000 && a * 2 <= sum as usize {
                let b = (sum - a as i32) as usize;
                if b > 1000 { a += 1; continue; }
                if a == b {
                    pairs += freq[a] / 2;
                } else {
                    pairs += std::cmp::min(freq[a], freq[b]);
                }
                a += 1;
            }
            best = best.max(pairs);
        }
        best
    }
}
```

## Racket

```racket
(define/contract (max-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-val 1000)
         (freq (make-vector (+ max-val 1) 0))) ; index 0 unused
    ;; count frequencies
    (for ([v nums])
      (vector-set! freq v (+ (vector-ref freq v) 1)))
    (define max-pairs 0)
    ;; try every possible sum s
    (for ([s (in-range 2 (+ (* max-val 2) 1))]) ; 2 .. 2000 inclusive
      (let ((pairs 0))
        ;; consider x <= y, x + y = s
        (for ([x (in-range 1 (add1 (quotient s 2)))])
          (let* ((y (- s x)))
            (when (and (>= y 1) (<= y max-val))
              (if (= x y)
                  (set! pairs (+ pairs (quotient (vector-ref freq x) 2)))
                  (set! pairs (+ pairs (min (vector-ref freq x)
                                            (vector-ref freq y))))))))
        (when (> pairs max-pairs)
          (set! max-pairs pairs))))
    max-pairs))
```

## Erlang

```erlang
-module(solution).
-export([max_operations/1]).

-spec max_operations(Nums :: [integer()]) -> integer().
max_operations(Nums) ->
    FreqMap = build_freq_map(Nums, #{}),
    lists:foldl(fun(S, Acc) ->
                        Ops = pairs_for_sum(S, FreqMap),
                        if Ops > Acc -> Ops; true -> Acc end
                end,
                0,
                lists:seq(2, 2000)).

build_freq_map([], Map) -> Map;
build_freq_map([H|T], Map) ->
    Count = maps:get(H, Map, 0),
    build_freq_map(T, Map#{H => Count + 1}).

pairs_for_sum(S, FreqMap) ->
    pairs_for_sum(S, maps:to_list(FreqMap), 0, FreqMap).

pairs_for_sum(_S, [], Acc, _FreqMap) -> Acc;
pairs_for_sum(S, [{Val, Cnt}|Rest], Acc, FreqMap) ->
    Complement = S - Val,
    case Complement of
        X when X < Val ->
            pairs_for_sum(S, Rest, Acc, FreqMap);
        X when X == Val ->
            NewAcc = Acc + (Cnt div 2),
            pairs_for_sum(S, Rest, NewAcc, FreqMap);
        X ->
            case maps:is_key(X, FreqMap) of
                true ->
                    CntComp = maps:get(X, FreqMap),
                    NewAcc = Acc + erlang:min(Cnt, CntComp),
                    pairs_for_sum(S, Rest, NewAcc, FreqMap);
                false ->
                    pairs_for_sum(S, Rest, Acc, FreqMap)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_operations(nums :: [integer]) :: integer
  def max_operations(nums) do
    freq = Enum.frequencies(nums)

    Enum.reduce(2..2000, 0, fn s, best ->
      ops = count_pairs_for_sum(s, freq)
      if ops > best, do: ops, else: best
    end)
  end

  defp count_pairs_for_sum(s, freq) do
    Enum.reduce(1..1000, 0, fn x, acc ->
      y = s - x

      cond do
        y < 1 or y > 1000 -> acc
        x < y ->
          fx = Map.get(freq, x, 0)
          fy = Map.get(freq, y, 0)
          acc + min(fx, fy)

        x == y ->
          fx = Map.get(freq, x, 0)
          acc + div(fx, 2)

        true ->
          acc
      end
    end)
  end
end
```
