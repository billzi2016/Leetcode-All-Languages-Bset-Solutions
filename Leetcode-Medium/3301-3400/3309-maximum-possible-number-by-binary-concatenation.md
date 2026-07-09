# 3309. Maximum Possible Number by Binary Concatenation

## Cpp

```cpp
class Solution {
public:
    int maxGoodNumber(vector<int>& nums) {
        auto bitlen = [](int x) { return 32 - __builtin_clz(x); };
        vector<int> v = nums;
        sort(v.begin(), v.end());
        long long best = 0;
        do {
            long long cur = v[0];
            cur = (cur << bitlen(v[1])) | v[1];
            cur = (cur << bitlen(v[2])) | v[2];
            if (cur > best) best = cur;
        } while (next_permutation(v.begin(), v.end()));
        return static_cast<int>(best);
    }
};
```

## Java

```java
class Solution {
    public int maxGoodNumber(int[] nums) {
        int n = nums.length;
        int max = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) if (j != i) {
                for (int k = 0; k < n; k++) if (k != i && k != j) {
                    int a = nums[i];
                    int b = nums[j];
                    int c = nums[k];
                    int lenB = bitLength(b);
                    int lenC = bitLength(c);
                    int val = (a << (lenB + lenC)) | (b << lenC) | c;
                    if (val > max) {
                        max = val;
                    }
                }
            }
        }
        return max;
    }

    private int bitLength(int x) {
        return 32 - Integer.numberOfLeadingZeros(x);
    }
}
```

## Python

```python
class Solution(object):
    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        max_val = 0
        for perm in itertools.permutations(nums):
            val = 0
            for x in perm:
                l = x.bit_length()
                val = (val << l) | x
            if val > max_val:
                max_val = val
        return max_val
```

## Python3

```python
import itertools
from typing import List

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        best = 0
        for perm in itertools.permutations(nums):
            val = 0
            for x in perm:
                val = (val << x.bit_length()) | x
            if val > best:
                best = val
        return best
```

## C

```c
int bitlen(int x){
    int l = 0;
    while (x){
        l++;
        x >>= 1;
    }
    return l;
}

int maxGoodNumber(int* nums, int numsSize){
    int best = 0;
    for (int i = 0; i < 3; ++i){
        for (int j = 0; j < 3; ++j) if (j != i){
            for (int k = 0; k < 3; ++k) if (k != i && k != j){
                long long cur = 0;
                int len = bitlen(nums[i]);
                cur = (cur << len) | nums[i];
                len = bitlen(nums[j]);
                cur = (cur << len) | nums[j];
                len = bitlen(nums[k]);
                cur = (cur << len) | nums[k];
                if (cur > best) best = (int)cur;
            }
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxGoodNumber(int[] nums) {
        int max = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (j == i) continue;
                int k = 3 - i - j; // the remaining index
                int val = Concatenate(nums[i], nums[j], nums[k]);
                if (val > max) max = val;
            }
        }
        return max;
    }

    private int BitLen(int x) {
        int len = 0;
        while (x > 0) {
            len++;
            x >>= 1;
        }
        return len;
    }

    private int Concatenate(int a, int b, int c) {
        int lenB = BitLen(b);
        int lenC = BitLen(c);
        return (a << (lenB + lenC)) | (b << lenC) | c;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxGoodNumber = function(nums) {
    const bins = nums.map(n => n.toString(2));
    const perms = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0]
    ];
    let max = 0;
    for (const p of perms) {
        const s = bins[p[0]] + bins[p[1]] + bins[p[2]];
        const val = parseInt(s, 2);
        if (val > max) max = val;
    }
    return max;
};
```

## Typescript

```typescript
function maxGoodNumber(nums: number[]): number {
    const bitLen = (x: number): number => 32 - Math.clz32(x);
    let best = 0;
    const perms = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0]
    ];
    for (const p of perms) {
        let val = 0;
        for (const idx of p) {
            const n = nums[idx];
            val = (val << bitLen(n)) + n;
        }
        if (val > best) best = val;
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxGoodNumber($nums) {
        // helper to get bit length of a positive integer
        $bitlen = function ($x) {
            $len = 0;
            while ($x > 0) {
                $len++;
                $x >>= 1;
            }
            return $len;
        };

        $permutations = [
            [$nums[0], $nums[1], $nums[2]],
            [$nums[0], $nums[2], $nums[1]],
            [$nums[1], $nums[0], $nums[2]],
            [$nums[1], $nums[2], $nums[0]],
            [$nums[2], $nums[0], $nums[1]],
            [$nums[2], $nums[1], $nums[0]],
        ];

        $max = 0;
        foreach ($permutations as $order) {
            $value = 0;
            foreach ($order as $num) {
                $len = $bitlen($num);
                $value = ($value << $len) | $num;
            }
            if ($value > $max) {
                $max = $value;
            }
        }

        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxGoodNumber(_ nums: [Int]) -> Int {
        func bitLength(_ x: Int) -> Int {
            var v = x
            var cnt = 0
            while v > 0 {
                cnt += 1
                v >>= 1
            }
            return cnt
        }

        let n = nums
        var maxVal = 0

        for i in 0..<3 {
            for j in 0..<3 where j != i {
                for k in 0..<3 where k != i && k != j {
                    let a = n[i]
                    let b = n[j]
                    let c = n[k]

                    let lenB = bitLength(b)
                    let lenC = bitLength(c)

                    var val = a
                    val = (val << lenB) | b
                    val = (val << lenC) | c

                    if val > maxVal {
                        maxVal = val
                    }
                }
            }
        }

        return maxVal
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxGoodNumber(nums: IntArray): Int {
        fun bitLen(x: Int): Int = 32 - Integer.numberOfLeadingZeros(x)
        var best = 0
        for (i in 0..2) {
            for (j in 0..2) {
                if (j == i) continue
                val k = 3 - i - j
                val a = nums[i]
                val b = nums[j]
                val c = nums[k]
                var value = ((a shl bitLen(b)) or b)
                value = (value shl bitLen(c)) or c
                if (value > best) best = value
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxGoodNumber(List<int> nums) {
    int n = nums.length;
    int best = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (j == i) continue;
        for (int k = 0; k < n; ++k) {
          if (k == i || k == j) continue;
          int res = 0;
          // first number
          res = (res << nums[i].bitLength) | nums[i];
          // second number
          res = (res << nums[j].bitLength) | nums[j];
          // third number
          res = (res << nums[k].bitLength) | nums[k];
          if (res > best) best = res;
        }
      }
    }
    return best;
  }
}
```

