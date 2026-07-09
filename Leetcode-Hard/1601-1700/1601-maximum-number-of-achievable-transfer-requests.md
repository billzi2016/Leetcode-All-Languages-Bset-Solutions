# 1601. Maximum Number of Achievable Transfer Requests

## Cpp

```cpp
class Solution {
public:
    int maximumRequests(int n, vector<vector<int>>& requests) {
        int m = requests.size();
        vector<int> balance(n, 0);
        int best = 0;
        function<void(int,int)> dfs = [&](int idx, int cnt) {
            if (idx == m) {
                for (int v : balance) if (v != 0) return;
                best = max(best, cnt);
                return;
            }
            // Prune if even taking all remaining cannot beat current best
            if (cnt + (m - idx) <= best) return;

            int from = requests[idx][0];
            int to   = requests[idx][1];

            // take this request
            balance[from]--;
            balance[to]++;
            dfs(idx + 1, cnt + 1);
            balance[from]++;
            balance[to]--;

            // skip this request
            dfs(idx + 1, cnt);
        };
        dfs(0, 0);
        return best;
    }
};
```

## Java

```java
class Solution {
    private int[] balance;
    private int[][] reqs;
    private int nBuildings;
    private int totalReq;
    private int best;

    public int maximumRequests(int n, int[][] requests) {
        this.nBuildings = n;
        this.reqs = requests;
        this.totalReq = requests.length;
        this.balance = new int[n];
        this.best = 0;
        dfs(0, 0);
        return best;
    }

    private void dfs(int idx, int count) {
        // Prune if even taking all remaining cannot beat current best
        if (count + (totalReq - idx) <= best) {
            return;
        }
        if (idx == totalReq) {
            for (int b : balance) {
                if (b != 0) {
                    return;
                }
            }
            best = Math.max(best, count);
            return;
        }

        int from = reqs[idx][0];
        int to = reqs[idx][1];

        // Take this request
        balance[from]--;
        balance[to]++;
        dfs(idx + 1, count + 1);
        balance[from]++;
        balance[to]--;

        // Skip this request
        dfs(idx + 1, count);
    }
}
```

## Python

```python
class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        m = len(requests)
        indegree = [0] * n
        self.ans = 0

        def dfs(i, taken):
            # prune if even taking all remaining cannot beat current answer
            if taken + (m - i) <= self.ans:
                return
            if i == m:
                if all(x == 0 for x in indegree):
                    self.ans = max(self.ans, taken)
                return

            frm, to = requests[i]
            # take this request
            indegree[frm] -= 1
            indegree[to] += 1
            dfs(i + 1, taken + 1)
            # backtrack
            indegree[frm] += 1
            indegree[to] -= 1

            # skip this request
            dfs(i + 1, taken)

        dfs(0, 0)
        return self.ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        indeg = [0] * n
        ans = 0

        def dfs(idx: int, cnt: int) -> None:
            nonlocal ans
            # prune if even taking all remaining cannot beat current answer
            if cnt + (m - idx) <= ans:
                return
            if idx == m:
                if all(v == 0 for v in indeg):
                    ans = max(ans, cnt)
                return

            a, b = requests[idx]
            # take this request
            indeg[a] -= 1
            indeg[b] += 1
            dfs(idx + 1, cnt + 1)
            indeg[a] += 1
            indeg[b] -= 1

            # skip this request
            dfs(idx + 1, cnt)

        dfs(0, 0)
        return ans
```

## C

