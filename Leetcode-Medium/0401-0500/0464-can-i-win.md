# 0464. Can I Win

## Cpp

```cpp
#include <unordered_map>
#include <functional>

class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) return true;
        int totalSum = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
        if (totalSum < desiredTotal) return false;

        std::unordered_map<int, bool> memo;
        std::function<bool(int, int)> dfs = [&](int usedMask, int remain) -> bool {
            if (memo.count(usedMask)) return memo[usedMask];
            for (int i = 1; i <= maxChoosableInteger; ++i) {
                int bit = 1 << (i - 1);
                if ((usedMask & bit) == 0) {
                    if (i >= remain) {
                        return memo[usedMask] = true;
                    }
                    if (!dfs(usedMask | bit, remain - i)) {
                        return memo[usedMask] = true;
                    }
                }
            }
            return memo[usedMask] = false;
        };

        return dfs(0, desiredTotal);
    }
};
```

## Java

```java
class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) return true;
        long totalSum = (long) maxChoosableInteger * (maxChoosableInteger + 1) / 2;
        if (totalSum < desiredTotal) return false;

        Map<Integer, Boolean> memo = new HashMap<>();
        return canWin(0, desiredTotal, maxChoosableInteger, memo);
    }

    private boolean canWin(int usedMask, int needed, int max, Map<Integer, Boolean> memo) {
        if (memo.containsKey(usedMask)) {
            return memo.get(usedMask);
        }
        for (int i = 1; i <= max; i++) {
            int bit = 1 << (i - 1);
            if ((usedMask & bit) != 0) continue;
            if (i >= needed) {
                memo.put(usedMask, true);
                return true;
            }
            // opponent's turn
            if (!canWin(usedMask | bit, needed - i, max, memo)) {
                memo.put(usedMask, true);
                return true;
            }
        }
        memo.put(usedMask, false);
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= 0:
            return True
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False

        memo = {}

        def dfs(mask, remaining):
            if mask in memo:
                return memo[mask]
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if not (mask & bit):
                    # If picking i reaches or exceeds the target, current player wins
                    if i >= remaining:
                        memo[mask] = True
                        return True
                    # Otherwise, see if opponent loses after this move
                    if not dfs(mask | bit, remaining - i):
                        memo[mask] = True
                        return True
            memo[mask] = False
            return False

        return dfs(0, desiredTotal)
```

## Python3

