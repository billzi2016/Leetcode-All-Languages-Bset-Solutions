# 1340. Jump Game V

## Cpp

```cpp
class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> memo(n, 0);
        function<int(int)> dfs = [&](int i) -> int {
            if (memo[i]) return memo[i];
            int best = 1; // at least the current index
            // jump left
            for (int step = 1; step <= d && i - step >= 0; ++step) {
                if (arr[i] > arr[i - step]) {
                    best = max(best, 1 + dfs(i - step));
                } else {
                    break; // cannot jump over equal or higher
                }
            }
            // jump right
            for (int step = 1; step <= d && i + step < n; ++step) {
                if (arr[i] > arr[i + step]) {
                    best = max(best, 1 + dfs(i + step));
                } else {
                    break;
                }
            }
            memo[i] = best;
            return best;
        };
        
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, dfs(i));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int[] memo;
    private int[] arr;
    private int n;
    private int d;

    public int maxJumps(int[] arr, int d) {
        this.arr = arr;
        this.d = d;
        this.n = arr.length;
        memo = new int[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, dfs(i));
        }
        return ans;
    }

    private int dfs(int i) {
        if (memo[i] != 0) return memo[i];
        int best = 1;

        // jump to the left
        for (int step = 1; step <= d && i - step >= 0; step++) {
            if (arr[i] > arr[i - step]) {
                best = Math.max(best, 1 + dfs(i - step));
            } else {
                break;
            }
        }

        // jump to the right
        for (int step = 1; step <= d && i + step < n; step++) {
            if (arr[i] > arr[i + step]) {
                best = Math.max(best, 1 + dfs(i + step));
            } else {
                break;
            }
        }

        memo[i] = best;
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        memo = [0] * n

        import sys
        sys.setrecursionlimit(10000)

        def dfs(i):
            if memo[i]:
                return memo[i]
            best = 1
            # left direction
            for step in range(1, d + 1):
                j = i - step
                if j < 0 or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            # right direction
            for step in range(1, d + 1):
                j = i + step
                if j >= n or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            memo[i] = best
            return best

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def dfs(i: int) -> int:
            if dp[i] != -1:
                return dp[i]
            best = 1
            # left direction
            for step in range(1, d + 1):
                j = i - step
                if j < 0 or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            # right direction
            for step in range(1, d + 1):
                j = i + step
                if j >= n or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            dp[i] = best
            return best

        return max(dfs(i) for i in range(n))
```

## C

```c
#include <stdlib.h>

static int dfs(int i, int *arr, int n, int d, int *dp) {
    if (dp[i] != 0) return dp[i];
    int best = 1;
    for (int step = 1; step <= d && i - step >= 0; ++step) {
        if (arr[i - step] >= arr[i]) break;
        int cand = 1 + dfs(i - step, arr, n, d, dp);
        if (cand > best) best = cand;
    }
    for (int step = 1; step <= d && i + step < n; ++step) {
        if (arr[i + step] >= arr[i]) break;
        int cand = 1 + dfs(i + step, arr, n, d, dp);
        if (cand > best) best = cand;
    }
    dp[i] = best;
    return best;
}

int maxJumps(int* arr, int arrSize, int d) {
    int *dp = (int *)calloc(arrSize, sizeof(int));
    int ans = 0;
    for (int i = 0; i < arrSize; ++i) {
        int cur = dfs(i, arr, arrSize, d, dp);
        if (cur > ans) ans = cur;
    }
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private int[] _arr;
    private int _d;
    private int _n;
    private int[] _memo;

    public int MaxJumps(int[] arr, int d)
    {
        _arr = arr;
        _d = d;
        _n = arr.Length;
        _memo = new int[_n];
        int result = 0;
        for (int i = 0; i < _n; i++)
        {
            result = Math.Max(result, Dfs(i));
        }
        return result;
    }

    private int Dfs(int index)
    {
        if (_memo[index] != 0) return _memo[index];
        int best = 1;

        // jump to the left
        for (int step = 1; step <= _d; step++)
        {
            int j = index - step;
            if (j < 0) break;
            if (_arr[j] >= _arr[index]) break;
            best = Math.Max(best, 1 + Dfs(j));
        }

        // jump to the right
        for (int step = 1; step <= _d; step++)
        {
            int j = index + step;
            if (j >= _n) break;
            if (_arr[j] >= _arr[index]) break;
            best = Math.Max(best, 1 + Dfs(j));
        }

        _memo[index] = best;
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} d
 * @return {number}
 */
var maxJumps = function(arr, d) {
    const n = arr.length;
    const memo = new Array(n).fill(0);
    
    const dfs = (i) => {
        if (memo[i] !== 0) return memo[i];
        let best = 1; // count the current index
        
        // jump to the left
        for (let step = 1; step <= d && i - step >= 0; ++step) {
            const j = i - step;
            if (arr[j] < arr[i]) {
                best = Math.max(best, 1 + dfs(j));
            } else {
                break; // cannot jump over a higher or equal element
            }
        }
        
        // jump to the right
        for (let step = 1; step <= d && i + step < n; ++step) {
            const j = i + step;
            if (arr[j] < arr[i]) {
                best = Math.max(best, 1 + dfs(j));
            } else {
                break;
            }
        }
        
        memo[i] = best;
        return best;
    };
    
    let answer = 0;
    for (let i = 0; i < n; ++i) {
        answer = Math.max(answer, dfs(i));
    }
    return answer;
};
```

