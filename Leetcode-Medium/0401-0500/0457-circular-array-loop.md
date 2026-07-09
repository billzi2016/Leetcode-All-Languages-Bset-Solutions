# 0457. Circular Array Loop

## Cpp

```cpp
class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        int n = nums.size();
        auto nextIndex = [&](int idx) -> int {
            int nxt = ((idx + nums[idx]) % n + n) % n;
            return nxt;
        };
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) continue;               // already processed
            
            bool direction = nums[i] > 0;              // true for forward, false for backward
            int slow = i, fast = i;
            
            auto getNext = [&](int cur) -> int {
                if (nums[cur] == 0) return -1;         // visited
                if ((nums[cur] > 0) != direction) return -1; // different direction
                int nxt = nextIndex(cur);
                if (nxt == cur) return -1;            // single-element loop not allowed
                return nxt;
            };
            
            while (true) {
                int ns = getNext(slow);
                if (ns == -1) break;
                
                int nf = getNext(fast);
                if (nf == -1) break;
                nf = getNext(nf);
                if (nf == -1) break;
                
                slow = ns;
                fast = nf;
                
                if (slow == fast) return true;        // found a valid cycle
            }
            
            // Mark all nodes visited in this traversal as 0 to avoid reprocessing
            int j = i;
            while (nums[j] != 0 && ((nums[j] > 0) == direction)) {
                int nxt = nextIndex(j);
                nums[j] = 0;                          // mark as processed
                if (nxt == j) break;                  // single-element loop
                j = nxt;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) continue;
            boolean forward = nums[i] > 0;
            int slow = i, fast = i;

            while (true) {
                slow = nextIndex(nums, n, slow, forward);
                if (slow == -1) break;
                fast = nextIndex(nums, n, fast, forward);
                if (fast == -1) break;
                fast = nextIndex(nums, n, fast, forward);
                if (fast == -1) break;

                if (slow == fast) return true;
            }

            int cur = i;
            while (nums[cur] != 0) {
                boolean dir = nums[cur] > 0;
                if (dir != forward) break;
                int nxt = ((cur + nums[cur]) % n + n) % n;
                nums[cur] = 0;
                cur = nxt;
            }
        }
        return false;
    }

    private int nextIndex(int[] nums, int n, int current, boolean forward) {
        if (nums[current] == 0) return -1;
        boolean dir = nums[current] > 0;
        if (dir != forward) return -1;
        int nxt = ((current + nums[current]) % n + n) % n;
        if (nxt == current) return -1; // single-element loop not allowed
        return nxt;
    }
}
```

## Python

```python
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            # direction of movement
            forward = nums[i] > 0
            slow, fast = i, i

            while True:
                # move one step for slow pointer
                nxt_slow = next_index(slow)
                if (nums[nxt_slow] > 0) != forward or nxt_slow == slow:
                    break

                # first step for fast pointer
                nxt_fast = next_index(fast)
                if (nums[nxt_fast] > 0) != forward or nxt_fast == fast:
                    break

                # second step for fast pointer
                nxt_fast2 = next_index(nxt_fast)
                if (nums[nxt_fast2] > 0) != forward or nxt_fast2 == nxt_fast:
                    break

                slow, fast = nxt_slow, nxt_fast2

                if slow == fast:
                    return True

            # mark all nodes in the current traversal as visited
            j = i
            while nums[j] != 0 and (nums[j] > 0) == forward:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False
```

## Python3

