# 1218. Longest Arithmetic Subsequence of Given Difference

## Cpp

```cpp
class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<long long, int> dp;
        dp.reserve(arr.size() * 2);
        int ans = 0;
        for (int x : arr) {
            long long prev = (long long)x - difference;
            int curLen = 1;
            auto it = dp.find(prev);
            if (it != dp.end()) curLen = it->second + 1;
            auto &ref = dp[(long long)x];
            if (curLen > ref) ref = curLen;
            ans = max(ans, curLen);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        java.util.HashMap<Integer, Integer> dp = new java.util.HashMap<>();
        int maxLen = 0;
        for (int num : arr) {
            int prev = num - difference;
            int curLen = dp.getOrDefault(prev, 0) + 1;
            int existing = dp.getOrDefault(num, 0);
            if (curLen > existing) {
                dp.put(num, curLen);
            }
            if (curLen > maxLen) {
                maxLen = curLen;
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        max_len = 0
        for x in arr:
            prev = x - difference
            cur_len = dp.get(prev, 0) + 1
            if cur_len > dp.get(x, 0):
                dp[x] = cur_len
            else:
                # keep existing longer subsequence ending at x
                cur_len = dp[x]
            if cur_len > max_len:
                max_len = cur_len
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        best = 0
        for x in arr:
            length = dp.get(x - difference, 0) + 1
            if length > dp.get(x, 0):
                dp[x] = length
            if length > best:
                best = length
        return best
```

## C

```c
#include <stdlib.h>

int longestSubsequence(int* arr, int arrSize, int difference) {
    const int OFFSET = 10000;
    const int RANGE = 20001; // from -10000 to 10000 inclusive
    int *dp = (int *)calloc(RANGE, sizeof(int));
    int ans = 0;

    for (int i = 0; i < arrSize; ++i) {
        int val = arr[i];
        int prev = val - difference;
        int len = 1;
        if (prev >= -10000 && prev <= 10000) {
            len = dp[prev + OFFSET] + 1;
        }
        int idx = val + OFFSET;
        if (len > dp[idx]) dp[idx] = len;
        if (dp[idx] > ans) ans = dp[idx];
    }

    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int LongestSubsequence(int[] arr, int difference) {
        var dp = new Dictionary<int, int>();
        int best = 0;
        foreach (int x in arr) {
            int prev = x - difference;
            int len = 1;
            if (dp.TryGetValue(prev, out int prevLen)) {
                len = prevLen + 1;
            }
            if (!dp.ContainsKey(x) || dp[x] < len) {
                dp[x] = len;
            }
            if (len > best) best = len;
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} difference
 * @return {number}
 */
var longestSubsequence = function(arr, difference) {
    const dp = new Map();
    let maxLen = 0;
    for (const num of arr) {
        const prev = dp.get(num - difference) || 0;
        const cur = prev + 1;
        dp.set(num, Math.max(dp.get(num) || 0, cur));
        if (cur > maxLen) maxLen = cur;
    }
    return maxLen;
};
```

## Typescript

```typescript
function longestSubsequence(arr: number[], difference: number): number {
    const dp = new Map<number, number>();
    let maxLen = 0;
    for (const val of arr) {
        const prevLen = dp.get(val - difference) ?? 0;
        const curLen = prevLen + 1;
        const stored = dp.get(val) ?? 0;
        if (curLen > stored) dp.set(val, curLen);
        if (curLen > maxLen) maxLen = curLen;
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $difference
     * @return Integer
     */
    function longestSubsequence($arr, $difference) {
        $dp = [];
        $maxLen = 0;
        foreach ($arr as $value) {
            $prev = $value - $difference;
            $len = isset($dp[$prev]) ? $dp[$prev] + 1 : 1;
            if (!isset($dp[$value]) || $len > $dp[$value]) {
                $dp[$value] = $len;
            }
            if ($dp[$value] > $maxLen) {
                $maxLen = $dp[$value];
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestSubsequence(_ arr: [Int], _ difference: Int) -> Int {
        var dp = [Int: Int]()
        var maxLen = 0
        for value in arr {
            let prev = value - difference
            let curLen = (dp[prev] ?? 0) + 1
            if let existing = dp[value] {
                if curLen > existing {
                    dp[value] = curLen
                }
            } else {
                dp[value] = curLen
            }
            if curLen > maxLen { maxLen = curLen }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSubsequence(arr: IntArray, difference: Int): Int {
        val dp = HashMap<Int, Int>()
        var maxLen = 0
        for (value in arr) {
            val prevLen = dp.getOrDefault(value - difference, 0)
            val curLen = prevLen + 1
            if (curLen > dp.getOrDefault(value, 0)) {
                dp[value] = curLen
            }
            if (curLen > maxLen) maxLen = curLen
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestSubsequence(List<int> arr, int difference) {
    final Map<int, int> dp = {};
    int maxLen = 0;
    for (final x in arr) {
      final prev = x - difference;
      final curLen = (dp[prev] ?? 0) + 1;
      if ((dp[x] ?? 0) < curLen) {
        dp[x] = curLen;
      }
      if (curLen > maxLen) {
        maxLen = curLen;
      }
    }
    return maxLen;
  }
}
```

