# 0849. Maximize Distance to Closest Person

## Cpp

```cpp
class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int n = seats.size();
        int prev = -1;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (seats[i] == 1) {
                if (prev == -1) {
                    // leading zeros
                    ans = i;
                } else {
                    // zeros between two people
                    ans = max(ans, (i - prev) / 2);
                }
                prev = i;
            }
        }
        // trailing zeros
        if (seats[n - 1] == 0) {
            ans = max(ans, n - 1 - prev);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxDistToClosest(int[] seats) {
        int n = seats.length;
        int maxDist = 0;
        int prevOccupied = -1; // index of previous occupied seat
        
        for (int i = 0; i < n; i++) {
            if (seats[i] == 1) {
                if (prevOccupied == -1) {
                    // leading zeros
                    maxDist = Math.max(maxDist, i);
                } else {
                    int gap = i - prevOccupied - 1; // number of empty seats between two occupied seats
                    int candidate = (gap + 1) / 2;
                    maxDist = Math.max(maxDist, candidate);
                }
                prevOccupied = i;
            }
        }
        
        // trailing zeros
        if (seats[n - 1] == 0) {
            int distance = n - 1 - prevOccupied;
            maxDist = Math.max(maxDist, distance);
        }
        
        return maxDist;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        last = -1
        max_dist = 0
        n = len(seats)
        for i, s in enumerate(seats):
            if s == 1:
                if last == -1:
                    # leading zeros
                    max_dist = i
                else:
                    gap = i - last - 1
                    max_dist = max(max_dist, (gap + 1) // 2)
                last = i
        # trailing zeros
        if seats[-1] == 0:
            max_dist = max(max_dist, n - 1 - last)
        return max_dist
```

## Python3

```python
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = -1
        max_dist = 0
        n = len(seats)
        for i, s in enumerate(seats):
            if s == 1:
                if last == -1:
                    # leading zeros
                    max_dist = i
                else:
                    gap = i - last - 1
                    max_dist = max(max_dist, (gap + 1) // 2)
                last = i
        # trailing zeros
        if seats[-1] == 0:
            max_dist = max(max_dist, n - 1 - last)
        return max_dist
```

## C

```c
int maxDistToClosest(int* seats, int seatsSize) {
    int prev = -1;
    int ans = 0;
    for (int i = 0; i < seatsSize; ++i) {
        if (seats[i] == 1) {
            if (prev == -1) {
                // Leading zeros
                if (i > ans) ans = i;
            } else {
                int gap = i - prev - 1;
                int cand = (gap + 1) / 2;
                if (cand > ans) ans = cand;
            }
            prev = i;
        }
    }
    // Trailing zeros
    if (prev != -1) {
        int tail = seatsSize - 1 - prev;
        if (tail > ans) ans = tail;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDistToClosest(int[] seats) {
        int n = seats.Length;
        int maxDist = 0;
        int prevOccupied = -1;

        for (int i = 0; i < n; i++) {
            if (seats[i] == 1) {
                if (prevOccupied == -1) {
                    // leading zeros
                    maxDist = Math.Max(maxDist, i);
                } else {
                    int gap = i - prevOccupied - 1;
                    int candidate = (gap + 1) / 2;
                    maxDist = Math.Max(maxDist, candidate);
                }
                prevOccupied = i;
            }
        }

        // trailing zeros
        if (seats[n - 1] == 0) {
            int trailingZeros = n - 1 - prevOccupied;
            maxDist = Math.Max(maxDist, trailingZeros);
        }

        return maxDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function(seats) {
    let maxDist = 0;
    let lastOccupied = -1;
    const n = seats.length;
    
    for (let i = 0; i < n; i++) {
        if (seats[i] === 1) {
            if (lastOccupied === -1) {
                // leading zeros
                maxDist = i;
            } else {
                // zeros between two occupied seats
                const dist = Math.floor((i - lastOccupied) / 2);
                if (dist > maxDist) maxDist = dist;
            }
            lastOccupied = i;
        }
    }
    
    // trailing zeros
    if (seats[n - 1] === 0) {
        const trailingDist = n - 1 - lastOccupied;
        if (trailingDist > maxDist) maxDist = trailingDist;
    }
    
    return maxDist;
};
```