```python
from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            direction = nums[i] > 0
            slow, fast = i, i

            while True:
                # move slow one step
                nxt_slow = next_index(slow)
                if nums[nxt_slow] == 0 or (nums[nxt_slow] > 0) != direction:
                    break

                # move fast first step
                nxt_fast1 = next_index(fast)
                if nums[nxt_fast1] == 0 or (nums[nxt_fast1] > 0) != direction:
                    break

                # move fast second step
                nxt_fast2 = next_index(nxt_fast1)
                if nums[nxt_fast2] == 0 or (nums[nxt_fast2] > 0) != direction:
                    break

                slow, fast = nxt_slow, nxt_fast2

                if slow == fast:
                    # single-element loop is not valid
                    if slow == next_index(slow):
                        break
                    return True

            # mark all nodes visited in this component as 0
            j = i
            while nums[j] != 0 and ((nums[j] > 0) == direction):
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False
```

## C

```c
#include <stdbool.h>

static int nextIndex(int *nums, int n, int cur) {
    int nxt = (cur + nums[cur]) % n;
    if (nxt < 0) nxt += n;
    return nxt;
}

bool circularArrayLoop(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 0) continue;

        bool direction = nums[i] > 0;
        int slow = i, fast = i;

        while (true) {
            // move slow one step
            int nxtSlow = nextIndex(nums, numsSize, slow);
            if (nums[nxtSlow] == 0 || (nums[nxtSlow] > 0) != direction || nxtSlow == slow)
                break;

            // move fast first step
            int nxtFast = nextIndex(nums, numsSize, fast);
            if (nums[nxtFast] == 0 || (nums[nxtFast] > 0) != direction || nxtFast == fast)
                break;

            // move fast second step
            int nxtFast2 = nextIndex(nums, numsSize, nxtFast);
            if (nums[nxtFast2] == 0 || (nums[nxtFast2] > 0) != direction || nxtFast2 == nxtFast)
                break;

            slow = nxtSlow;
            fast = nxtFast2;

            if (slow == fast) return true;
        }

        // mark all nodes visited in this traversal as 0
        int cur = i;
        while (nums[cur] != 0) {
            int nxt = nextIndex(nums, numsSize, cur);
            nums[cur] = 0;
            if (nxt == cur) break;
            cur = nxt;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool CircularArrayLoop(int[] nums) {
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) continue;

            bool forward = nums[i] > 0;
            int slow = i, fast = i;

            while (true) {
                int nextSlow = NextIndex(nums, slow, n, forward);
                if (nextSlow == -1) break;

                int nextFast = NextIndex(nums, fast, n, forward);
                if (nextFast == -1) break;
                int nextFast2 = NextIndex(nums, nextFast, n, forward);
                if (nextFast2 == -1) break;

                slow = nextSlow;
                fast = nextFast2;

                if (slow == fast) {
                    // check that the cycle length is greater than 1
                    if (slow != NextIndex(nums, slow, n, forward))
                        return true;
                    else
                        break;
                }
            }

            // Mark all nodes visited in this traversal as 0 to avoid reprocessing
            int j = i;
            while (nums[j] != 0) {
                int next = NextIndex(nums, j, n, forward);
                nums[j] = 0;
                if (next == -1) break;
                j = next;
            }
        }
        return false;
    }

    private int NextIndex(int[] nums, int cur, int n, bool forward) {
        if (nums[cur] == 0) return -1;
        if ((nums[cur] > 0) != forward) return -1;
        int next = ((cur + nums[cur]) % n + n) % n; // ensure non‑negative
        return next;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var circularArrayLoop = function(nums) {
    const n = nums.length;
    const nextIdx = (i) => ((i + nums[i]) % n + n) % n;

    for (let i = 0; i < n; i++) {
        if (nums[i] === 0) continue;
        const dir = nums[i] > 0;
        let slow = i, fast = i;

        while (true) {
            // one step for slow
            let ns = nextIdx(slow);
            if (nums[ns] === 0 || (nums[ns] > 0) !== dir) break;

            // two steps for fast
            let nf1 = nextIdx(fast);
            if (nums[nf1] === 0 || (nums[nf1] > 0) !== dir) break;
            let nf2 = nextIdx(nf1);
            if (nums[nf2] === 0 || (nums[nf2] > 0) !== dir) break;

            slow = ns;
            fast = nf2;

            if (slow === fast) {
                // ensure loop length > 1
                if (slow !== nextIdx(slow)) return true;
                else break;
            }
        }

        // mark visited nodes in this traversal
        let j = i;
        while (nums[j] !== 0 && ((nums[j] > 0) === dir)) {
            const nxt = nextIdx(j);
            nums[j] = 0;
            j = nxt;
        }
    }
    return false;
};
```

