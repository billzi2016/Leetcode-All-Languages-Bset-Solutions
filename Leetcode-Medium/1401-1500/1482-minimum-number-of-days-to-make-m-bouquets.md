# 1482. Minimum Number of Days to Make m Bouquets

## Cpp

```cpp
class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        long long need = 1LL * m * k;
        if (need > (int)bloomDay.size()) return -1;
        int lo = 1, hi = *max_element(bloomDay.begin(), bloomDay.end());
        int ans = -1;
        auto canMake = [&](int day) {
            int bouquets = 0, cnt = 0;
            for (int d : bloomDay) {
                if (d <= day) {
                    ++cnt;
                    if (cnt == k) {
                        ++bouquets;
                        cnt = 0;
                        if (bouquets >= m) return true;
                    }
                } else {
                    cnt = 0;
                }
            }
            return bouquets >= m;
        };
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (canMake(mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        long needed = (long) m * k;
        if (needed > bloomDay.length) return -1;

        int low = 1;
        int high = 0;
        for (int day : bloomDay) {
            if (day > high) high = day;
        }

        int answer = -1;
        while (low <= high) {
            int mid = low + ((high - low) >> 1);
            if (canMake(bloomDay, m, k, mid)) {
                answer = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return answer;
    }

    private boolean canMake(int[] bloomDay, int m, int k, int day) {
        int bouquets = 0;
        int consecutive = 0;
        for (int d : bloomDay) {
            if (d <= day) {
                consecutive++;
                if (consecutive == k) {
                    bouquets++;
                    if (bouquets >= m) return true;
                    consecutive = 0;
                }
            } else {
                consecutive = 0;
            }
        }
        return bouquets >= m;
    }
}
```

## Python

```python
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if m * k > n:
            return -1

        def can_make(day):
            bouquets = 0
            consecutive = 0
            for d in bloomDay:
                if d <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        if bouquets >= m:
                            return True
                        consecutive = 0
                else:
                    consecutive = 0
            return False

        lo, hi = min(bloomDay), max(bloomDay)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def can_make(day: int) -> bool:
            bouquets = 0
            consecutive = 0
            for d in bloomDay:
                if d <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        if bouquets >= m:
                            return True
                        consecutive = 0
                else:
                    consecutive = 0
            return False

        left, right = min(bloomDay), max(bloomDay)
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if can_make(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
```

## C

```c
#include <stddef.h>

static int canMake(int *bloomDay, int bloomDaySize, int m, int k, int day) {
    int bouquets = 0;
    int consecutive = 0;
    for (int i = 0; i < bloomDaySize; ++i) {
        if (bloomDay[i] <= day) {
            ++consecutive;
            if (consecutive == k) {
                ++bouquets;
                if (bouquets >= m) return 1;
                consecutive = 0;
            }
        } else {
            consecutive = 0;
        }
    }
    return bouquets >= m;
}

int minDays(int* bloomDay, int bloomDaySize, int m, int k) {
    long long need = (long long)m * k;
    if (need > bloomDaySize) return -1;

    int low = bloomDay[0];
    int high = bloomDay[0];
    for (int i = 1; i < bloomDaySize; ++i) {
        if (bloomDay[i] < low) low = bloomDay[i];
        if (bloomDay[i] > high) high = bloomDay[i];
    }

    int ans = -1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1);
        if (canMake(bloomDay, bloomDaySize, m, k, mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinDays(int[] bloomDay, int m, int k)
    {
        long need = (long)m * k;
        if (need > bloomDay.Length) return -1;

        int low = 1;
        int high = 0;
        foreach (int d in bloomDay)
            if (d > high) high = d;

        int ans = -1;
        while (low <= high)
        {
            int mid = low + ((high - low) >> 1);
            if (CanMake(bloomDay, m, k, mid))
            {
                ans = mid;
                high = mid - 1;
            }
            else
            {
                low = mid + 1;
            }
        }
        return ans;
    }

    private bool CanMake(int[] bloomDay, int m, int k, int day)
    {
        int bouquets = 0;
        int consecutive = 0;
        foreach (int d in bloomDay)
        {
            if (d <= day)
            {
                consecutive++;
                if (consecutive == k)
                {
                    bouquets++;
                    if (bouquets >= m) return true;
                    consecutive = 0;
                }
            }
            else
            {
                consecutive = 0;
            }
        }
        return bouquets >= m;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} bloomDay
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var minDays = function(bloomDay, m, k) {
    const n = bloomDay.length;
    if (m * k > n) return -1;

    let low = 1;
    let high = Math.max(...bloomDay);
    let answer = -1;

    const canMake = (day) => {
        let bouquets = 0;
        let consecutive = 0;
        for (let i = 0; i < n; ++i) {
            if (bloomDay[i] <= day) {
                consecutive++;
                if (consecutive === k) {
                    bouquets++;
                    if (bouquets >= m) return true;
                    consecutive = 0;
                }
            } else {
                consecutive = 0;
            }
        }
        return false;
    };

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (canMake(mid)) {
            answer = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return answer;
};
```