## Typescript

```typescript
function maxJumps(arr: number[], d: number): number {
    const n = arr.length;
    const memo = new Array<number>(n).fill(0);
    const dfs = (i: number): number => {
        if (memo[i] !== 0) return memo[i];
        let best = 1;
        // left direction
        for (let step = 1; step <= d && i - step >= 0; ++step) {
            const j = i - step;
            if (arr[j] < arr[i]) {
                best = Math.max(best, 1 + dfs(j));
            } else {
                break;
            }
        }
        // right direction
        for (let step = 1; step <= d && i + step < n; ++step) {
            const j = i + step;
            if (arr[j] < arr[i]) {
                best = Math.max(best, 1 + dfs(j));
            } else {
                break;
            }
        }
        memo[i] = best;
        return best;
    };
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        ans = Math.max(ans, dfs(i));
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $d
     * @return Integer
     */
    function maxJumps($arr, $d) {
        $n = count($arr);
        $memo = array_fill(0, $n, 0);

        $dfs = function($i) use (&$dfs, &$arr, $d, $n, &$memo) {
            if ($memo[$i] !== 0) {
                return $memo[$i];
            }
            $maxLen = 1;

            // jump to the left
            for ($step = 1; $step <= $d && $i - $step >= 0; $step++) {
                $j = $i - $step;
                if ($arr[$j] < $arr[$i]) {
                    $len = 1 + $dfs($j);
                    if ($len > $maxLen) {
                        $maxLen = $len;
                    }
                } else {
                    break;
                }
            }

            // jump to the right
            for ($step = 1; $step <= $d && $i + $step < $n; $step++) {
                $j = $i + $step;
                if ($arr[$j] < $arr[$i]) {
                    $len = 1 + $dfs($j);
                    if ($len > $maxLen) {
                        $maxLen = $len;
                    }
                } else {
                    break;
                }
            }

            $memo[$i] = $maxLen;
            return $maxLen;
        };

        $answer = 0;
        for ($i = 0; $i < $n; $i++) {
            $val = $dfs($i);
            if ($val > $answer) {
                $answer = $val;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func maxJumps(_ arr: [Int], _ d: Int) -> Int {
        let n = arr.count
        var memo = Array(repeating: 0, count: n)
        
        func dfs(_ i: Int) -> Int {
            if memo[i] != 0 { return memo[i] }
            var best = 1
            
            // explore left side
            var step = 1
            while step <= d && i - step >= 0 {
                let j = i - step
                if arr[j] >= arr[i] { break }
                let cand = 1 + dfs(j)
                if cand > best { best = cand }
                step += 1
            }
            
            // explore right side
            step = 1
            while step <= d && i + step < n {
                let j = i + step
                if arr[j] >= arr[i] { break }
                let cand = 1 + dfs(j)
                if cand > best { best = cand }
                step += 1
            }
            
            memo[i] = best
            return best
        }
        
        var answer = 0
        for i in 0..<n {
            let val = dfs(i)
            if val > answer { answer = val }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxJumps(arr: IntArray, d: Int): Int {
        val n = arr.size
        val memo = IntArray(n)
        fun dfs(i: Int): Int {
            if (memo[i] != 0) return memo[i]
            var best = 1
            // left direction
            var step = 1
            while (step <= d) {
                val j = i - step
                if (j < 0) break
                if (arr[j] >= arr[i]) break
                best = maxOf(best, 1 + dfs(j))
                step++
            }
            // right direction
            step = 1
            while (step <= d) {
                val j = i + step
                if (j >= n) break
                if (arr[j] >= arr[i]) break
                best = maxOf(best, 1 + dfs(j))
                step++
            }
            memo[i] = best
            return best
        }

        var answer = 0
        for (i in 0 until n) {
            answer = maxOf(answer, dfs(i))
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxJumps(List<int> arr, int d) {
    final n = arr.length;
    List<int> memo = List.filled(n, 0);

    int dfs(int i) {
      if (memo[i] != 0) return memo[i];
      int best = 1;

      for (int step = 1; step <= d && i - step >= 0; ++step) {
        if (arr[i - step] < arr[i]) {
          best = max(best, 1 + dfs(i - step));
        } else {
          break;
        }
      }

      for (int step = 1; step <= d && i + step < n; ++step) {
        if (arr[i + step] < arr[i]) {
          best = max(best, 1 + dfs(i + step));
        } else {
          break;
        }
      }

      memo[i] = best;
      return best;
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      ans = max(ans, dfs(i));
    }
    return ans;
  }
}
```

