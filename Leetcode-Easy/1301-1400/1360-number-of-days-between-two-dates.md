# 1360. Number of Days Between Two Dates

## Cpp

```cpp
class Solution {
public:
    bool isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }
    
    int daysSince1970(const string& date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8, 2));
        
        static const int mdays[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
        int days = 0;
        for (int y = 1970; y < year; ++y) {
            days += isLeap(y) ? 366 : 365;
        }
        for (int m = 1; m < month; ++m) {
            if (m == 2 && isLeap(year))
                days += 29;
            else
                days += mdays[m - 1];
        }
        days += day - 1; // Jan 1 -> offset 0
        return days;
    }
    
    int daysBetweenDates(string date1, string date2) {
        int d1 = daysSince1970(date1);
        int d2 = daysSince1970(date2);
        return abs(d1 - d2);
    }
};
```

## Java

```java
class Solution {
    public int daysBetweenDates(String date1, String date2) {
        return Math.abs(toDays(date1) - toDays(date2));
    }

    private int toDays(String date) {
        int year = Integer.parseInt(date.substring(0, 4));
        int month = Integer.parseInt(date.substring(5, 7));
        int day = Integer.parseInt(date.substring(8, 10));

        int days = 0;
        for (int y = 1970; y < year; ++y) {
            days += isLeap(y) ? 366 : 365;
        }

        int[] dim = {31,28,31,30,31,30,31,31,30,31,30,31};
        for (int m = 1; m < month; ++m) {
            days += dim[m - 1];
            if (m == 2 && isLeap(year)) {
                days += 1;
            }
        }

        days += day - 1; // exclude current day
        return days;
    }

    private boolean isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }
}
```

## Python

```python
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        def is_leap(y):
            return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days_from_epoch(date):
            y, m, d = map(int, date.split('-'))
            total = 0
            for yr in range(1970, y):
                total += 366 if is_leap(yr) else 365
            for i in range(1, m):
                total += month_days[i - 1]
                if i == 2 and is_leap(y):
                    total += 1
            total += d - 1
            return total

        return abs(days_from_epoch(date1) - days_from_epoch(date2))
```

## Python3

```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(y: int) -> bool:
            return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

        def to_days(date: str) -> int:
            y = int(date[0:4])
            m = int(date[5:7])
            d = int(date[8:10])

            days = 0
            for year in range(1900, y):
                days += 366 if is_leap(year) else 365

            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if is_leap(y):
                month_days[1] = 29
            for month in range(1, m):
                days += month_days[month - 1]

            days += d - 1  # exclude current day
            return days

        return abs(to_days(date1) - to_days(date2))
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

static int isLeap(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

static int daysFromBase(int y, int m, int d) {
    int days = 0;
    for (int yr = 1900; yr < y; ++yr)
        days += isLeap(yr) ? 366 : 365;

    static const int mdays[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    for (int mo = 1; mo < m; ++mo) {
        if (mo == 2 && isLeap(y))
            days += 29;
        else
            days += mdays[mo - 1];
    }
    days += d - 1; // exclude current day
    return days;
}

int daysBetweenDates(char* date1, char* date2) {
    int y1, m1, d1;
    int y2, m2, d2;
    sscanf(date1, "%d-%d-%d", &y1, &m1, &d1);
    sscanf(date2, "%d-%d-%d", &y2, &m2, &d2);

    int days1 = daysFromBase(y1, m1, d1);
    int days2 = daysFromBase(y2, m2, d2);
    return abs(days1 - days2);
}
```

## Csharp

```csharp
public class Solution {
    public int DaysBetweenDates(string date1, string date2) {
        var d1 = DateTime.ParseExact(date1, "yyyy-MM-dd", System.Globalization.CultureInfo.InvariantCulture);
        var d2 = DateTime.ParseExact(date2, "yyyy-MM-dd", System.Globalization.CultureInfo.InvariantCulture);
        return Math.Abs((d1 - d2).Days);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} date1
 * @param {string} date2
 * @return {number}
 */
var daysBetweenDates = function(date1, date2) {
    const toMs = (d) => {
        const [y, m, day] = d.split('-').map(Number);
        return Date.UTC(y, m - 1, day);
    };
    const diff = Math.abs(toMs(date1) - toMs(date2));
    return diff / (1000 * 60 * 60 * 24);
};
```

## Typescript

```typescript
function daysBetweenDates(date1: string, date2: string): number {
    const isLeap = (year: number): boolean => {
        return (year % 400 === 0) || (year % 4 === 0 && year % 100 !== 0);
    };

    const daysFromBase = (date: string): number => {
        const [yStr, mStr, dStr] = date.split('-');
        const year = parseInt(yStr, 10);
        const month = parseInt(mStr, 10);
        const day = parseInt(dStr, 10);

        let days = 0;
        // base year chosen as 1971 (minimum possible year)
        for (let y = 1971; y < year; ++y) {
            days += isLeap(y) ? 366 : 365;
        }

        const monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        for (let m = 1; m < month; ++m) {
            if (m === 2 && isLeap(year)) {
                days += 29;
            } else {
                days += monthDays[m - 1];
            }
        }

        days += day - 1; // exclude the current day
        return days;
    };

    return Math.abs(daysFromBase(date1) - daysFromBase(date2));
}
```