## Typescript

```typescript
function circularArrayLoop(nums: number[]): boolean {
    const n = nums.length;
    const mod = (x: number): number => ((x % n) + n) % n;

    const getNext = (idx: number, forward: boolean): number => {
        if ((nums[idx] > 0) !== forward) return -1; // direction mismatch
        const next = mod(idx + nums[idx]);
        if (next === idx) return -1; // self-loop not allowed
        return next;
    };

    for (let i = 0; i < n; i++) {
        if (nums[i] === 0) continue; // already processed

        const forward = nums[i] > 0;
        let slow = i, fast = i;

        while (true) {
            slow = getNext(slow, forward);
            if (slow === -1) break;

            fast = getNext(fast, forward);
            if (fast === -1) break;
            fast = getNext(fast, forward);
            if (fast === -1) break;

            if (slow === fast) return true;
        }

        // Mark all nodes in this traversal as visited
        let j = i;
        while (nums[j] !== 0 && ((nums[j] > 0) === forward)) {
            const next = mod(j + nums[j]);
            nums[j] = 0; // mark as visited
            j = next;
        }
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function circularArrayLoop($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] == 0) continue;
            $direction = $nums[$i] > 0;

            $slow = $i;
            $fast = $i;

            while (true) {
                $nextSlow = $this->nextIdx($slow, $nums, $direction);
                if ($nextSlow === -1) break;

                $nextFast = $this->nextIdx($fast, $nums, $direction);
                if ($nextFast === -1) break;
                $nextFast = $this->nextIdx($nextFast, $nums, $direction);
                if ($nextFast === -1) break;

                $slow = $nextSlow;
                $fast = $nextFast;

                if ($slow == $fast) {
                    // ensure cycle length > 1
                    $nextOfSlow = $this->nextIdx($slow, $nums, $direction);
                    if ($nextOfSlow !== -1 && $nextOfSlow != $slow) {
                        return true;
                    }
                    break;
                }
            }

            // mark all nodes visited in this pass as 0
            $j = $i;
            while (true) {
                if ($nums[$j] == 0) break;
                $currDir = $nums[$j] > 0;
                if ($currDir != $direction) break;
                $next = $this->nextIdxRaw($j, $nums);
                $nums[$j] = 0;
                $j = $next;
            }
        }
        return false;
    }

    private function nextIdx($idx, $nums, $direction) {
        if ($nums[$idx] == 0) return -1;
        $currDir = $nums[$idx] > 0;
        if ($currDir != $direction) return -1;
        $n = count($nums);
        $next = ($idx + $nums[$idx]) % $n;
        if ($next < 0) $next += $n;
        return $next;
    }

    private function nextIdxRaw($idx, $nums) {
        $n = count($nums);
        $next = ($idx + $nums[$idx]) % $n;
        if ($next < 0) $next += $n;
        return $next;
    }
}
```

## Swift

