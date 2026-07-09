# 1758. Minimum Changes To Make Alternating Binary String

## Cpp

```cpp
class Solution {
public:
    int minOperations(string s) {
        int mismatchesStartWithZero = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            char expected = (i % 2 == 0) ? '0' : '1';
            if (s[i] != expected) ++mismatchesStartWithZero;
        }
        int n = s.size();
        int mismatchesStartWithOne = n - mismatchesStartWithZero;
        return min(mismatchesStartWithZero, mismatchesStartWithOne);
    }
};
```

## Java

```java
class Solution {
    public int minOperations(String s) {
        int n = s.length();
        int mismatchesStartWithZero = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            // Expected character if the alternating string starts with '0'
            char expected = (i % 2 == 0) ? '0' : '1';
            if (c != expected) {
                mismatchesStartWithZero++;
            }
        }
        int mismatchesStartWithOne = n - mismatchesStartWithZero;
        return Math.min(mismatchesStartWithZero, mismatchesStartWithOne);
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        mismatches = 0
        for i, ch in enumerate(s):
            # expected char if pattern starts with '0'
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                mismatches += 1
        return min(mismatches, len(s) - mismatches)
```

## Python3

```python
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        start0 = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                start0 += 1
        return min(start0, n - start0)
```

## C

```c
int minOperations(char* s) {
    int cnt = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        char expected = (i % 2 == 0) ? '0' : '1';
        if (s[i] != expected) cnt++;
    }
    int n = 0;
    while (s[n] != '\0') n++;
    return cnt < (n - cnt) ? cnt : (n - cnt);
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(string s) {
        int start0 = 0;
        for (int i = 0; i < s.Length; i++) {
            char expected = (i % 2 == 0) ? '0' : '1';
            if (s[i] != expected) start0++;
        }
        return Math.Min(start0, s.Length - start0);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    let mismatchesStartWithZero = 0;
    for (let i = 0; i < s.length; i++) {
        const expectedChar = (i % 2 === 0) ? '0' : '1';
        if (s[i] !== expectedChar) mismatchesStartWithZero++;
    }
    return Math.min(mismatchesStartWithZero, s.length - mismatchesStartWithZero);
};
```

## Typescript

```typescript
function minOperations(s: string): number {
    let mismatches = 0;
    const n = s.length;
    for (let i = 0; i < n; i++) {
        const expected = (i % 2 === 0) ? '0' : '1';
        if (s[i] !== expected) mismatches++;
    }
    return Math.min(mismatches, n - mismatches);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minOperations($s) {
        $n = strlen($s);
        $mismatch = 0;
        for ($i = 0; $i < $n; $i++) {
            $expected = ($i % 2 === 0) ? '0' : '1';
            if ($s[$i] !== $expected) {
                $mismatch++;
            }
        }
        return min($mismatch, $n - $mismatch);
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ s: String) -> Int {
        var mismatches = 0
        for (i, ch) in s.enumerated() {
            if i % 2 == 0 {
                if ch == "1" { mismatches += 1 }
            } else {
                if ch == "0" { mismatches += 1 }
            }
        }
        let n = s.count
        return min(mismatches, n - mismatches)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(s: String): Int {
        var mismatchesStartWithZero = 0
        for (i in s.indices) {
            val c = s[i]
            if (i % 2 == 0) {
                if (c != '0') mismatchesStartWithZero++
            } else {
                if (c != '1') mismatchesStartWithZero++
            }
        }
        return kotlin.math.min(mismatchesStartWithZero, s.length - mismatchesStartWithZero)
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(String s) {
    int mismatches = 0;
    for (int i = 0; i < s.length; i++) {
      if ((i % 2 == 0 && s[i] != '0') || (i % 2 == 1 && s[i] != '1')) {
        mismatches++;
      }
    }
    int n = s.length;
    return mismatches < n - mismatches ? mismatches : n - mismatches;
  }
}
```

## Golang

```go
package main

func minOperations(s string) int {
	cnt := 0
	for i, ch := range s {
		if i%2 == 0 {
			if ch != '0' {
				cnt++
			}
		} else {
			if ch != '1' {
				cnt++
			}
		}
	}
	n := len(s)
	if cnt > n-cnt {
		return n - cnt
	}
	return cnt
}
```

## Ruby

```ruby
def min_operations(s)
  start0 = 0
  s.each_char.with_index do |ch, i|
    if i.even?
      start0 += 1 if ch == '1'
    else
      start0 += 1 if ch == '0'
    end
  end
  [start0, s.length - start0].min
end
```

## Scala

```scala
object Solution {
    def minOperations(s: String): Int = {
        var mismatchesStartWithZero = 0
        val n = s.length
        for (i <- 0 until n) {
            if ((i & 1) == 0) { // even index, expect '0' for pattern starting with '0'
                if (s.charAt(i) != '0') mismatchesStartWithZero += 1
            } else { // odd index, expect '1'
                if (s.charAt(i) != '1') mismatchesStartWithZero += 1
            }
        }
        Math.min(mismatchesStartWithZero, n - mismatchesStartWithZero)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut start0 = 0usize;
        for (i, &c) in bytes.iter().enumerate() {
            let expected = if i % 2 == 0 { b'0' } else { b'1' };
            if c != expected {
                start0 += 1;
            }
        }
        let start1 = n - start0;
        std::cmp::min(start0, start1) as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (start0
          (for/sum ([i (in-range n)])
            (if (= (modulo i 2) 0)
                (if (char=? (string-ref s i) #\1) 1 0)
                (if (char=? (string-ref s i) #\0) 1 0)))))
    (min start0 (- n start0))))
```

## Erlang

```erlang
-spec min_operations(S :: unicode:unicode_binary()) -> integer().
min_operations(S) ->
    Len = byte_size(S),
    {_, Count} = lists:foldl(
        fun(Char, {Idx, Acc}) ->
            Expected = case Idx rem 2 of
                0 -> $0;
                _ -> $1
            end,
            NewAcc = if Char =/= Expected -> Acc + 1; true -> Acc end,
            {Idx + 1, NewAcc}
        end,
        {0, 0},
        binary_to_list(S)
    ),
    erlang:min(Count, Len - Count).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(s :: String.t()) :: integer()
  def min_operations(s) do
    {mismatch_start0, _} =
      s
      |> String.graphemes()
      |> Enum.reduce({0, 0}, fn ch, {cnt, idx} ->
        cnt =
          if rem(idx, 2) == 0 do
            if ch == "1", do: cnt + 1, else: cnt
          else
            if ch == "0", do: cnt + 1, else: cnt
          end

        {cnt, idx + 1}
      end)

    n = String.length(s)
    Kernel.min(mismatch_start0, n - mismatch_start0)
  end
end
```
