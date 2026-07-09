# 2731. Movement of Robots

## Cpp

```cpp
class Solution {
public:
    int sumDistance(vector<int>& nums, string s, int d) {
        const long long MOD = 1000000007LL;
        int n = nums.size();
        vector<long long> pos(n);
        for (int i = 0; i < n; ++i) {
            if (s[i] == 'L')
                pos[i] = (long long)nums[i] - d;
            else
                pos[i] = (long long)nums[i] + d;
        }
        sort(pos.begin(), pos.end());
        long long prefix = 0; // sum of previous positions modulo MOD
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long curMod = (pos[i] % MOD + MOD) % MOD;
            long long contrib = (curMod * i) % MOD;
            contrib = (contrib - prefix + MOD) % MOD;
            ans = (ans + contrib) % MOD;
            prefix = (prefix + curMod) % MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int sumDistance(int[] nums, String s, int d) {
        int n = nums.length;
        long[] pos = new long[n];
        for (int i = 0; i < n; i++) {
            long delta = (s.charAt(i) == 'L') ? - (long) d : (long) d;
            pos[i] = (long) nums[i] + delta;
        }
        java.util.Arrays.sort(pos);
        final long MOD = 1_000_000_007L;
        long prefix = 0;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long cur = pos[i];
            long diff = cur * i - prefix; // sum of distances contributed by cur with previous elements
            diff %= MOD;
            if (diff < 0) diff += MOD;
            ans += diff;
            ans %= MOD;
            prefix += cur;
        }
        return (int) (ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def sumDistance(self, nums, s, d):
        """
        :type nums: List[int]
        :type s: str
        :type d: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        pos = [0] * n
        for i in range(n):
            if s[i] == 'R':
                pos[i] = nums[i] + d
            else:
                pos[i] = nums[i] - d

        pos.sort()
        prefix = 0
        ans = 0
        for i, val in enumerate(pos):
            ans = (ans + val * i - prefix) % MOD
            prefix += val
        return ans % MOD
```

## Python3

```python
from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        final_pos = [nums[i] + (d if c == 'R' else -d) for i, c in enumerate(s)]
        final_pos.sort()
        pref = 0
        ans = 0
        for i, val in enumerate(final_pos):
            ans = (ans + val * i - pref) % MOD
            pref += val
        return ans % MOD
```

## C