```c
#include <stddef.h>

static void backtrack(int idx, int cnt, int n, int **req, int m,
                      int *indeg, int *ans) {
    if (cnt + (m - idx) <= *ans) return;          // prune
    if (idx == m) {
        for (int i = 0; i < n; ++i)
            if (indeg[i] != 0) return;
        if (cnt > *ans) *ans = cnt;
        return;
    }
    int from = req[idx][0];
    int to   = req[idx][1];

    /* take this request */
    indeg[from]--;
    indeg[to]++;
    backtrack(idx + 1, cnt + 1, n, req, m, indeg, ans);
    indeg[from]++;   // revert
    indeg[to]--;

    /* skip this request */
    backtrack(idx + 1, cnt, n, req, m, indeg, ans);
}

int maximumRequests(int n, int** requests, int requestsSize,
                    int* requestsColSize) {
    (void)requestsColSize; // unused
    int indeg[20] = {0};
    int ans = 0;
    backtrack(0, 0, n, requests, requestsSize, indeg, &ans);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumRequests(int n, int[][] requests)
    {
        int m = requests.Length;
        int[] balance = new int[n];
        int best = 0;

        void Dfs(int idx, int taken)
        {
            if (idx == m)
            {
                for (int i = 0; i < n; i++)
                    if (balance[i] != 0) return;
                if (taken > best) best = taken;
                return;
            }

            // Prune if even taking all remaining cannot beat current best
            if (taken + (m - idx) <= best) return;

            int from = requests[idx][0];
            int to = requests[idx][1];

            // Take this request
            balance[from]--;
            balance[to]++;
            Dfs(idx + 1, taken + 1);
            // Backtrack
            balance[from]++;
            balance[to]--;

            // Skip this request
            Dfs(idx + 1, taken);
        }

        Dfs(0, 0);
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} requests
 * @return {number}
 */
var maximumRequests = function(n, requests) {
    const m = requests.length;
    const indeg = new Array(n).fill(0);
    let best = 0;

    const dfs = (idx, cnt) => {
        if (idx === m) {
            for (let i = 0; i < n; ++i) {
                if (indeg[i] !== 0) return;
            }
            if (cnt > best) best = cnt;
            return;
        }

        // Prune if even taking all remaining requests cannot beat current best
        if (cnt + (m - idx) <= best) {
            // Still need to explore the branch that skips current request,
            // because it might lead to a valid zero-indegree configuration with same count.
            // However, since cnt won't increase, it can't improve best, so we can skip both branches.
            return;
        }

        const [from, to] = requests[idx];

        // Take this request
        indeg[from]--;
        indeg[to]++;
        dfs(idx + 1, cnt + 1);
        indeg[from]++;
        indeg[to]--;

        // Skip this request
        dfs(idx + 1, cnt);
    };

    dfs(0, 0);
    return best;
};
```

## Typescript

```typescript
function maximumRequests(n: number, requests: number[][]): number {
    const indeg = new Array<number>(n).fill(0);
    let best = 0;
    const m = requests.length;

    function dfs(idx: number, cnt: number): void {
        // prune if even taking all remaining cannot beat current best
        if (cnt + (m - idx) <= best) return;

        if (idx === m) {
            for (let i = 0; i < n; ++i) {
                if (indeg[i] !== 0) return;
            }
            best = cnt;
            return;
        }

        const [from, to] = requests[idx];

        // take this request
        indeg[from]--;
        indeg[to]++;
        dfs(idx + 1, cnt + 1);
        indeg[from]++;
        indeg[to]--;

        // skip this request
        dfs(idx + 1, cnt);
    }

    dfs(0, 0);
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $requests
     * @return Integer
     */
    function maximumRequests($n, $requests) {
        $len = count($requests);
        $indeg = array_fill(0, $n, 0);
        $max = 0;

        $dfs = function ($idx, $cnt) use (&$dfs, &$requests, &$indeg, $n, &$max) {
            if ($idx == count($requests)) {
                foreach ($indeg as $v) {
                    if ($v !== 0) {
                        return;
                    }
                }
                if ($cnt > $max) {
                    $max = $cnt;
                }
                return;
            }

            // take current request
            $from = $requests[$idx][0];
            $to   = $requests[$idx][1];
            $indeg[$from]--;
            $indeg[$to]++;
            $dfs($idx + 1, $cnt + 1);
            // backtrack
            $indeg[$from]++;
            $indeg[$to]--;

            // skip current request
            $dfs($idx + 1, $cnt);
        };

        $dfs(0, 0);
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximumRequests(_ n: Int, _ requests: [[Int]]) -> Int {
        let m = requests.count
        var indegree = Array(repeating: 0, count: n)
        var ans = 0

        func dfs(_ idx: Int, _ cnt: Int) {
            if idx == m {
                for v in indegree where v != 0 { return }
                ans = max(ans, cnt)
                return
            }

            // Prune if even taking all remaining cannot improve answer
            if cnt + (m - idx) <= ans { return }

            // Take current request
            let from = requests[idx][0]
            let to = requests[idx][1]
            indegree[from] -= 1
            indegree[to] += 1
            dfs(idx + 1, cnt + 1)
            indegree[from] += 1
            indegree[to] -= 1

            // Skip current request
            dfs(idx + 1, cnt)
        }

        dfs(0, 0)
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumRequests(n: Int, requests: Array<IntArray>): Int {
        val balance = IntArray(n)
        var best = 0

        fun dfs(idx: Int, count: Int) {
            if (idx == requests.size) {
                for (b in balance) {
                    if (b != 0) return
                }
                if (count > best) best = count
                return
            }

            // take this request
            val from = requests[idx][0]
            val to = requests[idx][1]
            balance[from]--
            balance[to]++
            dfs(idx + 1, count + 1)
            balance[from]++
            balance[to]--

            // skip this request
            dfs(idx + 1, count)
        }

        dfs(0, 0)
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maximumRequests(int n, List<List<int>> requests) {
    List<int> indegree = List.filled(n, 0);
    int ans = 0;

    void dfs(int idx, int cnt) {
      if (idx == requests.length) {
        for (int v in indegree) {
          if (v != 0) return;
        }
        if (cnt > ans) ans = cnt;
        return;
      }

      // Take the current request
      int from = requests[idx][0];
      int to = requests[idx][1];
      indegree[from]--;
      indegree[to]++;
      dfs(idx + 1, cnt + 1);
      indegree[from]++;
      indegree[to]--;

      // Skip the current request
      dfs(idx + 1, cnt);
    }

    dfs(0, 0);
    return ans;
  }
}
```

