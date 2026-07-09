# 2404. Most Frequent Even Element

## Cpp

```cpp
class Solution {
public:
    int mostFrequentEven(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int x : nums) {
            if ((x & 1) == 0) ++freq[x];
        }
        int ans = -1, maxCnt = 0;
        for (const auto& p : freq) {
            int val = p.first, cnt = p.second;
            if (cnt > maxCnt || (cnt == maxCnt && val < ans)) {
                maxCnt = cnt;
                ans = val;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int mostFrequentEven(int[] nums) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int num : nums) {
            if ((num & 1) == 0) { // even
                freq.put(num, freq.getOrDefault(num, 0) + 1);
            }
        }
        if (freq.isEmpty()) return -1;
        int best = -1;
        int maxCount = 0;
        for (java.util.Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int val = entry.getKey();
            int cnt = entry.getValue();
            if (cnt > maxCount || (cnt == maxCount && val < best)) {
                maxCount = cnt;
                best = val;
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
        if not freq:
            return -1
        max_freq = max(freq.values())
        candidates = [num for num, cnt in freq.items() if cnt == max_freq]
        return min(candidates)
```

## Python3

```python
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
        if not freq:
            return -1
        max_count = max(freq.values())
        candidates = [num for num, cnt in freq.items() if cnt == max_count]
        return min(candidates)
```

## C

```c
#include <string.h>

int mostFrequentEven(int* nums, int numsSize) {
    static int freq[100001];
    memset(freq, 0, sizeof(freq));
    
    int bestCount = 0;
    int bestVal = -1;
    
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if ((v & 1) == 0) {               // even
            ++freq[v];
            if (freq[v] > bestCount || 
                (freq[v] == bestCount && (bestVal == -1 || v < bestVal))) {
                bestCount = freq[v];
                bestVal = v;
            }
        }
    }
    
    return bestVal;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MostFrequentEven(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var num in nums) {
            if ((num & 1) == 0) { // even
                if (freq.ContainsKey(num))
                    freq[num]++;
                else
                    freq[num] = 1;
            }
        }

        int bestFreq = 0;
        int answer = -1;

        foreach (var kvp in freq) {
            int val = kvp.Key;
            int count = kvp.Value;
            if (count > bestFreq || (count == bestFreq && (answer == -1 || val < answer))) {
                bestFreq = count;
                answer = val;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function(nums) {
    const freq = new Map();
    for (const num of nums) {
        if ((num & 1) === 0) {
            freq.set(num, (freq.get(num) || 0) + 1);
        }
    }
    let result = -1;
    let maxCount = 0;
    for (const [val, cnt] of freq.entries()) {
        if (cnt > maxCount || (cnt === maxCount && val < result)) {
            maxCount = cnt;
            result = val;
        }
    }
    return result;
};
```

## Typescript

```typescript
function mostFrequentEven(nums: number[]): number {
    const freq = new Map<number, number>();
    for (const num of nums) {
        if ((num & 1) === 0) { // even
            freq.set(num, (freq.get(num) ?? 0) + 1);
        }
    }
    let result = -1;
    let maxCount = 0;
    for (const [val, count] of freq.entries()) {
        if (count > maxCount || (count === maxCount && val < result)) {
            maxCount = count;
            result = val;
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function mostFrequentEven($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (($num & 1) === 0) { // even check
                if (!isset($freq[$num])) {
                    $freq[$num] = 0;
                }
                $freq[$num]++;
            }
        }

        $maxCount = 0;
        $answer = -1;

        foreach ($freq as $val => $cnt) {
            if ($cnt > $maxCount || ($cnt === $maxCount && $val < $answer)) {
                $maxCount = $cnt;
                $answer = $val;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func mostFrequentEven(_ nums: [Int]) -> Int {
        var freq = [Int: Int]()
        for num in nums where num % 2 == 0 {
            freq[num, default: 0] += 1
        }
        var maxCount = 0
        var answer = -1
        for (num, count) in freq {
            if count > maxCount || (count == maxCount && num < answer) {
                maxCount = count
                answer = num
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostFrequentEven(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (num in nums) {
            if ((num and 1) == 0) {
                freq[num] = (freq[num] ?: 0) + 1
            }
        }
        var best = -1
        var bestCount = 0
        for ((key, count) in freq) {
            if (count > bestCount || (count == bestCount && key < best)) {
                best = key
                bestCount = count
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int mostFrequentEven(List<int> nums) {
    final Map<int, int> freq = {};
    for (var v in nums) {
      if ((v & 1) == 0) {
        freq[v] = (freq[v] ?? 0) + 1;
      }
    }

    int best = -1;
    int bestCount = 0;
    for (var entry in freq.entries) {
      final val = entry.key;
      final cnt = entry.value;
      if (cnt > bestCount || (cnt == bestCount && val < best)) {
        bestCount = cnt;
        best = val;
      }
    }

    return best;
  }
}
```

