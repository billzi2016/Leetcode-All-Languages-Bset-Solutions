# 2261. K Divisible Elements Subarrays

## Cpp

```cpp
class Solution {
public:
    struct VectorHash {
        size_t operator()(const std::vector<int>& v) const noexcept {
            size_t seed = v.size();
            for (int x : v) {
                seed ^= static_cast<size_t>(x) + 0x9e3779b97f4a7c15ULL + (seed << 6) + (seed >> 2);
            }
            return seed;
        }
    };
    
    int countDistinct(std::vector<int>& nums, int k, int p) {
        std::unordered_set<std::vector<int>, VectorHash> uniq;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int cntDiv = 0;
            std::vector<int> cur;
            cur.reserve(n - i);
            for (int j = i; j < n; ++j) {
                if (nums[j] % p == 0) ++cntDiv;
                if (cntDiv > k) break;
                cur.push_back(nums[j]);
                uniq.insert(cur);
            }
        }
        return static_cast<int>(uniq.size());
    }
};
```

## Java

```java
class Solution {
    public int countDistinct(int[] nums, int k, int p) {
        int n = nums.length;
        java.util.HashSet<java.util.List<Integer>> set = new java.util.HashSet<>();
        for (int i = 0; i < n; i++) {
            int cntDiv = 0;
            java.util.ArrayList<Integer> cur = new java.util.ArrayList<>();
            for (int j = i; j < n; j++) {
                if (nums[j] % p == 0) cntDiv++;
                if (cntDiv > k) break;
                cur.add(nums[j]);
                set.add(new java.util.ArrayList<>(cur));
            }
        }
        return set.size();
    }
}
```

## Python

```python
class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        n = len(nums)
        seen = set()
        for i in range(n):
            div_cnt = 0
            cur = []
            for j in range(i, n):
                if nums[j] % p == 0:
                    div_cnt += 1
                if div_cnt > k:
                    break
                cur.append(nums[j])
                seen.add(tuple(cur))
        return len(seen)
```

## Python3

```python
from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        n = len(nums)
        for i in range(n):
            cnt = 0
            cur = []
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                cur.append(nums[j])
                seen.add(tuple(cur))
        return len(seen)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int countDistinct(int* nums, int numsSize, int k, int p) {
    const unsigned int MOD1 = 1000000007U;
    const unsigned int MOD2 = 1000000009U;
    const unsigned int BASE = 91138233U;

    /* prefix hashes and powers */
    unsigned int *pref1 = (unsigned int*)calloc(numsSize + 1, sizeof(unsigned int));
    unsigned int *pref2 = (unsigned int*)calloc(numsSize + 1, sizeof(unsigned int));
    unsigned int *pow1  = (unsigned int*)calloc(numsSize + 1, sizeof(unsigned int));
    unsigned int *pow2  = (unsigned int*)calloc(numsSize + 1, sizeof(unsigned int));

    pow1[0] = 1;
    pow2[0] = 1;
    for (int i = 0; i < numsSize; ++i) {
        pref1[i + 1] = ( (uint64_t)pref1[i] * BASE + (unsigned int)nums[i]) % MOD1;
        pref2[i + 1] = ( (uint64_t)pref2[i] * BASE + (unsigned int)nums[i]) % MOD2;
        pow1[i + 1] = ( (uint64_t)pow1[i] * BASE ) % MOD1;
        pow2[i + 1] = ( (uint64_t)pow2[i] * BASE ) % MOD2;
    }

    /* hash set for distinct subarray hashes */
    const int TABLE_SIZE = 131071;               // a prime > 2 * max possible distinct subarrays
    unsigned long long *keys = (unsigned long long*)calloc(TABLE_SIZE, sizeof(unsigned long long));
    char *used = (char*)calloc(TABLE_SIZE, sizeof(char));

    int distinctCount = 0;

    for (int i = 0; i < numsSize; ++i) {
        int divCnt = 0;
        for (int j = i; j < numsSize; ++j) {
            if (nums[j] % p == 0) ++divCnt;
            if (divCnt > k) break;

            int len = j - i + 1;
            unsigned int h1 = pref1[j + 1];
            unsigned int sub1 = ( (uint64_t)pref1[i] * pow1[len]) % MOD1;
            if (h1 < sub1) h1 += MOD1;
            h1 -= sub1;

            unsigned int h2 = pref2[j + 1];
            unsigned int sub2 = ( (uint64_t)pref2[i] * pow2[len]) % MOD2;
            if (h2 < sub2) h2 += MOD2;
            h2 -= sub2;

            unsigned long long key = ((unsigned long long)h1 << 32) | h2;

            int idx = (int)(key % TABLE_SIZE);
            while (used[idx]) {
                if (keys[idx] == key) break;          // already present
                idx++;
                if (idx == TABLE_SIZE) idx = 0;
            }
            if (!used[idx]) {
                used[idx] = 1;
                keys[idx] = key;
                ++distinctCount;
            }
        }
    }

    free(pref1);
    free(pref2);
    free(pow1);
    free(pow2);
    free(keys);
    free(used);

    return distinctCount;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public int CountDistinct(int[] nums, int k, int p) {
        var seen = new HashSet<string>();
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            int cntDiv = 0;
            var sb = new StringBuilder();
            for (int j = i; j < n; j++) {
                if (nums[j] % p == 0) cntDiv++;
                if (cntDiv > k) break;
                if (sb.Length > 0) sb.Append(',');
                sb.Append(nums[j]);
                seen.Add(sb.ToString());
            }
        }
        return seen.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} p
 * @return {number}
 */
var countDistinct = function(nums, k, p) {
    const seen = new Set();
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        let divCount = 0;
        const cur = [];
        for (let j = i; j < n; ++j) {
            if (nums[j] % p === 0) divCount++;
            if (divCount > k) break;
            cur.push(nums[j]);
            seen.add(cur.join(','));
        }
    }
    return seen.size;
};
```

