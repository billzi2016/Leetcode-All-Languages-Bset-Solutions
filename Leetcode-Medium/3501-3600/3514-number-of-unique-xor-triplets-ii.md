# 3514. Number of Unique XOR Triplets II

## Cpp

```cpp
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        const int MAX_XOR = 2048; // since nums[i] <= 1500 < 2^11
        static bool dp[4][MAX_XOR];
        for (int t = 0; t <= 3; ++t)
            fill(dp[t], dp[t] + MAX_XOR, false);
        dp[0][0] = true;
        for (int x : nums) {
            for (int t = 2; t >= 0; --t) {
                for (int v = 0; v < MAX_XOR; ++v) {
                    if (dp[t][v]) {
                        dp[t + 1][v ^ x] = true;
                    }
                }
            }
        }
        bool seen[MAX_XOR] = {false};
        int ans = 0;
        for (int t = 1; t <= 3; ++t) {
            for (int v = 0; v < MAX_XOR; ++v) {
                if (dp[t][v] && !seen[v]) {
                    seen[v] = true;
                    ++ans;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        final int MAX = 2048; // since nums[i] <= 1500 < 2^11
        boolean[] pairXor = new boolean[MAX];
        boolean[] result = new boolean[MAX];
        int n = nums.length;
        for (int i = n - 1; i >= 0; --i) {
            int vi = nums[i];
            // add pairs where the first index is i
            for (int k = i; k < n; ++k) {
                pairXor[vi ^ nums[k]] = true;
            }
            // combine current element with all existing pair XORs
            for (int v = 0; v < MAX; ++v) {
                if (pairXor[v]) {
                    result[vi ^ v] = true;
                }
            }
        }
        int count = 0;
        for (boolean b : result) {
            if (b) count++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maximum possible xor value given constraints (nums[i] <= 1500 < 2^11)
        SIZE = 1 << 11  # 2048
        
        a = [0] * SIZE
        for v in nums:
            a[v] = 1

        def fwht(arr):
            n = len(arr)
            step = 1
            while step < n:
                for i in range(0, n, step << 1):
                    for j in range(i, i + step):
                        x = arr[j]
                        y = arr[j + step]
                        arr[j] = x + y
                        arr[j + step] = x - y
                step <<= 1

        # forward transform
        fwht(a)
        # pointwise cube (ordered triples)
        for i in range(SIZE):
            a[i] = a[i] * a[i] * a[i]
        # inverse transform (same as forward) and normalize
        fwht(a)
        for i in range(SIZE):
            a[i] //= SIZE

        # count distinct xor values reachable by some ordered triple
        cnt = 0
        for val in a:
            if val > 0:
                cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def uniqueXorTriplets(self, nums):
        distinct = list(set(nums))
        MAX = 2048  # since nums[i] <= 1500 < 2^11
        dp = [False] * MAX
        dp[0] = True
        for _ in range(3):
            ndp = [False] * MAX
            for x, ok in enumerate(dp):
                if not ok:
                    continue
                for v in distinct:
                    ndp[x ^ v] = True
            dp = ndp
        return sum(dp)
```

## C

