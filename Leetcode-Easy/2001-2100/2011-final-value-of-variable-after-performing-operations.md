# 2011. Final Value of Variable After Performing Operations

## Cpp

```cpp
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (const string& op : operations) {
            if (op.find("++") != string::npos) ++x;
            else --x;
        }
        return x;
    }
};
```

## Java

```java
class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for (String op : operations) {
            if (op.charAt(0) == '+' || op.charAt(1) == '+') {
                x++;
            } else {
                x--;
            }
        }
        return x;
    }
}
```

## Python

```python
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x
```

## Python3

```python
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x
```

## C

```c
int finalValueAfterOperations(char** operations, int operationsSize) {
    int x = 0;
    for (int i = 0; i < operationsSize; ++i) {
        if (operations[i][0] == '+' || operations[i][1] == '+')
            ++x;
        else
            --x;
    }
    return x;
}
```

## Csharp

```csharp
public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int x = 0;
        foreach (var op in operations) {
            if (op.Contains("++")) {
                x++;
            } else {
                x--;
            }
        }
        return x;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x = 0;
    for (const op of operations) {
        if (op.includes('++')) {
            x++;
        } else {
            x--;
        }
    }
    return x;
};
```

## Typescript

```typescript
function finalValueAfterOperations(operations: string[]): number {
    let x = 0;
    for (const op of operations) {
        // If the operation contains "++", increment; otherwise decrement.
        if (op.includes('++')) {
            x++;
        } else {
            x--;
        }
    }
    return x;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $operations
     * @return Integer
     */
    function finalValueAfterOperations($operations) {
        $x = 0;
        foreach ($operations as $op) {
            if (strpos($op, '++') !== false) {
                $x++;
            } else {
                $x--;
            }
        }
        return $x;
    }
}
```

## Swift

```swift
class Solution {
    func finalValueAfterOperations(_ operations: [String]) -> Int {
        var x = 0
        for op in operations {
            if op == "++X" || op == "X++" {
                x += 1
            } else {
                x -= 1
            }
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun finalValueAfterOperations(operations: Array<String>): Int {
        var x = 0
        for (op in operations) {
            if (op.contains("++")) {
                x++
            } else {
                x--
            }
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int finalValueAfterOperations(List<String> operations) {
    int x = 0;
    for (var op in operations) {
      if (op.contains('++')) {
        x++;
      } else {
        x--;
      }
    }
    return x;
  }
}
```

## Golang

```go
func finalValueAfterOperations(operations []string) int {
    x := 0
    for _, op := range operations {
        if op[0] == '+' || op[1] == '+' {
            x++
        } else {
            x--
        }
    }
    return x
}
```

## Ruby

```ruby
def final_value_after_operations(operations)
  x = 0
  operations.each do |op|
    if op.include?("++")
      x += 1
    else
      x -= 1
    end
  end
  x
end
```

## Scala

```scala
object Solution {
    def finalValueAfterOperations(operations: Array[String]): Int = {
        var x = 0
        for (op <- operations) {
            if (op == "++X" || op == "X++") x += 1
            else x -= 1
        }
        x
    }
}
```

## Rust

```rust
impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut x = 0;
        for op in operations.iter() {
            if op.contains('+') {
                x += 1;
            } else {
                x -= 1;
            }
        }
        x
    }
}
```

## Racket

```racket
(define/contract (final-value-after-operations operations)
  (-> (listof string?) exact-integer?)
  (foldl (lambda (op acc)
           (cond [(or (string=? op "++X") (string=? op "X++")) (+ acc 1)]
                 [else (- acc 1)]))
         0
         operations))
```

## Erlang

```erlang
-spec final_value_after_operations(Operations :: [unicode:unicode_binary()]) -> integer().
final_value_after_operations(Operations) ->
    lists:foldl(
        fun(Op, Acc) ->
            case Op of
                <<"++X">> -> Acc + 1;
                <<"X++">> -> Acc + 1;
                <<"--X">> -> Acc - 1;
                <<"X--">> -> Acc - 1
            end
        end,
        0,
        Operations
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec final_value_after_operations(operations :: [String.t]) :: integer
  def final_value_after_operations(operations) do
    Enum.reduce(operations, 0, fn op, acc ->
      case op do
        "++X" -> acc + 1
        "X++" -> acc + 1
        "--X" -> acc - 1
        "X--" -> acc - 1
        _ -> acc
      end
    end)
  end
end
```