## Golang

```go
func maximumRequests(n int, requests [][]int) int {
	indeg := make([]int, n)
	ans := 0
	var dfs func(idx, cnt int)
	dfs = func(idx, cnt int) {
		if idx == len(requests) {
			for _, v := range indeg {
				if v != 0 {
					return
				}
			}
			if cnt > ans {
				ans = cnt
			}
			return
		}
		// prune if even taking all remaining cannot beat current answer
		if cnt+len(requests)-idx <= ans {
			return
		}
		from, to := requests[idx][0], requests[idx][1]
		indeg[from]--
		indeg[to]++
		dfs(idx+1, cnt+1)
		indeg[from]++
		indeg[to]--

		dfs(idx+1, cnt)
	}
	dfs(0, 0)
	return ans
}
```

## Ruby

```ruby
def maximum_requests(n, requests)
  max_ans = 0
  indegree = Array.new(n, 0)

  dfs = nil
  dfs = lambda do |idx, count|
    if idx == requests.length
      if indegree.all?(&:zero?)
        max_ans = [max_ans, count].max
      end
      next
    end

    from, to = requests[idx]

    # take the request
    indegree[from] -= 1
    indegree[to] += 1
    dfs.call(idx + 1, count + 1)
    indegree[from] += 1
    indegree[to] -= 1

    # skip the request
    dfs.call(idx + 1, count)
  end

  dfs.call(0, 0)
  max_ans
end
```

## Scala

```scala
object Solution {
    def maximumRequests(n: Int, requests: Array[Array[Int]]): Int = {
        val m = requests.length
        val indeg = new Array[Int](n)
        var ans = 0

        def dfs(idx: Int, cnt: Int): Unit = {
            if (idx == m) {
                var ok = true
                var i = 0
                while (i < n && ok) {
                    if (indeg(i) != 0) ok = false
                    i += 1
                }
                if (ok && cnt > ans) ans = cnt
            } else {
                val from = requests(idx)(0)
                val to   = requests(idx)(1)

                indeg(from) -= 1
                indeg(to)   += 1
                dfs(idx + 1, cnt + 1)
                indeg(from) += 1
                indeg(to)   -= 1

                dfs(idx + 1, cnt)
            }
        }

        dfs(0, 0)
        ans
    }
}
```

## Rust