## Typescript

```typescript
function minDays(bloomDay: number[], m: number, k: number): number {
    const n = bloomDay.length;
    if (m * k > n) return -1;

    let low = Math.min(...bloomDay);
    let high = Math.max(...bloomDay);
    let answer = -1;

    const canMake = (day: number): boolean => {
        let bouquets = 0;
        let consecutive = 0;
        for (let i = 0; i < n; i++) {
            if (bloomDay[i] <= day) {
                consecutive++;
                if (consecutive === k) {
                    bouquets++;
                    if (bouquets >= m) return true;
                    consecutive = 0;
                }
            } else {
                consecutive = 0;
            }
        }
        return false;
    };

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (canMake(mid)) {
            answer = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $bloomDay
     * @param Integer $m
     * @param Integer $k
     * @return Integer
     */
    function minDays($bloomDay, $m, $k) {
        $n = count($bloomDay);
        if ($m * $k > $n) {
            return -1;
        }

        $low = PHP_INT_MAX;
        $high = 0;
        foreach ($bloomDay as $d) {
            if ($d < $low) $low = $d;
            if ($d > $high) $high = $d;
        }

        $ans = -1;
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canMake($bloomDay, $m, $k, $mid)) {
                $ans = $mid;
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }

        return $ans;
    }

    private function canMake($bloomDay, $m, $k, $day) {
        $bouquets = 0;
        $cnt = 0;
        foreach ($bloomDay as $d) {
            if ($d <= $day) {
                $cnt++;
                if ($cnt == $k) {
                    $bouquets++;
                    $cnt = 0;
                    if ($bouquets >= $m) return true;
                }
            } else {
                $cnt = 0;
            }
        }
        return $bouquets >= $m;
    }
}
```

## Swift

```swift
class Solution {
    func minDays(_ bloomDay: [Int], _ m: Int, _ k: Int) -> Int {
        let n = bloomDay.count
        if m * k > n { return -1 }
        
        var low = 1
        var high = bloomDay.max()!
        var answer = -1
        
        while low <= high {
            let mid = (low + high) / 2
            if canMake(bloomDay, m, k, day: mid) {
                answer = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        
        return answer
    }
    
    private func canMake(_ bloomDay: [Int], _ m: Int, _ k: Int, day: Int) -> Bool {
        var bouquets = 0
        var consecutive = 0
        
        for b in bloomDay {
            if b <= day {
                consecutive += 1
                if consecutive == k {
                    bouquets += 1
                    if bouquets >= m { return true }
                    consecutive = 0
                }
            } else {
                consecutive = 0
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDays(bloomDay: IntArray, m: Int, k: Int): Int {
        val n = bloomDay.size
        if (m.toLong() * k > n) return -1

        var low = bloomDay.minOrNull() ?: 0
        var high = bloomDay.maxOrNull() ?: 0
        var answer = -1

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (canMake(bloomDay, m, k, mid)) {
                answer = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }

        return answer
    }

    private fun canMake(days: IntArray, m: Int, k: Int, limit: Int): Boolean {
        var bouquets = 0
        var consecutive = 0
        for (d in days) {
            if (d <= limit) {
                consecutive++
                if (consecutive == k) {
                    bouquets++
                    if (bouquets >= m) return true
                    consecutive = 0
                }
            } else {
                consecutive = 0
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  int minDays(List<int> bloomDay, int m, int k) {
    int n = bloomDay.length;
    if (m * k > n) return -1;

    int lo = bloomDay.reduce((a, b) => a < b ? a : b);
    int hi = bloomDay.reduce((a, b) => a > b ? a : b);
    int ans = -1;

    while (lo <= hi) {
      int mid = lo + ((hi - lo) >> 1);
      if (_canMake(bloomDay, m, k, mid)) {
        ans = mid;
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }

    return ans;
  }

  bool _canMake(List<int> bloomDay, int m, int k, int day) {
    int bouquets = 0;
    int consecutive = 0;

    for (int d in bloomDay) {
      if (d <= day) {
        consecutive++;
        if (consecutive == k) {
          bouquets++;
          if (bouquets >= m) return true;
          consecutive = 0;
        }
      } else {
        consecutive = 0;
      }
    }

    return false;
  }
}
```

