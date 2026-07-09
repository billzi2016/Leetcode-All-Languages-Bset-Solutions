# 2122. Recover the Original Array

## Cpp

```cpp
class Solution {
public:
    vector<int> recoverArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int m = nums.size();
        int n = m / 2;
        int low0 = nums[0];
        for (int i = 1; i < m; ++i) {
            long long diff = (long long)nums[i] - low0;
            if (diff <= 0 || diff % 2 != 0) continue;
            int k = diff / 2;
            unordered_map<long long, int> cnt;
            cnt.reserve(m * 2);
            for (int v : nums) ++cnt[v];
            vector<int> arr;
            bool ok = true;
            for (int x : nums) {
                if (cnt[x] == 0) continue;
                --cnt[x];
                long long y = (long long)x + 2LL * k;
                auto it = cnt.find(y);
                if (it == cnt.end() || it->second == 0) { ok = false; break; }
                --(it->second);
                arr.push_back(x + k);
            }
            if (ok && (int)arr.size() == n) return arr;
        }
        return {};
    }
};
```

## Java

```java
class Solution {
    public int[] recoverArray(int[] nums) {
        int m = nums.length;
        int n = m / 2;
        java.util.Arrays.sort(nums);
        int smallest = nums[0];
        // build original counts map
        java.util.HashMap<Integer, Integer> baseCount = new java.util.HashMap<>();
        for (int v : nums) {
            baseCount.put(v, baseCount.getOrDefault(v, 0) + 1);
        }
        for (int i = 1; i < m; i++) {
            int diff = nums[i] - smallest;
            if (diff <= 0 || (diff & 1) == 1) continue; // need positive even difference
            int k = diff / 2;
            if (k == 0) continue;
            java.util.HashMap<Integer, Integer> cnt = new java.util.HashMap<>(baseCount);
            int[] res = new int[n];
            int idx = 0;
            boolean ok = true;
            for (int num : nums) {
                int c = cnt.getOrDefault(num, 0);
                if (c == 0) continue; // already used
                // use as lower
                cnt.put(num, c - 1);
                long higherLong = (long) num + 2L * k;
                if (higherLong > Integer.MAX_VALUE) {
                    ok = false;
                    break;
                }
                int higher = (int) higherLong;
                int ch = cnt.getOrDefault(higher, 0);
                if (ch == 0) {
                    ok = false;
                    break;
                }
                cnt.put(higher, ch - 1);
                res[idx++] = num + k; // original value
            }
            if (ok && idx == n) {
                return res;
            }
        }
        // According to problem statement, a solution always exists.
        return new int[0];
    }
}
```

## Python

```python
class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        nums.sort()
        n = len(nums) // 2
        first = nums[0]

        for i in range(1, len(nums)):
            diff = nums[i] - first
            if diff <= 0 or diff % 2 != 0:
                continue
            k = diff // 2  # positive integer

            cnt = Counter(nums)
            arr = []
            ok = True

            for x in nums:
                if cnt[x] == 0:
                    continue
                y = x + 2 * k
                if cnt[y] == 0:
                    ok = False
                    break
                cnt[x] -= 1
                cnt[y] -= 1
                arr.append((x + y) // 2)

            if ok and len(arr) == n:
                return arr

        # According to problem statement, a solution always exists.
        return []
```

## Python3

