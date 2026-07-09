# 2826. Sorting Three Groups

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> pref(4, vector<int>(n + 1, 0));
        for (int i = 0; i < n; ++i) {
            for (int v = 1; v <= 3; ++v) {
                pref[v][i + 1] = pref[v][i];
            }
            pref[nums[i]][i + 1]++;
        }
        int best = 0;
        for (int i = 0; i <= n; ++i) {          // end of segment for 1's
            for (int j = i; j <= n; ++j) {      // end of segment for 2's
                int correct = pref[1][i]                         // 1's in [0, i)
                            + (pref[2][j] - pref[2][i])          // 2's in [i, j)
                            + (pref[3][n] - pref[3][j]);         // 3's in [j, n)
                best = max(best, correct);
            }
        }
        return n - best;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(java.util.List<Integer> nums) {
        int n = nums.size();
        int[] pref1 = new int[n + 1];
        int[] pref2 = new int[n + 1];
        int[] pref3 = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int v = nums.get(i);
            pref1[i + 1] = pref1[i] + (v == 1 ? 1 : 0);
            pref2[i + 1] = pref2[i] + (v == 2 ? 1 : 0);
            pref3[i + 1] = pref3[i] + (v == 3 ? 1 : 0);
        }
        int maxKeep = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                int keep = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j]);
                if (keep > maxKeep) {
                    maxKeep = keep;
                }
            }
        }
        return n - maxKeep;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # best[v] = length of longest non-decreasing subsequence ending with value v (1..3)
        best = [0, 0, 0, 0]  # index 0 unused
        for x in nums:
            # maximum length we can extend from any value <= x
            cur = max(best[1:x+1]) + 1
            if cur > best[x]:
                best[x] = cur
        longest = max(best)
        return len(nums) - longest
```

## Python3

```python
class Solution:
    def minimumOperations(self, nums):
        n = len(nums)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        pref3 = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            pref1[i] = pref1[i - 1] + (x == 1)
            pref2[i] = pref2[i - 1] + (x == 2)
            pref3[i] = pref3[i - 1] + (x == 3)

        max_keep = 0
        for i in range(n + 1):
            for j in range(i, n + 1):
                keep = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j])
                if keep > max_keep:
                    max_keep = keep

        return n - max_keep
