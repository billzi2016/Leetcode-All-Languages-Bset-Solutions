# 1663. Smallest String With A Given Numeric Value

## Cpp

```cpp
class Solution {
public:
    string getSmallestString(int n, int k) {
        int extra = k - n; // amount to distribute beyond all 'a's
        string res(n, 'a');
        for (int i = n - 1; i >= 0 && extra > 0; --i) {
            int add = min(25, extra);
            res[i] = char('a' + add);
            extra -= add;
        }
        return res;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public String getSmallestString(int n, int k) {
        char[] res = new char[n];
        Arrays.fill(res, 'a');
        int remaining = k - n;
        for (int i = n - 1; i >= 0 && remaining > 0; i--) {
            int add = Math.min(25, remaining);
            res[i] = (char) ('a' + add);
            remaining -= add;
        }
        return new String(res);
    }
}
```

## Python

```python
class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        extra = k - n  # additional value beyond all 'a's
        res = ['a'] * n
        i = n - 1
        while extra > 0 and i >= 0:
            add = min(25, extra)
            res[i] = chr(ord('a') + add)
            extra -= add
            i -= 1
        return ''.join(res)
```

## Python3

```python
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        extra = k - n
        res = ['a'] * n
        i = n - 1
        while extra > 0 and i >= 0:
            inc = min(25, extra)
            res[i] = chr(ord('a') + inc)
            extra -= inc
            i -= 1
        return ''.join(res)
```

## C

```c
#include <stdlib.h>

char* getSmallestString(int n, int k) {
    char *s = (char *)malloc((n + 1) * sizeof(char));
    if (!s) return NULL;
    
    for (int i = 0; i < n; ++i) s[i] = 'a';
    s[n] = '\0';
    
    int remaining = k - n; // extra value to distribute
    for (int i = n - 1; i >= 0 && remaining > 0; --i) {
        int add = remaining < 25 ? remaining : 25;
        s[i] += add;
        remaining -= add;
    }
    
    return s;
}
```

## Csharp

```csharp
public class Solution
{
    public string GetSmallestString(int n, int k)
    {
        char[] result = new char[n];
        for (int i = 0; i < n; i++) result[i] = 'a';
        int remaining = k - n;
        for (int i = n - 1; i >= 0 && remaining > 0; i--)
        {
            int add = Math.Min(25, remaining);
            result[i] = (char)('a' + add);
            remaining -= add;
        }
        return new string(result);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getSmallestString = function(n, k) {
    const chars = new Array(n).fill('a');
    let remaining = k - n; // extra value beyond all 'a's
    
    for (let i = n - 1; i >= 0 && remaining > 0; i--) {
        const add = Math.min(25, remaining);
        chars[i] = String.fromCharCode(97 + add); // 97 is code of 'a'
        remaining -= add;
    }
    
    return chars.join('');
};
```

## Typescript

```typescript
function getSmallestString(n: number, k: number): string {
    const result: string[] = new Array(n).fill('a');
    let remaining = k - n; // extra value beyond all 'a's
    for (let i = n - 1; i >= 0 && remaining > 0; i--) {
        const add = Math.min(25, remaining);
        result[i] = String.fromCharCode(97 + add);
        remaining -= add;
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getSmallestString($n, $k) {
        $remaining = $k - $n; // extra value beyond all 'a's
        $chars = array_fill(0, $n, 'a');
        for ($i = $n - 1; $i >= 0 && $remaining > 0; $i--) {
            $add = min(25, $remaining);
            $chars[$i] = chr(ord('a') + $add);
            $remaining -= $add;
        }
        return implode('', $chars);
    }
}
```

## Swift