```python
class Solution:
    def recoverArray(self, nums):
        from collections import Counter
        nums.sort()
        n = len(nums) // 2
        smallest = nums[0]
        for j in range(1, len(nums)):
            diff = nums[j] - smallest
            if diff <= 0 or diff % 2:
                continue
            k = diff // 2
            cnt = Counter(nums)
            arr = []
            valid = True
            for x in nums:
                if cnt[x] == 0:
                    continue
                cnt[x] -= 1
                higher = x + 2 * k
                if cnt[higher] == 0:
                    valid = False
                    break
                cnt[higher] -= 1
                arr.append(x + k)
            if valid and len(arr) == n:
                return arr
        # According to problem statement, a solution always exists
        return []
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/* binary search for value in sorted array uniqVals of size m.
   returns index if found, otherwise -1 */
static int find_index(const long long *uniqVals, int m, long long target) {
    int l = 0, r = m - 1;
    while (l <= r) {
        int mid = l + ((r - l) >> 1);
        if (uniqVals[mid] == target) return mid;
        if (uniqVals[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* recoverArray(int* nums, int numsSize, int* returnSize) {
    int n = numsSize / 2;
    qsort(nums, numsSize, sizeof(int), cmp_int);

    /* Build unique values and their counts */
    long long *uniqVals = (long long *)malloc(sizeof(long long) * numsSize);
    int *cnt = (int *)malloc(sizeof(int) * numsSize);
    int uniqCnt = 0;
    for (int i = 0; i < numsSize; ) {
        int j = i;
        while (j < numsSize && nums[j] == nums[i]) ++j;
        uniqVals[uniqCnt] = nums[i];
        cnt[uniqCnt] = j - i;
        ++uniqCnt;
        i = j;
    }

    int *answer = NULL;

    for (int idx = 1; idx < numsSize && answer == NULL; ++idx) {
        long long diff = (long long)nums[idx] - (long long)nums[0];
        if (diff <= 0 || (diff & 1LL)) continue;   // need positive even difference
        long long k = diff / 2;
        int *tempCnt = (int *)malloc(sizeof(int) * uniqCnt);
        memcpy(tempCnt, cnt, sizeof(int) * uniqCnt);

        int *candidate = (int *)malloc(sizeof(int) * n);
        int candSize = 0;
        int ok = 1;

        for (int u = 0; u < uniqCnt && ok; ++u) {
            while (tempCnt[u] > 0) {
                long long lowVal = uniqVals[u];
                long long highVal = lowVal + 2 * k;
                int pIdx = find_index(uniqVals, uniqCnt, highVal);
                if (pIdx == -1 || tempCnt[pIdx] == 0) {
                    ok = 0;
                    break;
                }
                /* use one pair */
                tempCnt[u]--;
                tempCnt[pIdx]--;
                candidate[candSize++] = (int)(lowVal + k); // arr element
            }
        }

        free(tempCnt);
        if (ok && candSize == n) {
            answer = candidate;
            *returnSize = n;
        } else {
            free(candidate);
        }
    }

    /* clean up */
    free(uniqVals);
    free(cnt);

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] RecoverArray(int[] nums) {
        int total = nums.Length;
        int n = total / 2;
        Array.Sort(nums);
        long[] sorted = new long[total];
        for (int i = 0; i < total; i++) sorted[i] = nums[i];

        // Build base frequency map
        var baseFreq = new Dictionary<long, int>();
        foreach (var v in sorted) {
            if (!baseFreq.ContainsKey(v)) baseFreq[v] = 0;
            baseFreq[v]++;
        }

        long low0 = sorted[0];
        for (int j = 1; j < total; j++) {
            long diff = sorted[j] - low0;
            if (diff <= 0 || diff % 2 != 0) continue; // need positive even difference
            long k = diff / 2;
            var freq = new Dictionary<long, int>(baseFreq);
            List<int> arr = new List<int>();
            bool ok = true;

            foreach (var x in sorted) {
                if (!freq.TryGetValue(x, out int cntX) || cntX == 0) continue; // already used
                long y = x + 2 * k;
                if (!freq.TryGetValue(y, out int cntY) || cntY == 0) {
                    ok = false;
                    break;
                }
                // use pair (x as lower, y as higher)
                freq[x] = cntX - 1;
                freq[y] = cntY - 1;
                arr.Add((int)(x + k));
            }

            if (ok && arr.Count == n) {
                return arr.ToArray();
            }
        }

        // According to problem statement, a solution always exists.
        return new int[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var recoverArray = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length / 2;
    for (let i = 1; i < nums.length; i++) {
        const diff = nums[i] - nums[0];
        if (diff <= 0 || diff % 2 !== 0) continue;
        const k = diff / 2;

        const freq = new Map();
        for (const v of nums) {
            freq.set(v, (freq.get(v) || 0) + 1);
        }

        const arr = [];
        let ok = true;
        for (const v of nums) {
            if (!freq.has(v) || freq.get(v) === 0) continue; // already used
            const low = v;
            const high = low + 2 * k;
            if (!freq.has(high) || freq.get(high) === 0) {
                ok = false;
                break;
            }
            freq.set(low, freq.get(low) - 1);
            freq.set(high, freq.get(high) - 1);
            arr.push(low + k);
        }

        if (ok && arr.length === n) return arr;
    }
    // According to problem guarantees this line is never reached.
    return [];
};
```

