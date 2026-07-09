# 1386. Cinema Seat Allocation

## Cpp

```cpp
class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, int> rowMask;
        rowMask.reserve(reservedSeats.size() * 2);
        for (const auto& seat : reservedSeats) {
            int r = seat[0];
            int c = seat[1];
            if (c >= 2 && c <= 9) { // only seats that affect placement
                rowMask[r] |= 1 << (c - 1);
            }
        }
        const int leftMask   = (1 << (2 - 1)) | (1 << (3 - 1)) | (1 << (4 - 1)) | (1 << (5 - 1));
        const int rightMask  = (1 << (6 - 1)) | (1 << (7 - 1)) | (1 << (8 - 1)) | (1 << (9 - 1));
        const int middleMask = (1 << (4 - 1)) | (1 << (5 - 1)) | (1 << (6 - 1)) | (1 << (7 - 1));

        long long ans = static_cast<long long>(n - rowMask.size()) * 2; // rows without reservations
        for (const auto& kv : rowMask) {
            int mask = kv.second;
            bool leftFree  = (mask & leftMask) == 0;
            bool rightFree = (mask & rightMask) == 0;
            if (leftFree && rightFree) {
                ans += 2;
            } else if (leftFree || rightFree) {
                ans += 1;
            } else if ((mask & middleMask) == 0) {
                ans += 1;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        java.util.Map<Integer, Integer> rowMask = new java.util.HashMap<>();
        for (int[] seat : reservedSeats) {
            int r = seat[0];
            int c = seat[1];
            if (c == 1 || c == 10) continue; // irrelevant
            int bit = 1 << (c - 2); // seats 2..9 map to bits 0..7
            rowMask.put(r, rowMask.getOrDefault(r, 0) | bit);
        }

        int families = 0;
        final int LEFT_MASK = 0b1111;          // seats 2-5
        final int MIDDLE_MASK = 0b1111 << 2;   // seats 4-7
        final int RIGHT_MASK = 0b1111 << 4;    // seats 6-9

        for (int mask : rowMask.values()) {
            boolean leftFree = (mask & LEFT_MASK) == 0;
            boolean rightFree = (mask & RIGHT_MASK) == 0;
            if (leftFree && rightFree) {
                families += 2;
            } else {
                boolean middleFree = (mask & MIDDLE_MASK) == 0;
                if (leftFree || rightFree || middleFree) {
                    families += 1;
                }
            }
        }

        families += (n - rowMask.size()) * 2;
        return families;
    }
}
```

## Python

```python
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        row_masks = {}
        for r, c in reservedSeats:
            if 2 <= c <= 9:  # only seats that affect possible blocks
                mask = row_masks.get(r, 0)
                mask |= 1 << (c - 2)
                row_masks[r] = mask

        def count_families(mask):
            left_free = (mask & 0b1111) == 0          # seats 2-5
            right_free = (mask & 0b11110000) == 0    # seats 6-9
            middle_free = (mask & 0b111100) == 0     # seats 4-7 (bits 2-5)
            if left_free and right_free:
                return 2
            if left_free or right_free or middle_free:
                return 1
            return 0

        total = (n - len(row_masks)) * 2
        for mask in row_masks.values():
            total += count_families(mask)
        return total
```

## Python3

