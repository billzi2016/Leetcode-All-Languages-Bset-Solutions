# 2409. Count Days Spent Together

## Cpp

```cpp
class Solution {
public:
    int toDay(const string& date) {
        static const int monthDays[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
        int month = stoi(date.substr(0,2));
        int day = stoi(date.substr(3,2));
        int res = day;
        for (int m = 1; m < month; ++m) res += monthDays[m];
        return res;
    }
    
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int aStart = toDay(arriveAlice);
        int aEnd   = toDay(leaveAlice);
        int bStart = toDay(arriveBob);
        int bEnd   = toDay(leaveBob);
        
        int start = max(aStart, bStart);
        int end   = min(aEnd, bEnd);
        if (start > end) return 0;
        return end - start + 1;
    }
};
```

## Java

```java
class Solution {
    private static final int[] DAYS_IN_MONTH = {31,28,31,30,31,30,31,31,30,31,30,31};

    private int dayOfYear(String date) {
        int month = Integer.parseInt(date.substring(0, 2));
        int day = Integer.parseInt(date.substring(3, 5));
        int sum = 0;
        for (int i = 1; i < month; i++) {
            sum += DAYS_IN_MONTH[i - 1];
        }
        return sum + day;
    }

    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int aA = dayOfYear(arriveAlice);
        int lA = dayOfYear(leaveAlice);
        int aB = dayOfYear(arriveBob);
        int lB = dayOfYear(leaveBob);

        int start = Math.max(aA, aB);
        int end = Math.min(lA, lB);
        return start > end ? 0 : (end - start + 1);
    }
}
```

## Python

```python
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for d in month_days:
            prefix.append(prefix[-1] + d)

        def to_day(date):
            m, d = map(int, date.split('-'))
            return prefix[m - 1] + d

        a_start = to_day(arriveAlice)
        a_end = to_day(leaveAlice)
        b_start = to_day(arriveBob)
        b_end = to_day(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)
        return max(0, end - start + 1)
```

## Python3

```python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for d in month_days:
            prefix.append(prefix[-1] + d)

        def to_day(date: str) -> int:
            m, d = map(int, date.split('-'))
            return prefix[m - 1] + d

        a_start = to_day(arriveAlice)
        a_end = to_day(leaveAlice)
        b_start = to_day(arriveBob)
        b_end = to_day(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        return max(0, end - start + 1)
```

## C

```c
#include <stddef.h>

static int dayOfYear(const char *date) {
    // date format "MM-DD"
    int month = (date[0] - '0') * 10 + (date[1] - '0');
    int day   = (date[3] - '0') * 10 + (date[4] - '0');

    static const int prefixDays[13] = {
        0,   // before January
        0,   // before February (31 days of Jan)
        31,  // before March
        59,  // before April
        90,  // before May
        120, // before June
        151, // before July
        181, // before August
        212, // before September
        243, // before October
        273, // before November
        304, // before December
        334  // after December (unused)
    };
    return prefixDays[month] + day;
}

int countDaysTogether(char* arriveAlice, char* leaveAlice, char* arriveBob, char* leaveBob) {
    int startA = dayOfYear(arriveAlice);
    int endA   = dayOfYear(leaveAlice);
    int startB = dayOfYear(arriveBob);
    int endB   = dayOfYear(leaveBob);

    int startOverlap = startA > startB ? startA : startB;
    int endOverlap   = endA < endB ? endA : endB;

    if (startOverlap > endOverlap) return 0;
    return endOverlap - startOverlap + 1;
}
```

## Csharp

