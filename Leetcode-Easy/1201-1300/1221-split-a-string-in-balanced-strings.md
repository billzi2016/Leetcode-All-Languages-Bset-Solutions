# 1221. Split a String in Balanced Strings

## Cpp

```cpp
class Solution {
public:
    int balancedStringSplit(string s) {
        int balance = 0, count = 0;
        for (char c : s) {
            if (c == 'L') ++balance;
            else --balance;
            if (balance == 0) ++count;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int balancedStringSplit(String s) {
        int balance = 0;
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == 'L') {
                balance++;
            } else { // c == 'R'
                balance--;
            }
            if (balance == 0) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        count = 0
        for ch in s:
            if ch == 'L':
                balance += 1
            else:  # ch == 'R'
                balance -= 1
            if balance == 0:
                count += 1
        return count
```

## Python3

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for ch in s:
            if ch == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count
```

## C

```c
int balancedStringSplit(char* s) {
    int count = 0;
    int balance = 0;
    for (char *p = s; *p != '\0'; ++p) {
        if (*p == 'L')
            ++balance;
        else
            --balance;
        if (balance == 0)
            ++count;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int BalancedStringSplit(string s) {
        int balance = 0;
        int count = 0;
        foreach (char c in s) {
            if (c == 'L') balance++;
            else balance--;
            if (balance == 0) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let count = 0;
    let balance = 0;
    for (let ch of s) {
        if (ch === 'L') balance++;
        else balance--;
        if (balance === 0) count++;
    }
    return count;
};
```

## Typescript

```typescript
function balancedStringSplit(s: string): number {
    let balance = 0;
    let count = 0;
    for (const ch of s) {
        balance += ch === 'L' ? 1 : -1;
        if (balance === 0) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function balancedStringSplit($s) {
        $balance = 0;
        $cnt = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === 'L') {
                $balance++;
            } else { // 'R'
                $balance--;
            }
            if ($balance === 0) {
                $cnt++;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func balancedStringSplit(_ s: String) -> Int {
        var balance = 0
        var count = 0
        for ch in s {
            if ch == "L" {
                balance += 1
            } else { // ch == "R"
                balance -= 1
            }
            if balance == 0 {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun balancedStringSplit(s: String): Int {
        var count = 0
        var balance = 0
        for (ch in s) {
            if (ch == 'L') balance++ else balance--
            if (balance == 0) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int balancedStringSplit(String s) {
    int balance = 0;
    int count = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == 'L') {
        balance++;
      } else {
        balance--;
      }
      if (balance == 0) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func balancedStringSplit(s string) int {
    count, balance := 0, 0
    for _, ch := range s {
        if ch == 'L' {
            balance++
        } else { // ch == 'R'
            balance--
        }
        if balance == 0 {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
# @param {String} s
# @return {Integer}
def balanced_string_split(s)
  balance = 0
  count = 0
  s.each_char do |ch|
    balance += (ch == 'L' ? 1 : -1)
    if balance == 0
      count += 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def balancedStringSplit(s: String): Int = {
        var count = 0
        var balance = 0
        for (ch <- s) {
            if (ch == 'L') balance += 1 else balance -= 1
            if (balance == 0) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let mut balance = 0;
        let mut count = 0;
        for ch in s.chars() {
            if ch == 'L' {
                balance += 1;
            } else {
                balance -= 1;
            }
            if balance == 0 {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (balanced-string-split s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         (iter
          (lambda (i bal cnt)
            (if (= i len)
                cnt
                (let* ((c (string-ref s i))
                       (new-bal (if (char=? c #\L) (+ bal 1) (- bal 1))))
                  (if (= new-bal 0)
                      (iter (+ i 1) 0 (+ cnt 1))
                      (iter (+ i 1) new-bal cnt)))))))
    (iter 0 0 0)))
```

## Erlang

```erlang
-module(solution).
-export([balanced_string_split/1]).

-spec balanced_string_split(S :: unicode:unicode_binary()) -> integer().
balanced_string_split(S) ->
    split(S, 0, 0).

split(<<>>, _Balance, Count) ->
    Count;
split(<<Char, Rest/binary>>, Balance, Count) ->
    NewBal = case Char of
        $L -> Balance + 1;
        $R -> Balance - 1
    end,
    if NewBal == 0 ->
            split(Rest, 0, Count + 1);
       true ->
            split(Rest, NewBal, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec balanced_string_split(s :: String.t()) :: integer()
  def balanced_string_split(s) do
    {_, count} =
      s
      |> String.to_charlist()
      |> Enum.reduce({0, 0}, fn ch, {balance, cnt} ->
        balance = if ch == ?L, do: balance + 1, else: balance - 1

        if balance == 0 do
          {balance, cnt + 1}
        else
          {balance, cnt}
        end
      end)

    count
  end
end
```
