# 2575. Find the Divisibility Array of a String

## Cpp

```cpp
class Solution {
public:
    vector<int> divisibilityArray(string word, int m) {
        int n = word.size();
        vector<int> ans(n);
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            cur = (cur * 10 + (word[i] - '0')) % m;
            ans[i] = (cur == 0) ? 1 : 0;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] divisibilityArray(String word, int m) {
        int n = word.length();
        int[] result = new int[n];
        long remainder = 0;
        for (int i = 0; i < n; i++) {
            int digit = word.charAt(i) - '0';
            remainder = (remainder * 10 + digit) % m;
            if (remainder == 0) {
                result[i] = 1;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        res = []
        cur = 0
        for ch in word:
            cur = (cur * 10 + ord(ch) - 48) % m
            res.append(1 if cur == 0 else 0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        rem = 0
        for ch in word:
            rem = (rem * 10 + int(ch)) % m
            res.append(1 if rem == 0 else 0)
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* divisibilityArray(char* word, int m, int* returnSize) {
    int n = 0;
    while (word[n] != '\0') n++;
    *returnSize = n;
    int *res = (int*)malloc(n * sizeof(int));
    long long cur = 0;
    for (int i = 0; i < n; ++i) {
        int digit = word[i] - '0';
        cur = (cur * 10 + digit) % m;
        res[i] = (cur == 0) ? 1 : 0;
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] DivisibilityArray(string word, int m) {
        int n = word.Length;
        int[] result = new int[n];
        long remainder = 0;
        for (int i = 0; i < n; i++) {
            int digit = word[i] - '0';
            remainder = (remainder * 10 + digit) % m;
            if (remainder == 0) result[i] = 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} m
 * @return {number[]}
 */
var divisibilityArray = function(word, m) {
    const n = word.length;
    const res = new Array(n);
    let rem = 0;
    for (let i = 0; i < n; ++i) {
        const digit = word.charCodeAt(i) - 48; // '0' char code is 48
        rem = (rem * 10 + digit) % m;
        res[i] = rem === 0 ? 1 : 0;
    }
    return res;
};
```

## Typescript

```typescript
function divisibilityArray(word: string, m: number): number[] {
    const n = word.length;
    const result = new Array<number>(n);
    let remainder = 0;
    for (let i = 0; i < n; i++) {
        const digit = word.charCodeAt(i) - 48; // '0' char code is 48
        remainder = (remainder * 10 + digit) % m;
        result[i] = remainder === 0 ? 1 : 0;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $m
     * @return Integer[]
     */
    function divisibilityArray($word, $m) {
        $n = strlen($word);
        $result = [];
        $rem = 0;
        for ($i = 0; $i < $n; $i++) {
            $digit = intval($word[$i]);
            $rem = ($rem * 10 + $digit) % $m;
            $result[] = ($rem === 0) ? 1 : 0;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func divisibilityArray(_ word: String, _ m: Int) -> [Int] {
        var result = [Int]()
        result.reserveCapacity(word.count)
        var remainder = 0
        for ch in word {
            let digit = Int(ch.unicodeScalars.first!.value - 48)
            remainder = (remainder * 10 + digit) % m
            result.append(remainder == 0 ? 1 : 0)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun divisibilityArray(word: String, m: Int): IntArray {
        val n = word.length
        val result = IntArray(n)
        var rem = 0L
        val mod = m.toLong()
        for (i in 0 until n) {
            val digit = (word[i] - '0')
            rem = (rem * 10 + digit) % mod
            if (rem == 0L) result[i] = 1
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> divisibilityArray(String word, int m) {
    List<int> result = List.filled(word.length, 0);
    int rem = 0;
    for (int i = 0; i < word.length; i++) {
      int digit = word.codeUnitAt(i) - 48; // '0' ascii is 48
      rem = (rem * 10 + digit) % m;
      result[i] = rem == 0 ? 1 : 0;
    }
    return result;
  }
}
```

## Golang

```go
func divisibilityArray(word string, m int) []int {
    n := len(word)
    res := make([]int, n)
    var rem int64
    mod := int64(m)
    for i, ch := range word {
        digit := int64(ch - '0')
        rem = (rem*10 + digit) % mod
        if rem == 0 {
            res[i] = 1
        }
    }
    return res
}
```

## Ruby

```ruby
def divisibility_array(word, m)
  result = []
  rem = 0
  word.each_byte do |b|
    digit = b - 48
    rem = (rem * 10 + digit) % m
    result << (rem.zero? ? 1 : 0)
  end
  result
end
```

## Scala

```scala
object Solution {
    def divisibilityArray(word: String, m: Int): Array[Int] = {
        val n = word.length
        val res = new Array[Int](n)
        var rem: Long = 0L
        val mod = m.toLong
        var i = 0
        while (i < n) {
            val digit = (word.charAt(i) - '0').toInt
            rem = (rem * 10 + digit) % mod
            res(i) = if (rem == 0L) 1 else 0
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn divisibility_array(word: String, m: i32) -> Vec<i32> {
        let mut result = Vec::with_capacity(word.len());
        let mut rem: i64 = 0;
        let mod_val = m as i64;
        for b in word.bytes() {
            let digit = (b - b'0') as i64;
            rem = (rem * 10 + digit) % mod_val;
            result.push(if rem == 0 { 1 } else { 0 });
        }
        result
    }
}
```

## Racket

```racket
(define/contract (divisibility-array word m)
  (-> string? exact-integer? (listof exact-integer?))
  (let ((len (string-length word)))
    (let loop ((i 0) (rem 0) (acc '()))
      (if (= i len)
          (reverse acc)
          (let* ((ch (string-ref word i))
                 (digit (- (char->integer ch) (char->integer #\0)))
                 (new-rem (modulo (+ (* rem 10) digit) m))
                 (val (if (= new-rem 0) 1 0)))
            (loop (+ i 1) new-rem (cons val acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([divisibility_array/2]).

-spec divisibility_array(Word :: unicode:unicode_binary(), M :: integer()) -> [integer()].
divisibility_array(Word, M) ->
    Bytes = binary_to_list(Word),
    compute(Bytes, M, 0, []).

compute([], _M, _Rem, Acc) ->
    lists:reverse(Acc);
compute([C|Rest], M, Rem, Acc) ->
    Digit = C - $0,
    NewRem = (Rem * 10 + Digit) rem M,
    Flag = case NewRem of
        0 -> 1;
        _ -> 0
    end,
    compute(Rest, M, NewRem, [Flag|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec divisibility_array(word :: String.t(), m :: integer) :: [integer]
  def divisibility_array(word, m) do
    word
    |> String.to_charlist()
    |> Enum.reduce({[], 0}, fn ch, {acc, remainder} ->
      digit = ch - ?0
      new_remainder = remainder * 10 + digit
      new_remainder = rem(new_remainder, m)
      {[if new_remainder == 0, do: 1, else: 0 | acc], new_remainder}
    end)
    |> elem(0)
    |> Enum.reverse()
  end
end
```
