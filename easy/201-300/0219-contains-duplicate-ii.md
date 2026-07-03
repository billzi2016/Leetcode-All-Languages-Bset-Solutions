# 0219. Contains Duplicate II

## Cpp

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(std::vector<int>& nums, int k) {
        if (k <= 0) return false;
        std::unordered_map<int, int> lastPos;
        for (int i = 0; i < (int)nums.size(); ++i) {
            auto it = lastPos.find(nums[i]);
            if (it != lastPos.end() && i - it->second <= k)
                return true;
            lastPos[nums[i]] = i;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        java.util.HashMap<Integer, Integer> lastIndex = new java.util.HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (lastIndex.containsKey(nums[i])) {
                int prev = lastIndex.get(nums[i]);
                if (i - prev <= k) {
                    return true;
                }
            }
            lastIndex.put(nums[i], i);
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_index = {}
        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True
            last_index[num] = i
        return False
```

## Python3

```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True
            last_index[num] = i
        return False
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int idx;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *p1 = (const Pair *)a;
    const Pair *p2 = (const Pair *)b;
    if (p1->val != p2->val)
        return (p1->val < p2->val) ? -1 : 1;
    return (p1->idx < p2->idx) ? -1 : (p1->idx > p2->idx);
}

bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
    if (numsSize <= 1)
        return false;

    Pair *arr = (Pair *)malloc(sizeof(Pair) * numsSize);
    if (!arr) return false; // allocation failure fallback

    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
    }

    qsort(arr, numsSize, sizeof(Pair), cmpPair);

    for (int i = 1; i < numsSize; ++i) {
        if (arr[i].val == arr[i - 1].val) {
            int diff = arr[i].idx - arr[i - 1].idx;
            if (diff <= k && diff >= 0)
                return true;
        }
    }

    free(arr);
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var window = new HashSet<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (window.Contains(nums[i])) return true;
            window.Add(nums[i]);
            if (i >= k) {
                window.Remove(nums[i - k]);
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const lastPos = new Map();
    for (let i = 0; i < nums.length; i++) {
        const val = nums[i];
        if (lastPos.has(val)) {
            if (i - lastPos.get(val) <= k) return true;
        }
        lastPos.set(val, i);
    }
    return false;
};
```

## Typescript

```typescript
function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const lastIndex = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        const val = nums[i];
        if (lastIndex.has(val)) {
            const prev = lastIndex.get(val)!;
            if (i - prev <= k) return true;
        }
        lastIndex.set(val, i);
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function containsNearbyDuplicate($nums, $k) {
        $lastPos = [];
        foreach ($nums as $i => $num) {
            if (isset($lastPos[$num])) {
                if ($i - $lastPos[$num] <= $k) {
                    return true;
                }
            }
            $lastPos[$num] = $i;
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
        var lastIndex = [Int: Int]()
        for (i, num) in nums.enumerated() {
            if let prev = lastIndex[num], i - prev <= k {
                return true
            }
            lastIndex[num] = i
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        val window = HashSet<Int>()
        for (i in nums.indices) {
            if (!window.add(nums[i])) return true
            if (window.size > k) {
                window.remove(nums[i - k])
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool containsNearbyDuplicate(List<int> nums, int k) {
    final Map<int, int> lastIndex = {};
    for (int i = 0; i < nums.length; i++) {
      int val = nums[i];
      if (lastIndex.containsKey(val)) {
        if (i - lastIndex[val]! <= k) return true;
      }
      lastIndex[val] = i;
    }
    return false;
  }
}
```

## Golang

```go
func containsNearbyDuplicate(nums []int, k int) bool {
    lastIdx := make(map[int]int)
    for i, v := range nums {
        if j, ok := lastIdx[v]; ok && i-j <= k {
            return true
        }
        lastIdx[v] = i
    }
    return false
}
```

## Ruby

```ruby
def contains_nearby_duplicate(nums, k)
  last_index = {}
  nums.each_with_index do |num, i|
    if last_index.key?(num) && i - last_index[num] <= k
      return true
    end
    last_index[num] = i
  end
  false
end
```

## Scala

```scala
object Solution {
    def containsNearbyDuplicate(nums: Array[Int], k: Int): Boolean = {
        val lastIdx = scala.collection.mutable.HashMap[Int, Int]()
        var i = 0
        while (i < nums.length) {
            val v = nums(i)
            lastIdx.get(v) match {
                case Some(prev) if i - prev <= k => return true
                case _ =>
            }
            lastIdx.update(v, i)
            i += 1
        }
        false
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut last_index: HashMap<i32, usize> = HashMap::new();
        let k_usize = k as usize;
        for (i, &num) in nums.iter().enumerate() {
            if let Some(&prev_i) = last_index.get(&num) {
                if i - prev_i <= k_usize {
                    return true;
                }
            }
            last_index.insert(num, i);
        }
        false
    }
}
```

## Racket

```racket
(define/contract (contains-nearby-duplicate nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let ((ht (make-hash)))
    (let loop ((lst nums) (i 0))
      (cond
        [(null? lst) #f]
        [else
         (define val (car lst))
         (define prev (hash-ref ht val #f))
         (if (and (not (eq? prev #f)) (<= (- i prev) k))
             #t
             (begin
               (hash-set! ht val i)
               (loop (cdr lst) (+ i 1))))]))))
```

## Erlang

```erlang
-module(solution).
-export([contains_nearby_duplicate/2]).

-spec contains_nearby_duplicate(Nums :: [integer()], K :: integer()) -> boolean().
contains_nearby_duplicate(Nums, K) ->
    loop(0, Nums, K, #{}).

loop(_Idx, [], _K, _Map) ->
    false;
loop(Idx, [H|T], K, Map) ->
    case maps:is_key(H, Map) of
        true ->
            Last = maps:get(H, Map),
            if
                Idx - Last =< K -> true;
                true -> loop(Idx + 1, T, K, maps:put(H, Idx, Map))
            end;
        false ->
            loop(Idx + 1, T, K, maps:put(H, Idx, Map))
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec contains_nearby_duplicate(nums :: [integer], k :: integer) :: boolean
  def contains_nearby_duplicate(nums, k) do
    check(nums, k, %{}, 0)
  end

  defp check([], _k, _map, _idx), do: false

  defp check([head | tail], k, map, idx) do
    case Map.get(map, head) do
      nil ->
        check(tail, k, Map.put(map, head, idx), idx + 1)

      prev_idx when idx - prev_idx <= k ->
        true

      _prev_idx ->
        check(tail, k, Map.put(map, head, idx), idx + 1)
    end
  end
end
```
