# 2167. Minimum Time to Remove All Cars Containing Illegal Goods

## Cpp

```cpp
class Solution {
public:
    int minimumTime(string s) {
        int n = s.size();
        vector<int> left(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            int costDeleteOne = (s[i - 1] == '1') ? 2 : 0;
            left[i] = min(left[i - 1] + costDeleteOne, i);
        }
        vector<int> right(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            int costDeleteOne = (s[i] == '1') ? 2 : 0;
            right[i] = min(right[i + 1] + costDeleteOne, n - i);
        }
        int ans = INT_MAX;
        for (int i = 0; i <= n; ++i) {
            ans = min(ans, left[i] + right[i]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumTime(String s) {
        int n = s.length();
        int totalOnes = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') totalOnes++;
        }
        // Minimum prefix cost
        int prefMin = 0; // L=0 case
        int onesPref = 0;
        for (int i = 1; i <= n; i++) {
            if (s.charAt(i - 1) == '1') onesPref++;
            int cost = i - 2 * onesPref;
            if (cost < prefMin) prefMin = cost;
        }
        // Minimum suffix cost
        int sufMin = 0; // R=0 case
        int onesSuf = 0;
        for (int r = 1; r <= n; r++) {
            if (s.charAt(n - r) == '1') onesSuf++;
            int cost = r - 2 * onesSuf;
            if (cost < sufMin) sufMin = cost;
        }
        return prefMin + sufMin + 2 * totalOnes;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # bestLeft[i]: min time to remove all '1's in prefix s[:i] using left removals and direct deletions
        bestLeft = [0] * (n + 1)
        for i in range(1, n + 1):
            if s[i - 1] == '1':
                bestLeft[i] = min(i, bestLeft[i - 1] + 2)
            else:
                bestLeft[i] = min(i, bestLeft[i - 1])
        # bestRight[i]: min time to remove all '1's in suffix s[i:] using right removals and direct deletions
        bestRight = [0] * (n + 1)
        bestRight[n] = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                bestRight[i] = min(n - i, bestRight[i + 1] + 2)
            else:
                bestRight[i] = min(n - i, bestRight[i + 1])
        ans = float('inf')
        for i in range(n + 1):
            cur = bestLeft[i] + bestRight[i]
            if cur < ans:
                ans = cur
        return ans
```

## Python3

```python
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        # onlyFirst[i]: min time to clean prefix [0..i] using left deletions and individual removals
        onlyFirst = [0] * n
        dp = 0
        for i, ch in enumerate(s):
            if ch == '1':
                dp = min(dp + 2, i + 1)   # either remove this car individually or delete whole prefix up to i
            onlyFirst[i] = dp

        # withoutFirst[i]: min time to clean suffix [i..n-1] using right deletions and individual removals
        withoutFirst = [0] * n
        dp = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                dp = min(dp + 2, n - i)   # either remove this car individually or delete whole suffix from i
            withoutFirst[i] = dp

        ans = min(onlyFirst[-1], withoutFirst[0])  # all left or all right deletions
        for i in range(n - 1):
            ans = min(ans, onlyFirst[i] + withoutFirst[i + 1])
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minimumTime(char* s) {
    int n = strlen(s);
    int *pre = (int*)malloc((n + 1) * sizeof(int));
    pre[0] = 0;
    for (int i = 0; i < n; ++i) {
        pre[i + 1] = pre[i] + (s[i] == '1');
    }

    int *rightVal = (int*)malloc(n * sizeof(int));
    for (int r = 0; r < n; ++r) {
        rightVal[r] = (n - 1 - r) + 2 * pre[r + 1];
    }

    int *suffMin = (int*)malloc(n * sizeof(int));
    suffMin[n - 1] = rightVal[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        suffMin[i] = rightVal[i] < suffMin[i + 1] ? rightVal[i] : suffMin[i + 1];
    }

    int ans = n; // delete all cars from ends
    for (int l = 0; l < n; ++l) {
        int leftVal = l - 2 * pre[l];
        int cand = leftVal + suffMin[l];
        if (cand < ans) ans = cand;
    }

    free(pre);
    free(rightVal);
    free(suffMin);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumTime(string s) {
        int n = s.Length;
        int[] prefOnes = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefOnes[i + 1] = prefOnes[i] + (s[i] == '1' ? 1 : 0);
        }

        long ans = n; // remove all cars using only end deletions
        long bestA = long.MaxValue;

        for (int j = 0; j < n; j++) {
            long Ai = j - 2L * prefOnes[j];
            if (Ai < bestA) bestA = Ai;

            long Bj = (n - 1 - j) + 2L * prefOnes[j + 1];
            long cand = bestA + Bj;
            if (cand < ans) ans = cand;
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumTime = function(s) {
    const n = s.length;
    // prefix count of '1's
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + (s[i] === '1' ? 1 : 0);
    }
    // B[j] = (n - j) + 2 * prefOnes[j]
    const B = new Array(n + 1);
    for (let j = 0; j <= n; ++j) {
        B[j] = (n - j) + 2 * pref[j];
    }
    // suffix minima of B
    const minB = new Array(n + 1);
    minB[n] = B[n];
    for (let i = n - 1; i >= 0; --i) {
        minB[i] = Math.min(B[i], minB[i + 1]);
    }
    // withoutFirst[i]: minimal cost for suffix starting at i using only type2 and type3
    const withoutFirst = new Array(n + 1);
    for (let i = 0; i <= n; ++i) {
        withoutFirst[i] = minB[i] - 2 * pref[i];
    }
    // onlyFirst[i]: minimal cost for prefix ending at i using only type1 deletions
    const onlyFirst = new Array(n);
    let lastOne = -1;
    for (let i = 0; i < n; ++i) {
        if (s[i] === '1') lastOne = i;
        onlyFirst[i] = lastOne + 1; // 0 when no '1' seen yet
    }
    let ans = Infinity;
    // split before first character
    ans = Math.min(ans, withoutFirst[0]);
    for (let i = 0; i < n; ++i) {
        const cost = onlyFirst[i] + withoutFirst[i + 1];
        if (cost < ans) ans = cost;
    }
    return ans;
};
```