```python
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = {}
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                rows.setdefault(r, 0)
                rows[r] |= 1 << (c - 2)

        # rows without any reservation can always seat two families
        ans = (n - len(rows)) * 2

        LEFT_MASK = 0b1111          # seats 2-5 -> bits 0-3
        MIDDLE_MASK = 0b111100      # seats 4-7 -> bits 2-5
        RIGHT_MASK = 0b11110000     # seats 6-9 -> bits 4-7

        for mask in rows.values():
            families = 0
            if (mask & LEFT_MASK) == 0:
                families += 1
            if (mask & RIGHT_MASK) == 0:
                families += 1
            if families == 0 and (mask & MIDDLE_MASK) == 0:
                families = 1
            ans += families

        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int row;
    int seat;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->row != pb->row) return pa->row - pb->row;
    return pa->seat - pb->seat;
}

int maxNumberOfFamilies(int n, int** reservedSeats, int reservedSeatsSize, int* reservedSeatsColSize){
    long long total = (long long)n * 2; // maximum families without any reservations
    if (reservedSeatsSize == 0) return (int)total;

    Pair *arr = (Pair *)malloc(sizeof(Pair) * reservedSeatsSize);
    for (int i = 0; i < reservedSeatsSize; ++i) {
        arr[i].row = reservedSeats[i][0];
        arr[i].seat = reservedSeats[i][1];
    }
    qsort(arr, reservedSeatsSize, sizeof(Pair), cmpPair);

    int i = 0;
    while (i < reservedSeatsSize) {
        int curRow = arr[i].row;
        int mask = 0;
        // collect all seats in this row
        while (i < reservedSeatsSize && arr[i].row == curRow) {
            mask |= (1 << arr[i].seat);
            ++i;
        }

        bool leftFree   = (mask & ((1<<2)|(1<<3)|(1<<4)|(1<<5))) == 0;
        bool rightFree  = (mask & ((1<<6)|(1<<7)|(1<<8)|(1<<9))) == 0;
        bool middleFree = (mask & ((1<<4)|(1<<5)|(1<<6)|(1<<7))) == 0;

        int families = 0;
        if (leftFree) families++;
        if (rightFree) families++;
        if (!leftFree && !rightFree && middleFree) families = 1;

        total -= 2;          // remove the default two families for this row
        total += families;   // add back the actually possible families
    }

    free(arr);
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxNumberOfFamilies(int n, int[][] reservedSeats) {
        var rowMask = new Dictionary<int, int>();
        foreach (var seat in reservedSeats) {
            int r = seat[0];
            int c = seat[1];
            if (!rowMask.ContainsKey(r)) {
                rowMask[r] = 0;
            }
            rowMask[r] |= 1 << (c - 1);
        }

        int families = 0;
        int leftMask   = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4); // seats 2-5
        int middleMask = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6); // seats 4-7
        int rightMask  = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8); // seats 6-9

        foreach (var kv in rowMask) {
            int mask = kv.Value;
            bool leftFree   = (mask & leftMask) == 0;
            bool rightFree  = (mask & rightMask) == 0;
            bool middleFree = (mask & middleMask) == 0;

            if (leftFree && rightFree) {
                families += 2;
            } else if (leftFree || rightFree || middleFree) {
                families += 1;
            }
        }

        families += (n - rowMask.Count) * 2;
        return families;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} reservedSeats
 * @return {number}
 */
var maxNumberOfFamilies = function(n, reservedSeats) {
    const rowMask = new Map();
    for (const [r, c] of reservedSeats) {
        const mask = rowMask.get(r) || 0;
        rowMask.set(r, mask | (1 << (c - 1)));
    }
    
    const LEFT_MASK  = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4); // seats 2-5
    const MID_MASK   = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6); // seats 4-7
    const RIGHT_MASK = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8); // seats 6-9
    
    let total = (n - rowMask.size) * 2;
    
    for (const mask of rowMask.values()) {
        const leftFree  = (mask & LEFT_MASK) === 0;
        const rightFree = (mask & RIGHT_MASK) === 0;
        if (leftFree && rightFree) {
            total += 2;
        } else {
            const midFree = (mask & MID_MASK) === 0;
            if (leftFree || rightFree || midFree) total += 1;
        }
    }
    
    return total;
};
```

## Typescript

