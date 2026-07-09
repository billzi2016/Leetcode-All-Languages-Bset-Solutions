# 0165. Compare Version Numbers

## Cpp

```cpp
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int i = 0, j = 0;
        int n1 = version1.size(), n2 = version2.size();
        while (i < n1 || j < n2) {
            long num1 = 0, num2 = 0;
            while (i < n1 && version1[i] != '.') {
                num1 = num1 * 10 + (version1[i] - '0');
                ++i;
            }
            while (j < n2 && version2[j] != '.') {
                num2 = num2 * 10 + (version2[j] - '0');
                ++j;
            }
            if (num1 < num2) return -1;
            if (num1 > num2) return 1;
            ++i; // skip '.'
            ++j; // skip '.'
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        int n = Math.max(v1.length, v2.length);
        for (int i = 0; i < n; i++) {
            int num1 = i < v1.length ? Integer.parseInt(v1[i]) : 0;
            int num2 = i < v2.length ? Integer.parseInt(v2[i]) : 0;
            if (num1 < num2) return -1;
            if (num1 > num2) return 1;
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        for i in range(n):
            r1 = int(v1[i]) if i < len(v1) else 0
            r2 = int(v2[i]) if i < len(v2) else 0
            if r1 > r2:
                return 1
            if r1 < r2:
                return -1
        return 0
```

