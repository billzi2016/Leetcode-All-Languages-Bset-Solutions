# 1027. Longest Arithmetic Subsequence

## Cpp

```cpp
class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return n;
        vector<unordered_map<int, int>> dp(n);
        int ans = 2;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int diff = nums[i] - nums[j];
                int len = 2;
                auto it = dp[j].find(diff);
                if (it != dp[j].end()) {
                    len = it->second + 1;
                }
                auto &ref = dp[i][diff];
                if (len > ref) ref = len;
                ans = max(ans, len);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;
        @SuppressWarnings("unchecked")
        java.util.HashMap<Integer, Integer>[] dp = new java.util.HashMap[n];
        for (int i = 0; i < n; i++) dp[i] = new java.util.HashMap<>();
        int ans = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j];
                int len = dp[j].getOrDefault(diff, 1) + 1;
                dp[i].put(diff, Math.max(dp[i].getOrDefault(diff, 0), len));
                ans = Math.max(ans, len);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        dp = [dict() for _ in range(n)]
        ans = 2
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev_len = dp[j].get(diff, 1)
                cur_len = prev_len + 1
                if cur_len > dp[i].get(diff, 0):
                    dp[i][diff] = cur_len
                    if cur_len > ans:
                        ans = cur_len
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        dp = [dict() for _ in range(n)]
        ans = 2
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev_len = dp[j].get(diff, 1)
                cur_len = prev_len + 1
                if cur_len > dp[i].get(diff, 0):
                    dp[i][diff] = cur_len
                    if cur_len > ans:
                        ans = cur_len
        return ans
```

## C

