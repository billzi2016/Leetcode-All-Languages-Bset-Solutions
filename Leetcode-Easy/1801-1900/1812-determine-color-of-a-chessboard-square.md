# 1812. Determine Color of a Chessboard Square

## Cpp

```cpp
class Solution {
public:
    bool squareIsWhite(string coordinates) {
        int file = coordinates[0] - 'a' + 1;
        int rank = coordinates[1] - '0';
        return ((file + rank) % 2) == 1;
    }
};
```

## Java

```java
class Solution {
    public boolean squareIsWhite(String coordinates) {
        int col = coordinates.charAt(0) - 'a' + 1;
        int row = coordinates.charAt(1) - '0';
        return ((col + row) & 1) == 1;
    }
}
```

## Python

```python
class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        col = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])
        return (col + row) % 2 == 1
```

## Python3

```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])
        return (col + row) % 2 == 1
```

## C

```c
#include <stdbool.h>

bool squareIsWhite(char* coordinates) {
    int x = coordinates[0] - 'a' + 1;
    int y = coordinates[1] - '0';
    return ((x + y) % 2) == 1;
}
```

## Csharp

```csharp
public class Solution {
    public bool SquareIsWhite(string coordinates) {
        int col = coordinates[0] - 'a' + 1;
        int row = coordinates[1] - '0';
        return ((col + row) & 1) == 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} coordinates
 * @return {boolean}
 */
var squareIsWhite = function(coordinates) {
    const file = coordinates.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
    const rank = coordinates.charCodeAt(1) - '0';
    return (file + rank) % 2 === 1;
};
```

## Typescript

```typescript
function squareIsWhite(coordinates: string): boolean {
    const col = coordinates.charCodeAt(0) - 96; // 'a' is 97 in ASCII
    const row = Number(coordinates[1]);
    return ((col + row) & 1) === 1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $coordinates
     * @return Boolean
     */
    function squareIsWhite($coordinates) {
        $col = ord($coordinates[0]) - ord('a') + 1;
        $row = intval($coordinates[1]);
        return (($col + $row) % 2) === 1;
    }
}
```

## Swift

```swift
class Solution {
    func squareIsWhite(_ coordinates: String) -> Bool {
        let chars = Array(coordinates)
        guard chars.count == 2,
              let colAscii = chars[0].asciiValue,
              let rowVal = chars[1].wholeNumberValue else { return false }
        let col = Int(colAscii - Character("a").asciiValue! + 1)
        let sum = col + rowVal
        return sum % 2 == 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun squareIsWhite(coordinates: String): Boolean {
        val col = coordinates[0] - 'a' + 1
        val row = coordinates[1] - '0'
        return ((col + row) % 2 == 1)
    }
}
```

## Dart

```dart
class Solution {
  bool squareIsWhite(String coordinates) {
    int col = coordinates.codeUnitAt(0) - 'a'.codeUnitAt(0);
    int row = coordinates.codeUnitAt(1) - '1'.codeUnitAt(0);
    return ((col + row) & 1) == 1;
  }
}
```

## Golang

```go
func squareIsWhite(coordinates string) bool {
	file := int(coordinates[0]-'a') + 1
	rank := int(coordinates[1] - '0')
	return (file+rank)%2 == 1
}
```

## Ruby

```ruby
def square_is_white(coordinates)
  file = coordinates[0].ord - 'a'.ord + 1
  rank = coordinates[1].to_i
  ((file + rank) & 1) == 1
end
```

## Scala

```scala
object Solution {
    def squareIsWhite(coordinates: String): Boolean = {
        val col = coordinates.charAt(0) - 'a' + 1
        val row = coordinates.charAt(1) - '0'
        ((col + row) % 2) == 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        let bytes = coordinates.as_bytes();
        let col = (bytes[0] - b'a' + 1) as i32;
        let row = (bytes[1] - b'0') as i32;
        ((col + row) % 2) != 0
    }
}
```

## Racket

```racket
(define/contract (square-is-white coordinates)
  (-> string? boolean?)
  (let* ([file-char (string-ref coordinates 0)]
         [rank-num (string->number (substring coordinates 1 2))]
         [file-index (+ 1 (- (char->integer file-char) (char->integer #\a)))]
         [sum (+ file-index rank-num)])
    (= (modulo sum 2) 1)))
```

## Erlang

```erlang
-spec square_is_white(Coordinates :: unicode:unicode_binary()) -> boolean().
square_is_white(<<FileChar, RankChar>>) ->
    File = FileChar - $a + 1,
    Rank = RankChar - $0,
    ((File + Rank) band 1) =:= 1;
square_is_white([FileChar, RankChar]) ->
    File = FileChar - $a + 1,
    Rank = RankChar - $0,
    ((File + Rank) band 1) =:= 1.
```

## Elixir

```elixir
defmodule Solution do
  @spec square_is_white(coordinates :: String.t) :: boolean
  def square_is_white(<<file, rank>> ) do
    x = file - ?a + 1
    y = rank - ?0
    rem(x + y, 2) == 1
  end
end
```
