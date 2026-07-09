# 2729. Check if The Number is Fascinating

## Cpp

```cpp
class Solution {
public:
    bool isFascinating(int n) {
        long long a = n;
        long long b = 2LL * n;
        long long c = 3LL * n;
        std::string s = std::to_string(a) + std::to_string(b) + std::to_string(c);
        if (s.size() != 9) return false;
        int cnt[10] = {0};
        for (char ch : s) {
            if (ch == '0') return false;
            ++cnt[ch - '0'];
        }
        for (int d = 1; d <= 9; ++d) {
            if (cnt[d] != 1) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isFascinating(int n) {
        String combined = "" + n + (n * 2) + (n * 3);
        if (combined.length() != 9) return false;
        boolean[] seen = new boolean[10];
        for (char ch : combined.toCharArray()) {
            int d = ch - '0';
            if (d == 0 || seen[d]) return false;
            seen[d] = true;
        }
        // all digits 1-9 must be present
        for (int i = 1; i <= 9; i++) {
            if (!seen[i]) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n) + str(2 * n) + str(3 * n)
        if len(s) != 9:
            return False
        # must contain digits 1-9 exactly once and no zeros
        return set(s) == set('123456789') and s.count('0') == 0
```

## Python3

```python
class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        return len(s) == 9 and set(s) == set("123456789")
```

## C

```c
#include <stdbool.h>
#include <stdio.h>

bool isFascinating(int n) {
    char s[30];
    int len = sprintf(s, "%d%d%d", n, n * 2, n * 3);
    int cnt[10] = {0};
    for (int i = 0; i < len; ++i) {
        if (s[i] == '0') return false;
        cnt[s[i] - '0']++;
    }
    for (int d = 1; d <= 9; ++d) {
        if (cnt[d] != 1) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsFascinating(int n)
    {
        string combined = $"{n}{2 * n}{3 * n}";
        if (combined.Length != 9) return false;

        bool[] seen = new bool[10];
        foreach (char ch in combined)
        {
            if (ch == '0') return false;
            int digit = ch - '0';
            if (seen[digit]) return false;
            seen[digit] = true;
        }

        for (int i = 1; i <= 9; i++)
        {
            if (!seen[i]) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isFascinating = function(n) {
    const combined = '' + n + (2 * n) + (3 * n);
    if (combined.length !== 9) return false;
    
    const seen = new Array(10).fill(false);
    for (let i = 0; i < combined.length; i++) {
        const digit = combined.charCodeAt(i) - 48; // '0' -> 48
        if (digit === 0 || seen[digit]) return false;
        seen[digit] = true;
    }
    return true;
};
```

## Typescript

```typescript
function isFascinating(n: number): boolean {
    const s = '' + n + (2 * n) + (3 * n);
    if (s.length !== 9) return false;
    const seen = new Array(10).fill(false);
    for (const ch of s) {
        const d = ch.charCodeAt(0) - 48; // '0' => 48
        if (d === 0 || seen[d]) return false;
        seen[d] = true;
    }
    for (let i = 1; i <= 9; i++) {
        if (!seen[i]) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isFascinating($n) {
        $s = (string)$n . (string)(2 * $n) . (string)(3 * $n);
        if (strlen($s) !== 9) {
            return false;
        }
        $digits = str_split($s);
        sort($digits);
        return implode('', $digits) === '123456789';
    }
}
```

## Swift

```swift
class Solution {
    func isFascinating(_ n: Int) -> Bool {
        let combined = "\(n)\(2 * n)\(3 * n)"
        if combined.count != 9 { return false }
        var seen = [Bool](repeating: false, count: 10)
        for ch in combined {
            guard let digit = ch.wholeNumberValue else { return false }
            if digit == 0 || seen[digit] { return false }
            seen[digit] = true
        }
        for d in 1...9 {
            if !seen[d] { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isFascinating(n: Int): Boolean {
        val s = "$n${2 * n}${3 * n}"
        if (s.length != 9) return false
        val seen = BooleanArray(10)
        for (ch in s) {
            if (ch == '0') return false
            val d = ch - '0'
            if (seen[d]) return false
            seen[d] = true
        }
        for (i in 1..9) {
            if (!seen[i]) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isFascinating(int n) {
    final concatenated = '$n${n * 2}${n * 3}';
    if (concatenated.length != 9) return false;
    final seen = <String>{};
    for (int i = 0; i < concatenated.length; i++) {
      final ch = concatenated[i];
      if (ch == '0' || seen.contains(ch)) return false;
      seen.add(ch);
    }
    return seen.length == 9;
  }
}
```