## Typescript

```typescript
function minimumTime(s: string): number {
    const n = s.length;
    const prefix = new Array<number>(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; i++) {
        if (s[i] === '0') {
            // keep it or delete from left end
            prefix[i + 1] = Math.min(prefix[i] + 1, prefix[i]);
        } else { // '1'
            // delete from left end or remove directly (cost 2)
            prefix[i + 1] = Math.min(prefix[i] + 1, prefix[i] + 2);
        }
    }

    const suffix = new Array<number>(n + 1);
    suffix[n] = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === '0') {
            // keep it or delete from right end
            suffix[i] = Math.min(suffix[i + 1] + 1, suffix[i + 1]);
        } else { // '1'
            // delete from right end or remove directly (cost 2)
            suffix[i] = Math.min(suffix[i + 1] + 1, suffix[i + 1] + 2);
        }
    }

    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i <= n; i++) {
        const total = prefix[i] + suffix[i];
        if (total < ans) ans = total;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumTime($s) {
        $n = strlen($s);
        if ($n == 0) return 0;

        $dpL = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; ++$i) {
            $costRemoveAll = $i + 1; // delete all cars up to i from left
            $prev = ($i > 0) ? $dpL[$i - 1] : 0;
            $costIndiv = ($s[$i] === '1' ? 2 : 0) + $prev; // handle current '1' with type‑3
            $dpL[$i] = min($costRemoveAll, $costIndiv);
        }

        $dpR = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $costRemoveAll = $n - $i; // delete all cars from i to right end
            $next = ($i < $n - 1) ? $dpR[$i + 1] : 0;
            $costIndiv = ($s[$i] === '1' ? 2 : 0) + $next;
            $dpR[$i] = min($costRemoveAll, $costIndiv);
        }

        $ans = PHP_INT_MAX;
        for ($i = 0; $i < $n - 1; ++$i) {
            $ans = min($ans, $dpL[$i] + $dpR[$i + 1]);
        }
        // cases where we only use left deletions or only right deletions
        $ans = min($ans, $dpL[$n - 1], $dpR[0]);

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTime(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var answer = n               // delete all via right-end removals
        var dpPrev = 0               // min time for prefix processed so far
        
        for i in 0..<n {
            let dpCurr: Int
            if chars[i] == "0" {
                dpCurr = dpPrev                     // nothing to do for '0'
            } else {
                let useDirect = dpPrev + 2          // remove this '1' directly (cost 2)
                let deletePrefix = i + 1            // delete whole prefix up to i from left
                dpCurr = min(useDirect, deletePrefix)
            }
            let suffixCost = n - i - 1               // delete remaining suffix from right
            answer = min(answer, dpCurr + suffixCost)
            dpPrev = dpCurr
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTime(s: String): Int {
        val n = s.length
        val pref = IntArray(n + 1)
        for (i in 1..n) {
            val costDirect = if (s[i - 1] == '1') 2 else 0
            pref[i] = kotlin.math.min(pref[i - 1] + costDirect, i)
        }
        val suff = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            val costDirect = if (s[i] == '1') 2 else 0
            suff[i] = kotlin.math.min(suff[i + 1] + costDirect, n - i)
        }
        var ans = Int.MAX_VALUE
        for (i in 0..n) {
            ans = kotlin.math.min(ans, pref[i] + suff[i])
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumTime(String s) {
    int n = s.length;
    List<int> pre = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      pre[i + 1] = pre[i] + (s.codeUnitAt(i) == 49 ? 1 : 0); // '1' ascii 49
    }
    int ans = n; // remove all cars from ends
    int minA = 0; // A for l = 0
    for (int r = 0; r < n; r++) {
      int B = (n - r - 1) + 2 * pre[r + 1];
      int cand = minA + B;
      if (cand < ans) ans = cand;
      int A = (r + 1) - 2 * pre[r + 1];
      if (A < minA) minA = A;
    }
    return ans;
  }
}
```

