# 2712. Minimum Cost to Make All Characters Equal

## Cpp

```cpp
class Solution {
public:
    vector<long long> prefixCost(const string& s, int target) {
        int n = s.size();
        const long long INF = (1LL<<60);
        vector<long long> res(n+1);
        long long dp0 = 0; // parity 0
        long long dp1 = INF; // parity 1
        res[0] = 0;
        for (int i = 1; i <= n; ++i) {
            int bit = s[i-1] - '0';
            long long ndp0 = INF, ndp1 = INF;
            // end with parity 0
            if ((bit ^ 0) == target) ndp0 = min(ndp0, dp0);
            if ((bit ^ 1) == target) ndp0 = min(ndp0, dp1 + i);
            // end with parity 1
            if ((bit ^ 1) == target) ndp1 = min(ndp1, dp1);
            if ((bit ^ 0) == target) ndp1 = min(ndp1, dp0 + i);
            dp0 = ndp0;
            dp1 = ndp1;
            res[i] = min(dp0, dp1);
        }
        return res;
    }

    long long minimumCost(string s) {
        int n = s.size();
        auto pref0 = prefixCost(s, 0);
        auto pref1 = prefixCost(s, 1);

        string rev(s.rbegin(), s.rend());
        auto revPref0 = prefixCost(rev, 0);
        auto revPref1 = prefixCost(rev, 1);

        vector<long long> suff0(n+1), suff1(n+1);
        for (int pos = 0; pos <= n; ++pos) {
            int len = n - pos;
            suff0[pos] = revPref0[len];
            suff1[pos] = revPref1[len];
        }

        long long ans = LLONG_MAX;
        for (int i = 0; i < n; ++i) {
            int bit = s[i] - '0';
            long long left = (bit == 0 ? pref0[i] : pref1[i]);
            long long right = (bit == 0 ? suff0[i+1] : suff1[i+1]);
            ans = min(ans, left + right);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minimumCost(String s) {
        int n = s.length();
        long ans = 0L;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) != s.charAt(i - 1)) {
                ans += Math.min(i, n - i);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        def prefix_cost(arr, target):
            n = len(arr)
            flip = [0] * (n + 1)   # flip[k]=1 if we flip prefix of length k
            cur = 0
            for i in range(n - 1, -1, -1):
                need = (arr[i] != target)
                if cur != need:
                    flip[i + 1] = 1
                    cur ^= 1
            pref = [0] * (n + 1)
            for k in range(1, n + 1):
                pref[k] = pref[k - 1] + (k if flip[k] else 0)
            return pref

        n = len(s)
        pref_zero = prefix_cost(s, '0')
        pref_one = prefix_cost(s, '1')

        rev = s[::-1]
        pref_zero_rev = prefix_cost(rev, '0')
        pref_one_rev = prefix_cost(rev, '1')

        ans = float('inf')
        for i, ch in enumerate(s):
            left_len = i
            right_len = n - i - 1
            if ch == '0':
                cost = pref_zero[left_len] + pref_zero_rev[right_len]
            else:
                cost = pref_one[left_len] + pref_one_rev[right_len]
            if cost < ans:
                ans = cost
        return ans
```

## Python3

```python
class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        # prefix transition costs (i+1) when s[i] != s[i+1]
        pre_trans = [0] * (n - 1)
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                pre_trans[i] = i + 1
        pref_cum = [0] * (n + 1)   # pref_cum[i] = sum_{j< i} pre_trans[j]
        for i in range(1, n):
            pref_cum[i] = pref_cum[i - 1] + pre_trans[i - 1]

        # suffix transition costs (n-i) when s[i] != s[i-1]
        suf_trans = [0] * n
        for i in range(1, n):
            if s[i] != s[i - 1]:
                suf_trans[i] = n - i
        suf_cum = [0] * (n + 2)   # suf_cum[i] = sum_{j>=i} suf_trans[j]
        for i in range(n - 1, -1, -1):
            suf_cum[i] = suf_cum[i + 1] + suf_trans[i]

        INF = 10 ** 18
        ans = INF
        for i in range(n):
            t = s[i]
            # cost to make prefix [0, i-1] all equal to t
            if i == 0:
                left_cost = 0
            else:
                left_cost = pref_cum[i]          # transitions inside the prefix
                if s[i - 1] != t:               # last char vs target
                    left_cost += i               # cost of flipping prefix length i

            # cost to make suffix [i+1, n-1] all equal to t
            j = i + 1
            if j >= n:
                right_cost = 0
            else:
                right_cost = suf_cum[j + 1]      # transitions inside the suffix
                if s[j] != t:                   # first char of suffix vs target
                    right_cost += (n - j)       # cost of flipping suffix starting at j

            ans = min(ans, left_cost + right_cost)

        return ans
```

