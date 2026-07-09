# 2147. Number of Ways to Divide a Long Corridor

## Cpp

```cpp
class Solution {
public:
    int numberOfWays(string corridor) {
        const long long MOD = 1000000007LL;
        vector<int> seats;
        for (int i = 0; i < (int)corridor.size(); ++i) {
            if (corridor[i] == 'S') seats.push_back(i);
        }
        int m = seats.size();
        if (m == 0 || (m & 1)) return 0;
        long long ans = 1;
        for (int i = 1; i + 1 < m; i += 2) {
            ans = ans * (seats[i + 1] - seats[i]) % MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numberOfWays(String corridor) {
        final long MOD = 1_000_000_007L;
        int n = corridor.length();
        // Collect indices of seats 'S'
        java.util.ArrayList<Integer> seatIdx = new java.util.ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (corridor.charAt(i) == 'S') {
                seatIdx.add(i);
            }
        }
        int m = seatIdx.size();
        // No seats or odd number of seats -> impossible
        if (m == 0 || (m & 1) == 1) {
            return 0;
        }
        long ans = 1L;
        // Multiply gaps between consecutive pairs: seat[2k+1] and seat[2k+2]
        for (int i = 1; i + 1 < m; i += 2) {
            long diff = seatIdx.get(i + 1) - seatIdx.get(i);
            ans = (ans * diff) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10**9 + 7
        seats = [i for i, ch in enumerate(corridor) if ch == 'S']
        n = len(seats)
        # Need even number of seats and at least one pair
        if n == 0 or n % 2:
            return 0
        ans = 1
        # multiply gaps between consecutive pairs: seat[2k+1] to seat[2k+2]
        for i in range(1, n - 1, 2):
            gap = seats[i + 1] - seats[i]
            ans = (ans * gap) % MOD
        return ans
```

## Python3

```python
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        ans = 1
        prev_last = -1          # index of the second seat in previous pair
        cnt = 0                 # seats seen in current pair (0 or 1)
        total_seats = 0

        for i, ch in enumerate(corridor):
            if ch == 'S':
                total_seats += 1
                cnt += 1
                if cnt == 1:
                    if prev_last != -1:
                        ans = (ans * (i - prev_last)) % MOD
                else:  # cnt == 2, pair completed
                    prev_last = i
                    cnt = 0

        if total_seats == 0 or total_seats % 2 == 1:
            return 0
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int numberOfWays(char* corridor) {
    const int MOD = 1000000007;
    int n = (int)strlen(corridor);
    
    // Store indices of all seats 'S'
    int *pos = (int *)malloc(sizeof(int) * n);
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (corridor[i] == 'S') {
            pos[cnt++] = i;
        }
    }
    
    // If number of seats is zero or odd, no valid division exists
    if (cnt == 0 || (cnt & 1)) {
        free(pos);
        return 0;
    }
    
    long long ans = 1;
    // Multiply gaps between consecutive pairs of sections
    for (int i = 2; i < cnt; i += 2) {
        long long diff = pos[i] - pos[i - 1];
        ans = (ans * diff) % MOD;
    }
    
    free(pos);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfWays(string corridor) {
        const long MOD = 1000000007L;
        var seatIndices = new System.Collections.Generic.List<int>();
        for (int i = 0; i < corridor.Length; i++) {
            if (corridor[i] == 'S') seatIndices.Add(i);
        }
        int m = seatIndices.Count;
        if (m == 0 || (m & 1) == 1) return 0;
        long ans = 1;
        for (int i = 2; i < m; i += 2) {
            long diff = seatIndices[i] - seatIndices[i - 1];
            ans = (ans * diff) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} corridor
 * @return {number}
 */
var numberOfWays = function(corridor) {
    const MOD = 1000000007n;
    const seats = [];
    for (let i = 0; i < corridor.length; ++i) {
        if (corridor[i] === 'S') seats.push(i);
    }
    const m = seats.length;
    // No seats or odd number of seats -> impossible
    if (m === 0 || (m & 1)) return 0;
    
    let ans = 1n;
    for (let i = 2; i < m; i += 2) {
        const diff = BigInt(seats[i] - seats[i - 1]);
        ans = (ans * diff) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function numberOfWays(corridor: string): number {
    const MOD = 1000000007n;
    let prevPairLast = -1;          // index of the second seat in the previous pair
    let seatsInCurrent = 0;         // seats counted in the current (incomplete) pair
    let ans = 1n;
    let totalSeats = 0;

    for (let i = 0; i < corridor.length; ++i) {
        if (corridor[i] === 'S') {
            totalSeats++;
            seatsInCurrent++;

            if (seatsInCurrent === 1) {          // first seat of a new pair
                if (prevPairLast !== -1) {
                    const diff = BigInt(i - prevPairLast);
                    ans = (ans * diff) % MOD;
                }
            } else {                              // second seat completes the pair
                prevPairLast = i;
                seatsInCurrent = 0;
            }
        }
    }

    if (totalSeats === 0 || totalSeats % 2 === 1) return 0;
    return Number(ans);
}
```

