# 3209. Number of Subarrays With AND Value of K

## Cpp

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        vector<pair<int,long long>> prev;
        long long ans = 0;
        for (int x : nums) {
            vector<pair<int,long long>> cur;
            cur.emplace_back(x, 1);
            for (auto &p : prev) {
                int v = p.first & x;
                if (cur.back().first == v) {
                    cur.back().second += p.second;
                } else {
                    cur.emplace_back(v, p.second);
                }
            }
            for (auto &p : cur) {
                if (p.first == k) ans += p.second;
            }
            prev.swap(cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countSubarrays(int[] nums, int k) {
        java.util.HashMap<Integer, Long> cur = new java.util.HashMap<>();
        java.util.HashMap<Integer, Long> nxt = new java.util.HashMap<>();
        long ans = 0;
        for (int num : nums) {
            nxt.clear();
            nxt.put(num, 1L);
            for (java.util.Map.Entry<Integer, Long> e : cur.entrySet()) {
                int v = e.getKey() & num;
                long cnt = e.getValue();
                nxt.merge(v, cnt, Long::sum);
            }
            ans += nxt.getOrDefault(k, 0L);
            java.util.HashMap<Integer, Long> tmp = cur;
            cur = nxt;
            nxt = tmp;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        prev = {}
        for x in nums:
            cur = {x: 1}
            for val, cnt in prev.items():
                new_val = val & x
                cur[new_val] = cur.get(new_val, 0) + cnt
            if k in cur:
                ans += cur[k]
            prev = cur
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        prev = {}
        for x in nums:
            cur = {x: 1}
            for v, cnt in prev.items():
                nv = v & x
                cur[nv] = cur.get(nv, 0) + cnt
            if k in cur:
                ans += cur[k]
            prev = cur
        return ans
```

## C

```c
long long countSubarrays(int* nums, int numsSize, int k) {
    const int MAXD = 35; // enough for distinct AND values per position
    int prev_val[MAXD];
    int prev_cnt[MAXD];
    int cur_val[MAXD];
    int cur_cnt[MAXD];
    int prev_sz = 0;
    long long ans = 0;

    for (int i = 0; i < numsSize; ++i) {
        int sz = 0;
        // subarray consisting only of nums[i]
        cur_val[sz] = nums[i];
        cur_cnt[sz] = 1;
        ++sz;

        // extend all previous subarrays ending at i-1
        for (int j = 0; j < prev_sz; ++j) {
            int v = prev_val[j] & nums[i];
            if (v == cur_val[sz - 1]) {
                cur_cnt[sz - 1] += prev_cnt[j];
            } else {
                cur_val[sz] = v;
                cur_cnt[sz] = prev_cnt[j];
                ++sz;
            }
        }

        // accumulate answer for this right endpoint
        for (int j = 0; j < sz; ++j) {
            if (cur_val[j] == k) {
                ans += (long long)cur_cnt[j];
            }
        }

        // prepare for next iteration
        prev_sz = sz;
        for (int j = 0; j < sz; ++j) {
            prev_val[j] = cur_val[j];
            prev_cnt[j] = cur_cnt[j];
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long CountSubarrays(int[] nums, int k) {
        var prev = new Dictionary<int, long>();
        long ans = 0;
        foreach (int num in nums) {
            var cur = new Dictionary<int, long>();
            // subarray consisting of only current element
            cur[num] = 1;
            foreach (var kvp in prev) {
                int newVal = kvp.Key & num;
                if (cur.TryGetValue(newVal, out long existing)) {
                    cur[newVal] = existing + kvp.Value;
                } else {
                    cur[newVal] = kvp.Value;
                }
            }
            if (cur.TryGetValue(k, out long cnt)) ans += cnt;
            prev = cur;
        }
        return ans;
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
var countSubarrays = function(nums, k) {
    let ans = 0;
    let prev = []; // each element: [andValue, count] for subarrays ending at previous index
    
    for (const x of nums) {
        const cur = [[x, 1]];
        for (const [val, cnt] of prev) {
            const newVal = val & x;
            if (cur[cur.length - 1][0] === newVal) {
                cur[cur.length - 1][1] += cnt;
            } else {
                cur.push([newVal, cnt]);
            }
        }
        for (const [val, cnt] of cur) {
            if (val === k) ans += cnt;
        }
        prev = cur;
    }
    
    return ans;
};
```

## Typescript

```typescript
function countSubarrays(nums: number[], k: number): number {
    let ans = 0;
    // list of [andValue, count] for subarrays ending at previous index
    let prev: Array<[number, number]> = [];

    for (const num of nums) {
        const curMap = new Map<number, number>();
        // subarray consisting only of current element
        curMap.set(num, (curMap.get(num) ?? 0) + 1);

        for (const [val, cnt] of prev) {
            const newVal = val & num;
            curMap.set(newVal, (curMap.get(newVal) ?? 0) + cnt);
        }

        if (curMap.has(k)) {
            ans += curMap.get(k)!;
        }

        // prepare for next iteration
        prev = Array.from(curMap.entries());
    }

    return ans;
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
    function countSubarrays($nums, $k) {
        $ans = 0;
        $prev = [];
        foreach ($nums as $x) {
            $cur = [];
            // subarray consisting of only current element
            $cur[$x] = ($cur[$x] ?? 0) + 1;
            foreach ($prev as $val => $cnt) {
                $newVal = $val & $x;
                if (isset($cur[$newVal])) {
                    $cur[$newVal] += $cnt;
                } else {
                    $cur[$newVal] = $cnt;
                }
            }
            if (isset($cur[$k])) {
                $ans += $cur[$k];
            }
            $prev = $cur;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var prev = [Int:Int]()
        var ans: Int64 = 0
        for num in nums {
            var cur = [Int:Int]()
            cur[num, default: 0] += 1
            for (val, cnt) in prev {
                let newVal = val & num
                cur[newVal, default: 0] += cnt
            }
            if let countK = cur[k] {
                ans += Int64(countK)
            }
            prev = cur
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray, k: Int): Long {
        var ans = 0L
        var prev = mutableListOf<Pair<Int, Long>>()
        for (num in nums) {
            val cur = mutableListOf<Pair<Int, Long>>()
            // subarray consisting only of current element
            cur.add(Pair(num, 1L))
            for ((value, cnt) in prev) {
                val newVal = value and num
                if (cur.isNotEmpty() && cur.last().first == newVal) {
                    val last = cur.removeAt(cur.size - 1)
                    cur.add(Pair(last.first, last.second + cnt))
                } else {
                    cur.add(Pair(newVal, cnt))
                }
            }
            for ((value, cnt) in cur) {
                if (value == k) ans += cnt
            }
            prev = cur
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countSubarrays(List<int> nums, int k) {
    Map<int, int> prev = {};
    int ans = 0;
    for (int x in nums) {
      Map<int, int> cur = {x: 1};
      for (var entry in prev.entries) {
        int newVal = entry.key & x;
        cur.update(newVal, (v) => v + entry.value,
            ifAbsent: () => entry.value);
      }
      ans += cur[k] ?? 0;
      prev = cur;
    }
    return ans;
  }
}
```

## Golang

```go
func countSubarrays(nums []int, k int) int64 {
	type pair struct {
		val int
		cnt int64
	}
	var prev []pair
	var ans int64
	for _, x := range nums {
		cur := make([]pair, 0, len(prev)+1)
		// subarray consisting of only current element
		cur = append(cur, pair{val: x, cnt: 1})
		// extend previous subarrays
		for _, p := range prev {
			v := p.val & x
			if cur[len(cur)-1].val == v {
				cur[len(cur)-1].cnt += p.cnt
			} else {
				cur = append(cur, pair{val: v, cnt: p.cnt})
			}
		}
		// count those equal to k
		for _, p := range cur {
			if p.val == k {
				ans += p.cnt
			}
		}
		prev = cur
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  prev = {}
  ans = 0
  nums.each do |x|
    cur = Hash.new(0)
    cur[x] += 1
    prev.each do |val, cnt|
      new_val = val & x
      cur[new_val] += cnt
    end
    ans += cur[k] if cur.key?(k)
    prev = cur
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int], k: Int): Long = {
        import scala.collection.mutable
        var cur = mutable.Map.empty[Int, Long]
        var ans: Long = 0L
        for (num <- nums) {
            val next = mutable.Map.empty[Int, Long]
            // subarray consisting of only current element
            next(num) = next.getOrElse(num, 0L) + 1L
            // extend previous subarrays
            for ((v, cnt) <- cur) {
                val nv = v & num
                next(nv) = next.getOrElse(nv, 0L) + cnt
            }
            ans += next.getOrElse(k, 0L)
            cur = next
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mut ans: i64 = 0;
        let mut prev: Vec<(i32, i64)> = Vec::new();
        for &x in nums.iter() {
            let mut cur: Vec<(i32, i64)> = Vec::new();
            // subarray consisting of only current element
            cur.push((x, 1));
            // extend previous subarrays
            for &(v, cnt) in prev.iter() {
                let nv = v & x;
                if let Some(last) = cur.last_mut() {
                    if last.0 == nv {
                        last.1 += cnt;
                    } else {
                        cur.push((nv, cnt));
                    }
                }
            }
            // count those equal to k
            for &(v, cnt) in cur.iter() {
                if v == k {
                    ans += cnt;
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
(define/contract (count-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((lst nums) (prev '()) (ans 0))
    (if (null? lst)
        ans
        (let* ((x (car lst))
               (h (make-hash)))
          ;; subarray consisting only of x
          (hash-set! h x (+ (hash-ref h x 0) 1))
          ;; extend previous subarrays
          (for ([pair prev])
            (define val (car pair))
            (define cnt (cdr pair))
            (define newval (bitwise-and val x))
            (hash-set! h newval (+ (hash-ref h newval 0) cnt)))
          (define add (hash-ref h k 0))
          (define new-list (hash->list h))
          (loop (cdr lst) new-list (+ ans add))))))
```

## Erlang

```erlang
-module(solution).
-export([count_subarrays/2]).

-spec count_subarrays(Nums :: [integer()], K :: integer()) -> integer().
count_subarrays(Nums, K) ->
    count_subarrays(Nums, K, #{}, 0).

count_subarrays([], _K, _Prev, Ans) ->
    Ans;
count_subarrays([Num|Rest], K, Prev, Ans) ->
    Curr0 = maps:put(Num, 1, #{}),
    Curr = maps:fold(
        fun(Val, Cnt, Acc) ->
            NewVal = Val band Num,
            case maps:is_key(NewVal, Acc) of
                true -> maps:update_with(NewVal, fun(X) -> X + Cnt end, Acc);
                false -> maps:put(NewVal, Cnt, Acc)
            end
        end,
        Curr0,
        Prev),
    Add = maps:get(K, Curr, 0),
    count_subarrays(Rest, K, Curr, Ans + Add).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer], k :: integer) :: integer
  def count_subarrays(nums, k) do
    import Bitwise

    {_, ans} =
      Enum.reduce(nums, {%{}, 0}, fn num, {prev_map, acc} ->
        cur = %{num => 1}

        cur =
          Enum.reduce(prev_map, cur, fn {val, cnt}, m ->
            new_val = band(val, num)
            Map.update(m, new_val, cnt, &(&1 + cnt))
          end)

        add = Map.get(cur, k, 0)
        {cur, acc + add}
      end)

    ans
  end
end
```