## Golang

```go
func minDays(bloomDay []int, m int, k int) int {
	if int64(m)*int64(k) > int64(len(bloomDay)) {
		return -1
	}
	low, high := bloomDay[0], bloomDay[0]
	for _, v := range bloomDay {
		if v < low {
			low = v
		}
		if v > high {
			high = v
		}
	}
	possible := func(day int) bool {
		bouquets, cnt := 0, 0
		for _, v := range bloomDay {
			if v <= day {
				cnt++
				if cnt == k {
					bouquets++
					if bouquets >= m {
						return true
					}
					cnt = 0
				}
			} else {
				cnt = 0
			}
		}
		return false
	}
	for low < high {
		mid := low + (high-low)/2
		if possible(mid) {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}
```

## Ruby

```ruby
# @param {Integer[]} bloom_day
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def min_days(bloom_day, m, k)
  n = bloom_day.length
  return -1 if m * k > n

  low = bloom_day.min
  high = bloom_day.max
  answer = -1

  possible = lambda do |day|
    bouquets = 0
    consecutive = 0
    bloom_day.each do |b|
      if b <= day
        consecutive += 1
        if consecutive == k
          bouquets += 1
          return true if bouquets >= m
          consecutive = 0
        end
      else
        consecutive = 0
      end
    end
    false
  end

  while low <= high
    mid = (low + high) / 2
    if possible.call(mid)
      answer = mid
      high = mid - 1
    else
      low = mid + 1
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
    def minDays(bloomDay: Array[Int], m: Int, k: Int): Int = {
        val n = bloomDay.length
        if (m.toLong * k > n) return -1

        var low = bloomDay.min
        var high = bloomDay.max
        var ans = -1

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (canMake(bloomDay, m, k, mid)) {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }

        ans
    }

    private def canMake(arr: Array[Int], m: Int, k: Int, day: Int): Boolean = {
        var bouquets = 0
        var cnt = 0
        var i = 0
        while (i < arr.length && bouquets < m) {
            if (arr(i) <= day) {
                cnt += 1
                if (cnt == k) {
                    bouquets += 1
                    cnt = 0
                }
            } else {
                cnt = 0
            }
            i += 1
        }
        bouquets >= m
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_days(bloom_day: Vec<i32>, m: i32, k: i32) -> i32 {
        let n = bloom_day.len();
        if (m as i64) * (k as i64) > n as i64 {
            return -1;
        }
        let mut low = *bloom_day.iter().min().unwrap();
        let mut high = *bloom_day.iter().max().unwrap();
        let mut ans = -1;
        while low <= high {
            let mid = low + (high - low) / 2;
            if Self::can_make(mid, &bloom_day, m, k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        ans
    }

    fn can_make(days: i32, bloom_day: &[i32], m: i32, k: i32) -> bool {
        let mut bouquets = 0;
        let mut consecutive = 0;
        for &d in bloom_day.iter() {
            if d <= days {
                consecutive += 1;
                if consecutive == k {
                    bouquets += 1;
                    if bouquets >= m {
                        return true;
                    }
                    consecutive = 0;
                }
            } else {
                consecutive = 0;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (min-days bloomDay m k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (if (< (length bloomDay) (* m k))
      -1
      (let* ((max-day (apply max bloomDay))
             (can-make?
               (lambda (day)
                 (let-values ([(bouquets cnt)
                               (for/fold ([b 0] [c 0]) ([d bloomDay])
                                 (if (<= d day)
                                     (let ((nc (+ c 1)))
                                       (if (= nc k) (values (+ b 1) 0) (values b nc)))
                                     (values b 0)))])
                   (>= bouquets m))))
             (binary-search
               (let loop ((l 0) (r max-day) (best #f))
                 (if (> l r)
                     best
                     (let ((mid (quotient (+ l r) 2)))
                       (if (can-make? mid)
                           (loop l (- mid 1) mid)
                           (loop (+ mid 1) r best)))))))
        (binary-search))))
```

