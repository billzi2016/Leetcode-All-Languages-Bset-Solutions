# 3280. Convert Date to Binary

## Cpp

```cpp
class Solution {
public:
    string toBinary(int n) {
        string s;
        while (n > 0) {
            s.push_back((n & 1) + '0');
            n >>= 1;
        }
        reverse(s.begin(), s.end());
        return s.empty() ? "0" : s;
    }
    
    string convertDateToBinary(string date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8, 2));
        
        string yb = toBinary(year);
        string mb = toBinary(month);
        string db = toBinary(day);
        
        return yb + "-" + mb + "-" + db;
    }
};
```

## Java

```java
class Solution {
    public String convertDateToBinary(String date) {
        String[] parts = date.split("-");
        int year = Integer.parseInt(parts[0]);
        int month = Integer.parseInt(parts[1]);
        int day = Integer.parseInt(parts[2]);
        return Integer.toBinaryString(year) + "-" +
               Integer.toBinaryString(month) + "-" +
               Integer.toBinaryString(day);
    }
}
```

## Python

```python
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year_str, month_str, day_str = date.split('-')
        year_bin = bin(int(year_str))[2:]
        month_bin = bin(int(month_str))[2:]
        day_bin = bin(int(day_str))[2:]
        return f"{year_bin}-{month_bin}-{day_bin}"
```

## Python3

```python
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year_str, month_str, day_str = date.split('-')
        year_bin = bin(int(year_str))[2:]
        month_bin = bin(int(month_str))[2:]
        day_bin = bin(int(day_str))[2:]
        return f"{year_bin}-{month_bin}-{day_bin}"
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static char *toBinary(int num) {
    char *buf = (char *)malloc(33); // enough for 32 bits + null
    int idx = 0;
    int started = 0;
    for (int i = 31; i >= 0; --i) {
        if ((num >> i) & 1) {
            started = 1;
            buf[idx++] = '1';
        } else if (started) {
            buf[idx++] = '0';
        }
    }
    if (!started) { // num == 0, not expected here but handle safely
        buf[idx++] = '0';
    }
    buf[idx] = '\0';
    return buf;
}

char* convertDateToBinary(char* date) {
    int year, month, day;
    sscanf(date, "%d-%d-%d", &year, &month, &day);
    
    char *binY = toBinary(year);
    char *binM = toBinary(month);
    char *binD = toBinary(day);
    
    size_t len = strlen(binY) + strlen(binM) + strlen(binD) + 2 + 1; // two hyphens and null
    char *result = (char *)malloc(len);
    sprintf(result, "%s-%s-%s", binY, binM, binD);
    
    free(binY);
    free(binM);
    free(binD);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public string ConvertDateToBinary(string date) {
        var parts = date.Split('-');
        int year = int.Parse(parts[0]);
        int month = int.Parse(parts[1]);
        int day = int.Parse(parts[2]);

        string yearBin = Convert.ToString(year, 2);
        string monthBin = Convert.ToString(month, 2);
        string dayBin = Convert.ToString(day, 2);

        return $"{yearBin}-{monthBin}-{dayBin}";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} date
 * @return {string}
 */
var convertDateToBinary = function(date) {
    const [year, month, day] = date.split('-');
    return parseInt(year, 10).toString(2) + '-' +
           parseInt(month, 10).toString(2) + '-' +
           parseInt(day,   10).toString(2);
};
```

## Typescript

```typescript
function convertDateToBinary(date: string): string {
    const year = parseInt(date.slice(0, 4), 10);
    const month = parseInt(date.slice(5, 7), 10);
    const day = parseInt(date.slice(8, 10), 10);
    return `${year.toString(2)}-${month.toString(2)}-${day.toString(2)}`;
}
```

## Php

```php
class Solution {

    /**
     * @param String $date
     * @return String
     */
    function convertDateToBinary($date) {
        // Split the date into year, month, day
        list($yearStr, $monthStr, $dayStr) = explode('-', $date);
        
        // Convert each part to integer then to binary string without leading zeros
        $yearBin  = decbin((int)$yearStr);
        $monthBin = decbin((int)$monthStr);
        $dayBin   = decbin((int)$dayStr);
        
        // Concatenate with hyphens
        return $yearBin . '-' . $monthBin . '-' . $dayBin;
    }
}
```

## Swift