## C

```c
#include <string.h>

long long minimumCost(char* s) {
    int n = strlen(s);
    long long total = 0;
    for (int i = 0; i < n - 1; ++i) {
        if (s[i] != s[i + 1]) {
            int left = i + 1;
            int right = n - left;
            total += (left < right) ? left : right;
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public long MinimumCost(string s) {
        int n = s.Length;
        if (n == 1) return 0L;

        // Prefix transition sums
        long[] sumPref = new long[n + 1];
        int[] cntPref = new int[n + 1];
        for (int i = 1; i < n; i++) {
            if (s[i - 1] != s[i]) {
                sumPref[i] = sumPref[i - 1] + i; // cost of transition at position i-1 is i
                cntPref[i] = cntPref[i - 1] + 1;
            } else {
                sumPref[i] = sumPref[i - 1];
                cntPref[i] = cntPref[i - 1];
            }
        }

        long[] prefCost = new long[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                prefCost[i] = 0;
                continue;
            }
            long baseCost = sumPref[i];
            int parity = cntPref[i] & 1;
            char afterFlips = parity == 0 ? s[0] : (s[0] == '0' ? '1' : '0');
            if (afterFlips != s[i]) baseCost += i; // flip whole prefix of length i
            prefCost[i] = baseCost;
        }

        // Prepare reversed string data for suffix calculations
        char[] revArr = new char[n];
        for (int i = 0; i < n; i++) revArr[i] = s[n - 1 - i];
        string rev = new string(revArr);

        long[] sumRev = new long[n + 1];
        int[] cntRev = new int[n + 1];
        for (int i = 1; i < n; i++) {
            if (rev[i - 1] != rev[i]) {
                sumRev[i] = sumRev[i - 1] + i;
                cntRev[i] = cntRev[i - 1] + 1;
            } else {
                sumRev[i] = sumRev[i - 1];
                cntRev[i] = cntRev[i - 1];
            }
        }

        long answer = long.MaxValue;
        for (int i = 0; i < n; i++) {
            // suffix length after position i
            int len = n - i - 1;
            long suffixCost = 0;
            if (len > 0) {
                long baseCost = sumRev[len];
                int parity = cntRev[len] & 1;
                char afterFlips = parity == 0 ? rev[0] : (rev[0] == '0' ? '1' : '0');
                if (afterFlips != s[i]) baseCost += len; // flip whole suffix of length len
                suffixCost = baseCost;
            }
            long total = prefCost[i] + suffixCost;
            if (total < answer) answer = total;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumCost = function(s) {
    const n = s.length;
    let total = 0;
    for (let i = 1; i < n; ++i) {
        if (s[i] !== s[i - 1]) {
            total += Math.min(i, n - i);
        }
    }
    return total;
};
```

## Typescript

