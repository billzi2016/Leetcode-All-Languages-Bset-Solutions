# 2190. Most Frequent Number Following Key In an Array

## Cpp

```cpp
class Solution {
public:
    int mostFrequent(vector<int>& nums, int key) {
        unordered_map<int,int> cnt;
        for (int i = 0; i + 1 < (int)nums.size(); ++i) {
            if (nums[i] == key) {
                ++cnt[nums[i+1]];
            }
        }
        int bestTarget = -1, bestFreq = -1;
        for (auto& p : cnt) {
            if (p.second > bestFreq) {
                bestFreq = p.second;
                bestTarget = p.first;
            }
        }
        return bestTarget;
    }
};
```

## Java

```java
class Solution {
    public int mostFrequent(int[] nums, int key) {
        int[] count = new int[1001];
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == key) {
                count[nums[i + 1]]++;
            }
        }
        int maxFreq = 0;
        int result = 0;
        for (int v = 1; v < count.length; v++) {
            if (count[v] > maxFreq) {
                maxFreq = count[v];
                result = v;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        counts = {}
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == key:
                nxt = nums[i + 1]
                counts[nxt] = counts.get(nxt, 0) + 1

        best_target = None
        max_cnt = -1
        for target, cnt in counts.items():
            if cnt > max_cnt:
                max_cnt = cnt
                best_target = target
        return best_target
```

## Python3

```python
from typing import List
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                nxt = nums[i + 1]
                freq[nxt] = freq.get(nxt, 0) + 1
        # Find the target with maximum count (unique per problem statement)
        max_target = None
        max_count = -1
        for target, cnt in freq.items():
            if cnt > max_count:
                max_count = cnt
                max_target = target
        return max_target
```

## C

```c
int mostFrequent(int* nums, int numsSize, int key) {
    int cnt[1001] = {0};
    for (int i = 0; i < numsSize - 1; ++i) {
        if (nums[i] == key) {
            int t = nums[i + 1];
            cnt[t]++;
        }
    }
    int ans = 0, maxc = 0;
    for (int v = 1; v <= 1000; ++v) {
        if (cnt[v] > maxc) {
            maxc = cnt[v];
            ans = v;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MostFrequent(int[] nums, int key) {
        var freq = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] == key) {
                int target = nums[i + 1];
                if (freq.ContainsKey(target))
                    freq[target]++;
                else
                    freq[target] = 1;
            }
        }

        int result = -1;
        int maxCount = -1;
        foreach (var kvp in freq) {
            if (kvp.Value > maxCount) {
                maxCount = kvp.Value;
                result = kvp.Key;
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} key
 * @return {number}
 */
var mostFrequent = function(nums, key) {
    const freq = new Map();
    for (let i = 1; i < nums.length; ++i) {
        if (nums[i - 1] === key) {
            const t = nums[i];
            freq.set(t, (freq.get(t) || 0) + 1);
        }
    }
    let bestCount = -1;
    let answer = -1;
    for (const [num, cnt] of freq.entries()) {
        if (cnt > bestCount) {
            bestCount = cnt;
            answer = num;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function mostFrequent(nums: number[], key: number): number {
    const freq = new Map<number, number>();
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] === key) {
            const nxt = nums[i + 1];
            freq.set(nxt, (freq.get(nxt) ?? 0) + 1);
        }
    }
    let answer = -1;
    let maxCount = -1;
    for (const [target, count] of freq.entries()) {
        if (count > maxCount) {
            maxCount = count;
            answer = target;
        }
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $key
     * @return Integer
     */
    function mostFrequent($nums, $key) {
        $counts = [];
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] === $key) {
                $target = $nums[$i + 1];
                if (!isset($counts[$target])) {
                    $counts[$target] = 0;
                }
                $counts[$target]++;
            }
        }

        $maxCount = -1;
        $answer = null;
        foreach ($counts as $val => $cnt) {
            if ($cnt > $maxCount) {
                $maxCount = $cnt;
                $answer = (int)$val;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func mostFrequent(_ nums: [Int], _ key: Int) -> Int {
        var freq = [Int: Int]()
        for i in 0..<(nums.count - 1) {
            if nums[i] == key {
                let target = nums[i + 1]
                freq[target, default: 0] += 1
            }
        }
        var result = 0
        var maxCount = -1
        for (num, count) in freq {
            if count > maxCount {
                maxCount = count
                result = num
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostFrequent(nums: IntArray, key: Int): Int {
        val maxVal = 1000
        val count = IntArray(maxVal + 1)
        for (i in 0 until nums.size - 1) {
            if (nums[i] == key) {
                count[nums[i + 1]]++
            }
        }
        var result = 0
        var best = -1
        for (v in 1..maxVal) {
            if (count[v] > best) {
                best = count[v]
                result = v
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int mostFrequent(List<int> nums, int key) {
    final Map<int, int> count = {};
    for (int i = 0; i < nums.length - 1; ++i) {
      if (nums[i] == key) {
        int nxt = nums[i + 1];
        count[nxt] = (count[nxt] ?? 0) + 1;
      }
    }
    int result = -1;
    int maxFreq = -1;
    count.forEach((target, freq) {
      if (freq > maxFreq) {
        maxFreq = freq;
        result = target;
      }
    });
    return result;
  }
}
```

