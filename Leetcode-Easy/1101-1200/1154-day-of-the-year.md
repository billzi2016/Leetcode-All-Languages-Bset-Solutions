# 1154. Day of the Year

## Cpp

```cpp
class Solution {
public:
    int dayOfYear(string date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8, 2));
        
        bool leap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
        static const int daysInMonth[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
        
        int ans = day;
        for (int m = 1; m < month; ++m) {
            ans += daysInMonth[m - 1];
            if (m == 2 && leap) ans += 1; // add Feb 29
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int dayOfYear(String date) {
        int year = Integer.parseInt(date.substring(0, 4));
        int month = Integer.parseInt(date.substring(5, 7));
        int day = Integer.parseInt(date.substring(8, 10));

        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // Check for leap year
        boolean isLeap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
        if (isLeap) {
            daysInMonth[1] = 29;
        }

        int dayOfYear = day;
        for (int i = 0; i < month - 1; i++) {
            dayOfYear += daysInMonth[i];
        }
        return dayOfYear;
    }
}
```

## Python

```python
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check leap year
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        if is_leap:
            days_in_month[1] = 29
        
        # Sum days of previous months
        total_days = sum(days_in_month[:month - 1]) + day
        return total_days
```

## Python3

```python
class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Check leap year
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29
        return sum(days_in_month[:month - 1]) + day
```

## C

```c
int dayOfYear(char* date) {
    int year = (date[0] - '0') * 1000 + (date[1] - '0') * 100 + (date[2] - '0') * 10 + (date[3] - '0');
    int month = (date[5] - '0') * 10 + (date[6] - '0');
    int day = (date[8] - '0') * 10 + (date[9] - '0');

    int mdays[12] = {31,28,31,30,31,30,31,31,30,31,30,31};

    // Check for leap year
    if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
        mdays[1] = 29;
    }

    int result = day;
    for (int i = 0; i < month - 1; ++i) {
        result += mdays[i];
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int DayOfYear(string date)
    {
        int year = int.Parse(date.Substring(0, 4));
        int month = int.Parse(date.Substring(5, 2));
        int day = int.Parse(date.Substring(8, 2));

        int[] daysInMonth = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        bool isLeap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
        if (isLeap) daysInMonth[1] = 29;

        int result = day;
        for (int i = 0; i < month - 1; i++)
            result += daysInMonth[i];

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    const year = parseInt(date.slice(0, 4), 10);
    const month = parseInt(date.slice(5, 7), 10);
    const day = parseInt(date.slice(8, 10), 10);
    
    const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let total = day;
    
    for (let i = 0; i < month - 1; i++) {
        total += daysInMonth[i];
    }
    
    // Add leap day if past February in a leap year
    const isLeap = (year % 400 === 0) || (year % 4 === 0 && year % 100 !== 0);
    if (month > 2 && isLeap) {
        total += 1;
    }
    
    return total;
};
```

## Typescript

```typescript
function dayOfYear(date: string): number {
    const year = parseInt(date.slice(0, 4), 10);
    const month = parseInt(date.slice(5, 7), 10);
    const day = parseInt(date.slice(8, 10), 10);

    const isLeap = (year % 400 === 0) || (year % 4 === 0 && year % 100 !== 0);
    const daysInMonth = [31, isLeap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    let total = day;
    for (let i = 0; i < month - 1; i++) {
        total += daysInMonth[i];
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $date
     * @return Integer
     */
    function dayOfYear($date) {
        // Extract year, month, day as integers
        $year = intval(substr($date, 0, 4));
        $month = intval(substr($date, 5, 2));
        $day = intval(substr($date, 8, 2));

        // Days in each month for a non-leap year
        $daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31];

        // Adjust February for leap years
        if (($year % 400 == 0) || ($year % 4 == 0 && $year % 100 != 0)) {
            $daysInMonth[1] = 29;
        }

        // Sum days of the months before the given month
        $total = 0;
        for ($i = 0; $i < $month - 1; $i++) {
            $total += $daysInMonth[$i];
        }
        $total += $day;

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func dayOfYear(_ date: String) -> Int {
        let parts = date.split(separator: "-")
        guard parts.count == 3,
              let year = Int(parts[0]),
              let month = Int(parts[1]),
              let day = Int(parts[2]) else { return 0 }
        
        var daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        // Check for leap year
        if (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0) {
            daysInMonth[1] = 29
        }
        
        var dayOfYear = day
        for i in 0..<(month - 1) {
            dayOfYear += daysInMonth[i]
        }
        return dayOfYear
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun dayOfYear(date: String): Int {
        val year = date.substring(0, 4).toInt()
        val month = date.substring(5, 7).toInt()
        val day = date.substring(8, 10).toInt()

        val daysInMonth = intArrayOf(
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        )

        var total = 0
        for (i in 0 until month - 1) {
            total += daysInMonth[i]
        }
        if (month > 2 && isLeapYear(year)) {
            total += 1
        }
        return total + day
    }

    private fun isLeapYear(y: Int): Boolean {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)
    }
}
```

