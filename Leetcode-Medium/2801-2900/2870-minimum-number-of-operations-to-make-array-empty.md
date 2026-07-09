# 2870. Minimum Number of Operations to Make Array Empty

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int,int> cnt;
        for (int x : nums) ++cnt[x];
        long long ans = 0;
        for (auto &p : cnt) {
            int c = p.second;
            if (c == 1) return -1;
            ans += (c + 2) / 3; // ceil division by 3
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        int operations = 0;
        for (int count : freq.values()) {
            if (count == 1) {
                return -1;
            }
            operations += (count + 2) / 3; // ceil division by 3
        }
        return operations;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(nums)
        ans = 0
        for c in cnt.values():
            if c == 1:
                return -1
            ans += (c + 2) // 3  # ceil division by 3
        return ans
```

## Python3

```python
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = 0
        for c in freq.values():
            if c == 1:
                return -1
            ans += (c + 2) // 3  # ceil division by 3
        return ans
```

## C

```c
#include <stdlib.h>

int minOperations(int* nums, int numsSize) {
    const int MAX_VAL = 1000000;
    int *cnt = (int *)calloc(MAX_VAL + 1, sizeof(int));
    if (!cnt) return -1;  // allocation failure, treat as impossible

    int maxV = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        cnt[v]++;
        if (v > maxV) maxV = v;
    }

    long long ops = 0;
    for (int v = 0; v <= maxV; ++v) {
        int c = cnt[v];
        if (c == 0) continue;
        if (c == 1) {
            free(cnt);
            return -1;
        }
        ops += (c + 2) / 3;   // ceil(c / 3)
    }

    free(cnt);
    return (int)ops;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinOperations(int[] nums)
    {
        var freq = new System.Collections.Generic.Dictionary<int, int>();
        foreach (int x in nums)
        {
            if (freq.ContainsKey(x))
                freq[x]++;
            else
                freq[x] = 1;
        }

        long operations = 0;
        foreach (int count in freq.Values)
        {
            if (count == 1)
                return -1;
            operations += (count + 2) / 3; // ceil(count / 3)
        }

        return (int)operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const freq = new Map();
    for (const x of nums) {
        freq.set(x, (freq.get(x) || 0) + 1);
    }
    let ans = 0;
    for (const cnt of freq.values()) {
        if (cnt === 1) return -1;
        ans += Math.ceil(cnt / 3);
    }
    return ans;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    const freq = new Map<number, number>();
    for (const x of nums) {
        freq.set(x, (freq.get(x) ?? 0) + 1);
    }
    let ops = 0;
    for (const count of freq.values()) {
        if (count === 1) return -1;
        ops += Math.ceil(count / 3);
    }
    return ops;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }
        $ans = 0;
        foreach ($freq as $count) {
            if ($count == 1) {
                return -1;
            }
            $ans += intdiv($count + 2, 3); // ceil(count / 3)
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var freq = [Int: Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        var operations = 0
        for count in freq.values {
            if count == 1 { return -1 }
            operations += (count + 2) / 3
        }
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (v in nums) {
            freq[v] = freq.getOrDefault(v, 0) + 1
        }
        var ans = 0
        for (c in freq.values) {
            if (c == 1) return -1
            ans += (c + 2) / 3
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    final Map<int, int> freq = {};
    for (var num in nums) {
      freq[num] = (freq[num] ?? 0) + 1;
    }
    int ans = 0;
    for (var count in freq.values) {
      if (count == 1) return -1;
      ans += (count + 2) ~/ 3; // ceil division by 3
    }
    return ans;
  }
}
```

## Golang

```go
func minOperations(nums []int) int {
    freq := make(map[int]int)
    for _, v := range nums {
        freq[v]++
    }
    ops := 0
    for _, c := range freq {
        if c == 1 {
            return -1
        }
        ops += (c + 2) / 3
    }
    return ops
}
```

## Ruby

```ruby
def min_operations(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  ans = 0
  freq.each_value do |c|
    return -1 if c == 1
    ans += (c + 2) / 3
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        for (x <- nums) {
            freq(x) = freq.getOrElse(x, 0) + 1
        }
        var ops = 0
        for ((_, cnt) <- freq) {
            if (cnt == 1) return -1
            ops += (cnt + 2) / 3
        }
        ops
    }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for num in nums {
            *freq.entry(num).or_insert(0) += 1;
        }
        let mut ans: usize = 0;
        for &c in freq.values() {
            if c == 1 {
                return -1;
            }
            ans += (c + 2) / 3; // ceil division by 3
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((cnts (make-hash)))
    (for ([x nums])
      (hash-update! cnts x add1 0))
    (let ((impossible #f) (total 0))
      (for ([c (in-hash-values cnts)])
        (cond [(= c 1) (set! impossible #t)]
              [else (set! total (+ total (quotient (+ c 2) 3)))]))
      (if impossible -1 total))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    CountMap = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Nums
    ),
    Values = maps:values(CountMap),
    min_operations_counts(Values, 0).

min_operations_counts([], Ans) ->
    Ans;
min_operations_counts([C|_Rest], _Ans) when C == 1 ->
    -1;
min_operations_counts([C|Rest], Ans) ->
    NewAns = Ans + ((C + 2) div 3),
    min_operations_counts(Rest, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    freq = Enum.frequencies(nums)

    Enum.reduce_while(freq, 0, fn {_k, v}, acc ->
      if v == 1 do
        {:halt, -1}
      else
        {:cont, acc + div(v + 2, 3)}
      end
    end)
  end
end
```