## Golang

```go
func mostFrequent(nums []int, key int) int {
	cnt := make(map[int]int)
	for i := 0; i+1 < len(nums); i++ {
		if nums[i] == key {
			cnt[nums[i+1]]++
		}
	}
	bestVal, bestCnt := 0, -1
	for v, c := range cnt {
		if c > bestCnt {
			bestCnt = c
			bestVal = v
		}
	}
	return bestVal
}
```

## Ruby

```ruby
def most_frequent(nums, key)
  counts = Hash.new(0)
  (0...nums.length - 1).each do |i|
    counts[nums[i + 1]] += 1 if nums[i] == key
  end
  result = nil
  max_cnt = -1
  counts.each do |num, cnt|
    if cnt > max_cnt
      max_cnt = cnt
      result = num
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def mostFrequent(nums: Array[Int], key: Int): Int = {
        val counts = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        for (i <- 0 until nums.length - 1) {
            if (nums(i) == key) {
                val target = nums(i + 1)
                counts(target) += 1
            }
        }
        var bestTarget = -1
        var bestCount = -1
        for ((target, cnt) <- counts) {
            if (cnt > bestCount) {
                bestCount = cnt
                bestTarget = target
            }
        }
        bestTarget
    }
}
```

## Rust

```rust
impl Solution {
    pub fn most_frequent(nums: Vec<i32>, key: i32) -> i32 {
        use std::collections::HashMap;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() - 1 {
            if nums[i] == key {
                *cnt.entry(nums[i + 1]).or_insert(0) += 1;
            }
        }
        let mut best_target = 0;
        let mut best_count = -1;
        for (target, c) in cnt {
            if c > best_count {
                best_count = c;
                best_target = target;
            }
        }
        best_target
    }
}
```

## Racket

```racket
(define/contract (most-frequent nums key)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([counts (make-hash)])
    (for ([i (in-range (- (length nums) 1))])
      (when (= (list-ref nums i) key)
        (define target (list-ref nums (+ i 1)))
        (hash-set! counts target (add1 (hash-ref counts target 0)))))
    (define max-key #f)
    (define max-count -1)
    (for ([k (in-hash-keys counts)])
      (define c (hash-ref counts k))
      (when (> c max-count)
        (set! max-count c)
        (set! max-key k)))
    max-key))
```

## Erlang

```erlang
-module(solution).
-export([most_frequent/2]).

-spec most_frequent(Nums :: [integer()], Key :: integer()) -> integer().
most_frequent(Nums, Key) ->
    Map = count_pairs(Nums, Key, #{}),
    {Ans,_} = maps:fold(
        fun(K,V,{Mk,Mv}) ->
            if V > Mv -> {K,V}; true -> {Mk,Mv} end
        end,
        {0,-1},
        Map),
    Ans.

count_pairs([], _Key, Map) -> Map;
count_pairs([_], _Key, Map) -> Map;
count_pairs([Prev, Curr | Rest], Key, Map) ->
    NewMap = case Prev == Key of
                true -> maps:update_with(Curr,
                                          fun(V) -> V + 1 end,
                                          1,
                                          Map);
                false -> Map
            end,
    count_pairs([Curr|Rest], Key, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec most_frequent(nums :: [integer], key :: integer) :: integer
  def most_frequent(nums, key) do
    counts = count_follow(nums, key, %{})
    {target, _} = Enum.max_by(counts, fn {_k, v} -> v end)
    target
  end

  defp count_follow([], _key, acc), do: acc
  defp count_follow([_], _key, acc), do: acc
  defp count_follow([a, b | rest], key, acc) do
    new_acc =
      if a == key do
        Map.update(acc, b, 1, &(&1 + 1))
      else
        acc
      end

    count_follow([b | rest], key, new_acc)
  end
end
```