```c
#include <string.h>

static void fwht(long long *a, int n, int inverse) {
    for (int len = 1; len < n; len <<= 1) {
        for (int i = 0; i < n; i += len << 1) {
            for (int j = 0; j < len; ++j) {
                long long u = a[i + j];
                long long v = a[i + j + len];
                a[i + j] = u + v;
                a[i + j + len] = u - v;
            }
        }
    }
    if (inverse) {
        for (int i = 0; i < n; ++i) a[i] /= n;
    }
}

int uniqueXorTriplets(int* nums, int numsSize) {
    const int SZ = 2048;               // 2^11 > 1500
    static long long f[SZ];
    memset(f, 0, sizeof(f));
    for (int i = 0; i < numsSize; ++i) f[nums[i]]++;

    fwht(f, SZ, 0);
    for (int i = 0; i < SZ; ++i) f[i] = f[i] * f[i] * f[i];
    fwht(f, SZ, 1);

    int ans = 0;
    for (int i = 0; i < SZ; ++i)
        if (f[i] > 0) ++ans;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int UniqueXorTriplets(int[] nums) {
        const int MAX = 2048; // since nums[i] <= 1500, xor fits in 11 bits
        bool[] possible = new bool[MAX];
        foreach (int x in nums) possible[x] = true;

        bool[] pairPossible = new bool[MAX];
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int v = nums[i] ^ nums[j];
                pairPossible[v] = true;
            }
        }

        for (int p = 0; p < MAX; p++) {
            if (!pairPossible[p]) continue;
            foreach (int x in nums) {
                possible[p ^ x] = true;
            }
        }

        int count = 0;
        for (int i = 0; i < MAX; i++) {
            if (possible[i]) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var uniqueXorTriplets = function(nums) {
    // maximum possible xor value for numbers <= 1500 is < 2048 (2^11)
    const MAX_VAL = 2048;
    let size = 1;
    while (size <= MAX_VAL) size <<= 1; // power of two >= 2049, e.g., 4096

    const a = new Array(size).fill(0);
    for (const v of nums) {
        a[v] = 1; // presence
    }

    // Fast Walsh-Hadamard Transform for XOR convolution
    function fwht(arr, invert) {
        for (let len = 1; len < arr.length; len <<= 1) {
            for (let i = 0; i < arr.length; i += len << 1) {
                for (let j = 0; j < len; ++j) {
                    const u = arr[i + j];
                    const v = arr[i + j + len];
                    arr[i + j] = u + v;
                    arr[i + j + len] = u - v;
                }
            }
        }
        if (invert) {
            for (let i = 0; i < arr.length; ++i) {
                arr[i] /= arr.length;
            }
        }
    }

    fwht(a, false);
    // cube each component to get convolution of three copies
    for (let i = 0; i < a.length; ++i) {
        const x = a[i];
        a[i] = x * x * x;
    }
    fwht(a, true);

    let count = 0;
    for (let i = 0; i < MAX_VAL; ++i) { // only values up to 2047 are possible
        if (Math.round(a[i]) > 0) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function uniqueXorTriplets(nums: number[]): number {
    const MAX_XOR = 1 << 12; // 4096, enough for values up to 1500
    const n = nums.length;
    const pairXor = new Uint8Array(MAX_XOR);
    const resultXor = new Uint8Array(MAX_XOR);

    for (let k = 0; k < n; ++k) {
        // add all pairs (i, k) where i <= k
        const valK = nums[k];
        for (let i = 0; i <= k; ++i) {
            const x = nums[i] ^ valK;
            pairXor[x] = 1;
        }
        // combine each existing pair xor with the third element at index k
        for (let v = 0; v < MAX_XOR; ++v) {
            if (pairXor[v]) {
                resultXor[v ^ valK] = 1;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < MAX_XOR; ++i) {
        if (resultXor[i]) ++count;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function uniqueXorTriplets($nums) {
        $MAX = 2048; // since nums[i] <= 1500, xor fits in 11 bits
        $present = array_fill(0, $MAX, false);
        foreach ($nums as $v) {
            $present[$v] = true;
        }

        // XOR of any two (with repetitions allowed)
        $pairXor = array_fill(0, $MAX, false);
        for ($a = 0; $a < $MAX; $a++) {
            if (!$present[$a]) continue;
            for ($b = $a; $b < $MAX; $b++) { // a <= b to avoid duplicate work
                if (!$present[$b]) continue;
                $pairXor[$a ^ $b] = true;
            }
        }

        // XOR of three numbers: (xor of two) xor third
        $final = array_fill(0, $MAX, false);
        for ($x = 0; $x < $MAX; $x++) {
            if (!$pairXor[$x]) continue;
            for ($c = 0; $c < $MAX; $c++) {
                if (!$present[$c]) continue;
                $final[$x ^ $c] = true;
            }
        }

        $count = 0;
        foreach ($final as $v) {
            if ($v) $count++;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func uniqueXorTriplets(_ nums: [Int]) -> Int {
        var distinct = Set<Int>()
        for v in nums { distinct.insert(v) }
        let vals = Array(distinct)
        let m = vals.count
        
        var pairSet = Set<Int>()
        for i in 0..<m {
            for j in i..<m {
                pairSet.insert(vals[i] ^ vals[j])
            }
        }
        
        var result = Set<Int>()
        for p in pairSet {
            for v in vals {
                result.insert(p ^ v)
            }
        }
        return result.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        val MAX_XOR = 2048 // since nums[i] <= 1500, max xor < 2^11
        val pairXor = BooleanArray(MAX_XOR)
        val result = BooleanArray(MAX_XOR)

        val n = nums.size
        for (i in n - 1 downTo 0) {
            var j = i
            while (j < n) {
                val x = nums[i] xor nums[j]
                pairXor[x] = true
                j++
            }
            for (p in 0 until MAX_XOR) {
                if (pairXor[p]) {
                    result[nums[i] xor p] = true
                }
            }
        }

        var count = 0
        for (b in result) if (b) count++
        return count
    }
}
```

