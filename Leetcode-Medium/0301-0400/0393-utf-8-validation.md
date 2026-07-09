# 0393. UTF-8 Validation

## Cpp

```cpp
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int remaining = 0;
        for (int byte : data) {
            byte &= 0xFF; // ensure only lowest 8 bits
            if (remaining == 0) {
                int mask = 0x80; // 1000 0000
                int count = 0;
                while (mask & byte) {
                    ++count;
                    mask >>= 1;
                }
                if (count == 0) continue;               // 1‑byte character
                if (count == 1 || count > 4) return false; // invalid leading pattern
                remaining = count - 1;                   // need this many continuation bytes
            } else {
                // must be of form 10xxxxxx
                if ((byte & 0xC0) != 0x80) return false;
                --remaining;
            }
        }
        return remaining == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean validUtf8(int[] data) {
        int remaining = 0;
        for (int num : data) {
            int val = num & 0xFF; // ensure only lowest 8 bits
            if (remaining == 0) {
                int mask = 1 << 7;
                while ((mask & val) != 0) {
                    remaining++;
                    mask >>= 1;
                }
                if (remaining == 0) continue;          // 1‑byte character
                if (remaining == 1 || remaining > 4) return false; // invalid leading byte
                remaining--; // subtract the current leading byte
            } else {
                // must be of form 10xxxxxx
                if ((val & 0b11000000) != 0b10000000) return false;
                remaining--;
            }
        }
        return remaining == 0;
    }
}
```

## Python

```python
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = len(data)
        i = 0
        while i < n:
            first = data[i] & 0xFF
            mask = 0x80
            num_ones = 0
            while mask & first:
                num_ones += 1
                mask >>= 1
            if num_ones == 0:
                i += 1
                continue
            if num_ones == 1 or num_ones > 4:
                return False
            if i + num_ones > n:
                return False
            for j in range(i + 1, i + num_ones):
                if (data[j] & 0xC0) != 0x80:
                    return False
            i += num_ones
        return True
```

## Python3

```python
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0
        for num in data:
            # consider only least significant 8 bits
            byte = num & 0xFF
            if remaining == 0:
                mask = 0x80  # 10000000
                count = 0
                while mask & byte:
                    count += 1
                    mask >>= 1
                if count == 0:
                    continue  # 1-byte character
                if count == 1 or count > 4:
                    return False
                remaining = count - 1
            else:
                if (byte & 0xC0) != 0x80:  # must be 10xxxxxx
                    return False
                remaining -= 1
        return remaining == 0
```

## C

```c
#include <stdbool.h>

bool validUtf8(int* data, int dataSize) {
    int remaining = 0;
    for (int i = 0; i < dataSize; ++i) {
        unsigned char byte = (unsigned char)(data[i] & 0xFF);
        if (remaining == 0) {
            // count leading ones
            unsigned char mask = 0x80; // 1000 0000
            int count = 0;
            while (mask & byte) {
                ++count;
                mask >>= 1;
            }
            if (count == 0) {
                continue; // 1-byte character
            }
            if (count == 1 || count > 4) {
                return false; // invalid leading byte
            }
            remaining = count - 1;
        } else {
            // must be a continuation byte: starts with '10'
            if ((byte & 0xC0) != 0x80) {
                return false;
            }
            --remaining;
        }
    }
    return remaining == 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool ValidUtf8(int[] data) {
        int n = data.Length;
        for (int i = 0; i < n; i++) {
            int b = data[i] & 0xFF;
            int numBytes = 0;
            int mask = 0x80; // 1000 0000
            while ((b & mask) != 0) {
                numBytes++;
                mask >>= 1;
            }
            if (numBytes == 0) continue;               // 1‑byte character
            if (numBytes == 1 || numBytes > 4) return false; // invalid leading byte
            if (i + numBytes > n) return false;        // not enough bytes left
            for (int j = 1; j < numBytes; j++) {
                int nb = data[i + j] & 0xFF;
                if ((nb & 0xC0) != 0x80) return false; // must start with '10'
            }
            i += numBytes - 1; // skip continuation bytes
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} data
 * @return {boolean}
 */
var validUtf8 = function(data) {
    let remaining = 0; // number of continuation bytes expected
    
    for (let i = 0; i < data.length; i++) {
        const byte = data[i] & 0xFF; // ensure only lowest 8 bits
        
        if (remaining === 0) {
            // count leading 1s
            let mask = 0x80; // 10000000
            while ((byte & mask) !== 0) {
                remaining++;
                mask >>= 1;
            }
            
            // 0 leading ones -> 1-byte character
            if (remaining === 0) continue;
            
            // invalid cases: leading pattern "10" or more than 4 bytes
            if (remaining === 1 || remaining > 4) return false;
            
            // we have counted the first byte, need remaining-1 continuation bytes
            remaining--; 
        } else {
            // must be a continuation byte of form 10xxxxxx
            if ((byte & 0xC0) !== 0x80) return false;
            remaining--;
        }
    }
    
    return remaining === 0;
};
```

