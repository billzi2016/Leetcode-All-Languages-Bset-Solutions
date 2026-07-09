# 1404. Number of Steps to Reduce a Number in Binary Representation to One

## Cpp

```cpp
class Solution {
public:
    int numSteps(string s) {
        int n = s.size();
        int operations = 0;
        int carry = 0;
        for (int i = n - 1; i > 0; --i) {
            int bit = (s[i] - '0') + carry;
            if (bit % 2 == 1) { // odd
                operations += 2; // add 1 then divide by 2
                carry = 1;       // overflow to the next higher bit
            } else {
                operations += 1; // just divide by 2
                // carry remains unchanged
            }
        }
        return operations + carry;
    }
};
```

## Java

```java
class Solution {
    public int numSteps(String s) {
        int n = s.length();
        int operations = 0;
        int carry = 0;
        for (int i = n - 1; i > 0; --i) {
            int bit = s.charAt(i) - '0';
            int sum = bit + carry;
            if (sum == 1) { // odd
                operations += 2;
                carry = 1;
            } else { // even (0 or 2)
                operations += 1;
                // carry remains unchanged
            }
        }
        return operations + carry;
    }
}
```

## Python

```python
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            bit = (ord(s[i]) - 48) + carry  # convert char to int and add carry
            if bit & 1:          # odd
                ops += 2
                carry = 1
            else:                # even
                ops += 1
                # carry remains unchanged
        return ops + carry
```

## Python3

```python
class Solution:
    def numSteps(self, s: str) -> int:
        ops = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            bit = (ord(s[i]) - 48) + carry  # convert char to int and add carry
            if bit & 1:          # odd
                ops += 2
                carry = 1
            else:                # even
                ops += 1
                # carry remains unchanged
        return ops + carry
```

## C

```c
#include <string.h>

int numSteps(char* s) {
    int len = strlen(s);
    int steps = 0;
    int carry = 0;

    for (int i = len - 1; i > 0; --i) {
        int bit = s[i] - '0';
        int sum = bit + carry;
        if (sum == 1) {          // odd
            steps += 2;          // add 1 then divide by 2
            carry = 1;           // result generates a carry to the next higher bit
        } else {
            steps += 1;          // just divide by 2
            carry = sum / 2;     // sum is 0 or 2, propagate possible carry
        }
    }

    return steps + carry;
}
```

## Csharp

```csharp
public class Solution {
    public int NumSteps(string s) {
        int operations = 0;
        int carry = 0;
        for (int i = s.Length - 1; i > 0; --i) {
            int bit = s[i] - '0';
            int sum = bit + carry;
            if ((sum & 1) == 1) { // odd
                operations += 2;
                carry = 1;
            } else { // even
                operations += 1;
                // carry remains unchanged (if sum == 2, carry stays 1)
            }
        }
        return operations + carry;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numSteps = function(s) {
    const n = s.length;
    if (n === 1) return 0;
    let ops = 0;
    let carry = 0;
    for (let i = n - 1; i > 0; --i) {
        const bit = (s.charCodeAt(i) - 48) + carry; // current bit plus any carry
        if (bit % 2 === 1) { // odd -> need add 1 then divide
            ops += 2;
            carry = 1;      // addition creates a carry to the left
        } else {
            ops += 1;       // even -> just divide
            // carry remains unchanged
        }
    }
    return ops + carry;
};
```

## Typescript

```typescript
function numSteps(s: string): number {
    let operations = 0;
    let carry = 0;
    for (let i = s.length - 1; i > 0; i--) {
        const bit = (s.charCodeAt(i) - 48) + carry;
        if (bit % 2 === 1) { // odd
            operations += 2;
            carry = 1;
        } else { // even
            operations += 1;
            // carry remains unchanged
        }
    }
    return operations + carry;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numSteps($s) {
        $n = strlen($s);
        if ($n == 1) {
            return 0;
        }
        $steps = 0;
        $carry = 0;
        for ($i = $n - 1; $i > 0; --$i) {
            $bit = intval($s[$i]);
            $cur = $bit + $carry;
            if ($cur == 1) {          // odd
                $steps += 2;
                $carry = 1;
            } else {                  // even (0 or 2)
                $steps += 1;
                // carry remains unchanged
            }
        }
        return $steps + $carry;
    }
}
```

## Swift