## Typescript

```typescript
function recoverArray(nums: number[]): number[] {
    const sorted = nums.slice().sort((a, b) => a - b);
    const total = sorted.length;
    const n = total / 2;

    for (let i = 1; i < total; i++) {
        const diff = sorted[i] - sorted[0]; // this should be 2 * k
        if (diff <= 0 || diff % 2 !== 0) continue;
        const k = diff / 2;

        const freq = new Map<number, number>();
        for (const v of sorted) {
            freq.set(v, (freq.get(v) ?? 0) + 1);
        }

        const original: number[] = [];
        let possible = true;

        for (const low of sorted) {
            const cntLow = freq.get(low) ?? 0;
            if (cntLow === 0) continue; // already used

            const high = low + diff;
            const cntHigh = freq.get(high) ?? 0;
            if (cntHigh === 0) {
                possible = false;
                break;
            }

            // use one low and one high
            freq.set(low, cntLow - 1);
            freq.set(high, cntHigh - 1);
            original.push(low + k);
        }

        if (possible && original.length === n) {
            return original;
        }
    }

    // According to problem guarantees, this line should never be reached.
    return [];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function recoverArray($nums) {
        sort($nums);
        $len = count($nums);
        $n = intdiv($len, 2);
        $minVal = $nums[0];

        for ($i = 1; $i < $len; $i++) {
            $candidate = $nums[$i];
            $diff = $candidate - $minVal;
            if ($diff % 2 !== 0) {
                continue;
            }
            $k = intdiv($diff, 2);
            if ($k <= 0) {
                continue;
            }

            $freq = array_count_values($nums);
            $original = [];
            $valid = true;

            foreach ($nums as $x) {
                if (!isset($freq[$x]) || $freq[$x] == 0) {
                    continue;
                }
                // x is considered a lower element
                $freq[$x]--;
                $y = $x + 2 * $k; // corresponding higher element

                if (!isset($freq[$y]) || $freq[$y] == 0) {
                    $valid = false;
                    break;
                }
                $freq[$y]--;
                $original[] = $x + $k; // original value
            }

            if ($valid && count($original) === $n) {
                return $original;
            }
        }

        // According to problem constraints, this line should never be reached.
        return [];
    }
}
```

## Swift