```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Trivial cases
        if desiredTotal <= 0:
            return True
        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if total_sum < desiredTotal:
            return False

        from functools import lru_cache

        @lru_cache(None)
        def can_win(used_mask: int, remaining: int) -> bool:
            # Try every possible choice
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if used_mask & bit:
                    continue
                # If picking i reaches or exceeds the needed total, current player wins
                if i >= remaining:
                    return True
                # Otherwise, opponent's turn; if opponent cannot win, we win
                if not can_win(used_mask | bit, remaining - i):
                    return True
            return False

        return can_win(0, desiredTotal)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int g_max;
static int g_target;
static char *g_memo;      // -1 = unknown, 0 = false, 1 = true
static int *g_sumMask;

static bool canWin(int mask) {
    if (g_memo[mask] != -1) return g_memo[mask];
    int remaining = g_target - g_sumMask[mask];
    for (int i = 0; i < g_max; ++i) {
        if (!(mask & (1 << i))) {
            if (i + 1 >= remaining) {
                g_memo[mask] = 1;
                return true;
            }
            int nextMask = mask | (1 << i);
            if (!canWin(nextMask)) {
                g_memo[mask] = 1;
                return true;
            }
        }
    }
    g_memo[mask] = 0;
    return false;
}

bool canIWin(int maxChoosableInteger, int desiredTotal) {
    if (desiredTotal <= 0) return true;
    int totalSum = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
    if (totalSum < desiredTotal) return false;

    g_max = maxChoosableInteger;
    g_target = desiredTotal;

    int states = 1 << maxChoosableInteger;
    g_sumMask = (int *)malloc(states * sizeof(int));
    g_memo = (char *)malloc(states);
    if (!g_sumMask || !g_memo) return false; // allocation failure fallback

    g_sumMask[0] = 0;
    for (int mask = 1; mask < states; ++mask) {
        int lowbit = mask & -mask;
        int idx = __builtin_ctz(lowbit);   // index of the chosen number (0‑based)
        g_sumMask[mask] = g_sumMask[mask ^ lowbit] + (idx + 1);
    }
    memset(g_memo, -1, states);

    bool result = canWin(0);

    free(g_sumMask);
    free(g_memo);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private int max;
    private int target;
    private Dictionary<int, bool> memo;

    public bool CanIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) return true;
        int sum = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
        if (sum < desiredTotal) return false;

        this.max = maxChoosableInteger;
        this.target = desiredTotal;
        memo = new Dictionary<int, bool>();
        return CanWin(0, 0);
    }

    private bool CanWin(int usedMask, int currentTotal) {
        if (memo.TryGetValue(usedMask, out bool cached)) return cached;

        for (int i = 1; i <= max; i++) {
            int bit = 1 << (i - 1);
            if ((usedMask & bit) == 0) {
                if (currentTotal + i >= target) {
                    memo[usedMask] = true;
                    return true;
                }
                if (!CanWin(usedMask | bit, currentTotal + i)) {
                    memo[usedMask] = true;
                    return true;
                }
            }
        }

        memo[usedMask] = false;
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} maxChoosableInteger
 * @param {number} desiredTotal
 * @return {boolean}
 */
var canIWin = function(maxChoosableInteger, desiredTotal) {
    if (desiredTotal <= 0) return true;
    const sumAll = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2;
    if (sumAll < desiredTotal) return false;

    const memo = new Map();

    function dfs(mask, remaining) {
        if (memo.has(mask)) return memo.get(mask);
        for (let i = 1; i <= maxChoosableInteger; i++) {
            const bit = 1 << (i - 1);
            if ((mask & bit) === 0) {
                // picking i reaches or exceeds the needed total -> win
                if (i >= remaining) {
                    memo.set(mask, true);
                    return true;
                }
                // otherwise, see if opponent loses after this move
                if (!dfs(mask | bit, remaining - i)) {
                    memo.set(mask, true);
                    return true;
                }
            }
        }
        memo.set(mask, false);
        return false;
    }

    return dfs(0, desiredTotal);
};
```

## Typescript

```typescript
function canIWin(maxChoosableInteger: number, desiredTotal: number): boolean {
    if (desiredTotal <= 0) return true;
    const maxSum = (maxChoosableInteger * (maxChoosableInteger + 1)) >> 1;
    if (maxSum < desiredTotal) return false;

    const memo = new Map<number, boolean>();

    function dfs(usedMask: number, remaining: number): boolean {
        if (memo.has(usedMask)) return memo.get(usedMask)!;
        for (let i = 1; i <= maxChoosableInteger; i++) {
            const bit = 1 << (i - 1);
            if ((usedMask & bit) !== 0) continue;
            if (i >= remaining) {
                memo.set(usedMask, true);
                return true;
            }
            if (!dfs(usedMask | bit, remaining - i)) {
                memo.set(usedMask, true);
                return true;
            }
        }
        memo.set(usedMask, false);
        return false;
    }

    return dfs(0, desiredTotal);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $maxChoosableInteger
     * @param Integer $desiredTotal
     * @return Boolean
     */
    function canIWin($maxChoosableInteger, $desiredTotal) {
        if ($desiredTotal <= 0) {
            return true;
        }
        $totalSum = $maxChoosableInteger * ($maxChoosableInteger + 1) / 2;
        if ($totalSum < $desiredTotal) {
            return false;
        }

        $this->max = $maxChoosableInteger;
        $this->memo = [];

        return $this->dfs(0, $desiredTotal);
    }

    private function dfs($usedMask, $remaining) {
        if (isset($this->memo[$usedMask])) {
            return $this->memo[$usedMask];
        }

        for ($i = 1; $i <= $this->max; $i++) {
            $bit = 1 << ($i - 1);
            if (($usedMask & $bit) === 0) { // number i not used yet
                if ($i >= $remaining) {
                    $this->memo[$usedMask] = true;
                    return true;
                }
                $nextMask = $usedMask | $bit;
                // If the opponent cannot win from the next state, current player wins
                if (!$this->dfs($nextMask, $remaining - $i)) {
                    $this->memo[$usedMask] = true;
                    return true;
                }
            }
        }

        $this->memo[$usedMask] = false;
        return false;
    }
}
```