```c
#include <stdlib.h>

int longestArithSeqLength(int* nums, int numsSize) {
    if (numsSize <= 2) return numsSize;
    const int OFFSET = 500;
    const int D = 1001; // possible differences from -500 to 500 inclusive

    int **dp = (int **)malloc(numsSize * sizeof(int *));
    for (int i = 0; i < numsSize; ++i) {
        dp[i] = (int *)calloc(D, sizeof(int));
    }

    int ans = 2;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = 0; j < i; ++j) {
            int diff = nums[i] - nums[j];
            int idx = diff + OFFSET;
            int len = dp[j][idx] ? dp[j][idx] + 1 : 2;
            if (len > dp[i][idx]) {
                dp[i][idx] = len;
                if (len > ans) ans = len;
            }
        }
    }

    for (int i = 0; i < numsSize; ++i) {
        free(dp[i]);
    }
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestArithSeqLength(int[] nums)
    {
        int n = nums.Length;
        if (n <= 2) return n;

        var dp = new Dictionary<int, int>[n];
        int maxLen = 2;

        for (int i = 0; i < n; i++)
        {
            dp[i] = new Dictionary<int, int>();
            for (int j = 0; j < i; j++)
            {
                int diff = nums[i] - nums[j];
                int len = 2;
                if (dp[j].TryGetValue(diff, out int prev))
                    len = prev + 1;

                if (dp[i].TryGetValue(diff, out int existing))
                {
                    if (len > existing) dp[i][diff] = len;
                }
                else
                {
                    dp[i][diff] = len;
                }

                if (len > maxLen) maxLen = len;
            }
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestArithSeqLength = function(nums) {
    const n = nums.length;
    if (n <= 2) return n;
    const dp = Array.from({ length: n }, () => new Map());
    let ans = 2;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            const diff = nums[i] - nums[j];
            const prevLen = dp[j].get(diff) || 1; // length ending at j, default is just the element itself
            const curLen = prevLen + 1;
            const existing = dp[i].get(diff) || 0;
            if (curLen > existing) {
                dp[i].set(diff, curLen);
                if (curLen > ans) ans = curLen;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function longestArithSeqLength(nums: number[]): number {
    const n = nums.length;
    if (n <= 2) return n;

    const dp: Array<Map<number, number>> = new Array(n);
    for (let i = 0; i < n; i++) dp[i] = new Map();

    let maxLen = 2;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            const diff = nums[i] - nums[j];
            const prevLen = dp[j].get(diff) ?? 1;
            const curLen = prevLen + 1;

            const existing = dp[i].get(diff) ?? 2;
            if (curLen > existing) {
                dp[i].set(diff, curLen);
            } else {
                // ensure at least length 2 is stored for this diff
                dp[i].set(diff, existing);
            }

            if (curLen > maxLen) maxLen = curLen;
        }
    }

    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestArithSeqLength($nums) {
        $n = count($nums);
        if ($n <= 2) return $n;
        $dp = array_fill(0, $n, []);
        $maxLen = 2;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                $diff = $nums[$i] - $nums[$j];
                if (isset($dp[$j][$diff])) {
                    $len = $dp[$j][$diff] + 1;
                } else {
                    $len = 2;
                }
                if (!isset($dp[$i][$diff]) || $dp[$i][$diff] < $len) {
                    $dp[$i][$diff] = $len;
                }
                if ($len > $maxLen) {
                    $maxLen = $len;
                }
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestArithSeqLength(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 2 { return n }
        var dp = Array(repeating: [Int:Int](), count: n)
        var result = 2
        
        for i in 0..<n {
            for j in 0..<i {
                let diff = nums[i] - nums[j]
                let prevLen = dp[j][diff] ?? 1
                let curLen = prevLen + 1
                if let existing = dp[i][diff] {
                    if curLen > existing {
                        dp[i][diff] = curLen
                    }
                } else {
                    dp[i][diff] = curLen
                }
                result = max(result, curLen)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestArithSeqLength(nums: IntArray): Int {
        val n = nums.size
        if (n <= 2) return n
        val dp = Array(n) { HashMap<Int, Int>() }
        var ans = 2
        for (i in 0 until n) {
            for (j in 0 until i) {
                val diff = nums[i] - nums[j]
                val len = dp[j].getOrDefault(diff, 1) + 1
                val cur = dp[i].getOrDefault(diff, 0)
                if (len > cur) {
                    dp[i][diff] = len
                }
                if (len > ans) ans = len
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int longestArithSeqLength(List<int> nums) {
    int n = nums.length;
    if (n <= 2) return n;
    List<Map<int, int>> dp = List.generate(n, (_) => <int, int>{});
    int ans = 2;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < i; ++j) {
        int diff = nums[i] - nums[j];
        int len = (dp[j][diff] ?? 1) + 1;
        if (len > (dp[i][diff] ?? 0)) {
          dp[i][diff] = len;
        }
        if (len > ans) ans = len;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func longestArithSeqLength(nums []int) int {
	n := len(nums)
	if n <= 2 {
		return n
	}
	dp := make([]map[int]int, n)
	for i := range dp {
		dp[i] = make(map[int]int)
	}
	ans := 2
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			diff := nums[i] - nums[j]
			prev := dp[j][diff]
			curLen := 2
			if prev > 0 {
				curLen = prev + 1
			}
			if dp[i][diff] < curLen {
				dp[i][diff] = curLen
			}
			if ans < curLen {
				ans = curLen
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def longest_arith_seq_length(nums)
  n = nums.length
  dp = Array.new(n) { Hash.new(0) }
  max_len = 0

  (0...n).each do |i|
    (0...i).each do |j|
      diff = nums[i] - nums[j]
      len = dp[j][diff] > 0 ? dp[j][diff] + 1 : 2
      dp[i][diff] = len if len > dp[i][diff]
      max_len = len if len > max_len
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def longestArithSeqLength(nums: Array[Int]): Int = {
        val n = nums.length
        if (n <= 2) return n
        val dp = Array.fill(n)(mutable.Map.empty[Int, Int])
        var maxLen = 2

        for (i <- 0 until n) {
            for (j <- 0 until i) {
                val diff = nums(i) - nums(j)
                // length of sequence ending at j with this diff, default is 1 (single element)
                val prevLen = dp(j).getOrElse(diff, 1)
                val curLen = prevLen + 1
                val existing = dp(i).getOrElse(diff, 0)
                if (curLen > existing) {
                    dp(i)(diff) = curLen
                }
                if (curLen > maxLen) maxLen = curLen
            }
        }

        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_arith_seq_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 2 {
            return n as i32;
        }
        use std::collections::HashMap;
        let mut dp: Vec<HashMap<i32, usize>> = vec![HashMap::new(); n];
        let mut max_len = 2usize;

        for i in 0..n {
            for j in 0..i {
                let diff = nums[i] - nums[j];
                let prev_len = *dp[j].get(&diff).unwrap_or(&1);
                let cur_len = prev_len + 1;
                let entry = dp[i].entry(diff).or_insert(cur_len);
                if *entry < cur_len {
                    *entry = cur_len;
                }
                if cur_len > max_len {
                    max_len = cur_len;
                }
            }
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (longest-arith-seq-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((arr (list->vector nums))
         (n (vector-length arr))
         (dp (make-vector n)))
    ;; initialize hash tables for each index
    (for ([i (in-range n)])
      (vector-set! dp i (make-hash)))
    (define maxlen 0)
    (for ([i (in-range n)])
      (let ((hash-i (vector-ref dp i)))
        (for ([j (in-range i)])
          (let* ((diff (- (vector-ref arr i) (vector-ref arr j)))
                 (prev (hash-ref (vector-ref dp j) diff #f))
                 (len (if prev (+ prev 1) 2))
                 (existing (hash-ref hash-i diff #f)))
            (when (or (not existing) (> len existing))
              (hash-set! hash-i diff len)
              (when (> len maxlen) (set! maxlen len)))))))
    maxlen))
```

