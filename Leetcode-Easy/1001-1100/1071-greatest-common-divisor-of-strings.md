# 1071. Greatest Common Divisor of Strings

## Cpp

```cpp
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) return "";
        int g = std::gcd((int)str1.size(), (int)str2.size());
        return str1.substr(0, g);
    }
};
```

## Java

```java
class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (! (str1 + str2).equals(str2 + str1)) {
            return "";
        }
        int g = gcd(str1.length(), str2.length());
        return str1.substring(0, g);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        from math import gcd
        g = gcd(len(str1), len(str2))
        return str1[:g]
```

## Python3

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        import math
        g = math.gcd(len(str1), len(str2))
        return str1[:g]
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

char* gcdOfStrings(char* str1, char* str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    /* Verify that str1 + str2 == str2 + str1 */
    for (int i = 0; i < len1 + len2; ++i) {
        char c1 = (i < len1) ? str1[i] : str2[i - len1];
        char c2 = (i < len2) ? str2[i] : str1[i - len2];
        if (c1 != c2) {
            return "";
        }
    }

    int g = gcd(len1, len2);
    char* res = (char*)malloc(g + 1);
    memcpy(res, str1, g);
    res[g] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string GcdOfStrings(string str1, string str2)
    {
        if (str1 + str2 != str2 + str1) return "";
        int gcdLength = Gcd(str1.Length, str2.Length);
        return str1.Substring(0, gcdLength);
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    if (str1 + str2 !== str2 + str1) return "";
    
    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    };
    
    const len = gcd(str1.length, str2.length);
    return str1.slice(0, len);
};
```

## Typescript

```typescript
function gcdOfStrings(str1: string, str2: string): string {
    if (str1 + str2 !== str2 + str1) return "";
    
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    };
    
    const g = gcd(str1.length, str2.length);
    return str1.slice(0, g);
}
```

## Php

```php
class Solution {

    /**
     * @param String $str1
     * @param String $str2
     * @return String
     */
    function gcdOfStrings($str1, $str2) {
        if ($str1 . $str2 !== $str2 . $str1) {
            return "";
        }
        $len1 = strlen($str1);
        $len2 = strlen($str2);
        $g = $this->gcd($len1, $len2);
        return substr($str1, 0, $g);
    }

    private function gcd(int $a, int $b): int {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func gcdOfStrings(_ str1: String, _ str2: String) -> String {
        if str1 + str2 != str2 + str1 {
            return ""
        }
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a
            var y = b
            while y != 0 {
                let temp = x % y
                x = y
                y = temp
            }
            return x
        }
        let length = gcd(str1.count, str2.count)
        return String(str1.prefix(length))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun gcdOfStrings(str1: String, str2: String): String {
        if (str1 + str2 != str2 + str1) return ""
        val g = gcd(str1.length, str2.length)
        return str1.substring(0, g)
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  String gcdOfStrings(String str1, String str2) {
    if (str1 + str2 != str2 + str1) return "";
    int len = _gcd(str1.length, str2.length);
    return str1.substring(0, len);
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = a % b;
      a = b;
      b = temp;
    }
    return a;
  }
}
```

## Golang

```go
func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}
	g := gcd(len(str1), len(str2))
	return str1[:g]
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
```

## Ruby

```ruby
def gcd_of_strings(str1, str2)
  return "" unless (str1 + str2) == (str2 + str1)
  len = str1.length.gcd(str2.length)
  str1[0, len]
end
```

## Scala

```scala
object Solution {
    def gcdOfStrings(str1: String, str2: String): String = {
        if ((str1 + str2) != (str2 + str1)) return ""
        val g = gcd(str1.length, str2.length)
        str1.substring(0, g)
    }

    private def gcd(a: Int, b: Int): Int = {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        x
    }
}
```

## Rust

```rust
impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        // Check if concatenations are equal; otherwise no common divisor string exists.
        if format!("{}{}", str1, str2) != format!("{}{}", str2, str1) {
            return "".to_string();
        }

        fn gcd(mut a: usize, mut b: usize) -> usize {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a
        }

        let g = gcd(str1.len(), str2.len());
        // Both strings consist of uppercase ASCII letters, so byte slicing is safe.
        str1[..g].to_string()
    }
}
```

## Racket

```racket
(define/contract (gcd-of-strings str1 str2)
  (-> string? string? string?)
  (let* ((concat1 (string-append str1 str2))
         (concat2 (string-append str2 str1)))
    (if (not (string=? concat1 concat2))
        ""
        (letrec ((gcd (lambda (a b)
                        (if (= b 0) a (gcd b (remainder a b))))))
          (let* ((len1 (string-length str1))
                 (len2 (string-length str2))
                 (g (gcd len1 len2)))
            (substring str1 0 g))))))
```

## Erlang

```erlang
-module(solution).
-export([gcd_of_strings/2]).

-spec gcd_of_strings(Str1 :: unicode:unicode_binary(), Str2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
gcd_of_strings(Str1, Str2) ->
    case (Str1 ++ Str2) =:= (Str2 ++ Str1) of
        false -> <<>>;
        true ->
            G = gcd(byte_size(Str1), byte_size(Str2)),
            binary:part(Str1, {0, G})
    end.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec gcd_of_strings(String.t(), String.t()) :: String.t()
  def gcd_of_strings(str1, str2) do
    if str1 <> str2 == str2 <> str1 do
      len = Integer.gcd(String.length(str1), String.length(str2))
      String.slice(str1, 0, len)
    else
      ""
    end
  end
end
```