```swift
class Solution {
    func circularArrayLoop(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n == 0 { return false }
        var arr = nums
        
        func nextIndex(_ idx: Int) -> Int {
            let move = arr[idx]
            var nxt = (idx + move) % n
            if nxt < 0 { nxt += n }
            return nxt
        }
        
        for i in 0..<n {
            if arr[i] == 0 { continue }
            var slow = i
            var fast = i
            let direction = arr[i] > 0
            
            while true {
                // move slow one step
                let nextSlow = nextIndex(slow)
                if arr[nextSlow] == 0 || (arr[nextSlow] > 0) != direction { break }
                
                // move fast first step
                var nextFast = nextIndex(fast)
                if arr[nextFast] == 0 || (arr[nextFast] > 0) != direction { break }
                // move fast second step
                nextFast = nextIndex(nextFast)
                if arr[nextFast] == 0 || (arr[nextFast] > 0) != direction { break }
                
                slow = nextSlow
                fast = nextFast
                
                if slow == fast {
                    // check cycle length > 1
                    if slow == nextIndex(slow) {
                        break
                    } else {
                        return true
                    }
                }
            }
            
            // mark all nodes visited in this traversal as 0
            var j = i
            while arr[j] != 0 && ((arr[j] > 0) == direction) {
                let nxt = nextIndex(j)
                arr[j] = 0
                j = nxt
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun circularArrayLoop(nums: IntArray): Boolean {
        val n = nums.size
        fun next(idx: Int): Int {
            var nxt = (idx + nums[idx]) % n
            if (nxt < 0) nxt += n
            return nxt
        }
        fun sameDirection(idx: Int, forward: Boolean): Boolean {
            return nums[idx] != 0 && (nums[idx] > 0) == forward
        }

        for (i in 0 until n) {
            if (nums[i] == 0) continue
            var slow = i
            var fast = i
            val forward = nums[i] > 0

            while (true) {
                // move one step for slow pointer
                val nextSlow = next(slow)
                if (!sameDirection(slow, forward) || !sameDirection(nextSlow, forward) || nextSlow == slow) break

                // move fast pointer first step
                var nextFast = next(fast)
                if (!sameDirection(fast, forward) || !sameDirection(nextFast, forward) || nextFast == fast) break

                // move fast pointer second step
                val nextFast2 = next(nextFast)
                if (!sameDirection(nextFast, forward) || !sameDirection(nextFast2, forward) || nextFast2 == nextFast) break

                slow = nextSlow
                fast = nextFast2

                if (slow == fast) return true
            }

            // mark visited nodes to 0
            var j = i
            while (nums[j] != 0 && sameDirection(j, forward)) {
                val nxt = next(j)
                nums[j] = 0
                if (nxt == j) break
                j = nxt
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool circularArrayLoop(List<int> nums) {
    int n = nums.length;
    int getNext(int idx) {
      return ((idx + nums[idx]) % n + n) % n;
    }

    for (int i = 0; i < n; ++i) {
      if (nums[i] == 0) continue;

      int dir = nums[i] > 0 ? 1 : -1;
      int slow = i, fast = i;

      while (true) {
        // move one step for slow pointer
        int nextSlow = getNext(slow);
        if (dir * nums[slow] <= 0 ||
            dir * nums[nextSlow] <= 0 ||
            nextSlow == slow) break;

        // move two steps for fast pointer
        int nextFast1 = getNext(fast);
        int nextFast2 = getNext(nextFast1);
        if (dir * nums[fast] <= 0 ||
            dir * nums[nextFast1] <= 0 ||
            dir * nums[nextFast2] <= 0 ||
            nextFast1 == fast ||
            nextFast2 == nextFast1) break;

        slow = nextSlow;
        fast = nextFast2;

        if (slow == fast) return true;
      }

      // mark all nodes visited in this component as 0
      int j = i;
      while (nums[j] != 0) {
        int nxt = getNext(j);
        nums[j] = 0;
        if (nxt == j) break;
        j = nxt;
      }
    }

    return false;
  }
}
```

## Golang

