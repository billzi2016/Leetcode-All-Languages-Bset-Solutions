# 2305. Fair Distribution of Cookies

## Cpp

```cpp
class Solution {
public:
    int distributeCookies(vector<int>& cookies, int k) {
        sort(cookies.rbegin(), cookies.rend()); // assign larger bags first for better pruning
        int n = cookies.size();
        vector<int> sum(k, 0);
        int ans = INT_MAX;
        
        function<void(int,int)> dfs = [&](int idx, int zero) {
            if (idx == n) {
                int cur = *max_element(sum.begin(), sum.end());
                ans = min(ans, cur);
                return;
            }
            // prune: not enough remaining bags to give each empty child at least one bag
            if (n - idx < zero) return;
            // prune: current max already exceeds known answer
            int curMax = *max_element(sum.begin(), sum.end());
            if (curMax >= ans) return;
            
            for (int i = 0; i < k; ++i) {
                bool wasZero = (sum[i] == 0);
                sum[i] += cookies[idx];
                dfs(idx + 1, zero - (wasZero ? 1 : 0));
                sum[i] -= cookies[idx];
                
                // If we placed the current bag into an empty child,
                // no need to try other empty children (symmetry pruning)
                if (wasZero) break;
            }
        };
        
        dfs(0, k);
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int[] sums;
    private int[] cookies;
    private int k;
    private int best;

    public int distributeCookies(int[] cookies, int k) {
        this.cookies = cookies;
        this.k = k;
        this.sums = new int[k];
        this.best = Integer.MAX_VALUE;
        dfs(0);
        return best;
    }

    private void dfs(int idx) {
        if (idx == cookies.length) {
            int curMax = 0;
            for (int s : sums) {
                if (s > curMax) curMax = s;
            }
            if (curMax < best) best = curMax;
            return;
        }

        for (int i = 0; i < k; i++) {
            sums[i] += cookies[idx];
            int curMax = 0;
            for (int s : sums) {
                if (s > curMax) curMax = s;
            }
            if (curMax < best) {
                dfs(idx + 1);
            }
            sums[i] -= cookies[idx];

            // avoid symmetric states: if this child had no cookies before adding,
            // then assigning the current bag to any later empty child yields equivalent states.
            if (sums[i] == 0) break;
        }
    }
}
```

## Python

```python
class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cookies)
        cookies.sort(reverse=True)  # larger bags first for better pruning
        loads = [0] * k
        best = sum(cookies)

        def dfs(idx, zero):
            nonlocal best
            if idx == n:
                cur_max = max(loads)
                if cur_max < best:
                    best = cur_max
                return
            # not enough remaining bags to give each empty child at least one bag
            if n - idx < zero:
                return
            # current maximum already not better than best
            cur_max = max(loads)
            if cur_max >= best:
                return

            bag = cookies[idx]
            seen = set()
            for i in range(k):
                if loads[i] in seen:  # skip symmetric states
                    continue
                seen.add(loads[i])
                new_zero = zero - (1 if loads[i] == 0 else 0)
                loads[i] += bag
                dfs(idx + 1, new_zero)
                loads[i] -= bag

        dfs(0, k)
        return best
```

## Python3

```python
class Solution:
    def distributeCookies(self, cookies, k):
        from math import inf
        n = len(cookies)
        cookies.sort(reverse=True)  # assign larger bags first for better pruning
        distribute = [0] * k
        ans = sum(cookies)

        def dfs(idx, zero):
            nonlocal ans
            if idx == n:
                cur = max(distribute)
                if cur < ans:
                    ans = cur
                return
            # not enough remaining bags to give each empty child at least one bag
            if n - idx < zero:
                return

            for j in range(k):
                before = distribute[j]
                distribute[j] += cookies[idx]
                new_zero = zero - 1 if before == 0 else zero

                # prune if current max already exceeds known answer
                if max(distribute) < ans:
                    dfs(idx + 1, new_zero)

                distribute[j] = before
                # symmetry breaking: if this child was empty and we chose not to put the bag,
                # no need to try other empty children at this level
                if before == 0:
                    break

        dfs(0, k)
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int n;
static int kGlobal;
static int *cookiesArr;
static int best;

static int cmpDesc(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return y - x; // descending
}

static void dfs(int idx, int zeroCount, int *loads) {
    if (idx == n) {
        int curMax = 0;
        for (int i = 0; i < kGlobal; ++i)
            if (loads[i] > curMax) curMax = loads[i];
        if (curMax < best) best = curMax;
        return;
    }

    int remaining = n - idx;
    if (remaining < zeroCount) return; // impossible to give each empty child a bag

    int curMaxSoFar = 0;
    for (int i = 0; i < kGlobal; ++i)
        if (loads[i] > curMaxSoFar) curMaxSoFar = loads[i];
    if (curMaxSoFar >= best) return; // cannot improve current best

    for (int j = 0; j < kGlobal; ++j) {
        // skip duplicate states to reduce symmetry
        int dup = 0;
        for (int p = 0; p < j; ++p)
            if (loads[p] == loads[j]) { dup = 1; break; }
        if (dup) continue;

        int before = loads[j];
        loads[j] += cookiesArr[idx];
        int newZero = zeroCount - (before == 0 ? 1 : 0);
        dfs(idx + 1, newZero, loads);
        loads[j] = before;
    }
}

int distributeCookies(int* cookies, int cookiesSize, int k) {
    n = cookiesSize;
    kGlobal = k;

    cookiesArr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) cookiesArr[i] = cookies[i];
    qsort(cookiesArr, n, sizeof(int), cmpDesc); // larger bags first

    int *loads = (int *)calloc(kGlobal, sizeof(int));
    best = INT_MAX;

    dfs(0, kGlobal, loads);

    free(cookiesArr);
    free(loads);
    return best;
}
```