## Erlang

```erlang
-module(solution).
-export([min_days/3]).

-spec min_days(BloomDay :: [integer()], M :: integer(), K :: integer()) -> integer().
min_days(BloomDay, M, K) ->
    N = length(BloomDay),
    case N < M * K of
        true -> -1;
        false ->
            Max = lists:max(BloomDay),
            bs(1, Max, BloomDay, K, M, -1)
    end.

-spec bs(Low :: integer(), High :: integer(),
         BloomDay :: [integer()], K :: integer(),
         M :: integer(), Ans :: integer()) -> integer().
bs(Low, High, _BloomDay, _K, _M, Ans) when Low > High ->
    Ans;
bs(Low, High, BloomDay, K, M, Ans) ->
    Mid = (Low + High) div 2,
    case can_make(Mid, BloomDay, K, M) of
        true -> bs(Low, Mid - 1, BloomDay, K, M, Mid);
        false -> bs(Mid + 1, High, BloomDay, K, M, Ans)
    end.

-spec can_make(Day :: integer(), BloomDay :: [integer()], K :: integer(), M :: integer()) -> boolean().
can_make(Day, BloomDay, K, M) ->
    can_make(BloomDay, Day, K, 0, 0, M).

-spec can_make(List :: [integer()], Day :: integer(),
               K :: integer(), Count :: integer(),
               Bouquets :: integer(), M :: integer()) -> boolean().
can_make(_List, _Day, _K, _Count, Bouquets, M) when Bouquets >= M ->
    true;
can_make([], _Day, _K, _Count, _Bouquets, _M) ->
    false;
can_make([H|T], Day, K, Count, Bouquets, M) ->
    NewCount = if H =< Day -> Count + 1; true -> 0 end,
    case NewCount of
        C when C == K ->
            can_make(T, Day, K, 0, Bouquets + 1, M);
        _ ->
            can_make(T, Day, K, NewCount, Bouquets, M)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_days(bloom_day :: [integer], m :: integer, k :: integer) :: integer
  def min_days(bloom_day, m, k) do
    n = length(bloom_day)

    if m * k > n do
      -1
    else
      low = Enum.min(bloom_day)
      high = Enum.max(bloom_day)

      case search(bloom_day, m, k, low, high) do
        nil -> -1
        ans -> ans
      end
    end
  end

  defp can_make?(bloom_day, day, m, k) do
    {_cnt, bouquets} =
      Enum.reduce(bloom_day, {0, 0}, fn val, {cnt, bouq} ->
        if val <= day do
          cnt = cnt + 1

          if cnt == k do
            {0, bouq + 1}
          else
            {cnt, bouq}
          end
        else
          {0, bouq}
        end
      end)

    bouquets >= m
  end

  defp search(_bloom_day, _m, _k, low, high) when low > high, do: nil

  defp search(bloom_day, m, k, low, high) do
    mid = div(low + high, 2)

    if can_make?(bloom_day, mid, m, k) do
      case search(bloom_day, m, k, low, mid - 1) do
        nil -> mid
        earlier -> earlier
      end
    else
      search(bloom_day, m, k, mid + 1, high)
    end
  end
end
```
