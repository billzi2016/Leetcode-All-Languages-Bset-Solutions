# 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers

## Cpp

```cpp
class Solution {
public:
    long long countTriplets(const vector<int>& A, const unordered_map<int,int>& freqB) {
        long long res = 0;
        for (int a : A) {
            long long target = 1LL * a * a;
            for (const auto& kv : freqB) {
                int b = kv.first;
                if (target % b != 0) continue;
                long long cVal = target / b;
                if (cVal > INT_MAX) continue;
                int c = static_cast<int>(cVal);
                auto it = freqB.find(c);
                if (it == freqB.end()) continue;
                if (b < c) {
                    res += 1LL * kv.second * it->second;
                } else if (b == c) {
                    long long cnt = kv.second;
                    res += cnt * (cnt - 1) / 2;
                }
            }
        }
        return res;
    }

    int numTriplets(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> freq1, freq2;
        for (int x : nums1) ++freq1[x];
        for (int x : nums2) ++freq2[x];

        long long ans = 0;
        ans += countTriplets(nums1, freq2);
        ans += countTriplets(nums2, freq1);
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numTriplets(int[] nums1, int[] nums2) {
        long total = count(nums1, nums2) + count(nums2, nums1);
        return (int) total;
    }
    
    private long count(int[] a, int[] b) {
        java.util.Map<Long, Integer> squareFreq = new java.util.HashMap<>();
        for (int v : a) {
            long sq = 1L * v * v;
            squareFreq.merge(sq, 1, Integer::sum);
        }
        long ans = 0;
        int n = b.length;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long prod = 1L * b[i] * b[j];
                Integer cnt = squareFreq.get(prod);
                if (cnt != null) {
                    ans += cnt;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        from collections import Counter

        def pair_product_counts(arr):
            cnt = Counter()
            n = len(arr)
            for i in range(n):
                a = arr[i]
                for j in range(i + 1, n):
                    cnt[a * arr[j]] += 1
            return cnt

        prod2 = pair_product_counts(nums2)
        prod1 = pair_product_counts(nums1)

        total = 0
        for x in nums1:
            total += prod2.get(x * x, 0)
        for y in nums2:
            total += prod1.get(y * y, 0)

        return total
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)

        def count(arr_cnt: Counter, other_cnt: Counter) -> int:
            total = 0
            for val, freq in arr_cnt.items():
                target = val * val
                for y in other_cnt:
                    if target % y != 0:
                        continue
                    z = target // y
                    if z not in other_cnt:
                        continue
                    if y < z:
                        total += freq * other_cnt[y] * other_cnt[z]
                    elif y == z:
                        total += freq * (other_cnt[y] * (other_cnt[y] - 1) // 2)
            return total

        ans = count(cnt1, cnt2) + count(cnt2, cnt1)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int numTriplets(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    const int MAXV = 100000;
    long long ans = 0;
    int *freq = (int *)calloc(MAXV + 1, sizeof(int));
    if (!freq) return 0;

    // Type 1: nums1[i]^2 == nums2[j] * nums2[k]
    for (int i = 0; i < nums1Size; ++i) {
        long long target = (long long)nums1[i] * nums1[i];
        memset(freq, 0, (MAXV + 1) * sizeof(int));
        for (int j = 0; j < nums2Size; ++j) {
            int b = nums2[j];
            if (target % b == 0) {
                long long c = target / b;
                if (c <= MAXV) ans += freq[c];
            }
            ++freq[b];
        }
    }

    // Type 2: nums2[i]^2 == nums1[j] * nums1[k]
    for (int i = 0; i < nums2Size; ++i) {
        long long target = (long long)nums2[i] * nums2[i];
        memset(freq, 0, (MAXV + 1) * sizeof(int));
        for (int j = 0; j < nums1Size; ++j) {
            int b = nums1[j];
            if (target % b == 0) {
                long long c = target / b;
                if (c <= MAXV) ans += freq[c];
            }
            ++freq[b];
        }
    }

    free(freq);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumTriplets(int[] nums1, int[] nums2)
    {
        long result = Count(nums1, nums2);
        result += Count(nums2, nums1);
        return (int)result;
    }

    private long Count(int[] a, int[] b)
    {
        var freq = new Dictionary<int, int>();
        foreach (var x in b)
        {
            if (freq.ContainsKey(x))
                freq[x]++;
            else
                freq[x] = 1;
        }

        long total = 0;
        foreach (var valA in a)
        {
            long target = (long)valA * valA;
            foreach (var kvp in freq)
            {
                int v = kvp.Key;
                if (target % v != 0) continue;

                long wLong = target / v;
                if (wLong > int.MaxValue) continue;
                int w = (int)wLong;

                if (!freq.ContainsKey(w)) continue;
                if (v > w) continue; // ensure each unordered pair counted once

                int cntV = kvp.Value;
                int cntW = freq[w];

                if (v == w)
                    total += (long)cntV * (cntV - 1) / 2;
                else
                    total += (long)cntV * cntW;
            }
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var numTriplets = function(nums1, nums2) {
    const buildSquareMap = (arr) => {
        const map = new Map();
        for (const v of arr) {
            const sq = v * v;
            map.set(sq, (map.get(sq) || 0) + 1);
        }
        return map;
    };
    
    const countPairs = (arr, squareMap) => {
        let cnt = 0;
        const n = arr.length;
        for (let i = 0; i < n; ++i) {
            for (let j = i + 1; j < n; ++j) {
                const prod = arr[i] * arr[j];
                if (squareMap.has(prod)) {
                    cnt += squareMap.get(prod);
                }
            }
        }
        return cnt;
    };
    
    const map1 = buildSquareMap(nums1);
    const map2 = buildSquareMap(nums2);
    
    return countPairs(nums2, map1) + countPairs(nums1, map2);
};
```

