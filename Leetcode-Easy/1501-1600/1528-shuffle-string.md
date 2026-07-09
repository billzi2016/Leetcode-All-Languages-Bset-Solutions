# 1528. Shuffle String

## Cpp

```cpp
class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        int n = s.size();
        string t(n, ' ');
        for (int i = 0; i < n; ++i) {
            t[indices[i]] = s[i];
        }
        return t;
    }
};
```

## Java

```java
class Solution {
    public String restoreString(String s, int[] indices) {
        int n = s.length();
        char[] res = new char[n];
        for (int i = 0; i < n; i++) {
            res[indices[i]] = s.charAt(i);
        }
        return new String(res);
    }
}
```

## Python

```python
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n = len(s)
        res = [''] * n
        for ch, idx in zip(s, indices):
            res[idx] = ch
        return ''.join(res)
```

## Python3

```python
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        res = [''] * n
        for ch, idx in zip(s, indices):
            res[idx] = ch
        return ''.join(res)
```

## C

```c
#include <stdlib.h>

char* restoreString(char* s, int* indices, int indicesSize) {
    char *res = (char *)malloc(indicesSize + 1);
    for (int i = 0; i < indicesSize; ++i) {
        res[indices[i]] = s[i];
    }
    res[indicesSize] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string RestoreString(string s, int[] indices) {
        int n = s.Length;
        char[] result = new char[n];
        for (int i = 0; i < n; i++) {
            result[indices[i]] = s[i];
        }
        return new string(result);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    const n = s.length;
    const result = new Array(n);
    for (let i = 0; i < n; i++) {
        result[indices[i]] = s.charAt(i);
    }
    return result.join('');
};
```

## Typescript

```typescript
function restoreString(s: string, indices: number[]): string {
    const n = s.length;
    const result = new Array<string>(n);
    for (let i = 0; i < n; i++) {
        result[indices[i]] = s[i];
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $indices
     * @return String
     */
    function restoreString($s, $indices) {
        $n = strlen($s);
        $res = array_fill(0, $n, '');
        for ($i = 0; $i < $n; $i++) {
            $res[$indices[$i]] = $s[$i];
        }
        return implode('', $res);
    }
}
```

## Swift

```swift
class Solution {
    func restoreString(_ s: String, _ indices: [Int]) -> String {
        var result = [Character](repeating: " ", count: s.count)
        let chars = Array(s)
        for (i, ch) in chars.enumerated() {
            result[indices[i]] = ch
        }
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun restoreString(s: String, indices: IntArray): String {
        val n = s.length
        val result = CharArray(n)
        for (i in 0 until n) {
            result[indices[i]] = s[i]
        }
        return String(result)
    }
}
```

## Dart

```dart
class Solution {
  String restoreString(String s, List<int> indices) {
    int n = s.length;
    List<String> result = List.filled(n, '');
    for (int i = 0; i < n; i++) {
      result[indices[i]] = s[i];
    }
    return result.join();
  }
}
```

## Golang

```go
func restoreString(s string, indices []int) string {
	n := len(s)
	res := make([]byte, n)
	for i, idx := range indices {
		res[idx] = s[i]
	}
	return string(res)
}
```

## Ruby

```ruby
def restore_string(s, indices)
  n = s.length
  result = Array.new(n)
  s.each_char.with_index do |ch, i|
    result[indices[i]] = ch
  end
  result.join
end
```

## Scala

```scala
object Solution {
    def restoreString(s: String, indices: Array[Int]): String = {
        val n = s.length
        val res = new Array[Char](n)
        var i = 0
        while (i < n) {
            res(indices(i)) = s.charAt(i)
            i += 1
        }
        new String(res)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        let n = s.len();
        let mut res = vec![' '; n];
        for (i, ch) in s.chars().enumerate() {
            let idx = indices[i] as usize;
            res[idx] = ch;
        }
        res.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (restore-string s indices)
  (-> string? (listof exact-integer?) string?)
  (let* ([n (string-length s)]
         [result (make-string n #\space)]
         [idx-vec (list->vector indices)])
    (for ([i (in-range n)])
      (let ([pos (vector-ref idx-vec i)])
        (string-set! result pos (string-ref s i))))
    result))
```

## Erlang

```erlang
-spec restore_string(S :: unicode:unicode_binary(), Indices :: [integer()]) -> unicode:unicode_binary().
restore_string(S, Indices) ->
    N = byte_size(S),
    Chars = [binary:at(S, I) || I <- lists:seq(0, N - 1)],
    Pairs = lists:zip(Indices, Chars),
    Sorted = lists:keysort(1, Pairs),
    ShuffledChars = [C || {_Idx, C} <- Sorted],
    list_to_binary(ShuffledChars).
```

## Elixir

```elixir
defmodule Solution do
  @spec restore_string(s :: String.t(), indices :: [integer]) :: String.t()
  def restore_string(s, indices) do
    chars = String.graphemes(s)
    n = length(chars)
    result = List.duplicate("", n)

    shuffled =
      Enum.reduce(0..(n - 1), result, fn i, acc ->
        idx = Enum.at(indices, i)
        ch = Enum.at(chars, i)
        List.replace_at(acc, idx, ch)
      end)

    Enum.join(shuffled)
  end
end
```