## Csharp

```csharp
public class Solution {
    private int[] cookiesArr;
    private int n;
    private int k;
    private int[] sums;
    private int best;

    public int DistributeCookies(int[] cookies, int k) {
        this.cookiesArr = (int[])cookies.Clone();
        System.Array.Sort(this.cookiesArr);
        System.Array.Reverse(this.cookiesArr); // descending order for better pruning
        this.n = this.cookiesArr.Length;
        this.k = k;
        sums = new int[k];
        best = int.MaxValue;
        Dfs(0, k);
        return best;
    }

    private void Dfs(int idx, int zeroCount) {
        if (idx == n) {
            int curMax = 0;
            foreach (int s in sums) if (s > curMax) curMax = s;
            if (curMax < best) best = curMax;
            return;
        }

        // Not enough remaining bags to give each empty child at least one bag
        if (n - idx < zeroCount) return;

        int cookie = cookiesArr[idx];
        bool placedZero = false; // avoid symmetric assignments to multiple empty children

        for (int i = 0; i < k; ++i) {
            if (sums[i] == 0) {
                if (placedZero) continue;
                placedZero = true;
            }

            int prev = sums[i];
            bool wasZero = prev == 0;
            sums[i] += cookie;
            int newZeroCount = zeroCount - (wasZero ? 1 : 0);

            // Prune if current max already exceeds known best
            int curMax = 0;
            foreach (int s in sums) if (s > curMax) curMax = s;
            if (curMax < best) {
                Dfs(idx + 1, newZeroCount);
            }

            sums[i] = prev; // backtrack
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cookies
 * @param {number} k
 * @return {number}
 */
var distributeCookies = function(cookies, k) {
    const n = cookies.length;
    // sort descending to improve pruning
    cookies.sort((a, b) => b - a);
    const sums = new Array(k).fill(0);
    let ans = Infinity;

    const dfs = (idx, zeroCount) => {
        if (idx === n) {
            const cur = Math.max(...sums);
            if (cur < ans) ans = cur;
            return;
        }
        // not enough remaining bags to give each empty child at least one
        if (n - idx < zeroCount) return;

        for (let i = 0; i < k; ++i) {
            const before = sums[i];
            sums[i] += cookies[idx];
            const newZero = before === 0 ? zeroCount - 1 : zeroCount;
            // prune if current max already not better than best answer
            if (sums[i] < ans) {
                dfs(idx + 1, newZero);
            }
            sums[i] = before; // backtrack
        }
    };

    dfs(0, k);
    return ans;
};
```

## Typescript