```swift
class Solution {
    func recoverArray(_ nums: [Int]) -> [Int] {
        let sortedNums = nums.sorted()
        let total = sortedNums.count
        let n = total / 2
        
        for j in 1..<total {
            let diff = sortedNums[j] - sortedNums[0]
            if diff <= 0 || diff % 2 != 0 { continue } // diff must be positive and even
            
            var freq = [Int: Int]()
            for v in sortedNums {
                freq[v, default: 0] += 1
            }
            
            var result = [Int]()
            var possible = true
            
            for v in sortedNums {
                guard let cntV = freq[v], cntV > 0 else { continue }
                // use v as lower element
                freq[v] = cntV - 1
                let higher = v + diff
                if let cntH = freq[higher], cntH > 0 {
                    freq[higher] = cntH - 1
                    result.append(v + diff / 2) // original value
                } else {
                    possible = false
                    break
                }
            }
            
            if possible && result.count == n {
                return result
            }
        }
        // According to problem statement, a solution always exists.
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun recoverArray(nums: IntArray): IntArray {
        val sorted = nums.sorted()
        val n = nums.size / 2
        for (i in 1 until sorted.size) {
            val diff = sorted[i] - sorted[0]
            if (diff <= 0 || diff % 2 != 0) continue
            val k = diff / 2
            val countMap = HashMap<Int, Int>()
            for (v in sorted) {
                countMap[v] = (countMap[v] ?: 0) + 1
            }
            val result = mutableListOf<Int>()
            var possible = true
            for (v in sorted) {
                val cnt = countMap.getOrDefault(v, 0)
                if (cnt == 0) continue
                // use v as lower element
                countMap[v] = cnt - 1
                val partner = v + 2 * k
                val cntPartner = countMap.getOrDefault(partner, 0)
                if (cntPartner == 0) {
                    possible = false
                    break
                }
                countMap[partner] = cntPartner - 1
                result.add(v + k) // original element
            }
            if (possible && result.size == n) {
                return result.toIntArray()
            }
        }
        // According to problem guarantees, this line is never reached.
        return intArrayOf()
    }
}
```

## Dart

```dart
class Solution {
  List<int> recoverArray(List<int> nums) {
    List<int> sorted = List.from(nums);
    sorted.sort();
    int m = sorted.length;
    for (int j = 1; j < m; ++j) {
      int diff = sorted[j] - sorted[0];
      if (diff <= 0 || diff % 2 != 0) continue;
      int k = diff ~/ 2;
      Map<int, int> cnt = {};
      for (int v in sorted) {
        cnt[v] = (cnt[v] ?? 0) + 1;
      }
      List<int> arr = [];
      bool ok = true;
      for (int x in sorted) {
        if ((cnt[x] ?? 0) == 0) continue;
        cnt[x] = cnt[x]! - 1;
        int higher = x + 2 * k;
        if ((cnt[higher] ?? 0) == 0) {
          ok = false;
          break;
        }
        cnt[higher] = cnt[higher]! - 1;
        arr.add(x + k);
      }
      if (ok && arr.length * 2 == m) return arr;
    }
    return [];
  }
}
```

## Golang

```go
import "sort"

func recoverArray(nums []int) []int {
	sort.Ints(nums)
	n := len(nums) / 2
	for i := 1; i < len(nums); i++ {
		diff := nums[i] - nums[0]
		if diff <= 0 || diff%2 != 0 {
			continue
		}
		k := diff / 2
		cnt := make(map[int]int, len(nums))
		for _, v := range nums {
			cnt[v]++
		}
		res := make([]int, 0, n)
		ok := true
		for _, v := range nums {
			if cnt[v] == 0 {
				continue
			}
			partner := v + 2*k
			if cnt[partner] == 0 {
				ok = false
				break
			}
			cnt[v]--
			cnt[partner]--
			res = append(res, v+k)
		}
		if ok && len(res) == n {
			return res
		}
	}
	return []int{}
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def recover_array(nums)
  nums.sort!
  len = nums.length
  n = len / 2
  base = nums[0]

  (1...len).each do |i|
    diff = nums[i] - base
    next if diff <= 0 || diff.odd?
    k = diff / 2

    cnt = Hash.new(0)
    nums.each { |v| cnt[v] += 1 }

    arr = []
    success = true

    nums.each do |val|
      next if cnt[val] == 0
      higher = val + 2 * k
      if cnt[higher] == 0
        success = false
        break
      end
      cnt[val] -= 1
      cnt[higher] -= 1
      arr << (val + k)
    end

    return arr if success && arr.length == n
  end

  [] # guaranteed to have a solution per problem statement
end
```

## Scala

