# 1507. Reformat Date

## Cpp

```cpp
class Solution {
public:
    string reformatDate(string date) {
        // Split the input by spaces
        vector<string> parts;
        string cur;
        for (char c : date) {
            if (c == ' ') {
                parts.push_back(cur);
                cur.clear();
            } else {
                cur.push_back(c);
            }
        }
        parts.push_back(cur); // last part
        
        // Day: remove the suffix (last two characters)
        string day = parts[0].substr(0, parts[0].size() - 2);
        if (day.size() == 1) day = "0" + day;
        
        // Month mapping
        static const unordered_map<string, string> monthMap = {
            {"Jan","01"}, {"Feb","02"}, {"Mar","03"}, {"Apr","04"},
            {"May","05"}, {"Jun","06"}, {"Jul","07"}, {"Aug","08"},
            {"Sep","09"}, {"Oct","10"}, {"Nov","11"}, {"Dec","12"}
        };
        string month = monthMap.at(parts[1]);
        
        // Year
        string year = parts[2];
        
        return year + "-" + month + "-" + day;
    }
};
```

## Java

```java
class Solution {
    public String reformatDate(String date) {
        String[] parts = date.split(" ");
        // Day: remove the suffix (last two characters)
        int day = Integer.parseInt(parts[0].substring(0, parts[0].length() - 2));
        String dayStr = String.format("%02d", day);
        
        // Month mapping
        String monthStr;
        switch (parts[1]) {
            case "Jan": monthStr = "01"; break;
            case "Feb": monthStr = "02"; break;
            case "Mar": monthStr = "03"; break;
            case "Apr": monthStr = "04"; break;
            case "May": monthStr = "05"; break;
            case "Jun": monthStr = "06"; break;
            case "Jul": monthStr = "07"; break;
            case "Aug": monthStr = "08"; break;
            case "Sep": monthStr = "09"; break;
            case "Oct": monthStr = "10"; break;
            case "Nov": monthStr = "11"; break;
            case "Dec": monthStr = "12"; break;
            default: monthStr = ""; // should never happen
        }
        
        // Year is already in correct format
        String yearStr = parts[2];
        
        return yearStr + "-" + monthStr + "-" + dayStr;
    }
}
```

## Python

```python
class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        day_str, month_str, year = date.split()
        # Remove the suffix (last two characters) from day and convert to int for zero padding
        day = "{:02d}".format(int(day_str[:-2]))
        # Map month abbreviation to its numeric representation
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        month = months[month_str]
        return "{}-{}-{}".format(year, month, day)
```

## Python3

```python
class Solution:
    def reformatDate(self, date: str) -> str:
        day_str, month_str, year = date.split()
        # Remove the suffix (last two characters)
        day = int(day_str[:-2])
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        month = month_map[month_str]
        return f"{year}-{month}-{day:02d}"
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

char* reformatDate(char* date) {
    const char *p = date;
    int day = 0, year = 0, monthNum = 0;
    
    // parse day
    while (isdigit(*p)) {
        day = day * 10 + (*p - '0');
        p++;
    }
    // skip suffix letters until space
    while (*p && *p != ' ') p++;
    while (*p == ' ') p++;
    
    // parse month abbreviation (first three letters)
    char monthStr[4] = {0};
    for (int i = 0; i < 3 && *p; ++i) {
        monthStr[i] = *p++;
    }
    monthStr[3] = '\0';
    
    // skip remaining month characters and space
    while (*p && *p != ' ') p++;
    while (*p == ' ') p++;
    
    // parse year
    while (isdigit(*p)) {
        year = year * 10 + (*p - '0');
        p++;
    }
    
    const char *months[] = {"Jan","Feb","Mar","Apr","May","Jun",
                            "Jul","Aug","Sep","Oct","Nov","Dec"};
    for (int i = 0; i < 12; ++i) {
        if (strcmp(monthStr, months[i]) == 0) {
            monthNum = i + 1;
            break;
        }
    }
    
    char *res = (char *)malloc(11); // "YYYY-MM-DD" + '\0'
    sprintf(res, "%04d-%02d-%02d", year, monthNum, day);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ReformatDate(string date)
    {
        var parts = date.Split(' ');
        // Day: remove the last two characters (suffix) and parse
        int day = int.Parse(parts[0].Substring(0, parts[0].Length - 2));
        string dd = day.ToString("D2");

        // Month mapping
        var monthMap = new Dictionary<string, string>
        {
            {"Jan","01"}, {"Feb","02"}, {"Mar","03"}, {"Apr","04"},
            {"May","05"}, {"Jun","06"}, {"Jul","07"}, {"Aug","08"},
            {"Sep","09"}, {"Oct","10"}, {"Nov","11"}, {"Dec","12"}
        };
        string mm = monthMap[parts[1]];

        // Year is already in correct form
        string yyyy = parts[2];

        return $"{yyyy}-{mm}-{dd}";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} date
 * @return {string}
 */
var reformatDate = function(date) {
    const months = {
        Jan: '01', Feb: '02', Mar: '03', Apr: '04',
        May: '05', Jun: '06', Jul: '07', Aug: '08',
        Sep: '09', Oct: '10', Nov: '11', Dec: '12'
    };
    
    const parts = date.split(' ');
    // Day: remove the last two characters (suffix like "th", "st", "nd", "rd")
    let dayNum = parseInt(parts[0].slice(0, -2), 10);
    const day = dayNum < 10 ? '0' + dayNum : '' + dayNum;
    
    const month = months[parts[1]];
    const year = parts[2];
    
    return `${year}-${month}-${day}`;
};
```