## Golang

```go
func maxJumps(arr []int, d int) int {
	n := len(arr)
	memo := make([]int, n)
	for i := range memo {
		memo[i] = -1
	}
	var dfs func(int) int
	dfs = func(i int) int {
		if memo[i] != -1 {
			return memo[i]
		}
		best := 1
		// left direction
		for step := 1; step <= d && i-step >= 0; step++ {
			if arr[i-step] < arr[i] {
				val := 1 + dfs(i-step)
				if val > best {
					best = val
				}
			} else {
				break
			}
		}
		// right direction
		for step := 1; step <= d && i+step < n; step++ {
			if arr[i+step] < arr[i] {
				val := 1 + dfs(i+step)
				if val > best {
					best = val
				}
			} else {
				break
			}
		}
		memo[i] = best
		return best
	}

	ans := 0
	for i := 0; i < n; i++ {
		if v := dfs(i); v > ans {
			ans = v
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_jumps(arr, d)
  n = arr.length
  dp = Array.new(n, 0)

  dfs = nil
  dfs = ->(i) do
    return dp[i] if dp[i] != 0
    best = 1

    (i - 1).downto([i - d, 0].max) do |j|
      break if arr[j] >= arr[i]
      cand = 1 + dfs.call(j)
      best = cand if cand > best
    end

    (i + 1).upto([i + d, n - 1].min) do |j|
      break if arr[j] >= arr[i]
      cand = 1 + dfs.call(j)
      best = cand if cand > best
    end

    dp[i] = best
    best
  end

  max_len = 0
  (0...n).each do |i|
    len = dfs.call(i)
    max_len = len if len > max_len
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def maxJumps(arr: Array[Int], d: Int): Int = {
        val n = arr.length
        val memo = new Array[Int](n)

        def dfs(i: Int): Int = {
            if (memo(i) != 0) return memo(i)
            var best = 1

            // jump to the left
            var step = 1
            while (step <= d && i - step >= 0 && arr(i) > arr(i - step)) {
                val j = i - step
                best = math.max(best, 1 + dfs(j))
                step += 1
            }

            // jump to the right
            step = 1
            while (step <= d && i + step < n && arr(i) > arr(i + step)) {
                val j = i + step
                best = math.max(best, 1 + dfs(j))
                step += 1
            }

            memo(i) = best
            best
        }

        var ans = 0
        for (i <- 0 until n) {
            ans = math.max(ans, dfs(i))
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_jumps(arr: Vec<i32>, d: i32) -> i32 {
        let n = arr.len();
        let d_usize = d as usize;
        let mut memo = vec![0i32; n];

        fn dfs(i: usize, arr: &Vec<i32>, d: usize, memo: &mut Vec<i32>) -> i32 {
            if memo[i] != 0 {
                return memo[i];
            }
            let n = arr.len();
            let mut best = 1;

            // jump to the left
            for step in 1..=d {
                if i < step {
                    break;
                }
                let j = i - step;
                if arr[j] >= arr[i] {
                    break;
                }
                let cand = 1 + dfs(j, arr, d, memo);
                if cand > best {
                    best = cand;
                }
            }

            // jump to the right
            for step in 1..=d {
                let j = i + step;
                if j >= n {
                    break;
                }
                if arr[j] >= arr[i] {
                    break;
                }
                let cand = 1 + dfs(j, arr, d, memo);
                if cand > best {
                    best = cand;
                }
            }

            memo[i] = best;
            best
        }

        let mut ans = 0;
        for i in 0..n {
            let cur = dfs(i, &arr, d_usize, &mut memo);
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-jumps arr d)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector arr)]
         [n (vector-length v)]
         [dp (make-vector n 0)])
    (define (dfs i)
      (let ([cached (vector-ref dp i)])
        (if (> cached 0)
            cached
            (let ([cur (vector-ref v i)])
              ;; explore left side
              (let loop-left ((step 1) (best 1))
                (if (> step d)
                    (let loop-right ((step 1) (best best))
                      (if (> step d)
                          (begin (vector-set! dp i best) best)
                          (let ([r (+ i step)])
                            (cond [(>= r n) (loop-right (+ step 1) best)]
                                  [(>= (vector-ref v r) cur) (begin (vector-set! dp i best) best)]
                                  [else
                                   (define cand (+ 1 (dfs r)))
                                   (loop-right (+ step 1) (max best cand))]))))
                    (let ([l (- i step)])
                      (cond [(< l 0) (let loop-right ((step 1) (best best))
                                        (if (> step d)
                                            (begin (vector-set! dp i best) best)
                                            (let ([r (+ i step)])
                                              (cond [(>= r n) (loop-right (+ step 1) best)]
                                                    [(>= (vector-ref v r) cur) (begin (vector-set! dp i best) best)]
                                                    [else
                                                     (define cand (+ 1 (dfs r)))
                                                     (loop-right (+ step 1) (max best cand))]))))]
                            [(>= (vector-ref v l) cur) (let loop-right ((step 1) (best best))
                                                         (if (> step d)
                                                             (begin (vector-set! dp i best) best)
                                                             (let ([r (+ i step)])
                                                               (cond [(>= r n) (loop-right (+ step 1) best)]
                                                                     [(>= (vector-ref v r) cur) (begin (vector-set! dp i best) best)]
                                                                     [else
                                                                      (define cand (+ 1 (dfs r)))
                                                                      (loop-right (+ step 1) (max best cand))]))))]
                            [else
                             (define cand (+ 1 (dfs l)))
                             (loop-left (+ step 1) (max best cand))])))))))
    (let loop ((i 0) (ans 0))
      (if (= i n)
          ans
          (let ([res (dfs i)])
            (loop (+ i 1) (max ans res)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_jumps/2]).

-spec max_jumps(Arr :: [integer()], D :: integer()) -> integer().
max_jumps(Arr, D) ->
    ArrTuple = list_to_tuple(Arr),
    N = tuple_size(ArrTuple),
    {Ans, _} = max_jumps_loop(1, N, ArrTuple, D, #{}),
    Ans.

%% iterate over all indices to find global maximum
max_jumps_loop(I, N, _ArrTuple, _D, Memo) when I > N ->
    {0, Memo};
max_jumps_loop(I, N, ArrTuple, D, Memo) ->
    {LenI, Memo1} = dfs(I, ArrTuple, D, Memo),
    {BestRest, Memo2} = max_jumps_loop(I + 1, N, ArrTuple, D, Memo1),
    {erlang:max(LenI, BestRest), Memo2}.

%% depth‑first search with memoization
dfs(Index, ArrTuple, D, Memo) ->
    case maps:get(Index, Memo, undefined) of
        Value when is_integer(Value) ->
            {Value, Memo};
        _ ->
            Reachable = get_reachable(Index, -1, D, ArrTuple) ++
                        get_reachable(Index, 1, D, ArrTuple),
            {BestLen, NewMemo} = dfs_list(Reachable, ArrTuple, D, Memo, 0),
            Result = BestLen + 1,
            UpdatedMemo = maps:put(Index, Result, NewMemo),
            {Result, UpdatedMemo}
    end.

%% evaluate all reachable positions and keep the maximum length
dfs_list([], _ArrTuple, _D, Memo, Max) ->
    {Max, Memo};
dfs_list([J | Rest], ArrTuple, D, Memo, Max) ->
    {LenJ, Memo1} = dfs(J, ArrTuple, D, Memo),
    NewMax = erlang:max(Max, LenJ),
    dfs_list(Rest, ArrTuple, D, Memo1, NewMax).

%% collect reachable indices in one direction
get_reachable(Index, Dir, D, ArrTuple) ->
    Val = element(Index, ArrTuple),
    get_reachable_loop(Index + Dir, 1, Dir, D, Val, ArrTuple, []).

get_reachable_loop(Pos, Step, Dir, D, Val, ArrTuple, Acc)
        when Step =< D,
             Pos >= 1,
             Pos =< tuple_size(ArrTuple) ->
    CurVal = element(Pos, ArrTuple),
    if
        CurVal < Val ->
            NewAcc = [Pos | Acc],
            get_reachable_loop(Pos + Dir, Step + 1, Dir, D, Val, ArrTuple, NewAcc);
        true ->
            lists:reverse(Acc)
    end;
get_reachable_loop(_Pos, _Step, _Dir, _D, _Val, _ArrTuple, Acc) ->
    lists:reverse(Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_jumps(arr :: [integer], d :: integer) :: integer
  def max_jumps(arr, d) do
    n = length(arr)
    arr_t = List.to_tuple(arr)

    indices = Enum.to_list(0..(n - 1))

    sorted =
      Enum.sort_by(indices, fn i -> elem(arr_t, i) end, &>=/2)

    {_dp_map, answer} =
      Enum.reduce(sorted, {%{}, 0}, fn i, {dp, best} ->
        cur_val = elem(arr_t, i)
        max_len = 0

        # explore left side
        max_len =
          Enum.reduce_while(1..d, max_len, fn step, acc ->
            j = i - step

            if j < 0 do
              {:halt, acc}
            else
              val_j = elem(arr_t, j)

              if val_j < cur_val do
                len_j = Map.get(dp, j, 1)
                {:cont, max(acc, len_j)}
              else
                {:halt, acc}
              end
            end
          end)

        # explore right side
        max_len =
          Enum.reduce_while(1..d, max_len, fn step, acc ->
            j = i + step

            if j >= n do
              {:halt, acc}
            else
              val_j = elem(arr_t, j)

              if val_j < cur_val do
                len_j = Map.get(dp, j, 1)
                {:cont, max(acc, len_j)}
              else
                {:halt, acc}
              end
            end
          end)

        dp_i = 1 + max_len
        {Map.put(dp, i, dp_i), max(best, dp_i)}
      end)

    answer
  end
end
```
