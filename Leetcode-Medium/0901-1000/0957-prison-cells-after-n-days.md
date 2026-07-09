# 0957. Prison Cells After N Days

## Cpp

```cpp
class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int n) {
        auto vecToStr = [&](const vector<int>& v) {
            string s(8, '0');
            for (int i = 0; i < 8; ++i) s[i] = char(v[i] + '0');
            return s;
        };
        
        unordered_map<string, int> seen;
        vector<vector<int>> states;
        vector<int> cur = cells;
        
        while (n > 0) {
            string key = vecToStr(cur);
            if (seen.count(key)) {
                int cycle_start = seen[key];
                int cycle_len = (int)states.size() - cycle_start;
                n %= cycle_len;
                return states[cycle_start + n];
            }
            seen[key] = (int)states.size();
            states.push_back(cur);
            
            vector<int> nxt(8, 0);
            for (int i = 1; i < 7; ++i) {
                nxt[i] = (cur[i - 1] == cur[i + 1]) ? 0 : 1;
            }
            cur.swap(nxt);
            --n;
        }
        return cur;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] prisonAfterNDays(int[] cells, int n) {
        Map<String, Integer> seen = new HashMap<>();
        int day = 0;
        while (n > 0) {
            String key = Arrays.toString(cells);
            if (seen.containsKey(key)) {
                int cycleLen = day - seen.get(key);
                n %= cycleLen;
                seen.clear();
            } else {
                seen.put(key, day);
                cells = nextDay(cells);
                n--;
                day++;
            }
        }
        return cells;
    }

    private int[] nextDay(int[] cells) {
        int[] next = new int[8];
        for (int i = 1; i < 7; i++) {
            next[i] = cells[i - 1] == cells[i + 1] ? 1 : 0;
        }
        return next;
    }
}
```

## Python

```python
class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        def next_day(cur):
            nxt = [0] * 8
            for i in range(1, 7):
                nxt[i] = 1 if cur[i - 1] == cur[i + 1] else 0
            return nxt

        seen = {}
        states = []
        while n > 0:
            key = tuple(cells)
            if key in seen:
                cycle_start = seen[key]
                cycle_len = len(states) - cycle_start
                n %= cycle_len
                return states[cycle_start + n]
            seen[key] = len(states)
            states.append(list(cells))
            cells = next_day(cells)
            n -= 1
        return cells
```

## Python3

```python
from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n > 0:
            state = tuple(cells)
            if state in seen:
                cycle_len = seen[state] - n
                n %= cycle_len
            else:
                seen[state] = n
            if n == 0:
                break
            new_cells = [0] * 8
            for i in range(1, 7):
                new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = new_cells
            n -= 1
        return cells
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* prisonAfterNDays(int* cells, int cellsSize, int n, int* returnSize) {
    // Encode an 8‑cell state into an integer (0..255)
    auto encode = [](int arr[8]) -> int {
        int code = 0;
        for (int i = 0; i < 8; ++i) {
            code = (code << 1) | (arr[i] & 1);
        }
        return code;
    };
    // Decode an integer back into an array of 8 ints
    auto decode = [](int code, int arr[8]) -> void {
        for (int i = 7; i >= 0; --i) {
            arr[i] = code & 1;
            code >>= 1;
        }
    };
    
    int curEncode = 0;
    for (int i = 0; i < 8; ++i) {
        curEncode = (curEncode << 1) | (cells[i] & 1);
    }

    int seen[256];
    for (int i = 0; i < 256; ++i) seen[i] = -1;
    int day = 0;

    while (n > 0) {
        if (seen[curEncode] != -1) {                 // cycle detected
            int cycle_len = day - seen[curEncode];
            n %= cycle_len;
            if (n == 0) break;                       // current state is the answer
            for (int i = 0; i < 256; ++i) seen[i] = -1; // reset to avoid re‑detecting
        } else {
            seen[curEncode] = day;
        }

        int cur[8];
        decode(curEncode, cur);
        int nxt[8];
        nxt[0] = 0;
        nxt[7] = 0;
        for (int i = 1; i < 7; ++i) {
            nxt[i] = (cur[i - 1] == cur[i + 1]) ? 1 : 0;
        }
        curEncode = encode(nxt);
        ++day;
        --n;
    }

    int *result = (int*)malloc(8 * sizeof(int));
    decode(curEncode, result);
    *returnSize = 8;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] PrisonAfterNDays(int[] cells, int n) {
        var seen = new Dictionary<int, int>();
        int day = 0;
        while (n > 0) {
            int mask = ToMask(cells);
            if (seen.TryGetValue(mask, out int prevDay)) {
                int cycleLen = day - prevDay;
                n %= cycleLen;
                if (n == 0) break;
            } else {
                seen[mask] = day;
            }
            cells = NextDay(cells);
            n--;
            day++;
        }
        return cells;
    }

    private int ToMask(int[] arr) {
        int mask = 0;
        for (int i = 0; i < 8; i++) {
            mask <<= 1;
            mask |= arr[i];
        }
        return mask;
    }

    private int[] NextDay(int[] cells) {
        int[] next = new int[8];
        for (int i = 1; i < 7; i++) {
            next[i] = cells[i - 1] == cells[i + 1] ? 1 : 0;
        }
        return next;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cells
 * @param {number} n
 * @return {number[]}
 */
var prisonAfterNDays = function(cells, n) {
    const nextDay = (c) => {
        const nxt = new Array(8).fill(0);
        for (let i = 1; i < 7; i++) {
            nxt[i] = c[i - 1] === c[i + 1] ? 1 : 0;
        }
        return nxt;
    };
    
    const seen = new Map();
    let day = 0;
    while (n > 0) {
        const key = cells.join('');
        if (seen.has(key)) {
            const cycleLen = day - seen.get(key);
            n %= cycleLen;
            if (n === 0) break;
        } else {
            seen.set(key, day);
        }
        cells = nextDay(cells);
        day++;
        n--;
    }
    return cells;
};
```