```go
func circularArrayLoop(nums []int) bool {
    n := len(nums)
    nextIdx := func(i int) int {
        return ((i + nums[i]) % n + n) % n
    }

    for i := 0; i < n; i++ {
        if nums[i] == 0 {
            continue
        }
        dir := nums[i] > 0

        slow, fast := i, nextIdx(i)

        for nums[fast] != 0 && (nums[fast] > 0) == dir {
            fastNext := nextIdx(fast)
            if nums[fastNext] == 0 || (nums[fastNext] > 0) != dir {
                break
            }

            slow = nextIdx(slow)
            fast = nextIdx(fastNext)

            if slow == fast {
                if slow == nextIdx(slow) {
                    break
                }
                return true
            }
        }

        j := i
        for nums[j] != 0 && (nums[j] > 0) == dir {
            nxt := nextIdx(j)
            nums[j] = 0
            j = nxt
        }
    }
    return false
}
```

## Ruby

```ruby
def circular_array_loop(nums)
  n = nums.length
  get_next = ->(idx) { ((idx + nums[idx]) % n + n) % n }

  (0...n).each do |i|
    next if nums[i] == 0

    direction = nums[i] > 0
    slow = i
    fast = i

    loop do
      nxt_slow = get_next.call(slow)
      break unless (nums[slow] > 0) == direction && (nums[nxt_slow] > 0) == direction && nxt_slow != slow

      nxt_fast1 = get_next.call(fast)
      break unless (nums[fast] > 0) == direction && (nums[nxt_fast1] > 0) == direction && nxt_fast1 != fast

      nxt_fast2 = get_next.call(nxt_fast1)
      break unless (nums[nxt_fast1] > 0) == direction && (nums[nxt_fast2] > 0) == direction && nxt_fast2 != nxt_fast1

      slow = nxt_slow
      fast = nxt_fast2

      return true if slow == fast
    end

    j = i
    while nums[j] != 0 && (nums[j] > 0) == direction
      next_j = get_next.call(j)
      nums[j] = 0
      j = next_j
    end
  end

  false
end
```

## Scala

```scala
object Solution {
  def circularArrayLoop(nums: Array[Int]): Boolean = {
    val n = nums.length
    def next(idx: Int): Int = {
      val move = nums(idx)
      ((idx + move) % n + n) % n
    }

    for (i <- 0 until n) {
      if (nums(i) != 0) {
        var slow = i
        var fast = i
        val dir = nums(i) > 0
        var ok = true

        while (ok) {
          val nextSlow = next(slow)
          if (nums(nextSlow) == 0 || (nums(nextSlow) > 0) != dir) {
            ok = false
          } else {
            var nextFast1 = next(fast)
            if (nums(nextFast1) == 0 || (nums(nextFast1) > 0) != dir) {
              ok = false
            } else {
              var nextFast2 = next(nextFast1)
              if (nums(nextFast2) == 0 || (nums(nextFast2) > 0) != dir) {
                ok = false
              } else {
                slow = nextSlow
                fast = nextFast2
                if (slow == fast) {
                  if (slow != next(slow)) return true
                  else ok = false
                }
              }
            }
          }
        }

        var cur = i
        while (nums(cur) != 0) {
          val nxt = next(cur)
          nums(cur) = 0
          cur = nxt
        }
      }
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn circular_array_loop(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n == 0 {
            return false;
        }
        let mut nums = nums;

        // helper to compute next index in a circular manner
        let next_idx = |idx: usize, arr: &Vec<i32>| -> usize {
            let len = arr.len() as i32;
            ((idx as i32 + arr[idx]) % len + len) % len as usize
        };

        for i in 0..n {
            if nums[i] == 0 {
                continue;
            }
            let direction = nums[i] > 0;
            let mut slow = i;
            let mut fast = i;

            loop {
                // move one step for slow pointer
                let next_slow = next_idx(slow, &nums);
                if nums[next_slow] == 0
                    || (nums[next_slow] > 0) != direction
                    || next_slow == slow
                {
                    break;
                }

                // first step for fast pointer
                let next_fast1 = next_idx(fast, &nums);
                if nums[next_fast1] == 0
                    || (nums[next_fast1] > 0) != direction
                    || next_fast1 == fast
                {
                    break;
                }

                // second step for fast pointer
                let next_fast2 = next_idx(next_fast1, &nums);
                if nums[next_fast2] == 0
                    || (nums[next_fast2] > 0) != direction
                    || next_fast2 == next_fast1
                {
                    break;
                }

                slow = next_slow;
                fast = next_fast2;

                if slow == fast {
                    return true;
                }
            }

            // mark all nodes visited in this traversal as 0 to avoid reprocessing
            let mut j = i;
            while nums[j] != 0 {
                let nxt = next_idx(j, &nums);
                nums[j] = 0;
                j = nxt;
            }
        }

        false
    }
}
```

