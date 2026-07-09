# 2183. Count Array Pairs Divisible by K

## Cpp

```cpp
class Solution {
public:
    long long countPairs(vector<int>& nums, int k) {
        // compute all divisors of k
        vector<int> divs;
        for (int i = 1; i * 1LL * i <= k; ++i) {
            if (k % i == 0) {
                divs.push_back(i);
                if (i != k / i) divs.push_back(k / i);
            }
        }
        // map divisor to its index
        unordered_map<int, int> idx;
        for (int i = 0; i < (int)divs.size(); ++i) {
            idx[divs[i]] = i;
        }
        vector<long long> cnt(divs.size(), 0);
        long long ans = 0;
        for (int num : nums) {
            int g = std::gcd(num, k); // divisor of k
            for (int d : divs) {
                if ((1LL * g * d) % k == 0) {
                    ans += cnt[idx[d]];
                }
            }
            cnt[idx[g]]++;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long countPairs(int[] nums, int k) {
        // compute all divisors of k
        List<Integer> divList = new ArrayList<>();
        for (int d = 1; d * (long)d <= k; ++d) {
            if (k % d == 0) {
                divList.add(d);
                if (d != k / d) divList.add(k / d);
            }
        }
        // map divisor value to its index in array
        int m = divList.size();
        Map<Integer, Integer> idxMap = new HashMap<>(m * 2);
        for (int i = 0; i < m; ++i) {
            idxMap.put(divList.get(i), i);
        }
        long[] cnt = new long[m];
        long ans = 0L;
        for (int num : nums) {
            int g = gcd(num, k);
            int need = k / g; // divisor of k
            Integer needIdx = idxMap.get(need);
            if (needIdx != null) {
                ans += cnt[needIdx];
            }
            // update counts for divisors that divide num
            for (int d : divList) {
                if (num % d == 0) {
                    int id = idxMap.get(d);
                    cnt[id]++;
                }
            }
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
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import math
        freq = {}
        for num in nums:
            g = math.gcd(num, k)
            freq[g] = freq.get(g, 0) + 1

        divisors = list(freq.keys())
        ans = 0
        m = len(divisors)
        for i in range(m):
            d1 = divisors[i]
            f1 = freq[d1]
            # pairs with itself
            if (d1 * d1) % k == 0:
                ans += f1 * (f1 - 1) // 2
            for j in range(i + 1, m):
                d2 = divisors[j]
                if (d1 * d2) % k == 0:
                    ans += f1 * freq[d2]
        return ans
```

## Python3

