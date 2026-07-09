# 3132. Find the Integer Added to Array II

## Cpp

```cpp
class Solution {
public:
    int minimumAddedInteger(vector<int>& nums1, vector<int>& nums2) {
        vector<int> a = nums1;
        vector<int> b = nums2;
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        int n = a.size();
        int ans = INT_MAX;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                vector<int> rem;
                rem.reserve(n - 2);
                for (int k = 0; k < n; ++k) {
                    if (k == i || k == j) continue;
                    rem.push_back(a[k]);
                }
                int x = b[0] - rem[0];
                bool ok = true;
                for (int t = 0; t < (int)rem.size(); ++t) {
                    if (rem[t] + x != b[t]) { ok = false; break; }
                }
                if (ok) ans = min(ans, x);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumAddedInteger(int[] nums1, int[] nums2) {
        int n = nums1.length;
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int[] remaining = new int[n - 2];
                int idx = 0;
                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) continue;
                    remaining[idx++] = nums1[k];
                }
                int diff = nums2[0] - remaining[0];
                boolean ok = true;
                for (int k = 0; k < n - 2; k++) {
                    if (nums2[k] - remaining[k] != diff) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    answer = Math.min(answer, diff);
                }
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        A = sorted(nums1)
        B = sorted(nums2)
        n = len(A)
        best = None

        for i in range(n):
            for j in range(i + 1, n):
                # build remaining list without indices i and j
                C = []
                for k in range(n):
                    if k != i and k != j:
                        C.append(A[k])
                # candidate x from smallest elements
                x = B[0] - C[0]
                ok = True
                for t in range(len(C)):
                    if C[t] + x != B[t]:
                        ok = False
                        break
                if ok:
                    if best is None or x < best:
                        best = x
        return best
```

## Python3

```python
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sorted(nums1)
        s2 = sorted(nums2)
        n = len(s1)
        best = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                rem = []
                for k in range(n):
                    if k != i and k != j:
                        rem.append(s1[k])
                x = s2[0] - rem[0]
                ok = True
                for idx in range(len(rem)):
                    if rem[idx] + x != s2[idx]:
                        ok = False
                        break
                if ok and x < best:
                    best = x
        return best
```

## C

```c
#include <limits.h>
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int minimumAddedInteger(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int A[200];
    int B[200];
    for (int i = 0; i < nums1Size; ++i) A[i] = nums1[i];
    for (int i = 0; i < nums2Size; ++i) B[i] = nums2[i];
    qsort(A, nums1Size, sizeof(int), cmp_int);
    qsort(B, nums2Size, sizeof(int), cmp_int);

    int ans = INT_MAX;
    int n = nums1Size;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int pA = 0;
            int x = 0;
            int haveX = 0;
            int ok = 1;

            for (int k = 0; k < nums2Size; ++k) {
                while (pA == i || pA == j) pA++;
                if (pA >= n) { ok = 0; break; }
                int curX = B[k] - A[pA];
                if (!haveX) {
                    x = curX;
                    haveX = 1;
                } else if (curX != x) {
                    ok = 0;
                    break;
                }
                ++pA;
            }

            if (ok && haveX && x < ans) ans = x;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumAddedInteger(int[] nums1, int[] nums2) {
        Array.Sort(nums1);
        Array.Sort(nums2);
        int n = nums1.Length;
        int answer = int.MaxValue;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int idxB = 0;
                bool first = true;
                int x = 0;
                bool ok = true;

                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) continue;
                    int aVal = nums1[k];
                    int bVal = nums2[idxB];

                    if (first) {
                        x = bVal - aVal;
                        first = false;
                    } else if (bVal - aVal != x) {
                        ok = false;
                        break;
                    }
                    idxB++;
                }

                if (ok) {
                    answer = Math.Min(answer, x);
                }
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minimumAddedInteger = function(nums1, nums2) {
    const n = nums1.length;
    const target = [...nums2].sort((a, b) => a - b);
    let best = Infinity;

    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            const remain = [];
            for (let k = 0; k < n; ++k) {
                if (k !== i && k !== j) remain.push(nums1[k]);
            }
            remain.sort((a, b) => a - b);
            const diff = target[0] - remain[0];
            let ok = true;
            for (let t = 1; t < remain.length; ++t) {
                if (target[t] - remain[t] !== diff) {
                    ok = false;
                    break;
                }
            }
            if (ok && diff < best) best = diff;
        }
    }

    return best;
};
```

## Typescript

