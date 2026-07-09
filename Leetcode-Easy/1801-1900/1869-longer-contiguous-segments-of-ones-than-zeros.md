# 1869. Longer Contiguous Segments of Ones than Zeros

## Cpp

```cpp
class Solution {
public:
    bool checkZeroOnes(string s) {
        int maxOne = 0, maxZero = 0;
        int cur = 0;
        char prev = s[0];
        for (char c : s) {
            if (c == prev) {
                ++cur;
            } else {
                if (prev == '1') maxOne = max(maxOne, cur);
                else maxZero = max(maxZero, cur);
                prev = c;
                cur = 1;
            }
        }
        // update for the last segment
        if (prev == '1') maxOne = max(maxOne, cur);
        else maxZero = max(maxZero, cur);
        
        return maxOne > maxZero;
    }
};
```

## Java

```java
class Solution {
    public boolean checkZeroOnes(String s) {
        int maxOnes = 0, maxZeros = 0;
        int curCount = 0;
        char prev = ' ';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == prev) {
                curCount++;
            } else {
                // reset count for new character
                curCount = 1;
                prev = c;
            }
            if (c == '1') {
                if (curCount > maxOnes) maxOnes = curCount;
            } else { // c == '0'
                if (curCount > maxZeros) maxZeros = curCount;
            }
        }
        return maxOnes > maxZeros;
    }
}
```

## Python

```python
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_one = max_zero = 0
        cur_char = s[0]
        cur_len = 1

        for ch in s[1:]:
            if ch == cur_char:
                cur_len += 1
            else:
                if cur_char == '1':
                    max_one = max(max_one, cur_len)
                else:
                    max_zero = max(max_zero, cur_len)
                cur_char = ch
                cur_len = 1

        # update for the last segment
        if cur_char == '1':
            max_one = max(max_one, cur_len)
        else:
            max_zero = max(max_zero, cur_len)

        return max_one > max_zero
```

## Python3

```python
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_one = max_zero = 0
        cur_char = s[0]
        cur_len = 1

        for ch in s[1:]:
            if ch == cur_char:
                cur_len += 1
            else:
                if cur_char == '1':
                    max_one = max(max_one, cur_len)
                else:
                    max_zero = max(max_zero, cur_len)
                cur_char = ch
                cur_len = 1

        # handle last segment
        if cur_char == '1':
            max_one = max(max_one, cur_len)
        else:
            max_zero = max(max_zero, cur_len)

        return max_one > max_zero
```

## C

```c
#include <stdbool.h>

bool checkZeroOnes(char* s) {
    int maxOne = 0, maxZero = 0;
    char prev = s[0];
    int cur = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == prev) {
            ++cur;
        } else {
            if (prev == '1') {
                if (cur > maxOne) maxOne = cur;
            } else {
                if (cur > maxZero) maxZero = cur;
            }
            prev = s[i];
            cur = 1;
        }
    }
    if (prev == '1') {
        if (cur > maxOne) maxOne = cur;
    } else {
        if (cur > maxZero) maxZero = cur;
    }
    return maxOne > maxZero;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckZeroOnes(string s)
    {
        int maxZero = 0, maxOne = 0;
        int currentCount = 0;
        char prevChar = '\0';

        foreach (char c in s)
        {
            if (c == prevChar)
            {
                currentCount++;
            }
            else
            {
                // reset count for new character
                currentCount = 1;
                prevChar = c;
            }

            if (c == '0')
                maxZero = Math.Max(maxZero, currentCount);
            else // c == '1'
                maxOne = Math.Max(maxOne, currentCount);
        }

        return maxOne > maxZero;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkZeroOnes = function(s) {
    let max0 = 0, max1 = 0;
    let curChar = s[0];
    let curLen = 0;
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === curChar) {
            curLen++;
        } else {
            if (curChar === '0') max0 = Math.max(max0, curLen);
            else max1 = Math.max(max1, curLen);
            curChar = s[i];
            curLen = 1;
        }
    }
    // finalize last segment
    if (curChar === '0') max0 = Math.max(max0, curLen);
    else max1 = Math.max(max1, curLen);
    
    return max1 > max0;
};
```

## Typescript