```typescript
function maxNumberOfFamilies(n: number, reservedSeats: number[][]): number {
    const rowMap = new Map<number, number>();
    for (const [r, s] of reservedSeats) {
        const mask = (rowMap.get(r) ?? 0) | (1 << (s - 1));
        rowMap.set(r, mask);
    }
    const leftMask = (1 << (2 - 1)) | (1 << (3 - 1)) | (1 << (4 - 1)) | (1 << (5 - 1));
    const middleMask = (1 << (4 - 1)) | (1 << (5 - 1)) | (1 << (6 - 1)) | (1 << (7 - 1));
    const rightMask = (1 << (6 - 1)) | (1 << (7 - 1)) | (1 << (8 - 1)) | (1 << (9 - 1));

    let result = (n - rowMap.size) * 2;
    for (const mask of rowMap.values()) {
        const leftFree = (mask & leftMask) === 0;
        const rightFree = (mask & rightMask) === 0;
        if (leftFree && rightFree) {
            result += 2;
        } else {
            const middleFree = (mask & middleMask) === 0;
            if (leftFree || rightFree || middleFree) {
                result += 1;
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $reservedSeats
     * @return Integer
     */
    function maxNumberOfFamilies($n, $reservedSeats) {
        $rowMask = [];
        foreach ($reservedSeats as $seat) {
            $r = $seat[0];
            $c = $seat[1];
            if (!isset($rowMask[$r])) {
                $rowMask[$r] = 0;
            }
            // set bit for this column
            $rowMask[$r] |= (1 << $c);
        }

        // rows without any reserved seats can always seat two families
        $total = ($n - count($rowMask)) * 2;

        foreach ($rowMask as $mask) {
            $leftFree  = (($mask & ((1<<2)|(1<<3)|(1<<4)|(1<<5))) == 0);
            $rightFree = (($mask & ((1<<6)|(1<<7)|(1<<8)|(1<<9))) == 0);
            $midFree   = (($mask & ((1<<4)|(1<<5)|(1<<6)|(1<<7))) == 0);

            if ($leftFree && $rightFree) {
                $total += 2;
            } elseif ($leftFree || $rightFree || $midFree) {
                $total += 1;
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maxNumberOfFamilies(_ n: Int, _ reservedSeats: [[Int]]) -> Int {
        var rowMask = [Int: Int]()
        for seat in reservedSeats {
            let r = seat[0]
            let c = seat[1]
            if c >= 2 && c <= 9 {
                let bit = 1 << (c - 1)
                rowMask[r, default: 0] |= bit
            }
        }
        
        let left = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)   // seats 2-5
        let middle = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6) // seats 4-7
        let right = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8)  // seats 6-9
        
        var result = 0
        for mask in rowMask.values {
            if (mask & left) == 0 && (mask & right) == 0 {
                result += 2
            } else if (mask & left) == 0 || (mask & middle) == 0 || (mask & right) == 0 {
                result += 1
            }
        }
        
        result += (n - rowMask.count) * 2
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNumberOfFamilies(n: Int, reservedSeats: Array<IntArray>): Int {
        val rowMask = HashMap<Int, Int>()
        for (seat in reservedSeats) {
            val r = seat[0]
            val c = seat[1]
            if (c >= 2 && c <= 9) {
                val bit = 1 shl (c - 2)
                rowMask[r] = rowMask.getOrDefault(r, 0) or bit
            }
        }

        var result = (n - rowMask.size) * 2

        val leftMask = 0b1111          // seats 2-5
        val midMask = 0b111100         // seats 4-7
        val rightMask = 0b11110000     // seats 6-9

        for (mask in rowMask.values) {
            val canLeft = (mask and leftMask) == 0
            val canRight = (mask and rightMask) == 0
            if (canLeft && canRight) {
                result += 2
            } else {
                val canMid = (mask and midMask) == 0
                if (canLeft || canRight || canMid) {
                    result += 1
                }
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  int maxNumberOfFamilies(int n, List<List<int>> reservedSeats) {
    const int leftMask = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4);   // seats 2-5
    const int rightMask = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8); // seats 6-9
    const int middleMask = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6); // seats 4-7

    final Map<int, int> rowMask = {};

    for (final seat in reservedSeats) {
      final int r = seat[0];
      final int c = seat[1];
      rowMask[r] = (rowMask[r] ?? 0) | (1 << (c - 1));
    }

    int families = 0;

    rowMask.forEach((int _, int mask) {
      final bool leftFree = (mask & leftMask) == 0;
      final bool rightFree = (mask & rightMask) == 0;

      if (leftFree && rightFree) {
        families += 2;
      } else {
        final bool middleFree = (mask & middleMask) == 0;
        if (leftFree || rightFree || middleFree) {
          families += 1;
        }
      }
    });

    families += (n - rowMask.length) * 2;
    return families;
  }
}
```