```typescript
function minimumCost(s: string): number {
    const n = s.length;
    if (n <= 1) return 0;

    const invert = (c: string) => (c === '0' ? '1' : '0');

    function prefCost(target: string, str: string): number[] {
        const res = new Array<number>(str.length);
        let cost = 0;
        let flipped = false;
        for (let i = str.length - 1; i >= 0; --i) {
            let ch = str.charAt(i);
            if (flipped) ch = invert(ch);
            if (ch !== target) {
                cost += i + 1;          // prefix flip cost
                flipped = !flipped;
            }
            res[i] = cost;
        }
        return res;
    }

    const prefZero = prefCost('0', s);
    const prefOne = prefCost('1', s);

    const rev = s.split('').reverse().join('');
    const prefZeroRev = prefCost('0', rev);
    const prefOneRev = prefCost('1', rev);

    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < n; ++i) {
        const target = s.charAt(i);
        let left = 0, right = 0;

        if (i > 0) {
            left = target === '0' ? prefZero[i - 1] : prefOne[i - 1];
        }
        if (i < n - 1) {
            const idx = n - i - 2; // corresponding prefix index in reversed string
            right = target === '0' ? prefZeroRev[idx] : prefOneRev[idx];
        }

        ans = Math.min(ans, left + right);
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
    function minimumCost($s) {
        $n = strlen($s);
        // DP to compute prefix costs for target 0 and 1
        $prefZero = $this->computePrefixCosts($s, 0);
        $prefOne  = $this->computePrefixCosts($s, 1);

        // reversed string for suffix calculations
        $rev = strrev($s);
        $revPrefZero = $this->computePrefixCosts($rev, 0);
        $revPrefOne  = $this->computePrefixCosts($rev, 1);

        $ans = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            $bit = intval($s[$i]);
            $leftLen = $i;                     // length of prefix before i
            $rightLen = $n - $i - 1;           // length of suffix after i

            if ($bit === 0) {
                $leftCost = $prefZero[$leftLen];
                $rightCost = $revPrefZero[$rightLen];
            } else {
                $leftCost = $prefOne[$leftLen];
                $rightCost = $revPrefOne[$rightLen];
            }
            $total = $leftCost + $rightCost;
            if ($total < $ans) {
                $ans = $total;
            }
        }
        return $ans;
    }

    /**
     * Compute minimal costs to make first len characters equal to target using only prefix flips.
     *
     * @param string $str
     * @param int $target 0 or 1
     * @return array costs where index = length (0..n)
     */
    private function computePrefixCosts($str, $target) {
        $n = strlen($str);
        $INF = PHP_INT_MAX;
        $dpEven = 0;      // parity 0 cost for current length
        $dpOdd  = $INF;   // parity 1 cost

        $costs = array_fill(0, $n + 1, 0);
        $costs[0] = 0;

        for ($len = 1; $len <= $n; $len++) {
            $b = intval($str[$len - 1]);

            $newEven = $INF;
            $newOdd  = $INF;

            // transition from even parity
            if ($dpEven < $INF) {
                if ( ($b ^ 0) == $target ) {
                    // no flip needed, parity stays even
                    $newEven = min($newEven, $dpEven);
                } else {
                    // flip prefix of length $len, parity becomes odd
                    $newOdd = min($newOdd, $dpEven + $len);
                }
            }

            // transition from odd parity
            if ($dpOdd < $INF) {
                if ( ($b ^ 1) == $target ) {
                    // no flip needed, parity stays odd
                    $newOdd = min($newOdd, $dpOdd);
                } else {
                    // flip prefix, parity becomes even
                    $newEven = min($newEven, $dpOdd + $len);
                }
            }

            $dpEven = $newEven;
            $dpOdd  = $newOdd;

            $costs[$len] = min($dpEven, $dpOdd);
        }

        return $costs;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var total = 0
        if n <= 1 { return 0 }
        for i in 0..<(n - 1) {
            if chars[i] != chars[i + 1] {
                let left = i + 1
                let right = n - i - 1
                total += min(left, right)
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(s: String): Long {
        val n = s.length
        var total = 0L
        for (i in 0 until n - 1) {
            if (s[i] != s[i + 1]) {
                val left = (i + 1).toLong()
                val right = (n - i - 1).toLong()
                total += if (left < right) left else right
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(String s) {
    int n = s.length;
    List<int> bits = List<int>.generate(n, (i) => s.codeUnitAt(i) - 48);

    // Prefix costs
    List<int> prefZero = List<int>.filled(n + 1, 0);
    List<int> prefOne = List<int>.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefZero[i + 1] = prefZero[i];
      prefOne[i + 1] = prefOne[i];
      // For target '0', mismatching segment ends where a '1' is followed by '0' or end
      if (bits[i] == 1 && (i == n - 1 || bits[i + 1] == 0)) {
        prefZero[i + 1] += i + 1;
      }
      // For target '1', mismatching segment ends where a '0' is followed by '1' or end
      if (bits[i] == 0 && (i == n - 1 || bits[i + 1] == 1)) {
        prefOne[i + 1] += i + 1;
      }
    }

    // Suffix costs
    List<int> suffZero = List<int>.filled(n + 1, 0);
    List<int> suffOne = List<int>.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      suffZero[i] = suffZero[i + 1];
      suffOne[i] = suffOne[i + 1];
      // For target '0', mismatching segment starts where a '1' follows a '0' or at start
      if (bits[i] == 1 && (i == 0 || bits[i - 1] == 0)) {
        suffZero[i] += n - i;
      }
      // For target '1', mismatching segment starts where a '0' follows a '1' or at start
      if (bits[i] == 0 && (i == 0 || bits[i - 1] == 1)) {
        suffOne[i] += n - i;
      }
    }

    const int INF = 1 << 60;
    int ans = INF;
    for (int i = 0; i < n; ++i) {
      int left, right;
      if (bits[i] == 0) {
        left = prefZero[i];
        right = suffZero[i + 1];
      } else {
        left = prefOne[i];
        right = suffOne[i + 1];
      }
      int total = left + right;
      if (total < ans) ans = total;
    }
    return ans;
  }
}
```

## Golang