## Typescript

```typescript
function countDistinct(nums: number[], k: number, p: number): number {
    const seen = new Set<string>();
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        let cnt = 0;
        const cur: number[] = [];
        for (let j = i; j < n; ++j) {
            if (nums[j] % p === 0) cnt++;
            if (cnt > k) break;
            cur.push(nums[j]);
            seen.add(cur.join(','));
        }
    }
    return seen.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $p
     * @return Integer
     */
    function countDistinct($nums, $k, $p) {
        $n = count($nums);
        $seen = [];

        for ($i = 0; $i < $n; $i++) {
            $cntDiv = 0;
            $key = '';
            for ($j = $i; $j < $n; $j++) {
                if ($nums[$j] % $p == 0) {
                    $cntDiv++;
                }
                if ($cntDiv > $k) {
                    break;
                }

                if ($key === '') {
                    $key = (string)$nums[$j];
                } else {
                    $key .= ',' . $nums[$j];
                }
                $seen[$key] = true;
            }
        }

        return count($seen);
    }
}
```

## Swift

```swift
class Solution {
    func countDistinct(_ nums: [Int], _ k: Int, _ p: Int) -> Int {
        var seen = Set<[Int]>()
        let n = nums.count
        for i in 0..<n {
            var divCount = 0
            var subarray = [Int]()
            for j in i..<n {
                let val = nums[j]
                if val % p == 0 { divCount += 1 }
                if divCount > k { break }
                subarray.append(val)
                seen.insert(subarray)
            }
        }
        return seen.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countDistinct(nums: IntArray, k: Int, p: Int): Int {
        val n = nums.size
        val seen = HashSet<List<Int>>()
        for (i in 0 until n) {
            var cntDivisible = 0
            for (j in i until n) {
                if (nums[j] % p == 0) cntDivisible++
                if (cntDivisible > k) break
                seen.add(nums.slice(i..j))
            }
        }
        return seen.size
    }
}
```

## Dart

```dart
class Solution {
  int countDistinct(List<int> nums, int k, int p) {
    final n = nums.length;
    final Set<String> seen = {};
    for (int i = 0; i < n; ++i) {
      int cntDiv = 0;
      final List<int> cur = [];
      for (int j = i; j < n; ++j) {
        if (nums[j] % p == 0) cntDiv++;
        if (cntDiv > k) break;
        cur.add(nums[j]);
        seen.add(cur.join(','));
      }
    }
    return seen.length;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func countDistinct(nums []int, k int, p int) int {
	n := len(nums)
	seen := make(map[string]struct{})
	for i := 0; i < n; i++ {
		divCnt := 0
		var sb strings.Builder
		for j := i; j < n; j++ {
			if nums[j]%p == 0 {
				divCnt++
			}
			if divCnt > k {
				break
			}
			sb.WriteByte('#')
			sb.WriteString(strconv.Itoa(nums[j]))
			key := sb.String()
			seen[key] = struct{}{}
		}
	}
	return len(seen)
}
```