```python
import math
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # all divisors of k
        divs = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                divs.append(i)
                if i != k // i:
                    divs.append(k // i)
            i += 1

        cnt = {d: 0 for d in divs}
        ans = 0
        for num in nums:
            g = math.gcd(num, k)
            need = k // g
            ans += cnt.get(need, 0)

            for d in divs:
                if num % d == 0:
                    cnt[d] += 1

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

/* LeetCode function */
long long countPairs(int* nums, int numsSize, int k) {
    // collect divisors of k
    int divs[256];
    int dcnt = 0;
    for (int i = 1; i * (long long)i <= k; ++i) {
        if (k % i == 0) {
            divs[dcnt++] = i;
            if (i != k / i) {
                divs[dcnt++] = k / i;
            }
        }
    }
    qsort(divs, dcnt, sizeof(int), cmp_int);
    
    // map divisor value to its index
    static int idx[100001];
    memset(idx, -1, sizeof(idx));
    for (int i = 0; i < dcnt; ++i) {
        idx[divs[i]] = i;
    }
    
    long long *cnt = (long long *)calloc(dcnt, sizeof(long long));
    long long ans = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        int g = gcd_int(nums[i], k);
        int need = k / g;
        // sum counts of previous numbers whose gcd divisor is multiple of need
        for (int j = 0; j < dcnt; ++j) {
            if (divs[j] % need == 0) {
                ans += cnt[j];
            }
        }
        // record current number's gcd
        int pos = idx[g];
        cnt[pos]++;
    }
    
    free(cnt);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long CountPairs(int[] nums, int k) {
        // Get all divisors of k
        var divisors = new System.Collections.Generic.List<int>();
        for (int i = 1; i * (long)i <= k; ++i) {
            if (k % i == 0) {
                divisors.Add(i);
                if (i != k / i) divisors.Add(k / i);
            }
        }

        // Count occurrences of each divisor (gcd value)
        int[] cnt = new int[k + 1];
        long ans = 0;

        foreach (int num in nums) {
            int g = Gcd(num, k);
            foreach (int d in divisors) {
                if ((long)g * d % k == 0) {
                    ans += cnt[d];
                }
            }
            cnt[g]++;
        }

        return ans;
    }

    private static int Gcd(int a, int b) {
        while (b != 0) {
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
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    const maxVal = Math.max(k, ...nums);
    const cntDiv = new Uint32Array(maxVal + 1);
    
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    let ans = 0;
    for (const num of nums) {
        const g = gcd(num, k);
        const need = k / g;               // smallest multiplier needed
        if (need <= maxVal) ans += cntDiv[need];
        
        // add all divisors of current number to the frequency table
        const limit = Math.floor(Math.sqrt(num));
        for (let d = 1; d <= limit; ++d) {
            if (num % d === 0) {
                cntDiv[d] ++;
                const other = num / d;
                if (other !== d) cntDiv[other] ++;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function countPairs(nums: number[], k: number): number {
    const divisors: number[] = [];
    for (let i = 1; i * i <= k; ++i) {
        if (k % i === 0) {
            divisors.push(i);
            if (i !== k / i) divisors.push(k / i);
        }
    }

    const cnt = new Map<number, number>();
    for (const d of divisors) cnt.set(d, 0);

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let ans = 0;
    for (const num of nums) {
        const g = gcd(num, k);
        const need = k / g;
        ans += cnt.get(need)!;

        for (const d of divisors) {
            if (num % d === 0) {
                cnt.set(d, cnt.get(d)! + 1);
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countPairs($nums, $k) {
        // compute all divisors of k
        $divs = [];
        for ($i = 1; $i * $i <= $k; ++$i) {
            if ($k % $i == 0) {
                $divs[] = $i;
                if ($i != intdiv($k, $i)) {
                    $divs[] = intdiv($k, $i);
                }
            }
        }

        // initialize count map for each divisor
        $cnt = [];
        foreach ($divs as $d) {
            $cnt[$d] = 0;
        }

        $ans = 0;

        foreach ($nums as $num) {
            $g = $this->gcd($num, $k);
            $need = intdiv($k, $g); // divisor that partner must be multiple of
            if (isset($cnt[$need])) {
                $ans += $cnt[$need];
            }

            // update counts for current number
            foreach ($divs as $d) {
                if ($num % $d == 0) {
                    $cnt[$d]++;
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
    func countPairs(_ nums: [Int], _ k: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a
            var y = b
            while y != 0 {
                let temp = x % y
                x = y
                y = temp
            }
            return x
        }

        // All divisors of k
        var divisors = [Int]()
        var i = 1
        while i * i <= k {
            if k % i == 0 {
                divisors.append(i)
                if i != k / i {
                    divisors.append(k / i)
                }
            }
            i += 1
        }

        var countMap = [Int: Int]()
        var result: Int64 = 0

        for num in nums {
            let g = gcd(num, k)
            let need = k / g
            if let c = countMap[need] {
                result += Int64(c)
            }
            // Update counts for divisors of k that divide current number
            for d in divisors {
                if num % d == 0 {
                    countMap[d, default: 0] += 1
                }
            }
        }

        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(nums: IntArray, k: Int): Long {
        // Precompute all divisors of k
        val divisors = mutableListOf<Int>()
        var i = 1
        while (i * i <= k) {
            if (k % i == 0) {
                divisors.add(i)
                if (i != k / i) divisors.add(k / i)
            }
            i++
        }
        // No need to sort, but sorting can help cache locality
        divisors.sort()
        val cnt = HashMap<Int, Long>()
        var ans = 0L

        for (num in nums) {
            val g = gcd(num, k)
            val need = k / g
            var add = 0L
            for (d in divisors) {
                if (d % need == 0) {
                    add += cnt.getOrDefault(d, 0L)
                }
            }
            ans += add
            cnt[g] = cnt.getOrDefault(g, 0L) + 1
        }
        return ans
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  int countPairs(List<int> nums, int k) {
    // Get all divisors of k
    List<int> divisors = [];
    for (int i = 1; i * i <= k; ++i) {
      if (k % i == 0) {
        divisors.add(i);
        if (i != k ~/ i) divisors.add(k ~/ i);
      }
    }

    // Map divisor -> count of previous numbers divisible by it
    Map<int, int> cnt = {};
    for (int d in divisors) cnt[d] = 0;

    int ans = 0;
    for (int num in nums) {
      int g = _gcd(num, k);
      int required = k ~/ g; // divisor of k
      ans += cnt[required] ?? 0;

      // Update counts for current number
      for (int d in divisors) {
        if (num % d == 0) {
          cnt[d] = (cnt[d] ?? 0) + 1;
        }
      }
    }
    return ans;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int tmp = a % b;
      a = b;
      b = tmp;
    }
    return a;
  }
}
```