## Golang

```go
func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
    rowMask := make(map[int]int)
    for _, rs := range reservedSeats {
        r, c := rs[0], rs[1]
        if c >= 2 && c <= 9 {
            mask := rowMask[r]
            mask |= 1 << (c - 2)
            rowMask[r] = mask
        }
    }

    total := (n - len(rowMask)) * 2

    const leftMask = 0xF   // seats 2-5
    const rightMask = 0xF0 // seats 6-9
    const middleMask = 0x3C // seats 4-7

    for _, mask := range rowMask {
        leftFree := (mask & leftMask) == 0
        rightFree := (mask & rightMask) == 0
        middleFree := (mask & middleMask) == 0

        if leftFree && rightFree {
            total += 2
        } else if leftFree || rightFree || middleFree {
            total++
        }
    }

    return total
}
```

## Ruby

```ruby
def max_number_of_families(n, reserved_seats)
  left_mask   = 0b1111       # seats 2-5
  middle_mask = 0b111100     # seats 4-7
  right_mask  = 0b11110000   # seats 6-9

  row_masks = Hash.new(0)

  reserved_seats.each do |row, seat|
    next if seat < 2 || seat > 9
    bit = seat - 2
    row_masks[row] |= (1 << bit)
  end

  families = (n - row_masks.size) * 2

  row_masks.each_value do |mask|
    left_free  = (mask & left_mask).zero?
    right_free = (mask & right_mask).zero?

    if left_free && right_free
      families += 2
    elsif left_free || right_free || (mask & middle_mask).zero?
      families += 1
    end
  end

  families
end
```

## Scala

```scala
object Solution {
    def maxNumberOfFamilies(n: Int, reservedSeats: Array[Array[Int]]): Int = {
        val leftMask = (1 << 4) - 1               // seats 2-5 -> bits 0..3
        val rightMask = ((1 << 4) - 1) << 4       // seats 6-9 -> bits 4..7
        val middleMask = ((1 << 4) - 1) << 2      // seats 4-7 -> bits 2..5

        import scala.collection.mutable
        val rowMap = mutable.Map[Int, Int]()

        for (seat <- reservedSeats) {
            val r = seat(0)
            val c = seat(1)
            if (c >= 2 && c <= 9) {
                val bit = 1 << (c - 2)
                rowMap.update(r, rowMap.getOrElse(r, 0) | bit)
            }
        }

        var result: Long = n.toLong * 2

        for ((_, mask) <- rowMap) {
            result -= 2
            val leftFree = (mask & leftMask) == 0
            val rightFree = (mask & rightMask) == 0
            if (leftFree && rightFree) {
                result += 2
            } else if (leftFree || rightFree || ((mask & middleMask) == 0)) {
                result += 1
            }
        }

        result.toInt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn max_number_of_families(n: i32, reserved_seats: Vec<Vec<i32>>) -> i32 {
        let mut rows: HashMap<i32, u16> = HashMap::new();
        for seat in reserved_seats.iter() {
            let row = seat[0];
            let col = seat[1];
            if (2..=9).contains(&col) {
                let entry = rows.entry(row).or_insert(0);
                *entry |= 1 << (col - 2);
            }
        }

        let left_mask: u16 = 0b1111;          // seats 2,3,4,5
        let right_mask: u16 = 0b1111 << 4;    // seats 6,7,8,9
        let middle_mask: u16 = 0b1111 << 2;   // seats 4,5,6,7

        let mut families = 0i32;
        for &bits in rows.values() {
            let left_free = (bits & left_mask) == 0;
            let right_free = (bits & right_mask) == 0;
            let middle_free = (bits & middle_mask) == 0;

            if left_free && right_free {
                families += 2;
            } else if left_free || right_free || middle_free {
                families += 1;
            }
        }

        families + (n - rows.len() as i32) * 2
    }
}
```