## Racket

```racket
(define/contract (circular-array-loop nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (define (next-index i)
      (modulo (+ i (vector-ref v i)) n))
    (define (same-direction? val dir) ; dir #t for positive
      (if dir (> val 0) (< val 0)))
    (let outer-loop ((i 0))
      (cond
        [(>= i n) #f]                                   ; finished, no cycle
        [(zero? (vector-ref v i)) (outer-loop (+ i 1))] ; already processed
        [else
         (define dir (> (vector-ref v i) 0))           ; direction of start
         ;; Floyd's Tortoise and Hare
         (let ((slow i) (fast i))
           (let find-cycle ()
             (define ns (next-index slow))
             (if (or (zero? (vector-ref v ns))
                     (not (same-direction? (vector-ref v ns) dir)))
                 #f
                 (let ((nf1 (next-index fast)))
                   (if (or (zero? (vector-ref v nf1))
                           (not (same-direction? (vector-ref v nf1) dir)))
                       #f
                       (let ((nf (next-index nf1)))
                         (if (or (zero? (vector-ref v nf))
                                 (not (same-direction? (vector-ref v nf) dir)))
                             #f
                             (begin
                               (set! slow ns)
                               (set! fast nf)
                               (if (= slow fast)
                                   (if (= slow (next-index slow)) ; single‑element loop
                                       #f
                                       #t)
                                   (find-cycle))))))))))
           (if (find-cycle)
               #t
               ;; mark all nodes visited from i as 0
               (let walk ((j i))
                 (when (and (not (zero? (vector-ref v j)))
                            (same-direction? (vector-ref v j) dir))
                   (define nxt (next-index j))
                   (vector-set! v j 0)
                   (walk nxt)))
               (outer-loop (+ i 1))))]))))
```

## Erlang