## Dart

```dart
class Solution {
  int uniqueXorTriplets(List<int> nums) {
    const int LIMIT = 2048;
    List<bool> reachable = List.filled(LIMIT, false);
    for (int v in nums) {
      reachable[v] = true;
    }

    // Compute all possible XORs of two elements (with repetition)
    List<bool> twoSeen = List.filled(LIMIT, false);
    List<int> twoVals = [];
    int n = nums.length;
    for (int i = 0; i < n; ++i) {
      int a = nums[i];
      for (int j = 0; j < n; ++j) {
        int x = a ^ nums[j];
        if (!twoSeen[x]) {
          twoSeen[x] = true;
          twoVals.add(x);
        }
      }
    }

    // Combine each two‑element XOR with a third element
    for (int val in twoVals) {
      for (int v in nums) {
        reachable[val ^ v] = true;
      }
    }

    int count = 0;
    for (bool b in reachable) {
      if (b) ++count;
    }
    return count;
  }
}
```

## Golang

```go
func uniqueXorTriplets(nums []int) int {
	const maxVal = 2048 // 2^11, enough for values up to 1500 and their XORs
	n := maxVal

	// frequency array
	f := make([]int64, n)
	for _, v := range nums {
		f[v]++
	}

	// FWHT (XOR) transform
	fwht := func(a []int64, invert bool) {
		for step := 1; step < n; step <<= 1 {
			for i := 0; i < n; i += step << 1 {
				for j := 0; j < step; j++ {
					u := a[i+j]
					v := a[i+j+step]
					a[i+j] = u + v
					a[i+j+step] = u - v
				}
			}
		}
		if invert {
			for i := 0; i < n; i++ {
				a[i] /= int64(n)
			}
		}
	}

	// h = f xor-convolution f (ordered pairs)
	h := make([]int64, n)
	copy(h, f)
	fwht(h, false)
	for i := 0; i < n; i++ {
		h[i] *= h[i]
	}
	fwht(h, true)

	// totalWays = h xor-convolution f (ordered triples)
	total := make([]int64, n)
	copy(total, h)
	fwht(total, false)

	tmp := make([]int64, n)
	copy(tmp, f)
	fwht(tmp, false)

	for i := 0; i < n; i++ {
		total[i] *= tmp[i]
	}
	fwht(total, true)

	// count distinct XOR values achievable
	cnt := 0
	for i := 0; i < n; i++ {
		if total[i] > 0 {
			cnt++
		}
	}
	return cnt
}
```

## Ruby

```ruby
def unique_xor_triplets(nums)
  max_val = 1 << 11
  present = Array.new(max_val, false)
  nums.each { |v| present[v] = true }

  distinct = []
  present.each_with_index { |p, i| distinct << i if p }

  # xor of any two (with repetitions)
  set2 = Array.new(max_val, false)
  d_len = distinct.length
  (0...d_len).each do |i|
    a = distinct[i]
    (i...d_len).each do |j|
      b = distinct[j]
      x = a ^ b
      set2[x] = true
    end
  end

  y_vals = []
  set2.each_index { |i| y_vals << i if set2[i] }

  possible = Array.new(max_val, false)
  distinct.each do |c|
    y_vals.each { |y| possible[c ^ y] = true }
  end

  possible.count(true)
end
```

## Scala