## Golang

```go
func mostFrequentEven(nums []int) int {
    freq := make(map[int]int)
    for _, v := range nums {
        if v%2 == 0 {
            freq[v]++
        }
    }
    bestVal, bestFreq := -1, 0
    for val, cnt := range freq {
        if cnt > bestFreq || (cnt == bestFreq && val < bestVal) {
            bestFreq = cnt
            bestVal = val
        }
    }
    return bestVal
}
```

## Ruby

```ruby
def most_frequent_even(nums)
  freq = Hash.new(0)
  nums.each do |num|
    freq[num] += 1 if num.even?
  end
  return -1 if freq.empty?

  max_count = freq.values.max
  candidates = freq.select { |k, v| v == max_count }.keys
  candidates.min
end
```

## Scala

```scala
object Solution {
    def mostFrequentEven(nums: Array[Int]): Int = {
        import scala.collection.mutable
        val freq = mutable.Map[Int, Int]()
        for (x <- nums) {
            if ((x & 1) == 0) {
                freq.put(x, freq.getOrElse(x, 0) + 1)
            }
        }
        var ans = -1
        var maxCount = 0
        for ((num, cnt) <- freq) {
            if (cnt > maxCount || (cnt == maxCount && num < ans)) {
                maxCount = cnt
                ans = num
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn most_frequent_even(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for &num in nums.iter() {
            if num % 2 == 0 {
                *counts.entry(num).or_insert(0) += 1;
            }
        }
        let mut answer = -1;
        let mut best_cnt = 0;
        for (&val, &cnt) in counts.iter() {
            if cnt > best_cnt || (cnt == best_cnt && val < answer) {
                best_cnt = cnt;
                answer = val;
            }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (most-frequent-even nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)])
    (for ([x nums])
      (when (even? x)
        (hash-set! freq x (+ 1 (hash-ref freq x 0)))))
    (if (hash-empty? freq)
        -1
        (let-values ([(best-key best-count)
                      (for/fold ([bk -1] [bc 0]) ([kv (in-hash freq)])
                        (define k (car kv))
                        (define v (cdr kv))
                        (cond [(> v bc) (values k v)]
                              [(and (= v bc) (< k bk)) (values k v)]
                              [else (values bk bc)]))])
          best-key))))
```

## Erlang

```erlang
-spec most_frequent_even(Nums :: [integer()]) -> integer().
most_frequent_even(Nums) ->
    FreqMap = lists:foldl(
        fun(N, Acc) ->
            case N rem 2 of
                0 -> maps:update_with(N, fun(C) -> C + 1 end, 1, Acc);
                _ -> Acc
            end
        end,
        #{},
        Nums),
    case maps:size(FreqMap) of
        0 -> -1;
        _ ->
            {MaxCount, Candidates} = maps:fold(
                fun(Key, Count, {CurMax, CurList}) ->
                    if
                        Count > CurMax -> {Count, [Key]};
                        Count == CurMax -> {CurMax, [Key | CurList]};
                        true -> {CurMax, CurList}
                    end
                end,
                {0, []},
                FreqMap),
            lists:min(Candidates)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec most_frequent_even(nums :: [integer]) :: integer
  def most_frequent_even(nums) do
    freq =
      Enum.reduce(nums, %{}, fn x, acc ->
        if rem(x, 2) == 0 do
          Map.update(acc, x, 1, &(&1 + 1))
        else
          acc
        end
      end)

    if map_size(freq) == 0 do
      -1
    else
      {result, _} =
        Enum.reduce(freq, {nil, 0}, fn {k, v}, {best_key, best_cnt} ->
          cond do
            v > best_cnt -> {k, v}
            v == best_cnt and (best_key == nil or k < best_key) -> {k, v}
            true -> {best_key, best_cnt}
          end
        end)

      result
    end
  end
end
```