## Typescript

```typescript
function numTriplets(nums1: number[], nums2: number[]): number {
    const freq1 = new Map<number, number>();
    const freq2 = new Map<number, number>();

    for (const v of nums1) {
        freq1.set(v, (freq1.get(v) ?? 0) + 1);
    }
    for (const v of nums2) {
        freq2.set(v, (freq2.get(v) ?? 0) + 1);
    }

    function count(arrFreq: Map<number, number>, otherFreq: Map<number, number>): number {
        let total = 0;
        for (const [a, cntA] of arrFreq.entries()) {
            const target = a * a;
            for (const [b, cntB] of otherFreq.entries()) {
                if (target % b !== 0) continue;
                const c = target / b;
                if (!otherFreq.has(c)) continue;
                if (b < c) {
                    total += cntA * cntB * (otherFreq.get(c) ?? 0);
                } else if (b === c) {
                    total += cntA * (cntB * (cntB - 1) / 2);
                }
            }
        }
        return total;
    }

    return count(freq1, freq2) + count(freq2, freq1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function numTriplets($nums1, $nums2) {
        $freq1 = [];
        foreach ($nums1 as $v) {
            $freq1[$v] = ($freq1[$v] ?? 0) + 1;
        }
        $freq2 = [];
        foreach ($nums2 as $v) {
            $freq2[$v] = ($freq2[$v] ?? 0) + 1;
        }

        $total = 0;

        // Type 1: nums1[i]^2 == nums2[j] * nums2[k]
        foreach ($freq1 as $val => $cnt) {
            $target = $val * $val;
            $pairs = $this->countPairs($freq2, $target);
            $total += $cnt * $pairs;
        }

        // Type 2: nums2[i]^2 == nums1[j] * nums1[k]
        foreach ($freq2 as $val => $cnt) {
            $target = $val * $val;
            $pairs = $this->countPairs($freq1, $target);
            $total += $cnt * $pairs;
        }

        return $total;
    }

    /**
     * @param array $freq  associative array value=>frequency
     * @param int   $target product to match
     * @return int number of unordered pairs (j,k) with j<k whose product equals target
     */
    private function countPairs($freq, $target) {
        $cnt = 0;
        foreach ($freq as $a => $fa) {
            if ($a == 0) continue; // avoid division by zero, though constraints guarantee >=1
            if ($target % $a !== 0) continue;
            $b = intdiv($target, $a);
            if (!isset($freq[$b])) continue;
            $fb = $freq[$b];
            if ($a == $b) {
                $cnt += $fa * ($fa - 1) / 2;
            } elseif ($a < $b) { // count each unordered pair once
                $cnt += $fa * $fb;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func numTriplets(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let freq1 = buildFreq(nums1)
        let freq2 = buildFreq(nums2)
        let count1 = countTriplets(nums1, freq2)
        let count2 = countTriplets(nums2, freq1)
        return count1 + count2
    }
    
    private func buildFreq(_ arr: [Int]) -> [Int:Int] {
        var dict = [Int:Int]()
        for v in arr {
            dict[v, default: 0] += 1
        }
        return dict
    }
    
    private func countTriplets(_ a: [Int], _ bFreq: [Int:Int]) -> Int {
        var total = 0
        let bItems = Array(bFreq)   // [(value, frequency)]
        for x in a {
            let target = Int64(x) * Int64(x)
            for (y, fy) in bItems {
                if target % Int64(y) != 0 { continue }
                let e = target / Int64(y)
                guard let fe = bFreq[Int(e)] else { continue }
                if y < Int(e) {
                    total += fy * fe
                } else if y == Int(e) {
                    total += fy * (fy - 1) / 2
                }
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numTriplets(nums1: IntArray, nums2: IntArray): Int {
        fun count(squareArr: IntArray, prodArr: IntArray): Long {
            val freq = HashMap<Int, Int>()
            for (v in prodArr) {
                freq[v] = (freq[v] ?: 0) + 1
            }
            var ans = 0L
            for (a in squareArr) {
                val target = a.toLong() * a
                for ((b, cntB) in freq) {
                    if (target % b != 0L) continue
                    val cLong = target / b
                    if (cLong > Int.MAX_VALUE) continue
                    val c = cLong.toInt()
                    val cntC = freq[c] ?: 0
                    if (cntC == 0) continue
                    when {
                        b < c -> ans += cntB.toLong() * cntC
                        b == c -> ans += cntB.toLong() * (cntB - 1) / 2
                    }
                }
            }
            return ans
        }

        val total = count(nums1, nums2) + count(nums2, nums1)
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numTriplets(List<int> nums1, List<int> nums2) {
    Map<int, int> freq1 = _frequency(nums1);
    Map<int, int> freq2 = _frequency(nums2);

    int ans = 0;

    // Type 1: nums1 element squared equals product of two nums2 elements
    for (var entry in freq1.entries) {
      int val = entry.key;
      int countVal = entry.value;
      int target = val * val;
      int pairs = _countPairs(target, freq2);
      ans += countVal * pairs;
    }

    // Type 2: nums2 element squared equals product of two nums1 elements
    for (var entry in freq2.entries) {
      int val = entry.key;
      int countVal = entry.value;
      int target = val * val;
      int pairs = _countPairs(target, freq1);
      ans += countVal * pairs;
    }

    return ans;
  }

  Map<int, int> _frequency(List<int> nums) {
    final map = <int, int>{};
    for (var v in nums) {
      map[v] = (map[v] ?? 0) + 1;
    }
    return map;
  }

  int _countPairs(int target, Map<int, int> freq) {
    int total = 0;
    for (var b in freq.keys) {
      if (target % b != 0) continue;
      int c = target ~/ b;
      if (!freq.containsKey(c)) continue;

      if (b < c) {
        total += freq[b]! * freq[c]!;
      } else if (b == c) {
        int f = freq[b]!;
        total += f * (f - 1) ~/ 2;
      }
    }
    return total;
  }
}
```