## Typescript

```typescript
function validUtf8(data: number[]): boolean {
    const n = data.length;
    let i = 0;
    while (i < n) {
        const first = data[i];
        // Count leading 1 bits
        let mask = 0x80; // 1000 0000
        let ones = 0;
        while ((first & mask) !== 0 && mask > 0) {
            ones++;
            mask >>= 1;
        }
        if (ones === 0) {
            i += 1;
            continue; // single-byte character
        }
        // Invalid patterns: leading '10' or more than 4 bytes
        if (ones === 1 || ones > 4) return false;
        // Not enough continuation bytes
        if (i + ones > n) return false;
        // Check continuation bytes start with '10'
        for (let j = 1; j < ones; ++j) {
            const byte = data[i + j];
            if ((byte & 0xC0) !== 0x80) return false;
        }
        i += ones;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $data
     * @return Boolean
     */
    function validUtf8($data) {
        $remaining = 0;
        foreach ($data as $byte) {
            $byte &= 0xFF; // ensure only lowest 8 bits are used
            if ($remaining === 0) {
                $mask = 0x80; // 10000000
                $numOnes = 0;
                while (($mask & $byte) !== 0) {
                    $numOnes++;
                    $mask >>= 1;
                }
                if ($numOnes === 0) {
                    continue; // 1-byte character
                }
                if ($numOnes === 1 || $numOnes > 4) {
                    return false; // invalid leading byte
                }
                $remaining = $numOnes - 1;
            } else {
                // continuation bytes must start with '10'
                if (($byte & 0xC0) !== 0x80) {
                    return false;
                }
                $remaining--;
            }
        }
        return $remaining === 0;
    }
}
```

## Swift

```swift
class Solution {
    func validUtf8(_ data: [Int]) -> Bool {
        var remaining = 0
        for byte in data {
            let b = byte & 0xFF
            if remaining == 0 {
                var mask = 1 << 7
                var count = 0
                while (b & mask) != 0 {
                    count += 1
                    mask >>= 1
                }
                if count == 0 { continue }               // 1‑byte character
                if count == 1 || count > 4 { return false } // invalid leading byte
                remaining = count - 1                     // expect continuation bytes
            } else {
                // Continuation byte must start with '10'
                if (b & (1 << 7)) == 0 { return false }
                if (b & (1 << 6)) != 0 { return false }
                remaining -= 1
            }
        }
        return remaining == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validUtf8(data: IntArray): Boolean {
        var remaining = 0
        for (num in data) {
            val b = num and 0xFF
            if (remaining == 0) {
                var mask = 0x80
                var count = 0
                while ((mask and b) != 0) {
                    count++
                    mask = mask shr 1
                }
                if (count == 0) continue
                if (count == 1 || count > 4) return false
                remaining = count - 1
            } else {
                if ((b and 0xC0) != 0x80) return false
                remaining--
            }
        }
        return remaining == 0
    }
}
```

## Dart

```dart
class Solution {
  bool validUtf8(List<int> data) {
    int remaining = 0;
    for (int num in data) {
      int b = num & 0xFF;
      if (remaining == 0) {
        int mask = 0x80;
        int count = 0;
        while ((b & mask) != 0) {
          count++;
          mask >>= 1;
        }
        if (count == 0) continue; // 1-byte character
        if (count == 1 || count > 4) return false; // invalid start byte
        remaining = count - 1;
      } else {
        if ((b & 0xC0) != 0x80) return false; // not a continuation byte
        remaining--;
      }
    }
    return remaining == 0;
  }
}
```

## Golang

```go
func validUtf8(data []int) bool {
	n := len(data)
	for i := 0; i < n; {
		first := data[i] & 0xFF

		// count leading 1 bits
		cnt := 0
		mask := 0x80
		for mask&first != 0 {
			cnt++
			mask >>= 1
		}

		if cnt == 0 { // 1-byte character
			i++
			continue
		}
		// invalid patterns: leading 1 count is 1 or >4
		if cnt == 1 || cnt > 4 {
			return false
		}
		// need cnt-1 continuation bytes
		if i+cnt > n {
			return false
		}
		for j := i + 1; j < i+cnt; j++ {
			b := data[j] & 0xFF
			if (b&0xC0) != 0x80 { // must start with '10'
				return false
			}
		}
		i += cnt
	}
	return true
}
```

## Ruby

```ruby
def valid_utf8(data)
  n = data.length
  i = 0
  while i < n
    byte = data[i] & 0xFF
    mask = 0b10000000
    count = 0
    while (mask & byte) != 0 && count < 5
      count += 1
      mask >>= 1
    end

    if count == 0
      i += 1
      next
    end

    return false if count == 1 || count > 4
    return false if i + count > n

    j = 1
    while j < count
      cont = data[i + j] & 0xFF
      return false unless (cont & 0b11000000) == 0b10000000
      j += 1
    end

    i += count
  end
  true
end
```