```typescript
function distributeCookies(cookies: number[], k: number): number {
    const n = cookies.length;
    // Assign larger bags first for better pruning
    cookies.sort((a, b) => b - a);
    const sums = new Array(k).fill(0);
    let best = Number.MAX_SAFE_INTEGER;

    function dfs(idx: number, zeroCnt: number, curMax: number): void {
        if (idx === n) {
            if (curMax < best) best = curMax;
            return;
        }
        // Not enough remaining bags to give each empty child at least one bag
        if (n - idx < zeroCnt) return;

        const val = cookies[idx];
        for (let i = 0; i < k; ++i) {
            // Skip symmetric states: children with identical current sums
            if (i > 0 && sums[i] === sums[i - 1]) continue;

            const wasZero = sums[i] === 0;
            sums[i] += val;
            const newMax = Math.max(curMax, sums[i]);
            if (newMax < best) {
                dfs(idx + 1, zeroCnt - (wasZero ? 1 : 0), newMax);
            }
            sums[i] -= val; // backtrack
        }
    }

    dfs(0, k, 0);
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cookies
     * @param Integer $k
     * @return Integer
     */
    function distributeCookies($cookies, $k) {
        rsort($cookies); // assign larger bags first for better pruning
        $sum = array_fill(0, $k, 0);
        $ans = PHP_INT_MAX;
        $n = count($cookies);

        $dfs = function ($idx) use (&$dfs, &$cookies, $k, &$sum, &$ans, $n) {
            if ($idx == $n) {
                $current = max($sum);
                if ($current < $ans) {
                    $ans = $current;
                }
                return;
            }

            $c = $cookies[$idx];
            for ($i = 0; $i < $k; $i++) {
                $sum[$i] += $c;

                // prune if current max already exceeds known answer
                $maxSoFar = max($sum);
                if ($maxSoFar < $ans) {
                    $dfs($idx + 1);
                }

                $sum[$i] -= $c;

                // If this child had no cookies before adding, break to avoid symmetric states
                if ($sum[$i] == 0) {
                    break;
                }
            }
        };

        $dfs(0);
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func distributeCookies(_ cookies: [Int], _ k: Int) -> Int {
        let sorted = cookies.sorted(by: >)
        var sums = Array(repeating: 0, count: k)
        var answer = Int.max
        let n = sorted.count

        func dfs(_ idx: Int, _ zeroCount: Int) {
            // prune if current max already not better than best
            var curMax = 0
            for v in sums where v > curMax { curMax = v }
            if curMax >= answer { return }

            // not enough remaining bags to give each empty child at least one bag
            if n - idx < zeroCount { return }

            if idx == n {
                var maxVal = 0
                for v in sums where v > maxVal { maxVal = v }
                if maxVal < answer { answer = maxVal }
                return
            }

            let cookie = sorted[idx]
            for i in 0..<k {
                var newZero = zeroCount
                if sums[i] == 0 { newZero -= 1 }
                sums[i] += cookie

                dfs(idx + 1, newZero)

                sums[i] -= cookie
                // avoid symmetric states: only try first empty child
                if sums[i] == 0 {
                    break
                }
            }
        }

        dfs(0, k)
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distributeCookies(cookies: IntArray, k: Int): Int {
        val n = cookies.size
        val sums = IntArray(k)
        var best = Int.MAX_VALUE

        fun dfs(idx: Int, zeroCount: Int) {
            if (idx == n) {
                val curMax = sums.maxOrNull() ?: 0
                if (curMax < best) best = curMax
                return
            }
            // not enough remaining bags to give at least one to each child without cookies yet
            if (n - idx < zeroCount) return

            for (j in 0 until k) {
                var newZero = zeroCount
                if (sums[j] == 0) newZero--
                sums[j] += cookies[idx]

                // prune if current max already not better than best
                val curMax = sums.maxOrNull() ?: 0
                if (curMax < best) {
                    dfs(idx + 1, newZero)
                }

                sums[j] -= cookies[idx]
            }
        }

        dfs(0, k)
        return best
    }
}
```

## Dart

```dart
class Solution {
  int distributeCookies(List<int> cookies, int k) {
    List<int> sorted = List.from(cookies);
    sorted.sort((a, b) => b.compareTo(a));
    List<int> sums = List.filled(k, 0);
    int n = sorted.length;
    int best = 1 << 60;

    void dfs(int idx, int zeroCount) {
      if (idx == n) {
        int curMax = 0;
        for (int v in sums) {
          if (v > curMax) curMax = v;
        }
        if (curMax < best) best = curMax;
        return;
      }

      // Not enough remaining bags to give each empty child at least one.
      if (n - idx < zeroCount) return;

      int curMax = 0;
      for (int v in sums) {
        if (v > curMax) curMax = v;
      }
      if (curMax >= best) return; // pruning

      int cookie = sorted[idx];
      for (int i = 0; i < k; i++) {
        bool wasZero = sums[i] == 0;
        // avoid symmetric states when multiple children are still empty
        if (wasZero && i > 0 && sums[i - 1] == 0) continue;

        sums[i] += cookie;
        dfs(idx + 1, wasZero ? zeroCount - 1 : zeroCount);
        sums[i] -= cookie;
      }
    }

    dfs(0, k);
    return best;
  }
}
```

## Golang