## Typescript

```typescript
function prisonAfterNDays(cells: number[], n: number): number[] {
    const nextDay = (cur: number[]): number[] => {
        const nxt = new Array(8).fill(0);
        for (let i = 1; i < 7; i++) {
            nxt[i] = cur[i - 1] === cur[i + 1] ? 1 : 0;
        }
        return nxt;
    };

    const seen = new Map<string, number>();
    const states: number[][] = [];

    while (n > 0) {
        const key = cells.join('');
        if (seen.has(key)) {
            const cycleStart = seen.get(key)!;
            const cycleLen = states.length - cycleStart;
            const remaining = n % cycleLen;
            return states[cycleStart + remaining];
        }
        seen.set(key, states.length);
        states.push(cells.slice());

        cells = nextDay(cells);
        n--;
    }

    return cells;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $cells
     * @param Integer $n
     * @return Integer[]
     */
    function prisonAfterNDays($cells, $n) {
        $seen = [];
        $day = 0;
        while ($n > 0) {
            $key = implode('', $cells);
            if (isset($seen[$key])) {
                $cycleLen = $day - $seen[$key];
                $n %= $cycleLen;
                $seen = [];
                if ($n == 0) break;
            }
            $seen[$key] = $day;
            $cells = $this->nextDay($cells);
            $n--;
            $day++;
        }
        return $cells;
    }

    private function nextDay($cells) {
        $new = array_fill(0, 8, 0);
        for ($i = 1; $i < 7; $i++) {
            $new[$i] = ($cells[$i - 1] == $cells[$i + 1]) ? 1 : 0;
        }
        return $new;
    }
}
```

## Swift

```swift
class Solution {
    func prisonAfterNDays(_ cells: [Int], _ n: Int) -> [Int] {
        var cur = cells
        var day = 0
        var seen = [Int:Int]()
        let totalDays = n
        
        while day < totalDays {
            let key = mask(cur)
            if let prevDay = seen[key] {
                let cycleLen = day - prevDay
                let remaining = (totalDays - day) % cycleLen
                for _ in 0..<remaining {
                    cur = nextState(cur)
                }
                return cur
            } else {
                seen[key] = day
                cur = nextState(cur)
                day += 1
            }
        }
        return cur
    }
    
    private func mask(_ cells: [Int]) -> Int {
        var m = 0
        for c in cells {
            m = (m << 1) | c
        }
        return m
    }
    
    private func nextState(_ cells: [Int]) -> [Int] {
        var newCells = Array(repeating: 0, count: 8)
        for i in 1..<7 {
            newCells[i] = (cells[i - 1] == cells[i + 1]) ? 1 : 0
        }
        return newCells
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun prisonAfterNDays(cells: IntArray, n: Int): IntArray {
        var cur = cells.clone()
        val seen = HashMap<String, Int>()
        val states = mutableListOf<IntArray>()
        var day = 0
        while (day < n) {
            val next = nextDay(cur)
            day++
            val key = next.joinToString("")
            if (seen.containsKey(key)) {
                val cycleStart = seen[key]!!          // first day this state appeared
                val cycleLen = day - cycleStart       // length of the cycle
                val remaining = (n - cycleStart) % cycleLen
                val targetDay = cycleStart + remaining
                return states[targetDay - 1]
            }
            seen[key] = day
            states.add(next)
            cur = next
        }
        return cur
    }

    private fun nextDay(cells: IntArray): IntArray {
        val nxt = IntArray(8)
        for (i in 1 until 7) {
            nxt[i] = if (cells[i - 1] == cells[i + 1]) 1 else 0
        }
        return nxt
    }
}
```