```csharp
public class Solution {
    private static readonly int[] monthDays = new int[] {31,28,31,30,31,30,31,31,30,31,30,31};

    private int ToDayOfYear(string date) {
        int month = int.Parse(date.Substring(0, 2));
        int day = int.Parse(date.Substring(3, 2));
        int total = 0;
        for (int i = 0; i < month - 1; i++) {
            total += monthDays[i];
        }
        total += day;
        return total;
    }

    public int CountDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int aStart = ToDayOfYear(arriveAlice);
        int aEnd   = ToDayOfYear(leaveAlice);
        int bStart = ToDayOfYear(arriveBob);
        int bEnd   = ToDayOfYear(leaveBob);

        int start = Math.Max(aStart, bStart);
        int end   = Math.Min(aEnd, bEnd);

        return Math.Max(0, end - start + 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob) {
    const monthDays = [31,28,31,30,31,30,31,31,30,31,30,31];
    
    const toDayOfYear = (date) => {
        const [mStr, dStr] = date.split('-');
        const month = parseInt(mStr, 10);
        const day = parseInt(dStr, 10);
        let sum = 0;
        for (let i = 0; i < month - 1; i++) {
            sum += monthDays[i];
        }
        return sum + day;
    };
    
    const aStart = toDayOfYear(arriveAlice);
    const aEnd   = toDayOfYear(leaveAlice);
    const bStart = toDayOfYear(arriveBob);
    const bEnd   = toDayOfYear(leaveBob);
    
    const start = Math.max(aStart, bStart);
    const end   = Math.min(aEnd, bEnd);
    
    return start > end ? 0 : end - start + 1;
};
```

## Typescript

```typescript
function countDaysTogether(arriveAlice: string, leaveAlice: string, arriveBob: string, leaveBob: string): number {
    const monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const prefix = new Array(13).fill(0);
    for (let i = 1; i <= 12; i++) {
        prefix[i] = prefix[i - 1] + monthDays[i - 1];
    }
    const toDayOfYear = (date: string): number => {
        const [mStr, dStr] = date.split('-');
        const m = parseInt(mStr, 10);
        const d = parseInt(dStr, 10);
        return prefix[m - 1] + d;
    };
    const aStart = toDayOfYear(arriveAlice);
    const aEnd = toDayOfYear(leaveAlice);
    const bStart = toDayOfYear(arriveBob);
    const bEnd = toDayOfYear(leaveBob);
    const start = Math.max(aStart, bStart);
    const end = Math.min(aEnd, bEnd);
    return start > end ? 0 : end - start + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $arriveAlice
     * @param String $leaveAlice
     * @param String $arriveBob
     * @param String $leaveBob
     * @return Integer
     */
    function countDaysTogether($arriveAlice, $leaveAlice, $arriveBob, $leaveBob) {
        $monthDays = [31,28,31,30,31,30,31,31,30,31,30,31];
        
        $toDayOfYear = function($date) use ($monthDays) {
            list($m, $d) = array_map('intval', explode('-', $date));
            $day = 0;
            for ($i = 0; $i < $m - 1; $i++) {
                $day += $monthDays[$i];
            }
            $day += $d;
            return $day;
        };
        
        $aStart = $toDayOfYear($arriveAlice);
        $aEnd   = $toDayOfYear($leaveAlice);
        $bStart = $toDayOfYear($arriveBob);
        $bEnd   = $toDayOfYear($leaveBob);
        
        $start = max($aStart, $bStart);
        $end   = min($aEnd, $bEnd);
        
        return ($start > $end) ? 0 : ($end - $start + 1);
    }
}
```

## Swift

