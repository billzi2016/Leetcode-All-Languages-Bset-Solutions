# 0273. Integer to English Words

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        
        vector<string> below20 = {"","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
                                  "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
                                  "Seventeen","Eighteen","Nineteen"};
        vector<string> tens = {"","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"};
        
        function<string(int)> helper = [&](int n) -> string {
            if (n == 0) return "";
            if (n < 20) return below20[n];
            if (n < 100) {
                string s = tens[n / 10];
                if (n % 10) s += " " + below20[n % 10];
                return s;
            }
            string s = below20[n / 100] + " Hundred";
            if (n % 100) s += " " + helper(n % 100);
            return s;
        };
        
        vector<pair<int,string>> units = {
            {1000000000, "Billion"},
            {1000000,    "Million"},
            {1000,       "Thousand"}
        };
        
        string ans;
        int cur = num;
        for (auto &p : units) {
            if (cur >= p.first) {
                int cnt = cur / p.first;
                ans += helper(cnt) + " " + p.second;
                cur %= p.first;
                if (cur) ans += " ";
            }
        }
        if (cur > 0) ans += helper(cur);
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final String[] LESS_THAN_20 = {
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    };
    private static final String[] TENS = {
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    };

    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        StringBuilder sb = new StringBuilder();

        if (num >= 1_000_000_000) {
            sb.append(helper(num / 1_000_000_000)).append("Billion ");
            num %= 1_000_000_000;
        }
        if (num >= 1_000_000) {
            sb.append(helper(num / 1_000_000)).append("Million ");
            num %= 1_000_000;
        }
        if (num >= 1000) {
            sb.append(helper(num / 1000)).append("Thousand ");
            num %= 1000;
        }
        if (num > 0) {
            sb.append(helper(num));
        }

        return sb.toString().trim();
    }

    private String helper(int n) {
        if (n == 0) return "";
        if (n < 20) {
            return LESS_THAN_20[n] + " ";
        }
        if (n < 100) {
            return TENS[n / 10] + " " + helper(n % 10);
        }
        return LESS_THAN_20[n / 100] + " Hundred " + helper(n % 100);
    }
}
```

## Python

```python
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + helper(n % 10) if n % 10 else "")
            else:  # n < 1000
                return below_20[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 else "")

        parts = []
        billions = num // 1_000_000_000
        if billions:
            parts.append(helper(billions) + " Billion")
        millions = (num // 1_000_000) % 1000
        if millions:
            parts.append(helper(millions) + " Million")
        thousands = (num // 1_000) % 1000
        if thousands:
            parts.append(helper(thousands) + " Thousand")
        remainder = num % 1000
        if remainder:
            parts.append(helper(remainder))

        return " ".join(parts)
```

## Python3

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            if n < 20:
                return below_20[n] + " "
            if n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            # n < 1000
            return below_20[n // 100] + " Hundred " + helper(n % 100)

        parts = []
        i = 0
        while num > 0:
            cur = num % 1000
            if cur != 0:
                segment = helper(cur).strip()
                if thousands[i]:
                    segment += " " + thousands[i]
                parts.append(segment)
            num //= 1000
            i += 1

        return " ".join(reversed(parts))
```

## C

```c
#include <stdlib.h>
#include <string.h>

static const char *below20[] = {
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
};

static const char *tens[] = {
    "", "", "Twenty", "Thirty", "Forty", "Fifty",
    "Sixty", "Seventy", "Eighty", "Ninety"
};

static void helperBelow1000(int num, char *buf) {
    if (num == 0) return;
    if (num < 20) {
        strcat(buf, below20[num]);
        strcat(buf, " ");
    } else if (num < 100) {
        strcat(buf, tens[num / 10]);
        strcat(buf, " ");
        helperBelow1000(num % 10, buf);
    } else {
        strcat(buf, below20[num / 100]);
        strcat(buf, " Hundred ");
        helperBelow1000(num % 100, buf);
    }
}

char* numberToWords(int num) {
    if (num == 0) {
        char *zero = malloc(5);
        strcpy(zero, "Zero");
        return zero;
    }

    static const int unitVals[] = {1000000000, 1000000, 1000};
    static const char *unitNames[] = {"Billion", "Million", "Thousand"};

    char *buf = malloc(512);
    buf[0] = '\0';

    for (int i = 0; i < 3; ++i) {
        if (num >= unitVals[i]) {
            int cur = num / unitVals[i];
            helperBelow1000(cur, buf);
            strcat(buf, unitNames[i]);
            strcat(buf, " ");
            num %= unitVals[i];
        }
    }

    helperBelow1000(num, buf);

    size_t len = strlen(buf);
    if (len && buf[len - 1] == ' ') {
        buf[len - 1] = '\0';
    }
    return buf;
}
```

## Csharp

```csharp
public class Solution
{
    private static readonly string[] BelowTwenty = {
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    };

    private static readonly string[] Tens = {
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    };

    private static readonly string[] Thousands = { "", "Thousand", "Million", "Billion" };

    public string NumberToWords(int num)
    {
        if (num == 0) return "Zero";

        int i = 0;
        string result = "";
        while (num > 0)
        {
            int cur = num % 1000;
            if (cur != 0)
            {
                string segment = Helper(cur).Trim();
                if (!string.IsNullOrEmpty(Thousands[i]))
                    segment += " " + Thousands[i];
                result = segment + (result.Length > 0 ? " " : "") + result;
            }
            num /= 1000;
            i++;
        }

        return result.Trim();
    }

    private string Helper(int num)
    {
        if (num == 0) return "";
        if (num < 20) return BelowTwenty[num] + " ";
        if (num < 100) return Tens[num / 10] + " " + Helper(num % 10);
        return BelowTwenty[num / 100] + " Hundred " + Helper(num % 100);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function(num) {
    if (num === 0) return "Zero";
    
    const belowTwenty = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ];
    
    const tens = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ];
    
    const thousands = ["", "Thousand", "Million", "Billion"];
    
    function helper(n) {
        if (n === 0) return "";
        else if (n < 20) return belowTwenty[n] + " ";
        else if (n < 100) return tens[Math.floor(n / 10)] + " " + helper(n % 10);
        else return belowTwenty[Math.floor(n / 100)] + " Hundred " + helper(n % 100);
    }
    
    let result = "";
    let i = 0;
    while (num > 0) {
        const curChunk = num % 1000;
        if (curChunk !== 0) {
            const chunkWords = helper(curChunk).trim();
            result = chunkWords + (thousands[i] ? " " + thousands[i] : "") + (result ? " " + result : "");
        }
        num = Math.floor(num / 1000);
        i++;
    }
    
    return result.trim();
};
```

## Typescript

```typescript
function numberToWords(num: number): string {
    if (num === 0) return "Zero";

    const belowTwenty = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ];
    const tens = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ];
    const thousands = ["", "Thousand", "Million", "Billion"];

    function helper(n: number): string {
        if (n === 0) return "";
        if (n < 20) return belowTwenty[n] + " ";
        if (n < 100) return tens[Math.floor(n / 10)] + " " + helper(n % 10);
        // n < 1000
        return belowTwenty[Math.floor(n / 100)] + " Hundred " + helper(n % 100);
    }

    let result = "";
    let i = 0;
    while (num > 0) {
        const curChunk = num % 1000;
        if (curChunk !== 0) {
            const chunkWords = helper(curChunk).trim();
            const scale = thousands[i];
            const combined = scale ? `${chunkWords} ${scale}` : chunkWords;
            result = result ? `${combined} ${result}` : combined;
        }
        num = Math.floor(num / 1000);
        i++;
    }

    return result.trim();
}
```

## Php

```php
class Solution {
    private $lessThan20 = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ];
    
    private $tens = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ];
    
    private $thousands = ["", "Thousand", "Million", "Billion"];
    
    /**
     * @param Integer $num
     * @return String
     */
    function numberToWords($num) {
        if ($num == 0) return "Zero";
        $i = 0;
        $result = "";
        while ($num > 0) {
            $curr = $num % 1000;
            if ($curr != 0) {
                $segment = trim($this->helper($curr));
                if ($this->thousands[$i] !== "") {
                    $segment .= " " . $this->thousands[$i];
                }
                $result = $segment . ($result === "" ? "" : " " . $result);
            }
            $num = intdiv($num, 1000);
            $i++;
        }
        return trim($result);
    }
    
    private function helper($num) {
        if ($num == 0) {
            return "";
        } elseif ($num < 20) {
            return $this->lessThan20[$num] . " ";
        } elseif ($num < 100) {
            return $this->tens[intval($num / 10)] . " " . $this->helper($num % 10);
        } else {
            return $this->lessThan20[intval($num / 100)] . " Hundred " . $this->helper($num % 100);
        }
    }
}
```

## Swift

```swift
class Solution {
    func numberToWords(_ num: Int) -> String {
        if num == 0 { return "Zero" }
        
        let lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        let tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        let thousands = ["","Thousand","Million","Billion"]
        
        func helper(_ n: Int) -> String {
            if n == 0 { return "" }
            else if n < 20 {
                return lessThan20[n]
            } else if n < 100 {
                let tenWord = tens[n / 10]
                let rest = helper(n % 10)
                return tenWord + (rest.isEmpty ? "" : " " + rest)
            } else { // n < 1000
                let hundredWord = lessThan20[n / 100] + " Hundred"
                let rest = helper(n % 100)
                return hundredWord + (rest.isEmpty ? "" : " " + rest)
            }
        }
        
        var n = num
        var i = 0
        var result = ""
        while n > 0 {
            let cur = n % 1000
            if cur != 0 {
                var segment = helper(cur)
                if !thousands[i].isEmpty {
                    segment += " " + thousands[i]
                }
                result = segment + (result.isEmpty ? "" : " " + result)
            }
            n /= 1000
            i += 1
        }
        return result.trimmingCharacters(in: .whitespaces)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val belowTwenty = arrayOf(
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    )
    private val tens = arrayOf(
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    )

    fun numberToWords(num: Int): String {
        if (num == 0) return "Zero"
        return helper(num).trim()
    }

    private fun helper(num: Int): String {
        return when {
            num == 0 -> ""
            num < 20 -> belowTwenty[num] + " "
            num < 100 -> tens[num / 10] + " " + helper(num % 10)
            num < 1_000 -> belowTwenty[num / 100] + " Hundred " + helper(num % 100)
            num < 1_000_000 -> helper(num / 1_000) + "Thousand " + helper(num % 1_000)
            num < 1_000_000_000 -> helper(num / 1_000_000) + "Million " + helper(num % 1_000_000)
            else -> helper(num / 1_000_000_000) + "Billion " + helper(num % 1_000_000_000)
        }
    }
}
```

## Dart

```dart
class Solution {
  final List<String> _belowTen = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine"
  ];
  final List<String> _belowTwenty = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen"
  ];
  final List<String> _tens = [
    "",
    "",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety"
  ];

  String numberToWords(int num) {
    if (num == 0) return "Zero";
    String result = "";

    int billions = num ~/ 1000000000;
    if (billions > 0) {
      result += _helper(billions) + " Billion";
      num %= 1000000000;
    }

    int millions = num ~/ 1000000;
    if (millions > 0) {
      if (result.isNotEmpty) result += " ";
      result += _helper(millions) + " Million";
      num %= 1000000;
    }

    int thousands = num ~/ 1000;
    if (thousands > 0) {
      if (result.isNotEmpty) result += " ";
      result += _helper(thousands) + " Thousand";
      num %= 1000;
    }

    if (num > 0) {
      if (result.isNotEmpty) result += " ";
      result += _helper(num);
    }

    return result;
  }

  String _helper(int n) {
    if (n == 0) return "";
    if (n < 20) {
      return _belowTwenty[n];
    } else if (n < 100) {
      int ten = n ~/ 10;
      int rest = n % 10;
      return _tens[ten] + (rest != 0 ? " " + _helper(rest) : "");
    } else {
      int hundred = n ~/ 100;
      int rest = n % 100;
      return _belowTen[hundred] + " Hundred" + (rest != 0 ? " " + _helper(rest) : "");
    }
  }
}
```

## Golang

```go
import "strings"

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	below20 := []string{
		"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
		"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
		"Seventeen", "Eighteen", "Nineteen",
	}
	tens := []string{
		"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
	}
	thousands := []string{"", "Thousand", "Million", "Billion"}

	var helper func(int) string
	helper = func(n int) string {
		if n == 0 {
			return ""
		}
		if n < 20 {
			return below20[n] + " "
		}
		if n < 100 {
			return tens[n/10] + " " + helper(n%10)
		}
		return below20[n/100] + " Hundred " + helper(n%100)
	}

	parts := []string{}
	idx := 0
	for num > 0 {
		cur := num % 1000
		if cur != 0 {
			segment := strings.TrimSpace(helper(cur))
			if thousands[idx] != "" {
				segment = segment + " " + thousands[idx]
			}
			parts = append(parts, segment)
		}
		num /= 1000
		idx++
	}

	var res strings.Builder
	for i := len(parts) - 1; i >= 0; i-- {
		if res.Len() > 0 {
			res.WriteString(" ")
		}
		res.WriteString(parts[i])
	}
	return res.String()
}
```

## Ruby

```ruby
def number_to_words(num)
  return "Zero" if num == 0

  below_twenty = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
  tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
  thousands = ["","Thousand","Million","Billion"]

  helper = lambda do |n|
    if n == 0
      ""
    elsif n < 20
      below_twenty[n] + " "
    elsif n < 100
      tens[n / 10] + " " + helper.call(n % 10)
    else
      below_twenty[n / 100] + " Hundred " + helper.call(n % 100)
    end
  end

  i = 0
  words = ""
  while num > 0
    if (num % 1000) != 0
      segment = helper.call(num % 1000).strip
      segment += " #{thousands[i]}" unless thousands[i].empty?
      words = words.empty? ? segment : "#{segment} #{words}"
    end
    num /= 1000
    i += 1
  end

  words.strip
end
```

## Scala

```scala
object Solution {
  private val belowTen = Array("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
  private val belowTwenty = Array("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
  private val tens = Array("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
  private val thousands = Array("", "Thousand", "Million", "Billion")

  def numberToWords(num: Int): String = {
    if (num == 0) return "Zero"
    var n = num
    var i = 0
    var parts = List[String]()
    while (n > 0) {
      val cur = n % 1000
      if (cur != 0) {
        var seg = helper(cur)
        if (thousands(i).nonEmpty) seg = s"$seg ${thousands(i)}"
        parts = seg :: parts
      }
      n /= 1000
      i += 1
    }
    parts.mkString(" ")
  }

  private def helper(num: Int): String = {
    if (num == 0) ""
    else if (num < 10) belowTen(num)
    else if (num < 20) belowTwenty(num - 10)
    else if (num < 100) {
      val tenPart = tens(num / 10)
      val rest = num % 10
      if (rest != 0) s"$tenPart ${belowTen(rest)}" else tenPart
    } else {
      val hundredPart = belowTen(num / 100) + " Hundred"
      val rest = num % 100
      if (rest != 0) s"$hundredPart ${helper(rest)}" else hundredPart
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn number_to_words(num: i32) -> String {
        if num == 0 {
            return "Zero".to_string();
        }
        const LESS_THAN_20: [&str; 20] = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen",
        ];
        const TENS: [&str; 10] = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
        ];
        const THOUSANDS: [&str; 4] = ["", "Thousand", "Million", "Billion"];

        fn three(num: i32, less: &[&str; 20], tens: &[&str; 10]) -> String {
            let mut res = String::new();
            if num >= 100 {
                res.push_str(less[(num / 100) as usize]);
                res.push_str(" Hundred");
                if num % 100 != 0 {
                    res.push(' ');
                }
            }
            let rem = num % 100;
            if rem >= 20 {
                res.push_str(tens[(rem / 10) as usize]);
                if rem % 10 != 0 {
                    res.push(' ');
                    res.push_str(less[(rem % 10) as usize]);
                }
            } else if rem > 0 {
                res.push_str(less[rem as usize]);
            }
            res
        }

        let mut n = num;
        let mut i = 0usize;
        let mut parts: Vec<String> = Vec::new();

        while n > 0 {
            let cur = n % 1000;
            if cur != 0 {
                let mut segment = three(cur, &LESS_THAN_20, &TENS);
                if !THOUSANDS[i].is_empty() {
                    segment.push(' ');
                    segment.push_str(THOUSANDS[i]);
                }
                parts.push(segment);
            }
            n /= 1000;
            i += 1;
        }

        parts.iter().rev().map(|s| s.as_str()).collect::<Vec<&str>>().join(" ")
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (number-to-words num)
  (-> exact-integer? string?)
  (if (= num 0) "Zero"
      (let* ([below-20 #vector "" "One" "Two" "Three" "Four" "Five" "Six" "Seven" "Eight" "Nine"
                                 "Ten" "Eleven" "Twelve" "Thirteen" "Fourteen" "Fifteen"
                                 "Sixteen" "Seventeen" "Eighteen" "Nineteen"]
             [tens #vector "" "" "Twenty" "Thirty" "Forty" "Fifty" "Sixty" "Seventy" "Eighty" "Ninety"]
             [thousands #vector "" "Thousand" "Million" "Billion"])
        (define (helper n)
          (cond
            [(= n 0) ""]
            [(< n 20) (vector-ref below-20 n)]
            [(< n 100)
             (let* ([t (quotient n 10)]
                    [r (remainder n 10)])
               (if (= r 0)
                   (vector-ref tens t)
                   (string-append (vector-ref tens t) " " (helper r))))]
            [else
             (let* ([h (quotient n 100)]
                    [r (remainder n 100)])
               (if (= r 0)
                   (string-append (vector-ref below-20 h) " Hundred")
                   (string-append (vector-ref below-20 h) " Hundred " (helper r))))]))
        (let loop ((n num) (i 0) (segments '()))
          (if (= n 0)
              (string-join (reverse segments) " ")
              (let* ([cur (remainder n 1000)]
                     [rest (quotient n 1000)])
                (if (= cur 0)
                    (loop rest (+ i 1) segments)
                    (let* ([seg (helper cur)]
                           [suffix (vector-ref thousands i)]
                           [full (if (string=? suffix "")
                                     seg
                                     (string-append seg " " suffix))])
                      (loop rest (+ i 1) (cons full segments))))))))))
```

## Erlang

```erlang
-module(solution).
-export([number_to_words/1]).

-spec number_to_words(Num :: integer()) -> unicode:unicode_binary().
number_to_words(0) ->
    <<"Zero">>;
number_to_words(Num) when Num > 0 ->
    Words = convert(Num),
    unicode:characters_to_binary(string:join(Words, " ")).

convert(N) when N >= 1000000000 ->
    Billion = N div 1000000000,
    Rest = N rem 1000000000,
    Prefix = convert(Billion) ++ ["Billion"],
    case Rest of
        0 -> Prefix;
        _ -> Prefix ++ convert(Rest)
    end;
convert(N) when N >= 1000000 ->
    Million = N div 1000000,
    Rest = N rem 1000000,
    Prefix = convert(Million) ++ ["Million"],
    case Rest of
        0 -> Prefix;
        _ -> Prefix ++ convert(Rest)
    end;
convert(N) when N >= 1000 ->
    Thousand = N div 1000,
    Rest = N rem 1000,
    Prefix = convert(Thousand) ++ ["Thousand"],
    case Rest of
        0 -> Prefix;
        _ -> Prefix ++ convert(Rest)
    end;
convert(N) when N >= 100 ->
    Hundred = N div 100,
    Rest = N rem 100,
    Prefix = convert(Hundred) ++ ["Hundred"],
    case Rest of
        0 -> Prefix;
        _ -> Prefix ++ convert(Rest)
    end;
convert(N) when N >= 20 ->
    Tens = N div 10,
    Rest = N rem 10,
    TensWord = tens_word(Tens),
    case Rest of
        0 -> [TensWord];
        _ -> [TensWord] ++ convert(Rest)
    end;
convert(N) when N > 0 ->
    [unit_word(N)];
convert(0) -> [].

unit_word(1) -> "One";
unit_word(2) -> "Two";
unit_word(3) -> "Three";
unit_word(4) -> "Four";
unit_word(5) -> "Five";
unit_word(6) -> "Six";
unit_word(7) -> "Seven";
unit_word(8) -> "Eight";
unit_word(9) -> "Nine";
unit_word(10) -> "Ten";
unit_word(11) -> "Eleven";
unit_word(12) -> "Twelve";
unit_word(13) -> "Thirteen";
unit_word(14) -> "Fourteen";
unit_word(15) -> "Fifteen";
unit_word(16) -> "Sixteen";
unit_word(17) -> "Seventeen";
unit_word(18) -> "Eighteen";
unit_word(19) -> "Nineteen".

tens_word(2) -> "Twenty";
tens_word(3) -> "Thirty";
tens_word(4) -> "Forty";
tens_word(5) -> "Fifty";
tens_word(6) -> "Sixty";
tens_word(7) -> "Seventy";
tens_word(8) -> "Eighty";
tens_word(9) -> "Ninety".
```

## Elixir

```elixir
defmodule Solution do
  @spec number_to_words(num :: integer) :: String.t()
  def number_to_words(0), do: "Zero"

  def number_to_words(num) do
    below_20 = [
      "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
      "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
      "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]

    tens = [
      "", "", "Twenty", "Thirty", "Forty", "Fifty",
      "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    thousands = ["", "Thousand", "Million", "Billion"]

    build(num, 0, "", thousands, below_20, tens)
  end

  defp build(0, _idx, acc, _thousands, _below_20, _tens), do: acc

  defp build(num, idx, acc, thousands, below_20, tens) do
    cur = rem(num, 1000)

    new_acc =
      if cur == 0 do
        acc
      else
        words = convert_chunk(cur, below_20, tens)
        scale = Enum.at(thousands, idx)
        segment = if scale == "", do: words, else: words <> " " <> scale

        if acc == "", do: segment, else: segment <> " " <> acc
      end

    build(div(num, 1000), idx + 1, new_acc, thousands, below_20, tens)
  end

  defp convert_chunk(0, _below_20, _tens), do: ""

  defp convert_chunk(n, below_20, _tens) when n < 20,
    do: Enum.at(below_20, n)

  defp convert_chunk(n, below_20, tens) when n < 100 do
    ten = div(n, 10)
    rest = rem(n, 10)
    base = Enum.at(tens, ten)

    if rest == 0,
      do: base,
      else: base <> " " <> Enum.at(below_20, rest)
  end

  defp convert_chunk(n, below_20, tens) when n < 1000 do
    hundred = div(n, 100)
    rest = rem(n, 100)
    part = Enum.at(below_20, hundred) <> " Hundred"

    if rest == 0,
      do: part,
      else: part <> " " <> convert_chunk(rest, below_20, tens)
  end
end
```