## Golang

```go
package main

import "strconv"

func isFascinating(n int) bool {
	s := strconv.Itoa(n) + strconv.Itoa(2*n) + strconv.Itoa(3*n)
	if len(s) != 9 {
		return false
	}
	var cnt [10]int
	for i := 0; i < len(s); i++ {
		d := s[i] - '0'
		if d == 0 {
			return false
		}
		cnt[d]++
	}
	for d := 1; d <= 9; d++ {
		if cnt[d] != 1 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def is_fascinating(n)
  s = "#{n}#{2 * n}#{3 * n}"
  return false unless s.length == 9
  s.chars.sort.join == "123456789"
end
```

## Scala

```scala
object Solution {
    def isFascinating(n: Int): Boolean = {
        val concat = s"${n}${2 * n}${3 * n}"
        if (concat.length != 9) return false
        val seen = new Array[Boolean](10)
        for (ch <- concat) {
            val d = ch - '0'
            if (d == 0 || seen(d)) return false
            seen(d) = true
        }
        // all digits 1..9 must be present; length check guarantees this if no duplicates and no zero
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_fascinating(n: i32) -> bool {
        let s = format!("{}{}{}", n, n * 2, n * 3);
        if s.len() != 9 {
            return false;
        }
        let mut cnt = [0u8; 10];
        for ch in s.chars() {
            if ch == '0' {
                return false;
            }
            let d = (ch as u8 - b'0') as usize;
            cnt[d] += 1;
            if cnt[d] > 1 {
                return false;
            }
        }
        for i in 1..=9 {
            if cnt[i] != 1 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-fascinating n)
  (-> exact-integer? boolean?)
  (let* ([s (string-append (number->string n)
                           (number->string (* 2 n))
                           (number->string (* 3 n)))])
    (if (= (string-length s) 9)
        (let loop ((i 0) (seen (make-vector 10 #f)) (ok #t))
          (cond
            [(not ok) #f]
            [(= i (string-length s)) #t]
            [else
             (define ch (string-ref s i))
             (if (char=? ch #\0)
                 #f
                 (let* ([digit (- (char->integer ch) (char->integer #\0))]
                        [already (vector-ref seen digit)])
                   (if already
                       #f
                       (begin
                         (vector-set! seen digit #t)
                         (loop (+ i 1) seen #t)))))]))
        #f)))
```

## Erlang

```erlang
-module(solution).
-export([is_fascinating/1]).

-spec is_fascinating(N :: integer()) -> boolean().
is_fascinating(N) ->
    Concat = integer_to_list(N) ++ integer_to_list(2 * N) ++ integer_to_list(3 * N),
    case length(Concat) of
        9 -> lists:sort(Concat) == "123456789";
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec is_fascinating(n :: integer) :: boolean
  def is_fascinating(n) do
    s = Integer.to_string(n) <> Integer.to_string(2 * n) <> Integer.to_string(3 * n)

    if String.length(s) != 9 do
      false
    else
      result =
        Enum.reduce_while(String.graphemes(s), 0, fn ch, acc ->
          if ch == "0" do
            {:halt, :error}
          else
            d = String.to_integer(ch)
            bit = 1 <<< d

            if (acc &&& bit) != 0 do
              {:halt, :error}
            else
              {:cont, acc ||| bit}
            end
          end
        end)

      case result do
        :error -> false
        mask -> mask == 1022
      end
    end
  end
end
```