```go
func minimumCost(s string) int64 {
    n := len(s)
    var ans int64
    for i := 0; i < n-1; i++ {
        if s[i] != s[i+1] {
            left := int64(i + 1)
            right := int64(n - i - 1)
            if left < right {
                ans += left
            } else {
                ans += right
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_cost(s)
  n = s.length
  ans = 0
  (1...n).each do |i|
    if s.getbyte(i) != s.getbyte(i - 1)
      left = i
      right = n - i
      ans += left < right ? left : right
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
  def minimumCost(s: String): Long = {
    val n = s.length
    if (n <= 1) return 0L

    def computeLeft(target: Char): Array[Long] = {
      val res = new Array[Long](n)
      var cost: Long = 0L
      var parity = 0 // 0 means even flips, 1 odd flips
      for (i <- 0 until n) {
        val bit = if (s.charAt(i) == '1') 1 else 0
        val effective = bit ^ parity
        val need = if (target == '1') 1 else 0
        if (effective != need) {
          cost += (i + 1).toLong
          parity ^= 1
        }
        res(i) = cost
      }
      res
    }

    def computeRight(target: Char): Array[Long] = {
      val res = new Array[Long](n)
      var cost: Long = 0L
      var parity = 0
      for (i <- (n - 1) to 0 by -1) {
        val bit = if (s.charAt(i) == '1') 1 else 0
        val effective = bit ^ parity
        val need = if (target == '1') 1 else 0
        if (effective != need) {
          cost += (n - i).toLong
          parity ^= 1
        }
        res(i) = cost
      }
      res
    }

    val leftZero = computeLeft('0')
    val leftOne  = computeLeft('1')
    val rightZero = computeRight('0')
    val rightOne  = computeRight('1')

    var answer: Long = Long.MaxValue

    for (i <- 0 until n) {
      val leftCost =
        if (i == 0) 0L
        else if (s.charAt(i) == '0') leftZero(i - 1)
        else leftOne(i - 1)

      val rightCost =
        if (i == n - 1) 0L
        else if (s.charAt(i) == '0') rightZero(i + 1)
        else rightOne(i + 1)

      val total = leftCost + rightCost
      if (total < answer) answer = total
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_cost(s: String) -> i64 {
        let bytes = s.as_bytes();
        let n = bytes.len() as i64;
        let mut ans: i64 = 0;
        for i in 1..bytes.len() {
            if bytes[i] != bytes[i - 1] {
                let idx = i as i64;
                ans += std::cmp::min(idx, n - idx);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-cost s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (total
          (for/sum ([i (in-range (- n 1))])
            (if (char=? (string-ref s i) (string-ref s (+ i 1)))
                0
                (min (+ i 1) (- n i 1))))))
    total))
```

## Erlang