```

## C

```c
int minimumOperations(int* nums, int numsSize) {
    int dp1 = 0, dp2 = 0, dp3 = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        if (x == 1) {
            dp1 += 1;
        } else if (x == 2) {
            int bestPrev = dp1 > dp2 ? dp1 : dp2;
            dp2 = bestPrev + 1;
        } else { // x == 3
            int bestPrev = dp2 > dp3 ? dp2 : dp3;
            dp3 = bestPrev + 1;
        }
    }
    int maxLen = dp1;
    if (dp2 > maxLen) maxLen = dp2;
    if (dp3 > maxLen) maxLen = dp3;
    return numsSize - maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperations(IList<int> nums) {
        int n = nums.Count;
        int[] pref1 = new int[n + 1];
        int[] pref2 = new int[n + 1];
        int[] pref3 = new int[n + 1];

        for (int i = 0; i < n; i++) {
            pref1[i + 1] = pref1[i] + (nums[i] == 1 ? 1 : 0);
            pref2[i + 1] = pref2[i] + (nums[i] == 2 ? 1 : 0);
            pref3[i + 1] = pref3[i] + (nums[i] == 3 ? 1 : 0);
        }

        int maxKeep = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                int keep = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j]);
                if (keep > maxKeep) maxKeep = keep;
            }
        }

        return n - maxKeep;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    const n = nums.length;
    const pref1 = new Array(n + 1).fill(0);
    const pref2 = new Array(n + 1).fill(0);
    const pref3 = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref1[i + 1] = pref1[i] + (nums[i] === 1 ? 1 : 0);
        pref2[i + 1] = pref2[i] + (nums[i] === 2 ? 1 : 0);
        pref3[i + 1] = pref3[i] + (nums[i] === 3 ? 1 : 0);
    }
    let maxCorrect = 0;
    for (let i = 0; i <= n; ++i) {
        for (let j = i; j <= n; ++j) {
            const correct = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j]);
            if (correct > maxCorrect) maxCorrect = correct;
        }
    }
    return n - maxCorrect;
};
```

## Typescript

```typescript
function minimumOperations(nums: number[]): number {
    const n = nums.length;
    const pref1 = new Array(n + 1).fill(0);
    const pref2 = new Array(n + 1).fill(0);
    const pref3 = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        pref1[i + 1] = pref1[i] + (nums[i] === 1 ? 1 : 0);
        pref2[i + 1] = pref2[i] + (nums[i] === 2 ? 1 : 0);
        pref3[i + 1] = pref3[i] + (nums[i] === 3 ? 1 : 0);
    }
    let maxCorrect = 0;
    for (let i = 0; i <= n; i++) {
        for (let j = i; j <= n; j++) {
            const correct = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j]);
            if (correct > maxCorrect) maxCorrect = correct;
        }
    }
    return n - maxCorrect;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        $dp0 = 0; // longest subsequence of only 1's
        $dp1 = 0; // longest subsequence of 1's followed by 2's
        $dp2 = 0; // longest subsequence of 1's, then 2's, then 3's

        foreach ($nums as $x) {
            if ($x == 1) {
                $dp0 = $dp0 + 1;
            } elseif ($x == 2) {
                $dp1 = max($dp0, $dp1) + 1;
            } else { // x == 3
                $dp2 = max($dp1, $dp2) + 1;
            }
        }

        $maxLen = max($dp0, $dp1, $dp2);
        return count($nums) - $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var pref1 = Array(repeating: 0, count: n + 1)
        var pref2 = Array(repeating: 0, count: n + 1)
        var pref3 = Array(repeating: 0, count: n + 1)
        
        for i in 0..<n {
            pref1[i + 1] = pref1[i] + (nums[i] == 1 ? 1 : 0)
            pref2[i + 1] = pref2[i] + (nums[i] == 2 ? 1 : 0)
            pref3[i + 1] = pref3[i] + (nums[i] == 3 ? 1 : 0)
        }
        
        var maxKept = 0
        for i in 0...n {
            for j in i...n {
                let kept = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j])
                if kept > maxKept { maxKept = kept }
            }
        }
        
        return n - maxKept
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: List<Int>): Int {
        val n = nums.size
        val pref1 = IntArray(n + 1)
        val pref2 = IntArray(n + 1)
        val pref3 = IntArray(n + 1)
        for (i in 0 until n) {
            pref1[i + 1] = pref1[i] + if (nums[i] == 1) 1 else 0
            pref2[i + 1] = pref2[i] + if (nums[i] == 2) 1 else 0
            pref3[i + 1] = pref3[i] + if (nums[i] == 3) 1 else 0
        }
        var maxKeep = 0
        for (i in 0..n) {
            for (j in i..n) {
                val keep = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j])
                if (keep > maxKeep) maxKeep = keep
            }
        }
        return n - maxKeep
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    int n = nums.length;
    List<int> pref1 = List.filled(n + 1, 0);
    List<int> pref2 = List.filled(n + 1, 0);
    List<int> pref3 = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      pref1[i + 1] = pref1[i] + (nums[i] == 1 ? 1 : 0);
      pref2[i + 1] = pref2[i] + (nums[i] == 2 ? 1 : 0);
      pref3[i + 1] = pref3[i] + (nums[i] == 3 ? 1 : 0);
    }
    int maxKeep = 0;
    for (int i = 0; i <= n; i++) {
      for (int j = i; j <= n; j++) {
        int keep = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j]);
        if (keep > maxKeep) maxKeep = keep;
      }
    }
    return n - maxKeep;
  }
}
```

## Golang

```go
func minimumOperations(nums []int) int {
    n := len(nums)
    pref1 := make([]int, n+1)
    pref2 := make([]int, n+1)
    pref3 := make([]int, n+1)

    for i, v := range nums {
        pref1[i+1] = pref1[i]
        pref2[i+1] = pref2[i]
        pref3[i+1] = pref3[i]
        switch v {
        case 1:
            pref1[i+1]++
        case 2:
            pref2[i+1]++
        case 3:
            pref3[i+1]++
        }
    }

    total3 := pref3[n]
    minOps := n
    for i := 0; i <= n; i++ {
        onesCorrect := pref1[i]
        for j := i; j <= n; j++ {
            twosCorrect := pref2[j] - pref2[i]
            threesCorrect := total3 - pref3[j]
            keep := onesCorrect + twosCorrect + threesCorrect
            ops := n - keep
            if ops < minOps {
                minOps = ops
            }
        }
    }
    return minOps
}
```

## Ruby

```ruby
def minimum_operations(nums)
  n = nums.length
  pref1 = Array.new(n + 1, 0)
  pref2 = Array.new(n + 1, 0)
  pref3 = Array.new(n + 1, 0)

  (0...n).each do |i|
    pref1[i + 1] = pref1[i] + (nums[i] == 1 ? 1 : 0)
    pref2[i + 1] = pref2[i] + (nums[i] == 2 ? 1 : 0)
    pref3[i + 1] = pref3[i] + (nums[i] == 3 ? 1 : 0)
  end

  max_keep = 0
  (0..n).each do |i|
    (i..n).each do |j|
      keep = pref1[i] + (pref2[j] - pref2[i]) + (pref3[n] - pref3[j])
      max_keep = keep if keep > max_keep
    end
  end

  n - max_keep
