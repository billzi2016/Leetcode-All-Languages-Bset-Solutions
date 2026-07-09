# 3171. Find Subarray With Bitwise OR Closest to K

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        const long long INF = (1LL<<60);
        long long best = INF;
        vector<int> prev, cur;
        for (int x : nums) {
            cur.clear();
            cur.push_back(x);
            for (int v : prev) {
                cur.push_back(v | x);
            }
            sort(cur.begin(), cur.end());
            cur.erase(unique(cur.begin(), cur.end()), cur.end());
            for (int v : cur) {
                long long diff = llabs((long long)k - v);
                if (diff < best) best = diff;
                if (best == 0) return 0;
            }
            prev.swap(cur);
        }
        return (int)best;
    }
};
```

## Java

```java
class Solution {
    public int minimumDifference(int[] nums, int k) {
        Set<Integer> prev = new java.util.HashSet<>();
        int best = Integer.MAX_VALUE;
        for (int num : nums) {
            Set<Integer> cur = new java.util.HashSet<>();
            cur.add(num);
            for (int v : prev) {
                cur.add(v | num);
            }
            for (int v : cur) {
                int diff = Math.abs(k - v);
                if (diff < best) {
                    best = diff;
                    if (best == 0) return 0;
                }
            }
            prev = cur;
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = float('inf')
        prev = set()
        for num in nums:
            cur = {num}
            for v in prev:
                cur.add(v | num)
            for v in cur:
                diff = abs(k - v)
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        return 0
            prev = cur
        return int(ans)
```

## Python3

```python
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        cur = set()
        for x in nums:
            new_set = {x}
            for v in cur:
                new_set.add(v | x)
            cur = new_set
            for v in cur:
                diff = k - v
                if diff < 0:
                    diff = -diff
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        return 0
        return ans
```

## C

```c
#include <limits.h>

int minimumDifference(int* nums, int numsSize, int k) {
    int ans = INT_MAX;
    int prev[32];
    int prevCnt = 0;

    for (int i = 0; i < numsSize; ++i) {
        int curTmp[64];
        int curCnt = 0;

        // start new subarray at i
        curTmp[curCnt++] = nums[i];

        // extend previous subarrays
        for (int j = 0; j < prevCnt; ++j) {
            curTmp[curCnt++] = prev[j] | nums[i];
        }

        // insertion sort (size <= 31)
        for (int a = 1; a < curCnt; ++a) {
            int key = curTmp[a];
            int b = a - 1;
            while (b >= 0 && curTmp[b] > key) {
                curTmp[b + 1] = curTmp[b];
                --b;
            }
            curTmp[b + 1] = key;
        }

        // deduplicate and store back into prev
        int cnt = 0;
        for (int a = 0; a < curCnt; ++a) {
            if (cnt == 0 || curTmp[a] != prev[cnt - 1]) {
                prev[cnt++] = curTmp[a];
            }
        }

        // update answer
        for (int a = 0; a < cnt; ++a) {
            int v = prev[a];
            int diff = k > v ? k - v : v - k;
            if (diff < ans) ans = diff;
            if (ans == 0) return 0; // optimal possible
        }

        prevCnt = cnt;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        int best = int.MaxValue;
        var prev = new HashSet<int>();
        foreach (int num in nums) {
            var cur = new HashSet<int>();
            cur.Add(num);
            foreach (int v in prev) {
                cur.Add(v | num);
            }
            foreach (int v in cur) {
                int diff = Math.Abs(k - v);
                if (diff < best) best = diff;
                if (best == 0) return 0;
            }
            prev = cur;
        }
        return best;
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
var minimumDifference = function(nums, k) {
    let best = Number.MAX_SAFE_INTEGER;
    let prev = new Set();
    for (let i = 0; i < nums.length; ++i) {
        const cur = new Set();
        const val = nums[i];
        cur.add(val);
        let diff = Math.abs(k - val);
        if (diff < best) best = diff;
        for (const v of prev) {
            const nv = v | val;
            cur.add(nv);
            diff = Math.abs(k - nv);
            if (diff < best) best = diff;
        }
        if (best === 0) return 0;
        prev = cur;
    }
    return best;
};
```

## Typescript

```typescript
function minimumDifference(nums: number[], k: number): number {
    let best = Number.MAX_SAFE_INTEGER;
    let prev = new Set<number>();
    for (const num of nums) {
        const cur = new Set<number>();
        cur.add(num);
        for (const v of prev) {
            cur.add(v | num);
        }
        for (const v of cur) {
            const diff = Math.abs(k - v);
            if (diff < best) {
                best = diff;
                if (best === 0) return 0;
            }
        }
        prev = cur;
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
    function minimumDifference($nums, $k) {
        $ans = PHP_INT_MAX;
        $prev = []; // associative array acting as a set

        foreach ($nums as $x) {
            $curr = [];
            $curr[$x] = true; // subarray consisting of only current element
            foreach ($prev as $v => $_) {
                $new = $v | $x;
                $curr[$new] = true;
            }
            foreach ($curr as $val => $_) {
                $diff = $k > $val ? $k - $val : $val - $k;
                if ($diff < $ans) {
                    $ans = $diff;
                    if ($ans === 0) {
                        return 0;
                    }
                }
            }
            $prev = $curr;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {
        var best = Int.max
        var prev = Set<Int>()
        for num in nums {
            var cur = Set<Int>()
            cur.insert(num)
            for v in prev {
                cur.insert(v | num)
            }
            for v in cur {
                let diff = abs(k - v)
                if diff < best { best = diff }
                if best == 0 { return 0 }
            }
            prev = cur
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDifference(nums: IntArray, k: Int): Int {
        var best = Int.MAX_VALUE
        var prev = mutableListOf<Int>()
        for (num in nums) {
            val curSet = HashSet<Int>()
            curSet.add(num)
            for (v in prev) {
                curSet.add(v or num)
            }
            val cur = ArrayList<Int>(curSet)
            for (v in cur) {
                val diff = kotlin.math.abs(k - v)
                if (diff < best) {
                    best = diff
                    if (best == 0) return 0
                }
            }
            prev = cur
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int minimumDifference(List<int> nums, int k) {
    int best = (nums[0] - k).abs();
    Set<int> prev = {};
    for (int x in nums) {
      Set<int> cur = {x};
      for (int v in prev) {
        cur.add(v | x);
      }
      for (int val in cur) {
        int diff = (val - k).abs();
        if (diff < best) {
          best = diff;
          if (best == 0) return 0;
        }
      }
      prev = cur;
    }
    return best;
  }
}
```

## Golang

```go
func minimumDifference(nums []int, k int) int {
	const INF = int(^uint(0) >> 1)
	ans := INF
	prev := []int{}
	for _, num := range nums {
		cur := []int{num}
		for _, v := range prev {
			nv := v | num
			if nv != cur[len(cur)-1] {
				cur = append(cur, nv)
			}
		}
		for _, v := range cur {
			diff := k - v
			if diff < 0 {
				diff = -diff
			}
			if diff < ans {
				ans = diff
				if ans == 0 {
					return 0
				}
			}
		}
		prev = cur
	}
	return ans
}
```

## Ruby

```ruby
def minimum_difference(nums, k)
  best = Float::INFINITY
  prev = []
  nums.each do |x|
    cur = [x]
    prev.each { |v| cur << (v | x) }
    cur.uniq!
    cur.each do |v|
      diff = (k - v).abs
      best = diff if diff < best
    end
    prev = cur
  end
  best.to_i
end
```

## Scala

```scala
object Solution {
    def minimumDifference(nums: Array[Int], k: Int): Int = {
        var best = Int.MaxValue
        var prev = scala.collection.mutable.Set[Int]()
        for (x <- nums) {
            val cur = scala.collection.mutable.Set[Int]()
            cur += x
            for (v <- prev) {
                cur += (v | x)
            }
            for (v <- cur) {
                val diff = math.abs(k - v)
                if (diff < best) best = diff
                if (best == 0) return 0
            }
            prev = cur
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = i32::MAX;
        let mut prev: Vec<i32> = Vec::new();
        for &x in nums.iter() {
            let mut cur: Vec<i32> = Vec::with_capacity(prev.len() + 1);
            cur.push(x);
            for &v in prev.iter() {
                cur.push(v | x);
            }
            cur.sort_unstable();
            cur.dedup();
            for &v in cur.iter() {
                let diff = (k - v).abs();
                if diff < ans {
                    ans = diff;
                    if ans == 0 {
                        return 0;
                    }
                }
            }
            prev = cur;
        }
        ans
    }
}
```

## Racket

```racket
(require racket/base)

(define/contract (minimum-difference nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ((inf (expt 2 60)))
    (let loop ((rest nums) (prev '()) (best inf))
      (if (null? rest)
          best
          (let* ((x (car rest))
                 (h (make-hash))
                 (_ (hash-set! h x #t))
                 (_ (for ([v prev])
                      (hash-set! h (bitwise-ior v x) #t)))
                 (new-set (hash-keys h))
                 (new-best (for/fold ([b best]) ([v new-set])
                             (let ((diff (abs (- k v))))
                               (if (< diff b) diff b)))))
            (loop (cdr rest) new-set new-best))))))
```

## Erlang

```erlang
-export([minimum_difference/2]).
-spec minimum_difference(Nums :: [integer()], K :: integer()) -> integer().
minimum_difference(Nums, K) ->
    InitialBest = (1 bsl 62),
    {Ans,_} = lists:foldl(fun(Num,{Best,PrevSet}) ->
        CurrOrs = compute_curr_set(Num, PrevSet),
        NewBest = min_best(CurrOrs, K, Best),
        {NewBest, CurrOrs}
    end, {InitialBest, []}, Nums),
    Ans.

compute_curr_set(Num, PrevSet) ->
    All = [Num | [Prev bor Num || Prev <- PrevSet]],
    lists:usort(All).

min_best(Set, K, Best) ->
    lists:foldl(fun(V,Acc) ->
        Diff = abs(K - V),
        if Diff < Acc -> Diff; true -> Acc end
    end, Best, Set).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_difference(nums :: [integer], k :: integer) :: integer
  def minimum_difference(nums, k) do
    import Bitwise

    {ans, _} =
      Enum.reduce(nums, {abs(k - hd(nums)), []}, fn x, {best, prev} ->
        cur =
          (prev |> Enum.map(fn v -> v ||| x end))
          ++ [x]
          |> Enum.uniq()

        new_best =
          Enum.reduce(cur, best, fn v, acc ->
            diff = abs(k - v)
            if diff < acc, do: diff, else: acc
          end)

        {new_best, cur}
      end)

    ans
  end
end
```
