# 2501. Longest Square Streak in an Array

## Cpp

```cpp
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        const int LIMIT = 100000;
        unordered_set<int> present(nums.begin(), nums.end());
        int best = 0;
        for (int start : nums) {
            long long cur = start;
            int len = 0;
            while (cur <= LIMIT && present.count((int)cur)) {
                ++len;
                long long nxt = cur * cur;
                if (nxt > LIMIT) break;
                cur = nxt;
            }
            best = max(best, len);
        }
        return best >= 2 ? best : -1;
    }
};
```

## Java

```java
class Solution {
    public int longestSquareStreak(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int v : nums) {
            set.add(v);
        }
        int best = 0;
        for (int start : nums) {
            long cur = start;
            int len = 0;
            while (set.contains((int) cur)) {
                len++;
                long next = cur * cur;
                if (next > 100000L) break;
                cur = next;
            }
            best = Math.max(best, len);
        }
        return best >= 2 ? best : -1;
    }
}
```

## Python

```python
class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        if not num_set:
            return -1
        limit = max(num_set)
        best = 0
        for start in num_set:
            cur = start
            length = 0
            while cur in num_set:
                length += 1
                nxt = cur * cur
                if nxt > limit:
                    break
                cur = nxt
            if length > best:
                best = length
        return best if best >= 2 else -1
```

## Python3

```python
from typing import List
import math

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        present = set(nums)
        max_len = 0
        limit = 10**5

        for x in nums:
            # skip if x can be reached from a smaller number (i.e., it's not a start of a streak)
            r = math.isqrt(x)
            if r * r == x and r in present:
                continue

            cur = x
            length = 0
            while cur in present:
                length += 1
                nxt = cur * cur
                if nxt > limit:
                    break
                cur = nxt

            max_len = max(max_len, length)

        return max_len if max_len >= 2 else -1
```

## C

```c
int longestSquareStreak(int* nums, int numsSize) {
    const int MAXV = 100000;
    static char present[100001];
    // reset presence array (LeetCode runs each test in fresh process, but ensure clean)
    for (int i = 0; i <= MAXV; ++i) present[i] = 0;

    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] <= MAXV) present[nums[i]] = 1;
    }

    int longest = 0;
    for (int i = 0; i < numsSize; ++i) {
        int cur = nums[i];
        if (!present[cur]) continue; // should always be true
        int len = 0;
        while (cur <= MAXV && present[cur]) {
            ++len;
            long long nxt = (long long)cur * cur;
            if (nxt > MAXV) break;
            cur = (int)nxt;
        }
        if (len > longest) longest = len;
    }

    return (longest >= 2) ? longest : -1;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestSquareStreak(int[] nums) {
        var present = new HashSet<int>(nums);
        int longest = 0;
        const int MAX = 100000;

        foreach (int start in nums) {
            long cur = start;
            int length = 0;
            while (present.Contains((int)cur)) {
                length++;
                long next = cur * cur;
                if (next > MAX) break;
                cur = next;
            }
            if (length > longest) longest = length;
        }

        return longest >= 2 ? longest : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSquareStreak = function(nums) {
    // Sort to ensure any possible root is processed before its square
    nums.sort((a, b) => a - b);
    
    const dp = new Map(); // number -> length of streak ending at this number
    let best = 1;
    
    for (const num of nums) {
        const root = Math.floor(Math.sqrt(num));
        if (root * root === num && dp.has(root)) {
            dp.set(num, dp.get(root) + 1);
        } else {
            dp.set(num, 1);
        }
        best = Math.max(best, dp.get(num));
    }
    
    return best >= 2 ? best : -1;
};
```

## Typescript

```typescript
function longestSquareStreak(nums: number[]): number {
    const numSet = new Set<number>(nums);
    let maxLen = 0;
    for (const start of nums) {
        let cur = start;
        let len = 1;
        while (true) {
            const next = cur * cur;
            if (next > 100000) break;
            if (!numSet.has(next)) break;
            cur = next;
            len++;
        }
        if (len > maxLen) maxLen = len;
    }
    return maxLen >= 2 ? maxLen : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSquareStreak($nums) {
        // Build a hash set for O(1) existence checks
        $set = [];
        foreach ($nums as $v) {
            $set[$v] = true;
        }

        $maxLen = 0;
        $limit = 100000; // maximum possible value according to constraints

        foreach ($nums as $start) {
            $len = 0;
            $cur = $start;

            while (isset($set[$cur])) {
                $len++;
                // compute next square, stop if it exceeds limit
                $next = $cur * $cur;
                if ($next > $limit) {
                    break;
                }
                $cur = $next;
            }

            if ($len > $maxLen) {
                $maxLen = $len;
            }
        }

        return $maxLen < 2 ? -1 : $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestSquareStreak(_ nums: [Int]) -> Int {
        let numSet = Set(nums)
        var maxLen = 0
        for start in nums {
            var cur = start
            var length = 0
            while numSet.contains(cur) {
                length += 1
                let sq = Int64(cur) * Int64(cur)
                if sq > 100_000 { break }
                cur = Int(sq)
            }
            if length > maxLen {
                maxLen = length
            }
        }
        return maxLen >= 2 ? maxLen : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSquareStreak(nums: IntArray): Int {
        val numSet = HashSet<Int>()
        for (v in nums) numSet.add(v)

        var maxLen = 0
        val limit = 100000L

        for (start in nums) {
            var cur = start.toLong()
            var len = 0
            while (numSet.contains(cur.toInt())) {
                len++
                val next = cur * cur
                if (next > limit) break
                cur = next
            }
            if (len > maxLen) maxLen = len
        }

        return if (maxLen >= 2) maxLen else -1
    }
}
```