```typescript
function minimumAddedInteger(nums1: number[], nums2: number[]): number {
    const a = [...nums1].sort((p, q) => p - q);
    const b = [...nums2].sort((p, q) => p - q);
    const n = a.length;
    let best = Infinity;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const c: number[] = [];
            for (let k = 0; k < n; k++) {
                if (k === i || k === j) continue;
                c.push(a[k]);
            }
            const x = b[0] - c[0];
            let ok = true;
            for (let idx = 0; idx < c.length; idx++) {
                if (c[idx] + x !== b[idx]) {
                    ok = false;
                    break;
                }
            }
            if (ok && x < best) {
                best = x;
            }
        }
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minimumAddedInteger($nums1, $nums2) {
        sort($nums1);
        sort($nums2);
        $n = count($nums1);
        $answer = null;

        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                // Build remaining array after removing indices i and j
                $remaining = [];
                for ($k = 0; $k < $n; $k++) {
                    if ($k === $i || $k === $j) continue;
                    $remaining[] = $nums1[$k];
                }

                // Candidate x based on first elements
                $x = $nums2[0] - $remaining[0];
                $valid = true;
                $m = count($remaining);
                for ($t = 0; $t < $m; $t++) {
                    if ($remaining[$t] + $x !== $nums2[$t]) {
                        $valid = false;
                        break;
                    }
                }

                if ($valid) {
                    if ($answer === null || $x < $answer) {
                        $answer = $x;
                    }
                }
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minimumAddedInteger(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let a = nums1.sorted()
        let b = nums2.sorted()
        let n = a.count
        var answer = Int.max
        
        for i in 0..<n {
            for j in (i + 1)..<n {
                var remaining = [Int]()
                remaining.reserveCapacity(n - 2)
                for k in 0..<n {
                    if k == i || k == j { continue }
                    remaining.append(a[k])
                }
                
                let x = b[0] - remaining[0]
                var valid = true
                for idx in 0..<(n - 2) {
                    if remaining[idx] + x != b[idx] {
                        valid = false
                        break
                    }
                }
                
                if valid && x < answer {
                    answer = x
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumAddedInteger(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        val sortedNums2 = nums2.sorted()
        var best: Int? = null
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val remaining = mutableListOf<Int>()
                for (k in 0 until n) {
                    if (k != i && k != j) remaining.add(nums1[k])
                }
                val sortedRem = remaining.sorted()
                val diff = sortedNums2[0] - sortedRem[0]
                var ok = true
                for (idx in 1 until sortedRem.size) {
                    if (sortedNums2[idx] - sortedRem[idx] != diff) {
                        ok = false
                        break
                    }
                }
                if (ok) {
                    best = if (best == null) diff else kotlin.math.min(best, diff)
                }
            }
        }
        return best!!
    }
}
```

## Dart

```dart
class Solution {
  int minimumAddedInteger(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    int m = nums2.length; // n - 2
    List<int> sortedNums2 = List.from(nums2)..sort();
    const int INF = 1 << 60;
    int best = INF;

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        List<int> remaining = [];
        for (int k = 0; k < n; ++k) {
          if (k != i && k != j) remaining.add(nums1[k]);
        }
        remaining.sort();
        int diff = sortedNums2[0] - remaining[0];
        bool ok = true;
        for (int t = 0; t < m; ++t) {
          if (sortedNums2[t] - remaining[t] != diff) {
            ok = false;
            break;
          }
        }
        if (ok && diff < best) best = diff;
      }
    }

    return best;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"sort"
)

func minimumAddedInteger(nums1 []int, nums2 []int) int {
	n1 := make([]int, len(nums1))
	copy(n1, nums1)
	sort.Ints(n1)

	n2 := make([]int, len(nums2))
	copy(n2, nums2)
	sort.Ints(n2)

	best := math.MaxInt64
	n := len(n1)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			rem := make([]int, 0, n-2)
			for k := 0; k < n; k++ {
				if k == i || k == j {
					continue
				}
				rem = append(rem, n1[k])
			}
			x := n2[0] - rem[0]
			ok := true
			for idx := 0; idx < len(rem); idx++ {
				if rem[idx]+x != n2[idx] {
					ok = false
					break
				}
			}
			if ok && x < best {
				best = x
			}
		}
	}
	return best
}
```

## Ruby