```swift
class Solution {
    func convertDateToBinary(_ date: String) -> String {
        let parts = date.split(separator: "-")
        guard parts.count == 3,
              let year = Int(parts[0]),
              let month = Int(parts[1]),
              let day = Int(parts[2]) else { return "" }
        let yBin = String(year, radix: 2)
        let mBin = String(month, radix: 2)
        let dBin = String(day, radix: 2)
        return "\(yBin)-\(mBin)-\(dBin)"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun convertDateToBinary(date: String): String {
        val parts = date.split("-")
        val yearBin = Integer.toBinaryString(parts[0].toInt())
        val monthBin = Integer.toBinaryString(parts[1].toInt())
        val dayBin = Integer.toBinaryString(parts[2].toInt())
        return "$yearBin-$monthBin-$dayBin"
    }
}
```

## Dart

```dart
class Solution {
  String convertDateToBinary(String date) {
    List<String> parts = date.split('-');
    int year = int.parse(parts[0]);
    int month = int.parse(parts[1]);
    int day = int.parse(parts[2]);

    String yearBin = year.toRadixString(2);
    String monthBin = month.toRadixString(2);
    String dayBin = day.toRadixString(2);

    return '$yearBin-$monthBin-$dayBin';
  }
}
```

## Golang

```go
import "strconv"

func convertDateToBinary(date string) string {
	yearStr := date[:4]
	monthStr := date[5:7]
	dayStr := date[8:10]

	y, _ := strconv.Atoi(yearStr)
	m, _ := strconv.Atoi(monthStr)
	d, _ := strconv.Atoi(dayStr)

	return strconv.FormatInt(int64(y), 2) + "-" + strconv.FormatInt(int64(m), 2) + "-" + strconv.FormatInt(int64(d), 2)
}
```

## Ruby

```ruby
def convert_date_to_binary(date)
  year_str, month_str, day_str = date.split('-')
  [year_str.to_i, month_str.to_i, day_str.to_i].map { |num| num.to_s(2) }.join('-')
end
```

## Scala

```scala
object Solution {
    def convertDateToBinary(date: String): String = {
        val parts = date.split("-")
        val yearBin = Integer.toBinaryString(parts(0).toInt)
        val monthBin = Integer.toBinaryString(parts(1).toInt)
        val dayBin = Integer.toBinaryString(parts(2).toInt)
        s"$yearBin-$monthBin-$dayBin"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn convert_date_to_binary(date: String) -> String {
        let parts: Vec<&str> = date.split('-').collect();
        let year: u32 = parts[0].parse().unwrap();
        let month: u32 = parts[1].parse().unwrap();
        let day: u32 = parts[2].parse().unwrap();

        format!("{}-{}-{}", format!("{:b}", year), format!("{:b}", month), format!("{:b}", day))
    }
}
```

## Racket

```racket
(define/contract (convert-date-to-binary date)
  (-> string? string?)
  (let* ([year-str (substring date 0 4)]
         [month-str (substring date 5 7)]
         [day-str (substring date 8 10)]
         [year-num (string->number year-str)]
         [month-num (string->number month-str)]
         [day-num (string->number day-str)]
         [year-bin (number->string year-num 2)]
         [month-bin (number->string month-num 2)]
         [day-bin (number->string day-num 2)])
    (string-append year-bin "-" month-bin "-" day-bin)))
```

## Erlang

```erlang
-spec convert_date_to_binary(Date :: unicode:unicode_binary()) -> unicode:unicode_binary().
convert_date_to_binary(Date) ->
    [YearB, MonthB, DayB] = binary:split(Date, <<"-">>, [global]),
    YearI = list_to_integer(binary_to_list(YearB)),
    MonthI = list_to_integer(binary_to_list(MonthB)),
    DayI = list_to_integer(binary_to_list(DayB)),
    YearBin = integer_to_binary(YearI, 2),
    MonthBin = integer_to_binary(MonthI, 2),
    DayBin = integer_to_binary(DayI, 2),
    <<YearBin/binary, $-, MonthBin/binary, $-, DayBin/binary>>.
```

## Elixir

```elixir
defmodule Solution do
  @spec convert_date_to_binary(date :: String.t) :: String.t
  def convert_date_to_binary(date) do
    [year_str, month_str, day_str] = String.split(date, "-")
    year_bin = Integer.to_string(String.to_integer(year_str), 2)
    month_bin = Integer.to_string(String.to_integer(month_str), 2)
    day_bin = Integer.to_string(String.to_integer(day_str), 2)
    Enum.join([year_bin, month_bin, day_bin], "-")
  end
end
```