```scala
object Solution {
    def recoverArray(nums: Array[Int]): Array[Int] = {
        val sorted = nums.sorted
        val n = sorted.length / 2

        for (j <- 1 until sorted.length) {
            val diff = sorted(j) - sorted(0)
            if (diff > 0 && diff % 2 == 0) {
                val k = diff / 2
                val cnt = scala.collection.mutable.Map[Int, Int]()
                for (v <- sorted) {
                    cnt(v) = cnt.getOrElse(v, 0) + 1
                }
                val arr = new scala.collection.mutable.ArrayBuffer[Int]()
                var ok = true

                for (v <- sorted if ok) {
                    val cV = cnt.getOrElse(v, 0)
                    if (cV == 0) {
                        // already paired
                    } else {
                        cnt(v) = cV - 1
                        val w = v + 2 * k
                        val cW = cnt.getOrElse(w, 0)
                        if (cW == 0) {
                            ok = false
                        } else {
                            cnt(w) = cW - 1
                            arr += v + k
                        }
                    }
                }

                if (ok && arr.length == n) return arr.toArray
            }
        }
        Array.emptyIntArray // guaranteed not to reach here
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn recover_array(nums: Vec<i32>) -> Vec<i32> {
        let mut sorted = nums.clone();
        sorted.sort_unstable();

        for i in 1..sorted.len() {
            let diff = sorted[i] - sorted[0];
            if diff <= 0 || diff % 2 != 0 {
                continue;
            }
            let k = diff / 2;
            if let Some(arr) = Self::try_k(&nums, &sorted, k) {
                return arr;
            }
        }
        Vec::new()
    }

    fn try_k(nums: &[i32], sorted: &[i32], k: i32) -> Option<Vec<i32>> {
        let mut cnt: HashMap<i32, usize> = HashMap::new();
        for &v in nums.iter() {
            *cnt.entry(v).or_insert(0) += 1;
        }

        let mut res = Vec::with_capacity(nums.len() / 2);
        for &x in sorted.iter() {
            let cur_cnt = cnt.get_mut(&x)?;
            if *cur_cnt == 0 {
                continue;
            }
            // use x as lower element
            *cur_cnt -= 1;

            let higher_i64 = (x as i64) + 2i64 * (k as i64);
            if higher_i64 < i32::MIN as i64 || higher_i64 > i32::MAX as i64 {
                return None;
            }
            let higher = higher_i64 as i32;

            let higher_cnt = cnt.get_mut(&higher)?;
            if *higher_cnt == 0 {
                return None;
            }
            *higher_cnt -= 1;

            res.push(x + k);
        }

        Some(res)
    }
}
```

## Racket

