# 1185. Day of the Week

## Cpp

```cpp
class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        static const vector<string> names = {"Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"};
        if (month <= 2) {
            month += 12;
            --year;
        }
        int q = day;
        int m = month;
        int K = year % 100;
        int J = year / 100;
        int h = (q + (13 * (m + 1)) / 5 + K + K / 4 + J / 4 + 5 * J) % 7;
        return names[h];
    }
};
```

## Java

```java
class Solution {
    public String dayOfTheWeek(int day, int month, int year) {
        String[] days = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
        // 1971-01-01 was a Friday, which is index 5
        int baseIdx = 5;
        int totalDays = 0;
        for (int y = 1971; y < year; y++) {
            totalDays += isLeap(y) ? 366 : 365;
        }
        int[] monthLen = {31,28,31,30,31,30,31,31,30,31,30,31};
        for (int m = 1; m < month; m++) {
            if (m == 2 && isLeap(year)) {
                totalDays += 29;
            } else {
                totalDays += monthLen[m - 1];
            }
        }
        totalDays += day - 1; // days before the given day
        int idx = (baseIdx + totalDays) % 7;
        return days[idx];
    }

    private boolean isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }
}
```

## Python

```python
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        def is_leap(y):
            return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 0

        # add days for full years before the given year
        for y in range(1971, year):
            total_days += 366 if is_leap(y) else 365

        # add days for months before the given month in the current year
        for m in range(1, month):
            if m == 2 and is_leap(year):
                total_days += 29
            else:
                total_days += days_in_month[m - 1]

        # add days within the month (day-1 because Jan 1 is offset 0)
        total_days += day - 1

        # Jan 1, 1971 was a Friday -> index 5 (Sunday=0)
        weekday_index = (total_days + 5) % 7
        names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return names[weekday_index]
```

## Python3

```python
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        y = year - (month < 3)
        w = (y + y // 4 - y // 100 + y // 400 + t[month - 1] + day) % 7
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][w]
```

## C

```c
char* dayOfTheWeek(int day, int month, int year) {
    int m = month;
    int y = year;
    if (m <= 2) {
        m += 12;
        y -= 1;
    }
    int K = y % 100;
    int J = y / 100;
    int h = (day + (13 * (m + 1)) / 5 + K + K / 4 + J / 4 + 5 * J) % 7;
    static const char* names[] = {
        "Saturday", "Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday"
    };
    return (char*)names[h];
}
```

## Csharp

```csharp
public class Solution {
    public string DayOfTheWeek(int day, int month, int year) {
        string[] week = new string[] { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };
        int[] monthDays = new int[] { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

        bool IsLeap(int y) => (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);

        int days = 0;
        for (int y = 1971; y < year; ++y) {
            days += IsLeap(y) ? 366 : 365;
        }

        for (int m = 1; m < month; ++m) {
            days += monthDays[m - 1];
            if (m == 2 && IsLeap(year)) {
                days += 1;
            }
        }

        days += day - 1; // offset from Jan 1, 1971

        int baseIndex = 5; // Jan 1, 1971 was a Friday
        return week[(baseIndex + days) % 7];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} day
 * @param {number} month
 * @param {number} year
 * @return {string}
 */
var dayOfTheWeek = function(day, month, year) {
    const names = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
    const d = new Date(Date.UTC(year, month - 1, day));
    return names[d.getUTCDay()];
};
```

## Typescript

```typescript
function dayOfTheWeek(day: number, month: number, year: number): string {
    const monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    // 1971-01-01 was a Friday (index 5)
    const baseIdx = 5;

    const leapCount = (y: number): number => Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400);

    const yearsDiff = year - 1971;
    const daysFromYears = yearsDiff * 365 + (leapCount(year - 1) - leapCount(1970));

    let daysFromMonths = 0;
    for (let m = 1; m < month; ++m) {
        if (m === 2 && ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0)) {
            daysFromMonths += 29;
        } else {
            daysFromMonths += monthDays[m - 1];
        }
    }

    const totalDays = daysFromYears + daysFromMonths + (day - 1);
    const idx = (baseIdx + totalDays) % 7;
    return names[idx];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $day
     * @param Integer $month
     * @param Integer $year
     * @return String
     */
    function dayOfTheWeek($day, $month, $year) {
        $daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31];
        $isLeap = function($y) {
            return ($y % 400 == 0) || ($y % 4 == 0 && $y % 100 != 0);
        };
        
        $total = 0;
        for ($y = 1971; $y < $year; $y++) {
            $total += $isLeap($y) ? 366 : 365;
        }
        for ($m = 1; $m < $month; $m++) {
            if ($m == 2 && $isLeap($year)) {
                $total += 29;
            } else {
                $total += $daysInMonth[$m - 1];
            }
        }
        $total += $day - 1; // days passed before the given day
        
        $week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
        $baseIdx = 5; // Jan 1, 1971 was a Friday
        return $week[($baseIdx + $total) % 7];
    }
}
```