## Dart

```dart
class Solution {
  List<int> prisonAfterNDays(List<int> cells, int n) {
    final Map<int, int> seen = {};
    while (n > 0) {
      final int state = _encode(cells);
      if (!seen.containsKey(state)) {
        seen[state] = n;
      } else {
        final int cycleLen = seen[state]! - n;
        n %= cycleLen;
      }
      if (n == 0) break;
      cells = _nextDay(cells);
      n--;
    }
    return cells;
  }

  int _encode(List<int> cells) {
    int num = 0;
    for (int i = 0; i < 8; i++) {
      num = (num << 1) | cells[i];
    }
    return num;
  }

  List<int> _nextDay(List<int> cells) {
    final List<int> next = List.filled(8, 0);
    for (int i = 1; i < 7; i++) {
      next[i] = cells[i - 1] == cells[i + 1] ? 1 : 0;
    }
    return next;
  }
}
```

## Golang

```go
func prisonAfterNDays(cells []int, n int) []int {
    // Encode current state into an 8-bit integer.
    state := 0
    for i, v := range cells {
        if v == 1 {
            state |= 1 << i
        }
    }

    seen := make(map[int]int) // state -> day index
    day := 0

    for n > 0 {
        if prevDay, ok := seen[state]; ok {
            cycleLen := day - prevDay
            n %= cycleLen
            if n == 0 {
                break
            }
        } else {
            seen[state] = day
        }

        // Compute next day's state.
        next := 0
        for i := 1; i < 7; i++ { // cells 1..6 can become occupied
            left := (state >> (i - 1)) & 1
            right := (state >> (i + 1)) & 1
            if left == right {
                next |= 1 << i
            }
        }

        state = next
        n--
        day++
    }

    // Decode integer back to slice.
    res := make([]int, 8)
    for i := 0; i < 8; i++ {
        if (state>>i)&1 == 1 {
            res[i] = 1
        }
    }
    return res
}
```

## Ruby

```ruby
def prison_after_n_days(cells, n)
  seen = {}
  day = 0
  while n > 0 && !seen.key?(cells.join)
    seen[cells.join] = day
    cells = next_state(cells)
    n -= 1
    day += 1
  end

  if n > 0
    cycle_len = day - seen[cells.join]
    n %= cycle_len
    while n > 0
      cells = next_state(cells)
      n -= 1
    end
  end
  cells
end

def next_state(cells)
  new_cells = Array.new(8, 0)
  (1..6).each do |i|
    new_cells[i] = cells[i - 1] == cells[i + 1] ? 1 : 0
  end
  new_cells
end
```

## Scala

```scala
object Solution {
    def prisonAfterNDays(cells: Array[Int], n: Int): Array[Int] = {
        var cur = cells.clone()
        val seen = scala.collection.mutable.Map[String, Int]()
        var day = 0
        while (day < n) {
            val key = cur.mkString("")
            if (!seen.contains(key)) {
                seen(key) = day
            } else {
                val cycleLen = day - seen(key)
                val remaining = (n - day) % cycleLen
                for (_ <- 0 until remaining) {
                    cur = nextDay(cur)
                }
                return cur
            }
            cur = nextDay(cur)
            day += 1
        }
        cur
    }

    private def nextDay(cells: Array[Int]): Array[Int] = {
        val nxt = new Array[Int](8)
        for (i <- 1 until 7) {
            nxt(i) = if (cells(i - 1) == cells(i + 1)) 1 else 0
        }
        nxt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

fn mask_to_vec(mask: u8) -> Vec<i32> {
    let mut v = vec![0; 8];
    for i in 0..8 {
        v[i] = ((mask >> i) & 1) as i32;
    }
    v
}

impl Solution {
    pub fn prison_after_n_days(cells: Vec<i32>, n: i32) -> Vec<i32> {
        let mut cur: u8 = {
            let mut m = 0u8;
            for i in 0..8 {
                if cells[i] == 1 {
                    m |= 1 << i;
                }
            }
            m
        };

        let total_days = n as usize;
        let mut seen: HashMap<u8, usize> = HashMap::new();
        let mut states: Vec<u8> = Vec::new();
        let mut day: usize = 0;

        while day < total_days {
            if let Some(&first_day) = seen.get(&cur) {
                let cycle_len = day - first_day;
                let remaining = (total_days - day) % cycle_len;
                return mask_to_vec(states[first_day + remaining]);
            }
            seen.insert(cur, day);
            states.push(cur);

            // compute next state
            let mut next: u8 = 0;
            for i in 1..7 {
                let left = (cur >> (i - 1)) & 1;
                let right = (cur >> (i + 1)) & 1;
                if left == right {
                    next |= 1 << i;
                }
            }
            cur = next;
            day += 1;
        }

        mask_to_vec(cur)
    }
}
```

