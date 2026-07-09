# 3274. Check if Two Chessboard Squares Have the Same Color

## Cpp

```cpp
class Solution {
public:
    bool checkTwoChessboards(string coordinate1, string coordinate2) {
        auto color = [](const string& s) -> int {
            int col = s[0] - 'a' + 1; // a->1 ... h->8
            int row = s[1] - '0';     // '1'->1 ... '8'->8
            return (col + row) % 2;
        };
        return color(coordinate1) == color(coordinate2);
    }
};
```

## Java

```java
class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        int col1 = coordinate1.charAt(0) - 'a' + 1;
        int row1 = coordinate1.charAt(1) - '0';
        int col2 = coordinate2.charAt(0) - 'a' + 1;
        int row2 = coordinate2.charAt(1) - '0';
        return ((col1 + row1) & 1) == ((col2 + row2) & 1);
    }
}
```

## Python

```python
class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        def color(coord):
            col = ord(coord[0]) - ord('a')
            row = int(coord[1]) - 1
            return (col + row) & 1
        return color(coordinate1) == color(coordinate2)
```

## Python3

```python
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        col1 = ord(coordinate1[0]) - ord('a')
        row1 = int(coordinate1[1]) - 1
        col2 = ord(coordinate2[0]) - ord('a')
        row2 = int(coordinate2[1]) - 1
        return (col1 + row1) % 2 == (col2 + row2) % 2
```

## C

```c
#include <stdbool.h>

bool checkTwoChessboards(char* coordinate1, char* coordinate2) {
    int col1 = coordinate1[0] - 'a';
    int row1 = coordinate1[1] - '1';
    int col2 = coordinate2[0] - 'a';
    int row2 = coordinate2[1] - '1';
    return ((col1 + row1) & 1) == ((col2 + row2) & 1);
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckTwoChessboards(string coordinate1, string coordinate2) {
        int col1 = coordinate1[0] - 'a' + 1;
        int row1 = coordinate1[1] - '0';
        int col2 = coordinate2[0] - 'a' + 1;
        int row2 = coordinate2[1] - '0';
        return ((col1 + row1) & 1) == ((col2 + row2) & 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} coordinate1
 * @param {string} coordinate2
 * @return {boolean}
 */
var checkTwoChessboards = function(coordinate1, coordinate2) {
    const parity1 = (coordinate1.charCodeAt(0) + coordinate1.charCodeAt(1)) & 1;
    const parity2 = (coordinate2.charCodeAt(0) + coordinate2.charCodeAt(1)) & 1;
    return parity1 === parity2;
};
```

## Typescript

```typescript
function checkTwoChessboards(coordinate1: string, coordinate2: string): boolean {
    const getParity = (coord: string): number => {
        const col = coord.charCodeAt(0) - 'a'.charCodeAt(0);
        const row = parseInt(coord[1], 10) - 1;
        return (col + row) & 1; // 0 for even, 1 for odd
    };
    return getParity(coordinate1) === getParity(coordinate2);
}
```

## Php

```php
class Solution {

    /**
     * @param String $coordinate1
     * @param String $coordinate2
     * @return Boolean
     */
    function checkTwoChessboards($coordinate1, $coordinate2) {
        $col1 = ord($coordinate1[0]) - ord('a') + 1;
        $row1 = intval($coordinate1[1]);
        $col2 = ord($coordinate2[0]) - ord('a') + 1;
        $row2 = intval($coordinate2[1]);

        return (($col1 + $row1) % 2) === (($col2 + $row2) % 2);
    }
}
```

## Swift

```swift
class Solution {
    func checkTwoChessboards(_ coordinate1: String, _ coordinate2: String) -> Bool {
        let chars1 = Array(coordinate1)
        let chars2 = Array(coordinate2)
        
        let col1 = Int(chars1[0].unicodeScalars.first!.value - UnicodeScalar("a").value)
        let row1 = Int(String(chars1[1]))! - 1
        
        let col2 = Int(chars2[0].unicodeScalars.first!.value - UnicodeScalar("a").value)
        let row2 = Int(String(chars2[1]))! - 1
        
        return (col1 + row1) % 2 == (col2 + row2) % 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkTwoChessboards(coordinate1: String, coordinate2: String): Boolean {
        val col1 = coordinate1[0] - 'a'
        val row1 = coordinate1[1] - '1'
        val col2 = coordinate2[0] - 'a'
        val row2 = coordinate2[1] - '1'
        return (col1 + row1) % 2 == (col2 + row2) % 2
    }
}
```

