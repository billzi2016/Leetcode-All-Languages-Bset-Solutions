# 1521. Find a Value of a Mysterious Function Closest to Target

## Cpp

```cpp
class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        const int INF = 1e9;
        int ans = INF;
        vector<pair<int,int>> prev; // (and value, start index)
        for (int i = 0; i < (int)arr.size(); ++i) {
            vector<pair<int,int>> cur;
            cur.emplace_back(arr[i], i);
            for (auto &p : prev) {
                int newVal = p.first & arr[i];
                if (newVal == cur.back().first) continue;
                cur.emplace_back(newVal, p.second);
            }
            for (auto &p : cur) {
                int diff = abs(p.first - target);
                if (diff < ans) {
                    ans = diff;
                    if (ans == 0) return 0;
                }
            }
            prev.swap(cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int closestToTarget(int[] arr, int target) {
        int ans = Integer.MAX_VALUE;
        // list of distinct AND values for subarrays ending at previous index
        java.util.ArrayList<Integer> prev = new java.util.ArrayList<>();
        for (int num : arr) {
            java.util.ArrayList<Integer> cur = new java.util.ArrayList<>();
            cur.add(num);
            for (int v : prev) {
                int nv = v & num;
                if (nv != cur.get(cur.size() - 1)) {
                    cur.add(nv);
                }
            }
            // update answer with current AND values
            for (int v : cur) {
                int diff = Math.abs(v - target);
                if (diff < ans) {
                    ans = diff;
                    if (ans == 0) return 0; // cannot get better than zero
                }
            }
            prev = cur;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        ans = float('inf')
        cur = []  # distinct AND values for subarrays ending at previous index
        for a in arr:
            nxt = [a]
            for v in cur:
                nv = v & a
                if nv != nxt[-1]:
                    nxt.append(nv)
            cur = nxt
            for v in cur:
                diff = abs(v - target)
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        return 0
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = float('inf')
        cur = []
        for a in arr:
            nxt = [a]
            for v in cur:
                nv = v & a
                if nv != nxt[-1]:
                    nxt.append(nv)
            cur = nxt
            for v in cur:
                diff = v - target
                if diff < 0:
                    diff = -diff
                if diff < ans:
                    ans = diff
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int closestToTarget(int* arr, int arrSize, int target) {
    int answer = INT_MAX;
    int prevVals[32];
    int prevSize = 0;

    for (int i = 0; i < arrSize; ++i) {
        int curVals[32];
        int curSize = 0;

        // start new subarray at i
        curVals[curSize++] = arr[i];

        // extend previous subarrays
        for (int k = 0; k < prevSize; ++k) {
            int v = prevVals[k] & arr[i];
            if (v != curVals[curSize - 1]) {
                curVals[curSize++] = v;
            }
        }

        // update answer with all distinct AND values ending at i
        for (int k = 0; k < curSize; ++k) {
            int diff = abs(curVals[k] - target);
            if (diff < answer) {
                answer = diff;
                if (answer == 0) return 0;
            }
        }

        // prepare for next iteration
        memcpy(prevVals, curVals, curSize * sizeof(int));
        prevSize = curSize;
    }

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int ClosestToTarget(int[] arr, int target) {
        int best = int.MaxValue;
        List<int> prev = new List<int>();
        foreach (int a in arr) {
            List<int> cur = new List<int>();
            cur.Add(a);
            foreach (int v in prev) {
                int nv = v & a;
                if (nv != cur[cur.Count - 1]) {
                    cur.Add(nv);
                }
            }
            foreach (int v in cur) {
                int diff = Math.Abs(v - target);
                if (diff < best) {
                    best = diff;
                    if (best == 0) return 0;
                }
            }
            prev = cur;
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var closestToTarget = function(arr, target) {
    let best = Infinity;
    let prev = []; // distinct AND values for subarrays ending at previous index
    
    for (let i = 0; i < arr.length; ++i) {
        const x = arr[i];
        const cur = [x];
        // update answer with the single element subarray
        best = Math.min(best, Math.abs(x - target));
        
        for (const v of prev) {
            const nv = v & x;
            if (nv !== cur[cur.length - 1]) {
                cur.push(nv);
            }
        }
        // check all AND values ending at i
        for (const v of cur) {
            const diff = Math.abs(v - target);
            if (diff < best) best = diff;
        }
        prev = cur; // move to next position
    }
    
    return best;
};
```