```scala
object Solution {
    def uniqueXorTriplets(nums: Array[Int]): Int = {
        val MAX = 2048 // sufficient for values up to 1500 (2^11)
        val pairPossible = new Array[Boolean](MAX)

        val n = nums.length
        var i = 0
        while (i < n) {
            var j = i
            while (j < n) {
                val x = nums(i) ^ nums(j)
                pairPossible(x) = true
                j += 1
            }
            i += 1
        }

        val result = new Array[Boolean](MAX)

        var idx = 0
        while (idx < n) {
            val c = nums(idx)
            var p = 0
            while (p < MAX) {
                if (pairPossible(p)) {
                    result(p ^ c) = true
                }
                p += 1
            }
            idx += 1
        }

        var cnt = 0
        var v = 0
        while (v < MAX) {
            if (result(v)) cnt += 1
            v += 1
        }
        cnt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        const MAX_VAL: usize = 1500;
        const MAX_XOR: usize = 2048; // 2^11, enough for values up to 1500

        let mut present = [false; MAX_VAL + 1];
        for &num in &nums {
            present[num as usize] = true;
        }
        let vals: Vec<usize> = (0..=MAX_VAL)
            .filter(|&i| present[i])
            .collect();

        // dp[t][x] = can achieve xor x using exactly t elements
        let mut dp = [[false; MAX_XOR]; 4];
        dp[0][0] = true;

        for _ in 0..3 {
            let mut ndp = dp;
            for t in 0..=2 {
                for x in 0..MAX_XOR {
                    if dp[t][x] {
                        for &v in &vals {
                            let nx = x ^ v;
                            ndp[t + 1][nx] = true;
                        }
                    }
                }
            }
            dp = ndp;
        }

        let mut count = 0;
        for x in 0..MAX_XOR {
            if dp[3][x] {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(require racket/vector)

(define/contract (unique-xor-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-val (apply max nums))
         (size (bitwise-ior max-val max-val) ; ensure at least max element bits
               )
         ;; Since nums[i] ≤ 1500, xor of three numbers fits in 11 bits → 2048 possibilities.
         (limit 2048)
         (pair (make-vector limit #f))
         (result (make-vector limit #f)))
    ;; compute all pair xors
    (for* ([i nums] [j nums])
      (vector-set! pair (bitwise-xor i j) #t))
    ;; compute triple xors and count unique values
    (let ((cnt 0))
      (for ([a nums])
        (for ([v (in-range limit)])
          (when (vector-ref pair v)
            (define val (bitwise-xor a v))
            (unless (vector-ref result val)
              (vector-set! result val #t)
              (set! cnt (+ cnt 1))))))
      cnt)))
```

## Erlang

```erlang
-spec unique_xor_triplets([integer()]) -> integer().
unique_xor_triplets(Nums) ->
    Cur0 = #{0 => true},
    Result0 = #{},
    {Result,_} = lists:foldl(fun(_Step, {Res, Cur}) ->
        Next = compute_next(Cur, Nums),
        Res1 = maps:merge(Res, Next),
        {Res1, Next}
    end, {Result0, Cur0}, [1,2,3]),
    maps:size(Result).

compute_next(Cur, Nums) ->
    lists:foldl(fun({Val,_}, Acc) ->
        lists:foldl(fun(A, Aacc) ->
            X = Val bxor A,
            maps:put(X, true, Aacc)
        end, Acc, Nums)
    end, #{}, maps:to_list(Cur)).
```

## Elixir

```elixir
defmodule Solution do
  @spec unique_xor_triplets(nums :: [integer]) :: integer
  def unique_xor_triplets(nums) do
    require Bitwise

    {_pair_set, result_set, _suffix_vals} =
      Enum.reduce(Enum.reverse(nums), {MapSet.new(), MapSet.new(), []},
        fn val, {pair_set, res_set, suffix_vals} ->
          # add new pair XORs involving current value and all suffix values
          pair_set =
            Enum.reduce(suffix_vals, pair_set, fn v, acc ->
              MapSet.put(acc, Bitwise.bxor(val, v))
            end)

          # pair (val, val) gives xor 0
          pair_set = MapSet.put(pair_set, 0)

          # update result set with XOR of current value and each possible pair xor
          res_set =
            Enum.reduce(pair_set, res_set, fn p, acc ->
              MapSet.put(acc, Bitwise.bxor(val, p))
            end)

          {pair_set, res_set, [val | suffix_vals]}
        end)

    MapSet.size(result_set)
  end
end
```
