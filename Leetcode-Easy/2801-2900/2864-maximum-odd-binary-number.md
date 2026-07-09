# 2864. Maximum Odd Binary Number

## Cpp

```cpp
class Solution {
public:
    std::string maximumOddBinaryNumber(std::string s) {
        int ones = 0;
        for (char c : s) if (c == '1') ++ones;
        int zeros = s.size() - ones;
        std::string result;
        result.append(ones > 0 ? ones - 1 : 0, '1');
        result.append(zeros, '0');
        result.push_back('1');
        return result;
    }
};
```

## Java

```java
class Solution {
    public String maximumOddBinaryNumber(String s) {
        int n = s.length();
        int ones = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                ones++;
            }
        }
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < ones - 1; i++) {
            sb.append('1');
        }
        for (int i = 0; i < n - ones; i++) {
            sb.append('0');
        }
        sb.append('1');
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count('1')
        zeros = len(s) - ones
        return '1' * (ones - 1) + '0' * zeros + '1'
```

## Python3

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = len(s) - ones
        return '1' * (ones - 1) + '0' * zeros + '1'
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* maximumOddBinaryNumber(char* s) {
    int n = strlen(s);
    int ones = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') ++ones;
    }
    
    char *res = (char *)malloc((n + 1) * sizeof(char));
    int idx = 0;
    
    for (int i = 0; i < ones - 1; ++i) {
        res[idx++] = '1';
    }
    for (int i = 0; i < n - ones; ++i) {
        res[idx++] = '0';
    }
    res[idx++] = '1';
    res[idx] = '\0';
    
    return res;
}
```

## Csharp

```csharp
using System.Text;

public class Solution {
    public string MaximumOddBinaryNumber(string s) {
        int n = s.Length;
        int ones = 0;
        foreach (char c in s) {
            if (c == '1') ones++;
        }
        var sb = new StringBuilder(n);
        if (ones > 1) sb.Append('1', ones - 1);
        sb.Append('0', n - ones);
        sb.Append('1');
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function(s) {
    let ones = 0;
    for (const ch of s) {
        if (ch === '1') ones++;
    }
    const zeros = s.length - ones;
    const prefixOnes = ones > 1 ? '1'.repeat(ones - 1) : '';
    return prefixOnes + '0'.repeat(zeros) + '1';
};
```

## Typescript

```typescript
function maximumOddBinaryNumber(s: string): string {
    let ones = 0;
    for (const ch of s) {
        if (ch === '1') ones++;
    }
    const zeros = s.length - ones;
    return '1'.repeat(ones - 1) + '0'.repeat(zeros) + '1';
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function maximumOddBinaryNumber($s) {
        $ones = substr_count($s, '1');
        $n = strlen($s);
        $prefixOnes = $ones > 1 ? str_repeat('1', $ones - 1) : '';
        $zeros = $n - $ones > 0 ? str_repeat('0', $n - $ones) : '';
        return $prefixOnes . $zeros . '1';
    }
}
```

## Swift

```swift
class Solution {
    func maximumOddBinaryNumber(_ s: String) -> String {
        let n = s.count
        var ones = 0
        for ch in s {
            if ch == "1" { ones += 1 }
        }
        var result = ""
        if ones > 1 {
            result += String(repeating: "1", count: ones - 1)
        }
        let zerosCount = n - ones
        if zerosCount > 0 {
            result += String(repeating: "0", count: zerosCount)
        }
        result += "1"
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumOddBinaryNumber(s: String): String {
        val ones = s.count { it == '1' }
        val zeros = s.length - ones
        val sb = StringBuilder()
        repeat(ones - 1) { sb.append('1') }
        repeat(zeros) { sb.append('0') }
        sb.append('1')
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String maximumOddBinaryNumber(String s) {
    int ones = 0;
    for (int i = 0; i < s.length; ++i) {
      if (s.codeUnitAt(i) == 49) { // '1'
        ones++;
      }
    }
    int zeros = s.length - ones;
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < ones - 1; ++i) {
      sb.write('1');
    }
    for (int i = 0; i < zeros; ++i) {
      sb.write('0');
    }
    sb.write('1');
    return sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func maximumOddBinaryNumber(s string) string {
	n := len(s)
	ones := 0
	for i := 0; i < n; i++ {
		if s[i] == '1' {
			ones++
		}
	}
	var b strings.Builder
	b.Grow(n)
	for i := 0; i < ones-1; i++ {
		b.WriteByte('1')
	}
	for i := 0; i < n-ones; i++ {
		b.WriteByte('0')
	}
	b.WriteByte('1')
	return b.String()
}
```

## Ruby

```ruby
def maximum_odd_binary_number(s)
  ones = s.count('1')
  zeros = s.length - ones
  ('1' * (ones - 1)) + ('0' * zeros) + '1'
end
```

## Scala

```scala
object Solution {
    def maximumOddBinaryNumber(s: String): String = {
        val n = s.length
        var ones = 0
        var i = 0
        while (i < n) {
            if (s.charAt(i) == '1') ones += 1
            i += 1
        }
        val zeros = n - ones
        val sb = new StringBuilder(n)
        var j = 0
        while (j < ones - 1) {
            sb.append('1')
            j += 1
        }
        j = 0
        while (j < zeros) {
            sb.append('0')
            j += 1
        }
        sb.append('1')
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let n = s.len();
        let ones = s.bytes().filter(|&b| b == b'1').count();
        let mut result = String::with_capacity(n);
        for _ in 0..ones.saturating_sub(1) {
            result.push('1');
        }
        for _ in 0..(n - ones) {
            result.push('0');
        }
        result.push('1');
        result
    }
}
```

## Racket

```racket
(define/contract (maximum-odd-binary-number s)
  (-> string? string?)
  (let* ((n (string-length s))
         (ones (for/sum ([c (in-string s)]) (if (char=? c #\1) 1 0)))
         (lead-ones (make-string (- ones 1) #\1))
         (zeros (make-string (- n ones) #\0)))
    (string-append lead-ones zeros "1")))
```

## Erlang

```erlang
-spec maximum_odd_binary_number(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
maximum_odd_binary_number(S) ->
    Ones = count_ones(binary_to_list(S), 0),
    N = byte_size(S),
    PrefixOnes = lists:duplicate(Ones - 1, $1),
    Zeros = lists:duplicate(N - Ones, $0),
    ResultList = PrefixOnes ++ Zeros ++ [$1],
    list_to_binary(ResultList).

count_ones([], Acc) -> Acc;
count_ones([$1 | Rest], Acc) -> count_ones(Rest, Acc + 1);
count_ones([_   | Rest], Acc) -> count_ones(Rest, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_odd_binary_number(s :: String.t) :: String.t
  def maximum_odd_binary_number(s) do
    len = byte_size(s)
    ones = :binary.matches(s, "1") |> length
    zeros = len - ones

    prefix =
      if ones > 1 do
        String.duplicate("1", ones - 1)
      else
        ""
      end

    middle = String.duplicate("0", zeros)
    prefix <> middle <> "1"
  end
end
```