## Php

```php
class Solution {
    /**
     * @param String $corridor
     * @return Integer
     */
    function numberOfWays($corridor) {
        $mod = 1000000007;
        $indices = [];
        $n = strlen($corridor);
        for ($i = 0; $i < $n; $i++) {
            if ($corridor[$i] === 'S') {
                $indices[] = $i;
            }
        }
        $cnt = count($indices);
        if ($cnt == 0 || ($cnt & 1)) {
            return 0;
        }
        $ans = 1;
        for ($j = 1; $j < $cnt - 1; $j += 2) {
            $gap = $indices[$j + 1] - $indices[$j];
            $ans = ($ans * $gap) % $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfWays(_ corridor: String) -> Int {
        let MOD = 1_000_000_007
        var totalSeats = 0
        var seatInPair = 0          // seats counted in the current pair (0 or 1)
        var prevSecondIdx = -1      // index of the second seat of the previous completed pair
        var result: Int64 = 1
        
        for (i, ch) in corridor.enumerated() {
            if ch == "S" {
                totalSeats += 1
                seatInPair += 1
                if seatInPair == 1 {
                    // first seat of a new pair; multiply gap with previous pair's second seat
                    if prevSecondIdx != -1 {
                        let gap = i - prevSecondIdx
                        result = (result * Int64(gap)) % Int64(MOD)
                    }
                } else { // seatInPair == 2, pair completed
                    prevSecondIdx = i
                    seatInPair = 0
                }
            }
        }
        
        if totalSeats == 0 || totalSeats % 2 != 0 {
            return 0
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfWays(corridor: String): Int {
        val MOD = 1000000007L
        val seatIndices = mutableListOf<Int>()
        for (i in corridor.indices) {
            if (corridor[i] == 'S') seatIndices.add(i)
        }
        val cnt = seatIndices.size
        if (cnt == 0 || cnt % 2 == 1) return 0
        var ans = 1L
        var i = 0
        while (i + 2 < cnt) {
            val gap = seatIndices[i + 2] - seatIndices[i + 1]
            ans = (ans * gap) % MOD
            i += 2
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numberOfWays(String corridor) {
    List<int> seats = [];
    for (int i = 0; i < corridor.length; i++) {
      if (corridor.codeUnitAt(i) == 83) { // 'S'
        seats.add(i);
      }
    }

    if (seats.length.isOdd) return 0;

    int result = 1;
    for (int i = 1; i + 1 < seats.length; i += 2) {
      int gap = seats[i + 1] - seats[i];
      result = (result * gap) % _mod;
    }
    return result;
  }
}
```

## Golang