## Dart

```dart
class Solution {
  bool checkTwoChessboards(String coordinate1, String coordinate2) {
    int col1 = coordinate1.codeUnitAt(0) - 'a'.codeUnitAt(0);
    int row1 = coordinate1.codeUnitAt(1) - '1'.codeUnitAt(0);
    int col2 = coordinate2.codeUnitAt(0) - 'a'.codeUnitAt(0);
    int row2 = coordinate2.codeUnitAt(1) - '1'.codeUnitAt(0);
    return ((col1 + row1) & 1) == ((col2 + row2) & 1);
  }
}
```

## Golang

```go
func checkTwoChessboards(coordinate1 string, coordinate2 string) bool {
	c1 := int(coordinate1[0]-'a') + int(coordinate1[1]-'1')
	c2 := int(coordinate2[0]-'a') + int(coordinate2[1]-'1')
	return c1%2 == c2%2
}
```

## Ruby

```ruby
# @param {String} coordinate1
# @param {String} coordinate2
# @return {Boolean}
def check_two_chessboards(coordinate1, coordinate2)
  col1 = coordinate1[0].ord - 'a'.ord
  row1 = coordinate1[1].to_i
  col2 = coordinate2[0].ord - 'a'.ord
  row2 = coordinate2[1].to_i

  ((col1 + row1) & 1) == ((col2 + row2) & 1)
end
```

## Scala

```scala
object Solution {
    def checkTwoChessboards(coordinate1: String, coordinate2: String): Boolean = {
        def parity(coord: String): Int = {
            val col = coord.charAt(0) - 'a'
            val row = coord.charAt(1) - '1'
            (col + row) & 1
        }
        parity(coordinate1) == parity(coordinate2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_two_chessboards(coordinate1: String, coordinate2: String) -> bool {
        let b1 = coordinate1.as_bytes();
        let col1 = (b1[0] - b'a') as i32;
        let row1 = (b1[1] - b'1') as i32;
        let parity1 = (col1 + row1) & 1;

        let b2 = coordinate2.as_bytes();
        let col2 = (b2[0] - b'a') as i32;
        let row2 = (b2[1] - b'1') as i32;
        let parity2 = (col2 + row2) & 1;

        parity1 == parity2
    }
}
```

## Racket

```racket
(define/contract (check-two-chessboards coordinate1 coordinate2)
  (-> string? string? boolean?)
  (let* ((col1 (+ (- (char->integer (string-ref coordinate1 0)) (char->integer #\a)) 1))
         (row1 (- (char->integer (string-ref coordinate1 1)) (char->integer #\0)))
         (col2 (+ (- (char->integer (string-ref coordinate2 0)) (char->integer #\a)) 1))
         (row2 (- (char->integer (string-ref coordinate2 1)) (char->integer #\0))))
    (= (modulo (+ col1 row1) 2)
       (modulo (+ col2 row2) 2))))
```

## Erlang

```erlang
-spec check_two_chessboards(Coordinate1 :: unicode:unicode_binary(), Coordinate2 :: unicode:unicode_binary()) -> boolean().
check_two_chessboards(Coordinate1, Coordinate2) ->
    <<C1, R1>> = Coordinate1,
    <<C2, R2>> = Coordinate2,
    ColIdx1 = C1 - $a + 1,
    RowIdx1 = R1 - $0,
    ColIdx2 = C2 - $a + 1,
    RowIdx2 = R2 - $0,
    ((ColIdx1 + RowIdx1) band 1) =:= ((ColIdx2 + RowIdx2) band 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec check_two_chessboards(coordinate1 :: String.t(), coordinate2 :: String.t()) :: boolean()
  def check_two_chessboards(coord1, coord2) do
    {c1_col, c1_row} = parse(coord1)
    {c2_col, c2_row} = parse(coord2)

    rem(c1_col + c1_row, 2) == rem(c2_col + c2_row, 2)
  end

  defp parse(<<col::utf8, row::utf8>>) do
    col_index = col - ?a + 1
    row_num = row - ?0
    {col_index, row_num}
  end
end
```