## Golang

```go
func maxGoodNumber(nums []int) int {
	if len(nums) != 3 {
		return 0
	}
	bitLen := func(x int) int {
		cnt := 0
		for x > 0 {
			cnt++
			x >>= 1
		}
		return cnt
	}
	perms := [][]int{
		{0, 1, 2},
		{0, 2, 1},
		{1, 0, 2},
		{1, 2, 0},
		{2, 0, 1},
		{2, 1, 0},
	}
	maxVal := 0
	for _, p := range perms {
		a, b, c := nums[p[0]], nums[p[1]], nums[p[2]]
		val := a
		val = (val << bitLen(b)) | b
		val = (val << bitLen(c)) | c
		if val > maxVal {
			maxVal = val
		}
	}
	return maxVal
}
```

## Ruby

```ruby
def max_good_number(nums)
  max_val = 0
  nums.permutation do |perm|
    cur = 0
    perm.each do |x|
      bits = x.bit_length
      cur = (cur << bits) + x
    end
    max_val = cur if cur > max_val
  end
  max_val
end
```

## Scala

```scala
object Solution {
    def maxGoodNumber(nums: Array[Int]): Int = {
        var best = 0
        val seq = nums.toSeq
        for (perm <- seq.permutations) {
            var value = 0
            for (num <- perm) {
                val bits = 32 - Integer.numberOfLeadingZeros(num)
                value = (value << bits) | num
            }
            if (value > best) best = value
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_good_number(nums: Vec<i32>) -> i32 {
        let mut best: i64 = 0;
        for a in 0..3 {
            for b in 0..3 {
                if b == a { continue; }
                for c in 0..3 {
                    if c == a || c == b { continue; }
                    let order = [nums[a], nums[b], nums[c]];
                    let mut cur: i64 = 0;
                    for &v in order.iter() {
                        let len = (32 - (v as u32).leading_zeros()) as i64;
                        cur = (cur << len) | v as i64;
                    }
                    if cur > best { best = cur; }
                }
            }
        }
        best as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/list)

(define/contract (max-good-number nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((perms (permutations nums))
         (best
          (foldl
           (lambda (perm acc)
             (let* ((bin-str (apply string-append (map (lambda (n) (number->string n 2)) perm)))
                    (val (string->number bin-str 2)))
               (if (> val acc) val acc)))
           0
           perms)))
    best))
```

## Erlang

```erlang
-module(solution).
-export([max_good_number/1]).

-spec max_good_number(Nums :: [integer()]) -> integer().
max_good_number(Nums) ->
    Perms = perm(Nums),
    Values = [value(P) || P <- Perms],
    lists:max(Values).

perm([]) -> [[]];
perm(L) ->
    [ [H|T] ||
        H <- L,
        T <- perm(lists:delete(H, L))
    ].

value(List) -> value(List, 0).

value([], Acc) -> Acc;
value([N|Rest], Acc) ->
    Len = bits_len(N),
    NewAcc = (Acc bsl Len) bor N,
    value(Rest, NewAcc).

bits_len(N) -> bits_len(N, 0).

bits_len(0, Acc) -> Acc;
bits_len(N, Acc) -> bits_len(N bsr 1, Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec max_good_number(nums :: [integer]) :: integer
  def max_good_number(nums) do
    Enum.reduce(Enum.permutations(nums), 0, fn [a, b, c], acc ->
      len_b = bit_len(b)
      len_c = bit_len(c)

      val = (a <<< (len_b + len_c)) ||| (b <<< len_c) ||| c

      if val > acc, do: val, else: acc
    end)
  end

  defp bit_len(n) do
    :math.log2(n) |> trunc() + 1
  end
end
```