```go
func numberOfWays(corridor string) int {
	const MOD int64 = 1000000007
	seatIdx := make([]int, 0, len(corridor))
	for i, ch := range corridor {
		if ch == 'S' {
			seatIdx = append(seatIdx, i)
		}
	}
	if len(seatIdx) == 0 || len(seatIdx)%2 == 1 {
		return 0
	}
	ans := int64(1)
	for i := 1; i+1 < len(seatIdx); i += 2 {
		diff := seatIdx[i+1] - seatIdx[i]
		ans = (ans * int64(diff)) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def number_of_ways(corridor)
  seats = []
  corridor.each_char.with_index { |c, i| seats << i if c == 'S' }
  return 0 if seats.empty? || (seats.length & 1) == 1

  ans = 1
  (2...seats.length).step(2) do |i|
    diff = seats[i] - seats[i - 1]
    ans = (ans * diff) % MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numberOfWays(corridor: String): Int = {
        val MOD = 1000000007L
        val seatIndices = scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- corridor.indices) {
            if (corridor.charAt(i) == 'S') seatIndices += i
        }
        if (seatIndices.isEmpty || seatIndices.size % 2 == 1) return 0
        var ans: Long = 1L
        var i = 1
        while (i + 1 < seatIndices.size) {
            val diff = seatIndices(i + 1) - seatIndices(i)
            ans = (ans * diff) % MOD
            i += 2
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut seats: Vec<i64> = Vec::new();
        for (i, ch) in corridor.chars().enumerate() {
            if ch == 'S' {
                seats.push(i as i64);
            }
        }
        if seats.is_empty() || seats.len() % 2 == 1 {
            return 0;
        }
        let mut ans: i64 = 1;
        // multiply distances between consecutive pairs of seats
        for i in (0..seats.len() - 2).step_by(2) {
            let diff = seats[i + 2] - seats[i + 1];
            ans = ans * diff % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (number-of-ways corridor)
  (-> string? exact-integer?)
  (let* ((n (string-length corridor))
         (prev -1)          ; index of the second seat of previous pair
         (seat-mod 0)       ; seats seen in current unfinished pair (0 or 1)
         (result 1)
         (total 0))         ; total number of seats encountered
    (for ([i (in-range n)])
      (let ((ch (string-ref corridor i)))
        (when (char=? ch #\S)
          (set! total (+ total 1))
          (set! seat-mod (+ seat-mod 1))
          (cond
            [(= seat-mod 1)               ; first seat of a new pair
             (when (>= prev 0)            ; there is a previous completed pair
               (set! result (modulo (* result (- i prev)) MOD)))]
            [(= seat-mod 2)               ; second seat completes the pair
             (set! prev i)
             (set! seat-mod 0)]))))
    (if (or (= total 0) (> seat-mod 0))
        0
        result)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_ways/1]).

-spec number_of_ways(Corridor :: unicode:unicode_binary()) -> integer().
number_of_ways(Corridor) ->
    Mod = 1000000007,
    Seats = collect_seat_positions(Corridor, 0, []),
    case length(Seats) of
        N when N == 0; N rem 2 =:= 1 -> 0;
        _ -> product_gaps(Seats, Mod, 1)
    end.

collect_seat_positions(Binary, Index, Acc) ->
    Size = byte_size(Binary),
    if Index >= Size ->
            lists:reverse(Acc);
       true ->
            case binary:at(Binary, Index) of
                $S -> collect_seat_positions(Binary, Index + 1, [Index | Acc]);
                _  -> collect_seat_positions(Binary, Index + 1, Acc)
            end
    end.

product_gaps([], _Mod, Acc) -> Acc;
product_gaps([_], _Mod, Acc) -> Acc;
product_gaps([A,B|Rest], Mod, Acc) ->
    case Rest of
        [] -> Acc rem Mod;
        [C|Rest2] ->
            Gap = C - B,
            NewAcc = (Acc * Gap) rem Mod,
            product_gaps([C|Rest2], Mod, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(String.t()) :: integer
  def number_of_ways(corridor) do
    mod = 1_000_000_007

    {count, prev_idx, seat_cnt} =
      corridor
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({1, nil, 0}, fn {ch, idx}, {cnt, prev, s_cnt} ->
        if ch == "S" do
          s_cnt = s_cnt + 1

          cond do
            s_cnt == 1 and not is_nil(prev) ->
              cnt = rem(cnt * (idx - prev), mod)
              {cnt, prev, s_cnt}

            s_cnt == 2 ->
              {cnt, idx, 0}

            true ->
              {cnt, prev, s_cnt}
          end
        else
          {cnt, prev, s_cnt}
        end
      end)

    if seat_cnt != 0 do
      0
    else
      case prev_idx do
        nil -> 0
        _ -> rem(count, mod)
      end
    end
  end
end
```
