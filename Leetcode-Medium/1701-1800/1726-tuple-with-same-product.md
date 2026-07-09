# 1726. Tuple with Same Product

## Cpp

```cpp
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<long long, int> freq;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long long prod = 1LL * nums[i] * nums[j];
                ++freq[prod];
            }
        }
        long long ans = 0;
        for (const auto& kv : freq) {
            long long f = kv.second;
            if (f > 1) {
                ans += (f * (f - 1) / 2) * 8;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int tupleSameProduct(int[] nums) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int prod = nums[i] * nums[j];
                freq.put(prod, freq.getOrDefault(prod, 0) + 1);
            }
        }
        long total = 0;
        for (int count : freq.values()) {
            if (count > 1) {
                total += (long) count * (count - 1) / 2 * 8;
            }
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        prod_count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                prod_count[a * nums[j]] += 1

        total = 0
        for cnt in prod_count.values():
            if cnt > 1:
                total += 8 * (cnt * (cnt - 1) // 2)
        return total
```

## Python3

```python
class Solution:
    def tupleSameProduct(self, nums):
        from collections import Counter
        cnt = Counter()
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                cnt[a * nums[j]] += 1
        ans = 0
        for f in cnt.values():
            if f > 1:
                ans += (f * (f - 1) // 2) * 8
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int tupleSameProduct(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    int n = numsSize;
    long long pairCountLL = (long long)n * (n - 1) / 2;
    int pairCount = (int)pairCountLL;  // fits in int for given constraints
    int *prods = (int *)malloc(pairCount * sizeof(int));
    if (!prods) return 0;  // allocation failure fallback

    int idx = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            prods[idx++] = nums[i] * nums[j];
        }
    }

    qsort(prods, pairCount, sizeof(int), cmp_int);

    long long total = 0;
    long long cnt = 1;
    for (int i = 1; i < pairCount; ++i) {
        if (prods[i] == prods[i - 1]) {
            ++cnt;
        } else {
            total += (cnt * (cnt - 1) / 2) * 8;
            cnt = 1;
        }
    }
    total += (cnt * (cnt - 1) / 2) * 8;

    free(prods);
    return (int)total;
}
```

## Csharp

```csharp
public class Solution
{
    public int TupleSameProduct(int[] nums)
    {
        var freq = new Dictionary<int, int>();
        int n = nums.Length;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                int prod = nums[i] * nums[j];
                if (freq.ContainsKey(prod))
                    freq[prod]++;
                else
                    freq[prod] = 1;
            }
        }

        long total = 0;
        foreach (var kvp in freq)
        {
            int f = kvp.Value;
            if (f > 1)
            {
                total += ((long)f * (f - 1) / 2) * 8;
            }
        }

        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function(nums) {
    const prodCount = new Map();
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            const p = nums[i] * nums[j];
            prodCount.set(p, (prodCount.get(p) || 0) + 1);
        }
    }
    let ans = 0;
    for (const cnt of prodCount.values()) {
        if (cnt > 1) {
            ans += 8 * cnt * (cnt - 1) / 2;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function tupleSameProduct(nums: number[]): number {
    const productCount = new Map<number, number>();
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const prod = nums[i] * nums[j];
            productCount.set(prod, (productCount.get(prod) ?? 0) + 1);
        }
    }

    let total = 0;
    for (const freq of productCount.values()) {
        if (freq > 1) {
            const pairs = (freq * (freq - 1)) / 2;
            total += pairs * 8;
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function tupleSameProduct($nums) {
        $n = count($nums);
        $freq = [];

        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $prod = $nums[$i] * $nums[$j];
                if (isset($freq[$prod])) {
                    $freq[$prod]++;
                } else {
                    $freq[$prod] = 1;
                }
            }
        }

        $ans = 0;
        foreach ($freq as $cnt) {
            if ($cnt > 1) {
                $pairs = $cnt * ($cnt - 1) / 2;
                $ans += $pairs * 8;
            }
        }

        return (int)$ans;
    }
}
```

## Swift

```swift
class Solution {
    func tupleSameProduct(_ nums: [Int]) -> Int {
        var productCount = [Int:Int]()
        let n = nums.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                let prod = nums[i] * nums[j]
                productCount[prod, default: 0] += 1
            }
        }
        var result = 0
        for count in productCount.values {
            if count > 1 {
                let pairs = count * (count - 1) / 2
                result += pairs * 8
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun tupleSameProduct(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        val n = nums.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val prod = nums[i] * nums[j]
                freq[prod] = (freq[prod] ?: 0) + 1
            }
        }
        var ans = 0L
        for (cnt in freq.values) {
            if (cnt > 1) {
                ans += 8L * cnt * (cnt - 1) / 2
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int tupleSameProduct(List<int> nums) {
    final Map<int, int> freq = {};
    final int n = nums.length;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        final int product = nums[i] * nums[j];
        freq[product] = (freq[product] ?? 0) + 1;
      }
    }

    int total = 0;
    for (final int count in freq.values) {
      if (count > 1) {
        total += ((count * (count - 1)) ~/ 2) * 8;
      }
    }
    return total;
  }
}
```