```swift
class Solution {
    func numSteps(_ s: String) -> Int {
        let chars = Array(s)
        var operations = 0
        var carry = 0
        
        // Process from least significant bit to the second most significant bit
        for i in stride(from: chars.count - 1, through: 1, by: -1) {
            let bit = (chars[i] == "1") ? 1 : 0
            let sum = bit + carry
            if sum % 2 == 1 {          // odd -> need add 1 then divide
                operations += 2
                carry = 1              // addition creates a carry to the left
            } else {                   // even -> just divide
                operations += 1
                // carry remains unchanged (0 or 1)
            }
        }
        return operations + carry
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSteps(s: String): Int {
        var ops = 0
        var carry = 0
        for (i in s.length - 1 downTo 1) {
            val bit = s[i] - '0'
            if ((bit + carry) % 2 == 1) {
                ops += 2
                carry = 1
            } else {
                ops += 1
                // carry remains unchanged
            }
        }
        return ops + carry
    }
}
```

## Dart

```dart
class Solution {
  int numSteps(String s) {
    int ops = 0;
    int carry = 0;
    for (int i = s.length - 1; i > 0; --i) {
      int bit = (s.codeUnitAt(i) - 48) + carry;
      if ((bit & 1) == 1) { // odd
        ops += 2;
        carry = 1;
      } else { // even
        ops += 1;
        // carry remains unchanged (0 or 1)
      }
    }
    return ops + carry;
  }
}
```

## Golang

```go
func numSteps(s string) int {
	ops, carry := 0, 0
	for i := len(s) - 1; i > 0; i-- {
		bit := int(s[i]-'0') + carry
		if bit%2 == 1 {
			ops += 2
			carry = 1
		} else {
			ops++
		}
	}
	return ops + carry
}
```

## Ruby

```ruby
def num_steps(s)
  n = s.length
  return 0 if n == 1

  ops = 0
  carry = 0
  (n - 1).downto(1) do |i|
    bit = s.getbyte(i) - 48
    sum = bit + carry
    if sum.odd?
      ops += 2
      carry = 1
    else
      ops += 1
      # carry remains unchanged (could be 0 or 1)
    end
  end

  ops + carry
end
```

## Scala

```scala
object Solution {
  def numSteps(s: String): Int = {
    var ops = 0
    var carry = 0
    var i = s.length - 1
    while (i > 0) {
      val bit = (s.charAt(i) - '0') + carry
      if ((bit & 1) == 1) {
        ops += 2
        carry = 1
      } else {
        ops += 1
        // carry remains unchanged
      }
      i -= 1
    }
    ops + carry
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_steps(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ops: i32 = 0;
        let mut carry: i32 = 0;
        for i in (1..n).rev() {
            let bit = (bytes[i] - b'0') as i32;
            let sum = bit + carry;
            if sum % 2 == 1 {
                ops += 2;
                carry = 1;
            } else {
                ops += 1;
                // carry remains unchanged
            }
        }
        ops + carry
    }
}
```

## Racket

```racket
(define/contract (num-steps s)
  (-> string? exact-integer?)
  (let ((ops 0)
        (carry 0))
    (for ([i (in-range (- (string-length s) 1) 0 -1)])
      (let* ((bit (if (char=? (string-ref s i) #\1) 1 0))
             (total (+ bit carry)))
        (if (= (modulo total 2) 1)
            (begin
              (set! ops (+ ops 2))
              (set! carry 1))
            (set! ops (+ ops 1)))))
    (+ ops carry)))
```

## Erlang

```erlang
-module(solution).
-export([num_steps/1]).

-spec num_steps(S :: unicode:unicode_binary()) -> integer().
num_steps(S) ->
    L = binary_to_list(S),
    Rest = tl(L),                     % drop most significant bit
    Rev = lists:reverse(Rest),
    loop(Rev, 0, 0).

loop([], Ops, Carry) ->
    Ops + Carry;
loop([Bit|Rest], Ops, Carry) ->
    Val = (Bit - $0) + Carry,
    case Val rem 2 of
        1 -> % odd
            loop(Rest, Ops + 2, 1);
        0 ->
            loop(Rest, Ops + 1, Carry)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_steps(s :: String.t()) :: integer
  def num_steps(s) do
    n = String.length(s)

    if n == 1 do
      0
    else
      {ops, carry} = process(s, n - 1, 0, 0)
      ops + carry
    end
  end

  defp process(_s, 0, ops, carry), do: {ops, carry}

  defp process(s, idx, ops, carry) do
    bit = if String.at(s, idx) == "1", do: 1, else: 0
    sum = bit + carry

    if rem(sum, 2) == 1 do
      process(s, idx - 1, ops + 2, 1)
    else
      process(s, idx - 1, ops + 1, carry)
    end
  end
end
```