## Php

```php
class Solution {

    /**
     * @param String $date1
     * @param String $date2
     * @return Integer
     */
    function daysBetweenDates($date1, $date2) {
        return abs($this->daysFromBase($date1) - $this->daysFromBase($date2));
    }

    private function isLeap(int $year): bool {
        return ($year % 400 === 0) || ($year % 4 === 0 && $year % 100 !== 0);
    }

    private function daysFromBase(string $date): int {
        [$y, $m, $d] = array_map('intval', explode('-', $date));
        $days = 0;
        for ($year = 1971; $year < $y; $year++) {
            $days += $this->isLeap($year) ? 366 : 365;
        }
        $monthDays = [31,28,31,30,31,30,31,31,30,31,30,31];
        if ($this->isLeap($y)) {
            $monthDays[1] = 29;
        }
        for ($i = 0; $i < $m - 1; $i++) {
            $days += $monthDays[$i];
        }
        $days += $d - 1; // exclude current day
        return $days;
    }
}
```

## Swift

```swift
class Solution {
    func daysBetweenDates(_ date1: String, _ date2: String) -> Int {
        let d1 = totalDays(date1)
        let d2 = totalDays(date2)
        return abs(d1 - d2)
    }
    
    private func totalDays(_ date: String) -> Int {
        let parts = date.split(separator: "-")
        let year = Int(parts[0])!
        let month = Int(parts[1])!
        let day = Int(parts[2])!
        
        var days = 0
        for y in 1900..<year {
            days += isLeap(y) ? 366 : 365
        }
        
        let monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        for m in 1..<month {
            if m == 2 && isLeap(year) {
                days += 29
            } else {
                days += monthDays[m - 1]
            }
        }
        
        days += day - 1
        return days
    }
    
    private func isLeap(_ year: Int) -> Bool {
        if year % 400 == 0 { return true }
        if year % 100 == 0 { return false }
        return year % 4 == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun daysBetweenDates(date1: String, date2: String): Int {
        val d1 = java.time.LocalDate.parse(date1)
        val d2 = java.time.LocalDate.parse(date2)
        return kotlin.math.abs(java.time.temporal.ChronoUnit.DAYS.between(d1, d2).toInt())
    }
}
```

## Dart

```dart
class Solution {
  int daysBetweenDates(String date1, String date2) {
    final d1 = DateTime.parse(date1);
    final d2 = DateTime.parse(date2);
    return (d1.difference(d2).inDays).abs();
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func isLeap(year int) bool {
	if year%400 == 0 {
		return true
	}
	if year%100 == 0 {
		return false
	}
	return year%4 == 0
}

func daysSinceStart(date string) int {
	parts := strings.Split(date, "-")
	y, _ := strconv.Atoi(parts[0])
	m, _ := strconv.Atoi(parts[1])
	d, _ := strconv.Atoi(parts[2])

	days := 0
	for yr := 1970; yr < y; yr++ {
		if isLeap(yr) {
			days += 366
		} else {
			days += 365
		}
	}

	monthDays := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	for i := 1; i < m; i++ {
		if i == 2 && isLeap(y) {
			days += 29
		} else {
			days += monthDays[i-1]
		}
	}

	days += d - 1
	return days
}

func daysBetweenDates(date1 string, date2 string) int {
	diff := daysSinceStart(date1) - daysSinceStart(date2)
	if diff < 0 {
		diff = -diff
	}
	return diff
}
```

## Ruby

```ruby
def days_between_dates(date1, date2)
  def leap_year?(year)
    (year % 400).zero? || ((year % 4).zero? && (year % 100 != 0))
  end

  def days_until(date)
    year, month, day = date.split('-').map(&:to_i)

    # days from year 1971 to the previous year
    days = 0
    (1971...year).each do |y|
      days += leap_year?(y) ? 366 : 365
    end

    # days for months before the given month in the current year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days[1] = 29 if leap_year?(year)
    (0...(month - 1)).each do |i|
      days += month_days[i]
    end

    # add days in current month (subtract 1 to make Jan 1 => 0)
    days + day - 1
  end

  (days_until(date1) - days_until(date2)).abs
end
```

## Scala