## Golang

```go
func tupleSameProduct(nums []int) int {
    productCount := make(map[int]int)
    n := len(nums)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            prod := nums[i] * nums[j]
            productCount[prod]++
        }
    }

    var total int64
    for _, cnt := range productCount {
        if cnt > 1 {
            total += int64(cnt*(cnt-1)/2) * 8
        }
    }
    return int(total)
}
```

## Ruby

```ruby
def tuple_same_product(nums)
  freq = Hash.new(0)
  n = nums.length
  i = 0
  while i < n
    j = i + 1
    while j < n
      prod = nums[i] * nums[j]
      freq[prod] += 1
      j += 1
    end
    i += 1
  end

  total = 0
  freq.each_value do |cnt|
    if cnt > 1
      total += (cnt * (cnt - 1) / 2) * 8
    end
  end
  total
end
```

## Scala

```scala
object Solution {
  def tupleSameProduct(nums: Array[Int]): Int = {
    import scala.collection.mutable

    val freq = mutable.HashMap[Int, Int]()
    val n = nums.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val prod = nums(i) * nums(j)
        freq.put(prod, freq.getOrElse(prod, 0) + 1)
        j += 1
      }
      i += 1
    }

    var total: Long = 0L
    for ((_, f) <- freq) {
      if (f > 1) {
        val pairs = f.toLong * (f - 1) / 2
        total += pairs * 8
      }
    }
    total.toInt
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut freq: HashMap<i32, i32> = HashMap::new();

        for i in 0..n {
            for j in (i + 1)..n {
                let prod = nums[i] * nums[j];
                *freq.entry(prod).or_insert(0) += 1;
            }
        }

        let mut total: i64 = 0;
        for &cnt in freq.values() {
            if cnt > 1 {
                let c = cnt as i64;
                total += 8 * (c * (c - 1) / 2);
            }
        }

        total as i32
    }
}
```

## Racket

```racket
(define/contract (tuple-same-product nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector nums))
         (n   (vector-length vec))
         (freq (make-hash)))
    ;; count frequencies of each product
    (for ([i (in-range n)])
      (for ([j (in-range (+ i 1) n)])
        (define prod (* (vector-ref vec i) (vector-ref vec j)))
        (hash-set! freq prod (+ 1 (hash-ref freq prod 0)))))
    ;; compute total tuples
    (let ((total 0))
      (for ([kv (in-hash freq)])
        (define f (cdr kv))
        (when (> f 1)
          (set! total (+ total (* 8 (/ (* f (- f 1)) 2))))))
      total)))
```

## Erlang

```erlang
-module(solution).
-export([tuple_same_product/1]).

-spec tuple_same_product(Nums :: [integer()]) -> integer().
tuple_same_product(Nums) ->
    FreqMap = build_freq_map(Nums, #{}),
    compute_total(FreqMap).

build_freq_map([], Map) -> Map;
build_freq_map([H|T], Map) ->
    NewMap = add_products(H, T, Map),
    build_freq_map(T, NewMap).

add_products(_, [], Map) -> Map;
add_products(A, [B|Rest], Map) ->
    Prod = A * B,
    Count = maps:get(Prod, Map, 0),
    UpdatedMap = maps:put(Prod, Count + 1, Map),
    add_products(A, Rest, UpdatedMap).

compute_total(Map) ->
    maps:fold(fun(_Key, Freq, Acc) ->
        case Freq > 1 of
            true ->
                Pairs = (Freq * (Freq - 1)) div 2,
                Acc + 8 * Pairs;
            false -> Acc
        end
    end, 0, Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec tuple_same_product(nums :: [integer]) :: integer
  def tuple_same_product(nums) do
    products =
      for {a, i} <- Enum.with_index(nums),
          {b, j} <- Enum.with_index(nums),
          i < j,
          do: a * b

    freq =
      Enum.reduce(products, %{}, fn p, acc ->
        Map.update(acc, p, 1, &(&1 + 1))
      end)

    Enum.reduce(freq, 0, fn {_p, f}, sum ->
      if f > 1 do
        sum + 8 * div(f * (f - 1), 2)
      else
        sum
      end
    end)
  end
end
```