## Dart

```dart
class Solution {
  int dayOfYear(String date) {
    int year = int.parse(date.substring(0, 4));
    int month = int.parse(date.substring(5, 7));
    int day = int.parse(date.substring(8, 10));

    bool isLeap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    List<int> daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    if (isLeap) daysInMonth[1] = 29;

    int total = day;
    for (int i = 0; i < month - 1; ++i) {
      total += daysInMonth[i];
    }
    return total;
  }
}
```

## Golang

```go
func dayOfYear(date string) int {
	year := (int(date[0]-'0')*1000 + int(date[1]-'0')*100 + int(date[2]-'0')*10 + int(date[3]-'0'))
	month := (int(date[5]-'0')*10 + int(date[6]-'0'))
	day := (int(date[8]-'0')*10 + int(date[9]-'0'))

	isLeap := (year%400 == 0) || (year%4 == 0 && year%100 != 0)

	daysInMonth := [12]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if isLeap {
		daysInMonth[1] = 29
	}

	total := day
	for i := 0; i < month-1; i++ {
		total += daysInMonth[i]
	}
	return total
}
```

## Ruby

```ruby
# @param {String} date
# @return {Integer}
def day_of_year(date)
  year = date[0,4].to_i
  month = date[5,2].to_i
  day = date[8,2].to_i

  days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

  # Check for leap year
  leap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)

  days_before = days_in_month.take(month - 1).sum
  days_before += 1 if leap && month > 2

  days_before + day
end
```

## Scala

```scala
object Solution {
    def dayOfYear(date: String): Int = {
        val year = date.substring(0, 4).toInt
        val month = date.substring(5, 7).toInt
        val day = date.substring(8, 10).toInt

        val daysInMonth = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        val isLeap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)

        var total = day
        for (i <- 0 until month - 1) {
            total += daysInMonth(i)
        }
        if (isLeap && month > 2) total += 1
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn day_of_year(date: String) -> i32 {
        let year: i32 = date[0..4].parse().unwrap();
        let month: usize = date[5..7].parse::<usize>().unwrap();
        let day: i32 = date[8..10].parse().unwrap();

        let leap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
        let month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

        let mut total = day;
        for i in 0..month - 1 {
            total += month_days[i];
        }
        if leap && month > 2 {
            total += 1;
        }
        total
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (day-of-year date)
  (-> string? exact-integer?)
  (let* ([year (string->number (substring date 0 4))]
         [month (string->number (substring date 5 7))]
         [day (string->number (substring date 8 10))]
         [leap? (or (= (modulo year 400) 0)
                    (and (= (modulo year 4) 0) (not (= (modulo year 100) 0)) ))]
         [days-per-month (list 31 (if leap? 29 28) 31 30 31 30 31 31 30 31 30 31)])
    (+ day
       (apply + (take days-per-month (- month 1))))))
```

## Erlang

```erlang
-spec day_of_year(Date :: unicode:unicode_binary()) -> integer().
day_of_year(Date) ->
    <<Y1,Y2,Y3,Y4,$-,M1,M2,$-,D1,D2>> = Date,
    Year = binary_to_integer(<<Y1,Y2,Y3,Y4>>),
    Month = binary_to_integer(<<M1,M2>>),
    Day = binary_to_integer(<<D1,D2>>),

    DaysBeforeMonth = case Month of
        1 -> 0;
        2 -> 31;
        3 -> 59;
        4 -> 90;
        5 -> 120;
        6 -> 151;
        7 -> 181;
        8 -> 212;
        9 -> 243;
        10 -> 273;
        11 -> 304;
        12 -> 334
    end,

    Leap = (Year rem 4 == 0 andalso Year rem 100 /= 0) orelse (Year rem 400 == 0),
    Add = if Leap, Month > 2 -> 1; true -> 0 end,
    DaysBeforeMonth + Day + Add.
```

## Elixir

```elixir
defmodule Solution do
  @common_days [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  @leap_days   [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  @spec day_of_year(date :: String.t()) :: integer()
  def day_of_year(date) do
    year = date |> String.slice(0, 4) |> String.to_integer()
    month = date |> String.slice(5, 2) |> String.to_integer()
    day = date |> String.slice(8, 2) |> String.to_integer()

    days_before =
      (if leap?(year), do: @leap_days, else: @common_days)
      |> Enum.take(month - 1)
      |> Enum.sum()

    days_before + day
  end

  defp leap?(year) do
    rem(year, 400) == 0 or (rem(year, 4) == 0 and rem(year, 100) != 0)
  end
end
```