```scala
object Solution {
    def daysBetweenDates(date1: String, date2: String): Int = {
        val monthDays = Array(31,28,31,30,31,30,31,31,30,31,30,31)

        def isLeap(y: Int): Boolean =
            (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)

        def daysSinceBase(date: String): Int = {
            val parts = date.split("-")
            val year = parts(0).toInt
            val month = parts(1).toInt
            val day = parts(2).toInt

            var days = 0
            // years before the given year
            for (y <- 1970 until year) {
                days += if (isLeap(y)) 366 else 365
            }
            // months before the given month in current year
            for (m <- 1 until month) {
                days += monthDays(m - 1)
                if (m == 2 && isLeap(year)) days += 1
            }
            // days before the given day
            days + (day - 1)
        }

        math.abs(daysSinceBase(date1) - daysSinceBase(date2))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn days_between_dates(date1: String, date2: String) -> i32 {
        fn is_leap(y: i32) -> bool {
            (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)
        }

        fn days_until(y: i32, m: i32, d: i32) -> i32 {
            let mut days = 0;
            for year in 1971..y {
                days += if is_leap(year) { 366 } else { 365 };
            }
            // days in months
            const MDAYS: [i32; 12] = [31,28,31,30,31,30,31,31,30,31,30,31];
            for month in 1..m {
                days += MDAYS[(month - 1) as usize];
                if month == 2 && is_leap(y) {
                    days += 1;
                }
            }
            days + (d - 1)
        }

        let parse = |s: String| -> (i32, i32, i32) {
            let parts: Vec<i32> = s.split('-')
                                   .map(|p| p.parse::<i32>().unwrap())
                                   .collect();
            (parts[0], parts[1], parts[2])
        };

        let (y1, m1, d1) = parse(date1);
        let (y2, m2, d2) = parse(date2);

        let days1 = days_until(y1, m1, d1);
        let days2 = days_until(y2, m2, d2);
        (days1 - days2).abs()
    }
}
```

## Racket

```racket
#lang racket

(define (parse-date s)
  (list (string->number (substring s 0 4))
        (string->number (substring s 5 7))
        (string->number (substring s 8 10))))

(define (leap-year? y)
  (or (= (modulo y 400) 0)
      (and (= (modulo y 4) 0) (not (= (modulo y 100) 0)))))

(define (month-days m y)
  (cond [(member m '(1 3 5 7 8 10 12)) 31]
        [(member m '(4 6 9 11)) 30]
        [else (if (leap-year? y) 29 28)]))

(define (days-up-to-year y)
  (let loop ([cur 1970] [acc 0])
    (if (= cur y) acc
        (loop (+ cur 1) (+ acc (if (leap-year? cur) 366 365))))))

(define (days-up-to-month m y)
  (let loop ([cur 1] [acc 0])
    (if (= cur m) acc
        (loop (+ cur 1) (+ acc (month-days cur y))))))

(define (total-days d)
  (match-define (list yr mo da) d)
  (+ (days-up-to-year yr)
     (days-up-to-month mo yr)
     (- da 1)))

(define/contract (days-between-dates date1 date2)
  (-> string? string? exact-integer?)
  (let* ([t1 (total-days (parse-date date1))]
         [t2 (total-days (parse-date date2))])
    (abs (- t1 t2))))
```

## Erlang

```erlang
-spec days_between_dates(Date1 :: unicode:unicode_binary(), Date2 :: unicode:unicode_binary()) -> integer().
days_between_dates(Date1, Date2) ->
    {Y1,M1,D1} = parse_date(Date1),
    {Y2,M2,D2} = parse_date(Date2),
    Days1 = days_from_1970(Y1,M1,D1),
    Days2 = days_from_1970(Y2,M2,D2),
    abs(Days1 - Days2).

parse_date(Date) ->
    [YBin, MBin, DBin] = binary:split(Date, <<"-">>, [global]),
    {binary_to_integer(YBin), binary_to_integer(MBin), binary_to_integer(DBin)}.

days_from_1970(Year, Month, Day) ->
    YearsDays = years_days(1970, Year - 1),
    MonthsDays = months_days(Year, Month - 1),
    YearsDays + MonthsDays + (Day - 1).

years_days(Cur, End) when Cur > End -> 0;
years_days(Cur, End) ->
    DaysInYear = if is_leap(Cur) -> 366; true -> 365 end,
    DaysInYear + years_days(Cur + 1, End).

months_days(_Year, 0) -> 0;
months_days(Year, N) ->
    MonthLengths = [31,28,31,30,31,30,31,31,30,31,30,31],
    Len0 = lists:nth(N, MonthLengths),
    Len = if N == 2 andalso is_leap(Year) -> Len0 + 1; true -> Len0 end,
    Len + months_days(Year, N - 1).

is_leap(Year) ->
    (Year rem 4 =:= 0 andalso Year rem 100 =/= 0) orelse (Year rem 400 =:= 0).
```

## Elixir

```elixir
defmodule Solution do
  @spec days_between_dates(String.t(), String.t()) :: integer()
  def days_between_dates(date1, date2) do
    d1 = parse(date1)
    d2 = parse(date2)

    diff = days_until(d1) - days_until(d2)
    if diff < 0, do: -diff, else: diff
  end

  defp parse(str) do
    [y, m, d] = String.split(str, "-") |> Enum.map(&String.to_integer/1)
    {y, m, d}
  end

  defp leap?(year) do
    (rem(year, 4) == 0 and rem(year, 100) != 0) or rem(year, 400) == 0
  end

  defp days_until({year, month, day}) do
    years_days =
      Enum.reduce(1970..(year - 1), 0, fn y, acc ->
        acc + if leap?(y), do: 366, else: 365
      end)

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_sum = month_days |> Enum.take(month - 1) |> Enum.sum()
    months_sum = if leap?(year) and month > 2, do: months_sum + 1, else: months_sum

    years_days + months_sum + (day - 1)
  end
end
```
