# 2100. Find Good Days to Rob the Bank

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        int n = security.size();
        vector<int> left(n, 0), right(n, 0);
        for (int i = 1; i < n; ++i) {
            if (security[i - 1] >= security[i])
                left[i] = left[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; --i) {
            if (security[i] <= security[i + 1])
                right[i] = right[i + 1] + 1;
        }
        vector<int> ans;
        for (int i = 0; i < n; ++i) {
            if (left[i] >= time && right[i] >= time)
                ans.push_back(i);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        int n = security.length;
        List<Integer> result = new ArrayList<>();
        if (time == 0) {
            for (int i = 0; i < n; i++) result.add(i);
            return result;
        }
        int[] left = new int[n];
        int[] right = new int[n];
        
        left[0] = 1;
        for (int i = 1; i < n; i++) {
            if (security[i - 1] >= security[i]) {
                left[i] = left[i - 1] + 1;
            } else {
                left[i] = 1;
            }
        }
        
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (security[i] <= security[i + 1]) {
                right[i] = right[i + 1] + 1;
            } else {
                right[i] = 1;
            }
        }
        
        int need = time + 1;
        for (int i = 0; i < n; i++) {
            if (left[i] >= need && right[i] >= need) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        n = len(security)
        if time == 0:
            return list(range(n))
        
        left = [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1
        
        right = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        
        res = []
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                res.append(i)
        return res
```

## Python3

```python
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))
        left = [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1
        right = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        res = []
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                res.append(i)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodDaysToRobBank(int* security, int securitySize, int time, int* returnSize) {
    int n = securitySize;
    if (n == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int *left = (int *)malloc(n * sizeof(int));
    int *right = (int *)malloc(n * sizeof(int));
    if (!left || !right) {
        free(left);
        free(right);
        *returnSize = 0;
        return NULL;
    }
    
    left[0] = 0;
    for (int i = 1; i < n; ++i) {
        if (security[i - 1] >= security[i])
            left[i] = left[i - 1] + 1;
        else
            left[i] = 0;
    }
    
    right[n - 1] = 0;
    for (int i = n - 2; i >= 0; --i) {
        if (security[i] <= security[i + 1])
            right[i] = right[i + 1] + 1;
        else
            right[i] = 0;
    }
    
    int *result = (int *)malloc(n * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (left[i] >= time && right[i] >= time) {
            result[cnt++] = i;
        }
    }
    
    free(left);
    free(right);
    
    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> GoodDaysToRobBank(int[] security, int time) {
        int n = security.Length;
        var left = new int[n];
        var right = new int[n];

        for (int i = 1; i < n; i++) {
            if (security[i - 1] >= security[i])
                left[i] = left[i - 1] + 1;
            else
                left[i] = 0;
        }

        for (int i = n - 2; i >= 0; i--) {
            if (security[i] <= security[i + 1])
                right[i] = right[i + 1] + 1;
            else
                right[i] = 0;
        }

        var result = new List<int>();
        for (int i = 0; i < n; i++) {
            if (left[i] >= time && right[i] >= time)
                result.Add(i);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} security
 * @param {number} time
 * @return {number[]}
 */
var goodDaysToRobBank = function(security, time) {
    const n = security.length;
    const left = new Array(n).fill(0);
    const right = new Array(n).fill(0);
    
    for (let i = 1; i < n; ++i) {
        if (security[i - 1] >= security[i]) {
            left[i] = left[i - 1] + 1;
        }
    }
    
    for (let i = n - 2; i >= 0; --i) {
        if (security[i] <= security[i + 1]) {
            right[i] = right[i + 1] + 1;
        }
    }
    
    const result = [];
    for (let i = 0; i < n; ++i) {
        if (left[i] >= time && right[i] >= time) {
            result.push(i);
        }
    }
    return result;
};
```

## Typescript

```typescript
function goodDaysToRobBank(security: number[], time: number): number[] {
    const n = security.length;
    if (time === 0) {
        // Every day is valid
        return Array.from({ length: n }, (_, i) => i);
    }
    const left: number[] = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (security[i - 1] >= security[i]) {
            left[i] = left[i - 1] + 1;
        } else {
            left[i] = 1;
        }
    }

    const right: number[] = new Array(n).fill(1);
    for (let i = n - 2; i >= 0; i--) {
        if (security[i] <= security[i + 1]) {
            right[i] = right[i + 1] + 1;
        } else {
            right[i] = 1;
        }
    }

    const result: number[] = [];
    const need = time + 1; // length of required non‑increasing / non‑decreasing segment
    for (let i = 0; i < n; i++) {
        if (left[i] >= need && right[i] >= need) {
            result.push(i);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $security
     * @param Integer $time
     * @return Integer[]
     */
    function goodDaysToRobBank($security, $time) {
        $n = count($security);
        if ($time == 0) {
            $res = [];
            for ($i = 0; $i < $n; $i++) {
                $res[] = $i;
            }
            return $res;
        }

        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);

        // left[i]: length of non‑increasing sequence ending at i (including i)
        $left[0] = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($security[$i - 1] >= $security[$i]) {
                $left[$i] = $left[$i - 1] + 1;
            } else {
                $left[$i] = 1;
            }
        }

        // right[i]: length of non‑decreasing sequence starting at i (including i)
        $right[$n - 1] = 1;
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($security[$i] <= $security[$i + 1]) {
                $right[$i] = $right[$i + 1] + 1;
            } else {
                $right[$i] = 1;
            }
        }

        $res = [];
        for ($i = $time; $i < $n - $time; $i++) {
            if ($left[$i] >= $time + 1 && $right[$i] >= $time + 1) {
                $res[] = $i;
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func goodDaysToRobBank(_ security: [Int], _ time: Int) -> [Int] {
        let n = security.count
        if time == 0 { return Array(0..<n) }
        var left = Array(repeating: 0, count: n)
        for i in 1..<n {
            if security[i - 1] >= security[i] {
                left[i] = left[i - 1] + 1
            } else {
                left[i] = 0
            }
        }
        var right = Array(repeating: 0, count: n)
        if n > 0 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                if security[i] <= security[i + 1] {
                    right[i] = right[i + 1] + 1
                } else {
                    right[i] = 0
                }
            }
        }
        var result = [Int]()
        for i in 0..<n {
            if left[i] >= time && right[i] >= time {
                result.append(i)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun goodDaysToRobBank(security: IntArray, time: Int): List<Int> {
        val n = security.size
        if (time == 0) return (0 until n).toList()
        val left = IntArray(n)
        val right = IntArray(n)

        left[0] = 1
        for (i in 1 until n) {
            left[i] = if (security[i - 1] >= security[i]) left[i - 1] + 1 else 1
        }

        right[n - 1] = 1
        for (i in n - 2 downTo 0) {
            right[i] = if (security[i] <= security[i + 1]) right[i + 1] + 1 else 1
        }

        val result = mutableListOf<Int>()
        for (i in time until n - time) {
            if (left[i] >= time + 1 && right[i] >= time + 1) {
                result.add(i)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> goodDaysToRobBank(List<int> security, int time) {
    int n = security.length;
    if (time == 0) {
      return List<int>.generate(n, (i) => i);
    }
    List<int> left = List.filled(n, 0);
    for (int i = 1; i < n; i++) {
      if (security[i - 1] >= security[i]) {
        left[i] = left[i - 1] + 1;
      } else {
        left[i] = 0;
      }
    }

    List<int> right = List.filled(n, 0);
    for (int i = n - 2; i >= 0; i--) {
      if (security[i] <= security[i + 1]) {
        right[i] = right[i + 1] + 1;
      } else {
        right[i] = 0;
      }
    }

    List<int> result = [];
    for (int i = time; i <= n - time - 1; i++) {
      if (left[i] >= time && right[i] >= time) {
        result.add(i);
      }
    }
    return result;
  }
}
```

## Golang

```go
func goodDaysToRobBank(security []int, time int) []int {
	n := len(security)
	if n == 0 {
		return nil
	}
	left := make([]int, n)
	right := make([]int, n)

	// left[i]: length of non‑increasing sequence ending at i (including i)
	for i := 0; i < n; i++ {
		if i > 0 && security[i-1] >= security[i] {
			left[i] = left[i-1] + 1
		} else {
			left[i] = 1
		}
	}

	// right[i]: length of non‑decreasing sequence starting at i (including i)
	for i := n - 1; i >= 0; i-- {
		if i+1 < n && security[i] <= security[i+1] {
			right[i] = right[i+1] + 1
		} else {
			right[i] = 1
		}
	}

	required := time + 1
	var ans []int
	for i := time; i <= n-time-1; i++ {
		if left[i] >= required && right[i] >= required {
			ans = append(ans, i)
		}
	}
	return ans
}
```

## Ruby

```ruby
def good_days_to_rob_bank(security, time)
  n = security.length
  return (0...n).to_a if time == 0

  left = Array.new(n, 0)
  (1...n).each do |i|
    left[i] = security[i - 1] >= security[i] ? left[i - 1] + 1 : 0
  end

  right = Array.new(n, 0)
  (n - 2).downto(0) do |i|
    right[i] = security[i] <= security[i + 1] ? right[i + 1] + 1 : 0
  end

  result = []
  (0...n).each do |i|
    result << i if left[i] >= time && right[i] >= time
  end
  result
end
```

## Scala

```scala
object Solution {
    def goodDaysToRobBank(security: Array[Int], time: Int): List[Int] = {
        val n = security.length
        if (time == 0) return (0 until n).toList

        val left = new Array[Int](n)
        for (i <- 1 until n) {
            if (security(i - 1) >= security(i)) left(i) = left(i - 1) + 1
            else left(i) = 0
        }

        val right = new Array[Int](n)
        for (i <- (0 until n - 1).reverse) {
            if (security(i) <= security(i + 1)) right(i) = right(i + 1) + 1
            else right(i) = 0
        }

        val res = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 0 until n) {
            if (left(i) >= time && right(i) >= time) res += i
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn good_days_to_rob_bank(security: Vec<i32>, time: i32) -> Vec<i32> {
        let n = security.len();
        let t = time as usize;
        if t == 0 {
            return (0..n).map(|i| i as i32).collect();
        }
        let mut left = vec![0usize; n];
        for i in 1..n {
            if security[i - 1] >= security[i] {
                left[i] = left[i - 1] + 1;
            }
        }
        let mut right = vec![0usize; n];
        for i in (0..n - 1).rev() {
            if security[i] <= security[i + 1] {
                right[i] = right[i + 1] + 1;
            }
        }
        let mut res = Vec::new();
        for i in 0..n {
            if left[i] >= t && right[i] >= t {
                res.push(i as i32);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (good-days-to-rob-bank security time)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((sec-vec (list->vector security))
         (n (vector-length sec-vec)))
    (if (= time 0)
        (build-list n (lambda (i) i))
        (let ((left (make-vector n 0))
              (right (make-vector n 0)))
          ;; left[i]: consecutive non‑increasing days ending at i
          (for ([i (in-range 1 n)])
            (if (>= (vector-ref sec-vec (- i 1)) (vector-ref sec-vec i))
                (vector-set! left i (+ (vector-ref left (- i 1)) 1))
                (vector-set! left i 0)))
          ;; right[i]: consecutive non‑decreasing days starting at i
          (for ([i (in-range (- n 2) -1 -1)])
            (if (<= (vector-ref sec-vec i) (vector-ref sec-vec (+ i 1)))
                (vector-set! right i (+ (vector-ref right (+ i 1)) 1))
                (vector-set! right i 0)))
          ;; collect good days
          (for/list ([i (in-range n)]
                     #:when (and (>= (vector-ref left i) time)
                                 (>= (vector-ref right i) time)))
            i))))))
```

## Erlang

```erlang
-spec good_days_to_rob_bank(Security :: [integer()], Time :: integer()) -> [integer()].
good_days_to_rob_bank(Security, Time) ->
    case Time of
        0 ->
            Len = length(Security),
            lists:seq(0, Len - 1);
        _ ->
            SecTuple = list_to_tuple(Security),
            N = tuple_size(SecTuple),
            LeftTuple = compute_left(SecTuple, N),
            RightTuple = compute_right(SecTuple, N),
            gather_good(N, Time, LeftTuple, RightTuple, [])
    end.

%% Compute left array: consecutive non‑increasing days ending at each index
compute_left(Tuple, N) ->
    List = left_loop(0, N, Tuple, 0, []),
    list_to_tuple(lists:reverse(List)).

left_loop(I, N, _Tuple, _PrevLeft, Acc) when I >= N -> Acc;
left_loop(I, N, Tuple, PrevLeft, Acc) ->
    CurrLeft = case I of
        0 -> 0;
        _ ->
            PrevSec = element(I, Tuple),      % security[i-1]
            CurrSec = element(I + 1, Tuple),  % security[i]
            if PrevSec >= CurrSec -> PrevLeft + 1; true -> 0 end
    end,
    left_loop(I + 1, N, Tuple, CurrLeft, [CurrLeft | Acc]).

%% Compute right array: consecutive non‑decreasing days starting at each index
compute_right(Tuple, N) ->
    List = right_loop(N - 1, Tuple, N, 0, []),
    list_to_tuple(List).

right_loop(I, _Tuple, _N, _PrevRight, Acc) when I < 0 -> Acc;
right_loop(I, Tuple, N, PrevRight, Acc) ->
    CurrRight = if I == N - 1 ->
                        0;
                   true ->
                        SecI = element(I + 1, Tuple),
                        SecNext = element(I + 2, Tuple),
                        if SecI =< SecNext -> PrevRight + 1; true -> 0 end
                end,
    right_loop(I - 1, Tuple, N, CurrRight, [CurrRight | Acc]).

%% Gather good days where both left and right counts satisfy Time
gather_good(N, Time, LeftTuple, RightTuple, Acc) ->
    gather_good(0, N, Time, LeftTuple, RightTuple, Acc).

gather_good(I, N, _Time, _Left, _Right, Acc) when I >= N -> lists:reverse(Acc);
gather_good(I, N, Time, Left, Right, Acc) ->
    L = element(I + 1, Left),
    R = element(I + 1, Right),
    NewAcc = if L >= Time andalso R >= Time -> [I | Acc]; true -> Acc end,
    gather_good(I + 1, N, Time, Left, Right, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec good_days_to_rob_bank(security :: [integer], time :: integer) :: [integer]
  def good_days_to_rob_bank(security, time) do
    n = length(security)

    if time == 0 do
      Enum.to_list(0..(n - 1))
    else
      sec = List.to_tuple(security)
      left = compute_left(sec, n)
      right = compute_right(sec, n)

      left_t = List.to_tuple(left)
      right_t = List.to_tuple(right)

      0..(n - 1)
      |> Enum.filter(fn i ->
        :erlang.element(i + 1, left_t) >= time and
          :erlang.element(i + 1, right_t) >= time
      end)
      |> Enum.to_list()
    end
  end

  defp compute_left(sec, n), do: compute_left(0, sec, n, [])

  defp compute_left(i, _sec, n, acc) when i == n,
    do: Enum.reverse(acc)

  defp compute_left(i, sec, n, acc) do
    left_val =
      if i == 0 do
        0
      else
        prev = :erlang.element(i, sec)
        cur = :erlang.element(i + 1, sec)

        if prev >= cur do
          hd(acc) + 1
        else
          0
        end
      end

    compute_left(i + 1, sec, n, [left_val | acc])
  end

  defp compute_right(sec, n), do: compute_right(n - 1, sec, n, [])

  defp compute_right(i, _sec, _n, acc) when i < 0,
    do: Enum.reverse(acc)

  defp compute_right(i, sec, n, acc) do
    right_val =
      if i == n - 1 do
        0
      else
        cur = :erlang.element(i + 1, sec)
        nxt = :erlang.element(i + 2, sec)

        if cur <= nxt do
          hd(acc) + 1
        else
          0
        end
      end

    compute_right(i - 1, sec, n, [right_val | acc])
  end
end
```