```go
func distributeCookies(cookies []int, k int) int {
    n := len(cookies)
    sums := make([]int, k)
    best := int(^uint(0) >> 1)

    var dfs func(i int, zero int)
    dfs = func(i int, zero int) {
        if i == n {
            mx := 0
            for _, v := range sums {
                if v > mx {
                    mx = v
                }
            }
            if mx < best {
                best = mx
            }
            return
        }

        remaining := n - i
        if remaining < zero {
            return
        }

        for j := 0; j < k; j++ {
            prev := sums[j]
            needZeroDec := false
            if prev == 0 {
                zero--
                needZeroDec = true
            }
            sums[j] += cookies[i]

            mx := 0
            for _, v := range sums {
                if v > mx {
                    mx = v
                }
            }
            if mx < best {
                dfs(i+1, zero)
            }

            sums[j] = prev
            if needZeroDec {
                zero++
            }
        }
    }

    dfs(0, k)
    return best
}
```

## Ruby

```ruby
def distribute_cookies(cookies, k)
  cookies.sort!.reverse!
  n = cookies.length
  sums = Array.new(k, 0)

  dfs = nil
  dfs = lambda do |i, zero|
    return Float::INFINITY if n - i < zero
    return sums.max if i == n

    ans = Float::INFINITY
    cookie = cookies[i]

    k.times do |j|
      was_zero = sums[j] == 0
      sums[j] += cookie
      new_zero = zero - (was_zero ? 1 : 0)

      cur_max = sums.max
      if cur_max < ans
        val = dfs.call(i + 1, new_zero)
        ans = [ans, val].min
      end

      sums[j] -= cookie
      break if was_zero
    end

    ans
  end

  dfs.call(0, k)
end
```

## Scala

```scala
object Solution {
  def distributeCookies(cookies: Array[Int], k: Int): Int = {
    val n = cookies.length
    // Sort descending to improve pruning
    val sorted = cookies.sorted(Ordering[Int].reverse)
    val loads = new Array[Int](k)
    var best = Int.MaxValue

    def dfs(idx: Int, zeroCount: Int): Unit = {
      if (idx == n) {
        val curMax = loads.max
        if (curMax < best) best = curMax
        return
      }
      // Not enough remaining bags to give each empty child at least one bag
      if (n - idx < zeroCount) return
      // Prune if current max already not better than best
      if (loads.max >= best) return

      for (j <- 0 until k) {
        val wasZero = loads(j) == 0
        loads(j) += sorted(idx)
        dfs(idx + 1, if (wasZero) zeroCount - 1 else zeroCount)
        loads(j) -= sorted(idx)
      }
    }

    dfs(0, k)
    best
  }
}
```

## Rust

```rust
impl Solution {
    pub fn distribute_cookies(cookies: Vec<i32>, k: i32) -> i32 {
        fn dfs(
            idx: usize,
            zero_cnt: i32,
            cookies: &Vec<i32>,
            k: usize,
            sums: &mut Vec<i32>,
            best: &mut i32,
        ) {
            let n = cookies.len();
            if idx == n {
                let cur_max = *sums.iter().max().unwrap();
                if cur_max < *best {
                    *best = cur_max;
                }
                return;
            }

            // not enough remaining bags to give each empty child at least one bag
            if (n - idx) < zero_cnt as usize {
                return;
            }

            for child in 0..k {
                let before = sums[child];
                let mut new_zero = zero_cnt;
                if before == 0 {
                    new_zero -= 1;
                }
                sums[child] += cookies[idx];

                // prune if current max already not better than best
                let cur_max = *sums.iter().max().unwrap();
                if cur_max < *best {
                    dfs(idx + 1, new_zero, cookies, k, sums, best);
                }

                sums[child] = before; // backtrack
            }
        }

        let mut sums = vec![0; k as usize];
        let mut best = i32::MAX;
        dfs(0, k, &cookies, k as usize, &mut sums, &mut best);
        best
    }
}
```

## Racket

```racket
(define/contract (distribute-cookies cookies k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted (sort > cookies)]
         [n (length sorted)]
         [sums (make-vector k 0)]
         [INF (expt 2 60)])
    (define best (box INF))
    (define (current-max)
      (apply max (vector->list sums)))
    (letrec ([dfs
              (lambda (i zero-count)
                (cond
                  [(= i n)
                   (let ([mx (current-max)])
                     (when (< mx (unbox best))
                       (set-box! best mx))
                     mx)]
                  [(< (- n i) zero-count) INF]
                  [else
                   (let loop ((j 0) (ans INF))
                     (if (= j k)
                         ans
                         (let* ([prev (vector-ref sums j)]
                                [new (+ prev (list-ref sorted i))]
                                [_ (vector-set! sums j new)]
                                [new-zero-count (if (= prev 0) (- zero-count 1) zero-count)])
                           (define sub
                             (if (< (current-max) (unbox best))
                                 (dfs (+ i 1) new-zero-count)
                                 INF))
                           (when (< sub ans)
                             (set! ans sub))
                           (vector-set! sums j prev)
                           (loop (+ j 1) ans))))]))])
      (dfs 0 k))
    (unbox best)))
```

