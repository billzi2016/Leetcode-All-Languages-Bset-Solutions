# 1819. Number of Different Subsequences GCDs

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        const int MAXV = 200000;
        vector<int> freq(MAXV + 1, 0);
        int maxNum = 0;
        for (int x : nums) {
            ++freq[x];
            if (x > maxNum) maxNum = x;
        }
        int ans = 0;
        for (int g = 1; g <= maxNum; ++g) {
            int curGcd = 0;
            for (int mult = g; mult <= maxNum; mult += g) {
                if (freq[mult]) {
                    if (curGcd == 0) curGcd = mult;
                    else curGcd = std::gcd(curGcd, mult);
                    if (curGcd == g) break; // cannot get lower than g
                }
            }
            if (curGcd == g) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countDifferentSubsequenceGCDs(int[] nums) {
        int max = 0;
        for (int v : nums) {
            if (v > max) max = v;
        }
        int[] freq = new int[max + 1];
        for (int v : nums) {
            freq[v]++;
        }
        int ans = 0;
        for (int g = 1; g <= max; g++) {
            int curGcd = 0;
            for (int multiple = g; multiple <= max; multiple += g) {
                if (freq[multiple] > 0) {
                    curGcd = gcd(curGcd, multiple / g);
                    if (curGcd == 1) break;
                }
            }
            if (curGcd == 1) ans++;
        }
        return ans;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for v in nums:
            freq[v] += 1

        ans = 0
        # iterate possible gcd values
        for g in range(1, max_val + 1):
            cur_gcd = 0
            multiple = g
            while multiple <= max_val:
                if freq[multiple]:
                    cur_gcd = math.gcd(cur_gcd, multiple)
                    if cur_gcd == g:  # early stop, cannot get lower than g
                        # still need to ensure there is at least one multiple,
                        # but we already have since cur_gcd updated from 0.
                        break
                multiple += g
            if cur_gcd == g:
                ans += 1
        return ans
```

## Python3

```python
from typing import List
import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for v in nums:
            freq[v] += 1

        ans = 0
        for g in range(1, max_val + 1):
            cur_gcd = 0
            has = False
            step = g
            m = g
            while m <= max_val:
                if freq[m]:
                    cur_gcd = math.gcd(cur_gcd, m // g)
                    has = True
                    if cur_gcd == 1:
                        break
                m += step
            if has and cur_gcd == 1:
                ans += 1
        return ans
```

## C

```c
#include <string.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int countDifferentSubsequenceGCDs(int* nums, int numsSize) {
    const int LIMIT = 200000;
    static int freq[LIMIT + 1];
    memset(freq, 0, sizeof(freq));

    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        ++freq[v];
        if (v > maxVal) maxVal = v;
    }

    int ans = 0;
    for (int g = 1; g <= maxVal; ++g) {
        int cur = 0;
        for (int m = g; m <= maxVal; m += g) {
            if (freq[m]) {
                if (cur == 0)
                    cur = m;
                else
                    cur = gcd_int(cur, m);
                if (cur == 1) break; // cannot get larger again
            }
        }
        if (cur == g && cur != 0) ++ans;
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountDifferentSubsequenceGCDs(int[] nums)
    {
        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;

        int[] freq = new int[maxVal + 1];
        foreach (int v in nums) freq[v]++;

        int result = 0;
        for (int g = 1; g <= maxVal; g++)
        {
            int curGcd = 0;
            for (int mult = g; mult <= maxVal; mult += g)
            {
                if (freq[mult] > 0)
                {
                    curGcd = GCD(curGcd, mult / g);
                    if (curGcd == 1) break; // early stop
                }
            }
            if (curGcd == 1) result++;
        }

        return result;
    }

    private int GCD(int a, int b)
    {
        while (b != 0)
        {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countDifferentSubsequenceGCDs = function(nums) {
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    const cnt = new Uint32Array(maxVal + 1);
    for (const v of nums) cnt[v]++;

    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let ans = 0;
    for (let g = 1; g <= maxVal; ++g) {
        let cur = 0;
        for (let m = g; m <= maxVal; m += g) {
            if (cnt[m]) {
                cur = cur === 0 ? m : gcd(cur, m);
                if (cur === g) break; // cannot get lower than g
            }
        }
        if (cur === g) ans++;
    }
    return ans;
};
```

## Typescript

```typescript
function countDifferentSubsequenceGCDs(nums: number[]): number {
    let maxVal = 0;
    for (const v of nums) {
        if (v > maxVal) maxVal = v;
    }
    const freq = new Uint32Array(maxVal + 1);
    for (const v of nums) {
        freq[v]++;
    }

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let answer = 0;
    for (let g = 1; g <= maxVal; ++g) {
        let curGcd = 0;
        for (let m = g; m <= maxVal; m += g) {
            if (freq[m] > 0) {
                curGcd = curGcd === 0 ? m : gcd(curGcd, m);
                // early exit: once curGcd equals g it will stay g
                if (curGcd === g) break;
            }
        }
        if (curGcd === g) answer++;
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    public function countDifferentSubsequenceGCDs($nums) {
        $max = max($nums);
        $freq = array_fill(0, $max + 1, 0);
        foreach ($nums as $v) {
            $freq[$v]++;
        }

        $ans = 0;
        for ($g = 1; $g <= $max; $g++) {
            $currentGcd = 0;
            for ($multiple = $g; $multiple <= $max; $multiple += $g) {
                if ($freq[$multiple] > 0) {
                    $currentGcd = $this->gcd($currentGcd, $multiple);
                    if ($currentGcd == $g) {
                        $ans++;
                        break;
                    }
                }
            }
        }

        return $ans;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func countDifferentSubsequenceGCDs(_ nums: [Int]) -> Int {
        guard let maxVal = nums.max(), maxVal > 0 else { return 0 }
        var freq = [Int](repeating: 0, count: maxVal + 1)
        for v in nums {
            freq[v] += 1
        }
        
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a, y = b
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }
        
        var result = 0
        for g in 1...maxVal {
            var curGCD = 0
            var multiple = g
            while multiple <= maxVal {
                if freq[multiple] > 0 {
                    if curGCD == 0 {
                        curGCD = multiple
                    } else {
                        curGCD = gcd(curGCD, multiple)
                    }
                    if curGCD == g { break }
                }
                multiple += g
            }
            if curGCD == g {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countDifferentSubsequenceGCDs(nums: IntArray): Int {
        var maxNum = 0
        val limit = 200000
        val freq = IntArray(limit + 1)
        for (v in nums) {
            freq[v]++
            if (v > maxNum) maxNum = v
        }
        fun gcd(a: Int, b: Int): Int {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            return x
        }
        var ans = 0
        for (g in 1..maxNum) {
            var cur = 0
            var m = g
            while (m <= maxNum) {
                if (freq[m] > 0) {
                    cur = if (cur == 0) m else gcd(cur, m)
                    if (cur == g) break
                }
                m += g
            }
            if (cur == g) ans++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countDifferentSubsequenceGCDs(List<int> nums) {
    int maxVal = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }
    List<int> freq = List.filled(maxVal + 1, 0);
    for (int v in nums) {
      freq[v]++;
    }

    int gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a;
    }

    int result = 0;
    for (int g = 1; g <= maxVal; ++g) {
      int cur = 0;
      for (int m = g; m <= maxVal; m += g) {
        if (freq[m] > 0) {
          if (cur == 0) {
            cur = m;
          } else {
            cur = gcd(cur, m);
          }
        }
      }
      if (cur == g) result++;
    }

    return result;
  }
}
```

## Golang

```go
func countDifferentSubsequenceGCDs(nums []int) int {
	maxVal := 0
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}
	freq := make([]int, maxVal+1)
	for _, v := range nums {
		freq[v]++
	}
	ans := 0
	for g := 1; g <= maxVal; g++ {
		cur := 0
		for m := g; m <= maxVal; m += g {
			if freq[m] > 0 {
				if cur == 0 {
					cur = m
				} else {
					cur = gcd(cur, m)
				}
				if cur == g { // further multiples won't change the gcd
					// continue scanning to ensure there is at least one multiple,
					// but we can break early for speed
					break
				}
			}
		}
		if cur == g && cur != 0 {
			ans++
		}
	}
	return ans
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
```

## Ruby

```ruby
def count_different_subsequence_gc_ds(nums)
  max_val = nums.max
  freq = Array.new(max_val + 1, 0)
  nums.each { |v| freq[v] += 1 }

  ans = 0
  (1..max_val).each do |g|
    cur = 0
    m = g
    while m <= max_val
      if freq[m] > 0
        cur = cur.gcd(m)
      end
      m += g
    end
    ans += 1 if cur == g
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countDifferentSubsequenceGCDs(nums: Array[Int]): Int = {
        val maxVal = 200000
        val present = new Array[Boolean](maxVal + 1)
        var maxNum = 0
        for (v <- nums) {
            present(v) = true
            if (v > maxNum) maxNum = v
        }

        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            x
        }

        var answer = 0
        for (g <- 1 to maxNum) {
            var cur = 0
            var mult = g
            while (mult <= maxNum) {
                if (present(mult)) {
                    if (cur == 0) cur = mult
                    else cur = gcd(cur, mult)
                }
                mult += g
            }
            if (cur == g && cur != 0) answer += 1
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_different_subsequence_gc_ds(nums: Vec<i32>) -> i32 {
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut cnt = vec![0i32; max_val + 1];
        for &v in nums.iter() {
            cnt[v as usize] += 1;
        }
        fn gcd(mut a: usize, mut b: usize) -> usize {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut ans = 0i32;
        for g in 1..=max_val {
            let mut cur_gcd = 0usize;
            let mut m = g;
            while m <= max_val {
                if cnt[m] > 0 {
                    if cur_gcd == 0 {
                        cur_gcd = m;
                    } else {
                        cur_gcd = gcd(cur_gcd, m);
                    }
                    if cur_gcd == g {
                        // cannot get smaller than g, break early
                        // but continue to skip remaining multiples for speed
                        // (optional)
                    }
                }
                m += g;
            }
            if cur_gcd == g {
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-different-subsequence-gc-ds nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let* ((maxA (apply max nums))
             (cnt (make-vector (+ maxA 1) 0)))
        ;; count frequencies
        (for ([v nums])
          (vector-set! cnt v (+ 1 (vector-ref cnt v))))
        (let ((ans 0))
          (for ([g (in-range 1 (+ maxA 1))])
            (let ((cur 0))
              (for ([m (in-range g (+ maxA 1) g)])
                (when (> (vector-ref cnt m) 0)
                  (set! cur (gcd cur m))))
              (when (= cur g)
                (set! ans (+ ans 1)))))
          ans))))
```

## Erlang

```erlang
-module(solution).
-export([count_different_subsequence_gc_ds/1]).

count_different_subsequence_gc_ds(Nums) ->
    Max = lists:max(Nums),
    FreqMap = build_freq(Nums, #{}),
    count_gcds(1, Max, FreqMap, 0).

build_freq([], Acc) -> Acc;
build_freq([H|T], Acc) ->
    NewAcc = maps:update_with(H,
                               fun(C) -> C + 1 end,
                               1,
                               Acc),
    build_freq(T, NewAcc).

count_gcds(G, Max, _Map, Count) when G > Max ->
    Count;
count_gcds(G, Max, Map, Count) ->
    CurGcd = find_gcd_multiple(G, Max, Map, 0),
    NewCount = if CurGcd == G -> Count + 1; true -> Count end,
    count_gcds(G + 1, Max, Map, NewCount).

find_gcd_multiple(G, Max, Map, Acc) ->
    find_gcd_multiple_step(G, G, Max, Map, Acc).

find_gcd_multiple_step(_G, M, Max, _Map, Acc) when M > Max ->
    Acc;
find_gcd_multiple_step(G, M, Max, Map, Acc) ->
    case maps:get(M, Map, 0) of
        0 -> find_gcd_multiple_step(G, M + G, Max, Map, Acc);
        _ -> NewAcc = gcd(Acc, M),
             find_gcd_multiple_step(G, M + G, Max, Map, NewAcc)
    end.

gcd(0, B) -> B;
gcd(A, 0) -> A;
gcd(A, B) when A < B ->
    gcd(B, A);
gcd(A, B) ->
    case A rem B of
        0 -> B;
        R -> gcd(B, R)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_different_subsequence_gc_ds(nums :: [integer]) :: integer
  def count_different_subsequence_gc_ds(nums) do
    max_val = Enum.max(nums)

    freq =
      :array.new(max_val + 1, default: 0)
      |> Enum.reduce(nums, fn x, acc -> :array.set(x, 1, acc) end)

    1..max_val
    |> Enum.reduce(0, fn g, ans ->
      cur_gcd =
        1..div(max_val, g)
        |> Enum.reduce(0, fn k, cg ->
          m = k * g

          if :array.get(m, freq) == 1 do
            Integer.gcd(cg, m)
          else
            cg
          end
        end)

      if cur_gcd == g and cur_gcd != 0 do
        ans + 1
      else
        ans
      end
    end)
  end
end
```
