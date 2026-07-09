# 2934. Minimum Operations to Maximize Last Elements in Arrays

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        const int INF = 1e9;
        
        auto calc = [&](int a_last, int b_last) -> int {
            int ops = 0;
            for (int i = 0; i < n - 1; ++i) {
                if (nums1[i] <= a_last && nums2[i] <= b_last) {
                    continue;
                } else if (nums1[i] <= b_last && nums2[i] <= a_last) {
                    ++ops;
                } else {
                    return INF;
                }
            }
            return ops;
        };
        
        int ans = INF;
        // case 1: keep last elements as they are
        ans = min(ans, calc(nums1[n-1], nums2[n-1]));
        // case 2: swap the last pair (cost +1)
        int second = calc(nums2[n-1], nums1[n-1]);
        if (second != INF) ans = min(ans, 1 + second);
        
        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums1, int[] nums2) {
        int withoutSwap = compute(nums1, nums2, false);
        int withSwapLast = compute(nums1, nums2, true);
        if (withoutSwap == -1 && withSwapLast == -1) return -1;
        if (withoutSwap == -1) return withSwapLast;
        if (withSwapLast == -1) return withoutSwap;
        return Math.min(withoutSwap, withSwapLast);
    }

    private int compute(int[] a, int[] b, boolean swapLast) {
        int n = a.length;
        int lastA = a[n - 1];
        int lastB = b[n - 1];
        int targetA = swapLast ? lastB : lastA; // final value at nums1[n-1]
        int targetB = swapLast ? lastA : lastB; // final value at nums2[n-1]
        int ops = swapLast ? 1 : 0;

        for (int i = 0; i < n - 1; i++) {
            int ai = a[i];
            int bi = b[i];
            boolean keep = ai <= targetA && bi <= targetB;
            boolean needSwap = ai <= targetB && bi <= targetA;
            if (!keep && !needSwap) return -1; // impossible
            if (!keep && needSwap) ops++;      // must swap this index
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        INF = 10**9

        def swaps_needed(a_last, b_last):
            swaps = 0
            for i in range(n - 1):
                x, y = nums1[i], nums2[i]
                if x <= a_last and y <= b_last:
                    continue
                elif y <= a_last and x <= b_last:
                    swaps += 1
                else:
                    return INF
            return swaps

        # case 1: keep last elements as they are
        ops1 = swaps_needed(nums1[-1], nums2[-1])
        # case 2: swap the last elements (cost +1)
        ops2 = swaps_needed(nums2[-1], nums1[-1])
        if ops2 != INF:
            ops2 += 1

        ans = min(ops1, ops2)
        return -1 if ans >= INF else ans
```

## Python3

```python
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)

        def needed_ops(a: int, b: int) -> int | None:
            ops = 0
            for i in range(n - 1):
                x, y = nums1[i], nums2[i]
                if x <= a and y <= b:
                    continue
                if y <= a and x <= b:
                    ops += 1
                else:
                    return None
            return ops

        ans = None

        # case 0: keep last elements as they are
        op0 = needed_ops(nums1[-1], nums2[-1])
        if op0 is not None:
            ans = op0

        # case 1: swap the last pair (cost +1)
        op1 = needed_ops(nums2[-1], nums1[-1])
        if op1 is not None:
            total = 1 + op1
            if ans is None or total < ans:
                ans = total

        return -1 if ans is None else ans
```

## C

```c
#include <stdbool.h>
#include <limits.h>

int minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size;
    const int INF = INT_MAX / 2;
    int answer = INF;

    // Scenario 1: keep last elements as they are
    int a = nums1[n - 1];
    int b = nums2[n - 1];
    int swaps = 0;
    bool possible = true;
    for (int i = 0; i < n - 1; ++i) {
        if (nums1[i] <= a && nums2[i] <= b) {
            continue;
        } else if (nums1[i] <= b && nums2[i] <= a) {
            ++swaps;
        } else {
            possible = false;
            break;
        }
    }
    if (possible) {
        answer = swaps < answer ? swaps : answer;
    }

    // Scenario 2: swap the last elements first
    int a2 = nums2[n - 1];
    int b2 = nums1[n - 1];
    swaps = 0;
    possible = true;
    for (int i = 0; i < n - 1; ++i) {
        if (nums1[i] <= a2 && nums2[i] <= b2) {
            continue;
        } else if (nums1[i] <= b2 && nums2[i] <= a2) {
            ++swaps;
        } else {
            possible = false;
            break;
        }
    }
    if (possible) {
        int total = 1 + swaps; // include the swap of last elements
        answer = total < answer ? total : answer;
    }

    return (answer == INF) ? -1 : answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinOperations(int[] nums1, int[] nums2)
    {
        const int INF = int.MaxValue;
        int n = nums1.Length;

        int answer = INF;

        // Case 1: keep the last elements as they are
        answer = Math.Min(answer, Evaluate(nums1, nums2, false));

        // Case 2: swap the last elements (cost +1)
        answer = Math.Min(answer, Evaluate(nums1, nums2, true));

        return answer == INF ? -1 : answer;
    }

    private int Evaluate(int[] a, int[] b, bool swapLast)
    {
        int n = a.Length;
        long lastA = a[n - 1];
        long lastB = b[n - 1];
        int ops = 0;

        if (swapLast)
        {
            // swap the values of the last position
            long temp = lastA;
            lastA = lastB;
            lastB = temp;
            ops = 1; // cost for swapping at index n-1
        }

        for (int i = 0; i < n - 1; i++)
        {
            long x = a[i];
            long y = b[i];

            if (x <= lastA && y <= lastB)
            {
                // no swap needed at this index
                continue;
            }
            else if (x <= lastB && y <= lastA)
            {
                // must swap at this index
                ops++;
            }
            else
            {
                // impossible to satisfy the conditions for this configuration
                return int.MaxValue;
            }
        }

        return ops;
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
var minOperations = function(nums1, nums2) {
    const n = nums1.length;
    if (n === 0) return -1; // shouldn't happen per constraints
    
    const evaluate = (a, b) => {
        let swaps = 0;
        for (let i = 0; i < n - 1; ++i) {
            const x = nums1[i];
            const y = nums2[i];
            if (x <= a && y <= b) {
                // no swap needed
                continue;
            } else if (x <= b && y <= a) {
                // must swap this pair
                swaps++;
            } else {
                return Infinity; // impossible configuration
            }
        }
        return swaps;
    };
    
    const a1 = nums1[n - 1];
    const b1 = nums2[n - 1];
    let ans = evaluate(a1, b1);
    
    // consider swapping the last pair first (cost +1)
    const a2 = nums2[n - 1];
    const b2 = nums1[n - 1];
    const second = evaluate(a2, b2);
    if (second !== Infinity) {
        ans = Math.min(ans, second + 1);
    }
    
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minOperations(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const compute = (a: number, b: number): number => {
        let swaps = 0;
        for (let i = 0; i < n - 1; ++i) {
            const x = nums1[i];
            const y = nums2[i];
            if (x <= a && y <= b) continue;
            if (y <= a && x <= b) swaps++;
            else return -1;
        }
        return swaps;
    };
    let best = Infinity;
    const withoutSwap = compute(nums1[n - 1], nums2[n - 1]);
    if (withoutSwap !== -1) best = Math.min(best, withoutSwap);
    const withSwapLast = compute(nums2[n - 1], nums1[n - 1]);
    if (withSwapLast !== -1) best = Math.min(best, withSwapLast + 1);
    return best === Infinity ? -1 : best;
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
    function minOperations($nums1, $nums2) {
        $n = count($nums1);
        $calc = function($a, $b) use ($nums1, $nums2, $n) {
            $cnt = 0;
            for ($i = 0; $i < $n - 1; $i++) {
                $x = $nums1[$i];
                $y = $nums2[$i];
                if ($x <= $a && $y <= $b) {
                    continue;
                } elseif ($x <= $b && $y <= $a) {
                    $cnt++;
                } else {
                    return -1;
                }
            }
            return $cnt;
        };
        $ans = PHP_INT_MAX;
        $c1 = $calc($nums1[$n-1], $nums2[$n-1]);
        if ($c1 != -1) {
            $ans = min($ans, $c1);
        }
        $c2 = $calc($nums2[$n-1], $nums1[$n-1]);
        if ($c2 != -1) {
            $ans = min($ans, $c2 + 1);
        }
        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var answer = Int.max

        func tryCase(a: Int, b: Int, baseCost: Int) -> Int? {
            var swaps = baseCost
            if n > 1 {
                for i in 0..<(n - 1) {
                    let x = nums1[i]
                    let y = nums2[i]
                    if x <= a && y <= b {
                        continue
                    } else if y <= a && x <= b {
                        swaps += 1
                    } else {
                        return nil
                    }
                }
            }
            return swaps
        }

        if let v = tryCase(a: nums1[n - 1], b: nums2[n - 1], baseCost: 0) {
            answer = min(answer, v)
        }
        if let v = tryCase(a: nums2[n - 1], b: nums1[n - 1], baseCost: 1) {
            answer = min(answer, v)
        }

        return answer == Int.max ? -1 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        val INF = Int.MAX_VALUE / 4

        fun ops(lastA: Int, lastB: Int): Int {
            var cnt = 0
            for (i in 0 until n - 1) {
                val a = nums1[i]
                val b = nums2[i]
                if (a <= lastA && b <= lastB) continue
                else if (a <= lastB && b <= lastA) cnt++
                else return INF
            }
            return cnt
        }

        var answer = INF

        val withoutSwapLast = ops(nums1[n - 1], nums2[n - 1])
        if (withoutSwapLast < answer) answer = withoutSwapLast

        val withSwapLast = ops(nums2[n - 1], nums1[n - 1])
        if (withSwapLast < INF) {
            val total = withSwapLast + 1
            if (total < answer) answer = total
        }

        return if (answer >= INF) -1 else answer
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    const int INF = 1 << 30;

    int helper(int last1, int last2) {
      int cnt = 0;
      for (int i = 0; i < n - 1; ++i) {
        int a = nums1[i];
        int b = nums2[i];
        if (a <= last1 && b <= last2) {
          continue;
        } else if (a <= last2 && b <= last1) {
          cnt++;
        } else {
          return INF;
        }
      }
      return cnt;
    }

    int ans = INF;

    int res1 = helper(nums1[n - 1], nums2[n - 1]);
    if (res1 < INF) ans = res1;

    int res2 = helper(nums2[n - 1], nums1[n - 1]);
    if (res2 < INF) {
      int total = 1 + res2; // swap the last index
      if (total < ans) ans = total;
    }

    return ans >= INF ? -1 : ans;
  }
}
```

## Golang

```go
func minOperations(nums1 []int, nums2 []int) int {
	n := len(nums1)
	const INF = int(1e9)

	helper := func(a, b int) (int, bool) {
		cnt := 0
		for i := 0; i < n-1; i++ {
			if nums1[i] <= a && nums2[i] <= b {
				continue
			} else if nums1[i] <= b && nums2[i] <= a {
				cnt++
			} else {
				return 0, false
			}
		}
		return cnt, true
	}

	ans := INF

	if cnt, ok := helper(nums1[n-1], nums2[n-1]); ok {
		if cnt < ans {
			ans = cnt
		}
	}
	if cnt, ok := helper(nums2[n-1], nums1[n-1]); ok {
		if cnt+1 < ans {
			ans = cnt + 1
		}
	}

	if ans == INF {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
INF = (1 << 60)

def count_swaps(nums1, nums2, a_last, b_last)
  cnt = 0
  (0...nums1.length - 1).each do |i|
    if nums1[i] <= a_last && nums2[i] <= b_last
      next
    elsif nums2[i] <= a_last && nums1[i] <= b_last
      cnt += 1
    else
      return INF
    end
  end
  cnt
end

def min_operations(nums1, nums2)
  ops_keep = count_swaps(nums1, nums2, nums1[-1], nums2[-1])
  ops_swap_last = count_swaps(nums1, nums2, nums2[-1], nums1[-1])

  ans = ops_keep
  if ops_swap_last != INF
    ans = [ans, ops_swap_last + 1].min
  end

  ans >= INF ? -1 : ans
end
```

## Scala

```scala
object Solution {
    def minOperations(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length

        def solve(x: Int, y: Int): Option[Int] = {
            var swaps = 0
            for (i <- 0 until n - 1) {
                val a = nums1(i)
                val b = nums2(i)
                val noSwap = a <= x && b <= y
                val swap   = b <= x && a <= y
                if (!noSwap && !swap) return None
                else if (!noSwap && swap) swaps += 1
            }
            Some(swaps)
        }

        val opt1 = solve(nums1(n - 1), nums2(n - 1))
        val opt2 = solve(nums2(n - 1), nums1(n - 1)).map(_ + 1)

        (opt1, opt2) match {
            case (None, None) => -1
            case (Some(v1), None) => v1
            case (None, Some(v2)) => v2
            case (Some(v1), Some(v2)) => math.min(v1, v2)
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        if n == 1 {
            return 0;
        }

        fn needed_swaps(nums1: &[i32], nums2: &[i32], a: i32, b: i32) -> Option<i32> {
            let mut cnt = 0;
            for i in 0..nums1.len() - 1 {
                let x = nums1[i];
                let y = nums2[i];
                if x <= a && y <= b {
                    continue;
                } else if x <= b && y <= a {
                    cnt += 1;
                } else {
                    return None;
                }
            }
            Some(cnt)
        }

        let mut answer: Option<i32> = None;

        // Case 1: keep last elements as they are
        if let Some(c) = needed_swaps(&nums1, &nums2, nums1[n - 1], nums2[n - 1]) {
            answer = Some(match answer {
                Some(prev) => prev.min(c),
                None => c,
            });
        }

        // Case 2: swap the last elements (cost +1)
        if let Some(c) = needed_swaps(&nums1, &nums2, nums2[n - 1], nums1[n - 1]) {
            let total = c + 1;
            answer = Some(match answer {
                Some(prev) => prev.min(total),
                None => total,
            });
        }

        match answer {
            Some(v) => v,
            None => -1,
        }
    }
}
```

## Racket

```racket
(define/contract (min-operations nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (n (vector-length v1))
         (last-index (- n 1))
         (a0 (vector-ref v1 last-index))
         (b0 (vector-ref v2 last-index)))
    (define (count-swaps a b)
      (let loop ((i 0) (cnt 0))
        (if (= i last-index)
            cnt
            (let ((x (vector-ref v1 i))
                  (y (vector-ref v2 i)))
              (cond [(and (<= x a) (<= y b)) (loop (+ i 1) cnt)]
                    [(and (<= y a) (<= x b)) (loop (+ i 1) (+ cnt 1))]
                    [else #f])))))
    (define total0 (count-swaps a0 b0))
    (define a1 (vector-ref v2 last-index))
    (define b1 (vector-ref v1 last-index))
    (define total1
      (let ((cnt (count-swaps a1 b1)))
        (if cnt (+ 1 cnt) #f)))
    (cond [(and total0 total1) (min total0 total1)]
          [total0 total0]
          [total1 total1]
          [else -1])))
```

## Erlang

```erlang
-define(INF, 1000000).

min_operations(Nums1, Nums2) ->
    N = length(Nums1),
    case N of
        1 -> 0;
        _ ->
            LastIdx = N,
            Last1 = lists:nth(LastIdx, Nums1),
            Last2 = lists:nth(LastIdx, Nums2),
            PrefixLen = N - 1,
            Prefix1 = lists:sublist(Nums1, PrefixLen),
            Prefix2 = lists:sublist(Nums2, PrefixLen),

            Res0 = case solve(Prefix1, Prefix2, Last1, Last2) of
                       {ok, Sw} -> Sw;
                       error -> ?INF
                   end,
            Res1 = case solve(Prefix1, Prefix2, Last2, Last1) of
                       {ok, Sw} -> Sw + 1;
                       error -> ?INF
                   end,
            Min = erlang:min(Res0, Res1),
            if Min == ?INF -> -1; true -> Min end
    end.

solve(Prefix1, Prefix2, A_last, B_last) ->
    solve_helper(Prefix1, Prefix2, A_last, B_last, 0).

solve_helper([], [], _A, _B, Acc) ->
    {ok, Acc};
solve_helper([X|Xs], [Y|Ys], A_last, B_last, Acc) ->
    if
        X =< A_last andalso Y =< B_last ->
            solve_helper(Xs, Ys, A_last, B_last, Acc);
        X =< B_last andalso Y =< A_last ->
            solve_helper(Xs, Ys, A_last, B_last, Acc + 1);
        true ->
            error
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_operations(nums1, nums2) do
    n = length(nums1)
    a = Enum.at(nums1, n - 1)
    b = Enum.at(nums2, n - 1)

    case evaluate(nums1, nums2, a, b) do
      {:ok, cnt_a} ->
        # scenario with swapping last elements
        case evaluate(nums1, nums2, b, a) do
          {:ok, cnt_b} -> min(cnt_a, cnt_b + 1)
          :error -> cnt_a
        end

      :error ->
        case evaluate(nums1, nums2, b, a) do
          {:ok, cnt_b} -> cnt_b + 1
          :error -> -1
        end
    end
  end

  defp evaluate(nums1, nums2, limit1, limit2) do
    n = length(nums1)
    max_idx = n - 2

    if max_idx < 0 do
      {:ok, 0}
    else
      Enum.reduce_while(0..max_idx, 0, fn i, acc ->
        x = Enum.at(nums1, i)
        y = Enum.at(nums2, i)

        cond do
          x <= limit1 and y <= limit2 -> {:cont, acc}
          x <= limit2 and y <= limit1 -> {:cont, acc + 1}
          true -> {:halt, :error}
        end
      end)
      |> case do
        :error -> :error
        cnt -> {:ok, cnt}
      end
    end
  end
end
```