end
```

## Scala

```scala
object Solution {
    def minimumOperations(nums: List[Int]): Int = {
        val n = nums.length
        val pref1 = new Array[Int](n + 1)
        val pref2 = new Array[Int](n + 1)
        val pref3 = new Array[Int](n + 1)

        for (i <- 0 until n) {
            pref1(i + 1) = pref1(i) + (if (nums(i) == 1) 1 else 0)
            pref2(i + 1) = pref2(i) + (if (nums(i) == 2) 1 else 0)
            pref3(i + 1) = pref3(i) + (if (nums(i) == 3) 1 else 0)
        }

        var maxKeep = 0
        for (i <- 0 to n) {
            val ones = pref1(i)
            for (j <- i to n) {
                val twos   = pref2(j) - pref2(i)
                val threes = pref3(n) - pref3(j)
                val keep = ones + twos + threes
                if (keep > maxKeep) maxKeep = keep
            }
        }

        n - maxKeep
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut dp1 = 0i32;
        let mut dp2 = 0i32;
        let mut dp3 = 0i32;
        for &v in nums.iter() {
            match v {
                1 => {
                    dp1 += 1;
                }
                2 => {
                    let new_dp2 = std::cmp::max(dp1, dp2) + 1;
                    if new_dp2 > dp2 {
                        dp2 = new_dp2;
                    }
                }
                3 => {
                    let new_dp3 = std::cmp::max(dp2, dp3) + 1;
                    if new_dp3 > dp3 {
                        dp3 = new_dp3;
                    }
                }
                _ => {}
            }
        }
        let max_len = *[dp1, dp2, dp3].iter().max().unwrap();
        nums.len() as i32 - max_len
    }
}
```

## Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (values
          (for/fold ([a 0] [b 0] [c 0]) ([x nums])
            (cond [(= x 1) (values (+ a 1) b c)]
                  [(= x 2) (values a (add1 (max a b)) c)]
                  [(= x 3) (values a b (add1 (max b c)))]))))
    (let-values ([(a b c) values])
      (- n (max a (max b c))))))
```

## Erlang

```erlang
-export([minimum_operations/1]).

-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
    N = length(Nums),
    {Pref1, Pref2, Pref3} = build_prefixes(Nums),
    MaxKeep = max_keep(N, Pref1, Pref2, Pref3),
    N - MaxKeep.

build_prefixes(Nums) ->
    build_prefixes(Nums, 0, 0, 0, [0], [0], [0]).

build_prefixes([], _C1, _C2, _C3, Acc1, Acc2, Acc3) ->
    {lists:reverse(Acc1), lists:reverse(Acc2), lists:reverse(Acc3)};
build_prefixes([H|T], C1, C2, C3, Acc1, Acc2, Acc3) ->
    case H of
        1 -> NewC1 = C1 + 1, NewC2 = C2,   NewC3 = C3;
        2 -> NewC1 = C1,     NewC2 = C2+1, NewC3 = C3;
        3 -> NewC1 = C1,     NewC2 = C2,   NewC3 = C3+1
    end,
    build_prefixes(T, NewC1, NewC2, NewC3,
                   [NewC1|Acc1], [NewC2|Acc2], [NewC3|Acc3]).

max_keep(N, Pref1, Pref2, Pref3) ->
    Values = [
        keep_for(I, J, N, Pref1, Pref2, Pref3)
        || I <- lists:seq(0, N),
           J <- lists:seq(I, N)
    ],
    lists:max(Values).

keep_for(I, J, N, Pref1, Pref2, Pref3) ->
    Count1 = nth(I, Pref1),
    Count2 = nth(J, Pref2) - nth(I, Pref2),
    Count3 = nth(N, Pref3) - nth(J, Pref3),
    Count1 + Count2 + Count3.

nth(Index, List) ->
    lists:nth(Index + 1, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    n = length(nums)

    pref1 = build_prefix(nums, 1)
    pref2 = build_prefix(nums, 2)
    pref3 = build_prefix(nums, 3)

    max_keep =
      for i <- 0..n,
          j <- i..n do
        ones = Enum.at(pref1, i)
        twos = Enum.at(pref2, j) - Enum.at(pref2, i)
        threes = Enum.at(pref3, n) - Enum.at(pref3, j)
        ones + twos + threes
      end
      |> Enum.max()

    n - max_keep
  end

  defp build_prefix(nums, val) do
    {list, _} =
      Enum.map_reduce(nums, 0, fn x, acc ->
        new = acc + if x == val, do: 1, else: 0
        {new, new}
      end)

    [0 | list]
  end
end
```
