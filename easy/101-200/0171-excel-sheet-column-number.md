# 0171. Excel Sheet Column Number

## Cpp

```cpp
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0;
        for (char c : columnTitle) {
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int titleToNumber(String columnTitle) {
        int result = 0;
        for (int i = 0; i < columnTitle.length(); i++) {
            char c = columnTitle.charAt(i);
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for c in columnTitle:
            result = result * 26 + (ord(c) - ord('A') + 1)
        return result
```

## Python3

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result
```

## C

```c
int titleToNumber(char* columnTitle) {
    int result = 0;
    for (int i = 0; columnTitle[i] != '\0'; ++i) {
        result = result * 26 + (columnTitle[i] - 'A' + 1);
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int TitleToNumber(string columnTitle)
    {
        int result = 0;
        foreach (char c in columnTitle)
        {
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    let result = 0;
    for (let i = 0; i < columnTitle.length; i++) {
        const charCode = columnTitle.charCodeAt(i) - 64; // 'A' -> 1
        result = result * 26 + charCode;
    }
    return result;
};
```

## Typescript

```typescript
function titleToNumber(columnTitle: string): number {
    let result = 0;
    for (let i = 0; i < columnTitle.length; i++) {
        const value = columnTitle.charCodeAt(i) - 64; // 'A' -> 1
        result = result * 26 + value;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $columnTitle
     * @return Integer
     */
    function titleToNumber($columnTitle) {
        $result = 0;
        $len = strlen($columnTitle);
        for ($i = 0; $i < $len; $i++) {
            $charVal = ord($columnTitle[$i]) - ord('A') + 1;
            $result = $result * 26 + $charVal;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func titleToNumber(_ columnTitle: String) -> Int {
        var result = 0
        for scalar in columnTitle.unicodeScalars {
            let value = Int(scalar.value) - 64 // 'A' is 65 in ASCII/Unicode
            result = result * 26 + value
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun titleToNumber(columnTitle: String): Int {
        var result = 0
        for (ch in columnTitle) {
            result = result * 26 + (ch - 'A' + 1)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int titleToNumber(String columnTitle) {
    int result = 0;
    for (int i = 0; i < columnTitle.length; i++) {
      int value = columnTitle.codeUnitAt(i) - 'A'.codeUnitAt(0) + 1;
      result = result * 26 + value;
    }
    return result;
  }
}
```

## Golang

```go
func titleToNumber(columnTitle string) int {
    result := 0
    for i := 0; i < len(columnTitle); i++ {
        result = result*26 + int(columnTitle[i]-'A'+1)
    }
    return result
}
```

## Ruby

```ruby
def title_to_number(column_title)
  result = 0
  column_title.each_byte do |b|
    result = result * 26 + (b - 64) # 'A'.ord == 65, so subtract 64 to get 1..26
  end
  result
end
```

## Scala

```scala
object Solution {
    def titleToNumber(columnTitle: String): Int = {
        var result: Long = 0L
        for (c <- columnTitle) {
            result = result * 26 + (c - 'A' + 1)
        }
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        let mut result: i32 = 0;
        for b in column_title.bytes() {
            let digit = (b - b'A' + 1) as i32;
            result = result * 26 + digit;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (title-to-number columnTitle)
  (-> string? exact-integer?)
  (let loop ((i 0) (result 0))
    (if (= i (string-length columnTitle))
        result
        (let* ((c (string-ref columnTitle i))
               (val (+ (- (char->integer c) (char->integer #\A)) 1)))
          (loop (+ i 1) (+ (* result 26) val))))))
```

## Erlang

```erlang
-module(solution).
-export([title_to_number/1]).

-spec title_to_number(ColumnTitle :: unicode:unicode_binary()) -> integer().
title_to_number(ColumnTitle) ->
    title_to_number(binary_to_list(ColumnTitle), 0).

title_to_number([], Acc) -> 
    Acc;
title_to_number([C|Rest], Acc) ->
    Digit = C - $A + 1,
    NewAcc = Acc * 26 + Digit,
    title_to_number(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec title_to_number(column_title :: String.t) :: integer
  def title_to_number(column_title) do
    column_title
    |> String.to_charlist()
    |> Enum.reduce(0, fn char, acc ->
      acc * 26 + (char - ?A + 1)
    end)
  end
end
```
