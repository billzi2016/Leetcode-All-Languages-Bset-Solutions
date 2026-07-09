# 3228. Maximum Number of Operations to Move Ones to the End

## Cpp

```cpp
class Solution {
public:
    int maxOperations(string s) {
        long long zeroCount = 0;
        long long ans = 0;
        for (int i = (int)s.size() - 1; i >= 0; --i) {
            if (s[i] == '0') {
                ++zeroCount;
            } else { // s[i] == '1'
                ans += zeroCount;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxOperations(String s) {
        long ones = 0;
        long ops = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') {
                ones++;
            } else { // c == '0'
                ops += ones;
            }
        }
        return (int) ops;
    }
}
```

## Python

```python
class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = 0
        ops = 0
        for ch in s:
            if ch == '1':
                ones += 1
            else:  # ch == '0'
                ops += ones
        return ops
```

## Python3

```python
class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ops = 0
        for ch in s:
            if ch == '1':
                ones += 1
            else:  # ch == '0'
                ops += ones
        return ops
```

## C

```c
#include <stddef.h>

int maxOperations(char* s) {
    long long zeros = 0;
    long long ops = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '0') {
            zeros++;
        } else { // '1'
            ops += zeros;
        }
    }
    return (int)ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxOperations(string s) {
        long ans = 0;
        int zeroGroups = 0;
        for (int i = s.Length - 1; i >= 0; --i) {
            if (s[i] == '0') {
                if (i == s.Length - 1 || s[i + 1] != '0') {
                    zeroGroups++;
                }
            } else { // '1'
                ans += zeroGroups;
            }
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxOperations = function(s) {
    let ones = 0;
    let ops = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '1') {
            ones++;
        } else {
            ops += ones;
        }
    }
    return ops;
};
```

## Typescript

```typescript
function maxOperations(s: string): number {
    let ones = 0;
    let operations = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            ones++;
        } else { // s[i] === '0'
            operations += ones;
        }
    }
    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxOperations($s) {
        $ones = 0;
        $ans = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '1') {
                $ones++;
            } else { // '0'
                $ans += $ones;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxOperations(_ s: String) -> Int {
        var zeroCount = 0
        var operations = 0
        for ch in s.reversed() {
            if ch == "0" {
                zeroCount += 1
            } else { // ch == '1'
                operations += zeroCount
            }
        }
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxOperations(s: String): Int {
        var ones = 0L
        var ops = 0L
        for (ch in s) {
            if (ch == '1') {
                ones++
            } else { // ch == '0'
                ops += ones
            }
        }
        return ops.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxOperations(String s) {
    int zeroCount = 0;
    int operations = 0;
    for (int i = s.length - 1; i >= 0; --i) {
      if (s.codeUnitAt(i) == 48) { // '0'
        zeroCount++;
      } else { // '1'
        operations += zeroCount;
      }
    }
    return operations;
  }
}
```

## Golang

```go
func maxOperations(s string) int {
    var zeros, ops int64
    for i := len(s) - 1; i >= 0; i-- {
        if s[i] == '0' {
            zeros++
        } else { // s[i] == '1'
            ops += zeros
        }
    }
    return int(ops)
}
```

## Ruby

```ruby
def max_operations(s)
  ones = 0
  ops = 0
  s.each_char do |ch|
    if ch == '1'
      ones += 1
    else # '0'
      ops += ones
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def maxOperations(s: String): Int = {
        var ones: Long = 0L
        var ops: Long = 0L
        for (c <- s) {
            if (c == '1') {
                ones += 1
            } else { // c == '0'
                ops += ones
            }
        }
        ops.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_operations(s: String) -> i32 {
        let mut ones: i64 = 0;
        let mut ops: i64 = 0;
        for ch in s.bytes() {
            if ch == b'1' {
                ones += 1;
            } else { // '0'
                ops += ones;
            }
        }
        ops as i32
    }
}
```

## Racket

```racket
(define/contract (max-operations s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (zeros 0)
         (ans 0))
    (for ([i (in-range (- n 1) -1 -1)])
      (if (char=? (string-ref s i) #\0)
          (set! zeros (+ zeros 1))
          (set! ans (+ ans zeros))))
    ans))
```

## Erlang

```erlang
-spec max_operations(S :: unicode:unicode_binary()) -> integer().
max_operations(S) ->
    List = binary_to_list(S),
    TotalZeros = count_zeros(List, 0),
    {Ans,_} = lists:foldl(
        fun(C,{A,Z}) ->
            if C == $0 -> {A, Z-1};
               true   -> {A+Z, Z}
            end
        end,
        {0, TotalZeros},
        List),
    Ans.

count_zeros([], Acc) -> Acc;
count_zeros([H|T], Acc) ->
    if H == $0 -> count_zeros(T, Acc + 1);
       true   -> count_zeros(T, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_operations(s :: String.t) :: integer
  def max_operations(s) do
    {ans, _zeros} =
      s
      |> String.graphemes()
      |> Enum.reduce({0, 0}, fn ch, {ans, zeros} ->
        case ch do
          "0" -> {ans, zeros + 1}
          "1" ->
            if zeros > 0 do
              {ans + zeros, zeros - 1}
            else
              {ans, zeros}
            end
        end
      end)

    ans
  end
end
```