```swift
class Solution {
    private let monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    private func dayOfYear(_ date: String) -> Int {
        let parts = date.split(separator: "-")
        let month = Int(parts[0])!
        let day = Int(parts[1])!
        var total = 0
        for i in 0..<(month - 1) {
            total += monthDays[i]
        }
        total += day
        return total
    }
    
    func countDaysTogether(_ arriveAlice: String, _ leaveAlice: String, _ arriveBob: String, _ leaveBob: String) -> Int {
        let aStart = dayOfYear(arriveAlice)
        let aEnd = dayOfYear(leaveAlice)
        let bStart = dayOfYear(arriveBob)
        let bEnd = dayOfYear(leaveBob)
        
        let start = max(aStart, bStart)
        let end = min(aEnd, bEnd)
        if start > end {
            return 0
        }
        return end - start + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val monthDays = intArrayOf(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    private fun dayOfYear(date: String): Int {
        val parts = date.split("-")
        val month = parts[0].toInt()
        val day = parts[1].toInt()
        var sum = 0
        for (i in 0 until month - 1) {
            sum += monthDays[i]
        }
        return sum + day
    }

    fun countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int {
        val aStart = dayOfYear(arriveAlice)
        val aEnd = dayOfYear(leaveAlice)
        val bStart = dayOfYear(arriveBob)
        val bEnd = dayOfYear(leaveBob)

        val start = maxOf(aStart, bStart)
        val end = minOf(aEnd, bEnd)
        return if (start > end) 0 else end - start + 1
    }
}
```

## Dart

```dart
class Solution {
  int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
    int dayOfYear(String date) {
      int month = int.parse(date.substring(0, 2));
      int day = int.parse(date.substring(3, 5));
      const List<int> daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
      int sum = 0;
      for (int i = 0; i < month - 1; i++) {
        sum += daysInMonth[i];
      }
      return sum + day;
    }

    int startAlice = dayOfYear(arriveAlice);
    int endAlice = dayOfYear(leaveAlice);
    int startBob = dayOfYear(arriveBob);
    int endBob = dayOfYear(leaveBob);

    int overlapStart = startAlice > startBob ? startAlice : startBob;
    int overlapEnd = endAlice < endBob ? endAlice : endBob;

    if (overlapStart > overlapEnd) return 0;
    return overlapEnd - overlapStart + 1;
  }
}
```

## Golang

```go
func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
	monthDays := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	toDay := func(s string) int {
		m := int(s[0]-'0')*10 + int(s[1]-'0')
		d := int(s[3]-'0')*10 + int(s[4]-'0')
		day := d
		for i := 0; i < m-1; i++ {
			day += monthDays[i]
		}
		return day
	}

	startAlice := toDay(arriveAlice)
	endAlice := toDay(leaveAlice)
	startBob := toDay(arriveBob)
	endBob := toDay(leaveBob)

	start := startAlice
	if startBob > start {
		start = startBob
	}
	end := endAlice
	if endBob < end {
		end = endBob
	}

	if start > end {
		return 0
	}
	return end - start + 1
}
```

## Ruby

```ruby
def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob)
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  parse_day = lambda do |date|
    month = date[0, 2].to_i
    day   = date[3, 2].to_i
    days_before = days_in_month[0...(month - 1)].inject(0, :+)
    days_before + day
  end

  a_start = parse_day.call(arrive_alice)
  a_end   = parse_day.call(leave_alice)
  b_start = parse_day.call(arrive_bob)
  b_end   = parse_day.call(leave_bob)

  start_day = [a_start, b_start].max
  end_day   = [a_end, b_end].min

  return 0 if start_day > end_day
  end_day - start_day + 1
end
```

## Scala

```scala
object Solution {
  private val monthDays = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

  private def toDay(date: String): Int = {
    val month = date.substring(0, 2).toInt
    val day   = date.substring(3, 5).toInt
    var sum = 0
    for (i <- 0 until month - 1) sum += monthDays(i)
    sum + day
  }

  def countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int = {
    val aStart = toDay(arriveAlice)
    val aEnd   = toDay(leaveAlice)
    val bStart = toDay(arriveBob)
    val bEnd   = toDay(leaveBob)

    val start = math.max(aStart, bStart)
    val end   = math.min(aEnd, bEnd)

    if (start > end) 0 else end - start + 1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_days_together(arrive_alice: String, leave_alice: String, arrive_bob: String, leave_bob: String) -> i32 {
        fn day_of_year(date: &str) -> i32 {
            let parts: Vec<&str> = date.split('-').collect();
            let month: usize = parts[0].parse().unwrap();
            let day: i32 = parts[1].parse().unwrap();
            const MONTH_DAYS: [i32; 12] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
            let mut sum = 0;
            for i in 0..month - 1 {
                sum += MONTH_DAYS[i];
            }
            sum + day
        }

        let a_start = day_of_year(&arrive_alice);
        let a_end = day_of_year(&leave_alice);
        let b_start = day_of_year(&arrive_bob);
        let b_end = day_of_year(&leave_bob);

        let start = a_start.max(b_start);
        let end = a_end.min(b_end);
        if start > end {
            0
        } else {
            (end - start + 1) as i32
        }
    }
}
```