## Typescript

```typescript
function reformatDate(date: string): string {
    const monthMap: { [key: string]: string } = {
        Jan: "01",
        Feb: "02",
        Mar: "03",
        Apr: "04",
        May: "05",
        Jun: "06",
        Jul: "07",
        Aug: "08",
        Sep: "09",
        Oct: "10",
        Nov: "11",
        Dec: "12"
    };
    const parts = date.split(' ');
    let day = parts[0].slice(0, -2);
    if (day.length === 1) day = '0' + day;
    const month = monthMap[parts[1]];
    const year = parts[2];
    return `${year}-${month}-${day}`;
}
```

## Php

```php
class Solution {

    /**
     * @param String $date
     * @return String
     */
    function reformatDate($date) {
        $monthMap = [
            "Jan" => "01", "Feb" => "02", "Mar" => "03", "Apr" => "04",
            "May" => "05", "Jun" => "06", "Jul" => "07", "Aug" => "08",
            "Sep" => "09", "Oct" => "10", "Nov" => "11", "Dec" => "12"
        ];
        
        $parts = explode(' ', $date);
        // Remove the suffix (last two characters) from day
        $dayNum = substr($parts[0], 0, -2);
        $day = str_pad(intval($dayNum), 2, '0', STR_PAD_LEFT);
        $month = $monthMap[$parts[1]];
        $year = $parts[2];
        
        return $year . '-' . $month . '-' . $day;
    }
}
```

## Swift

```swift
class Solution {
    func reformatDate(_ date: String) -> String {
        let parts = date.split(separator: " ")
        // Day
        var day = String(parts[0].dropLast(2))
        if day.count == 1 { day = "0" + day }
        // Month
        let monthMap: [String: String] = [
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        ]
        let month = monthMap[String(parts[1])]!
        // Year
        let year = String(parts[2])
        return "\(year)-\(month)-\(day)"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reformatDate(date: String): String {
        val parts = date.split(" ")
        val dayNum = parts[0].dropLast(2).toInt()
        val monthStr = parts[1]
        val year = parts[2]

        val month = when (monthStr) {
            "Jan" -> "01"
            "Feb" -> "02"
            "Mar" -> "03"
            "Apr" -> "04"
            "May" -> "05"
            "Jun" -> "06"
            "Jul" -> "07"
            "Aug" -> "08"
            "Sep" -> "09"
            "Oct" -> "10"
            "Nov" -> "11"
            else -> "12"
        }

        val day = if (dayNum < 10) "0$dayNum" else "$dayNum"

        return "$year-$month-$day"
    }
}
```

## Dart

```dart
class Solution {
  String reformatDate(String date) {
    List<String> parts = date.split(' ');
    String dayPart = parts[0];
    String dayNum = dayPart.substring(0, dayPart.length - 2);
    if (dayNum.length == 1) dayNum = '0' + dayNum;
    const monthMap = {
      'Jan': '01',
      'Feb': '02',
      'Mar': '03',
      'Apr': '04',
      'May': '05',
      'Jun': '06',
      'Jul': '07',
      'Aug': '08',
      'Sep': '09',
      'Oct': '10',
      'Nov': '11',
      'Dec': '12',
    };
    String monthNum = monthMap[parts[1]]!;
    String year = parts[2];
    return '$year-$monthNum-$dayNum';
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func reformatDate(date string) string {
	parts := strings.Split(date, " ")
	dayPart := parts[0][:len(parts[0])-2] // remove suffix
	dayInt, _ := strconv.Atoi(dayPart)
	dayStr := strconv.Itoa(dayInt)
	if len(dayStr) == 1 {
		dayStr = "0" + dayStr
	}

	monthMap := map[string]string{
		"Jan": "01",
		"Feb": "02",
		"Mar": "03",
		"Apr": "04",
		"May": "05",
		"Jun": "06",
		"Jul": "07",
		"Aug": "08",
		"Sep": "09",
		"Oct": "10",
		"Nov": "11",
		"Dec": "12",
	}
	monthStr := monthMap[parts[1]]
	yearStr := parts[2]

	return yearStr + "-" + monthStr + "-" + dayStr
}
```

## Ruby