## Swift

```swift
class Solution {
    func dayOfTheWeek(_ day: Int, _ month: Int, _ year: Int) -> String {
        var m = month
        var y = year
        if m <= 2 {
            m += 12
            y -= 1
        }
        let q = day
        let K = y % 100
        let J = y / 100
        let h = (q + (13 * (m + 1)) / 5 + K + K / 4 + J / 4 + 5 * J) % 7
        let names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return names[h]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun dayOfTheWeek(day: Int, month: Int, year: Int): String {
        val daysInMonth = intArrayOf(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        fun isLeap(y: Int) = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)

        var total = 0
        for (y in 1971 until year) {
            total += if (isLeap(y)) 366 else 365
        }
        for (m in 1 until month) {
            total += daysInMonth[m - 1]
            if (m == 2 && isLeap(year)) total += 1
        }
        total += day - 1

        val week = arrayOf(
            "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"
        )
        val baseIdx = 5 // Jan 1, 1971 was a Friday
        return week[(baseIdx + total) % 7]
    }
}
```

## Dart

```dart
class Solution {
  String dayOfTheWeek(int day, int month, int year) {
    if (month <= 2) {
      month += 12;
      year -= 1;
    }
    int K = year % 100;
    int J = year ~/ 100;
    int h = (day +
            ((13 * (month + 1)) ~/ 5) +
            K +
            (K ~/ 4) +
            (J ~/ 4) +
            5 * J) %
        7;
    const List<String> days = [
      "Saturday",
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ];
    return days[h];
  }
}
```

## Golang

```go
func dayOfTheWeek(day int, month int, year int) string {
    // Reference: January 1, 1971 was a Friday.
    const referenceIdx = 5 // Friday in days slice below

    days := []string{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
    monthDays := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

    isLeap := func(y int) bool {
        return (y%400 == 0) || (y%4 == 0 && y%100 != 0)
    }

    total := 0

    // Add days for full years before the given year
    for y := 1971; y < year; y++ {
        total += 365
        if isLeap(y) {
            total++
        }
    }

    // Add days for months before the given month in the current year
    for m := 1; m < month; m++ {
        total += monthDays[m-1]
        if m == 2 && isLeap(year) {
            total++ // February in a leap year
        }
    }

    // Add days within the month (zero‑based)
    total += day - 1

    idx := (referenceIdx + total) % 7
    return days[idx]
}
```

## Ruby

```ruby
def day_of_the_week(day, month, year)
  m = month
  y = year
  if m <= 2
    m += 12
    y -= 1
  end
  k = y % 100
  j = y / 100
  h = (day + ((13 * (m + 1)) / 5) + k + (k / 4) + (j / 4) + 5 * j) % 7
  ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][h]
end
```

## Scala

```scala
object Solution {
    def dayOfTheWeek(day: Int, month: Int, year: Int): String = {
        val t = Array(0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
        var y = year
        if (month < 3) y -= 1
        val dow = (y + y / 4 - y / 100 + y / 400 + t(month - 1) + day) % 7
        val names = Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        names(dow)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn day_of_the_week(day: i32, month: i32, year: i32) -> String {
        let (mut m, mut y) = (month, year);
        if m <= 2 {
            m += 12;
            y -= 1;
        }
        let q = day;
        let k = y % 100;
        let j = y / 100;
        let h = (q + ((13 * (m + 1)) / 5) + k + k / 4 + j / 4 + 5 * j) % 7;
        let days = [
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ];
        days[h as usize].to_string()
    }
}
```