```typescript
function checkZeroOnes(s: string): boolean {
    let maxOnes = 0;
    let maxZeros = 0;
    let i = 0;
    const n = s.length;
    while (i < n) {
        const ch = s[i];
        let count = 0;
        while (i < n && s[i] === ch) {
            ++count;
            ++i;
        }
        if (ch === '1') {
            if (count > maxOnes) maxOnes = count;
        } else { // ch === '0'
            if (count > maxZeros) maxZeros = count;
        }
    }
    return maxOnes > maxZeros;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkZeroOnes($s) {
        $maxOne = 0;
        $maxZero = 0;
        $currentChar = '';
        $count = 0;

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === $currentChar) {
                $count++;
            } else {
                // update previous segment max
                if ($currentChar === '1') {
                    $maxOne = max($maxOne, $count);
                } elseif ($currentChar === '0') {
                    $maxZero = max($maxZero, $count);
                }
                $currentChar = $s[$i];
                $count = 1;
            }
        }

        // update for the last segment
        if ($currentChar === '1') {
            $maxOne = max($maxOne, $count);
        } elseif ($currentChar === '0') {
            $maxZero = max($maxZero, $count);
        }

        return $maxOne > $maxZero;
    }
}
```

## Swift

```swift
class Solution {
    func checkZeroOnes(_ s: String) -> Bool {
        var maxOnes = 0
        var maxZeros = 0
        var prevChar: Character? = nil
        var curCount = 0
        
        for ch in s {
            if let p = prevChar, p == ch {
                curCount += 1
            } else {
                if let p = prevChar {
                    if p == "1" {
                        maxOnes = max(maxOnes, curCount)
                    } else {
                        maxZeros = max(maxZeros, curCount)
                    }
                }
                prevChar = ch
                curCount = 1
            }
        }
        
        if let p = prevChar {
            if p == "1" {
                maxOnes = max(maxOnes, curCount)
            } else {
                maxZeros = max(maxZeros, curCount)
            }
        }
        
        return maxOnes > maxZeros
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkZeroOnes(s: String): Boolean {
        var maxOnes = 0
        var maxZeros = 0
        var i = 0
        val n = s.length
        while (i < n) {
            val ch = s[i]
            var j = i
            while (j < n && s[j] == ch) {
                j++
            }
            val len = j - i
            if (ch == '1') {
                if (len > maxOnes) maxOnes = len
            } else {
                if (len > maxZeros) maxZeros = len
            }
            i = j
        }
        return maxOnes > maxZeros
    }
}
```

## Dart

```dart
class Solution {
  bool checkZeroOnes(String s) {
    int maxOne = 0, maxZero = 0;
    int count = 1;
    for (int i = 1; i < s.length; ++i) {
      if (s[i] == s[i - 1]) {
        count++;
      } else {
        if (s[i - 1] == '1') {
          if (count > maxOne) maxOne = count;
        } else {
          if (count > maxZero) maxZero = count;
        }
        count = 1;
      }
    }
    // handle last segment
    if (s[s.length - 1] == '1') {
      if (count > maxOne) maxOne = count;
    } else {
      if (count > maxZero) maxZero = count;
    }
    return maxOne > maxZero;
  }
}
```

## Golang

```go
func checkZeroOnes(s string) bool {
	maxOne, maxZero := 0, 0
	var curChar byte
	curCount := 0

	for i := 0; i < len(s); i++ {
		if i == 0 || s[i] != curChar {
			if i != 0 {
				if curChar == '1' {
					if curCount > maxOne {
						maxOne = curCount
					}
				} else {
					if curCount > maxZero {
						maxZero = curCount
					}
				}
			}
			curChar = s[i]
			curCount = 1
		} else {
			curCount++
		}
	}

	if curChar == '1' {
		if curCount > maxOne {
			maxOne = curCount
		}
	} else {
		if curCount > maxZero {
			maxZero = curCount
		}
	}

	return maxOne > maxZero
}
```

## Ruby

```ruby
def check_zero_ones(s)
  max_one = 0
  max_zero = 0
  cur_char = nil
  cur_len = 0

  s.each_char do |ch|
    if ch == cur_char
      cur_len += 1
    else
      if cur_char == '1'
        max_one = [max_one, cur_len].max
      elsif cur_char == '0'
        max_zero = [max_zero, cur_len].max
      end
      cur_char = ch
      cur_len = 1
    end
  end

  if cur_char == '1'
    max_one = [max_one, cur_len].max
  elsif cur_char == '0'
    max_zero = [max_zero, cur_len].max
  end

  max_one > max_zero
end
```