## Golang

```go
func minimumTime(s string) int {
	n := len(s)
	pre := make([]int, n+1)
	for i := 0; i < n; i++ {
		if s[i] == '1' {
			pre[i+1] = pre[i] + 1
		} else {
			pre[i+1] = pre[i]
		}
	}

	ans := n // remove all cars from ends
	const inf = int(^uint(0) >> 1) // max int
	minLeft := inf

	for j := 0; j < n; j++ {
		leftTerm := j - 2*pre[j]
		if leftTerm < minLeft {
			minLeft = leftTerm
		}
		suffixCost := (n - 1 - j) + 2*pre[j+1]
		candidate := minLeft + suffixCost
		if candidate < ans {
			ans = candidate
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimum_time(s)
  n = s.length
  min_ending_here = 0
  min_so_far = 0
  s.each_char do |ch|
    val = ch == '1' ? 1 : -1
    if min_ending_here > 0
      min_ending_here = val
    else
      min_ending_here += val
    end
    min_so_far = min_so_far < min_ending_here ? min_so_far : min_ending_here
  end
  n + min_so_far
end
```

## Scala

```scala
object Solution {
    def minimumTime(s: String): Int = {
        val n = s.length
        if (n == 0) return 0

        val left = new Array[Int](n)
        var prev = 0
        for (i <- 0 until n) {
            val ch = s.charAt(i)
            if (ch == '0') {
                left(i) = Math.min(prev, i + 1)
            } else {
                val useMiddle = prev + 2
                val deleteAll = i + 1
                left(i) = Math.min(useMiddle, deleteAll)
            }
            prev = left(i)
        }

        val right = new Array[Int](n)
        var next = 0
        for (i <- (n - 1) to 0 by -1) {
            val ch = s.charAt(i)
            if (ch == '0') {
                right(i) = Math.min(next, n - i)
            } else {
                val useMiddle = next + 2
                val deleteAll = n - i
                right(i) = Math.min(useMiddle, deleteAll)
            }
            next = right(i)
        }

        var ans = Int.MaxValue
        for (i <- -1 until n) {
            val leftCost = if (i >= 0) left(i) else 0
            val rightCost = if (i + 1 < n) right(i + 1) else 0
            ans = Math.min(ans, leftCost + rightCost)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_time(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        // only_first[i]: min time to clear all '1's in prefix [0, i)
        let mut only_first = vec![0i32; n + 1];
        for i in 0..n {
            let c = bytes[i];
            let opt_delete_left = only_first[i] + 1;
            let opt_keep_or_remove = if c == b'0' { only_first[i] } else { only_first[i] + 2 };
            only_first[i + 1] = std::cmp::min(opt_delete_left, opt_keep_or_remove);
        }
        // without_first[i]: min time to clear all '1's in suffix [i, n)
        let mut without_first = vec![0i32; n + 1];
        for i in (0..n).rev() {
            let c = bytes[i];
            let opt_delete_right = without_first[i + 1] + 1;
            let opt_keep_or_remove = if c == b'0' { without_first[i + 1] } else { without_first[i + 1] + 2 };
            without_first[i] = std::cmp::min(opt_delete_right, opt_keep_or_remove);
        }
        // combine prefix and suffix
        let mut ans = i32::MAX;
        for i in 0..=n {
            let total = only_first[i] + without_first[i];
            if total < ans {
                ans = total;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-time s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (pref (make-vector n))
         (suff (make-vector n)))
    ;; compute prefix DP using left deletions and type‑3 removals
    (let loop-left ((i 0) (cur 0))
      (when (< i n)
        (let* ((ch (string-ref s i))
               (add (if (char=? ch #\1) 2 0))
               (opt1 (+ cur add))          ; keep previous plan, handle this char
               (opt2 (+ i 1))              ; delete whole prefix with left ops
               (new (if (< opt1 opt2) opt1 opt2)))
          (vector-set! pref i new)
          (loop-left (+ i 1) new))))
    ;; compute suffix DP using right deletions and type‑3 removals
    (let loop-right ((i (- n 1)) (cur 0))
      (when (>= i 0)
        (let* ((ch (string-ref s i))
               (add (if (char=? ch #\1) 2 0))
               (opt1 (+ cur add))
               (opt2 (- n i))              ; delete whole suffix with right ops
               (new (if (< opt1 opt2) opt1 opt2)))
          (vector-set! suff i new)
          (loop-right (- i 1) new))))
    ;; combine prefix and suffix solutions
    (let ((ans (vector-ref pref (- n 1))))   ; all left deletions / internal removals
      (let loop-split ((i 0) (best ans))
        (if (< i (- n 1))
            (let* ((candidate (+ (vector-ref pref i)
                                 (vector-ref suff (+ i 1))))
                   (new-best (if (< candidate best) candidate best)))
              (loop-split (+ i 1) new-best))
            (let ((right-only (vector-ref suff 0)))
              (if (< right-only best) right-only best)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_time/1]).

-spec minimum_time(S :: unicode:unicode_binary()) -> integer().
minimum_time(S) ->
    L = binary_to_list(S),
    RevL = lists:reverse(L),
    SufList = compute_suffix(RevL, 0, 1, [0]),
    find_min(SufList).

compute_suffix([], _Prev, _Pos, Acc) ->
    Acc;
compute_suffix([Char|Rest], Prev, Pos, Acc) ->
    Cost = case Char of
        $1 -> 2;
        _ -> 0
    end,
    Best = erlang:min(Prev + Cost, Pos),
    compute_suffix(Rest, Best, Pos + 1, [Best | Acc]).

find_min([First|Rest]) ->
    InitialMin = First,
    find_min(Rest, 1, InitialMin).

find_min([], _Idx, Min) ->
    Min;
find_min([Suf|Rest], Idx, Min) ->
    Total = Idx + Suf,
    NewMin = if Total < Min -> Total; true -> Min end,
    find_min(Rest, Idx + 1, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time(s :: String.t) :: integer
  def minimum_time(s) do
    chars = :binary.bin_to_list(s)
    n = length(chars)

    # Prefix DP: only left removals and type-3 deletions
    {pref_rev, _} =
      Enum.reduce(Enum.with_index(chars, 1), {[], 0}, fn {c, i}, {acc, prev} ->
        val = if c == ?0, do: prev, else: min(prev + 2, i)
        {[val | acc], val}
      end)

    pref = [0] ++ Enum.reverse(pref_rev)   # length n+1

    # Suffix DP: only right removals and type-3 deletions
    {suff_rev, _} =
      Enum.reduce(Enum.with_index(Enum.reverse(chars), 1), {[], 0}, fn {c, i}, {acc, prev} ->
        val = if c == ?0, do: prev, else: min(prev + 2, i)
        {[val | acc], val}
      end)

    suff = suff_rev ++ [0]                 # length n+1

    # Minimum over all split points
    Enum.zip(pref, suff)
    |> Enum.map(fn {a, b} -> a + b end)
    |> Enum.min()
  end
end
```
