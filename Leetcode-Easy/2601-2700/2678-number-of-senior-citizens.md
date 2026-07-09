# 2678. Number of Senior Citizens

## Cpp

```cpp
class Solution {
public:
    int countSeniors(std::vector<std::string>& details) {
        int seniorCount = 0;
        for (const std::string& info : details) {
            int age = (info[11] - '0') * 10 + (info[12] - '0');
            if (age > 60) ++seniorCount;
        }
        return seniorCount;
    }
};
```

## Java

```java
class Solution {
    public int countSeniors(String[] details) {
        int seniors = 0;
        for (String d : details) {
            int age = (d.charAt(11) - '0') * 10 + (d.charAt(12) - '0');
            if (age > 60) {
                seniors++;
            }
        }
        return seniors;
    }
}
```

## Python

```python
class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        senior = 0
        for d in details:
            age = (ord(d[11]) - 48) * 10 + (ord(d[12]) - 48)
            if age > 60:
                senior += 1
        return senior
```

## Python3

```python
from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_count = 0
        for info in details:
            age = (ord(info[11]) - ord('0')) * 10 + (ord(info[12]) - ord('0'))
            if age > 60:
                senior_count += 1
        return senior_count
```

## C

```c
int countSeniors(char** details, int detailsSize) {
    int seniors = 0;
    for (int i = 0; i < detailsSize; ++i) {
        const char *s = details[i];
        int age = (s[11] - '0') * 10 + (s[12] - '0');
        if (age > 60) {
            ++seniors;
        }
    }
    return seniors;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountSeniors(string[] details)
    {
        int seniorCount = 0;
        foreach (var info in details)
        {
            int age = (info[11] - '0') * 10 + (info[12] - '0');
            if (age > 60)
                seniorCount++;
        }
        return seniorCount;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
    let seniorCount = 0;
    for (const info of details) {
        const age = (info.charCodeAt(11) - 48) * 10 + (info.charCodeAt(12) - 48);
        if (age > 60) seniorCount++;
    }
    return seniorCount;
};
```

## Typescript

```typescript
function countSeniors(details: string[]): number {
    let seniorCount = 0;
    for (const info of details) {
        const age = (info.charCodeAt(11) - 48) * 10 + (info.charCodeAt(12) - 48);
        if (age > 60) seniorCount++;
    }
    return seniorCount;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $details
     * @return Integer
     */
    function countSeniors($details) {
        $count = 0;
        foreach ($details as $s) {
            $age = (ord($s[11]) - 48) * 10 + (ord($s[12]) - 48);
            if ($age > 60) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countSeniors(_ details: [String]) -> Int {
        var seniorCount = 0
        for info in details {
            let tensIndex = info.index(info.startIndex, offsetBy: 11)
            let onesIndex = info.index(info.startIndex, offsetBy: 12)
            let tensChar = info[tensIndex]
            let onesChar = info[onesIndex]
            if let tensScalar = tensChar.unicodeScalars.first,
               let onesScalar = onesChar.unicodeScalars.first {
                let age = Int(tensScalar.value - 48) * 10 + Int(onesScalar.value - 48)
                if age > 60 {
                    seniorCount += 1
                }
            }
        }
        return seniorCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSeniors(details: Array<String>): Int {
        var seniorCount = 0
        for (detail in details) {
            val age = (detail[11] - '0') * 10 + (detail[12] - '0')
            if (age > 60) seniorCount++
        }
        return seniorCount
    }
}
```

## Dart

```dart
class Solution {
  int countSeniors(List<String> details) {
    int seniorCount = 0;
    for (var info in details) {
      int tens = info.codeUnitAt(11) - 48; // '0' ASCII is 48
      int ones = info.codeUnitAt(12) - 48;
      int age = tens * 10 + ones;
      if (age > 60) seniorCount++;
    }
    return seniorCount;
  }
}
```

## Golang

```go
func countSeniors(details []string) int {
	cnt := 0
	for _, s := range details {
		age := (s[11] - '0')*10 + (s[12] - '0')
		if age > 60 {
			cnt++
		}
	}
	return cnt
}
```

## Ruby

```ruby
def count_seniors(details)
  count = 0
  details.each do |s|
    age = (s.getbyte(11) - 48) * 10 + (s.getbyte(12) - 48)
    count += 1 if age > 60
  end
  count
end
```

## Scala

```scala
object Solution {
    def countSeniors(details: Array[String]): Int = {
        var seniorCount = 0
        for (info <- details) {
            val age = (info.charAt(11) - '0') * 10 + (info.charAt(12) - '0')
            if (age > 60) seniorCount += 1
        }
        seniorCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        let mut count = 0;
        for s in details.iter() {
            let b = s.as_bytes();
            let age = (b[11] - b'0') * 10 + (b[12] - b'0');
            if age > 60 {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-seniors details)
  (-> (listof string?) exact-integer?)
  (foldl (lambda (s acc)
           (let* ((tens (- (char->integer (string-ref s 11))
                           (char->integer #\0)))
                  (ones (- (char->integer (string-ref s 12))
                           (char->integer #\0)))
                  (age (+ (* tens 10) ones)))
             (if (> age 60) (add1 acc) acc)))
         0
         details))
```

## Erlang

```erlang
-spec count_seniors(Details :: [unicode:unicode_binary()]) -> integer().
count_seniors(Details) ->
    lists:foldl(
        fun(Bin, Acc) ->
            case Bin of
                <<_:11, Tens, Ones, _/binary>> ->
                    Age = (Tens - $0) * 10 + (Ones - $0),
                    if Age > 60 -> Acc + 1; true -> Acc end;
                _ -> Acc
            end
        end,
        0,
        Details
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_seniors(details :: [String.t]) :: integer
  def count_seniors(details) do
    Enum.reduce(details, 0, fn detail, acc ->
      <<_::binary-size(11), tens, ones, _rest::binary>> = detail
      age = (tens - ?0) * 10 + (ones - ?0)
      if age > 60, do: acc + 1, else: acc
    end)
  end
end
```
