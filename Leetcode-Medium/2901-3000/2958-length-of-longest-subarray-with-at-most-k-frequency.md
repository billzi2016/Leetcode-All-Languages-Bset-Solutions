# 2958. Length of Longest Subarray With at Most K Frequency

## Cpp

```cpp
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        int left = 0, ans = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            ++freq[nums[right]];
            while (freq[nums[right]] > k) {
                --freq[nums[left]];
                ++left;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        int left = 0;
        int ans = 0;
        for (int right = 0; right < nums.length; right++) {
            int val = nums[right];
            freq.put(val, freq.getOrDefault(val, 0) + 1);
            while (freq.get(val) > k) {
                int leftVal = nums[left];
                freq.put(leftVal, freq.get(leftVal) - 1);
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        left = 0
        ans = 0
        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1
            while freq[val] > k:
                left_val = nums[left]
                freq[left_val] -= 1
                left += 1
            cur_len = right - left + 1
            if cur_len > ans:
                ans = cur_len
        return ans
```

## Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                y = nums[left]
                cnt[y] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## C

```c
#include <stdlib.h>

struct Node {
    long long key;
    int cnt;
    struct Node *next;
};

int maxSubarrayLength(int* nums, int numsSize, int k) {
    const int MOD = 200003;                 // prime > 2 * 10^5
    struct Node **table = (struct Node **)calloc(MOD, sizeof(struct Node *));
    int left = 0, ans = 0, over = 0;

    for (int right = 0; right < numsSize; ++right) {
        long long key = nums[right];
        unsigned idx = ((unsigned)key) % MOD;
        struct Node *node = table[idx];
        while (node && node->key != key) node = node->next;
        if (!node) {
            node = (struct Node *)malloc(sizeof(struct Node));
            node->key = key;
            node->cnt = 1;
            node->next = table[idx];
            table[idx] = node;
        } else {
            node->cnt++;
        }
        if (node->cnt == k + 1) over++;

        while (over > 0) {
            long long lkey = nums[left];
            unsigned lidx = ((unsigned)lkey) % MOD;
            struct Node *lnode = table[lidx];
            while (lnode && lnode->key != lkey) lnode = lnode->next;
            if (lnode->cnt == k + 1) over--;
            lnode->cnt--;
            left++;
        }

        int len = right - left + 1;
        if (len > ans) ans = len;
    }

    for (int i = 0; i < MOD; ++i) {
        struct Node *cur = table[i];
        while (cur) {
            struct Node *next = cur->next;
            free(cur);
            cur = next;
        }
    }
    free(table);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSubarrayLength(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < nums.Length; right++) {
            int val = nums[right];
            if (freq.ContainsKey(val))
                freq[val]++;
            else
                freq[val] = 1;

            while (freq[val] > k) {
                int leftVal = nums[left];
                freq[leftVal]--;
                if (freq[leftVal] == 0)
                    freq.Remove(leftVal);
                left++;
            }

            int currentLen = right - left + 1;
            if (currentLen > maxLen)
                maxLen = currentLen;
        }

        return maxLen;
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
var maxSubarrayLength = function(nums, k) {
    const freq = new Map();
    let left = 0;
    let best = 0;

    for (let right = 0; right < nums.length; right++) {
        const val = nums[right];
        freq.set(val, (freq.get(val) || 0) + 1);

        while ((freq.get(val) || 0) > k) {
            const lval = nums[left];
            freq.set(lval, freq.get(lval) - 1);
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
};
```

## Typescript

```typescript
function maxSubarrayLength(nums: number[], k: number): number {
    const freq = new Map<number, number>();
    let left = 0;
    let best = 0;

    for (let right = 0; right < nums.length; right++) {
        const val = nums[right];
        freq.set(val, (freq.get(val) ?? 0) + 1);

        while ((freq.get(val) ?? 0) > k) {
            const leftVal = nums[left];
            freq.set(leftVal, (freq.get(leftVal) ?? 0) - 1);
            left++;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
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
    function maxSubarrayLength($nums, $k) {
        $freq = [];
        $left = 0;
        $maxLen = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $val = $nums[$right];
            if (!isset($freq[$val])) {
                $freq[$val] = 0;
            }
            $freq[$val]++;
            while ($freq[$val] > $k) {
                $leftVal = $nums[$left];
                $freq[$leftVal]--;
                $left++;
            }
            $currentLen = $right - $left + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func maxSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        var left = 0
        var overK = 0
        var answer = 0
        
        for right in 0..<nums.count {
            let val = nums[right]
            freq[val, default: 0] += 1
            if freq[val]! == k + 1 {
                overK += 1
            }
            
            while overK > 0 {
                let leftVal = nums[left]
                if let cnt = freq[leftVal] {
                    if cnt == k + 1 {
                        overK -= 1
                    }
                    if cnt == 1 {
                        freq.removeValue(forKey: leftVal)
                    } else {
                        freq[leftVal] = cnt - 1
                    }
                }
                left += 1
            }
            
            answer = max(answer, right - left + 1)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubarrayLength(nums: IntArray, k: Int): Int {
        val freq = HashMap<Int, Int>()
        var left = 0
        var best = 0
        for (right in nums.indices) {
            val cur = nums[right]
            freq[cur] = (freq[cur] ?: 0) + 1
            while ((freq[cur] ?: 0) > k) {
                val leftVal = nums[left]
                freq[leftVal] = (freq[leftVal]!! - 1)
                if (freq[leftVal] == 0) freq.remove(leftVal)
                left++
            }
            best = kotlin.math.max(best, right - left + 1)
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxSubarrayLength(List<int> nums, int k) {
    int left = 0;
    int ans = 0;
    final Map<int, int> freq = {};
    for (int right = 0; right < nums.length; ++right) {
      int v = nums[right];
      freq[v] = (freq[v] ?? 0) + 1;
      while ((freq[v] ?? 0) > k) {
        int lv = nums[left];
        freq[lv] = (freq[lv]! - 1);
        left++;
      }
      int curLen = right - left + 1;
      if (curLen > ans) ans = curLen;
    }
    return ans;
  }
}
```