## Ruby

```ruby
def count_distinct(nums, k, p)
  n = nums.length
  seen = {}
  (0...n).each do |i|
    cnt = 0
    (i...n).each do |j|
      cnt += 1 if nums[j] % p == 0
      break if cnt > k
      key = nums[i..j].join(',')
      seen[key] = true
    end
  end
  seen.size
end
```

## Scala

```scala
object Solution {
  def countDistinct(nums: Array[Int], k: Int, p: Int): Int = {
    val n = nums.length
    val seen = scala.collection.mutable.HashSet[Seq[Int]]()
    for (i <- 0 until n) {
      var cntDiv = 0
      val buffer = new collection.mutable.ArrayBuffer[Int]()
      var j = i
      while (j < n && cntDiv <= k) {
        if (nums(j) % p == 0) cntDiv += 1
        if (cntDiv > k) {
          // stop extending this subarray
        } else {
          buffer.append(nums(j))
          seen.add(buffer.toList)
        }
        j += 1
      }
    }
    seen.size
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn count_distinct(nums: Vec<i32>, k: i32, p: i32) -> i32 {
        let n = nums.len();
        let mut seen: HashSet<Vec<i32>> = HashSet::new();

        for i in 0..n {
            let mut cnt = 0;
            let mut cur = Vec::new();
            for j in i..n {
                let val = nums[j];
                if val % p == 0 {
                    cnt += 1;
                }
                if cnt > k {
                    break;
                }
                cur.push(val);
                seen.insert(cur.clone());
            }
        }

        seen.len() as i32
    }
}
```

## Racket

```racket
(define/contract (count-distinct nums k p)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (seen (make-hash)))
    (for ([i (in-range n)])
      (let loop ((j i) (cnt 0))
        (when (< j n)
          (define new-cnt (+ cnt (if (= (mod (vector-ref vec j) p) 0) 1 0)))
          (if (> new-cnt k)
              (void)
              (begin
                (define sublist
                  (vector->list (vector-copy vec i (add1 j))))
                (hash-set! seen sublist #t)
                (loop (add1 j) new-cnt))))))
    (hash-count seen)))
```

## Erlang

```erlang
-spec count_distinct(Nums :: [integer()], K :: integer(), P :: integer()) -> integer().
count_distinct(Nums, K, P) ->
    N = length(Nums),
    Set0 = sets:new(),
    FinalSet = outer_loop(0, N, Nums, K, P, Set0),
    sets:size(FinalSet).

outer_loop(I, N, _Nums, _K, _P, Set) when I >= N -> Set;
outer_loop(I, N, Nums, K, P, Set) ->
    {NewSet,_} = process_start(I, N, Nums, K, P, Set),
    outer_loop(I + 1, N, Nums, K, P, NewSet).

process_start(S, N, Nums, K, P, Set) ->
    process_end(S, S, N, Nums, K, P, 0, Set).

process_end(_S, J, N, _Nums, _K, _P, DivCnt, Set) when J >= N -> {Set, DivCnt};
process_end(S, J, N, Nums, K, P, DivCnt, Set) ->
    Num = lists:nth(J + 1, Nums),
    NewDiv = if Num rem P == 0 -> DivCnt + 1; true -> DivCnt end,
    if NewDiv > K ->
            {Set, NewDiv};
       true ->
            Sub = lists:sublist(Nums, S + 1, J - S + 1),
            Set1 = sets:add_element(Sub, Set),
            process_end(S, J + 1, N, Nums, K, P, NewDiv, Set1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_distinct(nums :: [integer], k :: integer, p :: integer) :: integer
  def count_distinct(nums, k, p) do
    n = length(nums)

    set =
      Enum.reduce(0..(n - 1), MapSet.new(), fn i, acc ->
        inner(nums, k, p, i, i, 0, acc)
      end)

    MapSet.size(set)
  end

  defp inner(_nums, _k, _p, _start, idx, _cnt, set) when idx >= length(_nums), do: set

  defp inner(nums, k, p, start, idx, cnt, set) do
    val = Enum.at(nums, idx)
    new_cnt = if rem(val, p) == 0, do: cnt + 1, else: cnt

    if new_cnt > k do
      set
    else
      sub = Enum.slice(nums, start..idx)
      set2 = MapSet.put(set, sub)
      inner(nums, k, p, start, idx + 1, new_cnt, set2)
    end
  end
end
```