```c
#include <stdlib.h>

static int cmp_longlong(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

int sumDistance(int* nums, int numsSize, char* s, int d) {
    const long long MOD = 1000000007LL;
    long long *pos = (long long *)malloc(numsSize * sizeof(long long));
    if (!pos) return 0;

    for (int i = 0; i < numsSize; ++i) {
        long long shift = (s[i] == 'R') ? (long long)d : -(long long)d;
        pos[i] = (long long)nums[i] + shift;
    }

    qsort(pos, numsSize, sizeof(long long), cmp_longlong);

    long long prefix = 0;   // sum of positions before current index
    long long ans = 0;

    for (int i = 0; i < numsSize; ++i) {
        long long diff = pos[i] * (long long)i - prefix;   // non‑negative
        diff %= MOD;
        if (diff < 0) diff += MOD;
        ans += diff;
        if (ans >= MOD) ans -= MOD;
        prefix += pos[i];
    }

    free(pos);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int SumDistance(int[] nums, string s, int d) {
        int n = nums.Length;
        long[] pos = new long[n];
        for (int i = 0; i < n; i++) {
            if (s[i] == 'R')
                pos[i] = (long)nums[i] + d;
            else
                pos[i] = (long)nums[i] - d;
        }
        Array.Sort(pos);
        const long MOD = 1_000_000_007L;
        long prefix = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            long val = ((pos[i] % MOD) + MOD) % MOD;
            long contrib = (val * i) % MOD;
            contrib = (contrib - prefix + MOD) % MOD;
            ans = (ans + contrib) % MOD;
            prefix = (prefix + val) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {string} s
 * @param {number} d
 * @return {number}
 */
var sumDistance = function(nums, s, d) {
    const MOD = 1000000007n;
    const n = nums.length;
    const bigD = BigInt(d);
    const positions = new Array(n);
    for (let i = 0; i < n; ++i) {
        const delta = s[i] === 'R' ? bigD : -bigD;
        positions[i] = BigInt(nums[i]) + delta;
    }
    positions.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
    
    let prefix = 0n;
    let total = 0n;
    for (let i = 0; i < n; ++i) {
        const pos = positions[i];
        total += pos * BigInt(i) - prefix;
        prefix += pos;
    }
    const ans = ((total % MOD) + MOD) % MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function sumDistance(nums: number[], s: string, d: number): number {
    const MOD = 1_000_000_007;
    const n = nums.length;
    const pos: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        pos[i] = nums[i] + (s.charAt(i) === 'R' ? d : -d);
    }
    pos.sort((a, b) => a - b);
    let prefix = 0;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const val = pos[i];
        const contrib = val * i - prefix;
        const add = ((contrib % MOD) + MOD) % MOD;
        ans = (ans + add) % MOD;
        prefix += val;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param String $s
     * @param Integer $d
     * @return Integer
     */
    function sumDistance($nums, $s, $d) {
        $mod = 1000000007;
        $n = count($nums);
        $finals = [];
        for ($i = 0; $i < $n; $i++) {
            $val = ($s[$i] === 'R') ? $nums[$i] + $d : $nums[$i] - $d;
            $finals[] = $val;
        }
        sort($finals, SORT_NUMERIC);
        $prefix = 0;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $val = $finals[$i];
            $contrib = $i * $val - $prefix;
            $ans = ($ans + $contrib) % $mod;
            $prefix += $val;
        }
        if ($ans < 0) {
            $ans += $mod;
        }
        return (int)$ans;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func sumDistance(_ nums: [Int], _ s: String, _ d: Int) -> Int {
        let MOD = Int64(1_000_000_007)
        let n = nums.count
        var positions = [Int64]()
        positions.reserveCapacity(n)
        let dd = Int64(d)
        let dirs = Array(s)
        
        for i in 0..<n {
            var pos = Int64(nums[i])
            if dirs[i] == "L" {
                pos -= dd
            } else {
                pos += dd
            }
            positions.append(pos)
        }
        
        positions.sort()
        var prefix: Int64 = 0
        var result: Int64 = 0
        
        for i in 0..<n {
            let p = positions[i]
            let contrib = (p * Int64(i) - prefix) % MOD
            result = (result + contrib) % MOD
            if result < 0 { result += MOD }
            prefix += p
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumDistance(nums: IntArray, s: String, d: Int): Int {
        val MOD = 1_000_000_007L
        val n = nums.size
        val shift = d.toLong()
        val arr = LongArray(n)
        for (i in 0 until n) {
            val delta = if (s[i] == 'R') shift else -shift
            arr[i] = nums[i].toLong() + delta
        }
        java.util.Arrays.sort(arr)
        var prefixMod = 0L
        var ans = 0L
        for (i in 0 until n) {
            var curMod = arr[i] % MOD
            if (curMod < 0) curMod += MOD
            val contribution = ((curMod * i % MOD - prefixMod + MOD) % MOD)
            ans += contribution
            if (ans >= MOD) ans -= MOD
            prefixMod += curMod
            if (prefixMod >= MOD) prefixMod -= MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;
  int sumDistance(List<int> nums, String s, int d) {
    int n = nums.length;
    List<int> pos = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      if (s[i] == 'L') {
        pos[i] = nums[i] - d;
      } else {
        pos[i] = nums[i] + d;
      }
    }
    pos.sort();
    int ans = 0;
    int prefix = 0;
    for (int i = 0; i < n; i++) {
      int cur = pos[i];
      int diff = cur * i - prefix;
      int add = ((diff % MOD) + MOD) % MOD;
      ans += add;
      if (ans >= MOD) ans -= MOD;
      prefix += cur;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func sumDistance(nums []int, s string, d int) int {
    n := len(nums)
    pos := make([]int64, n)
    dd := int64(d)
    for i := 0; i < n; i++ {
        if s[i] == 'R' {
            pos[i] = int64(nums[i]) + dd
        } else {
            pos[i] = int64(nums[i]) - dd
        }
    }
    sort.Slice(pos, func(i, j int) bool { return pos[i] < pos[j] })
    const MOD int64 = 1000000007
    var prefix int64
    var ans int64
    for i := 0; i < n; i++ {
        ans += pos[i]*int64(i) - prefix
        prefix += pos[i]
    }
    ans %= MOD
    if ans < 0 {
        ans += MOD
    }
    return int(ans)
}
```

## Ruby