## Golang

```go
func maxSubarrayLength(nums []int, k int) int {
    freq := make(map[int]int)
    left, best := 0, 0
    for right, v := range nums {
        freq[v]++
        if freq[v] > k {
            for freq[v] > k {
                freq[nums[left]]--
                left++
            }
        }
        if cur := right - left + 1; cur > best {
            best = cur
        }
    }
    return best
}
```

## Ruby

```ruby
def max_subarray_length(nums, k)
  freq = Hash.new(0)
  left = 0
  best = 0

  nums.each_with_index do |num, right|
    freq[num] += 1
    while freq[num] > k
      freq[nums[left]] -= 1
      left += 1
    end
    length = right - left + 1
    best = length if length > best
  end

  best
end
```

## Scala

```scala
object Solution {
    def maxSubarrayLength(nums: Array[Int], k: Int): Int = {
        import scala.collection.mutable

        val freq = mutable.HashMap[Int, Int]()
        var left = 0
        var best = 0

        for (right <- nums.indices) {
            val v = nums(right)
            freq.update(v, freq.getOrElse(v, 0) + 1)

            while (freq(v) > k) {
                val lv = nums(left)
                freq.update(lv, freq(lv) - 1)
                if (freq(lv) == 0) freq.remove(lv)
                left += 1
            }

            best = math.max(best, right - left + 1)
        }

        best
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq: HashMap<i32, usize> = HashMap::new();
        let mut left: usize = 0;
        let mut best: usize = 0;
        let limit = k as usize;

        for right in 0..nums.len() {
            *freq.entry(nums[right]).or_insert(0) += 1;

            while *freq.get(&nums[right]).unwrap() > limit {
                if let Some(cnt) = freq.get_mut(&nums[left]) {
                    *cnt -= 1;
                }
                left += 1;
            }

            best = best.max(right - left + 1);
        }

        best as i32
    }
}
```

## Racket

```racket
(define/contract (max-subarray-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let ((freq (make-hash))
          (start 0)
          (ans 0))
      (for ([end (in-range n)])
        (define cur (vector-ref v end))
        (hash-set! freq cur (+ 1 (hash-ref freq cur 0)))
        ;; shrink window while any element exceeds k
        (let loop ()
          (when (> (hash-ref freq cur) k)
            (define left (vector-ref v start))
            (define left-count (hash-ref freq left))
            (if (= left-count 1)
                (hash-remove! freq left)
                (hash-set! freq left (- left-count 1)))
            (set! start (+ start 1))
            (loop)))
        (set! ans (max ans (+ 1 (- end start)))))
      ans)))
```

## Erlang

```erlang
-spec max_subarray_length(Nums :: [integer()], K :: integer()) -> integer().
max_subarray_length(Nums, K) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    {_, _, _, Ans} = lists:foldl(
        fun(Idx, {Start, Map, OverK, MaxLen}) ->
            Val = element(Idx + 1, Tuple),
            Count = maps:get(Val, Map, 0) + 1,
            Map1 = maps:put(Val, Count, Map),
            OverK1 = if Count == K + 1 -> OverK + 1; true -> OverK end,
            {NewStart, NewMap, NewOverK} = shrink_window(Start, Map1, OverK1, K, Tuple),
            Len = Idx - NewStart + 1,
            MaxLen2 = erlang:max(MaxLen, Len),
            {NewStart, NewMap, NewOverK, MaxLen2}
        end,
        {0, #{}, 0, 0},
        lists:seq(0, N - 1)
    ),
    Ans.

shrink_window(Start, Map, OverK, K, Tuple) when OverK =:= 0 ->
    {Start, Map, OverK};
shrink_window(Start, Map, OverK, K, Tuple) ->
    Val = element(Start + 1, Tuple),
    Count = maps:get(Val, Map),
    NewCount = Count - 1,
    Map2 = case NewCount of
        0 -> maps:remove(Val, Map);
        _ -> maps:put(Val, NewCount, Map)
    end,
    OverK2 = if Count == K + 1 -> OverK - 1; true -> OverK end,
    shrink_window(Start + 1, Map2, OverK2, K, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_subarray_length(nums :: [integer], k :: integer) :: integer
  def max_subarray_length(nums, k) do
    tuple = List.to_tuple(nums)
    len = tuple_size(tuple)

    {ans, _left, _freq} =
      Enum.reduce(0..(len - 1), {0, 0, %{}}, fn right, {ans, left, freq} ->
        val = elem(tuple, right)
        freq = Map.update(freq, val, 1, &(&1 + 1))

        {left, freq} = shrink(left, freq, tuple, k, val)

        ans = max(ans, right - left + 1)
        {ans, left, freq}
      end)

    ans
  end

  defp shrink(left, freq, tuple, k, cur_val) do
    if Map.get(freq, cur_val, 0) <= k do
      {left, freq}
    else
      left_val = elem(tuple, left)
      new_freq = Map.update!(freq, left_val, fn cnt -> cnt - 1 end)
      shrink(left + 1, new_freq, tuple, k, cur_val)
    end
  end
end
```