## Golang

```go
func countPairs(nums []int, k int) int64 {
    // compute all divisors of k
    divisors := make([]int, 0)
    for i := 1; i*i <= k; i++ {
        if k%i == 0 {
            divisors = append(divisors, i)
            if i != k/i {
                divisors = append(divisors, k/i)
            }
        }
    }

    // helper gcd
    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }

    cnt := make(map[int]int64)
    var ans int64

    for _, num := range nums {
        g := gcd(num, k)
        need := k / g
        if v, ok := cnt[need]; ok {
            ans += v
        }
        // update counts for divisors of k that divide num
        for _, d := range divisors {
            if num%d == 0 {
                cnt[d]++
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def count_pairs(nums, k)
  # Find all divisors of k
  divisors = []
  i = 1
  while i * i <= k
    if k % i == 0
      divisors << i
      div2 = k / i
      divisors << div2 unless div2 == i
    end
    i += 1
  end

  # Hash to store counts of numbers seen so far that are divisible by each divisor
  div_count = Hash.new(0)

  ans = 0
  nums.each do |num|
    g = num.gcd(k)
    req = k / g
    ans += div_count[req]

    divisors.each do |d|
      if (num % d).zero?
        div_count[d] += 1
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def countPairs(nums: Array[Int], k: Int): Long = {
    // Compute all divisors of k
    val divBuf = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 1
    while (i * i <= k) {
      if (k % i == 0) {
        divBuf += i
        if (i != k / i) divBuf += k / i
      }
      i += 1
    }
    val divisors = divBuf.toArray
    // Map divisor -> index in count array
    val idx = scala.collection.mutable.HashMap[Int, Int]()
    var pos = 0
    while (pos < divisors.length) {
      idx(divisors(pos)) = pos
      pos += 1
    }
    val cnt = new Array[Long](divisors.length)
    var ans: Long = 0L

    def gcd(a: Int, b: Int): Int = {
      var x = a
      var y = b
      while (y != 0) {
        val tmp = x % y
        x = y
        y = tmp
      }
      x
    }

    for (a <- nums) {
      val g = gcd(a, k)
      val need = k / g // always a divisor of k
      ans += cnt(idx(need))

      var j = 0
      while (j < divisors.length) {
        val d = divisors(j)
        if (a % d == 0) {
          cnt(j) += 1
        }
        j += 1
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i64 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        let k_usize = k as usize;
        let mut cnt = vec![0i64; k_usize + 1];
        let mut ans: i64 = 0;

        for &val in nums.iter() {
            let g = gcd(val, k);
            let need = (k / g) as usize;
            if need <= k_usize {
                ans += cnt[need];
            }

            // update counts for divisors of val that also divide k
            let mut d: i32 = 1;
            while d * d <= val {
                if val % d == 0 {
                    let d1 = d as usize;
                    let d2 = (val / d) as usize;
                    if k_usize % d1 == 0 {
                        cnt[d1] += 1;
                    }
                    if d2 != d1 && k_usize % d2 == 0 {
                        cnt[d2] += 1;
                    }
                }
                d += 1;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([cnt (make-vector (+ k 1) 0)]
         [ans 0])
    (for ([x nums])
      (define g (gcd x k))
      (define need (quotient k g))
      (set! ans (+ ans (vector-ref cnt need)))
      (define limit (floor (sqrt x)))
      (let loop ((d 1))
        (when (<= d limit)
          (when (= (remainder x d) 0)
            (when (<= d k)
              (vector-set! cnt d (+ (vector-ref cnt d) 1)))
            (define other (/ x d))
            (when (and (not (= other d)) (<= other k))
              (vector-set! cnt other (+ (vector-ref cnt other) 1))))
          (loop (+ d 1)))))
    ans))
```