## Erlang

```erlang
-spec longest_arith_seq_length(Nums :: [integer()]) -> integer().
longest_arith_seq_length(Nums) ->
    NumsTuple = list_to_tuple(Nums),
    Len = tuple_size(NumsTuple),
    case Len of
        0 -> 0;
        1 -> 1;
        _ -> process(0, Len, NumsTuple, #{}, 2)
    end.

process(I, Len, _NumsTuple, _DPMap, Max) when I >= Len ->
    Max;
process(I, Len, NumsTuple, DPMap, Max) ->
    NumI = element(I + 1, NumsTuple),
    {MapI, NewMax} = inner(0, I, NumI, NumsTuple, DPMap, #{}, Max),
    DPMap1 = maps:put(I, MapI, DPMap),
    process(I + 1, Len, NumsTuple, DPMap1, NewMax).

inner(J, I, _NumI, _NumsTuple, _DPMap, CurMapI, CurMax) when J >= I ->
    {CurMapI, CurMax};
inner(J, I, NumI, NumsTuple, DPMap, CurMapI, CurMax) ->
    NumJ = element(J + 1, NumsTuple),
    Diff = NumI - NumJ,
    PrevMapJ = case maps:find(J, DPMap) of
        {ok, M} -> M;
        error -> #{}
    end,
    PrevLen = case maps:find(Diff, PrevMapJ) of
        {ok, L} -> L;
        error -> 1
    end,
    NewLen = PrevLen + 1,
    Existing = maps:get(Diff, CurMapI, 0),
    UpdatedMapI = if NewLen > Existing ->
                      maps:put(Diff, NewLen, CurMapI);
                  true ->
                      CurMapI
                  end,
    UpdatedMax = max(CurMax, NewLen),
    inner(J + 1, I, NumI, NumsTuple, DPMap, UpdatedMapI, UpdatedMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_arith_seq_length(nums :: [integer]) :: integer
  def longest_arith_seq_length(nums) do
    n = length(nums)

    if n <= 2 do
      n
    else
      nums_t = :erlang.list_to_tuple(nums)
      dp = List.duplicate(%{}, n)

      {_dp_final, ans} =
        Enum.reduce(0..(n - 1), {dp, 0}, fn i, {dp_acc, best} ->
          num_i = elem(nums_t, i)

          map_i =
            Enum.reduce(0..(i - 1), %{}, fn j, map_acc ->
              diff = num_i - elem(nums_t, j)
              prev_len = Map.get(Enum.at(dp_acc, j), diff, 1)
              new_len = prev_len + 1

              case Map.get(map_acc, diff) do
                nil -> Map.put(map_acc, diff, new_len)
                existing when existing < new_len -> Map.put(map_acc, diff, new_len)
                _ -> map_acc
              end
            end)

          best2 =
            Enum.reduce(Map.values(map_i), best, fn v, acc ->
              if v > acc, do: v, else: acc
            end)

          dp_updated = List.replace_at(dp_acc, i, map_i)
          {dp_updated, best2}
        end)

      ans
    end
  end
end
```