```rust
use std::cmp::max;

fn dfs(idx: usize, cnt: i32, requests: &Vec<Vec<i32>>, indegree: &mut Vec<i32>, ans: &mut i32) {
    if idx == requests.len() {
        if indegree.iter().all(|&x| x == 0) {
            *ans = max(*ans, cnt);
        }
        return;
    }

    // Take the current request
    let from = requests[idx][0] as usize;
    let to = requests[idx][1] as usize;
    indegree[from] -= 1;
    indegree[to] += 1;
    dfs(idx + 1, cnt + 1, requests, indegree, ans);
    // Backtrack
    indegree[from] += 1;
    indegree[to] -= 1;

    // Skip the current request (prune if impossible to beat current answer)
    let remaining = (requests.len() - idx - 1) as i32;
    if cnt + remaining > *ans {
        dfs(idx + 1, cnt, requests, indegree, ans);
    }
}

impl Solution {
    pub fn maximum_requests(n: i32, requests: Vec<Vec<i32>>) -> i32 {
        let mut indegree = vec![0i32; n as usize];
        let mut ans = 0;
        dfs(0, 0, &requests, &mut indegree, &mut ans);
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-requests n requests)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length requests))
         (indeg (make-vector n 0))
         (ans (box 0)))
    (define (all-zero?)
      (let loop ((i 0))
        (if (= i n) #t
            (and (= (vector-ref indeg i) 0)
                 (loop (+ i 1))))))
    (letrec ((dfs (lambda (idx cnt)
                    (if (= idx m)
                        (when (all-zero?)
                          (when (> cnt (unbox ans))
                            (set-box! ans cnt)))
                        (begin
                          (define req (list-ref requests idx))
                          (define from (first req))
                          (define to   (second req))
                          ;; take request
                          (vector-set! indeg from (- (vector-ref indeg from) 1))
                          (vector-set! indeg to (+ (vector-ref indeg to) 1))
                          (dfs (+ idx 1) (+ cnt 1))
                          ;; backtrack
                          (vector-set! indeg from (+ (vector-ref indeg from) 1))
                          (vector-set! indeg to (- (vector-ref indeg to) 1))
                          ;; skip request
                          (dfs (+ idx 1) cnt))))))
      (dfs 0 0))
    (unbox ans)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_requests/2]).

-spec maximum_requests(N :: integer(), Requests :: [[integer()]]) -> integer().
maximum_requests(N, Requests) ->
    M = length(Requests),
    MaxMask = 1 bsl M,
    loop(0, MaxMask, N, Requests, 0).

loop(Mask, MaxMask, _N, _Requests, Best) when Mask >= MaxMask ->
    Best;
loop(Mask, MaxMask, N, Requests, Best) ->
    BitCount = popcount(Mask),
    NewBest =
        if
            BitCount > Best,
            check_mask(N, Requests, Mask) ->
                BitCount;
            true ->
                Best
        end,
    loop(Mask + 1, MaxMask, N, Requests, NewBest).

popcount(0) -> 0;
popcount(X) ->
    (X band 1) + popcount(X bsr 1).

check_mask(N, Requests, Mask) ->
    Tuple = erlang:make_tuple(N, 0),
    UpdatedTuple = apply_requests(Tuple, Requests, Mask, 0),
    all_zero(UpdatedTuple, N).

apply_requests(Tuple, [], _Mask, _Idx) -> Tuple;
apply_requests(Tuple, [_|Rest], Mask, Idx) when (Mask band (1 bsl Idx)) =:= 0 ->
    apply_requests(Tuple, Rest, Mask, Idx + 1);
apply_requests(Tuple, [[From, To] | Rest], Mask, Idx) ->
    Tuple1 = update(Tuple, From, -1),
    Tuple2 = update(Tuple1, To, 1),
    apply_requests(Tuple2, Rest, Mask, Idx + 1).

update(Tuple, Index, Delta) ->
    Pos = Index + 1,
    Old = element(Pos, Tuple),
    setelement(Pos, Tuple, Old + Delta).

all_zero(_Tuple, 0) -> true;
all_zero(Tuple, Pos) ->
    case element(Pos, Tuple) of
        0 -> all_zero(Tuple, Pos - 1);
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_requests(n :: integer, requests :: [[integer]]) :: integer
  def maximum_requests(n, requests) do
    m = length(requests)
    indegree0 = List.duplicate(0, n)

    dfs(0, 0, indegree0, requests, m)
  end

  defp dfs(idx, count, indeg, _requests, m) when idx == m do
    if Enum.all?(indeg, &(&1 == 0)), do: count, else: 0
  end

  defp dfs(idx, count, indeg, requests, m) do
    [from, to] = Enum.at(requests, idx)

    indeg_take =
      indeg
      |> List.update_at(from, fn v -> v - 1 end)
      |> List.update_at(to, fn v -> v + 1 end)

    take_max = dfs(idx + 1, count + 1, indeg_take, requests, m)
    skip_max = dfs(idx + 1, count, indeg, requests, m)

    if take_max > skip_max, do: take_max, else: skip_max
  end
end
```