```ruby
def minimum_added_integer(nums1, nums2)
  s1 = nums1.sort
  s2 = nums2.sort
  n = s1.length
  ans = nil

  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      # find first kept index after removing i and j
      k0 = nil
      (0...n).each do |k|
        next if k == i || k == j
        k0 = k
        break
      end

      x = s2[0] - s1[k0]
      ok = true
      t = 0
      (0...n).each do |k|
        next if k == i || k == j
        if s1[k] + x != s2[t]
          ok = false
          break
        end
        t += 1
      end

      if ok
        ans = ans.nil? ? x : [ans, x].min
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minimumAddedInteger(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        val sortedNums2 = nums2.sorted
        var best = Int.MaxValue

        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                val buf = new scala.collection.mutable.ArrayBuffer[Int]()
                var k = 0
                while (k < n) {
                    if (k != i && k != j) buf += nums1(k)
                    k += 1
                }
                val sortedR = buf.toArray.sorted
                val diff = sortedNums2(0) - sortedR(0)

                var ok = true
                var idx = 0
                while (ok && idx < sortedR.length) {
                    if (sortedNums2(idx) - sortedR(idx) != diff) ok = false
                    idx += 1
                }

                if (ok && diff < best) best = diff
            }
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_added_integer(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut a = nums1.clone();
        a.sort_unstable();
        let mut b = nums2.clone();
        b.sort_unstable();

        let n = a.len();
        let m = b.len(); // n - 2
        let mut ans = i32::MAX;

        for i in 0..n {
            for j in (i + 1)..n {
                let mut rem: Vec<i32> = Vec::with_capacity(m);
                for k in 0..n {
                    if k != i && k != j {
                        rem.push(a[k]);
                    }
                }
                let diff = b[0] - rem[0];
                let mut ok = true;
                for idx in 0..m {
                    if rem[idx] + diff != b[idx] {
                        ok = false;
                        break;
                    }
                }
                if ok && diff < ans {
                    ans = diff;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-added-integer nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((sorted1 (sort nums1 <))
         (sorted2 (sort nums2 <))
         (n (length sorted1)))
    (define candidates
      (for/list ([i (in-range n)]
                 [j (in-range (+ i 1) n)])
        (let* ((rem (for/list ([idx (in-range n)]
                               #:when (and (not (= idx i)) (not (= idx j))))
                      (list-ref sorted1 idx)))
               (x (- (first sorted2) (apply min rem)))
               (transformed (sort (map (lambda (v) (+ v x)) rem) <)))
          (if (equal? transformed sorted2) x #f))))
    (apply min (filter (lambda (v) (not (eq? v #f))) candidates))))
```

## Erlang

```erlang
-export([minimum_added_integer/2]).

-spec minimum_added_integer(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
minimum_added_integer(Nums1, Nums2) ->
    S1 = lists:sort(Nums1),
    S2 = lists:sort(Nums2),
    Len1 = length(S1),
    MinX = loop_i(0, Len1, S1, S2, undefined),
    MinX.

loop_i(I, Len1, _S1, _S2, Min) when I >= Len1 - 1 ->
    Min;
loop_i(I, Len1, S1, S2, Min) ->
    NewMin = loop_j(I, I + 1, Len1, S1, S2, Min),
    loop_i(I + 1, Len1, S1, S2, NewMin).

loop_j(_I, J, Len1, _S1, _S2, Min) when J >= Len1 ->
    Min;
loop_j(I, J, Len1, S1, S2, Min) ->
    Remaining = remove_two(S1, I, J),
    X = hd(S2) - hd(Remaining),
    UpdatedMin =
        case verify(Remaining, S2, X) of
            true ->
                case Min of
                    undefined -> X;
                    _ when X < Min -> X;
                    _ -> Min
                end;
            false -> Min
        end,
    loop_j(I, J + 1, Len1, S1, S2, UpdatedMin).

remove_two(List, I, J) ->
    remove_two(List, 0, I, J).

remove_two([], _Pos, _I, _J) ->
    [];
remove_two([H|T], Pos, I, J) ->
    if
        Pos =:= I; Pos =:= J ->
            remove_two(T, Pos + 1, I, J);
        true ->
            [H | remove_two(T, Pos + 1, I, J)]
    end.

verify([], [], _X) ->
    true;
verify([R|Rs], [S|Ss], X) ->
    if
        R + X =:= S -> verify(Rs, Ss, X);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_added_integer(nums1 :: [integer], nums2 :: [integer]) :: integer
  def minimum_added_integer(nums1, nums2) do
    s1 = Enum.sort(nums1)
    s2 = Enum.sort(nums2)
    n = length(s1)

    candidates =
      for i <- 0..(n - 1), j <- (i + 1)..(n - 1) do
        remaining =
          s1
          |> Enum.with_index()
          |> Enum.filter(fn {_val, idx} -> idx != i and idx != j end)
          |> Enum.map(&elem(&1, 0))

        x = List.first(s2) - List.first(remaining)

        if Enum.zip(remaining, s2) |> Enum.all?(fn {a, b} -> a + x == b end) do
          x
        else
          nil
        end
      end
      |> Enum.filter(& &1)

    Enum.min(candidates)
  end
end
```