## Swift

```swift
class Solution {
    private var memo = [Int: Bool]()
    private var maxChoosable = 0
    private var target = 0

    func canIWin(_ maxChoosableInteger: Int, _ desiredTotal: Int) -> Bool {
        if desiredTotal <= 0 { return true }
        let totalSum = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2
        if totalSum < desiredTotal { return false }

        maxChoosable = maxChoosableInteger
        target = desiredTotal
        memo.removeAll()
        return canWin(0, target)
    }

    private func canWin(_ usedMask: Int, _ remaining: Int) -> Bool {
        if let cached = memo[usedMask] { return cached }
        for i in 1...maxChoosable {
            let bit = 1 << (i - 1)
            if (usedMask & bit) == 0 {
                if i >= remaining {
                    memo[usedMask] = true
                    return true
                }
                let nextMask = usedMask | bit
                if !canWin(nextMask, remaining - i) {
                    memo[usedMask] = true
                    return true
                }
            }
        }
        memo[usedMask] = false
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val memo = HashMap<Int, Boolean>()
    private var maxChoosableInteger = 0

    fun canIWin(maxChoosableInteger: Int, desiredTotal: Int): Boolean {
        this.maxChoosableInteger = maxChoosableInteger
        if (desiredTotal <= 0) return true
        val sumAll = maxChoosableInteger * (maxChoosableInteger + 1) / 2
        if (sumAll < desiredTotal) return false
        memo.clear()
        return canWin(0, desiredTotal)
    }

    private fun canWin(mask: Int, remaining: Int): Boolean {
        memo[mask]?.let { return it }
        for (i in 1..maxChoosableInteger) {
            val bit = 1 shl (i - 1)
            if ((mask and bit) == 0) {
                if (i >= remaining) {
                    memo[mask] = true
                    return true
                }
                val nextMask = mask or bit
                if (!canWin(nextMask, remaining - i)) {
                    memo[mask] = true
                    return true
                }
            }
        }
        memo[mask] = false
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool canIWin(int maxChoosableInteger, int desiredTotal) {
    if (desiredTotal <= 0) return true;
    int totalSum = maxChoosableInteger * (maxChoosableInteger + 1) ~/ 2;
    if (totalSum < desiredTotal) return false;

    final Map<int, bool> memo = {};

    bool dfs(int usedMask, int curTotal) {
      if (memo.containsKey(usedMask)) return memo[usedMask]!;
      for (int i = 1; i <= maxChoosableInteger; ++i) {
        int bit = 1 << (i - 1);
        if ((usedMask & bit) == 0) {
          if (curTotal + i >= desiredTotal) {
            memo[usedMask] = true;
            return true;
          }
          if (!dfs(usedMask | bit, curTotal + i)) {
            memo[usedMask] = true;
            return true;
          }
        }
      }
      memo[usedMask] = false;
      return false;
    }

    return dfs(0, 0);
  }
}
```

## Golang

```go
func canIWin(maxChoosableInteger int, desiredTotal int) bool {
	if desiredTotal <= 0 {
		return true
	}
	sum := maxChoosableInteger * (maxChoosableInteger + 1) / 2
	if sum < desiredTotal {
		return false
	}

	memo := make(map[int]bool)

	var dfs func(mask, total int) bool
	dfs = func(mask, total int) bool {
		if v, ok := memo[mask]; ok {
			return v
		}
		for i := 1; i <= maxChoosableInteger; i++ {
			bit := 1 << (i - 1)
			if mask&bit != 0 {
				continue
			}
			if total+i >= desiredTotal {
				memo[mask] = true
				return true
			}
			if !dfs(mask|bit, total+i) {
				memo[mask] = true
				return true
			}
		}
		memo[mask] = false
		return false
	}

	return dfs(0, 0)
}
```