## Typescript

```typescript
function maxDistToClosest(seats: number[]): number {
    const n = seats.length;
    let firstOccupied = -1;
    let lastOccupied = -1;

    for (let i = 0; i < n; i++) {
        if (seats[i] === 1) {
            if (firstOccupied === -1) firstOccupied = i;
            lastOccupied = i;
        }
    }

    // Distance from start to first occupied seat and from last occupied seat to end
    let maxDist = Math.max(firstOccupied, n - 1 - lastOccupied);

    // Scan between first and last occupied seats
    let i = firstOccupied;
    while (i <= lastOccupied) {
        if (seats[i] === 1) {
            let j = i + 1;
            while (j <= lastOccupied && seats[j] === 0) {
                j++;
            }
            if (j > lastOccupied) break; // no more occupied seat on the right
            const zerosBetween = j - i - 1;
            maxDist = Math.max(maxDist, Math.floor((zerosBetween + 1) / 2));
            i = j;
        } else {
            i++;
        }
    }

    return maxDist;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $seats
     * @return Integer
     */
    function maxDistToClosest($seats) {
        $n = count($seats);
        $lastOccupied = -1;
        $maxDist = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($seats[$i] == 1) {
                if ($lastOccupied == -1) {
                    // leading zeros
                    $maxDist = max($maxDist, $i);
                } else {
                    $gap = $i - $lastOccupied - 1;
                    $candidate = intdiv($gap + 1, 2);
                    $maxDist = max($maxDist, $candidate);
                }
                $lastOccupied = $i;
            }
        }

        // trailing zeros
        if ($lastOccupied != -1) {
            $tail = $n - 1 - $lastOccupied;
            $maxDist = max($maxDist, $tail);
        }

        return $maxDist;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistToClosest(_ seats: [Int]) -> Int {
        var prev = -1
        var answer = 0
        let n = seats.count
        for i in 0..<n {
            if seats[i] == 1 {
                if prev == -1 {
                    // leading zeros
                    answer = max(answer, i)
                } else {
                    let zeros = i - prev - 1
                    let dist = (zeros + 1) / 2
                    answer = max(answer, dist)
                }
                prev = i
            }
        }
        // trailing zeros
        if seats[n - 1] == 0 {
            let zeros = n - prev - 1
            answer = max(answer, zeros)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistToClosest(seats: IntArray): Int {
        var last = -1
        var ans = 0
        for (i in seats.indices) {
            if (seats[i] == 1) {
                if (last == -1) {
                    ans = i
                } else {
                    val gap = i - last - 1
                    val dist = (gap + 1) / 2
                    if (dist > ans) ans = dist
                }
                last = i
            }
        }
        if (last != -1) {
            val tailDist = seats.size - 1 - last
            if (tailDist > ans) ans = tailDist
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxDistToClosest(List<int> seats) {
    int last = -1;
    int maxDist = 0;
    for (int i = 0; i < seats.length; ++i) {
      if (seats[i] == 1) {
        if (last == -1) {
          // Leading zeros
          maxDist = i;
        } else {
          int dist = ((i - last) ~/ 2);
          if (dist > maxDist) maxDist = dist;
        }
        last = i;
      }
    }
    // Trailing zeros
    if (last != -1) {
      int tailDist = seats.length - 1 - last;
      if (tailDist > maxDist) maxDist = tailDist;
    }
    return maxDist;
  }
}
```

## Golang

```go
func maxDistToClosest(seats []int) int {
    last := -1
    maxDist := 0
    n := len(seats)
    for i, s := range seats {
        if s == 1 {
            if last == -1 {
                // leading zeros
                if i > maxDist {
                    maxDist = i
                }
            } else {
                // zeros between two occupied seats
                dist := (i - last) / 2
                if dist > maxDist {
                    maxDist = dist
                }
            }
            last = i
        }
    }
    // trailing zeros
    if last != -1 && last < n-1 {
        tailDist := n - 1 - last
        if tailDist > maxDist {
            maxDist = tailDist
        }
    }
    return maxDist
}
```

## Ruby

