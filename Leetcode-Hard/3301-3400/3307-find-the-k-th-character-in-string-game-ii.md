# 3307. Find the K-th Character in String Game II

## Cpp

```cpp
class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        long long x = k - 1;
        long long shift = 0;
        int idx = 0;
        while (x > 0) {
            if (x & 1LL) {
                if (idx < (int)operations.size())
                    shift += operations[idx];
            }
            x >>= 1;
            ++idx;
        }
        shift %= 26;
        return char('a' + shift);
    }
};
```

## Java

```java
class Solution {
    public char kthCharacter(long k, int[] operations) {
        long mask = k - 1;
        int shiftCount = 0;
        for (int i = 0; mask != 0 && i < operations.length; i++) {
            if ((mask & 1L) == 1L && operations[i] == 1) {
                shiftCount++;
            }
            mask >>= 1;
        }
        shiftCount %= 26;
        return (char) ('a' + shiftCount);
    }
}
```

## Python

```python
class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        shift = 0
        mask = k - 1
        i = 0
        while mask:
            if mask & 1:
                shift += operations[i]
            mask >>= 1
            i += 1
        return chr(ord('a') + (shift % 26))
```

## Python3

```python
from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shift = 0
        x = k - 1
        i = 0
        while x:
            if x & 1:
                shift += operations[i]
            x >>= 1
            i += 1
        return chr(ord('a') + (shift % 26))
```

## C

```c
char kthCharacter(long long k, int* operations, int operationsSize) {
    long long kk = k - 1;
    int inc = 0;
    for (int i = 0; kk > 0 && i < operationsSize; ++i) {
        if (kk & 1LL) {
            inc += operations[i];
        }
        kk >>= 1LL;
    }
    inc %= 26;
    return 'a' + inc;
}
```

## Csharp

```csharp
public class Solution {
    public char KthCharacter(long k, int[] operations) {
        long kk = k - 1;
        int idx = 0;
        int shiftCount = 0;
        while (kk > 0 && idx < operations.Length) {
            if ((kk & 1L) != 0 && operations[idx] == 1) {
                shiftCount++;
            }
            kk >>= 1;
            idx++;
        }
        return (char)('a' + (shiftCount % 26));
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number[]} operations
 * @return {character}
 */
var kthCharacter = function(k, operations) {
    let offset = BigInt(k - 1); // use BigInt for safety with large k up to 1e14
    let ans = 0; // 0 corresponds to 'a'
    let idx = 0;
    while (offset > 0n) {
        if ((offset & 1n) === 1n) {
            if (operations[idx] === 1) {
                ans = (ans + 1) % 26;
            }
        }
        offset >>= 1n;
        idx++;
    }
    return String.fromCharCode(97 + ans);
};
```

## Typescript

```typescript
function kthCharacter(k: number, operations: number[]): string {
    let shift = 0;
    let x = k - 1; // zero‑based offset
    let idx = 0;
    while (x > 0) {
        if ((x & 1) === 1 && operations[idx] === 1) {
            shift++;
        }
        x >>= 1;
        idx++;
    }
    const base = 'a'.charCodeAt(0);
    return String.fromCharCode(base + (shift % 26));
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer[] $operations
     * @return String
     */
    function kthCharacter($k, $operations) {
        $kMinusOne = $k - 1;
        $idx = 0;
        $add = 0;
        while ($kMinusOne > 0) {
            if (($kMinusOne & 1) == 1) {
                if (isset($operations[$idx]) && $operations[$idx] == 1) {
                    $add++;
                }
            }
            $kMinusOne >>= 1;
            $idx++;
        }
        $add %= 26;
        return chr(ord('a') + $add);
    }
}
```

## Swift

```swift
class Solution {
    func kthCharacter(_ k: Int, _ operations: [Int]) -> Character {
        var inc = 0
        var pos = k - 1          // zero‑based index
        var idx = 0              // operation level
        
        while pos > 0 {
            if (pos & 1) == 1 {
                if idx < operations.count && operations[idx] == 1 {
                    inc += 1
                }
            }
            pos >>= 1
            idx += 1
        }
        
        let aScalar = UnicodeScalar("a")!.value
        let resultScalar = (aScalar + UInt32(inc % 26))!
        return Character(UnicodeScalar(resultScalar)!)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthCharacter(k: Long, operations: IntArray): Char {
        var x = k - 1
        var idx = 0
        var shift = 0
        while (x > 0) {
            if ((x and 1L) == 1L && operations[idx] == 1) {
                shift++
                if (shift >= 26) shift -= 26
            }
            x = x shr 1
            idx++
        }
        return ('a'.code + shift).toChar()
    }
}
```