## Scala

```scala
object Solution {
    def checkZeroOnes(s: String): Boolean = {
        var maxOne = 0
        var maxZero = 0
        var i = 0
        val n = s.length
        while (i < n) {
            val ch = s.charAt(i)
            var j = i
            while (j < n && s.charAt(j) == ch) {
                j += 1
            }
            val len = j - i
            if (ch == '1') {
                if (len > maxOne) maxOne = len
            } else {
                if (len > maxZero) maxZero = len
            }
            i = j
        }
        maxOne > maxZero
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_zero_ones(s: String) -> bool {
        let bytes = s.as_bytes();
        let mut max_one = 0usize;
        let mut max_zero = 0usize;

        let mut cur_char = bytes[0];
        let mut cur_len = 0usize;

        for &b in bytes.iter() {
            if b == cur_char {
                cur_len += 1;
            } else {
                if cur_char == b'1' {
                    if cur_len > max_one { max_one = cur_len; }
                } else {
                    if cur_len > max_zero { max_zero = cur_len; }
                }
                cur_char = b;
                cur_len = 1;
            }
        }

        // update for the last segment
        if cur_char == b'1' {
            if cur_len > max_one { max_one = cur_len; }
        } else {
            if cur_len > max_zero { max_zero = cur_len; }
        }

        max_one > max_zero
    }
}
```

## Racket

```racket
(define/contract (check-zero-ones s)
  (-> string? boolean?)
  (let* ((len (string-length s))
         (first (if (> len 0) (string-ref s 0) #\space)))
    (if (= len 0)
        #false
        (let loop ((i 1) (cur-char first) (cur-len 1) (max1 0) (max0 0))
          (if (= i len)
              (let ((final-max1 (if (char=? cur-char #\1) (max max1 cur-len) max1))
                    (final-max0 (if (char=? cur-char #\0) (max max0 cur-len) max0)))
                (> final-max1 final-max0))
              (let ((c (string-ref s i)))
                (if (char=? c cur-char)
                    (loop (+ i 1) cur-char (+ cur-len 1) max1 max0)
                    (if (char=? cur-char #\1)
                        (loop (+ i 1) c 1 (max max1 cur-len) max0)
                        (loop (+ i 1) c 1 max1 (max max0 cur-len)))))))))
```

## Erlang

```erlang
-spec check_zero_ones(S :: unicode:unicode_binary()) -> boolean().
check_zero_ones(S) ->
    List = binary_to_list(S),
    {MaxZero, MaxOne} = scan(List, undefined, 0, 0, 0),
    MaxOne > MaxZero.

scan([], Prev, CurrCount, MaxZero, MaxOne) ->
    case Prev of
        $0 -> {erlang:max(MaxZero, CurrCount), MaxOne};
        $1 -> {MaxZero, erlang:max(MaxOne, CurrCount)};
        _  -> {MaxZero, MaxOne}
    end;
scan([Char | Rest], Prev, CurrCount, MaxZero, MaxOne) ->
    if Char =:= Prev ->
            scan(Rest, Prev, CurrCount + 1, MaxZero, MaxOne);
       true ->
            case Prev of
                $0 -> NewMaxZero = erlang:max(MaxZero, CurrCount), NewMaxOne = MaxOne;
                $1 -> NewMaxOne = erlang:max(MaxOne, CurrCount), NewMaxZero = MaxZero;
                _  -> NewMaxZero = MaxZero, NewMaxOne = MaxOne
            end,
            scan(Rest, Char, 1, NewMaxZero, NewMaxOne)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_zero_ones(s :: String.t()) :: boolean()
  def check_zero_ones(s) do
    max_one =
      s
      |> String.split("0", trim: true)
      |> Enum.map(&String.length/1)
      |> Enum.max(fn -> 0 end)

    max_zero =
      s
      |> String.split("1", trim: true)
      |> Enum.map(&String.length/1)
      |> Enum.max(fn -> 0 end)

    max_one > max_zero
  end
end
```