## Python3

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        for i in range(n):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        return 0
```

## C

```c
int compareVersion(char* version1, char* version2) {
    const char *p1 = version1, *p2 = version2;
    while (*p1 != '\0' || *p2 != '\0') {
        int n1 = 0, n2 = 0;
        while (*p1 && *p1 != '.') {
            n1 = n1 * 10 + (*p1 - '0');
            p1++;
        }
        if (*p1 == '.') p1++;  // skip dot
        
        while (*p2 && *p2 != '.') {
            n2 = n2 * 10 + (*p2 - '0');
            p2++;
        }
        if (*p2 == '.') p2++;  // skip dot
        
        if (n1 > n2) return 1;
        if (n1 < n2) return -1;
    }
    return 0;
}
```

## Csharp

```csharp
public class Solution
{
    public int CompareVersion(string version1, string version2)
    {
        var v1 = version1.Split('.');
        var v2 = version2.Split('.');

        int len = Math.Max(v1.Length, v2.Length);
        for (int i = 0; i < len; i++)
        {
            int num1 = i < v1.Length ? int.Parse(v1[i]) : 0;
            int num2 = i < v2.Length ? int.Parse(v2[i]) : 0;

            if (num1 > num2) return 1;
            if (num1 < num2) return -1;
        }
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    const v1Parts = version1.split('.');
    const v2Parts = version2.split('.');
    const len = Math.max(v1Parts.length, v2Parts.length);
    
    for (let i = 0; i < len; i++) {
        const num1 = i < v1Parts.length ? parseInt(v1Parts[i], 10) : 0;
        const num2 = i < v2Parts.length ? parseInt(v2Parts[i], 10) : 0;
        if (num1 > num2) return 1;
        if (num1 < num2) return -1;
    }
    
    return 0;
};
```

## Typescript

```typescript
function compareVersion(version1: string, version2: string): number {
    const v1 = version1.split('.');
    const v2 = version2.split('.');
    const n = Math.max(v1.length, v2.length);
    for (let i = 0; i < n; i++) {
        const num1 = i < v1.length ? parseInt(v1[i], 10) : 0;
        const num2 = i < v2.length ? parseInt(v2[i], 10) : 0;
        if (num1 > num2) return 1;
        if (num1 < num2) return -1;
    }
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $version1
     * @param String $version2
     * @return Integer
     */
    function compareVersion($version1, $version2) {
        $v1 = explode('.', $version1);
        $v2 = explode('.', $version2);
        $len = max(count($v1), count($v2));
        for ($i = 0; $i < $len; $i++) {
            $num1 = $i < count($v1) ? (int)$v1[$i] : 0;
            $num2 = $i < count($v2) ? (int)$v2[$i] : 0;
            if ($num1 > $num2) return 1;
            if ($num1 < $num2) return -1;
        }
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func compareVersion(_ version1: String, _ version2: String) -> Int {
        let parts1 = version1.split(separator: ".")
        let parts2 = version2.split(separator: ".")
        let maxCount = max(parts1.count, parts2.count)
        for i in 0..<maxCount {
            let num1 = i < parts1.count ? Int(parts1[i])! : 0
            let num2 = i < parts2.count ? Int(parts2[i])! : 0
            if num1 < num2 { return -1 }
            if num1 > num2 { return 1 }
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun compareVersion(version1: String, version2: String): Int {
        val v1Parts = version1.split('.')
        val v2Parts = version2.split('.')
        val n = maxOf(v1Parts.size, v2Parts.size)
        for (i in 0 until n) {
            val num1 = if (i < v1Parts.size) v1Parts[i].toInt() else 0
            val num2 = if (i < v2Parts.size) v2Parts[i].toInt() else 0
            if (num1 != num2) return if (num1 > num2) 1 else -1
        }
        return 0
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int compareVersion(String version1, String version2) {
    List<String> v1 = version1.split('.');
    List<String> v2 = version2.split('.');

    int len = max(v1.length, v2.length);
    for (int i = 0; i < len; i++) {
      int num1 = i < v1.length ? int.parse(v1[i]) : 0;
      int num2 = i < v2.length ? int.parse(v2[i]) : 0;
      if (num1 > num2) return 1;
      if (num1 < num2) return -1;
    }
    return 0;
  }
}
```

## Golang

```go
package main

import (
	"strconv"
	"strings"
)

func compareVersion(version1 string, version2 string) int {
	v1 := strings.Split(version1, ".")
	v2 := strings.Split(version2, ".")

	n := len(v1)
	if len(v2) > n {
		n = len(v2)
	}

	for i := 0; i < n; i++ {
		var num1, num2 int
		if i < len(v1) {
			num1, _ = strconv.Atoi(v1[i])
		}
		if i < len(v2) {
			num2, _ = strconv.Atoi(v2[i])
		}
		if num1 > num2 {
			return 1
		}
		if num1 < num2 {
			return -1
		}
	}
	return 0
}
```

## Ruby

```ruby
def compare_version(version1, version2)
  v1 = version1.split('.')
  v2 = version2.split('.')
  max_len = [v1.length, v2.length].max
  (0...max_len).each do |i|
    num1 = i < v1.length ? v1[i].to_i : 0
    num2 = i < v2.length ? v2[i].to_i : 0
    return -1 if num1 < num2
    return 1 if num1 > num2
  end
  0
end
```

## Scala

```scala
object Solution {
    def compareVersion(version1: String, version2: String): Int = {
        val v1Parts = version1.split("\\.")
        val v2Parts = version2.split("\\.")
        val maxLen = math.max(v1Parts.length, v2Parts.length)
        var i = 0
        while (i < maxLen) {
            val num1 = if (i < v1Parts.length) v1Parts(i).toInt else 0
            val num2 = if (i < v2Parts.length) v2Parts(i).toInt else 0
            if (num1 < num2) return -1
            if (num1 > num2) return 1
            i += 1
        }
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let v1: Vec<i32> = version1.split('.').map(|s| s.parse::<i32>().unwrap()).collect();
        let v2: Vec<i32> = version2.split('.').map(|s| s.parse::<i32>().unwrap()).collect();

        let n = std::cmp::max(v1.len(), v2.len());
        for i in 0..n {
            let a = if i < v1.len() { v1[i] } else { 0 };
            let b = if i < v2.len() { v2[i] } else { 0 };
            if a > b {
                return 1;
            }
            if a < b {
                return -1;
            }
        }
        0
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (compare-version version1 version2)
  (-> string? string? exact-integer?)
  (let* ([parts1 (map string->number (string-split version1 "."))]
         [parts2 (map string->number (string-split version2 "."))])
    (let loop ((i 0))
      (cond
        [(and (>= i (length parts1)) (>= i (length parts2))) 0]
        [else
         (define v1 (if (< i (length parts1)) (list-ref parts1 i) 0))
         (define v2 (if (< i (length parts2)) (list-ref parts2 i) 0))
         (cond [(< v1 v2) -1]
               [(> v1 v2) 1]
               [else (loop (+ i 1))])]))))
```

## Erlang

```erlang
-spec compare_version(Version1 :: unicode:unicode_binary(), Version2 :: unicode:unicode_binary()) -> integer().
compare_version(Version1, Version2) ->
    L1 = binary:split(Version1, <<".">>, [global]),
    L2 = binary:split(Version2, <<".">>, [global]),
    compare_lists(L1, L2).

-spec compare_lists([binary()], [binary()]) -> integer().
compare_lists([], []) ->
    0;
compare_lists([], Rest2) ->
    case any_nonzero(Rest2) of
        true -> -1;
        false -> 0
    end;
compare_lists(Rest1, []) ->
    case any_nonzero(Rest1) of
        true -> 1;
        false -> 0
    end;
compare_lists([H1|T1], [H2|T2]) ->
    N1 = to_int(H1),
    N2 = to_int(H2),
    if
        N1 > N2 -> 1;
        N1 < N2 -> -1;
        true -> compare_lists(T1, T2)
    end.

-spec any_nonzero([binary()]) -> boolean().
any_nonzero(List) ->
    lists:any(fun(Bin) -> to_int(Bin) =/= 0 end, List).

-spec to_int(binary()) -> integer().
to_int(Bin) ->
    list_to_integer(binary_to_list(Bin)).
```

## Elixir

```elixir
defmodule Solution do
  @spec compare_version(version1 :: String.t(), version2 :: String.t()) :: integer()
  def compare_version(version1, version2) do
    v1 = String.split(version1, ".") |> Enum.map(&String.to_integer/1)
    v2 = String.split(version2, ".") |> Enum.map(&String.to_integer/1)

    max_len = max(length(v1), length(v2))

    Enum.reduce_while(0..(max_len - 1), 0, fn i, _acc ->
      n1 = Enum.at(v1, i, 0)
      n2 = Enum.at(v2, i, 0)

      cond do
        n1 < n2 -> {:halt, -1}
        n1 > n2 -> {:halt, 1}
        true -> {:cont, 0}
      end
    end)
  end
end
```
