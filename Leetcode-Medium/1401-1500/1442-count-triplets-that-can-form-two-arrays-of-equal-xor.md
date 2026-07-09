# 1442. Count Triplets That Can Form Two Arrays of Equal XOR

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countTriplets(vector<int>& arr) {
        unordered_map<int, pair<long long,long long>> mp;
        mp[0] = {1, 0}; // prefix xor 0 occurs at virtual index -1 (store sum of idx+1 as 0)
        long long ans = 0;
        int pref = 0;
        for (int i = 0; i < (int)arr.size(); ++i) {
            pref ^= arr[i];
            auto it = mp.find(pref);
            if (it != mp.end()) {
                ans += it->second.first * i - it->second.second;
            }
            mp[pref].first++;
            mp[pref].second += (long long)i + 1; // store sum of (index+1)
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countTriplets(int[] arr) {
        long ans = 0;
        int prefix = 0;
        java.util.HashMap<Integer, Integer> cnt = new java.util.HashMap<>();
        java.util.HashMap<Integer, Long> sumIdx = new java.util.HashMap<>();
        cnt.put(0, 1);
        sumIdx.put(0, 0L); // position of the initial prefix (index -1) contributes 0
        
        for (int i = 0; i < arr.length; i++) {
            prefix ^= arr[i];
            if (cnt.containsKey(prefix)) {
                ans += (long) cnt.get(prefix) * i - sumIdx.get(prefix);
            }
            cnt.put(prefix, cnt.getOrDefault(prefix, 0) + 1);
            sumIdx.put(prefix, sumIdx.getOrDefault(prefix, 0L) + (i + 1));
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict

        # Build prefix XOR array with an initial 0.
        pref = [0]
        for num in arr:
            pref.append(pref[-1] ^ num)

        cnt = defaultdict(int)   # count of each prefix value seen so far
        total = defaultdict(int) # sum of indices where each prefix value occurred
        ans = 0

        for i, val in enumerate(pref):
            # For all previous positions j with same prefix XOR,
            # each contributes (i - j - 1) triplets.
            ans += cnt[val] * i - total[val]
            cnt[val] += 1
            total[val] += i

        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt = defaultdict(int)
        total = defaultdict(int)
        cnt[0] = 1
        prefix = 0
        ans = 0
        for i, v in enumerate(arr):
            prefix ^= v
            if prefix in cnt:
                ans += cnt[prefix] * i - total[prefix]
            cnt[prefix] += 1
            total[prefix] += i + 1
        return ans
```

## C

```c
int countTriplets(int* arr, int arrSize) {
    int prefix[302];
    prefix[0] = 0;
    for (int i = 0; i < arrSize; ++i) {
        prefix[i + 1] = prefix[i] ^ arr[i];
    }
    long long ans = 0;
    for (int i = 0; i <= arrSize; ++i) {
        for (int j = i + 1; j <= arrSize; ++j) {
            if (prefix[i] == prefix[j]) {
                ans += (j - i - 1);
            }
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountTriplets(int[] arr) {
        var countMap = new System.Collections.Generic.Dictionary<int, long>();
        var totalMap = new System.Collections.Generic.Dictionary<int, long>();
        // initial prefix xor 0 at position 0
        countMap[0] = 1;
        totalMap[0] = 0;

        long result = 0;
        int prefix = 0;
        for (int i = 0; i < arr.Length; i++) {
            prefix ^= arr[i];

            if (!countMap.TryGetValue(prefix, out long cnt)) {
                cnt = 0;
                countMap[prefix] = 0;
                totalMap[prefix] = 0;
            }
            long sumIdx = totalMap[prefix];
            // contribution from previous occurrences
            result += cnt * i - sumIdx;

            // update maps with current position (i + 1)
            countMap[prefix] = cnt + 1;
            totalMap[prefix] = sumIdx + (i + 1);
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var countTriplets = function(arr) {
    const cnt = new Map();
    const sumIdx = new Map();
    cnt.set(0, 1);
    sumIdx.set(0, 0);
    let prefix = 0;
    let ans = 0;
    for (let i = 0; i < arr.length; ++i) {
        prefix ^= arr[i];
        const c = cnt.get(prefix) || 0;
        const s = sumIdx.get(prefix) || 0;
        ans += c * i - s;
        cnt.set(prefix, c + 1);
        sumIdx.set(prefix, s + (i + 1));
    }
    return ans;
};
```

## Typescript

```typescript
function countTriplets(arr: number[]): number {
    let prefix = 0;
    let result = 0;
    const cnt = new Map<number, number>();
    const total = new Map<number, number>();
    cnt.set(0, 1);
    total.set(0, 0);
    for (let i = 0; i < arr.length; i++) {
        prefix ^= arr[i];
        const pos = i + 1; // position in prefix array
        const c = cnt.get(prefix) ?? 0;
        const s = total.get(prefix) ?? 0;
        if (c > 0) {
            result += c * pos - s - c;
        }
        cnt.set(prefix, c + 1);
        total.set(prefix, s + pos);
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function countTriplets($arr) {
        $cnt = [0 => 1];
        $total = [0 => 0];
        $prefix = 0;
        $ans = 0;
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $prefix ^= $arr[$i];
            if (!isset($cnt[$prefix])) {
                $cnt[$prefix] = 0;
                $total[$prefix] = 0;
            }
            $ans += $cnt[$prefix] * $i - $total[$prefix];
            $cnt[$prefix]++;
            $total[$prefix] += $i + 1;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countTriplets(_ arr: [Int]) -> Int {
        var prefix = 0
        var result = 0
        var cnt: [Int:Int] = [0:1]
        var total: [Int:Int] = [0:0]

        for i in 0..<arr.count {
            prefix ^= arr[i]
            if let c = cnt[prefix] {
                let t = total[prefix] ?? 0
                result += c * i - t
                cnt[prefix] = c + 1
                total[prefix] = t + (i + 1)
            } else {
                cnt[prefix] = 1
                total[prefix] = i + 1
            }
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countTriplets(arr: IntArray): Int {
        val countMap = HashMap<Int, Long>()
        val totalMap = HashMap<Int, Long>()
        countMap[0] = 1L
        totalMap[0] = 0L
        var prefix = 0
        var result = 0L
        for (i in arr.indices) {
            prefix = prefix xor arr[i]
            val cnt = countMap.getOrDefault(prefix, 0L)
            val tot = totalMap.getOrDefault(prefix, 0L)
            result += cnt * i - tot
            countMap[prefix] = cnt + 1
            totalMap[prefix] = tot + (i + 1).toLong()
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countTriplets(List<int> arr) {
    Map<int, int> countMap = {0: 1};
    Map<int, int> totalMap = {0: 0};

    int prefix = 0;
    int result = 0;

    for (int i = 0; i < arr.length; ++i) {
      prefix ^= arr[i];
      int idx = i + 1; // position in the prefix array

      int cnt = countMap[prefix] ?? 0;
      int totalIdx = totalMap[prefix] ?? 0;

      result += cnt * (idx - 1) - totalIdx;

      countMap[prefix] = cnt + 1;
      totalMap[prefix] = totalIdx + idx;
    }

    return result;
  }
}
```

## Golang

```go
func countTriplets(arr []int) int {
	cnt := map[int]int{0: 1}
	sumIdx := map[int]int{0: 0}
	prefix, ans := 0, 0
	for i, v := range arr {
		prefix ^= v
		if c, ok := cnt[prefix]; ok {
			ans += c*i - sumIdx[prefix]
		}
		cnt[prefix] = cnt[prefix] + 1
		sumIdx[prefix] = sumIdx[prefix] + (i + 1)
	}
	return ans
}
```

## Ruby

```ruby
def count_triplets(arr)
  cnt = Hash.new(0)
  sum_idx = Hash.new(0)
  cnt[0] = 1
  prefix = 0
  result = 0

  arr.each_with_index do |val, i|
    prefix ^= val
    result += cnt[prefix] * i - sum_idx[prefix]
    cnt[prefix] += 1
    sum_idx[prefix] += i + 1
  end

  result
end
```

## Scala

```scala
object Solution {
    def countTriplets(arr: Array[Int]): Int = {
        import scala.collection.mutable

        val countMap = mutable.Map[Int, Long]().withDefaultValue(0L)
        val totalMap = mutable.Map[Int, Long]().withDefaultValue(0L)

        // prefix XOR 0 at index 0
        countMap(0) = 1L
        totalMap(0) = 0L

        var prefix = 0
        var ans: Long = 0L

        for (i <- arr.indices) {
            prefix ^= arr(i)
            val idx = i + 1 // current prefix index (1-based in terms of pref array)

            val cnt = countMap(prefix)
            val sumIdx = totalMap(prefix)

            if (cnt > 0) {
                ans += cnt * (idx - 1) - sumIdx
            }

            countMap(prefix) = cnt + 1
            totalMap(prefix) = sumIdx + idx
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_triplets(arr: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut cnt: HashMap<i32, i64> = HashMap::new();
        let mut sum: HashMap<i32, i64> = HashMap::new();
        cnt.insert(0, 1);
        sum.insert(0, 0);
        let mut prefix = 0i32;
        let mut ans: i64 = 0;
        for (i, &v) in arr.iter().enumerate() {
            prefix ^= v;
            if let Some(&c) = cnt.get(&prefix) {
                let s = *sum.get(&prefix).unwrap_or(&0);
                ans += c * (i as i64) - s;
            }
            *cnt.entry(prefix).or_insert(0) += 1;
            *sum.entry(prefix).or_insert(0) += (i as i64) + 1;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-triplets arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((cnt   (make-hash))
         (total (make-hash))
         (_     (hash-set! cnt   0 1))   ; prefix xor 0 occurs once before start
         (_     (hash-set! total 0 0))   ; sum of (index+1) for that occurrence
         (prefix 0)
         (ans    0)
         (n (length arr)))
    (for ([i (in-range n)]
          [val (in-list arr)])
      (set! prefix (bitwise-xor prefix val))
      (let ((c (hash-ref cnt   prefix 0))
            (t (hash-ref total prefix 0)))
        (when (> c 0)
          (set! ans (+ ans (- (* c i) t)))))
      (hash-set! cnt   prefix (+ (hash-ref cnt   prefix 0) 1))
      (hash-set! total prefix (+ (hash-ref total prefix 0) (+ i 1))))
    ans))
```

## Erlang

```erlang
-spec count_triplets([integer()]) -> integer().
count_triplets(Arr) ->
    {Result, _, _, _, _} =
        lists:foldl(
            fun(Elem, {Res, Pref, CMap, TMap, Idx}) ->
                NewPref = Pref bxor Elem,
                Count = maps:get(NewPref, CMap, 0),
                Total = maps:get(NewPref, TMap, 0),
                Contribution = Count * Idx - Total,
                NewRes = Res + Contribution,
                NewCMap = maps:put(NewPref, Count + 1, CMap),
                NewTMap = maps:put(NewPref, Total + (Idx + 1), TMap),
                {NewRes, NewPref, NewCMap, NewTMap, Idx + 1}
            end,
            {0, 0, #{0 => 1}, #{}, 0},
            Arr
        ),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_triplets(arr :: [integer]) :: integer
  def count_triplets(arr) do
    {ans, _, _, _} =
      Enum.reduce(Enum.with_index(arr), {0, 0, %{0 => 1}, %{0 => 0}}, fn {val, i},
                                                                          {acc, pref, cnt_map, sum_map} ->
        new_pref = pref ^^^ val
        idx = i + 1

        cnt = Map.get(cnt_map, new_pref, 0)
        sum_idx = Map.get(sum_map, new_pref, 0)

        acc2 = acc + cnt * (idx - 1) - sum_idx

        cnt_map2 = Map.update(cnt_map, new_pref, 1, &(&1 + 1))
        sum_map2 = Map.update(sum_map, new_pref, idx, &(&1 + idx))

        {acc2, new_pref, cnt_map2, sum_map2}
      end)

    ans
  end
end
```