## Dart

```dart
class Solution {
  String kthCharacter(int k, List<int> operations) {
    int shift = 0;
    int x = k - 1;
    int idx = 0;
    while (x > 0 && idx < operations.length) {
      if ((x & 1) == 1) {
        shift += operations[idx];
      }
      x >>= 1;
      idx++;
    }
    int charCode = 'a'.codeUnitAt(0) + (shift % 26);
    return String.fromCharCode(charCode);
  }
}
```

## Golang

```go
func kthCharacter(k int64, operations []int) byte {
    shift := 0
    x := k - 1
    pos := 0
    for x > 0 {
        if x&1 == 1 && operations[pos] == 1 {
            shift = (shift + 1) % 26
        }
        x >>= 1
        pos++
    }
    return byte('a' + shift)
}
```

## Ruby

```ruby
def kth_character(k, operations)
  shifts = 0
  x = k - 1
  idx = 0
  while x > 0 && idx < operations.length
    shifts += operations[idx] if (x & 1) == 1
    x >>= 1
    idx += 1
  end
  ((('a'.ord + shifts) % 26) + 'a'.ord).chr
end
```

## Scala

```scala
object Solution {
    def kthCharacter(k: Long, operations: Array[Int]): Char = {
        var shift = 0
        var x = k - 1
        var idx = 0
        while (x > 0 && idx < operations.length) {
            if ((x & 1L) != 0L) {
                shift += operations(idx)
            }
            idx += 1
            x >>= 1
        }
        ('a' + (shift % 26)).toChar
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_character(k: i64, operations: Vec<i32>) -> char {
        let mut ans = 0i32;
        let mut offset = k - 1; // zero‑based index
        let mut idx = 0usize;
        while offset > 0 && idx < operations.len() {
            if (offset & 1) == 1 && operations[idx] == 1 {
                ans = (ans + 1) % 26;
            }
            offset >>= 1;
            idx += 1;
        }
        (b'a' + ans as u8) as char
    }
}
```

## Racket

```racket
(define/contract (kth-character k operations)
  (-> exact-integer? (listof exact-integer?) char?)
  (let* ((ops (list->vector operations))
         (mask (- k 1)))
    (let loop ((idx 0) (m mask) (sum 0))
      (if (= m 0)
          (integer->char
           (+ (char->integer #\a)
              (modulo sum 26)))
          (let* ((bit (bitwise-and m 1))
                 (new-sum (if (= bit 1)
                              (+ sum (vector-ref ops idx))
                              sum))
                 (next-m (arithmetic-shift m -1)))
            (loop (+ idx 1) next-m new-sum))))))
```

## Erlang

```erlang
-spec kth_character(K :: integer(), Operations :: [integer()]) -> char().
kth_character(K, Operations) ->
    Count = count_shifts(K - 1, Operations, 0, 0),
    $a + (Count rem 26).

count_shifts(0, _Ops, _Idx, Acc) ->
    Acc;
count_shifts(N, Ops, Idx, Acc) ->
    Bit = N band 1,
    NewAcc = case Bit of
        1 -> 
            Op = lists:nth(Idx + 1, Ops),
            Acc + Op;
        0 -> Acc
    end,
    count_shifts(N bsr 1, Ops, Idx + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec kth_character(k :: integer, operations :: [integer]) :: String.t()
  def kth_character(k, operations) do
    x = k - 1
    ans = compute(x, operations, 0, 0)
    <<(?a + rem(ans, 26))>>
  end

  defp compute(0, _ops, _idx, acc), do: acc
  defp compute(x, ops, idx, acc) do
    bit = x &&& 1
    new_acc = if bit == 1, do: acc + Enum.at(ops, idx), else: acc
    compute(x >>> 1, ops, idx + 1, new_acc)
  end
end
```