## Ruby

```ruby
def can_i_win(max_choosable_integer, desired_total)
  total_sum = max_choosable_integer * (max_choosable_integer + 1) / 2
  return false if total_sum < desired_total
  return true if desired_total <= 0

  memo = {}
  max = max_choosable_integer
  target = desired_total

  dfs = nil
  dfs = ->(mask, cur_total) {
    return memo[mask] if memo.key?(mask)

    (1..max).each do |i|
      bit = 1 << (i - 1)
      next if (mask & bit) != 0

      # Immediate win
      if cur_total + i >= target
        memo[mask] = true
        return true
      end

      # Opponent cannot win => current wins
      unless dfs.call(mask | bit, cur_total + i)
        memo[mask] = true
        return true
      end
    end

    memo[mask] = false
    false
  }

  dfs.call(0, 0)
end
```

## Scala

```scala
object Solution {
    def canIWin(maxChoosableInteger: Int, desiredTotal: Int): Boolean = {
        if (desiredTotal <= 0) return true
        val totalSum = maxChoosableInteger * (maxChoosableInteger + 1) / 2
        if (totalSum < desiredTotal) return false

        import scala.collection.mutable
        val memo = mutable.Map[Int, Boolean]()

        def canWin(mask: Int, current: Int): Boolean = {
            memo.get(mask) match {
                case Some(res) => res
                case None =>
                    var i = 1
                    while (i <= maxChoosableInteger) {
                        val bit = 1 << (i - 1)
                        if ((mask & bit) == 0) {
                            // If picking i reaches or exceeds desiredTotal, current player wins.
                            // Otherwise, opponent must lose for current player to win.
                            if (current + i >= desiredTotal || !canWin(mask | bit, current + i)) {
                                memo(mask) = true
                                return true
                            }
                        }
                        i += 1
                    }
                    memo(mask) = false
                    false
            }
        }

        canWin(0, 0)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn can_i_win(max_choosable_integer: i32, desired_total: i32) -> bool {
        if desired_total <= 0 {
            return true;
        }
        let max = max_choosable_integer as usize;
        let total_sum = (max * (max + 1)) / 2;
        if total_sum < desired_total as usize {
            return false;
        }

        fn dfs(
            mask: u32,
            remaining: i32,
            max: usize,
            memo: &mut HashMap<u32, bool>,
        ) -> bool {
            if let Some(&res) = memo.get(&mask) {
                return res;
            }
            for i in 0..max {
                let bit = 1u32 << i;
                if mask & bit == 0 {
                    let pick = (i as i32) + 1;
                    // If picking this number reaches or exceeds the needed total, win immediately.
                    if pick >= remaining {
                        memo.insert(mask, true);
                        return true;
                    }
                    // Otherwise, see if opponent can be forced to lose.
                    if !dfs(mask | bit, remaining - pick, max, memo) {
                        memo.insert(mask, true);
                        return true;
                    }
                }
            }
            memo.insert(mask, false);
            false
        }

        let mut memo = HashMap::new();
        dfs(0, desired_total, max, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (can-i-win maxChoosableInteger desiredTotal)
  (-> exact-integer? exact-integer? boolean?)
  (cond
    [(<= desiredTotal 0) #t]
    [(>= maxChoosableInteger desiredTotal) #t]
    [(< (/ (* (+ maxChoosableInteger 1) maxChoosableInteger) 2) desiredTotal) #f]
    [else
     (let ((memo (make-hash)))
       (define (mask-sum mask)
         (let loop ((i 1) (sum 0))
           (if (> i maxChoosableInteger)
               sum
               (loop (+ i 1)
                     (if (zero? (bitwise-and mask (arithmetic-shift 1 (- i 1))))
                         sum
                         (+ sum i))))))
       (define (win? mask)
         (hash-ref memo mask
           (lambda ()
             (let ((remaining (- desiredTotal (mask-sum mask))))
               (if (<= remaining 0)
                   #t
                   (let loop ((i 1))
                     (cond
                       [(> i maxChoosableInteger)
                        (hash-set! memo mask #f)
                        #f]
                       [else
                        (if (zero? (bitwise-and mask (arithmetic-shift 1 (- i 1))))
                            (if (>= i remaining)
                                (begin (hash-set! memo mask #t) #t)
                                (let ((next-mask (bitwise-ior mask (arithmetic-shift 1 (- i 1)))))
                                  (if (not (win? next-mask))
                                      (begin (hash-set! memo mask #t) #t)
                                      (loop (+ i 1)))))
                            (loop (+ i 1)))])))))))
       (win? 0))]))
```

