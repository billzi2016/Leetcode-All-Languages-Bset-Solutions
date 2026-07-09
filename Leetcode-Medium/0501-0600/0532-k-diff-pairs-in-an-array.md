# 0532. K-diff Pairs in an Array

## Cpp

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (k < 0) return 0;
        unordered_map<int,int> cnt;
        for (int x : nums) ++cnt[x];
        int ans = 0;
        if (k == 0) {
            for (auto &p : cnt) {
                if (p.second > 1) ++ans;
            }
        } else {
            for (auto &p : cnt) {
                if (cnt.find(p.first + k) != cnt.end()) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findPairs(int[] nums, int k) {
        if (k < 0) return 0;
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        int count = 0;
        if (k == 0) {
            for (int val : freq.values()) {
                if (val > 1) count++;
            }
        } else {
            for (int key : freq.keySet()) {
                if (freq.containsKey(key + k)) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Python

```python
import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        freq = collections.Counter(nums)
        if k == 0:
            return sum(1 for v in freq.values() if v > 1)
        num_set = set(freq.keys())
        return sum(1 for x in num_set if x + k in num_set)
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        freq = Counter(nums)
        if k == 0:
            return sum(1 for v in freq.values() if v > 1)
        count = 0
        for num in freq:
            if num + k in freq:
                count += 1
        return count
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return (ai > bi) - (ai < bi);
}

int findPairs(int* nums, int numsSize, int k) {
    if (k < 0 || numsSize < 2) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int i = 0, j = 1, count = 0;
    while (i < numsSize && j < numsSize) {
        if (i == j) { ++j; continue; }
        long diff = (long)nums[j] - (long)nums[i];
        if (diff == k) {
            ++count;
            int vi = nums[i];
            while (i < numsSize && nums[i] == vi) ++i;
            int vj = nums[j];
            while (j < numsSize && nums[j] == vj) ++j;
        } else if (diff < k) {
            ++j;
        } else {
            ++i;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindPairs(int[] nums, int k)
    {
        if (k < 0) return 0;

        var freq = new Dictionary<int, int>();
        foreach (var num in nums)
        {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        int result = 0;
        if (k == 0)
        {
            foreach (var kvp in freq)
            {
                if (kvp.Value > 1) result++;
            }
        }
        else
        {
            foreach (var key in freq.Keys)
            {
                if (freq.ContainsKey(key + k)) result++;
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
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    if (k < 0) return 0;
    const freq = new Map();
    for (const n of nums) {
        freq.set(n, (freq.get(n) || 0) + 1);
    }
    let ans = 0;
    if (k === 0) {
        for (const cnt of freq.values()) {
            if (cnt > 1) ans++;
        }
    } else {
        const set = new Set(freq.keys());
        for (const n of set) {
            if (set.has(n + k)) ans++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function findPairs(nums: number[], k: number): number {
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }
    let count = 0;
    if (k === 0) {
        for (const cnt of freq.values()) {
            if (cnt > 1) count++;
        }
    } else {
        for (const num of freq.keys()) {
            if (freq.has(num + k)) count++;
        }
    }
    return count;
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
    function findPairs($nums, $k) {
        if ($k < 0) return 0;
        $freq = [];
        foreach ($nums as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }

        $count = 0;
        if ($k == 0) {
            foreach ($freq as $val => $cnt) {
                if ($cnt > 1) {
                    $count++;
                }
            }
        } else {
            foreach ($freq as $val => $_) {
                $target = $val + $k;
                if (isset($freq[$target])) {
                    $count++;
                }
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func findPairs(_ nums: [Int], _ k: Int) -> Int {
        guard k >= 0 else { return 0 }
        var freq = [Int: Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        var count = 0
        if k == 0 {
            for (_, v) in freq where v > 1 {
                count += 1
            }
        } else {
            for (num, _) in freq {
                if freq[num + k] != nil {
                    count += 1
                }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPairs(nums: IntArray, k: Int): Int {
        if (k < 0) return 0
        val freq = HashMap<Int, Int>()
        for (num in nums) {
            freq[num] = (freq[num] ?: 0) + 1
        }
        var count = 0
        if (k == 0) {
            for ((_, v) in freq) {
                if (v > 1) count++
            }
        } else {
            for (key in freq.keys) {
                if (freq.containsKey(key + k)) count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int findPairs(List<int> nums, int k) {
    if (k < 0) return 0;
    final Map<int, int> freq = {};
    for (final n in nums) {
      freq[n] = (freq[n] ?? 0) + 1;
    }
    int count = 0;
    if (k == 0) {
      freq.forEach((_, v) {
        if (v > 1) count++;
      });
    } else {
      for (final key in freq.keys) {
        if (freq.containsKey(key + k)) count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func findPairs(nums []int, k int) int {
	if k < 0 {
		return 0
	}
	freq := make(map[int]int)
	for _, v := range nums {
		freq[v]++
	}
	count := 0
	if k == 0 {
		for _, c := range freq {
			if c > 1 {
				count++
			}
		}
	} else {
		for num := range freq {
			if _, ok := freq[num+k]; ok {
				count++
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def find_pairs(nums, k)
  return 0 if k < 0
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  count = 0
  if k == 0
    freq.each_value { |v| count += 1 if v > 1 }
  else
    freq.each_key do |key|
      count += 1 if freq.key?(key + k)
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def findPairs(nums: Array[Int], k: Int): Int = {
        if (k < 0) return 0
        val freq = scala.collection.mutable.Map[Int, Int]()
        for (num <- nums) {
            freq(num) = freq.getOrElse(num, 0) + 1
        }
        var count = 0
        if (k == 0) {
            for ((_, c) <- freq) {
                if (c > 1) count += 1
            }
        } else {
            val set = freq.keySet
            for (num <- set) {
                if (set.contains(num + k)) count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn find_pairs(nums: Vec<i32>, k: i32) -> i32 {
        if k < 0 {
            return 0;
        }
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for num in nums {
            *freq.entry(num).or_insert(0) += 1;
        }

        let mut count = 0i32;
        if k == 0 {
            for &v in freq.values() {
                if v > 1 {
                    count += 1;
                }
            }
        } else {
            for (&key, _) in freq.iter() {
                if freq.contains_key(&(key + k)) {
                    count += 1;
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (find-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([freq (make-hash)])
    (for ([n nums])
      (hash-set! freq n (+ 1 (hash-ref freq n 0))))
    (if (= k 0)
        (let loop ((keys (hash-keys freq)) (cnt 0))
          (cond [(null? keys) cnt]
                [else (define key (car keys))
                      (loop (cdr keys)
                            (if (> (hash-ref freq key) 1) (+ cnt 1) cnt))]))
        (let loop ((keys (hash-keys freq)) (cnt 0))
          (cond [(null? keys) cnt]
                [else (define key (car keys))
                      (loop (cdr keys)
                            (if (hash-has-key? freq (+ key k)) (+ cnt 1) cnt))])))))
```

## Erlang

```erlang
-spec find_pairs([integer()], integer()) -> integer().
find_pairs(Nums, K) ->
    Freq = build_freq_map(Nums, #{}),
    case K of
        0 ->
            maps:fold(fun(_Key, Cnt, Acc) ->
                if Cnt > 1 -> Acc + 1; true -> Acc end
            end, 0, Freq);
        _ when K > 0 ->
            maps:fold(fun(Key, _Cnt, Acc) ->
                case maps:is_key(Key + K, Freq) of
                    true -> Acc + 1;
                    false -> Acc
                end
            end, 0, Freq)
    end.

build_freq_map([], M) -> M;
build_freq_map([H|T], M) ->
    NewM = maps:update_with(H,
        fun(C) -> C + 1 end,
        1,
        M),
    build_freq_map(T, NewM).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_pairs(nums :: [integer], k :: integer) :: integer
  def find_pairs(nums, k) do
    freq =
      Enum.reduce(nums, %{}, fn num, acc ->
        Map.update(acc, num, 1, &(&1 + 1))
      end)

    if k == 0 do
      Enum.count(freq, fn {_num, cnt} -> cnt > 1 end)
    else
      Enum.reduce(freq, 0, fn {num, _cnt}, acc ->
        if Map.has_key?(freq, num + k), do: acc + 1, else: acc
      end)
    end
  end
end
```