```swift
class Solution {
    func getSmallestString(_ n: Int, _ k: Int) -> String {
        var chars = [UInt8](repeating: 97, count: n) // 'a' ASCII is 97
        var remaining = k - n
        var i = n - 1
        while remaining > 0 && i >= 0 {
            let add = min(25, remaining)
            chars[i] += UInt8(add)
            remaining -= add
            i -= 1
        }
        return String(bytes: chars, encoding: .utf8)!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getSmallestString(n: Int, k: Int): String {
        val chars = CharArray(n) { 'a' }
        var remaining = k - n
        var idx = n - 1
        while (idx >= 0 && remaining > 0) {
            val add = if (remaining >= 25) 25 else remaining
            chars[idx] = ('a'.code + add).toChar()
            remaining -= add
            idx--
        }
        return String(chars)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  String getSmallestString(int n, int k) {
    List<int> chars = List.filled(n, 97); // ASCII of 'a'
    int extra = k - n; // additional value needed beyond all 'a's
    for (int i = n - 1; i >= 0 && extra > 0; i--) {
      int add = min(25, extra);
      chars[i] += add;
      extra -= add;
    }
    return String.fromCharCodes(chars);
  }
}
```

## Golang

```go
func getSmallestString(n int, k int) string {
    res := make([]byte, n)
    for i := 0; i < n; i++ {
        res[i] = 'a'
    }
    extra := k - n
    for i := n - 1; i >= 0 && extra > 0; i-- {
        add := 25
        if extra < 25 {
            add = extra
        }
        res[i] = byte('a' + add)
        extra -= add
    }
    return string(res)
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_smallest_string(n, k)
  chars = Array.new(n, 'a')
  extra = k - n
  i = n - 1
  while extra > 0 && i >= 0
    add = [extra, 25].min
    chars[i] = (97 + add).chr
    extra -= add
    i -= 1
  end
  chars.join
end
```

## Scala

```scala
object Solution {
    def getSmallestString(n: Int, k: Int): String = {
        val chars = new Array[Char](n)
        java.util.Arrays.fill(chars, 'a')
        var remaining = k - n
        var idx = n - 1
        while (remaining > 0 && idx >= 0) {
            val add = math.min(25, remaining)
            chars(idx) = ('a'.toInt + add).toChar
            remaining -= add
            idx -= 1
        }
        new String(chars)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_smallest_string(n: i32, k: i32) -> String {
        let len = n as usize;
        let mut chars = vec![b'a'; len];
        let mut remaining = k - n; // extra value beyond all 'a's
        let mut idx = len;
        while remaining > 0 {
            idx -= 1;
            let add = std::cmp::min(25, remaining);
            chars[idx] = b'a' + add as u8;
            remaining -= add;
        }
        unsafe { String::from_utf8_unchecked(chars) }
    }
}
```

## Racket

```racket
(define/contract (get-smallest-string n k)
  (-> exact-integer? exact-integer? string?)
  (let* ((s (make-string n #\a))
         (remaining (- k n)))
    (for ([i (in-range (sub1 n) -1 -1)])
      (when (> remaining 0)
        (define inc (min 25 remaining))
        (string-set! s i (integer->char (+ (char->integer #\a) inc)))
        (set! remaining (- remaining inc))))
    s))
```

## Erlang

```erlang
-module(solution).
-export([get_smallest_string/2]).

-spec get_smallest_string(N :: integer(), K :: integer()) -> unicode:unicode_binary().
get_smallest_string(N, K) ->
    Rem = K - N,
    List = build(N, Rem, []),
    list_to_binary(List).

build(0, _Rem, Acc) ->
    Acc;
build(Pos, Rem, Acc) when Pos > 0 ->
    Add = case Rem of
        R when R >= 25 -> 25;
        R -> R
    end,
    Char = $a + Add,
    build(Pos - 1, Rem - Add, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_smallest_string(n :: integer, k :: integer) :: String.t()
  def get_smallest_string(n, k) do
    extra = k - n
    chars = build(n, extra, [])
    List.to_string(chars)
  end

  defp build(0, _extra, acc), do: acc

  defp build(pos, extra, acc) when pos > 0 do
    inc = if extra >= 25, do: 25, else: extra
    char_code = ?a + inc
    build(pos - 1, extra - inc, [char_code | acc])
  end
end
```