## Racket

```racket
(define month-days '#(31 28 31 30 31 30 31 31 30 31 30 31))

(define (date->day s)
  (let* ((month (string->number (substring s 0 2)))
         (day   (string->number (substring s 3 5))))
    (+ day
       (for/sum ([i (in-range 1 month)])
         (vector-ref month-days (- i 1))))))

(define/contract (count-days-together arriveAlice leaveAlice arriveBob leaveBob)
  (-> string? string? string? string? exact-integer?)
  (let* ((a-start (date->day arriveAlice))
         (a-end   (date->day leaveAlice))
         (b-start (date->day arriveBob))
         (b-end   (date->day leaveBob))
         (start (max a-start b-start))
         (end   (min a-end b-end)))
    (if (<= start end)
        (+ 1 (- end start))
        0)))
```

## Erlang

```erlang
-module(solution).
-export([count_days_together/4]).

-spec count_days_together(ArriveAlice :: unicode:unicode_binary(),
                          LeaveAlice :: unicode:unicode_binary(),
                          ArriveBob :: unicode:unicode_binary(),
                          LeaveBob :: unicode:unicode_binary()) -> integer().
count_days_together(ArriveAlice, LeaveAlice, ArriveBob, LeaveBob) ->
    StartA = date_to_day(ArriveAlice),
    EndA   = date_to_day(LeaveAlice),
    StartB = date_to_day(ArriveBob),
    EndB   = date_to_day(LeaveBob),

    OverlapStart = erlang:max(StartA, StartB),
    OverlapEnd   = erlang:min(EndA, EndB),

    case OverlapStart > OverlapEnd of
        true  -> 0;
        false -> OverlapEnd - OverlapStart + 1
    end.

%% Convert "MM-DD" to day-of-year (1..365)
date_to_day(Date) ->
    [MonthBin, DayBin] = binary:split(Date, <<"-">>, []),
    Month = list_to_integer(binary_to_list(MonthBin)),
    Day   = list_to_integer(binary_to_list(DayBin)),
    DaysBefore = sum_months(Month - 1),
    DaysBefore + Day.

%% Sum days of the first N months (non‑leap year)
sum_months(N) when N =< 0 -> 0;
sum_months(N) ->
    MonthLengths = [31,28,31,30,31,30,31,31,30,31,30,31],
    lists:foldl(fun(X, Acc) -> X + Acc end, 0,
                lists:sublist(MonthLengths, N)).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_days_together(arrive_alice :: String.t(), leave_alice :: String.t(),
                            arrive_bob :: String.t(), leave_bob :: String.t()) :: integer()
  def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob) do
    a_start = day_of_year(arrive_alice)
    a_end   = day_of_year(leave_alice)
    b_start = day_of_year(arrive_bob)
    b_end   = day_of_year(leave_bob)

    start_day = max(a_start, b_start)
    end_day   = min(a_end, b_end)

    if start_day > end_day do
      0
    else
      end_day - start_day + 1
    end
  end

  defp day_of_year(date) do
    [month_str, day_str] = String.split(date, "-")
    {month, _} = Integer.parse(month_str)
    {day, _}   = Integer.parse(day_str)

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_before =
      month
      |> Kernel.-(1)
      |> Enum.take(month_days)
      |> Enum.sum()

    days_before + day
  end
end
```