```ruby
def sum_distance(nums, s, d)
  n = nums.length
  final = Array.new(n)
  n.times do |i|
    if s[i] == 'R'
      final[i] = nums[i] + d
    else
      final[i] = nums[i] - d
    end
  end

  final.sort!
  mod = 1_000_000_007
  prefix = 0
  ans = 0

  final.each_with_index do |val, i|
    val_mod = val % mod
    ans = (ans + (val_mod * i - prefix)) % mod
    prefix = (prefix + val_mod) % mod
  end

  ans += mod if ans < 0
  ans
end
```

## Scala

```scala
object Solution {
    def sumDistance(nums: Array[Int], s: String, d: Int): Int = {
        val n = nums.length
        val arr = new Array[Long](n)
        var i = 0
        while (i < n) {
            if (s.charAt(i) == 'L')
                arr(i) = nums(i).toLong - d
            else
                arr(i) = nums(i).toLong + d
            i += 1
        }
        java.util.Arrays.sort(arr)
        val MOD = 1000000007L
        var prefixMod = 0L
        var ans = 0L
        i = 0
        while (i < n) {
            var posMod = arr(i) % MOD
            if (posMod < 0) posMod += MOD
            var contrib = (posMod * i) % MOD
            contrib = (contrib - prefixMod + MOD) % MOD
            ans = (ans + contrib) % MOD
            prefixMod = (prefixMod + posMod) % MOD
            i += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_distance(nums: Vec<i32>, s: String, d: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut pos: Vec<i64> = Vec::with_capacity(n);
        let d_i64 = d as i64;
        let s_bytes = s.as_bytes();
        for i in 0..n {
            let mut p = nums[i] as i64;
            if s_bytes[i] == b'R' {
                p += d_i64;
            } else {
                p -= d_i64;
            }
            pos.push(p);
        }
        pos.sort_unstable();
        let mut prefix: i64 = 0;
        let mut ans: i64 = 0;
        for (i, &val) in pos.iter().enumerate() {
            let i_mod = i as i64 % MOD;
            let val_mod = ((val % MOD) + MOD) % MOD;
            let term = (val_mod * i_mod % MOD - (prefix % MOD) + MOD) % MOD;
            ans += term;
            if ans >= MOD { ans -= MOD; }
            prefix += val;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (sum-distance nums s d)
  (-> (listof exact-integer?) string? exact-integer? exact-integer?)
  (let* ((chars (string->list s))
         (positions
           (for/list ([x nums] [c chars])
             (+ x (if (char=? c #\R) d (- d)))))
         (sorted (sort positions <)))
    (define M 1000000007)
    (let loop ((lst sorted) (i 0) (pref 0) (ans 0))
      (if (null? lst)
          (modulo ans M)
          (let* ((x (car lst))
                 (new-ans (+ ans (- (* x i) pref))))
            (loop (cdr lst) (add1 i) (+ pref x) new-ans))))))
```

## Erlang

```erlang
-spec sum_distance([integer()], binary(), integer()) -> integer().
sum_distance(Nums, S, D) ->
    Mod = 1000000007,
    DirList = binary_to_list(S),
    Positions = [N + case Dir of
                        $R -> D;
                        $L -> -D
                    end || {N, Dir} <- lists:zip(Nums, DirList)],
    Sorted = lists:sort(Positions),
    {_, _, Sum} = lists:foldl(
        fun(X, {Idx, Pref, Acc}) ->
            Contribution = X * Idx - Pref,
            NewAcc = (Acc + Contribution) rem Mod,
            {Idx + 1, Pref + X, NewAcc}
        end,
        {0, 0, 0},
        Sorted),
    (Sum + Mod) rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec sum_distance(nums :: [integer], s :: String.t(), d :: integer) :: integer
  def sum_distance(nums, s, d) do
    mod = 1_000_000_007

    dirs = String.graphemes(s)

    positions =
      Enum.map(Enum.with_index(nums), fn {num, idx} ->
        if Enum.at(dirs, idx) == "R", do: num + d, else: num - d
      end)

    sorted = Enum.sort(positions)

    {_sum_prev, total} =
      Enum.reduce(Enum.with_index(sorted), {0, 0}, fn {a, i}, {sum_prev, acc} ->
        contribution = a * i - sum_prev
        {sum_prev + a, acc + contribution}
      end)

    rem = total % mod
    if rem < 0, do: rem + mod, else: rem
  end
end
```
