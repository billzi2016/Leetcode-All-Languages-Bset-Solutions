# 0967. Numbers With Same Consecutive Differences

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> ans;
        if (n == 1) {
            for (int d = 0; d <= 9; ++d) ans.push_back(d);
            return ans;
        }
        function<void(int,int)> dfs = [&](int len, int cur) {
            if (len == n) {
                ans.push_back(cur);
                return;
            }
            int last = cur % 10;
            int nxt1 = last + k;
            int nxt2 = last - k;
            if (nxt1 >= 0 && nxt1 <= 9) {
                dfs(len + 1, cur * 10 + nxt1);
            }
            if (k != 0 && nxt2 >= 0 && nxt2 <= 9) { // avoid duplicate when k==0
                dfs(len + 1, cur * 10 + nxt2);
            }
        };
        for (int d = 1; d <= 9; ++d) {
            dfs(1, d);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
        List<Integer> res = new ArrayList<>();
        if (n == 1) {
            for (int d = 0; d <= 9; d++) {
                res.add(d);
            }
        } else {
            for (int d = 1; d <= 9; d++) {
                dfs(n, k, 1, d, res);
            }
        }
        int[] ans = new int[res.size()];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = res.get(i);
        }
        return ans;
    }

    private void dfs(int n, int k, int pos, int num, List<Integer> res) {
        if (pos == n) {
            res.add(num);
            return;
        }
        int last = num % 10;
        int plus = last + k;
        int minus = last - k;

        if (plus >= 0 && plus <= 9) {
            dfs(n, k, pos + 1, num * 10 + plus, res);
        }
        if (k != 0 && minus >= 0 && minus <= 9) { // avoid duplicate when k == 0
            dfs(n, k, pos + 1, num * 10 + minus, res);
        }
    }
}
```

## Python

```python
class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if n == 1:
            return [i for i in range(10)]
        
        res = []
        def dfs(num, length):
            if length == n:
                res.append(num)
                return
            last = num % 10
            next_digits = set()
            if last + k <= 9:
                next_digits.add(last + k)
            if last - k >= 0:
                next_digits.add(last - k)
            for nd in next_digits:
                dfs(num * 10 + nd, length + 1)
        
        for start in range(1, 10):
            dfs(start, 1)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        cur = [i for i in range(1, 10)]
        for _ in range(n - 1):
            nxt = []
            for num in cur:
                last = num % 10
                add = last + k
                sub = last - k
                if add < 10:
                    nxt.append(num * 10 + add)
                if k != 0 and sub >= 0:
                    nxt.append(num * 10 + sub)
            cur = nxt
        return cur
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numsSameConsecDiff(int n, int k, int* returnSize) {
    if (n == 1) {
        *returnSize = 10;
        int *res = (int*)malloc(10 * sizeof(int));
        for (int i = 0; i < 10; ++i) res[i] = i;
        return res;
    }

    int maxCount = (k == 0) ? 9 : 9 * (1 << (n - 1));
    int *cur = (int*)malloc(maxCount * sizeof(int));
    int curSize = 0;

    for (int d = 1; d <= 9; ++d) {
        cur[curSize++] = d;
    }

    for (int len = 2; len <= n; ++len) {
        int *next = (int*)malloc(maxCount * sizeof(int));
        int nextSize = 0;
        for (int i = 0; i < curSize; ++i) {
            int num = cur[i];
            int last = num % 10;

            if (last + k <= 9) {
                next[nextSize++] = num * 10 + (last + k);
            }
            if (k != 0 && last - k >= 0) {
                next[nextSize++] = num * 10 + (last - k);
            }
        }
        free(cur);
        cur = next;
        curSize = nextSize;
    }

    *returnSize = curSize;
    int *ans = (int*)malloc(curSize * sizeof(int));
    memcpy(ans, cur, curSize * sizeof(int));
    free(cur);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] NumsSameConsecDiff(int n, int k)
    {
        if (n == 1)
        {
            int[] all = new int[10];
            for (int i = 0; i < 10; i++) all[i] = i;
            return all;
        }

        List<int> cur = new List<int>();
        for (int d = 1; d <= 9; d++) cur.Add(d);

        for (int len = 2; len <= n; len++)
        {
            List<int> next = new List<int>();
            foreach (int num in cur)
            {
                int last = num % 10;
                int plus = last + k;
                int minus = last - k;

                if (plus >= 0 && plus <= 9)
                    next.Add(num * 10 + plus);
                if (k != 0 && minus >= 0 && minus <= 9)
                    next.Add(num * 10 + minus);
            }
            cur = next;
        }

        return cur.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var numsSameConsecDiff = function(n, k) {
    const res = [];
    
    // Special case when length is 1: all digits are valid including 0.
    if (n === 1) {
        for (let d = 0; d <= 9; ++d) res.push(d);
        return res;
    }
    
    const dfs = (len, num) => {
        if (len === n) {
            res.push(num);
            return;
        }
        const last = num % 10;
        const nextSet = new Set();
        const plus = last + k;
        const minus = last - k;
        if (plus >= 0 && plus <= 9) nextSet.add(plus);
        if (minus >= 0 && minus <= 9) nextSet.add(minus);
        for (const nxt of nextSet) {
            dfs(len + 1, num * 10 + nxt);
        }
    };
    
    // Start with non‑zero leading digit.
    for (let d = 1; d <= 9; ++d) {
        dfs(1, d);
    }
    
    return res;
};
```

## Typescript

```typescript
function numsSameConsecDiff(n: number, k: number): number[] {
    const result: number[] = [];
    if (n === 1) {
        for (let i = 0; i <= 9; i++) result.push(i);
        return result;
    }
    const dfs = (num: number, len: number) => {
        if (len === n) {
            result.push(num);
            return;
        }
        const last = num % 10;
        const nextDigits = new Set<number>();
        const plus = last + k;
        const minus = last - k;
        if (plus >= 0 && plus <= 9) nextDigits.add(plus);
        if (minus >= 0 && minus <= 9) nextDigits.add(minus);
        for (const nd of nextDigits) {
            dfs(num * 10 + nd, len + 1);
        }
    };
    for (let d = 1; d <= 9; d++) dfs(d, 1);
    return result;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[]
     */
    function numsSameConsecDiff($n, $k) {
        if ($n == 1) {
            return range(0, 9);
        }

        $queue = [];
        for ($i = 1; $i <= 9; $i++) {
            $queue[] = $i;
        }

        for ($len = 2; $len <= $n; $len++) {
            $next = [];
            foreach ($queue as $num) {
                $last = $num % 10;

                if ($k == 0) {
                    $candidates = [$last];
                } else {
                    $candidates = [];
                    $plus = $last + $k;
                    $minus = $last - $k;
                    if ($plus >= 0 && $plus <= 9) {
                        $candidates[] = $plus;
                    }
                    if ($minus >= 0 && $minus <= 9 && $minus != $plus) {
                        $candidates[] = $minus;
                    }
                }

                foreach ($candidates as $d) {
                    $next[] = $num * 10 + $d;
                }
            }
            $queue = $next;
        }

        return $queue;
    }
}
?>
```

## Swift

```swift
class Solution {
    func numsSameConsecDiff(_ n: Int, _ k: Int) -> [Int] {
        if n == 1 {
            return Array(0...9)
        }
        var result = [Int]()
        
        func dfs(_ num: Int, _ remaining: Int) {
            if remaining == 0 {
                result.append(num)
                return
            }
            let lastDigit = num % 10
            var nextDigits = Set<Int>()
            let plus = lastDigit + k
            let minus = lastDigit - k
            if plus >= 0 && plus <= 9 { nextDigits.insert(plus) }
            if minus >= 0 && minus <= 9 { nextDigits.insert(minus) }
            for nd in nextDigits {
                dfs(num * 10 + nd, remaining - 1)
            }
        }
        
        for first in 1...9 {
            dfs(first, n - 1)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numsSameConsecDiff(n: Int, k: Int): IntArray {
        if (n == 1) return IntArray(10) { it }
        var cur = mutableListOf<Int>()
        for (i in 1..9) cur.add(i)
        repeat(n - 1) {
            val next = mutableListOf<Int>()
            for (num in cur) {
                val last = num % 10
                if (last + k <= 9) {
                    next.add(num * 10 + (last + k))
                }
                if (k != 0 && last - k >= 0) {
                    next.add(num * 10 + (last - k))
                }
            }
            cur = next
        }
        return cur.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> numsSameConsecDiff(int n, int k) {
    if (n == 1) {
      return List<int>.generate(10, (i) => i);
    }
    List<int> result = [];

    void dfs(int length, int num) {
      if (length == n) {
        result.add(num);
        return;
      }
      int last = num % 10;
      Set<int> nextDigits = {};
      int plus = last + k;
      int minus = last - k;
      if (plus >= 0 && plus <= 9) nextDigits.add(plus);
      if (minus >= 0 && minus <= 9) nextDigits.add(minus);
      for (int nd in nextDigits) {
        dfs(length + 1, num * 10 + nd);
      }
    }

    for (int i = 1; i <= 9; ++i) {
      dfs(1, i);
    }
    return result;
  }
}
```

## Golang

```go
func numsSameConsecDiff(n int, k int) []int {
	if n == 1 {
		res := make([]int, 10)
		for i := 0; i < 10; i++ {
			res[i] = i
		}
		return res
	}

	cur := []int{}
	for d := 1; d <= 9; d++ {
		cur = append(cur, d)
	}

	for level := 2; level <= n; level++ {
		next := []int{}
		for _, num := range cur {
			last := num % 10
			if last+k <= 9 {
				next = append(next, num*10+last+k)
			}
			if k != 0 && last-k >= 0 {
				next = append(next, num*10+last-k)
			}
		}
		cur = next
	}

	return cur
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def nums_same_consec_diff(n, k)
  return (0..9).to_a if n == 1

  queue = (1..9).to_a
  (n - 1).times do
    next_queue = []
    queue.each do |num|
      last_digit = num % 10
      # add digit +k
      plus = last_digit + k
      next_queue << num * 10 + plus if plus <= 9

      # add digit -k (avoid duplicate when k == 0)
      minus = last_digit - k
      if k != 0 && minus >= 0
        next_queue << num * 10 + minus
      end
    end
    queue = next_queue
  end
  queue
end
```

## Scala

```scala
object Solution {
    def numsSameConsecDiff(n: Int, k: Int): Array[Int] = {
        if (n == 1) {
            return (0 to 9).toArray
        }
        var cur = List[Int]()
        for (d <- 1 to 9) {
            cur ::= d
        }
        for (_ <- 2 to n) {
            var next = List[Int]()
            for (num <- cur) {
                val last = num % 10
                if (last + k <= 9) {
                    next ::= num * 10 + (last + k)
                }
                if (k != 0 && last - k >= 0) {
                    next ::= num * 10 + (last - k)
                }
            }
            cur = next
        }
        cur.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn nums_same_consec_diff(n: i32, k: i32) -> Vec<i32> {
        let n = n as usize;
        if n == 1 {
            return (0..=9).collect();
        }
        let mut res = Vec::new();

        fn dfs(pos: usize, n: usize, num: i32, k: i32, out: &mut Vec<i32>) {
            if pos == n {
                out.push(num);
                return;
            }
            let last = num % 10;
            let plus = last + k;
            if plus >= 0 && plus <= 9 {
                dfs(pos + 1, n, num * 10 + plus, k, out);
            }
            // avoid duplicate when k == 0
            if k != 0 {
                let minus = last - k;
                if minus >= 0 && minus <= 9 {
                    dfs(pos + 1, n, num * 10 + minus, k, out);
                }
            }
        }

        for d in 1..=9 {
            dfs(1, n, d as i32, k, &mut res);
        }
        res
    }
}
```

## Racket

```racket
#lang racket

(provide nums-same-consec-diff)

(define/contract (nums-same-consec-diff n k)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (if (= n 1)
      (build-list 10 (lambda (i) i))
      (let loop ((len 1) (currs (range 1 10)) (res '()))
        (if (= len n)
            (append res currs)
            (let ((next
                   (apply append
                          (map (lambda (num)
                                 (let* ((last-digit (modulo num 10))
                                        (cands (if (= k 0)
                                                   (list (+ last-digit k))
                                                   (filter (lambda (d) (and (>= d 0) (< d 10)))
                                                           (list (+ last-digit k) (- last-digit k))))))
                                   (map (lambda (d) (+ (* num 10) d)) cands)))
                               currs))))
              (loop (+ len 1) next res))))))
```

## Erlang

```erlang
-module(solution).
-export([nums_same_consec_diff/2]).

-spec nums_same_consec_diff(N :: integer(), K :: integer()) -> [integer()].
nums_same_consec_diff(N, K) ->
    case N of
        1 -> lists:seq(0,9);
        _ ->
            Initial = lists:seq(1,9),
            build(N, K, Initial, 2)
    end.

build(N, _K, Current, Level) when Level > N -> Current;
build(N, K, Current, Level) ->
    Next = [Num*10 + D || Num <- Current,
                           D <- possible_digits(Num rem 10, K)],
    build(N, K, Next, Level+1).

possible_digits(_Last, K) when K == 0 -> [_Last];
possible_digits(Last, K) ->
    Up = Last + K,
    Down = Last - K,
    Digits = case {Up,Down} of
                {U,D} when U == D -> [U];
                _ -> [Up,Down]
            end,
    lists:filter(fun(D) -> D >= 0 andalso D =< 9 end, Digits).
```

## Elixir

```elixir
defmodule Solution do
  @spec nums_same_consec_diff(n :: integer, k :: integer) :: [integer]
  def nums_same_consec_diff(n, k) do
    if n == 1 do
      Enum.to_list(0..9)
    else
      init = Enum.to_list(1..9)

      Enum.reduce(2..n, init, fn _level, acc ->
        Enum.flat_map(acc, fn num ->
          last = rem(num, 10)

          candidates =
            if k == 0 do
              [last]
            else
              [last + k, last - k] |> Enum.uniq()
            end

          candidates
          |> Enum.filter(&(&1 >= 0 and &1 <= 9))
          |> Enum.map(fn d -> num * 10 + d end)
        end)
      end)
    end
  end
end
```