## Racket

```racket
(define/contract (day-of-the-week day month year)
  (-> exact-integer? exact-integer? exact-integer? string?)
  (let* ((month-days '#(31 28 31 30 31 30 31 31 30 31 30 31))
         (leap?
          (lambda (y)
            (or (and (= (modulo y 4) 0) (not (= (modulo y 100) 0)))
                (= (modulo y 400) 0))))
         ;; days in months before the given month
         (month-sum
          (let loop ((i 0) (sum 0))
            (if (= i (- month 1))
                sum
                (loop (+ i 1) (+ sum (vector-ref month-days i))))))
         (days-before-month
          (+ month-sum (if (and (leap? year) (> month 2)) 1 0)))
         (total-years (- year 1971))
         (leap-count-up-to
          (lambda (y)
            (- (+ (quotient y 4) (quotient y 400)) (quotient y 100))))
         (leaps (- (leap-count-up-to (- year 1)) (leap-count-up-to 1970)))
         (days-from-years (+ (* total-years 365) leaps))
         (total-days (+ days-from-years days-before-month (- day 1)))
         (weekday-index (modulo (+ 5 total-days) 7))
         (names '#("Sunday" "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday")))
    (vector-ref names weekday-index)))
```

## Erlang

```erlang
-spec day_of_the_week(Day :: integer(), Month :: integer(), Year :: integer()) -> unicode:unicode_binary().
day_of_the_week(Day, Month, Year) ->
    % reference: Jan 1, 1971 is Friday (index 5, where Sunday=0)
    RefOffset = 5,
    DaysBeforeYear = (Year - 1971) * 365 + leap_count(1971, Year - 1),
    DaysBeforeMonth = days_before_month(Month, is_leap(Year)),
    TotalDays = DaysBeforeYear + DaysBeforeMonth + (Day - 1),
    Index = (TotalDays + RefOffset) rem 7,
    DayNames = [<<"Sunday">>, <<"Monday">>, <<"Tuesday">>,
                <<"Wednesday">>, <<"Thursday">>, <<"Friday">>, <<"Saturday">>],
    lists:nth(Index + 1, DayNames).

is_leap(Year) ->
    (Year rem 400 =:= 0) orelse ((Year rem 4 =:= 0) andalso (Year rem 100 =/= 0)).

leap_count(From, To) when From =< To ->
    leaps_up_to(To) - leaps_up_to(From - 1);
leap_count(_, _) -> 0.

leaps_up_to(Y) ->
    Y div 4 - Y div 100 + Y div 400.

days_before_month(Month, _IsLeap) when Month =:= 1 -> 0;
days_before_month(Month, IsLeap) ->
    CumNonLeap = [0,31,59,90,120,151,181,212,243,273,304,334],
    Base = lists:nth(Month, CumNonLeap),
    case {IsLeap, Month > 2} of
        {true, true} -> Base + 1;
        _ -> Base
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec day_of_the_week(day :: integer, month :: integer, year :: integer) :: String.t()
  def day_of_the_week(day, month, year) do
    # Days in each month for a non-leap year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Total days from years before the given year (starting from 1971)
    total_year_days =
      if year > 1971 do
        Enum.reduce(1971..(year - 1), 0, fn y, acc ->
          if leap?(y), do: acc + 366, else: acc + 365
        end)
      else
        0
      end

    # Days from months before the given month in the current year
    months_before = Enum.take(month_days, month - 1) |> Enum.sum()
    months_before =
      if month > 2 and leap?(year), do: months_before + 1, else: months_before

    # Total offset days from 1971-01-01 to the given date (excluding the start day)
    total_offset = total_year_days + months_before + (day - 1)

    # 1971-01-01 was a Friday, which is index 5 in the week list
    weekday_index = rem(5 + total_offset, 7)

    ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    |> Enum.at(weekday_index)
  end

  defp leap?(y) when rem(y, 400) == 0, do: true
  defp leap?(y) when rem(y, 100) == 0, do: false
  defp leap?(y) when rem(y, 4) == 0, do: true
  defp leap?(_), do: false
end
```
