# 1814. Count Nice Pairs in an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long revNum(int x) {
        long long r = 0;
        while (x > 0) {
            r = r * 10 + (x % 10);
            x /= 10;
        }
        return r;
    }

    int countNicePairs(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        unordered_map<long long, long long> freq;
        freq.reserve(nums.size() * 2);
        long long ans = 0;
        for (int num : nums) {
            long long diff = (long long)num - revNum(num);
            auto it = freq.find(diff);
            if (it != freq.end()) {
                ans += it->second;
                if (ans >= MOD) ans %= MOD;
                ++(it->second);
            } else {
                freq[diff] = 1;
            }
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    
    public int countNicePairs(int[] nums) {
        java.util.HashMap<Long, Long> freq = new java.util.HashMap<>();
        long ans = 0;
        for (int num : nums) {
            long rev = reverse(num);
            long diff = (long) num - rev;
            long cnt = freq.getOrDefault(diff, 0L);
            ans += cnt;
            if (ans >= MOD) ans -= MOD;
            freq.put(diff, cnt + 1);
        }
        return (int) ans;
    }
    
    private long reverse(int x) {
        long res = 0;
        while (x > 0) {
            res = res * 10 + (x % 10);
            x /= 10;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def rev(x):
            r = 0
            while x:
                r = r * 10 + x % 10
                x //= 10
            return r

        freq = {}
        ans = 0
        for num in nums:
            diff = num - rev(num)
            cnt = freq.get(diff, 0)
            ans = (ans + cnt) % MOD
            freq[diff] = cnt + 1
        return ans
```

## Python3

```python
from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def rev(x: int) -> int:
            r = 0
            while x:
                r = r * 10 + x % 10
                x //= 10
            return r

        freq = {}
        ans = 0
        for num in nums:
            diff = num - rev(num)
            cnt = freq.get(diff, 0)
            ans = (ans + cnt) % MOD
            freq[diff] = cnt + 1
        return ans
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

static long long reverse_num(long long x) {
    long long rev = 0;
    while (x > 0) {
        rev = rev * 10 + (x % 10);
        x /= 10;
    }
    return rev;
}

static int cmp_longlong(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

int countNicePairs(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    long long *diffs = (long long *)malloc(sizeof(long long) * numsSize);
    if (!diffs) return 0; // allocation failure fallback

    for (int i = 0; i < numsSize; ++i) {
        long long val = (long long)nums[i];
        diffs[i] = val - reverse_num(val);
    }

    qsort(diffs, numsSize, sizeof(long long), cmp_longlong);

    long long ans = 0;
    int i = 0;
    while (i < numsSize) {
        int j = i + 1;
        while (j < numsSize && diffs[j] == diffs[i]) ++j;
        long long cnt = j - i;
        ans = (ans + (cnt * (cnt - 1) / 2) % MOD) % MOD;
        i = j;
    }

    free(diffs);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1_000_000_007;
    
    private long Reverse(long x) {
        long rev = 0;
        while (x > 0) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return rev;
    }

    public int CountNicePairs(int[] nums) {
        var freq = new Dictionary<long, long>();
        long ans = 0;
        foreach (int num in nums) {
            long diff = (long)num - Reverse(num);
            if (freq.TryGetValue(diff, out long count)) {
                ans += count;
                if (ans >= MOD) ans %= MOD;
                freq[diff] = count + 1;
            } else {
                freq[diff] = 1;
            }
        }
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countNicePairs = function(nums) {
    const MOD = 1000000007;
    const freq = new Map();
    let ans = 0;

    for (const num of nums) {
        // compute rev(num)
        let x = num, rev = 0;
        while (x > 0) {
            rev = rev * 10 + (x % 10);
            x = Math.floor(x / 10);
        }
        const diff = num - rev;
        const cnt = freq.get(diff) || 0;
        ans = (ans + cnt) % MOD;
        freq.set(diff, cnt + 1);
    }

    return ans;
};
```

## Typescript

```typescript
function countNicePairs(nums: number[]): number {
    const MOD = 1000000007;
    const freq = new Map<number, number>();
    let ans = 0;

    for (const num of nums) {
        // compute rev(num)
        let rev = 0;
        let x = num;
        while (x > 0) {
            rev = rev * 10 + (x % 10);
            x = Math.floor(x / 10);
        }
        const diff = num - rev;
        const cnt = freq.get(diff) ?? 0;
        ans = (ans + cnt) % MOD;
        freq.set(diff, cnt + 1);
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
    function countNicePairs($nums) {
        $mod = 1000000007;
        $freq = [];
        $ans = 0;
        foreach ($nums as $num) {
            $rev = $this->reverseInt($num);
            $key = $num - $rev;
            if (isset($freq[$key])) {
                $ans = ($ans + $freq[$key]) % $mod;
                $freq[$key] += 1;
            } else {
                $freq[$key] = 1;
            }
        }
        return $ans;
    }

    private function reverseInt($x) {
        $rev = 0;
        while ($x > 0) {
            $rev = $rev * 10 + ($x % 10);
            $x = intdiv($x, 10);
        }
        return $rev;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func countNicePairs(_ nums: [Int]) -> Int {
        var freq = [Int: Int]()
        var ans = 0

        for num in nums {
            let revNum = reverse(num)
            let diff = num - revNum
            if let cnt = freq[diff] {
                ans += cnt
                if ans >= MOD { ans -= MOD }
                freq[diff] = cnt + 1
            } else {
                freq[diff] = 1
            }
        }

        return ans % MOD
    }

    private func reverse(_ x: Int) -> Int {
        var n = x
        var rev = 0
        while n > 0 {
            rev = rev * 10 + n % 10
            n /= 10
        }
        return rev
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countNicePairs(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        val freq = HashMap<Long, Long>()
        var ans = 0L
        for (num in nums) {
            val revNum = reverse(num)
            val diff = num.toLong() - revNum.toLong()
            val cnt = freq.getOrDefault(diff, 0L)
            ans = (ans + cnt) % MOD
            freq[diff] = cnt + 1
        }
        return ans.toInt()
    }

    private fun reverse(x: Int): Int {
        var n = x
        var res = 0
        while (n > 0) {
            res = res * 10 + n % 10
            n /= 10
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countNicePairs(List<int> nums) {
    final Map<int, int> freq = {};
    int ans = 0;
    for (final num in nums) {
      final revNum = _reverse(num);
      final key = num - revNum;
      final cnt = freq[key] ?? 0;
      ans += cnt;
      if (ans >= _mod) ans -= _mod;
      freq[key] = cnt + 1;
    }
    return ans % _mod;
  }

  int _reverse(int x) {
    int rev = 0;
    while (x > 0) {
      rev = rev * 10 + x % 10;
      x ~/= 10;
    }
    return rev;
  }
}
```

## Golang

```go
func countNicePairs(nums []int) int {
	const MOD int = 1000000007
	freq := make(map[int]int)
	var ans int64
	for _, v := range nums {
		rv := reverse(v)
		diff := v - rv
		if cnt, ok := freq[diff]; ok {
			ans += int64(cnt)
		}
		freq[diff]++
	}
	return int(ans % int64(MOD))
}

func reverse(x int) int {
	res := 0
	for x > 0 {
		res = res*10 + x%10
		x /= 10
	}
	return res
}
```

## Ruby

```ruby
def count_nice_pairs(nums)
  mod = 1_000_000_007
  freq = Hash.new(0)
  ans = 0

  nums.each do |num|
    rev = 0
    x = num
    while x > 0
      rev = rev * 10 + (x % 10)
      x /= 10
    end
    diff = num - rev
    ans = (ans + freq[diff]) % mod
    freq[diff] += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
  def countNicePairs(nums: Array[Int]): Int = {
    val MOD = 1000000007L
    val freq = scala.collection.mutable.HashMap[Long, Long]()
    var ans = 0L
    for (num <- nums) {
      val revNum = reverse(num)
      val diff = num.toLong - revNum.toLong
      val cnt = freq.getOrElse(diff, 0L)
      ans = (ans + cnt) % MOD
      freq.update(diff, cnt + 1)
    }
    ans.toInt
  }

  private def reverse(x: Int): Int = {
    var n = x
    var res = 0
    while (n > 0) {
      res = res * 10 + n % 10
      n /= 10
    }
    res
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_nice_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut freq: HashMap<i64, i64> = HashMap::new();
        let mut ans: i64 = 0;

        for &num in nums.iter() {
            let rev = Self::rev(num);
            let diff = num as i64 - rev as i64;
            if let Some(&cnt) = freq.get(&diff) {
                ans += cnt;
                if ans >= MOD {
                    ans %= MOD;
                }
            }
            *freq.entry(diff).or_insert(0) += 1;
        }

        (ans % MOD) as i32
    }

    fn rev(mut x: i32) -> i32 {
        let mut res = 0i32;
        while x > 0 {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (rev n)
  (let loop ((x n) (r 0))
    (if (= x 0)
        r
        (loop (quotient x 10) (+ (* r 10) (remainder x 10))))))

(define/contract (count-nice-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((ht (make-hash))
        (ans 0))
    (for ([num nums])
      (let* ((diff (- num (rev num)))
             (cnt (hash-ref ht diff 0)))
        (set! ans (modulo (+ ans cnt) MOD))
        (hash-set! ht diff (+ cnt 1))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_nice_pairs/1]).

-spec count_nice_pairs(Nums :: [integer()]) -> integer().
count_nice_pairs(Nums) ->
    Mod = 1000000007,
    count_nice_pairs(Nums, #{}, 0, Mod).

count_nice_pairs([], _Map, Ans, _Mod) ->
    Ans;
count_nice_pairs([Num|Rest], Map, Ans, Mod) ->
    Rev = rev(Num),
    Diff = Num - Rev,
    Cnt = maps:get(Diff, Map, 0),
    NewAns = (Ans + Cnt) rem Mod,
    NewMap = maps:put(Diff, Cnt + 1, Map),
    count_nice_pairs(Rest, NewMap, NewAns, Mod).

rev(Num) when Num >= 0 ->
    rev_acc(Num, 0).

rev_acc(0, Acc) -> Acc;
rev_acc(N, Acc) ->
    Digit = N rem 10,
    rev_acc(N div 10, Acc * 10 + Digit).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_nice_pairs(nums :: [integer]) :: integer
  def count_nice_pairs(nums) do
    {ans, _} =
      Enum.reduce(nums, {0, %{}}, fn num, {acc, freq} ->
        diff = num - rev(num)
        cnt = Map.get(freq, diff, 0)
        new_acc = rem(acc + cnt, @mod)
        new_freq = Map.update(freq, diff, 1, &(&1 + 1))
        {new_acc, new_freq}
      end)

    ans
  end

  defp rev(0), do: 0
  defp rev(num), do: rev_acc(num, 0)

  defp rev_acc(0, acc), do: acc
  defp rev_acc(n, acc) do
    rev_acc(div(n, 10), acc * 10 + rem(n, 10))
  end
end
```