## Scala

```scala
object Solution {
  def validUtf8(data: Array[Int]): Boolean = {
    var remaining = 0
    for (num <- data) {
      val b = num & 0xFF
      if (remaining == 0) {
        var mask = 0x80
        var count = 0
        while ((b & mask) != 0 && mask > 0) {
          count += 1
          mask >>= 1
        }
        if (count == 0) {
          // single-byte character
        } else if (count == 1 || count > 4) {
          return false
        } else {
          remaining = count - 1
        }
      } else {
        if ((b & 0xC0) != 0x80) return false
        remaining -= 1
      }
    }
    remaining == 0
  }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_utf8(data: Vec<i32>) -> bool {
        let n = data.len();
        let mut i = 0usize;
        while i < n {
            let first = data[i] as u8;
            // count leading ones
            let mut num_bytes = 0usize;
            let mut mask = 0b1000_0000u8;
            while mask & first != 0 {
                num_bytes += 1;
                mask >>= 1;
            }
            if num_bytes == 0 {
                i += 1;
                continue; // 1‑byte character
            }
            // UTF-8 allows only 2,3,4 byte sequences
            if num_bytes == 1 || num_bytes > 4 {
                return false;
            }
            // need (num_bytes - 1) continuation bytes
            if i + num_bytes > n {
                return false;
            }
            for j in 1..num_bytes {
                let b = data[i + j] as u8;
                if (b & 0b1100_0000) != 0b1000_0000 {
                    return false;
                }
            }
            i += num_bytes;
        }
        true
    }
}
```

## Racket

```racket
(define/contract (valid-utf8 data)
  (-> (listof exact-integer?) boolean?)
  (letrec
      ((count-leading-ones
        (lambda (byte)
          (let loop ((mask #x80) (cnt 0))
            (if (= mask 0)
                cnt
                (if (zero? (bitwise-and byte mask))
                    cnt
                    (loop (arithmetic-shift mask -1) (+ cnt 1)))))))
       (check-continuation
        (lambda (lst needed)
          (if (= needed 0)
              lst
              (if (null? lst)
                  #f
                  (let ((b (car lst)))
                    (if (= (bitwise-and b #xC0) #x80)
                        (check-continuation (cdr lst) (- needed 1))
                        #f))))))
       (process
        (lambda (lst)
          (cond
            [(null? lst) #t]
            [else
             (define first (car lst))
             (define leading (count-leading-ones first))
             (cond
               [(= leading 0) ; single-byte character
                (process (cdr lst))]
               [(or (= leading 1) (> leading 4)) #f] ; invalid start byte
               [else
                (define rest (check-continuation (cdr lst) (- leading 1)))
                (if rest
                    (process rest)
                    #f)]))])))
    (process data)))
```

## Erlang

```erlang
-module(solution).
-export([valid_utf8/1]).

-spec valid_utf8(Data :: [integer()]) -> boolean().
valid_utf8(Data) ->
    validate(Data, 0).

validate([], 0) -> true;
validate([], _) -> false;
validate([Byte|Rest], 0) ->
    NumOnes = count_leading_ones(Byte),
    case NumOnes of
        0 -> validate(Rest, 0);
        1 -> false;                     % a continuation byte cannot start a character
        N when N >= 2, N =< 4 ->
            Remaining = N - 1,
            validate(Rest, Remaining);
        _ -> false                      % more than 4 leading ones is invalid
    end;
validate([Byte|Rest], Expected) ->
    case (Byte band 16#C0) of
        16#80 -> validate(Rest, Expected - 1);   % matches pattern 10xxxxxx
        _     -> false
    end.

count_leading_ones(Byte) ->
    count_leading_ones(Byte, 128, 0).

count_leading_ones(_, 0, Count) -> Count;
count_leading_ones(Byte, Mask, Count) ->
    case Byte band Mask of
        0 -> Count;
        _ -> count_leading_ones(Byte, Mask bsr 1, Count + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec valid_utf8(data :: [integer]) :: boolean
  def valid_utf8(data) do
    result =
      Enum.reduce_while(data, 0, fn byte, remaining ->
        if remaining > 0 do
          if (byte &&& 0b11000000) == 0b10000000 do
            {:cont, remaining - 1}
          else
            {:halt, false}
          end
        else
          leading = count_leading_ones(byte)

          cond do
            leading == 0 ->
              {:cont, 0}

            leading >= 2 and leading <= 4 ->
              {:cont, leading - 1}

            true ->
              {:halt, false}
          end
        end
      end)

    case result do
      false -> false
      remaining when is_integer(remaining) -> remaining == 0
    end
  end

  defp count_leading_ones(byte), do: count_leading_ones(byte, 0b10000000, 0)

  defp count_leading_ones(_byte, 0, acc), do: acc

  defp count_leading_ones(byte, mask, acc) do
    if (byte &&& mask) != 0 do
      count_leading_ones(byte, mask >>> 1, acc + 1)
    else
      acc
    end
  end
end
```