```ruby
def reformat_date(date)
  months = {
    "Jan"=>"01","Feb"=>"02","Mar"=>"03","Apr"=>"04","May"=>"05",
    "Jun"=>"06","Jul"=>"07","Aug"=>"08","Sep"=>"09","Oct"=>"10",
    "Nov"=>"11","Dec"=>"12"
  }
  day, mon, year = date.split(' ')
  day_num = day[0..-3].rjust(2, '0')
  month_num = months[mon]
  "#{year}-#{month_num}-#{day_num}"
end
```

## Scala

```scala
object Solution {
    def reformatDate(date: String): String = {
        val months = Map(
            "Jan" -> "01",
            "Feb" -> "02",
            "Mar" -> "03",
            "Apr" -> "04",
            "May" -> "05",
            "Jun" -> "06",
            "Jul" -> "07",
            "Aug" -> "08",
            "Sep" -> "09",
            "Oct" -> "10",
            "Nov" -> "11",
            "Dec" -> "12"
        )
        val parts = date.split(" ")
        val dayNum = parts(0).dropRight(2).toInt
        val day = f"$dayNum%02d"
        val month = months(parts(1))
        val year = parts(2)
        s"$year-$month-$day"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reformat_date(date: String) -> String {
        let parts: Vec<&str> = date.split_whitespace().collect();
        let day_part = parts[0];
        let day_num_str = &day_part[..day_part.len() - 2];
        let day: u32 = day_num_str.parse().unwrap();

        let month_str = parts[1];
        let month: u32 = match month_str {
            "Jan" => 1,
            "Feb" => 2,
            "Mar" => 3,
            "Apr" => 4,
            "May" => 5,
            "Jun" => 6,
            "Jul" => 7,
            "Aug" => 8,
            "Sep" => 9,
            "Oct" => 10,
            "Nov" => 11,
            "Dec" => 12,
            _ => 0,
        };

        let year = parts[2];
        format!("{}-{:02}-{:02}", year, month, day)
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (reformat-date date)
  (-> string? string?)
  (let* ([parts (string-split date)]
         [day-str (list-ref parts 0)]
         [month-str (list-ref parts 1)]
         [year-str (list-ref parts 2)]
         [day-num-str (substring day-str 0 (- (string-length day-str) 2))]
         [day-num (string->number day-num-str)]
         [day-padded (format "~02d" day-num)]
         [month-alist '(("Jan" . "01") ("Feb" . "02") ("Mar" . "03")
                        ("Apr" . "04") ("May" . "05") ("Jun" . "06")
                        ("Jul" . "07") ("Aug" . "08") ("Sep" . "09")
                        ("Oct" . "10") ("Nov" . "11") ("Dec" . "12"))]
         [month-padded (cdr (assoc month-str month-alist))])
    (string-append year-str "-" month-padded "-" day-padded)))
```

## Erlang

```erlang
-module(solution).
-export([reformat_date/1]).

-spec reformat_date(Date :: unicode:unicode_binary()) -> unicode:unicode_binary().
reformat_date(Date) ->
    [DayBin, MonthBin, YearBin] = binary:split(Date, <<" ">>, [global]),
    DayNum = strip_day(DayBin),
    DayPadded = pad_day(DayNum),
    MonthNum = month_to_num(MonthBin),
    <<YearBin/binary, $-, MonthNum/binary, $-, DayPadded/binary>>.

strip_day(D) ->
    Size = byte_size(D) - 2,
    binary:part(D, 0, Size).

pad_day(D) when byte_size(D) =:= 1 ->
    <<"0", D/binary>>;
pad_day(D) -> D.

month_to_num(<<"Jan">>) -> <<"01">>;
month_to_num(<<"Feb">>) -> <<"02">>;
month_to_num(<<"Mar">>) -> <<"03">>;
month_to_num(<<"Apr">>) -> <<"04">>;
month_to_num(<<"May">>) -> <<"05">>;
month_to_num(<<"Jun">>) -> <<"06">>;
month_to_num(<<"Jul">>) -> <<"07">>;
month_to_num(<<"Aug">>) -> <<"08">>;
month_to_num(<<"Sep">>) -> <<"09">>;
month_to_num(<<"Oct">>) -> <<"10">>;
month_to_num(<<"Nov">>) -> <<"11">>;
month_to_num(<<"Dec">>) -> <<"12">>.
```

## Elixir

```elixir
defmodule Solution do
  @spec reformat_date(date :: String.t()) :: String.t()
  def reformat_date(date) do
    [day, mon, year] = String.split(date, " ")

    day_len = byte_size(day)
    day_num = String.slice(day, 0, day_len - 2)
    day_formatted = if byte_size(day_num) == 1, do: "0" <> day_num, else: day_num

    month_map = %{
      "Jan" => "01",
      "Feb" => "02",
      "Mar" => "03",
      "Apr" => "04",
      "May" => "05",
      "Jun" => "06",
      "Jul" => "07",
      "Aug" => "08",
      "Sep" => "09",
      "Oct" => "10",
      "Nov" => "11",
      "Dec" => "12"
    }

    month_formatted = Map.fetch!(month_map, mon)

    "#{year}-#{month_formatted}-#{day_formatted}"
  end
end
```