## Golang

```go
func numTriplets(nums1 []int, nums2 []int) int {
    // build frequency maps
    freq1 := make(map[int]int)
    for _, v := range nums1 {
        freq1[v]++
    }
    freq2 := make(map[int]int)
    for _, v := range nums2 {
        freq2[v]++
    }

    countPairs := func(freq map[int]int, target int64) int {
        var cnt int64
        for v, fv := range freq {
            if target%int64(v) != 0 {
                continue
            }
            w := int(target / int64(v))
            fw, ok := freq[w]
            if !ok {
                continue
            }
            if v < w {
                cnt += int64(fv) * int64(fw)
            } else if v == w {
                cnt += int64(fv) * int64(fv-1) / 2
            }
        }
        return int(cnt)
    }

    var total int64

    // type 1: square from nums1, product from nums2
    for _, x := range nums1 {
        target := int64(x) * int64(x)
        total += int64(countPairs(freq2, target))
    }

    // type 2: square from nums2, product from nums1
    for _, x := range nums2 {
        target := int64(x) * int64(x)
        total += int64(countPairs(freq1, target))
    }

    return int(total)
}
```

## Ruby

```ruby
def num_triplets(nums1, nums2)
  # helper to count all unordered pairs (j<k) product frequencies in an array
  pair_counts = lambda do |arr|
    freq = Hash.new(0)
    arr.each { |v| freq[v] += 1 }
    counts = Hash.new(0)
    keys = freq.keys
    n = keys.size
    (0...n).each do |i|
      a = keys[i]
      fa = freq[a]
      # same value pairs
      if fa > 1
        prod = a * a
        counts[prod] += fa * (fa - 1) / 2
      end
      ((i + 1)...n).each do |j|
        b = keys[j]
        fb = freq[b]
        prod = a * b
        counts[prod] += fa * fb
      end
    end
    counts
  end

  cnt12 = pair_counts.call(nums2)
  cnt21 = pair_counts.call(nums1)

  ans = 0
  nums1.each { |x| ans += cnt12[x * x] }
  nums2.each { |x| ans += cnt21[x * x] }

  ans
end
```

