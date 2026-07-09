# 1898. Maximum Number of Removable Characters

## Cpp

```cpp
class Solution {
public:
    int maximumRemovals(string s, string p, vector<int>& removable) {
        int n = s.size();
        const int INF = 1e9;
        vector<int> step(n, INF);
        for (int i = 0; i < (int)removable.size(); ++i) {
            step[removable[i]] = i + 1; // removal order (1-indexed)
        }
        auto can = [&](int k) -> bool {
            int j = 0;
            for (int i = 0; i < n && j < (int)p.size(); ++i) {
                if (step[i] > k && s[i] == p[j]) {
                    ++j;
                }
            }
            return j == (int)p.size();
        };
        int low = 0, high = removable.size();
        while (low < high) {
            int mid = (low + high + 1) / 2;
            if (can(mid)) low = mid;
            else high = mid - 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public int maximumRemovals(String s, String p, int[] removable) {
        int n = s.length();
        int[] removalOrder = new int[n];
        java.util.Arrays.fill(removalOrder, Integer.MAX_VALUE);
        for (int i = 0; i < removable.length; i++) {
            removalOrder[removable[i]] = i + 1; // 1‑based step at which this index is removed
        }

        int low = 0, high = removable.length;
        while (low < high) {
            int mid = (low + high + 1) >>> 1; // try to keep mid removals
            if (isSubsequenceAfterRemovals(s, p, removalOrder, mid)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private boolean isSubsequenceAfterRemovals(String s, String p, int[] order, int k) {
        int pi = 0;
        int plen = p.length();
        for (int i = 0; i < s.length() && pi < plen; i++) {
            if (order[i] <= k) continue; // this character is removed
            if (s.charAt(i) == p.charAt(pi)) {
                pi++;
            }
        }
        return pi == plen;
    }
}
```

## Python

```python
class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        n = len(s)

        def can(k):
            removed = [False] * n
            for i in range(k):
                removed[removable[i]] = True
            j = 0  # pointer in p
            for idx, ch in enumerate(s):
                if removed[idx]:
                    continue
                if j < len(p) and ch == p[j]:
                    j += 1
                    if j == len(p):
                        break
            return j == len(p)

        low, high = 0, len(removable)
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## Python3

```python
from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        order = [float('inf')] * n
        for idx, pos in enumerate(removable):
            order[pos] = idx

        def can(k: int) -> bool:
            i = 0
            plen = len(p)
            for j, ch in enumerate(s):
                if order[j] < k:
                    continue
                if ch == p[i]:
                    i += 1
                    if i == plen:
                        return True
            return i == plen

        low, high = 0, len(removable)
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <limits.h>