## Racket

```racket
(define (next-state cells)
  (for/list ([i (in-range 8)])
    (cond [(or (= i 0) (= i 7)) 0]
          [else (if (= (list-ref cells (- i 1))
                       (list-ref cells (+ i 1))) 1 0)])))

(define/contract (prison-after-n-days cells n)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([steps (let ([r (remainder n 14)]) (if (= r 0) 14 r))])
    (let loop ((cur cells) (cnt steps))
      (if (= cnt 0)
          cur
          (loop (next-state cur) (- cnt 1))))))
```

## Erlang

```erlang
-export([prison_after_n_days/2]).

-spec prison_after_n_days(Cells :: [integer()], N :: integer()) -> [integer()].
prison_after_n_days(Cells, N) ->
    Mask0 = lists:foldl(fun(Bit, Acc) -> (Acc bsl 1) bor Bit end, 0, Cells),
    FinalMask = loop(Mask0, 0, N, #{}),
    mask_to_list(FinalMask).

loop(CurMask, Step, N, _Seen) when Step == N ->
    CurMask;
loop(CurMask, Step, N, Seen) ->
    case maps:find(CurMask, Seen) of
        {ok, PrevStep} ->
            CycleLen = Step - PrevStep,
            Remaining = N - Step,
            if Remaining >= CycleLen ->
                    Skip = (Remaining div CycleLen) * CycleLen,
                    loop(CurMask, Step + Skip, N, Seen);
               true ->
                    NextMask = next_state(CurMask),
                    loop(NextMask, Step + 1, N, Seen)
            end;
        error ->
            NewSeen = maps:put(CurMask, Step, Seen),
            NextMask = next_state(CurMask),
            loop(NextMask, Step + 1, N, NewSeen)
    end.

next_state(Mask) ->
    ShiftL = (Mask bsl 1) band 255,
    ShiftR = Mask bsr 1,
    Xor = ShiftL bxor ShiftR,
    Tmp = bnot Xor band 255,
    Tmp band 126.

mask_to_list(Mask) ->
    [ ((Mask bsr (7 - I)) band 1) || I <- lists:seq(0,7) ].
```

## Elixir

```elixir
defmodule Solution do
  @spec prison_after_n_days(cells :: [integer], n :: integer) :: [integer]
  def prison_after_n_days(cells, n) do
    {states, cycle_start, cycle_len} = build_states(cells)

    if n < length(states) do
      Enum.at(states, n)
    else
      idx = cycle_start + rem(n - cycle_start, cycle_len)
      Enum.at(states, idx)
    end
  end

  defp build_states(cells) do
    build_states(cells, [], %{}, 0)
  end

  defp build_states(cur, states_rev, seen, index) do
    key = Enum.join(cur)

    if Map.has_key?(seen, key) do
      start_idx = Map.get(seen, key)
      cycle_len = index - start_idx
      {Enum.reverse(states_rev), start_idx, cycle_len}
    else
      build_states(
        next_state(cur),
        [cur | states_rev],
        Map.put(seen, key, index),
        index + 1
      )
    end
  end

  defp next_state([a, b, c, d, e, f, g, h]) do
    [
      0,
      if a == c, do: 1, else: 0,
      if b == d, do: 1, else: 0,
      if c == e, do: 1, else: 0,
      if d == f, do: 1, else: 0,
      if e == g, do: 1, else: 0,
      if f == h, do: 1, else: 0,
      0
    ]
  end
end
```