## Scala

```scala
object Solution {
    def numTriplets(nums1: Array[Int], nums2: Array[Int]): Int = {
        def count(arrA: Array[Int], arrB: Array[Int]): Long = {
            val prodCount = scala.collection.mutable.Map[Long, Long]().withDefaultValue(0L)
            val n = arrB.length
            var i = 0
            while (i < n) {
                val bi = arrB(i).toLong
                var j = i + 1
                while (j < n) {
                    val prod = bi * arrB(j).toLong
                    prodCount(prod) = prodCount(prod) + 1L
                    j += 1
                }
                i += 1
            }
            var total: Long = 0L
            for (x <- arrA) {
                val sq = x.toLong * x
                total += prodCount.getOrElse(sq, 0L)
            }
            total
        }
        val ans = count(nums1, nums2) + count(nums2, nums1)
        ans.toInt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn num_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        fn build_freq(arr: &Vec<i32>) -> HashMap<i64, i64> {
            let mut map = HashMap::new();
            for &v in arr.iter() {
                *map.entry(v as i64).or_insert(0) += 1;
            }
            map
        }

        fn count(arr: &Vec<i32>, freq_other: &HashMap<i64, i64>) -> i64 {
            let mut total = 0i64;
            for &x in arr.iter() {
                let target = (x as i64) * (x as i64);
                for (&y, &fy) in freq_other.iter() {
                    if target % y != 0 {
                        continue;
                    }
                    let z = target / y;
                    if let Some(&fz) = freq_other.get(&z) {
                        if y < z {
                            total += fy * fz;
                        } else if y == z {
                            total += fy * (fy - 1) / 2;
                        }
                    }
                }
            }
            total
        }

        let freq1 = build_freq(&nums1);
        let freq2 = build_freq(&nums2);

        let ans = count(&nums1, &freq2) + count(&nums2, &freq1);
        ans as i32
    }
}
```