```racket
(define/contract (recover-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted-nums (sort nums <))
         (n (/ (length sorted-nums) 2))
         (min-val (first sorted-nums)))
    (define (attempt k)
      (let ((cnt (make-hash)))
        ;; build multiset counts
        (for ([v sorted-nums])
          (hash-set! cnt v (+ 1 (hash-ref cnt v 0))))
        (define arr '())
        (define ok? #t)
        (for ([x sorted-nums] #:break (not ok?))
          (when (> (hash-ref cnt x) 0)
            ;; use x as lower
            (hash-set! cnt x (- (hash-ref cnt x) 1))
            (define y (+ x (* 2 k))) ; corresponding higher
            (if (and (hash-has-key? cnt y) (> (hash-ref cnt y) 0))
                (begin
                  (hash-set! cnt y (- (hash-ref cnt y) 1))
                  (set! arr (cons (+ x k) arr)))
                (set! ok? #f))))
        (if ok?
            (reverse arr)
            #f)))
    ;; try all possible ks derived from min-val paired with another element
    (let loop ((i 1))
      (cond [(>= i (length sorted-nums))
             (error "No valid array found, but problem guarantees existence")]
            [else
             (define higher (list-ref sorted-nums i))
             (define diff (- higher min-val))
             (if (and (> diff 0) (= (modulo diff 2) 0))
                 (let ((k (/ diff 2)))
                   (define res (attempt k))
                   (if res
                       res
                       (loop (+ i 1))))
                 (loop (+ i 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([recover_array/1]).

-spec recover_array(Nums :: [integer()]) -> [integer()].
recover_array(Nums) ->
    Sorted = lists:sort(Nums),
    Min = hd(Sorted),
    Candidates0 = [ (X - Min) div 2
                    || X <- tl(Sorted),
                       Diff = X - Min,
                       Diff > 0,
                       Diff rem 2 == 0 ],
    Candidates = lists:usort(Candidates0),
    find_solution(Candidates, Sorted).

find_solution([K | Rest], Sorted) ->
    case try_k(K, Sorted) of
        {ok, Arr} -> Arr;
        error -> find_solution(Rest, Sorted)
    end;
find_solution([], _) -> [].

try_k(K, Sorted) ->
    CountMap = build_counts(Sorted),
    pair_all(Sorted, K, CountMap, []).

pair_all([], _K, _Map, Acc) ->
    {ok, lists:reverse(Acc)};
pair_all([V | Rest], K, Map, Acc) ->
    case maps:get(V, Map, 0) of
        0 ->
            pair_all(Rest, K, Map, Acc);
        C when C > 0 ->
            Higher = V + 2 * K,
            case maps:get(Higher, Map, 0) of
                0 -> error;
                CH when CH > 0 ->
                    M1 = dec_map(Map, V),
                    M2 = dec_map(M1, Higher),
                    pair_all(Rest, K, M2, [V + K | Acc])
            end
    end.

dec_map(Map, Key) ->
    case maps:get(Key, Map) of
        1 -> maps:remove(Key, Map);
        N when N > 1 -> maps:put(Key, N - 1, Map)
    end.

build_counts(List) -> build_counts(List, #{}).

build_counts([], M) -> M;
build_counts([H | T], M) ->
    NewM = case maps:get(H, M, 0) of
        0 -> maps:put(H, 1, M);
        N -> maps:put(H, N + 1, M)
    end,
    build_counts(T, NewM).
```

## Elixir

```elixir
defmodule Solution do
  @spec recover_array(nums :: [integer]) :: [integer]
  def recover_array(nums) do
    sorted = Enum.sort(nums)
    low = hd(sorted)

    candidates =
      sorted
      |> Enum.drop(1)
      |> Enum.filter(fn high ->
        diff = high - low
        rem(diff, 2) == 0 and diff > 0
      end)
      |> Enum.map(&div(&1 - low, 2))
      |> Enum.uniq()

    Enum.reduce_while(candidates, [], fn k, _acc ->
      case try_build(sorted, k) do
        {:ok, arr} -> {:halt, arr}
        :error -> {:cont, []}
      end
    end)
  end

  defp try_build(sorted, k) do
    freq = Enum.reduce(sorted, %{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)

    case build_pairs(sorted, k, freq, []) do
      {arr_rev, true} -> {:ok, Enum.reverse(arr_rev)}
      _ -> :error
    end
  end

  defp build_pairs([], _k, _freq, acc), do: {acc, true}

  defp build_pairs([v | rest], k, freq, acc) do
    cnt = Map.get(freq, v, 0)

    if cnt == 0 do
      build_pairs(rest, k, freq, acc)
    else
      w = v + 2 * k

      case Map.get(freq, w, 0) do
        0 ->
          {[], false}

        _cnt_w ->
          freq1 = dec(freq, v)
          freq2 = dec(freq1, w)
          build_pairs(rest, k, freq2, [v + k | acc])
      end
    end
  end

  defp dec(map, key) do
    case Map.get(map, key) do
      nil -> map
      1 -> Map.delete(map, key)
      cnt -> Map.put(map, key, cnt - 1)
    end
  end
end
```