## Typescript

```typescript
function closestToTarget(arr: number[], target: number): number {
    let best = Number.MAX_SAFE_INTEGER;
    let prev: number[] = [];
    for (const num of arr) {
        const curSet = new Set<number>();
        curSet.add(num);
        for (const v of prev) {
            curSet.add(v & num);
        }
        prev = Array.from(curSet);
        for (const v of prev) {
            const diff = Math.abs(v - target);
            if (diff < best) {
                best = diff;
                if (best === 0) return 0;
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
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function closestToTarget($arr, $target) {
        $ans = PHP_INT_MAX;
        $prev = []; // associative array of possible AND values ending at previous index

        foreach ($arr as $x) {
            $curr = [];
            $curr[$x] = true; // subarray consisting only of current element
            foreach ($prev as $val => $_) {
                $new = $val & $x;
                $curr[$new] = true;
            }
            foreach ($curr as $val => $_) {
                $diff = abs($val - $target);
                if ($diff < $ans) {
                    $ans = $diff;
                    if ($ans === 0) {
                        return 0; // cannot get better than zero
                    }
                }
            }
            $prev = $curr;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func closestToTarget(_ arr: [Int], _ target: Int) -> Int {
        var answer = Int.max
        var prevAnds = [Int]()
        
        for num in arr {
            var curAnds = [Int]()
            curAnds.append(num)
            
            for val in prevAnds {
                let newVal = val & num
                if newVal != curAnds.last! {
                    curAnds.append(newVal)
                }
            }
            
            for v in curAnds {
                let diff = abs(v - target)
                if diff < answer { answer = diff }
                if answer == 0 { return 0 }
            }
            
            prevAnds = curAnds
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closestToTarget(arr: IntArray, target: Int): Int {
        var answer = Int.MAX_VALUE
        var cur = mutableListOf<Int>()
        for (a in arr) {
            val nxt = mutableListOf<Int>()
            nxt.add(a)
            for (v in cur) {
                val newVal = v and a
                if (newVal != nxt.last()) {
                    nxt.add(newVal)
                }
            }
            for (v in nxt) {
                val diff = kotlin.math.abs(v - target)
                if (diff < answer) answer = diff
            }
            cur = nxt
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int closestToTarget(List<int> arr, int target) {
    int ans = (target - arr[0]).abs();
    Set<int> cur = {};
    for (int a in arr) {
      Set<int> nxt = {a};
      for (int v in cur) {
        nxt.add(v & a);
      }
      cur = nxt;
      for (int v in cur) {
        int diff = (v - target).abs();
        if (diff < ans) ans = diff;
      }
      if (ans == 0) return 0;
    }
    return ans;
  }
}
```

## Golang

```go
func closestToTarget(arr []int, target int) int {
    const INF = int(^uint(0) >> 1)
    ans := INF
    prev := make([]int, 0)

    for _, x := range arr {
        cur := make([]int, 0, len(prev)+1)
        cur = append(cur, x)

        for _, v := range prev {
            nv := v & x
            if nv != cur[len(cur)-1] {
                cur = append(cur, nv)
            }
        }

        for _, v := range cur {
            diff := v - target
            if diff < 0 {
                diff = -diff
            }
            if diff < ans {
                ans = diff
                if ans == 0 {
                    return 0
                }
            }
        }

        prev = cur
    }

    return ans
}
```

## Ruby