## Erlang

```erlang
-module(solution).
-export([distribute_cookies/2]).

-spec distribute_cookies(Cookies :: [integer()], K :: integer()) -> integer().
distribute_cookies(Cookies, K) ->
    Sorted = lists:sort(fun(A, B) -> A > B end, Cookies), % descending order for better pruning
    N = length(Sorted),
    Sums0 = erlang:make_tuple(K, 0),
    MaxInt = (1 bsl 60),
    dfs(0, Sorted, N, K, Sums0, K, MaxInt).

%% dfs(Index, CookiesSorted, N, K, SumsTuple, ZeroCount, Best) -> MinUnfairness
dfs(Index, _Cookies, N, _K, _Sums, _Zero, Best) when Index == N ->
    % all cookies assigned, compute max load
    MaxLoad = max_in_tuple(_Sums, _K),
    if MaxLoad < Best -> MaxLoad; true -> Best end;
dfs(Index, Cookies, N, K, Sums, ZeroCount, Best) ->
    Remaining = N - Index,
    %% prune if not enough cookies to give each empty child at least one bag
    case Remaining < ZeroCount of
        true -> Best;
        false ->
            Cookie = lists:nth(Index + 1, Cookies),
            dfs_children(1, K, Cookie, Index, Cookies, N, Sums, ZeroCount, Best)
    end.

%% iterate over children to assign current cookie
dfs_children(ChildIdx, K, _Cookie, _Index, _Cookies, _N, _Sums, _Zero, Best) when ChildIdx > K ->
    Best;
dfs_children(ChildIdx, K, Cookie, Index, Cookies, N, Sums, ZeroCount, Best) ->
    OldVal = element(ChildIdx, Sums),
    NewZero = case OldVal of
                  0 -> ZeroCount - 1;
                  _ -> ZeroCount
              end,
    NewSum = OldVal + Cookie,
    NewSums = setelement(ChildIdx, Sums, NewSum),

    CurMax = max_in_tuple(NewSums, K),
    RecBest =
        if CurMax >= Best ->
                Best; % prune this branch
           true ->
                dfs(Index + 1, Cookies, N, K, NewSums, NewZero, Best)
        end,

    NextBest = dfs_children(ChildIdx + 1, K, Cookie, Index, Cookies, N, Sums, ZeroCount,
                            case RecBest < Best of
                                true -> RecBest;
                                false -> Best
                            end),
    if NextBest < RecBest -> NextBest; true -> RecBest end.

%% compute maximum value in a tuple of size K
max_in_tuple(Tuple, K) ->
    max_in_tuple(1, K, Tuple, 0).

max_in_tuple(I, K, Tuple, Acc) when I =< K ->
    Val = element(I, Tuple),
    NewAcc = if Val > Acc -> Val; true -> Acc end,
    max_in_tuple(I + 1, K, Tuple, NewAcc);
max_in_tuple(_, _, _, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec distribute_cookies(cookies :: [integer], k :: integer) :: integer
  def distribute_cookies(cookies, k) do
    sorted = Enum.sort(cookies, &>=/2)
    n = length(sorted)
    total = Enum.sum(cookies)
    init_dist = List.duplicate(0, k)

    dfs(0, k, init_dist, 0, total, sorted, n, k)
  end

  defp dfs(i, _zero_cnt, _dist, cur_max, best, _sorted, n, _k) when i == n do
    min(cur_max, best)
  end

  defp dfs(i, zero_cnt, dist, cur_max, best, sorted, n, k) do
    cond do
      n - i < zero_cnt ->
        best

      cur_max >= best ->
        best

      true ->
        cookie = Enum.at(sorted, i)

        Enum.reduce(0..k-1, best, fn child_idx, acc_best ->
          child_sum = Enum.at(dist, child_idx)
          new_zero = if child_sum == 0, do: zero_cnt - 1, else: zero_cnt
          updated_child_sum = child_sum + cookie
          new_dist = List.replace_at(dist, child_idx, updated_child_sum)
          new_cur_max = max(cur_max, updated_child_sum)

          dfs(i + 1, new_zero, new_dist, new_cur_max, acc_best, sorted, n, k)
        end)
    end
  end
end
```