```erlang
-module(solution).
-export([circular_array_loop/1]).

-spec circular_array_loop(Nums :: [integer()]) -> boolean().
circular_array_loop(Nums) ->
    N = length(Nums),
    Table = ets:new(nums, [named_table, public]),
    lists:foldl(
      fun({Val, Idx}, _) ->
              ets:insert(Table, {Idx, Val})
          end,
      ok,
      lists:zip(Nums, lists:seq(0, N - 1))
    ),
    Result = check_all(0, N, Table),
    ets:delete(Table),
    Result.

%% iterate over all start indices
check_all(I, N, _Table) when I >= N ->
    false;
check_all(I, N, Table) ->
    case ets:lookup(Table, I) of
        [] -> check_all(I + 1, N, Table);
        [{I, 0}] -> check_all(I + 1, N, Table);
        [{I, V}] ->
            Dir = sign(V),
            case has_cycle(I, N, Table, Dir) of
                true -> true;
                false ->
                    mark_visited(I, N, Table, Dir),
                    check_all(I + 1, N, Table)
            end
    end.

%% Floyd's cycle detection respecting direction
has_cycle(Start, N, Table, Dir) ->
    has_cycle_loop(Start, Start, N, Table, Dir).

has_cycle_loop(Slow, Fast, N, Table, Dir) ->
    case move(Slow, N, Table, Dir) of
        -1 -> false;
        NewSlow ->
            case move(Fast, N, Table, Dir) of
                -1 -> false;
                TempFast ->
                    case move(TempFast, N, Table, Dir) of
                        -1 -> false;
                        NewFast ->
                            if NewSlow =:= NewFast ->
                                    % ensure cycle length > 1
                                    case move(NewSlow, N, Table, Dir) of
                                        -1 -> false;
                                        Next when Next =/= NewSlow -> true;
                                        _ -> false
                                    end;
                               true ->
                                    has_cycle_loop(NewSlow, NewFast, N, Table, Dir)
                            end
                    end
            end
    end.

%% mark all nodes visited in this component as 0
mark_visited(Index, N, Table, Dir) ->
    mark_visited_loop(Index, N, Table, Dir).

mark_visited_loop(Cur, N, Table, Dir) ->
    case ets:lookup(Table, Cur) of
        [] -> ok;
        [{Cur, 0}] -> ok;
        [{Cur, V}] ->
            if sign(V) =/= Dir ->
                    ok;
               true ->
                    Next = ((Cur + V) rem N + N) rem N,
                    ets:insert(Table, {Cur, 0}),
                    if Next =:= Cur -> ok; % self‑loop, stop
                       true -> mark_visited_loop(Next, N, Table, Dir)
                    end
            end
    end.

%% compute next index respecting direction, return -1 on invalid move
move(Index, N, Table, Dir) ->
    case ets:lookup(Table, Index) of
        [] -> -1;
        [{Index, 0}] -> -1;
        [{Index, V}] ->
            if sign(V) =/= Dir -> -1;
               true ->
                    ((Index + V) rem N + N) rem N
            end
    end.

sign(V) when V > 0 -> 1;
sign(_V) -> -1.
```

## Elixir

```elixir
defmodule Solution do
  @spec circular_array_loop(nums :: [integer]) :: boolean
  def circular_array_loop(nums) do
    n = length(nums)
    nums_t = List.to_tuple(nums)

    result =
      Enum.reduce_while(0..n - 1, MapSet.new(), fn i, visited ->
        if MapSet.member?(visited, i) do
          {:cont, visited}
        else
          dir = sign(elem(nums_t, i))

          if detect_cycle(i, i, nums_t, n, dir) do
            {:halt, true}
          else
            new_visited = mark_path(i, nums_t, n, visited)
            {:cont, new_visited}
          end
        end
      end)

    case result do
      true -> true
      _ -> false
    end
  end

  defp detect_cycle(slow, fast, nums_t, n, dir) do
    next_slow = next_index(nums_t, n, slow)

    if sign(elem(nums_t, next_slow)) != dir do
      false
    else
      next_fast1 = next_index(nums_t, n, fast)

      if sign(elem(nums_t, next_fast1)) != dir do
        false
      else
        next_fast2 = next_index(nums_t, n, next_fast1)

        if sign(elem(nums_t, next_fast2)) != dir do
          false
        else
          if next_slow == next_fast2 do
            # ensure cycle length > 1
            if next_slow != next_index(nums_t, n, next_slow) do
              true
            else
              false
            end
          else
            detect_cycle(next_slow, next_fast2, nums_t, n, dir)
          end
        end
      end
    end
  end

  defp mark_path(start_idx, nums_t, n, visited) do
    dir = sign(elem(nums_t, start_idx))

    Stream.iterate(start_idx, fn idx -> next_index(nums_t, n, idx) end)
    |> Enum.reduce_while(visited, fn idx, acc ->
      if MapSet.member?(acc, idx) or sign(elem(nums_t, idx)) != dir do
        {:halt, acc}
      else
        {:cont, MapSet.put(acc, idx)}
      end
    end)
  end

  defp next_index(nums_t, n, idx) do
    step = elem(nums_t, idx)
    nxt = rem(idx + step, n)

    if nxt < 0, do: nxt + n, else: nxt
  end

  defp sign(x) when x > 0, do: 1
  defp sign(_), do: -1
end
```