## Erlang

```erlang
-module(solution).
-export([can_i_win/2]).

-spec can_i_win(integer(), integer()) -> boolean().
can_i_win(MaxChoosableInteger, DesiredTotal) ->
    TotalSum = MaxChoosableInteger * (MaxChoosableInteger + 1) div 2,
    case DesiredTotal of
        D when D =< 0 -> true;
        _ ->
            if
                TotalSum < DesiredTotal -> false;
                true ->
                    {Res, _} = win(0, #{}, MaxChoosableInteger, DesiredTotal),
                    Res
            end
    end.

win(Mask, Memo, Max, Target) ->
    case maps:is_key(Mask, Memo) of
        true ->
            {maps:get(Mask, Memo), Memo};
        false ->
            UsedSum = sum_used(Mask, Max),
            Remain = Target - UsedSum,
            {Res, NewMemo} = win_loop(1, Max, Mask, Remain, Memo, Max, Target),
            UpdatedMemo = maps:put(Mask, Res, NewMemo),
            {Res, UpdatedMemo}
    end.

win_loop(I, Max, _Mask, _Remain, Memo, _MaxOrig, _Target) when I > Max ->
    {false, Memo};
win_loop(I, Max, Mask, Remain, Memo, MaxOrig, Target) ->
    Bit = 1 bsl (I - 1),
    case Mask band Bit of
        0 ->
            if I >= Remain ->
                {true, Memo};
               true ->
                    NewMask = Mask bor Bit,
                    {OppRes, Memo2} = win(NewMask, Memo, MaxOrig, Target),
                    if not OppRes ->
                        {true, Memo2};
                       true ->
                        win_loop(I + 1, Max, Mask, Remain, Memo2, MaxOrig, Target)
                    end
            end;
        _ ->
            win_loop(I + 1, Max, Mask, Remain, Memo, MaxOrig, Target)
    end.

sum_used(Mask, Max) -> sum_used(Mask, Max, 1, 0).

sum_used(_Mask, Max, I, Acc) when I > Max -> Acc;
sum_used(Mask, Max, I, Acc) ->
    Bit = 1 bsl (I - 1),
    NewAcc = case Mask band Bit of
                0 -> Acc;
                _ -> Acc + I
            end,
    sum_used(Mask, Max, I + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_i_win(max_choosable_integer :: integer, desired_total :: integer) :: boolean
  def can_i_win(max_choosable_integer, desired_total) do
    if desired_total <= 0 do
      true
    else
      total_sum = div(max_choosable_integer * (max_choosable_integer + 1), 2)

      if total_sum < desired_total do
        false
      else
        tid = :ets.new(:can_i_win_memo, [:set, :private])
        result = dfs(0, desired_total, max_choosable_integer, tid)
        :ets.delete(tid)
        result
      end
    end
  end

  import Bitwise

  defp dfs(mask, remaining, max_int, tid) do
    case :ets.lookup(tid, mask) do
      [{^mask, res}] -> res
      [] ->
        win =
          Enum.any?(1..max_int, fn i ->
            bit = 1 <<< (i - 1)

            if (mask &&& bit) != 0 do
              false
            else
              if i >= remaining do
                true
              else
                not dfs(mask ||| bit, remaining - i, max_int, tid)
              end
            end
          end)

        :ets.insert(tid, {mask, win})
        win
    end
  end
end
```