```ruby
def closest_to_target(arr, target)
  # Initialize answer with a large value
  ans = (arr[0] - target).abs
  cur = []

  arr.each do |x|
    new_cur = [x]
    cur.each do |v|
      new_cur << (v & x)
    end
    # Remove duplicates; number of distinct values stays small (~log maxA)
    cur = new_cur.uniq

    cur.each do |v|
      diff = (v - target).abs
      ans = diff if diff < ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def closestToTarget(arr: Array[Int], target: Int): Int = {
        var best = Int.MaxValue
        var prev = new scala.collection.mutable.ArrayBuffer[Int]()
        for (a <- arr) {
            val cur = new scala.collection.mutable.ArrayBuffer[Int]()
            cur += a
            var idx = 0
            while (idx < prev.length) {
                val nv = prev(idx) & a
                if (nv != cur(cur.length - 1)) {
                    cur += nv
                }
                idx += 1
            }
            idx = 0
            while (idx < cur.length) {
                val diff = math.abs(cur(idx) - target)
                if (diff < best) best = diff
                idx += 1
            }
            prev = cur
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn closest_to_target(arr: Vec<i32>, target: i32) -> i32 {
        let mut ans = (arr[0] - target).abs();
        let mut cur: Vec<i32> = Vec::new();

        for &x in arr.iter() {
            let mut nxt: Vec<i32> = Vec::new();
            // subarray that starts and ends at current index
            nxt.push(x);
            // extend previous subarrays
            for &v in cur.iter() {
                let nv = v & x;
                if *nxt.last().unwrap() != nv {
                    nxt.push(nv);
                }
            }
            // update answer with all distinct AND values ending at this index
            for &val in nxt.iter() {
                let diff = (val - target).abs();
                if diff < ans {
                    ans = diff;
                }
            }
            cur = nxt;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (closest-to-target arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((first (car arr))
         (init-best (abs (- first target))))
    (let loop ((rest (cdr arr))
               (prev (list first))
               (best init-best))
      (if (null? rest)
          best
          (let* ((x (car rest))
                 (candidates (cons x (map (lambda (v) (bitwise-and v x)) prev)))
                 (seen (make-hash))
                 (uniq (for/list ([v candidates]
                                  #:when (not (hash-ref seen v #f)))
                         (begin (hash-set! seen v #t) v)))
                 (new-best (foldl (lambda (v b)
                                    (let ((diff (abs (- v target))))
                                      (if (< diff b) diff b)))
                                  best uniq)))
            (loop (cdr rest) uniq new-best))))))
```

## Erlang

```erlang
-spec closest_to_target(Arr :: [integer()], Target :: integer()) -> integer().
closest_to_target(Arr, Target) ->
    {_, Answer} = lists:foldl(
        fun(X, {PrevVals, Best}) ->
            NewVals = combine(PrevVals, X),
            NewBest = lists:foldl(
                fun(V, Acc) ->
                    D = abs(V - Target),
                    if D < Acc -> D; true -> Acc end
                end,
                Best,
                NewVals
            ),
            {NewVals, NewBest}
        end,
        {[], 1 bsl 60},
        Arr
    ),
    Answer.

%% Helper: compute distinct AND values for subarrays ending at current element.
-spec combine([integer()], integer()) -> [integer()].
combine(PrevVals, X) ->
    lists:foldl(
        fun(V, Acc) ->
            Vb = V band X,
            case Acc of
                [] -> [Vb];
                [Last|_] when Last == Vb -> Acc;
                _ -> [Vb | Acc]
            end
        end,
        [X],
        PrevVals
    ).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec closest_to_target(arr :: [integer], target :: integer) :: integer
  def closest_to_target(arr, target) do
    init_best = 1_000_000_000

    {_last_vals, answer} =
      Enum.reduce(arr, {[], init_best}, fn x, {prev_vals, best} ->
        cur_vals = [x | Enum.map(prev_vals, fn v -> band(v, x) end)]
        uniq_cur = Enum.uniq(cur_vals)

        new_best =
          Enum.reduce(uniq_cur, best, fn val, acc ->
            diff = abs(val - target)
            if diff < acc, do: diff, else: acc
          end)

        {uniq_cur, new_best}
      end)

    answer
  end
end
```