int maximumRemovals(char* s, char* p, int* removable, int removableSize) {
    int n = strlen(s);
    int m = strlen(p);
    
    int *remStep = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) remStep[i] = INT_MAX;
    for (int i = 0; i < removableSize; ++i) {
        remStep[removable[i]] = i + 1; // removal order (1‑based)
    }
    
    int lo = 0, hi = removableSize, ans = 0;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int j = 0;
        for (int i = 0; i < n && j < m; ++i) {
            if (remStep[i] > mid && s[i] == p[j]) {
                ++j;
            }
        }
        if (j == m) {          // p is still a subsequence
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    
    free(remStep);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumRemovals(string s, string p, int[] removable) {
        int n = s.Length;
        int[] removalStep = new int[n];
        for (int i = 0; i < n; i++) removalStep[i] = int.MaxValue;
        for (int i = 0; i < removable.Length; i++) {
            removalStep[removable[i]] = i + 1; // steps are 1‑based
        }

        bool Can(int k) {
            int j = 0;
            for (int i = 0; i < n && j < p.Length; i++) {
                if (removalStep[i] <= k) continue; // removed
                if (s[i] == p[j]) j++;
            }
            return j == p.Length;
        }

        int lo = 0, hi = removable.Length;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @param {number[]} removable
 * @return {number}
 */
var maximumRemovals = function(s, p, removable) {
    const n = s.length;
    const order = new Array(n).fill(Number.MAX_SAFE_INTEGER);
    for (let i = 0; i < removable.length; ++i) {
        order[removable[i]] = i + 1; // 1‑based rank
    }

    const can = (k) => {
        let j = 0;
        for (let i = 0; i < n && j < p.length; ++i) {
            if (order[i] <= k) continue; // removed
            if (s[i] === p[j]) ++j;
        }
        return j === p.length;
    };

    let low = 0, high = removable.length;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maximumRemovals(s: string, p: string, removable: number[]): number {
    const n = s.length;
    const order = new Array<number>(n).fill(Infinity);
    for (let i = 0; i < removable.length; ++i) {
        order[removable[i]] = i + 1; // removal step (1‑based)
    }

    const can = (k: number): boolean => {
        let j = 0;
        for (let i = 0; i < n && j < p.length; ++i) {
            if (order[i] > k && s[i] === p[j]) {
                ++j;
            }
        }
        return j === p.length;
    };

    let low = 0, high = removable.length;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @param Integer[] $removable
     * @return Integer
     */
    function maximumRemovals($s, $p, $removable) {
        $n = strlen($s);
        $order = array_fill(0, $n, PHP_INT_MAX);
        foreach ($removable as $idx => $pos) {
            $order[$pos] = $idx;
        }

        $lenP = strlen($p);
        $can = function(int $k) use ($s, $p, $order, $lenP): bool {
            $j = 0;
            $n = strlen($s);
            for ($i = 0; $i < $n && $j < $lenP; $i++) {
                if ($order[$i] < $k) {
                    continue; // removed
                }
                if ($s[$i] === $p[$j]) {
                    $j++;
                }
            }
            return $j === $lenP;
        };

        $low = 0;
        $high = count($removable);
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2); // upper mid
            if ($can($mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func maximumRemovals(_ s: String, _ p: String, _ removable: [Int]) -> Int {
        let sArr = Array(s)
        let pArr = Array(p)
        let n = sArr.count
        var removalOrder = Array(repeating: Int.max, count: n)
        for (idx, pos) in removable.enumerated() {
            removalOrder[pos] = idx + 1   // 1‑based order
        }
        
        func canKeep(_ k: Int) -> Bool {
            var j = 0
            let pLen = pArr.count
            if pLen == 0 { return true }
            for i in 0..<n {
                if removalOrder[i] <= k { continue }   // character removed
                if sArr[i] == pArr[j] {
                    j += 1
                    if j == pLen { break }
                }
            }
            return j == pLen
        }
        
        var low = 0
        var high = removable.count
        while low < high {
            let mid = (low + high + 1) / 2   // upper middle
            if canKeep(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumRemovals(s: String, p: String, removable: IntArray): Int {
        var low = 0
        var high = removable.size
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (canForm(s, p, removable, mid)) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }

    private fun canForm(s: String, p: String, removable: IntArray, k: Int): Boolean {
        val removed = BooleanArray(s.length)
        for (i in 0 until k) {
            removed[removable[i]] = true
        }
        var j = 0
        if (p.isEmpty()) return true
        for (idx in s.indices) {
            if (!removed[idx] && s[idx] == p[j]) {
                j++
                if (j == p.length) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  int maximumRemovals(String s, String p, List<int> removable) {
    int n = s.length;
    List<int> order = List.filled(n, -1);
    for (int i = 0; i < removable.length; i++) {
      order[removable[i]] = i;
    }

    bool can(int k) {
      int pi = 0;
      for (int i = 0; i < n && pi < p.length; i++) {
        if (order[i] != -1 && order[i] < k) continue; // removed
        if (s.codeUnitAt(i) == p.codeUnitAt(pi)) {
          pi++;
        }
      }
      return pi == p.length;
    }

    int low = 0, high = removable.length;
    while (low < high) {
      int mid = (low + high + 1) >> 1;
      if (can(mid)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func maximumRemovals(s string, p string, removable []int) int {
	n := len(s)
	m := len(removable)

	// step[i] = the 1‑based order in which index i is removed,
	// or a value larger than m if it is never removed.
	step := make([]int, n)
	inf := m + 1
	for i := range step {
		step[i] = inf
	}
	for i, idx := range removable {
		step[idx] = i + 1 // removal order (1‑based)
	}

	isSubseq := func(k int) bool {
		j := 0
		for i := 0; i < n && j < len(p); i++ {
			if step[i] > k && s[i] == p[j] {
				j++
			}
		}
		return j == len(p)
	}

	low, high := 0, m
	for low < high {
		mid := (low + high + 1) / 2 // try larger k
		if isSubseq(mid) {
			low = mid
		} else {
			high = mid - 1
		}
	}
	return low
}
```

## Ruby

```ruby
def maximum_removals(s, p, removable)
  n = s.length
  order = Array.new(n, n + 1)
  removable.each_with_index { |idx, i| order[idx] = i + 1 }

  check = lambda do |k|
    i = 0
    j = 0
    while i < n && j < p.length
      if order[i] <= k
        i += 1
        next
      end
      j += 1 if s[i] == p[j]
      i += 1
    end
    j == p.length
  end

  low = 0
  high = removable.length
  while low < high
    mid = (low + high + 1) / 2
    if check.call(mid)
      low = mid
    else
      high = mid - 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
    def maximumRemovals(s: String, p: String, removable: Array[Int]): Int = {
        val n = s.length
        val removalStep = Array.fill(n)(Int.MaxValue)
        for (i <- removable.indices) {
            removalStep(removable(i)) = i + 1 // step when this index is removed (1‑based)
        }

        def canRemove(k: Int): Boolean = {
            var j = 0
            val m = p.length
            var i = 0
            while (i < n && j < m) {
                if (removalStep(i) > k) { // character remains after removing first k indices
                    if (s.charAt(i) == p.charAt(j)) j += 1
                }
                i += 1
            }
            j == m
        }

        var low = 0
        var high = removable.length
        while (low < high) {
            val mid = (low + high + 1) >>> 1 // upper middle
            if (canRemove(mid)) low = mid else high = mid - 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_removals(s: String, p: String, removable: Vec<i32>) -> i32 {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();
        let n = s_bytes.len();
        let m = removable.len();

        // order[i] = position of index i in removable, or usize::MAX if never removed
        let mut order = vec![usize::MAX; n];
        for (i, &idx) in removable.iter().enumerate() {
            order[idx as usize] = i;
        }

        // check if p is subsequence after removing first k indices from removable
        let can = |k: usize| -> bool {
            let mut j = 0usize;
            for (i, &ch) in s_bytes.iter().enumerate() {
                if order[i] < k {
                    continue; // this character is removed
                }
                if j < p_bytes.len() && ch == p_bytes[j] {
                    j += 1;
                    if j == p_bytes.len() {
                        break;
                    }
                }
            }
            j == p_bytes.len()
        };

        let mut low = 0usize;
        let mut high = m;
        while low < high {
            let mid = (low + high + 1) / 2;
            if can(mid) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }

        low as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-removals s p removable)
  (-> string? string? (listof exact-integer?) exact-integer?)
  (let* ((n (string-length s))
         (rem-vec (list->vector removable))
         (m (vector-length rem-vec)))
    ;; predicate: can we keep p as subsequence after removing first k indices?
    (define (can? k)
      (let ((removed (make-vector n #f)))
        (let loop ((i 0))
          (when (< i k)
            (vector-set! removed (vector-ref rem-vec i) #t)
            (loop (add1 i))))
        (let ((p-len (string-length p)))
          (let loop2 ((i 0) (j 0))
            (cond
              [(= j p-len) #t]
              [(>= i n) #f]
              [else
               (if (vector-ref removed i)
                   (loop2 (add1 i) j)
                   (if (char=? (string-ref s i) (string-ref p j))
                       (loop2 (add1 i) (add1 j))
                       (loop2 (add1 i) j)))])))))
    ;; binary search for maximum feasible k
    (let loop ((lo 0) (hi m))
      (if (> lo hi)
          (- lo 1)
          (let ((mid (quotient (+ lo hi) 2)))
            (if (can? mid)
                (loop (add1 mid) hi)
                (loop lo (sub1 mid))))))))
```

## Erlang

```erlang
-spec maximum_removals(S :: unicode:unicode_binary(), P :: unicode:unicode_binary(), Removable :: [integer()]) -> integer().
maximum_removals(S, P, Removable) ->
    SList = binary_to_list(S),
    PList = binary_to_list(P),
    RemMap = build_map(Removable, 1, #{}),
    LenRem = length(Removable),
    bs(0, LenRem, SList, PList, RemMap).

build_map([], _Step, Map) -> Map;
build_map([Idx|Rest], Step, Map) ->
    build_map(Rest, Step + 1, maps:put(Idx, Step, Map)).

bs(Low, High, _SList, _PList, _RemMap) when Low >= High ->
    Low;
bs(Low, High, SList, PList, RemMap) ->
    Mid = (Low + High + 1) div 2,
    case can(Mid, SList, PList, 0, RemMap) of
        true -> bs(Mid, High, SList, PList, RemMap);
        false -> bs(Low, Mid - 1, SList, PList, RemMap)
    end.

can(_K, _SList, [], _Idx, _RemMap) ->
    true;
can(K, [Sc|Ss], [Pc|Ps] = PList, Idx, RemMap) ->
    RemovedStep = maps:get(Idx, RemMap, 0),
    if (RemovedStep == 0 orelse RemovedStep > K) andalso Sc == Pc ->
            can(K, Ss, Ps, Idx + 1, RemMap);
       true ->
            can(K, Ss, PList, Idx + 1, RemMap)
    end;
can(_K, [], _PList, _Idx, _RemMap) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_removals(s :: String.t(), p :: String.t(), removable :: [integer]) :: integer
  def maximum_removals(s, p, removable) do
    step_map = build_step_map(removable)
    max_k = length(removable)

    binary_search(0, max_k, -1, s, p, step_map)
  end

  defp build_step_map(removable) do
    Enum.with_index(removable, 1)
    |> Enum.reduce(%{}, fn {idx, order}, acc -> Map.put(acc, idx, order) end)
  end

  defp binary_search(low, high, ans, _s_bin, _p_bin, _step_map) when low > high do
    ans
  end

  defp binary_search(low, high, ans, s_bin, p_bin, step_map) do
    mid = div(low + high, 2)

    if can?(mid, s_bin, p_bin, step_map, 0) do
      binary_search(mid + 1, high, mid, s_bin, p_bin, step_map)
    else
      binary_search(low, mid - 1, ans, s_bin, p_bin, step_map)
    end
  end

  defp can?(k, _s_bin, p_bin, _step_map, _idx) when byte_size(p_bin) == 0 do
    true
  end

  defp can?(_k, <<>>, _p_bin, _step_map, _idx), do: false

  defp can?(k, <<sc, s_rest::binary>>, p_bin, step_map, idx) do
    removed =
      case Map.get(step_map, idx) do
        nil -> false
        order when order <= k -> true
        _ -> false
      end

    if not removed do
      <<pc, p_rest::binary>> = p_bin

      if sc == pc do
        can?(k, s_rest, p_rest, step_map, idx + 1)
      else
        can?(k, s_rest, p_bin, step_map, idx + 1)
      end
    else
      can?(k, s_rest, p_bin, step_map, idx + 1)
    end
  end
end
```