```erlang
-spec minimum_cost(S :: unicode:unicode_binary()) -> integer().
minimum_cost(S) ->
    BinList = binary:bin_to_list(S),
    Bits = [B - $0 || B <- BinList],
    N = length(Bits),

    %% Compute suffix costs for making suffix all 0 or all 1
    RevBits = lists:reverse(Bits),
    {Suff0, Suff1} = suffix_costs(RevBits, 0, 0, [], 0, 0, [], 0),

    Suff0Arr = array:from_list(Suff0),
    Suff1Arr = array:from_list(Suff1),

    Infinity = 1 bsl 60,
    forward_loop(Bits, 0, 0, 0, 0, 0, N, Suff0Arr, Suff1Arr, Infinity).

%% suffix_costs(RevBits, Parity0, Cost0, Acc0, Parity1, Cost1, Acc1, LenSeen)
suffix_costs([], _Parity0, _Cost0, Acc0, _Parity1, _Cost1, Acc1, _LenSeen) ->
    {lists:reverse(Acc0), lists:reverse(Acc1)};
suffix_costs([Bit|Rest], Parity0, Cost0, Acc0,
             Parity1, Cost1, Acc1, LenSeen) ->
    Effective0 = (Bit + Parity0) band 1,
    {Parity0New, Cost0New} =
        if Effective0 == 1 ->
                {1 - Parity0, Cost0 + LenSeen + 1};
           true -> {Parity0, Cost0}
        end,
    Effective1 = (Bit + Parity1) band 1,
    {Parity1New, Cost1New} =
        if Effective1 == 0 ->
                {1 - Parity1, Cost1 + LenSeen + 1};
           true -> {Parity1, Cost1}
        end,
    NewAcc0 = [Cost0New | Acc0],
    NewAcc1 = [Cost1New | Acc1],
    suffix_costs(Rest, Parity0New, Cost0New, NewAcc0,
                 Parity1New, Cost1New, NewAcc1, LenSeen + 1).

forward_loop([], _Idx, _Parity0, _Cost0, _Parity1, _Cost1,
              _N, _Suff0Arr, _Suff1Arr, Ans) ->
    Ans;
forward_loop([Bit|Rest], Idx, Parity0, Cost0, Parity1, Cost1,
              N, Suff0Arr, Suff1Arr, Ans) ->
    Target = Bit,
    LeftCost = case Target of
        0 -> Cost0;
        1 -> Cost1
    end,
    RightCost =
        if Idx == N - 1 ->
                0;
           true ->
                Index = Idx + 2, % array is 1‑based
                case Target of
                    0 -> array:get(Index, Suff0Arr);
                    1 -> array:get(Index, Suff1Arr)
                end
        end,
    Total = LeftCost + RightCost,
    NewAns = if Total < Ans -> Total; true -> Ans end,

    %% Update prefix costs for next positions
    Effective0 = (Bit + Parity0) band 1,
    {Parity0New, Cost0New} =
        if Effective0 == 1 ->
                {1 - Parity0, Cost0 + Idx + 1};
           true -> {Parity0, Cost0}
        end,
    Effective1 = (Bit + Parity1) band 1,
    {Parity1New, Cost1New} =
        if Effective1 == 0 ->
                {1 - Parity1, Cost1 + Idx + 1};
           true -> {Parity1, Cost1}
        end,

    forward_loop(Rest, Idx + 1, Parity0New, Cost0New,
                 Parity1New, Cost1New, N, Suff0Arr, Suff1Arr, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(String.t()) :: integer()
  def minimum_cost(s) do
    chars = String.to_charlist(s) |> Enum.map(&(&1 - ?0))
    n = length(chars)

    {suffix_zero, suffix_one} = compute_suffix(chars, n)

    best_initial = 1 <<< 60

    {_best, _par0, _cost0, _par1, _cost1} =
      Enum.reduce(Enum.with_index(chars), {best_initial, 0, 0, 0, 0}, fn {c, i},
                                                                      {best, par0, cost0,
                                                                       par1, cost1} ->
        left_cost = if c == 0, do: cost0, else: cost1

        right_cost =
          cond do
            i == n - 1 -> 0
            c == 0 -> Enum.at(suffix_zero, i + 1)
            true -> Enum.at(suffix_one, i + 1)
          end

        total = left_cost + right_cost
        best = if total < best, do: total, else: best

        # update prefix state for target '0'
        effective0 = if rem(par0, 2) == 0, do: c, else: 1 - c

        {par0_new, cost0_new} =
          if effective0 != 0 do
            {par0 + 1, cost0 + i + 1}
          else
            {par0, cost0}
          end

        # update prefix state for target '1'
        effective1 = if rem(par1, 2) == 0, do: c, else: 1 - c

        {par1_new, cost1_new} =
          if effective1 != 1 do
            {par1 + 1, cost1 + i + 1}
          else
            {par1, cost1}
          end

        {best, par0_new, cost0_new, par1_new, cost1_new}
      end)
    |> elem(0)
  end

  defp compute_suffix(chars, n) do
    acc =
      Enum.reduce(Enum.with_index(Enum.reverse(chars)), %{
        z_rev: [],
        o_rev: [],
        par0: 0,
        cost0: 0,
        par1: 0,
        cost1: 0
      }, fn {c, rev_idx}, state ->
        i = n - 1 - rev_idx

        # target '0'
        effective0 =
          if rem(state.par0, 2) == 0, do: c, else: 1 - c

        {par0_new, cost0_new, z_rev_new} =
          if effective0 != 0 do
            new_cost = state.cost0 + (n - i)
            {state.par0 + 1, new_cost, [new_cost | state.z_rev]}
          else
            {state.par0, state.cost0, [state.cost0 | state.z_rev]}
          end

        # target '1'
        effective1 =
          if rem(state.par1, 2) == 0, do: c, else: 1 - c

        {par1_new, cost1_new, o_rev_new} =
          if effective1 != 1 do
            new_cost = state.cost1 + (n - i)
            {state.par1 + 1, new_cost, [new_cost | state.o_rev]}
          else
            {state.par1, state.cost1, [state.cost1 | state.o_rev]}
          end

        %{
          z_rev: z_rev_new,
          o_rev: o_rev_new,
          par0: par0_new,
          cost0: cost0_new,
          par1: par1_new,
          cost1: cost1_new
        }
      end)

    zero = Enum.reverse(acc.z_rev)
    one = Enum.reverse(acc.o_rev)
    {zero, one}
  end
end
```