## Golang

```go
func longestSubsequence(arr []int, difference int) int {
	dp := make(map[int]int)
	maxLen := 0
	for _, v := range arr {
		prev := v - difference
		cur := 1
		if val, ok := dp[prev]; ok {
			cur = val + 1
		}
		if existing, ok := dp[v]; !ok || cur > existing {
			dp[v] = cur
		}
		if cur > maxLen {
			maxLen = cur
		}
	}
	return maxLen
}
```

## Ruby

```ruby
def longest_subsequence(arr, difference)
  dp = {}
  best = 0
  arr.each do |x|
    cur_len = (dp[x - difference] || 0) + 1
    dp[x] = cur_len if cur_len > (dp[x] || 0)
    best = cur_len if cur_len > best
  end
  best
end
```

## Scala

```scala
object Solution {
    def longestSubsequence(arr: Array[Int], difference: Int): Int = {
        val dp = scala.collection.mutable.HashMap[Int, Int]()
        var maxLen = 0
        for (v <- arr) {
            val prevLen = dp.getOrElse(v - difference, 0)
            val curLen = prevLen + 1
            dp.update(v, math.max(dp.getOrElse(v, 0), curLen))
            if (curLen > maxLen) maxLen = curLen
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_subsequence(arr: Vec<i32>, difference: i32) -> i32 {
        use std::collections::HashMap;
        let mut dp: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        for &x in arr.iter() {
            let prev_len = dp.get(&(x - difference)).cloned().unwrap_or(0);
            let cur_len = prev_len + 1;
            let entry = dp.entry(x).or_insert(0);
            if cur_len > *entry {
                *entry = cur_len;
            }
            if cur_len > ans {
                ans = cur_len;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (longest-subsequence arr difference)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([dp (make-hash)]
        [maxlen 0])
    (for ([x arr])
      (let* ((prev (- x difference))
             (prev-len (hash-ref dp prev 0))
             (cur (+ prev-len 1)))
        (define existing (hash-ref dp x 0))
        (when (> cur existing)
          (hash-set! dp x cur))
        (when (> cur maxlen)
          (set! maxlen cur))))
    maxlen))
```

## Erlang

```erlang
-module(solution).
-export([longest_subsequence/2]).

-spec longest_subsequence(Arr :: [integer()], Difference :: integer()) -> integer().
longest_subsequence(Arr, Diff) ->
    longest_subsequence(Arr, Diff, #{}, 0).

%% internal recursive helper with accumulator map and current max
longest_subsequence([], _Diff, _Map, Max) ->
    Max;
longest_subsequence([X|Rest], Diff, Map, Max) ->
    Prev = X - Diff,
    LenPrev = maps:get(Prev, Map, 0),
    CurrLen = LenPrev + 1,
    Existing = maps:get(X, Map, 0),
    NewLen = case CurrLen > Existing of
        true -> CurrLen;
        false -> Existing
    end,
    NewMap = maps:put(X, NewLen, Map),
    NewMax = case NewLen > Max of
        true -> NewLen;
        false -> Max
    end,
    longest_subsequence(Rest, Diff, NewMap, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_subsequence(arr :: [integer], difference :: integer) :: integer
  def longest_subsequence(arr, difference) do
    {max_len, _} =
      Enum.reduce(arr, {0, %{}}, fn x, {max_len, dp} ->
        prev = Map.get(dp, x - difference, 0)
        cur = prev + 1
        new_dp = Map.put(dp, x, cur)
        new_max = if cur > max_len, do: cur, else: max_len
        {new_max, new_dp}
      end)

    max_len
  end
end
```