## Dart

```dart
class Solution {
  int longestSquareStreak(List<int> nums) {
    final Set<int> set = nums.toSet();
    const int limit = 100000;
    int longest = 0;

    for (final start in nums) {
      int cur = start;
      int streak = 0;
      while (set.contains(cur)) {
        streak++;
        int next = cur * cur;
        if (next > limit) break;
        cur = next;
      }
      if (streak > longest) longest = streak;
    }

    return longest >= 2 ? longest : -1;
  }
}
```

## Golang

```go
import (
	"math"
	"sort"
)

func longestSquareStreak(nums []int) int {
	present := make(map[int]bool, len(nums))
	for _, v := range nums {
		present[v] = true
	}
	sort.Ints(nums)
	dp := make(map[int]int, len(present))
	maxLen := 0
	for _, v := range nums {
		root := int(math.Sqrt(float64(v)))
		if root*root == v && present[root] {
			dp[v] = dp[root] + 1
		} else {
			dp[v] = 1
		}
		if dp[v] > maxLen {
			maxLen = dp[v]
		}
	}
	if maxLen < 2 {
		return -1
	}
	return maxLen
}
```

## Ruby

```ruby
require 'set'

def longest_square_streak(nums)
  present = nums.to_set
  max_len = 0

  nums.each do |start|
    cur = start
    len = 0
    while present.include?(cur)
      len += 1
      break if cur > 100_000   # next square will exceed possible values
      cur *= cur
    end
    max_len = len if len > max_len
  end

  max_len >= 2 ? max_len : -1
end
```

## Scala

```scala
object Solution {
  def longestSquareStreak(nums: Array[Int]): Int = {
    val numSet = nums.toSet
    val maxVal = nums.max
    var best = 0

    for (num <- nums) {
      var cur = num.toLong
      var len = 0
      while (numSet.contains(cur.toInt)) {
        len += 1
        val next = cur * cur
        if (next > maxVal) {
          cur = maxVal + 1L // force exit
        } else {
          cur = next
        }
      }
      if (len > best) best = len
    }

    if (best >= 2) best else -1
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn longest_square_streak(nums: Vec<i32>) -> i32 {
        let set: HashSet<i32> = nums.iter().cloned().collect();
        let mut best = 0usize;
        const LIMIT: i64 = 100_000;

        for &start in nums.iter() {
            let mut cur = start as i64;
            let mut len = 0usize;
            while cur <= LIMIT && set.contains(&(cur as i32)) {
                len += 1;
                // prepare next square
                if cur > LIMIT / cur { // would overflow or exceed limit
                    break;
                }
                cur *= cur;
            }
            if len > best {
                best = len;
            }
        }

        if best < 2 {
            -1
        } else {
            best as i32
        }
    }
}
```

## Racket

```racket
(define/contract (longest-square-streak nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((num-set (make-hash))
         (max-val (apply max nums)))
    (for-each (lambda (x) (hash-set! num-set x #t)) nums)
    (define longest 0)
    (for ([start nums])
      (let loop ((cur start) (len 0))
        (when (hash-has-key? num-set cur)
          (set! longest (max longest (+ len 1)))
          (let ((next (* cur cur)))
            (if (and (<= next max-val) (hash-has-key? num-set next))
                (loop next (+ len 1))
                (void))))))
    (if (< longest 2) -1 longest)))
```

## Erlang

```erlang
-module(solution).
-export([longest_square_streak/1]).
-spec longest_square_streak(Nums :: [integer()]) -> integer().
longest_square_streak(Nums) ->
    Set = maps:from_list([{N, true} || N <- Nums]),
    MaxVal = lists:max(Nums),
    Longest = longest_square_streak_loop(Nums, Set, MaxVal, 0),
    case Longest of
        L when L < 2 -> -1;
        _ -> Longest
    end.

longest_square_streak_loop([], _Set, _MaxVal, Acc) ->
    Acc;
longest_square_streak_loop([H|T], Set, MaxVal, Acc) ->
    Len = streak_length(H, Set, MaxVal),
    NewAcc = max(Acc, Len),
    longest_square_streak_loop(T, Set, MaxVal, NewAcc).

streak_length(Start, Set, MaxVal) ->
    streak_length_iter(Start, Set, MaxVal, 0).

streak_length_iter(Cur, Set, MaxVal, Count) ->
    case maps:is_key(Cur, Set) of
        true ->
            Next = Cur * Cur,
            if
                Next > MaxVal -> Count + 1;
                true -> streak_length_iter(Next, Set, MaxVal, Count + 1)
            end;
        false -> Count
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_square_streak(nums :: [integer]) :: integer
  def longest_square_streak(nums) do
    set = MapSet.new(nums)
    limit = 100_000

    longest =
      Enum.reduce(nums, 0, fn start, acc ->
        len = streak_len(set, limit, start)
        if len > acc, do: len, else: acc
      end)

    if longest < 2, do: -1, else: longest
  end

  defp streak_len(set, limit, cur) do
    if MapSet.member?(set, cur) do
      next =
        if cur <= limit div cur do
          cur * cur
        else
          nil
        end

      1 + (if next != nil, do: streak_len(set, limit, next), else: 0)
    else
      0
    end
  end
end
```