```ruby
def max_dist_to_closest(seats)
  n = seats.length
  first_one = seats.index(1)
  last_one = seats.rindex(1)

  max_dist = [first_one, n - 1 - last_one].max

  i = first_one
  while i <= last_one
    if seats[i] == 0
      cnt = 0
      while i <= last_one && seats[i] == 0
        cnt += 1
        i += 1
      end
      max_dist = [max_dist, (cnt + 1) / 2].max
    else
      i += 1
    end
  end

  max_dist
end
```

## Scala

```scala
object Solution {
    def maxDistToClosest(seats: Array[Int]): Int = {
        var ans = 0
        var prev = -1
        val n = seats.length
        for (i <- 0 until n) {
            if (seats(i) == 1) {
                if (prev == -1) {
                    ans = math.max(ans, i)
                } else {
                    val gap = i - prev - 1
                    ans = math.max(ans, (gap + 1) / 2)
                }
                prev = i
            }
        }
        if (prev != -1) {
            ans = math.max(ans, n - 1 - prev)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_dist_to_closest(seats: Vec<i32>) -> i32 {
        let n = seats.len();
        let mut prev_one: isize = -1;
        let mut max_dist: usize = 0;
        for (i, &s) in seats.iter().enumerate() {
            if s == 1 {
                if prev_one == -1 {
                    // leading zeros
                    max_dist = i.max(max_dist);
                } else {
                    let gap = i as isize - prev_one - 1; // zeros between two occupied seats
                    let cand = ((gap + 1) / 2) as usize;
                    if cand > max_dist {
                        max_dist = cand;
                    }
                }
                prev_one = i as isize;
            }
        }
        // trailing zeros
        if prev_one != -1 {
            let tail = n as isize - 1 - prev_one;
            if (tail as usize) > max_dist {
                max_dist = tail as usize;
            }
        }
        max_dist as i32
    }
}
```

## Racket

```racket
(define/contract (max-dist-to-closest seats)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length seats))
         (ans 0)
         (prev -1))
    (for ([s seats] [idx (in-naturals)])
      (when (= s 1)
        (if (= prev -1)
            (set! ans (max ans idx)) ; leading zeros
            (let* ((gap (- idx prev 1))
                   (cand (quotient (+ gap 1) 2)))
              (set! ans (max ans cand))))
        (set! prev idx)))
    (let ((tail (- n prev 1))) ; trailing zeros after last occupied seat
      (when (> tail 0)
        (set! ans (max ans tail))))
    ans))
```

## Erlang

```erlang
-spec max_dist_to_closest(Seats :: [integer()]) -> integer().
max_dist_to_closest(Seats) ->
    N = length(Seats),
    max_dist_to_closest(Seats, 0, -1, 0, N).

max_dist_to_closest([], _Idx, Prev, MaxDist, N) ->
    case Prev of
        -1 -> MaxDist;
        _ ->
            Trailing = N - 1 - Prev,
            erlang:max(MaxDist, Trailing)
    end;
max_dist_to_closest([Seat|Rest], Idx, Prev, MaxDist, N) ->
    if Seat == 1 ->
            NewMax =
                case Prev of
                    -1 -> erlang:max(MaxDist, Idx);
                    _ ->
                        Gap = Idx - Prev - 1,
                        Candidate = (Gap + 1) div 2,
                        erlang:max(MaxDist, Candidate)
                end,
            max_dist_to_closest(Rest, Idx + 1, Idx, NewMax, N);
       true ->
            max_dist_to_closest(Rest, Idx + 1, Prev, MaxDist, N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_dist_to_closest(seats :: [integer]) :: integer
  def max_dist_to_closest(seats) do
    {max, cnt, seen} =
      Enum.reduce(seats, {0, 0, false}, fn seat, {cur_max, cur_cnt, any_seen} ->
        if seat == 0 do
          {cur_max, cur_cnt + 1, any_seen}
        else
          new_max =
            if not any_seen do
              max(cur_cnt, cur_max)
            else
              max(div(cur_cnt + 1, 2), cur_max)
            end

          {new_max, 0, true}
        end
      end)

    if cnt > 0 do
      max(cnt, max)
    else
      max
    end
  end
end
```