## Erlang

```erlang
-spec count_pairs(Nums :: [integer()], K :: integer()) -> integer().
count_pairs(Nums, K) ->
    Divs = divisors(K),
    InitMap = init_counts(Divs),
    {Ans, _} = lists:foldl(fun(Num, {Acc, CntMap}) ->
        G = gcd(Num, K),
        Sum = count_compatible(G, K, Divs, CntMap),
        NewAcc = Acc + Sum,
        UpdatedMap = update_count(G, CntMap),
        {NewAcc, UpdatedMap}
    end, {0, InitMap}, Nums),
    Ans.

%% Compute all divisors of N
-spec divisors(integer()) -> [integer()].
divisors(N) ->
    divisors(N, 1, []).

-spec divisors(integer(), integer(), [integer()]) -> [integer()].
divisors(N, I, Acc) when I * I > N ->
    Acc;
divisors(N, I, Acc) ->
    if
        N rem I =:= 0 ->
            D2 = N div I,
            NewAcc = case I == D2 of
                true -> [I | Acc];
                false -> [I, D2 | Acc]
            end,
            divisors(N, I + 1, NewAcc);
        true ->
            divisors(N, I + 1, Acc)
    end.

%% Initialize map with zero counts for each divisor
-spec init_counts([integer()]) -> maps:map().
init_counts(Divs) ->
    lists:foldl(fun(D, M) -> maps:put(D, 0, M) end, #{}, Divs).

%% Update count of a divisor in the map
-spec update_count(integer(), maps:map()) -> maps:map().
update_count(G, Map) ->
    case maps:is_key(G, Map) of
        true ->
            Old = maps:get(G, Map),
            maps:put(G, Old + 1, Map);
        false ->
            maps:put(G, 1, Map)
    end.

%% Count how many previous numbers are compatible with current G
-spec count_compatible(integer(), integer(), [integer()], maps:map()) -> integer().
count_compatible(G, K, Divs, Map) ->
    lists:foldl(fun(D, Acc) ->
        case (G * D) rem K of
            0 -> Acc + maps:get(D, Map);
            _ -> Acc
        end
    end, 0, Divs).

%% Euclidean algorithm for GCD
-spec gcd(integer(), integer()) -> integer().
gcd(0, B) -> B;
gcd(A, 0) -> A;
gcd(A, B) when A < B ->
    gcd(B, A);
gcd(A, B) ->
    gcd(B rem A, A).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer], k :: integer) :: integer
  def count_pairs(nums, k) do
    divisors = get_divisors(k)

    # initialize counts for each divisor to 0
    init_cnt = Enum.reduce(divisors, %{}, fn d, acc -> Map.put(acc, d, 0) end)

    {ans, _} =
      Enum.reduce(nums, {0, init_cnt}, fn num, {res, cnt_map} ->
        g = Integer.gcd(num, k)
        need = div(k, g)
        add = Map.get(cnt_map, need, 0)

        # update counts for divisors that divide current number
        new_cnt =
          Enum.reduce(divisors, cnt_map, fn d, m ->
            if rem(num, d) == 0 do
              Map.update!(m, d, &(&1 + 1))
            else
              m
            end
          end)

        {res + add, new_cnt}
      end)

    ans
  end

  defp get_divisors(k) do
    limit = :math.sqrt(k) |> trunc()
    Enum.reduce(1..limit, [], fn i, acc ->
      if rem(k, i) == 0 do
        d2 = div(k, i)
        if i == d2 do
          [i | acc]
        else
          [i, d2 | acc]
        end
      else
        acc
      end
    end)
  end
end
```