## Racket

```racket
(define/contract (max-number-of-families n reservedSeats)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((row-mask (make-hash))
         (add-seat
          (lambda (row seat)
            (when (and (>= seat 2) (<= seat 9))
              (define cur (hash-ref row-mask row 0))
              (hash-set! row-mask row
                         (bitwise-ior cur (arithmetic-shift 1 (- seat 2))))))))
    ;; build masks for rows that have reserved seats affecting families
    (for ([pair reservedSeats])
      (match-define (list r s) pair)
      (add-seat r s))
    (define left-mask   #b1111)                     ; seats 2‑5
    (define right-mask  (arithmetic-shift #b1111 4)) ; seats 6‑9
    (define middle-mask (arithmetic-shift #b1111 2)) ; seats 4‑7
    (define free-rows (- n (hash-count row-mask)))   ; rows without any relevant reservation
    (+ (* 2 free-rows)
       (for/sum ([row (in-hash-keys row-mask)])
         (let ((mask (hash-ref row-mask row)))
           (cond
             [(and (= (bitwise-and mask left-mask) 0)
                   (= (bitwise-and mask right-mask) 0)) 2]
             [(or (= (bitwise-and mask left-mask) 0)
                  (= (bitwise-and mask right-mask) 0)
                  (= (bitwise-and mask middle-mask) 0)) 1]
             [else 0]))))))
```

## Erlang

```erlang
-spec max_number_of_families(N :: integer(), ReservedSeats :: [[integer()]]) -> integer().
max_number_of_families(N, ReservedSeats) ->
    Map = build_map(ReservedSeats, #{}),
    FamiliesWithReservations = maps:fold(
        fun(_Row, Mask, Acc) -> Acc + families_in_row(Mask) end,
        0,
        Map
    ),
    RowsWithout = N - maps:size(Map),
    FamiliesWithReservations + RowsWithout * 2.

build_map([], Map) ->
    Map;
build_map([[R, S] | Rest], Map) ->
    if
        S >= 2, S =< 9 ->
            Bit = 1 bsl (S - 2),
            NewMask = maps:get(R, Map, 0) bor Bit,
            build_map(Rest, Map#{R => NewMask});
        true ->
            build_map(Rest, Map)
    end.

families_in_row(Mask) ->
    LeftMask = 15,      % seats 2-5
    MiddleMask = 60,    % seats 4-7
    RightMask = 240,    % seats 6-9
    case ((Mask band LeftMask) == 0) andalso ((Mask band RightMask) == 0) of
        true ->
            2;
        false ->
            if
                ((Mask band LeftMask) == 0) orelse
                ((Mask band RightMask) == 0) orelse
                ((Mask band MiddleMask) == 0) ->
                    1;
                true ->
                    0
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_number_of_families(n :: integer, reserved_seats :: [[integer]]) :: integer
  def max_number_of_families(n, reserved_seats) do
    import Bitwise

    masks =
      Enum.reduce(reserved_seats, %{}, fn [row, col], acc ->
        if col >= 2 and col <= 9 do
          bit = 1 <<< (col - 2)
          Map.update(acc, row, bit, &(&1 ||| bit))
        else
          acc
        end
      end)

    families_reserved =
      Enum.reduce(masks, 0, fn {_row, mask}, sum ->
        left_free = (mask &&& 0b1111) == 0
        right_free = (mask &&& 0b11110000) == 0
        middle_free = (mask &&& 0b00111100) == 0

        cond do
          left_free and right_free -> sum + 2
          left_free or right_free or middle_free -> sum + 1
          true -> sum
        end
      end)

    families_reserved + (n - map_size(masks)) * 2
  end
end
```