## Racket

```racket
(define (choose2 n)
  (/ (* n (- n 1)) 2))

(define (pair-count-map nums)
  (let* ([freq (make-hash)])
    (for ([v nums])
      (hash-set! freq v (+ 1 (hash-ref freq v 0))))
    (define keys (hash-keys freq))
    (define prodMap (make-hash))
    (for ([i (in-range (length keys))])
      (let* ([a (list-ref keys i)]
             [ca (hash-ref freq a)])
        (for ([j (in-range i (length keys))])
          (let* ([b (list-ref keys j)]
                 [cb (hash-ref freq b)]
                 [product (* a b)]
                 [pair-count (if (= i j)
                                 (choose2 ca)
                                 (* ca cb))])
            (when (> pair-count 0)
              (hash-set! prodMap product (+ (hash-ref prodMap product 0) pair-count)))))))
    prodMap))

(define/contract (num-triplets nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([map2 (pair-count-map nums2)]
         [map1 (pair-count-map nums1)])
    (define ans
      (foldl (lambda (x acc)
               (+ acc (hash-ref map2 (* x x) 0)))
             0 nums1))
    (foldl (lambda (y acc)
             (+ acc (hash-ref map1 (* y y) 0)))
           ans nums2)))
```

## Erlang

```erlang
-module(solution).
-export([num_triplets/2]).

-spec num_triplets(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
num_triplets(Nums1, Nums2) ->
    SqMap1 = build_square_freq(Nums1),
    SqMap2 = build_square_freq(Nums2),
    Count1 = count_pairs(Nums2, SqMap1),
    Count2 = count_pairs(Nums1, SqMap2),
    Count1 + Count2.

build_square_freq(List) ->
    lists:foldl(fun(X, Acc) ->
        S = X * X,
        case maps:is_key(S, Acc) of
            true -> maps:update_with(S, fun(C) -> C + 1 end, 0, Acc);
            false -> maps:put(S, 1, Acc)
        end
    end, #{}, List).

count_pairs(List, SquareMap) ->
    count_pairs(List, SquareMap, 0).

count_pairs([], _Map, Acc) -> Acc;
count_pairs([H|T], Map, Acc) ->
    PairCount = count_with_rest(H, T, Map, 0),
    NewAcc = Acc + PairCount,
    count_pairs(T, Map, NewAcc).

count_with_rest(_Val, [], _Map, Acc) -> Acc;
count_with_rest(Val, [H|T], Map, Acc) ->
    Prod = Val * H,
    C = maps:get(Prod, Map, 0),
    count_with_rest(Val, T, Map, Acc + C).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_triplets(nums1 :: [integer], nums2 :: [integer]) :: integer
  def num_triplets(nums1, nums2) do
    freq1 = Enum.frequencies(nums1)
    freq2 = Enum.frequencies(nums2)

    pair_counts2 = pair_product_counts(freq2)
    pair_counts1 = pair_product_counts(freq1)

    total_type1 =
      Enum.reduce(freq1, 0, fn {a, ca}, acc ->
        target = a * a
        pairs = Map.get(pair_counts2, target, 0)
        acc + ca * pairs
      end)

    total_type2 =
      Enum.reduce(freq2, 0, fn {b, cb}, acc ->
        target = b * b
        pairs = Map.get(pair_counts1, target, 0)
        acc + cb * pairs
      end)

    total_type1 + total_type2
  end

  defp pair_product_counts(freq) do
    keys = Map.keys(freq)

    Enum.reduce(keys, %{}, fn x, acc ->
      cx = freq[x]

      Enum.reduce(keys, acc, fn y, inner_acc ->
        if y < x do
          inner_acc
        else
          cy = freq[y]
          prod = x * y

          pairs =
            if x == y do
              div(cx * (cx - 1), 2)
            else
              cx * cy
            end

          Map.update(inner_acc, prod, pairs, &(&1 + pairs))
        end
      end)
    end)
  end
end
```
